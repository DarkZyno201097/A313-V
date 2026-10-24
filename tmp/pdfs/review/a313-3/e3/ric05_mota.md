# Рис.5 — Устройство программного управления (У4) của A-313-3, ЕУ3.057.138 Э3

Người quét: Claude, 2026-10-24. Dữ liệu sinh bằng `ric05_gen.py` → `ric05_bom.csv`, `ric05_conn.csv`;
`ric05_net.csv`. Đối chiếu: `e3_vs_e4.py 5 У4` → `ric05_vs_e4.csv`; `e3_check.py` (ngoại lệ KNOWN: C3–C8).

**Trạng thái (2026-10-24): CHÉP MỘT PHẦN — 794 chân, 207 «НЕ ПРОСЛЕЖЕНО».** Tờ 1 do Claude chép (415 chân kể cả
chân 7/14); tờ 2 do Codex đọc ảnh a251 → `ric05_to2_raw.csv` (422 dòng, 126 dòng `?`), Claude ghép bằng union-find
trong `ric05_gen.py`. Chưa chép: C3–C8 (tờ 1). Netlist chưa đủ tin cậy để đấu dây.

## 1. Nguồn và định danh

| Ảnh | Nội dung | Căn cứ |
|---|---|---|
| `A313-3_CONTROL/Y4/RE_tr158_a250.jpg` | Tờ 1/2: bảng đầu nối П1/П2/П3, khối giải mã/đệm (У39…У64), C3–C8, ghi chú 1–2 | Ghi tay «Y4.1 ЕУ3.057.138 Э3 1/2» |
| `A313-3_CONTROL/Y4/RE_tr159_a251.jpg` | Tờ 2/2: trigger 133/136ТМ2, bộ dao động (Пэ1, C1, C2, R1, R2), У33/У35 (109ЛИ1) + R5–R8 | Ghi tay «Y4.2 ЕУ3.057.138 Э3 2/2»; «Начало см. на листе 1» |
| #137–#139 (`RE_trXXX_a137…a139`) | ПЭ «…устройства программного управления (рис. 5)», Приложение лист 22–24, 26.05.1983 | Tiêu đề in |
| #155, #156 (`RE_tr158_a155`, `RE_tr159_a156`) | Bản chụp cũ của chính hai tờ này | Trước đây bị xếp nhầm vào рис.6; khớp ПЭ рис.5 (R5–R8 24 Ω, C7, C8 К52-1 47 µF) |

Số trang 158/159 lấy theo #155/#156 trong `kiemke/trang.csv`. ? Trên a251 có số viết tay đọc giống «189» — chưa
phân định với 159, giữ tên `tr159` theo bảng trang.

## 2. Danh mục linh kiện (ПЭ #137–#139) — 80 ref

R1–R4, R11, R12: С2-23-0,125-1 kΩ ±10 %; R5–R8: С2-23-0,125-24 Ω ±5 %; C1 680 pF, C2 120 pF (КМ-6-А-М47);
C3–C7: КМ-6-А-Н50-0,015 µF; C8: К52-1-16В-47 µF; Пэ1: резонатор РГ-07-14ЕТ 2620,91 кГц.
61 vi mạch У1–У7, У9–У21, У23, У25, У26, У28–У65 (133/136ТМ2, 133/136ЛА3, ЛА4, ЛА6, ЛА8, 133ЛР1, 109ЛИ1).
**Không có У8, У22, У24, У27** trong ПЭ — khi chép netlist cần kiểm các vị trí này trên Э3 có bị gạch không.

## 3. Bảng đầu nối tờ 1 ↔ Э4 (У4П1/П2/П3)

`e3_vs_e4.py 5 У4`: **133 khớp / 25 lệch tên / 1 chỉ Э3 / 3 chỉ Э4** (176 hàng).
Phần lớn «lệch» là cách ghi (`→`↔`⇒`, «Зп» chữ З ↔ «3п» số 3, viết tắt «ИМП.СЧЕТА»). Khác biệt thật — đã phóng
to ảnh a250 xác nhận cách đọc Э3, giữ cả hai nguồn:

| Chân | Э3 (a250) | Э4 | Ghi chú |
|---|---|---|---|
| П1/5, 6 | «80кГц-1» (cả hai chân) | «80кГц 1-1», «80кГц 1-2» | Э3 không ghi hậu tố -1/-2 |
| П1/7, 8 | «80кГц-2» | «80кГц 2-1», «80кГц 2-2» | như trên |
| П1/38 | «1t-2» có gạch trên | «¬1t1» | ? khác số |
| П1/50 | «16рСчК» có gạch trên | «И-3мкс (6р Сч.К)» | khác hẳn |
| П2/3 | «12рРгК2» | «12р Рг.К1» | khác chỉ số thanh ghi |
| П2/18 | «Вход "П" ТТЛ» | «ВХОД ПРП ТТЛ» | cùng chỗ nghi «РГР/ПРП» ở рис.8 П1/10 |
| П1/15, 16 | gạch xoá («Сч бк», «Сч н») | «СИбк», «СИм» | Э3 bỏ chân |
| П3/41 | gạch xoá «СчК→М» | «Сч.К⇒М» | như рис.6 П3/30 |
| П3/42 | «18рСчК» | trống | |

## 3a. Kiểm chéo hai tờ

Nhãn chuyển tờ trên tờ 1 ghi chân nguồn + tên tín hiệu; tên mà Codex lần ra ở tờ 2 khớp 9/9:
«У28/6(2) 7рСчК» = П1/26 7рСчК · «У26/8(2) 6рСчК» = П1/25 · «У26/6(2) 5рСчК» = П1/24 · «У28/8(2) 8рСчК» = П1/28 ·
«У7/6(2) 10рСчК» = П1/30 · «У9/6(2)» = П1/31 11рСчК · «У9/8(2)» = П1/32 12рСчК · «У38/6(2) строб1-1» = П2/30 ·
«У36/8(2) строб1» = net 13 chân. Phần tử gạch bỏ (Codex): У8, У22, У24, У27 (4 phần tử mỗi vỏ), R9, R10 — **trùng
đúng các ký hiệu ПЭ không có** ⇒ bản vẽ và ПЭ nhất quán.

## 4. Việc tiếp theo

1. Lần 207 chân «НЕ ПРОСЛЕЖЕНО» (chủ yếu thanh dọc bộ giải mã tờ 1 và chốt RS У59/У60) và C3–C8.
2. Đọc nốt ghi chú 1–2 (chân 7/14 nối «a» hay «б» — chữ bị cắt ở mép ảnh a250).
3. Xác định số trang thật của a251 (159 hay 189) trên bản giấy.
