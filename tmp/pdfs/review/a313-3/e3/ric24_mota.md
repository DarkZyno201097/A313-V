# рис.24 — УЛП ±10 В; 0,2 А (ЕУ3.215.466 Э3), khối У23 của A-313-3

Nguồn: ảnh #228 (trang 228, sơ đồ), #229–#230 (trang 229–230, перечень элементов, «Лист 96–97»).
Tên in trên bản vẽ: «УЛП ±10 В; 0,2 А. Схема электрическая принципиальная (ЕУ3.215.466 Э3) Рис.24».
Перечень: «Перечень элементов к схеме электрической принципиальной УЛП ±10 В; 0,2 А (РИС.24)».

Tờ gấp được chụp **trọn**: thấy đủ khung, bảng đầu cắm 12 tiếp điểm và khung tên bên trái.
Không có phần bị cắt. Phản chiếu đèn ở giữa dưới (vùng C3/R21) nhưng vẫn đọc được.

File kèm: `ric24_bom.csv` (40 ký hiệu), `ric24_net.csv` (95 chân, 27 net, 19 net N#).
Số liệu dưới đây tính bằng `e3_check.py` (cùng thư mục).

## 1. Đầu cắm (bảng «Конт / Цепь» trên bản vẽ)

| Конт | Цепь | Đối chiếu Э4 (e4/p143.csv, У23) |
|---|---|---|
| 1, 9, 10, 11 | Корпус | 1, 9, 10, 11 КОРПУС — khớp |
| 2 | −5 В выход | −5 В 0,2 А → 3Ш1/42, У24/2 — khớp |
| 3 | −10 В выход | «10 В 0,2 А» (mất dấu) → bản vẽ xác nhận **−10 В** |
| 4 | −12,6 В вход | −12,6 В ВХ từ У22/3 — khớp |
| 5 | +10 В вых. | +10 В 0,25 А — khớp |
| 6 | +12,6 В вх. | +12,6 В ВХ — khớp |
| 7 | +3,5 В вых. | +3,5 В 0,25 А — khớp |
| 8 | **+6,3 В вх.** | **«5В ВХ» từ 3Ш5/1 — LỆCH** |
| 12 | (trống) | — |

Các số ghi trên mép khung chấm-gạch của từng mạch con trùng số tiếp điểm đầu cắm (đã lần dây từng sợi tới bảng).
Riêng dây ra +10 V của khối giữa đi qua mép khung **không có** vòng tròn số «5».

## 2. Topology — 4 bộ ổn áp tuyến tính độc lập, không có mạch chung ngoài «Корпус»

**a) −5 В (T1–T3, Д1, Д2)** — ổn áp nối tiếp cực âm, cấp từ −12,6 В (конт. 4).
T1 2Т904А (n-p-n) là phần tử điều chỉnh: э ở −12,6 В, к ra −5 В. R3 1,8 к nối б–э T1.
T2 2Т203А (p-n-p) cấp dòng gốc cho T1 từ phía ra (э T2 ở −5 В, к vào gốc T1); R2 6,8 к kéo gốc T2 về −12,6 В (mở).
Tham chiếu: R1 470 Ω từ −12,6 В nuôi Д1 Д818Е (9 V), cực к của Д1 ở корпус ⇒ nút R1/Д1 = −9 V.
R4 СП5-3 4,7 к mắc song song Д1, con trượt nối vào э T3 2Т203А (p-n-p); gốc T3 qua R5 560 Ω lấy thẳng từ đầu ra.
Ra âm hơn mức đặt ⇒ T3 dẫn ⇒ kéo gốc T2 lên ⇒ T2/T1 khoá bớt. **Uвых ≈ Uдвижка R4 − Ube(T3)**.
Để có −5 В con trượt R4 ở ≈ −4,35 V (≈ 0,48 hành trình tính từ корпус). Dải chỉnh lý thuyết −0,65…−9,65 V.
Д2 2С168А (6,8 V) nối ra–корпус: kẹp quá áp khi T1 đánh thủng. C1 К52-1 47 µF lọc ra (cực «+» về корпус).
Iст Д1 ≈ 7,66 − 1,91 (dòng R4) = 5,7 mA.

**b) +10 В (T4–T6, Д3)** — ổn áp nối tiếp cực dương, cấp từ +12,6 В (конт. 6).
Darlington T5 2Т603Б → T4 2Т904А (n-p-n, cực к ở +12,6 В); R10 7,5 к xả b-e T4; R7 1,5 к kéo gốc T5 lên.
Tham chiếu: R6 470 Ω + Д3 Д818Е (+9 V); chia R8 СП5-3 2 к + R9 1,2 к; con trượt R8 → э T6 2Т312Б (n-p-n).
Gốc T6 nối điểm giữa phân áp đầu ra R11 1,5 к / R20 1,5 к (= Uвых/2); к T6 rút dòng gốc T5.
**Uвых = 2·(Uдвижка R8 + Ube)** ⇒ để có +10 V cần Uдвижка = 4,35 V (dải 3,375…9 V).
Dải ra lý thuyết 8,05…19,3 V, thực tế bị trần ở ≈ +10,6 V vì đầu vào chỉ +12,6 V (2·Ube + sụt áp R7).
C2 К53-1А 68 µF lọc ra. Iст Д3 ≈ 4,85 mA. Phân áp R11+R20 ăn 3,33 mA.

**c) −10 В (T7–T10, Д4)** — ảnh gương của (a) nhưng có thêm tầng Darlington và phân áp đầu ra.
T7 2Т904А (n-p-n) điều chỉnh, э ở −12,6 В. T8 2Т603Б (n-p-n, к ở đầu ra) cấp gốc cho T7.
T9 2Т203А (p-n-p, э ở đầu ra) điều khiển T8. Ba điện trở R14 2,2 к / R13 5,6 к / R12 470 Ω nối từ −12,6 В.
Tham chiếu: R12 + Д4 Д818Е (−9 V); chia R15 + R16 3,0 к (dải −6…−9 V); con trượt R15 → э T10 2Т203А (p-n-p).
Gốc T10 lấy từ con trượt R21 СП5-3 2,2 к mắc ra–корпус. Để có −10 V: k(R21) = 0,665…0,965 tuỳ vị trí R15.
C3 К53-1А 68 µF (cực «+» về корпус). Iст Д4 ≈ 5,7 mA; dòng qua R21 4,55 mA.

**d) +3,5 В (T11, Д5)** — bộ lặp emitter đơn giản, cấp từ конт. 8.
R18 220 Ω / R19 220 Ω chia áp vào gốc T11; Д5 2С147А (4,7 V) song song R19 làm kẹp; э T11 → +3,5 В; C4 К52-1 47 µF.
**Nhưng** với R18 = R19 = 220 Ω: Uвх 6,3 V ⇒ Uб = 3,15 V (Д5 không dẫn) ⇒ Uвых ≈ 2,5 V không tải;
Uвх 5 V (theo Э4) ⇒ ≈ 1,85 V. **Không ra được 3,5 V** với số liệu đã đọc — xem mục 4.

## 3. Bảng điểm đo (theo net trong `ric24_net.csv`)

| TP | Điểm | Danh định |
|---|---|---|
| TP1 | конт. 4 (X:4) | −12,6 V vào |
| TP2 | N3 (anode Д1) | −9 V ±5 % |
| TP3 | N4 (con trượt R4 / э T3) | ≈ −4,35 V |
| TP4 | конт. 2 | −5 V |
| TP5 | конт. 6 | +12,6 V vào |
| TP6 | N8 (cathode Д3) | +9 V |
| TP7 | N9 (con trượt R8 / э T6) | ≈ +4,35 V |
| TP8 | N11 (R11/R20) | ≈ +5,0 V (= Uвых/2) |
| TP9 | конт. 5 | +10 V ±0,5 V (bảng 3 HDSDKT) |
| TP10 | N15 (anode Д4) | −9 V |
| TP11 | N16 (con trượt R15 / э T10) | −6…−9 V |
| TP12 | конт. 3 | −10 V ±0,5 V |
| TP13 | конт. 8 / N19 / конт. 7 | Uвх / ≈Uвх/2 / Uб − 0,65 V |
| — | Uкэ T1, T4, T7 | ≥ 2 V ở tải định mức (headroom) |

## 4. Chưa chắc / thiếu

1. **Конт. 8**: bản vẽ ghi «+6,3 В вх.», bảng Э4 trang 143 ghi «5В ВХ» (từ 3Ш5/1). Phải đo trên khối.
2. **Nhánh +3,5 V**: với R18 = R19 = 220 Ω (перечень in rõ) đầu ra chỉ ≈ 2,5 V (6,3 V vào) hoặc ≈ 1,85 V (5 V vào).
   Có thể: giá trị trong перечень sai, hoặc R19 là linh kiện chọn (trong thân R18/R19 trên ảnh có chấm, không rõ là dấu «*» hay vết bẩn).
   Văn bản HDSDKT §2.2.3 lại ghi «−3,5V» là nguồn tuyến tính. Cần đo thực tế và đọc giá trị trên mạch in.
3. **R15**: trên sơ đồ vẽ có con trượt (giống R4, R8, R21), trong перечень là С2-23 1,5 к cố định. Nếu là điện trở cố định thì con trượt nối vào đâu — phải xem mạch in.
4. **Перечень có lỗi in**: «С20», «С21» thực ra là R20, R21; C1 «Кол. 2»; «С4I»; T8 2Т603Б nhưng ТУ ЖК3.365.143 (ТУ của 2Т312); T11 «2Т204А» với ТУ И93.365.008 (ТУ của 2Т904А) — gần như chắc là 2Т904А, đọc mã trên vỏ.
5. **Kiểu cực tính T6, T3, T10** đọc từ mũi tên trên ảnh không dứt khoát; đã chốt theo перечень (2Т312Б n-p-n, 2Т203А p-n-p) và theo chiều phản hồi âm — nhất quán.
6. Không có R17 (cả sơ đồ lẫn перечень) — đánh số nhảy, không phải thiếu ảnh.
7. Dây vào −12,6 V của khối −10 V: đi vòng dưới khối −5 V; trên ảnh nét dây và mép khung chồng nhau, kết luận dựa trên việc khối này không còn nguồn vào nào khác.
8. Dây ra +10 V qua mép khung không có số «5» — số tiếp điểm suy ra từ việc lần dây tới bảng.
9. Bảng 3 HDSDKT chỉ liệt kê +10 V 0,2 A và −10 V 0,25 A cho ЕУ3.215.466; −5 V và +3,5 V không có dung sai.

## 5. Quy trình cấp điện thử trên bàn (khối tháo khỏi A-313-3)

Khối không tự sinh áp — cần **3 nguồn ngoài**: −12,6 V, +12,6 V, +6,3 V (hoặc 5 V, xem mục 4.1).

1. **Nguội**: đo điện trở конт. 2/3/5/7 → корпус (cả hai chiều que đo) — tìm chập T1/T4/T7/T11 (Ω thấp). Đo b-e, b-c các transistor công suất tại chỗ.
   Kiểm Д1/Д3/Д4 không chập (Д818Е ở chiều thuận ≈ 0,7 V).
2. Vặn R4, R8, R21 (và R15 nếu là biến trở) về giữa; đánh dấu vị trí cũ trước khi chạm vào.
3. Tải giả: −5 V → 47 Ω/2 W (≈ 0,1 A); +10 V → 100 Ω/2 W; −10 V → 100 Ω/2 W; +3,5 V → 47 Ω/1 W.
   Lần đầu chạy **không tải**, rồi mới gắn tải.
4. Cấp **từng kênh một**, nguồn bàn hạn dòng **50 mA**, tăng áp từ 0:
   - конт. 4 = −12,6 V (đúng cực: «+» nguồn vào корпус). Đo TP2 = −9 V trước, rồi TP4.
   - конт. 6 = +12,6 V. Đo TP6, TP8, TP9.
   - конт. 8 = +6,3 V. Đo конт. 7.
   Dòng không tải mỗi kênh dự kiến ≈ 10–15 mA (dòng Д + phân áp). Nếu chạm giới hạn 50 mA ⇒ dừng, có chập.
5. Chỉnh R4 → −5,00 V; R8 → +10,00 V; R21 (R15) → −10,00 V. Ghi lại vị trí.
6. Nâng giới hạn dòng lên 0,3 A rồi gắn tải; kiểm độ sụt Uвых (≤ dung sai bảng 3) và nhiệt T1/T4/T7.
   Biến thiên Uвх ±10 % (−11,3…−13,9 V; +11,3…+13,9 V) — đầu ra phải giữ.
   **Không** nâng giới hạn dòng để «ép» kênh đang lỗi chạy.
7. Kênh −5 V: Д2 6,8 V chỉ là kẹp — nếu ra ≈ −6,8 V và dòng lớn ⇒ T1 thủng.
