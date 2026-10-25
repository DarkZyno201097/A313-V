# v07 — V.07

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: cụm chuyển lệnh đơn ra.
- SchDoc: `machbiendoilenhdon/machbiendoilenhdon.SchDoc` (bản có J1/J2 và 11 đầu CON1).
- SHA-256 SchDoc: `bf39d77e99782c29b55a9102043ea6403b2194fd970568ac0acc6e7710ffe131`.
- `sodocactam.pdf` trang 7: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM CHUYỂN LỆNH ĐƠN RA A313_V.07`.

## Thống kê trích xuất

- Ref BOM: 121; net: 158; chân: 454; dòng đầu nối: 91.
- Net một chân đã khai báo ngoại lệ: 37; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 7: 109 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 35: 110 ref, 2 ref đầu nối (J1, J2).
- Kết quả lệch: sodocactam: 109 ref so với SchDoc 121 ref; BVTK: 110 ref so với SchDoc 121 ref; BVTK: 2 ref đầu nối so với SchDoc 13.

## Điểm mơ hồ và giới hạn

- Trang 7 sodocactam khớp bố cục bản Sheet1 (DC13C/DC13D), không khớp hoàn toàn bản này; giữ hai bộ output, không tự chọn bản chuẩn.
- Có 0 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v07.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
