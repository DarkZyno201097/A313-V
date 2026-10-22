"""Kiểm tra chéo ric25_bom.csv ↔ ric25_net.csv và tính các giá trị danh định trong ric25_mota.md.
Chạy: python3 tmp/pdfs/review/a313-3/e3/ric25_tinh.py
"""
import csv
from collections import Counter, defaultdict
from math import log
from pathlib import Path

D = Path(__file__).parent
bom = list(csv.DictReader(open(D / 'ric25_bom.csv', encoding='utf8')))
net = list(csv.DictReader(open(D / 'ric25_net.csv', encoding='utf8')))
br = [r['ref'] for r in bom]
assert len(br) == len(set(br)), [k for k, v in Counter(br).items() if v > 1]
B, Nn = set(br), {r['ref'] for r in net}
print('BOM refs:', len(B), '| net refs:', len(Nn), '| net rows:', len(net))
print('bom-only:', sorted(B - Nn)); print('net-only:', sorted(Nn - B))
pins = Counter((r['ref'], r['pin']) for r in net)
assert all(v == 1 for v in pins.values()), [k for k, v in pins.items() if v > 1]
nets = defaultdict(list)
for r in net: nets[r['net']].append(r['ref'] + '.' + r['pin'])
bad = [k for k, v in nets.items() if k.startswith('N') and len(v) < 2]
assert not bad, bad
print('nets:', len(nets), '| N#:', sum(k.startswith('N') and k != 'NC' for k in nets), '| N# <2 pins: none')
# số chân mong đợi theo loại
want = {'R': 2, 'C': 2, 'T': 3, 'Д': 2, 'Пр': 2, 'Др': 2}
per = Counter(r['ref'] for r in net)
for ref in sorted(Nn):
    k = 'Пр' if ref.startswith('Пр') else 'Др' if ref.startswith('Др') else ref[0]
    exp = {'R9': 3, 'R36': 3, 'Д31': 3, 'Др1': 4, 'Др2': 4, 'Др3': 4, 'Тр1': 7, 'Тр2': 8, 'Ш1': 35}.get(ref, want.get(k))
    if per[ref] != exp: print('  pin count', ref, per[ref], '!=', exp)

f = lambda x, d=2: f'{x:.{d}f}'.replace('.', ',')
print('\n--- giá trị danh định ---')
# chuỗi tham chiếu +5 В
VZ1, VZ2 = 13.0, 9.0                          # Д814Д 11,5…14 В; Д818Д 9 В
I6 = (27 - VZ1) / 680; print('I(R6)=', f(I6 * 1e3, 1), 'мА; P(R6)=', f((27 - VZ1) ** 2 / 680), 'Вт (định mức 1 Вт)')
I7 = (VZ1 - VZ2) / 270; print('I(R7)=', f(I7 * 1e3, 1), 'мА')
print('dải con trượt R9: 0 …', f(VZ2 * 6.8 / (1.2 + 6.8)), 'В; vị trí cho 5,00 В =', f(5 / VZ2 * 8.0, 2), 'кОм từ đáy (', f(5 / VZ2 * 8.0 / 6.8 * 100, 0), '%)')
# crowbar
k = 47 / (2 + 47)
for vz, vgt in [(4.7, 0.7), (4.7, 1.0), (4.23, 0.6), (5.17, 1.0)]:
    print(f'OVP: Д32={f(vz)} В, Uу={f(vgt,1)} В -> trip +5 В ≈', f((vz + vgt) / k), 'В')
print('tải mồi R32+R33: I=', f(5 / 49 * 1e3, 0), 'мА; P(R33)=', f((5 * k) ** 2 / 47), 'Вт')
print('R3+R4 =', f(3.2, 1), 'Ом (collector T4)')
# −6,3 В
v18 = 9 * 3.3 / (5.6 + 3.3); print('ref T18 (trên шина M) =', f(v18, 3), 'В')
print('|U| min (R36 trượt hết) =', f(v18 * 3.4 / 2.2), 'В; R36(dưới) cho 6,3 В =', f(v18 * 3.4 / 6.3, 2), 'кОм')
I44 = (27 - (-6.3) - 9) / 3300; print('I(R44) nếu шина M≈−6,3 В:', f(I44 * 1e3, 1), 'мА; P=', f(I44 ** 2 * 3300), 'Вт')
# đa hài T16/T19
t1, t2 = log(2) * 47e3 * 680e-12, log(2) * 120e3 * 1200e-12
print('đa hài: t1=', f(t1 * 1e6, 1), 'мкс, t2=', f(t2 * 1e6, 1), 'мкс, f≈', f(1 / (t1 + t2) / 1e3, 1), 'кГц (ước lượng 0,69RC)')
# tải giả / dòng vào
for frac in (0.25, 0.5, 1.0):
    I = 15 * frac; R = 5 / I; print(f'tải +5 В {int(frac*100)} %: R=', f(R), 'Ом, I=', f(I), 'А, P=', f(5 * I, 1), 'Вт')
for eta in (0.65, 0.75):
    print(f'I vào 27 В ở đầy tải (75+6,3 Вт), η={f(eta)}:', f((75 + 6.3) / eta / 27), 'А')
print('25 % tải (18,75 Вт), η=0,65:', f(18.75 / 0.65 / 27), 'А')
print('tỉ số Тр1 36/5 =', f(36 / 5, 1))
