"""Structural checker for the PARTIAL рис.14 transcription.

Run from any directory: python check_ric14.py
Checks schemas, BOM/net ref parity, unique (ref,pin), and Cyrillic placeholder spelling.
It does not validate the electrical interpretation or claim diagram completeness.
"""
import csv
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parent
BOM_HEADER = ["ref", "name", "qty", "page", "note"]
NET_HEADER = ["ref", "pin", "net", "note"]
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
    bom = read_csv(D / "ric14_bom.csv", BOM_HEADER)
    net = read_csv(D / "ric14_net.csv", NET_HEADER)
    bom_refs = [r["ref"] for r in bom]
    if any(not x for x in bom_refs):
        raise AssertionError("BOM has empty ref")
    if len(bom_refs) != len(set(bom_refs)):
        raise AssertionError("duplicate BOM ref")
    if any(not r["name"].strip() or not r["note"].strip() for r in bom):
        raise AssertionError("BOM has empty name/note")

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
    print(f"PASS structure: BOM refs={len(bom_refs)}, net rows={len(net)}, directly traced rows={real}, placeholder rows={untraced}")
    print("PASS ref parity, unique pin keys, CSV headers, exact Cyrillic placeholder format")
    print("LIMIT: structural checks only; no electrical/topology completeness claim")
    return True


if __name__ == "__main__":
    check()
