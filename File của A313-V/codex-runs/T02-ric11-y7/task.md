# Nhiệm vụ T02 — Chép sơ đồ Э3 рис.11 (Y7, Плата согласования) của A-313-3

Bạn là Executor; Claude (Orchestrator) sẽ kiểm lại từng dòng. Đọc `AGENTS.md` (luật §3, §4.9) trước.
Tiếng Việt, dấu thập phân là dấu phẩy. Bạn được sửa file trong worktree này.

## Nguồn
- Ảnh sơ đồ: #180 (trang tay 184), ПЭ: #179 (trang 185), bản lắp ráp рис.27: #242 (trang 241).
  Tra tên file ảnh: `tmp/pdfs/review/a313-3/kiemke/trang.csv` (cột idx = số ảnh), ảnh nằm trong `ЕУ.048.002.РЭ_A313-3/`.
  Phóng to từng vùng ảnh khi đọc (crop bằng Python/PIL ra thư mục tạm ngoài repo nếu cần).
- Mẫu định dạng và văn phong: `tmp/pdfs/review/a313-3/e3/ric21_bom.csv`, `ric21_net.csv`, `ric21_mota.md`.
- Bảng chân đầu nối đã chép (Э4): `tmp/pdfs/review/a313-3/e4/p152.csv`, bảng `У7П1`, `У7П2`.
- Báo cáo T01: `codex-runs/T01-y1y7-audit/r1/last.md`.

## Việc phải làm
1. Tạo `tmp/pdfs/review/a313-3/e3/ric11_bom.csv` (ref,name,qty,page,note) từ ПЭ #179 — mọi dòng ПЭ.
2. Tạo `ric11_net.csv` (ref,pin,net,note): mọi chân linh kiện thấy trên #180. Net nội bộ đặt `N1, N2…`;
   net ra đầu nối ghi `П1:<chân> <tên tín hiệu>` / `П2:...` đúng như in trên sơ đồ.
3. Thêm `11` vào tuple hình trong `e3_check.py` (dòng `for nn in (19, …)`) và chạy nó; phải pass cho рис.11
   hoặc ngoại lệ được liệt kê rõ như các ngoại lệ đã có.
4. Viết `tmp/pdfs/review/a313-3/e3/e3_vs_e4.py`: so chân П1/П2 trong `ric11_net.csv` với `У7П1/У7П2` trong
   p152.csv (tên tín hiệu, sau chuẩn hoá chữ Latin↔Cyrillic giống `e4_check.py`). In số khớp/lệch, ghi
   `e3/ric11_vs_e4.csv`. Có self-check bằng assert.
5. Viết `ric11_mota.md` theo mẫu ric21_mota.md: nguồn, cấu trúc, bảng linh kiện chính, các chỗ chưa chắc.

## Ràng buộc bắt buộc
- KHÔNG đoán. Chỗ không đọc được: ghi `?` trong cột note kèm số ảnh và vùng (ví dụ "#180 góc phải dưới, mép bị cắt").
  Linh kiện có trong ПЭ mà không thấy trên ảnh: liệt kê ở mục "chưa chắc", không bịa chân.
- Chỉ sửa/tạo các file nêu trên. Không sửa ảnh, không sửa tài liệu gốc, không sửa file CSV Э4.
- Không commit (Claude sẽ commit sau khi kiểm).

## Tiêu chí đạt
- `python tmp/pdfs/review/a313-3/e3/e3_check.py` exit 0 (рис.11 không lỗi ngoài ngoại lệ đã ghi).
- `python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py` exit 0, có số khớp/lệch.
- Mọi lệch e3↔e4 đều được giải thích trong mota (đọc sai phía nào, hay mâu thuẫn bản vẽ — giữ cả hai).

## Câu trả lời cuối (bắt buộc)
### 1. Tóm tắt  ### 2. File tạo/sửa  ### 3. Kết quả chạy 2 script (dán output)
### 4. Chỗ chưa chắc / "?" (bảng: ref, chân, ảnh, vùng, lý do)  ### 5. Lệch e3↔e4 và giải thích
### 6. Phần chưa làm và lý do
