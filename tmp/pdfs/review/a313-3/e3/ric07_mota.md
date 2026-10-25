# Chép рис.7 — Y6 — ЕУ3.057.140 (Э3)

- Phạm vi: chỉ ba ảnh RE_trXXX_a255.jpg, RE_trXXX_a256.jpg, RE_trXXX_a257.jpg (л.1/3, л.2/3, л.3/3; đổi tên 2026-10-24 theo quy tắc DANH-MUC_ANH_RE_A-313-3.md §0, trước đó tên tạm E3_lis1-3_recapture-2026-10-24.jpg…) do người dùng chỉ định.
- Tên “Устройство управления преобразованием”, khối A-313-3, Y6 và рис.7 lấy từ yêu cầu; không thấy trọn khung tên để xác nhận độc lập các dòng này.
- Chữ ghi tay nhìn thấy trên cả ba tờ: «ЕУ3.057.140 Э3»; số tờ ghi tay lần lượt «1/3», «2/3», «3/3».
- Không thấy đủ khung tên tiêu chuẩn, ô người vẽ/duyệt hoặc bảng liệt kê linh kiện.
- Лист 2: «(Начало см. на листе 1)» bên trái và «(Продолжение см. на листе 3)» bên phải.
- Лист 3: «(Начало см. на листе 2)» ở mép trái sau khi xoay để đọc.

## Cấu trúc nhìn thấy
- Лист 1 có khung «Я1…Я4»: các phần tử У1…У9, nhiều phần ký hiệu & và 1, các dây ghi S1…S4, R1…R4, A1…A4, Q1…Q4 có gạch trên.
- Лист 1 có khung «Я5…Я6»: У10…У13, bốn ký hiệu TT, các đầu Д1…Д4, S, C, R, Q1…Q4.
- Hai khung trên là sơ đồ mẫu; tiền tố Я1…Я4/ hoặc Я5…Я6/ trong CSV là phạm vi do người chép thêm để tránh lẫn các ký hiệu nội bộ.
- Qty 4 hoặc 2 trong BOM theo số Я ghi ở tiêu đề khung; không coi đây là kiểm đếm linh kiện thực.
- Лист 2 vẽ riêng các khung Я1…Я6 với dấu * và bus А có các số nhánh 0…15; xung quanh có các cổng logic và R2.
- Các đầu S/R/CS/CR/A/Q/B trong netlist của Я là nhãn đầu mút chức năng, không phải số chân vật lý IC.
- Лист 3 có các nhóm logic, TT của У49, R1 và C1…C5; nhiều đường có tham chiếu П1/П2/П3 hoặc У.../(лист).
- Phần ký hiệu gần mép dưới của лист 1 và góc dưới phải лист 3 bị cắt/mờ; không tự hoàn chỉnh phần không nhìn thấy.

## Bảng đầu nối — phần ưu tiên
- ric07_conn.csv có 173 hàng: П1 = 1…53; П2 = 1…53; П3 = 1…67; tất cả nằm trên л.1.
- Thứ tự trên ảnh của П1/П2 đan xen 1,28,2,29,...; CSV sắp số Конт. tăng dần, giữ đủ từng chân.
- Signal trống có hai trường hợp: ô trống thật hoặc ô có chữ nhưng chưa đọc chắc; note phân biệt rõ.
- Không mở rộng chữ viết tắt. Các nét gạch trên/xung vuông được ghi chú khi đọc được; không mặc định chúng là dấu gạch bỏ.

## Độ chắc và mọi dấu hỏi
- BOM: 77 hàng; name = ? vì không thấy/không đọc được mã hoặc trị số. Ký hiệu &/1/TT không đủ để suy mã IC.
- ref = ? dùng cho các ký hiệu sát mép dưới лист 1 và góc dưới phải лист 3 chưa đọc chắc; note nêu vị trí, không chốt số У bằng thứ tự.
- Netlist: 997 hàng; 184 hàng có net = ? vì điểm đến chưa chắc hoặc ô Цепь trống/khó đọc; đây là bản chép PARTIAL, không phải netlist đã xác nhận đầy đủ.
- 4 hàng có pin = ?: đầu ra У23.2 chưa đọc rõ số; hai đầu C5 không thấy số chân; một ký hiệu bị cắt ở mép dưới лист 1.
- Các đầu C5 chỉ phân biệt trên/dưới trong note; không tự gán số chân theo quy ước tụ điện.
- Nxxx là tên tạm cho đoạn dây không có nhãn; chỉ nối các đầu mút đã theo được trên ảnh. N900 ghi vòng hồi tiếp У25 sau khi xem phóng to.
- Hậu tố @ trong tên net phân biệt vị trí/nhánh chép; không phải một phần tên tín hiệu gốc. Không gộp nhánh chỉ vì tên tín hiệu giống nhau.
- Dòng net của П1/П2/П3 chỉ chép quan hệ trong bảng Конт./Цепь; không chứng minh đã theo dây từ bảng đến cổng logic.
- Chân 7 và 14 của các У được ghi theo ghi chú 4–5 trên л.2: «Корпус» (điểm б) và «+5В» (điểm a); không tra datasheet.
- BOM có cả khung chức năng và IC bên trong: không cộng toàn bộ qty thành tổng số linh kiện.
- Chưa xác nhận ký hiệu nào là gạch bỏ thật; các vết mờ/giao dây không được tự gán là “gạch bỏ trên bản vẽ”.
- Không đối chiếu Э4, không dùng nguồn ngoài ba ảnh, không kiểm điện/hardware; mọi hàng có ? phải đọc lại trước khi dùng làm dữ liệu kết nối.

## Cập nhật 2026-10-24 — soát lại (Codex đọc ảnh, Claude áp)
- Codex soát 196 dòng có `?` của ric07_net.csv trên ba ảnh a255–a257 → `ric07_soat_raw.csv`: 23 `ro`, 173 `van_chua_ro`
  (lý do: mờ, chữ nhỏ, nếp gấp, dây giao dày; chia đều л.1 60, л.2 50, л.3 63).
- `ric07_soat_apply.py` áp 23 dòng `ro` (chạy lại không đổi kết quả): 19 dòng netlist + 4 ô bảng đầu nối
  (П2/6 «0рРгК2», П2/7 «1рРгК2», П3/17 «0 → РгПР», П3/22 «РгПР → М»). Net gộp mới không có tên rõ đặt `SOAT:…`.
- Netlist còn 175 dòng `?`. `e3_vs_e4.py 7 У6`: 105 khớp / 38 lệch tên / 0 chỉ-Э3 / 14 chỉ-Э4 (trước 103/36/0/18).
  Kiểm chéo: 4 ô bảng mới đọc đều khớp Э4 (П3/17, П3/22 chỉ khác cách viết `→`/`⇒`).
- **Chưa vào `e3_check.py`:** 14 dòng `ref = ?` và 4 dòng `pin = ?` làm trùng khoá (ref, chân) — cần định danh trước.
- **Chưa có trị số linh kiện:** cả 77 dòng BOM `name = ?` vì chưa đối chiếu ПЭ рис.7 — ảnh ПЭ **đã có**: `ЕУ.048.002.РЭ(A313-3)/RE_tr168_a164.jpg`, `RE_tr169_a165.jpg`, `RE_tr170_a166.jpg` (sửa 2026-10-25).
- Đề xuất: chụp lại л.2, л.3 độ phân giải cao hơn (a256/a257 chỉ 1536×2048); điền trị số BOM từ ПЭ tr.168–170.
