# Kiểm chéo độc lập netlist SchDoc A313-V — V.05, V.06 (2026-10-25)

Phạm vi: chỉ V.05 và V.06 (cụm đầu ra, liên quan trực tiếp tấm .05/.06). V.01–V.04, V.07, V.08 **chưa** kiểm ở mức này.
Lý do cần: `PASS` của `check_vXX.py` chỉ kiểm quan hệ BOM–chân–net trong CSV, không kiểm topology.
Phương pháp và nguồn độc lập, không dùng lại code của bộ trích xuất:

| # | Kiểm | Nguồn đối chiếu | Kết quả |
|---|---|---|---|
| 1 | Chân lẻ loi của 140УД1Б (18 chip) | bảng chân trong etiket `tmp/pdfs/review/140ud1B.txt` | **PASS** — lẻ loi đúng các chân 2,3,6,8,11 trên cả 18 chip (контрольный/свободный); chân 1,4,5,7,9,10 luôn nối. Script `xcheck_v06_datasheet.py` |
| 2 | Chân lẻ loi theo (kiểu linh kiện, số chân) | tính nhất quán giữa các instance | V.05: 0 chân linh kiện lẻ loi. V.06: 105, đều thuộc 7 lớp lẻ loi 100% (140УД1Б ×5 chân, 168КТ2Б pin 11, 168КТ2В pin 11); không lớp lẻ loi một phần. Script `xcheck_structural.py` |
| 3 | Đồng cấu các khối lặp V.06 (4 khối × 4 kênh) | băm Weisfeiler–Lehman sau khi bỏ nét toàn cục | 3/4 khối đồng cấu tuyệt đối; khối ВЫХ.5А–6Б khác ở cách gán cổng 168КТ2 → chân 7/10/14/3 vào điện trở cộng. Xem ảnh: khối trái dùng cùng một vỏ cho 2 kênh (U2A+U2B, U2C+U2D), khối phải dùng vỏ riêng (U9A+U9B, U8A+U8B) → **khác biệt có thật trên bản vẽ, không phải lỗi trích xuất** |
| 4 | Đối chiếu ảnh 600 dpi `sodocactam.pdf` tr.6, kênh 1А/1Б và 5А/5Б | đọc trực tiếp ảnh | U1/U2, R4/R5/R85/R87, U7/U8/U9, R12/R13/R101/R103 khớp CSV (chân, net, ВЫХ.nА=) |
| 5 | Đối chiếu ảnh 600 dpi `sodocactam.pdf` tr.5, góc phải (U15/U16/U17, OC"a", OC"b", ВЫХОД"б") | đọc trực tiếp ảnh | Khớp CSV kể cả điểm bất đối xứng: U16.12 = U17.2,6,9,13 (N0044); U16.10 = U17.7,8 (N0133) |
| 6 | V.05: 57 vỏ 168КТ2, mỗi vỏ 14 chân; chỉ 7 kiểu nối chân (24+12+12+6+1+1+1) | tính nhất quán | khớp bố cục 6 khối + khối phải |

## Điểm cần biết
- Nhãn `М` (19 chân) và `М_` (34 chân) trong V.06 là **hai net khác nhau** theo nhãn gốc SchDoc (`M` / `M_`). Có vẻ là M và M đảo (điều khiển cổng tầng 1 và tầng 2); chưa xác nhận bằng BVTK.
- Net `a/GND` (85 chân) gộp hai nhãn `a` và `GND` theo tên (không phân biệt hoa thường), có vẻ là mát chung nhưng đây là suy luận từ nhãn, chưa xác nhận bằng BVTK; `GND/obs.prov` ở V.05 cũng vậy.
- V.01 còn 22 lớp (kiểu, chân) lẻ loi một phần (ví dụ CT25244 pin 10/12/14/15 lẻ loi 2/9, CY62256N pin 13 1/3), V.02 6 lớp (168КТ2Б pin 8–14), V.04 1 lớp (R 5k/1% pin 1, 2/6). Đây là những chỗ nghi dây chưa nối, **chưa soát** — làm trước khi dùng V.01/V.02/V.04.

## Sửa trong bộ trích xuất của Codex (kèm lần kiểm này)
- `extract_schdoc_netlists.py`: tên bản `v09` → `v10` (SchDoc `A313_10.SchDoc` là tấm linh kiện rời rạc V.10; V.09 tấm trung gian 12 đầu DC không có SchDoc trong thư mục).
- Cột "Dòng có `?`" bỏ đếm cột `note` (trước đây v01 = 567, nay 0; chỉ `v0802_ngoc` còn 411 vì ref `R?`/`D?` chưa đánh số).
- Sắp xếp nhãn gộp net theo `(casefold, nguyên văn)` — trước đó `5p_/5P_` ở V.04 và các net của V.08.02 đổi thứ tự giữa các lần chạy (không đồng nhất, chạy lại 6 lần giờ cho cùng một hash).
