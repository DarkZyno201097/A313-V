# PHẦN NGUỒN A-313-3 — Э3 các УЛП (рис.20–26) và tấm kiểm tra У24 (рис.19)

Nguồn: ảnh bản giấy ЕУ3.048.002 РЭ, Phụ lục tr.209–239 (tra ảnh trong `DANH-MUC_ANH_RE_A-313-3.md`).
Bản chép trong `tmp/pdfs/review/a313-3/e3/`: mỗi hình có `ricNN_bom.csv` (`ref,name,qty,page,note`),
`ricNN_net.csv` (`ref,pin,net,note`; net `X:n …` là chân đầu cắm của khối), `ricNN_mota.md` (nguyên lý, công thức
áp ra theo trị số trên bản vẽ, điểm đo, quy trình cấp điện thử, danh sách «Chưa chắc / thiếu»).

Kiểm chứng: `python tmp/pdfs/review/a313-3/e3/e3_check.py` — mọi ký hiệu trong netlist có trong перечень và
ngược lại, không chân trùng, mọi net nội bộ ≥ 2 chân; ngoại lệ đã biết: рис.19 Д7, рис.25 R28/Д3/Д4.
Các trị số danh định: `e3_ric19_tinh.py`, `ric_check.py` (рис.20/21), `e3_ric2223.py`, `e3_check.py` (рис.24/26),
`ric25_tinh.py`.

> ⚠ Netlist chép bằng mắt từ ảnh bản photocopy. Trước khi dùng để sửa: đo thông mạch các chỗ ghi «suy ra» trong
> cột `note`. Không tin công thức áp ra khi chưa đo trị số thật của biến trở/linh kiện chọn (`*`).

## 1. Tóm tắt từng khối

| Рис. | Khối | Số hiệu | Kiểu | Phần tử chính | Linh kiện / chân | Thiếu |
|---|---|---|---|---|---|---|
| 19 | У24 Плата контроля и сигнализации | ЕУ2.072.139 | so sánh 10 ray + giám sát 27 V | 6 × 140УД1Б, 4 ma trận diode, chuẩn ±9 V (2 × Д818Д), chuỗi tự giữ T2→T4 | 111 / 290 | **tr.211** (trị số R24…R51) |
| 20 | У18 УЛП +20 В 0,3 А | ЕУ3.215.446 | xung hạ áp tự dao động | khoá П701А + 2Т608Б, 140УД1А, chuẩn Д818Д, hạn dòng T6 qua R(Др3) | 44 / 98 | — |
| 21 | У20 УЛП +6,3 В 0,5 А | ЕУ3.215.448-01 | xung hạ áp | như рис.20, chuẩn nuôi từ 27 V, Д5 kẹp ra | 46 / 102 | **tr.220** (C4…C11, Д1…Д7, Др1…3, Пр1) |
| 22 | У21 УЛП −20 В 0,3 А | ЕУ3.215.451 | xung đảo cực tự dao động | Darlington T7/T6, đa hài T1/T4, vi sai T2/T3, Д818Д, hạn dòng T9 | 43 / 99 | tr.220 (tr.221 đủ) |
| 23 | У19 УЛП +12,6 В 1 А | ЕУ3.215.452 | xung hạ áp | 2Т803А, 140УД1А, hạn dòng T6, kẹp quá áp 2 × Д814А | 50 / 113 | — |
| 24 | У23 УЛП ±10 В 0,2 А (+ −5 В, +3,5 В) | ЕУ3.215.466 | 4 ổn áp tuyến tính | 2Т904А (−5 В), Darlington (+10 В), T7…T10 (−10 В), lặp emitter T11 (+3,5 В) | 40 / 95 | — |
| 25 | У17 УЛП 5 В 15 А (+ −6,3 В 1 А, ~5 В 400 Гц) | ЕУ3.215.469 | buck 5 В + buck-boost −6,3 В + biến áp | 4 × 2Т803А, 14 × Д817А thuận làm diode thoát, crowbar 2У202И, **Тр1 ТН-12-40-400** | 164 / 397 | góc trên-trái ảnh #233 bị che (Д3, Д4, R28?) |
| 26 | У22 УЛП −12,6 В 1 А | ЕУ3.215.470 | xung đảo cực | như рис.22; đa hài T1/T4, vi sai П307В | 47 / 106 | **tr.238** (trị số R1…R18), **tr.240** (loại T4…T9) |

Đầu cắm УЛП (5 chân, trừ У23 và У17): 1 УПРАВЛЕНИЕ, 2 lối ra, 3–4 КОРПУС, 5 +27 В ВХ. Chân 1 nối vào nút chuẩn:
chập xuống КОРПУС thì tắt (рис.20, 23) hoặc chỉ hạ áp (рис.22: còn ≈ 15,2 V) — đây là đường 3Ш7/26…32
«УПР.(…)» của bàn kiểm tra.

## 2. Phát hiện chính

* **Nguồn gốc ~5 В 400 Гц (CLAUDE.md §4.6) — đã rõ với khối Nga:** biến áp **Тр1 ТН-12-40-400 nằm trên chính
  khối У17** (рис.25): sơ cấp ~36 В 400 Гц pha С (3Ш5/25, qua cầu chì Пр2 0,5 А) và pha А (3Ш5/33), lấy từ máy bay
  3Ш4/56 và 3Ш4/55; thứ cấp ~5 В ra 3Ш5/11 (Ф.С) và 3Ш5/12 (Ф.А); Ф.А → У16КП2/49 → Вход 12 của mux vào У12
  (Э4 tr.142/145; chân 11/12 nằm trên nếp gấp — Ф.С có vẻ về КОРПУС). Tấm nào tạo `УПР.МОД` từ đây thì chưa lần. A313-V làm tương đương bằng biến thế trên sát-xi + chân 3Ш3В/55 «Uоп ~5В» (A-313-3 để trống chân này).
* **У24 không có rơ-le, không có đèn.** «K1…K6», «Y1…Y10» trong HDSD tiếng Việt là ký hiệu bộ so sánh trên sơ đồ
  chức năng và У1…У10 (ma trận diode + 140УД1Б).
* **Mâu thuẫn Э4 ↔ Э3 ở У24:** chân 2 Э4 ghi «ВКЛ.», Э3 ghi «КОНТР. −5В»; chân 4 Э4 «ОТКЛ.», Э3 «ИСПОЛН. УСТР-ВО».
  Bản Э3 giải thích được dòng У23/2 «−5В» → У24/2 (Э4). Cần đo trên khối.
* **У21:** bản vẽ là bản gốc −20 В (ЕУ3.215.451); khối lắp biến thể **-02 (−23 В; 0,25 А)** theo HDSD — chưa có
  tài liệu bản -02.
* **У20:** bảng đầu cắm trên Э3 ghi lối ra «+5 В», tiêu đề và перечень ghi 6,3 В; Э4 cấp «КОНТР. +6,3В» ⇒ chỉnh
  6,3 В.
* Tr.207–208 (ảnh #209/#210) là перечень **рис.18 «Усилители выходные»** (У10), không phải рис.19.

## 3. Cần chốt trên phần cứng hoặc chụp bổ sung

| # | Việc | Khối | Cách chốt |
|---|---|---|---|
| N1 | R11 in «680 кОм 1 Вт» — với trị này Д3/У1 chỉ được ~16 µA, mạch không chạy; nghi 680 Ω | У18 | đo R11 nguội |
| N2 | T9 emitter vào ray âm: không có chấm nối trên bản vẽ | У21 | đo thông mạch |
| N3 | Cầu chì Пр1: bản vẽ «1А», перечень «2А» | У21 | xem nhãn trên khối |
| N4 | Nhánh +3,5 В: với R18 = R19 = 220 Ω chỉ ra ≈ 2,5 V; chân 8 bản vẽ «+6,3 В вх.», Э4 «5В ВХ» | У23 | đo R18/R19 và áp chân 8 |
| N5 | B/E của T9, T10 vẽ chung net với E của T8 (R22 bị nối tắt) — vô lý | У17 | đo R(б-э) T9, T10 |
| N6 | Cụm T24/Д23/R49/C43 không ra chiều dòng hợp lý | У17 | xem mạch in |
| N7 | 7 chỗ nối không rõ trên У24 (R17/Д3 về mát, chân 4 của У5…У8, R22/R23, base T7, R37/R41, T1–R27 nét chấm, У9 chân 7 nối thẳng +27 V) | У24 | đo thông mạch |
| N8 | Điện trở dây Др3 (cảm biến hạn dòng) — quyết định ngưỡng bảo vệ | У18, У19, У20, У21, У22 | đo bằng milli-ohm kế |
| N9 | Chụp lại: **tr.211, 220, 238, 240**; góc trên-trái ảnh #233 (tờ gập che) | — | chụp bổ sung |
| N10 | Biến thể ЕУ3.215.451-02 (−23 В) khác bản −20 В ở đâu | У21 | so linh kiện trên khối với ric22_bom.csv |
