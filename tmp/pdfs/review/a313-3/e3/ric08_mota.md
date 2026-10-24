# Рис.8 — Устройство командного управления У5 của A-313-3

Nguồn chính: Э3 ảnh #167 (`RE_tr171_a263.jpg`, trang tay 171 — chụp lại rõ nét
2026-10-24, thay bản mờ `RE_tr171_a167.jpg` cũ) và #168
(`RE_tr172_a264.jpg`, trang tay 172 — chụp lại rõ nét 2026-10-24, thay bản mờ
`RE_tr172_a168.jpg` cũ); ПЭ ảnh #169
(`RE_tr173_a169.jpg`, trang 173) và #170
(`RE_tr174_a170.jpg`, trang 174). Bảng chân đối chiếu độc lập: Э4 trang
151, `e4/p151.csv`, các bảng `У5П1`, `У5П2`, `У5П3`.

Bản ghi: `ric08_bom.csv` có 86 ref vật lý; `ric08_net.csv` có 948 hàng
chân, 372 tên net, trong đó 108 net nội bộ `N1…N108`. Có 124 địa chỉ đầu nối
được parser nhận diện; một số tên còn dấu hỏi. `e3_check.py` kiểm BOM↔net;
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

## 3. Đối chiếu Э3 ↔ Э4 — soát T03b

Trạng thái: **soát một phần**, chưa nghiệm thu toàn bộ netlist. So với checkpoint
`10c0ba1`: dấu hỏi 187 → 169 → **84 hàng (2026-10-24)**; ONLY_E4 42 → 36 →
**35 hàng (2026-10-24, resolved П1/9)**; khớp 116 → 121; lệch tên 2 → 3 →
**0 còn tranh cãi (2026-10-24, cả 3 đã chốt hoặc đọc rõ hơn)**; ONLY_E3 vẫn 0.
Ba lệnh kiểm đều exit 0. Checker chỉ kiểm cấu trúc CSV, không chứng minh
topology hoặc tính đầy đủ.

**2026-10-24 — soát bằng 2 ảnh mới rõ nét** (`RE_tr171_a263.jpg` thay
`RE_tr171_a167.jpg`, `RE_tr172_a264.jpg` thay `RE_tr172_a168.jpg`), dùng
`vision_analyze` với crop zoom 3–8× qua PIL (ảnh gốc 1926×2568 px). Đã giải
quyết thêm 85 hàng dấu hỏi (chủ yếu cụm IC rời У8…У25 trên #168) và xác nhận
1 chân ONLY_E4 (П1/9). Chi tiết ở §4.

Các sửa đã xem trực tiếp trên crop #168 trái trên/giữa/dưới:

- R1…R11: chân 1 nối б (+5В); tín hiệu nối chân 2. Sửa nhầm phía điện trở.
- R11.2 nối П1/10; R4.2/R5.2/R6.2 nối П1/11, /12, /13.
- Bổ sung nối từ R4.2 tới У13.1/.2; R5.2/R6.2 tới У17.9/.11;
  R7.2…R10.2 tới У18.2/.6/.9/.11.
- У8.1 nối chung У8.13, nhãn П3/54. У8.10 nối П2/2, không phải П2/48.
- #167 góc phải dưới: У14.3 nhận П2/4; У14.5 nối chung .6 nhận П2/5.
- #167 bảng đầu nối: П3/29…32 là các đầu cùng số đường với
  П1/21 và П2/4…6; П3/49 cùng đường 8 với П1/45;
  П3/61 cùng đường 4 với П2/40. Ghi các alias vào cùng net.

### Lệch tên — đã chốt (2026-10-24)

| Chân | Э3 cũ trong CSV | Э4 | Kết luận sau soát ảnh mới |
|---|---|---|---|
| П1/10 | ВХОД РГР ТТЛ | ВХОД ПРП ТТЛ | **Đọc lại**: zoom rất sát bảng П1/10 và nhãn cạnh R11 trên #168 cho chữ **'Вход.П ТТЛ'** (một chữ cái đơn 'П' trong ngoặc/nháy nhỏ) — KHÔNG phải РГР, KHÔNG phải ПРП. Dấu chấm/nháy sau 'П' hơi mờ nhưng không đổi nội dung chính. Vẫn khác Э4, nhưng khác biệt này không còn do chữ khó đọc. |
| П3/42 | Nоб БК | NАБбк | **Xác nhận**: zoom rất sát góc phải dưới #167 và bảng П3/42 cho chữ **'Nоб БК'** rất rõ ràng, KHÔNG có nét gạch xoá/sửa đè. Giữ nguyên Э3 = 'Nоб БК'; khác biệt với Э4 là khác biệt thật giữa hai nguồn, không phải do chữ mờ. |
| П2/2 | Отв.Д | ОТВ.Д R15 | **Resolved**: zoom rất sát bảng П2/2 cho thấy chữ 'Отв.Д' bị **gạch ngang (gạch xoá)** và viết đè bên cạnh (không gạch) là **'R15'**. Đây là bản sửa tay cuối cùng trên Э3, khớp gần với cách Э4 chép ('ОТВ.Д R15' = chữ cũ + chữ sửa). Đã cập nhật У8,10 trong net.csv thành `П2:2 R15`. Lưu ý: 'R15' không có trong 86 ref vật lý của `ric08_bom.csv` (chỉ R1…R11) — không suy diễn thêm về ý nghĩa. |

### Các chân ONLY_E4 còn lại

Bảng dưới ghi riêng từng chân. “Chưa lần xong” không có nghĩa bản vẽ không
có nhánh; không dùng Э4 để gán chân linh kiện. Lượt này chưa hoàn tất truy
từng đường của các hàng này.

| Chân | Tên Э4 để định vị | Kết quả tìm trên Э3 / phần còn thiếu |
|---|---|---|
| П1/2 | 5ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/3 | 6ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/4 | 0ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/5 | 1ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/6 | 4ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/7 | 7ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/8 | 2ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| ~~П1/9~~ | 0,15с | **RESOLVED 2026-10-24**: lần dây xong trên #168 trái trên-cùng: П1/9 → У25-3 (chân vào 9,10 nối chung) → ngõ ra chân 8 → chân S (chân 4) của У8-1. Xem net.csv У25,9/У25,10/У25,8/У8,4. |
| П1/22 | Д0 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/23 | 1t16∧СТРОБ1 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/24 | СТРОБ4 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/44 | 3п.КПА | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/50 | СТРОБ1 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/51 | СТРОБ1-1 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П1/52 | 3ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П2/3 | Призн.налич ПКн | #167 bảng П2/3 chữ viết tay nhỏ; chưa xác nhận đường tới chân IC. |
| П2/48 | 0⇒РПР | #167 bảng П2/48 có 0⇒РПР; bỏ gán sai vào У8.10 vì nhánh đó trên #168 ghi П2/2. Chưa khóa đích thật. |
| П2/49 | ¬ИСПРАВН. | #167 bảng П2/49 có nhãn; chưa xác nhận dấu đảo và nhánh tới IC. |
| П3/3 | 7р Рг.Пр | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/4 | ПК вх. | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/27 | СТРОБ1 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/28 | СТРОБ1-1 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/34 | 2ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/35 | 3ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/36 | 5ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/37 | 6ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/38 | 0ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/39 | 1ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/40 | 4ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/41 | 7ОП | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/55 | +3,5В | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/56 | 1t0 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/62 | 0⇒РПР | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/63 | Д0 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/64 | 1t16∧СТРОБ1 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |
| П3/65 | СТРОБ4 | #167 bảng đầu nối có hàng tương ứng; chưa lần xong đường tới chân linh kiện trên #167/#168. |

## 4. Chỗ chưa chắc — 84 hàng note còn dấu hỏi (từ 169, soát 2026-10-24)

R1.2 chưa soát lại trong lượt này (giữ nguyên "?" cũ). R11.2, У14.8, У8.10 (П2/2)
đã **chốt xong** bằng ảnh mới — xem bảng "Lệch tên — đã chốt" ở §3. 85 hàng khác
đã lần dây xong bằng ảnh mới (chủ yếu cụm IC rời У8…У25 trên #168: У8, У11, У12,
У13 gần hết, У14, У15 phần lớn, У16 một chân, У19/У20/У21/У22/У23 các chân gate
dùng chung đầu vào, У25 phần lớn — chi tiết đầy đủ trong `ric08_net.csv`).
Bảng dưới liệt kê CHỈ các chân còn "?" sau lượt soát này, với lý do cụ thể
(không còn ghi chung chung "ảnh mờ"/"nếp gấp" — xem note từng hàng trong CSV):

| Ref | Chân còn ? | Lý do cụ thể (tóm tắt — xem note đầy đủ trong net.csv) |
|---|---|---|
| R1 | 2 | Chưa soát lại trong lượt 2026-10-24; giữ nguyên "?" cũ của checkpoint trước. |
| У8 | 2, 6, 8, 12 | Chân Д(2,12): không thấy đường dây xuất phát trong vùng đã zoom. Chân Q(6,8): đi vào bus dọc nhiều chấm nối chung với У9, chưa tách được chấm nào ứng với dây nào. |
| У9 | 2, 3, 5, 6, 8, 9, 11, 12 | Đã xác định đúng số chân từng cổng (gate1=2,3/out1 v.v.), nhưng nguồn các chân vào nằm trên bus dọc dùng chung chạy xuyên nhiều IC (У8→У9→У10), chưa tách được từng chấm nối. |
| У10 | 2, 3, 5, 6, 8, 9, 11, 12 | Cùng lý do với У9 (bus dọc dùng chung, chưa tách được). |
| У11 | 1, 4, 5, 8 | Gate1 chân 1 và gate2 chân 4,5: nguồn nằm ngoài vùng đã crop. Gate3 ngõ ra (chân 8): đường đi về phía У13-1/У17 nhưng chưa xác định chân đích do nhiều đường chồng nhau. |
| У13 | 3, 11 | Ngõ ra gate1 (chân 3) và gate4 (chân 11): đường dây đi ra ngoài vùng đã crop, chưa xác định chân đích. |
| У15 | 1, 3, 8, 11 | Chân 1,3: không thấy trong box gate1 trên ảnh (có thể là nhãn dây đi ngang, không phải chân IC — chưa xác nhận). Chân 8 (ngõ ra gate2) và chân 11: ra ngoài vùng crop. |
| У16 | 1, 3, 4, 5, 6, 11 | Phần lớn У16-1 (trừ chân 2, đã resolved) chưa được crop riêng trong lượt này; chân 6 (ngõ ra gate1) ra ngoài vùng crop. |
| У17 | 2, 3, 5, 6, 8, 12 | Một chân vào mỗi cổng đã biết (qua R4…R10); chân vào còn lại nối bus dọc dùng chung, chưa xác định nguồn trong vùng đã crop. |
| У18 | 3, 5, 8, 12 | Cùng lý do với У17. |
| У19 | 4, 5, 6, 8, 11, 12, 13 | Chưa xem vùng gate2/3/4 của У19 trong lượt zoom này (chỉ gate1 được soát, đã resolved chân 3). |
| У20 | 3, 11 | Không thấy trong box gate trên ảnh (box chỉ vẽ 4 chân dùng + 1 ra mỗi nửa IC) — có thể là chân không dùng/để hở, chưa xác nhận. |
| У21 | 4, 5, 6, 8, 11, 12, 13 | Chưa xem vùng gate2/3/4 của У21 trong lượt zoom này (chỉ gate1 được soát, đã resolved chân 3). |
| У22 | 3, 11 | Không thấy trong box gate trên ảnh, có thể không dùng — chưa xác nhận. |
| У23 | 3, 11 | Không thấy trong box gate trên ảnh, có thể không dùng — chưa xác nhận. |
| У24 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 (cả 12 chân) | **Không tìm thấy vị trí vật lý của У24** trên trang #168 trong phạm vi đã khảo sát (x≈0–1900, y≈100–2470 gốc ảnh) dù đã tìm quanh cụm У15/У16/У20/У22/У23 (cùng họ 133ЛА6). Có thể nằm ngoài vùng đã crop hoặc bị gate lân cận che nhãn ref — cần một lượt tìm kiếm riêng. |
| У25 | 3, 6, 11, 12, 13 | Ngõ ra gate1(3)/gate2(6): đường đi ra ngoài vùng crop. Gate4 (11,12,13): **không tìm thấy trên trang #168** — hộp gần R11 ban đầu tưởng là У25-4 nhưng zoom chữ sát xác nhận là У11-4 (xem У11,12/13), không phải У25. |


## 5. Giới hạn và phần chưa làm

Sau lượt soát 2026-10-24 (2 ảnh mới): còn 84 hàng dấu hỏi (từ 169) và 35 chân
ONLY_E4 (từ 36) cần soát tiếp — chủ yếu bus dữ liệu dùng chung giữa У9/У10/У17/У18
(chưa tách từng chấm nối), 4 gate chưa soát của У19/У21, và toàn bộ У24 (chưa
tìm thấy vị trí vật lý trên trang #168). Không tái xác nhận toàn bộ 15 ячейка
hoặc bó dữ liệu trong lượt này. Các diễn giải ở §1 là dữ liệu kế thừa T03, chưa
phải kết luận nghiệm thu T03b. Các tên `НЕ ПРОСЛЕЖЕНО ref.pin` chỉ là placeholder
chưa truy dây; các tên mới `N_<ref>-<gate>.<pin>` (thêm 2026-10-24) là net nội bộ
đã lần dây xong giữa hai chân IC nhưng không có nhãn văn bản trên sơ đồ — không
nên nhầm với các net ký hiệu `N1…N108` đã có từ trước (đó là net nội bộ của từng
ячейка, mã hoá theo thứ tự xuất hiện). Chưa đo thông mạch trên tấm thật.
Không commit, không sửa Э4 hoặc ảnh gốc.
