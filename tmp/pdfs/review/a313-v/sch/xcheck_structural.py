"""Kiểm độc lập netlist SchDoc A313-V bằng bất biến cấu trúc (không dùng lại code của Codex).
(1) Chân lẻ loi: mỗi (kiểu linh kiện, số chân) phải lẻ loi ở TẤT CẢ hoặc KHÔNG instance nào;
    tỷ lệ giữa = nghi dây chưa nối / nối nhầm.
(2) Các kênh lặp lại phải đồng cấu: bỏ net toàn cục (nguồn, mát, net >= GLOBAL_MIN chân),
    tách thành phần liên thông, băm Weisfeiler-Lehman; nhóm đông số nhất là chuẩn, nhóm lệch = nghi sai.
"""
import csv, collections, hashlib, re, sys
from pathlib import Path

SCH = Path(r"E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/2.BO TLTK DAU A_A313-V/tmp/pdfs/review/a313-v/sch")
import os
GLOBAL_MIN = int(os.environ.get("GLOBAL_MIN", "14"))
CONN = re.compile(r"^(DC|XS|XP|J)")

def load(stem):
    bom = {r["ref"]: r for r in csv.DictReader(open(SCH / f"{stem}_bom.csv", encoding="utf-8-sig"))}
    net = list(csv.DictReader(open(SCH / f"{stem}_net.csv", encoding="utf-8-sig")))
    return bom, net

def part_type(bom, ref):
    # tên linh kiện, bỏ giá trị trong [] để gộp biến thể; multipart U9A/U9B -> khác ref nhưng cùng kiểu
    return re.sub(r"\s*\[.*?\]", "", bom[ref]["name"]).strip() if ref in bom else "?"

def singleton_report(stem):
    bom, net = load(stem)
    cnt = collections.Counter(r["net"] for r in net)
    tot = collections.Counter(); sing = collections.Counter()
    for r in net:
        if CONN.match(r["ref"]):
            continue
        key = (part_type(bom, r["ref"]), r["pin"])
        tot[key] += 1
        if cnt[r["net"]] == 1:
            sing[key] += 1
    out = []
    for k in tot:
        if 0 < sing[k] < tot[k]:
            out.append((k, sing[k], tot[k]))
    full = sum(1 for k in tot if sing[k] == tot[k])
    return out, full, sum(sing.values())

def wl_components(stem, rounds=4):
    bom, net = load(stem)
    cnt = collections.Counter(r["net"] for r in net)
    glob = {n for n, c in cnt.items() if c >= GLOBAL_MIN}
    # đồ thị hai phía: nút 'p:ref' và 'n:net'; nhãn nút ban đầu
    adj = collections.defaultdict(list); label = {}
    for r in net:
        if CONN.match(r["ref"]):
            continue
        p = "p:" + r["ref"]; label[p] = part_type(bom, r["ref"])
        if r["net"] in glob:
            # giữ thông tin "nối vào net toàn cục" làm nhãn cạnh của chân
            adj[p].append(("g", r["pin"], r["net"] if len(glob) < 40 else "G"))
            continue
        n = "n:" + r["net"]; label[n] = "net"
        adj[p].append(("e", r["pin"], n)); adj[n].append(("e", r["pin"], p))
    # liên thông trên nút (bỏ cạnh toàn cục)
    seen = set(); comps = []
    for s in list(adj):
        if s in seen: continue
        st = [s]; seen.add(s); comp = []
        while st:
            u = st.pop(); comp.append(u)
            for t, pin, v in adj[u]:
                if t == "e" and v not in seen:
                    seen.add(v); st.append(v)
        comps.append(comp)
    def sig(comp):
        lab = {u: label[u] for u in comp}
        for _ in range(rounds):
            new = {}
            for u in comp:
                nb = sorted((t, pin, lab.get(v, v)) for t, pin, v in adj[u] if t == "g" or v in lab)
                new[u] = hashlib.md5(repr((lab[u], nb)).encode()).hexdigest()[:10]
            lab = new
        return hashlib.md5(repr(sorted(lab.values())).encode()).hexdigest()[:10]
    groups = collections.defaultdict(list)
    for c in comps:
        refs = sorted(u[2:] for u in c if u.startswith("p:"))
        groups[sig(c)].append(refs)
    return groups, len(glob)

if __name__ == "__main__":
    for stem in sys.argv[1:]:
        print("=" * 20, stem)
        out, full, nsing = singleton_report(stem)
        print(f"chân linh kiện lẻ loi: {nsing}; nhóm (kiểu,chân) lẻ loi 100%: {full}; nhóm lẻ loi MỘT PHẦN: {len(out)}")
        for k, a, b in sorted(out, key=lambda x: -x[1])[:25]:
            print("  PARTIAL", k, f"{a}/{b}")
        groups, ng = wl_components(stem)
        print(f"net toàn cục (>= {GLOBAL_MIN} chân): {ng}; thành phần liên thông: {sum(len(v) for v in groups.values())}; nhóm đồng cấu: {len(groups)}")
        for h, lst in sorted(groups.items(), key=lambda x: -len(x[1]))[:12]:
            print(f"  nhóm {h}: {len(lst):3d} thành phần, cỡ {len(lst[0])} ref, vd {lst[0][:6]}")
        small = [(h, l) for h, l in groups.items() if len(l) == 1]
        print("  nhóm chỉ 1 thành phần:", len(small))
