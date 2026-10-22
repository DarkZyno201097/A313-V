"""Corrections to the Э4/Y16 transcription found by e4_check.py and confirmed on the photos.

Run from project root BEFORE e4_check.py:  python tmp/pdfs/review/a313-3/e4_sua.py
Idempotent: each fix asserts the cell holds either the old or the new value. The note column
records the original reading, so the CSV stays traceable to the drawing.
"""
import csv
from pathlib import Path

DIR = Path('tmp/pdfs/review/a313-3/e4')
# (page, table, pin, field, old, new, reason)
FIX = [
    (143, 'У24', '14', 'address', 'У20/2, У16КП1/16', 'У20/2, У16КП1/6', 'КП1/6 «+6,3В»→У24/14; КП1/16 là ЗАПРЕТ ОБРАЩ.'),
    (145, 'У16КП2', '93', 'address', 'У23/1;3Ш3В/56', 'У23/7;3Ш3В/56', 'У23/7 «+3,5В»→КП2/93; У23/1 là КОРПУС'),
    (147, '3Ш4', '49', 'address', 'У24/19 20', 'У24/17', 'У24/17 «ИСПР.ПИТ»→3Ш4/49 (ảnh #140)'),
    (150, 'У1П1', '26', 'address', '3Ш4В/3', '3Ш4В/38', '3Ш4В/38 «ВХОД ПК3(М)»→У1П1/26; 3Ш4В/3 thuộc У1П1/30'),
    (142, 'У21', '3', 'address', 'У3/28;У24/9', 'У13/28;У24/9', 'У13/28 «−23В»→У21/3'),
    (145, 'У16КП2', '4', 'address', '3Ш7/31', '3Ш7/37', '3Ш7/37 «УПР.К4»→КП2/4 (ảnh #144); 3Ш7/31 là УПР(−20В)'),
    (143, 'У24', '4', 'address', 'Э5/18', '3Ш5/18', 'ảnh #140 đọc «3Ш5/18»'),
    # pin «Б» of У12/У13 is written like the digit 6 (ảnh #146)
    (146, '3Ш3В', '64', 'address', '3Ш3/64;У12/5', '3Ш3/64;У12/Б', 'У12/Б «+6,3В»→3Ш3В/64; У12/5 là Вход 9б'),
    (149, 'У12', 'Б', 'address', 'У13/6;3Ш3В/64', 'У13/Б;3Ш3В/64', 'chân Б viết giống số 6'),
    (149, 'У13', 'Б', 'address', 'У12/6, У23/8', 'У12/Б, У23/8', 'chân Б viết giống số 6'),
    (144, 'У20', '2', 'address', 'У13/6; У24/14', 'У13/Б; У24/14', 'chân Б viết giống số 6'),
    (150, 'У16КП11', '48', 'signal', 'К⇒РН', 'М⇒РМ', 'ma trận tr.153 cột 45: П8/48–П11/48 «М⇒РМ»; КП8/48 «М⇒РМ»'),
    (150, 'У16КП11', '21', 'signal', '¬СВНвх', '¬СВК БК', 'ma trận tr.154 cột 12: П3/26–П11/21; КП3/26 «СВК БК» → 3Ш4В/49'),
    (147, '3Ш4В', '20', 'signal', '¬СБК1-1', '¬СВК1-1', 'như 3Ш4В/25, 30, 35 và TMKT A313-V «СВК1-1»; В đọc nhầm Б'),
]


def main():
    by_page = {}
    for f in FIX:
        by_page.setdefault(f[0], []).append(f)
    done = 0
    for page, fixes in by_page.items():
        path = DIR / ('p%d.csv' % page)
        rows = list(csv.DictReader(open(path, encoding='utf8')))
        for _, table, pin, field, old, new, why in fixes:
            hit = [r for r in rows if r['table'] == table and r['pin'].strip() == pin]
            assert len(hit) == 1, (page, table, pin, len(hit))
            r = hit[0]
            assert r[field] in (old, new), (page, table, pin, r[field])
            if r[field] == old:
                r[field] = new
                r['note'] = ('%s | SỬA (e4_sua.py): gốc đọc «%s»; %s' % (r['note'], old, why)).lstrip(' |')
                done += 1
        with open(path, 'w', newline='', encoding='utf8') as f:
            w = csv.DictWriter(f, list(rows[0]))
            w.writeheader()
            w.writerows(rows)
    print('fixed', done, 'of', len(FIX), '(rest already applied)')


if __name__ == '__main__':
    main()
