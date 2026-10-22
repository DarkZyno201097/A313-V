# Рис.25 — УЛП 5 В 15 А (ЕУ3.215.469 Э3), khối У17 của A-313-3

Nguồn: ảnh #233 (sơ đồ gập, trang tay 231), #234–#238 (перечень, trang 232–236, «110.23.03 Приложение
лист 99–103»), #248 (сборочный, trang 247), #249 (ВШ6.730.530 Д7, рис.34, tấm phụ đầu ra).
Bảng kê và netlist: `ric25_bom.csv`, `ric25_net.csv` (sinh bởi `ric25_gen.py`).
Mọi con số dưới đây do `ric25_tinh.py` tính (kèm kiểm tra chéo bom↔net).

> Netlist đọc **bằng mắt từ ảnh chụp điện thoại** của bản photocopy, không phải trích vector. Chỗ nào
> không chắc đều có ghi chú `?` trong cột `note`. Trước khi dùng để sửa, phải đối chiếu với tấm thật
> (đo thông mạch).

## 1. Tổng quan

Một tấm cắm, đầu nối Ш1 = РС50Т (khi lắp vào khối là 3Ш5). Trên tấm có **ba nguồn độc lập**:

| Đầu ra | Chân Ш1 | Cách tạo | Phần tử chính |
|---|---|---|---|
| +5 В 15 А | 1…10 (về: Корпус 18…23, 26…31) | ổn áp xung hạ áp (buck) từ +27 В | T8–T11 (4 × 2Т803А), Др1, Др2, Тр2 |
| −6,3 В 1 А | 45, 46 | ổn áp xung đảo cực (buck-boost âm) từ +27 В | T21 (2Т803А) + T22 (2Т921А), Др6 |
| ~5 В 400 Гц (Ф.С/Ф.А) | 11, 12 | biến áp Тр1 ТН-12-40-400 từ ~36 В 400 Гц | Тр1, Пр2 0,5 А |

Vào: +27 В ở chân 41, 42, 43, 47, 48; ~36 В 400 Гц Ф.С chân 25 (qua Пр2), Ф.А chân 33.
Hai đầu «Управл.»: chân 13 «Упр.(+5В)» nối vào nút R8/R9 (đỉnh chiết áp chuẩn +5 В); chân 14
«Упр.(−6,3В)» nối vào nút R35/R36 (bộ chia hồi tiếp −6,3 В). Theo p142 cả hai đi tới 3Ш7/27, 3Ш7/26
(tấm kiểm tra) — nhiều khả năng là điểm đo/hiệu chỉnh mức hoặc khoá nguồn từ tấm kiểm tra. Chưa rõ.

**Câu hỏi mở trong CLAUDE.md §4.6 (nguồn ~5 В 400 Гц) — với A-313-3 đã có lời giải:** ~5 В 400 Гц
được tạo trên chính tấm У17 bằng biến áp Тр1 (sơ cấp 1–2 nối 36 В 400 Гц Ф.С/Ф.А qua Пр2; thứ cấp
8–9 ra chân 12/11; các đầu 2а, 2б, 10 bỏ trống). Tỉ số danh định 36/5 = 7,2.

## 2. Nguồn +5 В 15 А

**Lọc vào.** +27 В → Др3 (Д213В, hai cuộn 1-2 // 3-4) → nút N2 có C17…C32 (16 × 150 мкФ 70 В) xuống
Корпус → Пр1 // Пр4 (2 × 5 А) → «шина +27 sau cầu chì» N3 (cực C của T8–T11, R6, Тр2 6/8).

**Khoá công suất.** 4 × 2Т803А (n-p-n, 60 В/10 А). T4 (2Т803А) kích T8 theo kiểu Darlington; R3 + R4
(МОН-2, 2 × 1,6 Ом = 3,2 Ом) hạn dòng collector T4. Chuỗi kích: T3 (p-n-p) → T6 (p-n-p) → T5 (2Т608Б)
→ T4 → T8 → (T9, T10, T11). R16/R17 (trên Э3 in nhầm «R6/R7») là điện trở B-E của T4/T5, R22 24 Ом
là B-E của T11.

⚠ **Mâu thuẫn trên hình vẽ:** đường «vòng» của T9 và T10 nối chân B và chân E của chính nó với emitter
T8; theo hình, B=E của T9/T10 và R22 bị nối tắt. Ghi trong netlist **đúng như vẽ** (net N20).
Cách hiểu hợp lý: E(T8) → B chung của T9, T10, T11 (Darlington, R22 xả B-E chung), E(T9…T11) = nút
chuyển mạch. Cần đo R(б-э) của T9, T10 trên tấm.

**Nút chuyển mạch → lọc ra.** Nút chuyển mạch (N20) → Др1 (Д245В, 1-2 // 3-4) → N21 có C5…C14
(10 × 220 мкФ 16 В) → Др2 (Д245В) → +5 В: C34…C38 (5 × 220 мкФ) → Ш1/1…10.
Diode thoát (đi ốt ngược): **Д5…Д18 = 14 × Д817А song song** (ổn áp 56 В 5 Вт dùng theo chiều thuận;
catốt ở nút chuyển mạch, anốt ở Корпус), C53, C54 0,047 мкФ song song với chúng (snubber).

**Тр2 (ЕУ4.719.326).** Cuộn 1–4 nối song song với Др1 (1 → nút chuyển mạch, 4 → N21); 2, 3 bỏ trống.
Hai cuộn 5-6 // 7-8 nối giữa +27 В (sau cầu chì) và «nguồn tầng kích» N4 (R3, R5, R10, R13, E của T3,
T6). Tức là tầng kích được cấp +27 В cộng/trừ điện áp cảm ứng từ cuộn chặn — tăng áp nuôi kích khi
khoá dẫn (kiểu bootstrap/hồi tiếp dương). Đây là suy luận từ topology, chưa kiểm chứng.

**Chuẩn và khuếch đại sai số.** R6 (680 Ом 1 Вт) + Д1 (Д814Д, ~13 В) → R7 (270 Ом) + Д2 (Д818Д, 9 В,
có bù nhiệt) = N18 «+9 В», cũng nuôi emitter T12, T15. Chuẩn: R8 1,2 к + R9 (СП5-3 6,8 к) → con trượt
→ T13.б (C3 lọc). Hồi tiếp: N21 (sau Др1) → R18 → T14.б. T13/T14 (2Т312Б) là cặp vi sai, R27 6,8 к
chung emitter. Collector T13 → T12 (p-n-p), collector T14 → T15 (p-n-p); C15 2200 пФ, C16 3300 пФ,
Д24, Д25, R25, R26, R29, R30 tạo trigger có trễ (điều chế xung kiểu so sánh có trễ / tự dao động —
chưa xác định được tần số từ hình vẽ). Lối ra T15.к → R24 → T2.б → T2 → T3 → T6 … → khoá.

**Bảo vệ quá áp (crowbar).** Д31 = thyristor 2У202И nối thẳng từ +5 В xuống Корпус. Cực điều khiển: R31
56 Ом, C39 1 мкФ, qua Д32 (2С147А 4,7 В) từ bộ chia R32 (2 Ом 1 Вт) / R33 (47 Ом 2 Вт). Ngưỡng tính
(`ric25_tinh.py`): **≈ 5,6–5,9 В** với Д32 danh định; trải rộng 5,0–6,4 В theo dung sai Д32/Uу.
Đồng thời R32 + R33 = 49 Ом là tải mồi ≈ 102 мА (P(R33) ≈ 0,49 Вт). Khi crowbar bắn, dòng ngắn mạch
đi qua khoá → Пр1/Пр4 đứt (không thấy mạch hạn dòng riêng ngoài R3+R4 ở T4 — **không có cảm biến dòng
tải** trên Э3 phần +5 В).

**Giá trị danh định:** I(R6) ≈ 20,6 мА, P(R6) ≈ 0,29 Вт; I(R7) ≈ 14,8 мА; dải con trượt R9 = 0…7,65 В,
đặt 5,00 В tại ≈ 4,44 кОм từ đáy (≈ 65 % hành trình), giả thiết Uвых ≈ U(T13.б) (cặp vi sai, sụt áp trên
R18 bỏ qua). Bảng 3 của HDSDKT: +5 В 15 А ±0,26 В.

## 3. Nguồn −6,3 В 1 А

Cấu trúc gần như trùng mô tả bộ −12,6 В trong HDSDKT trang 54–55 (đa hài đối xứng làm bộ điều chế,
khuếch đại sai số thay đổi trở kháng trong của tranzito để đổi độ rỗng xung).

* Vào: +27 В → Пр3 (1 А) → Др5 (ДМ-0,6) → N33, C55 33 мкФ, C40 150 мкФ.
* Đa hài: T16, T19 (2Т203А p-n-p), C41 680 пФ, C42 1200 пФ, R37 47 к, R39 120 к, tải collector R34,
  R43. Ước lượng 0,69RC: t1 ≈ 22,2 мкс, t2 ≈ 99,8 мкс ⇒ **f ≈ 8,2 кГц** (chỉ ước lượng).
* Khuếch đại sai số: T17/T18 (П307В), R38 chung emitter; collector T17 → T19.б, T18 → T16.б (lấy bớt
  dòng gốc của đa hài). Chuẩn: R44 (3,3 к 1 Вт) từ +27 В → Д33 (Д818Д 9 В) → R40/R41 → T18.б
  (3,337 В trên «шина M»). Hồi tiếp: R35 1,2 к + R36 (СП5-3 2,2 к) giữa Корпус và «шина M», con trượt → T17.б.
  Nếu «шина M» ≈ Uвых thì |U| tối thiểu (R36 trượt hết) = 5,16 В; 6,3 В ứng với R36(dưới) ≈ 1,80 кОм.
* Kích + khoá: T19.э/R42 → T20 (p-n-p) → R45/C44/R46 → T23 (p-n-p) → T22 (2Т921А) → T21 (2Т803А), R47,
  R48 xả B-E. Nút chuyển mạch N43 (E của T21) → Др6 (Д123) → Корпус; Д34…Д41 (8 × 2Д510А, Э3 ghi
  «Д34…Д40») catốt ở N43, anốt ở N44 → C45…C50 (6 × 68 мкФ, cực + ở Корпус) → Др7 → Др8 → C51, C52
  (+ ở Корпус) → Ш1/45, 46. Đúng sơ đồ buck-boost đảo cực.
* **T24 (2Т301Д) + Д23 (2Д103А) + R49 + C43:** E(T24) là «шина M» (anốt Д33, đáy R36, R38, R41); B(T24)
  qua Д23 từ −6,3 В; C(T24) → C43(+)/R49 → catốt Д33. Không suy được chiều dòng hợp lý từ hình (loại
  n-p-n theo перечень, ký hiệu vẽ mũi tên hướng vào). Có thể là mạch khởi động / khoá khi ngắn mạch.
  **Chưa chắc — cần đo.**
* Không thấy cảm biến dòng riêng (khác bộ +6,3 В trong HDSDKT dùng điện trở thuần Др3).

## 4. Chưa chắc / thiếu

1. **B-E của T9, T10 bị nối tắt theo hình vẽ** (xem §2). Netlist giữ nguyên như vẽ.
2. **R16/R17**: trên Э3 in «R6»/«R7» lần thứ hai; gán R16 = trên (B-E T4), R17 = dưới (B-E T5) là suy
   đoán theo thứ tự.
3. **R18** đọc rõ trên Э3 nhưng không có trong перечень (nhảy R17→R22); **R28** (560 Ом) có trong
   перечень và #248 nhưng không thấy trên Э3 ⇒ nghi R18 = R28.
4. **Д25**: Э3 in «Д23» hai lần; cái cạnh R29/R30 gán là Д25 theo vị trí trên #248.
5. **Д3 (2Д510А), Д4 (2Д202В)**: có trong перечень, không tìm thấy trên Э3 (không nằm trong netlist).
   Có thể nằm dưới tấm giấy gập che góc trên-trái ảnh (vùng x < 0,28, y < 0,33 của ảnh #233 bị một tờ
   trắng che) — **cần chụp lại góc này**, hoặc kiểm trên tấm.
6. **Д34…Д41**: Э3 ghi «Д34…Д40» (7), перечень 8 cái; netlist lấy 8 cái song song.
7. Thanh nối chân Ш1 1…10 và 18…31 trên Э3 trông liền nhau qua nếp gập; netlist tách làm +5 В và
   Корпус theo bảng 3Ш5 (p142). Nhãn chân 14 bị mép khung cắt («Управл −6,…В»).
8. Тр2 2, 3; Тр1 2а, 2б, 10 không nối (ghi `NC`).
9. Пр1/Пр4 vẽ chung một ký hiệu «Пр1 Пр4 „5А“» ⇒ coi là song song.
10. Chân Др5, Др7, Др8 không đánh số (1/2 tự đặt). Chiết áp R9, R36: 1 = đầu trên, 2 = đầu dưới, 3 = con trượt.
11. T24/Д23/R49/C43 — chức năng chưa rõ (§3). Vai trò chân 13/14 «Управл.» chưa rõ.
12. Tần số chuyển mạch phần +5 В không suy được từ hình; phải đo.
13. Cột «Кол.» trong перечень trang 234 lệch xuống một dòng: C55 = 1 (không phải 2), C53/C54 = 2 song song.

## 5. Điểm đo đề xuất

| TP | Điểm | Giá trị kỳ vọng |
|---|---|---|
| TP1 | N2 (Др3.1 / C17…C32 +) | +27 В |
| TP2 | N3 (sau Пр1/Пр4, C của T8…T11) | +27 В; sụt = cầu chì đứt |
| TP3 | Д1.к (N17) | ≈ 13 В (Д814Д 11,5…14 В) |
| TP4 | Д2.к (N18) | ≈ 9 В |
| TP5 | con trượt R9 (T13.б) | ≈ 5,0 В (= Uвых đặt) |
| TP6 | nút chuyển mạch N20 (E T9/Др1.1) | xung 0 … ≈ 27 В, đo tần số và độ rỗng |
| TP7 | N4 (nguồn tầng kích, Тр2.5) | ≈ 27 В ± xung |
| TP8 | +5 В (Ш1/1…10, C34) | 5,00 ± 0,26 В; gợn |
| TP9 | cực điều khiển Д31 (N23) | ≈ 0 В khi bình thường |
| TP10 | N33 (sau Пр3/Др5) | +27 В |
| TP11 | C của T19 / T16 | xung đa hài ≈ 8 кГц (ước lượng) |
| TP12 | N43 (E T21, Др6.1) | xung +27 В … ≈ −7 В |
| TP13 | Д33.к so với «шина M» | 9 В |
| TP14 | −6,3 В (Ш1/45, 46) | −6,3 В |
| TP15 | Ш1/11–12 | ~5 В 400 Гц khi có 36 В ở 25–33 |

## 6. Quy trình bật nguồn an toàn trên bàn

1. **Kiểm nguội (không cấp điện):** đo R giữa Ш1/1…10 và Корпус (không được ≈ 0: Д31 thủng / C34…C38
   thủng), giữa 41…48 và Корпус (C17…C32, Д5…Д18 thủng), giữa N20 và Корпус (Д5…Д18), C-E của T8…T11,
   T21. Kiểm thông Пр1, Пр4, Пр2, Пр3. Đo R(б-э) T9, T10 (giải quyết mục 4.1). Đo Тр1: R cuộn 1-2, 8-9.
2. **Tải giả:** +5 В: bắt đầu **≤ 25 %** = 1,33 Ом (3,75 А, 18,8 Вт); 50 % = 0,67 Ом; đầy tải 0,33 Ом/≥ 75 Вт
   (tính 15,0 А, 75,0 Вт — chọn điện trở ≥ 100 Вт có tản nhiệt). −6,3 В: 6,3 Ом/≥ 10 Вт cho 1 А,
   bắt đầu 25 Ом. Không chạy không tải hoàn toàn lần đầu (tải mồi R32+R33 chỉ 0,1 А).
3. **Nguồn 27 В hạn dòng:** đặt 27 В, giới hạn **0,5 А** cho lần cấp đầu (chưa nối tải lớn): kỳ vọng tiêu
   thụ chỉ vài chục мА + tải mồi. Nếu nguồn vào chế độ hạn dòng ngay → tắt, quay lại bước 1.
   Nếu có thể, nâng áp từ từ 0 → 27 В bằng nguồn điều chỉnh, quan sát dòng vào và TP3/TP4.
4. Đo TP3…TP5, TP8, TP14. Chỉnh R9 cho +5,00 В, R36 cho −6,30 В (chỉ khi các điểm khác đúng).
5. Nối 25 % tải, nâng giới hạn dòng lên **1,5 А** (tính toán 25 % tải ở η = 0,65 → 1,07 А). Kiểm TP6 (dạng
   xung, tần số), nhiệt độ T8…T11, Д5…Д18, Др1.
6. Tăng dần 50 % → 100 %; giới hạn dòng **≤ 5 А** (đầy tải +5 В và −6,3 В: 4,0–4,6 А ở η = 0,75…0,65).
   Không nâng giới hạn dòng để «ép» tấm chạy.
7. Kiểm crowbar riêng, **không** bằng cách nâng R9 trên tấm đang có tải lớn: tách Д32 khỏi tấm và thử bằng
   nguồn ngoài, hoặc nâng chậm R9 với nguồn vào hạn dòng 0,5 А và tải 25 % — ngưỡng tính 5,6–5,9 В.
8. ~5 В 400 Гц: chỉ cấp 36 В 400 Гц khi có máy phát 400 Гц có hạn dòng; đo 11–12.
9. Đi dây, kẹp que đo khi **đã tắt nguồn**; chú ý nhiệt T8…T11/T21 lắp trên tản nhiệt — không chạm khi
   đang chạy.
