"""Bảng chân P1 (3Ш1, 3Ш2, 3Ш7) cho bàn kiểm tra A-313-3 mới.
Nguồn chân/tín hiệu: Excel center control/A313-3_ket-noi-toan-khoi.xlsx (sheet ket_noi_chung).
Nguồn HƯỚNG: A-313-3.HDSDKT.pdf Bảng 4 (vào khối: КШЧт, ИВЧ, ИКО) và Bảng 5 (ra khối: КШЗп, КША, ЗпУВВ, ЧтУВВ, ИКО, ВрМ1, ВрМ2).
Cột 'Số chiều tham chiếu' của workbook KHÔNG phải hướng đã xác minh nên không dùng.
Hướng tính từ khối A-313-3: out = khối phát (bàn đọc), in = khối nhận (bàn phát), ? = chưa có căn cứ.
"""
import csv, re
from pathlib import Path
import openpyxl

ROOT = Path(r"E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/2.BO TLTK DAU A_A313-V")
XLSX = ROOT / "Excel center control/A313-3_ket-noi-toan-khoi.xlsx"
OUT = ROOT / "tmp/pdfs/review/ban-kiem-tra/p1_pinout.csv"

def classify(name):
    n = name.upper().replace("¬", "")
    if n.startswith("КОРПУС") or n.startswith("ОБЩ"):
        return "gnd", "-", "-"
    if re.match(r"^[+-]\d", n) or n.startswith(("УПР. (", "УПР.(")):
        return "power/ctrl", "?", "rail hoặc điều khiển rail; không nối vào FPGA"
    if n.startswith("КШЗП"):
        return "data", "out", "Bảng 5 [A3]"
    if n.startswith("КША"):
        return "addr", "out", "Bảng 5 [A3]"
    if n.startswith(("ЗП УВВ", "ЧТ. УВВ", "ЧТ УВВ")):
        return "strobe", "out", "Bảng 5 [A3]; tích cực mức thấp (¬)"
    if n.startswith(("ВР. М1", "ВРМ1", "ВРМ2")):
        return "time", "out", "Bảng 5 [A3]"
    if n.startswith("КШЧТ"):
        return "data", "in", "Bảng 4 [A3]"
    if n.startswith("ИВЧ"):
        return "strobe", "in", "Bảng 4 [A3]; tích cực mức thấp (¬)"
    if n.startswith("ИКО"):
        return "strobe", "in", "Bảng 4 [A3]; Bảng 5 cũng liệt kê ИКО ở đầu ra → mâu thuẫn, cần Hình 8"
    if n.startswith(("СТРОБ", "0Р. СЧК", "1Р. СЧК", "2Р СЧК")) or "СЧК" in n:
        return "observe", "?", "điểm quan sát; hướng chưa xác minh"
    return "ctrl", "?", "hướng chưa có căn cứ trong [A3] Bảng 4–5"

wb = openpyxl.load_workbook(XLSX, read_only=True)
rows = list(wb["ket_noi_chung"].iter_rows(values_only=True))
hdr = rows[0]
out = []
for conn in ("3Ш1", "3Ш2", "3Ш7"):
    i = hdr.index(conn)
    for r in rows[1:]:
        if not r[0] or not r[i]:
            continue
        for pin in str(r[i]).split(";"):
            cls, d, note = classify(str(r[0]))
            out.append((conn, pin.strip(), r[0], cls, d, note))
out.sort(key=lambda x: (x[0], int(re.sub(r"\D", "", x[1]) or 0)))
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["connector", "pin", "signal", "class", "dir_from_uut", "basis"])
    w.writerows(out)

import collections
c = collections.Counter((o[0], o[3], o[4]) for o in out)
for k in sorted(c):
    print(k, c[k])
sig = [o for o in out if o[3] in ("data", "addr", "strobe", "time", "ctrl", "observe")]
print("tín hiệu số (không rail/mát):", collections.Counter(o[0] for o in sig))
