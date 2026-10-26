"""Sinh P1_BANG-CHAN_BAN-KIEM-TRA-A-313-3.md từ p1_pin_assignment.csv (không sửa tay file .md)."""
import csv, collections
from pathlib import Path
ROOT = Path(r"E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/2.BO TLTK DAU A_A313-V")
D = ROOT / "tmp/pdfs/review/ban-kiem-tra"
rows = list(csv.DictReader(open(D / "p1_pin_assignment.csv", encoding="utf-8-sig")))
gl = {"A-out": "A — khối → bàn (đệm một chiều, FPGA chỉ đọc)", "B-in": "B — bàn → khối (đệm một chiều, OE do DRV_EN_UUT_N)",
      "C-bi": "C — hai chiều/chưa rõ ai lái (DIR, mặc định Hi-Z)", "F-lvl": "F — đường mức không phải TTL (chia áp/kẹp rồi vào FPGA; chỉ đọc)",
      "D-obs": "D — quan sát 3Ш7 (thanh ghi dịch vào, chỉ đọc)", "N-nc": "N — không nối (Э4 gạch xoá), chân khối để hở",
      "E-ctrl": "E — điều khiển bàn trên JP1"}
out = []
out.append("# BẢNG CHÂN P1 — BÀN KIỂM TRA A-313-3 MỚI\n")
out.append("**File sinh tự động** từ `tmp/pdfs/review/ban-kiem-tra/p1_pin_assignment.csv` bằng `p1_md.py`; sửa dữ liệu bằng `p1_assign.py`, không sửa tay file này.  ")
out.append("Nguồn chân khối: `A313-3_ket-noi-toan-khoi.xlsx`; hướng: [A3] Bảng 4–5; chân FPGA/bank: tài liệu A7-Lite (Microphase) + Vivado 2022.1 `xc7a35tfgg484-2`.  ")
out.append("**Trạng thái: đề xuất để đánh giá khả thi, CHƯA dùng để đặt mạch** (xem P1 §9, các cổng G1–G6).\n")
cnt = collections.Counter((r["jp"], r["bank"]) for r in rows if r["jp"])
out.append("## Tóm tắt\n")
out.append("| Chỉ tiêu | Giá trị |\n|---|---|")
nused = sum(1 for r in rows if r['fpga_pin'])
out.append(f"| Chân FPGA dùng | **{nused}** / 86 dùng được (88 GPIO trừ U22 PUDC_B và V22 EMCCLK) → dư **{86 - nused}** |")
for k, v in sorted(cnt.items()):
    out.append(f"| {k[0]} bank {k[1]} | {v} chân |")
out.append("| Tín hiệu khối vào FPGA | " + str(sum(1 for r in rows if r['group'] in ('A-out', 'B-in', 'C-bi', 'F-lvl'))) + " (+ " + str(sum(1 for r in rows if r['group'] == 'D-obs')) + " quan sát 3Ш7; " + str(sum(1 for r in rows if r['group'] == 'N-nc')) + " không nối) |")
ics = collections.Counter(r["buffer"] for r in rows if r["buffer"])
out.append("| IC đệm 8 bit | " + ", ".join(f"{k}×{v}" for k, v in ics.items()) + " → " + str(len([k for k in ics if k != 'LV1'])) + " IC đệm/dịch + 4 mạch chia áp (LV1) |")
out.append("")
out.append("**Mức bằng chứng hướng tín hiệu (trong cột Ghi chú):** [A] bảng/văn bản HDSDKT nói thẳng; [B] suy từ biểu thức hoặc mô tả chức năng trong HDSDKT/Э4; [C] suy từ tên, **chưa xác minh**. Đường [C] chỉ vào nhóm nhận một chiều hoặc Hi-Z nên không thể lái ngược khối.\n")
for g in ["A-out", "B-in", "C-bi", "F-lvl", "N-nc", "D-obs", "E-ctrl"]:
    sub = [r for r in rows if r["group"] == g]
    out.append(f"## Nhóm {gl[g]} — {len(sub)} đường\n")
    out.append("| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |")
    out.append("|---|---:|---|---|---|---|---:|---|---|---|")
    for r in sub:
        buf = f"{r['buffer']}.{r['buf_ch']}" if r["buffer"] else ""
        out.append(f"| {r['connector']} | {r['uut_pin']} | {r['signal']} | {r['dir']} | {buf} | {r['jp']} | {r['jp_pin']} | {r['fpga_pin']} | {r['bank']} | {r['note']} |")
    out.append("")
out.append("## Chân không nối vào FPGA (ghi để không gán nhầm)\n")
out.append("- 3Ш1: 9 chân КОРПУС (1, 20, 30, 31, 44, 45, 47, 49, 50) và 14 chân rail (+20, +6,3 ×2, +5 ×7, +10, −6,3, −10, −5 В: chân 32–43, 46, 48). Khối nối rail ra đầu nối này: **không nối vào bàn P1**, chỉ đo bằng đầu dò khi cần (xem P1 §9 G5).\n- 3Ш2: 4 chân КОРПУС (1, 38, 49, 50) và chân 33, 34 = **+27 В** (hướng chưa rõ, không nối).\n- 3Ш7: 1 chân КОРПУС (1) và 7 chân Упр./УПР rail (26–32), không nối FPGA.\n- Header A7-Lite: chân 11, 12, 29, 30, 41, 42 là nguồn/mát (không GPIO), không dùng làm tín hiệu.\n- FPGA: U22 (PUDC_B) và V22 (EMCCLK) trên JP2 chân 13, 14 — tránh gán tín hiệu để không ảnh hưởng cấu hình.\n")
open(ROOT / "P1_BANG-CHAN_BAN-KIEM-TRA-A-313-3.md", "w", encoding="utf-8", newline="\n").write("\n".join(out).replace("  \n", "\n\n"))
print("ok", len(rows))
