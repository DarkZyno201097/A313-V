# рис.26 — УЛП минус 12,6 В; 1 А (ЕУ3.215.470 Э3), khối У22 của A-313-3

Nguồn: ảnh #239 (trang 237, sơ đồ), #241 (trang 239, перечень «Лист 106»).
Tên in trên bản vẽ: «УЛП минус 12,6 В; 1 А. Схема электрическая принципиальная (ЕУ3.215.470 Э3) Рис.26».

**Ảnh thiếu**: trang 238 (Лист 105 — phần đầu перечень: tiêu đề + **toàn bộ điện trở R1…R18**) và
trang 240 (Лист 107 — **transistor T4…T9**; ảnh #240 chụp nhầm sàn nhà). Trang 239 chỉ có tụ, Д1, Д2, Др1–Др3, Пр1, T1–T3.
Qua giấy mỏng thấy lờ mờ chữ trang 240: dòng T4, T5, T8 «…365.007 ТУ» (ТУ của 2Т203А), T6 «…365.004 ТУ», T7 «…365.008 ТУ» — chỉ là gợi ý.
Tờ sơ đồ được chụp trọn (khung, bảng đầu cắm, khung tên); có vệt phản chiếu ở góc trái dưới nhưng không che linh kiện.

File kèm: `ric26_bom.csv` (47 ký hiệu, 24 dòng name = «?»), `ric26_net.csv` (106 chân, 25 net, 21 net N#).

## 1. Đầu cắm

| Конт | Цепь trên bản vẽ | Nghĩa | Э4 (У22) |
|---|---|---|---|
| 1 | Управлен. | điều khiển | УПРАВЛЕНИЕ 3Ш7/32 |
| 2 | «+» } 12,6 В 1 А | cực «+» của ra = корпус | КОРПУС |
| 3 | «−» } | **−12,6 В ra** | −12,6В 1А |
| 4 | «−» } вход 27 В | cực «−» vào = корпус | КОРПУС |
| 5 | «+» } | **+27 В vào** | +27В ВХ |

Конт. 2 và 4 nối với nhau ngay ở bảng ⇒ một net «Корпус».

## 2. Topology — ổn áp xung kiểu buck-boost đảo cực (27 V → −12,6 V)

Khớp với mô tả HDSDKT §2.2.3 (trang 54–55 bản tiếng Việt).

1. **Lọc vào**: конт. 5 → Др1 (ДМ-1,2) → C1 К52-5 100 µF/70 V xuống корпус → Пр1 ВП1-2 2 A → thanh «+27 V sau Пр1».
2. **Khoá công suất**: T6 (n-p-n, к ở +27 V) + T7 (n-p-n, Darlington) nối +27 V vào nút SW; R14 xả b-e T6, R15 xả gốc T7 về SW.
   T8 (p-n-p, э ở +27 V) cấp dòng gốc cho T7. Đi-ốt ngược Д2 2Д213А: anode ở thanh −12,6 V, cathode ở SW; C14 0,047 µF song song Д2.
   Cuộn tích luỹ Др2 Д213В: chân 1 ở SW, chân 4 ở корпус, chân 2–3 nối tiếp (hai nửa cuộn).
   T6 mở: dòng nạp Др2 từ +27 V; T6 khoá: Др2 kéo SW xuống âm, Д2 dẫn, rút điện tích từ C6…C11 ⇒ thanh ra âm.
   CCM lý tưởng: D = U/(U+Uвх) = **0,318** ở 27 V (0,298…0,344 ở 29,7…24 V); áp ngược trên T6/Д2 ≈ 39,6 V (42,3 V ở 29,7 V);
   dòng TB qua Др2 ≈ 1,47 A ở tải 1 A.
3. **Lọc ra**: C6…C11 (6 × К53-1А 33 µF/30 V song song, «+» về корпус) → Др3 (ДМ-1,2) → C12, C13 (2 × 68 µF/16 V) → конт. 3.
4. **Bộ điều chế**: đa hài đối xứng T1 (2Т203А, p-n-p) và T4 (p-n-p, loại chưa rõ), tụ ghép C2 680 pF và **C3 2200 pF (không bằng nhau ⇒ hai nửa chu kỳ khác nhau, cố ý)**,
   R1/R9 tải cực góp, R5/R7 điện trở gốc về корпус. Lối ra lấy ở э T4 (nút «7», R8 từ +27 V) → gốc T5 (p-n-p).
   T5 dẫn ⇒ nút R12/R13 lên +27 V ⇒ T8 khoá ⇒ T6 khoá. T5 tắt ⇒ R13 kéo xuống ⇒ T8–T7–T6 mở. C4 1 µF tăng tốc chuyển mạch T8.
5. **Khuếch đại sai lệch**: cặp vi sai T2, T3 П307В (n-p-n), đuôi chung R6* (chọn khi chỉnh) về thanh −12,6 V.
   Gốc T3 = Uвых + 9 V (Д1 Д818Д, anode ở thanh ra, R10 từ корпус). Gốc T2 = con trượt R3 trên phân áp корпус–R2–R3–R4–thanh ra.
   Cực góp T2, T3 rút dòng từ hai nút gốc của đa hài ⇒ thay đổi độ rộng xung. Cân bằng khi
   **U = 9 V·(R2+R3+R4)/(R4 + k·R3)** — cần tỉ số 1,400; không tính tiếp được vì thiếu R2…R4 (trang 238).
6. **Bảo vệ quá dòng**: điện trở thuần của Др3 làm shunt. T9: э ở thanh trước Др3, gốc ở điểm chia R17 (về phía trước Др3) / R18 (về phía sau Др3).
   Quá dòng ⇒ T9 dẫn ⇒ qua R16, R11 kéo gốc T5 xuống ⇒ T5 dẫn ⇒ khoá T6. C5 330 pF lọc nhiễu nút R16/R11.
   Ngưỡng: Iкз ≈ Ube·(R17+R18)/(R17·R_Др3) — chưa có số.
7. **Управление (конт. 1)** nối vào nút R2/R3: kéo nút này lệch đi làm cặp vi sai bão hoà ⇒ dùng để tắt/bật khối từ tấm kiểm tra (3Ш7/32). Mức logic chưa rõ.

## 3. Điểm đo

| TP | Điểm (net) | Danh định / quan sát |
|---|---|---|
| TP1 | конт. 5 → корпус | +27 V (24…29,7 V) |
| TP2 | N2 (sau Пр1) | = TP1; nếu 0 ⇒ Пр1 đứt |
| TP3 | N12 (cathode Д1) so với thanh ra | +9 V |
| TP4 | N9 (con trượt R3) | = TP3 khi ổn định |
| TP5 | N8 (э T4, nút 7) | xung vuông, đo dao động ký (đất ở корпус) |
| TP6 | N17 SW | xung 0 ↔ +27 V / ↔ −13,3 V; D ≈ 0,32 |
| TP7 | N3 (trước Др3) / конт. 3 | −12,6 V ±0,63 V; chênh nhau = I·R_Др3 |
| TP8 | N19 → N3 (Ube T9) | < 0,4 V khi tải định mức |
| TP9 | конт. 1 | mức điều khiển — đo trên khối đang chạy tốt trước |

## 4. Chưa chắc / thiếu

1. **Trang 238 không có ảnh** ⇒ không biết loại/giá trị R1…R18 (R3 biến trở chỉnh, R6* chọn). Chụp bổ sung, hoặc đọc màu/mã trên mạch in.
2. **Trang 240 không có ảnh** ⇒ không biết loại T4…T9. Cực tính trong net suy từ mũi tên + chức năng: T4, T5, T8 p-n-p; T6, T7, T9 n-p-n. Mũi tên T9 trên ảnh mờ.
3. HDSDKT nói «các đi ốt Д2–Д9» và «−12,6 V 0,3 A»; sơ đồ và перечень chỉ có Д2 và ghi 1 A. Theo bản vẽ.
4. Dây từ nút «7» (gốc T5) xuống R11 và dây từ конт. 1 xuống nút R2/R3 chạy sát mép khung chấm-gạch — đọc theo ảnh, độ tin **trung bình**.
5. Số chân Др1, Др3 không in; Др2 có in 1-2-3-4, 2 và 3 vẽ liền (coi là nối tiếp).
6. Các số 6, 7, 8, 9, 10 trên mép khung là đầu nối giữa các tấm con bên trong khối, không phải chân đầu cắm.

## 5. Quy trình cấp điện thử trên bàn

1. **Nguội**: Пр1 thông mạch; конт. 5 → корпус không chập (C1 nạp dần); конт. 3 → корпус: đo hai chiều, tìm Д2/C6…C13 chập.
   T6 к-э (+27 V ↔ SW) không chập. Kiểm C6…C11 rò (К53-1А 30 V chạy sát 13,3 V + gợn — hay hỏng).
2. Tải giả ở конт. 3: **25 Ω/10 W** (≈ 0,5 A) cho lần đầu, sau đó 12,6 Ω/20 W (1 A). Lần đầu **có tải nhẹ 250 Ω** (≈ 50 mA) — buck-boost không tải có thể vọt áp nếu vòng hồi tiếp hở.
   Đặt thêm Zener/tải kẹp ~15 V trên ra hoặc theo dõi bằng đồng hồ có ngưỡng: C12/C13 chỉ 16 V.
3. Nguồn 27 V bàn **giới hạn dòng 0,2 A**, tăng chậm từ 0 V. Đúng cực: «+» vào конт. 5, «−» vào конт. 4.
   Конт. 1 để hở trước (ghi lại nếu khối không chạy — có thể cần mức «cho phép»; đo trên khối tốt trước).
4. Ở ~10 V vào: đo TP5 phải có dao động (đa hài khởi động). Không dao động ⇒ T1/T4/C2/C3/R1/R5/R7/R9.
5. Tăng lên 27 V: TP7 phải ≈ −12,6 V. Chỉnh R3 nếu lệch. Dòng vào ≈ 12,6·I/(27·η) — với 50 mA tải ⇒ ≈ 30–40 mA.
6. Gắn tải 1 A, nâng giới hạn lên 0,8 A (dự kiến ≈ 0,6 A ở η ≈ 0,75). Đo gợn ra, nhiệt T6, Д2, Др2.
7. Thử bảo vệ: giảm tải dần (không chập trực tiếp), quan sát TP8 và dòng vào giảm đột ngột khi T9 tác động. **Không** ngắn mạch ra khi chưa biết ngưỡng.
