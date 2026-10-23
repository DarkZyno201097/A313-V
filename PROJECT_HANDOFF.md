# Project Handoff

> Checkpoint hiện tại: §13 R01, ngày 2026-10-23; các mục trước là lịch sử.

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

## 11. Trạng thái A-313-3 (cập nhật 2026-10-22)

**Đã xong** (nhánh `claude/beautiful-lovelace-oamywv`):
* Danh mục 249 ảnh bản giấy ЕУ3.048.002 РЭ: `DANH-MUC_ANH_RE_A-313-3.md` (trang ↔ ảnh ↔ рис.).
* Э4/Y16 tr.142–157 chép ra CSV + kiểm chéo hai chiều + ma trận П1…П15: `SO-DO-DAU-NOI_E4_A-313-3.md`.
* So sánh 3Ш3/3Ш3В/3Ш4/3Ш4В với TMKT A313-V: 252/268 chân trùng, cắm lẫn được về sơ đồ chân máy bay.
* Э3 + перечень phần nguồn рис.20–26 và У24 рис.19: `SO-DO-NGUON_A-313-3.md`. Nguồn ~5 В 400 Гц khối Nga =
  Тр1 ТН-12-40-400 trên У17.

**Đang dở:**
* Sơ đồ phần số Y1–Y7 (рис.5–11) và tương tự Y8–Y15 (рис.12–18) — chưa chép.
* ~240 ô «?» trong bảng Э4 (`tmp/pdfs/review/a313-3/e4/p*.csv`, cột note) chưa soát từng ô.
* Trang ảnh còn thiếu: 211, 220, 238, 240 (перечень nguồn/У24); góc trên-trái ảnh #233; các trang
  ở `DANH-MUC_ANH_RE_A-313-3.md` §4; tờ gấp chụp chưa trọn.

**Mâu thuẫn còn nghi vấn** (chi tiết: `SO-DO-NGUON_A-313-3.md` §3 N1–N10, `SO-DO-DAU-NOI_E4_A-313-3.md` §3, §5):
* У24 chân 2/4: Э4 «ВКЛ./ОТКЛ.» ↔ Э3 «КОНТР. −5В / ИСПОЛН. УСТР-ВО».
* У21: bản vẽ −20 В (ЕУ3.215.451) ↔ khối lắp −02 (−23 В).
* У14/У15 nhãn РК I / РК II ghi lẫn giữa tr.142 và tr.149.
* У18 R11 «680 кОм» (nghi 680 Ω); У23 nhánh +3,5 В chỉ ra ≈ 2,5 V; У17 T9/T10 B/E chung net E(T8).
* Ma trận: cột «Выход 2б» ghi П3/23 (nghi П3/29); КП7/41,6 ↔ КП12/38,12 khác tên.

**Việc kế tiếp:** người dùng chụp bổ sung các trang thiếu + đo nguội N1–N10 trên khối; sau đó chép Э3 phần số
Y1–Y7 theo cùng cách (agent chép → script kiểm bom↔net).

**Script** (chạy từ gốc repo, theo thứ tự):
```
python tmp/pdfs/review/a313-3/e4_sua.py     # áp các chỗ sửa đã kiểm trên ảnh vào e4/p*.csv (idempotent)
python tmp/pdfs/review/a313-3/e4_check.py   # kiểm chéo hai chiều Э4 → e4/e4_all.csv, e4_mismatch.csv
python tmp/pdfs/review/a313-3/e4_tmkt.py    # so 3Ш3/3Ш4 với TMKT A313-V → e4/e4_vs_tmkt.csv
python tmp/pdfs/review/a313-3/e3/e3_check.py  # kiểm bom↔net 8 hình рис.19–26 + trị số danh định
```

## 12. Điều phối Claude ↔ Codex (cập nhật 2026-10-22, phiên Local)

**Khôi phục từ Cloud:** commit cloud `e6e4cd0` (nhánh `claude/beautiful-lovelace-oamywv`) đã nằm trong
`main` (`86074a7` = merge PR #1 + AGENTS.md). Không có thay đổi cloud nào bị thiếu trên Local.
4 script §11 chạy lại trên `main`: exit 0, không đổi file nào.

**Cơ chế:** Claude = Orchestrator, Codex CLI = Executor. Cách chạy, giới hạn an toàn: `tools/CODEX_ORCHESTRATION.md`;
script `tools/codex_run.sh`. Ban đầu Codex làm trong worktree `../A313-V_codex` (nhánh `codex/y1-y7-audit`); 2026-10-22 đã fast-forward vào `main` (`16ed722`) và gỡ worktree — nay mọi việc làm trong một thư mục repo, nhánh `main`.
Đã thử thật: `codex exec` (đăng nhập ChatGPT) và `codex exec resume <thread_id>` đều chạy.

**T01 — độ đầy đủ dữ liệu Y1–Y7 (A-313-3, рис.5–11): ĐẠT.** Báo cáo `codex-runs/T01-y1y7-audit/r1/last.md`,
thread `01a1629e-ac78-75c1-94b2-ab9e8a54688c`. Claude kiểm lại: 6 trích dẫn (trang.csv, p150.csv, ảnh #75/#167/
#168/#175/#180, KE-HOACH) khớp; độ phủ chân Э4 У1–У7 П1/П2 1–53, П3 1–70 không trùng — chạy lại độc lập, khớp.
Kết luận chính: Y4 thiếu Э3 (рис.5); Y6 thiếu tr.167; Y1 thiếu tr.180, #75 chưa định danh; các tấm còn lại
"thiếu một phần" do tờ gấp chụp mất mép/khung tên. Thứ tự chép đề xuất: Y7 → Y5 → Y3 → Y2 → Y1 → Y6 → Y4.
Mâu thuẫn ghi nhận: KE-HOACH ghi Y1/Y7 "thiếu danh mục" (theo bản dịch) ↔ ảnh bản giấy có ПЭ tr.181–183, 185.

**Việc kế tiếp:** người dùng chụp bổ sung рис.5 (Y4), tr.167, tr.180, khung tên các tờ gấp; giao T02 = chép Э3 Y7
(рис.11) ra `ric11_bom.csv`/`ric11_net.csv` theo mẫu `e3/`, kiểm bằng `e3_check.py`.

### 12.1. Nhiệm vụ Codex sau T01 (cập nhật 2026-10-22)

| Task | Kết quả | Commit | Codex thread |
|---|---|---|---|
| T02 рис.11 (Y7) | PASS — 166 ref, 462 chân; Э3↔Э4 khớp 105/105 (+ П2/1 КОРПУС chỉ có ở Э4); Claude kiểm ảnh #180 (ô mẫu + 3 bus) | `bf781fe` | `01a162ad-7126-7493-bd95-2d25663c3b92` |
| T03 рис.8 (Y5) | PARTIAL — hết giờ 3600 s trước khi có báo cáo cuối. Đã có `ric08_bom/net/mota/vs_e4`: 86 ref, 947 chân, 187 dòng `?`; Э3↔Э4 khớp 116, lệch tên 2 (П1/10, П3/42), chỉ-Э4 42. `e3_vs_e4.py` tổng quát hoá (tham số `NN БАНГ`), tái tạo đúng рис.11. Claude CHƯA kiểm ảnh #167/#168 | checkpoint WIP | cùng thread T02 |
| T03b рис.8 (Y5) | PARTIAL — `?` 187→169, ONLY_E4 42→36, khớp 121, lệch tên 3 (П1/10, П3/42, П2/2). Sửa gán lệch một bậc R4↔П1/10 của T03 (Claude kiểm ảnh #168: R11→П1/10, R4→П1/11, R5/R6→П1/12–13, R7–R10→П3/50–53, chân 1 chung rail б). Còn: soát 169 `?` (chủ yếu У8–У25 ở #168) + 36 ONLY_E4 | xem log | `01a162ad-…` (resume được) |

| T04 рис.6 (Y3) | Codex: lượt 1 bị chặn (đề bài thiếu quyền sửa `E4_FILES`), lượt 2 **từ chối** vì lý do chính sách (thiết bị quân sự). **Claude tự chép** — PARTIAL: BOM 99, bảng đầu nối tờ 1 176 hàng, net 818 chân (166 НЕ ПРОСЛЕЖЕНО, 213 dòng `?`); Э3↔Э4 У3: 125 khớp / 32 lệch tên (chủ yếu cách ghi) / 1 chỉ-Э3 / 9 chỉ-Э4. Phát hiện: У37, У53 bị gạch trên Э3 = vắng trong ПЭ; #155/#156 nghi KHÔNG thuộc рис.6 (có R5–R8, C7, C8); nhãn «У15/У16» tờ 1 và «У5-4» tờ 3 trùng ký hiệu. Chi tiết `e3/ric06_mota.md` | xem log | — |
**Quy trình:** sau mỗi task dừng chờ người dùng duyệt (`tools/CODEX_ORCHESTRATION.md` §5).
**Đề xuất kế tiếp (cũ, đã làm T03b):** T03b = resume thread, yêu cầu Codex xuất báo cáo cuối + soát 187 ô `?`, 42 chân chỉ-Э4, 2 lệch tên
(`CODEX_TIMEOUT=7200`); sau đó Claude kiểm ảnh. Rồi T04 Y3 (рис.6, 3 tờ, dùng #231/#232 cho tờ 1).

**Đề xuất kế tiếp (sau T03b):** T03c = resume `01a162ad`, chỉ soát У8–У25 trên #168 (169 `?`) và 36 ONLY_E4, CODEX_TIMEOUT=7200; hoặc chuyển T04 Y3 (рис.6) và để phần còn lại của рис.8 chờ ảnh chụp lại #168 rõ hơn.

**Codex không làm việc chép/khôi phục sơ đồ A-313-3 nữa** (từ chối T04 lượt 2, lý do chính sách). Chỉ giao Codex việc kiểm kê tài liệu / kiểm định dạng CSV; việc chép sơ đồ do Claude làm hoặc người dùng tự làm.
**Đề xuất kế tiếp (sau T04):** người dùng chụp lại tờ 2/3 рис.6 và #168 рис.8 rõ hơn, xác định #155/#156 thuộc hình nào; sau đó Claude chép Y2 (рис.9) hoặc soát tiếp các thanh dọc рис.6.

## 13. R01 — đổi tên ảnh bản giấy (2026-10-23)

### 1. Current Task

Đổi tên một lần 249 ảnh trong `ЕУ.048.002.РЭ_A313-3/`, giữ nguyên byte ảnh,
chỉ số #NNN và mọi tham chiếu đang dùng. Người dùng cho phép ngoại lệ đổi tên;
commit một lần có tiền tố `R01:`, không push.

### 2. Current Project State

Checkout hiện tại là thư mục gốc A313-V này. Theo xác nhận của người dùng,
đã chuyển từ `codex/a313-v-intake-20261022` sang `main`, baseline
`1450f2d7ce4bd03e3ac1e735cbdc063df3c0ccea`, giữ thay đổi đang dở.
Checkpoint này đi cùng commit R01; tra commit bằng `git log -1 --grep="^R01:"`.

### 3. Completed Work

Đổi tên 249 ảnh (239 JPG, 10 HEIC) bằng `git mv`; 249 hash SHA-256 khớp trước/sau.
`_DOI-TEN.csv` giữ tên cũ, tên mới, trang và hash. Thay tên trong 12 file tham chiếu.
Danh mục có quy tắc tên, hậu tố ảnh bổ sung và tên dự kiến từng trang thiếu.
AGENTS/CLAUDE ghi ngoại lệ đổi tên ngày 2026-10-23; ảnh tiếp tục chỉ-đọc.

### 4. Important Decisions

`page` trống giữ `trXXX` (19 ảnh); `kind=X` thêm `_x` (5 ảnh). Không suy số trang.
Log `codex-runs/` ở cả vị trí cũ/mới giữ nguyên, tra qua bảng ánh xạ.
`k3_kiemke.py` xếp theo aNNN để tránh đổi chỉ số khi tên mới xếp theo trang.

### 5. Files Changed

Danh sách 12 file đổi tham chiếu và output kiểm đầy đủ ở
`tmp/pdfs/review/a313-3/kiemke/r01_verification.json`.
Thêm `kiemke/doi_ten_anh.py`, `kiemke/test_doi_ten_anh.py`, bảng ánh xạ;
sửa `k3_kiemke.py`, chú thích `k3_crop.py`, danh mục, AGENTS/CLAUDE và checkpoint.
Chỉ stage câu mới R01 trong AGENTS/CLAUDE, giữ các sửa đổi có sẵn ngoài index.

### 6. Verification Already Completed

Kiểm trong lượt R01: `e4_check.py`, `e3/e3_check.py`, `e4_matrix.py` đều exit 0;
stdout/stderr trước/sau khớp nguyên byte. Các hash output ghi trong JSON bằng chứng.
Э4: 2877 dòng/58 bảng, reciprocal 1018, mismatch 20, chưa chép bảng đích 22,
243 dòng có dấu hỏi. Ma trận: 282 cột, 622 giao điểm, 254 khớp, 24 lệch/thiếu tên.
Э3 giữ ngoại lệ đã biết рис.6/19/25. Đây là kiểm dữ liệu, không xác nhận phần cứng.
Bốn unit test của script đổi tên đạt; dry-run trước/sau đạt; sinh lại `k3_trang.py`
exit 0 và `trang.csv` không đổi byte. Thứ tự kiểm kê và hai CSV khớp đủ a001…a249.
Quét cả file ẩn/bị ignore bằng `rg -uu`: không còn tên cũ ngoài ánh xạ và log lịch sử.
Đối chiếu snapshot SHA-256 trước nhiệm vụ: mọi file đọc được ngoài phạm vi R01 không đổi.

### 7. Known-Good State

249 ảnh không đổi nội dung; ánh xạ 1:1, tên mới duy nhất; tham chiếu hiện tại trỏ tên mới.
Các kết quả phần cứng/kết luận kỹ thuật của §11–12 là kế thừa, không kiểm lại trong R01.

### 8. Unfinished Work

Không mở rộng sang phân tích sơ đồ hoặc sửa các mismatch kế thừa. Giữ nguyên các việc
chụp bổ sung trong danh mục. JARVIS chưa có bản đồ/coverage A313 được đăng ký;
chưa nạp/công bố R01, giữ chứng cứ trong repo. Không có proposal ID của R01 cần consolidate.
Chủ đề cần nạp sau đăng ký: quy tắc tên/bảng ánh xạ, script và kiểm hồi quy, bẫy thứ tự #NNN.

### 9. Risks / Open Questions

File khóa Excel `~$a313.xlsx` bị khóa đọc nên không có hash; không tác động file này.
Các thay đổi có sẵn (dời `File của A313-V/`, a313.xlsx, IDEA.md, tài liệu khác) giữ nguyên,
không stage. Công cụ R01 giới hạn 249 ảnh cũ, không dùng để nhập ảnh bổ sung.

### 10. Exact Next Step

Sau commit R01, tra ảnh cần chụp ở `DANH-MUC_ANH_RE_A-313-3.md` §4;
ảnh mới bắt đầu a250. Không push nếu chưa có yêu cầu riêng của người dùng.
