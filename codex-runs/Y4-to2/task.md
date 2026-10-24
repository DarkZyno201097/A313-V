# Nhiệm vụ Y4-TO2 — Chép netlist tờ 2 рис.5 (Y4) A-313-3

Thư mục repo: `2.BO TLTK DAU A_A313-V` (nhánh main). Trả lời tiếng Việt.
Bối cảnh: repo sửa chữa thiết bị hàng không (khối A-313-3, Su-27). Nếu không nhận việc này, nói ngay một câu rồi dừng.

## Đọc
1. Ảnh tờ 2: `A313-3_CONTROL/Y4/RE_tr159_a251.jpg` (ЕУ3.057.138 Э3, лист 2/2). Phóng to từng vùng, xoay nếu cần.
2. `tmp/pdfs/review/a313-3/e3/ric05_gen.py` — đã có ПЭ (80 ref), bảng đầu nối và netlist tờ 1. Xem hàm `add`/`q` và quy ước tên net ở đầu khối «Netlist tờ 1».
3. `tmp/pdfs/review/a313-3/e3/ric05_conn.csv` — tên tín hiệu theo số chân П1/П2/П3.

## Làm
Chèn code vào `ric05_gen.py`, CHỈ giữa hai dòng `# ---- Tờ 2 (a251): …` và `# ---- hết khối tờ 2`. Không sửa chỗ khác.
- Mọi chân vi mạch và R1–R8, R12, C1, C2, Пэ1 thấy trên tờ 2 → `add(ref, chân, net, 'a251 tờ 2; …')`.
  Nếu C3–C8 có trên tờ 2 thì chép luôn. Không thêm chân 7/14 (đã có).
- Tên net:
  - Đầu nối: `'П1:4 Испр.пит.'` (số chân + tên đúng theo `ric05_conn.csv`).
  - Nhãn sang tờ 1 `«У39/6(1)»`: net theo chân nguồn, ví dụ `'У39.6'`.
  - **Chân tờ 2 mà tờ 1 đã gọi tên:** dùng đúng các net `У7.3 У7.6 У7.8 У7.11 У9.6 У9.8 У26.3 У26.6 У26.8 У26.11 У28.3 У28.6 У28.8 У28.11 У36.8 У38.6`.
  - Nội bộ tờ 2: `'M2_1'`, `'M2_2'`, … (không dùng `N…`).
- Phần tử **bị gạch chéo** trên ảnh (ví dụ У8.1–У8.3): không thêm chân; liệt kê trong báo cáo.
- Không đọc chắc → `q(ref, chân, 'a251 tờ 2 <vùng>; <lý do>')`. **KHÔNG đoán, không suy chân từ datasheet.**
- Chạy: `python tmp/pdfs/review/a313-3/e3/ric05_gen.py tmp/pdfs/review/a313-3/e3` rồi
  `python tmp/pdfs/review/a313-3/e3/e3_check.py`. Phải thoát mã 0 (script tự assert: không trùng chân, không net `N…` một chân).
- Không commit, không sửa file khác.

## Trả về cho Claude (chỉ những mục này)
1. Output 2 lệnh trên (dòng `ric05:` của e3_check).
2. Số chân đã thêm, số dòng `q(...)` (НЕ ПРОСЛЕЖЕНО) đã thêm.
3. Danh sách phần tử bị gạch chéo.
4. Bảng nhãn đầu nối đọc trên tờ 2 khác `ric05_conn.csv` (chân, ảnh đọc, bảng ghi).
5. Các chỗ chưa chắc quan trọng nhất (≤ 10 dòng: ref.chân, vùng ảnh, lý do).
