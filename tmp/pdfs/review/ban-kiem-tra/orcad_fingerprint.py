"""So khớp vân tay loại IC giữa bộ chép tay A-313-3 (ric*_bom.csv) và netlist rút từ OrCAD MNL (orcad/*_bom.csv).
Ánh xạ họ Nga -> mã 74xx (chỉ các loại gặp trong dữ liệu; loại lạ đếm là 'other').
KHÔNG phải kiểm chứng topology — chỉ cho biết cặp (ric, OrCAD) nào có thể là cùng một tấm.
"""
import csv, re, collections, glob
from pathlib import Path
D = Path(__file__).parent
E3 = D.parent / "a313-3" / "e3"
MAP = {"ЛА3": "7400", "ЛА1": "7420", "ЛА4": "7410", "ЛА2": "7430", "ЛА6": "7440", "ЛА7": "7401", "ЛА8": "7401",
       "ТМ2": "7474", "ТМ7": "7475", "ЛЕ1": "7402", "ЛИ1": "7408", "ЛН1": "7404", "ЛП5": "7486", "ЛЛ1": "7432",
       "ИР1": "74xx", "ИЕ": "74xx"}
def ktype(name):
    m = re.search(r"\d{3}\s?([А-ЯA-Z]{2})\s?(\d+)", name)
    if not m:
        return None
    return MAP.get(m.group(1) + m.group(2), "other:" + m.group(1) + m.group(2))

def ours(path):
    c = collections.Counter()
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        t = ktype(r["name"])
        if t:
            try:
                q = int(r["qty"])
            except Exception:
                q = 1
            c[t] += q
    return c

def orc(path):
    c = collections.Counter()
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        if re.fullmatch(r"74\d\d", r["part"]):
            c[r["part"]] += 1
    return c

def dist(a, b):
    ks = set(a) | set(b)
    ks = {k for k in ks if not k.startswith("other") and k != "74xx"}
    return sum(abs(a.get(k, 0) - b.get(k, 0)) for k in ks), sum(a.get(k, 0) for k in ks), sum(b.get(k, 0) for k in ks)

O = {Path(p).name[:-8]: orc(p) for p in sorted(glob.glob(str(D / "orcad" / "*_bom.csv")))}
_f = open(D / "orcad" / "fingerprint_match.csv", "w", encoding="utf-8-sig", newline="")
W = csv.writer(_f, lineterminator='\n')
W.writerow(["ric", "n_ic_ours", "best_orcad", "n_ic_orcad", "l1_dist", "second", "l1_second"])
for p in sorted(glob.glob(str(E3 / "ric*_bom.csv"))):
    a = ours(p)
    if sum(a.values()) < 8:
        continue
    sc = sorted((dist(a, b)[0], k, dist(a, b)[2]) for k, b in O.items() if sum(b.values()) >= 8)
    if len(sc) < 2:
        continue
    W.writerow([Path(p).name[:-8], sum(v for k, v in a.items() if not k.startswith("other") and k != "74xx"), sc[0][1], sc[0][2], sc[0][0], sc[1][1], sc[1][0]])
_f.close()
print(open(D / "orcad" / "fingerprint_match.csv", encoding="utf-8-sig").read())
