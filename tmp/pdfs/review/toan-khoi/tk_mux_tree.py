"""Multiplexer tree and input dividers of A313-V.02 from the SchDoc netlist.

Run from project root after tk_schdoc.py:
    python tmp/pdfs/review/toan-khoi/tk_mux_tree.py
Output: tmp/pdfs/review/toan-khoi/mux_tree_02.csv and printed summary.

Graph: node = net; edge = one 168КТ2 section (исток<->сток, labelled with its
затвор net) or one resistor. GND and supply nets are never crossed. For every
input label on DC3 the script walks switch-by-switch to a DC pin of the board
and records the packages on the way (level 1 = nearest the input).
Divider ratio = R_to_GND / (R_series + R_to_GND) at the first switch node,
values taken from the SchDoc "Comment" field (re-drawn, not BVTK).
"""
import collections
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tk_connectors import OUT, norm  # noqa: E402

SECT = [(3, 2, 1), (5, 6, 7), (10, 9, 8), (12, 13, 14)]  # (исток, затвор, сток) of 168КТ2
RAIL = re.compile(r'(gnd|^[+-]?\d+[.,]?\d*v$|-23v|\+6,3v|\+5v|\+3,5v)', re.I)


def ohms(s):
    m = re.match(r'\s*([\d.,]+)\s*([kKmMrRΩ]?)', s or '')
    if not m:
        return None
    v = float(m.group(1).replace(',', '.'))
    return v * {'k': 1e3, 'K': 1e3, 'm': 1e6, 'M': 1e6}.get(m.group(2), 1)


def load(board):
    lib, val = {}, {}
    for r in csv.DictReader(open(OUT/'schdoc_bom.csv', encoding='utf8')):
        if r['board'] == board:
            lib[r['designator']] = r['libref']
            val[r['designator']] = r['comment']
    pin_net, net_pins, net_name = {}, collections.defaultdict(list), {}
    for k, r in enumerate(csv.DictReader(open(OUT/'schdoc_nets.csv', encoding='utf8'))):
        if r['board'] != board:
            continue
        net_name[k] = r['net']
        for p in r['pins'].split():
            pin_net[p] = k
            net_pins[k].append(p)
    return lib, val, pin_net, net_pins, net_name


def graph(board):
    lib, val, pin_net, net_pins, net_name = load(board)
    rail = {k for k, n in net_name.items() if any(RAIL.search(x) for x in n.split('/'))}
    edges = collections.defaultdict(list)  # net -> [(other_net, kind, tag, gate_or_value)]
    for d, l in lib.items():
        if '168' in l.upper():
            for s, g, o in SECT:
                a, b, gn = pin_net.get('%s.%d' % (d, s)), pin_net.get('%s.%d' % (d, o)), pin_net.get('%s.%d' % (d, g))
                if a is not None and b is not None:
                    tag = '%s(%d-%d)' % (d, s, o)
                    edges[a].append((b, 'K', tag, net_name.get(gn, '?')))
                    edges[b].append((a, 'K', tag, net_name.get(gn, '?')))
        elif l.upper().startswith('R'):
            a, b = pin_net.get(d+'.1'), pin_net.get(d+'.2')
            if a is not None and b is not None:
                edges[a].append((b, 'R', d, val.get(d, '')))
                edges[b].append((a, 'R', d, val.get(d, '')))
    return net_name, net_pins, rail, edges


def trace(edges, rail, start, goal):
    """Shortest net-to-net walk from start to any net in goal, through >=1 switch, never through a rail."""
    seen, queue = {start}, [(start, [])]
    while queue:
        nxt = []
        for n, path in queue:
            for m, kind, tag, extra in edges[n]:
                if m in seen or m in rail:
                    continue
                p2 = path + [(kind, tag, extra, m)]
                if m in goal and any(x[0] == 'K' for x in p2):
                    return p2
                seen.add(m)
                nxt.append((m, p2))
        queue = nxt
    return []


def row(name, path, net_name, extra=None):
    sw = [x for x in path if x[0] == 'K']
    r = dict(input=name, levels=len(sw), packages=' > '.join(t.split('(')[0] for _, t, _, _ in sw),
             switches=' > '.join(t for _, t, _, _ in sw), gates=' > '.join(g for _, _, g, _ in sw),
             output=net_name[path[-1][3]] if path else '')
    r.update(extra or {})
    return r


def board02():
    net_name, net_pins, rail, edges = graph('A313-V.02')
    dc_nets = {k for k, ps in net_pins.items() if any(p.startswith('DC') for p in ps)}
    rows = []
    for k, name in net_name.items():
        if not name.startswith('vhod') or k not in dc_nets:
            continue
        path = trace(edges, rail, k, dc_nets - {k})
        # divider: series R from the input, shunt R from the first node to a rail
        series = [x for x in path if x[0] == 'R'][:1]
        ratio = None
        if series:
            node = series[0][3]
            shunt = [(t, e) for m, kd, t, e in edges[node] if kd == 'R' and m in rail and t != series[0][1]]
            rs, rp = ohms(series[0][2]), ohms(shunt[0][1]) if shunt else None
            if rs and rp:
                ratio = rp / (rs + rp)
        rows.append(row(name, path, net_name, dict(
            series_R='%s=%s' % (series[0][1], series[0][2]) if series else '',
            divider=round(ratio, 4) if ratio else '')))
    return rows


def board05():
    net_name, net_pins, rail, edges = graph('A313-V.05')
    by = {n: k for k, n in net_name.items()}
    src = {by['a pr'], by['b pr']}
    fb = {by['OC"a"'], by['OC"b"']}
    caps = collections.defaultdict(list)
    for k, ps in net_pins.items():
        caps[net_name[k]] += [p.split('.')[0] for p in ps if p.startswith('C')]
    rows = []
    for k, name in net_name.items():
        if not re.fullmatch(r'vih\.\d+[ab]=', name):
            continue
        # storage cell: the output is the source of 168КТ2 sections whose other end is a rail
        # (source followers); their common gate net holds the 4,7 µF cap and is written via the demux
        fol = [(t, g) for m, kd, t, g in edges[k] if kd == 'K' and m in rail]
        gate = {g for _, g in fol}
        w = trace(edges, rail, by[gate.pop()], src) if len(gate) == 1 else []
        r = trace(edges, rail, k, fb)    # read-back path to ОС a/б
        rows.append(row(name, w, net_name, dict(
            follower=' '.join(t for t, _ in fol), cap=' '.join(sorted(c for c in caps.get(fol[0][1], []))) if fol else '',
            readback=' > '.join(t for kd, t, _, _ in r if kd == 'K'), readback_to=net_name[r[-1][3]] if r else '')))
    return rows


def write(rows, fname):
    rows.sort(key=lambda r: (re.sub(r'\d+', '', r['input']), int((re.findall(r'\d+', r['input']) or ['0'])[0])))
    with open(OUT/fname, 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    share = collections.defaultdict(list)
    for r in rows:
        for lvl, p in enumerate(r['packages'].split(' > ')):
            if p:
                share[(lvl+1, p)].append(r['input'])
    print('==', fname)
    for (lvl, p), ins in sorted(share.items()):
        print('L%d %-4s %2d: %s' % (lvl, p, len(ins), ' '.join(ins)))


def main():
    assert ohms('10k') == 1e4 and ohms('2,05k') == 2050 and ohms('330') == 330
    r02 = board02()
    assert len(r02) == 48 and all(r['levels'] == 3 for r in r02), 'expected 32 analog + 16 PK inputs, 3 switch levels'
    write(r02, 'mux_tree_02.csv')
    r05 = board05()
    write(r05, 'mux_tree_05.csv')
    assert len(r05) == 48 and all(r['levels'] == 3 and r['readback_to'] for r in r05), 'expected 48 cells, 3-level write path, read-back'
    fol = collections.defaultdict(list)  # follower package -> channels (each channel uses 2 packages)
    for r in r05:
        for f in r['follower'].split():
            fol[f.split('(')[0]].append(r['input'][4:-1])
    assert len(fol) == 24 and all(len(v) == 4 for v in fol.values()) and fol['U2'] == ['1a', '2a', '5a', '6a']
    print('followers:', dict(sorted(fol.items(), key=lambda x: int(x[0][1:]))))
    for r in r05:
        print('%-9s w: %-30s %-26s | fol %-22s %-4s | r: %s -> %s' % (r['input'], r['switches'], r['gates'], r['follower'], r['cap'], r['readback'], r['readback_to']))


if __name__ == '__main__':
    main()
