# Рис.21 — УЛП 6,3 В; 0,5 А (ЕУ3.215.448-01), khối У20 của A-313-3

Nguồn: ảnh #219 (sơ đồ Э3, trang tay 218; khung tên «УЛП 6,3 В; 0,5 А. Схема электрическая
принципиальная (ЕУ3.215.448-01) Рис.21» có trong ảnh), #220 (ПЭ trang 219, «Лист 86»).
Bản ghi: `ric21_bom.csv` (46 ký hiệu), `ric21_net.csv` (102 chân, 21 net N# + 4 net đầu nối).
Kiểm tra chéo + tính số: `ric_check.py` (bom↔net khớp hoàn toàn, mọi N# ≥ 2 chân).
HDSDKT (`A313 original/A-313-3.HDSDKT.pdf`, trang PDF 54) mô tả chính khối này — khớp với bản trích.

Đầu nối 5 chân (bảng trên sơ đồ): 1 — Управл.; 2 — «+} **+5 В**»; 3 — «−} 0,5 А»; 4 — «−} 27 В»;
5 — «+} вход». Chân 3 và 4 nối với nhau ⇒ КОРПУС.

## 1. Cấu trúc

**Ổn áp xung hạ áp (buck) kiểu trễ**, cùng họ với рис.20 nhưng mạch kích khác:

| Khối | Linh kiện | Ghi chú |
|---|---|---|
| Lọc vào | Др1 + C1 68 µF/50 V, Пр1 «1,0 А» | |
| Khoá công suất | Т5 П701А (n-p-n) + Т4 2Т608Б (Darlington, collector +27 V) | R12 220 Ω (B-E Т5), R13 1,2k (B Т4 → B Т5) |
| Mạch kích | Т3 2Т203А (p-n-p, emitter +27 V) cấp gốc Т4; Т2 2Т203А (p-n-p) | R10 10k ∥ C2 1 µF từ collector Т2 vào gốc Т3; R11 10k kéo collector Т2 xuống КОРПУС (qua cọc 3) |
| Điều chế | Т1 2Т312Б (n-p-n), emitter qua Д7, R9 kéo gốc xuống, R7 từ У1:5 | collector qua R5* kéo gốc Т2; R4 3,3k kéo gốc Т2 lên +27 V |
| Điốt ngược | Д2…Д4 (HDSDKT: «đi ốt ngược») ∥ C10 | |
| Lọc ra | Др2 + C4, C5 (HDSDKT: «Др2 cùng C4, C5 tạo bộ lọc san bằng») + C8; Др3 + C6 | |
| Kẹp quá áp | Д5 (ổn áp) catot ở đầu ra, anot КОРПУС | chỉ là kẹp, không có mạch cắt |
| Điện áp chuẩn | Д1 (ổn áp) cấp qua R1 1,2k/1 W **từ +27 V**; chia R2 5,62k / R3 2,21k (1%); C9 | Vref ≈ 2,54 V nếu Д1 = 9 V |
| Khuếch đại sai số | У1 140УД1А: 10 ← con trượt R17; 9 ← chuẩn qua R8; 7 ← +Uп (Д1); 1 ← chung; 5 → R7 | |
| Hồi tiếp dương | R14 2,2k + C3 1200 pF từ nút chuyển mạch về gốc Т2 | |
| Bơm gợn | C11 + R6 2,2k từ trước Др3 vào У1:10 | |
| Chia hồi tiếp | R16 274 Ω (1%) + R17 2,2k (СП5-3, con trượt → У1:10) | HDSDKT: «Điện áp ra được xác lập nhờ R17» |
| Hạn dòng | Т6 2Т312Б: B nối thẳng phía trước Др3, E ở đầu ra ⇒ sụt áp trên R_DC(Др3); collector → R15 1,5k → (cọc 10) → R18* 27k → (cọc 8) → gốc Т2; C7 trễ | HDSDKT: «T6 mở T2, T2 phân nhánh B-E của T3 và đóng nó» |

Logic điều khiển:

* У1 ra **cao** ⇒ Т1 dẫn ⇒ kéo gốc Т2 xuống ⇒ Т2 dẫn ⇒ collector Т2 ≈ +27 V ⇒ qua R10∥C2 gốc Т3 lên
  bằng emitter ⇒ Т3 khoá ⇒ Т4/Т5 **khoá** (HDSDKT: «T1, T2 mở, T3–T5 đóng»).
* У1 ra **thấp** ⇒ Т1, Т2 khoá ⇒ R11 kéo collector Т2 xuống ⇒ Т3 dẫn ⇒ Т4/Т5 **dẫn**.
* Khác рис.20: У1 và Д1 được nuôi **từ 27 V vào** (R1), không phải từ đầu ra.
* Soft-start: C9 ∥ R3 trên nút chuẩn ⇒ Vref tăng chậm (τ = C9·(R2∥R3) = C9·1,586 kΩ; C9 chưa biết giá trị).
* **«УПРАВЛЕНИЕ» (chân 1)** nối thẳng vào nút chuẩn R2/R3/C9 (rồi qua R8 vào У1:9). Kéo chân 1 xuống
  КОРПУС ⇒ Vref = 0 ⇒ У1 ra cao ⇒ **tắt**. Để hở ⇒ chạy.
* Hạn dòng: I·R_DC(Др3) ≥ ~0,6 V ⇒ Т6 dẫn ⇒ kéo gốc Т2 xuống ⇒ cắt khoá. Không có R19 như рис.20; R18*
  (15/20/27/33 kΩ) là phần tử chọn để chỉnh ngưỡng/độ nhạy.

## 2. Giá trị danh định (tính bằng `ric_check.py`)

* Vref = VZ · 2,21/(5,62 + 2,21) = **2,54 V** nếu Д1 = 9 V (giả định giống Д818Д ở рис.20 vì cùng tỷ số
  chia 5,62/2,21; **chưa xác nhận** — trang ПЭ 220 thiếu).
* Uвых = Vref · (R16 + R17)/R17_dưới, R16 + R17 = 2,474 kΩ:
  * 6,3 V ⇔ R17_dưới ≈ **998 Ω (~45 %)**;
  * 5,0 V ⇔ R17_dưới ≈ **1 257 Ω (~57 %)**;
  * con trượt ở đỉnh ⇒ Uвых min ≈ 2,86 V; ở đáy ⇒ vòng hở.
* Dòng qua R1: (27 − 9)/1,2k = 15 mA, 0,27 W (R1 loại 1 W — hợp lý).

## 3. Chưa chắc / thiếu

1. **ПЭ trang 220 không có trong bộ ảnh** (kiemke: #220 = trang 219, #221 = trang 221). Thiếu tên/loại
   của C4…C11, Д1…Д5, Д7, Др1…Др3, Пр1, Т1…Т6, У1. Т1–Т6, У1 chỉ đọc được qua **bóng chữ xuyên giấy** ở
   phần dưới ảnh #220 (Т1, Т6 2Т312Б; Т2, Т3 2Т203А; Т4 2Т608Б; Т5 П701А; У1 140УД1А) — khớp sơ đồ (kiểu
   n-p-n/p-n-p) nhưng vẫn phải xác nhận. Các dòng C/Д/Др không đọc được.
2. **Điện áp ra mâu thuẫn**: tiêu đề và ПЭ ghi **6,3 В; 0,5 А**, bảng đầu nối trên sơ đồ ghi
   **«+5 В»**. Có thể bản vẽ dùng chung cho ЕУ3.215.448 (5 V) và -01 (6,3 V); chênh lệch chỉ nằm ở vị trí
   R17. Khối У20 thật là 6,3 V (p144: «КОНТР. +6,3В» ← У20/2) ⇒ chỉnh 6,3 V.
3. Nhãn R16 bị nếp gấp che (đọc như «R8»); xác định là R16 theo loại trừ (R8 đã có ở mạch У1:9) và theo
   HDSDKT «bộ chia R16–R18». HDSDKT nói «R16–R18» nhưng trên sơ đồ R18 thuộc mạch hạn dòng, không thuộc bộ
   chia — nghi lỗi văn bản (đúng là R16–R17).
4. Chân dưới У1 đọc «1» (rõ hơn рис.20). Vai trò 9/10 suy từ logic + HDSDKT.
5. Cực tính C2 (+ phía gốc Т3), C7 (+ phía R15/R18): đọc theo dấu «+» trên bản vẽ.
6. Không có Д6 trên sơ đồ.
7. Ngưỡng hạn dòng phụ thuộc R_DC(Др3) — chưa biết loại cuộn.
8. Cọc khung đánh số 6, 7, 8, 3, 10, 2 và một cọc không số sau Др2 / ở đường vào: chỉ là điểm nối giữa
   các mạch con trong vỏ.

## 4. Điểm đo đề xuất

| TP | Net | Kỳ vọng (27 V vào, tải danh định) |
|---|---|---|
| TP1 | N2 (sau Пр1) | 27 V |
| TP2 | N3 (catot Д1, У1:7) | VZ (≈ 9 V nếu đúng giả định) — có ngay khi cấp 27 V, kể cả khi khoá không chạy |
| TP3 | X:1 / nút chuẩn | ≈ 2,54 V; tăng chậm theo C9 |
| TP4 | У1:10 | ≈ TP3 khi vòng khoá |
| TP5 | У1:5 | xung |
| TP6 | N10 (collector Т2) | xung 0 … 27 V |
| TP7 | N14 nút chuyển mạch (emitter Т5) | xung 0 … ~26 V |
| TP8 | N16 (trước Др3) | ~6,3 V + gợn |
| TP9 | X:2 | 6,3 V |

## 5. Thủ tục cấp điện lần đầu trên bàn

1. Đo nguội: X:5–X:3,4 và X:2–X:3,4 không chập; Т5 C-E, Д2…Д4, Д5 (ổn áp kẹp đầu ra — nếu thủng sẽ
   thấy X:2 chập đất); đo R_DC Др3.
2. Đặt R17 ≈ 45 % (≈ 1 kΩ phần dưới) nếu đã bị vặn; không để ở đáy (vòng hở ⇒ Uвых lên tới ngưỡng kẹp
   Д5 và Д5 sẽ chịu dòng lớn).
3. Tải giả: 6,3 V/0,5 A ⇒ **12,6 Ω**, chọn **12–13 Ω ≥ 5 W** (3,2 W tiêu tán). Lần đầu ~33 Ω (0,19 A).
4. Nguồn 27 V **giới hạn 0,1 A** lần đầu (dòng vào ≈ 6,3·0,19/27/0,75 ≈ 0,06 A cộng ~15 mA nuôi Д1/У1).
5. Tăng 0 → 27 V. Kiểm TP2 trước (Д1/У1 có điện), rồi TP3, sau đó TP7/TP9.
6. Chỉnh R17 cho **6,3 V** (kiểm tấm kiểm tra dùng mức nào; p144: «КОНТР. +6,3В»).
7. Thử УПРАВЛЕНИЕ: chân 1 xuống КОРПУС ⇒ X:2 về 0; nhả ⇒ khởi động mềm.
8. Tải danh định 12,6 Ω, nâng giới hạn nguồn lên ~0,3 A. Thử hạn dòng bằng tải điện tử tăng dần; ghi
   ngưỡng. Thử 24 … 30 V vào.
