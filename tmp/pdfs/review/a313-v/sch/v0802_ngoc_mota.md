# v0802_ngoc — V.08.02

## Chức năng và nguồn

- Chức năng theo tên bản vẽ: tấm kiểm tra nguồn điện.
- SchDoc: `machkiemtranguon/ngoc.SchDoc` (bản ngoc chưa đánh số ref).
- SHA-256 SchDoc: `0736119d8e81b1cb958e1f3b3845a97832b4f2a0f1f2ab3609bff0aaf51667af`.
- `sodocactam.pdf` trang 9: `SƠ ĐỒ NGUYÊN LÝ MẠCH ĐIỆN CỤM KIỂM TRA NGUỒN ĐIỆN A313_V.08.02`.

## Thống kê trích xuất

- Ref BOM: 89; net: 129; chân: 304; dòng đầu nối: 18.
- Net một chân đã khai báo ngoại lệ: 61; dòng có dấu `?`: 411.
- Bản ghi bus/harness không hỗ trợ: 0 (không có).

## Kiểm chéo bắt buộc

- sodocactam trang 9: 89 ref. Lưu ý: ref trong PDF bị raster hóa; số này dựa trên trường designator SchDoc của đúng bố cục trang đã kiểm bằng render, nên không phải nguồn netlist độc lập.
- BVTK `File của A313-V\1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` trang 43: 89 ref, 1 ref đầu nối (J1).
- Kết quả lệch: không lệch về tổng ref/đầu nối trong phạm vi đếm.

## Điểm mơ hồ và giới hạn

- SchDoc có 89 instance nhưng chỉ 6 ref literal vì phần lớn là R?/D?/U?/T?/C?; hậu tố @record chỉ để phân biệt dòng, không phải ref gốc.
- Có 0 net mang nhiều nhãn; từng dòng được đánh `?` và giữ nguyên các alias, không ép tên cho khớp.
- Nhãn kiểu font giả Cyrillic được đổi có kiểm soát (ví dụ `vih.1a=` → `ВЫХ.1А=`); nhãn gốc luôn nằm trong cột `note` khi có đổi.
- Net không nhãn dùng Nxxxx. Net một chân chỉ PASS khi `note` khai báo `allowed_singleton`; đây là ngoại lệ cấu trúc, không chứng minh chân đó chủ ý NC.
- Netlist là khôi phục hình học một sheet: dây chỉ nối tại đầu mút/T-junction hoặc junction; nhãn/power port chỉ gộp theo tên không phân biệt hoa-thường. Không có netlist Altium xuất độc lập để chứng nhận topology.

## Tái kiểm

- Chạy `C:/Python314/python.exe check_v0802_ngoc.py`.
- Kết quả checker hiện tại: **PASS**.
- PASS chỉ xác nhận quan hệ BOM–pin–net và ngoại lệ singleton đã khai báo; không xác nhận phần cứng hay BVTK.
