"""Aircraft connectors 3Ш3/3Ш3В/3Ш4/3Ш4В: Soviet A-313-3 (Э4 transcription) vs A313-V (TMKT appendix).

Run from project root after e4_check.py and toan-khoi/tk_connectors.py:
    python tmp/pdfs/review/a313-3/e4_tmkt.py
Output: e4/e4_vs_tmkt.csv (connector, pin, A-313-3 signal, A313-V signal, verdict) + summary.
Verdict: same (normalised names equal), similar (difflib ratio >= 0.6), diff, or one side empty.
"""
import csv
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, 'tmp/pdfs/review/toan-khoi')
from tk_connectors import norm  # noqa: E402

E4 = Path('tmp/pdfs/review/a313-3/e4')
TMKT = Path('tmp/pdfs/review/toan-khoi/tmkt_3Sh_pinout.csv')


def n(s):
    s = re.sub(r'[¬⊓⊔⎍]|\(27в\)|\(\+27в\)', '', (s or '').lower())
    return norm(s, False).replace('корпус', 'gnd')


def main():
    assert n('ВХОД РК-1 (27В)') == n('Вход PK-1') and n('¬СВК2-1') == n('СВК2-1')
    v = {(r['connector'].replace('B', 'В'), int(r['pin'])): r['signal'] for r in csv.DictReader(open(TMKT, encoding='utf8'))}
    s = {}
    for r in csv.DictReader(open(E4 / 'e4_all.csv', encoding='utf8')):
        if r['table'] in ('3Ш3', '3Ш3В', '3Ш4', '3Ш4В'):
            s[(r['table'], int(r['pin']))] = (r['signal'], r['note'])
    assert len(s) == 4 * 67 and len(v) == 4 * 67, (len(s), len(v))
    rows, cnt = [], {}
    for k in sorted(v):
        a, note = s[k]
        b = v[k]
        na, nb = n(a), n(b)
        if not na and not nb:
            verdict = 'both empty'
        elif not na or not nb:
            verdict = 'A313-3 empty' if not na else 'A313-V empty'
        elif na == nb:
            verdict = 'same'
        elif difflib.SequenceMatcher(None, na, nb).ratio() >= 0.6:
            verdict = 'similar'
        else:
            verdict = 'diff'
        if 'зачёрк' in note or 'gạch xoá' in note:
            verdict += ' (struck on A-313-3)'
        cnt[verdict] = cnt.get(verdict, 0) + 1
        rows.append(dict(connector=k[0], pin=k[1], a313_3=a, a313_v=b, verdict=verdict))
    with open(E4 / 'e4_vs_tmkt.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for k2, c in sorted(cnt.items()):
        print(k2, c)
    for r in rows:
        if not r['verdict'].startswith(('same', 'similar', 'both')):
            print(r['connector'], r['pin'], '|', r['a313_3'], '|', r['a313_v'], '|', r['verdict'])


if __name__ == '__main__':
    main()
