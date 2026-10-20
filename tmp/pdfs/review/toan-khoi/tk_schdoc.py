"""Altium SchDoc (binary) -> BOM + geometric netlist for every board of A313-V.

Run from project root:  python tmp/pdfs/review/toan-khoi/tk_schdoc.py
Outputs (tmp/pdfs/review/toan-khoi/):
  schdoc_bom.csv     board, designator, libref, comment, footprint, partcount
  schdoc_nets.csv    board, net, pins (DES.PIN ...), labels
  schdoc_summary.json  per board: component count by libref, net count

The SchDoc files are a re-drawing, not the A32 original: every net here is a
candidate and must be checked against BVTK before it is used as a fact.
Text is kept raw; labels drawn with the Cyrillic-looking fonts keep their
Latin code points (vih.1a= renders as ВЫХ.1А=, see CLAUDE.md section 5).
Buses (RECORD 26/37) are not followed: nets that only meet through a bus stay split.
"""
import collections
import csv
import json
import re
import struct
from pathlib import Path

import olefile

SRC = Path('File mach in va mach nguyen ly_A313_V')
OUT = Path('tmp/pdfs/review/toan-khoi')
BOARDS = {  # SchDoc -> board id used in the analysis
    'TAM1_Xulytrungtam/PAGE1.SchDoc': 'A313-V.01',
    'TAM2_chuyenmachtinhieuvao/A313-2.SchDoc': 'A313-V.02',
    'Tam3_Cum_tich_phan/A313_3.SchDoc': 'A313-V.03',
    'TAM4_Cumbiendoi/A313_4.SchDoc': 'A313-V.04',
    'Tam5_Chuyenmachtinhieura/A313_5.SchDoc': 'A313-V.05',
    'Tam6_khuyechdaitinhieura/A313_6.SchDoc': 'A313-V.06',
    'machbiendoilenhdon/machbiendoilenhdon.SchDoc': 'A313-V.07',
    'machbiendoilenhdon/Sheet1.SchDoc': 'A313-V.07(Sheet1)',
    'machnguon_A313V/NGUON_A313.SchDoc': 'A313-V.08.01',
    'machkiemtranguon/mach_kiem_tra_nguon.SchDoc': 'A313-V.08.02',
    'machkiemtranguon/ngoc.SchDoc': 'A313-V.08.02(ngoc)',
    'machdaucam96chan_DC13/daucam96chan.SchDoc': 'DC13-96',
    'machdaucam31chan_A313V/DAUCAM.SchDoc': 'DAUCAM-31',
    'tamcaclinhkienroirac/A313_10.SchDoc': 'A313-V.10',
}


def records(path):
    data = olefile.OleFileIO(str(path)).openstream('FileHeader').read()
    i, out = 0, []
    while i < len(data):
        n, = struct.unpack('<I', data[i:i+4])
        body = data[i+4:i+4+(n & 0xffffff)]
        i += 4 + (n & 0xffffff)
        rec = {}
        for part in body.rstrip(b'\x00').decode('latin1').split('|'):
            if '=' in part:
                k, v = part.split('=', 1)
                rec[k.upper()] = v
        for k in [k for k in rec if k.startswith('%UTF8%')]:
            rec[k[6:]] = rec.pop(k).encode('latin1').decode('utf8', 'replace')
        out.append(rec)
    return out[1:]  # OWNERINDEX counts records after the header


def xy(r, p='LOCATION.'):
    f = lambda a: int(r.get(p+a, 0)) + int(r.get(p+a+'_FRAC', 0)) / 1e5
    return (f('X'), f('Y'))


def on_segment(p, a, b):
    if (a[0]-p[0])*(b[1]-p[1]) != (b[0]-p[0])*(a[1]-p[1]):
        return False
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def pin_hotspot(r):
    x, y = xy(r)
    ln = int(r.get('PINLENGTH', 0)) + int(r.get('PINLENGTH_FRAC', 0)) / 1e5
    dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][int(r.get('PINCONGLOMERATE', 0)) & 3]
    return (x + dx*ln, y + dy*ln)


def parse(path):
    R = records(path)
    comps = {}
    for i, r in enumerate(R):
        if r.get('RECORD') == '1':
            comps[i] = dict(lib=r.get('LIBREFERENCE', ''), part=r.get('CURRENTPARTID', '1'),
                            mode=r.get('DISPLAYMODE', '0'), des='', comment='', fp='',
                            parts=r.get('PARTCOUNT', ''))
    for r in R:
        o = int(r.get('OWNERINDEX', -1))
        if o not in comps:
            continue
        if r.get('RECORD') == '34':
            comps[o]['des'] = r.get('TEXT', '')
        elif r.get('RECORD') == '41' and r.get('NAME', '').lower() == 'comment':
            comps[o]['comment'] = r.get('TEXT', '')
        elif r.get('RECORD') == '45' and r.get('ISCURRENT') == 'T':
            comps[o]['fp'] = r.get('MODELNAME', '')
    # geometric items
    segs, pins, tags, dots = [], [], [], []
    for r in R:
        t = r.get('RECORD')
        if t == '27':
            pts = [(int(r['X%d' % k]) + int(r.get('X%d_FRAC' % k, 0))/1e5,
                    int(r['Y%d' % k]) + int(r.get('Y%d_FRAC' % k, 0))/1e5)
                   for k in range(1, int(r['LOCATIONCOUNT'])+1)]
            segs += list(zip(pts, pts[1:]))
        elif t == '2':
            o = int(r.get('OWNERINDEX', -1))
            c = comps.get(o)
            if c is None or r.get('OWNERPARTID', c['part']) not in (c['part'], '-1'):
                continue
            if r.get('OWNERPARTDISPLAYMODE', '0') != c['mode']:
                continue
            pins.append((pin_hotspot(r), '%s.%s' % (c['des'], r.get('DESIGNATOR', '?')), r.get('NAME', '')))
        elif t in ('25', '17'):
            tags.append((xy(r), ('L:' if t == '25' else 'P:') + r.get('TEXT', '')))
        elif t == '29':
            dots.append(xy(r))
    # union-find over segments + pins + tags
    n_s, n_p = len(segs), len(pins)
    parent = list(range(n_s + n_p + len(tags)))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def join(i, j):
        parent[root(j)] = root(i)

    ends = collections.defaultdict(list)
    for i, (a, b) in enumerate(segs):
        ends[a].append(i)
        ends[b].append(i)
    for idx in ends.values():
        for j in idx[1:]:
            join(idx[0], j)
    hot = set(ends) | set(dots)
    for p in hot:  # T-junctions (endpoint on another wire) and explicit junction dots
        for i, (a, b) in enumerate(segs):
            if on_segment(p, a, b) and p not in (a, b):
                if p in ends:
                    join(i, ends[p][0])
                elif p in dots:
                    # crossing wires through a dot: join every wire passing the dot
                    for k, (c, d) in enumerate(segs):
                        if on_segment(p, c, d):
                            join(i, k)
    by_point = collections.defaultdict(list)
    for k, (p, _, _) in enumerate(pins):
        by_point[p].append(n_s + k)
    for k, (p, _) in enumerate(tags):
        by_point[p].append(n_s + n_p + k)
    for p, idx in by_point.items():
        for j in idx[1:]:
            join(idx[0], j)
        for i, (a, b) in enumerate(segs):
            if on_segment(p, a, b):
                join(i, idx[0])
    by_name = collections.defaultdict(list)
    for k, (_, name) in enumerate(tags):
        by_name[name[2:]].append(n_s + n_p + k)  # same text = same net (labels and power ports)
    for idx in by_name.values():
        for j in idx[1:]:
            join(idx[0], j)
    nets = collections.defaultdict(lambda: dict(pins=[], labels=set()))
    for k, (_, ref, _) in enumerate(pins):
        nets[root(n_s + k)]['pins'].append(ref)
    for k, (_, name) in enumerate(tags):
        nets[root(n_s + n_p + k)]['labels'].add(name[2:])
    return comps, [v for v in nets.values() if v['pins']]


def selftest():
    assert on_segment((1, 0), (0, 0), (2, 0)) and not on_segment((1, 1), (0, 0), (2, 0))
    assert pin_hotspot({'LOCATION.X': '10', 'LOCATION.Y': '5', 'PINLENGTH': '3', 'PINCONGLOMERATE': '2'}) == (7, 5)


def crosscheck():
    """Facts of PHAN-TICH_TOAN-KHOI §0.3 that the SchDoc must reproduce (other sources in comments)."""
    bom = list(csv.DictReader(open(OUT/'schdoc_bom.csv', encoding='utf8')))
    nets = list(csv.DictReader(open(OUT/'schdoc_nets.csv', encoding='utf8')))
    pk = lambda b, f: len({r['designator'] for r in bom if r['board'] == b and f(r)})
    lib = lambda b, s: pk(b, lambda r: s.lower() in r['libref'].lower())
    # .06: README / PHAN-TICH .06 Rev. C
    assert (lib('A313-V.06', '168kt2'), lib('A313-V.06', '140yd1'), lib('A313-V.06', '2n1069'), lib('A313-V.06', '2n1132')) == (15, 18, 16, 16)
    kt06 = {r['designator'] for r in bom if r['board'] == 'A313-V.06' and '168' in r['libref']}
    lone = {p for r in nets if r['board'] == 'A313-V.06' and len(r['pins'].split()) == 1 for p in r['pins'].split()}
    assert all(d + '.11' in lone for d in kt06), '168КТ2 pin 11 must be unconnected on .06'
    # .05: CLAUDE.md 4.7 and BV.21
    v05 = [r['comment'] for r in bom if r['board'] == 'A313-V.05']
    assert (lib('A313-V.05', '168kt2'), v05.count('330k'), v05.count('4,7uf')) == (57, 58, 49)
    # .02 / .03 / .04 / .01 against BV.09, BV.13, BV.17, BV.05
    assert (lib('A313-V.02', '168kt2'), lib('A313-V.02', '198')) == (18, 12)  # BV.09: 18 / 11 (U9 in §6)
    assert (lib('A313-V.03', '168kt2'), lib('A313-V.03', '140yd1')) == (25, 10)
    assert lib('A313-V.04', '140yd1') == 8
    assert (lib('A313-V.01', '74hc374'), lib('A313-V.01', 'ct25244'), lib('A313-V.01', 'cy62256'), lib('A313-V.01', 'cy14b101')) == (4, 9, 3, 3)
    assert lib('A313-V.01', '3245') == 0  # BV.05 lists U28..U32 SN74CB3T3245: not drawn in the SchDoc
    # .08.01: module per designator (BV.33) and the measuring points of GIAO AN (+ rail through L2 for -6,3 V)
    mods = {r['designator']: r['comment'].upper() for r in bom if r['board'] == 'A313-V.08.01' and r['designator'].startswith('U')}
    assert mods == {'U1': 'PTN78020W', 'U2': 'PTN78020A', 'U3': 'PTN78020W', 'U4': 'THN30-2415',
                    'U5': 'THN30-2422', 'U6': 'TEN40-2411N'}, mods
    net_of = {p: r['net'] for r in nets if r['board'] == 'A313-V.08.01' for p in r['pins'].split()}
    ga = {'U6.4': '+5V', 'U1.5': '+6.3V', 'U1.6': '+6.3V', 'U5.3': '+12.6V', 'U5.5': '-12.6V',
          'U3.6': '+3.5V', 'U4.5': '-23V'}
    assert all(net_of[p] == v for p, v in ga.items()), {p: net_of[p] for p in ga}
    assert net_of['U2.1'] == net_of['L2.1'] and net_of['L2.2'] == '-6.3V'  # GIAO AN: -6,3 V at U2 pin 1
    # backplane power pin pattern (§2.2): odd DC A2/A3/A4 = +5/+3,5/+6,3 V, even DC = -23/-12,6/+12,6 V
    pins = {(r['board'], p): r['net'].split('/') for r in nets for p in r['pins'].split()}
    dc = {'A313-V.02': ('DC3', 'DC4'), 'A313-V.03': ('DC5', 'DC6'), 'A313-V.04': ('DC7', 'DC8'),
          'A313-V.05': ('DC9', 'DC10'), 'A313-V.06': ('DC11', 'DC12')}
    unused = lambda names: all(re.fullmatch(r'N\d{4}', x) for x in names)  # pin drawn but left open
    for b, (odd, even) in dc.items():
        for row in 'ABC':
            assert '+5V' in pins[(b, '%s.%s2' % (odd, row))] and '-23V' in pins[(b, '%s.%s2' % (even, row))], b
            for con, pin, rail in ((odd, '3', '+3,5V'), (odd, '4', '+6,3V'), (even, '3', '-12,6V'), (even, '4', '+12,6V')):
                names = pins.get((b, '%s.%s%s' % (con, row, pin)), [])
                assert not names or rail in names or unused(names), (b, con, row, pin, names)
    print('crosscheck OK: .06 15/18/16/16, .05 57/58/49, power 7/7 GIAO AN points, DC power pattern 5 boards')


def main():
    selftest()
    OUT.mkdir(parents=True, exist_ok=True)
    summary = {}
    with open(OUT/'schdoc_bom.csv', 'w', newline='', encoding='utf8') as fb, \
         open(OUT/'schdoc_nets.csv', 'w', newline='', encoding='utf8') as fn:
        wb, wn = csv.writer(fb), csv.writer(fn)
        wb.writerow(['board', 'designator', 'libref', 'comment', 'footprint', 'partcount'])
        wn.writerow(['board', 'net', 'pins', 'labels'])
        for rel, board in BOARDS.items():
            comps, nets = parse(SRC/rel)
            real = [c for c in comps.values() if c['des'] and not c['lib'].lower().startswith('titleblock')]
            for c in sorted(real, key=lambda c: c['des']):
                wb.writerow([board, c['des'], c['lib'], c['comment'], c['fp'], c['parts']])
            for k, nt in enumerate(sorted(nets, key=lambda v: sorted(v['labels']) or ['~'])):
                name = '/'.join(sorted(nt['labels'])) or 'N%04d' % k
                wn.writerow([board, name, ' '.join(sorted(nt['pins'])), len(nt['labels'])])
            # one package per designator; multi-part symbols (4 switches of a 168KT2) share it
            pkg = {c['des']: re.sub(r'_\d+$', '', c['lib']) for c in real}
            summary[board] = dict(
                file=rel, symbols=len(real), packages=len(pkg),
                by_libref=dict(collections.Counter(pkg.values()).most_common()),
                nets=len(nets), named_nets=sum(1 for v in nets if v['labels']))
            print('%-20s pkgs=%4d nets=%4d named=%4d' % (board, len(pkg), len(nets), summary[board]['named_nets']))
    (OUT/'schdoc_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding='utf8')
    crosscheck()


if __name__ == '__main__':
    main()
