# Рис.20 — УЛП +20 В; 0,3 А (ЕУ3.215.446), khối У18 của A-313-3

Nguồn: ảnh #215 (sơ đồ Э3, trang tay 214), #216–#218 (ПЭ, trang 215–217, «Лист 82–84», 6 декабря 1979 г.).
Bản ghi: `ric20_bom.csv` (44 ký hiệu), `ric20_net.csv` (98 chân, 22 net N# + 4 net đầu nối).
Kiểm tra chéo + tính số: `ric_check.py` (bom↔net khớp hoàn toàn, mọi N# ≥ 2 chân).

Đầu nối 5 chân (bảng trên sơ đồ): 1 — Управление; 2 — «+} 20 В»; 3 — «−} 0,3 А»; 4 — «−} 27 В»;
5 — «+} вход». Trên sơ đồ **chân 3 và 4 nối với nhau** ⇒ cùng là КОРПУС (khớp p143/p144).

## 1. Cấu trúc

**Ổn áp xung hạ áp (buck) kiểu trễ/tự dao động** — HDSDKT §2.2.3 xếp +20 V vào nhóm «ổn áp bù trừ có
điều chỉnh xung». Không có máy phát xung riêng: tần số do vòng hồi tiếp dương + gợn ra quyết định.

| Khối | Linh kiện | Ghi chú |
|---|---|---|
| Lọc vào | Др1 (ДМ-1,2-30 µH) + C1 68 µF/50 V, Пр1 1 A | chống nhiễu ngược về lưới 27 V |
| Khoá công suất | Т3 П701А (n-p-n) + Т4 2Т608Б → Darlington, collector ở +27 V | R7 220k (B-E Т3), R8 1,2k (B Т4 → B Т3) |
| Mạch kích | Т5 2Т203А (p-n-p, emitter +27 V) cấp dòng gốc Т4; Т1 2Т203А (p-n-p) đảo pha | R14 10k ∥ C9 1 µF (tụ tăng tốc) vào gốc Т5; R6 10k tải collector Т1 |
| Điốt ngược | Д1 ∥ Д2 (2Д510А ×2, «Параллельно») | anot về КОРПУС |
| Lọc ra | Др2 (Д126) + C3 100 µF + C7 33 µF; lọc thứ cấp Др3 (ДМ-1,2-30) + C4 100 µF | |
| Điện áp chuẩn | Д3 Д818Д cấp qua R11 **từ đầu ra +20 V**; chia R10 5,62k / R17 2,21k (1%); C5 4,7 µF | Vref ≈ 2,54 V |
| Khuếch đại sai số | У1 140УД1А: chân 10 ← hồi tiếp, chân 9 ← chuẩn qua R16, chân 7 ← +Uп (Д3), chân 1 ← chung | ra chân 5 → R4 → gốc Т2 |
| Tầng đệm | Т2 2Т312Б (n-p-n), emitter qua Д5 (2Д510А) xuống КОРПУС, R5 kéo gốc xuống | collector qua R3 kéo gốc Т1 |
| Hồi tiếp dương | C2 1200 pF + R2 2,2k từ nút chuyển mạch về gốc Т1 | tạo trễ, quyết định tần số |
| Bơm gợn | R9 2,2k + C8 0,047 µF từ trước Др3 về chân 10 | |
| Bù điện áp vào | R20 820k từ +27 V (sau Пр1) vào chân 10 | |
| Hạn dòng / ngắn mạch | Т6 2Т312Б: B qua R19 150 Ω ở phía trước Др3, E ở phía sau (+20 V ra) ⇒ sụt áp trên điện trở thuần Др3; collector → R15 1,5k → (cọc 7) → R18 12k → gốc Т1; C6 1 µF trễ | |

Logic điều khiển (suy từ sơ đồ, khớp mô tả УЛП 6,3 V trong HDSDKT trang PDF 54):

* У1 ra **cao** ⇒ Т2 dẫn ⇒ kéo gốc Т1 xuống ⇒ Т1 dẫn ⇒ collector Т1 ≈ +27 V ⇒ Т5 khoá ⇒ Т4/Т3 **khoá**.
* У1 ra **thấp** ⇒ Т2, Т1 khoá ⇒ R6 kéo collector Т1 xuống, R14 kéo gốc Т5 ⇒ Т5 dẫn ⇒ Т4/Т3 **dẫn**.
* Hồi tiếp: U(chân 10) > U(chân 9) ⇒ ra cao ⇒ cắt. Vậy chân 10 là vào không đảo, chân 9 là vào đảo
  (suy từ logic, **chưa đối chiếu sơ đồ chân 140УД1**).
* Khởi động: У1 lấy nguồn từ chính đầu ra (R11 → Д3). Lúc chưa có Uвых, У1 không hoạt động, Т2 khoá ⇒
  khoá công suất mặc định **dẫn** ⇒ tự khởi động. C5 làm Vref tăng chậm (soft-start τ ≈ 7,5 ms).
* **«УПРАВЛЕНИЕ» (chân 1)** nối thẳng vào nút chuẩn (R10/R17/C5/R16). Kéo chân 1 xuống КОРПУС ⇒
  Vref = 0 ⇒ chân 10 > chân 9 ⇒ У1 ra cao ⇒ **tắt nguồn**. Để hở ⇒ chạy bình thường.
  (Mức logic cụ thể do tấm kiểm tra/A-313-12 cấp — chưa có sơ đồ phía đó.)
* Hạn dòng: I·R_DC(Др3) ≥ ~0,6 V ⇒ Т6 dẫn ⇒ kéo gốc Т1 xuống qua R15–R18 ⇒ Т1 dẫn ⇒ cắt khoá. Ngưỡng phụ
  thuộc R_DC(Др3) (chưa biết): 0,1 Ω → ~6 A; 0,3 Ω → ~2 A; 1 Ω → ~0,6 A (`ric_check.py`). R19* chọn
  khi chỉnh — có lẽ để hiệu chỉnh ngưỡng này.
* **Không có mạch bảo vệ quá áp riêng** trong УЛП +20 V (không có ổn áp kẹp đầu ra như Д5 ở рис.21).
  Quá áp do tấm kiểm tra (K1/K3) xử lý bằng tín hiệu ОТКЛ. cắt 27 V.

## 2. Giá trị danh định (tính bằng `ric_check.py`)

* Vref = 9 V · 2,21/(5,62 + 2,21) = **2,54 V** (giả định Д818Д = 9 V danh định).
* Uвых = Vref · (R12 + R13)/R13_dưới. Với R12 = 5,62k, R13 = 2,2k:
  20 V ⇔ R13_dưới ≈ **993 Ω (~45 % hành trình)**. Con trượt lên đỉnh ⇒ Uвых ≈ 9,0 V; con trượt xuống
  đáy ⇒ không có chặn (vòng hở, Uвых → ~27 V). **Chỉnh R13 cẩn thận, không vặn về đáy khi có tải nhạy.**
* R20 820k: kéo Uвых thấp đi ≈ 0,22 V ở 27 V vào; ΔUвх ±3 V ⇒ ±25 mV đầu ra (bù theo lưới).
* Dòng nuôi Д3 + У1 qua R11: nếu R11 = 680 Ω ⇒ 16 mA, 0,18 W (hợp với loại 1 W); nếu đúng 680 kΩ như in
  ⇒ 16 µA, không đủ nuôi 140УД1 + Д818Д. ⇒ nghi in sai, **phải đo R11 trên mạch**.

## 3. Chưa chắc / thiếu

1. **Tiêu đề, khung tên và số «Рис.20» không có trong ảnh #215** — tờ gấp chỉ chụp phần sơ đồ, khung tên
   (bên trái/trên) bị cắt. Định danh lấy từ ПЭ (#216) và trang.csv.
2. R11: in «680кОм», nghi 680 Ом (xem §2).
3. Dấu «*»: ПЭ ghi **R19\***, sơ đồ đặt «*» cạnh **R20**. Chưa rõ cái nào chọn khi chỉnh (có thể cả hai).
4. Chân dưới của У1 đọc «1» (nét mờ, có thể là «4»). Vai trò chân 9/10/7/1 suy từ logic mạch, chưa đối
   chiếu datasheet 140УД1.
5. Kiểu Т6 (n-p-n hay p-n-p) trên sơ đồ không rõ hướng mũi tên; lấy theo ПЭ (2Т312Б, n-p-n) — logic
   hạn dòng chỉ đúng với n-p-n nên nhất quán.
6. C3, C4: cột «Кол.» để trống trong ảnh ПЭ.
7. R10 = 5,62 kΩ nhưng in ±10% (giá trị E96 thường đi với 1%) — ảnh hưởng độ chính xác Vref.
8. Điện trở thuần Др3 (ДМ-1,2-30) chưa biết ⇒ ngưỡng hạn dòng chưa tính được.
9. Không có Д4 (ПЭ và sơ đồ đều bỏ qua số này).
10. Các cọc 6/6, 1, 8, 7/7 trên khung gạch-chấm: là điểm nối giữa các mạch con/tấm trong vỏ УЛП —
    không ảnh hưởng netlist, nhưng là chỗ hàn/đo thuận tiện.

## 4. Điểm đo đề xuất

| TP | Net | Kỳ vọng (27 V vào, tải danh định) |
|---|---|---|
| TP1 | N2 (sau Пр1) | 27 V, gợn nhỏ |
| TP2 | N8 nút chuyển mạch (emitter Т3) | xung chữ nhật 0 … ~26 V (đáy ≈ −0,7 V do Д1/Д2) |
| TP3 | N10 (trước Др3) | ~20 V + gợn tam giác nhỏ |
| TP4 | X:2 (+20 V) | 20 V ± chỉnh R13 |
| TP5 | N18 (catot Д3, chân 7 У1) | ~9 V |
| TP6 | X:1 / nút chuẩn | ≈ 2,54 V |
| TP7 | У1:10 | ≈ TP6 (vòng đã khoá) |
| TP8 | У1:5 | xung, đồng bộ TP2 (ngược pha) |
| TP9 | N3 gốc Т1 | xung; khi ngắn mạch bị Т6 kéo |

## 5. Thủ tục cấp điện lần đầu trên bàn (ngoài khối)

1. Đo nguội: điện trở X:5–X:3,4 (không chập), X:2–X:3,4 (không chập; thấy C3/C4 nạp), Т3 C-E không
   chập; đo R11 để giải quyết nghi vấn 680 Ω/680 kΩ; đo R_DC Др3.
2. Đặt R13 về khoảng giữa (≈ 45 %) nếu đã bị vặn — **không** để con trượt ở đáy.
3. Tải giả: 20 V/0,3 A ⇒ **68 Ω ≥ 10 W** (66,7 Ω danh định; 6 W tiêu tán). Lần đầu dùng ~200 Ω (0,1 A, 2 W).
4. Nguồn 27 V, **giới hạn dòng 0,15 A** lần đầu (dòng vào ≈ 20·0,1/27/η ≈ 0,09 A ở η ≈ 0,8). Chân 1
   УПРАВЛЕНИЕ để hở (hoặc qua công tắc xuống КОРПУС để thử chức năng tắt).
5. Tăng dần 0 → 27 V, quan sát TP4 và dòng vào. Nếu dòng vào vọt mà TP4 không lên ⇒ tắt ngay (nghi
   khoá thủng/Д1-Д2 chập/C3 chập).
6. Dao động ký TP2 + TP4: phải có xung đóng cắt, tần số ổn định; chỉnh R13 cho 20,0 V.
7. Thử УПРАВЛЕНИЕ: nối chân 1 xuống КОРПУС ⇒ TP4 phải về 0; nhả ra ⇒ khởi động lại mềm.
8. Thử tải danh định 68 Ω, rồi tăng giới hạn dòng nguồn lên ~0,4 A. Thử hạn dòng bằng tải điện tử tăng
   dần (không chập cứng) cho tới khi TP4 sụt — ghi lại dòng ngưỡng.
9. Thử dải vào 24 … 30 V (lưới 27 V ±10 %), ghi Uвых.
