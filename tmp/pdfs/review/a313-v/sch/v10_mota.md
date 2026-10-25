# v10 — V.10 (không có trong sodocactam; nhãn nhầm V.09)

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: nguồn SchDoc mang nội dung tấm linh kiện rời rạc V.10, không phải tấm trung gian V.09.
- SchDoc: `tamcaclinhkienroirac/A313_10.SchDoc` (ánh xạ đang mâu thuẫn).
- SHA-256 SchDoc: `a7b5be7256c258afdd4314f2c402ed7bf773562c4b48928b242bb73750386e23`.
- `sodocactam.pdf` trang 10: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN TẤM MẠCH TRUNG GIAN A313_V.09`.

## Thống kê trích xuất

- Ref BOM: 7; net: 5; chân: 26; dòng đầu nối: 14.
- Net một chân đã khai báo ngoại lệ: 0; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 10: 12 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 47: 12 ref, 12 ref đầu nối (DC1, DC10, DC11, DC12, DC2, DC3, DC4, DC5, DC6, DC7, DC8, DC9).
- Kết quả lệch: sodocactam: 12 ref so với SchDoc 7 ref; BVTK: 12 ref so với SchDoc 7 ref; BVTK: 12 ref đầu nối so với SchDoc 1.

## Điểm mơ hồ và giới hạn

- Mâu thuẫn định danh: sodocactam tr.10 và BVTK BV.38/BV.41 là V.09 với 12 đầu DC; file được giao A313_10.SchDoc là tấm linh kiện rời rạc V.10.
- So với BVTK V.10/BV.44: 6 ref linh kiện; SchDoc có thêm DC15 nên thành 7 ref.
- Có 0 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v10.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
