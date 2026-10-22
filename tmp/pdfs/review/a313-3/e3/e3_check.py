"""Kiểm tra chéo ricNN_bom.csv / ricNN_net.csv và tính các giá trị danh định dùng trong ricNN_mota.md.

Chạy từ gốc repo:  python3 tmp/pdfs/review/a313-3/e3/e3_check.py
"""
import csv
from collections import defaultdict
from pathlib import Path

D = Path(__file__).parent


def check(nn):
    bom = [r['ref'] for r in csv.DictReader(open(D / f'ric{nn}_bom.csv', encoding='utf8'))]
    net = list(csv.DictReader(open(D / f'ric{nn}_net.csv', encoding='utf8')))
    assert len(bom) == len(set(bom)), f'ric{nn}: trùng ref trong bom'
    nref = {r['ref'] for r in net}
    pins = defaultdict(list)
    seen = set()
    for r in net:
        key = (r['ref'], r['pin'])
        assert key not in seen, f'ric{nn}: chân lặp {key}'
        seen.add(key)
        pins[r['net']].append(key)
    single = {n: p for n, p in pins.items() if n.startswith('N') and len(p) < 2}  # net X:… nối ra đầu cắm được phép 1 chân
    print(f'ric{nn}: bom {len(bom)} ref, net {len(net)} chân, {len(pins)} net '
          f'({sum(1 for n in pins if n.startswith("N"))} N#)')
    print('  trong bom không có trong net:', sorted(set(bom) - nref) or '—')
    print('  trong net không có trong bom:', sorted(nref - set(bom)) or '—')
    print('  N# < 2 chân:', single or '—')
    return not (set(bom) ^ nref) and not single


def calc():
    vbe = 0.65  # shortcut: Vbe cố định 0,65 V; thực tế 0,55–0,8 V theo dòng
    vz = 9.0    # Д818Д/Е: 9 V danh định
    print('\nрис.24')
    # Khối −5 V: R4 4,7k song song Д1; T3 p-n-p, база qua R5 từ ra: Vout ≈ Vwiper − Vbe
    k1 = (5.0 - vbe) / vz
    print(f'  −5 В: Vдвижка R4 = −{5 - vbe:.2f} В → движок ở {k1:.2f} hành trình R4 từ корпус')
    print(f'        dải chỉnh ≈ −{vbe:.2f} … −{vz + vbe:.2f} В (giới hạn thêm bởi đầu vào −12,6 В)')
    for name, rs, rl in (('Д1 (R1, R4)', 470, 4700), ('Д3 (R6, R8+R9)', 470, 3200), ('Д4 (R12, R15+R16)', 470, 4500)):
        i = (12.6 - vz) / rs - vz / rl
        print(f'  Iст {name} ≈ {(12.6 - vz) / rs * 1e3:.2f} − {vz / rl * 1e3:.2f} = {i * 1e3:.2f} мА')
    # Khối +10 В: Vout = (Vw + Vbe)(R11+R20)/R20; Vw ∈ [Vz·R9/(R8+R9); Vz]
    r8, r9, r11, r20 = 2000, 1200, 1500, 1500
    lo, hi = vz * r9 / (r8 + r9), vz
    g = (r11 + r20) / r20
    vw = 10 / g - vbe
    print(f'  +10 В: hệ số chia R11/R20 = {g:.2f}; Vw cần = {vw:.2f} В; dải Vw {lo:.3f}…{hi:.1f} В '
          f'→ Vout {g * (lo + vbe):.2f}…{g * (hi + vbe):.2f} В (thực tế ≤ ~10,6 В do đầu vào +12,6 В)')
    print(f'        dòng phân áp R11+R20 = {10 / (r11 + r20) * 1e3:.2f} мА')
    # Khối −10 В: Vw(R15) ∈ [−Vz·R16/(R15+R16); −Vz]; T10 p-n-p: k(R21)·Vout = Vw − Vbe
    r15, r16 = 1500, 3000
    lo, hi = vz * r16 / (r15 + r16), vz
    print(f'  −10 В: |Vw| {lo:.2f}…{hi:.2f} В → движок R21 k = {(lo + vbe) / 10:.3f}…{(hi + vbe) / 10:.3f} '
          f'(tỉ lệ từ корпус lên −10 В); dòng R21 = {10 / 2200 * 1e3:.2f} мА')
    # +3,5 В: phân áp R18/R19 (220/220) + Д5 2С147А 4,7 В
    for vin in (6.3, 5.0):
        vb = vin * 220 / 440
        print(f'  +3,5 В: Uвх {vin} В → Vб(T11) không tải = {vb:.2f} В (Д5 4,7 В {"không" if vb < 4.7 else ""} dẫn) '
              f'→ Vout ≈ {vb - vbe:.2f} В; R_Thevenin 110 Ом')
    print('\nрис.26')
    vin, vout = 27.0, 12.6
    print(f'  buck-boost đảo, CCM lý tưởng: D = U/(U+Uвх) = {vout / (vout + vin):.3f}; '
          f'Uвх 24…29,7 В → D {vout / (vout + 29.7):.3f}…{vout / (vout + 24):.3f}')
    print(f'  điện áp ngược trên T6/Д2 ≈ Uвх+U = {vin + vout:.1f} В (Uвх 29,7 → {29.7 + vout:.1f} В)')
    print(f'  dòng trung bình qua Др2 ≈ Iн/(1−D) = {1 / (1 - vout / (vout + vin)):.2f} А tại 1 А')
    print(f'  điểm cân bằng: U = Vz·(R2+R3+R4)/(R4+k·R3); cần (R2+R3+R4)/(R4+kR3) = {vout / vz:.3f} — R2…R4 thiếu (tr. 238)')
    print(f'  ngưỡng bảo vệ: Iкз ≈ Vbe(T9)·(R17+R18)/(R17·R_Др3) — R17, R18, R_Др3 chưa biết')


KNOWN = {19: 'Д7 có trong перечень, không có trên Э3', 25: 'R28, Д3, Д4 có trong перечень, không có trên Э3 (góc ảnh #233 bị che)'}

if __name__ == '__main__':
    bad = [nn for nn in (19, 20, 21, 22, 23, 24, 25, 26) if not check(nn)]
    calc()
    assert set(bad) <= set(KNOWN), 'có ngoại lệ mới: %s' % (set(bad) - set(KNOWN))
    for nn in bad:
        print('ngoại lệ đã biết ric%d: %s' % (nn, KNOWN[nn]))
