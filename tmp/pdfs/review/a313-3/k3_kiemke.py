"""Inventory of the paper-copy photos of ЕУ3.048.002 РЭ (A-313-3).

Run from project root:  python tmp/pdfs/review/a313-3/k3_kiemke.py
Outputs (tmp/pdfs/review/a313-3/kiemke/):
  kiemke.csv        file, w, h, MB, sharpness, dhash, duplicate group
  sheet_NNN.jpg     contact sheets (6 per sheet: whole photo thumbnail + 4 corner crops) for reading page numbers
Photos are read-only; nothing in the photo folder is modified.
"""
import csv
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:  # HEIC files are then reported as unreadable
    pass

SRC = Path('ЕУ.048.002.РЭ_A313-3')
OUT = Path('tmp/pdfs/review/a313-3/kiemke')


def dhash(img, n=16):
    g = np.asarray(img.convert('L').resize((n + 1, n)), dtype=np.int16)
    return int(''.join('1' if b else '0' for b in (g[:, 1:] > g[:, :-1]).flatten()), 2)


def sharpness(img):
    g = np.asarray(img.convert('L').resize((1200, int(1200 * img.height / img.width))), dtype=np.float32)
    lap = g[1:-1, 1:-1] * 4 - g[:-2, 1:-1] - g[2:, 1:-1] - g[1:-1, :-2] - g[1:-1, 2:]
    return float(lap.var())


def main():
    assert bin(dhash(Image.new('L', (40, 40)))).count('1') == 0
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in SRC.iterdir() if p.suffix.lower() in ('.jpg', '.jpeg', '.heic'))
    rows, thumbs = [], []
    for p in files:
        try:
            im = ImageOps.exif_transpose(Image.open(p))
        except Exception as e:  # noqa: BLE001
            rows.append(dict(file=p.name, w='', h='', MB=round(p.stat().st_size / 1e6, 2), sharp='', dhash='', note='LOI: %s' % e))
            continue
        rows.append(dict(file=p.name, w=im.width, h=im.height, MB=round(p.stat().st_size / 1e6, 2),
                         sharp=round(sharpness(im)), dhash='%064x' % dhash(im), note=''))
        # contact cell: thumbnail + 4 corners (page numbers sit in a corner)
        W, H = im.size
        c = int(min(W, H) * 0.22)
        corners = [im.crop(b).resize((300, 300)) for b in
                   ((0, 0, c, c), (W - c, 0, W, c), (0, H - c, c, H), (W - c, H - c, W, H))]
        cell = Image.new('RGB', (900, 640), 'white')
        th = im.copy()
        th.thumbnail((300, 620))
        cell.paste(th, (0, 10))
        for k, cr in enumerate(corners):
            cell.paste(cr, (300 + 300 * (k % 2), 20 * 0 + 320 * (k // 2)))
        thumbs.append((p.name, cell))
    # duplicate groups: dhash Hamming distance <= 40 of 256 bits
    for r in rows:
        r['group'] = ''
    g = 0
    for i, a in enumerate(rows):
        if not a['dhash'] or a['group']:
            continue
        mem = [a]
        for b in rows[i + 1:]:
            if b['dhash'] and not b['group'] and bin(int(a['dhash'], 16) ^ int(b['dhash'], 16)).count('1') <= 40:
                mem.append(b)
        if len(mem) > 1:
            g += 1
            for m in mem:
                m['group'] = 'G%03d' % g
    with open(OUT / 'kiemke.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.DictWriter(f, list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    from PIL import ImageDraw
    for s in range(0, len(thumbs), 6):
        sheet = Image.new('RGB', (1800, 3 * 680), 'white')
        d = ImageDraw.Draw(sheet)
        for k, (name, cell) in enumerate(thumbs[s:s + 6]):
            x, y = 900 * (k % 2), 680 * (k // 2)
            sheet.paste(cell, (x, y + 30))
            d.text((x + 5, y + 5), '%d  %s' % (s + k + 1, name), fill='red')
        sheet.save(OUT / ('sheet_%03d.jpg' % (s // 6 + 1)), quality=80)
    print(len(rows), 'files;', sum(1 for r in rows if r['note']), 'unreadable;', g, 'duplicate groups')


if __name__ == '__main__':
    main()
