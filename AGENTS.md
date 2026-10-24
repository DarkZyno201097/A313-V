# CLAUDE.md — Bản giao việc dự án A313-V

> File này được bàn giao từ một session Cowork (claude.ai) sang Claude Code.
> Lịch sử hội thoại **không** đi theo. Bộ nhớ claude.ai Project cũng **không**
> đọc được từ đây. Tất cả context cần thiết nằm trong file này và `README.md`.

---

## 1. Đọc trước khi làm bất cứ việc gì

Theo đúng thứ tự:

1. `README.md` — bản đồ thư mục, ràng buộc an toàn, trạng thái, các bẫy đã gặp
2. `PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md` — **Rev. C**, §0 là nhật ký
   phản biện với 31 mã kết luận; §12 là tồn đọng
3. `QUY-TRINH_TEST_TUNG-BUOC_A313-V.06.md` — quy trình test; nhật ký kết quả ở
   cuối file cho biết đang ở bài nào

---

## 2. Người dùng

Kỹ sư phần cứng avionics, Phân xưởng 5 — Nhà máy A32. Làm sửa chữa mạch
avionics (ARINC-429, MIL-STD-1553B), FPGA/CPLD (Xilinx XC4000/Spartan/Virtex,
Altera FLEX10K/MAX/Cyclone, EPM7xxx), thiết kế PCB và ATE, Verilog/VHDL,
STM32, JTAG/boundary-scan, reverse engineering FPGA đời cũ.

* **Trả lời bằng tiếng Việt.** Dùng đúng thuật ngữ Nga/Việt của ngành
  (СКТ, подложка, BVTK, DKKT, TMKT, LRU, đồ gá).
* Đi sâu kỹ thuật, bám datasheet và tiêu chuẩn (ARINC, MIL-STD, IEEE 1149.1).
  Không giải thích lại kiến thức cơ bản.
* **Dấu thập phân là dấu phẩy** (`2,05 kΩ`, `±12,6 V`) — giữ nguyên quy ước
  này trong mọi file.
* Chủ động đề xuất phương án debug, kiến trúc, và **cách kiểm chứng**.

---

## 3. Luật cứng

1. **Tài liệu gốc A32 là chỉ-đọc.** Không bao giờ sửa hay đổi tên:
   `File của A313-V/1.BVTK A313-V/`, `File của A313-V/2.DKKT A313-V/`,
   `File của A313-V/3.HDSD A313-V/`, `File của A313-V/TMKT&HDSD A313-V/`,
   `File của A313-V/BVTK-A313-V.04.pdf`, `File của A313-V/BVTK-A313-V.06.pdf`,
   `A313 original/`, `File của A313-V/File mach in va mach nguyen ly_A313_V/`,
   `File của A313-V/GIAO AN HLKT A313-V.*`,
   `ЕУ.048.002.РЭ(A313-3)/` (ảnh chụp bản giấy; tra trang ở `DANH-MUC_ANH_RE_A-313-3.md`).
   **Di chuyển 2026-10-24** (người dùng tự làm ngoài Hermes, đã xác nhận): toàn bộ tài liệu gốc
   A313-V dời từ thư mục gốc repo vào `File của A313-V/`, nội dung không đổi (đã kiểm diff = 0
   khác biệt so với bản cũ trong git HEAD trước khi commit). Thư mục `ЕУ.048.002.РЭ(A313-3)/`
   (đổi tên 2026-10-23, giữ ở gốc repo, không dời) đã đổi tên một lần theo quy tắc trong
   `DANH-MUC_ANH_RE_A-313-3.md`, nội dung không đổi, ánh xạ ở `ЕУ.048.002.РЭ(A313-3)/_DOI-TEN.csv`;
   từ nay vẫn chỉ-đọc.
   Bản chuyển đổi/trích xuất ghi ra file mới, đặt cạnh file gốc.
   **Repo chỉ chứa PDF** — mọi `.doc`/`.docx` bị `.gitignore` loại, chỉ có trên
   máy làm việc. Trên cloud không sửa được báo cáo Word.
2. **Ảnh trong `File của A313-V/KET-QUA-TEST_A313-V.06/` là số liệu đo thật** — không ghi đè.
   Bản nén ghi thành file mới.
3. **Repo GitHub phải private.** Nội dung là tài liệu kỹ thuật của A32. Không fork, không collaborator ngoài,
   không bật public.
4. **Không `git push` mà chưa được người dùng xác nhận.** Push rồi thì xoá
   khỏi history rất khó. Luôn chạy `git ls-files` cho người dùng xem trước.
5. **Số liệu phải kiểm chứng bằng script, không được khẳng định bằng cảm giác.**
   Session trước đã sai hệ số cơ bản (1,2348 thay vì **1,2446**) vì tính nhẩm.
   Mọi con số đưa vào tài liệu phải có script hoặc mô phỏng chứng minh, và
   script đó lưu lại trong `tmp/pdfs/review/`.

### ⚠ An toàn phần cứng — xem đầy đủ ở `README.md` §2

Tóm tắt: tấm .06 **không có bảo vệ ngược cực** · tải giả **≥ 400 Ω**
(`2Т203Б` chỉ 10 mA) · không chập đầu ra xuống mát · không song song hai nguồn
tín hiệu trên `DC11.A5` · đi dây và kẹp que đo khi **đã tắt nguồn** · không
nâng giới hạn dòng để ép tấm chạy.

---

## 4. Việc đang tồn — làm theo thứ tự này

### 4.1. Sửa lỗi Rev. C — ĐÃ XONG phần chữ (2026-10-20), còn một mục

Đã sửa trong `PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md` (người dùng duyệt diff):

* 50 chỗ dính chữ trên 33 dòng (nhiều hơn ước tính 20–25), gồm cả dạng
  chữ+`−`, chữ+chữ Hy Lạp (`mũτ`), hai âm tiết dính (`đođộng`), danh sách số
  dính dấu phẩy (`±4,±1,0 V`). Giữ nguyên các ký hiệu cố ý: `U14→U17`, `S→OA`,
  `pha+`/`pha−`, `Vref±`, `Mux+ADC`, toạ độ `(x;y)`, công thức trong code.
* `3 Ш 3` → `3Ш3`; `2,05 Ω M` → `2,05ΩM` ở 3 chỗ (đã kiểm bằng pdfplumber:
  BV.25 ghi đúng `2,05ΩM, 1%`, BVTK trang 31).
* Đã chèn dòng đầu §10.4: **giới hạn pass/fail lấy từ khối tốt**.

**Còn lại:** §5.2 và §10.4 bị giảm độ dễ đọc so với Rev. B — chưa xem được vì
không có bản Rev. B trong thư mục; cần người dùng cung cấp nếu muốn so.

### 4.2. Dời `tmp/pdfs/review/` thành `Phan-bien/`

Rev. C trích dẫn đường dẫn `tmp/pdfs/review/...` làm bằng chứng, nhưng `tmp/`
đọc như thư mục rác. Dời sang `Phan-bien/` và sửa toàn bộ link trong tài liệu.
Cập nhật `.gitignore` tương ứng.

### 4.3. Ảnh dao động ký — đã quyết định giữ bản gốc

12 ảnh `KET-QUA-TEST_A313-V.06/*.png` (~5 MB/ảnh) là **ảnh chụp bằng điện thoại**
màn hình máy đo (2568×1926 RGB, có phản chiếu), không phải ảnh xuất từ máy
Tektronix — nén PNG 8-bit palette sẽ loang màu. Người dùng đã duyệt commit
nguyên bản (63,9 MB, chỉ một lần vì ảnh không bao giờ sửa). Nếu cần bản nhẹ
(nhúng báo cáo), xuất JPEG ra file mới, giữ bản gốc.

### 4.4. Git — repo private `A313-V`, không dùng Git LFS

Chỉ PDF + Markdown + script + ảnh đo + Altium SchDoc/PcbDoc lên repo; Word ở
lại máy làm việc (xem `.gitignore`). Không dùng Git LFS (quota GitHub free nhỏ).
Mọi push vẫn cần người dùng xác nhận (luật §3.4).

### 4.5. Tiếp tục đo tấm .06 — B08 còn thiếu bảng số

Nhật ký cuối `QUY-TRINH_TEST_TUNG-BUOC_A313-V.06.md` ("Tổng hợp B09 đến B12"):
B05–B07± đạt; B09, B10 đo hết theo xác nhận; B11/B12 thử chọn mẫu; tấm .06
**đạt chức năng trong phạm vi đã thử**, đã lập báo cáo. **B08 chưa có bảng số
Vin/Vo** (bài B08-1a+ trở đi) — chưa tính được gain/offset/độ tuyến tính.

### 4.6. Hai câu hỏi mở (§12.2 của file PHAN-TICH)

* **Biên độ `~5V/400Hz`**: kết luận hiện tại **5 V<sub>rms</sub>**, chưa đo trên
  khối tốt. Phép thử phân định: Δt(М, xung400Hz) ≈ **358 µs** ⇒ rms ·
  ≈ **528 µs** ⇒ peak.
* **Nguồn gốc tín hiệu `~5V/400Hz` chưa rõ.** Chỉ xuất hiện ở trang 28/56 của
  BVTK. Tấm nguồn A313-V.08.01 chỉ có vào 27 V DC, không sinh 400 Hz
  (đã kiểm BV.30). Cần tìm trong tài liệu khối hoặc đo trên máy bay.
  **Cập nhật 2026-10-20** (`PHAN-TICH_TOAN-KHOI_A313-V.md` §2.5): BV.01, TMKT §4/§6.5
  và phụ lục đầu cắm chỉ ra **biến thế trên sát-xi** (`Tp1`), sơ cấp 3Ш4/55 (~36 V ФА)
  và 3Ш4/56 (~36 V ФС qua cầu chì 4 A), thứ cấp → DC11.A5. Không bản vẽ nào vẽ biến
  thế ⇒ vẫn phải đo (việc H2). Khối gốc A-313-3 cũng tạo `УПР. МОД 1/2` từ 5 V 400 Hz
  pha AC (`A-313-3.HDSDKT.pdf` §2.2.2, trang PDF 49) — cùng nguồn lưới.
  **Cập nhật 2026-10-22** (`SO-DO-NGUON_A-313-3.md` §2): trong khối Nga, ~5 V 400 Hz do **Тр1 ТН-12-40-400
  trên khối nguồn У17** (рис.25) hạ từ ~36 V pha A/C (3Ш4/55–56 → 3Ш5/33, /25), ra 3Ш5/11–12 ⇒ là
  điện áp xoay chiều hạ từ lưới 36 V 400 Hz, khớp giả thuyết biến thế của A313-V. Biên độ rms/peak vẫn phải đo.

### 4.7. Chưa làm: phân tích tấm **A313-V.05**

Người dùng đã yêu cầu từ lâu nhưng chưa làm — mới chỉ xong datasheet linh kiện.
Tấm .05 là **chuyển mạch tín hiệu ra**: 57 vỏ `168КТ2Б` (= 228 khoá tương tự),
58 × 330 kΩ, 49 × 4,7 µF, 2 đầu nối DC96C (DC9, DC10). Sơ đồ ở **BV.18**
(trang 24) và BV.21.

### 4.8. Mục tiêu tiếp theo: phân tích toàn khối và hướng sửa chữa

**Rev. A đã lập 2026-10-20:** `PHAN-TICH_TOAN-KHOI_A313-V.md` (sơ đồ khối, từng tấm,
cây chẩn đoán theo A-313-2, việc cần đo §5, bảng chưa chắc chắn §6) + script
`tmp/pdfs/review/toan-khoi/tk_*.py`. Việc còn lại là đo phần cứng theo §5 (H1…H18).

Người dùng muốn (làm trên cloud) phân tích **toàn bộ khối A313-V** và đưa ra
hướng xử lý sửa chữa cho cả khối, không chỉ tấm .06. Nguồn đã có trong repo:

* `A313 original/` — Hướng dẫn sử dụng kỹ thuật A-313, tiếng Việt (bìa ghi
  `ЕУ3.048.002 РЭ`), 4 PDF, tổng 241 trang.
  `A-313-2.pdf` có chương **"Tìm hỏng hóc: sơ đồ tìm kiếm và bài trừ hỏng
  hóc"** — điểm xuất phát cho cây chẩn đoán toàn khối.
* `File mach in va mach nguyen ly_A313_V/` — project Altium vẽ lại (SchDoc +
  PcbDoc) của các tấm: TAM1 xử lý trung tâm, TAM2 chuyển mạch tín hiệu vào,
  Tam3 tích phân, TAM4 biến đổi, Tam5 chuyển mạch tín hiệu ra, Tam6 khuếch đại
  tín hiệu ra, mạch nguồn, đầu cắm 31/96 chân, tấm linh kiện rời rạc, mạch
  biến đổi lệnh đơn, mạch kiểm tra nguồn. Không có file `.PrjPcb`.
  SchDoc đọc được bằng Python (`olefile`) không cần Altium; netlist rút ra
  phải đối chiếu với BVTK trước khi dùng.
* `File mach in.../sodocactam.pdf` (12 trang A3) — **mất chữ Cyrillic** khi
  xuất PDF (ví dụ nhãn rơ-le hiện thành `ro e PEC-49`, trang 7). Đọc ký hiệu
  thì dùng SchDoc hoặc BVTK, không tin bản PDF này.
* `GIAO AN HLKT A313-V.pdf` — giáo án huấn luyện kỹ thuật (nguyên lý khối).

### 4.9. Nhiệm vụ mới: sửa khối gốc Nga A-313-3 làm dự phòng cho A313-V

Người dùng (2026-10-20): khối A313-V vẫn có trục trặc chưa rõ nguyên nhân ⇒ khôi phục bộ Nga
A-313-2A + A-313-3 làm dự phòng; làm A-313-3 trước. Bàn ПС17-318/319 đang hỏng. Kế hoạch tổng
quát: `KE-HOACH_KIEM-TRA_A-313-3.md`. Tập `A313 original/A-313-3.HDSDKT.pdf` **mất toàn bộ hình**
(chỉ còn tên hình và danh mục linh kiện Y2–Y6) ⇒ đang chờ người dùng bổ sung sơ đồ theo §2 của
kế hoạch; có sơ đồ mới lập kế hoạch chi tiết từng tấm.

---

## 5. Phương pháp trích netlist từ PDF bản vẽ

Dùng `pdfplumber`, phân loại theo **màu nét vẽ**:

| Thành phần | `stroking_color` | Kiểu đối tượng |
|---|---|---|
| Dây nối | `(0.502, 0.0, 0.251)` nâu đỏ | `lines` |
| Chân linh kiện | `(1.0, 0.0, 0.0)` đỏ | `lines` |
| **Điểm nối (junction)** | `(1.0, 0.0, 1.0)` magenta | **`curves`** — không phải `lines` |
| Ký hiệu linh kiện | `(0.0, 0.0, 1.0)` xanh | `lines` |

Gộp net bằng union-find trên đầu mút đã snap + điểm nối + T-junction.
Script tham chiếu: `tmp/pdfs/review/netlist_review.py`.

### ⚠ Bẫy font — gặp là chắc chắn

Lớp text trong PDF bị map sai. Ghi `vih.1a=` nhưng render ra **`ВЫХ.1А=`**.

Bảng đổi: `v→В` `i→Ы` `h→Х` `a→А` `b→Б`

Hậu tố: `=` là đầu vào **DC** · `==` là đầu ra **400 Hz**.

### Khi cần đọc chính xác ký hiệu linh kiện

Render trang ở **400 dpi** rồi xem ảnh, đừng tin lớp text. Session trước đã sai
topology ba lần (`U14.10`/`U15.10`, cụm chia, cách ghép cổng A+C thay vì **A+D**)
vì tin lớp text.

---

## 6. Ghi chú về Codex

Người dùng cũng dùng Codex cho việc này. `PROMPT_CODEX_phan-bien-A313-V.06.md`
là prompt phản biện đối kháng đã dùng để sinh ra Rev. C.
Codex đọc `AGENTS.md`, không đọc `CLAUDE.md` — nếu cần, copy file này thành
`AGENTS.md`, nhưng nhớ là hai bản sẽ trôi lệch nhau theo thời gian.
