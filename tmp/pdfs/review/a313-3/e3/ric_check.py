"""Kiểm tra chéo ricNN_bom/net và tính các giá trị danh định cho рис.20 (УЛП +20 В) và рис.21 (УЛП 6,3 В).
Chạy: python3 tmp/pdfs/review/a313-3/e3/ric_check.py  (từ gốc repo)"""
import csv
from collections import defaultdict
from pathlib import Path

D = Path(__file__).parent


def check(nn):
    bom = [r['ref'] for r in csv.DictReader(open(D / f'ric{nn}_bom.csv', encoding='utf8'))]
    net = list(csv.DictReader(open(D / f'ric{nn}_net.csv', encoding='utf8')))
    assert len(bom) == len(set(bom)), 'trùng ref trong bom'
    refs_net = {r['ref'] for r in net}
    pins = defaultdict(list)
    for r in net:
        pins[r['net']].append(f"{r['ref']}:{r['pin']}")
    dup = [k for k in {(r['ref'], r['pin']) for r in net} if sum(1 for r in net if (r['ref'], r['pin']) == k) > 1]
    single = {n: p for n, p in pins.items() if n.startswith('N') and len(p) < 2}
    print(f'рис.{nn}: bom {len(bom)} ref, net {len(net)} chân, {len(pins)} net '
          f'({sum(1 for n in pins if n.startswith("N"))} N#, {sum(1 for n in pins if n.startswith("X"))} X)')
    print('  bom∖net:', sorted(set(bom) - refs_net) or '—', '| net∖bom:', sorted(refs_net - set(bom)) or '—')
    print('  chân trùng:', dup or '—', '| N# <2 chân:', single or '—')
    assert not dup and not single and set(bom) == refs_net
    return pins


def par(a, b):
    return a * b / (a + b)


p20, p21 = check(20), check(21)

# --- điện áp chuẩn: cả hai УЛП dùng cùng tỷ số 5,62k / 2,21k từ ổn áp ---
VZ = 9.0  # Д818Д danh định 9 V (giả định cho Д1 рис.21: ПЭ trang 220 thiếu)
k_ref = 2.21 / (5.62 + 2.21)
vref = VZ * k_ref
print(f'\nVref = VZ·2,21/(5,62+2,21) = {VZ}·{k_ref:.4f} = {vref:.3f} V')

# рис.20: Uвых → R12 (5,62k) → R13 (2,2k, con trượt → У1:10) → 0 ; R20 820k từ +27 V vào У1:10
R12, R13, R20 = 5.62e3, 2.2e3, 820e3
for vout in (20.0,):
    lo = vref * (R12 + R13) / vout
    print(f'рис.20: Uвых={vout} V ⇒ R13 phần dưới ≈ {lo:.0f} Ω ({lo / R13 * 100:.0f} % hành trình), bỏ qua R20')
umin = vref * (R12 + R13) / R13
print(f'рис.20: dải chỉnh (R20 bỏ qua): {umin:.2f} V (con trượt ở đỉnh) … ∞ ⇒ không có chặn dưới')
lo = vref * (R12 + R13) / 20.0
rth = par(lo, R12 + R13 - lo)
dv = 27.0 * rth / (R20 + rth)  # điện áp R20 bơm vào nút У1:10 khi Uвых = 0 (xấp xỉ tuyến tính)
print(f'рис.20: R20 820k từ 27 V bơm ≈ {dv * 1e3:.1f} mV vào У1:10 ⇒ Uвых giảm ≈ {dv * (R12 + R13) / lo:.2f} V '
      f'(bù theo điện áp vào; ΔUвх=±3 V ⇒ ±{3 * rth / (R20 + rth) * (R12 + R13) / lo * 1e3:.0f} mV ở đầu ra)')
tau = 4.7e-6 * par(5.62e3, 2.21e3)
print(f'рис.20: soft-start Vref: C5·(R10∥R17) = {tau * 1e3:.1f} ms (3τ ≈ {3 * tau * 1e3:.0f} ms)')
iz = (20 - VZ) / 680, (20 - VZ) / 680e3
print(f'рис.20: dòng qua R11 cấp Д3+У1 ở Uвых=20 V: 680 Ω → {iz[0] * 1e3:.1f} mA, P={iz[0] ** 2 * 680:.2f} W; '
      f'680 kΩ → {iz[1] * 1e6:.0f} µA (không đủ cho 140УД1 + Д818)')

# рис.21: Uвых → R16 (274 Ω) → R17 (2,2k, con trượt → У1:10) → 0
R16, R17 = 274.0, 2.2e3
for vout in (5.0, 6.3):
    lo = vref * (R16 + R17) / vout
    print(f'рис.21: Uвых={vout} V ⇒ R17 phần dưới ≈ {lo:.0f} Ω ({lo / R17 * 100:.0f} % hành trình)')
print(f'рис.21: con trượt ở đỉnh ⇒ Uвых min = {vref * (R16 + R17) / R17:.2f} V')
iz21 = (27 - VZ) / 1.2e3
print(f'рис.21: R1 1,2k cấp Д1+У1 từ 27 V: I={iz21 * 1e3:.1f} mA, P(R1)={iz21 ** 2 * 1.2e3:.2f} W (định mức 1 W)')

# ngưỡng hạn dòng: Т6 mở khi I·R_DC(Др3) ≈ 0,6 V
for r in (0.1, 0.3, 1.0):
    print(f'  Др3 R_DC={r} Ω ⇒ I_hạn ≈ {0.6 / r:.1f} A')
