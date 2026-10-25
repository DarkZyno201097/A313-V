"""Structural checker for the PARTIAL рис.16 (Y8, «Преобразователь») transcription.

Run from any directory: python check_ric16.py
Checks schemas, BOM/net ref parity, unique (ref,pin), exact Cyrillic placeholder spelling,
and the conn.csv (П1 pin-strip table) schema.
It does not validate the electrical interpretation or claim diagram completeness —
see ric16_mota.md for what is PARTIAL and why.
"""
import csv
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
    bom = read_csv(D / "ric16_bom.csv", BOM_HEADER)
    net = read_csv(D / "ric16_net.csv", NET_HEADER)
    conn = read_csv(D / "ric16_conn.csv", CONN_HEADER)

    bom_refs = [r["ref"] for r in bom]
    if any(not x for x in bom_refs):
        raise AssertionError("BOM has empty ref")
    if len(bom_refs) != len(set(bom_refs)):
        dup = sorted({r for r in bom_refs if bom_refs.count(r) > 1})
        raise AssertionError(f"duplicate BOM ref: {dup}")
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

    for r in conn:
        if not r["table"] or not r["pin"] or not r["signal"]:
            raise AssertionError(f"incomplete conn row: {r}")
    tables = sorted({r["table"] for r in conn})

    print(
        f"PASS structure: BOM refs={len(bom_refs)}, net rows={len(net)}, "
        f"directly traced rows={real}, placeholder rows={untraced}, "
        f"conn rows={len(conn)} (bảng: {tables})"
    )
    print("PASS ref parity, unique (ref,pin) keys, CSV headers, exact Cyrillic placeholder format")
    print("LIMIT: structural checks only; no electrical/topology completeness claim — see ric16_mota.md")
    return True


if __name__ == "__main__":
    check()
