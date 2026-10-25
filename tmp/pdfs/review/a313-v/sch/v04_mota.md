# v04 — V.04

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: cụm biến đổi.
- SchDoc: `TAM4_Cumbiendoi/A313_4.SchDoc` (chính).
- SHA-256 SchDoc: `4be0603851a1f8fe600beff99d0fb0082de578c393c1729e06b65ea4bfe9e203`.
- `sodocactam.pdf` trang 4: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM BIẾN ĐỔI A313_V.04`.

## Thống kê trích xuất

- Ref BOM: 244; net: 363; chân: 1163; dòng đầu nối: 192.
- Net một chân đã khai báo ngoại lệ: 176; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 4: 244 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 23: 242 ref, 2 ref đầu nối (DC7, DC8).
- Kết quả lệch: BVTK: 242 ref so với SchDoc 244 ref.

## Điểm mơ hồ và giới hạn

- Không có xung đột phiên bản riêng ngoài các chênh lệch đếm nêu trên.
- Có 4 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v04.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
