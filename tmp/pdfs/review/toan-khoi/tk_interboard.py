"""Inter-board signals inferred from SchDoc net names at the 96-pin DC connectors.

Run from project root after tk_schdoc.py:
    python tmp/pdfs/review/toan-khoi/tk_interboard.py
Outputs (tmp/pdfs/review/toan-khoi/):
  interboard_signals.csv  normalized name, boards, DC pins on each board, raw labels
  interboard_matrix.json  board x board count of shared signal names

There is no SchDoc of the A313-V.09 backplane, so a link here means "the same
net name appears on a DC pin of both boards". Same name, different pin rows
(A/B/C) on two boards is normal: the backplane routes it. Power and ground
names are listed separately. Names that only differ in spelling are missed.
"""
import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tk_connectors import OUT, norm  # noqa: E402

DC_OF = {'A313-V.01': ('DC1B', 'DC2B'), 'A313-V.02': ('DC3', 'DC4'), 'A313-V.03': ('DC5', 'DC6'),
         'A313-V.04': ('DC7', 'DC8'), 'A313-V.05': ('DC9', 'DC10'), 'A313-V.06': ('DC11', 'DC12'),
         'A313-V.08.01': ('DC13A', 'DC14C'), 'A313-V.08.02': ('DC14D',), 'A313-V.10': ('DC15',)}
POWER = re.compile(r'^(gnd|[+-]?\d+[.,]?\d*[вvb]|27|vccram|[+-]?\d+[.,]\d*в?|оп|30)$')


def main():
    sig = collections.defaultdict(lambda: collections.defaultdict(set))
    raw = collections.defaultdict(set)
    for r in csv.DictReader(open(OUT/'schdoc_nets.csv', encoding='utf8')):
        b = r['board']
        if b not in DC_OF or re.fullmatch(r'N\d{4}', r['net']):
            continue
        dc = [p for p in r['pins'].split() if p.split('.')[0] in DC_OF[b]]
        if not dc:
            continue
        for lab in r['net'].split('/'):
            k = norm(lab, True)
            if not k or len(k) < 2:
                continue
            sig[k][b] |= set(dc)
            raw[k].add(lab)
    rows, matrix = [], collections.Counter()
    for k, by in sorted(sig.items()):
        if len(by) < 2:
            continue
        boards = sorted(by)
        rows.append(dict(name=k, power=bool(POWER.match(k)), boards=' '.join(boards),
                         pins=' | '.join('%s: %s' % (b, ' '.join(sorted(by[b]))) for b in boards),
                         labels=' / '.join(sorted(raw[k]))))
        if not POWER.match(k):
            for i, a in enumerate(boards):
                for c in boards[i+1:]:
                    matrix['%s<->%s' % (a, c)] += 1
    assert rows, 'no shared names: check schdoc_nets.csv'
    with open(OUT/'interboard_signals.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    (OUT/'interboard_matrix.json').write_text(json.dumps(dict(matrix.most_common()), ensure_ascii=False, indent=1), encoding='utf8')
    print(len(rows), 'shared names;', sum(r['power'] for r in rows), 'power/ground')
    for k, v in matrix.most_common():
        print('  %-28s %d' % (k, v))


if __name__ == '__main__':
    main()
