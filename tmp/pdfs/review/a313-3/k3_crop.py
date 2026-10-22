"""Crop regions of the ЕУ3.048.002 РЭ photos for reading by eye.

Run from project root:
    python tmp/pdfs/review/a313-3/k3_crop.py OUT.jpg IDX[:x0,y0,x1,y1] [IDX[:box] ...] [--w 1600]
IDX is the 1-based index in kiemke/kiemke.csv (sorted file names); box is in fractions of the
upright photo (default whole photo). Several crops are stacked vertically into OUT.jpg.
Photos are read-only; only OUT.jpg is written.
"""
import csv
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

SRC = Path('ЕУ.048.002.РЭ_A313-3')
FILES = [r['file'] for r in csv.DictReader(open('tmp/pdfs/review/a313-3/kiemke/kiemke.csv', encoding='utf8'))]


def crop(idx, box=(0, 0, 1, 1)):
    im = ImageOps.exif_transpose(Image.open(SRC / FILES[idx - 1])).convert('RGB')
    W, H = im.size
    return im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))


def main(argv):
    width = 1600
    if '--w' in argv:
        k = argv.index('--w')
        width = int(argv[k + 1])
        del argv[k:k + 2]
    out, specs = argv[0], argv[1:]
    tiles = []
    for s in specs:
        idx, _, b = s.partition(':')
        box = tuple(float(v) for v in b.split(',')) if b else (0, 0, 1, 1)
        assert len(box) == 4 and 0 <= box[0] < box[2] <= 1 and 0 <= box[1] < box[3] <= 1, s
        c = crop(int(idx), box)
        c = c.resize((width, max(1, int(c.height * width / c.width))))
        tiles.append(('#%s %s' % (idx, FILES[int(idx) - 1]), c))
    sheet = Image.new('RGB', (width, sum(t.height + 24 for _, t in tiles)), 'white')
    d, y = ImageDraw.Draw(sheet), 0
    for label, t in tiles:
        d.text((4, y + 4), label, fill='red')
        sheet.paste(t, (0, y + 24))
        y += t.height + 24
    sheet.save(out, quality=85)


if __name__ == '__main__':
    assert len(FILES) == 249
    main(sys.argv[1:])
