"""Render the drawing crops cited as evidence in PHAN-TICH_TOAN-KHOI_A313-V.md.

Run from project root:  python tmp/pdfs/review/toan-khoi/tk_render.py   (needs poppler pdftoppm)
Crops are in PDF points (1/72 in) from the top-left corner; symbols are read at 400 dpi (CLAUDE.md §5).
"""
import subprocess
from pathlib import Path

OUT = Path('tmp/pdfs/review/toan-khoi')
BVTK = '1.BVTK A313-V/BVTK-A313-V_HS dau A.pdf'
A1 = 'A313 original/A-313-1ok.pdf'
CROPS = [  # name, pdf, page, dpi, (x, y, w, h) in pt or None for full page
    ('bv01_so-do-chuc-nang', BVTK, 5, 110, None),           # A313-12 36V/400Hz -> .10 -> 5V\400Hz -> .06
    ('bv42_tam-linh-kien-roi', BVTK, 48, 100, None),        # no transformer on A313-V.10
    ('bv38_diem-do-nguon', BVTK, 44, 400, (75, 30, 80, 310)),   # power test points on A313-V.09
    ('bv06_kenh-9-13', BVTK, 12, 400, (480, 200, 110, 110)),    # input dividers, values not printed
    ('a313-1_bang12', A1, 45, 150, (0, 60, 595, 370)),          # self-test word ОЗУ 367₈
]


def main():
    for name, pdf, page, dpi, box in CROPS:
        cmd = ['pdftoppm', '-r', str(dpi), '-f', str(page), '-l', str(page), '-png', '-singlefile']
        if box:
            k = dpi / 72
            cmd += ['-x', str(int(box[0]*k)), '-y', str(int(box[1]*k)), '-W', str(int(box[2]*k)), '-H', str(int(box[3]*k))]
        subprocess.run(cmd + [pdf, str(OUT/name)], check=True)
        assert (OUT/(name+'.png')).stat().st_size > 1000, name
        print(name + '.png')


if __name__ == '__main__':
    main()
