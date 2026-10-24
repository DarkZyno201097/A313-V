# 2Т203Б (КТ203Б)
# TRANSISTOR LƯỠNG CỰC p-n-p SILIC, CÔNG SUẤT NHỎ

**Phiên bản: Rev. C — 16/09/2026.** Đồng bộ phản biện A313-V.06; các giới hạn suy luận/đo thực được ghi riêng.

> Dùng trên **A313-V.06**: 16 con — Q2, Q4, Q6, Q8, Q10, Q12, Q14, Q16, Q18, Q20, Q22, Q24, Q26, Q28, Q30, Q32
> (nửa **dưới** của tầng đệm bù lớp B, mỗi kênh 1 con).
> **Không có trên tấm A313-V.05.**

---

## 1. CÔNG DỤNG

**«Транзисторы кремниевые эпитаксиально-планарные p-n-p. Предназначены для применения в усилителях и импульсных устройствах.»**

Transistor silic epitaxi-planar, cấu trúc **p-n-p**, công suất nhỏ, dùng cho tầng khuếch đại và mạch xung.

* `2 Т 203` — phiên bản quân sự; `КТ 203` — phiên bản dân dụng.
* Nhóm Б là nhóm trung bình về điện áp (30 V).

---

## 2. VỎ VÀ CÁCH ĐÁNH CHÂN

**Vỏ:** kim loại-thuỷ tinh (металлостеклянный), 3 chân mềm (выводы гибкие), thân trụ nhỏ.

⚠ Giống 2Т312Б: **phải xác minh chân theo linh kiện thật + bản vẽ mạch in BV.23/BV.24.**

### Cách xác định nhanh (đồng hồ chế độ đo diode)

Với transistor **p-n-p** (ngược với NPN):

| Que đo | Kết quả |
|---|---|
| Que **đen (−)** ở **base**, que đỏ lần lượt ở 2 chân còn lại | Cả hai đều dẫn (0,5…0,8 V) ⇒ chân đó là **base** |
| Đảo que | Không dẫn |

Kiểm chứng theo mạch: **collector của Q(PNP) nối −12,6 V**, **emitter nối nút ra chung với transistor NPN**.

---

## 3. THAM SỐ GIỚI HẠN (2Т203Б)

| Tham số | Ký hiệu | Giá trị | Điều kiện |
|---|---|---|---|
| Điện áp collector–emitter | U_кэ max | **30 V** | T = −60…+75 °C |
| Điện áp collector–base | U_кб max | **30 V** | T = −60…+75 °C |
| **Dòng collector liên tục** | I_к max | **10 mA** | ⚠ **rất nhỏ** |
| Dòng collector xung | I_к и | **50 mA** | t_и ≤ 10 µs |
| **Công suất tiêu tán** | P_к max | **150 mW** | T = −60…+75 °C |
| Nhiệt độ tiếp giáp | T_п | +150 °C |
| Dải nhiệt độ môi trường | — | **−60 … +125 °C** |

---

## 4. THAM SỐ ĐIỆN

| Tham số | Ký hiệu | Giá trị | Điều kiện |
|---|---|---|---|
| **Hệ số khuếch đại dòng** | h21э | **30 … 90** | T = +25 °C, U_кб = 5 V |
| **Tần số cắt** | f_гр | **5 MHz** | ⚠ thấp |
| Dòng ngược collector | I_кбо | ≤ 1 µA | T = +25 °C |
| Điện dung collector | C_к | 10 pF | U_кб = 5 V, f = 10 MHz |
| Điện áp bão hoà | U_кэ нас | 1 V | I_к = 20 mA, I_б = 4 mA |

> *(Nguồn khác ghi h21э = 30…150 cho КТ203Б dân dụng; với 2Т203Б quân sự lấy theo 30…90.)*

---

## 5. ⚠ LINH KIỆN GIỚI HẠN KHẢ NĂNG CỦA TOÀN TẤM A313-V.06

Đây là **linh kiện "yếu" nhất trong tầng ra** và quyết định giới hạn tải của cả 16 kênh:

| So sánh | 2Т312Б (NPN) | **2Т203Б (PNP)** |
|---|---|---|
| I_к max liên tục | 30 mA | **10 mA** |
| P_к max | 225 mW | **150 mW** |
| f_гр | 120 MHz | **5 MHz** |

### Hệ quả bắt buộc phải tuân thủ khi kiểm tra

| # | Quy tắc | Lý do |
|---|---|---|
| 1 | **Không coi 400 Ω là tải được bảo đảm; khởi đầu ≥1 kΩ thuần trở** | 400 Ω lấy 10 mA ngoài, còn tới 0,4 mA hồi tiếp. Cận tổngIE10 mA cho ≈417 Ω nhưng còn headroom,β,nhiệt vàquá độ; xem §10.6 tài liệu chính |
| 2 | **Không được chập đầu ra xuống mát** khi tấm đang làm việc | 66,11 mA là mô hình base sát rail, không phải dòngđo thực; có nguy cơ vượt giới hạn, R 180 Ω không phải bảo vệ ngắn mạch |
| 3 | Que đo dao động ký phải kẹp chắc, tránh trượt sang chân bên cạnh | Tránh gây ngắn mạch quá dòng; mức hư hại phụ thuộc chế độ/thời gian, không có cận an toàn đã xác nhận |
| 4 | Khi đo đồng thời nhiều kênh, kiểm tra tổng dòng ray −12,6 V | Mỗi kênh có thể lấy tới 10 mA từ ray âm |

### Giới hạn suy luận từ f_гр

f_гр của PNP thấp hơn NPN là tham số linh kiện. **Không đủ** suy sườn âm chắc chắn chậm hơn hay coi sườn méo là “bình thường”: OA, hồi tiếp RC, tải phản kháng và chiều dòng cùng quyết định. So trace tấm chuẩn ở đúng tải; kiểm ổn định khi thay chủng loại.

---

## 6. VAI TRÒ TRONG A313-V.06

```
                    +12,6 V
                       │
   chân 5 (140УД1Б) ──B  Q(NPN) 2Т312Б
                       E
                       ├──── nút ra ──[180 Ω]──► Вых.n==
                       E
   chân 5 (140УД1Б) ──B  Q(PNP) 2Т203Б   ← dẫn khi hút dòng từ tải
                       C
                       │
                    −12,6 V
```

* **2Т203Б hút dòng từ tải về−12,6 V**. Với tải thuần trở thường ở nửa điện áp âm; tải phản kháng phải xét chiều dòng.
* Nằm trong vòng hồi tiếp của 140УД1Б ⇒ méo xuyên tâm được bù.

### Chế độ làm việc thực tế (ước tính, tải 1 kΩ)

| Đại lượng | Giá trị |
|---|---|
| U_кэ khi dẫn (biên độ ra −4 V) | Tính cả R 180 Ω: |Y|≈4,72…4,792 V, |VCE|≈7,88…7,808 V cho tải 1 kΩ, hai pha P1/P2 |
| Dòng emitter | ≈4…4,4 mA kể dòng Rfb, chưa gồm quá độ/tảiC |
| Công suất tiêu tán | ≈31,5…34,4 mW xác lập, IC≈IE; còn phải xét nhiệt độ |

---

## 7. CÁCH KIỂM TRA

### 7.1. Trong mạch, KHÔNG cấp nguồn (đồng hồ chế độ diode)

| Phép đo (p-n-p: que Đ EN ở base) | Kết quả tốt | Bất thường |
|---|---|---|
| Base → Emitter | 0,5 … 0,8 V | 0 V ⇒ chập; hở ⇒ đứt |
| Base → Collector | 0,5 … 0,8 V | 0 V ⇒ chập; hở ⇒ đứt |
| Đảo chiều cả hai | Không dẫn | Dẫn ⇒ chập |
| Collector ↔ Emitter (2 chiều) | Không dẫn | Dẫn ⇒ **chập C-E — lỗi phổ biến nhất sau khi bị quá dòng** |

### 7.2. Trong mạch, CÓ cấp nguồn (dao động ký)

| Điểm đo | Dạng sóng tốt | Triệu chứng lỗi |
|---|---|---|
| Emitter (nút ra) | Y=Vo+180I_R39; so trace ở tải xác định | Hụt chiều dòng âm với tải thuần trở: nghi PNP, kiểm nguồn/tải để phân biệt |
| | | Bão hoà −12 V cố định ⇒ chập C-E |
| Collector | −12,6 V DC phẳng | Nhấp nhô ⇒ dòng bất thường |

**Gợi ý với tải thuần trở, không phải kết luận duy nhất:**
mất phần **dương** ⇒ lỗi NPN (2Т312Б); mất phần **âm** ⇒ lỗi PNP (2Т203Б).

### 7.3. Ngoài mạch — đo h21э

I_б = 100 µA, U_кэ = −5 V ⇒ `h21э = I_к / I_б` phải nằm trong **30 … 90**.
Khi thay, nên **ghép cặp NPN/PNP có h21э gần nhau** và giữ đồng đều giữa 16 kênh.

---

## 8. TƯƠNG ĐƯƠNG

* Cùng họ: КТ203А/Б/В, КТ203АМ/БМ/ВМ, 2Т203А/Б/В/Г/Д (khác nhau ở U_кэ và h21э).
* **Thay bằng linh kiện hiện đại:** chọn PNP có
  * U_кэо ≥ 40 V, I_к ≥ 100 mA, P ≥ 350 mW, f_т ≥ 100 MHz, h_FE 40…120
  * Ứng viên: **2N2907A, BC327-25, 2N3906, KSA733**
  * ⚠ Không bắt buộc thay cả cặp chỉ vìmột Q hỏng; nếu đổi chủng loại phải kiểm cả vòng, pinout, headroom và dòng base.
  * ⚠ Nếu thay bằng linh kiện có f_т cao hơn nhiều, **phải kiểm tra lại độ ổn định của vòng hồi tiếp** (mạng коррекция R 56 Ω + C 0,01 µF trên chân 12 của 140УД1Б được tính cho linh kiện cũ) — có nguy cơ tự kích.
  * Dòngđịnh mứcQmới cao hơn không tự chứng minh khả năng tải/chịu ngắn mạch của toàn mạch: OA, R 180 Ω, nhiệt và SOA vẫn giới hạn.

---

## 9. NGUỒN THAM KHẢO

* КТ203А/Б/В, 2Т203А…Д — bảng tham số đầy đủ: https://www.electronicsblog.ru/spravochnik-radioelektronnyx-komponentov/bipolyarnye-tranzistory/kt203a-kt203b-kt203v-kt203am-kt203bm-kt203vm-2t203a-2t203b-2t203v-2t203g-2t203d
* Транзистор КТ203Б — RadioLibrary: https://www.radiolibrary.ru/reference/transistor/kt203b.html
* КТ203 / 2Т203 — справочник: https://www.5v.ru/ds/trnz/kt203.htm
