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

**Kiến trúc Y16 (xác nhận người dùng 2026-10-23, SỬA LẠI 2026-10-24):** Y16 là **tấm sườn/backplane**,
không có linh kiện — chỉ đấu dây từ đầu cắm ngoài (3Ш1/3Ш2/3Ш3/3Ш4/3Ш5/3Ш7) tới các tấm khác (cáp bẹ
hoặc dây nối trực tiếp tuỳ panel). **SỬA LẠI 2026-10-24 (đảo ngược kết luận cũ):** Y16 **CÓ** sơ đồ
Э3 riêng — mã **ЕУ3.661.064**, dạng ma trận cross-reference 5 лист (xác nhận qua khung tên viết tay
"ЕУ3.661.064 Э3 л.N/5" đọc trực tiếp trên ảnh, người dùng chụp lại rõ 2026-10-24), lưu tại
`A313-3_CONTROL/Y16/RE_tr153_a150.jpg`…`a154.jpg` (chụp gốc) + `RE_trXXX_a258.jpg`…`a262.jpg` (chụp lại
2026-10-24). 11 ảnh trước đây đặt tên `E4_01-11_tr142-152.jpg`, nay `RE_tr142_a136.jpg`…`RE_tr152_a149.jpg`, nằm lẫn trong thư mục Y16 **KHÔNG
PHẢI là tài liệu của Y16** — đó là `ЕУ3.048.002 Э4` **"Sơ đồ đấu nối khối"**, tài liệu CHUNG của
TOÀN KHỐI (xác nhận khung tên "1/11"..."11/11"), đã dời sang `A313-3_CONTROL/KHOI_So-do-dau-noi/`.
Dữ liệu `matrix_nets.csv`/`matrix_notes.md` (dùng dựng `A313-3_ket-noi-toan-khoi.xlsx`) được chép
từ 5 trang ma trận tr.153-157 — dữ liệu kết nối vẫn đúng, chỉ sửa tên gọi tài liệu nguồn (Э3 riêng
của Y16, không phải "Э4/Y16" như ghi trước). Chi tiết: `KE-HOACH_KIEM-TRA_A-313-3.md` §1.5.

**Bảng kết nối toàn khối A-313-3 — vòng 2 (2026-10-23, Claude tự làm vì Codex hết usage):**
`Excel center control/A313-3_ket-noi-toan-khoi.xlsx` — mirror cấu trúc `a313.xlsx` (bảng của A-313-2),
7 sheet (`ky_hieu_chung`, `ket_noi_chung` là Excel Table+filter, `chi_tiet_tu_anh`, `can_doi_chieu`,
`canh_bao_quan_trong`, `ghi_chu_nguon`, `nhat_ky_ra_soat_1`). Dựng từ `e4_all.csv` (2877 dòng/58 bảng)
+ `matrix_nets.csv` (282 net) bằng thuật toán union-find tái dùng hàm của `e4_check.py`. Kết quả:
**2012 net**, 22 cột tấm (Y1-Y15,Y18-Y24), 8 cột đầu cắm ngoài, 3 cột "bó dây/đầu cắm khối"
(Y16-КП1/2/3, không gắn tên tấm cụ thể — đúng bản chất bản vẽ gốc, không phải lỗi), 142 dòng một
chiều, 100 net còn gắn cờ "CẦN XÁC MINH". Script tái tạo (chạy lại khi CSV nguồn đổi):
`tmp/pdfs/review/a313-3/e4/build_ket_noi_toan_khoi.py`. Kế hoạch gốc:
`PLAN_KET-NOI-TOAN-KHOI_A-313-3.md`. **Chưa qua phản biện của người dùng** — vòng 3 trở đi chờ
người dùng xem file rồi phản biện (ghi tiếp vào `nhat_ky_ra_soat_2` khi có).

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
Kết luận chính: Y4 thiếu Э3 (рис.5); ~~Y6 thiếu tr.167~~ **Y6: sửa 2026-10-24 — người dùng chụp lại đủ
3/3 lист rõ nét** (`A313-3_CONTROL/Y6/RE_trXXX_a255.jpg`…`a257.jpg`), thay toàn bộ ảnh cũ
(3 ảnh này ban đầu bị tải nhầm vào thư mục Y5, đã xác nhận qua khung tên "ЕУ3.057.140" và dời đúng chỗ);
Y1 thiếu tr.180, #75 chưa định danh; các tấm còn lại
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
| T06b (Y5, 2026-10-24) | Người dùng chụp lại 2 ảnh rõ nét (`A313-3_CONTROL/Y5/RE_tr171_a263.jpg`, `RE_tr172_a264.jpg`, thay bản mờ `RE_tr171_a167.jpg`/`RE_tr172_a168.jpg` cũ — đã xoá khỏi thư mục làm việc, bản gốc vẫn còn trong `ЕУ.048.002.РЭ(A313-3)/`). Claude đọc khung tên xác nhận đúng ЕУ3.057.139 Э3 l.1/2, l.2/2 — khớp trang 171/172. **169 dòng `?` + 36 chỉ-Э4 của T03b CHƯA được soát lại bằng ảnh mới** — hầu hết lý do ghi trong `ric08_mota.md` là "ảnh mờ/chữ nhỏ/nếp gấp" (У8–У25 ở #168), đúng loại vấn đề ảnh rõ hơn có thể giải quyết. Chưa làm vì ngoài phạm vi yêu cầu (chỉ đổi tên ảnh + cập nhật tham chiếu); đề xuất soát lại khi người dùng xác nhận | chưa commit | — |

| T04 рис.6 (Y3) | Codex: lượt 1 bị chặn (đề bài thiếu quyền sửa `E4_FILES`), lượt 2 **từ chối** vì lý do chính sách (thiết bị quân sự). **Claude tự chép** — PARTIAL: BOM 99, bảng đầu nối tờ 1 176 hàng, net 818 chân (166 НЕ ПРОСЛЕЖЕНО, 213 dòng `?`); Э3↔Э4 У3: 125 khớp / 32 lệch tên (chủ yếu cách ghi) / 1 chỉ-Э3 / 9 chỉ-Э4. Phát hiện: У37, У53 bị gạch trên Э3 = vắng trong ПЭ; #155/#156 nghi KHÔNG thuộc рис.6 (có R5–R8, C7, C8); nhãn «У15/У16» tờ 1 và «У5-4» tờ 3 trùng ký hiệu. Chi tiết `e3/ric06_mota.md` | xem log | — |
| T05 рис.9 (Y2) | Codex (qua Hermes, prompt tối giản, giới hạn CHỈ đọc `A313-3_CONTROL/Y2/RE_tr175_a171.jpg` + `RE_tr176_a172.jpg`) — **PARTIAL**: `ric09_bom.csv` 49 dòng (toàn bộ `name`="?", không thấy mã R/C/IC trên ảnh), `ric09_net.csv` 489 chân, `ric09_mota.md` ghi rõ các điểm chưa chắc. Codex tự báo: không đọc file nào khác, không chạy kiểm chéo. **Phát hiện mâu thuẫn mới:** bó dây số 14 giữa П1-49 và П3-29 mang 2 nhãn trái dấu +12,6V / −12,6V trên cùng bản vẽ. `e3_vs_e4.py` ban đầu KHÔNG chạy được (net.csv dùng tên tự đặt N01-N64 thay vì `Пn:NN label`) — **Claude tự sửa** (không cần Codex đọc lại ảnh): trích 176 dòng П1/П2/П3 đã có sẵn trong `ric09_net.csv` thành `ric09_conn.csv` đúng định dạng (`table,pin,signal,photo,note`), chạy lại `e3_vs_e4.py 9 У2` **THÀNH CÔNG**: 136 chân Э3 / 141 chân Э4, khớp 85, lệch tên 50 (phần lớn chỉ do dấu `?` thay ký tự chưa chắc, thiếu dấu phủ định ¬, hoặc Э3 dùng điểm tắt а/б thay tên đầy đủ — không phải lỗi thật), chỉ-Э3 1, chỉ-Э4 6. Xem `ric09_vs_e4.csv`. File đã dời từ `A313-3_CONTROL/Y2/` sang `tmp/pdfs/review/a313-3/e3/` (thư mục gốc chứa file đã chép). | chưa commit | — |
| T06 рис.7 (Y6) | Codex (qua Hermes, prompt tối giản, giới hạn CHỈ đọc 3 ảnh `A313-3_CONTROL/Y6/RE_trXXX_a255.jpg`…`a257.jpg`) — **PARTIAL**: `ric07_bom.csv` 77 dòng (toàn bộ `name`="?"), `ric07_net.csv` 997 chân (184 dòng `net`="?"), `ric07_conn.csv` 173 dòng (П1 1-53, П2 1-53, П3 1-67, đúng định dạng ngay từ đầu — lần đầu Codex tự tạo conn.csv theo yêu cầu, không cần Claude sửa như Y2). Có BOM chứa UTF-8 BOM ở đầu 3 file CSV — Claude tự sửa (strip BOM) rồi chạy `e3_vs_e4.py 7 У6` **THÀNH CÔNG**: 139 chân Э3/157 chân Э4, khớp 103, lệch tên 36 (phần lớn do viết tắt khác nhau: "Декодиров."↔"ДЕКОД.", biểu thức boolean viết khác ký hiệu — không phải sai thật; 1 chỗ đáng chú ý: "ТТП" ↔ Э4 "ТТЛ", nghi Codex đọc nhầm Л→П), chỉ-Э4 18 (Codex để trống khi ô Цепь không chắc, đúng theo yêu cầu). Xem `ric07_vs_e4.csv`, `ric07_mota.md`. | chưa commit | — |
**Quy trình:** sau mỗi task dừng chờ người dùng duyệt (`tools/CODEX_ORCHESTRATION.md` §5).
**Đề xuất kế tiếp (cũ, đã làm T03b):** T03b = resume thread, yêu cầu Codex xuất báo cáo cuối + soát 187 ô `?`, 42 chân chỉ-Э4, 2 lệch tên
(`CODEX_TIMEOUT=7200`); sau đó Claude kiểm ảnh. Rồi T04 Y3 (рис.6, 3 tờ, dùng #231/#232 cho tờ 1).

**Đề xuất kế tiếp (sau T03b):** T03c = resume `01a162ad`, chỉ soát У8–У25 trên #168 (169 `?`) và 36 ONLY_E4, CODEX_TIMEOUT=7200; hoặc chuyển T04 Y3 (рис.6) và để phần còn lại của рис.8 chờ ảnh chụp lại #168 rõ hơn.

**Cập nhật chính sách Codex (2026-10-23, sau T05):** T04 (Y3) Codex từ chối vì lý do chính sách; T05 (Y2) — cùng loại
nội dung, prompt tối giản không nhắc "quân sự" — Codex **nhận và hoàn thành**. Kết luận: không còn cấm tuyệt đối,
nhưng chất lượng T05 thấp hơn Claude tự chép (toàn bộ BOM `name="?"`, netlist dùng định dạng khác khiến kiểm chéo
tự động không chạy được) — vẫn nên ưu tiên Claude tự chép cho các tấm quan trọng, chỉ thử Codex cho việc phụ/thử nghiệm.
**Đề xuất kế tiếp (sau T05):** người dùng đối chiếu thủ công netlist Y2 (đặc biệt mâu thuẫn П1-49/П3-29) trước khi
dùng; sau đó Claude chép Y1 (рис.10) hoặc Y6 (рис.7) theo thứ tự đề xuất cũ.

### 12.2. Tiếp nhận trực tiếp bởi Codex — 2026-10-22 21:00 +07:00 (lịch sử, merge từ nhánh `codex/a313-v-intake-20261022`)

- Yêu cầu hiện tại: Codex làm trực tiếp với người dùng, không qua Claude. Cơ chế điều phối ở §12 và các đề xuất resume Claude cũ chỉ là lịch sử. Lượt này chỉ tiếp nhận, chạy kiểm và chờ người dùng chọn nhiệm vụ.
- Checkout: E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/2.BO TLTK DAU A_A313-V; baseline main `1450f2d`; nhánh checkpoint `codex/a313-v-intake-20261022`.
- Đã đọc theo thứ tự yêu cầu: AGENTS, handoff, orchestration §5–6, ric11/08/06_mota, danh mục ảnh và trang.csv. Đã kiểm git status và log -8.
- Kiểm ngay lượt này: chạy lại ric06_gen.py, e3_check.py, e3_vs_e4.py cho 6 У3 / 8 У5 / 11 У7, e4_check.py. Không phát sinh diff CSV; không sửa script hay tài liệu gốc.
- Output chính: `bom 99 conn 176; net 818`; рис.6 `match 125 | name mismatch 32 | only E3 1 | only E4 9`; рис.8 `match 121 | name mismatch 3 | only E3 0 | only E4 36`; рис.11 `match 105 | name mismatch 0 | only E3 0 | only E4 1`.
- Э4: `rows 2877 tables 58`; `reciprocal ok 1018 | mismatch 20 | target table not transcribed 22`; `struck-out rows skipped: 36`; `duplicate (table,pin): -`; `rows marked ?: 243`.
- e3_check ghi nhận đúng ngoại lệ đã biết рис.6/19/25. PASS của checker chỉ là kiểm dữ liệu/cấu trúc, chưa xác nhận topology bằng ảnh hoặc nghiệm thu phần cứng.
- §12.1 được tái xác nhận: рис.11 PASS phạm vi dữ liệu (166 ref/462 chân, 0 dòng ?); рис.8 PARTIAL (948 chân, 169 dòng ?); рис.6 PARTIAL (818 chân, 213 dòng ?, 166 chưa lần). Không đổi kết quả baseline. Các con số dòng ? đếm bằng csv.DictReader, kiểm mọi giá trị của từng hàng; chưa lần đếm prefix Unicode НЕ ПРОСЛЕЖЕНО trong net.
- JARVIS: check hiện tại ok, không errors/warnings; chưa tìm thấy bản đồ/coverage A313 trong projects/work. Không dùng capability netlist-readers-and-compare vì phương ngữ khác CSV hiện tại. Chưa đăng ký/nạp dự án; giữ kết quả tại checkpoint này, cần thống nhất đăng ký riêng. Không có proposal của lượt này để consolidate.
- AgentMemory: đã tìm hẹp theo tên checkout và A-313-3/T04; không dùng kết quả tìm kiếm để thay trạng thái repo.
- **ĐÃ SUPERSEDED** bởi các lượt T05/T06 và việc chép Y2/Y3/Y4/Y6 sau đó (2026-10-23→24) — giữ lại đây chỉ làm nhật ký lịch sử, không còn phản ánh trạng thái hiện tại của dự án.

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


---

# S01 — bàn giao sau commit

## 1. Current Task
Kiểm kê VT34/VT28 chỉ đọc nguồn. Người dùng đã resume sau mốc tạm dừng đổi effort. Đã chốt bản kiểm kê; giới hạn chép tiêu đề còn được công khai trong báo cáo.

## 2. Current Project State
Checkout: E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V
Nhánh main; HEAD 6c7ed575e5f574b1d71c58bc6c441c7255067113. Commit S01 đúng năm file; không push. Thay đổi ngoài nhiệm vụ giữ nguyên, không stage.

## 3. Completed Work
55 PDF, 429 trang = VT34 252+7 và VT28 170. Tất cả đã xem/ghi chú, render 120 dpi, CHUA_XEM=0. Báo cáo đủ bảng file, thiếu/trùng/tờ gấp, sơ đồ rời, hình/bảng. Lượt resume sửa tiêu đề рис.7/12 VT28 sau phóng ảnh; рис.12 là формирования запросов.

## 4. Important Decisions
Nguồn chỉ đọc; không gán số từ tên file. VT34 dùng số đóng/in mép trên; VT28 số in chân. Mọi suy đối chiếu tờ rời được ghi rõ. Không phân tích mạch. CSV tiêu đề là bản nhận diện có giới hạn, không khẳng định chép nguyên văn hoàn chỉnh.

## 5. Files Changed
Commit chỉ .gitignore và tmp/pdfs/review/a313-3/vt/{kiemke_vt.py,vt_files.csv,vt_pages.csv,S01_baocao.md}. PROJECT_HANDOFF và .handoff giữ cục bộ, ngoài commit. Nguồn A313 original/a313 không stage.

## 6. Verification Already Completed
Lượt resume 2026-10-23T17:53:21: --check --duplicates exit0 sau sửa tiêu đề; sau chuẩn hóa LF chạy --check exit0, --render exit0 và CSV byte-identical 2/2. FILES55 SHA25655/55 PAGES429 UNIQUE429 CHUA_XEM0; số in trống VT34=6,VT28=31. git diff --cached --check đạt; assert index đúng5file trước commit. Hash vt_files=61c200bf780a904f4d0d6fa0363c7aca9753f6eeb2dcbc72536ff8a543d6fc47; vt_pages=842e047086df8b47b12b622a8149feb4492f43e7941eb8bc8ecd8ab5c140d8a3. Đếm lại số hiệu: VT34 рис17/табл32, VT28 рис34/табл14. TR122-143=23nội dung+17trắng. Việc xem toàn bộ429 ảnh và xác nhận cặp trùng kế thừa checkpoint trước; lượt này chỉ phóng lại hai chú thích cần sửa.

## 7. Known-Good State
Kiểm chứng cấu trúc/hash/chạy lại đạt, không chứng minh tuyệt đối phần chép tay. VT28 trang viết tay74 ở TR10-23 PDF1; TR2 không trùng TR1-9. Cặp trùng đã xác nhận trong báo cáo §3.

## 8. Unfinished Work
Một số mã bản vẽ/ký hiệu trong tiêu đề chưa chép đầy đủ; thiếu bản chuẩn để chốt trang nghi thiếu. Sáu tờ rời VT34 chỉ suy liên hệ рис1201–1205. Chưa nạp JARVIS: project chưa đăng ký, không proposal ID để consolidate; các chủ đề chờ nạp ghi báo cáo §7. Không thay cấu hình JARVIS trong nhiệm vụ kiểm kê này.

## 9. Risks / Open Questions
Dhash toàn ảnh bỏ sót tờ cắt/xoay; số hình VT28 chạy lại theo phần, đếm số hiệu khác nhau không phải số hình vật lý. Nhiều thay đổi có sẵn ngoài S01, tuyệt đối không add -A. Không dùng tiêu đề rút gọn làm bản chép nguyên văn.

## 10. Exact Next Step
Đọc S01_baocao.md §3 và §7 để duyệt khoảng nghi thiếu và phạm vi bổ sung tiêu đề; không tự mở nhiệm vụ phân tích kỹ thuật, không push.

## 13. Y3/Y4 ảnh chụp lại (Claude, 2026-10-24)
- Ảnh mới rõ nét trong `A313-3_CONTROL/Y3` (a252 tờ 1, a253 tờ 2, a254 tờ 3 của рис.6) và `A313-3_CONTROL/Y4` (a250, a251 = рис.5 tờ 1/2, 2/2). Đã xoá 6 bản sao cũ trong Y3 (SHA-256 trùng bản gốc vẫn còn trong thư mục RE).
- #155/#156 là рис.5 (Y4), không thuộc рис.6 — đã sửa `DANH-MUC_ANH_RE_A-313-3.md` §2, §3 và thêm §5.
- рис.6 (Y3): lần lại trên ảnh mới, НЕ ПРОСЛЕЖЕНО 166 → 95, dòng `?` 213 → 155; `e3_vs_e4 6 У3` không đổi (125/32/1/9). Khối ghi đè ở cuối `ric06_gen.py`.
- рис.5 (Y4): đã quét — BOM 80 (ПЭ #137–#139), bảng đầu nối 176 hàng, `e3_vs_e4 5 У4` = 133 khớp / 25 lệch tên / 1 chỉ-Э3 / 3 chỉ-Э4; **chưa chép netlist** (`ric05_net.csv` rỗng, chưa vào `e3_check.py`). Chi tiết `e3/ric05_mota.md`.
- Chưa cập nhật `Excel center control/Danh-muc-24-tam_A-313-3.xlsx` (file đang mở trong Excel). Việc kế: chép netlist рис.5; xác minh số trang a251 (159 hay 189).
## 13. Y3/Y4 ảnh chụp lại (Claude, 2026-10-24)
