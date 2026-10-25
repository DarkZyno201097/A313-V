# Рис.10 — «Формирователь ПК и магистрали» (Y1, ЕУ2.035.587) — hai tờ sơ đồ

**Trạng thái: PARTIAL.** Nguồn: hai ảnh chụp —
`A313-3_CONTROL/Y1/RE_tr179_a175.jpg` (gọi tắt **tờ 1**, trang catalogue 179) và
`A313-3_CONTROL/Y1/RE_trXXX_a075.jpg` (gọi tắt **tờ 2**, xếp vật lý giữa trang 79/80,
catalogue gọi "tờ #75"). Ảnh thứ ba `Y1.jpg` là ảnh chụp PCB thật, **không dùng làm
nguồn transcribe** (chỉ tham khảo), đúng như giới hạn đề bài.

Phương pháp: crop từng vùng bằng PIL (giữ nguyên độ phân giải gốc, chỉ phóng to
scale 1.6-2.5× bằng LANCZOS resample, không downscale trước khi soi), rồi đọc trực
tiếp từng crop bằng vision. Danh sách crop đã soi: `s1_u5_diode.jpg`, `s1_u4_diode.jpg`,
`s1_topright_logic.jpg`, `s1_midright.jpg`, `s1_bottomleft_table.jpg`,
`s1_bottomright_transistor.jpg`, `s2_icgrid_top.jpg`, `s2_icgrid_bottom.jpg`,
`s2_p3_table.jpg`, `s2_tab2_top/mid/bottom.jpg`, `s2_tab2_header.jpg`,
`s2_tab2_boundary.jpg`, `s2_resnet.jpg`, `s2_resnet_lastic.jpg`,
`s2_handwritten_notes.jpg` (các file này nằm trong thư mục tạm của phiên làm việc,
không commit vào repo — có thể tái tạo bằng toạ độ crop ghi trong code gen_ric10*.py
nếu cần soát lại).

## Quy mô — vì sao đây là bản PARTIAL, không phải đầy đủ

Khác với рис.14 (26 ref, một khối socket nhỏ), tấm Y1 (рис.10) là **hai tờ sơ đồ số
lượng linh kiện rất lớn**: tờ 1 ước tính 40+ IC/transistor/tụ/điện trở, tờ 2 là một
**lưới giải mã/thanh ghi dịch dày đặc** ước tính 50+ IC cộng một mạng điện trở riêng.
Soi từng chân của toàn bộ ~82 ref trong ngân sách một phiên làm việc là không khả thi
ở độ phân giải ảnh gốc hiện có (ảnh 1926×2568 và 2976×3968, chụp bằng điện thoại,
không phải scan phẳng). Chiến lược áp dụng, theo đúng tinh thần "PARTIAL-but-honest":

1. **BOM đầy đủ nhất có thể** — liệt kê mọi ref designator đọc được trực tiếp trên cả
   hai tờ (82 dòng), kể cả khi chưa soi chi tiết từng chân.
2. **Netlist chọn mẫu sâu** — soi kỹ và truy đầy đủ các cụm có bằng chứng ảnh rõ ràng:
   hai dãy diode ИЛИ (У45, У64) và 4 thanh ghi chúng nạp (У9, У10, У11, У12); cụm 2
   transistor У63 cùng mạch phân cực (R18, C7, R20, У5.1); một nhánh đầy đủ của cây
   giải mã tờ 2 (У31→У29→У27, hàng vào 0-3); toàn bộ mạng điện trở R24-R33 cùng 4 IC
   nguồn (У18.1, У19.1, У20.1, У21.1-suy-ra) nối tới các chân П1/21-28; bảng kết nối
   П3 đầy đủ 48 dòng có chữ.
3. **Phần còn lại: placeholder `НЕ ПРОСЛЕЖЕНО <ref>.<pin>`** — mỗi ref BOM chưa soi chi
   tiết được gán đúng 1 dòng net với `pin="?"`, lý do ghi rõ là **khối lượng linh kiện**
   (không phải một vết hỏng cụ thể) — khác với рис.14 nơi lý do luôn là một chỗ hỏng ảnh
   cụ thể (nếp gấp, vết ố). Đây là khác biệt quan trọng cần nêu rõ, không gộp chung.

## Xác nhận hai tờ có phải cùng một bản vẽ hay không

**Chưa xác nhận 100%, nhưng có bằng chứng hỗ trợ khá mạnh — đánh giá: NHIỀU KHẢ NĂNG đúng.**

Bằng chứng ủng hộ (quan sát trực tiếp trong phiên này):

- **Không trùng dải số ref giữa hai tờ ở phần lớn trường hợp.** Tờ 1 dùng chủ yếu
  У1-У17, У43-У64; tờ 2 dùng chủ yếu У18-У41, У58. Nếu đây là 2 bản vẽ độc lập không
  liên quan, kỳ vọng thống kê là chúng sẽ đánh số trùng lặp nhiều hơn (mỗi tờ tự đánh
  lại từ У1). Việc **ít trùng** phù hợp với giả thuyết đánh số liên tục cho toàn bộ
  tấm Y1 trên cả 2 tờ.
- **Có đúng 2 trường hợp trùng số** đã phát hiện và ghi nhận minh bạch trong BOM/net
  (không giấu): `У44` (xuất hiện cả 2 tờ — ghi `У44b` ở tờ 2) và `R29`/`Р29` (tờ 1 là
  nhãn tiếp điểm cạnh dãy diode У64, tờ 2 là điện trở thật trong mạng R24-R33 — ghi
  `R29b` ở tờ 2). Đây là NGOẠI LỆ, không phải quy luật — không đủ để bác bỏ giả thuyết
  đánh số liên tục, nhưng cũng không chứng minh được chắc chắn 100% (có thể là trùng
  ngẫu nhiên giữa 2 bản vẽ không liên quan).
- **Cùng kiểu ký hiệu/quy ước trên cả 2 tờ**: nhãn tín hiệu dạng `П1/xx(1)`, `П2/xx(1)`,
  `П3/xx(1)` xuất hiện dày đặc ở CẢ HAI tờ với cùng cú pháp; cả hai tờ dùng cùng ký hiệu
  mũi tên bó dây `а`/`б`/`d` nối ra ngoài khung; cả hai tờ có chữ ký hiệu diode/IC viết
  tay cùng phong cách (chữ 'У' dễ lẫn số '4', nét kẻ khung chữ nhật giống nhau).
- **TÌM ĐƯỢC liên kết tín hiệu xuyên tờ cụ thể**: bảng П3 (tờ 2) có dòng `29 = Выд.ПК2`;
  đúng nhãn `П3/29(1)` với chú thích `Выд.ПК2` lại xuất hiện làm input của IC У20.1
  **trên CHÍNH tờ 2** (không phải tờ 1) — nên đây CHƯA PHẢI bằng chứng xuyên tờ. Tìm
  kiếm kỹ hơn: tờ 1 có nhãn `П3/13(1)/ПК вх` (đầu ra У46.4) và bảng П3 ở tờ 2 có dòng
  `3 = ПК вх.` — số thứ tự không khớp (13 so với 3), nên đây CŨNG KHÔNG xác nhận được
  trực tiếp là cùng một chân vật lý (có thể do cách đánh số `П3/xx(1)` khác với số thứ
  tự `Конт.` trong bảng, hoặc `(1)` là một ký hiệu nhóm/trang riêng chưa giải mã).
  **Kết luận cụ thể: KHÔNG tìm được một cặp nhãn `П3/xx` giống hệt số xuất hiện ở CẢ
  HAI tờ cùng lúc** — mọi nhãn `П3/xx` quan sát được trên tờ 1 (ví dụ `П3/26,27,28,
  36,37,38,39,40,41,46`) không trùng số thứ tự với bất kỳ dòng nào trong bảng П3 đọc
  được ở tờ 2 (dòng 1-48 chủ yếu các số khác). Đây có thể do: (a) bảng П3 ở tờ 2 là một
  connector HOÀN TOÀN KHÁC (không chung dải số) dùng tình cờ cùng tên "П3", hoặc (b) các
  số `П3/xx(1)` ở tờ 1 tham chiếu tới MỘT TỜ KHÁC chưa được chụp/không có trong 2 ảnh
  này, hoặc (c) chúng thực sự khớp nhưng tôi chưa xác định đúng cặp do khối lượng dữ
  liệu.

**Đánh giá cuối cùng:** hai tờ **CÓ THỂ** là cùng một bản vẽ рис.10 (phong cách, cú
pháp nhãn, dải số ref phần lớn không trùng — ủng hộ), nhưng **KHÔNG tìm được bằng
chứng xuyên tờ trực tiếp kiểu "nhãn П3/xx ở tờ 1 khớp đúng số dòng trong bảng П3 ở
tờ 2"** — nên theo đúng yêu cầu đề bài, **giữ nguyên trạng thái "nhiều khả năng nhưng
chưa xác nhận"**, không nâng lên "đã xác nhận".

## Bảng kết nối П3 và hai bảng bên phải — có phải cùng 1 đầu nối không?

**KHÔNG — đây là 3 bảng khác nhau**, xác định bằng cách quan sát **số thứ tự
reset về 1** giữa các bảng:

- `П3` (bảng chính, rõ nét, 48 dòng có chữ trong khoảng 1-52): **SỬA LẠI sau spot-check
  độc lập của coordinator** — designator "П3" THỰC SỰ CÓ ghi viết tay ngay phía trên
  tiêu đề "Конт."/"Цепь" (đọc trực tiếp, không phải suy luận từ nhãn `П3/xx(1)` như báo
  cáo ban đầu của subagent). Đã zoom xác nhận chữ "П3" rõ nét tại toạ độ ~(2050,230)
  trên ảnh gốc. 3 dòng đầu đối chiếu khớp: 1=Корпус, 2=ПК вых., 3=ПК вх.
- `П3-right-1` (bảng thứ 2, ngay bên phải bảng П3): bắt đầu tại Конт.1 = "+"(?),
  kết thúc ở Конт.27 = "Ко" (gần chắc chắn "Корпус"). KHÔNG thấy nhãn designator nào
  phía trên bảng — mép trên bị che bởi nếp giấy cong khi chụp (xem `s2_tab2_header.jpg`:
  toàn bộ phần trên khung là giấy trắng cong, không có chữ).
- `П3-right-2` (bảng thứ 3, ngay dưới bảng thứ 2): **Конт. RESET về 1 = "Ко"**
  (Корпус) một lần nữa — đây là bằng chứng rõ ràng nhất rằng đây là MỘT CONNECTOR
  KHÁC, không phải phần tiếp nối của bảng thứ 2 (nếu là tiếp nối, số thứ tự sẽ tiếp tục
  tăng, không quay lại 1). Cũng không thấy designator nào trong khung ảnh.

**Không xác định được những bảng này tương ứng với đầu nối nào** (П1? П2? một đầu
nối khác?) vì không có chữ designator nào lọt vào khung chụp. Phần lớn nội dung cột
"Цепь" của 2 bảng này chỉ đọc được 2-4 ký tự đầu (ví dụ "Ки", "Кш", "Эхо", "ВхО",
"Ис.") — **nguyên nhân cụ thể: mép phải của TRANG GIẤY GỐC bị cắt khỏi khung ảnh khi
chụp** (cắt vật lý do góc chụp/gấp trang, không phải do crop của công cụ — đã kiểm
bằng cách crop rộng tới tận x=2976, tức mép phải của file ảnh, vẫn thấy chữ bị cụt).
Không suy diễn các từ đầy đủ từ các mảnh 2-4 ký tự này — ghi nguyên văn mảnh đọc được.

## Những gì không truy được, và nguyên nhân cụ thể cho từng loại

- **Tờ 1, cụm logic chéo góc trên-phải (У1, У2, У14, У15, У17, v.v.)**: xác nhận vị
  trí và một số nhãn tín hiệu đúng với mô tả đề bài (Стрдe1≈"СТ1-1", Стрдe2≈"СТ2-1"/
  "стрoд2", Топ, D→РДР, Сдвиг кода đều đọc được), nhưng **không tách được từng cặp
  chân** trong vùng 4 IC bắt chéo (У1.1-3/У2.1-2) — các đường nét giao nhau hình chữ X
  dày đặc trong phạm vi <10px ở độ phân giải ảnh gốc, zoom 2× không đủ tách.
- **Tờ 1, bảng А/Б góc dưới-trái (chuỗi IC У47-У56)**: cấu trúc tổng thể rõ (4 chuỗi
  song song cho 4 nhóm hàng 0-3/4-7/8-11/12-15, gộp vào cột thu gom У47 bên phải — xem
  task mô tả khớp), nhưng **chữ số hàng chục của nhiều ref (49 vs 44, 52 vs 53, 56...)
  không phân biệt chắc chắn** — chữ viết tay nghiêng, nét số bị nhoè ở quy mô ảnh hiện
  có; đã ghi "đọc chưa chắc chắn" riêng cho từng ref này trong BOM thay vì khẳng định.
- **Tờ 1, cụm У63 (transistor) và chuỗi У61/У62**: 4 chân chính (12,4-5,11→3,10) và
  3 nhãn lỗi (Исправн.ключ/ТТЛ/.) đọc được; nhưng **chưa xác nhận được đúng chân nào
  của У63 nối trực tiếp tới `П1/39` so với qua trung gian У61/У62** — chuỗi IC trung
  gian (У61.2→.3→.4, У62.2→.3) đọc được nhãn nhưng không soi riêng từng mắt nối.
- **Tờ 2, lưới giải mã chính (~50 IC, У27-У41)**: chỉ truy đầy đủ MỘT nhánh mẫu (hàng
  vào 0-3: У31→У29→У27) theo đúng yêu cầu đề bài "trace 1 instance rồi verify các
  instance khác có thực sự giống hệt hay chỉ giống thoáng qua". **Đã verify bằng mắt**:
  nhánh hàng 4-7 (У32→У30→У28) có cấu trúc box/pin-count GIỐNG hệt nhánh 0-3 (cùng 4
  section × 3 tầng × ra 2 IC gộp), nhưng nhãn số tầng cuối khác (ra "4,5,6,7" thay vì
  "0,1,2,3") — **xác nhận ĐÂY LÀ MẪU LẶP LẠI THẬT, không phải khối khác loại giả dạng
  giống nhau** — nhưng KHÔNG soi riêng để trace từng chân của nhánh 4-7 (chỉ xác nhận
  cấu trúc, chưa trace chi tiết, vì ngân sách phiên làm việc). Hai nhánh còn lại
  (hàng 8-11, 12-15) CHỈ xác nhận bằng mắt là "trông giống" (box count, vị trí) nhưng
  **CHƯA verify kỹ như đã làm với nhánh 4-7** — không khẳng định chắc chắn là giống hệt,
  chỉ ghi "trông giống" trong BOM.
- **Tờ 2, chữ số hàng chục của У37/У39/У41 (hàng 8-11)**: ảnh gốc ở vùng này buộc phải
  downscale 4× khi soi tổng quan (crop 2560×3228 → hiển thị 640×807) để vừa khung vision
  — độ phân giải hiệu dụng thấp hơn các vùng khác, nên các chữ số 2 ký tự dễ lẫn (37 vs
  39 vs 31...); chưa re-crop tách riêng từng IC này do giới hạn thời gian phiên.
- **Mạng điện trở R24-R33, chữ cuối của nhãn "ПКдж/ПКдк" (R30) và "ПКц1/ПКц4" (R32)**:
  nét chữ viết tay nghiêng ở đúng ký tự cuối, ảnh ở `s2_handwritten_notes.jpg` không đủ
  sắc nét để phân biệt hai cách đọc — ghi cả 2 khả năng, không chọn 1 cách tuỳ tiện.
  Ranh giới nhánh "У19.1 nối R27-R28 hay R27-R29" cũng dựa trên suy luận từ vùng chồng
  lấn giữa 2 ảnh crop (`s2_resnet.jpg` và `s2_resnet_lastic.jpg`) — ghi rõ trong mota
  là tái dựng từ overlap, không phải đọc trực tiếp liền mạch trên 1 ảnh.
- **Ghi chú tay cuối tờ 2** (quy tắc chân 7→"Корпус", chân 14→"+5В" cho mọi IC):
  đọc được rõ, trích nguyên văn: *"1. Выводы 7 всех микросхем подключите к потенциалу
  'Корпус' (точка 'd'). 2. Выводы 14 всех микросхем подключите к потенциалу '+5В'
  (точка 'd')."* — đây là **GHI CHÚ CHUNG**, theo đúng chỉ dẫn đề bài, **KHÔNG tạo
  thêm dòng net riêng cho chân 7/14 của từng IC** dựa trên suy diễn từ ghi chú này;
  chỉ ghi nhận ở đây như một quy tắc nguồn điện chung áp dụng cho toàn tờ 2.

## Những gì ĐÃ xác nhận chắc chắn (đọc trực tiếp, không suy diễn)

- Hai dãy diode ИЛИ 8 ngõ vào У45 (tờ1) và У64 (tờ1), đầy đủ 8 nhãn tín hiệu vào mỗi
  dãy, đọc trực tiếp từ bó dây bên trái (xem net.csv).
- Toàn bộ 48 dòng có chữ của bảng П3 (tờ 2), đọc rõ nét ở crop riêng không bị downscale
  mạnh (`s2_p3_table.jpg`, scale 1.8× giữ được độ sắc nét).
- Toàn bộ mạng điện trở R24-R33 (tờ 2) với 6/10 đích `П1/xx` đọc rõ ký tự số, 4/10 còn
  lại chỉ ra thanh chung 'd'.
- Cụm У63 (2 transistor) với 4 nhãn tín hiệu lỗi/báo hỏng đọc rõ.
- Khung tổng thể của cây giải mã tờ 2 (4 nhánh song song × 3 tầng IC × gộp ra 2 IC),
  xác nhận lặp lại thật (không phải nguỵ trang giống nhau) cho ít nhất nhánh hàng 0-3
  và 4-7.

## Giới hạn phương pháp — không lặp lại lỗi đã biết của dự án

- Không gán trị số Ω/pF cho bất kỳ điện trở/tụ nào — **không ký hiệu nào trên cả 2 tờ
  có trị số in/viết kèm**, kể cả R18-R33 và C1-C7; đã kiểm bằng zoom, ghi rõ "trị số
  không in" thay vì bỏ trống im lặng.
- Không gán tên IC/loại linh kiện (К155xx, К555xx...) cho bất kỳ box nào — không box
  nào có chữ loại linh kiện in kèm, giống phát hiện của рис.14.
- Hai trường hợp trùng ref (`У44`/`У44b`, `R29`/`R29b`) được giữ nguyên minh bạch thay
  vì gộp hoặc đổi số ngầm — xem BOM/net để biết lý do kỹ thuật (checker yêu cầu ref
  BOM duy nhất).
- Không tạo dòng net giả cho các chân chưa soi — mọi ref BOM chưa trace chi tiết đều có
  đúng 1 dòng placeholder `НЕ ПРОСЛЕЖЕНО <ref>.?` với lý do cụ thể (khối lượng linh
  kiện lớn, không phải một vết hỏng ảnh cụ thể — khác рис.14).
