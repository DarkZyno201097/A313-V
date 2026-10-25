"""Kho tri thức A313: sinh phần AUTO của trang tấm + bảng trong 00_INDEX.md, rồi kiểm liên kết.

Chạy từ gốc repo:  python KHO-TRI-THUC_A313/tools/kb_check.py
Thoát mã 0 khi: không liên kết hỏng, mọi ảnh trong A313-3_CONTROL/ và mọi ric*_mota.md đều được kho nhắc tới.
Chạy lại không đổi file nếu dữ liệu nguồn không đổi.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / 'KHO-TRI-THUC_A313'
CTRL = ROOT / 'A313-3_CONTROL'
E3 = ROOT / 'tmp/pdfs/review/a313-3/e3'
AUTO = '<!-- AUTO: sinh bởi tools/kb_check.py, không sửa tay dưới dòng này -->'

# Y, tên Nga, số hiệu, рис. (Э3), tiền tố file ric, tương đương A313-V, vai trò [nguồn]
TAM = [
    ('Y1', 'Формирователь ПК и магистрали', 'ЕУ2.035.587', '10', 'ric10', '.01 (FPGA)',
     'Tạo và thu mã nối tiếp ПК từ thanh ghi РПР; điều khiển bus chính КШЗп/КШЧт sang A-313-2A [HDSD A-313-3 §2.2.1].'),
    ('Y2', 'Преобразователь цифровых сигналов', 'ВШ3.036.056', '9', 'ric09', '.01 (FPGA)',
     'Biến đổi tín hiệu số: tần số / cự ly → mã (bộ đếm СчД) [HDSD A-313-3 §2.2.1; KE-HOACH §1.1].'),
    ('Y3', 'Устройство управления обращением', 'ЕУ3.057.136', '6', 'ric06', '.01 (FPGA)',
     'Điều khiển giao tiếp: yêu cầu ЗпУВВ/ЧтУВВ, địa chỉ КША, tín hiệu chọn kênh К/Т/t, СИ, СВК, СПК, КША7–15 [HDSD; ric06_mota].'),
    ('Y4', 'Устройство программного управления', 'ЕУ3.057.138', '5', 'ric05', '.01 (FPGA)',
     'Điều khiển chương trình: bộ đếm lệnh СчК + máy phát xung nhịp (Пэ1 2620,91 кГц); tạo chu kỳ, 0оп–7оп, nhịp 1t/2t, '
     'ВрМ1/ВрМ2, strobe, thanh ghi М0–М15 [HDSD; ric05_mota].'),
    ('Y5', 'Устройство командного управления', 'ЕУ3.057.139', '8', 'ric08', '.01 (FPGA)',
     'Điều khiển lệnh: thanh ghi РгК1, РгК2, РгПр, РРК1/2; thu lệnh đơn TTL [HDSD; KE-HOACH §1.1].'),
    ('Y6', 'Устройство управления преобразованием', 'ЕУ3.057.140', '7', 'ric07', '.01 (FPGA)',
     'Điều khiển biến đổi: thanh ghi РПР 16 bit (4 cụm Я1–Я4) và РМ (Я5–Я6); điều khiển mã hoá/giải mã [HDSD §2.2.1].'),
    ('Y7', 'Плата согласования', 'ВШ3.031.020', '11', 'ric11', '.01 (◐)',
     'Tấm phối hợp mức tín hiệu vào/ra [HDSD; ric11_mota]. Bản vẽ lắp ráp рис.27.'),
    ('Y8', 'Преобразователь', 'ЕУ3.036.157', '16', None, '.04 (cùng topo, cùng số hiệu)',
     'Bộ biến đổi tương tự–số / số–tương tự (so sánh, bộ phối hợp) [HDSD §2.2.2; KE-HOACH §1.4].'),
    ('Y9', 'Интеграторы', 'ЕУ3.072.043', '15', 'ric15', '.03',
     'Các bộ tích phân có nhớ + tầng mux K, tích phân trước mã hoá [HDSD; ric15_mota].'),
    ('Y10', 'Усилители выходные', 'ЕУ2.032.463', '18', 'ric18', '.06 (cùng topo)',
     'Khuếch đại cửa ra 16 kênh, điều chế 400 Hz cho СКТ [HDSD; KE-HOACH §1.2].'),
    ('Y11', 'Коммутатор выходной', 'ЕУ2.242.113', '17', 'ric17', '.05',
     'Chuyển mạch cửa ra / bộ nhớ tương tự 49 ô (Выход 1а…24а) [HDSD; ric17_mota].'),
    ('Y12', 'Коммутатор входной (1)', 'ЕУ3.628.121 ⚠', '14', 'ric14', '.02 (◐)',
     'Chuyển mạch cửa vào: chọn kênh СКТ / điện áp tương đối / lệnh đơn đưa vào tích phân [HDSD; ric14_mota]. '
     'Số hiệu Y12/Y13 ghi ngược nhau giữa bảng 6 và danh mục hình 3.'),
    ('Y13', 'Коммутатор входной (2)', 'ЕУ3.628.122 ⚠', '14', 'ric14', '.02 (◐)',
     'Như Y12 (dùng chung рис.14) [ric14_mota].'),
    ('Y14', 'Преобразователь РК I', 'ВШ2.068.054', '13', 'ric12_13', '.07',
     'Lệnh đơn ra: 16 kênh +27 V qua rơ-le [HDSD; ric12_13_mota].'),
    ('Y15', 'Преобразователь РК II', 'ВШ2.068.054-01', '12', 'ric12_13', '.07',
     'Lệnh đơn ra: 16 kênh nối mát (colector hở) [HDSD; ric12_13_mota].'),
    ('Y16', 'Плата коммутационная', 'ЕУ3.661.064', '— (Э3 ma trận)', None, '.09',
     'Tấm sườn KHÔNG linh kiện: nối đầu cắm ngoài 3Ш1…3Ш7 với các tấm qua cáp dẹt. Bảng nối: Э4 + ma trận Y16 '
     '[xác nhận người dùng; SO-DO-DAU-NOI_E4_A-313-3.md].'),
    ('Y17', 'УЛП 5 В; 15 А', 'ЕУ3.215.469', '25', 'ric25', '.08.01',
     'Nguồn +5 V 15 A (cắm-rút được). Có Тр1 ТН-12-40-400 hạ ~36 V → ~5 V 400 Hz làm chuẩn [ric25_mota; SO-DO-NGUON].'),
    ('Y18', 'УЛП +20 В; 0,3 А', 'ЕУ3.215.446', '20', 'ric20', '.08.01', 'Nguồn +20 V 0,3 A [ric20_mota].'),
    ('Y19', 'УЛП +12,6 В; 1 А', 'ЕУ3.215.452', '23', 'ric23', '.08.01', 'Nguồn +12,6 V 1 A [ric23_mota].'),
    ('Y20', 'УЛП 6,3 В; 0,5 А', 'ЕУ3.215.448-01', '21', 'ric21', '.08.01', 'Nguồn +6,3 V 0,5 A [ric21_mota].'),
    ('Y21', 'УЛП −23 В; 0,3 А', 'ЕУ3.215.451-02', '22', 'ric22', '.08.01',
     'Nguồn −23 V (điều khiển khoá tương tự). Bản vẽ là −20 В, khối lắp −02 (−23 В) [ric22_mota].'),
    ('Y22', 'УЛП −12,6 В; 1 А', 'ЕУ3.215.470', '26', 'ric26', '.08.01', 'Nguồn −12,6 V 1 A (buck-boost đảo) [ric26_mota].'),
    ('Y23', 'УЛП ±10 В; 0,2 А', 'ЕУ3.215.466', '24', 'ric24', '.08.01', 'Nguồn ±10 V 0,2 A, kèm −5 V và +3,5 V [ric24_mota].'),
    ('Y24', 'Плата контроля и сигнализации', 'ЕУ3.215.139 ⚠', '19', 'ric19', '.08.02',
     'Kiểm tra các nguồn thứ cấp và báo hỏng. Số hiệu khác nhau giữa bảng 7 và danh mục hình 3 [ric19_mota].'),
]
ASK = [  # «hỏi gì đọc đâu»
    ('Thiết bị A-313 gồm gì, làm gì', 'tong-quan/A-313_thiet-bi.md'),
    ('Khối A-313-3 hoạt động thế nào (chu kỳ, СчК, ПК)', 'tong-quan/A-313-3_khoi.md'),
    ('Một tấm Y cụ thể: vai trò, ảnh, netlist, tình trạng', 'tam/Y01.md … tam/Y24.md (bảng tấm bên dưới)'),
    ('Kết nối giữa đầu cắm và các tấm (Э4, Y16)', '../SO-DO-DAU-NOI_E4_A-313-3.md'),
    ('Phần nguồn Y17–Y24, ~5 V 400 Hz', '../SO-DO-NGUON_A-313-3.md'),
    ('Kế hoạch kiểm tra / sửa chữa A-313-3', '../KE-HOACH_KIEM-TRA_A-313-3.md'),
    ('Danh mục ảnh bản giấy (trang ↔ ảnh ↔ рис.)', '../DANH-MUC_ANH_RE_A-313-3.md'),
    ('Khối mới A313-V, toàn khối', '../PHAN-TICH_TOAN-KHOI_A313-V.md'),
    ('Excel kết nối / danh mục tấm', '../Excel center control/'),
    ('Trạng thái phiên làm việc gần nhất', '../PROJECT_HANDOFF.md'),
]


def rel(p, base):
    """Đường dẫn tương đối dạng posix từ thư mục base, bọc < > cho markdown."""
    import os
    return '<' + os.path.relpath(p, base).replace('\\', '/') + '>'


def rows(f):
    return list(csv.DictReader(open(f, encoding='utf-8-sig')))


def net_stat(prefix):
    f = E3 / f'{prefix}_net.csv'
    if not prefix or not f.exists():
        return None
    r = rows(f)
    return dict(chan=len(r), hoi=sum(any('?' in (v or '') for v in x.values()) for x in r),
                chua_lan=sum('НЕ ПРОСЛЕЖЕНО' in (x.get('net') or '') for x in r))


def e4_stat(prefix):
    f = E3 / f'{prefix}_vs_e4.csv' if prefix else None
    if not f or not f.exists():
        return None
    c = Counter(x['status'] for x in rows(f))
    return f"{c['MATCH']} khớp / {c['NAME_MISMATCH']} lệch tên / {c['ONLY_E3']} chỉ-Э3 / {c['ONLY_E4']} chỉ-Э4"


def manual_part(t):
    y, ru, so, ric, _, a313v, role = t
    return f"""---
id: tam-{y}
loai: tam
ap-dung: A-313-3
tu-khoa: [{y}, {ru}, {so.replace(' ⚠', '')}, рис.{ric}]
nguon: [A313 original/A-313-3.HDSDKT.pdf bảng 6–7, DANH-MUC_ANH_RE_A-313-3.md §2]
do-tin-cay: HDSD
cap-nhat: 2026-10-25
---
# {y} — {ru} ({so})

## Vai trò
{role}

## Ghi chú (viết tay, thêm khi có thông tin mới)
- Tương đương trên A313-V: {a313v}.
"""


def auto_part(t, page):
    y, ru, so, ric, pre, a313v, role = t
    out = [AUTO, '', '## Tài liệu và dữ liệu (tự sinh)', '']
    d = CTRL / y
    imgs = sorted(p for p in d.iterdir() if p.is_file()) if d.exists() else []
    out.append(f'**Ảnh quét** ([thư mục]({rel(d, page.parent)})):' if d.exists() else '**Ảnh quét:** chưa có thư mục.')
    out += [f'- [{p.name}]({rel(p, page.parent)})' for p in imgs]
    out.append('')
    files = sorted(E3.glob(f'{pre}_*')) if pre else []
    if files:
        out.append('**Dữ liệu chép (Э3):**')
        out += [f'- [{p.name}]({rel(p, page.parent)})' for p in files]
        s, e = net_stat(pre), e4_stat(pre)
        out.append('')
        out.append('**Tình trạng:** ' + (f"netlist {s['chan']} dòng, {s['hoi']} dòng có «?», {s['chua_lan']} «НЕ ПРОСЛЕЖЕНО»" if s else 'chưa có netlist')
                   + (f'; đối chiếu Э4: {e}' if e else '') + '.')
    elif y == 'Y16':
        out += ['**Dữ liệu chép:**', f"- [SO-DO-DAU-NOI_E4_A-313-3.md]({rel(ROOT / 'SO-DO-DAU-NOI_E4_A-313-3.md', page.parent)})",
                f"- [tmp/pdfs/review/a313-3/e4/]({rel(ROOT / 'tmp/pdfs/review/a313-3/e4', page.parent)})"]
    else:
        out.append('**Dữ liệu chép:** chưa chép sơ đồ Э3.')
    out.append('')
    return '\n'.join(out)


def write_if_changed(p, text):
    if not p.exists() or p.read_text(encoding='utf8') != text:
        p.write_text(text, encoding='utf8', newline='\n')
        return True
    return False


def main():
    changed = []
    (KB / 'tam').mkdir(exist_ok=True)
    summary = []
    for t in TAM:
        y = t[0]
        page = KB / 'tam' / f'Y{int(y[1:]):02d}.md'
        head = page.read_text(encoding='utf8').split(AUTO)[0].rstrip() + '\n\n' if page.exists() else manual_part(t) + '\n'
        if write_if_changed(page, head + auto_part(t, page)):
            changed.append(page)
        s, e = net_stat(t[4]), e4_stat(t[4])
        st = (f"{s['chan']} dòng / {s['hoi']} «?»" if s else ('Э4 + ma trận' if y == 'Y16' else 'chưa chép'))
        summary.append(f"| [{y}](tam/{page.name}) | {t[1]} | {t[2]} | {t[3]} | {t[5]} | {st} | {e or '—'} |")

    # 00_INDEX.md
    kws = Counter()
    for md in sorted(KB.rglob('*.md')):
        m = re.search(r'^tu-khoa:\s*\[(.*)\]', md.read_text(encoding='utf8'), re.M)
        if m:
            for k in re.split(r',\s+', m.group(1)):  # dấu phẩy thập phân không có dấu cách sau
                kws[k.strip()] += 1
    idx = KB / '00_INDEX.md'
    head = idx.read_text(encoding='utf8').split(AUTO)[0].rstrip() + '\n\n'
    body = [AUTO, '', '## Hỏi gì đọc đâu', '', '| Câu hỏi | Đọc |', '|---|---|']
    for q, f in ASK:
        target = f if '…' in f else f'[{f}]({rel((KB / f).resolve(), KB)})'
        body.append(f'| {q} | {target} |')
    body += ['', '## Bảng 24 tấm A-313-3', '',
             '| Tấm | Tên (Nga) | Số hiệu | рис. | A313-V | Netlist Э3 | Э3 ↔ Э4 |', '|---|---|---|---|---|---|---|']
    body += summary
    body += ['', f"Ảnh sơ đồ đấu nối Э4 cả khối: [A313-3_CONTROL/KHOI_So-do-dau-noi/]({rel(CTRL / 'KHOI_So-do-dau-noi', KB)}) · "
             f"ảnh gốc toàn bộ cuốn RE: [ЕУ.048.002.РЭ(A313-3)/]({rel(ROOT / 'ЕУ.048.002.РЭ(A313-3)', KB)})", '',
             '## Từ khoá', '', ', '.join(sorted(kws)), '']
    if write_if_changed(idx, head + '\n'.join(body)):
        changed.append(idx)

    # Kiểm liên kết + độ phủ
    bad, linked = [], set()
    for md in sorted(KB.rglob('*.md')):
        text = re.sub(r'`[^`\n]*`', '', md.read_text(encoding='utf8'))  # bỏ qua ví dụ trong `code`
        for m in re.finditer(r'\]\((?:<([^>]+)>|([^)\s]+))\)', text):
            target = m.group(1) or m.group(2)
            if target.startswith(('http://', 'https://', '#')):
                continue
            p = (md.parent / target.split('#')[0]).resolve()
            if not p.exists():
                bad.append(f'{md.relative_to(ROOT)} → {target}')
            linked.add(p)
    imgs = [p.resolve() for p in CTRL.rglob('*') if p.is_file() and '.claude' not in p.parts]
    miss_img = [p for p in imgs if p not in linked and p.parent.resolve() not in linked]
    mota = [p.resolve() for p in E3.glob('ric*_mota.md')]
    miss_mota = [p for p in mota if p not in linked]
    print(f'trang tấm: {len(TAM)} | file đổi: {len(changed)} | liên kết hỏng: {len(bad)} | '
          f'ảnh chưa được nhắc: {len(miss_img)} | mota chưa được nhắc: {len(miss_mota)}')
    for x in bad + [str(p) for p in miss_img + miss_mota]:
        print('  !', x)
    assert len({t[0] for t in TAM}) == 24
    return 1 if bad or miss_img or miss_mota else 0


if __name__ == '__main__':
    sys.exit(main())
