# Рис.8 — Устройство командного управления У5 của A-313-3

Nguồn chính: Э3 ảnh #167 (`20261021_101555.jpg`, trang tay 171) và #168
(`20261021_101653.jpg`, trang tay 172); ПЭ ảnh #169
(`20261021_101707.jpg`, trang 173) và #170
(`20261021_101726.jpg`, trang 174). Bảng chân đối chiếu độc lập: Э4 trang
151, `e4/p151.csv`, các bảng `У5П1`, `У5П2`, `У5П3`.

Bản ghi: `ric08_bom.csv` có 86 ref vật lý; `ric08_net.csv` có 947 hàng
chân, 392 tên net, trong đó 108 net nội bộ `N1…N108`. Có 118 chân đầu nối
được gắn vào nhánh chân linh kiện đọc chắc. `e3_check.py` kiểm BOM↔net;
`e3_vs_e4.py 8 У5` sinh `ric08_vs_e4.csv` và so tên tín hiệu sau chuẩn
hoá Latin↔Cyrillic.

## 1. Cấu trúc

Tấm có 15 ячейка:

| Nhóm | Loại ячейка theo ПЭ | Chức năng nhìn từ nhãn Э3 | Đầu ra |
|---|---|---|---|
| Я1…Я4 | Рг К1, Рг К2; У1…У4 | thanh ghi Рг.К1, 16 bit | 0р…15р Рг.К1 |
| Я5…Я7 | Рг К1, Рг К2; У1…У4 | thanh ghi Рг.К2, 12 bit | 0р…11р Рг.К2 |
| Я8…Я11 | РРК1, РРК2; У5…У7 | thanh ghi lệnh thứ nhất | РК-1…РК-16 |
| Я12…Я15 | РРК1, РРК2; У5…У7 | thanh ghi lệnh thứ hai | РК-17…РК-32 |

Я1…Я7 dùng hai `136ТМ2`, một `133ЛА8`, một `136ЛА3`; Я8…Я15 dùng
hai `136ТМ2` và một `133ЛА8`. Ghi chú in ở đáy #167 quy định chân 7 của
mọi vi mạch nối `Корпус` (điểm `a`), chân 14 nối `+5В` (điểm `б`).

Bó dữ liệu nối hai tờ được nhận biết trực tiếp bằng nhãn `D` và 16 đường
đánh số `0…15`: số nằm cạnh ngõ Д1…Д4 của các ячейка trên cả #167 và #168.
Trong CSV, mỗi net dữ liệu ghi đồng thời hai đầu nối tương ứng, ví dụ
`П1:28 М0 | П3:8 М0`; đây là một net vật lý, không phải hai net suy từ Э4.
Hai rail `a`/`б` cũng được nhận biết bằng cùng chữ ở hai tờ và bằng hai
ghi chú chân nguồn nêu trên.

## 2. Linh kiện chính theo ПЭ #169–#170

| Ref | Tên ПЭ | Số lượng |
|---|---|---:|
| R1…R11 | С2-23-0,125-1 кОм±10% Б-Д ОЖ0.467.081 ТУ | 11 |
| C1…C4 | КМ-6-А-Н50-0,015 мкФ ОЖ0.460.061 ТУ | 4 |
| C5 | К52-1-16В-47 мкФ±20% ОЖ0.464.039 ТУ | 1 |
| У8 | 136ТМ2 | 1 |
| У9, У10, У17, У18 | 133ЛА8 | 4 |
| У11, У13, У19, У21 | 136ЛА3 | 4 |
| У12 | 136ЛА4 | 1 |
| У14 | 136ЛР3 | 1 |
| У15, У16, У20, У22…У24 | 133ЛА6 | 6 |
| У25 | 133ЛА3 | 1 |
| Я1…Я7 | mỗi ячейка: У1, У2, У3, У4 | 7 ячейка / 28 IC |
| Я8…Я15 | mỗi ячейка: У5, У6, У7 | 8 ячейка / 24 IC |

CSV mở rộng ký hiệu cục bộ thành ref vật lý `1У1…7У4` và
`8У5…15У7`. Mọi ref trong ПЭ đều thấy ít nhất ký hiệu hoặc chân nguồn trên
Э3; không cần ngoại lệ “có trong ПЭ nhưng không thấy trên ảnh”.

## 3. Đối chiếu Э3 ↔ Э4

| Kết quả | Số chân |
|---|---:|
| Khớp tên sau chuẩn hoá | 116 |
| Lệch tên | 2 |
| Chỉ có trong Э3 | 0 |
| Chỉ có trong Э4 | 42 |

Hai lệch tên thật sự được giữ nguyên cả hai phía:

| Chân | Э3 #167/#168 | Э4 p151.csv | Giải thích |
|---|---|---|---|
| П1/10 | `ВХОД РГР ТТЛ` | `ВХОД ПРП ТТЛ` | #167 bảng П1, chữ viết tay giữa giống `РГР`; Э4 giống `ПРП`. Không dùng Э4 sửa ngược Э3. |
| П3/42 | `Nоб БК` | `NАБбк` | #167 góc phải dưới, chữ đầu và cụm giữa rất khó phân biệt vì chữ nhỏ; ghi `?` ở hàng У14.8. |

42 hàng `ONLY_E4` không được coi là mâu thuẫn tên. Chúng là các chân có tên
trong bảng Э4 nhưng trên ảnh Э3 không lần được một nhánh tới **chân linh kiện**
đủ chắc để đưa vào netlist: П1/2–9, /22–24, /44, /50–52; П2/2, /3, /49;
П3/3, /4, /27–32, /34–41, /49, /55, /56, /61–65. Dù một số tên cũng hiện
trong bảng đầu nối ở mép phải #167, CSV không tạo ref/chân linh kiện giả chỉ
để tăng số khớp.

## 4. Chỗ chưa chắc

Có 187 hàng chứa ký tự `?` trong cột `note`; không có `?` trong
`ref`, `pin` hoặc tên net. Các hàng này ghi được số chân in trên sơ đồ
nhưng chưa khóa chắc toàn bộ đường dây do vùng trái sát mép, chữ nhỏ và nếp
gấp ngang của #168.

| Ref | Chân | Ảnh, vùng | Lý do |
|---|---|---|---|
| R4 | 1 | #167, bảng П1 góc phải | `РГР` hay `ПРП` không phân biệt chắc; giữ cách đọc Э3 và cách đọc Э4 riêng. |
| R1…R11 | 2 | #168, vùng trái | Thấy chân 2 sau điện trở; nhánh kế tiếp đi qua chữ nhỏ/nếp gấp, không khóa net. |
| У8 | 1, 2, 3, 4, 6, 8, 11, 12 | #168, trái trên | Số chân thấy được; tuyến dây/điểm giao nhỏ không đủ chắc. |
| У9, У10 | 2, 3, 5, 6, 8, 9, 11, 12 | #168, trái trên | Chỉ bốn đầu ra 1, 4, 10, 13 khóa được với bó D. |
| У11 | 1, 3–5, 8–13 | #168, trái giữa/đáy | Chỉ У11.2 và У11.6 có nhãn đầu nối đọc chắc. |
| У12, У13 | 1–6, 8–13 | #168, trái dưới | Chữ và điểm giao gần mép/nếp gấp không đủ chắc. |
| У14 | 8 | #167, góc phải dưới | Tên đầu ra П3/42 đọc gần `Nоб БК`, ký tự không chắc. |
| У15, У16 | 1–6, 8–13 | #168, trái dưới | Tuyến dây nhỏ, nhiều giao cắt; không suy bằng loại IC. |
| У17, У18 | 2, 3, 5, 6, 8, 9, 11, 12 | #168, trái/giữa | Chỉ các đầu ra 1, 4, 10, 13 khóa với bó D số 8…15. |
| У19, У21 | 3–6, 8, 11–13 | #168, đáy | Các đầu vào có nhãn П1/П3 đã chép; các đầu còn lại chưa lần chắc. |
| У20, У22…У25 | 1–6, 8–13 | #168, đáy và vùng nếp | Số chân in được ghi, nhưng không bịa nối qua vùng mờ/nếp gấp. |

## 5. Giới hạn

Netlist này khóa đầy đủ cấu trúc chân của 15 ячейка, nguồn, bó D 0…15 và các
nhánh đầu nối đọc chắc. Các tên `НЕ ПРОСЛЕЖЕНО ref.pin` là trạng thái chưa
lần được, không phải tên net in trên bản vẽ và không được dùng để suy chức
năng. Chưa đo thông mạch trên tấm У5 thật; chưa dùng Э4 hoặc datasheet để điền
ngược các nhánh mờ của Э3.
