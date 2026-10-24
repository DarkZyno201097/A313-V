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
`10c0ba1`: dấu hỏi 187 → 169 hàng; ONLY_E4 42 → 36; khớp 116 → 121;
lệch tên 2 → 3; ONLY_E3 vẫn 0. Ba lệnh kiểm đều exit 0.
Checker chỉ kiểm cấu trúc CSV, không chứng minh topology hoặc tính đầy đủ.

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

### Lệch tên còn lại

| Chân | Э3 giữ trong CSV | Э4 | Kết luận đọc lại |
|---|---|---|---|
| П1/10 | ВХОД РГР ТТЛ | ВХОД ПРП ТТЛ | #167 bảng П1 và #168 cạnh R11: chữ viết tay mờ; chưa phân định. Đã chuyển nhãn về đúng R11.2. |
| П3/42 | Nоб БК | NАБбк | #167 bảng П3 và đầu ra У14.8: N/№ và об/АБ chưa phân định. Giữ cả hai cách đọc. |
| П2/2 | Отв.Д | ОТВ.Д R15 | #168 nhánh S10 của У8 ghi Отв.Д; #167 bảng П2/2 có gạch xoá và R15. Chưa quyết định tên sau sửa tay; giữ cả hai. |

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
| П1/9 | 0,15с | #168 trái trên có mũi tên П1/9 vào cổng trước S của У8; cần khóa lại ref/chân cổng và dấu đảo, chưa thêm. |
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

## 4. Chỗ chưa chắc — 169 hàng note có dấu hỏi

Ba hàng R1.2, R11.2 và У14.8 đã xem lại nhưng còn khó đọc dấu đảo/chữ viết tay;
У8.10 đã sửa địa chỉ, còn mâu thuẫn sửa tay ở bảng П2/2.
Các hàng khác trong bảng dưới **chưa được soát hết từng chân ở T03b**:
giữ dấu hỏi của checkpoint, không khẳng định tất cả đều không thể đọc.
Các note cũ “thấy số chân” cần kiểm lại, đặc biệt các nhóm chân được liệt kê
theo mẫu trong T03. Không dùng dữ liệu chưa soát để đấu dây.

| Ref | Chân còn ? | Ảnh / vùng | Tình trạng |
|---|---|---|---|
| R1 | 2 | #168 trái dưới; #167 bảng П2/П3 | Đã khóa nối; gạch trên tên chưa chắc. |
| R11 | 2 | #168 trái trên; #167 bảng П1 | Đã khóa nối; РГР/ПРП chưa phân định. |
| У8 | 2, 3, 4, 6, 8, 10, 11, 12 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У9 | 2, 3, 5, 6, 8, 9, 11, 12 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У10 | 2, 3, 5, 6, 8, 9, 11, 12 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У11 | 1, 3, 4, 5, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У12 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У13 | 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У14 | 8 | #167 phải dưới | Đã xem lại; chữ Nоб БК/NАБбк chưa phân định. |
| У15 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У16 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У17 | 2, 3, 5, 6, 8, 12 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У18 | 3, 5, 8, 12 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У19 | 3, 4, 5, 6, 8, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У20 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У21 | 3, 4, 5, 6, 8, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У22 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У23 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У24 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |
| У25 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13 | #168 trái/giữa/đáy | Chưa hoàn tất soát từng chân; note T03 ghi chữ nhỏ/nếp gấp. |

## 5. Giới hạn và phần chưa làm

Chưa hoàn tất mục 1 và 2 T03b: còn 169 hàng dấu hỏi và 36 chân ONLY_E4 cần
soát tiếp. Không tái xác nhận toàn bộ 15 ячейка hoặc bó dữ liệu trong lượt này.
Các diễn giải ở §1 là dữ liệu kế thừa T03, chưa phải kết luận nghiệm thu T03b.
Các tên `НЕ ПРОСЛЕЖЕНО ref.pin` chỉ là placeholder chưa truy dây.
Chưa đo thông mạch trên tấm thật. Không commit, không sửa Э4 hoặc ảnh gốc.
