# рис.23 — УЛП +12,6 В; 1 А (ЕУ3.215.452 Э3), khối У19

Nguồn: ảnh #225 (sơ đồ, trang 225; số cũ «193»), #226 (перечень, tr.226, Лист 93), #227 (tr.227, Лист 94). Bảng
`ric23_bom.csv`, `ric23_net.csv`; số liệu dưới đây do `e3_ric2223.py` tính.

**Tiêu đề in:**

* Trên sơ đồ: «УЛП I2,6 В; I А. Схема электрическая принципиальная (ЕУ3.215.452 Э3) Рис.23».
* Trên перечень: «Перечень элементов к схеме электрической принципиальной УЛП 12,6 В; 1А (рис.23)».

Khớp У19 (ЕУ3.215.452) trong `e4/p143.csv` và Bảng 7 của HDSD.

## 1. Topology

* **Ổn áp xung hạ áp (buck), không đảo cực.** Khoá T5 (2Т803А, n-p-n): collector ở +27 V sau Пр1 (N2), emitter là
  nút chuyển mạch N8. Diode xả 6 × 2Д510А (Д2…Д7, song song): cathode ở N8, anode ở КОРПУС. Cuộn Др2 (Д127,
  ЕУ4.751.077) từ N8 sang N10 (lá 7). Tụ C4 // C5 (2 × 220 µF/16 В) ở N10.
* **Lọc ra:** Др3 (ДМ-2,4-20 µH) + C6 (220 µF) + C9 (33 µF) ⇒ X:2. Kẹp quá áp **Д8 + Д9** (2 × Д814А nối tiếp, 14…17 V)
  từ X:2 xuống КОРПУС. Lọc vào: Др1 (ДМ-1,2-30 µH) + C1 (33 µF/100 В), sau đó là Пр1 1 А.
* **Tầng kích:**
  * T4 (2Т608Б) ghép Darlington với T5. R11 (330 Ω) nối B-E T5, R12 (1,2 k) nối từ base T4 sang base T5.
  * T3 (2Т203А, p-n-p, emitter ở +27 V) cấp dòng vào base T4. Base T3 nhận dòng qua R9 + R10 (2 × 10 k) xuống
    КОРПУС, C2 (1 µF) nối từ base T3 sang nút R9/R10.
  * T2 (2Т203А, p-n-p) dẫn thì kéo nút R9/R10 lên +27 V, làm T3 khoá và **tắt khoá**. Base T2 kéo lên +27 V qua
    R1 (1 k), nên mặc định T2 khoá và khoá T5 tự khởi động.
* **Mạch phản hồi dương / tần số:** R13 (2,2 k) + C3 (4700 pF) nối từ nút chuyển mạch N8 về base T2 (lá 8).
* **So sánh:** У1 = **140УД1А** cấp đơn cực.
  * Chân 7 nối X:2 (+12,6 V), chân 1 nối КОРПУС.
  * Chân 9: điện áp chuẩn = Д1 (Д818Д, 9 V) nuôi qua R15 (330 Ω) từ đầu ra, chia bởi R2/R3, rồi qua R6. C8 (1 µF)
    lọc nút này (khởi động mềm).
  * Chân 10: phản hồi từ bộ phân áp R16–R17–R18 lấy ở **N10 (trước Др3)**. R17 mắc kiểu biến trở (движок nối chân 3).
  * Chân 5 (ra) → R8 → base T1 (2Т312Б, n-p-n). R7 nối B-E T1. Emitter T1 nâng lên ≈ 0,7 V nhờ Д10 (2С139А) nuôi
    qua R5 (1,8 k). Collector T1 → R4 → base T2.
  * Khi Uвых tăng: chân 10 lên, chân 5 lên, T1 dẫn, T2 dẫn, T3/T4/T5 khoá.
  * HDSD §2.2.3 (trang 54) tả đúng chuỗi này cho УЛП +6,3 В cùng họ.
* **Hạn dòng / ngắn mạch:** T6 (2Т312Б, n-p-n) có base ở N10 và emitter ở X:2, nên Vbe = I·R_DC(Др3). Khi T6 dẫn,
  collector qua R14 (680 Ω) + R19 (10 k) kéo base T2 xuống, T2 dẫn và T3…T5 khoá. C7 (1 µF; + ở nút R14/R19, − ở X:2)
  tạo trễ cho mạch bảo vệ.
* **Đầu vào УПР. (X:1)** nối thẳng vào nút chuẩn R2/R3/C8/R6, tức chân 9 của У1 qua R6. **Chập X:1 xuống КОРПУС ⇒
  chuẩn = 0 ⇒ У1 ra cao ⇒ T1, T2 dẫn ⇒ tắt.** Để hở thì tấm chạy bình thường.

## 2. Giá trị danh định (từ bản vẽ)

* Điện áp chuẩn vào У1.9: `Uref = Vz·R3/(R2+R3) = 9·2,2/5,5 = 3,600 V`.
* Điện áp ra: `Uвых = Uref·(R16 + R17' + R18)/R18`, với R16 = 5,6 k, R18 = 2,7 k, R17' = 0…2,2 k.

| Đại lượng | Giá trị |
|---|---|
| Dải chỉnh | 11,07 V (R17' = 0) … 14,00 V (R17' = 2,2 k) |
| Uвых = 12,6 V | R17' ≈ 1150 Ω (gần giữa hành trình) |
| Dòng Д1 | (12,6 − 9)/330 − 9/5,5 k ≈ 9,3 mA (Д818: 10 mA danh định) |
| Dòng Д10 (thuận) | ≈ 6,6 mA |
| Ngưỡng kẹp Д8+Д9 | 14…17 V |
| Ngưỡng hạn dòng | I ≈ 0,6 V / R_DC(Др3); R_DC chưa biết, phải đo |

Lưu ý: phân áp lấy ở N10 nên Uвых tại X:2 thấp hơn mức đặt một lượng I·R_DC(Др3).

## 3. Chưa chắc / thiếu

1. **Sơ đồ chân 140УД1А:** vai trò các chân 9 (đảo), 10 (không đảo), 5 (ra), 7 (+U), 1 (−U/КОРПУС) được **suy ra
   từ hướng phản hồi** và khớp lời tả HDSD («cửa vào 10 … từ R17, cửa vào 9 … từ bộ chia R2, R3»). Chưa đối chiếu
   datasheet. Các chân hiệu chỉnh tần số **không vẽ**, coi như bỏ trống, cần kiểm trên tấm.
2. **Д10 (2С139А) vẽ chiều thuận** (anode ở emitter T1, cathode ở КОРПУС). Nếu thực tế lắp ngược (ổn áp 3,9 V) thì
   ngưỡng mở T1 là ≈ 4,6 V thay vì ≈ 1,4 V. Phải kiểm trên tấm.
3. **Các điểm cắt không có chấm**, đã đọc là *không nối*:
   * R16 cắt đường sense X:2;
   * dây R7 → emitter T1 cắt đường КОРПУС;
   * dây C4,C5 cắt đường sense.
4. **Kí hiệu cực C6:** nét «+» ở bản trên mờ (trông như «1»). Chọn + ở X:2 theo loại tụ К52 và vị trí.
5. **Др2:** перечень ghi «Д127 ЕУ4.751.077 Сп», trùng số Сп với Др2 của рис.22 (ghi không có «Д127»). Có thể là cùng
   một loại cuộn hoặc lỗi đánh máy; cần đối chiếu nhãn trên cuộn thật.
6. **Số chân Др1, Др2, Др3** không in. Dùng quy ước 1 = phía vào, 2 = phía ra.
7. **Số chân R17:** bản vẽ in 1, 2 (движок), 3. Dùng đúng các số đó.
8. **Chân C3 (gốm):** đánh số 1 = phía R13, 2 = phía base T2.
9. **Lá nối nội bộ 7, 8** chỉ ghi trong note. Khung chấm–gạch là ranh giới tấm, không phải dây.
10. Ảnh chụp đủ toàn bộ tờ gấp. Không có phần nào bị cắt ngoài lề trái trống (khung tên).

## 4. Điểm đo đề xuất

| TP | Điểm | Kỳ vọng |
|---|---|---|
| TP1 | N1 / N2 | +27 V |
| TP2 | N8 (emitter T5, cathode Д2…Д7) | xung +27 V ↔ ≈ −0,7 V |
| TP3 | N10 (lá 7) | ≈ 12,6 V + I·R_DC(Др3) |
| TP4 | X:2 | 12,6 V ± 0,63 V (Bảng 3 HDSD) |
| TP5 | cathode Д1 (N13) | ≈ 9 V |
| TP6 | У1.9 / У1.10 | ≈ 3,6 V cả hai khi ổn định |
| TP7 | У1.5, base T1, base T2 (lá 8) | tín hiệu điều khiển |
| TP8 | N10 − X:2 | sụt áp trên Др3, dùng để suy ngưỡng hạn dòng |

## 5. Quy trình cấp điện thử an toàn

1. Đo nguội: X:5–X:4 không chập; diode Д2…Д7 (6 song song, thử thuận/nghịch); Д8/Д9 không chập (thử bằng thang
   diode); R_DC Др3 (ghi lại); Пр1 thông.
2. Tải giả **13 Ω / ≥ 25 W** (12,6 V/1 A = 12,6 Ω; P = 12,6 W) giữa X:2 (+) và X:3 (−), cộng tải nhẹ ~1 kΩ. X:1
   để hở. Đấu dây khi đã tắt nguồn.
3. Nguồn 0…30 V, giới hạn **150 mA**, + vào X:5, − vào X:4. Nâng chậm. Từ ~14 V trở lên khoá phải đóng-cắt (TP2).
   Nếu dòng vào chạm giới hạn ngay từ vài volt: nghi T5/T4 chập C-E hoặc Д2…Д7 chập.
4. Lên 27 V, nâng giới hạn ~0,8 A (Iвх ≈ 12,6/(27·0,75) ≈ 0,62 A). Chỉnh R17 cho X:2 = 12,6 V.
   **Không để Uвых vượt 14 V** (Д8/Д9 bắt đầu kẹp và quá nhiệt).
5. Thử hạn dòng bằng cách giảm tải dần (10 Ω → 8 Ω) và xem Uвых sụt. Chưa chập X:2.
6. Thử X:1: chập X:1 xuống КОРПУС qua 100 Ω. Uвых phải về ≈ 0; nhả ra thì khởi động mềm (theo C8).
