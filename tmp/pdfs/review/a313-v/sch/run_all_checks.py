"""Run every generated checker and write the requested summary table."""
from __future__ import annotations

import json
from pathlib import Path

from check_common import check


ROOT = Path(__file__).resolve().parent


def main() -> int:
    rows = json.loads((ROOT / "summary.json").read_text(encoding="utf-8"))
    failed = False
    for row in rows:
        status = "PASS" if check(row["stem"]) == 0 else "FAIL"
        row["checker_status"] = status
        failed |= status == "FAIL"
        mota_path = ROOT / f"{row['stem']}_mota.md"
        text = mota_path.read_text(encoding="utf-8")
        marker = "- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK."
        replacement = f"- Kết quả checker hiện tại: **{status}**.\n{marker}"
        if "- Kết quả checker hiện tại:" in text:
            lines = [
                f"- Kết quả checker hiện tại: **{status}**." if line.startswith("- Kết quả checker hiện tại:") else line
                for line in text.splitlines()
            ]
            text = "\n".join(lines) + "\n"
        else:
            text = text.replace(marker, replacement)
        mota_path.write_text(text, encoding="utf-8")

    (ROOT / "summary.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    table = [
        "# Tổng hợp netlist SchDoc A313-V",
        "",
        "| Bản | Ref | Net | Chân | Đầu nối | Checker | Dòng có `?` |",
        "|---|---:|---:|---:|---:|---|---:|",
    ]
    for row in rows:
        table.append(
            f"| {row['stem']} | {row['refs']} | {row['nets']} | {row['pins']} | "
            f"{row['conn_rows']} | {row['checker_status']} | {row['question_rows']} |"
        )
    table.extend([
        "",
        "`PASS` chỉ là kiểm cấu trúc BOM–pin–net và danh sách singleton đã khai báo; xem từng `*_mota.md` để biết lệch BVTK/sodocactam và giới hạn topology.",
        "",
    ])
    (ROOT / "summary.md").write_text("\n".join(table), encoding="utf-8")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
