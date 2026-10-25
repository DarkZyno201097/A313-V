"""Extract conservative BOM/net/connector datasets from the requested SchDocs.

Run with C:/Python314/python.exe. The only third-party dependency is the
vendored olefile package in this output directory.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import json
import re
import struct
import sys
from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
SOURCE_ROOT = ROOT / "File của A313-V/File mach in va mach nguyen ly_A313_V"
sys.path.insert(0, str(OUT / "_vendor"))
import olefile  # noqa: E402


@dataclass(frozen=True)
class Drawing:
    stem: str
    code: str
    page: int
    source: str
    function: str
    bvtk_key: str | None
    variant: str = "chính"


DRAWINGS = [
    Drawing("v01", "V.01", 1, "TAM1_Xulytrungtam/PAGE1.SchDoc", "cụm điều khiển và xử lý trung tâm", "v01"),
    Drawing("v02", "V.02", 2, "TAM2_chuyenmachtinhieuvao/A313-2.SchDoc", "cụm chuyển mạch tín hiệu vào", "v02"),
    Drawing("v03", "V.03", 3, "Tam3_Cum_tich_phan/A313_3.SchDoc", "cụm tích phân", "v03"),
    Drawing("v04", "V.04", 4, "TAM4_Cumbiendoi/A313_4.SchDoc", "cụm biến đổi", "v04"),
    Drawing("v05", "V.05", 5, "Tam5_Chuyenmachtinhieura/A313_5.SchDoc", "cụm chuyển mạch tín hiệu ra", "v05"),
    Drawing("v06", "V.06", 6, "Tam6_khuyechdaitinhieura/A313_6.SchDoc", "cụm khuếch đại tín hiệu ra", "v06"),
    Drawing("v07", "V.07", 7, "machbiendoilenhdon/machbiendoilenhdon.SchDoc", "cụm chuyển lệnh đơn ra", "v07", "bản có J1/J2 và 11 đầu CON1"),
    Drawing("v07_sheet1", "V.07", 7, "machbiendoilenhdon/Sheet1.SchDoc", "cụm chuyển lệnh đơn ra", "v07", "bản Sheet1 có DC13C/DC13D"),
    Drawing("v0801", "V.08.01", 8, "machnguon_A313V/NGUON_A313.SchDoc", "tấm nguồn điện", "v0801"),
    Drawing("v0802", "V.08.02", 9, "machkiemtranguon/mach_kiem_tra_nguon.SchDoc", "tấm kiểm tra nguồn điện", "v0802"),
    Drawing("v0802_ngoc", "V.08.02", 9, "machkiemtranguon/ngoc.SchDoc", "tấm kiểm tra nguồn điện", "v0802", "bản ngoc chưa đánh số ref"),
    Drawing("v10", "V.10 (không có trong sodocactam; nhãn nhầm V.09)", 10, "tamcaclinhkienroirac/A313_10.SchDoc", "nguồn SchDoc mang nội dung tấm linh kiện rời rạc V.10, không phải tấm trung gian V.09", "v09", "ánh xạ đang mâu thuẫn"),
    Drawing("daucam31", "DAUCAM-31", 12, "machdaucam31chan_A313V/DAUCAM.SchDoc", "đầu cắm 31 chân trên thân máy", None),
    Drawing("daucam96", "DAUCAM-96", 12, "machdaucam96chan_DC13/daucam96chan.SchDoc", "đầu cắm 96 chân trên thân máy", None),
]

# sodocactam stores ref glyphs as raster images, so these counts are tied to
# the matching SchDoc version after visual/layout identification, not a second
# text extraction. Page 7 visibly matches Sheet1; page 10 visibly has DC1..DC12.
SODO_COUNTS = {
    "v01": 145, "v02": 267, "v03": 198, "v04": 244,
    "v05": 173, "v06": 234, "v07": 109, "v07_sheet1": 109,
    "v0801": 51, "v0802": 89, "v0802_ngoc": 89, "v10": 12,
    "daucam31": 2, "daucam96": 103,
}


def records(path: Path) -> list[dict[str, str]]:
    with olefile.OleFileIO(str(path)) as compound:
        data = compound.openstream("FileHeader").read()
    offset, result = 0, []
    while offset < len(data):
        if offset + 4 > len(data):
            raise ValueError(f"bản ghi cụt tại byte {offset}")
        length, = struct.unpack("<I", data[offset:offset + 4])
        body_length = length & 0xFFFFFF
        body = data[offset + 4:offset + 4 + body_length]
        offset += 4 + body_length
        record: dict[str, str] = {}
        for part in body.rstrip(b"\x00").decode("latin1").split("|"):
            if "=" in part:
                key, value = part.split("=", 1)
                record[key.upper()] = value
        for key in [key for key in record if key.startswith("%UTF8%")]:
            record[key[6:]] = record.pop(key).encode("latin1").decode("utf-8", "replace")
        result.append(record)
    return result[1:]


def coordinate(record: dict[str, str], prefix: str = "LOCATION.") -> tuple[float, float]:
    def value(axis: str) -> float:
        return int(record.get(prefix + axis, 0)) + int(record.get(prefix + axis + "_FRAC", 0)) / 100000
    return value("X"), value("Y")


def pin_hotspot(record: dict[str, str]) -> tuple[float, float]:
    x, y = coordinate(record)
    length = int(record.get("PINLENGTH", 0)) + int(record.get("PINLENGTH_FRAC", 0)) / 100000
    dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][int(record.get("PINCONGLOMERATE", 0)) & 3]
    return x + dx * length, y + dy * length


def on_segment(point, start, end) -> bool:
    if (start[0] - point[0]) * (end[1] - point[1]) != (end[0] - point[0]) * (start[1] - point[1]):
        return False
    return min(start[0], end[0]) <= point[0] <= max(start[0], end[0]) and min(start[1], end[1]) <= point[1] <= max(start[1], end[1])


def decode_label(raw: str) -> str:
    """Decode the faux-Cyrillic drawing font without translating Latin capitals."""
    if raw in ("M", "M_"):
        return "М" + raw[1:]
    if re.fullmatch(r"vih\.\d+[ab]==?", raw, re.I):
        match = re.fullmatch(r"vih\.(\d+)([ab])(==?)", raw, re.I)
        suffix = "А" if match.group(2).lower() == "a" else "Б"
        return f"ВЫХ.{match.group(1)}{suffix}{match.group(3)}"
    replacements = {
        "ixpravn": "ИСПРАВН", "upr": "УПР", "vhod": "ВХОД", "bhod": "ВХОД",
        "vih": "ВЫХ", "rc": "РК", "xvc": "СВК", "aji": "АЦИ",
    }
    result = raw
    for source, target in replacements.items():
        result = re.sub(source, target, result, flags=re.I)
    return result


def component_name(component: dict[str, str]) -> str:
    comment = component.get("comment", "").strip()
    libref = component.get("libref", "").strip()
    if comment and comment.casefold() != libref.casefold():
        return f"{comment} [{libref}]"
    return comment or libref or "?"


def is_connector(component: dict[str, str]) -> bool:
    text = " ".join((component.get("libref", ""), component.get("comment", ""))).casefold()
    return any(token in text for token in ("con", "header", "giac", "dc96"))


def parse(path: Path) -> dict:
    source_records = records(path)
    components: dict[int, dict[str, str]] = {}
    for index, record in enumerate(source_records):
        if record.get("RECORD") == "1":
            components[index] = {
                "record_index": str(index),
                "libref": record.get("LIBREFERENCE", ""),
                "part": record.get("CURRENTPARTID", "1"),
                "mode": record.get("DISPLAYMODE", "0"),
                "ref": "",
                "comment": "",
                "footprint": "",
                "partcount": record.get("PARTCOUNT", ""),
            }
    for record in source_records:
        owner = int(record.get("OWNERINDEX", -1))
        if owner not in components:
            continue
        if record.get("RECORD") == "34":
            components[owner]["ref"] = record.get("TEXT", "")
        elif record.get("RECORD") == "41" and record.get("NAME", "").casefold() == "comment":
            components[owner]["comment"] = record.get("TEXT", "")
        elif record.get("RECORD") == "45" and record.get("ISCURRENT") == "T":
            components[owner]["footprint"] = record.get("MODELNAME", "")

    real = {
        index: component for index, component in components.items()
        if component["ref"] and component["ref"] != "*" and not component["libref"].casefold().startswith("titleblock")
    }
    literal_counts = collections.Counter(component["ref"] for component in real.values())
    for component in real.values():
        ref = component["ref"]
        if "?" in ref and literal_counts[ref] > 1:
            component["effective_ref"] = f"{ref}@record{component['record_index']}"
        else:
            component["effective_ref"] = ref

    segments: list[tuple[tuple[float, float], tuple[float, float]]] = []
    pins: list[dict] = []
    tags: list[dict] = []
    dots: list[tuple[float, float]] = []
    unsupported = collections.Counter()
    for record in source_records:
        record_type = record.get("RECORD")
        if record_type == "27":
            points = [
                (
                    int(record[f"X{number}"]) + int(record.get(f"X{number}_FRAC", 0)) / 100000,
                    int(record[f"Y{number}"]) + int(record.get(f"Y{number}_FRAC", 0)) / 100000,
                )
                for number in range(1, int(record["LOCATIONCOUNT"]) + 1)
            ]
            segments.extend(zip(points, points[1:]))
        elif record_type == "2":
            owner = int(record.get("OWNERINDEX", -1))
            component = real.get(owner)
            if component is None:
                continue
            if record.get("OWNERPARTID", component["part"]) not in (component["part"], "-1"):
                continue
            if record.get("OWNERPARTDISPLAYMODE", "0") != component["mode"]:
                continue
            pins.append({
                "point": pin_hotspot(record),
                "ref": component["effective_ref"],
                "pin": record.get("DESIGNATOR", "?"),
                "pin_name": record.get("NAME", ""),
            })
        elif record_type in ("25", "17"):
            raw = record.get("TEXT", "").strip()
            if raw:
                tags.append({"point": coordinate(record), "raw": raw, "kind": "label" if record_type == "25" else "power"})
        elif record_type == "29":
            dots.append(coordinate(record))
        elif record_type in ("26", "37"):
            unsupported[record_type] += 1

    segment_count, pin_count = len(segments), len(pins)
    parent = list(range(segment_count + pin_count + len(tags)))

    def root(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def join(left: int, right: int) -> None:
        parent[root(right)] = root(left)

    endpoints: dict[tuple[float, float], list[int]] = collections.defaultdict(list)
    for index, (start, end) in enumerate(segments):
        endpoints[start].append(index)
        endpoints[end].append(index)
    for members in endpoints.values():
        for member in members[1:]:
            join(members[0], member)

    for point in set(endpoints) | set(dots):
        passing = [index for index, (start, end) in enumerate(segments) if on_segment(point, start, end)]
        if point in endpoints:
            passing.extend(endpoints[point])
        if len(passing) > 1 and (point in endpoints or point in dots):
            for member in passing[1:]:
                join(passing[0], member)

    point_items: dict[tuple[float, float], list[int]] = collections.defaultdict(list)
    for index, pin in enumerate(pins):
        point_items[pin["point"]].append(segment_count + index)
    for index, tag in enumerate(tags):
        point_items[tag["point"]].append(segment_count + pin_count + index)
    for point, members in point_items.items():
        for member in members[1:]:
            join(members[0], member)
        for segment_index, (start, end) in enumerate(segments):
            if on_segment(point, start, end):
                join(segment_index, members[0])

    same_labels: dict[str, list[int]] = collections.defaultdict(list)
    for index, tag in enumerate(tags):
        same_labels[tag["raw"].casefold()].append(segment_count + pin_count + index)
    for members in same_labels.values():
        for member in members[1:]:
            join(members[0], member)

    # Altium repeats a package's physical supply pins on several multipart
    # symbols. The repeated ref.pin is one electrical terminal, so its roots
    # must be unified before rows are emitted.
    same_pins: dict[tuple[str, str], list[int]] = collections.defaultdict(list)
    for index, pin in enumerate(pins):
        same_pins[(pin["ref"], pin["pin"])].append(segment_count + index)
    for members in same_pins.values():
        for member in members[1:]:
            join(members[0], member)

    nets: dict[int, dict] = collections.defaultdict(lambda: {"pins": [], "tags": []})
    for index, pin in enumerate(pins):
        nets[root(segment_count + index)]["pins"].append(pin)
    for index, tag in enumerate(tags):
        nets[root(segment_count + pin_count + index)]["tags"].append(tag)
    nets = {key: value for key, value in nets.items() if value["pins"]}

    pin_owners: dict[tuple[str, str], list[int]] = collections.defaultdict(list)
    for net_id, net in nets.items():
        for pin in net["pins"]:
            pin_owners[(pin["ref"], pin["pin"])].append(net_id)
    duplicate_pins = {key: value for key, value in pin_owners.items() if len(set(value)) > 1}
    if duplicate_pins:
        raise ValueError(f"ref.pin thuộc nhiều net: {list(duplicate_pins)[:10]}")

    return {
        "records": source_records,
        "components": real,
        "nets": nets,
        "unsupported": dict(unsupported),
        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "literal_ref_count": len(set(component["ref"] for component in real.values())),
    }


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def natural_key(value: str):
    return [int(part) if part.isdigit() else part.casefold() for part in re.split(r"(\d+)", value)]


def build_drawing(drawing: Drawing, pdf_counts: dict) -> dict:
    path = SOURCE_ROOT / drawing.source
    parsed = parse(path)
    components = parsed["components"]

    by_ref: dict[str, list[dict[str, str]]] = collections.defaultdict(list)
    for component in components.values():
        by_ref[component["effective_ref"]].append(component)
    bom_rows = []
    for ref in sorted(by_ref, key=natural_key):
        group = by_ref[ref]
        names = sorted({component_name(component) for component in group})
        note_parts = [f"nguồn SchDoc={drawing.source}", f"sheet={Path(drawing.source).name}"]
        if len(names) > 1:
            note_parts.append("? nhiều name/libref: " + " | ".join(names))
        if "?" in ref:
            note_parts.append("? ref chưa được đánh số trong SchDoc")
        bom_rows.append({
            "ref": ref,
            "name": " | ".join(names),
            "qty": "1",
            "page": str(drawing.page),
            "note": "; ".join(note_parts),
        })

    ordered_nets = sorted(
        parsed["nets"].values(),
        key=lambda net: (
            sorted(tag["raw"].casefold() for tag in net["tags"]) or ["~"],
            sorted((pin["ref"], natural_key(pin["pin"])) for pin in net["pins"]),
        ),
    )
    net_rows: list[dict] = []
    pin_to_signal: dict[tuple[str, str], tuple[str, str]] = {}
    net_meta: list[dict] = []
    unnamed_index = 1
    for net in ordered_nets:
        raw_labels = sorted({tag["raw"] for tag in net["tags"]}, key=lambda s: (s.casefold(), s))
        labels = sorted({decode_label(label) for label in raw_labels}, key=lambda s: (s.casefold(), s))
        if labels:
            net_name = "/".join(labels)
        else:
            net_name = f"N{unnamed_index:04d}"
            unnamed_index += 1
        unique_pins = {(pin["ref"], pin["pin"]): pin for pin in net["pins"]}
        pins_here = sorted(unique_pins.values(), key=lambda pin: (natural_key(pin["ref"]), natural_key(pin["pin"])))
        singleton = len(pins_here) == 1
        external = bool(raw_labels)
        net_note_parts = []
        if raw_labels and labels != raw_labels:
            net_note_parts.append("nhãn gốc=" + "/".join(raw_labels))
        undecoded = [
            label for label in raw_labels
            if decode_label(label) == label and re.search(r"[a-z]", label)
        ]
        if undecoded:
            net_note_parts.append("? nhãn có mã font Latin chưa giải mã chắc chắn: " + "/".join(undecoded))
        if len(labels) > 1:
            net_note_parts.append("? nhiều nhãn trên cùng net: " + "/".join(labels))
        if singleton:
            if external:
                net_note_parts.append("allowed_singleton: cổng/nhãn ngoài chỉ có một chân linh kiện")
            else:
                net_note_parts.append("allowed_singleton: floating khai báo từ hình học SchDoc; cần kiểm nếu lẽ ra đi qua bus")
        note = "; ".join(net_note_parts)
        for pin in pins_here:
            row_note = note
            if pin["pin"] == "?":
                row_note = (row_note + "; " if row_note else "") + "? số chân thiếu trong SchDoc"
            row = {"ref": pin["ref"], "pin": pin["pin"], "net": net_name, "note": row_note}
            net_rows.append(row)
            pin_to_signal[(pin["ref"], pin["pin"])] = (net_name, row_note)
        net_meta.append({"name": net_name, "pins": len(pins_here), "labels": labels, "note": note})

    connector_refs = {
        component["effective_ref"] for component in components.values() if is_connector(component)
    }
    conn_rows = []
    for row in net_rows:
        if row["ref"] not in connector_refs:
            continue
        conn_rows.append({
            "table": row["ref"],
            "pin": row["pin"],
            "signal": row["net"],
            "sheet": drawing.source,
            "note": row["note"],
        })
    conn_rows.sort(key=lambda row: (natural_key(row["table"]), natural_key(row["pin"])))

    write_csv(OUT / f"{drawing.stem}_bom.csv", ["ref", "name", "qty", "page", "note"], bom_rows)
    write_csv(OUT / f"{drawing.stem}_net.csv", ["ref", "pin", "net", "note"], net_rows)
    write_csv(OUT / f"{drawing.stem}_conn.csv", ["table", "pin", "signal", "sheet", "note"], conn_rows)

    question_rows = sum("?" in " ".join(v for k, v in row.items() if k != "note") for row in bom_rows + net_rows + conn_rows)  # chỉ đếm ô dữ liệu, bỏ cột ghi chú
    singletons = sum(meta["pins"] == 1 for meta in net_meta)
    bvtk = pdf_counts["bvtk"].get(drawing.bvtk_key or "")
    sodo_count = SODO_COUNTS[drawing.stem]
    discrepancy: list[str] = []
    if sodo_count != len(bom_rows):
        discrepancy.append(f"sodocactam: {sodo_count} ref so với SchDoc {len(bom_rows)} ref")
    if bvtk and bvtk["ref_count"] != len(bom_rows):
        discrepancy.append(f"BVTK: {bvtk['ref_count']} ref so với SchDoc {len(bom_rows)} ref")
    if bvtk and bvtk["connector_count"] != len(connector_refs):
        discrepancy.append(f"BVTK: {bvtk['connector_count']} ref đầu nối so với SchDoc {len(connector_refs)}")

    special: list[str] = []
    if drawing.stem == "v07":
        special.append("Trang 7 sodocactam khớp bố cục bản Sheet1 (DC13C/DC13D), không khớp hoàn toàn bản này; giữ hai bộ output, không tự chọn bản chuẩn.")
    elif drawing.stem == "v07_sheet1":
        special.append("Bản Sheet1 khớp trang 7 sodocactam; vẫn còn lệch BVTK một ref (BVTK có 17 diode, SchDoc có 16).")
    elif drawing.stem == "v0802_ngoc":
        special.append(f"SchDoc có 89 instance nhưng chỉ {parsed['literal_ref_count']} ref literal vì phần lớn là R?/D?/U?/T?/C?; hậu tố @record chỉ để phân biệt dòng, không phải ref gốc.")
    elif drawing.stem == "v10":
        bvtk10 = pdf_counts["bvtk"]["v10"]
        special.append("Mâu thuẫn định danh: sodocactam tr.10 và BVTK BV.38/BV.41 là V.09 với 12 đầu DC; file được giao A313_10.SchDoc là tấm linh kiện rời rạc V.10.")
        special.append(f"So với BVTK V.10/BV.44: {bvtk10['ref_count']} ref linh kiện; SchDoc có thêm DC15 nên thành {len(bom_rows)} ref.")
    elif drawing.stem == "v0801":
        special.append("BVTK BV.33 không kê hai đầu nối DC13A/DC14C; SchDoc có hai ref này nên tổng cao hơn 2.")
    elif drawing.stem == "v0802":
        special.append("BVTK dùng ref đầu nối J1; SchDoc dùng DC14D. Số lượng cùng là 1 nhưng tên ref khác.")
    elif drawing.stem.startswith("daucam"):
        special.append("Không có bảng BOM tách riêng tương ứng trong BVTK được chỉ định; trang 12 sodocactam là bản gộp đầu cắm 31/96 chân.")

    title = pdf_counts["sodocactam"][str(drawing.page)]["title"]
    mota = [
        f"# {drawing.stem} — {drawing.code}",
        "",
        "## Chức năng và nguồn",
        "",
        f"- Chức năng theo tên bản vẽ: {drawing.function}.",
        f"- SchDoc: `{drawing.source}` ({drawing.variant}).",
        f"- SHA-256 SchDoc: `{parsed['source_sha256']}`.",
        f"- `sodocactam.pdf` trang {drawing.page}: `{title}`.",
        "",
        "## Thống kê trích xuất",
        "",
        f"- Ref BOM: {len(bom_rows)}; net: {len(net_meta)}; chân: {len(net_rows)}; dòng đầu nối: {len(conn_rows)}.",
        f"- Net một chân đã khai báo ngoại lệ: {singletons}; dòng có dấu `?`: {question_rows}.",
        f"- Bản ghi bus/harness không hỗ trợ: {sum(parsed['unsupported'].values())} ({parsed['unsupported'] or 'không có'}).",
        "",
        "## Kiểm chéo bắt buộc",
        "",
        f"- sodocactam trang {drawing.page}: {sodo_count} ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.",
    ]
    if bvtk:
        source = bvtk.get("dedicated_pdf", bvtk["pdf"])
        page = bvtk.get("dedicated_page", bvtk["page"])
        mota.append(f"- BVTK `{source}` trang {page}: {bvtk['ref_count']} ref, {bvtk['connector_count']} ref đầu nối ({', '.join(bvtk['connector_refs']) or 'không kê'}).")
    else:
        mota.append("- BVTK: không có bảng BOM tách riêng cho bản đầu cắm trong nguồn được chỉ định.")
    mota.extend([
        f"- Kết quả lệch: {'; '.join(discrepancy) if discrepancy else 'không lệch về tổng ref/đầu nối trong phạm vi đếm'}.",
        "",
        "## Điểm mơ hồ và giới hạn",
        "",
    ])
    mota.extend(f"- {item}" for item in special)
    if not special:
        mota.append("- Không có xung đột phiên bản riêng ngoài các chênh lệch đếm nêu trên.")
    multi_label_count = sum(len(meta["labels"]) > 1 for meta in net_meta)
    mota.extend([
        f"- Có {multi_label_count} net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.",
        "- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.",
        "- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.",
        "- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.",
        "",
        "## Tái kiểm",
        "",
        f"- Chạy `C:/Python314/python.exe check_{drawing.stem}.py`.",
        "- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.",
        "",
    ])
    (OUT / f"{drawing.stem}_mota.md").write_text("\n".join(mota), encoding="utf-8")

    wrapper = (
        "from check_common import check\n\n"
        f"if __name__ == '__main__':\n    raise SystemExit(check('{drawing.stem}'))\n"
    )
    (OUT / f"check_{drawing.stem}.py").write_text(wrapper, encoding="utf-8")
    return {
        "stem": drawing.stem,
        "code": drawing.code,
        "refs": len(bom_rows),
        "nets": len(net_meta),
        "pins": len(net_rows),
        "connectors": len(connector_refs),
        "conn_rows": len(conn_rows),
        "question_rows": question_rows,
        "singletons": singletons,
        "sha256": parsed["source_sha256"],
        "source": drawing.source,
    }


def selftest() -> None:
    assert on_segment((1, 0), (0, 0), (2, 0))
    assert not on_segment((1, 1), (0, 0), (2, 0))
    assert pin_hotspot({"LOCATION.X": "10", "LOCATION.Y": "5", "PINLENGTH": "3", "PINCONGLOMERATE": "2"}) == (7, 5)
    assert decode_label("vih.1a=") == "ВЫХ.1А="


def main() -> None:
    selftest()
    pdf_counts = json.loads((OUT / "crosscheck_counts.json").read_text(encoding="utf-8"))
    summary = [build_drawing(drawing, pdf_counts) for drawing in DRAWINGS]
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PASS extract_schdoc_netlists")
    for row in summary:
        print(f"{row['stem']:13s} refs={row['refs']:3d} nets={row['nets']:4d} pins={row['pins']:4d} ?={row['question_rows']:4d}")


if __name__ == "__main__":
    main()
