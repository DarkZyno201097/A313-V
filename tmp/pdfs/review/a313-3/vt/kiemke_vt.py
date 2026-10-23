"""S01: kiểm kê PDF chỉ đọc; render bằng Poppler 120 dpi, giữ ghi chú đọc bằng mắt.

Chạy từ bất kỳ thư mục: python kiemke_vt.py [--render] [--check].
--render tạo ảnh còn thiếu; --check chỉ kiểm, không ghi. Cần pdfinfo/pdftoppm trên PATH.
trang_in/loai/tieu_de/ghi_chu được biên tập trong vt_pages.csv, không suy từ tên file.
"""
import argparse
import csv
import hashlib
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
BOOKS = {'VT34': 'SU-27-VT-34.44(A-313-3)', 'VT28': 'su-27-01-vt-28(A-313-3)'}
FILE_FIELDS = 'book file sha256 size_mb pdf_pages tu_trang den_trang so_trang_theo_ten lech'.split()
PAGE_FIELDS = 'book file pdf_page trang_in loai tieu_de anh_render ghi_chu'.split()
TYPES = {'bia', 'muc_luc', 'van_ban', 'hinh', 'bang', 'to_gap', 'trang_trang', 'khac'}


def digest(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def page_range(name):
    m = re.fullmatch(r'TR (\d+)(?:-(\d+))?\.pdf', name)
    return (int(m[1]), int(m[2] or m[1])) if m else (None, None)


def read_csv(path):
    if not path.exists():
        return []
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def dhash(path):
    from PIL import Image
    with Image.open(path) as image:
        pixels = list(image.convert('L').resize((17, 16)).get_flattened_data())
    return int(''.join('1' if pixels[y * 17 + x] > pixels[y * 17 + x + 1] else '0'
                       for y in range(16) for x in range(16)), 2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render', action='store_true')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--duplicates', action='store_true', help='In ứng viên dhash 256 bit; phải đối chiếu bằng mắt')
    args = parser.parse_args()
    assert not (args.render and args.check)
    assert page_range('TR 122-143.pdf') == (122, 143)
    assert page_range('TR 2.pdf') == (2, 2)
    assert page_range('1.pdf') == (None, None)
    old_files = read_csv(OUT / 'vt_files.csv')
    initial_pages = (OUT / 'vt_pages.csv').read_bytes() if (OUT / 'vt_pages.csv').exists() else None
    hashes = {(r['book'], r['file']): r['sha256'] for r in old_files}
    existing = read_csv(OUT / 'vt_pages.csv')
    pages = {(r['book'], r['file'], r['pdf_page']): r for r in existing}
    assert len(pages) == len(existing), 'Trùng khóa trang PDF'
    files, result, totals = [], [], Counter()
    for book, folder in BOOKS.items():
        base = ROOT / 'A313 original/a313' / folder
        sources = sorted(base.rglob('*.pdf'), key=lambda p: (len(p.relative_to(base).parts), page_range(p.name)[0] or 0, p.name))
        assert len(sources) == (13 if book == 'VT34' else 42), (book, len(sources))
        for source in sources:
            relative = source.relative_to(base).as_posix()
            sha = digest(source)
            if hashes:
                assert hashes.get((book, relative)) == sha, f'Nguồn thay đổi: {book}/{relative}'
            info = subprocess.check_output(['pdfinfo', str(source)]).decode('utf-8', errors='replace')
            count = int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1])
            start, end = page_range(source.name)
            nominal = end - start + 1 if start is not None else None
            files.append(dict(book=book, file=relative, sha256=sha,
                              size_mb=f'{source.stat().st_size / 1_000_000:.3f}'.replace('.', ','),
                              pdf_pages=str(count), tu_trang=str(start) if start else '', den_trang=str(end) if end else '',
                              so_trang_theo_ten=str(nominal) if nominal else '', lech=str(count-nominal) if nominal else ''))
            totals[book + ('_anh' if start is None else '')] += count
            slug = ('anh_' if start is None else '') + source.stem.replace(' ', '_')
            dest = OUT / 'render' / book / slug
            if args.render:
                dest.mkdir(parents=True, exist_ok=True)
            for number in range(1, count + 1):
                image = dest / f'p{number:03d}.png'
                if args.render and not image.exists():
                    subprocess.run(['pdftoppm', '-f', str(number), '-l', str(number), '-r', '120',
                                    '-singlefile', '-png', str(source), str(image.with_suffix(''))], check=True,
                                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
                key = (book, relative, str(number))
                row = pages.get(key, dict(book=book, file=relative, pdf_page=str(number), trang_in='',
                                         loai='khac', tieu_de='', anh_render='', ghi_chu='CHUA_XEM'))
                row['anh_render'] = image.relative_to(ROOT).as_posix()
                assert row['loai'] in TYPES, row
                if args.check or args.render:
                    assert image.is_file() and image.stat().st_size > 0, image
                result.append(row)
            assert digest(source) == sha, source
    assert totals == {'VT34': 252, 'VT34_anh': 7, 'VT28': 170}, totals
    assert len(result) == 252 + 170 + 7 == len({(r['book'], r['file'], r['pdf_page']) for r in result})
    if existing:
        assert set(pages) == {(r['book'], r['file'], r['pdf_page']) for r in result}
    if args.check:
        assert files == old_files and result == existing, 'CSV không khớp nguồn hoặc thứ tự'
        assert all('CHUA_XEM' not in r['ghi_chu'] for r in result), 'Còn trang chưa xem'
        assert all(not r['trang_in'] or re.fullmatch(r'\d+(?:/\d+)?', r['trang_in']) for r in result)
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        current_pages = (OUT / 'vt_pages.csv').read_bytes() if (OUT / 'vt_pages.csv').exists() else None
        assert current_pages == initial_pages, 'CSV đang được sửa bởi tiến trình khác; không ghi đè'
        write_csv(OUT / 'vt_files.csv', FILE_FIELDS, files)
        write_csv(OUT / 'vt_pages.csv', PAGE_FIELDS, result)
    print('FILES 55; SHA256 55/55; VT34 252 + ANH 7; VT28 170; PAGES 429; UNIQUE 429')
    print('CHUA_XEM', sum('CHUA_XEM' in r['ghi_chu'] for r in result))
    print('EMPTY_PRINTED_PAGE', dict(Counter(r['book'] for r in result if not r['trang_in'])))
    if args.duplicates:
        values = [dhash(ROOT / r['anh_render']) for r in result]
        def label(i):
            r = result[i]
            return f"{r['book']}/{r['file']} PDF {r['pdf_page']}"
        # shortcut: dhash toàn ảnh bỏ sót ảnh cắt/xoay; đối chiếu thủ công các tờ gấp trong báo cáo.
        for i, row in enumerate(result):
            if row['loai'] == 'trang_trang':
                continue
            for j in range(i + 1, len(result)):
                if row['book'] == result[j]['book'] and result[j]['loai'] != 'trang_trang':
                    distance = (values[i] ^ values[j]).bit_count()
                    if distance <= 24:
                        print('DHASH', distance, label(i), '<=>', label(j))
        for source, target in [('TR 2.pdf', 'TR 1-9.pdf'), ('TR 10.pdf', 'TR 10-23.pdf')]:
            i = next(i for i, r in enumerate(result) if r['book'] == 'VT28' and r['file'] == source)
            candidates = [(values[i] ^ values[j]).bit_count() for j, r in enumerate(result)
                          if r['book'] == 'VT28' and r['file'] == target]
            print('TARGET_MIN_DHASH', source, target, min(candidates))
    print('CHECK OK' if args.check else 'INVENTORY OK')


if __name__ == '__main__':
    main()
