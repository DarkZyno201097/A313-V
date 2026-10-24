# Nhiệm vụ T03b — Hoàn tất рис.8 (Y5): soát `?`, chân chỉ-Э4, lệch tên, báo cáo cuối

Lượt T03 trước của bạn bị cắt do hết giờ (3600 s) trước khi có câu trả lời cuối. Claude đã commit checkpoint
`10c0ba1` gồm `ric08_bom.csv`, `ric08_net.csv`, `ric08_mota.md`, `ric08_vs_e4.csv` và `e3_vs_e4.py` tổng quát.
Tiếp tục từ trạng thái đó (file hiện có trong worktree), cùng ràng buộc như T02/T03.

## Việc phải làm
1. Soát 187 dòng `ric08_net.csv` có `?` trên ảnh #167/#168 (phóng to vùng). Đọc chắc thì bỏ `?` và ghi căn cứ
   (ảnh + vùng); vẫn không chắc thì giữ `?` và ghi rõ lý do (mờ / nếp gấp / mép cắt / chữ viết tay).
2. 42 chân "chỉ có ở Э4" trong `ric08_vs_e4.csv`: với từng chân, tìm trên Э3 (#167/#168) xem có đường tới linh kiện
   không. Có và đọc chắc → thêm hàng netlist từ chính Э3. Không thấy → giữ ONLY_E4, ghi lý do vào mota §3.
3. Hai lệch tên П1/10 («ВХОД РГР ТТЛ» ↔ «ВХОД ПРП ТТЛ») và П3/42 («Nоб БК» ↔ «NАБбк»): xem lại chữ trên Э3,
   ghi kết luận đọc được; nếu ảnh không quyết định được thì giữ cả hai cách đọc.
4. Cập nhật `ric08_mota.md` (§3, §4) theo kết quả; chạy lại 3 lệnh kiểm.

## Ràng buộc
- KHÔNG đoán, KHÔNG lấy tên/chân từ Э4 hay datasheet để lấp Э3. Chỉ sửa các file `ric08_*`. Không commit.
- Thời gian có hạn: ưu tiên mục 3 → 2 → 1; nếu không xong hết, dừng và báo cáo phần đã làm.

## Tiêu chí đạt
- `python tmp/pdfs/review/a313-3/e3/e3_check.py` exit 0
- `python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 8 У5` và `... 11 У7` exit 0 (рис.11 không đổi: 105/0/0/1)
- Báo cáo trung thực số `?` trước/sau, số ONLY_E4 trước/sau.

## Câu trả lời cuối (bắt buộc, 6 mục như T02)
### 1. Tóm tắt ### 2. File sửa ### 3. Output 3 lệnh kiểm ### 4. `?` còn lại (bảng) ### 5. Lệch/ONLY_E4 còn lại + giải thích ### 6. Chưa làm
