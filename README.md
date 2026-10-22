# A313-V — Bộ tài liệu thiết kế đầu A & hồ sơ kiểm tra

Khối **máy tính dẫn đường A313-V** (máy bay Su-27). Repo phục vụ công việc
reverse engineering, xây dựng quy trình kiểm tra và thiết kế ATE cho các tấm
PCB trong khối.

> ⚠ **REPO NÀY PHẢI Ở CHẾ ĐỘ PRIVATE.**
> Nội dung gồm bản vẽ thiết kế (BVTK), điều kiện kỹ thuật (DKKT), thuyết minh
> kỹ thuật (TMKT) gốc của Nhà máy A32, cùng các tài liệu phân tích dẫn xuất
> trực tiếp từ chúng (netlist, bảng chân connector, trị số linh kiện).
> Không fork, không thêm collaborator ngoài, không bật public.

---

## 1. Bản đồ thư mục

| Đường dẫn | Loại | Nội dung |
|---|---|---|
| `1.BVTK A313-V/` | **gốc A32** | Bản vẽ thiết kế, 56 trang (`.doc` + `.pdf`) |
| `2.DKKT A313-V/` | **gốc A32** | Điều kiện kỹ thuật |
| `3.HDSD A313-V/` | **gốc A32** | Hướng dẫn sử dụng |
| `TMKT&HDSD A313-V/` | **gốc A32** | Thuyết minh kỹ thuật + HDSD (`.pdf` xuất từ `.docx` gốc) |
| `BVTK-A313-V.04.pdf`, `BVTK-A313-V.06.pdf` | **gốc A32** | Bản vẽ trích riêng tấm .04 và .06 |
| `A313 original/` | **gốc** | HDSD kỹ thuật A-313 (4 PDF, 241 trang); `A-313-2.pdf` có phần tìm hỏng hóc |
| `File mach in va mach nguyen ly_A313_V/` | **gốc** | Altium SchDoc/PcbDoc vẽ lại các tấm của khối; `sodocactam.pdf` mất chữ Cyrillic |
| `GIAO AN HLKT A313-V.pdf` | **gốc** | Giáo án huấn luyện kỹ thuật A313-V |
| `PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md` | ✍ phân tích | Phân tích đầy đủ tấm .06 — **Rev. C** |
| `PHAN-TICH_TOAN-KHOI_A313-V.md` | ✍ phân tích | Toàn khối: sơ đồ khối, từng tấm, cây chẩn đoán, việc cần đo — **Rev. A** |
| `KE-HOACH_KIEM-TRA_A-313-3.md` | ✍ kế hoạch | Khối gốc Nga A-313-3: bảng kê 24 vị trí + tình trạng sơ đồ, danh sách cần bổ sung, kế hoạch kiểm tra tổng quát |
| `QUY-TRINH_TEST_TUNG-BUOC_A313-V.06.md` | ✍ quy trình | Quy trình test từng bước + nhật ký kết quả |
| `PROMPT_CODEX_phan-bien-A313-V.06.md` | ✍ công cụ | Prompt phản biện đối kháng dùng cho Codex |
| `Datasheet/` | ✍ + gốc NSX | 5 file `.md` giải thích linh kiện + datasheet gốc PDF |
| `KET-QUA-TEST_A313-V.06/` | 📊 số liệu | Ảnh dao động ký các bài test (xem `README.md` trong đó) |
| `BAO-CAO_KIEM-TRA_A313-V.06.docx` / `_CHANH.pdf` | 📄 báo cáo | Báo cáo kiểm tra |
| `tmp/pdfs/review/` | 🔬 bằng chứng | netlist.json, channel-audit.csv, PNG crop, script phản biện |
| `tmp/pdfs/review/toan-khoi/` | 🔬 bằng chứng | Script toàn khối `tk_*.py` (SchDoc → BOM/netlist, đầu cắm, mux), CSV/JSON, PNG |
| `tmp/build_test_report.py` | 🔧 script | Sinh lại báo cáo PDF từ các file `.md` |

**Ký hiệu:** `gốc A32` = không sửa, chỉ đọc · `✍` = tài liệu do ta viết, sửa
thường xuyên · `📊` = số liệu đo thật, không sửa · `🔬` = bằng chứng phản biện

---

## 2. Tấm A313-V.06 — "Khuếch đại tín hiệu ra"

16 kênh **điều chế cân bằng** (balanced modulator / chopper ±1): mỗi kênh nhận
một mức DC `Вых.nX=` và biến thành sóng vuông 400 Hz `Вых.nX==` — biên độ mang
`|giá trị|`, pha 0°/180° mang **dấu**. Cần vậy vì cuộn СКТ/resolver ở đầu nhận
không cho DC đi qua và cần đủ 4 góc vuông.

Thành phần: **18 × 140УД1Б** (op-amp) · **12 × 168КТ2Б** + **3 × 168КТ2В**
(khoá tương tự MOS 4 kênh) · **16 × 2Т312Б** (NPN) + **16 × 2Т203Б** (PNP).

### ⚠ Ràng buộc an toàn — đọc trước khi cấp nguồn

1. Tấm **không có bảo vệ ngược cực**. Tuyệt đối không cấp +5 V vào
   `DC11.A2/B2/C2` hay +6,3 V vào `DC11.A4/B4/C4` — đó là net không dùng.
2. **Không chập đầu ra xuống mát.** `2Т203Б` chỉ chịu 10 mA liên tục; dòng
   ngắn mạch qua R 180 Ω ≈ 66 mA ⇒ hỏng ngay. **Tải giả ≥ 400 Ω.**
3. **Không song song hai nguồn tín hiệu trên `DC11.A5`.** Phải ngắt hẳn nguồn
   DC trước khi nối máy phát AC.
4. Mọi việc đi dây, kẹp que đo, gắn tải đều làm khi **đã tắt nguồn**.
5. **Không nâng giới hạn dòng** để ép tấm chạy.

---

## 3. Trạng thái hiện tại

* `PHAN-TICH` đã qua **Rev. C** — Codex phản biện đối kháng, 31 mã kết luận,
  ghi ở §0 "NHẬT KÝ PHẢN BIỆN".
* Quy trình test: đạt **B05, B06, B07+, B07−**; B09/B10 đo hết theo xác nhận,
  B11/B12 thử chọn mẫu ⇒ tấm .06 đạt chức năng trong phạm vi đã thử, đã có báo
  cáo. **B08 còn thiếu bảng số Vin/Vo** (từ B08-1a+).
* Tồn đọng, xem §12 của file `PHAN-TICH`:
  * **#1 Biên độ `~5V/400Hz`** — kết luận hiện tại là **5 V<sub>rms</sub>**
    (quy ước `~` của Nga; bus 400 Hz máy bay ghi ~36 V/~115 V; CI 2003RP hiển
    thị V<sub>rms</sub>). Chưa đo trên khối tốt. Phép thử phân định:
    Δt(М, xung400Hz) ≈ **358 µs** ⇒ rms · ≈ **528 µs** ⇒ peak.
  * Nguồn gốc tín hiệu `~5V/400Hz` **chưa rõ**: chỉ xuất hiện ở trang 28 của
    BVTK; tấm nguồn A313-V.08.01 chỉ có vào 27 V DC, không sinh 400 Hz.
* Lỗi khoảng trắng của Rev. C (50 chỗ dính chữ, `3Ш3`, `2,05ΩM`) **đã sửa**
  ngày 2026-10-20; còn rà độ dễ đọc §5.2/§10.4 so với Rev. B (chưa có bản Rev. B).

---

## 4. Lưu ý khi dùng repo

* **Repo chỉ chứa PDF, không chứa Word.** `.gitignore` loại mọi `.doc`/`.docx`
  (115,7 MB, gồm `BAO-CAO_...docx` 52,8 MB) — chúng chỉ có trên máy làm việc;
  sửa báo cáo Word phải làm ở đó rồi xuất lại PDF.
* **Không dùng Git LFS** (quota GitHub free nhỏ). File nhị phân nào commit lại
  cũng cộng nguyên dung lượng vào history **vĩnh viễn** — commit PDF/PcbDoc thưa.
* 12 ảnh trong `KET-QUA-TEST_` (~5 MB/ảnh) là ảnh chụp điện thoại màn hình máy
  đo, giữ nguyên bản trong repo. Cần bản nhẹ thì xuất JPEG ra file mới.
* Tên file có dấu tiếng Việt. Chạy một lần để git hiển thị đúng:
  `git config core.quotepath false`
* Project Altium của tấm .06 nằm **ngoài** thư mục này, ở
  `MODULE\A313\A313-V.06\`. Chưa đưa vào repo.

### Sinh lại file dẫn xuất

```bash
python tmp/build_test_report.py          # dựng lại báo cáo PDF
python tmp/pdfs/review/netlist_review.py # trích netlist từ PDF bản vẽ
```

---

## 5. Bẫy đã gặp — đừng mắc lại

* **Font trong PDF bản vẽ bị map sai.** Lớp text ghi `vih.1a=` nhưng render ra
  **`ВЫХ.1А=`**. Bảng đổi: `v→В  i→Ы  h→Х  a→А  b→Б`. Hậu tố `=` là đầu vào DC,
  `==` là đầu ra 400 Hz.
* **Trích netlist theo màu nét vẽ:** dây = `stroking_color (0.502, 0, 0.251)`
  (nâu đỏ) · chân linh kiện = `(1, 0, 0)` · **điểm nối = magenta `(1,0,1)` và là
  `curves`, không phải `lines`** · ký hiệu linh kiện = `(0,0,1)`.
* **Chân 4 và 11 của mọi vỏ 168КТ2 đều không nối** (chân 11 là подложка/đế —
  để thả nổi). Đồ gá test không cần cấp nguồn cho đế.
* `f_гр` của NPN (120 MHz) và PNP (5 MHz) lệch 24 lần ⇒ **sườn xuống mềm hơn
  sườn lên là bình thường**, không phải lỗi.
* RMS toàn sóng ≠ RMS thành phần cơ bản. Ở `Vin = 4 V`: toàn sóng 3,752 V,
  cơ bản 3,520 V<sub>rms</sub>. Hệ số cơ bản = **1,2446 × Vin**.
