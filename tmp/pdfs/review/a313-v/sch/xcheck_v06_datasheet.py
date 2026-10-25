"""Đối chiếu chân lẻ loi của 140УД1Б (V.06) với bảng chân trong etiket (tmp/pdfs/review/140ud1B.txt).
Bảng: 1 -Ucc | 2,3,12 контрольный | 4 общий | 5 выход | 6 свободный | 7 +Ucc | 8,11 свободный | 9 вход инв. | 10 вход неинв.
Kỳ vọng: chân chắc chắn phải nối (1,4,5,7,9,10) không bao giờ lẻ loi; chân lẻ loi chỉ được thuộc {2,3,6,8,11,12}.
"""
import csv, collections, re
from pathlib import Path
SCH = Path(__file__).parent
MUST = {"1", "4", "5", "7", "9", "10"}
MAY_FLOAT = {"2", "3", "6", "8", "11", "12"}
bom = {r["ref"]: r["name"] for r in csv.DictReader(open(SCH / "v06_bom.csv", encoding="utf-8-sig"))}
net = list(csv.DictReader(open(SCH / "v06_net.csv", encoding="utf-8-sig")))
cnt = collections.Counter(r["net"] for r in net)
ops = {k for k, v in bom.items() if v.upper().startswith("140")}
bad = []
float_pins = collections.Counter()
for r in net:
    if r["ref"] in ops and cnt[r["net"]] == 1:
        float_pins[r["pin"]] += 1
        if r["pin"] in MUST:
            bad.append((r["ref"], r["pin"]))
        if r["pin"] not in MAY_FLOAT:
            bad.append((r["ref"], r["pin"], "ngoài tập cho phép"))
print("140УД1Б:", len(ops), "chip; chân lẻ loi theo số chân:", dict(sorted(float_pins.items(), key=lambda x: int(x[0]))))
print("PASS" if not bad else f"FAIL {bad}")
raise SystemExit(1 if bad else 0)
