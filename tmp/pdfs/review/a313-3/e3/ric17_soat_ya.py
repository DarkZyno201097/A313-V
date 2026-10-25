"""Chép lại 6 bảng ô Я1…Я6 (рис.17, Y11) trên ảnh A313-3_CONTROL/Y11/RE_tr202_a266.jpg (tờ 1), đối chiếu
bảng П1/П2 đầy đủ trên RE_tr203_a267.jpg (tờ 2). Claude, 2026-10-25. Ghi đè các dòng Я*.S/B/Q trong
ric17_net.csv và thêm chân У11/У12 còn thiếu; chạy lại không đổi kết quả.
Chạy: python -B tmp/pdfs/review/a313-3/e3/ric17_soat_ya.py"""
import csv, io
from pathlib import Path

NET = Path(__file__).parent / 'ric17_net.csv'
SRC = 'Soát 2026-10-25 trên a266 (zoom 2×), khớp bảng П{p} đầy đủ tờ 2 (a267)'
# ô: (IC cấp S/B, [(Вых, П, chân) cho Q1…Q8])
YA = {
    'Я1': ('У9', [('1а', 1, 34), ('2а', 1, 33), ('3а', 1, 7), ('4а', 1, 41), ('5а', 1, 35), ('6а', 1, 8), ('7а', 1, 36), ('8а', 1, 43)]),
    'Я2': ('У10', [('9а', 2, 28), ('10а', 2, 31), ('11а', 2, 8), ('12а', 2, 39), ('13а', 2, 29), ('14а', 2, 4), ('15а', 2, 36), ('16а', 2, 12)]),
    'Я3': ('У11', [('17а', 2, 43), ('18а', 2, 32), ('19а', 2, 9), ('20а', 2, 40), ('21а', 2, 30), ('22а', 2, 5), ('23а', 2, 46), ('24а', 2, 47)]),
    'Я4': ('У12', [('25а', 2, 3), ('26а', 2, 6), ('27а', 2, 37), ('28а', 2, 51), ('29а', 2, 33), ('30а', 2, 7), ('31а', 2, 10), ('32а', 2, 25)]),
    'Я5': ('У13', [('1б', 1, 52), ('2б', 1, 51), ('3б', 1, 46), ('4б', 1, 23), ('5б', 1, 24), ('6б', 1, 25), ('7б', 1, 49), ('8б', 1, 45)]),
    'Я6': ('У14', [('9б', 2, 53), ('10б', 2, 52), ('11б', 2, 50), ('12б', 2, 14), ('13б', 2, 34), ('14б', 2, 35), ('15б', 2, 38), ('16б', 2, 13)]),
}
SB = {'S1': 3, 'S2': 12, 'B1': 5, 'B2': 10}  # chân IC chuyển mạch cấp cho S/B, giống nhau ở cả 6 ô
NOTE_Y4 = '. Sửa: bản trước đọc S/B là У13 và Q1/Q2/Q3 là П2:13/16/17 — nhầm; Я4 ghi rõ У12, П2/3, 6, 37'
NOTE_Y3 = '. Sửa: bản trước đọc Q6/Q8 là П2:15/41 (ô trống trong П2) — đúng là П2/5, П2/47'


def want():
    out = {}
    for ya, (ic, qs) in YA.items():
        extra = NOTE_Y4 if ya == 'Я4' else NOTE_Y3 if ya == 'Я3' else ''
        for s, pin in SB.items():
            out[(ya, s)] = (f'{ic}.{pin}', SRC.format(p='1/П2') + extra)
        for i, (v, p, c) in enumerate(qs, 1):
            out[(ya, f'Q{i}')] = (f'Вых.{v} | П{p}:{c}', SRC.format(p=p) + extra)
    return out


def main():
    rows = list(csv.reader(open(NET, encoding='utf-8-sig', newline='')))
    head, body = rows[0], rows[1:]
    w = want()
    assert len(w) == 6 * 12 and len({n for n, _ in w.values()}) == 72  # mỗi net một chân, không trùng П
    for r in body:
        if (r[0], r[1]) in w:
            r[2], r[3] = w[(r[0], r[1])]
    have = {(r[0], r[1]) for r in body}
    assert all(k in have for k in w), 'thiếu dòng Я trong net'
    # chân IC phía ngược lại của S/B; У13 cũ (do nhầm Я4) vẫn đúng vì Я5 dùng У13
    tmpl = next(r for r in body if r[0] == 'У11' and r[1] == '5')
    at = body.index(tmpl)
    for ic in ('У11', 'У12'):
        for pin in (3, 12, 5, 10):
            if (ic, str(pin)) not in have:
                at += 1
                body.insert(at, [ic, str(pin), f'{ic}.{pin}', tmpl[3]])
    buf = io.StringIO()
    csv.writer(buf, lineterminator='\r\n').writerows([head] + body)
    NET.write_text(buf.getvalue(), encoding='utf-8', newline='')
    print('dòng net:', len(body))


if __name__ == '__main__':
    main()
