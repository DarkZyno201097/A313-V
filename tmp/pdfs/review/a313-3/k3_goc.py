"""Sheets of top-right corners (handwritten page number) for every photo, 24 per sheet.

Run from project root:  python tmp/pdfs/review/a313-3/k3_goc.py
Output: tmp/pdfs/review/a313-3/kiemke/goc_NN.jpg; label = index in kiemke.csv order + file name.
"""
import csv
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps
import pillow_heif

pillow_heif.register_heif_opener()
SRC = Path('ЕУ.048.002.РЭ_A313-3')
OUT = Path('tmp/pdfs/review/a313-3/kiemke')

rows = list(csv.DictReader(open(OUT / 'kiemke.csv', encoding='utf8')))
cells = []
for k, r in enumerate(rows, 1):
    im = ImageOps.exif_transpose(Image.open(SRC / r['file']))
    W, H = im.size
    crop = im.crop((int(W * 0.62), 0, W, int(H * 0.14))).convert('L')
    crop.thumbnail((440, 200))
    cells.append((k, r['file'], crop, W > H))
for s in range(0, len(cells), 24):
    sheet = Image.new('L', (4 * 450, 6 * 230), 255)
    d = ImageDraw.Draw(sheet)
    for j, (k, name, crop, land) in enumerate(cells[s:s + 24]):
        x, y = 450 * (j % 4), 230 * (j // 4)
        sheet.paste(crop, (x, y + 22))
        d.text((x + 2, y + 2), '#%d %s%s' % (k, name[9:15], ' NGANG' if land else ''), fill=0)
    sheet.save(OUT / ('goc_%02d.jpg' % (s // 24 + 1)), quality=85)
print(len(cells))
