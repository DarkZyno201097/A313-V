# DANH MỤC ẢNH CHỤP ЕУ3.048.002 РЭ (A-313-3) — trang ↔ ảnh ↔ hình

Nguồn: thư mục `ЕУ.048.002.РЭ_A313-3/` (249 ảnh, 21/10/2026, **bản gốc, chỉ-đọc**).
Bảng đầy đủ từng ảnh: `tmp/pdfs/review/a313-3/kiemke/trang.csv` (sinh bởi `k3_trang.py`;
số trang đọc bằng mắt từ số viết tay, ô có `?` là chưa chắc). Kiểm kê kỹ thuật (kích thước, độ nét,
ảnh trùng): `kiemke/kiemke.csv` (`k3_kiemke.py`). Cắt vùng để đọc: `k3_crop.py`.

Kiểm lại: `python tmp/pdfs/review/a313-3/k3_trang.py` → 226 trang thấy được trong khoảng 2…247.

## 0. Quy tắc tên ảnh và cách tra

Tên ảnh: `<SÁCH>_tr<TRANG>_a<SỐ ẢNH>[_<hậu tố>].<đuôi>`.

- Sách này dùng `RE`; mã dành cho sách khác: `VT34` = SU-27-VT-34.44,
  `VT28` = su-27-01-vt-28, `A2` = A-313-2, `VT72` = SU-C-VT-72.
- `trNNN` lấy đúng cột `page` của `trang.csv`, đủ 3 chữ số; ô trống dùng `trXXX`, không đoán trang.
- `aNNN` lấy cột `idx`, đủ 3 chữ số: chính là số **#NNN** trong tài liệu, không đánh số lại.
- Ảnh cũ chỉ thêm `_x` khi `kind=X` (không phải trang sách); giữ nguyên đuôi `.jpg`/`.heic`.
- Ví dụ **#167 → `RE_tr171_a167.jpg`**. Tra #NNN bằng `_aNNN`; tra trang bằng `RE_trNNN_`.
- Ánh xạ tên cũ → tên mới và SHA-256: [_DOI-TEN.csv](ЕУ.048.002.РЭ_A313-3/_DOI-TEN.csv).
  Log lịch sử trong `codex-runs/` (kể cả bản dời sang `File của A313-V/codex-runs/`) giữ tên cũ và tra qua bảng này.
- Ảnh bổ sung dùng số tiếp theo **a250, a251…**, mỗi file có số riêng, không dùng lại số ảnh cũ.
  Hậu tố tùy phần chụp: `_L` = nửa trái, `_R` = nửa phải, `_kt` = khung tên, `_cl` = cận cảnh.
  Ví dụ `RE_tr167_a250_L.jpg`, `RE_tr167_a251_R.jpg`, `RE_tr167_a252_kt.jpg`.
  Chỉ điền trang khi đọc được từ bản giấy; chưa rõ dùng `trXXX`.
  **Số `a` cao nhất đã dùng tính đến 2026-10-25: `a268`** (Y4 a250-251, Y3 a252-254, Y6 a255-257,
  Y16 a258-262, Y5 a263-264, Y9 a265, Y11 a266-267, Y12/Y13 a268 cùng một ảnh được lưu ở hai thư mục).
  Ảnh bổ sung tiếp theo bắt đầu từ **a269**.
  Quy tắc này áp dụng cho **mọi ảnh chụp mới từ nay**, không riêng lô 249 ảnh gốc —
  không tự đặt tên khác (vd không dùng tiền tố tự chế như `E3_lisN-M_...`).
- Tên `a2xx` ở §4 là **mẫu dự kiến**, thay bằng số ảnh tiếp theo khi nhập ảnh; không phải tên file đã tồn tại.

Đổi tên một lần ngày **2026-10-23**, nội dung ảnh không đổi; thư mục tiếp tục chỉ-đọc.
Script `tmp/pdfs/review/a313-3/kiemke/doi_ten_anh.py` mặc định chỉ chạy thử;
`--apply` dùng `git mv` và kiểm SHA-256. Đây là công cụ của đợt R01 gồm 249 ảnh,
không dùng để tự đánh số lại ảnh bổ sung.

## 1. Cấu trúc cuốn sách

| Trang | Ảnh | Nội dung |
|---|---|---|
| 2–139 | #1–#132 | Thuyết minh (TO) + hướng dẫn sử dụng + bảng kiểm 201–210 với ПС17-318/319 (tr.117–134). **Hình trong phần TO đánh số riêng** (ví dụ рис.5 formát từ, рис.6 máy phát xung nhịp, рис.10 giản đồ 80 kHz) — không lẫn với рис. của Phụ lục. |
| 139 | #132 | «Приложение, лист 1» — bắt đầu Phụ lục |
| 140–141 | #133, #134/#135 | Sơ đồ chức năng (Э2) cả khối, 2 tờ |
| 142–157 | #136, #140–#154 | Sơ đồ đấu nối Э4 / tấm chuyển mạch Y16: bảng chân 3Ш3В, 3Ш4, 3Ш5 (У17), 3Ш7, П1/П2 từng tấm; ma trận П8…П15 |
| 158–247 | #155–#249 | Sơ đồ nguyên lý Э3 từng tấm (tờ gấp) + Перечень элементов (ПЭ) + bản vẽ lắp ráp |

## 2. Hình trong Phụ lục ↔ tấm

Tên hình đọc từ trang đầu ПЭ («Перечень элементов к схеме электрической принципиальной …»)
hoặc khung tên tờ sơ đồ. Cột «Tấm» theo `KE-HOACH_KIEM-TRA_A-313-3.md` §1 — **khớp toàn bộ**.

| Рис. | Tên (Nga) | Tấm | Sơ đồ Э3 (trang/ảnh) | ПЭ (trang/ảnh) |
|---|---|---|---|---|
| 5 | Устройство программного управления (ЕУ3.057.138 Э3, 2 tờ) | Y4 | 158–159 (#155, #156); **chụp lại rõ 2026-10-24: `A313-3_CONTROL/Y4/RE_tr158_a250.jpg`, `RE_tr159_a251.jpg`** | #137–#139 (Приложение лист 22–24) |
| 6 | Устройство управления обращением (ЕУ3.057.136 Э3, 3 tờ) | Y3 | tờ 1 #231/#232 (không số trang), tờ 2 tr.160 (#157), tờ 3 tr.161 (#158); **chụp lại rõ 2026-10-24: `A313-3_CONTROL/Y3/RE_trXXX_a252.jpg`, `RE_tr160_a253.jpg`, `RE_tr161_a254.jpg`** | 162–163 (#159, #160) |
| 7 | Устройство управления преобразованием | Y6 | ~~164–166 (#161–#163); 167 thiếu~~ **THAY 2026-10-24: 3 ảnh chụp lại rõ nét đủ 3 lист** (`A313-3_CONTROL/Y6/RE_trXXX_a255.jpg`…`a257.jpg`), khung tên xác nhận "ЕУ3.057.140 л.N/3" | 168–170 (#164–#166) |
| 8 | Устройство командного управления | Y5 | 171–172 (#167, #168); **chụp lại rõ nét 2026-10-24: `A313-3_CONTROL/Y5/RE_tr171_a263.jpg`, `RE_tr172_a264.jpg`**, thay ảnh cũ mờ (đã xoá khỏi thư mục làm việc, bản gốc vẫn còn trong `ЕУ.048.002.РЭ(A313-3)/`) | 173–174 (#169, #170) |
| 9 | Преобразователь цифровых сигналов | Y2 | 175–176 (#171, #172) | 177–178 (#173, #174) |
| 10 | Формирователь ПК и магистрали | Y1 | **Chép PARTIAL 2026-10-25:** dataset `ric10_*` (82 ref BOM, net 115 dòng — 53 truy trực tiếp/62 placeholder do khối lượng lớn, bảng `П3` 48 dòng + 2 bảng phụ `П3-right-1/2` chưa rõ designator). `check_ric10.py` PASS. Chưa xác nhận 100% tờ 1 (tr.179) và tờ 2 (tờ #75) là cùng một bản vẽ — xem `ric10_mota.md` | 181–183 (#176–#178) |
| 11 | Плата согласования | Y7 | 184 (#180) | 185 (#179) |
| 12 | Преобразователь РК II | Y15 | **Chép PARTIAL 2026-10-25:** dùng chung ảnh `A313-3_CONTROL/Y14/RE_tr188_a184.jpg` (byte-identical ở Y15) với Y14; dataset `ric12_13_*`: BOM 42 ref, net 92 dòng (51 truy trực tiếp, 41 placeholder, checker PASS), bảng đầu nối П1 43 dòng. Khối У3-2/3/4 bị gạch chéo X (không lắp), У3-1 riêng phục vụ "Исправн" | 187 (#183) |
| 13 | Преобразователь РК I | Y14 | như trên — cùng dataset `ric12_13_*`; mã viết tay đọc được trên ảnh phụ (Y15) là "ВШ2.068.054 Э3" | #181 (số viết tay «185» trùng #179) |
| 14 | (mux vào; dùng chung cho Y12/Y13 theo xác nhận người dùng) | Y12/Y13 | **Ảnh chụp lại rõ 2026-10-25:** tr.189 `A313-3_CONTROL/Y13/RE_tr189_a268.jpg` + bản sao tại Y12; mã ghi trên ảnh ЕУ3.628.121 Э3. Chép PARTIAL (mở rộng 2026-10-25): `ric14_bom.csv` 26 ref; `ric14_net.csv` 111 dòng (90 truy trực tiếp, 21 placeholder, `check_ric14.py` PASS); bảng `Контакт / Цепь` trong `ric14_conn.csv` 37 dòng (1–34, 35/A/B) đã chốt đủ. Vùng chưa truy: Я1-3 chân 9–16 (vết ố/nếp gấp giấy thật), phần lớn У4 và У1/У3 (giới hạn thời gian của subagent, không phải giới hạn ảnh) | ПЭ riêng chưa thấy; BOM sơ bộ đã có trong `ric14_bom.csv` |
| 15 | Интегратор | Y9 | **XÁC ĐỊNH 2026-10-24: `A313-3_CONTROL/Y9/RE_tr191_a265.jpg`**, mã viết tay "ЕУ3.072.043 Э3" (đọc là "04373", "Э3" dễ nhầm "73"), trang 191 ngay trước ПЭ | 192–196 (#189–#193) |
| 16 | Преобразователь | Y8 | 197 (#195/#196/**#199 nét nhất**) | 198–201 (#200–#203) |
| 17 | (chuyển mạch ra, Выход 1а…24а) | Y11 | **ẢNH THAY 2026-10-24 (rõ nét, đủ cả tờ): `A313-3_CONTROL/Y11/RE_tr202_a266.jpg` (л.1/2, mã ЕУ2.242.113), `RE_tr203_a267.jpg` (л.2/2)** | 204–205 (#206, #207) |
| 18 | Усилители выходные (ЕУ2.032.463 Э3, 1 tờ) | Y10 | 206 (#208, nét nhất; ảnh chụp lại trong `A313-3_CONTROL/Y10/` để đối chiếu) — **ĐÃ CHÉP 2026-10-25** (`ric18_*`) | 207–208 (#209, #210) |
| 19 | Плата контроля и сигнализации | Y24 | 209 (#211) | 210–213 (#212–#214) |
| 20 | УЛП +20 В; 0,3 А | Y18 | 214 (#215) | 215–217 (#216–#218) |
| 21 | УЛП 6,3 В; 0,5 А | Y20 | 218 (#219) | 219 (#220) |
| 22 | УЛП минус 20 В; 0,3 А (ЕУ3.215.451 Э3; khối lắp −02 = −23 В) | Y21 | 221 (#221); **chụp lại rõ 2026-10-25: `A313-3_CONTROL/Y21/RE_tr221_a270.jpg`** (xác nhận chấm nối lá 7 ↔ C5…C8) | #222 (+ tr.222 thiếu?), 223–224 |
| 23 | УЛП 12,6 В; 1 А (ЕУ3.215.452 Э3) | Y19 | 225 (#225) | 226–227 |
| 24 | УЛП ±10 В; 0,2 А (ЕУ3.215.466 Э3) | Y23 | 228 (#228) | 229–230 |
| 25 | УЛП 5 В; 15 А (ЕУ3.215.469 Э3) | Y17 | **Chụp lại rõ 2026-10-25:** `A313-3_CONTROL/Y17/RE_tr231_a269.jpg` thay ảnh cũ #233 (mờ/gập góc, đã xoá). Soát lại `ric25_*` bằng ảnh mới: xác nhận Д3/Д4 (trong перечень) THỰC SỰ không vẽ trên trang này; sửa hướng mũi tên T24 (NPN, trước đọc nhầm từ ảnh mờ); xác nhận R16/R17, Д23, Д34…Д40. netlist vẫn 397 dòng, 5 dòng `?` còn lại (node "шина M", do chưa rõ mạch chứ không phải ảnh mờ) | 232–236 (#234–#238) |
| 26 | УЛП минус 12,6 В; 1 А (ЕУ3.215.470 Э3) | Y22 | 237 (#239) | 239 (#241); 238 thiếu |
| 27 | Плата согласования, lắp ráp (ВШ3.031.020 Д7) | Y7 | 241 (#242) | — |
| — | Lắp ráp khác; УЛП 5 В 15 А (ВШ6.730.530 Д7) | Y17 | 244–247 (#245–#249) | — |

Hệ quả: Hình 21 và 24 (vắng trong mục lục bản dịch PDF) **có** trên bản giấy; рис.13 = РК I (Y14)
xác nhận chỗ «Hình 13?» trong kế hoạch.

## 3. Ảnh trùng, ảnh hỏng

* Chụp lặp cùng trang: tr.52 (#46, #47) · tr.141 (#134, #135) · tr.197 (#195, #196, #199 — dùng #199) ·
  рис.6 tờ 1 (#231, #232). **Sửa 2026-10-24:** #155/#156 là рис.5 (Y4) tờ 1/2, không thuộc рис.6 (khớp ПЭ рис.5: R5–R8, C7, C8).
* Nhóm trùng do dhash báo sai: G003 (#235 = tr.233, #241 = tr.239 — hai trang ПЭ khác nhau).
* Không phải trang sách: #185 (đồng hồ), #194 (chụp hỏng), #197/#198 (ổ cắm 27 V), #240 (sàn).

## 4. Cần chụp bổ sung (theo ưu tiên) — rà lại 2026-10-25

Căn cứ: `tmp/pdfs/review/a313-3/k3_anh_mo.py` (độ nét, kích thước ảnh từng tấm, số dòng `?`/placeholder trong
`ricNN_net.csv`) và mục «chỗ chưa chắc» của từng `ricNN_mota.md`. Chỉ ghi những chỗ **nguyên nhân là ảnh**
(cắt mép, nếp gấp, vết ố, phân giải thấp, chưa có trang); `?` do chưa hiểu mạch hoặc do người chép chưa lần hết
thì không cần chụp lại. Cách chụp chung: mở phẳng, chụp thẳng góc, **từng nửa chồng lấn ~20 %** cộng một ảnh khung tên.

### 4.1. Sơ đồ Э3 cần chụp lại

| Ưu tiên | Tấm / рис. | Ảnh đang dùng | Vấn đề do ảnh | Cần chụp |
|---|---|---|---|---|
| 1 | Y1 / рис.10 | `Y1/RE_tr179_a175.jpg`, `Y1/RE_trXXX_a075.jpg` (ảnh cũ) | Mép phải tờ 2 bị cắt (bảng `П3-right-1/2` cụt chữ, mất designator); mép trên bị nếp giấy che; cụm chéo У1/У2/У14/У15/У17 tờ 1 nét cách nhau < 10 px; số ref У47…У56 nhoè. Net 115 dòng: 58 `?`, 62 placeholder | Cả hai tờ, từng nửa, gần hơn; một ảnh riêng mép phải tờ 2 có khung bảng đầu nối |
| 2 | Y2 / рис.9 | `Y2/RE_tr175_a171.jpg`, `RE_tr176_a172.jpg` (ảnh cũ) | Tờ gấp chụp một phần, mất khung tên/mã bản vẽ. Net 489 dòng: 106 `?` | Cả hai tờ + khung tên. (BOM `name = ?` là do chưa dùng ПЭ tr.177–178 đã có, không cần chụp) |
| 3 | Y6 / рис.7 л.2, л.3 | `Y6/RE_trXXX_a256.jpg`, `a257.jpg` (chỉ 1536×2048) | Phân giải thấp; mép dưới л.1 và góc dưới phải л.3 bị cắt/mờ. Net 997 dòng: 188 `?` | л.2, л.3 độ phân giải cao (như a255); mép dưới л.1 |
| 4 | Y11 / рис.17 | `Y11/RE_tr202_a266.jpg`, `RE_tr203_a267.jpg` | Bảng Я1 và Я4 đọc ra giống hệt (nghi nhầm bảng xếp liền); nhãn Я5 lẫn với Я2/Я4 do chụp nghiêng | Chụp thẳng, gần, riêng vùng bảng Я1…Я6 |
| 5 | Y12/Y13 / рис.14 | `Y13/RE_tr189_a268.jpg` | Vết ố/nếp gấp giấy thật cắt dải Я1-3 chân 9–16 ↔ У4…У6 | Ảnh gần dải đó, đèn chiếu xiên để giảm bóng nếp |
| 6 | Y9 / рис.15 | `Y9/RE_tr191_a265.jpg` (2560×1090) | Chữ viết tay bảng П1 quá nhỏ so với phân giải (П1/38 chưa đọc được; dòng B=54 có thể ngoài khung) | Ảnh gần bảng П1 |
| 7 | Y3 / рис.6 tờ 1 | `Y3/RE_trXXX_a252.jpg` (1536×2048) | Phân giải thấp hơn tờ 2/3. Còn 95 chân «НЕ ПРОСЛЕЖЕНО» chủ yếu ở các thanh dọc tờ 2/3 (ảnh a253/a254 đã rõ, hạn chế là mật độ nét) | Tờ 1 phân giải cao; nếu cần, ảnh gần các thanh dọc tờ 2/3. Bổ sung bằng đo thông mạch trên tấm |
| 8 | Y4 / рис.5 tờ 1 | `Y4/RE_tr158_a250.jpg` | Ghi chú 1–2 (chân 7/14 nối «а» hay «б») bị cắt ở mép ảnh | Ảnh mép chứa ghi chú 1–2 |
| 9 | Y18 / рис.20 | `Y18/RE_tr214_a273.jpg` | Khung tên/số «Рис.20» bị cắt (chỉ ảnh hưởng định danh, netlist đủ) | Ảnh khung tên |
| — | Y8 / рис.16 | `Y8/RE_tr197_a278.jpg` (Hermes đang chép) | File là **HEIC mang đuôi .jpg** — Pillow không mở được; nên đổi đuôi `.heic` hoặc xuất JPEG ra file mới | Đánh giá sau khi Hermes chép xong |

Không cần chụp lại sơ đồ: Y5, Y7, Y10, Y14/Y15, Y16, Y17, Y19…Y24 và bộ Э4 tr.142–152 (các `?` còn lại do
nội dung, không do ảnh).

### 4.2. Trang перечень (ПЭ) chưa có ảnh

| Trang | Thuộc | Thiếu gì |
|---|---|---|
| 220 | ПЭ рис.21 (Y20) | Tên/loại C4…C11, Д1…Д5, Д7, Др1…Др3, Пр1; Т1…Т6, У1 mới đọc qua bóng chữ xuyên giấy |
| 238, 240 | ПЭ рис.26 (Y22) | Loại T4…T9 (cực tính hiện suy từ mũi tên). `RE_tr238_a240_x.jpg` là ảnh sàn, không phải trang 238 |
| 222 | ПЭ рис.22 (Y21) | Cần xác nhận có tồn tại (ảnh #222 «Лист 89» không có số trang viết tay) |
| 211 | ПЭ рис.19 (Y24) | ПЭ tr.210–213 mới có 3 ảnh (#212–#214) |
| 188–190 | nghi ПЭ рис.14 (Y12/Y13) | Chưa thấy ПЭ riêng; BOM `ric14` hiện chỉ sơ bộ |
| 234 | ПЭ рис.25 (Y17) | Đã có `RE_tr234_a236.jpg`; chụp lại rõ hơn chỉ khi cần soát cột «Кол.» lệch dòng (C53…C55) |

### 4.3. Trang chưa thấy khác (ưu tiên thấp)

Phần TO (có thể là hình gấp): 24, 27, 29, 37, 42, 111, 121, 135. Phần phụ lục: 180, 245, 246.
Tên dự kiến `RE_trNNN_a2xx.jpg`; không gán các trang này cho ảnh `trXXX` khi chưa có bằng chứng.
Phụ lục рис.1–4 (nếu có) cần kiểm trên bản giấy.

### 4.4. Đọc lại số trang

#75 (`RE_trXXX_a075.jpg`), #137 (`RE_trXXX_a137.jpg`), #138 (`RE_trXXX_a138.jpg`),
#139 (`RE_trXXX_a139.jpg`), #181 (`RE_trXXX_a181.jpg`), #184 (`RE_trXXX_a184.jpg`),
#187 (`RE_trXXX_a187.heic`), #188 (`RE_trXXX_a188.heic`), #222 (`RE_trXXX_a222.jpg`),
#231 (`RE_trXXX_a231.heic`), #246 (`RE_trXXX_a246.heic`), #247 (`RE_trXXX_a247.jpg`),
#249 (`RE_trXXX_a249.jpg`).

## 5. Ảnh chụp bổ sung (lưu trong `A313-3_CONTROL/`, không chép vào thư mục RE)

| Số | File | Hình / tờ | Thay cho |
|---|---|---|---|
| a250 | `A313-3_CONTROL/Y4/RE_tr158_a250.jpg` | рис.5 (Y4) tờ 1/2 | #155 |
| a251 | `A313-3_CONTROL/Y4/RE_tr159_a251.jpg` | рис.5 (Y4) tờ 2/2 — ? số viết tay đọc giống «189» | #156 |
| a252 | `A313-3_CONTROL/Y3/RE_trXXX_a252.jpg` | рис.6 (Y3) tờ 1/3 | #231, #232 |
| a253 | `A313-3_CONTROL/Y3/RE_tr160_a253.jpg` | рис.6 (Y3) tờ 2/3 | #157 |
| a254 | `A313-3_CONTROL/Y3/RE_tr161_a254.jpg` | рис.6 (Y3) tờ 3/3 | #158 |
| a268 | `A313-3_CONTROL/Y13/RE_tr189_a268.jpg` + bản sao `A313-3_CONTROL/Y12/RE_tr189_a268.jpg` | Sơ đồ chung Y12/Y13 theo xác nhận người dùng; trang tay 189, mã trên ảnh ЕУ3.628.121 Э3 | thay nguồn cũ #186/#187 cho việc chép sơ đồ |

Ảnh chụp phẳng, đủ mép và khung, độ phân giải 1926×2568 (a252: 1536×2048). Bản cũ #155–#158, #231, #232 vẫn giữ
trong thư mục RE (chỉ xoá bản sao trong `A313-3_CONTROL/Y3/`).

Bổ sung 2026-10-25:

| Số | File | Hình / tờ | Thay cho |
|---|---|---|---|
| a270 | `A313-3_CONTROL/Y21/RE_tr221_a270.jpg` | рис.22 (Y21) | #221 |

Bổ sung 2026-10-25 (đổi tên ảnh chụp lại 1792…; bản sao RE cũ trong thư mục tấm đã xoá, bản gốc vẫn ở `ЕУ.048.002.РЭ(A313-3)/`):

| Số | File | Hình / tờ | Thay cho |
|---|---|---|---|
| a271 | `A313-3_CONTROL/Y10/RE_tr206_a271.jpg` | рис.18 (Y10) | — (ảnh đối chiếu; giữ #208 làm nguồn chính vì phân giải cao hơn) |
| a272 | `A313-3_CONTROL/Y15/RE_tr188_a272.jpg` | рис.12/13 (Y14/Y15) | #184 (bản sao trong Y15 đã xoá; Y14 vẫn giữ) |
| a273 | `A313-3_CONTROL/Y18/RE_tr214_a273.jpg` | рис.20 (Y18) | #215 |
| a274 | `A313-3_CONTROL/Y20/RE_tr218_a274.jpg` | рис.21 (Y20) | #219 |
| a275 | `A313-3_CONTROL/Y22/RE_tr237_a275.jpg` | рис.26 (Y22) | #239 |
| a276 | `A313-3_CONTROL/Y23/RE_tr228_a276.jpg` | рис.24 (Y23) | #228 |
| a277 | `A313-3_CONTROL/Y24/RE_tr209_a277.jpg` | рис.19 (Y24) | #211 |
