---
id: tong-quan-A-313
loai: tong-quan
ap-dung: A-313
tu-khoa: [A-313, ЕУ1.247.199, máy tính dẫn đường, A-313-2A, A-313-3, A-313-12, A313-5, A313-6, A313-6M, A313-7, ОЗУ, КШЗп, КШЧт, КША, ИКО, ИВЧ, ВрМ1, ВрМ2, chu trình 4,7 ms, 0,15 s, 4,8 s, A313-V]
nguon: [A313 original/A-313-1ok.pdf (HDSD thiết bị A-313, ЕУ1.247.199 РЭ) trang PDF 14–23, PHAN-TICH_TOAN-KHOI_A313-V.md §1, KE-HOACH_KIEM-TRA_A-313-3.md §0]
do-tin-cay: HDSD
cap-nhat: 2026-10-25
---
# Thiết bị A-313 (ЕУ1.247.199) — tổng quan

Nguồn chính: [HDSD thiết bị A-313](<../../A313 original/A-313-1ok.pdf>) (bản dịch tiếng Việt, gọi tắt [A1]).
Khối A-313-3 chi tiết: [A-313-3_khoi.md](A-313-3_khoi.md).

## 1. Công dụng [A1 §1.1]
Máy tính số trên máy bay, làm việc trong tổ hợp dẫn đường: điều khiển tự động, bán tự động và bằng tay
máy bay theo hành trình đặt trước, quay về vùng sân bay, cơ động trước hạ cánh.
Biến thể (bộ): ЕУ1.247.199-03 và -04.01 (tổ hợp dẫn đường), -09 (thiết bị kiểm tra bay).

## 2. Thông số chính [A1 §1.2]
| Hạng mục | Giá trị |
|---|---|
| Sẵn sàng làm việc | 3 s |
| Điểm lập trình | 5 sân bay, 9 điểm trung gian, 5 đài mốc vô tuyến; 4 tham số/điểm |
| Bộ nhớ (-03, -04.01) | cố định 8192 từ, thao tác 768 từ, bán cố định 256 từ (-09: cố định 16384 từ) |
| Nguồn | +27 V ≤ 11 A; ~36 V 400 Hz ≤ 0,7 A; ~115 V 400 Hz ≤ 0,5 A |
| Kiểm tra | tự kiểm tra liên tục; kiểm qua КПА |
| Khối lượng | -04.01 ≤ 35,8 kg; -09 ≤ 33,1 kg; -03 ≤ 31,1 kg |

## 3. Thành phần [A1 §1.3, bảng 2; §2.1]
| Thành phần | Số hiệu | Nhiệm vụ |
|---|---|---|
| **A-313-2A** thiết bị tính số | И13.031.009-01 | Bộ xử lý (hệ lệnh một địa chỉ) + ОЗУ (phân khối A-313-23) + РЗУ bộ nhớ chương trình (A-313-22). Chạy chương trình dẫn đường. |
| **A-313-3** thiết bị vào-ra và nguồn | ЕУ3.048.002 | Giao tiếp ngoại vi; đổi tín hiệu vào → mã song song 18 bit → ОЗУ; đọc ОЗУ → tín hiệu ra. Cấp nguồn thứ cấp. Chu trình khôi phục 0,15 s. |
| **A-313-12** thiết bị bảo vệ | ЕУ3.229.063 | Ngắt khỏi +27 V khi điện áp ra ngoài giới hạn hoặc một nguồn thứ cấp quá tải. |
| **A313-5** bảng điều khiển; **A313-6 / 6M** bảng thao tác | ЕУ3.624.413 / .414(-01) | Điều khiển và nhập chương trình bay, chỉ thị tham số dẫn đường. |
| **A313-7** khối chuyển mạch cửa vào | ЕУ3.628.117 | Mở rộng: +16 kênh tương tự, +16 lệnh đơn mỗi khối; tối đa 3 khối. |
| Khung giảm chấn A313-4A/4B/9A; cáp ЕУ4.855.905 | — | Giá lắp; cáp nối A-313-2A ↔ A-313-3. |

Ghi chú bảng 2: bộ -03 không có A313-5, A313-7 và dùng A313-6M thay A313-6.

## 4. Nguyên lý làm việc [A1 §2.1–2.2]
- Cảm biến → **A-313-3** (đổi sang mã song song) → **ОЗУ** → **A-313-2A** tính → **ОЗУ** → A-313-3 đổi thành tín hiệu ra.
- Hai khối chạy **chương trình riêng, độc lập**, trao đổi không đồng bộ qua ОЗУ.
- **A-313-3 chủ động:** tạo yêu cầu ЗпУВВ/ЧтУВВ và địa chỉ КША (9 bit, bit 7–15); dữ liệu theo КШЗп và КШЧт (18 bit, bit 0–17).
  A-313-2A trả **ИКО** (kết thúc đọc/ghi ОЗУ) và **ИВЧ** (cho phép thu mã vào thanh ghi A-313-3).
- Không có ИКО thì yêu cầu tự xoá sau «24»; A-313-2A bảo đảm thời gian chờ ≤ «17» [A1, bản dịch **mất đơn vị**; kế hoạch dự án ghi 24 µs — cần đối chiếu bản giấy].
- Ba chu trình: **СКЦ 4,7 ms** (cực ngắn), **КЦ 0,15 s** (ngắn), **ОЦ ≤ 4,8 s** (chuẩn). Vạch thời gian ВрМ1/ВрМ2 ngắt tiến trình tính.
- Với A313-6: từ nối tiếp 20 bit (5 cụm bốn bit, cụm đầu là số từ), tín hiệu đồng bộ xung 40 kHz (dãy 20 xung) và 80 kHz.

## 5. Tín hiệu trao đổi [A1 bảng 1]
| Chiều | Loại | Số lượng |
|---|---|---|
| Vào | xoay chiều 400 Hz từ СКТ, đến 10 V biên độ | 11 (+23 khi có A313-7) |
| Vào | điện áp tương đối một chiều ±10 V / xoay chiều | 4 / 8 (có A313-7) |
| Vào | mã nối tiếp | 2 kênh × 16 từ |
| Vào | tần số | 4 kênh |
| Vào | lệnh đơn 27 V | 16 (32 có A313-7) |
| Vào | lệnh đơn TTL | 8, thêm 12 qua A313-6 |
| Ra | một chiều ±4 V | 16 |
| Ra | xoay chiều đến 4 V (cho СКТ) | 8 |
| Ra | ±4 V tỉ lệ tang góc | 7 |
| Ra | lệnh đơn +27 V / nối mát | 16 |
| Ra | lệnh đơn nối mát / hở mạch | 16 |

## 6. Liên hệ với khối mới A313-V [PHAN-TICH_TOAN-KHOI §1.1]
A313-V thay **cả A-313-2A lẫn A-313-3**, dùng chung đầu cắm máy bay 3Ш3/3Ш4 (РПКМ3-67/67).
Chi tiết ánh xạ tấm: [PHAN-TICH_TOAN-KHOI_A313-V.md](<../../PHAN-TICH_TOAN-KHOI_A313-V.md>) §1.1, và cột «A313-V» trong [00_INDEX.md](../00_INDEX.md).
