# P1 — GIẢ LẬP ЦВУ (A-313-2A) + ĐỆM TTL CHO BÀN KIỂM TRA A-313-3 MỚI

**Rev. B — 26/10/2026.** Chi tiết hoá mốc P1 của `KE-HOACH_BAN-KIEM-TRA-MOI_A-313-3.md` (Rev. B). Chưa có thiết kế
mạch, chưa có phép đo phần cứng. Bảng chân: `tmp/pdfs/review/ban-kiem-tra/p1_pinout.csv` (sinh bằng
`p1_pinout.py` từ `A313-3_ket-noi-toan-khoi.xlsx`). Nguồn hành vi: [A3] = `A313 original/A-313-3.HDSDKT.pdf`.

---

## 1. Mục tiêu và phạm vi

**Làm gì.** Một bộ thay **phần số của ПС17-319 ở vai ЦВУ/A-313-2A** khi cấp nguồn cho A-313-3 và theo dõi khối:
1. đóng vai A-313-2A trên 3Ш1/3Ш2: nhận КШЗп/КША/ЗпУВВ/ЧтУВВ, trả КШЧт/ИВЧ/ИКО đúng thời gian;
2. ОЗУ 512 × 18 bit (КША 7–15р = 9 bit = 512 ô) đọc/ghi từ PC; ghi nhật ký mọi truy cập có nhãn thời gian;
3. điều khiển các đường điều khiển của ПС17-319 trên 3Ш2 (ЗАПРЕТ.ОБРАЩ./ВРМ/РМ, ПРИНУДИТ.ЗАПУСК, Рг К1/К2/М КПА, ЗП.КПА…);
4. quan sát СчК, СТРОБ trên 3Ш7 (chữ ký khối tốt).

**Không làm trong P1:** tương tự (3Ш3), 27 V RK (3Ш4), nguồn có lập trình, ПК/F1–F4 (3Ш4В). Cấp nguồn khối bằng
**nguồn phòng thí nghiệm có sẵn** (27 V, 36 V 400 Hz), người vận hành bật tay; GUI chỉ đọc/ghi số.

**Điều kiện kích hoạt:** thực hiện các phiếu kiểm tra phần số của [A3]/KE-HOACH giai đoạn 2–3 mà không cần ПС17-319.

---

## 2. Giao diện (đếm từ `p1_pinout.csv`)

| Đầu nối | Tín hiệu số | Hướng (từ khối) | Căn cứ | Ghi chú |
|---|---:|---|---|---|
| 3Ш1 | 27 | КШЗП 0–17р (18) **ra**, КША 7–15р (9) **ra** | [A3] Bảng 5 | còn lại là mát ×9 và rail ×14 (không nối FPGA) |
| 3Ш2 | 18 + 7 | КШЧТ 0–17р **vào**; ¬ИВЧ, ¬ИКО **vào**; ¬ЧТ УВВ, ¬ЗП УВВ, ¬ВрМ1, ВрМ2 **ra** | [A3] Bảng 4–5 | 7 = ИВЧ, ИКО, ЧТ, ЗП, ВрМ1, ВрМ2, ПРИНУДИТ.ЗАПУСК(?) |
| 3Ш2 (chậm) | 18 | СБОЙ, ВНЕШН.ПРЕРЫВ ×4, ПРЕДВАРИТ.ОТКАЗ, ИСПР.ПИТАНИЯ ЦВУ, НАПР.ВЫШЕ/НИЖЕ НОРМЫ, ИСПРАВН.ПИТ.ППЗУ, Рг К1/К2/М КПА, ЗП.КПА, ЗАПРЕТ ×3, ВХОД ПР."П" ТТЛ | **hướng chưa có căn cứ** | quyết định theo Э4 hoặc đo |
| 3Ш2 | 2 | +27 В (33, 34) | — | **không nối vào bàn P1** cho tới khi biết hướng/nguồn |
| 3Ш7 | 22 | СТРОБ ×4, 0–12р СчК (13), УПР К1–К4 (4), БЛОКИРОВКА ЗАЩИТЫ (1); 7 chân Упр.(±5/−6,3 В) và УПР rail không nối FPGA | chưa xác minh | quan sát, qua mở rộng chậm |

**Tổng chân FPGA trực tiếp P1:** 3Ш1 27 + 3Ш2 nhanh 25 (18 КШЧТ + 7 điều khiển/xung) + 3Ш2 chậm 18 = **70** (A7-Lite có 88 GPIO) → còn 18; 3Ш7 (22) và
điều khiển PC/ADC đi qua mở rộng SPI. Nếu hướng 3Ш2 chậm cho phép, 18 đường chậm cũng chuyển sang mở rộng → trực tiếp chỉ **52**.
**Sửa so với bản kế hoạch trước:** КШЗП và КШЧТ là hai nhóm dây riêng (18 + 18), **không** dùng chung bus 18 bit như tôi giả định ở Rev. A.

---

## 3. Hành vi cần mô hình hoá (từ [A3])

| # | Hành vi | Giá trị | Nguồn / tình trạng |
|---|---|---|---|
| H1 | Mức logic loạt 133/136: "1" = 2,4–4,5 V, "0" = 0–0,35 V | đầu ra bàn phải đạt ≤ 0,35 V ở mức thấp | [A3] §2.3, đã đọc |
| H2 | Khối là bên **chủ động**: phát ¬ЗП УВВ / ¬ЧТ УВВ + КША (+ КШЗП khi ghi) | tần suất theo СчК 4700 µs/chu kỳ, 8 thao tác × 588 µs | [A3] §2.2.1; KE-HOACH GĐ2 |
| H3 | Bàn trả ¬ИВЧ khi **đọc**, dùng làm cổng ghi КШЧТ vào thanh ghi | rộng ≈ 0,5 µs (đọc từ chữ ở Hình 8) | **Hình 8 mất hình, chỉ còn chữ → chưa chắc** |
| H4 | Bàn trả ¬ИКО khi kết thúc chu kỳ ghi/đọc | ≤ 17 µs sau ЗП/ЧТ; khi không có ИКО khối tự xoá yêu cầu sau 24 µs | [A3] Hình 8 (chữ), KE-HOACH GĐ2 |
| H5 | КШЧТ phải ổn định ≥ 0,25 µs quanh ИВЧ; КША ≈ 1 µs | số đọc từ chữ Hình 8, **không dùng làm số thiết kế** | cần ảnh Hình 8 |
| H6 | Bít chẵn lẻ КШЗП 16р/17р: tổng "1" **lẻ** cho 8 bit cao (0–7) và 8 bit thấp (8–15) | kiểm trên mọi chu kỳ ghi | [A3] §2.3 |
| H7 | ¬ВрМ1/ВрМ2 là vạch thời gian đồng bộ với КЦ | bàn chỉ đo, ghi nhãn thời gian | [A3] Bảng 5 |

**Mâu thuẫn dữ liệu cần chốt:** [A3] Bảng 4 liệt kê ИКО là **vào** khối, Bảng 5 cũng liệt kê ИКО là **ra** khối. §2.3 viết "khi kết thúc chu kỳ
A-313-2 đưa ra ИКО". Giả thiết làm việc: ИКО là **vào** khối (từ bàn); mục ra ở Bảng 5 là lỗi in. Chưa có ảnh sơ đồ để chứng minh.

**Cần thêm trước khi đóng cứng thời gian (việc P0-a, ≈ 1 tuần):**
1. Ảnh giấy **Hình 8** (biểu đồ trao đổi A-313-3 ↔ A-313-2) và **Hình 3**/**4**/**7** nếu có — `A313-3.HDSDKT.pdf` mất toàn bộ hình, KE-HOACH đã ghi nhận.
2. HDSD A-313-2A `И13.031.009-01 РЭ` (110.23.02), phía bus ОЗУ — để biết mức và thời gian thực của ИКО/ИВЧ từ phía bên kia.
3. Đo thực trên khối (máy phân tích logic ≥ 32 kênh theo KE-HOACH GĐ2) **trước** khi nối bàn vào: ghi thời gian thật ЗП/ЧТ/КША.

---

## 4. Phần cứng P1

| Khối | Chọn | Ghi chú |
|---|---|---|
| FPGA | A7-Lite XC7A35T (88 GPIO: JP1 44, JP2 44; JP1 chỉnh 1,2–3,3 V, JP2 3,3 V; 50 MHz) | đã có (ARINC429_ATS) |
| Đế | **Mạch đế mới** | **không dùng** board `0123_system` của ARINC429_ATS: GPIO1/GPIO2 đã bị ARINC/RS-422/LED/SW/SoM dùng, chỉ 10 chân trống (JARVIS) |
| Đệm khối→bàn (ra khối: КШЗП, КША, ЗП, ЧТ, ВрМ) | họ LVC cấp 3,3 V, đầu vào chịu 5 V, điện trở nối tiếp | đầu ra khối loạt 133/136 có "1" 2,4–4,5 V; kiểm datasheet đúng chip trước khi chốt Vih/Vcc (chưa tra trong lần này) |
| Đệm bàn→khối (КШЧТ, ИВЧ, ИКО) | đệm cấp 5 V (họ AHCT/HCT), 100 Ω nối tiếp (bàn Nga dùng 133ЛА6 + 100 Ω theo thuyết minh ПС17-319) | khối chịu tải TTL; "1" ≥ 2,4 V, không vượt 4,5 V; lý do dùng 5 V: Voh của đệm 3,3 V sát ngưỡng 2,4 V khi tải |
| Chậm (3Ш2 phần chậm, 3Ш7) | thanh ghi dịch/mở rộng SPI | quét ≥ 1 MHz |
| Kết nối | cáp 50 chân ×3 (3Ш1, 3Ш2, 3Ш7); chỉ nối các chân đã lập bảng; **không nối mát khối ↔ mát bàn qua chân rail** | dùng lại cáp bàn Nga nếu còn và xác nhận bảng chân bằng thông mạch |
| PC | UART trước (115200→921600), sau đó PROTO2/UDP nếu cần tốc độ | tái dùng ATS: CRC16 khung, framed mailbox |

**An toàn P1 (cứng):**
1. Lần đầu nối: **chỉ quan sát** (đệm bàn→khối ở Hi-Z, OE tắt cứng bằng thanh nhảy), nguồn khối bật bằng nguồn phòng thí nghiệm có giới hạn dòng (đặt theo dòng tiêu thụ ở HDSD; bộ A-313 hoàn chỉnh ≤ 11 A, riêng A-313-3 chưa có số).
2. Chỉ bật OE bàn→khối sau khi đã xem КШЗП/КША/ЗП/ЧТ đúng dạng và biên độ.
3. Mọi chân trùng với rail/27 V (3Ш1 rail, 3Ш2 +27 V) **không đi qua đệm**; kiểm bằng thông mạch trước khi cắm.
4. Dây tiếp mát khối ТЖ4.863.026-01 trước khi cắm cáp (HDSD); chống tĩnh điện; không cắm/rút khi có điện.

---

## 5. Kiến trúc FPGA (thanh ghi, không có CPU mềm)

Bài học ATS: bản dựng M3-B cần 68 600 B, vượt LMB 3 064 B → để PC làm sequencer.

```
pins ──► io_sync (2FF + lọc xung < 40 ns) ──► bus_slave ──► ram512x18 ◄─► reg_if ◄─► UART/UDP ◄─► PC
                                   │             │              ▲
                                   │             └─► access_log (FIFO 4 k, timestamp 100 MHz)
                                   └─► tb_monitor (СчК, СТРОБ, ВрМ) ──► log
ctrl_out (ЗАПРЕТ, ПРИНУД, Рг К1/К2/М КПА) ◄── reg_if
fault_inject: bỏ ИКО / trễ ИКО / sai bít chẵn lẻ КШЧТ / ИВЧ quá ngắn  ◄── reg_if
```

- Đồng hồ: 50 MHz của A7-Lite → PLL 200 MHz cho bộ đếm thời gian (độ phân giải 5 ns); logic bus ở 100 MHz.
- `bus_slave`: bắt sườn ¬ЗП/¬ЧТ, chốt КША, trong ≤ 1 µs trả ИВЧ/КШЧТ (đọc) hoặc nhận КШЗП (ghi); phát ¬ИКО sau một độ trễ **chỉnh được** (mặc định 2 µs; mục tiêu ≤ 17 µs, đóng cứng sau P0-a).
- `ram512x18`: 1 BRAM18; PC đọc/ghi qua cổng thứ hai; có chế độ "kịch bản": ô trả giá trị nạp sẵn (thay cho "mã tạo giả" của ПС17-319).
- `access_log`: mỗi bản ghi = {thời điểm, loại ghi/đọc, КША, КШЗП hoặc КШЧТ, cờ chẵn lẻ, cờ thời gian}. PC rút ra theo khung CRC16.

**Thanh ghi (nháp, đóng lại ở review):**

| Địa chỉ | Tên | R/W | Nội dung |
|---|---|---|---|
| 0x00 | ID/VER | R | mã bản + hash |
| 0x04 | CTRL | RW | enable_drive, run, soft_reset, log_en |
| 0x08 | DLY_IKO | RW | độ trễ ИКО (đơn vị 5 ns) |
| 0x0C | WIDTH_IVCH | RW | độ rộng ИВЧ (5 ns) |
| 0x10 | FAULT | RW | bit: no_iko, late_iko, bad_parity, short_ivch |
| 0x14 | OUT_CTRL | RW | bit: ЗАПРЕТ.ОБРАЩ./ВРМ/РМ, ПРИНУД, Рг К1/К2/М, ЗП.КПА |
| 0x18 | IN_STAT | R | СБОЙ, ПРЕРЫВ ×4, ПРЕДВ.ОТКАЗ, ИСПР ×3, НАПР ×2 |
| 0x20–0x3C | MEM_ADDR/DATA/MODE | RW | truy cập ОЗУ 512 × 18 |
| 0x40 | LOG_CNT | R | số bản ghi chưa đọc |
| 0x44 | LOG_POP | R | lấy bản ghi |
| 0x48 | TS_NOW | R | bộ đếm thời gian |
| 0x50–0x5C | TB_STAT | R | СчК, СТРОБ, ВрМ |

---

## 6. Xác minh

1. **Mô hình khối bằng Python** (`bus_master_model.py`): phát ЗП/ЧТ theo chu kỳ 4700 µs, 8 thao tác × 588 µs, kiểm lại phản hồi của RTL ≤ 17 µs, chẵn lẻ, sự kiện lỗi. Mô hình là **giả định** cho tới khi có đo thật.
2. **Mô phỏng RTL** (Vivado xsim): kiểm: ghi/đọc mọi ô 000–777₈; ИКО trễ 0…20 µs → khối "tự xoá 24 µs"; chẵn lẻ sai bị bắt; log đúng thứ tự.
3. **Bài kiểm tay viết, bất đối xứng** (bài học ATS): vector tay, không sinh từ chính mã đang kiểm.
4. **Fit sớm** trên XC7A35T: kiểm LUT/BRAM trước khi viết GUI.
5. **Trên khối thật, theo 4 bước (không bước nào bỏ):**
   - T1 quan sát thuần: cấp nguồn, đo КШЗП/КША/ЗП/ЧТ bằng máy phân tích logic độc lập, so với log của bàn;
   - T2 bật OE trả КШЧТ/ИВЧ/ИКО, ghi ô 225₈/226₈ → đo 32 đầu ra RK (cần P2; trước đó chỉ xem KШЗП);
   - T3 chạy phiếu "kiểm tra thu/phát mã nối tiếp" khi có P3; P1 chỉ đạt phần ghi/đọc ОЗУ;
   - T4 so với khối đã biết tốt hoặc bàn ПС17-319 sau khi sửa (chưa có → ghi "chưa đối chứng").

**Tiêu chí P1 đạt (đo được):**

| # | Tiêu chí | Cách chứng minh |
|---|---|---|
| P1-1 | ИКО/ИВЧ ≤ 17 µs, sai số cấu hình ≤ 50 ns | máy phân tích logic độc lập, 10⁶ chu kỳ không lỗi |
| P1-2 | Đọc/ghi 512 ô đúng, PC so từng ô | script vòng 100 lượt |
| P1-3 | Phát hiện chẵn lẻ sai và thiếu ИКО | chèn lỗi qua FAULT, kiểm log |
| P1-4 | Log không mất ở tốc độ thật (8 thao tác/4700 µs liên tục 1 h) | đếm ngược FIFO, báo `drop = 0` |
| P1-5 | Đệm không kéo khối ra ngoài mức quy định | đo Vol ≤ 0,35 V, Voh ≥ 2,4 V ở các chân bàn→khối |
| P1-6 | Khi mất PC > 1 s, bàn nhả mọi đầu ra về Hi-Z/an toàn | rút cáp PC |

---

## 7. Công việc P1 và thời gian (ước lượng ±40 %)

| # | Việc | Người | Tuần | Phụ thuộc |
|---|---|---|---:|---|
| 1 | P0-a: ảnh Hình 8/3/4/7, HDSD A-313-2A, đo thật giản đồ ЗП/ЧТ | anh (ảnh + đo) | 1 | — |
| 2 | Chốt hướng 3Ш2 chậm (đối chiếu Э4) | tôi/anh | 0,5 | 1 |
| 3 | Mô hình Python + xsim RTL (bus_slave, ram, log) | Codex xây, tôi review | 2 | 1 |
| 4 | Fit/timing XC7A35T | Codex | 0,5 | 3 |
| 5 | Thiết kế + gia công mạch đế đệm (Altium) | anh | 2–3 | 2 |
| 6 | PC: sequencer + GUI tối giản (tái dùng PySide6 worker, JSON/JUnit) | Codex | 1–2 | 3 |
| 7 | Bring-up T1→T2 trên khối thật | anh | 1 | 4, 5 |

Tổng ≈ **5–7 tuần lịch** (4 tuần nếu việc 5 chạy song song với 3–4). Đường găng: gia công mạch đế và ảnh Hình 8.


---

## 8. Trả lời của người dùng (26/10/2026) và hệ quả

| # | Câu hỏi | Trả lời | Hệ quả cho P1 |
|---|---|---|---|
| 1 | Có Hình 8/3/4/7 hay máy phân tích logic? | **Thiếu; chỉ tận dụng cái đang có** | Không đợi Hình 8: suy thời gian từ nguồn đã có (§9.2). Việc đo thật chuyển thành bước xác nhận sau, không phải điều kiện bắt đầu |
| 2 | Nguồn 27 V / 36 V 400 Hz | **Nguồn chuẩn máy bay đầy đủ, đặt giới hạn dòng tuỳ ý, cấp được mọi yêu cầu** | Nguồn không còn là rủi ro của P1. Giữ nguyên quy tắc: lần đầu đặt giới hạn dòng thấp rồi tăng dần (đây là biện pháp bảo vệ khối, không phải hạn chế nguồn) |
| 3 | Đặt mạch? | **Chưa vội; lập bảng chân + kế hoạch chi tiết, đủ điều kiện rồi mới đặt** | Bảng chân: `P1_BANG-CHAN_BAN-KIEM-TRA-A-313-3.md`. Cổng khả thi G1–G6 ở §9.3; mạch chỉ đặt khi G1–G5 đạt |

---

## 9. Bảng chân, tài sản có sẵn, cổng khả thi

### 9.1. Bảng chân

Sinh bằng `tmp/pdfs/review/ban-kiem-tra/p1_assign.py` từ `p1_pinout.csv` (chân khối), HDSDKT + Э4 (hướng 3Ш2, bảng `CLS` trong script, có mức bằng chứng A/B/C) và `a7lite_gpio_banks.csv` (JP1/JP2 → chân FPGA → bank). Kết quả: **`P1_BANG-CHAN_BAN-KIEM-TRA-A-313-3.md`** (+ `p1_pin_assignment.csv`). Bản này thay bản sinh trước đó (83 chân, 20 đường chưa rõ hướng).

| Chỉ tiêu | Kết quả |
|---|---|
| Khối → bàn (đệm một chiều) | 34 (27 từ 3Ш1, 7 từ 3Ш2) |
| Bàn → khối (đệm 5 V một chiều) | 27 (КШЧТ ×18, ИВЧ, ИКО, РгК1/К2/М КПА, ЗАПРЕТ ×3, ВХОД «П» ТТЛ) |
| Hai chiều Hi-Z | 1 (ПРИНУДИТ.ЗАПУСК, chưa biết ai lái) |
| Đường mức không TTL (chia áp) | 4 (ИСПР.ПИТАНИЯ ЦВУ, ИСПР.ПИТ.ППЗУ, НАПР.ВЫШЕ/НИЖЕ НОРМЫ) |
| Không nối | 4 (ВНЕШН.ПРЕРЫВ ×4, bị gạch xoá trong Э4) |
| Quan sát 3Ш7 | 22 (3 thanh ghi dịch, dùng chung SR_CLK, SR_LOAD_N, SR_MISO) |
| **Chân FPGA dùng** | **77 / 86** (88 GPIO trừ U22 PUDC_B, V22 EMCCLK) → **dư 9** |

Kết quả của việc 1 (chốt hướng 3Ш2):
- **ИКО là vào khối**: HDSDKT tr.24 «khi kết thúc chu kỳ ghi hoặc đọc, khối A-313-2 đưa ra ИКО»; Bảng 5 ghi trùng.
- **Rộng ra hai kết luận mới có ảnh hưởng thiết kế:** (1) KПА trong HDSDKT = **ПС17-318** (bàn kiểm), nên РгК1/К2/М КПА, ЗАПРЕТ, ВХОД «П» ТТЛ là tín hiệu **từ bàn vào khối**: bàn mới phải tạo chúng; (2) **НАПР.ВЫШЕ/НИЖЕ НОРМЫ và ИСПР.ПИТАНИЯ là đầu ra của tấm Y24 trong khối** (Э4 địa chỉ У24), không phải cờ bàn đặt cho khối. Bản kế hoạch trước (§5.5, M8) ghi ngược; đã sửa.
- **Mức không phải TTL** (HDSDKT, mạch Y24): ИСПР.ПИТ.ЦВУ tốt = 5,2 ± 1 V, hỏng < 0,5 V; **ИСПР.ПИТ.ППЗУ hỏng ≥ 15 V**; ИСПРАВНОСТЬ ПИТАНИЯ hỏng = hở mạch. Đơn vị V suy từ ngữ cảnh. Đưa thẳng vào GPIO 3,3 V sẽ hỏng chân → nhóm F có chia áp/kẹp (đo thật trước).
- Còn **chưa xác minh** (mức [C]): СБОЙ, ПРЕДВАРИТ.ОТКАЗ (xếp vào nhóm nhận một chiều, nên không lái ngược khối dù đoán sai), ПРИНУДИТ.ЗАПУСК, mức НАПР.ВЫШЕ/НИЖЕ. Đo trên khối thật (đã chạy được).

Chưa kiểm VCCIO của bank 34 (JP2 chân 49/50): không đường nào dùng, đang là chân dư.

### 9.2. Tận dụng những gì đang có (không có Hình 8)

| Tài sản | Trạng thái | Dùng để |
|---|---|---|
| Bộ dữ liệu chép 24 tấm Y1–Y24 + ma trận Y16 + Excel kết nối toàn khối | **đã có, đã kiểm** | Suy ngược yêu cầu thời gian của ИВЧ/ИКО/КША/ЗП/ЧТ: tìm mọi cổng/trigger nối vào các tín hiệu đó (ví dụ ИВЧ vào У19.2/10, У21.2/10 trên Y8, У58.1 trên Y10, qua П2/П3) và lập mô hình số của đường vào/ra; đây là bước thay Hình 8 |
| Văn bản HDSDKT | đã có | chu kỳ 4700 µs gồm 8 thao tác × 588 µs; ИКО ≤ 17 µs; tự xoá sau 24 µs; mức 1 = 2,4–4,5 V, 0 = 0–0,35 V |
| Tài liệu bàn Nga ПС17-319 (`thiet_bi_kiem_tra_a313/Thiet bi kiem tra 319.doc`, mục 12.5) | đã đọc | chế độ «ЦВУ-УВВ» của chính bàn Nga mô tả đúng việc P1 làm: cấp КША (hàng địa chỉ 7–15), nhận КШЗП 18 hàng khi ghi, trả КШЧТ 18 hàng + ИВЧ + ИКО khi đọc; công tắc ИМИТАЦИЯ ПО АДРЕСУ/ПО ПОЛЮ ≈ hai kiểu giả lập (theo địa chỉ, theo trường) |
| Thư mục `thiet_bi_kiem_tra_a313/ban ve Orcad va Layout/`, `…/macha313-318/` (OrCAD `.DSN`/`.LLB`, A3132AV, BKT320MOI) | đã đọc 26/10 (xem §11) | nguồn sơ đồ ПС17-319/320 để lấy cấu trúc УСС, đệm, mức; cần trích bằng công cụ đọc `.DSN` — một việc của P0-a |
| Thư mục `thiet_bi_kiem_tra_a313/Datmach318 cho A32/…` (file `.MAX` layout Y1–Y16) | có file, chưa đọc | chỉ là layout PCB, ít giá trị cho P1 |
| Bàn ПС17-318/319 đang hỏng | **có thật, hỏng** | tháo lấy: 3 УСС, cáp ТЖ4.853.xxx, đầu nối, đệm 133ЛА6 còn tốt, vỏ, nguồn nội bộ. Xác nhận từng thứ bằng đo, **chưa biết còn gì tốt** |
| A7-Lite + Vivado 2022.1 + dự án ARINC429_ATS | có (Vivado kiểm tại `C:/Xilinx/Vivado/2022.1`) | RTL UART/CRC16, khung PROTO2, GUI PySide6; không tái dùng board `0123_system` |
| Khối A-313-3 thật | **chưa biết tình trạng** | khối thật cũng là nguồn đo thời gian (khi có nguồn, P1-3 quan sát КШЗП/КША trước khi nối đầu ra) |
| Nguồn máy bay | có, giới hạn dòng tuỳ ý | bỏ yêu cầu M1 bên ngoài; vẫn cần cách ly 27 V RK ở các giai đoạn sau |

Kết luận: thời gian P1 có thể suy ra từ **dữ liệu đã chép + HDSDKT + chế độ ЦВУ-УВВ của bàn Nga**, không cần Hình 8. Điều chưa suy được và vẫn cần đo là độ rộng/độ trễ thực của ИВЧ/ИКО (Hình 8) — chỉ đo khi có khối chạy.

### 9.3. Cổng khả thi (mạch chỉ đặt khi G1–G5 đạt)

| Cổng | Câu hỏi | Cách kiểm | Trạng thái |
|---|---|---|---|
| **G1** Số chân | đường tín hiệu + điều khiển vừa 86 chân? | `p1_assign.py` (assert không trùng chân, không dùng chân nguồn/cấu hình) | **Đạt trên giấy** (77/86, dư 9) |
| **G2** Thời gian | Phản hồi ИВЧ/ИКО/КШЧТ đủ nhanh và đúng độ rộng mà khối chấp nhận? | mô hình Python của các cổng nối ИВЧ/ИКО/КШЧТ (từ `ric*_net.csv`) + chạy xsim RTL; đối chiếu ИКО ≤ 17 µs | **Chưa làm**; ИКО bị ghi hai hướng ở [A3] → xác định hướng bằng Э4 trước |
| **G3** Hướng và mức | hướng và mức 3Ш2 | HDSDKT + Э4 (việc 1) | **Đạt một phần**: 38/43 đường 3Ш2 có hướng ở mức [A]/[B]; 5 đường mức [C] (СБОЙ, ПРЕДВАРИТ.ОТКАЗ, ПРИНУДИТ.ЗАПУСК, НАПР.ВЫШЕ, НАПР.НИЖЕ); xác nhận bằng đo khối thật (§10) |
| **G4** Điện | IC đệm đúng họ (AHCT/LVC), dòng sink ИВЧ, Vil/Vih, sóng phản xạ | datasheet đúng IC + tính tải; xác nhận bằng PicoScope trên khối thật | **Chưa làm**; chưa tra datasheet |
| **G5** Có chỗ cắm | Cáp/đầu nối 3Ш1/3Ш2/3Ш7 có sẵn và tương thích? | anh xác nhận 26/10: cáp ТЖ4.853.xxx, 3 УСС và đầu nối còn nguyên; còn lại thông mạch theo bảng chân | **Đạt theo lời anh**, chưa kiểm bằng thông mạch |
| **G6** Cấu hình FPGA an toàn | Khi chưa nạp bitstream, mọi đầu ra bàn→khối Hi-Z? | điện trở kéo ngoài trên OE; kiểm U22 PUDC_B; thử rút điện | **Chưa làm** (sau khi có mạch) |

### 9.4. Việc cần làm trước khi đặt mạch (thứ tự)

| # | Việc | Ai | Phụ thuộc | Ghi chú |
|---|---|---|---|---|
| 1 | ~~Chốt hướng 3Ш2~~ **xong (26/10)**, xem §9.1; còn đo mức [C] trên khối thật | tôi + anh | — | đóng G3 |
| 2 | ~~Dựng mô hình số~~ **xong bản đồ đường đi + tải đầu vào (26/10)**, §11.2; mô hình thời gian chưa làm được vì thiếu dữ liệu | tôi + Codex | 1 | G2 chưa đóng |
| 3 | ~~Trích sơ đồ УСС từ `.DSN`~~ **xong một phần (26/10)**: đọc được netlist 53 tấm từ `.MNL`, nhưng **không có УСС trong OrCAD** (§11.1); УСС chỉ có ở hình Word | tôi | — | G4 chưa đóng |
| 4 | Chọn IC đệm, tra datasheet, tính tải ИВЧ | tôi | 1, 2 | đóng G4 |
| 5 | ~~Kiểm kho~~ anh xác nhận cáp/УСС/đầu nối còn nguyên; thông mạch theo bảng chân | anh | — | đóng G5 |
| 6 | RTL + xsim + PC tối giản (chưa cần mạch: thử trên A7-Lite với LED/máy phân tích logic) | Codex | 2 | |
| 7 | Nếu G1–G5 đạt → vẽ mạch đế | anh | 1–5 | |

Thời gian: việc 1–4 ≈ **2–3 tuần** (tôi + Codex làm trên dữ liệu đã có, ±40 %, chưa có phép đo); việc 5–6 chạy song song; mạch đế đặt sau đó. Tổng P1 như Rev. A §7, nhưng đường găng chuyển từ "ảnh Hình 8" sang "kho cáp/đầu nối và datasheet đệm".

**Anh đã trả lời (26/10):** khối A-313-3 còn chạy bình thường; cáp ТЖ4.853.xxx, 3 УСС, đầu nối còn nguyên. Hệ quả: đo thật được ngay (không cần đợi mạch), xem §10.

---

## 10. Đo thụ động trên khối thật (khối chạy bình thường)

Mục tiêu: đóng G2, G3, G4 bằng số đo thay vì Hình 8. **Chỉ quan sát**, không nối bất kỳ đầu ra nào của bàn mới vào khối.

**Quy tắc an toàn (cứng):**
1. Cấp 27 V (và 36 V 400 Hz theo HDSD) từ nguồn máy bay, **đặt giới hạn dòng thấp rồi tăng dần** khi bật lần đầu; ghi dòng tiêu thụ ở trạng thái ổn định (thông tin còn thiếu của HDSDKT).
2. Đầu dò trở kháng cao (≥ 1 MΩ; que ×10 nếu có). Kẹp mát vào chân КОРПУС (3Ш2/1, 38, 49, 50). **Không đo trên 3Ш1 chân 32–43, 46, 48 (rail) và 3Ш2 chân 33, 34 (+27 В)** khi chưa có đầu dò cách ly đã biết giới hạn.
3. Tuyệt đối không nối chân tín hiệu xuống mát hay vào nguồn; muốn đo dòng ra thì dùng điện trở nối tiếp ≥ 1 kΩ.
4. Đổi đầu dò chỉ khi **đã tắt nguồn** (luật phần cứng của dự án).

| # | Đo | Chân (3Ш) | Quyết định được gì | Cổng |
|---|---|---|---|---|
| M1 | Dạng sóng ЗП УВВ, ЧТ УВВ, ВрМ1, ВрМ2, КША 7–15 (logic analyzer/PicoScope kênh số) khi khối chạy tự do | 3Ш2/23–26, 3Ш1 КША | Độ rộng, chu kỳ (kiểm 4700 µs/chu kỳ, 588 µs/thao tác), quan hệ pha ЧТ/ЗП so với КША → đặt cửa sổ lấy mẫu của FPGA | G2 |
| M2 | Mức tĩnh lúc nghỉ của ИВЧ, ИКО, КШЧТ 0–17 (khi không ai lái) | 3Ш2/2–19, 21, 22 | Có kéo lên bên trong khối không; dòng nguồn cần cấp cho đệm; ngưỡng thật | G4 |
| M3 | Mức và dạng của ИСПР.ПИТАНИЯ ЦВУ, ИСПР.ПИТ.ППЗУ, НАПР.ВЫШЕ/НИЖЕ (lúc bật nguồn và ổn định) | 3Ш2/35, 36, 37, 39 | Mức thật so với (5,2 ± 1 V; ≥ 15 V hỏng) → chọn tỉ số chia | G4 |
| M4 | СБОЙ, ПРЕДВАРИТ.ОТКАЗ, ПРИНУДИТ.ЗАПУСК: có bị khối lái không (chỉ đo điện áp bằng đầu dò trở kháng cao: mức logic ổn định 0/1 = đang bị lái; ≈ 1–2 V trôi hoặc kéo lên = đầu vào; không kéo/xả thử) | 3Ш2/20, 27, 32 | đóng 3 đường mức [C] | G3 |
| M5 | Khối có chạy tiếp chu kỳ khi **không có ИВЧ/ИКО** (chỉ quan sát ЗП/ЧТ lặp hay treo) | 3Ш2/21–26 | Cần biết bàn mới có phải trả lời ngay từ chu kỳ đầu | G2 |
| M6 | Dòng tiêu thụ 27 V, 36 V 400 Hz | nguồn | Giới hạn dòng cho các lần sau | — |

Công cụ: PicoScope 5462E + pypicosdk (driver `psospa`, đã dùng cho ARINC429_ATS) cho M1–M5; số kênh số và băng thông cần kiểm lại trên máy thật. Sản phẩm: bảng số đo + ảnh sóng, lưu `Phan-bien/` hoặc `tmp/pdfs/review/ban-kiem-tra/do/` (theo quy ước của repo), không ghi đè ảnh đo cũ.

Sau M1–M5: cập nhật `CLS` trong `p1_assign.py` (đổi mức [C] thành [A]), chạy lại sinh bảng chân, rồi đánh giá G1–G5 để quyết định đặt mạch.

---

## 11. Kết quả đọc OrCAD và bản đồ đường đi (26/10/2026)

### 11.1. OrCAD trong `thiet_bi_kiem_tra_a313/`

| Việc | Kết quả |
|---|---|
| Tệp `.DSN` | 118 tệp, 115 mở được bằng `olefile` (OLE2); 3 tệp không phải OLE. Trang sơ đồ là nhị phân, chưa dựng được netlist từ đây |
| Tệp `.MNL` (Layout V7.00) | 53 tệp **duy nhất** theo md5. Đã đảo ngược định dạng (`mnl_parse.py`, `mnl_export.py`): linh kiện + net + chân, xuất `orcad/*_bom.csv`, `*_net.csv`, `summary.csv` |
| Kiểm tự động | chân nguồn/mát của IC 74xx phải về VCC/GND: **20/53 tệp đạt** hoàn toàn; 33 tệp `warn` (phần lớn do chỉ số linh kiện lệch ở tệp có tên trùng, một vài tệp có 1–4 chân nguồn nằm trên net khác — ví dụ `U21.7 → P1.7` trên tấm «Y8» — chưa phân biệt lỗi thật hay nguồn đi qua đầu nối) |
| Định dạng `.MNL` | tôi suy ra bằng đối chiếu, không có tài liệu; chưa kiểm bằng một netlist biết trước. Coi netlist này là **gợi ý**, không phải chuẩn |
| **Các tấm OrCAD không giống tấm của khối A-313-3** | so vân tay loại IC (`orcad_fingerprint.py`) với bộ chép tay: không khớp (khoảng cách L1 22–56 trên 50–70 IC). «MACHY16» của OrCAD là bo khuếch đại (168КТ2 ×21, NPN/PNP, ±12,6 V), không phải tấm chuyển mạch Y16. Đây là thiết kế riêng của bàn ПС17-318 (thư mục tên «Hình 4-22 … Hình 16-61», đánh số Y1–Y16 nhưng không nhất thiết trùng tấm cùng số của khối) |
| Có УСС không? | **Không.** Tìm Cyrillic trong 115 DSN: nhãn ЗП/ЧТ chỉ ở 3 tệp (`A_KY_MOI.DSN`, `MACH1BIENDOI Y13.DSN`, `MACHY15H16T125.DSN`), không có ИВЧ/ИКО/КШЧТ/КША. УСС ТЖ3.099.001/002/004 chỉ được mô tả bằng hình trong Word (hình 25–30 của «Thuyết minh kỹ thuật 319») |

⇒ **G4 không đóng được từ OrCAD.** Cần đọc hình Word (ảnh trong `.doc`) hoặc đo trên УСС thật (anh nói còn nguyên).
Ngoại lệ có thể khai thác sau: tấm Y14/Y15 của OrCAD có 168КТ2 ×25–26, gần với tấm «ric15» của bộ chép tay (168КТ2 ×25); nếu cùng một tấm thì đây là nguồn kiểm chéo độc lập cho mâu thuẫn РК I/РК II của Y14/Y15. Chưa kiểm.

### 11.2. Bản đồ đường đi tín hiệu giao tiếp (Э4)

`signal_paths.py` dựng nhóm dây từ `e4_all.csv` (kết quả: `signal_paths.csv`, `.md`):

| Tín hiệu | Điểm tới (theo Э4) | Ý nghĩa cho bàn mới |
|---|---|---|
| КШЧТ 0–17 | từng bit chỉ tới **một** điểm: У1П2/2…19 | tải bàn chỉ là một đầu vào trên tấm Y1 mỗi bit |
| ИВЧ | 3Ш2/21 → У1П2/29; sau đó Y1 chuyển tiếp qua П3/43 → Y2 (П3/28, П1/14) → У16КП9/14, У16КП8/11 → **Y5 П3/2, Y6 П2/17, П3/69** | Bàn chỉ lái **một** chân (У1П2/29). Bộ chép tay: đó là cổng У58.1 với **4 chân vào nối chung** (1, 2, 4, 5) — tải tương đương bốn đầu vào, loại IC chưa có (У58 = «IC logic, không ghi mã» trong `ric10_bom.csv`) |
| ИКО | 3Ш2/22 → У1П2/30 → У1П3/44 → У2П3/27, У2П2/36 → У3П1/45 | chân vào Y1; lan tới Y2, Y3 |
| ЧТ УВВ, ЗП УВВ, Вр.М1, ВрМ2 | nhóm dây chưa nối liền trong Э4 (chỉ 2–3 điểm mỗi tín hiệu) | **khoảng trống dữ liệu**: không dựng được đường đi đầy đủ; cần Э4 hoặc đo |

Không có số tải mA vì chưa biết loại IC (cần mã ИС từ ảnh Y1). **Bản đồ này chưa phải mô hình thời gian**: thiếu dữ liệu Y1 (КШЧТ, ИКО chưa chép chân vào) và Y2/Y3 (PARTIAL), nên G2 vẫn mở. Việc kế: chép nốt cổng đầu vào trên Y1 (КШЧТ, ИКО) từ ảnh tr.179.

### 11.3. Cập nhật cổng khả thi

| Cổng | Trạng thái sau 26/10 |
|---|---|
| G1 | đạt (77/86) |
| G2 | **mở**: có bản đồ đường đi, thiếu dữ liệu Y1/Y2/Y3 để tính thời gian |
| G3 | một phần (§9.1) |
| G4 | **mở**: OrCAD không có УСС; tải ИВЧ ≈ 4 đầu vào nối chung nhưng chưa biết loại IC |
| G5 | đạt theo lời anh |
| G6 | chưa làm |
