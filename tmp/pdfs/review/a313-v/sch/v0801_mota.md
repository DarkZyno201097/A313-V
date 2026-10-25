# v0801 — V.08.01

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: tấm nguồn điện.
- SchDoc: `machnguon_A313V/NGUON_A313.SchDoc` (chính).
- SHA-256 SchDoc: `b376cda3406a5a19c61f5919a3ce5564efe67ca8a5ab41bba34ae01ef8ca04b8`.
- `sodocactam.pdf` trang 8: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM NGUỒN ĐIỆN A313_V.08.01`.

## Thống kê trích xuất

- Ref BOM: 51; net: 115; chân: 253; dòng đầu nối: 127.
- Net một chân đã khai báo ngoại lệ: 86; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 8: 51 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 39: 49 ref, 0 ref đầu nối (không kê).
- Kết quả lệch: BVTK: 49 ref so với SchDoc 51 ref; BVTK: 0 ref đầu nối so với SchDoc 2.

## Điểm mơ hồ và giới hạn

- BVTK BV.33 không kê hai đầu nối DC13A/DC14C; SchDoc có hai ref này nên tổng cao hơn 2.
- Có 0 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v0801.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
