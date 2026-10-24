# Chép рис.7 — Y6 — ЕУ3.057.140 (Э3)

- Phạm vi: chỉ ba ảnh E3_lis1-3_recapture-2026-10-24.jpg, E3_lis2-3_recapture-2026-10-24.jpg, E3_lis3-3_recapture-2026-10-24.jpg do người dùng chỉ định.
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
