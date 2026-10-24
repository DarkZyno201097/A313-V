"""Áp kết quả soát lại рис.7 (Codex đọc ảnh a255–a257, ric07_soat_raw.csv) vào ric07_net.csv / ric07_conn.csv.

Chỉ áp dòng ket_qua = ro; dòng van_chua_ro giữ nguyên. Ghép theo (ref, pin, net cũ) vì ref «?» có thể lặp.
Chạy từ gốc repo:  python tmp/pdfs/review/a313-3/e3/ric07_soat_apply.py   (chạy lại không đổi kết quả)
"""
import csv
from pathlib import Path

D = Path(__file__).parent
rd = lambda f: list(csv.DictReader(open(D / f, encoding='utf-8-sig')))
net, conn, soat = rd('ric07_net.csv'), rd('ric07_conn.csv'), rd('ric07_soat_raw.csv')
TAG = 'soát 2026-10-24 (Codex): '
idx = {}
for i, r in enumerate(net):
    idx.setdefault((r['ref'], r['pin'], r['net']), []).append(i)
done = {i for i, r in enumerate(net) if TAG in r['note']}  # đã áp ở lần chạy trước
applied = 0
for s in soat:
    if s['ket_qua'] != 'ro':
        continue
    if s['ref'] in ('П1', 'П2', 'П3'):  # ô tín hiệu bảng đầu nối
        [c] = [c for c in conn if c['table'] == s['ref'] and c['pin'] == s['pin']]
        if c['signal'] != s['noi_toi']:
            c['signal'], c['note'] = s['noi_toi'], (c['note'] + '; ' if c['note'] else '') + TAG + s['note']
        applied += 1
        continue
    cand = [i for i in idx.get((s['ref'], s['pin'], s['net_cu']), [])]
    if not cand:  # đã áp: net cũ đã đổi
        assert any(TAG in net[i]['note'] for i, r in enumerate(net) if (r['ref'], r['pin']) == (s['ref'], s['pin'])), s
        continue
    i = cand[0]
    t = s['noi_toi']
    if '.' in t and ';' in t or t.count('.') == 1 and ' ' not in t:
        # danh sách chân: gom vào net của chân bạn nếu chân đó đã có net rõ, không thì đặt tên chung
        mates = [m.strip() for m in t.split(';')]
        name = None
        for m in mates:
            ref, pin = m.rsplit('.', 1)
            for r in net:
                if (r['ref'], r['pin']) == (ref, pin) and '?' not in r['net']:
                    name = r['net']
        t = name or 'SOAT:' + '+'.join(sorted([f"{s['ref']}.{s['pin']}"] + mates))
    net[i]['net'] = t
    net[i]['note'] = TAG + s['note']
    idx[(s['ref'], s['pin'], t)] = [i]
    applied += 1
for f, rows, cols in (('ric07_net.csv', net, ['ref', 'pin', 'net', 'note']), ('ric07_conn.csv', conn, ['table', 'pin', 'signal', 'photo', 'note'])):
    with open(D / f, 'w', newline='', encoding='utf8') as fh:  # giữ định dạng gốc: mọi ô trong ngoặc kép, CRLF
        w = csv.DictWriter(fh, cols, quoting=csv.QUOTE_ALL); w.writeheader(); w.writerows(rows)
print('ro trong soát:', sum(s['ket_qua'] == 'ro' for s in soat), '| áp lượt này:', applied,
      '| dòng net còn ?:', sum('?' in r['net'] for r in net))
