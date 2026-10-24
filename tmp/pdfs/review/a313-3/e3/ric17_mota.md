# Рис.17 — Коммутатор выходной (Выход 1а…24а), tấm Y11 của A-313-3

Mã sơ đồ: **ЕУ2.242.113 Э3**, 2 tờ. Nguồn ảnh:

- Tờ 1/2: `A313-3_CONTROL/Y11/RE_tr202_a266.jpg` (trang tay "202") — chú giải ký
  hiệu (Условное графическое обозначение), sơ đồ nguyên lý 1 ячейка (khối
  У1…У8 + R1…R8 + C1…C8), và 6 bảng đầu nối nhỏ cho Я1…Я6.
- Tờ 2/2: `A313-3_CONTROL/Y11/RE_tr203_a267.jpg` (trang tay "203") — khối
  У9…У17 (logic chọn kênh) và 2 bảng đầu nối đầy đủ П1, П2.
- ПЭ: `ЕУ.048.002.РЭ(A313-3)/RE_tr204_a206.jpg` (trang "204"),
  `RE_tr205_a207.jpg` (trang "205").

Bản ghi: `ric17_bom.csv` có **176 ref vật lý**; `ric17_net.csv` có **341 hàng
chân**, trong đó nhiều hàng còn đánh dấu `НЕ ПРОСЛЕЖЕНО` (xem §4). Script
kiểm `check_ric17.py` gọi `e3_check.check(17)` → **PASS** (176 ref khớp
2 chiều bom↔net, không có net nào <2 chân).

## 1. Cấu trúc tổng quan

Tấm là bộ chuyển mạch 24 kênh, mỗi kênh có 2 đường dự phòng "а" và "б"
(48 lối ra vật lý: Выход1а…24а, Выход1б…24б), dùng 57 vỏ `168КТ2Б`:

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

## 2. Ánh xạ cell ↔ Выход (xác nhận qua 6 bảng đầu nối + đối chiếu П1/П2 đầy đủ)

**⚠ CẬP NHẬT 2026-10-24 (Claude tự xác minh bằng vision_analyze trực tiếp):** dòng Я1/Я4 dưới đây
(cũng như toàn bộ cột Q5-Q8 của mọi hàng) **KHÔNG đáng tin** — xem §3.0 mới. Bảng giữ nguyên để tham
khảo lịch sử, nhưng chỉ tin **Q1-Q4 của Я1 và Я4** (đã xác minh trực tiếp), còn lại cần soát lại.

| Cell | Dải Выход | Kênh | Nguồn П | Trạng thái |
|---|---|---|---|---|
| Я1 | 1…4 xác nhận (П1 34,33,17,41); 5…8 **CHƯA xác nhận, có thể sai** | а | П1 | Q1-Q4 khớp trực tiếp; Q5-Q8 xem §3.0 |
| Я2 | 9…16 | а | П2 (chân 28,31,8,39,29,4,36,12) | ⚠ CHƯA xác minh lại Q5-Q8, xem §3.0 |
| Я3 | 17…24 | а | П2 (chân 43,32,9,40,30,?,46,?) | khớp 6/8 chân; 2 chân (15, 41) lệch — xem §3; ⚠ Q5-Q8 chưa xác minh lại |
| Я4 | 1…4 xác nhận **THẬT SỰ LÀ Вых.25а-28а, П2 13,16,17,51** (sửa 2026-10-24, KHÁC Я1); 5…8 chưa đọc | а | П2 | Q1-Q4 đã sửa đúng; Q5-Q8 chưa đọc |
| Я5 | 1…8 | б | П1 (52,51,46,23,24,25,49,45) | ⚠ CHƯA xác minh lại Q5-Q8, xem §3.0 |
| Я6 | chỉ đọc 14…16 | б | П2 (35,38,13) | khớp 3/8 chân đã đọc; Q1…Q5 chưa zoom |

### 3.0. LỖI PHÁT HIỆN 2026-10-24 (Claude tự kiểm, không qua subagent)

Zoom trực tiếp bảng Я1 và Я4 phát hiện: **Я4 KHÔNG giống Я1** — subagent lượt trước chép nhầm (copy
nguyên 8 dòng Q1-Q8 của Я1 sang Я4). Đọc lại trực tiếp:
- Я1 thật: Q1=Вых.1а(П1/34), Q2=Вых.2а(П1/33), Q3=Вых.3а(П1/17), Q4=Вых.4а(П1/41) — bảng Я1 chỉ có
  4 dòng Q thật trong khung kẻ, KHÔNG có Q5-Q8 trong chính bảng Я1.
- Я4 thật: Q1=Вых.25а(П2/13), Q2=Вых.26а(П2/16), Q3=Вых.27а(П2/17), Q4=Вых.28а(П2/51).
- Vậy "Вых.5а…8а" (chân П1 35,8,36,43) mà subagent gán cho cả Я1 VÀ Я4 không thuộc bảng nào trong 2
  bảng này — nghi thuộc về Я2 hoặc một bảng khác (thấy thoáng "Q5 Вых.5а П1/35" khi zoom vùng lân cận
  Я2), nhưng CHƯA xác nhận chắc chắn. Đã đổi `ric17_net.csv`: Я4 Q1-Q4 sửa đúng; Я1 Q5-Q8 và Я4 Q5-Q8
  đổi về `?` chờ soát lại.
- **Khuyến nghị mạnh:** toàn bộ cột Q5-Q8 của Я2, Я3, Я5 (ghi "khớp hoàn toàn"/"1…8" trong bảng trên)
  CÓ THỂ bị lỗi tương tự (suy diễn theo thứ tự thay vì đọc trực tiếp) — cần soát lại có hệ thống từng
  bảng bằng zoom trực tiếp trước khi tin dùng, giống cách đã phát hiện lỗi ở Я1/Я4.



4 tín hiệu A1…A4 (`Упр.т1…т4`, qua П1 chân 31,4,32,5) **giống hệt** ở cả
6 bảng — xác nhận trực tiếp bằng ảnh zoom riêng từng bảng.

Tín hiệu S1,S2,B1,B2 mỗi cell lấy từ 1 IC rời trên tờ 2 (đọc trực tiếp
nhãn viết tay, dạng "Уnn.chân" phía trên từng cột bảng đầu nối):

| Cell | S1 | S2 | B1 | B2 | Độ tin cậy |
|---|---|---|---|---|---|
| Я1 | У9.3 | У9.12 | У9.5 | У9.10 | cao, zoom riêng rõ |
| Я2 | У10.3 | У10.12 | У10.5 | У10.10 | cao, zoom riêng rõ |
| Я3 | ? | ? | У11.5 | У11.10 | B1/B2 cao; S1/S2 chưa đọc được (bị chú thích lớn che) |
| Я4 | У13.3 | У13.12 | У13.5 | У13.10 | trung bình, đọc được nhưng chưa đối chiếu chéo |
| Я5 | ? | ? | ? | ? | chưa tách được khỏi ảnh lân cận (xem §3) |
| Я6 | У14.3 | У14.12(?) | У14.5 | У14.10 | trung bình, "12" của S2 hơi mờ |

## 3. Mâu thuẫn / nghi vấn CHƯA giải quyết (ghi nhận, không tự suy diễn)

1. **Я1 và Я4 đọc được output row GIỐNG HỆT NHAU** (cùng "Вых.1а…8а",
   cùng số chân П1 34,33,7,41,35,8,36,43). Hai khả năng: (a) đây là
   mạch dự phòng 2 kênh thật sự đấu song song trên cùng chân П1 (hợp lý
   về mặt kiến trúc độ tin cậy cao của thiết bị bay), hoặc (b) một
   trong hai lần đọc đã bị nhầm bảng do 2 bảng (Я1 và Я4) xếp liền kề
   theo chiều dọc trên ảnh gốc. **Chưa chụp lại để phân định.**
2. **Я3**: hàng Q6 (22а) ghi chân П2/15, hàng Q8 (24а) ghi chân П2/41 —
   nhưng bảng П2 đầy đủ (tờ 2, đọc trực tiếp, xem `ric17_net.csv` không
   lưu bảng này riêng — xem bản ghi gốc trong báo cáo) cho thấy contact
   15 và 41 đều TRỐNG (không có nhãn Выход). Có thể đọc nhầm 1 trong 2
   số ở bảng nhỏ Я3, hoặc bảng П2 đầy đủ có ô bị bỏ sót khi chụp. Giữ
   nguyên số đọc trên bảng nhỏ trong net.csv, đánh dấu nghi vấn.
3. **Я5**: không tách được 4 nhãn S1/S2/B1/B2 — vùng ảnh lẫn giữa nhãn
   Вых của Я2 (bảng phía trên, cùng cột) và có thể trùng với chữ của
   Я4 ở cột bên cạnh do góc chụp nghiêng. Cần chụp lại riêng.
4. **Я6**: chỉ xác nhận được Q6,Q7,Q8 (14б,15б,16б); Q1…Q5 (9б…13б,
   theo suy luận dải số nhưng CHƯA xác nhận bằng ảnh) chưa zoom.
5. Mã TU của У9…У17 (ПЭ trang 204: `И10.302.029`) khác 1 chữ số với mã
   của У1…У8 trong mỗi Я (ПЭ trang 205: `И10.308.029`) dù cùng tên linh
   kiện `168КТ2Б` — giữ nguyên cả hai như trong tài liệu gốc, không tự
   sửa (có thể 1 trong 2 trang in sai).
6. Nhãn ô IC thứ 8 trong sơ đồ 1-ячейка mẫu (cạnh У7,У6,У5) đọc được là
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
- У12,У15,У16,У17 (standalone): chỉ có chân 7/11 (mát); chưa lần được
  chân nào khác (không zoom kịp trong lượt này).

## 5. Việc tiếp theo nếu soát lại

1. Chụp/zoom lại rõ 2 cột S1/S2 của Я3 (vùng bị chú thích che) và toàn
   bộ 4 cột S/B của Я5 (tách khỏi vùng chồng lấn với Я2/Я4).
2. Zoom lại output row của Я4 một lần nữa ở độ phóng đại khác góc để
   xác nhận có thật sự trùng Я1 hay không (mục §3.1).
3. Zoom Q1…Q5 của Я6.
4. Zoom vùng dây nối R9…R21, C9…C12 và 4 IC У12,У15,У16,У17 trên tờ 2.
5. Nếu cần netlist gate-level đầy đủ bên trong 6 ячейка (У1…У8 nối chi
   tiết), cần một lượt riêng tập trung chỉ vào đó — khối lượng tương
   đương với rис.8 trước đây (≈950 hàng) nhân thêm hệ số lặp.

Không đo thông mạch trên board thật. Không sửa ảnh gốc, không sửa
`e3_check.py`, không sửa các `ricNN_*` khác.
