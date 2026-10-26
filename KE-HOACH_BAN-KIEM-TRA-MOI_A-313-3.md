# KẾ HOẠCH CHẾ TẠO BÀN KIỂM TRA A-313-3 PHIÊN BẢN MỚI (BKT-A313-3 Gen-2)

**Rev. B — 26/10/2026** (Rev. A cùng ngày; Rev. B ghi quyết định của người dùng ở §9 và thêm §5.5, §5.6). Kế hoạch định hướng, chưa có thiết kế mạch. Số liệu lấy từ: thư mục
`thiet_bi_kiem_tra_a313/` (đã quét), `Excel center control/A313-3_ket-noi-toan-khoi.xlsx`,
`KE-HOACH_KIEM-TRA_A-313-3.md` (giai đoạn 2–6), tài liệu A7-Lite (Microphase) và tri thức JARVIS dự án
ARINC429_ATS. Mọi ước lượng thời gian là **ước lượng**, sai số ±40 %. Chưa có phép đo phần cứng nào.

---

## 1. Yêu cầu đã cải thiện (thay cho prompt gốc)

**Mục tiêu.** Một thiết bị duy nhất, điều khiển từ PC, thay chức năng của **ПС17-318 + ПС17-319 + 3 УСС +
УИН** trong sơ đồ Рис. 201 (A-313-3 ↔ bàn) để: (1) kiểm tra và khoanh vùng hỏng khối A-313-3 / tấm Y1–Y15;
(2) lập "chữ ký khối tốt". **Phạm vi chốt (26/10/2026): chỉ A-313-3**; việc dùng chung cho A313-V để sau.

**Giữ nguyên (không đổi so với bàn Nga):** 5 đầu nối khối (3Ш1, 3Ш2, 3Ш7: 50 chân; 3Ш3, 3Ш4: РПКМ3-67/67, mỗi cái hai phích 67 chân),
mức logic loạt 133/136, nguồn vào +27 V và ~36 V 400 Hz (cả hai vào qua 3Ш4), độ chính xác tạo giả
±0,18° / ±0,3 %, độ chính xác chỉ thị mã theo bảng 201–204 của phiếu công nghệ.

**Nghiệm thu (đo được):**

| # | Tiêu chí | Cách chứng minh |
|---|---|---|
| A1 | Thực hiện đủ phiếu công nghệ 1–12 (ПС17-318) và 1–10 (ПС17-319), kết quả đạt/không đạt tự động | chạy trên khối tốt, so với bàn Nga đã sửa (cùng khối, hai bàn, cùng kết quả) |
| A2 | Giả lập ЦВУ: trả ИКО/ИВЧ trong ≤ 17 µs (Bảng 4–5 [A3]); ОЗУ 512 × 18 bit đọc/ghi mọi ô 000–777₈ | đo bằng máy phân tích logic độc lập |
| A3 | Tạo giả góc ±0,18°, tuyến tính ±0,3 %; đo ngược ±0,25° / ±0,35 % (người đàm thoại thực) | so với vôn kế chuẩn |
| A4 | Không bao giờ cấp nguồn sai cực / quá dòng; mọi lệnh ngắt được từ PC và từ nút cứng | thử đảo cực, ngắn mạch tải giả |
| A5 | Báo cáo JSON + JUnit mỗi lần chạy; chỉ ra tấm nghi ngờ theo bảng triệu chứng §Giai đoạn 5 | xem §6 |
| A6 | ~~Hồ sơ kiểm định chính thức~~ **bỏ** (người dùng chốt: không cần kiểm định). Giữ hướng dẫn sử dụng ngắn + nhật ký kiểm tra nội bộ | §6 |

**Ngoài phạm vi:** sửa ПС17-318/319 (nhánh song song của đội khác), lắp lên máy bay, ARINC/1553, kiểm định chính thức, nút/đèn cứng (chỉ GUI PC), dùng cho A313-V.

---

## 2. Kết quả quét thư mục `thiet_bi_kiem_tra_a313/` (4143 file, 1,2 GB)

*(Thư mục đã được copy vào gốc repo ngày 26/10/2026: `<gốc repo>/thiet_bi_kiem_tra_a313/`, nằm ngoài git; mọi tên thư mục con dưới đây là tương đối từ đó.)*

| Nhóm | Nội dung | Dùng thế nào |
|---|---|---|
| Thuyết minh/HDSD ПС17-318, ПС17-319 (bản dịch, `Chỉnh lỗi Font/*.docx`) | chức năng, chế độ, bảng mã, DISS, nguồn thứ cấp, phiếu 1–12, bảng 201–204 | **nguồn yêu cầu** và test vector (§6) |
| `TMKT & HDSD PS17-318V` (361 kB) | thiết kế **BKT-A313V đã có**: 15 kênh tương tự, 2 kênh ПК, 16 lệnh đơn 27 V, 8 TTL, 4 xung 1,3–40 kHz, 5 xung, dải nguồn +5 V/15 A … −23 V; "Altera ASIC + vi điều khiển + 2 PC" | **tiền thân trực tiếp** — kế thừa danh mục chức năng, thay công nghệ |
| `cac duong lien lac 318/319`, `Bang dau cam 319`, `bang dau day - phuong` | bảng đường nối giữa các tấm bàn Nga và bảng chân đầu cắm | đối chiếu pin; sửa bàn Nga |
| `BKT_A313-2A`, `BKT-A313-23` | hồ sơ kiểm định, lý lịch, PKTK-CT của hai bàn đã chế tạo (2011–2012) | **mẫu hồ sơ** nghiệm thu |
| `Sơ đồ/PS17-320V`, `PS17-321V`, `A313-6V` | bàn 320V (bộ nhớ ПЗУ/ОЗУ/ППЗУ), 321V (ЦВУ), khối A313-6V làm bằng FPGA | cách nhóm đã làm FPGA; **320V chỉ dùng cho A313-V** |
| `ban ve Orcad va Layout` (BKT320MOI, so sánh điện áp 320, nguồn 320 2011, danh sách linh kiện) | mạch so sánh điện áp, nguồn, layout | tái dùng mạch so sánh/nguồn nếu kiểm lại đạt |
| `TL Thiet ke PS17-318` (3957 file, 989 MB) | OrCAD/Layout dựng lại **từng tấm** bàn 318 (Y1…Y16, `merge.txt`) | **hướng đã đi**: nhân bản bàn Nga bằng TTL; chưa mở chi tiết |
| `albom a313-3` (74 MB) | album tài liệu | chưa đọc |

**Khoảng trống dữ liệu** (cần trước khi thiết kế mạch): sơ đồ ПС17-319 (Hình 2, 22–32 "sách 1"), giá trị
УИН, sơ đồ УСС ТЖ3.099.001/002/004, xác nhận **hướng/mức/thời gian từng tín hiệu** (Bảng 4–5 [A3]), quan hệ
pha A–C của 36 V 400 Hz; vai trò **A-313-12** đã đọc từ [A3] (ngắt 27 V, báo điện áp ngoài chuẩn) nhưng sơ đồ A-313-12 chưa có.

---

## 3. Giao diện cần phục vụ (từ `A313-3_ket-noi-toan-khoi.xlsx`, số đếm đã đối chiếu 622 điểm Y16)

| Đầu nối khối | Số dây | Nội dung chính | Miền mức / tốc độ |
|---|---:|---|---|
| 3Ш1 | 49 | КШЗП 0–17, КША 7–15, rail +20/+6,3/+5/+10/−6,3/−10/−5 V (nghi là điểm tải УИН, chưa xác nhận); КШЗП/КША/ЗП/ЧТ/ВрМ = **ra khối** ([A3] Bảng 5), mát | TTL 133/136; rail = tải |
| 3Ш2 | 50 | КШЧТ 0–17 + ИВЧ + ИКО (**vào khối**, [A3] Bảng 4), ЧТ УВВ, ЗП УВВ, ВрМ1/2 (ra khối), СБОЙ, ИСПР., ВНЕШН.ПРЕРЫВ ×4, КПА, ЗАПРЕТ ×3, +27 V | TTL, ≤ 17 µs |
| 3Ш7 | 30 | СТРОБ ×4, СчК 0–12, УПР К1–К4, УПР ±20/±12,6/±6,3 V, БЛОКИРОВКА ЗАЩИТЫ | TTL quan sát + điều khiển |
| 3Ш3 + 3Ш3В | 67 + 67 | 16 РК vào (27 V), 15 cặp tương tự 1А…15Б, К1–К3, УПР t1–t4/T1–T4, ВЫХОД 1А…32А (~48 đường), rail ±12,6/−20/+3,5, Uоп = 4 V | tương tự ±8 V, 400 Hz; 27 V |
| 3Ш4 | 67 | РК ra 1–16 (+27 V), 17–32 (khoá), 35И/36И/ЗАПРОС Д1,2/ДИ, ИСПР., +27 V Б/С, ~36 V 400 Hz фаза А/С | 27 V; xung; **nguồn khối** |
| 3Ш4В | 67 | ПК ×4 kênh (ПК, СИ, ¬СВК, ¬СПК, 80 kHz), ПК ЦИ, 7 РК TTL, F1–F4 | TTL, 80 kHz |

Tổng ≈ **360 dây tín hiệu** trên 5 đầu nối (3Ш5 là nguồn nội bộ, không nối bàn).
Ước lượng theo lớp (±15 %): số TTL tốc độ trung bình ≈ 165; tương tự kích thích 30 + 9; tương tự đo ≈ 48 + 11 rail + ~10 điểm kiểm;
rời rạc 27 V: 16 ra khối + 32 vào bàn; xung/tần số ≈ 10.

---

## 4. Đánh giá phương án "board FPGA Artix-7 + chuyển mức + ngoại vi"

**Kết luận: đúng hướng làm lõi, nhưng một mình A7-Lite + chuyển mức chưa đủ. Cần thêm 3 khối ngoại vi
và một carrier.** Nó cũng khớp kế hoạch hiện hành (§3–4 KE-HOACH) và tái dùng được nhiều thứ từ dự án ARINC429_ATS.

### 4.1. Cái nó làm tốt
- **Giả lập ЦВУ** (thay ПС17-319 phần số): ОЗУ 512 × 18 bit chỉ 9 kbit (A7-Lite 35T có 1 800 kbit BRAM). Phản hồi ≤ 17 µs chỉ FPGA làm được, PC thì không.
- **Bộ đếm/thời gian** thay ИНД1/ИНД2 và đồng bộ máy hiện sóng: chốt thời điểm bằng phần cứng, ghi timestamp.
- **Máy phát F1–F4 (1,3–40 kHz), xung 35И/36И, ЗАПРОС Д, vòng ПК** — bộ chia số, không cần thêm linh kiện.
- **Đường truyền PC–FPGA đã có**: PROTO2/UDP chạy trên chính A7-Lite (485 000/485 000 gói, 0 lỗi FCS, ARINC429_ATS N0–N2).

### 4.2. Cái nó **không** làm được một mình
| Thiếu | Hệ quả | Cách bù |
|---|---|---|
| **Số chân**: A7-Lite có 2 × 50 chân, **88 GPIO** (44 + 44; JP1 chỉnh 1,2–3,3 V, JP2 3,3 V cố định); ≈ 165 dây TTL + 48 RK. **P1 (3Ш1 + 3Ш2) cần 70 chân trực tiếp, hoặc 52 nếu 18 đường chậm đi qua mở rộng**; toàn bàn vượt 88 | P1 vừa; toàn bàn cần mở rộng chậm hoặc SoM (§5.2) | không dựa vào "250 I/O" của chip, đó là số của vỏ, không phải của board |
| **Mức 5 V TTL ↔ 3,3 V**: khối đầu ra 133/136, vào cần dòng ≥ 1,6 mA/đầu vào, UUT có thể bị kéo ngược | LVC trực tiếp có thể không đủ; bàn Nga dùng 133ЛА6 + 100 Ω | 74LVC/AHCT 5 V-tolerant + 100 Ω nối tiếp, đệm 2 chiều có OE riêng |
| **Tương tự**: 30 + 9 kích thích ±8 V, 400 Hz; ~70 kênh đo; chính xác 0,3 % | FPGA không có DAC/ADC | DAC 16 bit đa kênh + ADC 16 bit đồng thời; xem §5.3 |
| **27 V**: 16 RK vào khối, 32 RK ra khối (16 nguồn 27 V, 16 khoá) | không nối trực tiếp | cách ly quang/số + MOSFET cao áp; RK vào khối cần 3 mức theo bàn Nga: 27 V (+2,7/−5,4), (1,7 ± 0,12) V, (0,8 ± 0,08) V; RK ra khối cần so sánh có ngưỡng chỉnh được |
| **Nguồn**: +27 V điều chỉnh, ~36 V 400 Hz hai pha | A7-Lite không tạo | nguồn có lập trình + bộ khuếch đại công suất 400 Hz đồng bộ DDS |
| **Điều khiển/hiển thị** (ИНД, trường đặt, ~60 nút) | không cần phần cứng | PC GUI (tái dùng khuôn PySide6) |

### 4.3. Phương án so sánh

| Phương án | Ưu | Nhược | Đánh giá |
|---|---|---|---|
| **A. A7-Lite + carrier tự làm + khối tương tự/27 V/nguồn** (đề xuất) | một FPGA, ít tấm; kế thừa ATS (Ethernet, GUI, báo cáo); 88 GPIO đủ cho tầng A | số chân sát giới hạn; cần carrier | **chọn** |
| B. SoM Artix-7 (có trong thư viện Altium của nhóm: `SOM_A7_200T`) | nhiều chân hơn (cần kiểm datasheet SoM) | cần thiết kế mạch đế đầy đủ; chưa kiểm | dự phòng nếu hết chân |
| C. STM32 + CPLD | quen thuộc, rẻ | 50 chân bus ≤ 17 µs và đồng bộ 400 Hz khó; mất ЦВУ real-time | không |
| D. Nhân bản ПС17-318/319 bằng TTL (như `TL Thiet ke PS17-318`) | giữ nguyên nguyên lý Nga | hàng chục tấm TTL, khó bảo trì, 989 MB tài liệu đã đi nửa chừng | không, chỉ lấy mạch tương tự đã có |
| E. Zynq-7020 (AC7020C, nhóm đã có) | có ARM chạy sequencer | thêm độ phức tạp Linux/PS; chưa cần | để sau nếu cần chạy độc lập không PC |

**Bài học từ ATS cần áp dụng ngay:** (i) chạy fit/map trên đúng chip trước khi viết RTL phần lớn (A7-Lite 35T nhỏ, M3-B
map cần 68 600 B, vượt LMB 3 064 B → **không dùng MicroBlaze làm bộ điều khiển**, để PC làm sequencer);
(ii) **lõi TEMAC của nhóm dùng IP có license mua** → kiểm `REQUIRES_LICENSE` trên máy dựng, hoặc dùng
`verilog-ethernet` (MIT) đã được đề xuất; (iii) giới hạn phần cứng lấy từ **sơ đồ của mọi board trên đường tín hiệu**
(kể cả A7-Lite R11 và carrier).

---

## 5. Kiến trúc đề xuất

### 5.1. Sơ đồ khối (thay từng hộp trong Рис. 201)

| Hộp cũ | Thay bằng |
|---|---|
| ПС17-319 (phần số: ЦВУ, ПК, РК, nguồn, ИНД) | **M1** FPGA A7-Lite + **M5** đệm TTL + **M6** nguồn + **M4** 27 V + PC GUI |
| ПС17-318 (tương tự: СКТ, АЗУ, ДИСС, БВК, rail) | **M2** kích thích + **M3** đo + F1–F4 trong M1 |
| УСС ×3 (đệm/ghép) | gộp vào **M5** (có thể dùng lại УСС nếu còn tốt) |
| УИН (tải rail) | **M7** tải điện trở chuyển bằng rơle, có đo dòng |
| Cáp ТЖ4.853.xxx | giữ nếu còn, hoặc cáp mới 67/50 chân |
| A-313-12 (bảo vệ/ngắt 27 V, báo НАПР.ВЫШЕ/НИЖЕ НОРМЫ, nhận ОТКЛ) | **M8** (§5.5): rơ-le/MOSFET ngắt 27 V + cờ GUI |
| A-313-6/6M (bảng điều khiển, hiển thị, ПК ra/vào, 12 lệnh TTL) | **M9** (§5.5): máy trạng thái ПК trong FPGA + bảng ảo trên GUI |
| A-313-7 (mở rộng đầu vào 11→23 СКТ, 4→8 DC, 16→32 РК) | **M10** (§5.5): không cần cho A-313-3 đơn lẻ; mở rộng kênh M2 nếu sau này cần |

### 5.2. Ba tầng chân FPGA (ước ≈ 85 chân trực tiếp, còn lại qua mở rộng)

| Tầng | Tín hiệu | Cách nối | Chân FPGA |
|---|---|---|---:|
| **A — thời gian thực (µs)** | КШЗП 18 (ra khối), КША 9 (ra khối), КШЧТ 18 (vào khối), ЗП/ЧТ УВВ, ИКО, ИВЧ, ВрМ1/2, ПРИНУД = **52**; **hai nhóm dây riêng, không dùng chung bus** ([A3] Bảng 4–5) | đệm một chiều (ra khối: LVC; vào khối: 5 V + 100 Ω) | **52** |
| **B — ПК và xung (80 kHz, F1–F4)** | 4 kênh × 5 dây, ПК ЦИ, F1–F4, 35И/36И/ЗАПРОС Д ≈ 30–35 | đệm một chiều; có thể qua mở rộng quét ≥ 1 MHz (80 kHz, 40 kHz đủ chậm) | 0–35 |
| **C — chậm (RK, 3Ш7, 18 đường chậm 3Ш2, ngắt, quan sát)** | ≈ 90 dây + 18 + 22 | SPI mở rộng 16 bit + chốt (quét ≤ 50 µs) | 4–6 |
| Tương tự + nguồn | DAC/ADC/nguồn | SPI | ≈ 12 |
| Dự phòng | — | — | 18 nếu B qua mở rộng; nếu B trực tiếp (35) thì **vượt 88** |

⇒ **P1 vừa với A7-Lite (70 chân, hoặc 52).** Toàn bàn vừa nếu tầng B/C đi qua mở rộng; nếu B phải đi trực tiếp thì chuyển SoM (phương án B của §4.3) hoặc thêm FPGA thứ hai. Quyết định ở P0-b.

### 5.3. Tương tự (khối khó nhất, 6–8 tuần)

- **Kích thích**: 15 cặp a/б = U·sin α, U·cos α, tải 400 Hz đồng bộ pha với 36 V 400 Hz (tích phân của khối cần đồng bộ). Hai chế độ sóng mang: **sin** và **meander** (công tắc МОДУЛ trên bàn Nga) → DAC 16 bit cập nhật ≥ 20 kS/s hoặc dùng meander điều chế bằng DAC DC.
  Ước lượng 30–39 đường; **chỉ cần giữ tín hiệu ở đúng kênh khối đang quét**, vì kênh chọn bằng t/T/K của khối. Có thể dùng 8 nguồn + ma trận 48 kênh như bàn Nga, hoặc 15 nguồn riêng. **Quyết định ở P0.**
- **Đo**: ≈ 48 đầu ra ВЫХОД + 11 rail + ~10 điểm → ≈ 70 kênh, ADC 16 bit đồng thời (1 LSB ≈ 0,3 mV trên ±10 V; yêu cầu 0,3 % của 8 V = 24 mV, dư ≥ 10×), giải điều chế 400 Hz trong FPGA (lock-in). Tải ≥ 3 kΩ trên mỗi đầu ra ([A2] Hình 104).
- **Tự hiệu chuẩn**: vòng DAC → ADC (thay chế độ СК của ПС17-318: mã 131520–132600 / 531520–532600).
- Linh kiện cụ thể (họ DAC/ADC) **chưa chọn**; chọn ở P3 sau khi kiểm tồn kho, giá, tầm với (xuất xứ), mức nhiệt.

### 5.4. An toàn (bắt buộc)
1. Mọi đầu ra RK 27 V và nguồn có **giới hạn dòng + tắt khi mất liên lạc PC** (watchdog).
2. Không đo/đổi cáp khi có điện (đúng HDSD gốc §10); dây tiếp mát khối ТЖ4.863.026-01 trước khi cắm; chống tĩnh điện.
3. Bàn không bao giờ kéo ngược các đầu ra 27 V của khối (3Ш4): điện trở nối tiếp + kẹp.
4. Khối A-313-3 chưa rõ có bảo vệ ngược cực → bàn có bảo vệ ngược cực và khởi động mềm.
5. Sơ đồ ghi nhận **dòng 27 V ≤ 18 A** (HDSD ПС17-319) nhưng chú thích Рис. 201 ghi **≥ 100 A, 16–40 V**: mâu thuẫn, phải làm rõ ở P0 (có thể 100 A là cho cả tổ hợp).

### 5.5. Thay thế các khối đi kèm (quyết định 26/10/2026: một bàn, không ghép khối thật)

| Khối thật | Vai trò với A-313-3 (nguồn) | Mô-đun thay | Cách làm | Khi nào |
|---|---|---|---|---|
| **A-313-12** | ngắt điện áp mạng 27 V khi khối phát ОТКЛ (hỏng nguồn thứ cấp); phát НАПРЯЖЕНИЕ ВЫШЕ/НИЖЕ НОРМЫ về khối ([A3] mô tả hệ thống nguồn, tr. =52=…); 12Ш1 dùng chung cáp Ш4 (Рис. 201) | **M8** | công tắc 27 V (MOSFET/rơ-le) trong bàn, điều khiển bởi ОТКЛ của 3Ш4 (qua đệm cách ly) **và** nút ngắt cứng; **đọc** НАПР.ВЫШЕ/НИЖЕ НОРМЫ (3Ш2/36, 37) — đây là đầu ra của tấm Y24 trong khối, không phải cờ bàn đặt (đã xác minh 26/10, P1 §9.1); đo dòng + điện áp 27 V để GUI hiện | P2 |
| **A-313-6 / 6M** | bảng thao tác: nhập chương trình bay, hiển thị tham số; trao đổi **từ ПК 20 bit** (khối nhận 4 từ УП0–УП3, phát 4 từ СП0–СП3) qua kênh ПК + 12 lệnh một lần TTL ([A1] Bảng 1; `Sơ đồ/A313-6V/Phuongan A313-6V.doc`) | **M9** | máy trạng thái ПК trong FPGA (dùng chung với bộ tạo ПК của ПС17-319); **bảng ảo trên GUI** thay 16 nút, đèn, chỉ thị số; 12 đầu ra TTL qua đệm. Nhóm đã có thiết kế A313-6V bằng FPGA → tái dùng định dạng từ | P3 (ПК), P4 (GUI) |
| **A-313-7** | khi nối thêm: СКТ xoay chiều 11→23, một chiều 4→8, lệnh 27 V 16→32 ([A1] Bảng 1); repo không có sơ đồ A-313-7 | **M10** | **không cần** để kiểm A-313-3 đơn lẻ (3Ш3 đã có 15 cặp 1А…15Б + К1–К3). Nếu cần sau này: thêm kênh DAC vào M2 sau khi đọc sơ đồ A-313-7 | sau P3, tuỳ chọn |

**Ghép khối thật?** Có thể và tốt hơn cho **kiểm cuối** (đối chứng đầu–cuối), nhưng không nên là điều kiện: tình trạng A-313-2A/12/6M/7 chưa rõ (KE-HOACH §5.1), nên
chế độ chính là mô phỏng; khối thật chỉ cắm song song khi cần xác nhận. Vì 12Ш1 dùng chung cáp Ш4, M8 phải có chế độ "bỏ qua" (nhả rơ-le bàn khi A-313-12 thật được cắm) để
không hai thiết bị cùng ngắt nguồn.

### 5.6. Thứ tự làm (quyết định 26/10/2026: P1 trước)

P1 (giả lập ЦВУ + đệm TTL) làm riêng, đặc tả tại **`P1_GIA-LAP-CVU_BAN-KIEM-TRA-A-313-3.md`**. M8 vào P2, M9 vào P3/P4, M10 để sau.

---

## 6. Phần mềm và kiểm tra

- **Sequencer ở PC**, FPGA chỉ có thanh ghi (không soft CPU): lệnh có khung + CRC, session, mailbox (tái dùng `framed-command-mailbox`, `crc-framed-stream-parser`, PROTO2 UDP).
- **Số hoá phiếu công nghệ** thành bảng test: bảng 201 (rail → mã), 202 (thu ПК: КОД1–4, địa chỉ 4…37), 203 (ОЗУ 000–037 → mã), 204 (ПУ/Д), bảng 12.2–12.5 (DISS, mã nguồn thứ cấp −23 … +20 V, dấu thời gian 135530–135630), dung sai ±15 %, mức logic "0" ≤ 0,4 V / "1" ≥ 2,4 V.
- **Bảng triệu chứng → tấm** lấy từ KE-HOACH §Giai đoạn 5 (Y4, Y3, Y5→Y14/Y15, Y6→Y8, Y11/Y10, Y9, Y12/Y13, Y1, Y2).
- **Kiểm chéo bắt buộc**: cùng một khối chạy trên bàn mới và trên ПС17-318/319 đã sửa; "chữ ký khối tốt" lưu JSON (dòng 27 V, rail, ô 013₈ và 227₈, bản ghi logic).
- Tái dùng JARVIS: `qt-engine-worker-replay` (GUI), `json-junit-run-report`, `evidence-json`, `guarded-test-round-engine` (có khoá, permit, journal), `offline-hardware-fence` (chạy GUI không chạm phần cứng khi dev). Không cần boundary-scan cho A-313-3 (không có JTAG).

---

## 7. Lộ trình và mốc (ước lượng, 1–2 kỹ sư)

| Mốc | Nội dung | Thời gian | Điều kiện hoàn thành |
|---|---|---:|---|
| **P0** | **P0-a (cho P1, ≈ 1 tuần):** ảnh Hình 8/3/4/7, HDSD A-313-2A, đo thật ЗП/ЧТ, hướng 3Ш2 chậm, mâu thuẫn ИКО. **P0-b (cho P2–P3, sau):** hình ПС17-319, УИН, УСС; 8 hay 15 nguồn; pha A–C; dòng 27 V; kiểm A7-Lite R11 | 1 + 2 tuần | P0-a: bảng chân 3Ш1/3Ш2 có hướng đã xác minh |
| **P1** (làm trước) | Giả lập ЦВУ + đệm TTL + PC tối giản; chi tiết ở `P1_GIA-LAP-CVU_BAN-KIEM-TRA-A-313-3.md` | **5–7 tuần** (Rev. A ghi 3–4; nới vì cần mạch đế và ảnh Hình 8) | A2 đạt, P1-1…P1-6 đạt, giai đoạn 2–3 KE-HOACH chạy được |
| **P2** | Nguồn 27 V có lập trình, 36 V 400 Hz đồng bộ, RK 27 V, УИН | 3–4 tuần (song song P1) | A4 đạt; khối lên nguồn an toàn |
| **P3** | Kích thích 30–39 + đo ~70 + tự hiệu chuẩn | 6–8 tuần | A3 đạt |
| **P4** | Sequencer, GUI, số hoá phiếu, báo cáo (chồng lấp P1–P3) | 4–6 tuần | A1, A5 đạt |
| **P5** | PCB tích hợp + vỏ + cáp | 4–6 tuần (gồm chế tạo) | bàn lắp hoàn chỉnh |
| **P6** | Kiểm chứng: khối tốt (+ so với bàn Nga nếu đã sửa); hướng dẫn sử dụng ngắn, không hồ sơ kiểm định | 2–3 tuần | A1–A5 đạt |

Tổng ≈ 25–35 tuần-người; khoảng **5–8 tháng** lịch với 1 kỹ sư, 4–5 tháng với 2. Giá trị sớm nhất: sau P1 đã thay được phần số của ПС17-319, dùng ngay cho KE-HOACH giai đoạn 2–3.

---

## 8. Rủi ro

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Hết chân A7-Lite | cao | tầng C qua SPI; kiểm lại ở P0; dự phòng SoM |
| Hình 8 (thời gian ИВЧ/ИКО/КША) mất hình trong [A3]; ИКО nằm cả ở Bảng 4 (vào) và Bảng 5 (ra) | **cao cho P1** | đo thật bằng máy phân tích logic trước khi nối bàn; xin ảnh giấy Hình 8 (P1 §3) |
| Tương tự không đạt 0,3 % (nhiễu, đồng bộ pha 400 Hz) | cao | tự hiệu chuẩn vòng kín, nguồn tương tự tách riêng, kiểm sớm ở P3 |
| Đầu nối РПКМ3-67/РС50 khó mua | trung bình | dùng lại cáp bàn Nga; hỏi nguồn đầu nối ngay P0 |
| License IP Ethernet | thấp–trung bình | kiểm `REQUIRES_LICENSE` hoặc dùng IP MIT |
| Dữ liệu sơ đồ ПС17-319 không đủ | cao | không cần sơ đồ để làm bàn mới, nhưng cần để **đối chứng**; xin đội sửa bàn |

---

## 9. Quyết định của người dùng (26/10/2026) và việc còn lại

| # | Câu hỏi | Trả lời | Hệ quả |
|---|---|---|---|
| 1 | Dùng cho A-313-3 và A313-V? | **Chỉ A-313-3** | bỏ yêu cầu bảng chân A313-V |
| 2 | Kiểm định chính thức? | **Không** | bỏ A6, bỏ thiết bị chuẩn, bớt ≈ 4 tuần |
| 3 | Chỉ GUI PC? | **Chấp nhận** | không nút/đèn cứng; giữ một nút ngắt khẩn cứng |
| 4 | Số bàn / ghép khối? | **1 bàn; không ghép → phương án thay A-313-12/6M/7**; ghép được thì tốt hơn | §5.5; ghép khối thật là tuỳ chọn |
| 5 | Làm gì trước? | **P1** | `P1_GIA-LAP-CVU_BAN-KIEM-TRA-A-313-3.md` |

**Trả lời bổ sung (26/10/2026):** thiếu tư liệu → chỉ tận dụng cái đang có; nguồn máy bay đầy đủ, giới hạn dòng tuỳ ý (nguồn không còn là hạn chế, bỏ ghi chú mâu thuẫn 27 V ≤ 18 A / ≥ 100 A khỏi đường găng); **chưa đặt mạch**, lập bảng chân + kế hoạch chi tiết, đủ điều kiện (cổng G1–G5) mới đặt.
Bảng chân: `P1_BANG-CHAN_BAN-KIEM-TRA-A-313-3.md`. Kế hoạch chi tiết và cổng khả thi: `P1_GIA-LAP-CVU…md` §9.

**Còn mở:** (a) khối A-313-3 còn chạy được không; (b) cáp/УСС trên bàn ПС17-318/319 hỏng còn nguyên không.
