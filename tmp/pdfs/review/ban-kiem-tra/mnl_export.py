"""Xuất BOM + net từ các tệp .MNL (OrCAD Layout V7) của hồ sơ bàn kiểm Nga.

  python mnl_export.py            -> tmp/pdfs/review/ban-kiem-tra/orcad/<tên>_{bom,net}.csv + summary.csv
Kiểm tự động mỗi tệp: (1) mọi chỉ số linh kiện của chân nằm trong danh sách; (2) với IC 74xx (14/16 chân) chân nguồn
phải về net VCC và chân mát về GND — nếu lệch, tệp bị đánh dấu `warn`, KHÔNG dùng làm chuẩn.
"""
import csv, hashlib, re, struct, sys, collections
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mnl_parse as m

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "thiet_bi_kiem_tra_a313"
OUT = Path(__file__).parent / "orcad"
OUT.mkdir(exist_ok=True)

def comps_of(st):
    comps = []
    for k in range(len(st) - 3):
        s = st[k][1]
        if m.REF.match(s) and st[k + 2][1] == b"":
            comps.append((s.decode(), st[k + 1][1].decode("cp1251").strip(), st[k + 3][1].decode("cp1251").strip()))
    return comps

PWR = {"7400": (14, 7), "7410": (14, 7), "7420": (14, 7), "7474": (14, 7), "7404": (14, 7), "7402": (14, 7), "7408": (14, 7),
       "7432": (14, 7), "7486": (14, 7), "7430": (14, 7), "7440": (14, 7), "74": (14, 7)}

def export(path, tag):
    b, st, nets = m.parse(path)
    comps = comps_of(st)
    pin_rows = []   # (net, compidx, pin)
    for nm, pl in nets.items():
        for p, d in pl:
            ci = struct.unpack_from("<I", d, 20)[0]
            pin_rows.append((nm, ci, p))
    maxi = max((r[1] for r in pin_rows), default=-1)
    bad_idx = sum(1 for r in pin_rows if r[1] >= len(comps))
    # kiểm nguồn/mát
    chk = bad = 0
    for ci in sorted({r[1] for r in pin_rows}):
        if ci >= len(comps):
            continue
        ref, pkg, part = comps[ci]
        mm = re.match(r"^74(?:LS|HC|ALS|F)?(\d+)", part.replace(" ", ""))
        if not (mm and re.match(r"^74\d\d$", part)):
            continue
        pins = [(n, p) for n, c, p in pin_rows if c == ci]
        v, g = PWR.get(part, (14, 7))
        nv = {n for n, p in pins if p == str(v)}
        ng = {n for n, p in pins if p == str(g)}
        if nv or ng:
            chk += 1
            if (nv and "VCC" not in nv) or (ng and "GND" not in ng):
                bad += 1
    with open(OUT / f"{tag}_bom.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(["idx", "ref", "package", "part"])
        used = {r[1] for r in pin_rows}
        for i, (r, pk, pt) in enumerate(comps):
            if i in used:
                w.writerow([i, r, pk, pt])
    with open(OUT / f"{tag}_net.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(["net", "ref", "pin"])
        for nm, ci, p in pin_rows:
            ref = comps[ci][0] if ci < len(comps) else f"?{ci}"
            w.writerow([nm, ref, p])
    return dict(tag=tag, comps_used=len({r[1] for r in pin_rows}), nets=len(nets), pins=len(pin_rows),
                max_idx=maxi, bad_idx=bad_idx, pwr_checked=chk, pwr_bad=bad,
                status="OK" if bad_idx == 0 and bad == 0 else "warn", src=str(path.relative_to(ROOT)))

def main():
    seen = {}
    rows = []
    for p in sorted(SRC.rglob("*")):
        if p.suffix.lower() != ".mnl":
            continue
        h = hashlib.md5(p.read_bytes()).hexdigest()
        if h in seen:
            continue
        seen[h] = p
    for h, p in seen.items():
        tag = re.sub(r"[^0-9A-Za-z]+", "_", p.stem).strip("_") + "_" + h[:6]
        try:
            rows.append(export(p, tag))
        except Exception as e:
            rows.append(dict(tag=tag, status="error:" + type(e).__name__, src=str(p.relative_to(ROOT))))
    keys = ["tag", "status", "comps_used", "nets", "pins", "max_idx", "bad_idx", "pwr_checked", "pwr_bad", "src"]
    with open(OUT / "summary.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore", lineterminator='\n'); w.writeheader(); w.writerows(rows)
    c = collections.Counter(r["status"] for r in rows)
    print("tệp MNL duy nhất:", len(rows), dict(c))
    for r in rows:
        print(r["status"], r.get("comps_used"), r.get("nets"), r.get("pwr_checked"), r.get("pwr_bad"), r["tag"][:40])

if __name__ == "__main__":
    main()
