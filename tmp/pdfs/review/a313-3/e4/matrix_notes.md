# Ma trận nối tấm У16 «Плата коммутационная» — Э3 RIÊNG của Y16 (ЕУ3.661.064), tr.153–157

**SỬA 2026-10-24:** tài liệu này KHÔNG phải Э4 (đã nhầm trước đây) — khung tên viết tay trên ảnh
gốc (chụp lại rõ 2026-10-24, xem `A313-3_CONTROL/Y16/E3_matran_lis1-5_recapture-2026-10-24.jpg`)
ghi rõ **"ЕУ3.661.064 Э3 л.N/5"**. Đây là sơ đồ RIÊNG của Y16 (ma trận cross-reference, không vẽ
linh kiện vì Y16 không có linh kiện), KHÔNG PHẢI một phần của `ЕУ3.048.002 Э4` "Sơ đồ đấu nối khối"
(tài liệu đó là tr.142-152, 11 lист riêng — xem `A313-3_CONTROL/KHOI_So-do-dau-noi/`).

Nguồn: ảnh #150–#154 (`kiemke.csv`), bản giấy ЕУ3.048.002 РЭ, chụp điện thoại (ảnh gốc chỉ đọc).
Chép bằng mắt từ ảnh phóng to (`k3_crop.py`), dữ liệu và kiểm chéo nằm trong script
`tmp/pdfs/review/a313-3/e4_matrix.py` (chạy từ gốc repo, sinh lại hai CSV và in kết quả kiểm chéo).

* `p153_157_matrix.csv` — mỗi dòng là một điểm cắt có ghi số chân (622 dòng).
* `matrix_nets.csv` — mỗi dòng là một cột dọc (282 cột, trong đó 4 cột trống), cột `note` gồm tên ở đầu cột
  và ghi chú.

## 1. Ma trận này là gì

Đây là **bảng nối dây điểm–điểm trên tấm nối mạch У16** giữa các đầu nối cắm tấm mạch của khối.

* **Đường ngang** = một đầu nối trên У16: `П1 … П15` (không có П6, П14). Kiểm bằng tên tín hiệu: `Пn` ≡
  bảng `У16КПn` ở tr.145–152 (ví dụ П9/2, /3, /4 = 2р, 1р, 0р Сч.К đúng như КП9; П5 = tích phân, П4 = khuếch
  đại ra). Tên tấm ghi bên trái, ngay trên đường của nó:
  П4 Усилители выходные (У10), П5 Интеграторы (У9), П7 Коммутатор выходной (У11),
  П8 Устр. управления преобразованием (У6), П9 Преобразователь цифровых сигналов (У2),
  П10 Плата согласования (У7), П11 Устр. управления обращением (У3), П12 Преобразователь (У8),
  П13 Устр. программного управления (У4), П15 Устр. командного управления (У5).
  П1, П2, П3 không ghi tên tấm; theo bảng tr.145 đó là các đầu nối ra bó dây/đầu cắm khối (КП1, КП2 94 chân, КП3).
* **Cột dọc** = một dây (một net). Ô đầu cột ghi **tên tín hiệu** (chữ có gạch trên = tín hiệu đảo, ghi `¬`).
* **Số ở điểm cắt** = **số chân trên đầu nối Пn** của đường ngang đó. Số viết ngay bên trái điểm cắt
  (tr.153–156 có chấm đen; tr.157 nhiều chỗ chỉ có số, chấm rất nhỏ).
* **Nét liền / nét đứt**: mọi cột đều kẻ nét đứt làm lưới dẫn; đoạn **nét liền** nối từ chân trên cùng đến
  chân dưới cùng của net = dây thật. Một cột chỉ có **một** số thì vẫn là nét đứt (9 cột: 1t17, 1t18,
  6р Рг.К2, Контакт R, Контакт С, 4 × ВНЕШН. ПРЕРЫВ.) — chân đó không nối sang tấm nào khác trên У16
  (có thể đi ra bó dây hoặc bỏ). Không thấy chú giải (легенда) nào trên 5 trang; cách hiểu trên suy từ hình
  vẽ và đã kiểm bằng tên tín hiệu (§3).
* **Móc ⊓** (chỉ tr.156): một chân thứ hai nằm cạnh cột, nối vào cột bằng nét gấp hình chữ U — cùng net
  (КП2/83+85 КОРПУС, КП2/50+92 +5В, КП2/2+94 và КП12/27+31 +12,6В, КП1/3+29 và КП12/36+39 −12,6В).
  Ghi `nối vào cột bằng móc ⊓` trong CSV.
* **Tên đầu cột bị gạch ngang** (bỏ khi chế tạo, khớp với ghi chú 3Ш2/28–31, 3Ш4/36–41 trong
  `SO-DO-DAU-NOI_E4_A-313-3.md`): ВНЕШН. ПРЕРЫВ. ×4 (tr.156, nét đứt, 1 chân), và ở tr.153: Запрос А1/А2, АИ,
  36И, 35И, АИ, «И-3мкс», «Отв.А» — **các cột này vẫn có nét liền và 2 chân**. Chưa rõ dây có thực sự bỏ không.

## 2. Nối tiếp giữa các tờ

Năm trang là 5 «лист» của cùng một bảng, cùng thứ tự đường ngang П1…П15:
tr.153 (лист 1, phải: «Продолжение см. на листе 2») → tr.154 (trái «Начало см. на листе 1», phải «…листе 3»)
→ tr.155 (trái «Начало см. на листе …», số tờ không đọc rõ trên ảnh) → tr.156 (phải «Продолжение см. на листе 5») → tr.157 (trái «Начало
см. на листе 4»). Không có cột nào vắt qua hai tờ; mỗi tờ là một nhóm cột độc lập.
Nội dung theo tờ: tr.153 bus Рг К2 / Сч.К / строб / СПК / F / t / К (56 cột); tr.154 АЦП, СВК, КША, 80 кГц,
СИ, Сч.К 5–12р, Т1–Т4, 1t (56); tr.155 РК1–РК32 (КП2 → КП15), КПА, kiểm tra (57); tr.156 **nguồn và mát**
(thanh cái nhiều điểm) + điều khiển РПР/РМ/t/T/К (57, có 4 ô đầu cột trống); tr.157 tích phân, vào К1–К3,
ra 1а…8б «=» và «⊓⊔», ~5В 400Гц, УПР.МОД 1/2 (56).

## 3. Kiểm chéo với bảng У16КПn (e4_all.csv)

278 net có chân (282 cột − 4 cột trống), 622 chân. Lấy tên tín hiệu của từng chân trong bảng `У16КПn` rồi so:

* **252 net**: tên ở mọi chân khớp nhau (so sau chuẩn hoá + so mờ ≥ 0,8).
* **9 net**: cùng tín hiệu, chỉ khác cách viết — СИ / СИ1-1 (153-c09), «F1» / «ВХОД F1» ×4, «16рСчК» /
  «И-3мкс (6р Сч.К)» (đầu cột ghi cả hai), СВК / СВН цп-1, ИСПРАВНОСТЬ / ¬ИСПРАВН., УПР.Ф / УПР.ФУНК.
  ⇒ coi là khớp: **261/278**.
* **11 net**: bảng КП để trống tên ở một chân nên không so được: КП3/37, 12, 38, 11, 36, 10 (đúng các cột tr.153
  bị gạch tên), КП1/32–35 (ВНЕШН. ПРЕРЫВ.), КП2/24 (ОБЩ. ПРОВОДА).
* **2 net** nghi **chép sai trong e4**: КП11/48 ghi «К⇒РН» (ma trận + КП8/48: М⇒РМ); КП11/21 ghi «¬СВНвх»
  (ma trận + КП3/26: СВК БК).
* **2 net** khác tên thật giữa hai bảng: КП7/41 «ВХОД а» ↔ КП12/38 «"а" ПР», КП7/6 «ВХОД б» ↔ КП12/12
  «"б" ПР» — có thể cùng dây mang hai tên theo tấm, cần sơ đồ У11/У8.
* **2 net mâu thuẫn**:
  - −20 В (156-c17): КП1/5 ghi «−23В», КП5/37, КП10/27, КП12/42 ghi «−20В» — đã biết (У21).
  - **Выход 2б ⊓⊔ (157-c40)**: ma trận ghi rõ **П3/23**, nhưng КП3/23 = СИм (đã dùng ở 154-c35), còn
    КП3/29 = ВЫХОД 2Б; dãy П3 ở tr.157 là 27, 28, 3, **23**, 4, 30, 5, 31… (quy luật n / n+26) ⇒ gần như chắc
    **lỗi bản vẽ, đúng là П3/29**. Đây là chân duy nhất bị dùng ở hai cột.

## 4. Chưa chắc / thiếu

* **5 số đọc chưa chắc** (cột `note` = «đọc chưa chắc»), cả 5 được chốt **nhờ bảng КП** nên với 5 net này
  kiểm chéo không độc lập:
  - 153-c27 АИ: П9/«45 hay 46» → 46 (dãy 49,48,47,**4?**,45,44…; КП9/46 = АИ).
  - 153-c46 РПР⇒М: П11/«12 hay 42» → 42 (П11/12 đã thuộc КША-13).
  - 154-c05 ¬Зп. ЦВУ: П11/«28 hay 23» → 28 (23 thuộc ¬СПК1-2; КП11/28 = ¬ЗП.УВВ). Đầu cột đọc «Зп. ЦВУ»,
    bảng ghi «Зп.УВВ» — chưa chốt chữ nào đúng.
  - 154-c13 Зп. КПА: П11/«43» nhoè.
  - 154-c54 ¬1t1: П13/«43 hay 45» → 43 (45 thuộc Т4).
* Tr.154 (ảnh #151) chụp nghiêng, giấy cong mạnh ở mép phải: các cột 50–56 cong, ghép cột ↔ chân ở П8/П13 dựa
  vào lần theo nét; đã khớp tên với КП8/КП13.
* Tr.153: nhiều chấm vẽ rỗng (o) thay vì đặc (П2/60, П9/14, П9/10, П11/12…); coi như chấm nối, không thấy
  khác biệt ý nghĩa.
* Tr.156 cạnh П5/48 (cột Вход б.) có nét nhỏ giống số «1», không có chấm — bỏ qua.
* Tr.156: 4 ô đầu cột trống (156-c09, c11, c14, c16) chỉ có nét đứt — giữ trong `matrix_nets.csv` cho đủ số cột.
* Không đọc được chú thích nối tiếp ở mép phải tr.155 và mép trái tr.156 (nằm ngoài khung ảnh/nếp gấp).
* Tiêu đề bảng (khung tên) không có trên 5 ảnh; tên «ma trận nối У16» là suy luận.
* Chưa kiểm chiều ngược: chân nào trong bảng КПn có tên tín hiệu nhưng **không** xuất hiện trong ma trận.
