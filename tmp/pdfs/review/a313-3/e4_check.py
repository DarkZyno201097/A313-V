"""Cross-check the hand transcription of the Э4 / Y16 connection tables (ЕУ3.048.002 РЭ pages 142-157).

Run from project root:  python tmp/pdfs/review/a313-3/e4_check.py
Input:  tmp/pdfs/review/a313-3/e4/p*.csv  (page,photo,table,pin,signal,address,wire,note)
Every row "table T pin p -> address A/k" should be mirrored by a row "table A pin k -> T/p" when
table A was also transcribed. Mismatches point to a misread pin/address (or a real one-way entry).
Output: e4/e4_all.csv (merged, normalised keys) and e4/e4_mismatch.csv; summary on stdout.
"""
import csv
import re
from pathlib import Path

DIR = Path('tmp/pdfs/review/a313-3/e4')
LAT = str.maketrans('ABCEHKMOPTXYacekmoptxy3', 'АВСЕНКМОРТХУасекмортху3')


def key(s):
    """Normalise a table name / address target: Cyrillic letters, no spaces/dots, upper case."""
    return re.sub(r'[\s.]', '', (s or '').translate(LAT)).upper()


def parse_addr(a):
    """'У1П1/29' -> ('У1П1', 29); '3Ш3В/25' -> ('3Ш3В', 25); anything else -> None."""
    m = re.fullmatch(r'(.+?)/(\d+|[АБ])', key(a).rstrip('?'))
    return (m.group(1), pin(m.group(2))) if m else None


def pin(s):
    """Pins are numbers, except А/Б on the input-switch boards У12/У13."""
    return int(s) if s.isdigit() else s


def addrs(a):
    """A cell may hold several targets: 'У16КП2/50;У24/11;У15/1'."""
    return [p for p in map(parse_addr, re.split(r'[;,:]|\s+(?=[УКШ3Э])', a or '')) if p]


def resolve(t, tables):
    """Address spellings vs table titles: 'Ш5' = '3Ш5'; 'У14' = 'У14П1' when only П1 was drawn."""
    t = '3' + t if t.startswith('Ш') else 'У16' + t if t.startswith('КП') else t
    return t + 'П1' if t not in tables and t + 'П1' in tables else t


def main():
    assert parse_addr('у1 п1/29') == ('У1П1', 29) and parse_addr('3Ш3B/25') == ('3Ш3В', 25)
    assert parse_addr('КОРПУС') is None and parse_addr('У13/Б') == ('У13', 'Б')
    assert addrs('3Ш4/49 У16КП2/89') == [('3Ш4', 49), ('У16КП2', 89)]
    assert addrs('У16КП2/50;У24/11, У15/1') == [('У16КП2', 50), ('У24', 11), ('У15', 1)]
    assert resolve('Ш5', set()) == '3Ш5' and resolve('У14', {'У14П1'}) == 'У14П1' and resolve('У1П1', {'У1П1'}) == 'У1П1'
    rows = []
    for f in sorted(DIR.glob('p[0-9]*.csv')):
        for r in csv.DictReader(open(f, encoding='utf8')):
            p = key(r['pin'])
            if r['table'] == 'ПРИМЕЧ' or not (p.isdigit() or p in ('А', 'Б')):
                continue
            r['T'], r['P'] = key(r['table']), pin(p)
            if r['T'].startswith('?3Ш5'):  # left harness table of У17 3Ш5 has no own title
                r['T'] = '3Ш5'
            rows.append(r)
    idx = {}
    for r in rows:
        idx.setdefault((r['T'], r['P']), []).append(r)
    dup = {k: v for k, v in idx.items() if len(v) > 1}
    tables = {r['T'] for r in rows}
    bad, ok, oneway = [], 0, 0
    struck = [r for r in rows if re.search(r'зач[её]ркн|gạch (bỏ|xoá|xóa)|struck|crossed', r['note'] or '', re.I)]
    for r in rows:
        if r in struck:  # struck out on the drawing itself
            continue
        for t, k in addrs(r['address']):
            a = (resolve(t, tables), k)
            if a[0] not in tables:
                oneway += 1
                continue
            back = [(resolve(t2, tables), k2) for x in idx.get(a, []) for t2, k2 in addrs(x['address'])]
            if (r['T'], r['P']) in back:
                ok += 1
            else:
                bad.append(dict(table=r['table'], pin=r['P'], signal=r['signal'], address=r['address'], page=r['page'],
                                target_rows=' | '.join('%s→%s' % (x['signal'], x['address']) for x in idx.get(a, [])) or '(không có dòng)'))
    with open(DIR / 'e4_all.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, ['page', 'photo', 'table', 'pin', 'signal', 'address', 'wire', 'note'], extrasaction='ignore')
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: (r['T'], str(r['P']).zfill(3))))
    with open(DIR / 'e4_mismatch.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, ['table', 'pin', 'signal', 'address', 'page', 'target_rows'])
        w.writeheader()
        w.writerows(bad)
    print('rows', len(rows), 'tables', len(tables), ':', ' '.join(sorted(tables)))
    print('reciprocal ok', ok, '| mismatch', len(bad), '| target table not transcribed', oneway)
    print('struck-out rows skipped:', len(struck))
    print('duplicate (table,pin):', ' '.join('%s/%s' % k for k in sorted(dup)) or '-')
    print('rows marked ?:', sum('?' in (r['note'] or '') for r in rows))


if __name__ == '__main__':
    main()
