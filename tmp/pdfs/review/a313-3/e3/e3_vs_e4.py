"""Đối chiếu chân đầu nối Э3 với Э4 cho рис.8/У5 và рис.11/У7.

Chạy từ gốc repo:
    python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 8 У5
    python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 11 У7
"""
import argparse
import csv
import re
from pathlib import Path

D = Path(__file__).parent
E4_FILES = {"У1": "p150.csv", "У2": "p150.csv", "У3": "p151.csv", "У4": "p151.csv",
            "У5": "p151.csv", "У6": "p152.csv", "У7": "p152.csv",
            "У10": "p148.csv"}
LAT = str.maketrans("ABCEHKMOPTXYacekmoptxy3", "АВСЕНКМОРТХУасекмортху3")


def norm(text):
    """Chuẩn hoá Latin↔Cyrillic, viết tắt ВХ./ВЫХ. và dấu cách."""
    s = (text or "").translate(LAT).upper().replace("−", "-")
    s = re.sub(r'[\s.„“"«»]', "", s)
    return s.replace("ВЫХОД", "ВЫХ").replace("ВХОД", "ВХ")


def e3_pins(net):
    """Một net có thể ghi nhiều đầu nối, phân cách bằng ' | '."""
    out = []
    for part in (net or "").split(" | "):
        m = re.fullmatch(r"(П[123]):(\d+)\s+(.+)", part)
        if m:
            out.append((m.group(1), int(m.group(2)), m.group(3)))
    return out


def e3_pin(net):
    pins = e3_pins(net)
    return pins[0] if len(pins) == 1 else None


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("figure", nargs="?", default="11")
    parser.add_argument("unit", nargs="?", default="У7")
    args = parser.parse_args(argv)
    assert args.figure.isdigit(), "figure phải là số"
    assert args.unit in E4_FILES, f"chưa biết file Э4 của {args.unit}"

    assert norm("BЫХОД 25") == norm("ВЫХ.25")
    assert norm("BX.1") == norm("ВХОД 1")
    assert e3_pin("П1:27 -20В") == ("П1", 27, "-20В")
    assert e3_pins("П1:28 М0 | П3:8 М0") == [
        ("П1", 28, "М0"), ("П3", 8, "М0")
    ]

    e3 = {}
    net_path = D / f"ric{int(args.figure):02d}_net.csv"
    for row in csv.DictReader(open(net_path, encoding="utf8")):
        for table, pin, signal in e3_pins(row["net"]):
            key = (table, pin)
            old = e3.setdefault(key, signal)
            assert norm(old) == norm(signal), (
                f"Э3: {table}/{pin} có hai tên: {old!r}, {signal!r}"
            )

    # Bảng đầu nối chép riêng từ chính tờ Э3 (nếu có), gộp như chân netlist.
    conn_path = D / f"ric{int(args.figure):02d}_conn.csv"
    if conn_path.exists():
        for row in csv.DictReader(open(conn_path, encoding="utf8")):
            if not row["signal"].strip():
                continue
            key = (row["table"], int(row["pin"]))
            old = e3.setdefault(key, row["signal"])
            assert norm(old) == norm(row["signal"]), f"Э3: {key} netlist {old!r} ≠ bảng {row['signal']!r}"

    e4_path = D.parent / "e4" / E4_FILES[args.unit]
    wanted = {f"{args.unit}П1", f"{args.unit}П2", f"{args.unit}П3"}
    e4 = {}
    for row in csv.DictReader(open(e4_path, encoding="utf8")):
        if row["table"] not in wanted or not row["signal"].strip():
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
            note = (
                "Э3 không có nhánh chân linh kiện tới chân đầu nối này"
                if int(args.figure) == 11 and args.unit == "У7"
                else "Э3 không có nhánh chân linh kiện đọc chắc tới chân này; không suy từ Э4"
            )
        elif not b:
            status = "ONLY_E3"
            note = "Tên có trên Э3; ô Э4 trống/không có — giữ nguyên hai nguồn"
        elif norm(a) == norm(b):
            status = "MATCH"
            note = ""
        else:
            status = "NAME_MISMATCH"
            note = "Tên đọc từ Э3 khác Э4; giữ nguyên hai cách đọc, xem ric%02d_mota.md" % int(args.figure)
        counts[status] += 1
        rows.append(dict(
            connector=key[0], pin=key[1], e3_signal=a, e4_signal=b,
            status=status, note=note
        ))

    out = D / f"ric{int(args.figure):02d}_vs_e4.csv"
    with open(out, "w", newline="", encoding="utf8") as f:
        w = csv.DictWriter(
            f, ["connector", "pin", "e3_signal", "e4_signal", "status", "note"]
        )
        w.writeheader()
        w.writerows(rows)

    assert len(rows) == len(set(e3) | set(e4))
    assert sum(counts.values()) == len(rows)
    assert all(k[0] in {"П1", "П2", "П3"} and k[1] > 0 for k in set(e3) | set(e4))
    if int(args.figure) == 11 and args.unit == "У7":
        assert len(e3) == 105 and len(e4) == 106
        assert counts == {
            "MATCH": 105, "NAME_MISMATCH": 0,
            "ONLY_E3": 0, "ONLY_E4": 1
        }
        assert [
            (r["connector"], r["pin"], r["e4_signal"])
            for r in rows if r["status"] == "ONLY_E4"
        ] == [("П2", 1, "КОРПУС")]
    else:
        assert e3 and e4, "không đọc được chân đầu nối để tự kiểm"

    print(f"E3 connector pins {len(e3)} | E4 connector pins {len(e4)}")
    print(
        "match {MATCH} | name mismatch {NAME_MISMATCH} | "
        "only E3 {ONLY_E3} | only E4 {ONLY_E4}".format(**counts)
    )
    if int(args.figure) == 11 and args.unit == "У7":
        print("only E4: П2/1 КОРПУС — bảng đầu nối có chân này, Э3 không vẽ nhánh tới chân linh kiện")
    print(f"wrote {out.as_posix()}")


if __name__ == "__main__":
    main()
