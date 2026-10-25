# v01 — V.01

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: cụm điều khiển và xử lý trung tâm.
- SchDoc: `TAM1_Xulytrungtam/PAGE1.SchDoc` (chính).
- SHA-256 SchDoc: `6e3f4500def50347d4dea00228cca264fc7fd8e66ab4900ad74b8df284ef27e3`.
- `sodocactam.pdf` trang 1: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM ĐIỀU KHIỂN VÀ XỬ LÝ TRUNG TÂM A313_V.01`.

## Thống kê trích xuất

- Ref BOM: 145; net: 551; chân: 1326; dòng đầu nối: 212.
- Net một chân đã khai báo ngoại lệ: 193; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 1: 145 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 11: 103 ref, 4 ref đầu nối (DC1B, DC2B, J1, J2).
- Kết quả lệch: BVTK: 103 ref so với SchDoc 145 ref.

## Điểm mơ hồ và giới hạn

- Không có xung đột phiên bản riêng ngoài các chênh lệch đếm nêu trên.
- Có 1 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v01.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
