# KẾ HOẠCH KIỂM TRA & SỬA CHỮA KHỐI GỐC A-313-3

# (thiết bị vào-ra và nguồn, ЕУ3.048.002 — thiết bị A-313)

**Rev. A — 20/10/2026.** Kế hoạch **tổng quát**. Kế hoạch chi tiết từng tấm lập sau khi có đủ sơ
đồ (§2). Nguồn: `A313 original/A-313-3.HDSDKT.pdf` (gọi tắt [A3]), `A-313-1ok.pdf` ([A1]),
`A-313-2.pdf` ([A2]); đối chiếu với `PHAN-TICH_TOAN-KHOI_A313-V.md` ([TK]).

---

## 0. Nhiệm vụ và nguyên tắc

**Nhiệm vụ.** Khôi phục khối Nga A-313-3 (cùng A-313-2A) thành **bộ dự phòng** cho khối mới
A313-V. Khối mới đôi khi trục trặc chưa rõ nguyên nhân; khi đó lắp bộ cũ vào để thay thế, đồng thời so chéo để khoanh lỗi của khối mới. Bàn kiểm tra ПС17-318/319 đang hỏng.

**Bốn nguyên tắc rút ra từ tài liệu:**

1. **Các tấm không cắm-rút được.** [A3] §2.4: 16 tấm là mạch in nhiều lớp (МПП) 200 × 170 mm, gắn
   bản lề, lật lên được 90°. Mỗi tấm có 2 dãy tiếp điểm 53 chân, **hàn** với băng cáp mềm ГПК;
   đầu kia hàn vào tấm chuyển mạch Y16. Tháo một tấm nghĩa là tháo hàn 106 điểm trên МПП (dễ bong
   pad, tách lớp). ⇒ Kiểm **tại chỗ** (lật tấm, cấp nguồn khối, đo trên tấm) là mặc định. **Chỉ
   tháo tấm đã khoanh là hỏng.** Ngoại lệ: bộ nguồn 5 V 15 A là tấm tháo được, cắm qua đầu nối.
2. **Phần số tự chạy.** Bộ đếm lệnh СчК 19 bit chạy theo thạch anh riêng của A-313-3, và A-313-3
   là bên **chủ động** mọi giao tiếp ([A3] §2.1, §2.2.1). Chỉ cần nguồn là khối tự phát chu kỳ
   4700 µs, 8 thao tác × 588 µs, chu kỳ 32 × 0,15 s, vạch ВрМ1/ВрМ2, yêu cầu ЗпУВВ/ЧтУВВ và địa
   chỉ КША, nhịp 80 kHz, СИ, СВК, СПК, cùng các tín hiệu chọn kênh t/T/K. Không có A-313-2A thì
   yêu cầu tự xoá sau 24 µs. ⇒ **Kiểm được phần lớn phần số bằng máy phân tích logic, không cần
   bàn thử.**
3. **Bàn ПС17-319 thay được bằng một bộ giả lập ЦВУ tự làm.** Giao tiếp A-313-2A ↔ A-313-3
   ([A3] Bảng 4–5) chỉ gồm КШЗп 18, КШЧт 18, КША 9 bit, ЗпУВВ, ЧтУВВ, ИКО, ИВЧ, ВрМ1, ВрМ2, mức
   logic loạt 133/136 (5 V). Một bo FPGA (Cyclone, sẵn có trong xưởng) làm ОЗУ 512 từ × 18 bit, trả
   ИКО/ИВЧ, nối PC qua UART là đọc-ghi được mọi ô 000–777₈. Đây chính là chế độ "ВНУТРЕННИЕ СВЯЗИ
   ЦВУ-УВВ" của ПС17-319 trong phiếu kiểm tra [A3].
4. **Bàn ПС17-318 (giả lập ngoại vi) nên làm mới theo 3Ш3/3Ш4, vì dùng được cho CẢ HAI khối.**
   A313-V thay đúng chỗ A-313-2A + A-313-3, cùng đầu nối máy bay 3Ш3/3Ш4 (РПКМ3-67/67). Một đồ gá
   ngoại vi (СКТ 400 Hz, PK 27 V, tải ra, vòng ПК, tần số F1–F4) phục vụ cả việc sửa khối cũ lẫn
   khoanh lỗi khối mới — đúng mục tiêu "dự phòng và so chéo".

---

## 1. Bảng kê tấm và tình trạng sơ đồ

Số hiệu theo [A3] Bảng 6–7 và danh mục kèm sơ đồ đấu nối (Hình 3, trang PDF 76). "Hình" là số hình
trong mục lục phụ lục [A3]. **Không hình nào còn nét vẽ** (trang PDF 73–90 chỉ còn tên hình; PDF
dừng ở trang tài liệu 104/159). "Danh mục LK" = bảng linh kiện dạng chữ còn đọc được.

Cột "Thay thế tạm" là bản vẽ khác trong repo có thể dùng tạm:
✅ = bản chép xác nhận được; ◐ = tương đương chức năng, chỉ để tham khảo; — = không có.

### 1.1. Phần biến đổi số

| Vị trí | Tên                                                            | Số hiệu        | Sơ đồ nguyên lý ([A3])            | Danh mục LK        | Thay thế tạm trong repo                        | Cần anh/chị bổ sung                              |
| -------- | --------------------------------------------------------------- | ---------------- | -------------------------------------- | ------------------- | ------------------------------------------------ | --------------------------------------------------- |
| Y1       | Bộ tạo ПК và BUS chính                                    | ЕУ2.035.587    | Hình 10 — **thiếu**           | **thiếu**    | — (chức năng nằm trong FPGA .01)             | Э3 + danh mục                                     |
| Y2       | Bộ biến đổi tín hiệu số (СчД, tần số/cự ly → mã) | ВШ3.036.056    | Hình 9 — **thiếu**            | ✔ trang PDF 88–89 | —                                               | Э3; bản vẽ lắp ráp Hình 31                    |
| Y3       | Bộ điều khiển giao tiếp                                    | ЕУ3.057.136    | Hình 6 (3 tờ) — **thiếu**    | ✔ trang PDF 80–82 | —                                               | Э3                                                 |
| Y4       | Bộ điều khiển chương trình (СчК, ГТИ)              | ЕУ3.057.138    | Hình 5 (2 tờ) — **thiếu**    | ✔ trang PDF 78–79 | —                                               | Э3                                                 |
| Y5       | Bộ điều khiển lệnh (РгК1/2, РгПр, РРК1/2)        | ЕУ3.057.139    | Hình 8 (2 tờ) — **thiếu**    | ✔ trang PDF 86–87 | —                                               | Э3                                                 |
| Y6       | Bộ điều khiển biến đổi (РПР 16 bit, РМ)             | ЕУ3.057.140    | ✔ đủ 3/3 lист + **ĐÃ CHÉP PARTIAL** 2026-10-24 (Codex: BOM 77, net 997, conn 173 — khớp Э3↔Э4 103/139) | ✔ (chung ảnh với Э3) | — | Э3 — PARTIAL, xem PROJECT_HANDOFF.md T06 |
| Y7       | Tấm mạch phối hợp                                           | ВШ3.031.020    | Hình 11 — **thiếu**           | **thiếu**    | —                                               | Э3 + danh mục; lắp ráp Hình 27                 |
| Y14      | Bộ biến đổi PK I (lệnh đơn ra 27 V)                      | ВШ2.068.054    | không có trong mục lục (Hình 13?) | **thiếu**    | ✅ A313-V.07 chép theo У14/У15 ([TMKT] §6.6) | Э3 hoặc xác nhận giống Y15; lắp ráp Hình 29 |
| Y15      | Bộ biến đổi PK II (lệnh đơn ra chập mát)               | ВШ2.068.054-01 | Hình 12 — **thiếu**           | **thiếu**    | ✅ A313-V.07 (như trên)                        | Э3; lắp ráp Hình 28                             |

### 1.2. Phần biến đổi số–tương tự

| Vị trí | Tên                                                          | Số hiệu        | Sơ đồ nguyên lý ([A3])  | Danh mục LK     | Thay thế tạm trong repo                                                      | Cần anh/chị bổ sung              |
| -------- | ------------------------------------------------------------- | ---------------- | ---------------------------- | ---------------- | ------------------------------------------------------------------------------ | ----------------------------------- |
| Y12      | Bộ chuyển mạch cửa vào (1)                               | ЕУ3.628.121 ⚠ | Hình 14 — **thiếu** | **thiếu** | ◐ A313-V.02: gộp 2 tấm làm 1, thêm tầng U2/U14 ([TK] §3.2)              | Э3 + danh mục; lắp ráp Hình 32 |
| Y13      | Bộ chuyển mạch cửa vào (2)                               | ЕУ3.628.122 ⚠ | Hình 14 — **thiếu** | **thiếu** | ◐ như trên                                                                  | như trên                          |
| Y9       | Các bộ tích phân (gồm tầng mux K)                       | ЕУ3.072.043    | Hình 15 — **thiếu** | **thiếu** | ◐ A313-V.03 (ЦУС, tầng K đúng cấu trúc gốc)                          | Э3 + danh mục                     |
| Y8       | Bộ biến đổi                                               | ЕУ3.036.157    | Hình 16 — **thiếu** | **thiếu** | ✅ A313-V.04: cùng topo **và cùng số hiệu** với mô tả Y8 (§1.4) | Э3 để chốt                      |
| Y11      | Bộ chuyển mạch cửa ra (АЗУ 49 ô)                      | ЕУ2.242.113    | Hình 17 — **thiếu** | **thiếu** | ✅ A313-V.05 chép theo У11 ([TMKT] §6.4)                                    | Э3 để chốt                      |
| Y10      | Các bộ khuếch đại cửa ra (16 kênh, điều chế 400 Hz) | ЕУ2.032.463    | Hình 18 — **thiếu** | **thiếu** | ◐ A313-V.06                                                                   | Э3 + danh mục                     |

### 1.3. Phần nguồn và khung

| Vị trí | Tên                                                                      | Số hiệu         | Sơ đồ nguyên lý ([A3])                                                                    | Danh mục LK                                                                                                                                                  | Thay thế tạm trong repo                 | Cần anh/chị bổ sung                                    |
| -------- | ------------------------------------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------- |
| Y17      | УЛП +5 V 15 A (tháo được)                                          | ЕУ3.215.469     | Hình 25 — **thiếu**                                                                   | **thiếu**                                                                                                                                              | —                                        | Э3; lắp ráp Hình 33/34 (ВШ6.730.527/530 Д7)        |
| Y18      | УЛП +20 V 0,3 A                                                        | ЕУ3.215.446     | Hình 20 — **thiếu**                                                                   | **thiếu**                                                                                                                                              | —                                        | Э3                                                       |
| Y19      | УЛП +12,6 V 1 A                                                        | ЕУ3.215.452     | Hình 23 — **thiếu**                                                                   | **thiếu**                                                                                                                                              | —                                        | Э3                                                       |
| Y20      | УЛП +6,3 V 0,5 A                                                       | ЕУ3.215.448-01  | Hình 21 (không có trong mục lục) — **thiếu**; [A3] §2.2.3 có mô tả mạch chữ | **thiếu**                                                                                                                                              | —                                        | Э3                                                       |
| Y21      | УЛП −23 V 0,25–0,3 A                                                 | ЕУ3.215.451-02  | Hình 22 — **thiếu**                                                                   | **thiếu**                                                                                                                                              | —                                        | Э3                                                       |
| Y22      | УЛП −12,6 V 1 A                                                       | ЕУ3.215.470     | Hình 26 — **thiếu**; [A3] §2.2.3 có mô tả mạch chữ                              | **thiếu**                                                                                                                                              | —                                        | Э3                                                       |
| Y23      | УЛП ±10 V 0,2 A                                                       | ЕУ3.215.466     | Hình 24 (không có trong mục lục) — **thiếu**                                      | **thiếu**                                                                                                                                              | —                                        | Э3                                                       |
| Y24      | Tấm kiểm tra và báo hiệu                                             | ЕУ3.215.139 ⚠  | Hình 19 — **thiếu**; [A3] §2.2.3 mô tả chi tiết (K1–K6, Y1–Y10)                 | **thiếu**                                                                                                                                              | ◐ A313-V.08.02 giữ nguyên lý tấm Nga | Э3 + danh mục; lắp ráp Hình 30                       |
| Y16      | **Tấm sườn/backplane** (nối đầu cắm ngoài 3Ш1/3Ш2/3Ш3/3Ш4/3Ш5/3Ш7 tới các tấm khác) — **KHÔNG có linh kiện**, chỉ là mạch in đấu dây thuần tuý | ЕУ3.661.064     | **CÓ Э3 riêng** — ma trận cross-reference 5 lист, xác nhận qua khung tên (sửa lần 2, 2026-10-24) — xem §1.5 | ✔ 5/5 lист, 2 bộ ảnh mỗi lист (`A313-3_CONTROL/Y16/`) | — | **Э3 — đủ** (ma trận, không phải sơ đồ nguyên lý vẽ linh kiện) |
| Khối    | Sơ đồ đấu nối khối                                                 | ЕУ3.048.002 Э4 | ✔ đủ 11/11 lист (tr.142-152), xác nhận khung tên "1/11"…"11/11" (sửa lần 2, 2026-10-24: KHÔNG phải của Y16) | ✔ `A313-3_CONTROL/KHOI_So-do-dau-noi/` (Y1…Y24; C1–C3, C5–C7 К52-5 150 µF; Д1 2Д201Г; Др1 Д213В; Л1; Пр1 10 A; 3Ш1/3Ш2/3Ш5/3Ш7 РС50; 3Ш3/3Ш4 РПКМ3-67/67) | —                                        | **Э4 — ưu tiên 1** (bảng chân 3Ш1…3Ш7)     |
| Khối    | Sơ đồ chức năng phần số / phần số–tương tự                   | —                | Hình 1, 2 — **thiếu**                                                                 | —                                                                                                                                                            | ◐ [TK] §2 (A313-V)                      | nên có                                                  |
| Khối    | Biểu đồ thời gian (ПК, chu kỳ, nhịp 2t/Д/1t, trao đổi, 80 kHz) | —                | Hình 3, 4, 7, 8, 10 trong phần thuyết minh — **thiếu** (chỉ còn chữ)             | —                                                                                                                                                            | —                                        | **ưu tiên 2** (chuẩn so sánh khi đo phần số) |

⚠ **Lệch số hiệu trong chính [A3]:**

- Bảng 6 ghi Y12 = ЕУ3.628.121, Y13 = ЕУ3.628.122; danh mục Hình 3 ghi ngược lại (u12 = .122,
  u13 = .121), và bản dịch còn ghi nhầm u13 là "chuyển mạch cửa **ra**".
- Y24: Bảng 7 ghi ЕУ3.215.139, danh mục Hình 3 ghi ЕУ2.072.139.
- ⇒ Đọc số hiệu trên nhãn tấm thật để chốt.

**Tài liệu ngoài tập A-313-3 cũng cần** (được nhắc trong [A1] §2.4):

- HDSD A-313-2A `И13.031.009-01 РЭ` (110.23.02): phía bus ОЗУ, mức và thời gian của ИКО/ИВЧ — để
  làm bộ giả lập ЦВУ.
- HDSD A-313-12 `ЕУ3.229.063 РЭ` (110.23.04): khoá liên động ОТКЛ / НАПРЯЖЕНИЕ ВЫШЕ-НИЖЕ НОРМЫ.
- Sơ đồ ПС17-318/319: hoặc để sửa bàn, hoặc để chép chức năng sang đồ gá mới.

### 1.4. Căn cứ cho cột "Thay thế tạm"

- **Y8 ↔ A313-V.04 (✅):** mô tả Y8 trong [A3] §2.2.2 và SchDoc `.04` trùng cả topo lẫn số hiệu
  (đối chiếu bằng `tmp/pdfs/review/toan-khoi/schdoc_nets.csv`):

  - đầu ra so sánh → U13 (12-14) → U28 (1-3) tới `A пр`, U28 (5-7) tới `B пр`;
  - bộ phối hợp D8, R44 về −23 V;
  - U14 (8-10), U19 (8-10) nối mát.

  Có vài chỗ khác số: [A3] ghi R27 và Y13 (8-10), TMKT .04 ghi R17 và U14 (12-14). ⇒ Dùng `.04`
  làm sơ đồ tạm cho Y8, đánh dấu chỗ khác.
- **Y11 ↔ A313-V.05, Y14/Y15 ↔ A313-V.07 (✅):** [TMKT] §6.4, §6.6 ghi rõ là chế tạo theo sơ đồ У11,
  У14/У15 của A-313-3.
- **Y12/Y13 ↔ .02, Y9 ↔ .03, Y10 ↔ .06, Y24 ↔ .08.02 (◐):** cùng chức năng, khác mạch. Chỉ dùng
  để hiểu luồng tín hiệu, không dùng để tra số hiệu.
- **Y1–Y7, Y17–Y23: không có thay thế.** Phần số của A313-V nằm trong FPGA; nguồn A313-V dùng
  module Traco/TI.

### 1.5. Y16 là tấm sườn (backplane) — không có linh kiện, CÓ Э3 riêng (ma trận)

**Xác nhận của người dùng (2026-10-23), kỹ sư trực tiếp quan sát khối thật:**

> Y16 thực ra chỉ là tấm sườn để kết nối giữa các đầu cắm ngoài (3Ш1, 3Ш2, 3Ш3, 3Ш4, 3Ш5, 3Ш7) nên
> bản thân tấm này không có linh kiện. Dây sẽ đi từ đầu cắm ngoài đến tấm Y16, và các dây cáp bẹ
> cũng nối từ tấm Y16 đến các panel khác (lưu ý có panel dùng dây nối trực tiếp thay vì cáp bẹ).

**Hệ quả quan trọng — đổi cách hiểu đã ghi trước đây (SỬA LẠI LẦN 2, 2026-10-24 — đảo ngược mục 1-2 cũ):**

1. **Y16 CÓ sơ đồ riêng — mã ЕУ3.661.064 Э3**, dạng bảng ma trận cross-reference (không vẽ linh
   kiện vì không có linh kiện, mà là bảng tên tín hiệu × tấm đích — đúng bản chất một tấm sườn).
   Tài liệu có **5 lист**, xác nhận qua khung tên viết tay "ЕУ3.661.064 Э3 л.N/5" đọc trực tiếp
   trên ảnh (người dùng chụp lại rõ 2026-10-24). Lưu tại `A313-3_CONTROL/Y16/RE_trXXX_a258.jpg`…`a262.jpg`.
   Kết luận cũ "không tồn tại sơ đồ Э3 cho Y16" là **SAI** — do nhầm 11 trang tr.142-152
   (thực ra là Э4 chung của khối) với tài liệu riêng của Y16.
2. **Tài liệu `ЕУ3.048.002 Э4` "Sơ đồ đấu nối khối" (11 trang, tr.142-152) là tài liệu CHUNG của
   TOÀN KHỐI, KHÔNG PHẢI của riêng Y16** — xác nhận qua khung tên "ЕУ3.048.002 Э4 1/11" đọc trực
   tiếp trên ảnh gốc tr.142. Đã dời sang thư mục riêng `A313-3_CONTROL/KHOI_So-do-dau-noi/`
   (trước đó nằm lẫn trong `A313-3_CONTROL/Y16/`, gây hiểu nhầm là tài liệu của Y16).
   5 trang ma trận tr.153-157 (trước gọi nhầm "E4-matran") thực ra thuộc tài liệu ở mục 1
   (ЕУ3.661.064 Э3 của Y16), KHÔNG thuộc ЕУ3.048.002 Э4 — tuy chụp liên tiếp trong cùng cuốn,
   nhưng là 2 tài liệu khác nhau theo đúng khung tên trên từng trang.
3. **Э4 là sơ đồ kết nối ĐẦY ĐỦ của toàn khối, không chỉ riêng Y16** (xác nhận người dùng
   2026-10-23): Э4 thể hiện **ba loại kết nối** —
   (a) đầu cắm ngoài (3Ш1/3Ш2/3Ш3/3Ш4/3Ш5/3Ш7) ↔ Y16;
   (b) Y16 ↔ các tấm Y1–Y24 khác;
   (c) **tấm ↔ tấm trực tiếp với nhau** (không qua Y16) — qua cáp bẹ hoặc dây nối trực tiếp.
   Vì vậy Э4 chính là **ma trận kết nối tín hiệu của toàn khối A-313-3**, từ đầu cắm ngoài tới
   mọi tấm bên trong — không chỉ là "bảng đấu nối của Y16". Xem kế hoạch khai thác dữ liệu này
   thành bảng kết nối toàn khối ở `PLAN_KET-NOI-TOAN-KHOI_A-313-3.md`.
4. **Kiến trúc đấu dây vật lý** (để tham khảo khi đo/sửa):
   `Đầu cắm ngoài (3Ш1/3Ш2/3Ш3/3Ш4/3Ш5/3Ш7) → dây → Y16 → {cáp bẹ hoặc dây nối trực tiếp} → các tấm Y1–Y24 khác`,
   và các tấm cũng có thể nối trực tiếp với nhau (không qua Y16).
   Khi dò lỗi mất tín hiệu giữa đầu cắm ngoài và một tấm bất kỳ, Y16 là điểm trung chuyển bắt buộc
   phải kiểm tra (đứt mạch in, chân hàn xấu, hoặc đầu cáp bẹ lỏng) — không có linh kiện bán dẫn nào
   trên đường đó nên không hỏng theo kiểu "cháy linh kiện".
5. **Chưa biết chắc**: panel nào dùng cáp bẹ, panel nào dùng dây nối trực tiếp — cần người dùng bổ
   sung khi có dịp mở khối quan sát. Ghi vào đây khi xác định được, thay vì để chung chung.

> **Cập nhật 22/10/2026:** người dùng đã chụp bản giấy ЕУ3.048.002 РЭ (`ЕУ.048.002.РЭ_A313-3/`, 249 ảnh).
> Phụ lục có Э4/Y16 (tr.142–157) và Э3 + ПЭ của hầu hết các tấm (рис.6–26) — xem
> `DANH-MUC_ANH_RE_A-313-3.md` §2. Còn thiếu sơ đồ рис.5 (Y4), рис.15 (Y9) và nhiều tờ gấp chụp
> chưa trọn (§4 của file đó). Cột «Sơ đồ» ở bảng trên chưa sửa — sẽ sửa khi chép xong từng tấm.
> Э4/Y16 tr.142–152 đã chép và kiểm chéo: `SO-DO-DAU-NOI_E4_A-313-3.md`. Danh mục cấp khối tr.142 sửa
> số hiệu У12/У13 (đảo), У14/У15, У24 = ЕУ2.072.139 và У21 = −20 В — xem §2 của file đó.
> Э3 phần nguồn рис.20–26 và У24 рис.19 đã chép (BOM + netlist + mô tả + quy trình cấp điện thử):
> `SO-DO-NGUON_A-313-3.md`; §3 của file đó là danh sách N1…N10 cần đo/chụp trước Giai đoạn 1.

---

## 2. Danh sách xin bổ sung (theo thứ tự ưu tiên)

| Ưu tiên   | Tài liệu                                                                                                                            | Vì sao                                                                                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Sơ đồ đấu nối khối **ЕУ3.048.002 Э4** (Hình 3, 4 tờ) + tấm chuyển mạch **Y16 ЕУ3.661.064 Э3** (Hình 4) | Bảng chân 3Ш1, 3Ш2 (sang A-313-2A), 3Ш3, 3Ш4 (máy bay), 3Ш5, 3Ш7 (kiểm tra) và đường đi qua Y16. Không có nó thì không làm được đồ gá, không dò được tín hiệu tại chỗ. |
| **1** | Bộ nguồn **Y17–Y23** (Hình 20–26) + tấm kiểm tra **Y24** (Hình 19)                                                | Giai đoạn 1 (nguồn) đi trước mọi thứ.                                                                                                                                                              |
| **2** | Phần số **Y1–Y7** (Hình 5–11) + các biểu đồ thời gian trong thuyết minh                                              | Giai đoạn 2–3 (phần số và giả lập ЦВУ). Riêng Y1 không còn cả danh mục linh kiện.                                                                                                         |
| **2** | HDSD **A-313-2A** (110.23.02) và **A-313-12** (110.23.04)                                                                | Thời gian và mức của bus ОЗУ; khoá liên động nguồn.                                                                                                                                            |
| **3** | Phần tương tự **Y12, Y13, Y9, Y10** (Hình 14, 15, 18)                                                                      | Chưa có bản tương đương đủ tin cậy.                                                                                                                                                             |
| **3** | **Y8, Y11** (Hình 16, 17)                                                                                                      | Đã có bản chép tạm (`.04`, `.05`), cần để chốt.                                                                                                                                              |
| **4** | **Y14, Y15**, bản vẽ lắp ráp Hình 27–34, sơ đồ ПС17-318/319                                                          | Có bản tạm hoặc chỉ cần khi sửa cơ khí/bàn thử.                                                                                                                                                 |

**Cách chuyển tài liệu vào repo:** scan 300–400 dpi, xuất PDF, đặt trong thư mục mới (ví dụ
`A313-3 so do/`), giữ nguyên tên số hiệu Nga. Nếu bản dịch Word còn hình, gửi file `.docx` hoặc riêng
thư mục `word/media/` (ảnh trích ra) — PDF hiện có bị mất hình khi xuất.

---

## 3. Kế hoạch kiểm tra tổng quát (chưa cần sơ đồ chi tiết)

Đi theo thứ tự phụ thuộc: **nguội → nguồn → phần số tự chạy → giả lập ЦВУ → giả lập ngoại vi →
khoanh tấm → ghép A-313-2A**. Mỗi giai đoạn có tiêu chí qua/không qua và một "chữ ký" ghi lại để
so với lần sau, và để so với A313-V.

### Giai đoạn 0 — Hồ sơ và kiểm tra nguội (không cấp điện)

1. Ghi lý lịch: số khối, số hiệu và năm sản xuất **trên nhãn từng tấm** (chốt các lệch số ở §1),
   dấu niêm, lịch sử sửa chữa. Chụp ảnh toàn bộ, kể cả hai mặt từng tấm khi lật bản lề.
2. Ngoại quan:
   - cháy, sém, linh kiện nứt;
   - tụ К52 (C1–C3, C5–C7 150 µF trên đường 27 V) phồng, rò;
   - băng cáp ГПК gãy hoặc nứt ở chỗ gập bản lề — **hỏng điển hình của kết cấu bản lề**;
   - ăn mòn ở đầu nối РПКМ3/РС50; cầu chì Пр1; đèn Л1.
3. Đo nguội:
   - điện trở giữa từng rail và mát tại đầu ra mỗi bộ nguồn, có và không có tải tấm (so hai bên
     để phát hiện chập trên tấm);
   - điện trở cách điện 27 V – vỏ;
   - thông mạch Пр1, Др1, Д1.
4. **Qua:** không có rail nào chập (< vài Ω) mà không giải thích được.

### Giai đoạn 1 — Nguồn

**1a. Từng bộ nguồn riêng.** Bắt đầu với Y17 (5 V 15 A, tháo được). Nếu các bộ khác hàn tại chỗ,
tách đường ra khỏi tải tấm trước. Nguồn phòng thí nghiệm 27 V, hạn dòng thấp lúc đầu; tải giả
≤ 25 % định mức; sau đó tăng dần tới 100 %. Đo điện áp, gợn (dao động ký, băng thông 20 MHz),
tần số chuyển mạch, độ ổn định khi 27 V thay đổi.

Tải giả tính bằng `tmp/pdfs/review/a313-3/k3_nguon.py` (số liệu [A3] Bảng 3):

| Rail     | I định mức | Dung sai      | Module                          | R tải 100 % | P 100 % | R ≤ 25 % (E12) | I       | P trên R |
| -------- | ------------- | ------------- | ------------------------------- | ------------ | ------- | --------------- | ------- | --------- |
| +20 V    | 0,30 A        | +1,00 V       | ЕУ3.215.446                   | 66,67 Ω     | 6,0 W   | 270 Ω          | 0,074 A | 1,48 W    |
| +12,6 V  | 1,00 A        | ±0,63 V      | ЕУ3.215.452                   | 12,60 Ω     | 12,6 W  | 56 Ω           | 0,225 A | 2,83 W    |
| +10 V    | 0,20 A        | ±0,5 V       | ЕУ3.215.466                   | 50,00 Ω     | 2,0 W   | 220 Ω          | 0,045 A | 0,45 W    |
| +6,3 V   | 0,50 A        | ±0,32 V      | ЕУ3.215.448-01                | 12,60 Ω     | 3,1 W   | 56 Ω           | 0,113 A | 0,71 W    |
| +5 V     | 15,00 A       | ±0,26 V      | ЕУ3.215.469                   | 0,33 Ω      | 75,0 W  | 1,50 Ω         | 3,333 A | 16,67 W   |
| −23 V   | 0,30 A        | +0,15/−0,5 V | ЕУ3.215.451-02                | 76,67 Ω     | 6,9 W   | 330 Ω          | 0,070 A | 1,60 W    |
| −12,6 V | 1,00 A        | ±0,63 V      | ЕУ3.215.470                   | 12,60 Ω     | 12,6 W  | 56 Ω           | 0,225 A | 2,83 W    |
| −10 V   | 0,25 A        | ±0,5 V       | ЕУ3.215.466                   | 40,00 Ω     | 2,5 W   | 180 Ω          | 0,056 A | 0,56 W    |
| −6,3 V  | 1,00 A        | ±0,32 V      | ЕУ3.215.469 (Bảng 3 in vậy) | 6,30 Ω      | 6,3 W   | 27 Ω           | 0,233 A | 1,47 W    |

Tổng công suất ra định mức là 127,0 W. Toàn khối tiêu thụ 220 W ([A3] §1.2), tương ứng 8,15 A ở
27 V ⇒ nguồn 27 V phòng thí nghiệm cần ≥ 10 A. Tải +5 V ở 100 % (75 W) dùng tải điện tử.

⚠ Chưa có sơ đồ nên chưa biết bộ nào cần tải tối thiểu để ổn áp xung khởi động. Nếu một bộ không
lên ở tải 25 %: **không nâng hạn dòng**, chờ sơ đồ.

**1b. Tấm Y24 (kiểm tra và báo hiệu).** [A3] §2.2.3 cho tiêu chí:

- K1/K3 quá áp → cắt;
- K2/K4 thấp áp;
- K5 lưới 27 V giảm 15 %, K6 lưới 27 V tăng 10 %.

Thay lần lượt từng rail bằng nguồn điều chỉnh được để tìm điểm tác động thực.

**1c. Toàn bộ nguồn trong khối** (tấm chức năng còn nối): đo mọi rail khi khối chạy không tải ngoài.
Ghi **dòng 27 V tĩnh** làm chữ ký. Dòng bất thường ⇒ cắt từng nhánh để tìm tấm ăn dòng.

**Phép đo 36 V 400 Hz pha A, C (6 W):** kiểm có tạo ra chuẩn 5 V 400 Hz dùng cho kênh 12a/б và УПР.
МОД hay không ([A3] §2.2.2, §2.3).

### Giai đoạn 2 — Phần số tự chạy (không cần A-313-2A, không cần bàn thử)

Cấp nguồn, máy phân tích logic ≥ 32 kênh đặt ở 3Ш1/3Ш2 (◐ nhiều khả năng là hai đầu РС50 sang
A-313-2A — theo [A3] §2.4 và Hình 201; chốt bằng Э4) và trên các tấm Y3/Y4.
Kiểm theo giá trị trong thuyết minh [A3]:

| Kiểm                                                   | Kỳ vọng ([A3])                                                       | Tấm liên quan          |
| ------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------ |
| Thạch anh ГТИ, nhịp 2t1–2t4, Д0–Д5, 1t-4…1t19 | có, đúng thứ tự                                                   | Y4                       |
| Chu kỳ / thao tác                                     | 4700 µs / 588 µs, 8 thao tác 0оп–7оп                           | Y4                       |
| Khung 32 chu kỳ                                        | 0,15 s                                                                 | Y4                       |
| ВрМ1, ВрМ2                                        | có, đồng bộ với КЦ                                              | Y4                       |
| ЗпУВВ / ЧтУВВ, địa chỉ КША 7–15р      | xuất hiện theo trình tự; tự xoá sau 24 µs khi không có ИКО | Y3                       |
| 80 kHz, СИ (20 xung 40 kHz), СВК, СПК           | đúng dạng                                                           | Y1, Y4                   |
| t1–t4, T1–T4, K1–K4 (theo СчЦ)                    | quét đủ 32 tổ hợp mỗi 0,15 s                                     | Y3, Y4 → Y12/Y13/Y9/Y11 |
| Mức logic                                              | "1" 2,4–4,5 V, "0" 0–0,35 V (loạt 133/136)                          | mọi tấm số            |

**Qua:** đủ tín hiệu, đúng chu kỳ. Lưu lại bản ghi logic làm chữ ký chuẩn. Biểu đồ gốc (Hình 3, 4,
7, 8, 10 [A3]) đang thiếu, nên tạm so với số liệu chữ ở trên.

### Giai đoạn 3 — Giả lập ЦВУ (thay ПС17-319 và thay A-313-2A khi kiểm)

Bo FPGA + chuyển mức 5 V/3,3 V, nối 3Ш1/3Ш2 (cần bảng chân từ Э4 — ưu tiên 1):

- ОЗУ 512 × 18 bit; trả ИКО, ИВЧ theo thời gian ở Bảng 4–5 [A3] (≤ 17 µs);
- ghi log mọi truy cập, đọc/ghi ô qua UART;
- kiểm bit chẵn lẻ КШЗп 16р/17р (tổng số "1" lẻ cho mỗi nửa 8 bit, [A3] §2.3).

**Bài kiểm làm được ngay khi có giả lập:**

1. **Lệnh đơn ra:** ghi ô 225₈/226₈ → đo 32 đầu ra ở 3Ш4 (Y5 → Y14/Y15).
2. **Giải mã:** ghi ô 040–077₈ → đo các đầu ra tương tự (Y6 → Y8 → Y11 → Y10).
3. **Mã hoá:** cấp tín hiệu vào → đọc ô 000–037₈ (Y12/Y13 → Y9 → Y8 → Y6).
4. **Tự hiệu chỉnh tích phân** như phiếu kiểm tra [A3] (trang 63–65): ô 227₈ = 000200₈ → đọc ô
   013₈, giá trị trung bình phải là (110000 ± 20)₈ (kênh chuẩn 12 ứng với 45°).
5. **Nối tiếp:** vòng ПК ra → ПК vào ở 3Ш4 → so ô 140–177₈ với 100–137₈ (Y1, Y6).
6. **Lệnh đơn TTL và РгПр:** ô 236₈.
7. **Tần số Doppler F1–F4 và cự ly:** máy phát 1,3–40 kHz → ô 235₈ (Y2).

### Giai đoạn 4 — Giả lập ngoại vi (thay ПС17-318; dùng chung cho A313-V)

| Phần             | Nội dung                                                                                                                       | Ghi chú                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Nguồn 400 Hz     | biến tần/nguồn 36 V 400 Hz pha A, C                                                                                          | tín hiệu СКТ phải **đồng bộ pha** với nguồn này (tích phân và chuẩn 5 V 400 Hz lấy từ đây) |
| Tín hiệu СКТ | 15 cặp a/б = U·sinα, U·cosα, 400 Hz; biên độ theo [A3] tới 12 V (đi qua A-313-7) hoặc 8 V (A313-V) — đặt được | dùng biến thế/DAC + khuếch đại; góc chuẩn 0°, 45°, 90°…                                                  |
| Lệnh đơn vào  | 16 khoá 27 V / hở                                                                                                             | rơ-le hoặc MOSFET                                                                                                  |
| Tải ra           | DC ±4 V (≥ 3 kΩ theo [A2] Hình 104); AC 4 V 400 Hz cấp СКТ; 16 tải lệnh đơn 27 V; 16 kéo lên cho đầu OC         |                                                                                                                      |
| Nối tiếp        | vòng ПК, hoặc giả lập thuê bao A-313-6                                                                                   |                                                                                                                      |
| Tần số          | 4 kênh 1,3–40 kHz                                                                                                             |                                                                                                                      |

Đồ gá cắm vào 3Ш3/3Ш4 (РПКМ3-67/67) nên dùng được nguyên cho A313-V; bảng chân A313-V đã có trong
`tmp/pdfs/review/toan-khoi/tmkt_3Sh_pinout.csv`. Khi có Э4 của A-313-3 thì đối chiếu để chốt hai
khối có thật sự cùng bảng chân không — **điều kiện tiên quyết để lắp lẫn trên máy bay**.

### Giai đoạn 5 — Khoanh vùng tấm và sửa

Dùng kết quả giai đoạn 2–4, lần theo chuỗi chức năng:

| Triệu chứng                                 | Chuỗi nghi ngờ (theo [A3] §2.2)     |
| --------------------------------------------- | -------------------------------------- |
| Nhịp/chu kỳ sai, không có ВрМ          | Y4 (СчК, ГТИ)                    |
| Không có yêu cầu bus / địa chỉ sai     | Y3                                     |
| Ghi ô đúng nhưng đầu ra lệnh đơn sai | Y5 → Y14/Y15                          |
| Giải mã sai mọi kênh                      | Y6 (РПР) → Y8                      |
| Giải mã sai vài kênh                      | Y11 (АЗУ) / Y10                     |
| Mã hoá sai mọi kênh; ô 013₈ lệch       | Y9 (tích phân, ЦУС) → Y8         |
| Mã hoá sai theo nhóm 4/8 kênh             | Y12/Y13 (tầng t/T) hoặc Y9 (tầng K) |
| Nối tiếp sai                                | Y1                                     |
| Doppler/cự ly sai                            | Y2                                     |

Chỉ tháo hàn tấm khi đã khoanh. Thay linh kiện đúng chủng loại gốc (133/136, 140УД, 168КТ…).
Phần tương tự cần hiệu chỉnh lại (biến trở, ЦУС) sau khi thay.

### Giai đoạn 6 — Ghép khối và tự kiểm

1. Ghép A-313-3 + A-313-2A (+ A-313-12 nếu có) qua cáp ЕУ4.855.905.
2. Giả lập ngoại vi + bảng A-313-6/6M (nếu có) → chế độ КОНТРОЛЬ: mong mã thử `T777000` và đèn
   ОТКАЗ tắt.
3. Chạy lại các phiếu kiểm tra của [A3] và [A1]. Mã thử khác `T777000` thì giải mã theo
   [TK] §4.1, `tmp/pdfs/review/toan-khoi/tk_codes.py`.
4. Lập **chữ ký khối tốt**: dòng 27 V, các rail, ô 013₈ và 227₈, bản ghi logic. Lưu lại để so khi
   dùng khối này làm dự phòng.

---

## 4. Vì sao đây là hướng tối ưu

1. **Không phụ thuộc bàn thử hỏng.** Giai đoạn 0–2 chỉ cần dụng cụ phổ thông. Giai đoạn 3–4 thay
   bàn bằng đồ gá tự làm. Sửa bàn ПС17-318/319 có thể chạy song song, không chặn việc chính.
2. **Ít rủi ro cho khối.** Kiểm tại chỗ là mặc định, chỉ tháo hàn tấm đã khoanh hỏng. Đúng với kết
   cấu bản lề + ГПК hàn của A-313-3.
3. **Đầu tư một lần, dùng cho hai khối.** Đồ gá ngoại vi theo 3Ш3/3Ш4 kiểm được cả A-313-3 lẫn
   A313-V. Giả lập ЦВУ là công cụ thay A-313-2A khi kiểm. So chéo hai khối trên cùng đồ gá là cách
   nhanh nhất để tìm lỗi "chưa xác định được nguyên nhân" của khối mới.
4. **Đi theo phụ thuộc:** mọi tấm cần nguồn; tấm tương tự cần tín hiệu chọn kênh từ phần số. Kiểm
   ngược thứ tự này sẽ ra kết luận sai.

---

## 5. Cần anh/chị trả lời để chốt kế hoạch chi tiết

1. Có khối A-313-2A, A-313-12, bảng A-313-6/6M, A-313-7 đi kèm không? Tình trạng từng khối?
2. Thiết bị PS17-320V (dùng cho A313-V) còn chạy không? Có dùng tạm cho A-313 không?
3. Dụng cụ có sẵn: máy phân tích logic (số kênh), nguồn 27 V ≥ 10 A, nguồn/biến tần 36 V 400 Hz,
   tải điện tử, bo FPGA dự định dùng làm giả lập.
4. Ưu tiên sửa bàn ПС17-318/319 hay làm đồ gá mới? (Kế hoạch này đề xuất làm đồ gá mới, sửa bàn
   chạy song song.)

### 5.1. Trả lời của người dùng (20/10/2026) và hệ quả cho kế hoạch

| # | Trả lời                                                                                                             | Hệ quả                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | A-313-2A, A-313-12, A-313-6/6M, A-313-7 **có**, chưa rõ tình trạng; sơ đồ chỉ có **bản giấy** | Scan sơ đồ giấy theo §2 (300–400 dpi) là việc đầu tiên. Các khối đi kèm cũng qua giai đoạn 0–1 (nguội, nguồn) trước khi ghép ở giai đoạn 6; chưa dùng chúng làm "chuẩn tốt".                                                                  |
| 2 | PS17-320V chạy tốt nhưng **chỉ cho A313-V**, không thuộc nhiệm vụ này                                  | Không dùng PS17-320V cho A-313. Vẫn dùng được nó để lấy **chữ ký khối A313-V tốt** khi so chéo trên đồ gá ngoại vi chung (§3, giai đoạn 4).                                                                                                      |
| 3 | Thiết bị đo **đầy đủ**                                                                                   | Không cắt giảm bài đo vì thiếu dụng cụ; giai đoạn 2 dùng máy phân tích logic đủ kênh cho toàn bộ bus КШЗп/КШЧт/КША.                                                                                                                             |
| 4 | **Song song**: một đội sửa ПС17-318/319, nhóm này làm đồ gá riêng để test tấm và khối         | Đồ gá (giả lập ЦВУ + giả lập ngoại vi) là nhánh chính. Khi bàn sửa xong thì dùng bàn để **đối chứng** đồ gá: cùng một khối, hai cách đo phải cho cùng kết quả. Chia sẻ bảng chân Э4 và sơ đồ ПС17-318/319 giữa hai đội. |

---

*Mọi số liệu trong file này lấy từ [A3] hoặc tính bằng `tmp/pdfs/review/a313-3/k3_nguon.py`.
Chưa có phép đo phần cứng nào.*
