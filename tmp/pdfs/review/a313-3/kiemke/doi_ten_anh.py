"""R01: dry-run mặc định; --apply ghi ánh xạ, git mv và kiểm SHA-256.

Chạy lại sau gián đoạn dùng _DOI-TEN.csv, không ghi đè bằng chứng tên cũ.
Chỉ đổi tên ảnh; cập nhật tham chiếu là bước riêng của nhiệm vụ R01.
"""
import argparse
import csv
import hashlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SRC = ROOT / 'ЕУ.048.002.РЭ_A313-3'
TABLE = Path(__file__).with_name('trang.csv')
MAPPING = SRC / '_DOI-TEN.csv'
FIELDS = ['idx', 'ten_cu', 'ten_moi', 'page', 'sha256']


def sha256(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def new_name(row, suffix):
    page = row['page']
    assert not page or (page.isascii() and page.isdigit() and 0 < int(page) < 1000), row
    idx = int(row['idx'])
    assert 0 < idx < 1000 and suffix in ('.jpg', '.heic'), row
    page = f'{int(page):03d}' if page else 'XXX'
    extra = '_x' if row['kind'] == 'X' else ''
    return f'RE_tr{page}_a{idx:03d}{extra}{suffix}'


def plan():
    with TABLE.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 249
    assert {int(r['idx']) for r in rows} == set(range(1, 250))
    assert len({r['file'].casefold() for r in rows}) == len(rows)
    assert {int(r['idx']) for r in rows if r['kind'] == 'X'} == {185, 194, 197, 198, 240}
    saved = {}
    if MAPPING.exists():
        with MAPPING.open(encoding='utf-8', newline='') as f:
            manifest = list(csv.DictReader(f))
        assert len(manifest) == 249
        saved = {int(r['idx']): r for r in manifest}
        assert set(saved) == set(range(1, 250))
    result, actual = [], []
    for row in sorted(rows, key=lambda r: int(r['idx'])):
        idx = int(row['idx'])
        old = saved[idx]['ten_cu'] if saved else row['file']
        assert Path(old).name == old and re.fullmatch(r'\d{8}_\d{6}\.(jpg|heic)', old), old
        new = new_name(row, Path(old).suffix)
        assert row['file'] in (old, new), row
        present = [name for name in (old, new) if (SRC / name).is_file()]
        assert len(present) == 1, (idx, present)
        digest = sha256(SRC / present[0])
        entry = dict(idx=str(idx), ten_cu=old, ten_moi=new, page=row['page'], sha256=digest)
        if saved:
            assert entry == saved[idx], f'Ánh xạ hoặc SHA-256 sai: #{idx}'
        result.append(entry)
        actual.append(present[0])
    assert len({r['ten_moi'].casefold() for r in result}) == 249
    assert {p.name for p in SRC.iterdir() if p.name != MAPPING.name} == set(actual), 'Thư mục và trang.csv không khớp 1:1'
    tracked = subprocess.check_output(['git', 'ls-files', '-z', '--', SRC.relative_to(ROOT).as_posix()], cwd=ROOT).decode('utf-8').split('\0')
    assert all((SRC / name).relative_to(ROOT).as_posix() in tracked for name in actual), 'Ảnh chưa được Git theo dõi'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Ghi ánh xạ và đổi tên bằng git mv')
    args = parser.parse_args()
    assert new_name(dict(idx='167', page='171', kind='S'), '.jpg') == 'RE_tr171_a167.jpg'
    assert new_name(dict(idx='185', page='', kind='X'), '.heic') == 'RE_trXXX_a185_x.heic'
    entries = plan()
    print('idx | ten_cu -> ten_moi')
    for r in entries:
        print(f"{r['idx']:>3} | {r['ten_cu']} -> {r['ten_moi']}")
    if not args.apply:
        print('DRY-RUN: 249 ảnh; ánh xạ 1:1; tên mới duy nhất; không ghi file.')
        return
    if not MAPPING.exists():
        with MAPPING.open('x', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, FIELDS)
            writer.writeheader()
            writer.writerows(entries)
    moved = 0
    for r in entries:
        old, new = SRC / r['ten_cu'], SRC / r['ten_moi']
        if old.exists():
            subprocess.run(['git', 'mv', '--', str(old.relative_to(ROOT)), str(new.relative_to(ROOT))], cwd=ROOT, check=True)
            moved += 1
        assert sha256(new) == r['sha256'], f"SHA-256 thay đổi: #{r['idx']}"
    assert plan() == entries
    print(f'APPLY: đổi tên {moved}; SHA-256 khớp 249/249; _DOI-TEN.csv: 249 dòng.')


if __name__ == '__main__':
    main()
