# 2Т312Б (КТ312Б)
# TRANSISTOR LƯỠNG CỰC n-p-n SILIC, CAO TẦN, CÔNG SUẤT NHỎ

**Phiên bản: Rev. C — 16/09/2026.** Đồng bộ phản biện A313-V.06; các giới hạn suy luận/đo thực được ghi riêng.

> Dùng trên **A313-V.06**: 16 con — Q1, Q3, Q5, Q7, Q9, Q11, Q13, Q15, Q17, Q19, Q21, Q23, Q25, Q27, Q29, Q31
> (nửa **trên** của tầng đệm bù lớp B, mỗi kênh 1 con).
> **Không có trên tấm A313-V.05.**

---

## 1. CÔNG DỤNG

Transistor silic **epitaxi-planar, cấu trúc n-p-n**, công suất nhỏ, tần số cao.
Dùng cho tầng khuếch đại và mạch xung.

* `2 Т 312` — phiên bản **quân sự / chấp nhận đặc biệt** (приёмка «5»), dải nhiệt độ rộng.
* `КТ 312` — phiên bản dân dụng cùng chip.

---

## 2. VỎ VÀ CÁCH ĐÁNH CHÂN

**Vỏ:** `КТЮ-3-1` — kim loại-thuỷ tinh, 3 chân cứng, thân trụ nhỏ có **vấu định vị (ключ)** trên viền đế.

⚠ **Cách đánh chân phải xác minh theo vấu định vị trên linh kiện thật và theo bản vẽ mạch in BV.23/BV.24, không tra theo trí nhớ** — họ КТ 312 có nhiều biến thể vỏ (kim loại KTЮ-3-1 cho 2 Т 312, nhựa КТ-13 cho КТ 312…М) với thứ tự chân **khác nhau**.

### Cách xác định nhanh, chắc chắn (dùng đồng hồ chế độ đo diode)

Với transistor **n-p-n**:

| Que đo | Kết quả |
|---|---|
| Que **đỏ (+)** ở **base**, que đen lần lượt ở 2 chân còn lại | Cả hai đều dẫn (0,5…0,8 V) ⇒ chân đó là **base** |
| Đảo que | Không dẫn |
| Trong hai chân còn lại: chân cho sụt áp **lớn hơn** một chút khi đo với base | Thường là **emitter** (U_бэ > U_бк) |

Kiểm chứng lại bằng vị trí trên mạch: **collector của Q(NPN) nối +12,6 V**, **emitter nối nút ra chung với transistor PNP**.

---

## 3. THAM SỐ GIỚI HẠN

| Tham số | Ký hiệu | Giá trị |
|---|---|---|
| Điện áp collector–base | U_кб max | **35 V** |
| Điện áp collector–emitter | U_кэ max | **30 V** (một số nguồn ghi 35 V cho КТ312Б) |
| **Dòng collector liên tục** | I_к max | **30 mA** |
| Dòng collector xung | I_к и | **60 mA** |
| **Công suất tiêu tán** | P_к max | **225 mW** (ở 25 °C) |
| Công suất ở +125 °C | P_к | **62,5 mW** |
| Dải nhiệt độ | — | **−60 … +125 °C** |

---

## 4. THAM SỐ ĐIỆN

| Tham số | Ký hiệu | Giá trị |
|---|---|---|
| **Hệ số khuếch đại dòng** | h21э | **25 … 100** |
| **Tần số cắt** | f_гр | **≥ 120 MHz** |
| Dòng ngược collector | I_кбо | ≤ 10 µA |

---

## 5. VAI TRÒ TRONG A313-V.06

Mỗi kênh có một cặp bù **Q(NPN 2Т312Б) + Q(PNP 2Т203Б)** mắc **lặp emitter lớp B**, đặt **bên trong vòng hồi tiếp** của khuếch đại 140УД1Б:

```
                    +12,6 V
                       │
                       C
   chân 5 (140УД1Б) ──B   Q(NPN) 2Т312Б      ← dẫn khi cấp dòng ra tải
                       E
                       ├──── nút ra ──[180 Ω]──► Вых.n==
                       E
   chân 5 (140УД1Б) ──B   Q(PNP) 2Т203Б      ← dẫn khi hút dòng từ tải
                       C
                       │
                    −12,6 V
```

* **2Т312Б dẫn khi cấp dòng từ+12,6 V ra tải**. Với tải thuần trở thường là nửa điện áp dương; tảiСКТ phản kháng có thể lệch dấu dòng/áp.
* 140УД1Б chỉ ra được vài mA; tầng đệm này mới là tầng cấp dòng cho cuộn sơ cấp biến thế sin-cos.
* Vì nằm trong vòng hồi tiếp, méo xuyên tâm (crossover) được bù ⇒ khi **một trong hai transistor hỏng hở** thường lộ rõ; méo cũng có thể do thiếuheadroom, tải hay mất ổn định: sóng ra bị "gãy/cụt" đúng một nửa chu kỳ.

### Chế độ làm việc thực tế (ước tính)

| Đại lượng | Giá trị |
|---|---|
| U_кэ khi dẫn (biên độ ra +4 V) | Ở tải 1 kΩ, Vo 4 V: I_R39≈4 mA(P1) hoặc 4,4 mA(P2); Y≈4,72…4,792 V, |VCE|≈7,88…7,808 V; chưa tính động |
| Dòng emitter với tải 1 kΩ | ≈4…4,4 mA khi tính cả Rfb, chưa tínhCfb/tải phản kháng |
| Công suất tiêu tán tức thời | ≈31,5…34,4 mW xác lập với các giả thiết trên; tính IC≈IE là xấp xỉ |
| **Khi ngắn mạch đầu ra** | Mô hình base sát rail cho 66,11 mA, chưa phải dòng thực. P_Q=|VCE|·IC: tạiY≈11,9 V thì VCE≈0,7 V, không phải 12 V; đường tảiR 180 có cực đại xấp xỉ 12,6²/(4×180)=220,5 mW nếuIC≈IE. Vẫn có thể quá dòng/nhiệt; không thử chập |

---

## 6. CÁCH KIỂM TRA

### 6.1. Trong mạch, KHÔNG cấp nguồn (đồng hồ chế độ diode)

| Phép đo | Kết quả tốt | Bất thường |
|---|---|---|
| Base → Emitter (đỏ ở B) | 0,5 … 0,8 V | 0 V ⇒ chập; hở mạch ⇒ đứt |
| Base → Collector (đỏ ở B) | 0,5 … 0,8 V | 0 V ⇒ chập; hở ⇒ đứt |
| Đảo chiều cả hai | Không dẫn | Dẫn ⇒ chập |
| Collector ↔ Emitter (2 chiều) | Không dẫn | Dẫn ⇒ chập C-E (lỗi phổ biến nhất) |

> Lưu ý: chân base nối trực tiếp chân 5 của 140УД1Б, chân C nối +12,6 V qua đường mạch — đồng hồ có thể "nhìn thấy" các đường song song. Nếu nghi ngờ, nhấc một chân hoặc tháo hẳn.

### 6.2. Trong mạch, CÓ cấp nguồn (dao động ký)

| Điểm đo | Dạng sóng tốt | Triệu chứng lỗi |
|---|---|---|
| Base (= chân 5 OA) | V5≈Y±VBE theo Q đang dẫn; Y=Vo+180I_R39, không chỉ ±4 V | Bão hoà ±12 V ⇒ hồi tiếp hở |
| Emitter (nút ra) | Theo Vo+180I_R39; chuyển tiếp gồm đường truyền trực tiếp và phần RC | Hụt chiều dòng dương với tải thuần trở: nghi 2Т312Б, đo phân biệt với mất nguồn/tải |
| Collector | +12,6 V DC phẳng | Sụt/nhấp nhô ⇒ dòng bất thường, nghi chập |

### 6.3. Ngoài mạch — đo h21э

Dùng máy đo h_FE hoặc mạch đơn giản: I_б = 100 µA, U_кэ = 5 V, đo I_к.
`h21э = I_к / I_б` phải nằm trong **25 … 100**.
Ngoài dải ⇒ loại. Nếu đã lắp cặp mới, **nên chọn cặp có h21э gần nhau giữa các kênh** để 16 kênh đồng đều.

---

## 7. TƯƠNG ĐƯƠNG

**Tương đương nước ngoài (theo sổ tay):** 2N729, 2N780, BCY42, 2SC105, 2SC33.

**Nếu phải thay bằng linh kiện hiện đại:** chọn NPN vỏ TO-92 hoặc TO-18 với:
* U_кэо ≥ 40 V, I_к ≥ 100 mA, P ≥ 350 mW, f_т ≥ 100 MHz, h_FE 40…120
* Ứng viên: **2N2222A, BC337-25, 2N3904 (nếu dòng nhỏ), KSP2222A**
* ⚠ Thay đúng linh kiện đã xác định hỏng; thay cả cặp/đổi chủng loại cần kiểm ổn định, dòng lái và pinout. βkhác không tự gây mất đối xứng khi hồi tiếp còn bù được.
* ⚠ Kiểm tra lại cách đánh chân — TO-92 hiện đại thường là E-B-C hoặc C-B-E, **khác** КТЮ-3-1.

---

## 8. NGUỒN THAM KHẢO

* 2Т312А/Б/В, КТ312А/Б/В — datasheet: https://eandc.ru/pdf/tranzistor/2t312_kt312.pdf
* Транзистор КТ312Б — RadioLibrary: https://www.radiolibrary.ru/reference/transistor/kt312b.html
* 2Т312Б — thông số và vỏ КТЮ-3-1: https://www.chipdip.ru/product/2t312b
* 2Т312Б — ParaTran: https://www.paratran.com/2paratranKR.php?tr=1195
