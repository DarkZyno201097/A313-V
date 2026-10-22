# рис.22 — УЛП minus 20 В; 0,3 А (ЕУ3.215.451 Э3), khối У21

Nguồn: ảnh #221 (sơ đồ, trang 221; số cũ gạch «189»), #222 (перечень, «Лист 89», không có số trang viết tay),
#223 (tr.223, Лист 90), #224 (tr.224, Лист 91). Bảng `ric22_bom.csv`, `ric22_net.csv`; số liệu dưới đây do
`e3_ric2223.py` tính.

**Tiêu đề in trên bản vẽ:** «УЛП минус 20 В; 0,3 А. Схема электрическая принципиальная (ЕУ3.215.451 Э3)», tay ghi
«рис. 22». ⚠ Bảng 3/6 của HDSD tiếng Việt và `e4/p142.csv` ghi У21 = **ЕУ3.215.451-02, −23 В; 0,25 А** (bản dịch gọi
Hình 22 là «Bộ nguồn −23V; 0,3A»). Bản Э3 là bản gốc −20 В; biến thể −02 nhiều khả năng chỉ khác ở mức chỉnh R3/R5*
(chưa có tài liệu chứng minh).

## 1. Topology

* **Ổn áp xung đảo cực (inverting buck-boost), tự dao động.** Khoá cao áp T6 (2Т908А) + T7 (2Т608Б) ghép
  Darlington, collector ở +27 V sau cầu chì (N2). Emitter T6 = nút chuyển mạch N12. Cuộn Др2 (ЕУ4.751.077, chân 1→2)
  từ N12 xuống КОРПУС. Diode Д2 (2Д213А): cathode ở N12, anode ở N13. Khi khoá đóng, Др2 tích năng lượng; khi mở,
  Др2 kéo N12 xuống âm, Д2 dẫn và nạp C5…C8 (4 × 33 µF) ⇒ N13 ≈ −20 В so với КОРПУС.
* **Lọc ra:** Др3 (ДМ-0,4-100 µH) + C10 và C11 (33 µF) ⇒ X:3. Lọc vào: Др1 (ДМ-0,6-60 µH) + C1 (100 µF/70 В). Пр1 nằm
  **sau** C1.
* **Tầng kích (tham chiếu +27 В):** T5 và T8 (2Т203А, p-n-p) có emitter ở +27 В. Khi T5 dẫn, nút N8 được kéo lên,
  T8 khoá, T7/T6 khoá. R14 nối base–emitter T7, R13 nối base–emitter T6. R11//C4 là mạch tăng tốc cho base T8, R12
  kéo N8 xuống КОРПУС.
* **Bộ điều chế = đa hài đối xứng có điều khiển T1/T4** (2Т203А). Theo HDSD §2.2.3 (trang 54–55): C2 (680 pF) ghép
  collector T1 → base T4, C3* (2200 pF) ghép collector T3/base T1 → collector T4, T4 lái T5 qua lá 10. Đa hài
  tự khởi động khi có 27 В.
* **Khuếch đại sai lệch:** cặp vi sai T2/T3 (П307В, n-p-n), emitter chung qua R6 (5,6 k) xuống ray N13. Collector
  T2 là base T4, có tải R5* (68 k). Collector T3 là base T1, có tải R7 (120 k).
  * Base T3 = **điện áp chuẩn Д1 (Д818Д, 9 V danh định)** trên ray N13, nuôi qua R8 (750 Ω) từ КОРПУС,
    C9 (1 µF) mắc song song R8.
  * Base T2 = движок R3 của bộ phân áp КОРПУС–R2–R3–R4–N13.
* **Hạn dòng / ngắn mạch:** T9 (2Т312Б, n-p-n) có base qua R16 (150 Ω) ở X:3, emitter ở N13, nên Vbe = sụt áp do
  dòng tải trên **điện trở thuần của Др3**. Khi I·R(Др3) ≈ 0,6 В, T9 dẫn và hút dòng khỏi nút chuẩn (base T3) qua R15
  (100 Ω), đa hài ngừng mở khoá. HDSD ghi rõ «trở kháng thuần trở của cuộn chặn Др3 … cảm biến bảo vệ».
* **Đầu vào УПРАВЛЕНИЕ (X:1)** nối vào nút R2/R3 của bộ phân áp, không có điện trở nối tiếp.

## 2. Giá trị danh định (từ bản vẽ)

Bộ phân áp đặt base T2 ở `|Uвых|·(R4 + x·R3)/(R2+R3+R4)` so với ray âm. Cặp vi sai cân bằng khi giá trị này = Vz.
Từ đó:

`|Uвых| = Vz·(R2+R3+R4)/(R4 + x·R3)`, với R2 = R4 = 1 kΩ, R3 = 2,2 kΩ, x = vị trí движок tính từ đầu R4.

| Đại lượng | Giá trị |
|---|---|
| Dải chỉnh (Vz = 9 V) | 11,81 V (x = 1) … 37,80 V (x = 0) |
| |Uвых| = 20 V | x = 0,405 (phần dưới R3 ≈ 890 Ω) |
| Dòng Д1 qua R8 | (20 − 9)/750 = 14,7 mA (Д818: Iст danh định 10 mA) |
| Dòng phân áp ở 20 V | 4,76 mA |
| X:1 chập xuống КОРПУС (R2 bị nối tắt, x giữ nguyên) | |Uвых| ≈ 15,24 V — **không tắt hẳn** |
| Ngưỡng hạn dòng | I ≈ 0,6 V / R_DC(Др3) — R_DC chưa biết, phải đo |

Lưu ý: dải chỉnh lên tới 37,8 V chỉ là toán học. Thực tế bị giới hạn bởi Uвх, C5…C11 (30 V) và C4 (20 V, nằm ở phía
+27 V nên không liên quan).

## 3. Chưa chắc / thiếu

1. **Giao điểm T9.э ↔ C5…C8 / anode Д2 (N13):** trên ảnh, dây từ lá 7 đến emitter T9 cắt đường dọc C5…C8 mà
   **không thấy chấm nối**. Việc gộp vào N13 là suy theo chức năng: nếu không nối thì ray âm của khâu điều khiển
   không có đường về đầu ra, và lời tả trong HDSD về cảm biến Др3 cũng không thực hiện được. Phải kiểm bằng ohm kế
   trên tấm.
2. **Nhãn Д2** trên bản vẽ đọc như «12». Ký hiệu D2 lấy theo перечень.
3. **Nhãn R16** cạnh T9 đọc như «R6»/«R16». Chọn R16 vì R6 đã có ở cặp vi sai.
4. **Пр1:** bản vẽ ghi «1А», перечень ghi «ВП1-2-**2А** 250В».
5. **Kол. của Д1/Д2** bị lệch dòng (chỉ thấy một chữ «I»). Giả định mỗi loại 1 cái.
6. **Перечень #222 không có tiêu đề** («Перечень элементов … (рис.22)»): phần đầu tờ không thấy trong ảnh. Ảnh #222
   cũng không có số trang viết tay. Việc gán #222 cho рис.22 dựa trên: R1…R16 khớp sơ đồ, Лист 89 → 90 → 91 liên tục
   với #223–#224.
7. **Số chân Др1, Др3** không in. Dùng quy ước 1 = phía vào, 2 = phía ra. Др2 có in số 1/2 trên bản vẽ.
8. **Số chân R3 (СП5-3):** quy ước 1 = phía R2, 2 = движок, 3 = phía R4. Bản vẽ không in số chân.
9. **Chân C2/C3 (gốm, không cực tính):** đánh số 1/2 theo thứ tự trái → phải trên bản vẽ.
10. **Mức logic X:1:** bản vẽ không cho biết nguồn ngoài (3Ш7/31) kéo X:1 lên mức nào. Chập X:1 xuống КОРПУС chỉ làm
    Uвых tụt còn ~15 V; muốn tắt hẳn phải kéo X:1 về phía dương. Cần xem sơ đồ khối nơi 3Ш7/31 được điều khiển.
11. **Biến thể −02 (−23 В; 0,25 А)** chưa có Э3/перечень riêng.
12. **Lá nối nội bộ 2, 6, 7, 8, 9, 10** (đánh số trên bản vẽ) chỉ được ghi trong cột note, không tách thành linh kiện.
    Khung chấm–gạch là ranh giới tấm/màn chắn, không phải dây dẫn.

## 4. Điểm đo đề xuất

| TP | Điểm | Kỳ vọng |
|---|---|---|
| TP1 | N1 (C1+) / N2 (sau Пр1, lá 9) | +27 V; chênh N1–N2 = sụt trên cầu chì |
| TP2 | N12 (emitter T6, Др2.1) | xung chữ nhật +27 V ↔ ≈ −20,7 V; xem f và độ rộng xung |
| TP3 | N13 (lá 7, anode Д2) | ≈ −20 V có gợn |
| TP4 | X:3 | −20,0 V (chỉnh R3) |
| TP5 | N16 (base T3, cathode Д1) | ≈ +9 V so với N13 |
| TP6 | N17 (движок R3) so với N13 | ≈ 9 V, tức bằng TP5 |
| TP7 | X:3 − N13 | sụt áp trên Др3 = I·R_DC, dùng để suy ngưỡng hạn dòng |
| TP8 | collector T1, T4 (N3, N6) | dao động đa hài |

## 5. Quy trình cấp điện thử an toàn (bàn thử)

1. Tắt nguồn rồi mới đo nguội: R giữa X:5 và X:2/X:4 (không chập), R_DC của Др3 (ghi lại), Пр1 có thông. Kiểm Д2
   và các B-E/B-C của T6, T7, T9 bằng thang diode.
2. Đấu tải giả **68 Ω / ≥ 10 W** (20 V/0,3 A = 66,7 Ω; P = 6 W) giữa X:2 (+) và X:3 (−). Dùng thêm tải nhẹ ~1 kΩ
   để đo không tải. X:1 để hở. Tắt nguồn khi đi dây.
3. Nguồn DC 0…30 V, **giới hạn dòng 100 mA**. + vào X:5, − vào X:4. Tăng từ từ 0 → 12 V, theo dõi dòng vào. Ở
   12 V đa hài phải chạy (TP2 có xung).
4. Lên 27 V, nâng giới hạn lên ~400 mA (Iвх ≈ 20·0,3/(27·η) ≈ 0,3 A ở η ≈ 0,75). Chỉnh R3 cho X:3 = −20,0 V
   (hoặc −23 V nếu tấm là −02).
5. Thử hạn dòng: giảm tải từng bước xuống ~50 Ω rồi ~40 Ω và quan sát Uвых sụt. **Không chập X:3 trực tiếp**
   trước khi đã xác nhận ngưỡng ở bước này.
6. Thử X:1: chỉ đo phản ứng khi chập X:1 qua 1 kΩ xuống КОРПУС, dự kiến Uвых về ~−15 V. Không đưa điện áp ngoài
   vào X:1 khi chưa rõ mức của 3Ш7/31.
