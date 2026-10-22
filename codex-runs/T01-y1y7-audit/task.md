# Nhiệm vụ T01 — Đánh giá độ đầy đủ dữ liệu sơ đồ phần số Y1–Y7 (CHỈ ĐỌC)

Bạn là Executor. Claude là Orchestrator và sẽ kiểm tra lại từng trích dẫn của bạn.
Làm việc trong repo hiện tại (worktree riêng của bạn). Đọc `AGENTS.md` trước (luật cứng §3, §4.9).
Trả lời bằng tiếng Việt, dấu thập phân là dấu phẩy.

## Bối cảnh
Theo `PROJECT_HANDOFF.md` §11 và `AGENTS.md` §4.9: dự án đang khôi phục khối Nga A-313-3
(dự phòng cho A313-V). "Phần số" Y1–Y7 là các tấm số của A-313-3, sơ đồ ở рис.5–11 của
tập ЕУ3.048.002 РЭ. Đã chép xong phần nguồn (рис.19–26) và bảng đầu nối Э4/Y16; Y1–Y7 chưa chép.

Nguồn cần rà (không giới hạn ở đây):
- `DANH-MUC_ANH_RE_A-313-3.md` — danh mục trang ↔ ảnh ↔ рис. của 249 ảnh bản giấy.
- `ЕУ.048.002.РЭ_A313-3/` — ảnh chụp bản giấy (chỉ mở vài ảnh để kiểm chứng, không duyệt hết).
- `A313 original/A-313-3.HDSDKT.pdf` — bản dịch, mất hình nhưng còn tên hình và перечень.
- `KE-HOACH_KIEM-TRA_A-313-3.md`, `SO-DO-NGUON_A-313-3.md`, `SO-DO-DAU-NOI_E4_A-313-3.md`.
- `tmp/pdfs/review/a313-3/` (script, CSV Э3/Э4 đã chép — dùng làm mẫu định dạng).

## Việc phải làm
1. Với từng tấm Y1…Y7: những dữ liệu nào ĐÃ CÓ trong repo (рис. số mấy, trang РЭ, ảnh số mấy,
   перечень/спецификация có hay không, chân đầu nối trong Э4 có hay không).
2. Những gì THIẾU hoặc chưa dùng được (trang không có ảnh, ảnh mờ/cắt góc, tờ gấp chụp chưa trọn,
   chỉ có tên hình mà không có hình...).
3. Điểm cần xác minh trên bản giấy hoặc trên khối thật.
4. Đề xuất thứ tự chép Y1–Y7 (tấm nào trước, vì sao), dựa trên mức đầy đủ dữ liệu.

## Ràng buộc bắt buộc
- KHÔNG sửa, tạo hay xoá file nào (sandbox chỉ đọc). Báo cáo nằm trong câu trả lời cuối.
- Mọi khẳng định phải kèm căn cứ: đường dẫn file + số trang/số ảnh/số dòng.
- KHÔNG suy đoán nội dung sơ đồ bị thiếu. Không chắc thì ghi "chưa xác minh" và nói cần gì để xác minh.
- Nếu tài liệu mâu thuẫn nhau, liệt kê cả hai phía, không tự chọn.

## Định dạng câu trả lời cuối (bắt buộc, đúng các mục này)
### 1. Tóm tắt (≤ 5 dòng)
### 2. Bảng Y1–Y7
| Tấm | рис. | Trang РЭ | Ảnh | Перечень | Э4 | Mức đầy đủ (Đủ/Thiếu một phần/Thiếu) | Căn cứ |
### 3. Thiếu / chưa dùng được (mỗi dòng có căn cứ)
### 4. Cần xác minh
### 5. Thứ tự đề xuất và lý do
### 6. Lệnh/đã đọc những gì (danh sách file và lệnh đã chạy)
### 7. Phần chưa làm được và lý do
