# daucam31 — DAUCAM-31

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: đầu cắm 31 chân trên thân máy.
- SchDoc: `machdaucam31chan_A313V/DAUCAM.SchDoc` (chính).
- SHA-256 SchDoc: `a2d0506dcdd65de8fa0d30b6c5253fa4878dd6771c3b3fd3a05b95830054f5fb`.
- `sodocactam.pdf` trang 12: `SƠ ĐỒ ĐẦU CẮM 31, 96 CHÂN TRÊN THÂN MÁY A313-V`.

## Thống kê trích xuất

- Ref BOM: 2; net: 14; chân: 62; dòng đầu nối: 62.
- Net một chân đã khai báo ngoại lệ: 0; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 12: 2 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK: không có bảng BOM tách riêng cho bản đầu cắm trong nguồn được chỉ định.
- Kết quả lệch: không lệch về tổng ref/đầu nối trong phạm vi đếm.

## Điểm mơ hồ và giới hạn

- Không có bảng BOM tách riêng tương ứng trong BVTK được chỉ định; trang 12 sodocactam là bản gộp đầu cắm 31/96 chân.
- Có 0 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_daucam31.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
