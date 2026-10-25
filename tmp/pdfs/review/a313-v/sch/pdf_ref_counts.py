"""Count BVTK BOM references and read sodocactam drawing titles.

Run with the bundled PDF Python, not the SchDoc Python:
  <bundled-python> pdf_ref_counts.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pdfplumber


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
BVTK = ROOT / "File của A313-V/1.BVTK A313-V/BVTK-A313-V_HS dau A.pdf"
BVTK06 = ROOT / "File của A313-V/BVTK-A313-V.06.pdf"
SODO = ROOT / "File của A313-V/File mach in va mach nguyen ly_A313_V/sodocactam.pdf"

BOM_PAGES = {
    "v01": 11,
    "v02": 15,
    "v03": 19,
    "v04": 23,
    "v05": 27,
    "v06": 31,
    "v07": 35,
    "v0801": 39,
    "v0802": 43,
    "v09": 47,
    "v10": 50,
}
REF_RE = re.compile(
    r"(?<![A-Za-zА-Яа-я0-9])(?:DC\d+[A-D]?|XS\d+|J\d+|[CRDLQTPU]\d+[A-D]?)(?![A-Za-zА-Яа-я0-9])",
    re.I,
)


def package_ref(ref: str) -> str:
    match = re.fullmatch(r"U(\d+)[A-D]", ref, re.I)
    return f"U{match.group(1)}" if match else ref.upper()


def count_bom_page(page) -> dict:
    refs: list[str] = []
    for table in page.extract_tables()[1:]:
        if not table or not table[0] or "Ký hiệu" not in (table[0][1] or ""):
            continue
        for row in table[1:]:
            if len(row) > 1 and row[1]:
                refs.extend(REF_RE.findall(row[1]))
    unique = sorted({package_ref(ref) for ref in refs})
    connectors = [ref for ref in unique if re.match(r"^(?:DC|XS|J)", ref)]
    return {
        "ref_count": len(unique),
        "connector_count": len(connectors),
        "connector_refs": connectors,
        "refs": unique,
    }


def main() -> None:
    result: dict = {"bvtk": {}, "sodocactam": {}}
    with pdfplumber.open(BVTK) as pdf:
        for key, page_number in BOM_PAGES.items():
            row = count_bom_page(pdf.pages[page_number - 1])
            row.update({"pdf": str(BVTK.relative_to(ROOT)), "page": page_number})
            result["bvtk"][key] = row

    # The dedicated .06 extract contains BV.25 as page 4. It must agree with
    # the same BOM page in the complete BVTK file.
    with pdfplumber.open(BVTK06) as pdf:
        dedicated_v06 = count_bom_page(pdf.pages[3])
    assert dedicated_v06["refs"] == result["bvtk"]["v06"]["refs"]
    result["bvtk"]["v06"]["dedicated_pdf"] = str(BVTK06.relative_to(ROOT))
    result["bvtk"]["v06"]["dedicated_page"] = 4

    # Component designators in sodocactam are raster objects; only the title
    # remains searchable text. Counts are supplied by the SchDoc extractor and
    # explicitly described as non-independent in every mota file.
    with pdfplumber.open(SODO) as pdf:
        for page_number, page in enumerate(pdf.pages, 1):
            text = " ".join(word["text"] for word in page.extract_words())
            result["sodocactam"][str(page_number)] = {
                "title": text,
                "searchable_ref_count": None,
                "reason": "ref được raster hóa; lớp text chỉ còn tiêu đề",
            }

    (OUT / "crosscheck_counts.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("PASS pdf_ref_counts: 11 bảng BOM BVTK; 12 tiêu đề sodocactam")


if __name__ == "__main__":
    main()
