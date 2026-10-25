# v02 — V.02

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: cụm chuyển mạch tín hiệu vào.
- SchDoc: `TAM2_chuyenmachtinhieuvao/A313-2.SchDoc` (chính).
- SHA-256 SchDoc: `c6c06ceccf075b2231b36a7513030184a11bd54fc2b3ae07e26f80ae8840ee6d`.
- `sodocactam.pdf` trang 2: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM CHUYỂN MẠCH TÍN HIỆU VÀO A313_V.02`.

## Thống kê trích xuất

- Ref BOM: 267; net: 320; chân: 1099; dòng đầu nối: 192.
- Net một chân đã khai báo ngoại lệ: 56; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 2: 267 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 15: 254 ref, 2 ref đầu nối (DC3, DC4).
- Kết quả lệch: BVTK: 254 ref so với SchDoc 267 ref.

## Điểm mơ hồ và giới hạn

- Không có xung đột phiên bản riêng ngoài các chênh lệch đếm nêu trên.
- Có 2 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v02.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
