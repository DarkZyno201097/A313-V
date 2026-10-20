# NHIỆM VỤ CHO CODEX — PHẢN BIỆN ĐỘC LẬP TÀI LIỆU PHÂN TÍCH A313-V.06

## 0. VAI TRÒ

Bạn là **kỹ sư phản biện độc lập** (adversarial reviewer) chuyên về mạch tương tự và reverse-engineering
mạch avionics đời cũ. Nhiệm vụ của bạn **KHÔNG phải** là tóm tắt hay khen tài liệu, mà là **tìm cho ra chỗ sai**.

Một tài liệu phân tích đã được lập sẵn (bởi một AI khác) từ bản vẽ thiết kế. Nó **có thể sai ở bất kỳ chỗ nào**.
Hãy mặc định **không tin** nó, và tự dựng lại kết luận từ bản vẽ gốc.

**Tiêu chí thành công:** tìm được ít nhất một lỗi thực sự, hoặc chứng minh được từng khẳng định rủi ro cao là đúng
kèm bằng chứng cụ thể (toạ độ, đoạn dây, số hiệu chân). Trả lời "tài liệu có vẻ ổn" mà không có bằng chứng
= thất bại.

---

## 1. FILE VÀ ĐƯỜNG DẪN

Thư mục gốc:

```
E:\Alitum\Tự học Altium\Projects\MODULE\HUAN LUYEN KTSD, CHUYEN GIAO CONG NGHE SC, SX CHO A32_2026\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\
```

| File | Nội dung | Vai trò |
|---|---|---|
| `BVTK-A313-V.06.pdf` | **4 trang A3** — chính là trang 28–31 của bộ bản vẽ | **NGUỒN SỰ THẬT SỐ 1** |
| `PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md` | Tài liệu cần phản biện (Rev. B) | Đối tượng kiểm tra |
| `Datasheet\00_TONG-QUAN_linh-kien-chinh_A313-V.md` | Tổng quan linh kiện | Kiểm tra tính nhất quán |
| `Datasheet\01_168KT2B_168KT2V_khoa-tuong-tu-4-kenh.md` | Datasheet khoá tương tự | Kiểm tra tính nhất quán |
| `Datasheet\02_140UD1B_khuech-dai-thuat-toan.md` | Datasheet KĐTT | Kiểm tra tính nhất quán |
| `Datasheet\03_2T312B_transistor-NPN.md` | Datasheet NPN | Kiểm tra tính nhất quán |
| `Datasheet\04_2T203B_transistor-PNP.md` | Datasheet PNP | Kiểm tra tính nhất quán |
| `1.BVTK A313-V\BVTK-A313-V_HS dau A.pdf` | Toàn bộ 56 trang | Tra cứu khi cần bối cảnh |
| `3.HDSD A313-V\HDSD-A313-V_HS dau A.pdf` | Hướng dẫn sử dụng, mục 3.2.4 | Đối chiếu chức năng hệ thống |
| `2.DKKT A313-V\DKKT-A313-V_HS dau A.pdf` | Điều kiện kỹ thuật, Phụ lục B | Đối chiếu chỉ tiêu |

**Nội dung 4 trang của `BVTK-A313-V.06.pdf`:**

| Trang | Ký hiệu | Nội dung |
|---|---|---|
| 1 | 07MB.A313-V.BV.22 | **Sơ đồ nguyên lý** cụm khuếch đại tín hiệu ra |
| 2 | 07MB.A313-V.BV.23 | Sơ đồ mạch in **mặt trên** |
| 3 | 07MB.A313-V.BV.24 | Sơ đồ mạch in **mặt dưới** |
| 4 | 07MB.A313-V.BV.25 | **Thống kê linh kiện** (BOM) |

---

## 2. CÁCH ĐỌC BẢN VẼ BẰNG CHƯƠNG TRÌNH (đọc kỹ — đây là phần tiết kiệm nhất cho bạn)

Bản vẽ là **PDF vector do Altium xuất qua Word**, không phải ảnh scan. Đừng cố đọc bằng mắt qua ảnh render
độ phân giải thấp — hãy **dựng lại netlist bằng chương trình**, rồi mới kiểm chứng bằng ảnh crop ở chỗ nghi ngờ.

### 2.1. Quy ước màu trong file (quan trọng nhất)

| Màu `stroking_color` | Ý nghĩa |
|---|---|
| `(0.502, 0.0, 0.251)` — nâu đỏ sẫm | **Dây nối (wire)** |
| `(1.0, 0.0, 0.0)` — đỏ | **Đoạn chân linh kiện (pin stub)** và **nhãn net** |
| `(1.0, 0.0, 1.0)` — magenta | **Chấm nối (junction dot)** — vẽ bằng `curves`, không phải `lines` |
| `(0.0, 0.0, 1.0)` — xanh dương | **Ký hiệu linh kiện** (điện trở, tụ, IC, transistor) — KHÔNG phải dây |
| Đen | Khung bản vẽ, số hiệu chân, khung khối |

### 2.2. Thuật toán dựng netlist đã dùng (bạn nên làm lại độc lập)

```python
import pdfplumber, collections
pdf = pdfplumber.open("BVTK-A313-V.06.pdf")
p = pdf.pages[0]                      # trang 1 = BV.22
# 1. Lấy mọi đoạn thẳng màu nâu-đỏ và đỏ  -> ~4400 đoạn
# 2. Snap 2 đầu mỗi đoạn về lưới 0.3 pt, union-find theo đầu chung
# 3. Với mỗi junction dot (curve magenta): nối mọi đoạn đi qua điểm đó
# 4. Với mỗi đầu mút nằm trên thân một đoạn khác (T-junction): nối
# 5. Gán nhãn: mỗi word của extract_words() -> net gần nhất (< 6 pt)
```

Kết quả tham chiếu (nếu bạn ra khác thì **một trong hai bên sai — phải điều tra**):
`~4422 đoạn dây`, `250 junction dot`, `~635 net`.

### 2.3. Bẫy đã gặp — cảnh báo trước

1. **Text bị vỡ vụn.** `extract_words()` trả về `'R'`,`'8'`,`'6'` riêng lẻ. Phải gom `chars` theo baseline
   (cùng `top` ±0,45 pt, khoảng cách `x0 - x1_trước` < 1,0 pt) mới ra `"R86"`.
2. **Font Cyrillic bị ánh xạ sai.** `vih.1a=` trên text layer thực tế hiển thị là **`ВЫХ.1А=`**.
   `v→В`, `i→Ы`, `h→Х`, `a→А`, `b→Б`. Phải render ảnh để đọc đúng.
3. **Nhãn net lệch trái so với chân cắm ~3,9 pt.** Khi ánh xạ nhãn `ВЫХ.n=` sang chân đầu nối,
   phải cộng bù, nếu không sẽ lệch 1 chân. **Đây là chỗ rất dễ sai — hãy kiểm tra lại độc lập.**
4. **Dây cắt nhau KHÔNG nối** nếu không có junction dot. Thuật toán union-find theo đầu mút xử lý đúng,
   nhưng bước 4 (T-junction) có thể **nối nhầm** 2 net khác nhau. Trong lần phân tích trước, bước này
   đã nối nhầm net `М` và `М̄` ở khu vực U18 — phải kiểm tra bằng mắt ở mọi chỗ kết luận quan trọng.
5. **Render ảnh để kiểm chứng:** `pdftoppm -f 1 -l 1 -r 400 -png` cho ra ảnh 6615×4678,
   crop vùng nghi ngờ rồi phóng to. Đây là cách kiểm chứng cuối cùng, đáng tin hơn thuật toán.

---

## 3. RÀNG BUỘC — NHỮNG ĐIỀU ĐÃ CHỐT, KHÔNG ĐƯỢC "SỬA NGƯỢC"

6 điểm dưới đây **đã được kỹ sư khai thác xác nhận trên mạch thật**. Bản vẽ ghi sai, thực tế đúng như sau.
**Không được kết luận ngược lại chỉ vì bản vẽ ghi khác** — nhưng **được phép chỉ ra nếu chúng mâu thuẫn với
phần còn lại của mạch**, và phải nêu rõ mâu thuẫn đó.

| # | Kết luận đã chốt |
|---|---|
| 1 | **R24 = 2,05 kΩ** (bản vẽ ghi "2,050Mom" / "2,05ΩM" là sai đơn vị) |
| 2 | Điện trở **0 Ω** nối tiếp lối vào `~5V/400Hz` của U14 có ký hiệu đúng là **R124** (bản vẽ ghi nhầm `R63`). `R63` chỉ là điện trở ra 180 Ω của kênh 5а |
| 3 | Sai số học ở cột "Số lượng" bảng BV.25: **bỏ qua**, lấy sơ đồ nguyên lý BV.22 làm gốc |
| 4 | BOM đếm theo *section* thay vì theo *vỏ*: số vỏ đúng là **12 × 168КТ2Б, 3 × 168КТ2В, 18 × 140УД1Б** |
| 5 | **Chân 4 và chân 11 của 168КТ2 thực tế KHÔNG được nối** trên tấm mạch (chân 11 = подложка, để thả nổi) |
| 6 | **+5 V và +6,3 V** (DC11) **không dùng** trên tấm này |

---

## 4. DANH SÁCH KHẲNG ĐỊNH PHẢI KIỂM CHỨNG (xếp theo mức rủi ro)

Với **mỗi** mục dưới đây, đưa ra kết luận: **[XÁC MINH]** / **[BÁC BỎ]** / **[SỬA LẠI]** / **[KHÔNG ĐỦ DỮ LIỆU]**,
kèm **bằng chứng cụ thể** (toạ độ trên trang, số hiệu chân, ảnh crop, hoặc kết quả netlist).

### 4.1. RỦI RO CAO — bắt buộc kiểm tra kỹ nhất

| # | Khẳng định trong tài liệu | Vì sao rủi ro |
|---|---|---|
| **A1** | **R38 (56 Ω) nối tiếp C2 (0,01 µF) tạo mạng коррекция từ chân 12 của U19 xuống MÁT.** R38 **KHÔNG** nằm trong đường lái base của Q1/Q2 | Trong lần phân tích trước, kết luận này **đã bị sửa giữa chừng** — ban đầu hiểu nhầm R38 nằm giữa chân 12 và nút ra. Rất dễ sai. Kiểm tra kỹ có/không có junction dot tại giao điểm của đường đứng từ R38 và đường ngang từ chân 5 |
| **A2** | **Chân 5 (ra) của U19 nối THẲNG vào base chung của Q1 và Q2.** Emitơ Q1+Q2 chập nhau = "nút Y" → R39 180 Ω → đầu ra | Quyết định toàn bộ cách hiểu tầng ra |
| **A3** | **Hồi tiếp R86 và C1 lấy tín hiệu SAU R39** (tại chân ra), không phải trước R39 | Ảnh hưởng trực tiếp tới trở kháng ra và cách đọc dạng sóng khi test |
| **A4** | **Net nhãn `a` = MÁT (корпус).** Mọi nhãn `a` trên trang 1 (cạnh C1, C2, C3, C4, chân 4 U19, chân 1 U1A, rail trên của khối lọc nguồn, đầu nối DC11/DC12) đều là **cùng một net = GND** | Nếu sai, toàn bộ cách hiểu bộ điều chế ±1 sụp đổ |
| **A5** | **U1A là khoá SHUNT nối nút S xuống mát** (điều khiển bằng М); **U2B là khoá NỐI TIẾP** đưa V_in vào nút S; **U2A + R4 10 kΩ** là nhánh **cân bằng tải** (V_in → R4 → mát) | Đây là "trái tim" của kết luận điều chế ±1 |
| **A6** | Kênh có **hệ số +1 ở pha này và −1 ở pha kia**, ra sóng vuông ±V_in 400 Hz | Kết luận trung tâm của cả tài liệu |
| **A7** | **Khoá 168КТ2 DẪN khi chân затвор ở −23 V, HỞ khi ở +3,5 V** | Nếu ngược, bảng pha ở §6.2 đảo hết |
| **A8** | **Nút N_ref (ngưỡng hysteresis) là chân 10 của CẢ U14 lẫn U15** (chung một nút) | Nếu là 2 nút riêng thì toàn bộ tính toán ngưỡng ở §5.2 sai |

### 4.2. RỦI RO TRUNG BÌNH

| # | Khẳng định |
|---|---|
| B1 | Bảng chân **DC11** ở §2.1 (GND / +5V / +3,5V / +6,3V / ~5V400Hz / xung400Hz / М / М̄ theo cụm A_n,B_n,C_n) — **kiểm tra lại độ lệch nhãn ±1 chân** (bẫy §2.3-3) |
| B2 | Bảng chân **DC12** ở §2.2 — đặc biệt ánh xạ 16 chân vào (A7/C7/A8/C8/…/A14/C14) và 16 chân ra (A17/C17/…/A24/C24) |
| B3 | Bảng ánh xạ **16 kênh → linh kiện** ở §7 (16 dòng). Kiểm tra **toàn bộ 16 dòng**, không chỉ vài dòng mẫu. Công thức đã dùng: kênh thứ `n` (1…16) → `R(3+n)`, `R(83+2n)`/`R(84+2n)`, `R(34+3n)`, `R(35+3n)`, `R(36+3n)`, `U(18+n)`, `Q(2n−1)`/`Q(2n)`, tụ `C1/C2` với n=1 và `C(2n+1)`/`C(2n+2)` với n≥2 |
| B4 | Bảng **chia sẻ vỏ khoá** ở §7.1 (U1/U4/U7/U10 cho khoá shunt; U2/U3/U5/U6/U8/U9/U11/U12 cho khoá nối tiếp) — lưu ý thứ tự U8/U9 **không** theo quy luật, dễ chép sai |
| B5 | Bản đồ **tụ lọc nguồn** §4: C35–C38 + C44 (3300 pF) và C39, C46 (4,7 µF) và C45 (22 µF) trên +12,6 V; C43 + C40, C42 trên −12,6 V; **C41 nối chéo giữa +12,6 V và −12,6 V** |
| B6 | **U17B và U17C mắc SONG SONG**, cùng do nút A điều khiển, cùng kéo `xung400Hz` xuống mát |
| B7 | Số hiệu chân **140УД1Б**: 1 = −Uп, 4 = общий (MÁT), 5 = ra, 7 = +Uп, 9 = vào đảo, 10 = vào không đảo, 12 = коррекция. **Đặc biệt kiểm tra chân 4 = MÁT** — điều này khác hoàn toàn OA hiện đại |

### 4.3. KIỂM TRA SỐ HỌC (tính lại độc lập, đừng chép)

| # | Số liệu trong tài liệu | Công thức |
|---|---|---|
| C1 | Hệ số chia U14 = **0,1034** | `301/(2610+301)` |
| C2 | Hệ số chia U15 = **0,1280** | `301/(2050+301)` |
| C3 | Ngưỡng hysteresis = **±0,3511 V** | `12,6 × 301/(10500+301)` |
| C4 | Ngưỡng quy đầu vào: U14 = **±3,396 V**, U15 = **±2,743 V** | C3 chia C1, C2 |
| C5 | Góc trễ sườn xung: 28,7°/22,8° (chuẩn 5 Vrms); 42,8°/33,3° (chuẩn 5 V đỉnh); **Δ = 5,9° ≈ 41 µs** hoặc **9,5° ≈ 66 µs** | `arcsin(U_ngưỡng/U_đỉnh)` |
| C6 | Hằng số thời gian vo tròn sườn xung **τ = 100 µs** (R86 ∥ C1), f_c ≈ 1,6 kHz | `10 kΩ × 0,01 µF` |
| C7 | Mạng коррекция **τ = 0,56 µs**, f ≈ 284 kHz | `56 Ω × 0,01 µF` |
| C8 | Dòng ngắn mạch đầu ra **≈ 66 mA** | `(12,6 − 0,7)/180` |
| C9 | Lệch không do dòng vào nếu bỏ R37 ≈ **45 mV** | `9 µA × (10k ∥ 10k)` |
| C10 | Tải tối thiểu **≥ 400 Ω** | `4 V / 10 mA` (giới hạn I_к của 2Т203Б) |
| C11 | Kiểm tra chéo số lượng: 12 vỏ × 4 khoá = 48 = 16 kênh × 3 khoá; 18 KĐTT = 16 + 2; 32 transistor = 16 × 2; 34 tụ 0,01 µF = 16×2 + 2 | — |

### 4.4. KIỂM TRA TÍNH KHẢ THI CỦA QUY TRÌNH TEST (§10)

| # | Nội dung cần phản biện |
|---|---|
| D1 | **§10.4 — "đóng băng pha điều chế" bằng cách cấp +5 V DC / −5 V DC vào chân `~5V/400Hz` (DC11 A5/B5/C5).** Bài test này có thực sự chạy được không? Với DC vào, U14/U15 có chốt trạng thái ổn định không, hay dao động? Mạng hysteresis U16 lúc đó ở trạng thái nào? Có rủi ro hỏng gì không? **Đây là bài test được đề xuất làm trọng tâm của ATE — nếu nó sai thì cả quy trình sai.** |
| D2 | Các ngưỡng đánh giá ở §10.4 (sai số +1 ≤ 0,3 %, sai số −1 ≤ 1 %, mất đối xứng ≤ 1 %, lệch không ≤ 50 mV) — có hợp lý với dung sai linh kiện (điện trở 1 %, U_см ≤ 7 mV của 140УД1Б) không? Tính lại giới hạn lý thuyết |
| D3 | Chuỗi điểm đo TP1–TP8 ở §10.6 — dạng sóng mong đợi ở mỗi điểm có đúng với topo mạch không? Đặc biệt **TP8 (chân 12 U19)**: nếu A1 đúng thì chân 12 chỉ có mạng RC xuống mát — dạng sóng mô tả trong tài liệu có hợp lý không? |
| D4 | Bảng chẩn đoán §10.7 — có triệu chứng nào **không thể xảy ra** theo topo mạch, hoặc bị gán nhầm nguyên nhân không? |
| D5 | Ước lượng dòng tiêu thụ ±12,6 V ≈ 100–200 mA (18 × 140УД1Б) — kiểm tra lại với I_пот ≤ 10 mA/con, có tính dòng tầng đệm không? |

### 4.5. PHÂN BIỆT SỰ KIỆN VỚI SUY DIỄN

Tài liệu có một số chỗ là **suy đoán về ý đồ thiết kế**, không phải sự kiện đọc được từ bản vẽ.
Hãy **đánh dấu rõ** những chỗ này và đánh giá độ thuyết phục:

* "R4 dùng để **cân bằng tải** cho nguồn S&H trên A313-V.05, tránh làm 'răng cưa' mức giữ"
* "Hàng B của đầu nối bỏ trống để **chống xuyên nhiễu** giữa 2 kênh liền kề"
* "C1 vo tròn sườn xung để **giảm sóng hài bơm vào СКТ**"
* "R39 180 Ω để **hạn dòng ngắn mạch và cách ly tải dung**"
* "Hai nhánh U14/U15 **cố ý** khác hệ số chia để tạo lệch pha"
* "168КТ2**Б** dùng cho kênh tín hiệu (U_сп 15 V) còn 168КТ2**В** dùng cho cụm tạo xung (U_сп 25 V) vì biên độ chuyển mạch tới 26,5 V"

---

## 5. NHỮNG THỨ **KHÔNG THỂ** KẾT LUẬN TỪ BẢN VẼ

Đừng bịa. Các mục sau chỉ có thể xác định bằng **đo trên mạch thật** — nếu bạn gặp, hãy giữ nguyên trạng thái "còn treo":

1. Biên độ thực của chuẩn `~5V/400Hz` là **rms hay đỉnh** (quyết định góc trễ 28,7° hay 42,8°)
2. Trở kháng tải thực của biến thế sin-cos đấu vào đầu cắm 3Ш3
3. Giá trị thực tế của overlap М/М̄
4. "Chữ ký" tấm chuẩn (dòng tiêu thụ, G+/G−, lệch không thực tế)
5. Chiều điều khiển 168КТ2 — hiện **suy ra** từ datasheet (R_си.отк đo ở U_з = −15 V) + cấu trúc mạch,
   **chưa** đo trực tiếp

---

## 6. QUYỀN SỬA FILE

Bạn **ĐƯỢC PHÉP** sửa trực tiếp các file `.md` trong thư mục trên, theo cách bạn thấy dễ hiểu và dễ dùng hơn:
tái cấu trúc mục, đổi cách trình bày bảng, thêm sơ đồ ASCII, gộp/tách mục, viết lại câu cho gọn.

### Bắt buộc giữ

| # | Ràng buộc |
|---|---|
| 1 | **Tiếng Việt**, thuật ngữ Nga giữ nguyên dạng Cyrillic (`ВЫХ.1А=`, `коррекция`, `подложка`, `140УД1Б`…) |
| 2 | **Giữ nguyên tên file.** Không đổi tên, không tạo file trùng lặp |
| 3 | Giữ đủ nội dung của: bảng chân 2 đầu nối, bảng ánh xạ 16 kênh, bảng chia sẻ vỏ khoá, bảng BOM, quy trình test §10 (có thể trình bày lại, **không được bỏ**) |
| 4 | **Không sửa ngược 6 điểm đã chốt ở §3** của prompt này |
| 5 | Mọi số liệu đã sửa phải **nhất quán trên toàn bộ tài liệu** — sửa 1 chỗ phải rà hết các chỗ tham chiếu chéo (đây chính là loại lỗi cần tìm) |
| 6 | Nâng phiên bản lên **Rev. C** và ghi ngày |

### Bắt buộc thêm

Thêm một mục mới ở đầu tài liệu: **`## 0. NHẬT KÝ PHẢN BIỆN (Rev. C)`** với bảng:

| Mã | Khẳng định | Kết luận | Bằng chứng | Đã sửa ở mục |
|---|---|---|---|---|
| A1 | R38+C2 là mạng коррекция xuống mát | [XÁC MINH] / [BÁC BỎ] / … | *toạ độ, chân, mô tả* | §6.1, §6.3, §10.6 |
| … | | | | |

Liệt kê **toàn bộ** mã A1–A8, B1–B7, C1–C11, D1–D5 và các mục §4.5 — **không được bỏ sót mã nào**.

---

## 7. ĐỊNH DẠNG BÁO CÁO CUỐI

Sau khi sửa file, in ra màn hình một báo cáo ngắn gồm:

1. **LỖI THỰC SỰ TÌM ĐƯỢC** — danh sách, mỗi lỗi 1 dòng: *mã | mô tả | mức nghiêm trọng (Nghiêm trọng / Trung bình / Nhỏ) | đã sửa ở đâu*
2. **KHẲNG ĐỊNH ĐÃ XÁC MINH** — chỉ liệt kê mã, không giải thích dài
3. **KHÔNG ĐỦ DỮ LIỆU** — mã + cần đo gì trên mạch thật
4. **BẤT ĐỒNG QUAN ĐIỂM** — chỗ bạn nghĩ khác nhưng chưa đủ chắc để sửa
5. **DANH SÁCH FILE ĐÃ SỬA**

Nếu bạn **không tìm được lỗi nào**, hãy nói thẳng và nêu rõ **bạn đã kiểm tra A1–A8 bằng cách nào** — kèm
bằng chứng cho ít nhất 3 mục rủi ro cao.

---

## 8. THỨ TỰ LÀM VIỆC ĐỀ XUẤT

```
1. Đọc PHAN-TICH_...md một lượt để nắm khẳng định  (KHÔNG tin, chỉ để biết cần kiểm gì)
2. Dựng netlist trang 1 bằng chương trình (§2.2)
3. Kiểm A1–A8 bằng netlist + ảnh crop 400 dpi       ← dành nhiều thời gian nhất ở đây
4. Kiểm B1–B7
5. Tính lại C1–C11
6. Phản biện D1–D5 (lý thuyết mạch, không cần bản vẽ)
7. Rà mục 4.5 — tách sự kiện khỏi suy diễn
8. Sửa file + viết §0 Nhật ký phản biện
9. Rà tính nhất quán chéo lần cuối (grep các số liệu đã sửa trên TẤT CẢ 6 file .md)
10. In báo cáo §7
```

**Bắt đầu ngay từ bước 2. Đừng hỏi lại xin phép.**
