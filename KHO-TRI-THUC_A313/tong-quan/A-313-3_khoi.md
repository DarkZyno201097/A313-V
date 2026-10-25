---
id: tong-quan-A-313-3
loai: tong-quan
ap-dung: A-313-3
tu-khoa: [A-313-3, ЕУ3.048.002, thiết bị vào-ra, СчК, СчЦ, СчОп, СчТ, СчСтр, 0оп, 7оп, 4700 µs, 588 µs, РгК1, РгК2, РгПр, ПК, СВК, СПК, СИ, АПи, НУ, Э4, Y16, tấm sườn, МПП, ГПК]
nguon: [A313 original/A-313-3.HDSDKT.pdf trang PDF 13–20, KE-HOACH_KIEM-TRA_A-313-3.md §0–1, SO-DO-NGUON_A-313-3.md, SO-DO-DAU-NOI_E4_A-313-3.md]
do-tin-cay: HDSD
cap-nhat: 2026-10-25
---
# Khối A-313-3 (ЕУ3.048.002) — thiết bị vào-ra và nguồn

Nguồn chính: [HDSD A-313-3](<../../A313 original/A-313-3.HDSDKT.pdf>) (bản dịch, **mất toàn bộ hình**, gọi tắt [A3]).
Tổng quan thiết bị: [A-313_thiet-bi.md](A-313_thiet-bi.md). Từng tấm: thư mục [tam/](../tam/) và bảng trong [00_INDEX.md](../00_INDEX.md).

## 1. Thông số và kết cấu
- Khối lượng 10 kg; tiêu thụ 220 W từ 27 V, 6 W từ 36 V 400 Hz pha A, C [A3 §1.2].
- 24 vị trí: 16 tấm chức năng Y1–Y16 (bảng 6) + 8 mô-đun nguồn Y17–Y24 (bảng 7) [A3 §1.3].
- 16 tấm là МПП 200 × 170 mm, gắn bản lề, lật được 90°; mỗi tấm 2 dãy 53 chân **hàn** với cáp dẹt mềm ГПК, đầu kia hàn
  vào tấm sườn Y16 ⇒ **kiểm tại chỗ là mặc định; chỉ tháo tấm đã khoanh hỏng**. Y17 (5 V 15 A) cắm-rút được
  [A3 §2.4; KE-HOACH §0].
- **Y16 là tấm sườn không linh kiện**; sơ đồ đấu nối **Э4 (ЕУ3.048.002 Э4) là sơ đồ kết nối đầy đủ**: đầu cắm ngoài
  3Ш1…3Ш7 ↔ Y16 ↔ các tấm, và giữa các tấm với nhau qua cáp dẹt [xác nhận người dùng 2026-10-23; SO-DO-DAU-NOI_E4].
- Đầu cắm: 3Ш3/3Ш4 (РПКМ3-67/67) ra máy bay; 3Ш1/3Ш2 sang A-313-2A; 3Ш5/3Ш7 kiểm tra [KE-HOACH §1.3].
  Ảnh Э4: [A313-3_CONTROL/KHOI_So-do-dau-noi/](<../../A313-3_CONTROL/KHOI_So-do-dau-noi/>).

## 2. Nguyên lý làm việc [A3 §2.1]
- **Chu kỳ 4700 µs = 8 thao tác 0оп–7оп × 588 µs.** 32 chu kỳ = **0,15 s**: phục vụ 32 thuê bao số thu, 32 số phát,
  32 tương tự thu, 32 tương tự phát.
- Nhịp do **СчК** (HDSD ghi 19 bit): СчЦ bit 0–4 (chu kỳ), СчОп bit 5–7 (thao tác), СчТ bit 8–12 (nhịp),
  СчСтр bit 13–17 (cổng). Chạy theo thạch anh riêng ⇒ **chỉ cần nguồn là khối tự phát chu kỳ**, không cần A-313-2A
  [A3; KE-HOACH §0 nguyên tắc 2].
- Thao tác 0, 1, 6, 7: chọn kênh theo СчЦ (giao tiếp chương trình) hoặc theo РгК1/РгК2 do A-313-2A nạp (giao tiếp
  lệnh); thao tác 2: thu ПК2; thao tác 3–7: phục vụ ngoại vi theo chương trình A-313-3.
- Giao tiếp phân khối A-313-21 (ОЗУ trong A-313-2): ЗАПИСЬ УВВ / ЧТЕНИЕ УВВ ở đầu hoặc cuối thao tác; địa chỉ 9 bit do
  A-313-3 tạo.
- **Mã nối tiếp ПК:** từ 20 bit, bit cao trước, xung kép; mã số thuê bao rồi thông tin; cổng phát СВК, cổng thu СПК
  (rộng hơn thời gian 20 bit 25 µs); xung đồng bộ СИ.
- **Tích phân trước mã hoá** (chống nhiễu cao tần): 3оп+4оп → mã hoá ở thao tác 5; 7оп+0оп → mã hoá ở thao tác đầu.
  Trước đó: tự chỉnh không (АПи) và nạp điều kiện ban đầu (НУ), mỗi chế độ nửa thao tác.
- Đường tương tự: vào — chuyển mạch chọn 1/16 kênh tương tự + 1/16 lệnh đơn → tích phân → biến đổi → mã song song →
  ô ОЗУ 000–037₈; ra — ô ОЗУ 040–077₈ → biến đổi → chuyển mạch cửa ra → khuếch đại cửa ra [A1 §2.3].
- Định dạng từ điều khiển РгК1, РгК2, РгПр: [A3 hình 5, trang PDF 20].

## 3. Ba phần chức năng [A3 §2.2]
| Phần | Tấm |
|---|---|
| Biến đổi số | Y4 điều khiển chương trình · Y3 điều khiển giao tiếp · Y5 điều khiển lệnh · Y6 điều khiển biến đổi · Y2 biến đổi tín hiệu số · Y1 tạo ПК và bus chính · Y7 tấm phối hợp · Y14/Y15 biến đổi PK I/II |
| Biến đổi số–tương tự | Y12/Y13 chuyển mạch cửa vào · Y8 bộ biến đổi · Y9 tích phân · Y11 chuyển mạch cửa ra · Y10 khuếch đại cửa ra |
| Nguồn | Y17…Y23 (7 bộ nguồn) · Y24 kiểm tra và báo hiệu |

Vai trò, ảnh quét, netlist và tình trạng từng tấm: bảng tấm trong [00_INDEX.md](../00_INDEX.md).

## 4. Điểm đáng chú ý cho sửa chữa
- ~5 V 400 Hz (chuẩn mã hoá) do **Тр1 ТН-12-40-400 trên Y17** hạ từ ~36 V pha A/C [chep-tu-anh, SO-DO-NGUON_A-313-3.md §2].
- Bàn ПС17-319 thay được bằng bộ giả lập ЦВУ (FPGA làm ОЗУ 512 × 18 bit, trả ИКО/ИВЧ); ПС17-318 thay bằng đồ gá ngoại vi
  theo 3Ш3/3Ш4 dùng chung cho A313-V [suy-luan, KE-HOACH §0 nguyên tắc 3–4].
- Kế hoạch kiểm tra tổng quát: [KE-HOACH_KIEM-TRA_A-313-3.md](<../../KE-HOACH_KIEM-TRA_A-313-3.md>).
