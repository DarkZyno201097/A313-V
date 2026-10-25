"""Sinh ric18_bom.csv, ric18_conn.csv, ric18_net.csv cho рис.18 — Y10 «Усилители выходные» (ЕУ2.032.463 Э3, 1 tờ).
Nguồn: sơ đồ A313-3_CONTROL/Y10/RE_tr206_a208.jpg (nét hơn ảnh chụp lại 1792807477591_…jpg — dùng ảnh sau để đối chiếu);
ПЭ: ЕУ.048.002.РЭ(A313-3)/RE_tr207_a209.jpg, RE_tr208_a210.jpg. Người chép: Claude, 2026-10-25.

Chạy từ gốc repo:  python tmp/pdfs/review/a313-3/e3/ric18_gen.py tmp/pdfs/review/a313-3/e3
"""
import csv
import sys
from collections import Counter
from pathlib import Path

E3 = Path(sys.argv[1])
SRC = 'a208'

# ---------- ПЭ (a209 tr.207, a210 tr.208) ----------
R10K1 = 'С2-23-0,125-10кОм±1% Б-В'
BOM = [(f'R{i}', R10K1, 207, 'ПЭ: R4…R19, 16 шт.') for i in range(4, 20)]
BOM += [('R20', 'С2-23-0,125-2,61кОм±1% Б', 207, ''), ('R21', 'С2-23-0,125-301Ом±1% Б', 207, ''),
        ('R22', 'С2-23-0,125-10,5кОм±1% Б', 207, ''), ('R23', 'С2-23-0,125-301Ом±1% Б-В', 207, ''),
        ('R24', 'С2-23-0,125-2,05кОм±1% Б', 207, 'ПЭ ghi rõ kΩ — đối chiếu A313-V.06 §9.1'),
        ('R25', 'С2-23-0,125-301Ом±1% Б', 207, ''), ('R26', 'С2-23-0,125-4,7кОм±10% Б-Д', 207, ''),
        ('R27', 'С2-23-0,125-56Ом±10% Б-Д', 207, ''), ('R28', 'С2-23-0,125-10,5кОм±1% Б-В', 207, ''),
        ('R29', 'С2-23-0,125-301Ом±1% Б-В', 207, ''), ('R30', 'С2-23-0,125-4,7кОм±10% Б-Д', 207, ''),
        ('R31', 'С2-23-0,125-56Ом±10% Б-Д', 207, ''), ('R32', 'С2-23-0,125-10кОм±10% Б-Д', 207, ''),
        ('R33', 'С2-23-0,125-10кОм±10% Б-Д', 207, ''), ('R34', 'С2-23-0,125-1,8кОм±10% Б-Д', 207, ''),
        ('R35', 'С2-23-0,125-10кОм±10% Б-Д', 207, ''), ('R36', 'С2-23-0,125-10кОм±10% Б-Д', 207, '')]
BOM += [(c, 'КМ-46-Н30-3300пФ+50-20%-В ОЖ0.460.043 ТУ', 207, '') for c in ('C3', 'C4')]
BOM += [(c, 'К52-1-16В-22мкФ±20% ОЖ0.464.039 ТУ', 207, '') for c in ('C5', 'C6')]
BOM += [(f'C{i}', 'КМ-46-Н30-3300пФ+50-20%-В ОЖ0.460.043 ТУ', 207, 'ПЭ: C7…C13, 7 шт.') for i in range(7, 14)]
BOM += [(f'C{i}', '?', '', '? có trên Э3 (a208, khối «Общий провод», ký hiệu có cực), KHÔNG có trong ПЭ tr.207–208')
        for i in (14, 15, 16)]
BOM += [(f'У{i}', '168КТ2Б ИИ0.308.029 ТУ', 208, '') for i in range(1, 13)]
BOM += [(f'У{i}', '140УД1Б БК0.347.004 ТУ1', 208, '') for i in (14, 15)]
BOM += [(f'У{i}', '168КТ2В ИИ0.308.029 ТУ', 208, '') for i in (16, 17, 18)]
BOM += [(f'У{i}', '302НР3 ОЖ0.345.003 ТУ', 208, 'mạng điện trở') for i in (19, 20)]
CELL = ('Ячейка усилителя (ПЭ vị trí R1…R16): R1 56Ом±10%, R2 0,25-180Ом±10%, R3 4,7кОм±5%, '
        'C1* КМ-5б-Н30-3300пФ (sửa tay «6800 пФ, Дополнение I»), C2 КМ-5б-М75-68пФ, T1 2Т312Б, T2 2Т203Б, У13 140УД1Б')
BOM += [(f'УМ{i}', CELL, 208, f'ПЭ ghi vị trí R{i}') for i in range(1, 17)]
refs = [r for r, *_ in BOM]
assert len(refs) == len(set(refs)) == 16 + 17 + 2 + 2 + 7 + 3 + 12 + 2 + 3 + 2 + 16

# ---------- Bảng đầu nối П1 (a208, góc phải) ----------
P1 = {1: '-12,6В', 28: 'Вх.13', 2: 'Вх.14', 29: 'Вх.10', 3: 'Вх.12', 30: 'Вх.15', 4: 'Вых.13', 31: 'Вых.9',
      5: 'Вых.14', 32: 'Вых.10', 6: 'Вых.15', 33: 'Вых.11', 7: 'Вых.12', 34: 'М', 8: '~5В400Гц', 35: 'Вх.16',
      9: '', 36: '', 10: '', 37: 'Вх.9', 11: '', 38: '+3,5В', 12: '', 39: 'Вх.1', 13: 'П400Гц', 40: 'Вх.11',
      14: '', 41: '~М', 15: 'Вых.16', 42: '+6,3В', 16: '', 43: 'Вых.4', 17: 'Вых.8', 44: 'Вых.3', 18: 'Вых.7',
      45: 'Вых.2', 19: 'Вых.6', 46: 'Вых.1', 20: 'Вых.5', 47: '', 21: '-23В', 48: 'Корпус', 22: '', 49: '+12,6В',
      23: '', 50: 'Вх.4', 24: 'Вх.8', 51: 'Вх.3', 25: 'Вх.7', 52: 'Вх.2', 26: 'Вх.6', 53: 'Вх.5', 27: 'Общий провод'}
NOTE = {('П1', 41): 'М có gạch trên (đảo), ghi «~М»', ('П1', 13): 'ký hiệu xung vuông «⎍400Гц»'}
assert set(P1) == set(range(1, 54))
with open(E3 / 'ric18_conn.csv', 'w', newline='', encoding='utf8') as f:
    w = csv.writer(f); w.writerow(['table', 'pin', 'signal', 'photo', 'note'])
    for p in sorted(P1):
        w.writerow(['П1', p, P1[p], SRC, NOTE.get(('П1', p), '')])
C = lambda p: f'П1:{p} {P1[p]}'  # tên net đầu nối

NET = []


def add(ref, pins, net, note=''):
    for p in (pins if isinstance(pins, (list, tuple)) else [pins]):
        NET.append((ref, str(p), net, (SRC + '; ' + note) if note else SRC))


GND = 'ĐẤT ⊥'
GQ = '? ký hiệu đất (vạch đậm) không ghi tên — chưa rõ «Общий провод» П1/27 hay «Корпус» П1/48'

# ---------- 16 kênh: khoá song song (shunt, gate М) + khoá nối tiếp 2 section (gate ~М) + R tải + mạng 302НР3 + УМ ----------
# (kênh, shunt (vỏ, S, đất, gate), series (vỏ, R, Vin, Vin, S, g1, g2), R, mạng (vỏ, Vin, −, ra), Вх chân, Вых chân)
CH = [
    (1, ('У1', 3, 1, 2), ('У2', 1, 3, 5, 7, 2, 6), 'R4', ('У19', 28, 1, 26), 39, 46),
    (2, ('У1', 7, 5, 6), ('У2', 8, 10, 12, 14, 9, 13), 'R5', ('У19', 24, 5, 22), 52, 45),
    (3, ('У1', 10, 8, 9), ('У3', 1, 3, 5, 7, 2, 6), 'R6', ('У19', 21, 6, 25), 51, 44),
    (4, ('У1', 14, 12, 13), ('У3', 8, 10, 12, 14, 9, 13), 'R7', ('У19', 18, 13, 16), 50, 43),
    (5, ('У4', 3, 1, 2), ('У5', 8, 10, 12, 14, 9, 13), 'R8', ('У20', 28, 1, 26), 53, 20),
    (6, ('У4', 7, 5, 6), ('У5', 1, 3, 5, 7, 2, 6), 'R9', ('У20', 24, 5, 22), 26, 19),
    (7, ('У4', 10, 8, 9), ('У6', 1, 3, 5, 7, 2, 6), 'R10', ('У20', 25, 6, 23), 25, 18),
    (8, ('У4', 14, 12, 13), ('У6', 8, 10, 12, 14, 9, 13), 'R11', ('У20', 18, 13, 16), 24, 17),
    (9, ('У7', 3, 1, 2), ('У9', 1, 3, 5, 7, 2, 6), 'R12', ('У19', 4, 27, 2), 37, 31),
    (10, ('У7', 7, 5, 6), ('У8', 1, 3, 5, 7, 2, 6), 'R13', ('У19', 10, 19, 8), 29, 32),
    (11, ('У7', 10, 8, 9), ('У9', 8, 10, 12, 14, 9, 13), 'R14', ('У19', 11, 20, 9), 40, 33),
    (12, ('У7', 14, 12, 13), ('У8', 8, 10, 12, 14, 9, 13), 'R15', ('У19', 14, 15, 12), 3, 7),
    (13, ('У10', 3, 1, 2), ('У11', 1, 3, 5, 7, 2, 6), 'R16', ('У20', 4, 27, 2), 28, 4),
    (14, ('У10', 7, 5, 6), ('У11', 8, 10, 12, 14, 9, 13), 'R17', ('У20', 10, 19, 8), 2, 5),
    (15, ('У10', 10, 8, 9), ('У12', 1, 3, 5, 7, 2, 6), 'R18', ('У20', 11, 20, 9), 30, 6),
    (16, ('У10', 14, 12, 13), ('У12', 8, 10, 12, 14, 9, 13), 'R19', ('У20', 14, 15, 12), 35, 15),
]
QPIN = {(14, 'shunt_gnd'): 'số chân đọc giống «3», theo quy luật section 2 của 168КТ2 là 5',
        (3, 'net_vin'): 'số chân đọc «71»/«21» — chọn 21 theo quy luật mạng 302НР3',
        (12, 'series'): 'nhãn vỏ đọc «Уg.2»; У9.2 đã dùng ở kênh 11 ⇒ У8.2'}
for n, (sh, sS, sG, sg), (se, rR, v1, v2, sS2, g1, g2), R, (nw, nV, nM, nO), vx, vy in CH:
    S, VIN, MID, OUT, RN = f'S{n}', C(vx), f'NM{n}', C(vy), f'RT{n}'
    add(sh, sS, S, f'kênh {n}: khoá song song, kéo S{n} xuống đất'); add(sh, sG, GND, GQ)
    add(sh, sg, C(34), f'kênh {n}: gate = М' + ('; ? ' + QPIN[(n, 'shunt_gnd')] if (n, 'shunt_gnd') in QPIN else ''))
    sq = ('; ? ' + QPIN[(n, 'series')]) if (n, 'series') in QPIN else ''
    add(se, rR, RN, f'kênh {n}: section nối Vin → R tải' + sq); add(se, [v1, v2], VIN, f'kênh {n}' + sq)
    add(se, sS2, S, f'kênh {n}: section nối Vin → S' + sq); add(se, [g1, g2], C(41), f'kênh {n}: gate = ~М' + sq)
    add(R, 1, GND, GQ); add(R, 2, RN, f'kênh {n}: R tải 10 kΩ')
    nq = ('; ? ' + QPIN[(n, 'net_vin')]) if (n, 'net_vin') in QPIN else ''
    add(nw, nV, VIN, f'kênh {n}: mạng 302НР3 đầu Vin' + nq); add(nw, nM, MID, f'kênh {n}: điểm giữa → УМ(−)')
    add(nw, nO, OUT, f'kênh {n}: đầu hồi tiếp từ ra')
    U = f'УМ{n}'
    add(U, 1, MID, 'УМ chân 1 = vào đảo (У13.9)'); add(U, 2, S, 'УМ chân 2 = vào không đảo qua R3 (У13.10)')
    add(U, 3, OUT, 'УМ chân 3 = ra (sau R2 180 Ω)')
    add(U, 'V+', C(49), 'ô УМ: collector T1 → П1/49 +12,6 В (hình ô mẫu)')
    add(U, 'V-', C(1), 'ô УМ: collector T2 → П1/1 −12,6 В (hình ô mẫu)')

# ---------- Khối tạo M / ~M / xung 400 Hz (giống A313-V.06 U14…U18) ----------
add('R20', 1, C(8), 'chuẩn ~5 В 400 Гц'); add('R20', 2, 'N1'); add('R21', 2, 'N1'); add('R21', 1, C(48))
add('У14', 9, 'N1', 'vào đảo = phân áp R20/R21'); add('У14', 10, 'N2', 'vào không đảo = trễ từ У16.1')
add('У14', 5, 'N3'); add('R26', 1, 'N3'); add('R26', 2, 'N4'); add('У17', 2, 'N4', 'gate У17.1')
add('У14', 12, 'N5', 'chân hiệu chỉnh'); add('R27', 1, 'N5'); add('R27', 2, 'N6'); add('C3', 2, 'N6'); add('C3', 1, GND, GQ)
add('R24', 1, C(8), 'chuẩn ~5 В 400 Гц'); add('R24', 2, 'N7'); add('R25', 2, 'N7'); add('R25', 1, C(48))
add('У15', 9, 'N7', 'vào đảo = phân áp R24/R25'); add('У15', 10, 'N8', 'vào không đảo = trễ từ У16.2')
add('У15', 5, 'N9'); add('R30', 1, 'N9'); add('R30', 2, 'N10'); add('У18', 2, 'N10', 'gate У18.1')
add('У15', 12, 'N11', 'chân hiệu chỉnh'); add('R31', 1, 'N11'); add('R31', 2, 'N12'); add('C4', 2, 'N12'); add('C4', 1, GND, GQ)
add('R22', 1, C(1)); add('R22', 2, 'HTRE-', 'ngưỡng −h'); add('R23', 2, 'HTRE-'); add('R23', 1, C(48))
add('R28', 2, C(49)); add('R28', 1, 'HTRE+', 'ngưỡng +h'); add('R29', 1, 'HTRE+'); add('R29', 2, C(48))
add('У16', 1, 'HTRE-'); add('У16', [3, 5], 'N2'); add('У16', 7, 'HTRE+'); add('У16', 2, 'B', 'gate, dây chéo X')
add('У16', 6, 'A', 'gate, dây chéo X'); add('У16', 8, 'HTRE-'); add('У16', [10, 12], 'N8'); add('У16', 14, 'HTRE+')
add('У16', 9, 'A', 'gate, dây chéo X'); add('У16', 13, 'B', 'gate, dây chéo X')
add('У17', 3, 'A', 'У17.1 kéo A'); add('У17', 1, C(38)); add('R32', 1, C(21)); add('R32', 2, 'A')
add('У17', 13, 'A', 'gate У17.4'); add('У17', 12, 'B'); add('У17', 14, C(38)); add('R33', 1, C(21)); add('R33', 2, 'B')
add('R34', 1, C(38)); add('R34', 2, C(13), 'kéo lên xung 400 Hz')
add('У17', 9, 'A', 'gate У17.3'); add('У17', 10, C(13)); add('У17', 8, C(48))
add('У17', 6, 'A', 'gate У17.2'); add('У17', 5, C(13)); add('У17', 7, C(48))
add('У18', 1, C(34), 'У18.1 kéo М'); add('У18', 3, C(38)); add('R35', 1, C(21)); add('R35', 2, C(34))
add('У18', 13, C(34), 'gate У18.2'); add('У18', 14, C(41)); add('У18', 12, C(38)); add('R36', 1, C(21)); add('R36', 2, C(41))

# ---------- Tụ nguồn (khối «Общий провод») ----------
for c, a, b, q in (('C5', C(27), C(1), '? chân 1 (+) đi lên qua dây +12,6 В không thấy chấm nối — lấy «Общий провод»'),
                   ('C7', C(27), C(49), ''), ('C8', C(49), C(1), '? chấm nối chân 1 có thể chỉ của C7'),
                   ('C9', C(1), C(48), ''), ('C10', C(27), C(49), ''), ('C11', C(27), C(49), ''),
                   ('C12', C(49), C(48), ''), ('C13', C(27), C(49), ''), ('C14', C(49), C(48), 'chân 1 (+)')):
    add(c, 1, a, q); add(c, 2, b, q)
add('C6', '−', C(1)); add('C6', '+', C(48))
add('C15', '−', C(27)); add('C15', '+', C(49))
add('C16', '+', C(49)); add('C16', '−', C(48))

# ---------- Ghi chú 1 trên Э3 ----------
for u in ('У14', 'У15'):
    add(u, 4, C(27), 'ghi chú 1: chân 4 → «общий провод»'); add(u, 1, C(1), 'ghi chú 1: chân 1 → −12,6 В')
    add(u, 7, C(49), 'ghi chú 1: chân 7 → +12,6 В')
for i in range(1, 13):
    add(f'У{i}', 11, C(42), 'ghi chú 1: chân 11 (подложка) → +6,3 В')
for i in (16, 17, 18):
    add(f'У{i}', 11, C(38), 'ghi chú 1: chân 11 (подложка) → +3,5 В')

keys = [(r, p) for r, p, *_ in NET]
dup = [k for k, v in Counter(keys).items() if v > 1]
assert not dup, dup
cnt = Counter(n for _, _, n, _ in NET)
single = [n for n, v in cnt.items() if n.startswith('N') and n[1:].isdigit() and v < 2]
assert not single, single
assert set(r for r, *_ in NET) == set(refs), set(refs) ^ set(r for r, *_ in NET)
with open(E3 / 'ric18_bom.csv', 'w', newline='', encoding='utf8') as f:
    w = csv.writer(f); w.writerow(['ref', 'name', 'qty', 'page', 'note'])
    for r, n, pg, nt in BOM:
        w.writerow([r, n, 1, pg, nt])
with open(E3 / 'ric18_net.csv', 'w', newline='', encoding='utf8') as f:
    w = csv.writer(f); w.writerow(['ref', 'pin', 'net', 'note']); w.writerows(NET)
print('bom', len(BOM), 'conn 53 net', len(NET))
