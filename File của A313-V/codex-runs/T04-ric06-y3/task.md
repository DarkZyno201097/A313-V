# Nhiệm vụ T04 — Chép Э3 рис.6 (Y3, Устройство управления обращением, ЕУ3.057.136 Э3, 3 tờ)

Cùng định dạng, cùng ràng buộc như T02/T03 (рис.11 đã PASS; рис.8 tạm dừng chờ ảnh chụp lại — KHÔNG sửa file `ric08_*`).

## Nguồn
- Sơ đồ: ảnh #155–#158 (trang tay 158–161). Tờ 1 có bản chụp lại #231 (`.heic`) và #232 (`.jpg`, chụp lại #231) —
  dùng #232 nếu nét hơn #155. Tra file theo `tmp/pdfs/review/a313-3/kiemke/trang.csv`.
- ПЭ: #159 (trang 162), #160 (trang 163).
- Э4: `tmp/pdfs/review/a313-3/e4/p151.csv`, bảng `У3П1`, `У3П2`, `У3П3`.
- T01 ghi: #156–#158 là tờ gấp chụp thiếu mép/khung tên; chưa có căn cứ #231/#232 bù được tờ khác.

## Việc phải làm
1. Xác định trước: mỗi ảnh là tờ mấy của рис.6 (đọc số tờ/khung tên nếu thấy; không thấy thì ghi "chưa xác định").
2. Tạo `e3/ric06_bom.csv`, `e3/ric06_net.csv`, `e3/ric06_mota.md`. Net nối giữa các tờ: ghi rõ cách nhận biết.
3. Thêm `6` vào tuple `e3_check.py` (ngoại lệ nếu có, kèm lý do + ảnh). Chạy `e3_vs_e4.py 6 У3` → `ric06_vs_e4.csv`.

## Ràng buộc
- KHÔNG đoán; vùng mờ/mép cắt/nếp gấp → `?` kèm ảnh + vùng. Tên tín hiệu đầu nối đọc từ Э3, không chép từ Э4/datasheet.
- Thời gian có hạn (7200 s): làm theo thứ tự tờ 1 → 2 → 3; hết giờ thì dừng gọn, file phải hợp lệ cho checker.
- Chỉ tạo/sửa `ric06_*` và tuple trong `e3_check.py`. Không commit.

## Tiêu chí đạt
- `e3_check.py` exit 0; `e3_vs_e4.py 6 У3`, `e3_vs_e4.py 11 У7` (giữ 105/0/0/1), `e3_vs_e4.py 8 У5` (giữ 121/3/0/36) exit 0.
- Báo cáo số `?`, số khớp/lệch/ONLY_E4 trung thực.

## Câu trả lời cuối: 6 mục như T02 (thêm bảng ảnh ↔ tờ ở mục 1).
