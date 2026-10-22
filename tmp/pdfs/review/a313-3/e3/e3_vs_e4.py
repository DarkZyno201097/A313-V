"""Đối chiếu chân đầu nối Э3 рис.11 với Э4 У7П1/У7П2.

Chạy từ gốc repo:
    python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py
"""
import csv
import re
from pathlib import Path

D = Path(__file__).parent
E4 = D.parent / "e4" / "p152.csv"
LAT = str.maketrans("ABCEHKMOPTXYacekmoptxy3", "АВСЕНКМОРТХУасекмортху3")


def norm(text):
    """Chuẩn hoá Latin↔Cyrillic, viết tắt ВХ./ВЫХ. và dấu cách."""
    s = (text or "").translate(LAT).upper().replace("−", "-")
    s = re.sub(r'[\s.„“"«»]', "", s)
    return s.replace("ВЫХОД", "ВЫХ").replace("ВХОД", "ВХ")


def e3_pin(net):
    m = re.fullmatch(r"(П[12]):(\d+)\s+(.+)", net or "")
    return (m.group(1), int(m.group(2)), m.group(3)) if m else None


def main():
    assert norm("BЫХОД 25") == norm("ВЫХ.25")
    assert norm("BX.1") == norm("ВХОД 1")
    assert e3_pin("П1:27 -20В") == ("П1", 27, "-20В")

    e3 = {}
    for row in csv.DictReader(open(D / "ric11_net.csv", encoding="utf8")):
        parsed = e3_pin(row["net"])
        if not parsed:
            continue
        table, pin, signal = parsed
        key = (table, pin)
        old = e3.setdefault(key, signal)
        assert norm(old) == norm(signal), f"Э3: {table}/{pin} có hai tên: {old!r}, {signal!r}"

    e4 = {}
    for row in csv.DictReader(open(E4, encoding="utf8")):
        if row["table"] not in ("У7П1", "У7П2"):
            continue
        key = (row["table"][-2:], int(row["pin"]))
        assert key not in e4, f"Э4: trùng {key}"
        e4[key] = row["signal"]

    rows = []
    counts = {"MATCH": 0, "NAME_MISMATCH": 0, "ONLY_E3": 0, "ONLY_E4": 0}
    for key in sorted(set(e3) | set(e4), key=lambda x: (x[0], x[1])):
        a, b = e3.get(key, ""), e4.get(key, "")
        if not a:
            status = "ONLY_E4"
        elif not b:
            status = "ONLY_E3"
        elif norm(a) == norm(b):
            status = "MATCH"
        else:
            status = "NAME_MISMATCH"
        counts[status] += 1
        note = "Э3 không có nhánh chân linh kiện tới chân đầu nối này" if status == "ONLY_E4" else ""
        rows.append(dict(connector=key[0], pin=key[1], e3_signal=a, e4_signal=b, status=status, note=note))

    out = D / "ric11_vs_e4.csv"
    with open(out, "w", newline="", encoding="utf8") as f:
        w = csv.DictWriter(f, ["connector", "pin", "e3_signal", "e4_signal", "status", "note"])
        w.writeheader()
        w.writerows(rows)

    assert len(e3) == 105 and len(e4) == 106
    assert counts == {"MATCH": 105, "NAME_MISMATCH": 0, "ONLY_E3": 0, "ONLY_E4": 1}
    assert [(r["connector"], r["pin"], r["e4_signal"]) for r in rows if r["status"] == "ONLY_E4"] == [("П2", 1, "КОРПУС")]

    print(f"E3 connector pins {len(e3)} | E4 connector pins {len(e4)}")
    print("match {MATCH} | name mismatch {NAME_MISMATCH} | only E3 {ONLY_E3} | only E4 {ONLY_E4}".format(**counts))
    print("only E4: П2/1 КОРПУС — bảng đầu nối có chân này, Э3 không vẽ nhánh tới chân linh kiện")
    print(f"wrote {out.as_posix()}")


if __name__ == "__main__":
    main()

