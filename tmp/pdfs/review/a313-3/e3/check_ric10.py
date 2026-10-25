"""Structural checker for the PARTIAL рис.10 transcription (board Y1).

Run from any directory: python check_ric10.py
Checks schemas, BOM/net ref parity, unique (ref,pin), and Cyrillic placeholder spelling.
It does not validate the electrical interpretation or claim diagram completeness.
Modeled directly on check_ric14.py (same logic, pointed at ric10_* filenames).
"""
import csv
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parent
BOM_HEADER = ["ref", "name", "qty", "page", "note"]
NET_HEADER = ["ref", "pin", "net", "note"]
CONN_HEADER = ["table", "pin", "signal", "photo", "note"]
UNTRACED_PREFIX = "НЕ ПРОСЛЕЖЕНО "


def read_csv(path, expected):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != expected:
            raise AssertionError(f"{path.name}: header {reader.fieldnames!r} != {expected!r}")
        rows = list(reader)
    if not rows:
        raise AssertionError(f"{path.name}: empty data")
    return rows


def check():
    bom = read_csv(D / "ric10_bom.csv", BOM_HEADER)
    net = read_csv(D / "ric10_net.csv", NET_HEADER)
    conn = read_csv(D / "ric10_conn.csv", CONN_HEADER)

    bom_refs = [r["ref"] for r in bom]
    if any(not x for x in bom_refs):
        raise AssertionError("BOM has empty ref")
    if len(bom_refs) != len(set(bom_refs)):
        dups = [r for r, c in Counter(bom_refs).items() if c > 1]
        raise AssertionError(f"duplicate BOM ref: {dups}")
    if any(not r["name"].strip() or not r["note"].strip() for r in bom):
        raise AssertionError("BOM has empty name/note")
    if any(not r["page"].strip() for r in bom):
        raise AssertionError("BOM has empty page")

    seen = set()
    net_refs = set()
    untraced = 0
    real = 0
    for r in net:
        ref, pin, name = r["ref"], r["pin"], r["net"]
        if not ref or not pin or not name or not r["note"].strip():
            raise AssertionError(f"incomplete net row: {r}")
        key = (ref, pin)
        if key in seen:
            raise AssertionError(f"duplicate ref/pin: {key}")
        seen.add(key)
        net_refs.add(ref)
        if name.startswith(UNTRACED_PREFIX):
            expected = UNTRACED_PREFIX + ref + "." + pin
            if name != expected:
                raise AssertionError(f"placeholder must be exact {expected!r}, got {name!r}")
            untraced += 1
        else:
            real += 1
    missing = set(bom_refs) - net_refs
    extra = net_refs - set(bom_refs)
    if missing or extra:
        raise AssertionError(f"BOM/net ref mismatch: missing={sorted(missing)}, extra={sorted(extra)}")

    # conn.csv structural checks (no placeholder convention required, just completeness of fields)
    if any(not r["table"].strip() or not r["pin"].strip() or not r["note"].strip() for r in conn):
        raise AssertionError("conn.csv has empty table/pin/note")
    conn_tables = sorted(set(r["table"] for r in conn))

    print(f"PASS structure: BOM refs={len(bom_refs)}, net rows={len(net)}, "
          f"directly traced rows={real}, placeholder rows={untraced}, conn rows={len(conn)}")
    print(f"PASS conn tables found: {conn_tables}")
    print("PASS ref parity, unique pin keys, CSV headers, exact Cyrillic placeholder format")
    print("LIMIT: structural checks only; no electrical/topology completeness claim")
    return True


if __name__ == "__main__":
    check()
