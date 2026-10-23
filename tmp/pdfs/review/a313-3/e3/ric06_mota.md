# Рис.6 — Устройство управления обращением (У3) của A-313-3, ЕУ3.057.136 Э3

Người chép: Claude (Codex từ chối nhiệm vụ này, xem `codex-runs/T04-ric06-y3/r2`). Ngày 2026-10-22.
Dữ liệu sinh lại bằng `ric06_gen.py` (bản đọc tay mã hoá trong script) → `ric06_bom.csv`, `ric06_conn.csv`,
`ric06_net.csv`. Kiểm: `e3_check.py` (рис.6 ghi ở KNOWN), `e3_vs_e4.py 6 У3` → `ric06_vs_e4.csv`.

**Trạng thái: CHÉP MỘT PHẦN.** Netlist chưa đủ tin cậy để đấu dây hay làm đồ gá. 818 chân, trong đó
166 chân «НЕ ПРОСЛЕЖЕНО» (thấy chân trên Э3 nhưng chưa lần chắc đường nối); 213 dòng có `?`.

## 1. Nguồn và định danh tờ

| Ảnh | Nội dung | Căn cứ định danh |
|---|---|---|
| #232 (`RE_trXXX_a232.jpg`) | **Tờ 1/3**: bảng đầu nối П1/П2/П3, giải mã У1/У64 → У9 → Т1–Т4пр., đệm СИ, C1–C6, ghi chú 1–2 | Khung tên «Рис.6 (лист I из 3) ЕУ3.057.136 Э3» |
| #157 (`RE_tr160_a157.jpg`, trang tay 160) | **Tờ 2**: trigger У16–У18, đệm 109ЛИ1 У21–У28 + R14–R35, У29–У44, У66 | «Начало см. на листе 1 / Продолжение на листе 3»; R14–R35, R9 khớp ПЭ |
| #158 (`RE_tr161_a158.jpg`, trang tay 161) | **Tờ 3**: К1–К4, Т1–Т4, t1–t4, R1–R4 + РА АЦИ, КША7–КША15 | «Начало см. на листе 2»; R1–R4 khớp ПЭ |
| #159, #160 | ПЭ trang 162, 163 | Tiêu đề «…устройства управления обращением (рис.6)» |

**Nghi vấn về danh mục ảnh:** `DANH-MUC_ANH_RE_A-313-3.md` §2 xếp #155–#158 cho рис.6. Nhưng #155 có C7, C8,
R11 và #156 có R5–R8, «Пр1» — **ПЭ рис.6 không có R5–R8, C7, C8**. Vậy #155/#156 nhiều khả năng **không thuộc
рис.6** (có thể là рис.7 hoặc hình khác). Chưa sửa danh mục; cần người dùng đối chiếu bản giấy.

## 2. Danh mục linh kiện (ПЭ #159/#160) — 99 ref

R1–R4, R9, R26–R35: С2-23-0,125-1 kΩ ±10 %; R10–R25: С2-23-0,125-24 Ω ±5 %; C1–C5: КМ-6-А-Н50-0,015 µF;
63 vi mạch У1–У36, У38–У52, У54–У64, У66 (họ 133/136, 109ЛИ1). **Không có R5–R8, У37, У53, У65.**

Khớp chéo Э3 ↔ ПЭ: **У37 (tờ 2) và У53 (tờ 3) bị gạch chéo trên Э3** — đúng là ПЭ không có. У36-1 cũng bị gạch
(chỉ dùng У36-2).

## 3. Bảng đầu nối tờ 1 ↔ Э4 (У3П1/П2/П3, `e4/p151.csv`)

`e3_vs_e4.py 6 У3`: **125 khớp / 32 lệch tên / 1 chỉ Э3 / 9 chỉ Э4** (176 hàng bảng, П3/70 bị mép ảnh cắt).

Phần lớn "lệch tên" là cách ghi, không phải khác tín hiệu: `→`↔`⇒`, «Зп» (chữ З) ↔ «3п» (số 3), viết tắt
(«Импульс счета»↔«ИМП.СЧЕТА», «Програм.кон.»↔«ПРОГР.КАНАЛ»). Không đổi hàm chuẩn hoá để giữ nguyên kết quả
рис.8/рис.11. Khác biệt **thật** cần xem bản giấy/tấm:

| Chân | Э3 (tờ 1) | Э4 | Ghi chú |
|---|---|---|---|
| П1/41–43, П3/21–23 | trống | М13, М14, М15 | Э3 để trống ô |
| П3/30 | «Корпус» (sửa tay, «СчК→М» bị gạch) | «Сч.К⇒М» | Э4 giữ tên gốc; tờ 2/3 cũng gạch «СчК→М» sửa «Корпус» |
| П2/40, 52, 53 | gạch xoá («АЗИ», «35И», «36И») | «АИ», «3БИ», «2БИ» | |
| П2/6–14 | «КША7»… | «КША-7р»… | Э4 có hậu tố «-р» |
| П2/31–34 | đọc «7РА АЦИ»… | «7р АЦИ»… | ? chữ viết tay «РА»/«р» chưa phân định |
| П3/29 | «18рСчК» (?) | trống | |
| П3/3 | «1t16» (?) | «1t16» khớp | chữ nhỏ |

## 4. Cấu trúc đã đọc chắc

* **Tờ 1:** У64 (2 cổng đảo) + У1 giải mã 2→4 từ П3/61 (1рСчК), П3/62 (2рСчК) — đã lần từng chấm nối:
  У1.1,4 = A; У1.2,10 = B; У1.9,12 = Ā; У1.5,13 = B̄ → У9 đảo → П1/49–52 (Т1–Т4пр.).
  П3/68 (СИ) → У20 đảo → hai phần tử 6 vào ra 8 → R10/R11 (24 Ω) → П2/4, П2/5 (СИ2-1/2) và R12/R13 → П2/2, П2/3
  (СИ1-1/2); R26/R27 1 kΩ xuống Корпус. C1–C5 lọc «a»–«б»; C6 (có cực, + ở «б») — **không có trong ПЭ**.
* **Tờ 2:** 8 tầng đệm 109ЛИ1 (vào 1–6 chung, ra 8) qua R 24 Ω ra П2 (СВК/СПК/СВКЦИ) và R 1 kΩ xuống Корпус;
  nguồn vào từ trigger У16–У18 (D lấy từ 7оп, 1оп, 6оп, 2оп, 5оп) qua У19/У20. Cột ra: У39/У40/У41 đảo các thanh
  ~М→РМ, ~М→РгК1/2, ~М→РК1/2, ~М→СчД, ~СчД→М, ~РгПр→М ra П2/П3; tên thanh khớp nhãn chuyển tờ hai chiều
  (vd. tờ 2 «У59/1(3)» ↔ tờ 3 «У32/8(2)» vào У59.1). У40.11 → «П1/17 М→СчД» **bị gạch xoá**.
* **Tờ 3:** ba bộ dồn kênh 136ЛР1 (У2, У3, У5-1/2) chọn giữa «рСчК» và «рРгК» → đảo → giải mã 2→4 (У10/У11/У12)
  → đảo (У13/У14/У15) → К1–К4 (П2/35–38), Т1–Т4 (П3/31–34), t1–t4 (П1/19–22). Khối t1–t4 đã lần chấm nối trên ảnh
  phóng to. R1–R4 1 kΩ kéo lên «б» các đường РА АЦИ (П2/31–34) vào У45 → У50 → У55 → КША7/8; KША9–15 qua
  У51/У52/У56, У54/У57, У58/У59/У63, У60/У61/У62. Nhãn vào У60.6 «14РА3», У61.6 «15РА3» **bị gạch xoá**.

## 5. Chưa chắc (bảng tóm tắt; chi tiết từng chân ở cột note của `ric06_net.csv`)

| Loại | Chân | Lý do |
|---|---|---|
| Ký hiệu trùng | «У15», «У16» tờ 1 (ghi `У15?т1`, `У16?т1`) | Nhãn đọc rõ nhưng У15 (133ЛА3) và У16 (136ТМ2) đã dùng ở tờ 3/2; phần tử vẽ 6 vào ra 8 (giống 109ЛИ1) |
| Ký hiệu trùng | «У5-4» tờ 3 (ghi `У5-4?`) | У5 là 136ЛР1, chân 13 đã dùng ở У5-2 |
| Thanh dọc | S/C/R của У16–У18; chân chọn của У2/У3/У5; vào У10/У11; nhiều vào У31–У36, У38, У42–У62 | Đường dọc dày song song, chưa thấy chắc chấm nối |
| Nhãn số chân | «П3/69(1) 7оп», «П3/51(1) 1оп» | Chữ số viết tay; net lấy số chân theo **tên tín hiệu** trong bảng tờ 1 (7оп = П3/59, 1оп = П3/57) |
| Nguồn ~0рСчК | phần tử «У8-4» tờ 2 ↔ nhãn tờ 3 «У19/11(2)» | Hai nơi ghi khác nhau |
| Bộ chân 7/14 | mọi vi mạch | Theo ghi chú 1–2 tờ 1; với 109ЛИ1 chưa kiểm sơ đồ chân vỏ |

## 6. Việc tiếp theo

1. Chụp lại tờ 2 và tờ 3 rõ hơn (mở phẳng, từng nửa có chồng lấn) để lần các thanh dọc; đo thông mạch trên tấm У3.
2. Đối chiếu #155/#156 với bản giấy để xác định thuộc hình nào; sửa danh mục ảnh khi người dùng duyệt.
3. Kiểm sơ đồ chân vỏ 109ЛИ1 trước khi dùng giả định chân 7/14.
