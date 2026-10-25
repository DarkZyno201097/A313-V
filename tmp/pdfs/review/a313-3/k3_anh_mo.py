"""Rà ảnh sơ đồ trong A313-3_CONTROL/Y* : độ nét (cùng thước đo k3_kiemke.sharpness), kích thước,
và đếm dòng «?» / placeholder trong ricNN_net.csv. In bảng để quyết định ảnh nào cần chụp lại.
Chạy: python -B tmp/pdfs/review/a313-3/k3_anh_mo.py  (từ gốc repo)"""
import csv, re, sys
from pathlib import Path
from PIL import Image, ImageOps
sys.path.insert(0, str(Path(__file__).parent))
from k3_kiemke import sharpness
try:
    import pillow_heif; pillow_heif.register_heif_opener()  # vài ảnh .jpg thực chất là HEIC
except ImportError:
    pass

ROOT = Path(__file__).resolve().parents[4]
CTRL, E3 = ROOT / 'A313-3_CONTROL', Path(__file__).parent / 'e3'
RIC = {'Y1': ['ric10'], 'Y2': ['ric09'], 'Y3': ['ric06'], 'Y4': ['ric05'], 'Y5': ['ric08'], 'Y6': ['ric07'],
       'Y7': ['ric11'], 'Y8': ['ric16'], 'Y9': ['ric15'], 'Y10': ['ric18'], 'Y11': ['ric17'],
       'Y12': ['ric14'], 'Y13': ['ric14'], 'Y14': ['ric12_13'], 'Y15': ['ric12_13'], 'Y17': ['ric25'],
       'Y18': ['ric20'], 'Y19': ['ric23'], 'Y20': ['ric21'], 'Y21': ['ric22'], 'Y22': ['ric26'],
       'Y23': ['ric24'], 'Y24': ['ric19']}


def net_stat(ric):
    p = E3 / f'{ric}_net.csv'
    if not p.exists():
        return None
    rows = [','.join(r) for r in list(csv.reader(open(p, encoding='utf-8-sig')))[1:]]
    q = sum('?' in r for r in rows)
    ph = sum(bool(re.search(r'placeholder|НЕ ПРОСЛЕЖЕНО|chưa truy', r, re.I)) for r in rows)
    return len(rows), q, ph


def main():
    assert sharpness(Image.new('L', (64, 64))) == 0.0
    for d in sorted((p for p in CTRL.iterdir() if p.is_dir()), key=lambda p: (len(p.name), p.name)):
        imgs = sorted(p for p in d.iterdir() if p.suffix.lower() in ('.jpg', '.jpeg', '.png'))
        stats = [net_stat(r) for r in RIC.get(d.name, [])]
        print(f'## {d.name}  net(dòng,«?»,placeholder)={stats}')
        for p in imgs:
            try:
                im = ImageOps.exif_transpose(Image.open(p))
            except Exception as e:
                print(f'   {p.name:40s} KHÔNG MỞ ĐƯỢC ({type(e).__name__})'); continue
            print(f'   {p.name:40s} {im.width}x{im.height}  sharp={sharpness(im):7.0f}')


if __name__ == '__main__':
    main()
