# PHÂN TÍCH CHỨC NĂNG & QUY TRÌNH KIỂM TRA
# CỤM KHUẾCH ĐẠI TÍN HIỆU RA — A313-V.06

**Nguồn tài liệu:** `BVTK-A313-V_HS dau A.pdf` tr. 28–31
(07MB.A313-V.BV.22 — sơ đồ nguyên lý; .BV.23/.BV.24 — mạch in mặt trên/dưới; .BV.25 — thống kê linh kiện),
đối chiếu `HDSD-A313-V` mục 3.2.4 và `DKKT-A313-V` Phụ lục B.

**Thông số cơ khí:** mạch in 218 × 130 mm (bao cả tai gá: 230 × 157 mm), dày 2 mm, 2 đầu nối cạnh DC96c (DC11, DC12).

**Phiên bản:** Rev. C — 16/09/2026. Phản biện độc lập và sửa topo U16, pha, sai số và quy trình test. Rev. B trước đó đã đối chiếu với người thiết kế/khai thác và chốt 6 điểm nghi vấn của Rev. A (chi tiết §9).
Tóm tắt thay đổi so với Rev. A:

| # | Nội dung Rev. A | Kết luận Rev. B |
|---|---|---|
| 9.1 | R24 ghi "2,050 MOm", nghi sai | **Xác nhận: R24 = 2,05 kΩ.** Bản vẽ ghi sai đơn vị |
| 9.2 | Trùng ký hiệu R63 | **Xác nhận: ký hiệu đúng là R124** (điện trở 0 Ω lối vào U14). R63 chỉ thuộc kênh 5а |
| 9.3 | Sai số lượng nhóm 8 bảng BV.25 | Không quan trọng — **lấy theo sơ đồ nguyên lý BV.22** |
| 9.4 | Nhóm 22 đếm theo section | **Xác nhận là lỗi xuất BOM** |
| 9.5 | Chân 4 và 11 của 168КТ2 | **Xác nhận: thực tế KHÔNG dùng, không nối** |
| 9.6 | +5 V và +6,3 V không dùng | **Xác nhận** |

---

## 0. NHẬT KÝ PHẢN BIỆN (Rev. C)

**Ngày: 16/09/2026.** Phản biện độc lập từ BV.22, bắt đầu bằng dựng kết nối vector, sau đó kiểm ảnh 400 dpi. Không thực hiện phép đo trên phần cứng. Sáu kết luận khai thác tại §9 được giữ nguyên. `[XÁC MINH]` về topo nghĩa là xác minh trên bản vẽ; không thay thế kiểm tra trên mạch thật. Các giá trị lý tưởng luôn tách khỏi giới hạn nghiệm thu.

**Quy ước bằng chứng:** tọa độ `(x,y)` tính bằng pt từ góc trên trái trang 1, khổ 1190,64 × 842,04 pt. Ảnh: [kênh 1а](tmp/pdfs/review/channel1.png), [U14–U18](tmp/pdfs/review/generator.png), [lọc nguồn](tmp/pdfs/review/power.png), [DC11](tmp/pdfs/review/DC11.png), [DC12](tmp/pdfs/review/DC12.png). Bằng chứng số: [net hình học](tmp/pdfs/review/netlist.json), [tọa độ chữ](tmp/pdfs/review/text-coordinates.txt), [kiểm đủ 16 dòng](tmp/pdfs/review/channel-audit.csv), [tính toán](tmp/pdfs/review/calculations.json). `netlist_review.py` và `review_checks.py` cùng thư mục tái tạo kết quả và chạy các assertion về nút, kênh, trạng thái DC và số học.

| Mã | Khẳng định | Kết luận | Bằng chứng | Đã sửa ở mục |
|---|---|---|---|---|
| A1 | R38+C2 là mạng коррекция xuống mát | [XÁC MINH] | Chân 12 đi lên rồi sang R38; giao `(344,82)` với đường chân 5 không có chấm; chấm base ở `(347,7;81,8)` riêng biệt. C2 đầu dưới mang nhãn a. | §6.1, §6.3, §10.6 |
| A2 | Chân 5 lái base chung; emitơ chung qua R39 | [XÁC MINH] | Net hình học 2062: U19.5/base; net 2079: hai emitơ/R39 trái, chấm `(361,7;81,8)`; colector về ±12,6 V. | §6.1 |
| A3 | R86 và C1 hồi tiếp sau R39 | [XÁC MINH] | Net 2091: đầu phải R39, hai dây hồi tiếp lên trên, chấm `(393,3;81,8)`; khác net 2079 trước R39. | §6.1, §6.3 |
| A4 | Nhãn a là GND | [XÁC MINH] | a ở DC11 `(1134,7;392,7)`, DC12 `(1127,7;468,0)` cùng thanh nối ký hiệu корпус; a của 16 shunt, chân 4 và tụ коррекция lặp lại. C1 KHÔNG nối mát: đường chân 4 cắt đường C1 không chấm. | §0.1, §6.1 |
| A5 | U1A shunt, U2B nối tiếp, U2A–R4 tải phụ | [XÁC MINH] | U1A.3 = S; U1A.1 = a; U2B.5 = Vin, .7 = S; U2A.3 = Vin, .1 → R4 → a, vùng `(80…260,80…110)`. Ý đồ cân bằng tải xem E1. | §6.1, §6.3 |
| A6 | Hệ số +1/−1 | [XÁC MINH] | KCL: Vo=(1+k)S−kVin; S=Vin hoặc 0, k=R86/R85=1 danh định. Đây là mức xác lập; chuyển tiếp không phải bộ lọc thông thấp đơn giản. | §6.2–6.3 |
| A7 | Gate −23 V dẫn, +3,5 V ngắt | [KHÔNG ĐỦ DỮ LIỆU] | Datasheet gốc 168kt2.pdf tr. 2 đo Ron với gate −15 V, đế +5 V; phù hợp suy luận gate âm dẫn. Đế tấm này thả nổi; chưa đo xác nhận hai mức trên toàn dải ±4 V. | §5.3, §12.2 |
| A8 | U14.10 và U15.10 chung N_ref | [BÁC BỎ] | Net 2097: U14.10 `(934,1;175,5)` ↔ U16A.3/U16B.5. Net 1872: U15.10 `(934,1;299,1)` ↔ U16C.10/U16D.12. Hai dây dọc x=916,6 tách bởi khoảng y=214,7…253,9. | §3, §5.2, §10.5 |
| B1 | Bảng chân DC11 | [XÁC MINH] | Crop DC11: theo dây đứng tới số chân, A/B/C1…8 đúng; X từ 9…30; GND 31…32. Không gán theo tâm chữ. | §2.1 |
| B2 | Bảng chân DC12 | [XÁC MINH] | Crop DC12: cả 32 dây tín hiệu khớp A/C7…14 và A/C17…24; nhãn xoay nằm bên trái dây. GND 30…32. | §2.2 |
| B3 | Toàn bộ 16 dòng ánh xạ kênh | [XÁC MINH] | 16/16 dòng CSV PASS; đối chiếu 8 crop ch-0/1-0/2/4/6, không chỉ suy từ công thức. Vị trí từng dòng có trong §0.1. | §7 giữ đủ bảng |
| B4 | Chia sẻ vỏ khoá, thứ tự U8/U9 | [XÁC MINH] | U27 tại `(656,7;70,5)` dùng U9A/B; U28 `(656,7;142,8)` dùng U8A/B; U29 dùng U9C/D; U30 dùng U8C/D. Các nhóm còn lại đúng. | §7.1 |
| B5 | Phân bố C35…C46, C41 nối chéo | [XÁC MINH] | Crop nguồn `(866…1022,38…110)`: C41 trên rail +12,6, dưới rail −12,6; C40 từ a tới −12,6; C42 từ −12,6 tới корпус. Các tụ còn lại khớp §4. | §4 |
| B6 | U17B/C song song | [XÁC MINH] | U17B.5/U17C.10 = xung400Hz; .7/.8 = GND; .6/.9 = A, vùng `(1020…1125,202…258)`. | §5.3 |
| B7 | Pinout 140УД1Б, chân 4 là общий | [XÁC MINH] | Datasheet gốc 140ud1B.pdf tr. 1, bảng chân; BV.22 U19.4 có nhãn a. 12 ghi контрольный; vai trò коррекция được chứng minh bởi mạch ngoài. | §5.1; datasheet 02 |
| C1 | Hệ số chia U14 0,1034 | [XÁC MINH] | 301/2911=0,103400893; R124/R117=0 Ω. | §5.1 |
| C2 | Hệ số chia U15 0,1280 | [XÁC MINH] | 301/2351=0,128030625; R24=2,05 kΩ theo xác nhận thực tế. | §5.1 |
| C3 | Ngưỡng 0,3511 V | [SỬA LẠI] | 12,6×301/10801=0,351134 V đúng; là hai nguồn chia áp rồi chọn ra H14/H15 đối dấu, không phải một nút chung. | §5.2 |
| C4 | Ngưỡng quy đầu vào 3,396/2,743 V | [XÁC MINH] | Trị tuyệt đối 3,395852/2,742579 V trong mô hình danh định không tải; dấu/ngữ cảnh chuyển mạch xem §5.2. | §5.2 |
| C5 | Cả hai trễ; Δ=5,9°/9,5° | [BÁC BỎ] | H14/H15 đối dấu: U15 chuyển TRƯỚC zero, U14 chuyển SAU zero; phải CỘNG góc: 51,5228°/76,0441° = 357,797/528,084 µs. | §5.2, §10.5, §12 |
| C6 | RC 100 µs mô tả toàn bộ sườn ra | [SỬA LẠI] | RC=100 µs, fc=1591,55 Hz đúng. Vo=[(2+sτ)/(1+sτ)]S−Vin/(1+sτ); đường truyền trực tiếp từ S tạo bước tức thời trong mô hình lý tưởng. | §6.3, §10.6 |
| C7 | RC коррекция 0,56 µs, 284 kHz | [SỬA LẠI] | Tích RC=0,56 µs và 1/(2 π RC)=284205 Hz đúng; không đủ suy ra cực vòng kín/băng thông hay biên độ chân 12. | §6.3, §10.6 |
| C8 | Dòng ngắn mạch ≈66 mA | [SỬA LẠI] | 11,9/180=66,111 mA chỉ là mô hình base lên tới rail; thực tế phụ thuộc swing OA, β, tải và giới hạn dòng. R39 không phải bảo vệ ngắn mạch. | §6.3, §11; datasheet 00/03/04 |
| C9 | Bỏ R37 gây lệch đầu ra 45 mV | [BÁC BỎ] | 9 µA×5 kΩ=45 mV quy đầu vào; noise gain=2 → đầu ra tới 90 mV do riêng Ib−. Không áp dụng cho R37 đứt hở. | §6.3, §10.4; datasheet 02 |
| C10 | Tải ≥400 Ω là đủ | [SỬA LẠI] | 4/10 mA=400 Ω chưa tính dòng hồi tiếp tới 0,4 mA và headroom trên 180 Ω; giới hạn bảo thủ dòng emitơ cho tải thuần trở >417 Ω, vẫn chưa đủ bảo đảm swing/ổn định. | §10.6, §12.2; datasheet 00/04 |
| C11 | Số lượng vỏ/khoá/OA/Q/tụ | [XÁC MINH] | 12×4=48=16×3; 18=16+2; 32=16×2; 34=16×2+2. Giữ nguyên sửa BOM đã chốt. | §8 |
| D1 | Đóng băng bằng ±5 V DC | [SỬA LẠI] | Mô hình topo cho trạng thái duy nhất ổn định: +5 → H14 âm/H15 dương → M cao → G+; −5 đảo lại. Không có cơ chế bắt buộc tự dao động. Chỉ đưa vào ATE sau xác nhận thực, xem §10.4. | §10.3–10.4, §11 |
| D2 | Ngưỡng +0,3%/−1%/đối xứng 1%/offset 50 mV | [BÁC BỎ] | Hai R1% cho tỉ số 0,980198…1,020202; Vos×2 tới 14 mV đã vượt 12 mV tại 4 V; offset bảo thủ khoảng 49,8 mV theo giả thiết 9 µA/2,5 µA, chưa tính mọi lỗi. | §10.4; datasheet 02 |
| D3 | Dạng sóng TP1–TP8 | [SỬA LẠI] | TP3 sụt Ib×4,7k có thể 42,3 mV; TP5=Y±VBE khi Q dẫn; Y=Vo+180I; TP8 không đủ mô hình nội để dự đoán biên độ. RMS fundamental ≠ peak. | §10.6; datasheet 03 |
| D4 | Chẩn đoán hỏng khoá/R/Q | [SỬA LẠI] | Khoá hở để S nổi không bắt buộc DC ±Vin; Rfb hở thường bão hòa, Rin hở vẫn truyền S. R24=2,05 MΩ vẫn có thể làm U15 lật theo H15 đổi dấu. | §9.1, §10.7, §11 |
| D5 | Dòng nguồn 100–200 mA | [SỬA LẠI] | 18×10 mA=180 mA chỉ giả thiết dòng IC; tài liệu gốc 140ud1B.pdf tr. 2 ghi 12 mA ở ±13,9 V → 216 mA; còn dòng Q/tải/hồi tiếp. Chưa biết biến thể/lô thực. | §5.1, §10.3; datasheet 02 |
| E1 | R4 cân bằng tải, tránh răng cưa S&H | [SỬA LẠI] | Tải pha + là R4+Ron, pha − là Rin; cân bằng gần đúng có cơ sở KCL. Mục tiêu thiết kế và hiệu quả trên .05 là suy luận, không chứng minh chỉ từ BV.22. | §6.3 |
| E2 | Hàng B trống để chống xuyên nhiễu | [KHÔNG ĐỦ DỮ LIỆU] | B7…14/B17…24 thực sự bỏ trống, nhưng không có thuyết minh ý đồ hay đo xuyên nhiễu; cần hồ sơ thiết kế/đo với đồ gá. | §2.2 |
| E3 | C1 giảm sóng hài vào СКТ | [SỬA LẠI] | Giảm thành phần cao tần của nhánh hồi tiếp là suy luận hợp lý; có đường truyền trực tiếp S nên không triệt sườn hoàn toàn; mục đích với СКТ chưa được chứng minh. | §6.3 |
| E4 | R39 hạn dòng, cách ly tải dung | [SỬA LẠI] | Điện trở nối tiếp hạn chế dòng/cách ly tức thời; hồi tiếp sau R39 giảm tác dụng điện trở ra ở tần số thấp, không làm nó bằng 0 và không bảo đảm ổn định tải dung. | §6.3 |
| E5 | Hai hệ số chia khác nhau cố ý tạo lệch pha | [SỬA LẠI] | Khác trị số là sự kiện; lệch pha còn do H14/H15 đối dấu. Ngay cả chia áp bằng nhau vẫn có khoảng sớm–trễ; ý đồ “cố ý” cần hồ sơ thiết kế. | §5.1–5.2 |
| E6 | Chọn Б 15 V/В 25 V vì swing 26,5 V | [BÁC BỎ] | Datasheet 168kt2.pdf tr. 3 định mức điện áp so với подложка, không phải Vpp giữa drain/source. Đế đang thả nổi: không suy được biên an toàn 30−26,5=3,5 V. | §5.3; datasheet 00/01 |

### 0.1. Kết nối độc lập và giới hạn phương pháp

Đọc được đúng **4422 đối tượng line nâu/đỏ**, nhưng chỉ **2121 đoạn có chiều dài >0,05 pt**; nhiều đối tượng là điểm dài 0. Có **239 curve magenta**, không phải 250; không có rect magenta bổ sung. Ghép đầu đoạn theo khoảng cách ≤0,78 pt để vượt các khe xuất PDF khoảng 0,3…0,7 pt, nối tại chấm và rà 10 T-junction: **546 thành phần hình học**. Ngưỡng ≤0,43 pt cho 1038 thành phần vì bỏ sót nhiều khe. Vì vậy số “~635 net” không phải chuẩn đúng/sai; số này phụ thuộc snap, điểm suy biến và cách ghép nhãn. Không tự nối mọi giao cắt hay gán nhãn bằng chữ gần nhất. Net hình học chưa gộp nhãn a/nguồn/М lặp trên trang; số hiệu net chỉ phục vụ tái kiểm script này.

Các T-junction được ghi tọa độ trong JSON và đối chiếu crop: đều thuộc chân nguồn/корпус. М và М̄ tại y=290,070 và 293,085 vẫn khác net (1789/1532); giao dây R36 với М không có chấm. Ảnh quyết định những giao cắt quan trọng.

Netlist chức năng đã kiểm ảnh:

```text
VIN1 = U2A.3 = U2B.5 = R85 phía vào
GND(a) = U1A.1 = R4 phía trái = U19.4 = C2 phía dưới
S = U1A.3 = U2B.7 = R37 phía trái
U2A.1 -> R4 -> GND; S -> R37 -> U19.10
U19.9 = R85 phía phải = R86 phía dưới = C1 phía trái
U19.5 = Q1.B = Q2.B; Y = Q1.E = Q2.E = R39 phía trái
OUT1 = R39 phía phải = R86 phía trên = C1 phía phải
U19.12 -> R38 -> C2 -> GND   (tách khỏi U19.5)
Vref− = R22 phía phải = R23 phía phải = U16A.1 = U16C.8
Vref+ = R28 phía trái = R29 phía trái = U16B.7 = U16D.14
H14 = U14.10 = U16A.3 = U16B.5
H15 = U15.10 = U16C.10 = U16D.12
A = U17A.3 = U17D.13 = U17B.6 = U17C.9 = U16B.6 = U16C.9
B = U17D.12 = U16A.2 = U16D.13
```

Ranh giới kiểm 16 dòng: cột trái x ≈66…421, cột phải x ≈410…765; y đầu các dòng trái ≈43;115,3;187,7;260,0;332,3;404,7;477,0;549,4, dòng phải cộng ≈3,0 pt. Mỗi vùng cao 69 pt. CSV ghi đủ linh kiện quan sát được của từng kênh. Chữ PDF `Rr63` được kiểm ảnh là R63. Đọc số chân đầu nối theo dây đứng (bước chân ≈3,51 pt), không lấy chữ nhãn lệch trái làm vị trí chân.

**Nguồn linh kiện:** ưu tiên bản PDF gốc cục bộ `Datasheet/168kt2.pdf` tr.1–3 và `Datasheet/140ud1B.pdf` tr.1–2. Bản 140ud1B.pdf là nhãn dòng **140УД1БВК**, khác tập thông số sổ tay cũ trong Rev. B; chưa xác nhận đồng nhất lô IC trên tấm. Không thay mọi giới hạn cũ bằng thông số ВК như thể đã đo. Thông số Iк 10 mA của 2Т203Б được đối chiếu với [thẻ nhà sản xuất trên Optochip](https://optochip.org/series/card/129200); pinout/điều kiện thử khoá có trong [datasheet nhà sản xuất 168КТ2](https://eandc.ru/pdf/mikroskhema/168kt2.pdf).

---

## 1. VỊ TRÍ VÀ VAI TRÒ TRONG KHỐI A313-V

Chuỗi tín hiệu ra tương tự của máy tính dẫn đường:

```
Bộ nhớ A313-23V (ô 040₈–077₈)
      │  (UVV đọc ra)
      ▼
A313-V.04  Cụm biến đổi        → DAC, ra mức một chiều rời rạc
      ▼
A313-V.05  Cụm chuyển mạch ra  → 49 bộ nhớ tương tự (S&H), giữ mức DC từng kênh
      │    Вых.1а=…Вых.8б=  (16 mức DC, ±4 V)
      ▼
A313-V.06  ★ CỤM KHUẾCH ĐẠI TÍN HIỆU RA ★
      │    Вых.1а==…Вых.8б== (16 tín hiệu 400 Hz, biên độ ±4 V)
      ▼
Đầu cắm 3Ш3 → biến thế sin-cos (СКТ) của hệ thống ngoại vi
```

**Chức năng cốt lõi:** tấm mạch **KHÔNG phải là bộ khuếch đại công suất thuần tuý** như tên gọi gợi ý.
Nó là **16 bộ điều chế cân bằng (balanced modulator / chopper ±1) 400 Hz** cộng bộ tạo xung điều chế và tầng đệm dòng.

Mỗi kênh biến mức một chiều `U_DC` (từ S&H trên A313-V.05) thành tín hiệu xoay chiều 400 Hz **sóng mang bị nén (suppressed-carrier AM)**:

* Biên độ tỉ lệ `|U_DC|`
* **Pha 0° hay 180° mang dấu của `U_DC`** — đúng định dạng tín hiệu СКТ/sel-syn.

Đây chính là câu trong HDSD 3.2.4: *"…được đưa sang cụm khuếch đại tín hiệu ra A313-V.06 để điều chế tạo tín hiệu xoay chiều 400 Hz biên độ ±4 V"*.

---

## 2. GIAO DIỆN ĐIỆN — BẢNG CHÂN 2 ĐẦU NỐI

### 2.1. DC11 (DC96c) — nguồn phụ, chuẩn 400 Hz, xung điều chế

| Chân | Tín hiệu | Hướng | Ghi chú |
|---|---|---|---|
| A1, B1, C1 | **Корпус (GND, net "a")** | — | |
| A2, B2, C2 | **+5 V** | vào | **Không dùng trên tấm này** (chỉ có điểm đo) |
| A3, B3, C3 | **+3,5 V** | vào | Mức cao của tầng dịch mức; quy luật dẫn/ngắt cần xác nhận theo §5.3 |
| A4, B4, C4 | **+6,3 V** | vào | **Không dùng trên tấm này** (chỉ có điểm đo) |
| A5, B5, C5 | **~5 V / 400 Hz** | vào | Chuẩn pha 400 Hz cho toàn bộ tấm |
| A6, B6, C6 | **xung400Hz** | **ra** | Xung vuông 0 / +3,5 V, 400 Hz |
| A7, B7, C7 | **М** | **ra** | Xung điều chế, mức −23 V / +3,5 V |
| A8, B8, C8 | **М̄ (M_)** | **ra** | Đảo của М |
| A9 … C30 | Không nối (X) | — | 66 chân trống |
| A31…C32 | **GND** | — | 6 chân |

### 2.2. DC12 (DC96c) — nguồn chính, 16 vào DC, 16 ra AC

| Chân | Tín hiệu | Hướng |
|---|---|---|
| A1, B1, C1 | **GND** | — |
| A2, B2, C2 | **−23 V** | vào |
| A3, B3, C3 | **−12,6 V** | vào |
| A4, B4, C4 | **+12,6 V** | vào |
| A5…C6 | Không nối | — |
| **A7 / C7 / A8 / C8 / A9 / C9 / A10 / C10 / A11 / C11 / A12 / C12 / A13 / C13 / A14 / C14** | **Вых.1а= … Вых.8б=** (16 mức DC vào) | vào |
| B7…B14, A15…C16 | Không nối | — |
| **A17 / C17 / A18 / C18 / A19 / C19 / A20 / C20 / A21 / C21 / A22 / C22 / A23 / C23 / A24 / C24** | **Вых.1а== … Вых.8б==** (16 tín hiệu 400 Hz ra) | **ra** |
| B17…B24, A25…C29 | Không nối | — |
| A30…C32 | **GND** | — |

> **Quy ước tên net trong bản vẽ:** hậu tố `=` = tín hiệu **một chiều vào**; hậu tố `==` = tín hiệu **xoay chiều 400 Hz ra**.
> Thứ tự chân: mỗi kênh chiếm 1 chân hàng A hoặc C, hàng B bỏ trống. Giảm xuyên nhiễu là giả thuyết về ý đồ thiết kế, chưa có bằng chứng định lượng (E2).

---

## 3. SƠ ĐỒ KHỐI TỔNG THỂ

```text
DC11 A5/B5/C5 (~5V/400Hz)
  ├─ R124,R20/R21,R117 → U14 (Schmitt) → R26 → U17
  │                                           ├─ A/B → U16 → H14/H15
  │                                           └─ xung400Hz → DC11
  └─ R119,R24/R25,R120 → U15 (H15) → R30 → U18 → М/М̄
                                                     │
DC12: 16 Vin → 3 khoá/kênh ←──────────────────────────┘
                  │
                  └─ OA G≈±1 → đệm NPN/PNP → R_ra180Ω → 16 Vo
                                  ↑              │
                                  └─ hồi tiếp sau R_ra

Nguồn: ±12,6V, −23V, +3,5V; lọc C35…C46 trên ±12,6V.
```

---

## 4. CỤM A — NGUỒN VÀ LỌC (C35 … C46)

Tấm mạch dùng 4 mức nguồn: **+12,6 V, −12,6 V, −23 V, +3,5 V** và GND. **Không có diode/cầu chì bảo vệ đảo cực** — cấp nhầm cực tính sẽ phá hỏng hàng loạt IC.

| Tụ | Trị số | Nối giữa |
|---|---|---|
| C35, C36, C37, C38, C44 | 3300 pF | GND ↔ **+12,6 V** |
| C39, C46 | 4,7 µF | GND ↔ **+12,6 V** |
| C45 | 22 µF | GND ↔ **+12,6 V** |
| C43 | 3300 pF | GND ↔ **−12,6 V** |
| C40, C42 | 22 µF (cực + về GND) | GND ↔ **−12,6 V** |
| **C41** | 3300 pF | **+12,6 V ↔ −12,6 V** (lọc chéo 2 ray) |

Tổng: +12,6 V ≈ 31,4 µF + 5×3300 pF; −12,6 V ≈ 44 µF + 3300 pF.
**Ray −23 V và +3,5 V không có tụ lọc trên tấm này** — phải do tấm nguồn đảm bảo.

**Điểm đo (test point) có sẵn trên bản vẽ:** +12,6 V; −12,6 V; −23 V; +3,5 V; +5 V; +6,3 V.

---

## 5. CỤM B — BỘ TẠO XUNG ĐIỀU CHẾ (chi tiết)

### 5.1. Hai bộ so sánh U14, U15 (140УД1Б)

| Nhánh | Chia áp vào (chân 9) | Hệ số chia | Ra chân 5 → | Sửa tần số |
|---|---|---|---|---|
| **U14** | R124 (0 Ω) + **R20 = 2,61 kΩ** / R21 = 301 Ω (+R117 0 Ω) | 301/2911 = **0,1034** | R26 4,7 kΩ → U17A chân 2 | R27 56 Ω + C3 (0,01 µF) từ chân 12 → GND |
| **U15** | R119 (0 Ω) + **R24 = 2,05 kΩ** / R25 = 301 Ω (+R120 0 Ω) | 301/2351 = **0,1280** | R30 4,7 kΩ → U18A chân 2 | R31 56 Ω + C4 (0,01 µF) từ chân 12 → GND |

> Hai nhánh **khác hệ số chia** là sự kiện. Lệch pha còn do hai ngưỡng H14/H15 đối dấu; ý đồ lựa chọn trị số chưa có thuyết minh thiết kế (E5).
> Bản vẽ BV.22 ghi R24 là "2,050Mom/1%" và bảng BV.25 ghi "2,05ΩM" — **đều là lỗi đơn vị, trị số đúng 2,05 kΩ** (§9.1).

**Chân 140УД1Б dùng trên tấm:** 1 = −Uп (−12,6 V), 4 = **общий (GND)**, 5 = ra, 7 = +Uп (+12,6 V), 9 = vào đảo, 10 = vào không đảo, 12 = chân коррекция. Chân 2, 3, 6, 8, 11 bỏ trống.
Thông số sổ tay cũ dùng làm giả thiết tính: K_u=1350…12000, Ib ≤9 µA, ΔIb ≤2,5 µA, Vos ≤7 mV. PDF gốc cục bộ 140ud1B.pdf tr. 2 cho dòng 140УД1БВК: A=2000…10500, Ib ≤8 µA, ΔIb ≤1,5 µA, Icc ≤12 mA ở ±13,9 V, swing +8/−6,3 V với RL=5,05 kΩ. Chưa xác nhận biến thể/lô trên tấm; không coi hai bộ giới hạn là một.

### 5.2. U16 chọn HAI ngưỡng đối dấu, hồi tiếp Schmitt qua U14

**H14 và H15 là hai nút riêng**, không được chập chung khi làm đồ gá:

* H14 = U14 chân 10 = U16A chân 3 = U16B chân 5.
* H15 = U15 chân 10 = U16C chân 10 = U16D chân 12.
* R22 (10,5k từ −12,6 V) và R23 (301 Ω về GND) chia sẵn Vref−; nút này tới U16A.1/U16C.8.
* R28 (10,5k từ +12,6 V) và R29 (301 Ω về GND) chia sẵn Vref+; nút này tới U16B.7/U16D.14.
* A điều khiển U16B/C; B điều khiển U16A/D. Cặp A/B do U14→U17 tạo, không do U15.

Với giả thiết khoá dẫn khi gate âm (§5.3):

| U14.5 | A | B | Khoá dẫn | H14 | H15 |
|---|---|---|---|---|---|
| Âm | Cao | Thấp | U16A + U16D | −h | +h |
| Dương | Thấp | Cao | U16B + U16C | +h | −h |

`h = 12,6×301/(10500+301) = 0,351134 V` là giá trị danh định không tải. U16 chỉ chọn các nguồn đã chia áp; Ron không nối tiếp 10,5k/301 Ω để tạo tỉ số này. Ron và dòng vào OA gây thêm sụt áp sau bộ chia. Trở Thévenin mỗi bộ chia ≈292,6 Ω; nếu giả thiết Ron ≤100 Ω, Ib ≤9 µA thì riêng sụt do Ib có thể ≈3,53 mV. Thêm dung sai nguồn/R và Vos; không nghiệm thu theo ±0,351134 V tuyệt đối.

U14 có hồi tiếp dương: khi đầu vào tăng vượt +h, đầu ra chuyển âm và H14 đổi từ +h sang −h, giữ trạng thái. U15 nhận ngưỡng **đối dấu với H14**, không phải một Schmitt độc lập có cùng hồi tiếp.

| Nhánh | Hệ số chia | Trị tuyệt đối ngưỡng tại chân 9 | Trị tuyệt đối quy đầu vào |
|---|---|---|---|
| U14 | 0,103400893 | h | 3,395852 V |
| U15 | 0,128030625 | h | 2,742579 V |

**Diễn tiến nửa chu kỳ sin đi lên:** sau đỉnh âm, U14.5 dương nên H14=+h, H15=−h. U15 đổi sang âm khi sin còn âm tại −2,742579 V → М lên cao. Qua zero rồi tới +3,395852 V, U14 mới đổi sang âm → xung400Hz lên cao, H14=−h/H15=+h. Lúc này chân 9 U15≈+0,435 V đã lớn hơn +h, nên U15 không lật lại. Nửa chu kỳ đi xuống đối xứng.

| Chuẩn | Uđỉnh | U14 trễ sau zero | U15 sớm trước zero | М sớm hơn xung400Hz (hai sườn cùng chiều) |
|---|---|---|---|---|
| 5 Vrms | 7,071068 V | 28,7015° | 22,8214° | **51,5228° = 357,797 µs** |
| 5 V đỉnh | 5 V | 42,7789° | 33,2653° | **76,0441° = 528,084 µs** |

`Δθ = asin(h/(k14·Uđỉnh)) + asin(h/(k15·Uđỉnh))` — **cộng hai góc**, không lấy hiệu. Đây là mô hình linh kiện lý tưởng, chưa gồm trễ OA/khoá và bất đối xứng. Duty 50% chỉ là danh định với sin và ngưỡng đối xứng. Thực tế phải đo. Biên độ tại chân 9 vẫn ≈0,731 V đỉnh/0,905 V đỉnh khi chuẩn 5 Vrms.

---

### 5.3. Tầng dịch mức U17 (xung400Hz) và U18 (М / М̄)

**Giả thiết làm việc của 168КТ2:** gate −23 V dẫn, gate +3,5 V ngắt. Có cơ sở từ điều kiện thử datasheet và topo nhưng **chưa xác minh trên tấm thật**; mọi bảng pha dưới đây phụ thuộc giả thiết này.
*Cơ sở:* (a) datasheet 168КТ2 đo R_си.отк ở chế độ U_з = −15 V ⇒ đây là khoá MOSFET kênh p, mở bằng điện thế âm;
(b) cấu trúc đảo U17A→U17D và U18A→U18D chỉ tự nhất quán khi khoá dẫn ở mức âm.

**U17 (168КТ2В):**
* `U17A`: đk ← U14 qua R26; chân 1 = +3,5 V; chân 3 = **nút A**, có R32 10 kΩ kéo xuống −23 V.
  ⇒ **nút A = +3,5 V khi U17A dẫn, = −23 V khi hở.**
* `U17D`: đk ← nút A; chân 14 = +3,5 V; chân 12 = **nút B**, có R33 10 kΩ kéo xuống −23 V ⇒ **nút B = đảo của nút A**.
* `U17B` (chân 5/6/7) và `U17C` (chân 8/9/10) mắc **song song**, cùng do nút A điều khiển, nối `xung400Hz` xuống GND.
  `R34 = 1,8 kΩ` kéo `xung400Hz` lên +3,5 V ⇒ **xung400Hz = 0 V / +3,5 V, 400 Hz** (mức tương thích logic).
* Nút A/B đồng thời quay lại điều khiển U16 (hysteresis).

**U18 (168КТ2В, dùng 2 khoá):**
* `U18A`: đk ← U15 qua R30; chân 3 = +3,5 V; chân 1 = **М**, R35 10 kΩ kéo xuống −23 V.
* `U18D`: đk ← **М**; chân 12 = +3,5 V; chân 14 = **М̄**, R36 10 kΩ kéo xuống −23 V.
⇒ **М và М̄ bù nhau ở trạng thái xác lập**, mức danh định −23 V/+3,5 V, 400 Hz; mức cao có sụt do Ron và tải kéo xuống. Không có bằng chứng bảo đảm không overlap trong chuyển tiếp.
Đúng như HDSD mô tả: *"được biến đổi từ mức logic thành mức điện áp −23 V, +3,5 V"*.

> Định mức Б 15 V/В 25 V là điện áp so với подложка, không phải swing 26,5 V giữa hai đầu kênh. Chân 11 thả nổi là sự kiện đã chốt; cơ chế phân cực bên trong và dự trữ điện áp thực chưa được chứng minh. Không tự nối chân 11 để “sửa” mạch.

> М, М̄ và xung400Hz **được đưa ra DC11** cho các cụm khác (A313-V.02/.05) dùng chung một pha chuẩn.

---

## 6. CỤM C — MỘT KÊNH ĐIỀU CHẾ (lấy kênh 1а làm mẫu)

### 6.1. Sơ đồ chức năng đúng của kênh 1а

```text
Vin = ВЫХ.1А= ── R85 10k ──● N = U19.9 (−)
                           │
Vo = ВЫХ.1А== ── R86 10k ──┤
Vo ───────────── C1 10nF ──┘

Vin ── U2B(5→7) ──● S ── R37 4,7k ── U19.10 (+)
                  │
              U1A(3→1) ── GND(a)
Vin ── U2A(3→1) ── R4 10k ── GND(a)

U19.5 ── base chung Q1/Q2
Q1 collector → +12,6V; Q2 collector → −12,6V
Q1/Q2 emitơ chung = Y ── R39 180Ω ── Vo
U19.12 ── R38 56Ω ── C2 10nF ── GND(a)
U19.1 → −12,6V; U19.7 → +12,6V; U19.4 → GND(a)
U1A gate2 ← М; U2A gate2/U2B gate6 ← М̄
```

R38 không ở đường base. Nhãn a gần C1 thuộc đường chân 4; C1 nối **N–Vo**, không nối mát. Hồi tiếp R86/C1 lấy **sau R39**.

### 6.2. Cơ chế ±1 ở trạng thái xác lập

| Pha | М | М̄ | U1A | U2A/U2B | S | Vo lý tưởng |
|---|---|---|---|---|---|---|
| P1 | +3,5 V | −23 V | Ngắt | Dẫn | Vin | +Vin |
| P2 | −23 V | +3,5 V | Dẫn | Ngắt | 0 | −(R86/R85)Vin |

Đặt `k=R86/R85`. Với OA lý tưởng, KCL cho `Vo=(1+k)S−kVin`. Ở P1, chân 9≈chân 10≈Vin nên dòng Rin/Rfb gần 0; ở P2, chân 9 là đất ảo nên G=−k. Với k=1, hai mức bằng ±Vin. Linh kiện thực có sai số, offset, headroom và chuyển tiếp; xem §10.4/10.6.

### 6.3. Vai trò linh kiện và giới hạn suy luận

| Linh kiện | Trị số | Chức năng và giới hạn |
|---|---|---|
| U2B | 168КТ2Б | Đường nối tiếp Vin→S ở P1 |
| U2A + R4 | Khoá +10 kΩ 1% | Nhánh tải Vin→U2A→R4→GND ở P1, **không nối vào S**. So với tải Rin ở P2, cân bằng gần đúng là suy luận có cơ sở; Ron/dung sai làm hai tải khác nhau. Mục tiêu chống răng cưa S&H chưa được xác minh. |
| U1A | 168КТ2Б | Shunt S xuống GND ở P2 |
| R85/R86 | 10 kΩ 1% | Xác định G−=−k; hai sai số độc lập 1% cho k=0,980198…1,020202 |
| C1 | 0,01 µF | Song song R86; τ=100 µs, 1/(2 πτ)=1,59155 kHz. Mô hình động bên dưới; không được mô tả toàn bộ kênh như bộ lọc thông thấp một cực. |
| R37 | 4,7 kΩ 5% theo BV.22 | Bù gần đúng trở kháng vào đảo 5 kΩ. Nếu thay bằng dây 0 Ω, riêng Ib−9 µA tạo offset đầu ra 90 mV, không phải 45 mV. R37 hở là lỗi khác: chân 10 mất đường DC. |
| U19 | 140УД1Б | OA sai lệch; chân 4 mát; tham số đúng biến thể phải xác nhận |
| R38+C2 | 56 Ω +0,01 µF | Nhánh коррекция; RC=0,56 µs, tần số bằng trở kháng R/Xc ≈284 kHz. Không suy trực tiếp cực vòng kín hay dạng sóng chân 12 từ tích RC. |
| Q1/Q2 | 2Т312Б/2Т203Б | Lặp emitơ bù lớp B trong hồi tiếp; transistor dẫn theo **chiều dòng**. Chỉ với tải thuần trở mới thường tương ứng nửa điện áp dương/âm. |
| R39 | 180 Ω | Hạn chế dòng và tạo cách ly nối tiếp là hệ quả vật lý. Hồi tiếp bù sụt áp trong băng thông và headroom cho phép; trở kháng ra không bằng 0. **Không phải bảo vệ ngắn mạch.** |

**Mô hình động danh định:** `Zf=R86/(1+sτ)`; `Vo=(1+Zf/R85)S−(Zf/R85)Vin`. Khi Vin giữ DC và k=1:

`Vo(s)=[(2+sτ)/(1+sτ)]S(s)−Vin(s)/(1+sτ)`.

Khi S nhảy 0→Vin, Vo có bước tức thời bằng Vin trong mô hình OA lý tưởng, rồi phần còn lại tiến theo hàm mũ τ. Mạch thực làm hữu hạn sườn đó bởi băng thông, коррекция, slew và tải. C1 có tác dụng giảm hài của nhánh hồi tiếp, nhưng kết luận “vo tròn hoàn toàn/triệt gai để bảo vệ СКТ” là quá mạnh.

**Ngắn mạch:** `(12,6−0,7)/180=66,11 mA` là ước lượng khi base lên sát rail, không phải dòng bảo đảm/đo được. Thực tế `I≈(|V5|−|VBE|)/180`, còn giới hạn bởi khả năng lái base/β. Không thử chập đầu ra. Công suất Q phải tính `|VCE|·|IC|`, không lấy 12 V×66 mA đồng thời với giả thiết emitơ lên 11,9 V.

R_fb/C_fb sau R39 giúp giảm méo của tầng Q khi vòng còn điều khiển được. Một Q hở thường làm sai rõ chiều dòng tương ứng; với tải phản kháng không quy trực tiếp theo dấu điện áp.

---

## 7. BẢNG ÁNH XẠ 16 KÊNH → LINH KIỆN (dùng khi dò lỗi)

| Kênh | Вых.n= (DC12) | Вых.n== (DC12) | Khoá shunt (М) | Khoá nối tiếp (М̄) | R_bal 10k | R_in 10k | R_fb 10k | C_fb 0,01µ | KĐ TT 140УД1Б | R_bias 4,7k | R_corr 56 Ω | C_corr 0,01µ | Q NPN/PNP | R_ra 180 Ω |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1а** | A7 | A17 | U1A | U2A, U2B | R4 | R85 | R86 | C1 | U19 | R37 | R38 | C2 | Q1/Q2 | R39 |
| **1б** | C7 | C17 | U1B | U2C, U2D | R5 | R87 | R88 | C5 | U20 | R40 | R41 | C6 | Q3/Q4 | R42 |
| **2а** | A8 | A18 | U1C | U3A, U3B | R6 | R89 | R90 | C7 | U21 | R43 | R44 | C8 | Q5/Q6 | R45 |
| **2б** | C8 | C18 | U1D | U3C, U3D | R7 | R91 | R92 | C9 | U22 | R46 | R47 | C10 | Q7/Q8 | R48 |
| **3а** | A9 | A19 | U4A | U5A, U5B | R8 | R93 | R94 | C11 | U23 | R49 | R50 | C12 | Q9/Q10 | R51 |
| **3б** | C9 | C19 | U4B | U5C, U5D | R9 | R95 | R96 | C13 | U24 | R52 | R53 | C14 | Q11/Q12 | R54 |
| **4а** | A10 | A20 | U4C | U6A, U6B | R10 | R97 | R98 | C15 | U25 | R55 | R56 | C16 | Q13/Q14 | R57 |
| **4б** | C10 | C20 | U4D | U6C, U6D | R11 | R99 | R100 | C17 | U26 | R58 | R59 | C18 | Q15/Q16 | R60 |
| **5а** | A11 | A21 | U7A | U9A, U9B | R12 | R101 | R102 | C19 | U27 | R61 | R62 | C20 | Q17/Q18 | R63 |
| **5б** | C11 | C21 | U7B | U8A, U8B | R13 | R103 | R104 | C21 | U28 | R64 | R65 | C22 | Q19/Q20 | R66 |
| **6а** | A12 | A22 | U7C | U9C, U9D | R14 | R105 | R106 | C23 | U29 | R67 | R68 | C24 | Q21/Q22 | R69 |
| **6б** | C12 | C22 | U7D | U8C, U8D | R15 | R107 | R108 | C25 | U30 | R70 | R71 | C26 | Q23/Q24 | R72 |
| **7а** | A13 | A23 | U10A | U11A, U11B | R16 | R109 | R110 | C27 | U31 | R73 | R74 | C28 | Q25/Q26 | R75 |
| **7б** | C13 | C23 | U10B | U11C, U11D | R17 | R111 | R112 | C29 | U32 | R76 | R77 | C30 | Q27/Q28 | R78 |
| **8а** | A14 | A24 | U10C | U12A, U12B | R18 | R113 | R114 | C31 | U33 | R79 | R80 | C32 | Q29/Q30 | R81 |
| **8б** | C14 | C24 | U10D | U12C, U12D | R19 | R115 | R116 | C33 | U34 | R82 | R83 | C34 | Q31/Q32 | R84 |

### 7.1. Bảng chia sẻ tài nguyên — chìa khoá khoanh vùng hỏng

**Vỏ khoá shunt (điều khiển bằng М) — mất pha "−1":**

| Vỏ | Kênh bị ảnh hưởng |
|---|---|
| **U1** | 1а, 1б, 2а, 2б |
| **U4** | 3а, 3б, 4а, 4б |
| **U7** | 5а, 5б, 6а, 6б |
| **U10** | 7а, 7б, 8а, 8б |

**Vỏ khoá nối tiếp (điều khiển bằng М̄) — mất pha "+1":**

| Vỏ | Kênh | | Vỏ | Kênh |
|---|---|---|---|---|
| **U2** | 1а, 1б | | **U8** | 5б, 6б |
| **U3** | 2а, 2б | | **U9** | 5а, 6а |
| **U5** | 3а, 3б | | **U11** | 7а, 7б |
| **U6** | 4а, 4б | | **U12** | 8а, 8б |

> **Quy tắc suy luận nhanh:** hỏng **4 kênh liền nhau theo nhóm** ⇒ nghi U1/U4/U7/U10.
> Hỏng **đúng 2 kênh cùng cặp** ⇒ nghi U2/U3/U5/U6/U8/U9/U11/U12.
> Hỏng **1 kênh** ⇒ nghi linh kiện riêng của kênh (140УД1Б, Q, R, C).
> Hỏng **cả 16 kênh** ⇒ nghi cụm B (U14/U15/U16/U17/U18) hoặc nguồn.

---

## 8. THỐNG KÊ LINH KIỆN (BV.25) — ĐÃ ĐỐI CHIẾU

| Nhóm | Ký hiệu | SL | Trị số | Vai trò |
|---|---|---|---|---|
| Tụ | C1…C34 | 34 | 0,01 µF | 16×(C_fb + C_corr) + C3, C4 của U14/U15 |
| Tụ | C35–C38, C41, C43, C44 | 7 | 3300 pF | lọc cao tần nguồn |
| Tụ | C39, C46 | 2 | 4,7 µF | lọc nguồn +12,6 V |
| Tụ | C40, C42, C45 | 3 | 22 µF | lọc nguồn |
| Đầu nối | DC11, DC12 | 2 | DC96c | 96 chân/cái |
| Transistor | Q1, Q3 … Q31 (lẻ) | 16 | **2Т312Б** (NPN) | nửa trên tầng đệm |
| Transistor | Q2, Q4 … Q32 (chẵn) | 16 | **2Т203Б** (PNP) | nửa dưới tầng đệm |
| Điện trở | R4…R19 | 16 | 10 kΩ 1 % | cân bằng tải nguồn |
| Điện trở | R20 | 1 | 2,61 kΩ 1 % | chia áp U14 |
| Điện trở | R21, R23, R25, R29 | 4 | 301 Ω 1 % | chia áp / trễ |
| Điện trở | R22, R28 | 2 | 10,5 kΩ 1 % | mạng trễ U16 |
| Điện trở | R24 | 1 | **2,05 kΩ 1 %** | chia áp U15 (bản vẽ ghi nhầm đơn vị "MOm" — §9.1) |
| Điện trở | R26, R30 | 2 | 4,7 kΩ | ghép U14/U15 → U17A/U18A |
| Điện trở | R27, R31, R38…R83 (bước 3) | 18 | 56 Ω 1 % | коррекция chân 12 |
| Điện trở | R32, R33, R35, R36 | 4 | 10 kΩ 1 % | kéo xuống −23 V |
| Điện trở | R34 | 1 | 1,8 kΩ 1 % | kéo lên +3,5 V cho xung400Hz |
| Điện trở | R37…R82 (bước 3) | 16 | 4,7 kΩ 5 % | cân bằng dòng phân cực chân 10 |
| Điện trở | R39…R84 (bước 3) | 16 | 180 Ω 1 % | hạn dòng ra |
| Điện trở | R85…R116 | 32 | 10 kΩ 1 % | cặp R_in/R_fb 16 kênh |
| Điện trở | **R117…R124** | 8 | 0 Ω | cầu nối (bảng BV.25 ghi nhầm R124 thành R63 — §9.2) |
| IC | U1…U12 | 12 vỏ | **168КТ2Б** | 48 khoá tương tự (3/kênh) |
| IC | U16, U17, U18 | 3 vỏ | **168КТ2В** | khoá của cụm tạo xung |
| IC | U14, U15, U19…U34 | 18 | **140УД1Б** | 2 so sánh + 16 khuếch đại kênh |

**Kiểm tra chéo số lượng (đều khớp):** 12 vỏ × 4 khoá = 48 = 16 kênh × 3 khoá ✔ ; 18 KĐ TT = 16 + 2 ✔ ; 32 transistor = 16 × 2 ✔ ; 34 tụ 0,01 µF = 16×2 + 2 ✔

---

## 9. CÁC SAI SÓT TRONG HỒ SƠ — ĐÃ CHỐT

> Toàn bộ 6 điểm dưới đây **đã được xác nhận với người thiết kế/khai thác**. Không còn hạng mục treo.
> Cột "Trạng thái": ✅ = đã chốt, áp dụng ngay; ℹ️ = ghi nhận, không ảnh hưởng kỹ thuật.

| # | Nội dung | Trạng thái |
|---|---|---|
| 9.1 | R24 = **2,05 kΩ** (bản vẽ ghi sai đơn vị) | ✅ |
| 9.2 | Điện trở 0 Ω lối vào U14 ký hiệu đúng là **R124** (không phải R63) | ✅ |
| 9.3 | Sai số lượng cột SL bảng BV.25 | ℹ️ bỏ qua, lấy theo sơ đồ chính |
| 9.4 | BOM đếm theo section thay vì theo vỏ | ✅ lỗi xuất BOM |
| 9.5 | Chân 4 và 11 của 168КТ2**thực tế không dùng** | ✅ |
| 9.6 | +5 V và +6,3 V không dùng trên tấm này | ✅ |

### 9.1. ✅ R24 = 2,05 kΩ — bản vẽ ghi sai đơn vị

**Hiện trạng hồ sơ:** sơ đồ BV.22 ghi `R24 2,050Mom/1%`; bảng BV.25 ghi `2,05ΩM, 1%`.
**Trị số đúng: R24 = 2,05 kΩ ± 1 %.**

*Kiểm chứng bằng tính toán (đồng nhất với kết luận thực tế):*

| Giả thiết | U tại chân 9 U15 (chuẩn 5 Vrms) | Ngưỡng ±0,3511 V | Kết quả |
|---|---|---|---|
| R24 = 2,05 **MΩ** | 7,071 × 301/2 050 301 ≈ **1,04 mV** | không đạt | H15 vẫn đổi dấu do U14/U16 ⇒ U15 **có thể vẫn lật**, nhưng theo ngưỡng đổi dấu, gây sai pha nghiêm trọng; không suy ra mất cả 16 tín hiệu |
| R24 = 2,05 **kΩ** | 7,071 × 301/2 351 ≈ **0,905 V** | đạt | Phù hợp mô hình pha danh định ở §5.2 (còn cần kiểm thật) |

**Việc cần làm với hồ sơ:** sửa BV.22 thành `2,05k/1%` và BV.25 thành `2,05KΩ, 1%`.

### 9.2. ✅ Ký hiệu đúng là R124, không phải R63

Điện trở **0 Ω** mắc nối tiếp lối vào `~5 V/400 Hz` của U14 bị ghi nhầm là `R63` trên **cả** sơ đồ BV.22 **và** bảng BV.25.
**Ký hiệu đúng: R124.**

Sau khi sửa, dãy ký hiệu trở nên liên tục và số lượng khớp:

| Nhóm | Ký hiệu đúng | SL | Trị số |
|---|---|---|---|
| Cầu nối 0 Ω | **R117, R118, R119, R120, R121, R122, R123, R124** | 8 | 0 Ω |
| Điện trở ra 16 kênh (bước 3) | R39, R42, R45, R48, R51, R54, R57, R60, **R63**, R66, R69, R72, R75, R78, R81, R84 | 16 | 180 Ω |

⇒ **R63 chỉ có một nghĩa duy nhất: điện trở ra 180 Ω của kênh 5а.** Không còn trùng ký hiệu.

**Việc cần làm với hồ sơ:** đổi ký hiệu trên BV.22, BV.23, BV.24, BV.25 và thư viện Altium.

### 9.3. ℹ️ Cột số lượng bảng BV.25 có sai số học — bỏ qua

Nhóm 8 liệt kê R4…R19 + R88 + R107 + R112 = **19 ký hiệu** nhưng cột SL ghi **17**.
Tổng điện trở 10 kΩ thực tế = 16 (R4–R19) + 32 (R85–R116) + 4 (R32, R33, R35, R36) = **52**, bảng ghi 17 + 33 = 50.

**Kết luận:** không ảnh hưởng đến việc sửa chữa hay kiểm tra. **Khi có mâu thuẫn, lấy theo sơ đồ nguyên lý BV.22 làm gốc**, bảng BV.25 chỉ dùng tham khảo khi lập định mức vật tư.

### 9.4. ✅ BOM đếm theo section thay vì theo vỏ

* Nhóm 22 (168КТ2В) ghi `U16, U16, U16, U17, U17, U18 — 6 chiếc` → thực tế **3 vỏ**.
* Nhóm 20 (168КТ2Б) ghi 16 dòng (lặp U1, U2, U8, U12) → thực tế **12 vỏ**.
* Nhóm 21 (140УД1Б) 18 dòng = **18 vỏ** ✔ (nhóm này đúng vì mỗi vỏ 1 section).

**Số lượng đặt hàng đúng: 12 × 168КТ2Б + 3 × 168КТ2В + 18 × 140УД1Б.**
Cần sửa khi lập định mức vật tư, nếu không sẽ thừa 4 vỏ Б và 3 vỏ В.

### 9.5. ✅ Chân 4 và 11 của 168КТ2 thực tế KHÔNG dùng

Sơ đồ chỉ vẽ 12/14 chân (1,2,3 / 5,6,7 / 8,9,10 / 12,13,14) — **và đây là đúng thực tế: chân 4 và chân 11 không được nối trên mạch in.**

Theo datasheet, **chân 11 là подложка (đế/substrate)**. Trên tấm này đế **để thả nổi**, **chưa đủ tài liệu để kết luận cơ chế phân cực đế nội bộ**. Không thay đổi đấu nối đã được xác nhận.

**Hệ quả cần nhớ:**

| Việc | Ảnh hưởng |
|---|---|
| Thiết kế đồ gá kiểm tra | **Không cần cấp nguồn phụ cho đế** — chỉ 4 mức ±12,6 V, −23 V, +3,5 V (§9.6) |
| Thay thế bằng linh kiện hiện đại | Mạch thay thế **không có sẵn điện thế đế** để tham chiếu ⇒ phải tự tạo phân cực đế trong module chuyển đổi |
| Dò lỗi | Không đo/không kỳ vọng tín hiệu ở chân 4, 11 |

### 9.6. ✅ +5 V và +6,3 V (DC11 A2–C2, A4–C4) không dùng

Hai mức này được đưa tới tấm mạch qua DC11 nhưng **không nối vào mạch nào**, chỉ có điểm đo trên bản vẽ (mục đích đo kiểm nguồn thứ cấp chung của khối).

**Khi làm đồ gá test A313-V.06: không cần cấp +5 V và +6,3 V.**

---

## 10. QUY TRÌNH KIỂM TRA THEO CỤM CHỨC NĂNG

### 10.1. Trang bị tối thiểu

| Thiết bị | Yêu cầu |
|---|---|
| Nguồn DC 4 kênh | +12,6 V / −12,6 V (≥ 0,5 A), −23 V (≥ 0,1 A), +3,5 V (≥ 0,1 A), có **giới hạn dòng** |
| Máy phát | Sin 400 Hz, biên độ chỉnh được quanh 5 V, méo thấp |
| Nguồn DC chuẩn | −4…+4 V, độ chính xác ≥ 0,05 % (làm V_in) |
| DMM 6½ chữ số | Đo DC và True-RMS AC |
| Dao động ký 2–4 kênh | ≥ 20 MHz, có trigger ngoài (dùng xung400Hz hoặc М) |
| Đồ gá | 2 ổ cắm DC96c + bảng chuyển mạch 16 kênh vào/ra |

### 10.2. Bước 0 — Kiểm tra nguội (KHÔNG cấp nguồn)

| # | Nội dung | Điểm đo | Chuẩn |
|---|---|---|---|
| 0.1 | Ngoại quan: cháy, phồng tụ, nứt vỏ IC tròn, mối hàn nứt, ăn mòn tiếp điểm cạnh | toàn tấm | sạch, bóng |
| 0.2 | Cách điện ray nguồn ↔ GND | DC12 A2/A3/A4 ↔ GND | Đo hai chiều, chờ tụ nạp, so tấm chuẩn; IC/đường kéo có thể cho trị số thấp. Không có cận 100 kΩ/1 kΩ tổng quát từ sơ đồ; không dùng megohmmeter cao áp |
| 0.3 | Ngắn mạch giữa 2 ray | +12,6 ↔ −12,6 (qua C41) | So tấm chuẩn sau quá trình nạp tụ; đường bán dẫn làm phép đo phụ thuộc cực tính |
| 0.4 | Trở kháng từng đầu ra | DC12 A17…C24 ↔ GND | So tương đối 16 kênh trong cùng điều kiện; chưa xác nhận ngưỡng 20% hay trị số vài kΩ |
| 0.5 | Trở kháng từng đầu vào | DC12 A7…C14 ↔ GND | So 16 kênh; không cố định 10–20 kΩ vì khoá mất nguồn/đế nổi và đường bán dẫn |
| 0.6 | Đo nguội R_ra 180 Ω từng kênh | 2 đầu R39…R84 | 180 Ω ±1 % |
| 0.7 | Diode-test Q1…Q32 tại chân | B-E, B-C | 0,5–0,8 V; **không được 0 V (chập) hay hở** |
| 0.8 | Tụ 22 µF / 4,7 µF (C39, C40, C42, C45, C46) | tại chỗ | không chập; nếu nghi thì tháo đo ESR |

> Mẹo: bước 0.4/0.5 tạo "chữ ký trở kháng" 16 kênh. Đây là **bài test nhanh nhất để khoanh vùng kênh hỏng mà chưa cần cấp nguồn**.

### 10.3. Bước 1 — Cấp nguồn và ghi dòng tĩnh

1. Tấm tháo khỏi hệ thống; nối GND chung chắc chắn, các đầu vào Vin=0, đầu ra chỉ nối thiết bị đo trở kháng cao. Nguồn đã đặt đúng cực/tất cả mức trước khi bật; **bật/tắt đồng thời hai ray ±12,6 V**, không cố ý cấp một ray rồi mới cấp ray kia. Trình tự bốn nguồn phải xác lập trên đồ gá/tấm chuẩn; chưa có căn cứ cho thứ tự riêng đã ghi ở Rev. B.
2. Giới hạn dòng theo tấm chuẩn và tải thực; đo riêng từng ray bằng thiết bị, không dùng tay sờ IC đang cấp điện để quyết định dừng. Dòng vượt 1,5×mốc ở cùng chế độ là dấu hiệu cần ngắt và kiểm, không phải chuẩn linh kiện tổng quát.
3. **Dòng IC:** giả thiết 10 mA/con cho 18 con là 180 mA, không suy ra dải 100–200 mA mỗi ray của toàn tấm. PDF 140ud1B.pdf ghi 12 mA tại ±13,9 V cho БВК, tương ứng 216 mA riêng 18 IC; cần xác nhận lô/điều kiện. Cộng dòng tầng Q, base, mạng chia/hồi tiếp và tải. Ví dụ 16 tải thuần trở 1 kΩ cùng mức 4 V cần riêng dòng tải 64 mA trên ray đang cấp/hút, chưa kể phần còn lại. Với điều chế đối xứng, chia dòng trung bình theo duty; đo cả đỉnh.
4. Bốn điện trở kéo 10k giữa −23 V và nút cao +3,5 V lấy ≈2,65 mA/nhánh đang cao. Bình thường hai nhánh cao cho ≈5,3 mA DC từ +3,5 sang −23 V; cộng chuyển mạch/tải ngoài và nhánh R34 (≈1,94 mA khi bị kéo thấp). Không lấy 5–15 mA làm chuẩn nghiệm thu cứng.
5. Đo +12,6/−12,6/−23/+3,5 V. DKKT đoạn kiểm nguồn thứ cấp liệt kê ±5% cho +5, ±12,6, −23, +6,3 V; **không nêu riêng +3,5 V**, nên phải lấy chuẩn của ray này từ hồ sơ nguồn/tấm chuẩn.
6. Ghi offset từng đầu ra ở cả hai pha tĩnh (§10.4). Mốc 50 mV chỉ sàng lọc tham khảo; offset lớn không riêng do OA, còn khoá, R_bias, rò và nguồn.

### 10.4. Bước 2 — Kiểm tra TĨNH bằng ±5 V DC tại ngõ chuẩn

**Giới hạn pass/fail lấy từ khối tốt** (tấm chuẩn đo thực), không phải từ tính toán lý thuyết; các ngân sách tính dưới đây chỉ để định hướng.

**Kết luận D1:** khả thi theo topo trong điều kiện mạch khỏe và giả thiết chiều khoá đúng. Không có vòng nào bắt buộc dao động khi chuẩn DC ở ±5 V. Đây chưa phải chứng nhận thử trên phần cứng; phải xác nhận các nút sau trước khi dùng làm bài ATE tự động.

| Chuẩn đưa vào DC11 A5/B5/C5 | U14.9 | U15.9 | H14/H15 | U14.5/U15.5 | A/B | М/М̄ | G |
|---|---|---|---|---|---|---|---|
| +5 V DC | +0,5170 V | +0,6402 V | −h/+h | Âm/âm | Cao/thấp | Cao/thấp | +1 |
| −5 V DC | −0,5170 V | −0,6402 V | +h/−h | Dương/dương | Thấp/cao | Thấp/cao | −1 |

“Cao/thấp” là mức gần +3,5 V/−23 V, không phải GPIO 3,3 V. Với +5 V, U14.9 vượt cả hai ngưỡng nên đầu ra âm bất kể trạng thái ban đầu; U16A/D dẫn. U15.9>+h nên U15 cũng âm, hệ tự giữ. Với −5 V ngược lại. Dự trữ danh định so với h: U14≈0,166 V, U15≈0,289 V; cần xét dung sai/offset/Ron trước khi hạ mức chuẩn. Ở chuẩn 0 V, trạng thái phụ thuộc lịch sử; không dùng 0 để chọn pha.

**Thực hiện:**

1. Tách nguồn sin và các kết nối ngoài có thể cùng lái DC11; tuyệt đối không đấu song song nguồn DC với đầu ra bộ tạo chuẩn. Cấp đủ 4 nguồn đúng mức trước khi bơm tín hiệu, tắt tín hiệu trước khi tắt nguồn. ±5 V là điện áp tại đầu nối; điện áp vào OA đã được chia như bảng.
2. Đầu ra không tải ngoài DMM, các Vin không đo nối GND. Chuyển chuẩn ±5 V, quan sát U14/U15.5, H14/H15, М/М̄ bằng scope: phải đứng yên, đúng bảng, không tự kích. Nếu sai, dừng quét DC; sửa cụm tạo xung/kiểm chiều khoá trước. Không ép М/М̄ từ ngoài chống tầng U18.
3. Đo Vo với Vin=+4, −4, +1, 0 V ở mỗi pha. Chờ xác lập theo trace; 10 ms có thể dùng làm giá trị khởi đầu, tăng nếu tấm chưa ổn. Mong đợi mức gần +Vin hoặc −Vin, **không áp sẵn cửa sổ ±60 mV** cho mọi linh kiện 1%.
4. Lặp 16 kênh, ghi cả Vin thực và Vo. Từ hai cực tính lấy `Gp=[Vo(+4)−Vo(−4)]/8` và `Op=[Vo(+4)+Vo(−4)]/2`, riêng p=P1/P2; đo thêm Vo(0) để kiểm phi tuyến/offset. Cách này tách gain khỏi offset.

**Ngân sách sai số D2 (trở thuần, tải nhẹ, trạng thái xác lập):**

* Rin/Rfb độc lập 1%: `kmin=0,99/1,01=0,980198`, `kmax=1,01/0,99=1,020202`. G− có thể lệch −1,9802…+2,0202% chỉ do trở; tại 4 V là ≈80,81 mV. Không thể bảo đảm 1% hoặc ±60 mV.
* G+ lý tưởng bằng 1 dù k sai. OA có gain hữu hạn gây sai số gần `(1+k)/A` (với đệm lý tưởng): A≥1350 cho ≈0,15%, nhưng Vos đến 7 mV tạo noise gain ≈2 → 14 mV, tương đương 0,35% tại 4 V, đã vượt 0,3% nếu dùng phép chia một điểm chưa khử offset.
* Offset DC xấp xỉ `E=(1+k)Vos+Rfb·Ib− − (1+k)(Rbias+Ron)·Ib+`. Không được lấy `(5−4,7)k×ΔIb` để thay tất cả sai số bias. Với giả thiết cũ Ib ≤9 µA, ΔIb ≤2,5 µA, Rbias ±5%, Rin/Rfb ±1%, Ron 0…100 Ω, cận bảo thủ riêng các hạng này ≈**49,8 mV**. Chưa gồm rò, trở nguồn, biến thiên Ron trong chế độ đế thả nổi, CMRR, nhiệt và gain hữu hạn/tầng Q. Với thông số БВК 8 µA/1,5 µA, cận nhỏ hơn; không trộn hai tập tham số.
* Vì vậy 50 mV là mốc tham khảo sát ngân sách, không phải bảo đảm chung. Cận cộng đơn giản tại 4 V pha− theo giả thiết cũ đã khoảng 80,8+49,8+6≈137 mV, chưa gồm mọi lỗi. Đây là **ngân sách tính**, không tự nâng thành dung sai sản phẩm.

| Chỉ tiêu cần ghi | Công thức/diễn giải | Cách đặt giới hạn |
|---|---|---|
| G+ | Hệ số từ hai cực tính, so với +1 | 0,3% có thể là mục tiêu đã hiệu chuẩn, chưa phải bảo đảm toàn tấm |
| G− | Hệ số từ hai cực tính, so với −1 | Không đòi ≤1% với hai điện trở 1% độc lập; cần đo/chọn cặp hoặc đặc tả chính thức |
| Mất đối xứng gain | `abs(G+ + G−)` | Có thể tới ≈2,02% riêng do tỉ số R; 1% chỉ dùng nếu có tuyển/hiệu chuẩn |
| Offset | Op và Vo(0), cả hai pha | Ghi tấm chuẩn theo nhiệt độ; 50 mV chỉ mốc khảo sát |
| Tuyến tính | So Vo(±1) với đường thẳng từ ±4, đã trừ offset | 0,2% chưa có bảo đảm từ dữ liệu đang có |

Giá trị vượt mốc gợi ý chưa tự chứng minh tấm hỏng. Chỉ khóa giới hạn pass/fail khi đã có đặc tả áp dụng và phân bố đo của tấm chuẩn. Bài DC không kiểm được overlap, pha 400 Hz hay ổn định tải phản kháng.

---

### 10.5. Bước 3 — Kiểm tra U14/U15/U16/U17/U18 với sin 400 Hz

Cấp chuẩn tại DC11 A5/B5/C5, ghi rõ biên độ đo thực là Vrms hay V đỉnh.

| # | Điểm đo | Mong đợi theo mô hình danh định | Nếu sai, kiểm |
|---|---|---|---|
| 3.1 | U14.9 | Sin=0,1034009×chuẩn,≈0,731 V đỉnh khi 5 Vrms | R20/R21/R124/R117 |
| 3.2a | U14.10=H14 | Gần ±0,351 V, đổi sau zero; theo trạng thái U14 | U16A/B, hai nguồn chia áp |
| 3.2b | U15.10=H15 | Gần ±0,351 V **đối dấu H14**, không chung nút | U16C/D, R22/R23/R28/R29 và cầu 0 Ω |
| 3.3 | U14.5 | Xung bão hòa; sườn sau zero theo §5.2 | U14, nguồn, hồi tiếp U16/U17, R27/C3 |
| 3.4 | A=U17A.3 | Gần −23/+3,5 V | U17A/R32/R26 |
| 3.5 | B=U17D.12 | Bù A ở xác lập | U17D/R33 |
| 3.6 | DC11 A6/B6/C6 | xung400Hz gần 0/+3,5 V; duty ≈50% nếu sin/ngưỡng đối xứng | U17B/C/R34 |
| 3.7 | U15.9 | Sin=0,1280306×chuẩn,≈0,905 V đỉnh khi 5 Vrms | R24=2,05 kΩ, R25/R119/R120 |
| 3.8 | U15.5 | Xung bão hòa; sườn **trước zero** danh định | U15 và H15; R31/C4 |
| 3.9 | DC11 A7/B7/C7 | М gần −23/+3,5 V | U18A/R35/R30 |
| 3.10 | DC11 A8/B8/C8 | М̄ bù ở xác lập; **đo**, không giả định overlap bằng 0 | U18D/R36 và tải điều khiển |
| 3.11 | Hai sườn cùng chiều của М và xung400Hz | М sớm ≈357,8 µs(5 Vrms) hoặc 528,1 µs(5 V đỉnh), chưa gồm sai số/trễ | H14/H15, tỉ số chia, biên độ chuẩn, chiều khoá |

Ghi hai sườn riêng và so với zero của sin. Các con số là mô hình danh định, không phải cửa sổ nghiệm thu. М/М̄ cùng mức dẫn có thể gây dòng xung từ Vin qua hai Ron xuống GND; mức hại phụ thuộc nguồn/trở kháng và thời gian. Đo cả hai gate và S/Vin để xác định chồng dẫn thực; ngưỡng logic tùy chọn không thay thế ngưỡng dẫn linh kiện.

### 10.6. Bước 4 — Kiểm tra ĐỘNG từng kênh

Chuẩn 400 Hz, Vin=+4 V; khởi đầu không tải ngoài đầu đo. Đo **8 điểm** kênh 1а, GND đầu đo về GND tấm (không kẹp mát scope vào rail âm).

| TP | Vị trí | Mong đợi và giới hạn |
|---|---|---|
| TP1 | DC12 A7, ВЫХ.1А= | DC+4 V; đo gợn thực, chưa có chuẩn “vài mV” được bảo đảm |
| TP2 | S=U2B.7=R37 trái | Gần 0↔4 V; Ron, rò, overlap làm sai lệch |
| TP3 | U19.10 | Theo S nhưng chênh DC có thể Ib×4,7k ≈42,3 mV với giả thiết 9 µA; không coi bằng hệt TP2 |
| TP4 | U19.9 | Gần TP3 khi vòng ổn định; sai khác phụ thuộc Vos/gain; ở sườn có thể tăng |
| TP5 | U19.5, base Q1/Q2 | Khi Q dẫn: `V5≈Y+VBE(NPN)` hoặc `Y−abs(VBE(PNP))`; không phải chỉ ±4 V. Khu vực chuyển dòng có méo/vùng chết; phụ thuộc tải |
| TP6 | Y=emitơ Q1/Q2 | `Y=Vo+180·I_R39`; khi không tải vẫn có dòng Rfb/Cfb. Sườn gồm phần truyền trực tiếp và phần quá độ, không chỉ hàm mũ 100 µs |
| TP7 | DC12 A17, ВЫХ.1А== | Mức xác lập gần ±4 V; khác Y theo dòng qua R39. So mô hình §6.3 và trace tấm chuẩn |
| TP8 | U19.12, đầu trên R38 | **Chưa đủ dữ liệu dự đoán dạng/biên độ.** Mạng RC nối đất không chứng minh nhỏ hơn TP5. Dùng đầu đo điện dung thấp, ghi tải đầu đo và trace chuẩn; không dùng biên độ suy đoán làm pass/fail |

**Tải:** bắt đầu bằng ≥1 kΩ thuần trở đã biết công suất, thử từng kênh; chỉ thêm tải tương đương СКТ khi biết trở kháng theo tần số/pha. Không tự chọn 1–2 kΩ//0,1 µF làm tải chuẩn: cạnh có thể tạo dòng C·dV/dt và gây mất ổn định. Mốc sụt ≤2% chỉ là mục tiêu cần xác nhận, chưa suy được từ bản vẽ.

400 Ω ở 4 V đã lấy 10 mA tải; pha− còn ≈0,4 mA qua Rfb, nên dòng emitơ ≈10,4 mA. Cận bảo thủ để tổng emitơ ≤10 mA là RL≥4/(10−0,4)mA≈417 Ω, nhưng **vẫn phải kiểm swing, β, nhiệt, quá độ và SOA**. Với RL=400 Ω, cần Y≈5,872 V và base ≈6,57 V (VBE0,7 V); vượt swing âm 6,3 V được bảo đảm ở điều kiện thử của PDF БВК. Vì vậy không chứng nhận tải 400 Ω bằng phép chia 4 V/10 mA.

**Thành phần 400 Hz:** với mô hình lý tưởng §6.3 và duty 50%, `V1_peak/abs(Vin)=(2/π)·abs((2+jωτ)/(1+jωτ))≈1,24455`; `V1_rms ≈0,88003·abs(Vin)`. Với Vin 4 V: khoảng 4,978 V đỉnh,3,520 Vrms riêng thành phần cơ bản. Không nhầm với RMS toàn dạng sóng hay với mức plateau 4 V. FFT phải ghi chuẩn peak/RMS; đo qua lọc dải phải hiệu chỉnh gain bộ lọc. Mạch thực cần ghi trace chuẩn, vì OA/коррекция/tải chưa nằm trong mô hình này.

---

### 10.7. Chẩn đoán theo topo (nguyên nhân là giả thuyết cần đo tiếp)

| Triệu chứng | Nguyên nhân khả dĩ / phép phân biệt |
|---|---|
| Cả 16 kênh không còn AC, Vin bình thường | Đo М/М̄,4 nguồn, chuẩn 400 Hz, U14/U15/H14/H15. Mất điều chế có thể để lại DC±Vin, không đồng nghĩa Vo=0 |
| Cả 16 kênh Vo ≈+Vin DC | Kiểm М cao/М̄ thấp, U18A/R35, U15.5 và chuẩn. Không chỉ một linh kiện gây được |
| Cả 16 kênh Vo ≈−Vin DC | Kiểm М thấp/М̄ cao, U18A/D/R35/R36 và U15; không gán riêng М̄ kẹt |
| Nhóm 4 kênh cùng bất thường | Kiểm vỏ shunt U1/U4/U7/U10 và dây М. Shunt hở để S nổi trong pha−: có thể giữ điện, trôi, méo; không bắt buộc +Vin DC |
| Cặp 2 kênh cùng bất thường | Kiểm vỏ U2/U3/U5/U6/U8/U9/U11/U12 và М̄. Khoá nối tiếp hở để S nổi trong pha+, không tự tạo −Vin DC |
| Một kênh Vo ≈0 dù TP2 bình thường | Đo TP3/4/5/Y và Rra. Rfb hở thường mất hồi tiếp DC/bão hòa; Rin hở còn đường S→OA nên không giả định Vo=0; hai Q hở còn đường hồi tiếp tới đầu đo |
| Kênh hụt chiều dòng dương/âm với tải thuần trở | NPN/PNP tương ứng hở/yếu hoặc mất nguồn cục bộ; thử tải đã biết. Với tải phản kháng, dấu điện áp không xác định Q đang dẫn |
| Kênh bão hòa, không theo Vin | Q chập C-E, hồi tiếp Rfb hở, mất nguồn/GND hoặc OA; điện áp không nhất thiết ±12 V |
| Mất đối xứng plateau | Đo Rfb/Rin,offset từng pha, Ron/Rbias và Vin tại chân tấm. Rbal hở chỉ tác động rõ qua trở kháng nguồn; nguồn áp lý tưởng không tự đổi G |
| Sườn/chuyển tiếp bất thường, fundamental thấp | Cfb tăng/rò, bandwidth OA, коррекция, tầng Q hoặc tải; phân biệt rò Cfb (đổi DC gain) với chỉ tăng C |
| Tự kích cao tần | Kiểm Rcorr/Ccorr, lọc nguồn, tải dung, hồi tiếp, Q thay thế; Rcorr/Ccorr hở là một khả năng, không điều kiện đủ |
| Gai tại sườn | Khoá/overlap, Cfb, nối đất, đầu đo và tải; không kết luận charge injection tăng chỉ từ một gai |
| Offset nhiều kênh | Nguồn, GND, rò/khoá, sai chế độ đo; sau đó mới so OA/Rbias |
| Sụt mạnh khi tải | Thiếu headroom, Q/Rra, vòng hồi tiếp, giới hạn dòng nguồn; Rra trôi chỉ gây sụt rõ khi bù không đủ |
| Vin gợn 400 Hz | Chồng dẫn М/М̄, trở kháng nguồn, Rbal sai/hở, trở nối chung hoặc S&H; đo đồng thời S/Vin/gate |
| −23 V tiêu thụ tăng | Chập khoá, R32/R33/R35/R36 sai, gate/tải ngoài, trạng thái không bù; khoanh vùng qua sụt áp từng R |
| R24 lắp nhầm 2,05 MΩ | Biên độ U15.9 rất nhỏ nhưng H15 vẫn đổi dấu do U14: U15 có thể vẫn phát 400 Hz, **sai pha**; kiểm pha và trị số thay vì chỉ kiểm có xung |

---

## 11. GỢI Ý THIẾT KẾ ATE CHO TẤM A313-V.06

```text
PC → controller FPGA/MCU
 ├─ DAC ±4V + mux → 16 Vin (kênh không đo được đưa về GND)
 ├─ Nguồn chuẩn cách ly/chuyển mạch sin400Hz ↔ +5VDC ↔ −5VDC
 ├─ 4 nguồn +12,6/−12,6/−23/+3,5V, đo dòng riêng
 ├─ Mux+ADC: đo DC hai pha, đo động đồng bộ 400 Hz
 └─ Đầu vào bảo vệ/dịch mức: М, М̄, xung400Hz, sin chuẩn
```

**Bài tĩnh:** chỉ chạy sau khi đã xác nhận trạng thái §10.4 trên tấm chuẩn; đo ±4, ±1, 0 V và khử offset để tính gain. Phủ 16 kênh không đồng nghĩa phủ 100% lỗi. Mux không được để các Vin còn lại thả nổi.

**Bài động:** đo fundamental/pha bằng tín hiệu tham chiếu và giữ trace sườn. ADC 100 kS/s có bước 10 µs, phù hợp thành phần 400 Hz nhưng không bắt chắc gai/overlap dưới µs; dùng scope hoặc đường capture/comparator đủ nhanh cho phép đó. Không quy gai vượt ngưỡng thành khoá hỏng mà bỏ qua tải/đầu đo.

**Overlap:** bộ so sánh phải chuyển mức −23/+3,5 V an toàn về logic, ngưỡng chọn theo quan hệ gate–kênh và phép đo thực. Hai cực đại datasheet t_on ≤0,3 µs, t_off ≤0,7 µs **không cho phép lấy hiệu 0,4 µs làm overlap dự đoán**, cũng không chứng minh ngưỡng vài chục ns hợp lý. Chốt cửa sổ chấp nhận từ đo thực và dòng xung vào S&H.

**Nguồn/tải:** bật/tắt ±12,6 V đồng thời; trình tự bốn nguồn và giới hạn dòng phải qua xác nhận đồ gá/tấm chuẩn. Các giá trị 400 mA/50 mA cũ chưa có ngân sách kiểm chứng nên không dùng làm chuẩn cố định. Tải thực, chế độ 16 kênh và dòng khởi động quyết định mức đặt. Không chập đầu ra: R 180 Ω không bảo vệ Q. Không cấp +5 V/+6,3 V vào rail không dùng, không tự nối chân 4/11 của 168КТ2. Mức ±5 V DC của bài đóng băng là **tín hiệu chuẩn**, không phải rail +5 V bị bỏ.

R24 phải 2,05 kΩ theo xác nhận thực; nếu lắp nhầm 2,05 MΩ có thể vẫn có 400 Hz nhưng sai pha (§9.1/10.7). Đầu vào DI/ADC cần chịu mức điện áp thực và trạng thái nguồn chưa sẵn, không nối thẳng М/М̄ vào GPIO.

---

## 12. DANH MỤC VIỆC CÒN LẠI

### 12.1. ✅ Các kết luận đã chốt từ Rev. B (giữ nguyên trong Rev. C)

| # | Nội dung | Kết quả |
|---|---|---|
| ✔ | Trị số R24 | **2,05 kΩ** (§9.1) |
| ✔ | Ký hiệu điện trở 0 Ω lối vào U14 | **R124** (§9.2) |
| ✔ | Chân 4 và 11 của 168КТ2 | **Không dùng, không nối** (§9.5) |
| ✔ | +5 V, +6,3 V trên DC11 | **Không dùng** (§9.6) |
| ✔ | Sai sót cột SL bảng BV.25 | Bỏ qua, lấy theo BV.22 (§9.3) |
| ✔ | BOM đếm theo section | Xác nhận lỗi, số vỏ đúng 12/3/18 (§9.4) |

### 12.2. ☐ Còn phải làm trên mạch thật

| # | Nội dung | Vì sao cần |
|---|---|---|
| 1 | ☐ Xác định **biên độ thực của chuẩn ~5 V/400 Hz** (rms hay đỉnh) do khối nguồn cấp | Quyết định độ sớm М so với xung400Hz: khoảng 357,8 µs (5 Vrms) hoặc 528,1 µs (5 V đỉnh) trong mô hình danh định — §5.2 |
| 2 | ☐ Xác nhận **chiều điều khiển 168КТ2** bằng phép đo đồng thời chân затвор và 2 chân tín hiệu của U1A trên tấm đang chạy | Hiện đang suy ra từ datasheet + cấu trúc mạch (§5.3) |
| 3 | ☐ Ghi **"chữ ký" tấm chuẩn (known-good)** | Mốc so sánh cho toàn bộ quy trình §10: dòng 4 ray; 16 giá trị `G+`/`G−`; lệch không; biên độ thành phần 400 Hz; Δt(М, xung400Hz); dạng sóng TP1–TP8 của 1 kênh mẫu |
| 4 | ☐ Xác định **trở kháng tải thực** của biến thế sin-cos đấu vào 3Ш3 | Thiết kế tải giả theo Z(f), pha, dòng đỉnh và headroom; 400 Ω không phải tải được bảo đảm — §10.6 |
| 5 | ☐ Kiểm tra **overlap М/М̄** trên tấm chuẩn | Hai thời gian 0,3/0,7 µs là các cực đại ở điều kiện thử; không trừ để suy overlap. Đo gate/S/Vin và dòng quá độ để chốt ngưỡng (§10.5, §11) |

**Bổ sung xác nhận Rev. C:** đo H14/H15 riêng và hai sườn М/xung400Hz; xác nhận ±5 V DC tạo đúng hai trạng thái tĩnh, ghi TP8 với tải đầu đo; xác định mã/lô OA để chọn đúng bộ giới hạn. Ghi điện áp nguồn, nhiệt độ, tải và phiên bản đồ gá cùng mọi chữ ký chuẩn.

### 12.3. ☐ Sửa hồ sơ thiết kế

| # | Bản vẽ | Nội dung sửa |
|---|---|---|
| 1 | ☐ BV.22 | `R24 2,050Mom/1%` → **`R24 2,05k/1%`** |
| 2 | ☐ BV.22, BV.23, BV.24 | Đổi ký hiệu điện trở 0 Ω lối vào U14: `R63` → **`R124`** |
| 3 | ☐ BV.25 | R24: `2,05ΩM` → **`2,05KΩ`**; nhóm 19: `R63, R117…R123` → **`R117…R124`** |
| 4 | ☐ BV.25 | Nhóm 20/22 đếm lại theo **vỏ**: 12 × 168КТ2Б, 3 × 168КТ2В |
| 5 | ☐ Thư viện Altium | Ký hiệu 168КТ2 giữ nguyên 12 chân (chân 4, 11 không dùng — §9.5) |

---

*Rev. C — 16/09/2026. Tài liệu lập trên cơ sở đọc và dựng lại netlist từ bản vẽ 07MB.A313-V.BV.22 (trang 28), BV.23/24 (trang 29–30), BV.25 (trang 31); HDSD-A313-V mục 3.2.4; DKKT-A313-V Phụ lục B; datasheet 168КТ2 và К140УД1Б.*
*Giữ nguyên sáu kết luận khai thác §9. Nhật ký §0 ghi riêng bằng chứng topo, tính toán, giả thiết và phần chưa đo. Rev. C không phải biên bản nghiệm thu phần cứng.*
