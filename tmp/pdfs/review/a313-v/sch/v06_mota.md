# v06 — V.06

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: cụm khuếch đại tín hiệu ra.
- SchDoc: `Tam6_khuyechdaitinhieura/A313_6.SchDoc` (chính).
- SHA-256 SchDoc: `d021a73e8301107783d0afc5e89c346456b8ec58fa36697c175224fe8b7a03cc`.
- `sodocactam.pdf` trang 6: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM KHUẾCH ĐẠI TÍN HIỆU RA A313_V.06`.

## Thống kê trích xuất

- Ref BOM: 234; net: 409; chân: 1027; dòng đầu nối: 192.
- Net một chân đã khai báo ngoại lệ: 214; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 6: 234 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\BVTK-A313-V.06.pdf` trang 4: 233 ref, 2 ref đầu nối (DC11, DC12).
- Kết quả lệch: BVTK: 233 ref so với SchDoc 234 ref.

## Điểm mơ hồ và giới hạn

- Không có xung đột phiên bản riêng ngoài các chênh lệch đếm nêu trên.
- Có 1 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v06.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
