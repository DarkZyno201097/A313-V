"""Bản đồ đường đi của tín hiệu giao tiếp ЦВУ trong khối A-313-3: dựng từ Э4 (e4_all.csv) + dữ liệu chép tay ric*.

Đầu ra: orcad/../signal_paths.csv  (tín hiệu, điểm đầu nối, nhãn, ghi chú) và signal_paths.md.
KHÔNG phải mô hình thời gian: chỉ liệt kê điểm cuối (tấm, đầu nối, chân) mà mỗi tín hiệu tới, và tải IC đã chép được ở đầu vào.
Điểm trống = dữ liệu chưa chép tới (ghi rõ), không suy đoán.
"""
import csv, re, collections
from pathlib import Path
D = Path(__file__).parent
E3 = D.parent / "a313-3" / "e3"
E4 = D.parent / "a313-3" / "e4" / "e4_all.csv"

def norm(tbl, pin):
    return (tbl.strip().replace(" ", ""), str(pin).strip())

parent = {}
def find(x):
    parent.setdefault(x, x)
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb

label = collections.defaultdict(set)
note = collections.defaultdict(list)
for r in csv.DictReader(open(E4, encoding="utf-8-sig")):
    node = norm(r["table"], r["pin"])
    find(node)
    sg = r["signal"].strip()
    if sg:
        label[node].add(sg)
    if r["note"]:
        note[node].append(r["note"][:60])
    for a in re.split(r"[;,]", r["address"] or ""):
        a = a.strip()
        m = re.match(r"^(.+?)/(\d+)$", a)
        if m and m.group(1) not in ("КОРПУС",):
            n2 = norm(m.group(1), m.group(2))
            union(node, n2)
            find(n2)

groups = collections.defaultdict(list)
for n in list(parent):
    groups[find(n)].append(n)

TARGETS = ["ИВЧ", "ИКО", "ЧТ. УВВ", "ЗП УВВ", "Вр. М1", "ВРМ2"]
rows = []
for root, nodes in groups.items():
    sigs = set()
    for n in nodes:
        sigs |= label[n]
    for t in TARGETS:
        if any(t in s for s in sigs):
            for n in sorted(nodes):
                rows.append([t, n[0], n[1], "; ".join(sorted(label[n])), "; ".join(note[n])[:100]])
# КШЧТ: nhóm riêng theo từng bit
for bit in range(18):
    key = f"КШЧТ {bit}Р"
    for root, nodes in groups.items():
        if any(key in s for n in nodes for s in label[n]):
            for n in sorted(nodes):
                rows.append([key, n[0], n[1], "; ".join(sorted(label[n])), ""])

with open(D / "signal_paths.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, lineterminator='\n'); w.writerow(["tin_hieu", "dau_noi", "chan", "nhan", "ghi_chu"]); w.writerows(rows)

# tóm tắt theo tín hiệu: số đầu nối khác nhau, các tấm đích
summ = collections.OrderedDict()
for t, tb, pin, lab, nt in rows:
    summ.setdefault(t, set()).add((tb, pin))
out = ["# Đường đi tín hiệu giao tiếp ЦВУ (từ Э4)\n", "Sinh bởi `signal_paths.py`; chi tiết ở `signal_paths.csv`. Mỗi dòng: các điểm đầu nối cùng một nhóm dây theo Э4.\n"]
for t, s in summ.items():
    def _b(tb):
        mm = re.match(r"^(У\d+|3Ш\d+В?)", tb)
        return mm.group(1) if mm else tb
    boards = collections.Counter(_b(tb) for tb, _ in s)
    out.append(f"- **{t}**: {len(s)} điểm — " + ", ".join(f"{k}×{v}" for k, v in sorted(boards.items())))
open(D / "signal_paths.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
