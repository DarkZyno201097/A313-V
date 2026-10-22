"""Dummy-load numbers for the stand-alone power test of the Soviet A-313-3 block.

Run from project root:  python tmp/pdfs/review/a313-3/k3_nguon.py
Source: A313 original/A-313-3.HDSDKT.pdf Bảng 3 (rails, rated load, tolerance) and §1.2
(27 V: 220 W; 36 V 400 Hz phases A, C: 6 W). Prints the table used in KE-HOACH_KIEM-TRA_A-313-3.md.
"""
RAILS = [  # (rail V, rated load A, tolerance as printed in Bảng 3, module)
    (+20.0, 0.30, '+1,00 V', 'ЕУ3.215.446'),
    (+12.6, 1.00, '±0,63 V', 'ЕУ3.215.452'),
    (+10.0, 0.20, '±0,5 V', 'ЕУ3.215.466'),
    (+6.3, 0.50, '±0,32 V', 'ЕУ3.215.448-01'),
    (+5.0, 15.0, '±0,26 V', 'ЕУ3.215.469'),
    (-23.0, 0.30, '+0,15/−0,5 V', 'ЕУ3.215.451-02'),
    (-12.6, 1.00, '±0,63 V', 'ЕУ3.215.470'),
    (-10.0, 0.25, '±0,5 V', 'ЕУ3.215.466'),
    (-6.3, 1.00, '±0,32 V', 'ЕУ3.215.469 (Bảng 3 in vậy)'),
]
E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]


def e12_above(r):
    """Smallest E12 value >= r (load never draws more than intended)."""
    d = 1.0
    while d * 10 <= r:
        d *= 10
    while d > r:
        d /= 10
    for k in (d, d * 10):
        for m in E12:
            if m * k >= r - 1e-9:
                return m * k
    raise ValueError(r)


def fmt(x, n=1):
    return ('%.*f' % (n, x)).replace('.', ',')


def main():
    assert e12_above(40) == 47 and e12_above(0.333) == 0.39 and e12_above(100) == 100
    rows = []
    for v, i, tol, mod in RAILS:
        r100 = abs(v) / i                 # load at rated current
        r25 = e12_above(4 * r100)         # first power-up: ≤ 25 % rated, rounded up to E12
        i25, p25 = abs(v) / r25, v * v / r25
        rows.append((v, i, tol, mod, r100, abs(v) * i, r25, i25, p25))
    assert abs(rows[4][4] - 5.0 / 15) < 1e-12 and abs(rows[4][5] - 75) < 1e-9   # +5 V 15 A: 0,333 Ω, 75 W
    assert rows[0][6] == 270 and rows[4][6] == 1.5                                # E12 picks
    total = sum(r[5] for r in rows)
    i27 = 220 / 27
    assert abs(i27 - 8.148) < 1e-3
    print('| Rail | I định mức | Dung sai | Module | R tải 100 % | P 100 % | R ≤ 25 % (E12) | I | P trên R |')
    print('|---|---|---|---|---|---|---|---|---|')
    for v, i, tol, mod, r100, p100, r25, i25, p25 in rows:
        print('| %s V | %s A | %s | %s | %s Ω | %s W | %s Ω | %s A | %s W |' % (
            fmt(v, 1), fmt(i, 2), tol, mod, fmt(r100, 2), fmt(p100, 1), fmt(r25, 2 if r25 < 10 else 0),
            fmt(i25, 3), fmt(p25, 2)))
    print('Tổng công suất ra định mức các rail: %s W; dòng 27 V ứng với 220 W: %s A' % (fmt(total, 1), fmt(i27, 2)))


if __name__ == '__main__':
    main()
