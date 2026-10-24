# SƠ ĐỒ ĐẤU NỐI KHỐI Э4 (ЕУ3.048.002 Э4) — A-313-3 (bản chép)

**SỬA LẠI 2026-10-24 (quan trọng):** tiêu đề cũ "Tấm chuyển mạch Y16" là SAI — tài liệu
này (tr.142-152, 11 lист, khung tên "ЕУ3.048.002 Э4 1/11"…"11/11") là **sơ đồ đấu nối
CHUNG của toàn khối**, KHÔNG PHẢI của riêng Y16. Y16 có tài liệu Э3 RIÊNG (ma trận 5 lист,
mã ЕУ3.661.064, nằm ở tr.153-157 — dữ liệu dưới đây KHÔNG áp dụng cho nó) — xem
`A313-3_CONTROL/Y16/00_GHI-CHU.txt` và `KE-HOACH_KIEM-TRA_A-313-3.md` §1.5.

**Lưu ý phạm vi (xác nhận người dùng 2026-10-23):** Э4 không chỉ là bảng đấu nối riêng của Y16.
Đây là **sơ đồ kết nối đầy đủ của toàn khối**, gồm 3 loại liên kết: (a) đầu cắm ngoài
(3Ш1/3Ш2/3Ш3/3Ш4/3Ш5/3Ш7) ↔ Y16; (b) Y16 ↔ các tấm Y1–Y24 khác; (c) tấm ↔ tấm trực tiếp
(không qua Y16) qua cáp bẹ hoặc dây nối trực tiếp. File này + `e4/e4_all.csv` là nguồn dữ liệu
chính để dựng bảng kết nối toàn khối — xem `PLAN_KET-NOI-TOAN-KHOI_A-313-3.md`.

Nguồn: ảnh bản giấy ЕУ3.048.002 РЭ, Phụ lục tr.142–152 (ảnh #136, #140–#149; tra trong
`DANH-MUC_ANH_RE_A-313-3.md`). Chép tay từ ảnh ra CSV: `tmp/pdfs/review/a313-3/e4/p142.csv` … `p152.csv`
(cột `page,photo,table,pin,signal,address,wire,note`; `wire=z` là dây xoắn đôi 0,07 mm²; `¬` là gạch trên;
ô có `?` là chưa chắc). Bản gộp: `e4/e4_all.csv`.

Kiểm chứng:
```
python tmp/pdfs/review/a313-3/e4_sua.py     # áp 11 chỗ sửa đã kiểm trên ảnh (ghi gốc vào note)
python tmp/pdfs/review/a313-3/e4_check.py   # kiểm chéo hai chiều
```
Kết quả: 2877 dòng chân, 58 bảng, **1018 liên kết khớp hai chiều**, 20 không khớp
(`e4/e4_mismatch.csv`, giải thích ở §3), 22 trỏ tới bảng chưa chép, 36 dòng bị gạch bỏ trên bản vẽ (bỏ qua).

## 1. Nội dung từng trang

| Tr. | Ảnh | Bảng |
|---|---|---|
| 142 | #136 | Danh mục linh kiện cấp khối (§2); bảng dây 3Ш5 ↔ У17 3Ш5 (1–50); У21 |
| 143 | #140 | Bảng chân nguồn: У24 (1–18), У22, У23 (1–11), У18, У19 |
| 144 | #141 | У20; mạch vào 27 V: Пр1 (ВП3Б1-10А), Л1, Др1 (Д213Т), C1…C3, C5…C7, Д1 (2Д201Г) |
| 145 | #142 | У16КП1 (1–52), У16КП2 (1–94), У16КП3 (1–52) |
| 146 | #143 | 3Ш1, 3Ш2 (1–50, sang A-313-2A), 3Ш3, 3Ш3В (1–67) |
| 147 | #144 | 3Ш4, 3Ш4В (1–67, máy bay), 3Ш7 (1–50, kiểm tra) |
| 148 | #145 | У16КП4↔У10П1, П1 (tích phân)↔У16КП5, У11П1↔У16КП7, У11П2 |
| 149 | #146 | У12, У13 (chân 1–35, А, Б), У14П1, У15П1 |
| 150 | #147 | У1П1–П3, У2П1–П3, У16КП9, У16КП11 |
| 151 | #148 | У3П1–П3, У4П1–П3, У5П1–П3, У16КП13, У16КП15 |
| 152 | #149 | У6П1–П3, У7П1–П2, У8П1, У16КП8, У16КП10, У16КП12 |
| 153–157 | #150–#154 | **Y16 Э3 riêng** (ЕУ3.661.064, л.1-5) — ma trận П1…П15, đã chép ra `tmp/pdfs/review/a313-3/e4/matrix_nets.csv` (282 net); KHÔNG thuộc tài liệu ЕУ3.048.002 Э4 ở trên dù chụp liên tiếp (sửa lần 2, 2026-10-24) |

Bảng chân tấm (Уn Пm) ở tr.148, 151, 152 không ghi địa chỉ chữ — nối với У16КПk bằng nét vẽ
từng hàng (cùng số chân, hoặc đảo kiểu 28−p / 71−p). Hai đầu của mỗi cặp được chép độc lập ở
một phần bảng và kiểm theo tên tín hiệu; У6П1 ↔ У16КП10 lệch tên ở chân 44 và 52 ngay trên bản vẽ.

## 2. Danh mục cấp khối (tr.142) — chốt các chỗ ⚠ của kế hoạch

| Vị trí | Tên | Số hiệu | So với `KE-HOACH_KIEM-TRA_A-313-3.md` §1 |
|---|---|---|---|
| У1 | Формирователь ПК и магистрали | ЕУ2.035.587 | khớp |
| У2 | Преобразователь цифровых сигналов | ВШ3.036.056 | khớp |
| У3 | Устройство управления обращением | ЕУ3.057.136 | khớp |
| У4 | Устройство программного управления | ЕУ3.057.138 | khớp |
| У5 | Устройство командного управления | ЕУ3.057.139 | khớp |
| У6 | Устройство управления преобразованием | ЕУ3.057.140 | khớp |
| У7 | Плата согласования | ВШ3.031.020 | khớp |
| У8 | Преобразователь | ЕУ3.036.157 | khớp |
| У9 | Интеграторы | ЕУ3.072.043 | khớp |
| У10 | Усилители выходные | ЕУ2.032.463 | khớp |
| У11 | Коммутатор выходной | ЕУ2.242.113 | khớp |
| У12 | Коммутатор входной | **ЕУ3.628.122** | ⚠ kế hoạch ghi .121 — đảo với У13 |
| У13 | Коммутатор входной | **ЕУ3.628.121** | ⚠ kế hoạch ghi .122 |
| У14 | Преобразователь **РК II** | **ВШ3.036.053** | ⚠ kế hoạch ghi «PK I, ВШ2.068.054»; nhưng tr.149 ghi dọc cạnh bảng У14 «РК I ВШ2.068.054» — mâu thuẫn trong chính bản vẽ, cần xem nhãn trên tấm thật |
| У15 | Преобразователь **РК I** | ВШ2.068.054 | ⚠ ký hiệu vị trí bị rách; tr.149 ghi «РК II ВШ2.068.054-01» |
| У16 | Плата коммутационная — **tấm sườn/backplane, KHÔNG có linh kiện** (xác nhận người dùng 2026-10-23); **CÓ Э3 riêng** (ma trận 5 лист, mã ЕУ3.661.064, ở tr.153-157 — KHÔNG thuộc tài liệu Э4 khối này; sửa lần 2, 2026-10-24, xem `KE-HOACH_KIEM-TRA_A-313-3.md` §1.5) | ЕУ3.661.064 | khớp |
| У17 | УЛП 5 В 15 А | ЕУ3.215.469 | khớp |
| У18 | УЛП +20 В 0,3 А | ЕУ3.215.446 | khớp |
| У19 | УЛП +12,6 В 1 А | ЕУ3.215.452 | khớp |
| У20 | УЛП +6,3 В 0,5 А | ЕУ3.215.448-01 | khớp |
| У21 | УЛП **−20 В** 0,3 А | ЕУ3.215.451 | kế hoạch ghi −23 V (theo Bảng 3); trên Э4 lẫn cả hai: У16КП1/5 «−23В», 3Ш3В/60 «−20В» |
| У22 | УЛП −12,6 В 1 А | ЕУ3.215.470 | khớp |
| У23 | УЛП ±10 В 0,2 А | ЕУ3.215.466 | khớp |
| У24 | Плата контроля и сигнализации | **ЕУ2.072.139** | ⚠ kế hoạch ghi ЕУ3.215.139 |
| 3Ш1, 3Ш2, 3Ш5, 3Ш7 | Вилка РС50ТВ | АВ0.364.047ТУ | — |
| 3Ш3, 3Ш4 | Вилка РПКМ3-67/67Ш1 | АВ0.364.040ТУ | — |

Quy định dây (tr.142): tín hiệu đi dây xoắn đôi 0,07 mm², bước xoắn 10–12 mm, dây vỏ của cặp
xoắn nối vỏ khối cả hai đầu cách đầu tín hiệu 10–20 mm; nguồn thứ cấp dây 0,35 mm²; **dây chung
nối vỏ tại đầu cắm 3Ш3**.

## 3. Chỗ chưa khớp còn lại (20 dòng) — phân loại

* **Lưới nhiều điểm ghi kiểu chuỗi** (A→B→C, không có B→A): nguồn ±10 В, +3,5 В, +6,3 В,
  ИСПР.ПИТ (3Ш4/49 → У24/17 → У16КП2/89 → У16КП13/24), ОТКЛ (3Ш4/51 → У24/4 → 3Ш5/18).
  Không phải lỗi chép.
* **Lệch ngay trên bản vẽ** (đã xem ảnh, giữ nguyên, cần đối chiếu tấm thật/đo thông mạch):
  - У23/2 «−5В» → У24/2, nhưng У24/2 là «ВКЛ.» (→ 3Ш4/47).
  - −6,3 В: 3Ш1/38 và У24/3 cùng trỏ 3Ш5/45; bảng 3Ш5 ghi «→У24/3» ở chân 46. Hai chân 45/46 cùng tên «−6,3В 1А».
  - 3Ш3В/58 → У12/15, còn У12/15 ghi ngược «3Ш3/58» (thiếu chữ В).
  - 3Ш4/46 → У14/65 và У1П1/39 → У14/66, nhưng bảng У14П1 chỉ có tới chân 43 (tín hiệu tương ứng ở chân 43 và 9).
  - У16КП2/49 «5В 400Гц» → У12/8, còn У12/8 (Вход 12б, nối cứng với У12/4 Вход 12а) ghi «→У16КП2/43»; КП2/42–47 in rất mờ.
  - У13/Б «+6,3В» → «У23/8», trong khi У20/2 «+6,3В» → У13/Б và У23/8 là «5В ВХ».
* **11 chỗ đã sửa** (lỗi đọc, xác nhận bằng chiều ngược + tên tín hiệu + ảnh): xem danh sách `FIX` trong
  `e4_sua.py`. Đáng chú ý: chân **Б** của У12/У13 viết giống số «6».

## 4. Phát hiện kỹ thuật

* **5 В 400 Hz đi vào bộ chuyển mạch vào:** 3Ш5/12 «~5В 400Гц Ф.А» → У16КП2/49 → У12 (Вход 12) (chân 11/12 của 3Ш5 nằm trên nếp gấp,
  chưa chắc). Giả thuyết: điện áp chuẩn xoay chiều cho kênh tự kiểm của mux vào, cùng nguồn với `УПР.МОД`
  (CLAUDE.md §4.6) — cần Э3 của Y12 (рис.14) để chốt.
* **~36 В 400 Hz** vào 3Ш4/55 (pha A) và 3Ш4/56 (pha C), đi tiếp 3Ш5/33, 3Ш5/25 (dây xoắn) sang khối nguồn — giống
  A313-V.
* **Tín hiệu bị bỏ khi chế tạo:** 3Ш2/28–31 và 3Ш4/42–45 «ВНЕШН. ПРЕРЫВ.», 3Ш4/36–41 (ВИ, 35И, 36И, ЗАПРОС Д1/Д2, ДИ)
  bị gạch trên bản vẽ ⇒ khi làm đồ gá không cấp các chân này.
* **У24 đọc 9 điện áp kiểm tra** (+5, −20, +10, +20, +6,3, −12,6, −10, −6,3, +12,6 В) và xuất ИСПР.ПИТ ЦВУ (3Ш2/35),
  НАПР. ВЫШЕ/НИЖЕ НОРМЫ (3Ш2/36, /37), ИСПР.ПИТ ППЗУ (3Ш2/39) sang A-313-2A — đây là các điểm đo đầu tiên của
  Giai đoạn 1 (nguồn) trong kế hoạch.

## 5. Ma trận nối Y16 (tr.153–157) và so sánh với A313-V

* **Ma trận П1…П15** (`e4/p153_157_matrix.csv`, `e4/matrix_nets.csv`, cách đọc ở `e4/matrix_notes.md`; tái tạo và kiểm
  bằng `e4_matrix.py`): Пn = У16КПn; mỗi cột dọc là một dây, số ở điểm cắt là chân. 278 dây, 622 điểm nối.
  Đối chiếu tên tín hiệu hai đầu với bảng КП: 261/278 khớp (kể cả khác chính tả). Hai ô bảng КП11 chép sai đã sửa
  theo ma trận (`e4_sua.py`). Còn lại: 11 dây có đầu bảng КП để trống tên; КП7/41,6 «ВХОД а/б» ↔ КП12/38,12
  «"а"/"б" ПР» (cần Э3 У11/У8); cột «Выход 2б» ghi П3/23 (trùng СИм) — gần như chắc là **П3/29** (lỗi bản vẽ).
* **3Ш3/3Ш3В/3Ш4/3Ш4В so với phụ lục TMKT A313-V** (`e4_tmkt.py` → `e4/e4_vs_tmkt.csv`): 252/268 chân cùng tín hiệu;
  10 chân bị gạch trên A-313-3 (3Ш4/36–45) thì A313-V để trống ⇒ hai khối **cắm lẫn được về sơ đồ chân máy bay**.
  Khác: 3Ш3В/55 «Uоп ~5В» chỉ có ở A313-V (khối Nga tự tạo ~5 В 400 Гц trong У17, xem `SO-DO-NGUON_A-313-3.md` §2);
  3Ш3В/60 −20 В (Nga) / −23 В (A313-V); 3Ш3В/63 −12,6 В / −12 В.
