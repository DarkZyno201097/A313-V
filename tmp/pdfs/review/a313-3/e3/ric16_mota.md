# Рис.16 — «Преобразователь» (Y8 của A-313-3), mã ЕУ3.036.157Э3

**Trạng thái: PARTIAL.** Nguồn duy nhất: `A313-3_CONTROL/Y8/RE_tr197_a278.jpg` (9134×3658,
trang catalogue 197, hiện là bản ảnh **nét nhất** còn lại của tấm Y8 — 3 bản chụp cũ
`RE_tr197_a195/a196/a199.jpg` đã bị xoá khỏi thư mục làm việc theo xác nhận trước đó của
người dùng). `Y8.jpg`/`Y8S.jpg` (ảnh chụp PCB thật, mặt trước/sau) **không dùng làm nguồn
chép**, chỉ tham khảo đối chiếu — lượt soát này không cần dùng tới chúng.

## 0. Bẫy kỹ thuật gặp ngay từ đầu — file `.jpg` thực chất là HEIC

`RE_tr197_a278.jpg` có đuôi `.jpg` nhưng nội dung byte thực là **HEIC** (hộp `ftypheic`,
xác nhận bằng cách đọc 64 byte đầu: `00 00 00 20 66 74 79 70 68 65 69 63 ...`). `PIL.Image.open`
báo lỗi `UnidentifiedImageError` cho tới khi convert bằng `ffmpeg -i src.heic full.png`
(9134×3658 RGB xác nhận qua PNG). Toàn bộ crop trong lượt soát này dùng từ `full.png` đã convert,
lưu tạm ở `tmp/pdfs/review/a313-3/e3/_y8cache/` (không commit, thư mục làm việc) — ảnh gốc
`RE_tr197_a278.jpg` **không bị sửa/đổi tên**.

## 1. Mã bản vẽ đọc được trực tiếp

Chữ viết tay mực xanh ở đáy-giữa trang (toạ độ gốc ảnh khoảng x≈5600-6300, y≈3200-3350,
soi ở độ phóng đại 2× sau khi crop): **`ЕУ3.036.157Э3`**. Khớp đúng mã `ЕУ3.036.157` ghi
trong `KHO-TRI-THUC_A313/tam/Y08.md` và `KE-HOACH_KIEM-TRA_A-313-3.md` (cột "ЕУ3.036.157",
Hình 16, tấm Y8) — hậu tố `Э3` là viết tắt chuẩn "схема электрическая принципиальная"
(sơ đồ nguyên lý điện), đúng loại tài liệu. Góc trên-phải và lề phải của tờ giấy **không
có khung tên/bảng tiêu đề nào khác** — vùng đó chỉ là nền sàn/vải phía sau tờ giấy (ảnh
chụp tờ giấy khổ lớn đặt trên nền, mép phải tờ giấy kết thúc ở khoảng x≈8650 trên ảnh gốc).

Số trang catalogue "197" xác nhận qua `DANH-MUC_ANH_RE_A-313-3.md` dòng Рис.16/Y8 và chữ số
"97" (phần cuối "197") nhìn thấy ở góc dưới-phải trang trong ảnh tổng quan.

## 2. Vì sao đây là bản PARTIAL — quy mô trang

Đây là **MỘT TỜ RẤT RỘNG** (tỷ lệ ngang ~2,5:1, đúng như mô tả đề bài), chia làm 2 phần rõ rệt:

* **~64% chiều cao phía trên**: hai khối mạch logic dày đặc (trái và phải), mỗi khối gồm
  hàng chục IC/khối chuyển mạch đánh số kiểu `Уnn-m` (nn = số thứ tự vỏ vật lý, m = đoạn/cổng
  con bên trong vỏ đó — quy ước này **giống hệt `Уnn-1..4` đã gặp ở ric10_mota.md**), cộng
  nhiều điện trở/diode/tụ/transistor rời rạc. Khảo sát sơ bộ (tile 8 vùng 2284-2450×1170px,
  xem §6) đọc được tối thiểu **16 vỏ IC, 22 điện trở, 2 tụ, 6 diode, 4 transistor** — và đây
  **CHƯA chắc là đầy đủ**, chỉ là những gì đọc chắc chắn qua khảo sát tổng quan, chưa soi
  từng chân.
* **~36% chiều cao phía dưới**: 4 khung **MẪU** (template) minh hoạ cách đấu dây của 1 "узел"
  (nút/cụm) lặp lại theo kênh — «Схема узла усилителя» (kênh 1…2), «Схема узла повторителя»
  (kênh 3…6), «Схема узла цифрового управляемого сопротивления» (kênh 7…10), «Схема узла
  инвертора» (kênh 11…15) — cộng bảng đầu nối dạng dải chân `П1`, một ô chú thích vẽ lưới
  cầu 11 tụ (С6,С8-С11,С14-С19) giữa 3 thanh nguồn В/Зо/Б, và khối ghi chú chữ viết tay quy
  định cách đấu chân nguồn các IC `168КТ2Б`/`168КТ2В`/`302НР1Г`.

**Đây CHÍNH LÀ kiểu cấu trúc "ô mẫu dùng lặp lại theo kênh" đã gặp ở `ric15_mota.md` (Y9,
«Интегратор»)** — tấm đó cũng có khung "Усилитель 1-4"/"Повторители 5-8" + bảng П1 + ma trận
chuyển mạch chính 175 ref chưa lần hết. Chiến lược áp dụng cho рис.16 **giống hệt tinh thần
ric10/ric15**: lần đầy đủ các ô mẫu (có khung rõ, ít linh kiện, bằng chứng ảnh tốt), còn
ma trận chính (phần lớn nhất, nặng nhất) chỉ khảo sát BOM sơ bộ, **KHÔNG lần netlist** —
lý do là **khối lượng linh kiện** (hàng chục vỏ IC × nhiều đoạn, hàng chục điện trở, dây
chồng chéo <10px ở nhiều vùng), **KHÔNG phải do ảnh hỏng** — ảnh `RE_tr197_a278.jpg` thực ra
**NÉT HƠN HẲN** các ảnh dùng cho ric10/ric14/ric15 (đã xác nhận qua các crop zoom 1,5-3× vẫn
đọc được nhãn in rõ ràng, không bị mờ/ố như ric14).

## 3. Đã lần tương đối đầy đủ — các ô mẫu (template)

### 3.1. «Схема узла усилителя» (kênh 1…2)

Khung khép kín riêng (đường chấm-gạch), 6 cực ngoài đánh số 1-6 (đánh số RIÊNG cho khung này,
không liên quan số cực của khung повторитель bên cạnh). Bên trong: `У1` (hộp panel 12 chân,
hàng trên 10,7,1,2,3,5 / hàng dưới 9,11,4,12,6,8 — chân 11 xác nhận HỞ, chấm rỗng không dây),
`R1,R2,R3,C1,C2,C3`, và 3 đoạn chuyển mạch con `У2.1/У2.2/У2.3`.

**Đã lần chắc chắn**: cực ngoài 1→У1.9, cực ngoài 2→У1.10, У1.11 không nối (xác nhận chắc),
У1.2/3/5 gộp thành 1 bus chung nối У2.2.1 và У2.3.5, đầu ra У2.2.2/У2.3.6 gộp bus vào У2.1.8/10,
У2.1.9 → cực ngoài 5 (đường cô lập, rõ ràng không chồng dây).

**Chưa tách được**: У1 chân 4/12/6/8 (hàng dưới-phải) đi chung 1 bó dây xuống mạng
R1-R2-C1 / R3-C2 rồi ra 3 cực ngoài 6/7/8 — 4 đường chồng sát nhau <10px, không tách được
từng cặp; C3 nối giữa cực 3/4 nhưng chưa chắc nối tiếp hay chỉ bắc cầu song song với đường
chân 1/7 của У1.

### 3.2. «Схема узла повторителя» (kênh 3…6)

Khung tương tự, `У3` (cặp transistor), `R4,R5`, `У4` (cùng panel 12 chân như У1), `R6,C4`.

**Đã lần chắc chắn**: cực ngoài 2→У3 pin"3", cực ngoài 1→У3 pin"7", У3 pin"4"(mũi tên lên)
→ cực ngoài 4, У4 pin"12"→R6→C4→ cực ngoài 6 (nhánh dọc cô lập, rõ ràng).

**Chưa tách được**: toàn bộ vùng R4/R5 ↔ У4 (nhiều đường chéo nhau sát khít giữa 2 khối —
y hệt khó khăn đã ghi trong `ric15_mota.md` §2.2 cho cặp У2↔У3 của Y9); У3 pin "8"/"6"
(cực ra transistor) không xác định đích cụ thể vì cùng lý do.

### 3.3. «Схема узла цифрового управляемого сопротивления» (kênh 7…10)

Khung lớn hơn, chứa `У6,У7,У8` (3 hộp panel 12 chân cùng khuôn, hàng trên 1,5,10,14 / hàng
dưới 3,2,7,6,8,9,12,13) và góc trên-phải thấy 1 mảnh `У5.1` (phần còn lại của У5 nằm ngoài
vùng ảnh đã crop trong phiên này).

**Cấu trúc bus đã xác nhận ở MỨC NHÓM (không phải từng chân)**: phía trên, 7 nhánh điện trở
**KHÔNG có ký hiệu tham chiếu in trên ảnh** (chỉ có số nhánh viết cạnh mỗi điện trở: 27, 24,
23, 22, 19, 17, 16 — áp dụng đúng quy tắc đã dùng ở `ric14_mota.md` khi gặp "dãy điện trở
không ký hiệu tham chiếu": **KHÔNG tạo ref R mới**, chỉ ghi số nhánh) dẫn vào hàng chân trên
của У6/У7/У8; phía dưới, 8 chân mỗi IC dẫn xuống các tiếp điểm ngoài khung đánh số từ 20
giảm dần tới 4 (У6→20,19,18,17,16,15; У7→14,13,12,11; У8→10,9,8,7,6,5,4).

**Bằng chứng chéo mạnh**: các tiếp điểm "Nр" này khớp đúng với cột **"NР"** đọc được ở
nửa phải bảng `П1` (5Р,4Р,7Р,6Р,9Р,8Р,11Р,10Р,13Р,12Р,15Р,14Р — xem §4) VÀ khớp với các mũi
tên tín hiệu phía trên khung «Схема узла инвертора» kế bên (nhãn "4Р,13Р,12Р" và "8,в,11Р,
10Р,9Р" đọc trực tiếp ở mép trên khung đó). Đây là cơ sở để tin cấu trúc tổng thể là đúng,
dù **chưa soi được từng chân cụ thể** (8 chân IC ứng với 4-7 tiếp điểm ngoài — số lượng
không khớp 1-1, cần crop riêng độ phân giải cao hơn mới tách được).

### 3.4. «Схема узла инвертора» (kênh 11…15)

`У9b` (đặt tên tránh trùng — xem §5), `R9,R10` (trên), `R48,R49,R50` (dưới). **Đã lần khá
đầy đủ**: У9b.10→R9, У9b.14→R10 (2 nhánh trên); У9b.12→R48, У9b.1→R49, У9b.13→R50 (3 nhánh
dưới) — các đường này cô lập, không chồng chéo. Chân 5,8,6 của У9b chưa xác định (crop bị
cắt ở mép trái khung ảnh, phần đầu khung «Схема узла инвертора» với chân "7" và các chân
khác nằm ngoài vùng đã crop trong phiên này).

**Mảnh thứ 2 nghi vấn** (góc phải crop «sch3»): thấy tiêu đề lặp lại "Схема узла и[нвертора]"
với `R7,R8`(?) và `R47,R48`(?) — **KHÔNG đưa vào BOM/net** vì độ tin cậy quá thấp (chỉ thấy
góc crop, không có ảnh riêng đủ nét); nếu đúng là R48 trùng tên với R48 đã dùng ở §3.4 thì
đây có thể là MỘT khung mẫu khác (ví dụ áp dụng cho dải kênh khác) — **cần một lượt soát
riêng với crop độ phân giải cao hơn** để xác nhận, không suy diễn ở lượt này.

## 4. Bảng đầu nối dạng dải chân П1

Nằm ngang ở đáy giữa-phải trang, ảnh chụp bị NGHIÊNG (toàn bộ chữ bị xoay so với trục ảnh)
nên các nhãn tín hiệu hiện ra dưới dạng mũi tên chỉ lên kèm chữ. Đã zoom 1,5-2,2× nhiều đoạn
(`pin_table_left/right.jpg`, `table_full_zoom.jpg`) để đọc.

**Khó khăn cụ thể, khác với лý do khối lượng ở §2–3**: bảng có (ít nhất) 2 lớp chữ chồng lên
nhau theo mỗi cột — (a) nhãn ngắn in đậm ngay cạnh mũi tên (dễ đọc, VD "19","20","ПП","3Н1")
và (b) một dòng số nhỏ viết tay bên dưới mỗi cột mà tôi tin là số **Конт.** (số chân vật lý
của đầu nối) nhưng **không đọc chắc chắn từng chữ số** ở độ phân giải ảnh hiện có — ảnh gốc
đủ nét cho hầu hết sơ đồ, nhưng vùng chữ số rất nhỏ này (ước lượng <15px cao trên ảnh gốc)
nằm dưới ngưỡng đọc được ngay cả sau khi phóng 2×.

**Phát hiện đáng chú ý (độ tin cậy trung bình-cao)**: khi đọc được một đoạn liên tục của
dòng số Конт., thấy mẫu **2 dãy số tăng song song** (ví dụ `33,34,35,36,37,38,39,40,41,42,
43,44` đi kèm `7,8,9,10,11,12,13,14,15,16,17,18` cùng lúc theo từng cột) — gợi ý đầu nối П1
có **2 hàng tiếp điểm** (kiểu connector 2 dãy, mỗi cột bảng ghi đồng thời số của cả 2 dãy
cho cùng 1 tín hiệu) — **giống cấu trúc "2 cột A/B offset +27" đã xác nhận ở `ric15_mota.md`
§3 cho П1 của Y9**. Đây là giả thuyết hợp lý nhưng **chưa xác nhận bằng cách đếm hết toàn
bảng** — ghi vào đây để lượt sau kiểm tiếp, KHÔNG dùng làm cơ sở suy ra số Конт. cho các
cột khác trong `ric16_conn.csv` (file đó để nguyên "?" ở cột pin, dùng nhãn ngắn đã đọc
chắc chắn làm cột `signal`).

`ric16_conn.csv` ghi được **~42 cột** theo thứ tự trái→phải với nhãn ngắn đọc được; cột
`pin` (số Конт. thật) để "?" toàn bộ — lý do ghi trong note từng dòng, không phải vì không
cố gắng mà vì **chữ số viết tay dưới ngưỡng đọc được** (khác ảnh hỏng vật lý, khác khối
lượng — là lý do thứ 3, ghi rõ để phân biệt với ric10).

## 5. Vấn đề trùng tên ref — У9 (khung mẫu) và У9 (khối chính)

Nhãn `У9` trong khung mẫu «Схема узла инвертора» (§3.4) **đọc đúng y nguyên trên ảnh là
"У9"**. Khối mạch chính (phần trên trang) cũng có một hộp 2 đoạn `У9-1`/`У9-3` ở góc trên-
trái. **Không xác nhận được** 2 ref này có phải cùng 1 linh kiện vật lý hay là 2 linh kiện
khác nhau trùng số (có khả năng các khung mẫu dùng hệ đánh số CỤC BỘ riêng, độc lập với khối
chính — tương tự cách `ric18_mota.md` mô tả "Ячейка усилителя" dùng ref mẫu `У13,У14,...`
lặp lại 16 lần cho 16 kênh thật). Để tránh vi phạm ràng buộc "ref duy nhất trong BOM" của
`check_ric16.py`, bản ghi trong file này đặt tên khung mẫu là **`У9b`** (theo đúng tiền lệ
`У44b` của `ric10_mota.md` §"Xác nhận hai tờ..."), và ghi rõ trong note của cả 2 dòng BOM
rằng đây là lựa chọn đặt tên của người chép, **không phải ký hiệu in trên ảnh**.

## 6. Khảo sát sơ bộ khối mạch chính — CHƯA lần netlist

Khối mạch chính (2 cụm logic dày đặc) khảo sát bằng cách chia lưới 4 cột × 2 hàng (8 ô,
mỗi ô ~2284-2450×1170px, downscale ~0,5× khi xem — đủ nét để đọc nhãn in). Kết quả: tối
thiểu **16 vỏ IC** (`У9,У10,У11,У12,У13,У14,У16,У17,У18,У19,У24,У25,У26,У27,У28,У29` — nhiều
vỏ có đánh dấu đoạn `-1..-4`, quy ước giống `Уnn-m` của ric10), **22 điện trở**, **2 tụ**
(`C7,C8`), **6 diode** (`Д1,Д3,Д4,Д5,Д8,Д9`), **4 transistor** (`T1,T2,T3,T4`).

**Ghi chú về độ tin cậy của khảo sát này**: một lần đọc thử bị sai do nhầm chữ "У" in nhỏ
với chữ số "7"/"8"/"9" (ví dụ nhãn thật là `У15-3` từng bị đọc nhầm thành "795-3" ở lần soát
đầu, **đã SỬA sau khi zoom riêng `spot_795.jpg` ở độ phóng đại 2×**). Vì lỗi loại này có
thể còn sót ở những nhãn CHƯA được zoom riêng (chỉ đọc qua tile tổng quát), **4 nhãn sau bị
loại khỏi BOM** vì độ tin cậy quá thấp để khẳng định: một dãy hộp điện trở dạng dải có nhãn
đọc tạm "895-x"/"995-x" (nghi là `У17-x` hoặc 1 vỏ khác giữa У16 và У18, chưa xác nhận);
một hộp lớn đọc tạm "У15" (pin 1,2,7,4/10) xuất hiện CẠNH dãy hộp dải đã nghi là У15-x khác
loại — **2 cách đọc này MÂU THUẪN nhau** (không thể cùng là У15), nên **cả 2 đều KHÔNG đưa
vào BOM** cho tới khi có crop riêng xác nhận; cặp diode cạnh T4 đọc "Д5" (tin cậy trung
bình) và "Д7" (tin cậy THẤP, có thể là Д6) — chỉ Д5 được đưa vào BOM với ghi chú, Д7/Д6
**không đưa vào BOM** vì chưa chắc chắn số.

**Hoàn toàn chưa lần netlist** cho toàn bộ khối này (ngoại trừ vài liên kết mức-khối ghi
chú trong `ric16_net.csv`, ví dụ T1←R28, T1→R31→cực ngoài"23", chuỗi Д8-R44-R45-Д9→"ПП",
dãy diode А2→У17 qua R21-R24) — lý do là **khối lượng linh kiện quá lớn** so với ngân sách
một phiên làm việc (đúng như lý do đã ghi ở рис.10/§2 của `ric10_mota.md`), **KHÔNG phải
do ảnh hỏng**. Mỗi ref trong nhóm này có đúng 1 dòng placeholder `НЕ ПРОСЛЕЖЕНО <ref>.?`
trong `ric16_net.csv`.

## 7. Lưới cầu 11 tụ (C6,C8,C9,C10,C11,C14-C19) và ghi chú chung

Ô vẽ nhỏ cạnh khối ghi chú chữ viết tay (góc dưới-phải trang) vẽ 3 thanh ngang `В` (trên),
`Зо` (giữa), `Б` (dưới) nối với nhau qua 2 tụ phân cực dọc riêng lẻ (`C9`: В-Зо; `C10`:
Зо-Б) và 2 chuỗi tụ ngang nối tiếp (`C14-C16-C18`: В-Зо; `C11-C6-C8-C15-C17-C19`: Зо-Б).
**Đánh giá: đây là SƠ ĐỒ MINH HOẠ cách bus các tụ rải rác trong khối chính, không phải một
cụm mạch độc lập** — suy luận từ việc `C8` (1 trong 11 tụ của lưới) cũng quan sát được NẰM
RIÊNG trong khối mạch chính (cạnh `R42`/`У27`, §6); khả năng cao là cùng 1 linh kiện vật lý
nhưng **không xác nhận chắc chắn 100%** (ghi rõ trong note BOM của C8).

Ghi chú chữ viết tay (nguyên văn, đọc trực tiếp, không phải suy diễn):

> Провода с одинаковыми буквенными и цифровыми обозначениями соединить между собой.
>
> Контакты 11 микросхем 168КТ2Б соединить с шиной питания +6,3В (г).
>
> Микросхемы 302НР1Г должны иметь одинаковую маркировку номера сопроводительного листа.
>
> Контакты 11 микросхем 168КТЗВ соединить с шиной питания +3,5В (г).

(dịch: nối các dây cùng ký hiệu chữ/số với nhau; nối chân "11" của IC 168КТ2Б vào thanh
nguồn +6,3В (điểm "г"); các IC 302НР1Г phải cùng số lô sản xuất ghi trên phiếu kèm; nối chân
"11" của IC 168КТ2В vào thanh nguồn +3,5В (điểm "г")). **Ghi chú này gần như GIỐNG HỆT** quy
tắc đã đọc ở `ric15_mota.md` §5 cho tấm Y9 (nối chân "Л"/"М" của cùng loại IC vào +6,3В/
+3,5В) — hai tấm Y8/Y9 dùng chung họ linh kiện chuyển mạch `168КТ2Б/В` và quy tắc nguồn
giống nhau, củng cố độ tin cậy của cả 2 lượt chép. **Không tạo thêm dòng net riêng cho chân
11 của từng IC** dựa trên suy diễn từ ghi chú này — chỉ ghi nhận như quy tắc nguồn chung,
đúng theo tinh thần `ric10_mota.md` §"Giới hạn phương pháp".

## 8. Tổng kết số liệu (xác nhận bằng `check_ric16.py`)

`python3 check_ric16.py` → PASS. Số liệu chính xác (script tự in ra, không tính nhẩm):
`ric16_bom.csv` **86 ref vật lý**; `ric16_net.csv` **155 dòng chân**, trong đó **70 dòng
truy trực tiếp** (đã lần được kết nối thật) và **85 dòng placeholder** `НЕ ПРОСЛЕЖЕНО`;
`ric16_conn.csv` **42 dòng** bảng `П1`.

## 9. Việc còn lại cho lượt soát sau (nêu rõ, không giấu)

1. Soi riêng từng vỏ IC của khối mạch chính (16+ vỏ) để tách netlist thật — ưu tiên các
   cụm có ít dây chồng nhất trước (học theo cách ric08/ric15 đã làm nhiều lượt).
2. Crop độ phân giải cao hơn cho bảng П1 để đọc chắc chắn dòng số Конт. nhỏ (xác nhận hoặc
   bác bỏ giả thuyết "2 dãy song song offset" ở §4).
3. Xác nhận lại 2 nhãn mâu thuẫn "У15" (§6) và cặp diode Д5/Д7(?) bằng crop riêng.
4. Xác nhận mảnh "Схема узла и[нвертора]" thứ 2 nghi vấn ở §3.4 (R7/R8/R47/R48?).
5. Xác nhận quan hệ У9(khung mẫu, đặt lại tên У9b)↔У9(khối chính) — §5.
