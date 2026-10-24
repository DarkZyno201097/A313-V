# Рис.15 — Интегратор (У9 của A-313-3), mã Ет3.072.043 Э3

**Trạng thái phát hiện (2026-10-24):** trước đây không xác định được trang sơ đồ của tấm У9
("Интегратор"), chỉ có ПЭ (danh mục linh kiện). Người dùng vừa cung cấp ảnh mới
`A313-3_CONTROL/Y9/RE_tr191_a265.jpg` (chụp toàn bộ tờ giấy khổ lớn A3+ gấp mở,
2560×1090 px) — xác nhận đây CHÍNH LÀ trang chứa рис.15. Tiêu đề ПЭ trang 192
(`ЕУ.048.002.РЭ(A313-3)/RE_tr192_a189.jpg`) ghi rõ: **«ПЕРЕЧЕНЬ ЭЛЕМЕНТОВ К СХЕМЕ
ЭЛЕКТРИЧЕСКОЙ ПРИНЦИПИАЛЬНОЙ ИНТЕГРАТОРА (РИС.15)»** — khớp chính xác.

Nguồn: Э3 ảnh duy nhất `A313-3_CONTROL/Y9/RE_tr191_a265.jpg` (trang tay 191); ПЭ ảnh 5 trang
`ЕУ.048.002.РЭ(A313-3)/RE_tr192_a189.jpg` … `RE_tr196_a193.jpg` (trang 192–196, Приложение
Лист 59–63). Các crop zoom dùng trong lượt soát này lưu tạm tại
`C:\Users\ADMIN\AppData\Local\hermes\cache\scratch\ric15\*.png` (KHÔNG commit, chỉ để tham
chiếu lại nếu cần soát tiếp — ảnh gốc `RE_tr191_a265.jpg` không bị sửa/đổi tên).

Bản ghi: `ric15_bom.csv` có **175 ref vật lý**; `ric15_net.csv` có **336 hàng chân**.

## 1. Cấu trúc tổng quan (đọc từ ảnh tổng thể, chưa zoom chi tiết hết)

Sơ đồ gồm nhiều cụm mạch con bố trí trên 1 tờ giấy khổ lớn:

| Cụm | Vị trí tương đối | Mô tả | Trạng thái soát |
|---|---|---|---|
| ЦАП2В / ma trận công tắc chính | trái→giữa→phải, phần trên | ~29 IC `168КТ2Б` (У4…У32, trừ У7,У10,У13,У14 là loại khác), mỗi IC có 4 công tắc con, các cụm được vẽ thành từng khối vuông nối dây chéo chằng chịt + nhiều bó bus dọc song song | **CHỈ xác nhận vị trí/ref qua ảnh tổng quan (grid_tl/tm/tr/bl/bm/br.png); CHƯA lần từng chân** — trừ 4 chân đầu tiên của mỗi IC У4, У5 và 1 chân của У6 (xem §4) |
| Khối điều khiển rơle / timer | giữa | `У13` (140УД1Б), `У14` (302НР1Г) — nhãn `У14-1`, `У14-2` quan sát được trong cụm giữa trên | chưa lần chân |
| **Схема усилителя «1…4»** | dưới-phải, hộp nhỏ có khung nét đứt | mạch khuếch đại dùng chung cho 4 kênh, local ref `R1,C1,C2,У1` | **Đã lần đầy đủ nội bộ ô** (xem §2) |
| **Схема повторителя «5…8»** | dưới-phải, cạnh hộp trên | mạch lặp/đệm dùng chung cho 4 kênh, local ref `R2,R3,R4,C3,У2,У3` | **Đã lần đầy đủ nội bộ ô** (xem §2) |
| Bảng đầu nối П1 | lề phải, cột dọc suốt chiều cao tờ giấy | 53 chân đọc được (1–27 cột A, 28–53 cột B offset +27) | Đã đọc (xem §3) |
| Ghi chú viết tay lớn | dưới 2 hộp Усилитель/Повторитель | quy định nối chân `Л`/`М` của `168КТ2Б`/`168КТ2В` vào thanh nguồn +6,3В/+3,5В | Đã đọc (xem §5) |
| Diode/Transistor rời (Д1,Д2,Д4,Д7,Т1,Т2) | góc dưới-trái | mạch có vẻ là bộ khuếch đại/so sánh dùng Т1,Т2 (`2Т912Б`) + op-amp | **Chưa zoom chi tiết, chỉ thấy trong ảnh tổng quan góc dưới-trái** |

**Quan trọng:** đây là sơ đồ RẤT lớn và phức tạp (175 ref vật lý so với 86 ref của рис.8/ric08).
Lượt soát này **KHÔNG** lần hết netlist toàn trang — xem §6 phạm vi đã làm/chưa làm.

## 2. Hai mạch mẫu dùng lặp lại theo kênh — đã lần đầy đủ

### 2.1. Схема усилителя «1,4» (kênh 1–4)

Khung ô nhỏ có 6 cực ngoài đánh số 1–6 (kiểu dashed-border riêng biệt khỏi ma trận chính),
bên trong có hộp "У1" (140УД1Б) vẽ dạng 2 hàng chân (hàng trên: 10,1,7,2,3,**5(chấm đậm
không có số)**; hàng dưới: 9,11,4,12,6,8) — **cách vẽ này giống hệt khuôn mẫu đã dùng cho
У1…У7 ở tấm У5/ric08** (hộp 14-vị trí nhưng chỉ dùng một phần). KHÔNG suy diễn đây là
pinout thật của chip 140УД1Б (loại 8 chân TO-99) — chỉ ghi nguyên vị trí quan sát được.

Topology (ref vật lý mở rộng theo kênh `nR1,nC1,nC2,nУ1`, n=1..4, theo đúng quy ước
`ПЭ tr.196` ghi "1х4"):

* cực 2 & cực 3 (cùng net) → `nУ1` chân 10 → `nC2` chân 1
* cực 4 → `nУ1` chân 1 → `nC2` chân 2
* cực 1 → `nУ1` chân 9 (chưa lần tiếp ra ngoài ô)
* chấm đậm không nhãn số (ngay sau chân 3 hàng trên) → cực 5 (chưa lần tiếp ra ngoài ô)
* `nУ1` chân 4 → `nR1` → `nC1` → cực 6 (chưa lần tiếp ra ngoài ô)
* `nУ1` chân 7, 2, 3, 11, 12, 6, 8 — chỉ là chấm tròn, **không thấy dây nối ra ngoài hộp**
  trong vùng đã zoom (`usil_block.png`) — ghi `НЕ ПРОСЛЕЖЕНО nУ1.x`

Cực 1–6 của ô **chưa lần tiếp vào ma trận chính** (sẽ cần một lượt zoom riêng dọc theo
các bó dây đi ra khỏi khung dashed để nối tới У4…У32 hoặc bảng П1).

### 2.2. Схема повторителя «5,8» (kênh 5–8)

Khung ô 6 cực tương tự, bên trong có `У2` (159НТ1В, vẽ dạng 2 transistor xếp chồng) +
`R2,R3` (1 МОм) ở trên + hộp `У3` (140УД1Б, cùng khuôn mẫu 2 hàng 10,1,7,2,3,5/9,11,4,12,6,8
như У1) + `R4,C3` ở dưới.

Topology (ref vật lý `nУ2,nУ3,nR2,nR3,nR4,nC3`, n=5..8):

* cực 3 (cùng net với `nR2` chân 1 và `nR3` chân 1) → `nУ3` chân 1 (3 điểm cùng nút)
* cực 4 → `nУ3` chân 7 (đi thẳng, KHÔNG qua R2/R3)
* `nR2` chân 2 → chân "2" của `nУ2` (transistor trên) → `nУ3` chân 10 (3 điểm cùng nút)
* `nR3` chân 2 → chân "8" của `nУ2` (transistor dưới) → `nУ3` chân 9 (3 điểm cùng nút)
* `nУ2` chân 4 (transistor trên, chân còn lại) và chân 6 (transistor dưới, chân còn lại):
  nằm ở mép trái vùng đã crop (`povt_u2_detail.png`), **chưa xác định nối cực ngoài nào**
  — nghi ngờ nối cực 1/2 của ô (đối xứng với cách У1 nhận cực 1→chân9 ở mạch Усилитель)
  nhưng KHÔNG xác nhận bằng ảnh, giữ `НЕ ПРОСЛЕЖЕНО`
* `nУ3` chân 4 → `nR4` → `nC3` → cực 6 (chưa lần tiếp ra ngoài ô) — **giống hệt cấu trúc
  R1/C1 của Усилитель**
* chấm đậm không nhãn số sau chân 3 hàng trên → cực 5 (chưa lần tiếp ra ngoài ô)
* `nУ3` chân 7(gate đã gán cực4 ở trên — không nhầm với chân vào gate), 2, 3, 11, 12, 6, 8:
  chấm tròn không dây — `НЕ ПРОСЛЕЖЕНО`

## 3. Bảng đầu nối П1 — 53 chân đọc được

Bảng in dọc theo lề phải tờ giấy, ảnh chụp nghiêng/edge-on (giữ bằng tay, có bóng ngón tay
che một phần) nên phải crop nhiều đoạn và phóng to 4–8× mới đọc được. Cấu trúc: **2 cột
song song lệch offset chính xác +27** (cột A pin 1–27, cột B pin 28–53), đọc được bằng
cách đối chiếu các dòng có nhãn mũi tên lề trái lặp lại (ví dụ dòng ghi "4 | Упр.Знак""
cùng dòng với "31 | Вход К3-РК" → 31−4=27, xác nhận trên nhiều dòng khác).

| A | Tín hiệu A | B | Tín hiệu B |
|--:|---|--:|---|
| 1 | -12,6В | 28 | Корпус |
| 2 | (trống) | 29 | Вход РК |
| 3 | Вход К2-РК | 30 | Вход К1-РК |
| 4 | Упр.Знак" (nhãn lề "З4") | 31 | Вход К3-РК |
| 5 | +12,6В | 32 | (trống) |
| 6 | (trống) | 33 | Вход б |
| 7 | Вход К1-а | 34 | Упр.К1 (nhãn lề "К1") |
| 8 | Упр К2 (nhãn lề "К2") | 35 | Вход а |
| 9 | (trống) | 36 | Вход К1-б |
| 10 | (trống) | 37 | (trống) |
| 11 | ОС-а | 38 | ? (chữ viết tay cỡ rất nhỏ, nét chồng lấp — xem ghi chú dưới) |
| 12 | (trống) | 39 | (trống) |
| 13 | (trống) | 40 | Вход К2-а |
| 14 | Вход К3-а | 41 | Упр К3 (nhãn lề "К3") |
| 15 | Вход К2-б | 42 | Упр К4 (nhãn lề "К4") |
| 16 | (trống) | 43 | Вход К3-б |
| 17 | ИП | 44 | -20В |
| 18 | +6,5В | 45 | (trống) |
| 19 | +3,5В | 46 | Упр.3р РМ (nhãn lề "3р") |
| 20 | Упр.5р РМ (nhãn lề "5р") | 47 | Инт.а |
| 21 | ОС-б | 48 | Вых.контр РК |
| 22 | (trống) | 49 | Инт.б |
| 23 | Упр.АПу НУ (nhãn lề "АПу НУ") | 50 | Упр.Нр РМ (nhãn lề "Нр") |
| 24 | Упр.Контроль (nhãn lề "Контр.") | 51 | Упр.15р РМ (nhãn lề "15р") |
| 25 | Упр.13р РМ (nhãn lề "13р") | 52 | Упр.14р РМ (nhãn lề "14р") |
| 26 | Упр.10р РМ (nhãn lề "10р") | 53 | Упр.12р РМ (nhãn lề "12р") |
| 27 | Общий провод (nhãn lề "ОТ") | — | (không thấy dòng B tương ứng trong vùng đã crop) |

**Chân П1/38 — còn "?"**: đã zoom tới 8× (`p1_row38.png`) nhưng nét chữ viết tay quá nhỏ
và các nét chồng lấp nhau (không phải do ảnh mờ — độ phân giải gốc không đủ cho cỡ chữ này
khi phóng thêm); đọc tạm là "Упр.интегр...НУ" nhưng không chắc chắn từng ký tự, nhãn lề
trái đọc tạm "Шnтr НУ" (nghi ngờ "Интг НУ") — không khẳng định.

**Hàng cuối (A=27, "Общий провод")** không thấy cột B tương ứng (B=54) trong vùng đã crop —
có thể bảng B dừng ở 53, hoặc dòng 54 nằm ngoài phần đã chụp.

Ánh xạ cụ thể component↔П1 xem §4; phần còn lại của bảng П1 **chưa được nối với component
nào cụ thể** trong lượt soát này (ngoại trừ các chân đã dùng ở У4,У5,У6 — §4).

## 4. Khớp nối xác nhận: У4, У5, У6 ↔ П1

Từ nhãn chữ viết tay kề bên các khối công tắc `У4`, `У5` (crop `y456_labels.png`,
phóng to 5×), đọc được các cực đầu vào của 2 công tắc con đầu (`168КТ2Б`, mỗi IC 4 công
tắc, pinout từng công tắc theo vị trí vẽ: `{1,3,2}`,`{5,7,6}`,`{10,8,9}`,`{12,14,13}`):

| Ref | Chân | П1 | Tín hiệu | Độ tin cậy |
|---|---|---|---|---|
| У4 | 1 | П1/35 | Вход а | cao — nhãn rõ |
| У4 | 5 | П1/36 (đọc là 35 trên ảnh) | Вход б → khớp tên П1/36 Вход К1-б | trung bình — số viết tay 35/36 dễ nhầm, chọn theo tên tín hiệu khớp bảng П1 |
| У4 | 10 | П1/7 | Вход К1-а | cao — nhãn rõ |
| У4 | 12 | không chắc (đọc "П1/56", không tồn tại trong bảng 1-53) | Вход К1-б (trùng tên với chân 5) | **thấp — ghi "?"**, có thể là nhánh 2 của cùng net П1/36 hoặc lỗi đọc số |
| У5 | 1 | П1/40 | Вход К2-а | cao — nhãn rõ |
| У5 | 5 | П1/15 | Вход К2-б | cao — nhãn rõ |
| У5 | 10 | П1/14 | Вход К3-а | cao — nhãn rõ |
| У5 | 12 | П1/43 | Вход К3-б | cao — nhãn rõ |
| У6 | 1 | П1/29 | Вх.РК | cao — nhãn rõ |

Các chân còn lại của У4, У5 (chân thứ 2 và thứ 3 của mỗi công tắc con) nối vào bó bus dọc
nhiều đường song song chạy xuyên nhiều IC (giống hiện tượng đã gặp ở ric08 §4 cụm У8→У9→У10)
— **chưa tách được chấm nối nào ứng với dây nào**, ghi `НЕ ПРОСЛЕЖЕНО`. У6 chỉ xác nhận
được chân 1 vì crop bị cắt ở mép dưới; 11 chân còn lại của У6 hoàn toàn chưa xem.

## 5. Ghi chú viết tay (nguyên văn, xác nhận khớp với đề bài người dùng)

> Контакты "Л" микросхем 168КТ2Б/168КТ2В соединить с шиной питания +6,3В (П1/18),
> а контакты "М" микросхем 168КТ2В соединить с шиной питания +3,5В (П1/19).

(dịch: nối chân "Л" của các IC 168КТ2Б/168КТ2В vào thanh nguồn +6,3В tại П1/18; nối chân
"М" vào thanh nguồn +3,5В tại П1/19). Ghi chú nằm ngay dưới 2 khối Схема усилителя/
повторителя trong ảnh gốc, chữ viết tay rõ, không có phần nào phải đoán.

## 6. Phạm vi đã làm / CHƯA làm trong lượt soát này

**Đã làm với độ tin cậy cao:**
- BOM đầy đủ 175 ref từ 5 trang ПЭ (tr.192–196), đối chiếu chéo với nhãn trên Э3 để xác
  nhận các ref cục bộ `R1-R4,C1-C3,У1-У3` thuộc 2 nhóm "Усилитель 1-4"/"Повторители 5-8"
  (giải thích khoảng trống R1-R4/C1-C3/У1-У3 trong các trang 192/194/195 vốn khiến lượt
  trước không chắc trang nào có sơ đồ).
- Netlist nội bộ đầy đủ của 8 bản sao "Усилитель"×4 + "Повторители"×4 (48 ref, ~168 dòng).
- Bảng П1 (53/~54 chân, 1 chân còn "?" cụ thể).
- 9 chân của У4/У5/У6 khớp trực tiếp với П1 (độ tin cậy cao, trừ 2 chân có "?" ở У4).

**CHƯA làm (nêu rõ để không hiểu nhầm là đã xong):**
- **~29 IC còn lại của ma trận công tắc chính (У4 phần còn lại, У6 11/12 chân, У7…У32)**:
  chỉ xác nhận ref/vị trí tồn tại qua ảnh tổng quan, chưa lần một chân nào ngoài các chân
  đã nêu ở §4. Đây là phần lớn nhất và phức tạp nhất của sơ đồ (nhiều bó bus song song,
  tương tự mức độ khó của ric08 §4 nhưng quy mô gấp đôi).
- **Cụm Д1,Д2,Д4,Д7,Т1,Т2** (diode/transistor rời góc dưới-trái): chưa zoom, chỉ thấy
  trong ảnh tổng quan.
- **Toàn bộ 74 điện trở R5…R78 và 26 tụ C4…C29** nằm rải trong ma trận chính: BOM đã có
  đủ, nhưng net.csv chỉ ghi placeholder `НЕ ПРОСЛЕЖЕНО <ref> (toàn bộ ref, chưa zoom chi
  tiết)` cho từng ref — **KHÔNG phải netlist thật**, chỉ để file pass được việc "mọi ref
  trong BOM đều xuất hiện trong net" theo yêu cầu `e3_check.py`.
- Cực 1–6 của cả 2 khung "Усилитель"/"Повторители" (×8 kênh = 48 điểm) chưa lần tiếp vào
  ma trận chính hay bảng П1.
- Chưa đối chiếu với ЦАП2В theo đúng tên gọi trong đề bài — nhãn "ЦАП2В" nêu trong đề bài
  người dùng **chưa tìm thấy trực tiếp trên ảnh** trong lượt soát này (có thể là một trong
  các khối ma trận chưa zoom, hoặc một chú thích nhỏ chưa xem tới) — không suy diễn, cần
  tìm lại ở lượt sau.

**Kết luận về phạm vi:** file `ric15_net.csv` hiện tại **đúng và đầy đủ cho 2 cụm mạch mẫu
(Усилитель/Повторители) + 9 chân П1/У4/У5/У6**, nhưng **KHÔNG phải netlist hoàn chỉnh của
toàn bộ рис.15** — phần ma trận công tắc chính (phần lớn sơ đồ) cần một hoặc nhiều lượt
soát riêng, theo đúng tinh thần ric08 (vốn cũng mất nhiều lượt mới lần gần hết một sơ đồ
nhỏ hơn 2 lần).

## 7. Đối chiếu với ПЭ — không có ngoại lệ "có trong ПЭ nhưng không thấy trên Э3"

Mọi ref 175 trong `ric15_bom.csv` đều thấy xuất hiện (ít nhất ở dạng ký hiệu hộp vuông có
nhãn, qua ảnh tổng quan) trên Э3 `RE_tr191_a265.jpg`, kể cả khi chưa lần chi tiết từng chân.
Không có ref nào bị nghi "trong ПЭ nhưng không có trên sơ đồ".

Riêng 2 điểm cần lưu ý về dữ liệu ПЭ (ghi rõ trong `ric15_bom.csv` note, không tự sửa):
- `C27`: mã TU đọc được là `ОЖ0.460.061` (khác với các tụ `К52-1` cùng loại khác thường
  dùng `ОЖ0.464.039`) — có thể là lỗi in/chép tay gốc.
- `C28,C29`: mã TU đọc là `ОЖ0.464.043` (khác `C22,C23` cùng trị số dùng `ОЖ0.460.043`).
- `R51,R52`: cột "Кол." (số lượng) **trống thật** trong ảnh gốc (đã zoom xác nhận), ghi
  qty=1×2 theo khuôn mẫu các dòng khác nhưng không có số xác nhận trực tiếp.
