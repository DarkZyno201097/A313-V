# v0802 — V.08.02

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: tấm kiểm tra nguồn điện.
- SchDoc: `machkiemtranguon/mach_kiem_tra_nguon.SchDoc` (chính).
- SHA-256 SchDoc: `61ec89e299ecbd4fe90008863412748fe7224d2df73b52e777391c3e2b039ada`.
- `sodocactam.pdf` trang 9: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM KIỂM TRA NGUỒN ĐIỆN A313_V.08.02`.

## Thống kê trích xuất

- Ref BOM: 89; net: 125; chân: 317; dòng đầu nối: 31.
- Net một chân đã khai báo ngoại lệ: 58; dòng có dấu `?`: 0.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 9: 89 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 43: 89 ref, 1 ref đầu nối (J1).
- Kết quả lệch: không lệch về tổng ref/đầu nối trong phạm vi đếm.

## Điểm mơ hồ và giới hạn

- BVTK dùng ref đầu nối J1; SchDoc dùng DC14D. Số lượng cùng là 1 nhưng tên ref khác.
- Có 1 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v0802.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
