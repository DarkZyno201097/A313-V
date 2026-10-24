# Mô tả bản chép BOM và netlist từ hai ảnh

- Nguồn duy nhất: RE_tr175_a171.jpg và RE_tr176_a172.jpg; hai ảnh được xử lý như cùng một sơ đồ.
- Số trang 175/176 dùng theo tên file được chỉ định, không khẳng định là số in trên bản vẽ.
- Không thấy khung tên, số «рис.» hoặc mã bản vẽ đủ rõ trong phạm vi hai ảnh; tên output ric09 do yêu cầu, không phải số hình đã xác nhận.
- BOM: 49 dòng, gồm У1–У23, R1–R15, C1–C8 và П1–П3; mỗi ref tính một linh kiện, không đếm lại các cổng cùng IC.
- Netlist: 489 dòng; chép chân xuất hiện trên hình và chân nguồn theo hai chú thích rõ ở trang 175.
- Không bổ sung các chân IC khác từ pinout/tra cứu bên ngoài; danh sách này không phải netlist đã xác nhận để chế tạo.

## Cấu trúc đọc được
- Trang 175: У1–У4 mang ký hiệu CT2; có các chân C1, C2 và R0, các nhánh nối tầng và hai đường chung vào chân 2/3.
- У7–У9 là các khối đảo thể hiện bằng vòng tròn ở đầu ra; У10–У13 có cổng ký hiệu & và đầu ra đảo.
- Các đầu ra У10–У13 được ghi M0–M15 và địa chỉ П3-48…П3-63; đã giữ đúng thứ tự từng dây, không sắp lại theo suy đoán chức năng.
- У5, У6, У14–У16 cùng R1 thuộc phần điều khiển; thấy nhãn «Исправность», «Принуд. пуск», «Запр. принуд. пуска».
- C1–C4 mắc song song giữa các điểm б và а trên trang 175.
- Trang 176: bốn nhánh F1–F4 đi từ П1-36…П1-39 qua C5–C8 và R2–R5 tới У19.
- У17 và У18 mỗi khối vẽ tám diode; thanh chung У17 chân 11 qua R6 tới б, thanh chung У18 chân 11 tới в.
- R7–R10 nối hồi tiếp quanh các cặp cổng У19/У20; R11–R14 nối từ các nút giữa hai cổng tới б.
- У21–У23 và hai cổng У14 tạo phần logic phía sau; đầu ra У14 chân 6 ghi địa chỉ У4-14, đầu vào tương ứng trên trang 175 ghi «У14.6(2)».
- R15 được vẽ giữa П1-32 và điểm б.
- Ba bảng П1, П2, П3 có tiêu đề «Цепь» và «Конт.»; các đường qua bó dây được ghép bằng đường bó và số nhánh nhìn thấy, không chỉ bằng tên giống nhau.

## Quy ước và mức chắc chắn
- Chắc ở mức đọc ảnh: ref, phần lớn số chân, các dây/chấm nối đã chép, các nhãn M0–M15/F1–F4 và các điểm а/б/в.
- N01…N64 là tên tự đặt cho các nút không có tên rõ hoặc có nhãn nguồn mâu thuẫn; không phải tên gốc.
- Điểm а/б được gộp theo ký hiệu điểm và chú thích nguồn rõ trên bản vẽ; điểm в theo mũi tên và đường bó dây số 18.
- Chú thích 1 trang 175: «Выводы 10 микросхем У1...У4 и выводы 7 всех остальных микросхем, кроме У17, У18 подключить к потенциалу „Корпус“ (точка „а“).»
- Chú thích 2 trang 175: «Выводы 5 микросхем У1...У4 и выводы 14 всех остальных микросхем, кроме У17, У18 подключить к потенциалу „+5В“ (точка „б“).»
- Toàn bộ name trong BOM là «?» vì hai ảnh không cung cấp trị số R/C, mã IC/khối diode hoặc mã đầu nối đọc được; không suy ra họ IC từ hình cổng.
- Pin «?» của C5–C8: ảnh có dấu + phía nối điện trở nhưng không ghi số chân; hai dòng mỗi tụ được phân biệt bằng phía trái/phải trong note.
- Net «?» của У1 chân 8/11, У17 chân 2/3/5/7 và У18 chân 2/6/8/7: chỉ thấy đầu chân ngắn, không thấy lưới đi tiếp; chưa kết luận NC.
- Net «?» ở các hàng П1–П3 còn trống: ô tên mạch không ghi và không thấy dây; bảng không đủ chứng cứ để khẳng định các chân này không dùng.
- Nhãn «рР?К2»: ký tự viết tay sau Р chưa phân biệt chắc giữa chữ và chữ số; «рС?К»: chữ ở giữa chưa phân biệt chắc; giữ phần đọc được và dấu ?.
- Nhãn «С?Д→М», «?t-4», «СПК?К-1»: tương ứng chưa đọc chắc ký tự sau С, ký tự đầu trước t, và ký tự trước К-1; không tự chuẩn hóa theo chức năng.
- Bó dây số 14 giữa П1-49 và П3-29 thấy nối, nhưng nhãn lần lượt ghi «+12,6В» và «−12,6В»; dùng N riêng và giữ cả hai nhãn trong note, không sửa dấu.
- Có dấu gạch nhỏ tại đầu chân 7 của У17; chưa rõ là gạch bỏ hay dấu đầu dây. Không thấy linh kiện nào bị gạch chéo toàn bộ đủ chắc để kết luận loại bỏ.
- Không mở tài liệu khác, không tra mã linh kiện, không kiểm chéo với repo hoặc chạy script kiểm chéo; chỉ phóng/xoay ảnh trong bộ nhớ và định dạng dữ liệu chép thành ba file.
