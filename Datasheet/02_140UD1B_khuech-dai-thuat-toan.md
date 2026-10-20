# 140УД1Б (К140УД1Б)
# KHUẾCH ĐẠI THUẬT TOÁN

**Phiên bản: Rev. C — 16/09/2026.** Đồng bộ phản biện A313-V.06; các giới hạn suy luận/đo thực được ghi riêng.

> Dùng trên **A313-V.06**: 18 con (U14, U15 làm bộ so sánh; U19…U34 làm khuếch đại 16 kênh).
> **Không có trên tấm A313-V.05.**

---

## 1. CÔNG DỤNG VÀ ĐẶC ĐIỂM HỌ

К140УД1 là thế hệ khuếch đại thuật toán đầu tiên của Liên Xô (tương tự về kiến trúc với µA702 của Fairchild). Đặc điểm khác biệt so với OA hiện đại:

1. **Có chân "общий" (chân 4) — phải nối mát.** Đây là điểm quan trọng nhất; OA hiện đại (741, LM358…) không có chân này.
2. **Nguồn danh định ±12,6 V** (loại Б). Loại А dùng ±6,3 V, loại В dùng ±12,6 V với hệ số khuếch đại cao hơn.
3. **Hệ số khuếch đại hở mạch thấp** (sổ tay cũ 1350…12000; PDF БВК 2000…10500) so với OA hiện đại (10⁵…10⁶).
4. **Dòng vào lớn** (tới 9 µA) — bắt buộc phải cân bằng trở kháng hai đầu vào.
5. **Cần mạch hiệu chỉnh tần số (коррекция) bên ngoài** gắn vào chân контрольный.

---

## 2. VỎ VÀ CÁCH ĐÁNH CHÂN

**Vỏ:** `301.12-1` — vỏ kim loại tròn, 12 chân, có vấu định vị (ключ).
Trên mạch in A313-V.06 các con này nhìn thấy rõ: **18 vòng tròn kim loại** rải đều trên tấm.

### Назначение выводов

| Chân | Chức năng (tiếng Nga) | Diễn giải | Dùng trên A313-V.06 |
|---|---|---|---|
| **1** | Питание −U_п | **Nguồn âm −12,6 V** | ✔ nối −12,6 V |
| 2 | Контрольный | chân kiểm tra / hiệu chỉnh | ✖ để trống |
| 3 | Контрольный | chân kiểm tra / hiệu chỉnh | ✖ để trống |
| **4** | **Общий** | **Mát (GND)** | ✔ nối mát (net "a") |
| **5** | Выход | **Đầu ra** | ✔ |
| 6 | — | | ✖ để trống |
| **7** | Питание +U_п | **Nguồn dương +12,6 V** | ✔ nối +12,6 V |
| 8 | — | | ✖ để trống |
| **9** | Вход инвертирующий | **Đầu vào đảo (−)** | ✔ |
| **10** | Вход неинвертирующий | **Đầu vào không đảo (+)** | ✔ |
| 11 | — | | ✖ để trống |
| **12** | Контрольный | chân hiệu chỉnh tần số | ✔ nối R 56 Ω + C 0,01 µF xuống mát |

> ⚠ **Dễ nhầm nhất:** chân 4 là **MÁT**, không phải chân bỏ trống. Nếu khi sửa chữa vô ý cắt/hở chân 4, mạch sẽ chạy sai hoàn toàn mà bề ngoài vẫn "có điện".

---

## 3. THAM SỐ ĐIỆN — KHÔNG TRỘN BIẾN THỂ

**Nguồn gốc ưu tiên:** `140ud1B.pdf` tr. 1–2 là nhãn ЛСАР.431130.011 ЭТ của **140УД1БВК/140УД101БВК**, theo АЕЯР.431130.171-01 ТУ. Chưa xác định đồng nhất với lô 140УД1Б trên tấm; thông số sổ tay cũ chỉ dùng làm giả thiết bảo thủ có ghi rõ.

| Đại lượng | PDF 140УД1БВК tr. 2 | Giá trị sổ tay Rev. B / phạm vi áp dụng |
|---|---|---|
| Nguồn danh định | ±12,6 V; RL=5,05 kΩ | Phù hợp ray tấm |
| Swing ra | +8 V/−6,3 V tại UI=±100 mV | Không suy đối xứng; không suy lên sát rail |
| Vos | −7…+7 mV | Phù hợp giả thiết ±7 mV |
| Ib | −8…+8 µA | Rev. B dùng 9 µA; cần đúng biến thể |
| ΔIb | −1,5…+1,5 µA | Rev. B dùng 2,5 µA; cần đúng biến thể |
| Icc | −12…+12 mA tại Uo=0, nguồn ±13,9 V | Rev. B dùng 10 mA;18 IC có thể 216 mA theo điều kiện PDF, chưa có dòng tầng Q/tải |
| A | 2000…10500 | Rev. B dùng 1350…12000 |
| Common-mode, unity bandwidth, slew, CMRR | Không được nêu trong PDF nhãn này | Các số ±6 V,0,1 MHz,3,5 V/µs,60dB của Rev. B chưa được xác minh ở đúng biến thể; không dùng để chứng nhận ATE |

Với noise gain ≈2, riêng Vos có thể tạo ≈14 mV đầu ra. ΔIb phải nhân trở hồi tiếp khi quy đầu ra: giả thiết 2,5 µA×10 kΩ=25 mV, không phải 12,5 mV đầu ra. Phần gain hữu hạn xấp xỉ 2/A chỉ đúng khi tầng đệm/vòng còn tuyến tính và không quá tải.

---

## 4. MẠCH HIỆU CHỈNH TẦN SỐ (КОРРЕКЦИЯ)

Trên A313-V.06 mỗi con 140УД1Б đều có mạng **R 56 Ω nối tiếp C 0,01 µF từ chân 12 xuống mát**:

```
    chân 12 ──[ 56 Ω ]──┤├── mát
                      0,01 µF
```

* Hằng số thời gian τ = 56 Ω × 0,01 µF = **0,56 µs** ⇒ 1/(2 π RC)≈284 kHz là tần số |Xc|=R của nhánh ngoài, không phải cực vòng kín đã được xác minh.
* Mục đích: **chống tự kích** khi vòng hồi tiếp có thêm tầng đệm transistor (làm tăng độ trễ pha).
* **Nếu R 56 Ω hoặc C hở có thể mất bù, gây tự kích**, nhìn trên dao động ký thấy sóng hình sin tần số cao chồng lên tín hiệu 400 Hz. Đây là triệu chứng đặc trưng.
* **Nếu C chập, chân 12 nối mát qua 56 Ω**; hậu quả định lượng phải kiểm theo mạch nội/đo, không mặc định mất tín hiệu.

Danh mục trên A313-V.06 (18 mạng): R27+C3 (U14), R31+C4 (U15), R38+C2 (U19), R41+C6 (U20), R44+C8 (U21), R47+C10 (U22), R50+C12 (U23), R53+C14 (U24), R56+C16 (U25), R59+C18 (U26), R62+C20 (U27), R65+C22 (U28), R68+C24 (U29), R71+C26 (U30), R74+C28 (U31), R77+C30 (U32), R80+C32 (U33), R83+C34 (U34).

---

## 5. CÁCH SỬ DỤNG CỤ THỂ TRONG A313-V.06

### 5.1. U19…U34 — khuếch đại của 16 kênh điều chế

Mắc theo sơ đồ **khuếch đại đổi hệ số ±1** (xem tài liệu phân tích A313-V.06):

| Chân | Nối tới |
|---|---|
| 9 (−) | Điểm nối R_in 10 kΩ (từ tín hiệu vào) và R_fb 10 kΩ (hồi tiếp), có C 0,01 µF song song R_fb |
| 10 (+) | Qua R 4,7 kΩ tới nút tổng của các khoá 168КТ2 |
| 5 (ra) | **Base chung của cặp transistor 2Т312Б / 2Т203Б** (tầng đệm nằm trong vòng hồi tiếp) |
| 12 | R 56 Ω + C 0,01 µF xuống mát |
| 1 / 7 | −12,6 V / +12,6 V |
| 4 | Mát |

**Vì sao R 4,7 kΩ ở chân 10:** Rin∥Rfb=5 kΩ, nên 4,7k cộng Ron bù gần đúng trở nguồn vào đảo. Với `k=Rfb/Rin`, offset đầu ra:

`E≈(1+k)Vos+Rfb·Ib−−(1+k)(4,7k+Ron)·Ib+`.

Nếu thay Rbias bằng dây 0 Ω và bỏ qua Ron, riêng Ib−9 µA gây **90 mV đầu ra** (45 mV quy đầu vào). Ở trị số danh định, cùng Ib 9 µA gây bất cân bằng ≈5,4 mV; chênh dòng 2,5 µA còn có thể tạo thêm tới 25 mV theo cận bảo thủ. Không thể kết luận sai số còn 0,75 mV hay giảm 60 lần. Rbias đứt hở là lỗi khác, làm mất đường DC tới chân 10.

Ngân sách góc dung sai 1% của Rin/Rfb,5% của Rbias, Ron 0…100 Ω và thông số giả thiết cũ 9 µA/2,5 µA cho cận các hạng offset ≈49,8 mV, chưa tính mọi sai số. Với thông số PDF БВК, tính riêng bằng 8 µA/1,5 µA. Xem §10.4 tài liệu phân tích Rev. C.

### 5.2. U14 Schmitt và U15 với ngưỡng đối dấu

Không có hồi tiếp âm tuyến tính: U14 có hồi tiếp dương qua U17/U16. U14.10=H14 và U15.10=H15 **không nối chung**, hai ngưỡng đối dấu gần ±0,351 V do U16 chọn. U15 không có vòng Schmitt độc lập. M sớm hơn xung400Hz ≈357,8 µs(5 Vrms) hoặc 528,1 µs(5 V đỉnh) trong mô hình danh định; xem §5.2 tài liệu phân tích Rev. C.
Dùng A theo đúng biến thể (§3) ⇒ với chênh lệch đầu vào chỉ vài chục mV thì đầu ra đã bão hoà ⇒ tạo xung vuông.

---

## 6. ⚠ CẢNH BÁO KHI KIỂM TRA

| Rủi ro | Giới hạn | Hậu quả nếu vượt |
|---|---|---|
| **Điện áp vào đồng pha** | Giới hạn đúng biến thể cần tra thêm | Giữ phép thử kênh trong ±4 V theo dải làm việc. ±6 V sổ tay chưa được xác minh, không xem đó là ngưỡng hỏng hoặc được phép thử. |
| Thứ tự cấp nguồn | — | Không cấp nguồn một ray trong khi ray kia có điện. Nguồn đồ gá phải bật/tắt đồng thời ±12,6 V. |
| Đảo cực nguồn | — | Tấm **không có diode bảo vệ** ⇒ cấp nhầm cực tính phá hỏng đồng loạt 18 con. |
| Ngắn mạch đầu ra | U_вых max ≥ 6 V nhưng dòng ra nhỏ | Chân 5 chỉ ra được vài mA; tầng đệm transistor mới là tầng cấp dòng. |

---

## 7. CÁCH KIỂM TRA LINH KIỆN

### 7.1. Trong mạch (nhanh, không tháo)

| # | Phép đo | Giá trị tốt | Bất thường ⇒ |
|---|---|---|---|
| 1 | Điện áp chân 1 / chân 7 | −12,6 V / +12,6 V (±5 %) | mất nguồn cục bộ: đứt mạch in, chân hàn nguội |
| 2 | Điện áp chân 4 so với mát | **0 V** | ≠ 0 ⇒ hở chân mát → mạch chạy sai |
| 3 | Chênh lệch chân 9 và chân 10 | **≤ vài chục mV** | lớn ⇒ vòng hồi tiếp hở (R_fb đứt) hoặc OA chết |
| 4 | Chân 5 khi Vin=0 V | So trace chuẩn; base có thể lệch theo chiều dòng Q dù Vo gần 0 | Nếu bão hòa: kiểm OA, nguồn, hồi tiếp và tải |
| 5 | Nhiệt độ vỏ | ấm nhẹ | nóng rõ rệt ⇒ chập nội bộ |
| 6 | Dạng sóng chân 12 | Chưa có mô hình biên độ/dạng; ghi trace chuẩn bằng đầu đo điện dung thấp | Tự kích có nhiều nguyên nhân, kiểm mạng коррекция và vòng/tải |

### 7.2. Ngoài mạch — sơ đồ thử đơn giản

Mắc mạch lặp (повторитель) và mạch đảo, cấp ±12,6 V, chân 4 nối mát:

```
Mạch thử 1 — khuếch đại đảo hệ số −1:
   Vin ──[10k]──┬── chân 9
                └──[10k]──┐
   mát ──[4,7k]─── chân 10 │
                 chân 5 ───┘  → đo Vout
   chân 12 ──[56Ω]──┤├── mát   (0,01 µF)
```

| Vin | Vout danh định (chưa có cửa sổ nghiệm thu) |
|---|---|
| 0 V | Gần 0; đo offset, so ngân sách §5.1 |
| +4,000 V | Gần−4 V; tỉ số hai điện trở 1% có thể lệch ≈2,02% trước khi cộng offset |
| −4,000 V | Gần+4 V; đo hai cực tính để tách gain/offset |
| +1,000 V | Gần−1 V; so tuyến tính sau khi trừ offset |

Đo thêm: **dòng từng ray ở điều kiện xác định**; dùng giới hạn đúng biến thể (§3), không tự đặt 10/15 mA làm chuẩn loại mọi 140УД1Б.

### 7.3. Tháo lắp

Vỏ kim loại tròn 12 chân, chân xuyên lỗ. Khi tháo phải hút thiếc từng chân, **không giật** — dễ bong pad/via trên mạch in 2 mm 2 lớp này. Ưu tiên dùng máy hút thiếc chân không.

---

## 8. TƯƠNG ĐƯƠNG / THAY THẾ

* **Trong nước Nga:** К140УД1Б, КР140УД1Б (vỏ nhựa DIP, cách đánh chân **khác**), 140УД1Б-1.
* **Không thể thay trực tiếp bằng OA hiện đại** vì:
  1. Chân 4 "общий" không có ở OA hiện đại;
  2. Cách đánh chân và vỏ hoàn toàn khác;
  3. Mạch коррекция chân 12 không còn ý nghĩa.
* **Nếu buộc phải hiện đại hoá:** làm một mạch chuyển đổi (adapter) nhỏ mang OA hiện đại (OP07, OPA192, LT1097 — offset thấp, băng thông đủ) với 12 chân cắm tương thích vỏ 301.12-1, nối:
  * chân 1 → V−, chân 7 → V+, chân 9 → IN−, chân 10 → IN+, chân 5 → OUT
  * chân 4 → không nối (hoặc nối mát của adapter)
  * chân 12 → để hở (bỏ mạch коррекция, vì OA hiện đại bù nội bộ) — nhưng **phải kiểm tra lại độ ổn định** do tầng đệm transistor vẫn nằm trong vòng hồi tiếp.
  * Ưu điểm kèm theo: U_см giảm từ 7 mV xuống < 50 µV, I_вх giảm từ 9 µA xuống pA ⇒ **có thể bỏ luôn R 4,7 kΩ cân bằng**, độ chính xác kênh tăng rõ rệt.

---

## 9. NGUỒN THAM KHẢO

* К140УД1 (А, Б, В), КР140УД1 — DataSheet: https://rudatasheet.ru/microchips/k140ud1_kr140ud1/
* Параметры интегральных микросхем К140УД1А-К140УД1В: http://www.chipinfo.ru/dsheets/ic/140/ud1.html
* К140УД1Б, схема включения — справочник: http://www.texnic.ru/data/ims1554/ims197.html
* Bản vẽ 07MB.A313-V.BV.22 / .BV.25
