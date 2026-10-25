"""Shared structural checker for one generated SchDoc dataset."""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def check(stem: str) -> int:
    root = Path(__file__).resolve().parent
    bom = read_csv(root / f"{stem}_bom.csv")
    nets = read_csv(root / f"{stem}_net.csv")
    conns = read_csv(root / f"{stem}_conn.csv")
    errors: list[str] = []

    refs = [row["ref"] for row in bom]
    ref_set = set(refs)
    if len(refs) != len(ref_set):
        errors.append(f"BOM trùng ref: {[r for r, n in Counter(refs).items() if n > 1]}")
    if any(row["qty"] != "1" for row in bom):
        errors.append("BOM phải có đúng một dòng qty=1 cho mỗi ref")

    pin_keys = [(row["ref"], row["pin"]) for row in nets]
    if len(pin_keys) != len(set(pin_keys)):
        errors.append("Một ref.pin xuất hiện trên nhiều dòng net")
    missing = sorted({row["ref"] for row in nets} - ref_set)
    if missing:
        errors.append(f"Pin thuộc ref không có trong BOM: {missing[:20]}")

    by_net = Counter(row["net"] for row in nets)
    bad_singletons = [
        row for row in nets
        if by_net[row["net"]] == 1
        and "allowed_singleton:" not in row["note"]
    ]
    if bad_singletons:
        errors.append(f"Net một chân chưa khai báo: {bad_singletons[:5]}")

    conn_missing = sorted({row["table"] for row in conns} - ref_set)
    if conn_missing:
        errors.append(f"Đầu nối không có trong BOM: {conn_missing[:20]}")

    if errors:
        print(f"FAIL {stem}")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"PASS {stem}: refs={len(ref_set)}, net_rows={len(nets)}, "
        f"nets={len(by_net)}, conn_rows={len(conns)}, "
        f"singletons={sum(n == 1 for n in by_net.values())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(check(sys.argv[1]))
