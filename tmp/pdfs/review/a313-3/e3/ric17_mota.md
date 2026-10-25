# Рис.17 — Коммутатор выходной (Выход 1а…32а, 1б…16б), tấm Y11 của A-313-3

Mã sơ đồ: **ЕУ2.242.113 Э3**, 2 tờ. Nguồn ảnh:

- Tờ 1/2: `A313-3_CONTROL/Y11/RE_tr202_a266.jpg` (trang tay "202") — chú giải ký
  hiệu (Условное графическое обозначение), sơ đồ nguyên lý 1 ячейка (khối
  У1…У8 + R1…R8 + C1…C8), và 6 bảng đầu nối nhỏ cho Я1…Я6.
- Tờ 2/2: `A313-3_CONTROL/Y11/RE_tr203_a267.jpg` (trang tay "203") — khối
  У9…У17 (logic chọn kênh) và 2 bảng đầu nối đầy đủ П1, П2.
- ПЭ: `ЕУ.048.002.РЭ(A313-3)/RE_tr204_a206.jpg` (trang "204"),
  `RE_tr205_a207.jpg` (trang "205").

Bản ghi: `ric17_bom.csv` có **176 ref vật lý**; `ric17_net.csv` có **347 hàng
chân** (cập nhật 2026-10-25), trong đó nhiều hàng còn đánh dấu `НЕ ПРОСЛЕЖЕНО` (xem §4). Script
kiểm `check_ric17.py` gọi `e3_check.check(17)` → **PASS** (176 ref khớp
2 chiều bom↔net, không có net nào <2 chân).

## 1. Cấu trúc tổng quan

Tấm là bộ chuyển mạch 48 lối ra vật lý: Выход 1а…32а và Выход 1б…16б (sửa 2026-10-25 theo 6 bảng Я,
xem §2), dùng 57 vỏ `168КТ2Б`:

- **6 ячейка Я1…Я6** (ПЭ: поз. "Я1...Я6", mỗi cái gồm 8×`168КТ2Б`
  (У1…У8), 8×điện trở 3,3 кОм (R1…R8), 8×tụ 4,7 µF (C1…C8) — tổng
  48 IC + 48 R + 48 C). Mỗi ячейка có giao diện ngoài 12 chân:
  `A1,A2,A3,A4` (địa chỉ/chọn transistor — 4 tín hiệu `Упр.т1…т4` DÙNG
  CHUNG cho cả 6 cell), `S1,S2,B1,B2` (chọn riêng từng cell, lấy từ
  У9…У17), và `Q1…Q8` (8 lối ra tới Выход).
- **9 IC rời У9…У17** (ПЭ: nhóm riêng, `168КТ2Б`) — logic tạo tín hiệu
  `S1,S2,B1,B2` cho từng cell, đặt trên cả 2 tờ.
- **Linh kiện rời khác**: R9…R21 (13 điện trở, nhiều trị số), C9…C12
  (4 tụ) — vị trí trên tờ 2, CHƯA lần net trong lượt này (xem §4).

Ghi chú in trên tờ 1 (áp dụng cho MỌI vi mạch cả 2 tờ): **"Выводы 7 и 11
всех микросхем соединены с цепью 'о'"** — chân 7 và 11 mọi IC nối net
`o` (mát chung). Đã ghi vào net.csv cho tất cả 57 ref `У*`.

## 2. Ánh xạ ячейка ↔ Выход — CHỐT 2026-10-25

Chép lại cả 6 bảng Я1…Я6 trên tờ 1 (`RE_tr202_a266.jpg`, zoom 2×) và đối chiếu từng chân với bảng П1/П2
đầy đủ trên tờ 2 (`RE_tr203_a267.jpg`): **48/48 chân Q khớp**, không còn ô nghi vấn. Ảnh đủ rõ; các lỗi
của bản chép trước (Я4 chép nhầm từ Я1, Я3 Q6/Q8, Я4 S/B = У13) là lỗi đọc, không phải do ảnh.
Script áp: `ric17_soat_ya.py` (ghi đè dòng Я*.S/B/Q trong `ric17_net.csv`, thêm chân У11.3/12, У12.3/12/5/10;
chạy lại không đổi kết quả).

| Ячейка | S1 / S2 / B1 / B2 | Q1…Q8 → Выход | Chân П |
|---|---|---|---|
| Я1 | У9.3 / .12 / .5 / .10 | 1а…8а | П1: 34, 33, 7, 41, 35, 8, 36, 43 |
| Я2 | У10.3 / .12 / .5 / .10 | 9а…16а | П2: 28, 31, 8, 39, 29, 4, 36, 12 |
| Я3 | У11.3 / .12 / .5 / .10 | 17а…24а | П2: 43, 32, 9, 40, 30, **5**, 46, **47** |
| Я4 | **У12**.3 / .12 / .5 / .10 | **25а…32а** | П2: **3, 6, 37**, 51, 33, 7, 10, 25 |
| Я5 | У13.3 / .12 / .5 / .10 | 1б…8б | П1: 52, 51, 46, 23, 24, 25, 49, 45 |
| Я6 | У14.3 / .12 / .5 / .10 | 9б…16б | П2: 53, 52, 50, 14, 34, 35, 38, 13 |

A1…A4 (`Упр.т1…т4`) giống hệt ở cả 6 bảng: П1/31, 4, 32, 5.

Hệ quả: tấm có **48 lối ra = 32 kênh «а» (Выход 1а…32а) + 16 kênh «б» (Выход 1б…16б)**, không phải
24 × (а, б) như §1 ghi trước đây. Tờ 2 cũng ghi nhãn «Я4S1, Я4B1…» ở khối У12, khớp Я4 ← У12.

Chữ chép cũ (đã sửa trong net): Я4 Q1/Q2/Q3 = П2:13/16/17 → **П2/3, 6, 37** (bảng П2 tờ 2: chân 3 = Выход 25а,
6 = 26а, 37 = 27а; chân 13 = Выход 16б thuộc Я6); Я3 Q6/Q8 = П2:15/41 (ô trống) → **П2/5, 47**;
Я1 Q3 trong bảng cũ ghi «П1 17» → **П1/7**.

## 3. Nghi vấn còn lại (ghi nhận, không tự suy diễn)

1. Mã TU của У9…У17 (ПЭ trang 204: `И10.302.029`) khác 1 chữ số với mã
   của У1…У8 trong mỗi Я (ПЭ trang 205: `И10.308.029`) dù cùng tên linh
   kiện `168КТ2Б` — giữ nguyên cả hai như trong tài liệu gốc, không tự
   sửa (có thể 1 trong 2 trang in sai).
2. Nhãn ô IC thứ 8 trong sơ đồ 1-ячейка mẫu (cạnh У7,У6,У5) đọc được là
   **У8** (khớp dải ПЭ "У1...У8") nhưng chữ viết tay có nét giống "9" —
   giữ theo ПЭ, không dùng "У9" (vì У9 đã là ref độc lập trên tờ 2).

## 4. Phần CHƯA lần được (đánh dấu `НЕ ПРОСЛЕЖЕНО` trong net.csv)

- **R9…R21, C9…C12** (17 ref độc lập trên tờ 2): chỉ xác nhận có trong
  ПЭ, CHƯA zoom vùng dây nối quanh khối У9…У17 để xác định net — mỗi ref
  mới có 1 hàng placeholder (chân "1").
- **144 ref nội bộ trong 6 ячейка** (`nУ1…nУ8`, `nR1…nR8`, `nC1…nC8`,
  n=1…6): sơ đồ 1-ячейка mẫu ở tờ 1 (quanh У1,У5) cho thấy rõ đánh số
  chân IC (1,2,3,5,6,7,8,9,10,12,13,14) và một phần nối R1/R2/R3/R4,
  C1…C8, nhưng dây nối chi tiết nối TỪNG chân У1…У8 với A1…A4/S/B/Q thì
  **CHƯA truy hết** trong lượt này (mạch 6 cell lặp lại giống nhau,
  khối lượng lớn — mỗi cell có tới ~8×14 chân). Mỗi ref trong nhóm này
  mới có 1 hàng placeholder `НЕ ПРОСЛЕЖЕНО <ref>.1`, ngoại trừ chân 7/11
  (mát, theo ghi chú chung §1) đã ghi cho 48 ref `nУk`.
- У15,У16,У17 (standalone): chỉ có chân 7/11 (mát); У12 có thêm 3/5/10/12 (→ Я4); chưa lần được
  chân nào khác (không zoom kịp trong lượt này).

## 5. Việc tiếp theo nếu soát lại

1. Zoom vùng dây nối R9…R21, C9…C12 và 4 IC У12,У15,У16,У17 trên tờ 2.
2. Nếu cần netlist gate-level đầy đủ bên trong 6 ячейка (У1…У8 nối chi
   tiết), cần một lượt riêng tập trung chỉ vào đó — khối lượng tương
   đương với rис.8 trước đây (≈950 hàng) nhân thêm hệ số lặp.

Không đo thông mạch trên board thật. Không sửa ảnh gốc, không sửa
`e3_check.py`, không sửa các `ricNN_*` khác.
