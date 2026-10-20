"""TMKT appendix (3Ш3/3Ш3B/3Ш4/3Ш4B -> DCx pin) vs SchDoc net labels at the same DC pin.

Run from project root after tk_schdoc.py:
    python tmp/pdfs/review/toan-khoi/tk_connectors.py
Outputs (tmp/pdfs/review/toan-khoi/):
  tmkt_3Sh_pinout.csv      connector, pin, signal, dir, dest, dc_pin, dc, board
  tmkt_vs_schdoc.csv       every appendix row that lands on a DC pin of a board with a SchDoc
  connector_summary.json   per connector: rows by destination board; cross-check rates

Source pages: TMKT&HDSD A313-V.pdf pages 51-57 ("PHẦN 3. PHỤ LỤC").
"""
import collections
import csv
import json
import re
from pathlib import Path

import pdfplumber

OUT = Path('tmp/pdfs/review/toan-khoi')
TMKT = Path('TMKT&HDSD A313-V/TMKT&HDSD A313-V.pdf')
# DC socket on the backplane -> connector designator inside each board SchDoc
SCHDOC_DC = {'DC1': ('A313-V.01', 'DC1B'), 'DC2': ('A313-V.01', 'DC2B'),
             'DC3': ('A313-V.02', 'DC3'), 'DC4': ('A313-V.02', 'DC4'),
             'DC5': ('A313-V.03', 'DC5'), 'DC6': ('A313-V.03', 'DC6'),
             'DC7': ('A313-V.04', 'DC7'), 'DC8': ('A313-V.04', 'DC8'),
             'DC9': ('A313-V.05', 'DC9'), 'DC10': ('A313-V.05', 'DC10'),
             'DC11': ('A313-V.06', 'DC11'), 'DC12': ('A313-V.06', 'DC12'),
             'DC13': ('A313-V.08.01', 'DC13A')}
# Latin code points of the Cyrillic-looking drawing fonts (CLAUDE.md section 5, extended
# from labels seen in the SchDoc files: vhod pc1 = Вход ПК1, rc10 = РК10, upr = Упр)
FONT = dict(zip('abvgdezijklmnoprstufhcxw[', 'абвгдезыцзлмнопрстуфхксше'))
ALIAS = [('выход', 'вых'), ('вход', 'вх'), ('корпус', 'gnd'), ('общийпровод', 'gnd'),
         ('гнд', 'gnd'), ('бход', 'вх'), ('ы', 'и')]  # и/ы share one key: the fonts disagree
LOOK = dict(zip('aвekmhopctyxbг', 'авекмнорстухьг'))  # Latin lookalikes typed inside Cyrillic text


def norm(s, font):
    s = s.lower().replace('ё', 'е')
    s = ''.join((FONT if font else LOOK).get(ch, ch) for ch in s)
    s = re.sub(r'[\s\.\-_"=≈~,;:()]+', '', s)
    for a, b in ALIAS:
        s = s.replace(a, b)
    return s


def appendix():
    pdf = pdfplumber.open(str(TMKT))
    rows, conn_l, conn_r = [], '3Ш4B', '3Ш4'
    for pno in range(50, 57):
        page = pdf.pages[pno]
        switch = [w['top'] for w in page.extract_words() if w['text'] == '3Ш3B']
        for tb in page.find_tables():
            left = tb.bbox[0] < 200
            if switch and tb.bbox[1] > switch[0]:
                conn_l, conn_r = '3Ш3B', '3Ш3'
            for cells in tb.extract():
                cells = [(c or '').replace('\n', ' ').strip() for c in cells]
                dest, typ, pin, sig = cells if left else cells[::-1]
                if pin.startswith('Chân') or (not pin and not dest and not sig):
                    continue
                conn = conn_l if left else conn_r
                if not pin:  # continuation of the previous row split over a page
                    prev = [r for r in rows if r['connector'] == conn][-1]
                    prev['dest'] = (prev['dest'] + ' ' + dest).strip()
                    continue
                rows.append(dict(connector=conn, pin=int(pin), signal=sig, dir=typ, dest=dest))
    for r in rows:
        m = re.match(r'\s*([A-C]?\d+[A-C]?)-(DC\d+[A-D]?)\s*[|/]\s*(A313-?\s*V\.[\d.]+)', r['dest'])
        r['dc_pin'], r['dc'], r['board'] = (m.group(1), m.group(2), re.sub(r'A313-?\s*V', 'A313-V', m.group(3))) if m else ('', '', '')
    return rows


def schdoc_pins():
    pins = {}
    for r in csv.DictReader(open(OUT/'schdoc_nets.csv', encoding='utf8')):
        for p in r['pins'].split():
            pins[(r['board'], p)] = r['net']
    return pins


def main():
    rows = appendix()
    # self-checks against rows read by eye in the PDF
    key = {(r['connector'], r['pin']): r for r in rows}
    assert key[('3Ш4B', 2)]['dc_pin'] == 'C9' and key[('3Ш4B', 2)]['dc'] == 'DC1'
    assert key[('3Ш4', 2)]['signal'] == 'Выход РК1' and key[('3Ш4', 2)]['dc'] == 'DC13'
    assert 'biến thế' in key[('3Ш4', 55)]['dest'] and '400' in key[('3Ш4', 55)]['signal']
    assert key[('3Ш3B', 55)]['signal'] == 'Uоп ~5В'
    assert [key[('3Ш3B', n)]['signal'] for n in (50, 51)] == ['Упр мод 1', 'Упр мод 2']
    assert not key[('3Ш3B', 50)]['dest'] and not key[('3Ш3B', 51)]['dest']  # destination left blank in TMKT
    for c in ('3Ш3', '3Ш3B', '3Ш4', '3Ш4B'):
        got = sorted(r['pin'] for r in rows if r['connector'] == c)
        assert got == list(range(1, 68)), (c, len(got), sorted(set(range(1, 68)) - set(got)))
    with open(OUT/'tmkt_3Sh_pinout.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r['connector'], r['pin'])))
    pins = schdoc_pins()
    checked = []
    for r in rows:
        if r['dc'] not in SCHDOC_DC:
            continue
        board, des = SCHDOC_DC[r['dc']]
        net = pins.get((board, '%s.%s' % (des, r['dc_pin'])), '')
        named = bool(net) and not re.fullmatch(r'N\d{4}', net)
        a, b = norm(r['signal'], False), norm(net, True)
        hit = named and any(a == x or (len(a) > 3 and (a in x or x in a)) for x in b.split('/'))
        checked.append(dict(connector=r['connector'], pin=r['pin'], signal=r['signal'], dc=r['dc'],
                            dc_pin=r['dc_pin'], schdoc_net=net, named=named, match=hit))
    with open(OUT/'tmkt_vs_schdoc.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, list(checked[0]))
        w.writeheader()
        w.writerows(checked)
    summary = {}
    for c in ('3Ш3', '3Ш3B', '3Ш4', '3Ш4B'):
        rs = [r for r in rows if r['connector'] == c]
        summary[c] = dict(rows=len(rs), by_board=dict(collections.Counter(r['board'] or r['dest'][:24] or '(trống)' for r in rs).most_common()))
    by_dc = collections.defaultdict(lambda: [0, 0, 0])
    for c in checked:
        by_dc[c['dc']][0] += 1
        by_dc[c['dc']][1] += c['named']
        by_dc[c['dc']][2] += c['match']
    summary['crosscheck_by_dc'] = {k: dict(rows=v[0], schdoc_named=v[1], name_match=v[2]) for k, v in sorted(by_dc.items())}
    (OUT/'connector_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding='utf8')
    for k, v in summary['crosscheck_by_dc'].items():
        print(k, v)
    print('total', len(checked), 'named', sum(c['named'] for c in checked), 'match', sum(c['match'] for c in checked))


if __name__ == '__main__':
    main()
