"""Bảng gán chân P1: đầu nối khối (3Ш1/3Ш2/3Ш7) -> kênh đệm -> chân header A7-Lite -> chân FPGA + bank.
Đầu vào:
  - tmp/pdfs/review/ban-kiem-tra/p1_pinout.csv   (sinh bởi p1_pinout.py)
  - tmp/pdfs/review/ban-kiem-tra/a7lite_gpio_banks.csv (JP1/JP2 -> chân FPGA -> bank; bank lấy từ Vivado 2022.1 get_property BANK
    trên xc7a35tfgg484-2; bảng JP1/JP2 lấy từ A7-Lite Reference Manual của Microphase)
Quy tắc gán (xem P1 §9):
  JP1 (bank 16, VCCIO_A mặc định 3,3 V)  <- 3Ш1 (27 tín hiệu) + điều khiển đệm + SPI mở rộng 3Ш7
  JP2 (bank 14, 3,3 V cố định)           <- 3Ш2 (43 tín hiệu); chân 49/50 (bank 34) chỉ cho đường chậm
  Chỉ dùng chân GPIO; bỏ chân nguồn/mát của header (11,12,29,30,41,42).
Hướng: out = khối -> bàn ([A3] Bảng 5), in = bàn -> khối ([A3] Bảng 4), bi = chưa chắc/hai chiều.
"""
import csv, re, collections, sys
from pathlib import Path

D = Path(r"E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/2.BO TLTK DAU A_A313-V/tmp/pdfs/review/ban-kiem-tra")
pinout = list(csv.DictReader(open(D / "p1_pinout.csv", encoding="utf-8-sig")))
gpio = list(csv.DictReader(open(D / "a7lite_gpio_banks.csv", encoding="utf-8-sig")))
G = {(r["jp"], int(r["jp_pin"])): r for r in gpio if r["signal"].startswith("GPIO")}
FUNC = {r[0]: r[2] for r in csv.reader(open(D / "xc7a35tfgg484_pkgpins.csv"))}
# Chân nhạy khi cấu hình: PUDC_B quyết định kéo lên trong lúc cấu hình, EMCCLK là xung nhịp cấu hình ngoài → không gán tín hiệu
AVOID = {pin for pin, f in FUNC.items() if "PUDC_B" in f or "EMCCLK" in f}

def free_pins(jp, allow_bank34=False):
    out = []
    for n in range(1, 51):
        r = G.get((jp, n))
        if not r:
            continue
        if r["bank"] == "34" and not allow_bank34:
            continue
        if r["fpga_pin"] in AVOID:
            continue
        out.append(n)
    return out

sig = [r for r in pinout if r["class"] in ("data", "addr", "strobe", "time", "ctrl", "observe")]
def key(r):
    m = re.search(r"(\d+)Р", r["signal"].upper())
    return (r["connector"], int(r["pin"]))
by = collections.defaultdict(list)
for r in sig:
    by[r["connector"]].append(r)
for k in by:
    by[k].sort(key=key)

def name(r):
    return r["signal"]

# --- phân nhóm đệm ---
# Hướng 3Ш2 (lần 2, 26/10/2026) lấy từ HDSDKT + Э4; mức bằng chứng:
#   A = bảng/văn bản HDSDKT nói thẳng; B = suy từ biểu thức/mô tả chức năng trong HDSDKT; C = suy từ tên, chưa xác minh
# Quy tắc an toàn: đường chưa chắc chiều (C) đi vào nhóm nhận-một-chiều (không bao giờ lái khối); chỉ ПРИНУДИТ.ЗАПУСК
# (chưa biết ai lái) vào nhóm hai chiều Hi-Z.
s31 = by["3Ш1"]                                  # 27: КШЗП, КША (ra khối)
s32 = {int(r["pin"]): r for r in by["3Ш2"]}
CLS = {}
for pn in range(2, 20):
    CLS[pn] = ("B-in", "A", "Bảng 4 [A3]")                       # КШЧТ 0–17 (pin 2–19)
CLS.update({
    21: ("B-in", "A", "Bảng 4: ИВЧ; tải sink lớn, xem P1 §9.3"),
    22: ("B-in", "A", "tr.24 [A3] «kết thúc chu kỳ… từ A-313-2 đưa ra ИКО», Bảng 4 (Bảng 5 cũng ghi ИКО: coi là ghi trùng, kiểm khi đo)"),
    23: ("A-out", "A", "Bảng 5"), 24: ("A-out", "A", "Bảng 5"), 25: ("A-out", "A", "Bảng 5"), 26: ("A-out", "A", "Bảng 5"),
    40: ("B-in", "B", "biểu thức РгПр∧(РМКПА∨РгК1КПА∨РгК2КПА) [A3]: tín hiệu từ КПА (= ПС17-318)"),
    41: ("B-in", "B", "như 40"), 42: ("B-in", "B", "như 40"),
    45: ("B-in", "B", "công tắc ЗАПРЕТ trên bàn Nga (HDSDKT bước 8); biểu thức СТРОБ∧ЗАПРЕТ ВрМ"),
    46: ("B-in", "B", "như 45; Э4 ghi thêm đích 3Ш4/52"), 47: ("B-in", "B", "như 45"),
    48: ("B-in", "B", "«Вх \"П\" ТТл» là lệnh đơn nhanh đưa vào BUS (HDSDKT, bộ điều khiển lệnh)"),
    44: ("A-out", "B", "«yêu cầu Чт, Зп ЦВУ, Зп КПА» do khối tạo (HDSDKT hình 12)"),
    27: ("A-out", "C", "СБОЙ mod 2 do khối tạo (HDSDKT hình 16); Э4 không ghi địa chỉ đích; nhận một chiều nên an toàn dù sai"),
    32: ("A-out", "C", "tên «cảnh báo hỏng sớm»; Э4 không ghi địa chỉ; nhận một chiều nên an toàn dù sai"),
    20: ("C-bi", "C", "Э4: У1П2/47; chưa biết ai lái; mặc định Hi-Z"),
    35: ("F-lvl", "B", "Y24 tạo: tốt = 5,2±1 V, hỏng < 0,5 V (HDSDKT, mạch Y24); vượt 5,5 V → chia áp"),
    36: ("F-lvl", "C", "Э4: У24/8; mức chưa có số; chia áp trước, đo thật"),
    37: ("F-lvl", "C", "Э4: У24/18; mức chưa có số; chia áp trước, đo thật"),
    39: ("F-lvl", "B", "Y24: tốt ≤ 0,5 V, hỏng ≥ 15 V (HDSDKT); **tới 15 V → bắt buộc chia áp/kẹp**"),
    28: ("N-nc", "B", "Э4: dòng bị gạch xoá, địa chỉ У16КП1/32 để trống; không nối, giữ chân dự phòng"),
    29: ("N-nc", "B", "như 28 (У16КП1/33)"), 30: ("N-nc", "B", "như 28 (У16КП1/34)"), 31: ("N-nc", "B", "như 28 (У16КП1/35)"),
})
s37 = by["3Ш7"]
assert len(s31) == 27 and len(s37) == 22
sig32 = {pn for pn, r in s32.items()}
assert sig32 == set(CLS), (sorted(sig32 - set(CLS)), sorted(set(CLS) - sig32))
cnt = collections.Counter(v[0] for v in CLS.values())
assert cnt == {"B-in": 27, "A-out": 7, "C-bi": 1, "F-lvl": 4, "N-nc": 4}, cnt

rows = []
def add(conn, r, grp, buf, ch, jp, jpn, note=""):
    g = G[(jp, jpn)] if jp else None
    rows.append(dict(connector=conn, uut_pin=r["pin"], signal=name(r), dir=grp[0], group=grp[1], buffer=buf, buf_ch=ch,
                     jp=jp or "", jp_pin=jpn or "", fpga_pin=(g["fpga_pin"] if g else ""), bank=(g["bank"] if g else ""), note=note))

# ---------- JP1 ----------
p1 = free_pins("JP1")                       # 44 chân bank 16
i1 = iter(p1)
bufA = ["BA1", "BA2", "BA3", "BA4", "BA5"]
aidx = 0
for r in s31:
    add("3Ш1", r, ("out", "A-out"), bufA[aidx // 8], aidx % 8 + 1, "JP1", next(i1), "[A] Bảng 5")
    aidx += 1

# ---------- JP2 ----------
p2 = free_pins("JP2")                       # bank 14
p2_slow_extra = [n for n in free_pins("JP2", allow_bank34=True) if n not in p2]   # 49, 50 (bank 34)
_i2 = iter(list(p2) + p2_slow_extra)
def next2():
    try:
        return ("JP2", next(_i2))
    except StopIteration:
        return ("JP1", next(i1))
bufI = ["BI1", "BI2", "BI3", "BI4"]
iidx = 0
order32 = [pn for pn in sorted(s32) if CLS[pn][0] == "B-in"] + [pn for pn in sorted(s32) if CLS[pn][0] == "A-out"] \
        + [pn for pn in sorted(s32) if CLS[pn][0] == "C-bi"] + [pn for pn in sorted(s32) if CLS[pn][0] == "F-lvl"]
fidx = 0
for pn in order32:
    grp, ev, why = CLS[pn]
    r = s32[pn]
    jp_, pn_ = next2()
    note = f"[{ev}] {why}" + ("; tràn sang JP1" if jp_ == "JP1" else "")
    if grp == "B-in":
        add("3Ш2", r, ("in", grp), bufI[iidx // 8], iidx % 8 + 1, jp_, pn_, note); iidx += 1
    elif grp == "A-out":
        add("3Ш2", r, ("out", grp), bufA[aidx // 8], aidx % 8 + 1, jp_, pn_, note); aidx += 1
    elif grp == "C-bi":
        add("3Ш2", r, ("bi", grp), "BB1", 1, jp_, pn_, note)
    else:
        fidx += 1
        add("3Ш2", r, ("lvl", grp), "LV1", fidx, jp_, pn_, note)
for pn in sorted(s32):
    if CLS[pn][0] == "N-nc":
        grp, ev, why = CLS[pn]
        add("3Ш2", s32[pn], ("-", grp), "", "", "", "", f"[{ev}] {why}")

# ---------- 3Ш7: quan sát qua thanh ghi dịch ----------
for n, r in enumerate(s37):
    add("3Ш7", r, ("obs", "D-obs"), f"SR{n // 8 + 1}", n % 8 + 1, "", "", "đọc nối tiếp, chỉ quan sát")

# ---------- điều khiển và mở rộng trên JP1 (phần còn lại) ----------
ctrl = [
    ("DRV_EN_UUT_N", "out", "OE cho nhóm B-in; kéo lên bằng điện trở ngoài để Hi-Z khi FPGA chưa nạp (PUDC_B)"),
    ("DIR_BB1", "out", "DIR đệm hai chiều BB1 (1 đường: ПРИНУДИТ.ЗАПУСК)"),
    ("OE_BB_N", "out", "OE nhóm C-bi; kéo lên ngoài"),
    ("SR_CLK", "out", "SPI/nối tiếp mở rộng 3Ш7: SCK"),
    ("SR_LOAD_N", "out", "tải song song SR1…SR3"),
    ("SR_MISO", "in", "dữ liệu nối tiếp về"),
    ("ESTOP_IN", "in", "nút ngắt khẩn cứng (mức an toàn khi mất dây)"),
    ("RES_1", "-", "dự phòng"), ("RES_2", "-", "dự phòng"), ("RES_3", "-", "dự phòng"), ("RES_4", "-", "dự phòng"),
]
for nme, d, note in ctrl:
    jpn = next(i1)
    g = G[("JP1", jpn)]
    rows.append(dict(connector="BÀN", uut_pin="", signal=nme, dir=d, group="E-ctrl", buffer="", buf_ch="",
                     jp="JP1", jp_pin=jpn, fpga_pin=g["fpga_pin"], bank=g["bank"], note=note))
remaining1 = list(i1)

# ---------- kiểm tra ----------
fp = [r["fpga_pin"] for r in rows if r["fpga_pin"]]
assert len(fp) == len(set(fp)), "trùng chân FPGA"
used = collections.Counter((r["jp"], r["bank"]) for r in rows if r["jp"])
power = {11, 12, 29, 30, 41, 42}
assert not any(r["jp_pin"] in power for r in rows if r["jp"]), "dùng chân nguồn"

OUT = D / "p1_pin_assignment.csv"
cols = ["connector", "uut_pin", "signal", "dir", "group", "buffer", "buf_ch", "jp", "jp_pin", "fpga_pin", "bank", "note"]
with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator='\n')
    w.writeheader()
    w.writerows(rows)

print("dòng:", len(rows), "| chân FPGA dùng:", len(fp))
print("theo (header, bank):", dict(used))
print("JP1 còn trống:", len(remaining1), "| JP2 còn trống:", len(list(_i2)), "| chân tránh (PUDC_B/EMCCLK):", sorted(AVOID & {r["fpga_pin"] for r in G.values()}))
g = collections.Counter(r["group"] for r in rows)
print("theo nhóm:", dict(g))
ics = {}
for r in rows:
    if r["buffer"]:
        ics.setdefault(r["buffer"], 0)
        ics[r["buffer"]] += 1
print("kênh/IC:", ics)
