# 168КТ2Б / 168КТ2В
# BỘ CHUYỂN MẠCH (KHOÁ) TƯƠNG TỰ 4 KÊNH TRÊN MOSFET

**Phiên bản: Rev. C — 16/09/2026.** Đồng bộ phản biện A313-V.06; các giới hạn suy luận/đo thực được ghi riêng.

> **Linh kiện quan trọng nhất của tấm A313-V.05** — tấm này dùng **57 vỏ 168КТ2Б = 228 khoá tương tự**.
> Tấm A313-V.06 dùng thêm 12 vỏ 168КТ2Б + 3 vỏ 168КТ2В.

---

## 1. CÔNG DỤNG

**Четырёхканальный аналоговый переключатель, предназначенный для коммутации тока и напряжения.**

Bộ chuyển mạch tương tự 4 kênh độc lập, dùng để đóng/ngắt dòng và điện áp tương tự.
Mỗi kênh là **một khoá MOSFET** (transistor trường) với 3 chân: исток (source/vào), сток (drain/ra), затвор (gate/điều khiển).

* Nhà sản xuất: АО «ВОСХОД» — КРЛЗ
* Tiêu chuẩn: **АЕЯР.431160.166 ТУ** (loại quân sự, ОСТ В 11 0998-99)
* Chủng loại theo cấp: **168КТ2А / 168КТ2Б / 168КТ2В** — khác nhau ở điện áp giới hạn và dòng rò

---

## 2. VỎ VÀ CÁCH ĐÁNH CHÂN (ЦОКОЛЕВКА)

**Vỏ:** 401.14-5 — 14 chân, kim loại-gốm phẳng
* `401.14-5.07НБ` — mạ niken (ví dụ 168КТ2Т1ВК)
* `401.14-5М` — mạ vàng (ví dụ 168КТ2ТВК)

### Назначение выводов (chức năng từng chân)

| Chân | Chức năng | Ghi chú |
|---|---|---|
| **1** | Сток (drain) — kênh 1 | "đầu ra" kênh A |
| **2** | **Затвор (gate)** — kênh 1 | **chân điều khiển** kênh A |
| **3** | Исток (source) — kênh 1 | "đầu vào" kênh A |
| **4** | **Không sử dụng** | **A313-V để trống** ✔ đã xác minh |
| **5** | Исток — kênh 2 | kênh B |
| **6** | **Затвор** — kênh 2 | kênh B |
| **7** | Сток — kênh 2 | kênh B |
| **8** | Сток — kênh 3 | kênh C |
| **9** | **Затвор** — kênh 3 | kênh C |
| **10** | Исток — kênh 3 | kênh C |
| **11** | **ПОДЛОЖКА (đế / substrate)** | **A313-V để trống (thả nổi)** ✔ đã xác minh — xem §7 |
| **12** | Исток — kênh 4 | kênh D |
| **13** | **Затвор** — kênh 4 | kênh D |
| **14** | Сток — kênh 4 | kênh D |

**Tóm tắt:** chân **1, 7, 8, 14 = сток**; **2, 6, 9, 13 = затвор**; **3, 5, 10, 12 = исток**; **11 = подложка**; **4 = trống**.

### Ánh xạ sang ký hiệu trên sơ đồ A313-V

| Section trong Altium | Chân đầu vào | Chân điều khiển | Chân đầu ra |
|---|---|---|---|
| **U_x_A** | 3 | **2** | 1 |
| **U_x_B** | 5 | **6** | 7 |
| **U_x_C** | 10 | **9** | 8 |
| **U_x_D** | 12 | **13** | 14 |

Trên sơ đồ nguyên lý, chân điều khiển được vẽ bằng **mũi tên đỏ chỉ vào thân ký hiệu**.

---

## 3. CHẾ ĐỘ GIỚI HẠN (ПРЕДЕЛЬНО ДОПУСТИМЫЕ РЕЖИМЫ)

| Tham số | 168КТ2**А** | 168КТ2**Б** | 168КТ2**В** |
|---|---|---|---|
| **U_сп** (сток – подложка) | 10 V | **15 V** | **25 V** |
| **U_ип** (исток – подложка) | 10 V | **15 V** | **25 V** |
| **U_зп** (затвор – подложка) | −30 V | **−30 V** | **−30 V** |
| **I_ком** (dòng chuyển mạch) | 20 mA | 20 mA | 20 mA |
| Công suất tiêu tán | 100 mW | 100 mW | 100 mW |
| Nhiệt độ làm việc | −60…+100 °C | −60…+100 °C | −60…+100 °C |

**Sự kiện:** U1…U12 dùng Б; U16/U17/U18 dùng В. Datasheet gốc `168kt2.pdf` tr. 3 cho U_сп/U_ип so vớiподложка:15 V(Б),25 V(В); gate–подложка định mức 30 V. Các con số này **không phải điện áp đỉnh–đỉnh giữa hai đầu khoá**.

**Suy luận chưa đủ:** swing−23/+3,5 V=26,5 V không tự chứng minh lý do chọnВ, cũng không chứng minh vượt/đạt định mức 25 V. Đế đang thả nổi; chưa biết điện thế thực. Không suy dự trữ 3,5 V bằng 30−26,5. Giữ đúng chủng loại gốc; thay Б↔В phải kiểm toàn bộ điều kiện, không chỉ điện áp.

---

## 4. THAM SỐ ĐIỆN (T = 25 ± 10 °C)

| Tham số | Ký hiệu | Giá trị | Điều kiện đo |
|---|---|---|---|
| **Điện trở kênh mở** | R_си.отк | **≤ 100 Ω** | U_и = −5 V; U_с = 0 V; U_см.п = 5 V; U_з = −15 V; I_и = 0,1 mA |
| Thời gian mở | t_вкл | **≤ 0,3 µs** | U_и = −5 V; U_см.п = 5 V |
| Thời gian đóng | t_выкл | **≤ 0,7 µs** | U_и = −5 V; U_см.п = 5 V |
| Dòng rò сток | I_ут.с | ≤ 20 nA (А) … ≤ 100 nA (В) | |
| Dòng rò исток | I_ут.и | ≤ 100 nA | |
| Dòng rò затвор | I_ут.з | ≤ 20 nA | |

---

## 5. NGUYÊN LÝ LÀM VIỆC — ĐIỀU QUAN TRỌNG NHẤT CẦN NHỚ

**Giả thiết có cơ sở:** hành vi gate âm dẫn phù hợp MOSFET kênh p và điều kiện thử datasheet. Chưa đo trên tấm thực; điện thế gate phải xét so với kênh/đế, không chỉ so GND:

| Điện thế trên затвор (so với kênh) | Trạng thái khoá | Trở kháng исток–сток |
|---|---|---|
| **Âm** (theo datasheet: U_з = −15 V ở chế độ thử) | **MỞ / DẪN** | ≤ 100 Ω |
| **Dương / bằng 0** | **ĐÓNG / NGẮT** | > hàng chục MΩ (dòng rò < 100 nA) |

### Áp dụng trên A313-V

Cụm tạo xung tạo ra hai mức điều khiển:

| Tín hiệu điều khiển | Mức | Tác dụng |
|---|---|---|
| **−23 V** | mức "мeандр" âm | **MỞ khoá** |
| **+3,5 V** | mức dương | **ĐÓNG khoá** |

Hai mức trên là mô hình làm việc của tấm, cần xác nhận trên toàn dải Vin ±4 V. Điện áp đế thả nổi chưa biết nên không tính được dự trữ gate–đế từ swing 26,5 V. Giữ nguồn đúng trị số; không tự đổi đấu nối chân 11.

### Lưu ý về tốc độ

Datasheet ghi **t_вкл ≤0,3 µs và t_выкл ≤0,7 µs** ở điều kiện thử đế+5 V; đây là hai cận trên, không phải cặp thời gian đo của một con. Không lấy hiệu 0,4 µs làm overlap, không khẳng định ngắt luôn chậm hơn dẫn. Trên tấm thật còn U18 nối tầng, tải gate, trở kéo 10k và đế thả nổi. Đo М/М̄ cùng S/Vin để xác định chồng dẫn và dòng xung thực; chưa có chuẩn “vài chục ns”.

---

## 6. CÁCH SỬ DỤNG CỤ THỂ TRONG A313-V

### 6.1. Tấm A313-V.05 — Cụm chuyển mạch tín hiệu ra (BV.18, 57 vỏ)

Đây là **49 "bộ nhớ tương tự" (sample & hold)**, mỗi bộ gồm:
* **1 khoá 168КТ2Б** đóng/ngắt đường nạp
* **1 tụ 4,7 µF** giữ mức (C1…C49)
* **điện trở 330 kΩ** (R1…R56, R60, R61) trong mạch nạp/xả

Khoá được điều khiển bằng tổ hợp **K1…K4, T1…T4, t1…t4** (mức −23 V / +3,5 V, đưa sang từ A313-V.02) để chọn kênh cần nạp. Mức DC từ cụm biến đổi A313-V.04 được nạp vào tụ 4,7 µF rồi **giữ nguyên trong suốt chu kỳ 0,15 s** cho đến lần làm tươi tiếp theo.

> **Hệ quả cho việc dò lỗi tấm .05:**
> * Dòng rò khoá tăng ⇒ mức giữ trên tụ **trôi dần** giữa 2 lần làm tươi ⇒ tín hiệu ra "gợn"/lệch. Với C = 4,7 µF và I_ут = 100 nA, độ trôi ≈ 100 nA × 0,15 s / 4,7 µF ≈ **3,2 mV** — chỉ tính riêng dòng rò giả thiết; không kết luận khoá hỏng chỉ từ tổng độ trôi khi còn các đường tải khác.
> * R_си tăng ⇒ thời gian nạp tụ dài ra: τ = R_си × C = 100 Ω × 4,7 µF = **0,47 ms**. Nếu R_си tăng lên 10 kΩ thì τ = 47 ms < chu kỳ 0,15s; thời gian cửa sổ nạp mới quyết định nạp có kịp hay không, không phải chỉ chu kỳ làm tươi. Chưa tính các điện trở nối tiếp khác của tấm.05.
> * Khoá chập (luôn dẫn) ⇒ tụ bị "bám" theo đầu vào, mất chức năng nhớ ⇒ kênh đó lẫn tín hiệu của kênh khác (crosstalk).

### 6.2. Tấm A313-V.06 — Cụm khuếch đại tín hiệu ra (BV.22, 12 vỏ Б + 3 vỏ В)

* **12 vỏ 168КТ2Б (U1…U12) = 48 khoá = 3 khoá/kênh × 16 kênh:**
  * 1 khoá **shunt** (nối nút tổng xuống đất) — điều khiển bằng **М**
  * 1 khoá nối tiếp Vin→S và 1 khoá tải phụ Vin→R_bal→GND — cùng điều khiển bằng **М̄**
  ⇒ tạo bộ điều chế hệ số ±1 ở 400 Hz.
* **3 vỏ 168КТ2В (U16, U17, U18):**
  * **U16** — chọn hai ngưỡng **H14/H15 riêng biệt, đối dấu** gần ±0,351 V: H14=U16A.3/U16B.5; H15=U16C.10/U16D.12. A điều khiển B/C, B điều khiển A/D; hồi tiếp Schmitt qua U14
  * **U17** — dịch mức, tạo `xung400Hz` và cặp nút bù A/B
  * **U18** — dịch mức, tạo **М** và **М̄**

---

## 7. ✅ CHÂN 4 VÀ CHÂN 11 (ПОДЛОЖКА) — ĐÃ XÁC MINH: KHÔNG DÙNG

**Kết luận đã chốt (16/09/2026):** trên các tấm mạch của A313-V, **chân 4 và chân 11 của mọi vỏ 168КТ2 đều KHÔNG được nối** — đúng như sơ đồ nguyên lý thể hiện (chỉ vẽ 12/14 chân).

Chân 11 là **подложка (đế)**. Trên tấm này đế **để thả nổi**, chưa đủ tài liệu để kết luận cơ chế phân cực đế nội bộ.
*(Trong điều kiện đo của datasheet nhà sản xuất, đế được phân cực U_см.п = +5 V — đó là điều kiện bảo đảm tham số thử; không tự suy mọi tham số vẫn được bảo đảm với đế thả nổi, và không sửa ngược đấu nối thực tế đã chốt.)*

### Hệ quả thực tế

| Việc | Ảnh hưởng |
|---|---|
| **Thiết kế đồ gá kiểm tra** | **Không cần cấp nguồn phụ cho đế.** Tấm .06 chỉ cần 4 mức: +12,6 V, −12,6 V, −23 V, +3,5 V. (+5 V và +6,3 V trên DC11 cũng không dùng.) |
| **Dò lỗi** | Không đo, không kỳ vọng tín hiệu ở chân 4 và chân 11 |
| **Thư viện Altium** | Giữ ký hiệu 12 chân như hiện tại — **không cần bổ sung chân 4/11** |
| **Thay bằng linh kiện hiện đại** | ⚠ Đây là điểm cần chú ý: mạch thay thế **không có sẵn điện thế đế để tham chiếu** ⇒ module chuyển đổi phải **tự tạo phân cực đế/nguồn riêng** từ các ray sẵn có (±12,6 V / −23 V / +3,5 V) |
| **Hàn/tháo lắp** | Hai chân này không mang tín hiệu; không cần lo mối hàn nguội ở đó |

---

## 8. CÁCH KIỂM TRA LINH KIỆN

### 8.1. Kiểm tra trong mạch (in-circuit), có cấp nguồn

| Phép đo | Cách làm | Kết quả tốt | Kết quả xấu |
|---|---|---|---|
| **Trạng thái đóng** | Quan sát gate ở **+3,5 V** do mạch tạo; không ép nguồn ngoài chống driver, đo điện áp giữa исток và сток khi có tín hiệu vào | Tín hiệu **không truyền qua** | Truyền qua ⇒ khoá chập |
| **Trạng thái mở** | Quan sát gate ở **−23 V** do mạch tạo, đo sụt áp исток→сток với dòng đã biết | Tính R=sụt áp/dòng, so trace chuẩn; 100 Ω chưa bảo đảm ở đế thả nổi | Sụt lớn: kiểm dòng và chế độ điều khiển trước khi kết luận R_си tăng |
| **Điện trở kênh mở** | Đo dòng thực và sụt áp khi khoá dẫn; không bơm nguồn chống mạch đang lái |100 Ω chỉ đối chiếu khi điều kiện tương ứng datasheet | So tấm chuẩn và kiểm ngoài mạch nếu nghi |
| **Tốc độ** | Dao động ký, so sườn tín hiệu điều khiển và sườn tín hiệu qua kênh | t_вкл ≤ 0,3 µs; t_выкл ≤ 0,7 µs | Chậm hơn nhiều ⇒ thay |

### 8.2. Kiểm tra ngoài mạch (đã tháo)

Sơ đồ đo tối thiểu cho từng kênh:

```
   +5V ── (đế, chân 11)                ┌─ Đồng hồ đo (chế độ Ω hoặc V)
                                       │
   Nguồn DC −5V ──[50 kΩ]──● исток ───►│ khoá ├───► сток ──● 0 V (mát)
                                       │
   Затвор ◄── chuyển mạch: −15 V (mở) / +5 V (đóng)
```

| Trạng thái затвор | Điện trở исток–сток đo được |
|---|---|
| −15 V | **≤ 100 Ω** (tốt) |
| +5 V | **> 10 MΩ** (tốt) |

**Chú ý:** đo bằng đồng hồ vạn năng thông thường (không cấp đúng điện thế đế và затвор) sẽ cho kết quả vô nghĩa — phép diode-test đơn giản không xác minh đầy đủ chức năng MOS; vẫn có các tiếp giáp với đế và điện tích gate ảnh hưởng phép đo.

### 8.3. Biện pháp phòng tĩnh điện

168КТ2 là linh kiện MOS, chịu tĩnh điện đến **100 V theo ОСТ В 11 0998-99** — **rất thấp**.
Bắt buộc: vòng đeo tay chống tĩnh điện, mỏ hàn nối đất, chiếu hàn ≤ 3 s, khay dẫn điện.

---

## 9. TƯƠNG ĐƯƠNG / THAY THẾ

* Không có tương đương phương Tây trực tiếp. Về chức năng gần nhất: **DG201/DG211, ADG441, CD4066** (nhưng khác hoàn toàn về mức điều khiển và cần nguồn riêng).
* **Nếu tính phương án hiện đại hoá** (theo hướng thay FPGA/linh kiện đời cũ): mạch thay thế phải tái tạo được:
  1. Mức điều khiển −23 V / +3,5 V, hoặc thêm tầng dịch mức;
  2. R_си ≤ 100 Ω;
  3. Dòng rò ≤ 100 nA (bắt buộc cho tấm .05 — quyết định độ trôi của bộ nhớ tương tự);
  3b. **Tự tạo phân cực đế/nguồn riêng** — mạch gốc không đưa điện thế đế ra chân (§7);
  4. Chịu được tín hiệu tương tự ±4 V và điện áp chuyển mạch tới 26,5 V (vị trí В);
  5. t_вкл/t_выкл cùng cấp độ, kiểm chồng dẫn thực. Break-before-make nghĩa là ngắt nhánh cũ trước khi dẫn nhánh mới; không suy tính năng này chỉ từ hai cận thời gian datasheet.

Ứng viên: **ADG5412F / ADG5433** (nguồn ±15 V, R_on ~10 Ω, rò pA, có bảo vệ lỗi) kèm bộ dịch mức từ −23 V/+3,5 V về mức logic.

---

## 10. NGUỒN THAM KHẢO

* Datasheet 168КТ2 (nhà sản xuất, ТУ АЕЯР.431160.166ТУ) — https://eandc.ru/pdf/mikroskhema/168kt2.pdf
* Thẻ chủng loại 168КТ2, АО «Восход»-КРЛЗ — https://optochip.org/series/card/169988
* Bản vẽ 07MB.A313-V.BV.18 / .BV.21 (A313-V.05); .BV.22 / .BV.25 (A313-V.06)
