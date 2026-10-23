"""Kiểm các chốt bảo vệ R01 bằng dữ liệu giả, không động ảnh gốc."""
import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import doi_ten_anh as rename


class RenameTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.src = self.root / 'photos'
        self.src.mkdir()
        self.table = self.root / 'trang.csv'
        self.rows = []
        for idx in range(1, 250):
            name = f'20000101_{idx:06d}.jpg'
            (self.src / name).write_bytes(f'photo {idx}'.encode())
            self.rows.append(dict(idx=str(idx), file=name, page='',
                                  kind='X' if idx in {185, 194, 197, 198, 240} else 'S'))
        self.write_table()
        for key, value in dict(ROOT=self.root, SRC=self.src, TABLE=self.table,
                               MAPPING=self.src / '_DOI-TEN.csv').items():
            p = patch.object(rename, key, value)
            p.start()
            self.addCleanup(p.stop)
        p = patch.object(rename.subprocess, 'check_output', side_effect=lambda *a, **k:
                         '\0'.join('photos/' + f.name for f in self.src.iterdir()).encode())
        p.start()
        self.addCleanup(p.stop)

    def write_table(self):
        with self.table.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, ['idx', 'file', 'page', 'kind'])
            w.writeheader()
            w.writerows(self.rows)

    def test_names_and_invalid_page(self):
        self.assertEqual(rename.new_name(dict(idx='167', page='171', kind='S'), '.jpg'), 'RE_tr171_a167.jpg')
        self.assertEqual(rename.new_name(dict(idx='185', page='', kind='X'), '.heic'), 'RE_trXXX_a185_x.heic')
        with self.assertRaises(AssertionError):
            rename.new_name(dict(idx='1', page='171?', kind='S'), '.jpg')

    def test_duplicate_and_missing(self):
        self.assertEqual(len(rename.plan()), 249)
        self.rows[1]['file'] = self.rows[0]['file']
        self.write_table()
        with self.assertRaises(AssertionError):
            rename.plan()

    def test_missing_and_destination_collision(self):
        p = self.src / self.rows[0]['file']
        data = p.read_bytes()
        p.unlink()
        with self.assertRaises(AssertionError):
            rename.plan()
        p.write_bytes(data)
        (self.src / 'RE_trXXX_a001.jpg').write_bytes(data)
        with self.assertRaises(AssertionError):
            rename.plan()

    def test_resume_and_hash_mismatch(self):
        entries = rename.plan()
        with rename.MAPPING.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, rename.FIELDS)
            w.writeheader()
            w.writerows(entries)
        first = entries[0]
        new = self.src / first['ten_moi']
        (self.src / first['ten_cu']).rename(new)
        self.assertEqual(rename.plan(), entries)
        new.write_bytes(b'changed')
        with self.assertRaises(AssertionError):
            rename.plan()


if __name__ == '__main__':
    unittest.main()
