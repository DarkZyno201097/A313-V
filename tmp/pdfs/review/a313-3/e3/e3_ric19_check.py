"""Kiểm chéo ric19_bom.csv <-> ric19_net.csv (У24, рис.19). Chạy: python3 e3_ric19_check.py"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

D = Path(__file__).parent
bom = list(csv.DictReader(open(D / 'ric19_bom.csv', encoding='utf8')))
net = list(csv.DictReader(open(D / 'ric19_net.csv', encoding='utf8')))

b = {r['ref'] for r in bom}
dup = [k for k, v in Counter(r['ref'] for r in bom).items() if v > 1]
n = {r['ref'] for r in net}
pins = Counter((r['ref'], r['pin']) for r in net)
by_net = defaultdict(list)
for r in net:
    by_net[r['net']].append(r['ref'] + '.' + r['pin'])

print('BOM rows', len(bom), '| BOM refs', len(b), '| dup', dup)
print('net rows', len(net), '| refs', len(n), '| nets', len(by_net),
      '(N#', sum(k.startswith('N') for k in by_net), ')')
print('in net, not in BOM:', sorted(n - b))
print('in BOM, not in net:', sorted(b - n))
print('pin used twice:', [k for k, v in pins.items() if v > 1])
print('N# with <2 pins:', {k: v for k, v in by_net.items() if k.startswith('N') and len(v) < 2})
missing_page = sorted(r['ref'] for r in bom if not r['name'])
print('BOM rows without name (page 211):', len(missing_page))
assert not dup and n <= b and not [k for k, v in pins.items() if v > 1]
assert all(len(v) >= 2 for k, v in by_net.items() if k.startswith('N'))
