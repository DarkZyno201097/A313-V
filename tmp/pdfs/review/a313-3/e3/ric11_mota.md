# Рис.11 — Плата согласования У7 của A-313-3

Nguồn chính: ảnh #180 (`20261021_102209.jpg`, trang tay 184, Э3); ПЭ ảnh #179
(`20261021_102128.jpg`, trang 185); bản lắp ráp рис.27 ảnh #242
(`20261021_143010.jpg`, trang 241). Bảng chân đối chiếu độc lập: Э4 trang 152,
`e4/p152.csv`, bảng `У7П1` và `У7П2`.

Bản ghi: `ric11_bom.csv` có 166 ref vật lý; `ric11_net.csv` có 462 chân,
51 net nội bộ `N1…N51`, 105 chân đầu nối có nhánh tới linh kiện và ba chân
không nối của `5У1.3`. `e3_check.py` kiểm BOM↔net; `e3_vs_e4.py` sinh
`ric11_vs_e4.csv` và so tên tín hiệu sau chuẩn hoá Latin↔Cyrillic.

## 1. Cấu trúc

Tấm gồm 13 ячейка. Mỗi ячейка dùng một `198НТ7Б` gồm bốn секция transistor;
mỗi секция có ba điện trở:

- điện trở 2,2 kΩ từ `ВХ.n` tới base;
- điện trở 33 kΩ từ base tới `+5В`;
- điện trở 4,7 kΩ từ `−20В` tới collector; collector là `ВЫХ.n`;
- emitter nối `+3,5В`.

Net `Nn` trong CSV là nút base của kênh tín hiệu `n`, không phải tên in trên
bản vẽ. Ячейка 5 không lắp R7–R9 và không dùng секция `5У1.3`; ba chân
`5У1.7/.8/.9` được ghi riêng là `Н.С.`, không nối chung nhau.

| Ячейка | секция 1 | секция 2 | секция 3 | секция 4 |
|---:|---:|---:|---:|---:|
| 1 | 51 | 25 | 24 | 50 |
| 2 | 49 | 23 | 22 | 48 |
| 3 | 47 | 21 | 20 | 46 |
| 4 | 45 | 19 | 18 | 44 |
| 5 | 43 | 17 | — | 42 |
| 6 | 16 | 41 | 40 | 15 |
| 7 | 14 | 39 | 12 | 38 |
| 8 | 37 | 11 | 10 | 36 |
| 9 | 35 | 9 | 8 | 34 |
| 10 | 33 | 7 | 6 | 32 |
| 11 | 31 | 5 | 4 | 30 |
| 12 | 29 | 3 | 2 | 28 |
| 13 | 27 | 1 | 13 | 26 |

Bảng trên bao phủ đúng một lần các tín hiệu 1…51. Chân tín hiệu dùng cùng số
chân trên П1 và П2: П2 mang `ВХ.n`, П1 mang `ВЫХ.n`. Các chân nguồn:
`П1/1 +3,5В`, `П1/27 −20В`, `П2/27 +5В`.

## 2. Linh kiện chính theo ПЭ #179

| Ref cục bộ trong mỗi ячейка | Tên ПЭ | Số lượng toàn tấm |
|---|---|---:|
| R1, R4, R10 | С2-23-0,125-2,2кОм±10% Б-Д | 13 mỗi ref |
| R7 | С2-23-0,125-2,2кОм±10% Б-Д | 12 |
| R2, R5, R11 | С2-23-0,125-33кОм±10% Б-Д | 13 mỗi ref |
| R8 | С2-23-0,125-33кОм±10% Б-Д | 12 |
| R3, R6, R12 | С2-23-0,25-4,7кОм±10% Б-Д | 13 mỗi ref |
| R9 | С2-23-0,25-4,7кОм±10% Б-Д | 12 |
| У1 | Микросхема 198НТ7Б ЩП0.348.002 ТУ | 13 |

CSV mở rộng ký hiệu cục bộ thành ref vật lý `1R1…13R12`,
`1У1…13У1`, theo cách ghi trên bản lắp рис.27; bỏ đúng `5R7`, `5R8`,
`5R9`. Tổng: 153 điện trở + 13 vi mạch = 166 ref.

## 3. Đối chiếu Э3 ↔ Э4

Kết quả dự kiến và đã khóa bằng assert trong `e3_vs_e4.py`:

| Kết quả | Số chân |
|---|---:|
| Khớp tên sau chuẩn hoá | 105 |
| Lệch tên | 0 |
| Chỉ có trong Э3 | 0 |
| Chỉ có trong Э4 | 1 |

Chân chỉ có trong Э4 là `П2/1 КОРПУС`. Bảng đầu nối ở góc phải ảnh #180
cũng ghi `КОРПУС`, nhưng phần mạch chính không vẽ nhánh từ chân đó tới bất kỳ
chân linh kiện rời nào. Vì `ric11_net.csv` chỉ liệt kê chân linh kiện nhìn thấy,
không tạo ref giả cho П2/1; giữ nguyên cả hai nguồn, không coi đây là mâu thuẫn
điện.

## 4. Chỗ chưa chắc

| Ref/chân | Ảnh, vùng | Ghi nhận |
|---|---|---|
| Khung tên Э3 | #180, mép ngoài tờ gấp | Ảnh không chứa khung tên; định danh рис.11/trang 184 lấy từ `trang.csv`, T01 và quan hệ trực tiếp với ПЭ #179. |
| 5У1.7/.8/.9 | #180, ячейка 5; #242, vùng 5У1 | Sơ đồ bỏ toàn bộ секция thứ ba; ПЭ ghi R7–R9 «всего 12» và bản lắp không có 5R7–5R9. Ghi `Н.С.`; chưa đo thông mạch trên tấm thật. |
| П2/1 | #180, bảng đầu nối góc phải | Tên `КОРПУС` đọc được, nhưng không có nhánh chân linh kiện trong phần mạch chính; vì vậy không có hàng tương ứng trong netlist chân linh kiện. |

Không có ô `?` trong hai CSV: các trường đã chép đều đọc được hoặc được kiểm
chéo bằng hai nguồn ảnh nêu trên. Chưa đối chiếu với tấm thật và chưa suy chức
năng động ngoài topology nhìn thấy.

