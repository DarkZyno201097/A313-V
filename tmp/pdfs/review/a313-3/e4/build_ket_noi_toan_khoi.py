# -*- coding: utf-8 -*-
"""
Build ket_noi_chung workbook (vong 1) cho A-313-3, theo PLAN_KET-NOI-TOAN-KHOI_A-313-3.md.

Chay tu goc repo:
    C:/Python314/python.exe tmp/pdfs/review/a313-3/e4/build_ket_noi_toan_khoi.py

Nguon: e4_all.csv (2877 dong, 58 bang, tr.142-152) + matrix_nets.csv (282 net, tr.153-157).
Tai su dung nguyen ham key/parse_addr/addrs/resolve tu e4_check.py (khong viet lai logic).
"""
import csv
import sys
from pathlib import Path
from collections import defaultdict, Counter

HERE = Path(__file__).resolve().parent          # .../a313-3/e4
A313_3_DIR = HERE.parent                         # .../a313-3
sys.path.insert(0, str(A313_3_DIR))
import e4_check as ec                             # noqa: E402  (key, parse_addr, addrs, resolve)

E4_ALL = HERE / 'e4_all.csv'
MATRIX_NETS = HERE / 'matrix_nets.csv'
MISMATCH = HERE / 'e4_mismatch.csv'

# Пn (tr.153-157, ma tran noi bo Y16) <-> ten tam, theo matrix_notes.md §1.
# P1/P2/P3 la "bo day / dau cam khoi" (ben ngoai), khong gan tam cu the.
PN_TO_BOARD = {
    4: 'Y10', 5: 'Y9', 7: 'Y11', 8: 'Y6', 9: 'Y2',
    10: 'Y7', 11: 'Y3', 12: 'Y8', 13: 'Y4', 15: 'Y5',
}
EXTERNAL_TABLES = {'3Ш1', '3Ш2', '3Ш3', '3Ш3В', '3Ш4', '3Ш4В', '3Ш7', '3Ш5'}


# ---------- Union-Find ----------
class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def load_e4_all():
    rows = []
    with open(E4_ALL, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            p = ec.key(r['pin'])
            if not (p.isdigit() or p in ('А', 'Б')):
                continue
            r['T'], r['P'] = ec.key(r['table']), ec.pin(p)
            rows.append(r)
    return rows


def board_column_for(t_raw, t_norm, p):
    """
    Quyet dinh cot dich + gia tri o cho mot (table, pin) cu the, theo PLAN §2
    phuong an 1 (moi TAM la mot cot, dau cam ngoai giu rieng).
    Tra ve (ten_cot, gia_tri_o, can_xac_minh:bool).
    """
    if t_norm in EXTERNAL_TABLES:
        return t_norm, str(p), False
    # У16КПn -> khong lam cot rieng, suy ra tam qua PN_TO_BOARD neu co
    if t_norm.startswith('У16КП'):
        try:
            n = int(t_norm.replace('У16КП', ''))
        except ValueError:
            return f'?{t_raw}', str(p), True
        board = PN_TO_BOARD.get(n)
        if board:
            return board, f'КП{n}/{p}', False
        # КП1/КП2/КП3: KHÔNG phải lỗi — theo matrix_notes.md §1, đây là "bó dây/đầu cắm khối",
        # không gắn tên tấm cụ thể trên bản vẽ gốc. Giữ cột riêng, không gắn cờ CẦN XÁC MINH.
        return f'Y16-КП{n} (bó dây/đầu cắm khối)', str(p), False
    # Bảng dac biet da xac dinh duoc tam qua tieu de rieng (vd "?П1(Интеграторы)" = Y9's own П1)
    if 'Интеграторы' in t_raw:
        return 'Y9', f'П1/{p}', False
    # УnП<k> -> cot Y<n>, gia tri "Пk/chan"
    import re
    m = re.fullmatch(r'У(\d+)П(\d+)', t_norm)
    if m:
        n, k = m.group(1), m.group(2)
        return f'Y{n}', f'П{k}/{p}', False
    # Уn thuan (khong chia П1/П2/П3): У12,У13,У18..У24
    m = re.fullmatch(r'У(\d+)', t_norm)
    if m:
        return f'Y{m.group(1)}', str(p), False
    # Con lai: bang dac biet/nghi van (У173Ш5, ?3Ш5-жгут..., ?П1(Интеграторы)...)
    if t_norm.startswith('3Ш5') or '3Ш5' in t_raw:
        return '3Ш5', str(p), True
    return f'?{t_raw}', str(p), True


def main():
    rows = load_e4_all()
    idx = defaultdict(list)
    for r in rows:
        idx[(r['T'], r['P'])].append(r)
    tables = {r['T'] for r in rows}

    uf = UF()
    for key_ in idx:
        uf.find(key_)  # dam bao moi node ton tai truoc khi union

    reciprocal = set()  # (T,P) ma it nhat 1 tham chieu duoc xac nhan hai chieu
    oneway_rows = []     # (T,P,address_text) chi co tham chieu mot chieu

    struck_pat = __import__('re').compile(r'зач[её]ркн|gạch (bỏ|xoá|xóa)|struck|crossed', __import__('re').I)
    struck_rows = []
    missing_target_rows = []  # dia chi tro toi bang CHUA duoc chep (thieu trang/component roi rac)
    for r in rows:
        if r.get('note') and struck_pat.search(r['note']):
            struck_rows.append((r['T'], r['P'], r['signal'], r['page']))
            continue
        src = (r['T'], r['P'])
        has_recip = False
        for t, k in ec.addrs(r['address']):
            a = (ec.resolve(t, tables), k)
            if a[0] not in tables:
                missing_target_rows.append((r['T'], r['P'], r['signal'], f'{a[0]}/{k}', r['page']))
                continue
            uf.union(src, a)
            back = [(ec.resolve(t2, tables), k2) for x in idx.get(a, []) for t2, k2 in ec.addrs(x['address'])]
            if src in back:
                has_recip = True
                reciprocal.add(src)
        if r['address'] and not has_recip:
            oneway_rows.append((r['T'], r['P'], r['signal'], r['address'], r['page']))

    qmark_rows = [(r['T'], r['P'], r['signal'], r['note'], r['page'])
                  for r in rows if r.get('note') and '?' in r['note']]

    # --- Hop nhat them tu matrix_nets.csv (tr.153-157, da ghep san) ---
    matrix_notes_rows = []
    if MATRIX_NETS.is_file():
        with open(MATRIX_NETS, encoding='utf-8') as f:
            for row in csv.DictReader(f):
                members = [m.strip() for m in row['members'].split(';') if m.strip()]
                keys_in_net = []
                for m in members:
                    try:
                        pn_str, chan = m.split('/')
                        n = int(pn_str.replace('П', ''))
                    except ValueError:
                        continue
                    k = ('У16КП%d' % n, ec.pin(chan))
                    keys_in_net.append(k)
                    matrix_notes_rows.append((row['net'], m, row.get('note', '')))
                for i in range(1, len(keys_in_net)):
                    uf.union(keys_in_net[0], keys_in_net[i])

    # --- Gom net ---
    nets = defaultdict(list)
    for key_ in uf.p:
        nets[uf.find(key_)].append(key_)

    # --- Dung bang ket_noi_chung ---
    out_rows = []          # moi phan tu: dict cot -> gia tri, + 'Tín hiệu', '_recip', '_flag'
    all_columns = set()
    flagged_tables = Counter()

    for root, members in nets.items():
        signal_votes = Counter()
        cells = {}
        any_recip = False
        needs_review = False
        for (t, p) in members:
            for r in idx.get((t, p), []):
                signal_votes[r['signal'].strip()] += 1
            if (t, p) in reciprocal:
                any_recip = True
            col, val, flag = board_column_for(idx.get((t, p), [{'table': t}])[0]['table'], t, p)
            cells.setdefault(col, []).append(val)
            all_columns.add(col)
            if flag:
                needs_review = True
                flagged_tables[col] += 1
        if not signal_votes:
            continue
        signal = signal_votes.most_common(1)[0][0]
        row_dict = {'Tín hiệu': signal}
        for col, vals in cells.items():
            row_dict[col] = ';'.join(sorted(set(vals)))
        row_dict['_recip'] = 'Hai chiều' if any_recip else 'Một chiều/chưa xác nhận'
        row_dict['_review'] = 'CẦN XÁC MINH' if needs_review else ''
        row_dict['_nmembers'] = len(members)
        out_rows.append(row_dict)

    EXT_COL_ORDER = ['3Ш1', '3Ш2', '3Ш3', '3Ш3В', '3Ш4', '3Ш4В', '3Ш5', '3Ш7']
    board_cols = sorted(
        [c for c in all_columns if c.startswith('Y') and c[1:].isdigit()],
        key=lambda c: int(c[1:]))
    special_cols = sorted(c for c in all_columns if c not in EXT_COL_ORDER and c not in board_cols)
    columns = ['Tín hiệu'] + [c for c in EXT_COL_ORDER if c in all_columns] + board_cols + special_cols

    print('=== THONG KE VONG 1 ===')
    print('Dong e4_all.csv dung:', len(rows), '| bang:', len(tables))
    print('So net (dong trong ket_noi_chung):', len(out_rows))
    print('So cot (tam + dau cam ngoai + dac biet):', len(columns) - 1)
    print('  - cot ngoai:', [c for c in EXT_COL_ORDER if c in all_columns])
    print('  - cot tam:', board_cols)
    print('  - cot dac biet/can xac minh:', special_cols)
    print('So dong mot chieu (can_doi_chieu):', len(oneway_rows))
    print('So net can xac minh them:', sum(1 for r in out_rows if r['_review']))
    print('So dong trong matrix_nets.csv da hop nhat:', len(matrix_notes_rows))

    data = {
        'columns': columns,
        'out_rows': out_rows,
        'oneway_rows': oneway_rows,
        'tables': tables,
        'rows_total': len(rows),
        'ntables': len(tables),
        'nmatrix': len(matrix_notes_rows),
        'board_cols': board_cols,
        'ext_cols': [c for c in EXT_COL_ORDER if c in all_columns],
        'special_cols': special_cols,
        'struck_rows': struck_rows,
        'missing_target_rows': missing_target_rows,
        'qmark_rows': qmark_rows,
    }
    export_workbook(data)
    return data


# ===================== XUAT EXCEL =====================

PHAN_BIEN_DOI_SO = 'Phần biến đổi số'
PHAN_BIEN_DOI_SO_TUONG_TU = 'Phần biến đổi số–tương tự'
PHAN_NGUON_VA_KHUNG = 'Phần nguồn và khung'
PHAN_DAU_CAM_NGOAI = 'Đầu cắm ngoài khối (không thuộc 3 phần)'

KY_HIEU_CHUNG = [
    # (Cot, Ten tam/dau cam (Nga), Ma ky hieu, Chuc nang, Phan, Ghi chu)
    ('Y1', 'Формирователь ПК и магистрали', 'ЕУ2.035.587',
     'Bộ tạo ПК (lệnh đơn) và BUS chính', PHAN_BIEN_DOI_SO, ''),
    ('Y2', 'Преобразователь цифровых сигналов', 'ВШ3.036.056',
     'Bộ biến đổi tín hiệu số (tần số/cự ly → mã)', PHAN_BIEN_DOI_SO, ''),
    ('Y3', 'Устройство управления обращением', 'ЕУ3.057.136',
     'Bộ điều khiển giao tiếp', PHAN_BIEN_DOI_SO, ''),
    ('Y4', 'Устройство программного управления', 'ЕУ3.057.138',
     'Bộ điều khiển chương trình (СчК, ГТИ)', PHAN_BIEN_DOI_SO, ''),
    ('Y5', 'Устройство командного управления', 'ЕУ3.057.139',
     'Bộ điều khiển lệnh (РгК1/2, РгПр, РРК1/2)', PHAN_BIEN_DOI_SO, ''),
    ('Y6', 'Устройство управления преобразованием', 'ЕУ3.057.140',
     'Bộ điều khiển biến đổi (РПР 16 bit, РМ)', PHAN_BIEN_DOI_SO, ''),
    ('Y7', 'Плата согласования', 'ВШ3.031.020',
     'Tấm mạch phối hợp', PHAN_BIEN_DOI_SO, ''),
    ('Y8', 'Преобразователь', 'ЕУ3.036.157',
     'Bộ biến đổi', PHAN_BIEN_DOI_SO_TUONG_TU, ''),
    ('Y9', 'Интеграторы', 'ЕУ3.072.043',
     'Các bộ tích phân (gồm tầng mux K)', PHAN_BIEN_DOI_SO_TUONG_TU,
     'Bảng П1 riêng (tiêu đề "Интеграторы") không có cột address nên không tự ghép được với dữ liệu phía КП5 — cùng cột Y9 nhưng là 2 nguồn dữ liệu độc lập, cần đối chiếu'),
    ('Y10', 'Усилители выходные', 'ЕУ2.032.463',
     'Các bộ khuếch đại cửa ra (16 kênh, điều chế 400 Hz)', PHAN_BIEN_DOI_SO_TUONG_TU, ''),
    ('Y11', 'Коммутатор выходной', 'ЕУ2.242.113',
     'Bộ chuyển mạch cửa ra (АЗУ 49 ô)', PHAN_BIEN_DOI_SO_TUONG_TU, ''),
    ('Y12', 'Коммутатор входной', 'ЕУ3.628.122',
     'Bộ chuyển mạch cửa vào (1)', PHAN_BIEN_DOI_SO_TUONG_TU, '⚠ kế hoạch cũ ghi .121, đã đảo với Y13'),
    ('Y13', 'Коммутатор входной', 'ЕУ3.628.121',
     'Bộ chuyển mạch cửa vào (2)', PHAN_BIEN_DOI_SO_TUONG_TU, ''),
    ('Y14', 'Преобразователь РК II (⚠ mâu thuẫn, xem canh_bao_quan_trong)', 'ВШ3.036.053',
     'Bộ biến đổi lệnh đơn PK I (ra 27V) — ⚠ xem mâu thuẫn', PHAN_BIEN_DOI_SO, '⚠ MÂU THUẪN với Y15'),
    ('Y15', 'Преобразователь РК I (⚠ mâu thuẫn, xem canh_bao_quan_trong)', 'ВШ2.068.054',
     'Bộ biến đổi lệnh đơn PK II (ra chập mát) — ⚠ xem mâu thuẫn', PHAN_BIEN_DOI_SO, '⚠ MÂU THUẪN với Y14'),
    ('Y16', 'Плата коммутационная — TẤM SƯỜN, không có linh kiện', 'ЕУ3.661.064',
     'Tấm sườn/backplane — nối mọi tấm, ra đầu cắm (không có linh kiện)', PHAN_NGUON_VA_KHUNG,
     'Trong bảng kết nối này: không có cột riêng, thể hiện qua Пn trong các tấm khác. '
     'NHƯNG Y16 CÓ Э3 riêng (ma trận cross-reference 5 лист, xác nhận khung tên, sửa lần 2 '
     '2026-10-24) — xem A313-3_CONTROL/Y16/, không liên quan tới bảng kết nối toàn khối này.'),
    ('Y17', 'УЛП 5 В 15 А', 'ЕУ3.215.469',
     'Ổn áp nguồn +5V/15A (tháo được)', PHAN_NGUON_VA_KHUNG, 'Đầu nối ra 3Ш5 gộp vào cột 3Ш5'),
    ('Y18', 'УЛП +20 В 0,3 А', 'ЕУ3.215.446',
     'Ổn áp nguồn +20V/0,3A', PHAN_NGUON_VA_KHUNG, ''),
    ('Y19', 'УЛП +12,6 В 1 А', 'ЕУ3.215.452',
     'Ổn áp nguồn +12,6V/1A', PHAN_NGUON_VA_KHUNG, ''),
    ('Y20', 'УЛП +6,3 В 0,5 А', 'ЕУ3.215.448-01',
     'Ổn áp nguồn +6,3V/0,5A', PHAN_NGUON_VA_KHUNG, ''),
    ('Y21', 'УЛП −20 В 0,25-0,3 А', 'ЕУ3.215.451',
     'Ổn áp nguồn −20V/0,25-0,3A', PHAN_NGUON_VA_KHUNG, '⚠ mâu thuẫn trị số với −23V, xem canh_bao_quan_trong'),
    ('Y22', 'УЛП −12,6 В 1 А', 'ЕУ3.215.470',
     'Ổn áp nguồn −12,6V/1A', PHAN_NGUON_VA_KHUNG, ''),
    ('Y23', 'УЛП ±10 В 0,2 А', 'ЕУ3.215.466',
     'Ổn áp nguồn ±10V/0,2A', PHAN_NGUON_VA_KHUNG, ''),
    ('Y24', 'Плата контроля и сигнализации', 'ЕУ2.072.139',
     'Tấm kiểm tra và báo hiệu', PHAN_NGUON_VA_KHUNG, ''),
    ('3Ш1', 'Đầu cắm ngoài khối', 'Вилка РПКМ3-67/67',
     'Đầu cắm giao tiếp ngoài khối', PHAN_DAU_CAM_NGOAI, ''),
    ('3Ш2', 'Đầu cắm ngoài khối', 'АВ0.364.047ТУ (РС50ТВ)',
     'Đầu cắm giao tiếp ngoài khối', PHAN_DAU_CAM_NGOAI, ''),
    ('3Ш3', 'Đầu cắm ngoài khối', 'АВ0.364.040ТУ (РПКМ3-67/67)',
     'Đầu cắm giao tiếp ngoài khối', PHAN_DAU_CAM_NGOAI, ''),
    ('3Ш3В', 'Đầu cắm ngoài khối (biến thể В)', '',
     'Đầu cắm giao tiếp ngoài khối', PHAN_DAU_CAM_NGOAI, ''),
    ('3Ш4', 'Đầu cắm ngoài khối', 'АВ0.364.040ТУ (РПКМ3-67/67)',
     'Đầu cắm giao tiếp ngoài khối', PHAN_DAU_CAM_NGOAI, ''),
    ('3Ш4В', 'Đầu cắm ngoài khối (biến thể В)', '',
     'Đầu cắm giao tiếp ngoài khối', PHAN_DAU_CAM_NGOAI, ''),
    ('3Ш5', 'Đầu cắm ngoài khối (nguồn 400Hz/У17)', '',
     'Đầu cắm giao tiếp ngoài khối — nguồn 400Hz từ У17', PHAN_DAU_CAM_NGOAI, ''),
    ('3Ш7', 'Đầu cắm ngoài khối', 'АВ0.364.047ТУ (РС50ТВ)',
     'Đầu cắm giao tiếp ngoài khối', PHAN_DAU_CAM_NGOAI, ''),
]

PHAN_COLOR = {
    PHAN_BIEN_DOI_SO: 'BDD7EE',            # xanh duong nhat
    PHAN_BIEN_DOI_SO_TUONG_TU: 'C6E0B4',   # xanh la nhat
    PHAN_NGUON_VA_KHUNG: 'FFE699',         # vang cam nhat
    PHAN_DAU_CAM_NGOAI: 'E2E2E2',          # xam nhat (khong thuoc 3 phan)
}

CANH_BAO_CO_DINH = [
    # (Muc, Noi dung, Nguon)
    ('Y2 (рис.9) mâu thuẫn dấu nguồn tại П1-49/П3-29',
     'Bó dây số 14 giữa П1-49 và П3-29 trên Э3 của Y2 mang 2 nhãn trái dấu trên cùng bản vẽ: '
     '+12,6В và −12,6В. Codex giữ nguyên cả hai nhãn (không tự sửa), gán net riêng. Cần đối chiếu '
     'vật lý hoặc ảnh gốc rõ hơn trước khi dùng. Netlist Y2 (ric09) còn PARTIAL: toàn bộ tên linh '
     'kiện trong BOM ghi "?" (không đọc được mã R/C/IC từ 2 ảnh nguồn). Kiểm chéo Э3↔Э4 (ric09_vs_e4.csv, '
     'Claude tự sửa conn.csv rồi chạy e3_vs_e4.py): 136 chân Э3/141 chân Э4, khớp 85, lệch tên 50 '
     '(phần lớn do dấu "?" thay ký tự chưa chắc hoặc thiếu dấu phủ định ¬ — không phải lỗi thật), '
     'chỉ-Э3 1, chỉ-Э4 6.',
     'tmp/pdfs/review/a313-3/e3/ric09_mota.md + ric09_vs_e4.csv (Codex transcribe + Claude cross-check, 2026-10-23)'),
    ('Y14/Y15 mâu thuẫn danh tính',
     'Danh mục cấp khối tr.142 ghi У14=РК II (ВШ3.036.053), У15=РК I (ВШ2.068.054); nhưng '
     'chính Э4 tr.149 lại ghi dọc cạnh bảng У14 "РК I ВШ2.068.054" — ngược lại. Phải xem nhãn '
     'trên tấm thật để chốt.',
     'SO-DO-DAU-NOI_E4_A-313-3.md §2 (У14,У15)'),
    ('Y21 mâu thuẫn trị số',
     'Kế hoạch ghi −23V theo Bảng 3, nhưng Э4 có cả hai: У16КП1/5 ghi "−23В", 3Ш3В/60 ghi "−20В".',
     'SO-DO-DAU-NOI_E4_A-313-3.md §2 (У21)'),
    ('Y24 mã ký hiệu',
     'Bảng 7 (KE-HOACH gốc) ghi ЕУ3.215.139; danh mục cấp khối Э4 tr.142 + bản vẽ lắp ráp Рис.30 '
     '(tr.244) đều xác nhận ЕУ2.072.139 — dùng mã này.',
     'SO-DO-DAU-NOI_E4_A-313-3.md §2 (У24) + KE-HOACH §1.5'),
    ('Y12/Y13 mã ký hiệu đảo',
     'Kế hoạch cũ ghi Y12=.121/Y13=.122; danh mục cấp khối tr.142 xác nhận NGƯỢC LẠI: '
     'Y12=ЕУ3.628.122, Y13=ЕУ3.628.121.',
     'SO-DO-DAU-NOI_E4_A-313-3.md §2 (У12,У13)'),
    ('Выход 2б ⊓⊔ (ma trận 157-c40) nghi lỗi bản vẽ',
     'Ma trận ghi rõ П3/23, nhưng КП3/23 = СИм (đã dùng ở cột khác); КП3/29 = ВЫХОД 2Б; quy luật '
     'dãy П3 cho thấy gần như chắc chắn đúng là П3/29, bản vẽ gốc ghi nhầm 23.',
     'tmp/pdfs/review/a313-3/e4/matrix_notes.md §3'),
    ('2 net nghi chép sai trong e4 (КП11)',
     'КП11/48 ghi "К⇒РН" (ma trận + КП8/48 ghi "М⇒РМ"); КП11/21 ghi "¬СВНвх" (ma trận + КП3/26 '
     'ghi "СВК БК"). Cần đối chiếu ảnh gốc.',
     'tmp/pdfs/review/a313-3/e4/matrix_notes.md §3'),
    ('2 net khác tên thật giữa hai bảng',
     'КП7/41 "ВХОД а" ↔ КП12/38 "а ПР"; КП7/6 "ВХОД б" ↔ КП12/12 "б ПР" — có thể cùng dây mang '
     'hai tên theo tấm (У11/У8), cần xem sơ đồ nguyên lý để xác nhận có đúng là cùng net không.',
     'tmp/pdfs/review/a313-3/e4/matrix_notes.md §3'),
    ('5 số đọc chưa chắc trong ma trận tr.153-157',
     '153-c27 АИ (П9/45 hay 46→46), 153-c46 РПР⇒М (П11/12 hay 42→42), 154-c05 ¬Зп.ЦВУ '
     '(П11/28 hay 23→28), 154-c13 Зп.КПА (П11/43 nhoè), 154-c54 ¬1t1 (П13/43 hay 45→43). '
     'Đã chốt theo bảng КПn nên KHÔNG phải kiểm chéo độc lập.',
     'tmp/pdfs/review/a313-3/e4/matrix_notes.md §4'),
    ('Cột Y16-КП1/КП2/КП3 — không phải lỗi, là kiến trúc',
     'Theo matrix_notes.md §1, header П1/П2/П3 trên tấm Y16 là "đầu nối ra bó dây/đầu cắm khối" '
     '(КП2 có 94 chân), KHÔNG gắn tên một tấm cụ thể trên bản vẽ gốc — khác với П4…П15 (mỗi cái '
     'gắn đúng 1 tấm). Vì vậy 3 cột này giữ riêng, không gộp vào cột tấm nào. Cần lần dây vật lý '
     'nếu muốn biết chính xác pin nào ra đầu cắm ngoài nào.',
     'tmp/pdfs/review/a313-3/e4/matrix_notes.md §1 (xác nhận vòng 2)'),
]


def export_workbook(data):
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    import datetime

    HDR = PatternFill('solid', fgColor='12304A')
    EVEN = PatternFill('solid', fgColor='DCE6F1')
    ODD = PatternFill('solid', fgColor='FFFFFF')
    WARN = PatternFill('solid', fgColor='FFF2CC')
    thin = Side(style='thin', color='B0B0B0')
    brd = Border(left=thin, right=thin, top=thin, bottom=thin)
    hdr_font = Font(bold=True, color='FFFFFF', size=11)

    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # ---- ky_hieu_chung ----
    ws = wb.create_sheet('ky_hieu_chung')
    ws.append(['Cột', 'Tên tấm/đầu cắm (Nga)', 'Mã ký hiệu', 'Chức năng', 'Phần', 'Ghi chú'])
    for c in range(1, 7):
        cell = ws.cell(row=1, column=c)
        cell.font, cell.fill, cell.border = hdr_font, HDR, brd
    for row in KY_HIEU_CHUNG:
        ws.append(list(row))
    for r in range(2, ws.max_row + 1):
        phan_val = ws.cell(row=r, column=5).value
        fill = PatternFill('solid', fgColor=PHAN_COLOR.get(phan_val, 'FFFFFF'))
        for c in range(1, 7):
            ws.cell(row=r, column=c).border = brd
            ws.cell(row=r, column=c).fill = fill
            ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical='top')
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 46
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 42
    ws.column_dimensions['E'].width = 24
    ws.column_dimensions['F'].width = 50
    ws.freeze_panes = 'A2'
    from openpyxl.worksheet.table import Table as _TblKH, TableStyleInfo as _TSIKH
    tblkh = _TblKH(displayName='KyHieuChung', ref=f'A1:F{ws.max_row}')
    tblkh.tableStyleInfo = _TSIKH(name='TableStyleLight1', showRowStripes=False)
    ws.add_table(tblkh)

    # ---- ket_noi_chung (Table + filter) ----
    ws = wb.create_sheet('ket_noi_chung')
    cols = data['columns'] + ['Số chiều tham chiếu', 'Cần xác minh']
    ws.append(cols)
    for i, row in enumerate(data['out_rows'], start=2):
        ws.append([row.get(c, '') for c in data['columns']] + [row['_recip'], row['_review']])
    n_cols = len(cols)
    n_rows = len(data['out_rows']) + 1
    from openpyxl.worksheet.table import Table, TableStyleInfo
    tbl = Table(displayName='KetNoiA313_3', ref=f'A1:{get_column_letter(n_cols)}{n_rows}')
    tbl.tableStyleInfo = TableStyleInfo(name='TableStyleLight2', showRowStripes=True)
    ws.add_table(tbl)
    for c in range(1, n_cols + 1):
        cell = ws.cell(row=1, column=c)
        cell.font, cell.fill = hdr_font, HDR
    ws.column_dimensions['A'].width = 28
    for c in range(2, n_cols + 1):
        ws.column_dimensions[get_column_letter(c)].width = 14
    ws.freeze_panes = 'B2'

    # ---- chi_tiet_tu_anh ----
    ws = wb.create_sheet('chi_tiet_tu_anh')
    headers = ['page', 'photo', 'table', 'pin', 'signal', 'address', 'wire', 'note']
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    with open(E4_ALL, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            ws.append([r.get(h, '') for h in headers])
    from openpyxl.worksheet.table import Table as _Table, TableStyleInfo as _TSI
    tbl2 = _Table(displayName='ChiTietTuAnh', ref=f'A1:{get_column_letter(len(headers))}{ws.max_row}')
    tbl2.tableStyleInfo = _TSI(name='TableStyleLight2', showRowStripes=True)
    ws.add_table(tbl2)
    ws.freeze_panes = 'A2'
    ws.column_dimensions['E'].width = 28
    ws.column_dimensions['F'].width = 24
    ws.column_dimensions['H'].width = 30

    # ---- doc_chua_chac (243 dong co '?' trong ghi chu — doc chua chac trong du lieu goc) ----
    ws = wb.create_sheet('doc_chua_chac')
    ws.append(['Bảng', 'Chân', 'Tín hiệu', 'Ghi chú (lý do chưa chắc)', 'Trang'])
    for c in range(1, 6):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    for (t, p, sig, note, page) in data['qmark_rows']:
        ws.append([t, p, sig, note, page])
    for r in range(2, ws.max_row + 1):
        for c in range(1, 6):
            ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical='top')
    ws.freeze_panes = 'A2'
    ws.column_dimensions['C'].width = 24
    ws.column_dimensions['D'].width = 55

    # ---- can_doi_chieu ----
    ws = wb.create_sheet('can_doi_chieu')
    ws.append(['Bảng', 'Chân', 'Tín hiệu', 'Địa chỉ ghi (một chiều)', 'Trang nguồn', 'Kết luận'])
    for c in range(1, 7):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    for (t, p, sig, addr, page) in data['oneway_rows']:
        ws.append([t, p, sig, addr, page, 'CHƯA XÁC NHẬN HAI CHIỀU'])
    ws.freeze_panes = 'A2'
    ws.column_dimensions['C'].width = 26
    ws.column_dimensions['D'].width = 30

    # ---- dia_chi_chua_chep (dia chi tro toi bang/linh kien CHUA co trong e4_all.csv) ----
    ws = wb.create_sheet('dia_chi_chua_chep')
    ws.append(['Bảng nguồn', 'Chân', 'Tín hiệu', 'Địa chỉ trỏ tới (chưa có dữ liệu)', 'Trang', 'Phân loại'])
    for c in range(1, 7):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    LINH_KIEN_ROI_RAC = {'Д1', 'ДР1', 'Л1', 'ПР1', 'R1'}  # theo KE-HOACH: Д1,Др1,Л1,Пр1 là linh kiện trên Э4, không phải bảng/trang
    for (t, p, sig, target, page) in data['missing_target_rows']:
        target_table = target.split('/')[0]
        loai = ('Linh kiện rời rạc trên Э4 (không phải trang thiếu)'
                if target_table in LINH_KIEN_ROI_RAC
                else 'CÓ THỂ LÀ TRANG/BẢNG THỰC SỰ CÒN THIẾU')
        ws.append([t, p, sig, target, page, loai])
    for r in range(2, ws.max_row + 1):
        loai_val = ws.cell(row=r, column=6).value
        if loai_val and 'THỰC SỰ' in loai_val:
            for c in range(1, 7):
                ws.cell(row=r, column=c).fill = WARN
    ws.freeze_panes = 'A2'
    ws.column_dimensions['C'].width = 26
    ws.column_dimensions['D'].width = 26
    ws.column_dimensions['F'].width = 42

    # ---- doi_chieu_khong_khop (20 dong e4_mismatch.csv, chi tiet tung dong) ----
    ws = wb.create_sheet('doi_chieu_khong_khop')
    ws.append(['Bảng', 'Chân', 'Tín hiệu', 'Địa chỉ ghi ở đây', 'Trang', 'Các dòng phía đối diện (không khớp ngược)'])
    for c in range(1, 7):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    if MISMATCH.is_file():
        with open(MISMATCH, encoding='utf-8') as f:
            for r in csv.DictReader(f):
                ws.append([r['table'], r['pin'], r['signal'], r['address'], r['page'], r['target_rows']])
    for r in range(2, ws.max_row + 1):
        for c in range(1, 7):
            ws.cell(row=r, column=c).fill = WARN
            ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical='top')
    ws.freeze_panes = 'A2'
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 26
    ws.column_dimensions['F'].width = 45

    # ---- canh_bao_quan_trong ----
    ws = wb.create_sheet('canh_bao_quan_trong')
    ws.append(['Mục', 'Nội dung', 'Nguồn'])
    for c in range(1, 4):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    for row in CANH_BAO_CO_DINH:
        ws.append(list(row))
    for r in range(2, ws.max_row + 1):
        for c in range(1, 4):
            ws.cell(row=r, column=c).fill = WARN
            ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical='top')
            ws.cell(row=r, column=c).border = brd
    ws.column_dimensions['A'].width = 28
    ws.column_dimensions['B'].width = 80
    ws.column_dimensions['C'].width = 40
    ws.freeze_panes = 'A2'

    # ---- ghi_chu_nguon ----
    ws = wb.create_sheet('ghi_chu_nguon')
    ws.append(['HẠNG MỤC', 'THÔNG TIN'])
    for c in range(1, 3):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    stats = [
        ('Nguồn chính', 'tmp/pdfs/review/a313-3/e4/e4_all.csv'),
        ('Nguồn ma trận Y16', 'tmp/pdfs/review/a313-3/e4/matrix_nets.csv'),
        ('Script sinh workbook', 'tmp/pdfs/review/a313-3/e4/build_ket_noi_toan_khoi.py'),
        ('Ngày sinh', datetime.date.today().isoformat()),
        ('Dòng e4_all.csv dùng', data['rows_total']),
        ('Số bảng (table) gốc', data['ntables']),
        ('Số net (dòng ket_noi_chung)', len(data['out_rows'])),
        ('Số cột tấm', len(data['board_cols'])),
        ('Số cột đầu cắm ngoài', len(data['ext_cols'])),
        ('Số cột đặc biệt/cần xác minh', len(data['special_cols'])),
        ('Số dòng một chiều (can_doi_chieu)', len(data['oneway_rows'])),
        ('Số dòng matrix_nets.csv đã hợp nhất', data['nmatrix']),
        ('Số dòng kiểm chéo KHÔNG khớp (doi_chieu_khong_khop)', 20),
        ('Số địa chỉ trỏ tới bảng/linh kiện chưa có (dia_chi_chua_chep)', len(data['missing_target_rows'])),
        ('  — trong đó là linh kiện rời rạc (Д1,Др1,Л1,Пр1), không phải trang thiếu', sum(1 for x in data['missing_target_rows'] if x[3].split('/')[0] in {'Д1','ДР1','Л1','ПР1','R1'})),
        ('  — trong đó CÓ THỂ là trang/bảng thực sự còn thiếu (vd 3Ш5, У17)', sum(1 for x in data['missing_target_rows'] if x[3].split('/')[0] not in {'Д1','ДР1','Л1','ПР1','R1'})),
        ('Số dòng gạch bỏ trên bản vẽ gốc, đã loại khỏi ghép net', len(data['struck_rows'])),
        ('Số dòng có "?" trong ghi chú gốc (đọc chưa chắc, xem doc_chua_chac)', len(data['qmark_rows'])),
        ('VÒNG', '2 (đã tự phản biện 2 điểm, xem nhat_ky_ra_soat_1) — CHƯA qua phản biện người dùng/Codex'),
    ]
    for row in stats:
        ws.append(list(row))
    for r in range(2, ws.max_row + 1):
        ws.cell(row=r, column=1).border = brd
        ws.cell(row=r, column=2).border = brd
    ws.column_dimensions['A'].width = 34
    ws.column_dimensions['B'].width = 70

    # ---- nhat_ky_ra_soat_1 (vong 1->2: tu-phan-bien truoc khi nguoi dung xem) ----
    ws = wb.create_sheet('nhat_ky_ra_soat_1')
    ws.append(['STT', 'Net/Cột sửa', 'Giá trị trước (vòng 1)', 'Giá trị sau (vòng 2)', 'Căn cứ', 'Trạng thái'])
    for c in range(1, 7):
        ws.cell(row=1, column=c).font = hdr_font
        ws.cell(row=1, column=c).fill = HDR
    log_v2 = [
        (1, 'Cột "?П1(Интеграторы)"',
         'Cột riêng, gắn cờ CẦN XÁC MINH (không rõ thuộc tấm nào)',
         'Gộp vào cột Y9, giá trị "П1/<chân>"',
         'Dữ liệu thô e4_all.csv: tiêu đề bảng ghi rõ "Интеграторы" = đúng tên Nga của Y9 '
         '(theo KE-HOACH/SO-DO-DAU-NOI). 53 dòng không có cột address nên vẫn hiển thị TÁCH '
         'khỏi dữ liệu Y9 qua КП5 — cần đối chiếu thủ công sau.',
         'ĐÃ SỬA (tự phản biện vòng 2)'),
        (2, 'Cột "?У16КП1/КП2/КП3(…chưa rõ tấm)"',
         'Gắn cờ CẦN XÁC MINH như thể là lỗi/thiếu dữ liệu',
         'Đổi tên "Y16-КПn (bó dây/đầu cắm khối)", BỎ cờ CẦN XÁC MINH',
         'matrix_notes.md §1 xác nhận П1/П2/П3 trên Y16 KHÔNG gắn tên tấm cụ thể trên bản vẽ gốc '
         '(khác hẳn П4…П15) — đây là sự thật kiến trúc, không phải lỗi transcribe.',
         'ĐÃ SỬA (tự phản biện vòng 2)'),
    ]
    for row in log_v2:
        ws.append(list(row))
    for r in range(2, ws.max_row + 1):
        for c in range(1, 7):
            ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical='top')
            ws.cell(row=r, column=c).border = brd
    ws.column_dimensions['B'].width = 24
    ws.column_dimensions['C'].width = 34
    ws.column_dimensions['D'].width = 34
    ws.column_dimensions['E'].width = 55

    out_dir = Path(r'E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\Excel center control')
    out_path = out_dir / 'A313-3_ket-noi-toan-khoi.xlsx'
    lock = out_dir / f'~${out_path.name}'
    if lock.is_file():
        raise RuntimeError(f'File dang mo trong Excel ({lock}), dong roi chay lai.')
    wb.save(out_path)
    print('\nDA LUU:', out_path)


if __name__ == '__main__':
    main()
