# Project Handoff

> Checkpoint phiên, không phải nguồn sự thật lâu dài. Luật dự án và hàng đợi
> việc ở `CLAUDE.md`; bản đồ thư mục và an toàn phần cứng ở `README.md`.

## 1. Current Task

Chuyển dự án A313-V lên GitHub private để làm việc trên cloud, rồi làm việc
4.1 của `CLAUDE.md` (sửa lỗi khoảng trắng Rev. C trong file PHAN-TICH).
Mục tiêu dài hơn trên cloud: phân tích **toàn khối** A313-V và đưa ra hướng
sửa chữa cho cả khối (`CLAUDE.md` §4.8).

## 2. Current Project State

- Repo: https://github.com/DarkZyno201097/A313-V — **PRIVATE**.
- Branch `main`, đồng bộ với `origin/main`. Lịch sử: `0085cd7` (commit đầu) →
  `ce764e9` (sửa 4.1) → commit cập nhật checkpoint này. Đã push và kiểm 2026-10-20.
- 110 file, 132,0 MB thô; file lớn nhất 6,6 MB (`1.BVTK .../BVTK-A313-V_HS dau A.pdf`).
- Commit identity (cấu hình local của repo): `Chanh Dinh
  <86103313+DarkZyno201097@users.noreply.github.com>` (email noreply vì tài
  khoản không công khai email; token gh không có scope `user:email`).

## 3. Completed Work

- Bổ sung `.gitignore`: loại `*.doc`, `*.docx`, `*.log`, `.claude/`.
- Xuất `TMKT&HDSD A313-V/TMKT&HDSD A313-V.pdf` từ `.docx` gốc bằng Word
  (`SaveAs2`, định dạng 17). `ExportAsFixedFormat` treo 2 lần qua COM nên không dùng.
- Cập nhật `CLAUDE.md` (§3.1 thêm 3 mục chỉ-đọc + quy ước chỉ PDF; §4.1, 4.3,
  4.4, 4.5 sửa theo thực tế; thêm §4.8) và `README.md` (bản đồ thư mục, trạng thái, lưu ý repo).
- Cài GitHub CLI 2.102.0 (winget, người dùng cho phép); người dùng tự `gh auth login`.
- `git init -b main`, `core.quotepath false`, commit `0085cd7`, `gh repo create A313-V --private --push`.
- Việc 4.1 (phần chữ): người dùng duyệt diff → đã ghi vào `PHAN-TICH_...md`
  50 chỗ sửa + 1 dòng chèn đầu §10.4; cập nhật trạng thái 4.1 trong
  `CLAUDE.md`, `README.md`. Commit `ce764e9`, đã push (người dùng xác nhận).

## 4. Important Decisions

- **Repo chỉ chứa PDF**: mọi `.doc/.docx` (115,7 MB) ở lại máy này. Sửa báo cáo
  Word chỉ làm được trên máy này.
- **Ảnh đo `KET-QUA-TEST_` commit nguyên bản** (63,9 MB): là ảnh chụp điện thoại
  màn hình máy đo, nén PNG palette sẽ loang màu; ảnh không bao giờ sửa nên chỉ tốn một lần.
- **Đưa Altium SchDoc + PcbDoc** (39,1 MB) của các tấm: nguồn sơ đồ chuẩn,
  vì `sodocactam.pdf` mất chữ Cyrillic.
- **CLAUDE.md có trong repo** để phiên cloud có luật cứng.
- Thứ tự: push trước, sửa 4.1 sau (theo prompt người dùng, khác thứ tự cũ của CLAUDE.md).

## 5. Files Changed

- `.gitignore` — thêm khối Word/log/.claude ở cuối.
- `CLAUDE.md`, `README.md` — như mục 3.
- `TMKT&HDSD A313-V/TMKT&HDSD A313-V.pdf` — file mới (2,65 MB, 57 trang).
- `PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md` — bản vá 4.1 (37+/35−).
- `PROJECT_HANDOFF.md` — file này.

## 6. Verification Already Completed (chạy trong phiên 2026-10-20)

- Kiểm kê staged bằng script: 0 file > 10 MB; 0 file trong `tmp/report_render/`,
  `__pycache__/`, `.claude/`, `History/`, `__Previews/`; 0 `.doc/.docx/.log/.pyc/~$*`.
- PDF TMKT: 57 trang = `ComputeStatistics` của Word; lớp text 87 440 ký tự
  (3 665 Cyrillic); `.docx` gốc giữ nguyên kích thước và ngày sửa.
- Sau push lần 1: `gh repo view` → `visibility: PRIVATE`; `git ls-remote` = HEAD local;
  cây remote 110 blob; collaborator chỉ chủ repo; truy cập ẩn danh HTTP 404.
- Sau push lần 2 (`ce764e9`): `ls-remote` = HEAD local, 111 blob, vẫn PRIVATE,
  ẩn danh 404, working tree sạch.
- BV.25 ghi đúng chuỗi `2,05ΩM, 1%` (pdfplumber: BVTK trang 31,
  `BVTK-A313-V.06.pdf` trang 4).
- Bản vá 4.1: mọi chuỗi cũ khớp đúng 1 lần/dòng (assert); quét lại chỉ còn
  ký hiệu cố ý (công thức, mũi tên giữa refdes, `pha+`, `Mux+ADC`). File sau
  khi ghi trùng byte với bản sao đã duyệt (`cmp`); 0 chuỗi `2,05 Ω M`/`3 Ш 3` còn lại.

## 7. Known-Good State

Commit `0085cd7` trên `origin/main` là bản sạch, private, đủ tài liệu PDF.

## 8. Unfinished Work

- 4.1 còn lại: rà §5.2 và §10.4 so với Rev. B — **không có bản Rev. B** trong thư mục.
- 4.2 dời `tmp/pdfs/review/` → `Phan-bien/`; B08 thiếu bảng số; 2 câu hỏi `~5V/400Hz`;
  tấm .05; phân tích toàn khối (§4.8).
- JARVIS: dự án chưa đăng ký nên chưa nạp tri thức.

## 9. Risks / Open Questions

- Mỗi lần commit lại PDF/PcbDoc cộng nguyên dung lượng vào history (không dùng LFS).
- Phiên cloud cần GitHub App của Claude được cấp quyền vào repo `A313-V`.

## 10. Exact Next Step

Mở phiên cloud trên repo `A313-V` cho `CLAUDE.md` §4.8 (phân tích toàn khối,
hướng sửa chữa), bắt đầu từ `A313 original/A-313-2.pdf` (tìm hỏng hóc) và
SchDoc các tấm; hoặc làm 4.2 (dời `tmp/pdfs/review/` → `Phan-bien/`).
