# Nhiệm vụ T03 — Chép Э3 рис.8 (Y5, Устройство командного управления)

T02 (рис.11) đã được Claude kiểm và commit `bf781fe`. Làm tương tự cho рис.8, cùng định dạng, cùng ràng buộc.

## Nguồn
- Sơ đồ: ảnh #167 (trang 171), #168 (trang 172). ПЭ: #169 (trang 173), #170 (trang 174).
- Э4 của tấm: `tmp/pdfs/review/a313-3/e4/p151.csv`, bảng `У5П1`, `У5П2`, `У5П3`.
- T01 đã ghi: #167/#168 không thấy khung tên, vùng trái sát mép, #168 chữ nhỏ kém rõ và có nếp gấp ngang.

## Việc phải làm
1. `e3/ric08_bom.csv`, `e3/ric08_net.csv`, `e3/ric08_mota.md` (định dạng như ric11).
   Vi mạch: ghi chân theo số chân in trên sơ đồ; net nối hai tờ (#167↔#168) ghi rõ cách nhận biết (số đường/nhãn).
2. Tổng quát hoá `e3/e3_vs_e4.py` để nhận tham số: `python e3_vs_e4.py 8 У5` (giữ `11 У7` chạy được, kết quả
   рис.11 không đổi: 105 khớp / 1 chỉ có ở Э4). Ghi `e3/ric08_vs_e4.csv`.
3. Thêm `8` vào tuple của `e3_check.py`. Nếu có linh kiện trong ПЭ không thấy trên ảnh, thêm vào danh sách ngoại lệ
   đã biết (như ric19/ric25) kèm lý do và số ảnh.

## Ràng buộc (nhắc lại, bắt buộc)
- KHÔNG đoán. Ảnh này có vùng mờ/mép/nếp gấp: chỗ không đọc chắc ghi `?` trong note kèm ảnh + vùng; không bịa chân, không
  suy chân từ Э4 hay từ datasheet. Tên tín hiệu đầu nối phải đọc từ chính sơ đồ Э3, không chép từ Э4.
- Chỉ sửa các file nêu trên. Không commit.

## Tiêu chí đạt
- `e3_check.py` exit 0; `e3_vs_e4.py 8 У5` và `e3_vs_e4.py 11 У7` exit 0.
- Mọi lệch e3↔e4 được giải thích. Số ô `?` báo cáo trung thực.

## Câu trả lời cuối: cùng 6 mục như T02.
