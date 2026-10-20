# TỔNG QUAN LINH KIỆN CHÍNH — KHỐI A313-V

**Phiên bản: Rev. C — 16/09/2026.** Đồng bộ phản biện A313-V.06; các giới hạn suy luận/đo thực được ghi riêng.

Tài liệu tra cứu nhanh cho 5 chủng loại linh kiện tích cực chính dùng trên các tấm mạch của máy tính dẫn đường A313-V.
Chi tiết từng loại xem các file kèm theo trong thư mục này.

---

## 1. BẢNG TRA NHANH

| Ký hiệu | Chủng loại | Vỏ / số chân | Dùng ở tấm nào | Số lượng |
|---|---|---|---|---|
| **168КТ2Б** | Khoá tương tự MOS 4 kênh | 401.14-5, 14 chân | **A313-V.05** (chuyển mạch tín hiệu ra)<br>A313-V.06 (khuếch đại tín hiệu ra) | **57 vỏ** (.05)<br>12 vỏ (.06) |
| **168КТ2В** | Khoá tương tự MOS 4 kênh, chịu áp cao hơn | 401.14-5, 14 chân | A313-V.06 (cụm tạo xung điều chế) | 3 vỏ (U16, U17, U18) |
| **140УД1Б** | Khuếch đại thuật toán | 301.12-1, vỏ kim loại tròn 12 chân | A313-V.06 | 18 |
| **2Т312Б** | Transistor **n-p-n** Si cao tần | КТЮ-3-1, kim loại-thuỷ tinh 3 chân | A313-V.06 (nửa trên tầng đệm) | 16 |
| **2Т203Б** | Transistor **p-n-p** Si | Kim loại-thuỷ tinh 3 chân | A313-V.06 (nửa dưới tầng đệm) | 16 |

> **Lưu ý cho tấm A313-V.05:** tấm này **chỉ có duy nhất một chủng loại linh kiện tích cực là 168КТ2Б** (57 vỏ = 228 khoá tương tự), cộng với 58 × 330 kΩ, 49 × 4,7 µF, 3 × 0,068 µF, 1 × 0,01 µF, 3 điện trở lẻ (R57 3,3 kΩ; R58 1,2 kΩ; R59 1,8 kΩ) và 2 đầu nối DC96C (DC9, DC10).
> ⇒ **File `01_168KT2B_168KT2V_...` là tài liệu quan trọng nhất cho tấm .05.**

---

## 2. SO SÁNH NHANH 2 TRANSISTOR TẦNG ĐỆM (A313-V.06)

| Tham số | 2Т312Б (NPN) | 2Т203Б (PNP) | Nhận xét |
|---|---|---|---|
| Cấu trúc | n-p-n Si epitaxi-planar | p-n-p Si epitaxi-planar | cặp bù |
| U_кэ max | 30 V (một số nguồn: 35 V) | 30 V | tương đương |
| **I_к max liên tục** | **30 mA** | **10 mA** | ⚠ lệch 3 lần |
| I_к xung | 60 mA | 50 mA (t_и ≤ 10 µs) | |
| P_к max | 225 mW | 150 mW | |
| h21э | 25…100 | 30…90 | |
| **f_гр** | **≥ 120 MHz** | **5 MHz** | ⚠ lệch 24 lần |
| I_кбо | ≤ 10 µA | ≤ 1 µA | |

### Hệ quả đối với phép thử A313-V.06

1. Iк liên tục 10 mA của 2Т203Б là giới hạn quan trọng, **không chứng minh tải 400 Ω an toàn**: tải 4 V/400 Ω đã 10 mA, còn dòng Rfb tới 0,4 mA, headroom 180 Ω, nhiệt và quá độ. Bắt đầu đo với ≥1 kΩ thuần trở; tảiСКТ thực phải xác địnhZ(f)/pha. Xem §10.6 tài liệu phân tích Rev. C.
2. Không thử chập đầu ra. **66,11 mA** là kết quả mô hình `(12,6−0,7)/180` với base lên sát rail, không phải dòng được bảo đảm. Thực tế phụ thuộc swing OA/β/giới hạn nguồn. Không suy thời gian “hỏng tức thì” chỉ từ phép tính này.
3. Chênh lệch f_гр giữa NPN/PNP không đủ dự đoán sườn âm chậm hơn: vòng hồi tiếp, mạng RC và tải cùng quyết định. Dẫn NPN/PNP theo chiều dòng; với tải phản kháng, không quy chỉ theo dấu điện áp.

---

## 3. CÁC MỨC NGUỒN VÀ TƯƠNG THÍCH

| Mức nguồn | Linh kiện tiêu thụ | Ghi chú |
|---|---|---|
| **+12,6 V / −12,6 V** | 140УД1Б (18 con), tầng đệm Q | 140УД1Б danh định đúng ±12,6 V |
| **−23 V** | Kéo xuống cho tầng dịch mức (R32, R33, R35, R36) | Là mức "mở khoá" cho затвор 168КТ2 |
| **+3,5 V** | Mức "đóng khoá" cho затвор 168КТ2 | |
| **+5 V** | **Không dùng** trên tấm .06 | ✔ đã xác minh (§4) |
| **+6,3 V** | **Không dùng** trên tấm .06 | ✔ đã xác minh (§4) |

**Biên độ điều khiển:**26,5 V là swing so GND. U_зп là điện áp gate–подложка; chân 11 thả nổi nên **chưa tính được dự trữ điện áp thực** bằng 30−26,5. Quy luật gate âm dẫn đang được dùng làm giả thiết, chưa đo trực tiếp trên tấm.

---

## 4. ✅ CHÂN 4 VÀ CHÂN 11 (ПОДЛОЖКА) CỦA 168КТ2 — ĐÃ CHỐT: KHÔNG DÙNG

Theo datasheet 168КТ2, **chân 11 là подложка (substrate/đế)** và **chân 4 không sử dụng**.

Sơ đồ nguyên lý (BV.18, BV.22) chỉ vẽ 12/14 chân — và **đây là đúng thực tế**:
**trên các tấm mạch A313-V, chân 4 và chân 11 của mọi vỏ 168КТ2 đều không được nối** (đã xác nhận 16/09/2026).

Đế để thả nổi là sự kiện đã chốt cho tấm. **Cơ chế phân cực đế nội bộ chưa được chứng minh**; không tự nối chân 11 để sửa ngược kết luận thực tế.

### Hệ quả

| # | Nội dung |
|---|---|
| 1 | **Đồ gá kiểm tra không cần cấp nguồn phụ cho đế.** Tấm .06 chỉ cần 4 mức: +12,6 V, −12,6 V, −23 V, +3,5 V |
| 2 | **+5 V và +6,3 V trên DC11 không dùng** — không cần cấp khi test |
| 3 | Thư viện Altium **giữ nguyên ký hiệu 12 chân**, không cần bổ sung chân 4/11 |
| 4 | ⚠ Khi thay bằng linh kiện hiện đại: mạch gốc **không đưa điện thế đế ra chân** ⇒ module chuyển đổi phải tự tạo phân cực đế/nguồn riêng từ các ray sẵn có |

> Áp dụng cho **cả tấm A313-V.05** (57 vỏ 168КТ2Б) — cần kiểm tra lại trên bản vẽ BV.19/BV.20 của tấm .05 khi phân tích tấm đó, nhưng theo cùng nguyên tắc thiết kế thì kết luận nhiều khả năng giống nhau.

---

## 5. NGUỒN TRA CỨU

* 168КТ2 — datasheet nhà sản xuất, АО «Восход»-КРЛЗ, ТУ АЕЯР.431160.166 ТУ
* К140УД1 / КР140УД1 — sổ tay vi mạch tương tự
* 2 Т 312 / КТ 312, 2 Т 203 / КТ 203 — sổ tay transistor lưỡng cực Liên Xô/Nga
* Bản vẽ gốc: 07MB.A313-V.BV.18 / .21 (tấm .05), .BV.22 / .25 (tấm .06)

*(Danh sách liên kết chi tiết ghi ở cuối từng file linh kiện.)*
