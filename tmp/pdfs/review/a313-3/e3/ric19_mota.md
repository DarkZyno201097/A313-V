# У24 — Плата контроля и сигнализации ЕУ2.072.139 (рис.19) — mô tả theo sơ đồ chép tay

Nguồn: ảnh #211 (sơ đồ, trang 209, gấp), #212/#213/#214 (danh mục, trang 210/212/213).
Trang 211 (R24…R51) **không có ảnh**. Netlist: `ric19_net.csv`, danh mục: `ric19_bom.csv`.
Kiểm chéo: `e3_ric19_check.py`; tính dải ngưỡng: `e3_ric19_tinh.py`.
Ký hiệu chân: op-amp theo số in trên hình; 140УД1Б (vỏ 301.12-1, xem `Datasheet/02_140UD1B_…md`):
1 = −Uп, 4 = общий, 5 = ra, 7 = +Uп, 9 = IN−, 10 = IN+.

Ảnh #209/#210 (trang 207/208) **không thuộc рис.19**: đó là danh mục của **рис.18 «Усилители выходные»**
(R4…R36, C3…C13, У1…У20, ô «Ячейка усилителя» R1…R16 / УМ1…УМ16 kèm 2Т312Б/2Т203Б/140УД1Б).

## 1. Đầu nối (bảng «Конт./Цепь» vẽ trên sơ đồ)

| Chân | Tín hiệu | Hướng | Nối vào |
|---|---|---|---|
| 1 | КОРПУС | — | bus mát chung (cả hai nửa dương/âm nối qua dây biên trái) |
| 6 | +27 В ВХОД | vào (nguồn) | R10, R14, У9.7, R26, R29, R32, R33, R39, R43, C2 |
| 13 | КОНТР. +12,6 В | vào (đo + nguồn) | R3 (kênh đo) **và** +Uп của У6, У7, У8, У10, R40 |
| 7 | КОНТР. −12,6 В | vào (đo + nguồn) | R53 (kênh đo), R55 (nuôi Д19) **và** −Uп (chân 1) của У5…У10 |
| 11 / 14 / 15 / 12 | КОНТР. +5 / +6,3 / +10 / +20 В | vào | R5 / R1 / R2 / R4 |
| 2 / 3 / 5 / 9 | КОНТР. −5 / −6,3 / −10 / −20 В | vào | R46 / R51 / R52 / R54 |
| 8 | НАПР. ВЫШЕ НОРМ. | vào (từ A-313-12) | nút «quá áp» (Д6.к, Д17.к, R27, Д24, Д11.а) |
| 4 | ИСПОЛН. УСТР-ВО | **ra** (lệnh cắt) | cùng nút với chân 8 — do T4 kéo lên qua Д11 |
| 18 | НАПР. НИЖЕ НОРМЫ | vào (từ A-313-12) | nút «thấp áp» (Д5.к, Д21.к, R18, Д14) |
| 16 | ИСПР. ПИТ. ЦВУ | ra | T8.э (lặp emitơ, kẹp Д16 2С456А) |
| 10 | ИСПР. ПИТ. ППЗУ | ra | T9.к, kéo lên +27 qua R43 |
| 17 | ИСПР. ПИТ. | ra | T10.к, collector hở |

⚠ Khác với bảng nối dây khối (`e4/p143.csv`): ở đó chân 2 = «ВКЛ.», chân 4 = «ОТКЛ.».
Trên рис.19 chân 2 = **КОНТР. −5 В** (khớp У23/2 «−5 В → У24/2» trong p143) và chân 4 = **ИСПОЛН. УСТР-ВО**.
⇒ Ghi chú «расхождение» trong p143 được giải: chân 2 là đầu đo −5 В.

## 2. Khối chức năng

### 2.1. Chuẩn áp
* **Vref+ ≈ +9 В**: Д1 (Д818Д) nuôi qua R10 1,5 кОм 1 Вт từ +27 В — I ≈ 12,0 мА.
* **Vref− ≈ −9 В**: Д19 (Д818Д), katốt ở КОРПУС, nuôi qua R55 330 Ом từ −12,6 В — I ≈ 10,9 мА.
* **R14 1 кОм 1 Вт + Д3 (Д814Д, ~13 В)**: nút R14/Д3.к cấp +Uп (chân 7) **chỉ cho У5**.
  Theo bản vẽ, anốt Д3 nối vào đầu phải R17, **không** vào mát (xem §4).

### 2.2. Chia áp kênh đo (bộ định mức)
Mỗi kênh = R nối tiếp + biến trở СП5-3 4,7 кОм xuống КОРПУС; con chạy là đầu ra đã quy về một mức chung.

| Kênh | Chuỗi | U con chạy tối đa |
|---|---|---|
| +5 / −5 В | R5 / R46 (chỉ biến trở) | 5,00 В |
| ±6,3 В | R1 1,8k + R6 / R51 (?) + R47 | 4,56 В |
| ±10 В | R2 4,7k + R7 / R52 4,7k + R48 | 5,00 В |
| ±12,6 В | R3 5,6k + R8 / R53 5,6k + R49 | 5,75 В |
| ±20 В | R4 12k + R9 / R54 12k + R50 | 5,63 В |

Kênh âm đối xứng với kênh dương: R52/R53/R54 trùng trị số với R2/R3/R4.

### 2.3. Ma trận diode (bộ khử ghép) — chọn cực trị
* **У1 2Д908А** (anốt chân 1…5 ← con chạy R5…R9, katốt chung 10/11) ⇒ **max** của 5 kênh dương → У6.10; R62 120k xuống mát.
* **У2 2Д917А** (katốt 8,7,6,5,4 ← R5…R9, anốt chung 10/11) ⇒ **min** kênh dương → У5.IN−; R11 120k kéo lên nút R16/R17.
* **У3 2Д917А** (katốt 4…8 ← R46…R50, anốt chung) ⇒ áp **âm nhất** → У7.IN−; R64 120k về mát.
* **У4 2Д908А** (anốt 5,4,3,2,1 ← R46…R50, katốt chung) ⇒ áp **ít âm nhất** → У8.IN+; R56 47k kéo về R57/R58.

### 2.4. So sánh (K1…K4 trong TMKT)
| OA | IN+ (10) | IN− (in «8», = 9) | Ra 1 khi | Ngưỡng chỉnh bằng |
|---|---|---|---|---|
| У5 | R13 47k từ Vref+ / Д2 → con chạy R15 (R12 4,7k + R15) | min(+) qua У2 | kênh dương **thấp** | R15: 0…4,50 В |
| У6 | max(+) qua У1 | con chạy R17 qua Д4 (R16 5,1k + R17) | kênh dương **cao** | R17: 0…4,32 В (nếu R17.2 = mát) |
| У7 | con chạy R58 qua Д18 (R57 5,1k + R58) | min(−) qua У3 | kênh âm **cao về trị tuyệt đối** | R58: −4,32…0 В |
| У8 | max(−) qua У4 | con chạy R59 qua Д20, R61 47k về Vref− | kênh âm **thấp về trị tuyệt đối** | R59: −4,50…0 В |

Diode 2Д510А (Д2, Д4, Д18, Д20) nằm ở phía ngưỡng để bù sụt áp diode ma trận.
Ra: У5→Д5, У8 (chân in «6»)→Д21 ⇒ nút **thấp áp** (= chân 18); У6→Д6, У7→Д17 ⇒ nút **quá áp** (= chân 8, 4).

### 2.5. Giám sát lưới +27 В (K5, K6)
* Phân áp đo: R26 (trị số ở trang 211) từ +27 В xuống hai biến trở R24, R25 song song về mát.
* Chuẩn: R22 15k / R23 5,6k từ Vref+ ⇒ 2,45 В; Д9 + R21 từ ra У9 cộng trễ (hồi tiếp dương).
* **У9**: IN+ = chuẩn, IN− = con chạy R24 ⇒ ra 1 khi 27 В **giảm** (TMKT: −15 %, tức ≈ 22,95 В).
  Ra → Д8 → R20 → **T1** (mạch trùng hợp) và → Д13 → T5.
* **У10**: IN+ = con chạy R25, IN− = chuẩn ⇒ ra 1 khi 27 В **tăng** (+10 %, ≈ 29,70 В). Ra → Д12 → T5.
* Nối R22/R23 ↔ У9.10/У10.9 là **suy luận** (giao cắt không chấm, xem §4).

### 2.6. Khuếch đại cắt nguồn (T1…T4)
* Nút quá áp (Д6/Д17/chân 8) → R27 → T2 (C1 0,047 µF + R28 chống nhiễu).
* Nút thấp áp (Д5/Д21/chân 18) → R18 1k → điểm T1.к; T1 mở (lưới thấp) thì nuốt tín hiệu thấp áp.
  Nối T1.к/R18 → R27 vẽ bằng **nét chấm-gạch** có vòng tròn hở hai đầu (xem §4).
* T2 mở → T3 đóng (R30, Д10; R31 + C2 3,3 µF + Д22 chống tác động giả lúc bật nguồn) → T4 (2Т608Б) mở →
  emitơ T4 lên, Д11 (2С456А) dẫn → kéo **chân 4 ИСПОЛН. УСТР-ВО** lên và giữ lại (tự giữ) nút quá áp → T2.

### 2.7. Báo trạng thái (T5…T10)
* T5 nhận OR qua Д12 (У10), Д13 (У9), Д14 (thấp áp), Д24 (quá áp) → R35/R36.
* R37 + C3 15 µF trễ báo tốt khi bật; T5 mở thì xả C3. Khi U(C3) > Uст Д15 (Д818Д) → T6 mở → T7 đóng.
* T7 đóng: T8 (2Т608Б, lặp emitơ) → **chân 16 ЦВУ ≈ 5,2 ± 1 В** (kẹp Д16 2С456А, tải R42);
  T9 mở → **chân 10 ППЗУ ≤ 0,5 В**; T10 mở → **chân 17 ≤ 0,5 В**.
* Hỏng: T7 mở → T8, T9, T10 tắt ⇒ ЦВУ < 0,5 В, ППЗУ ≥ 15 В (R43 lên +27 В), chân 17 hở mạch.
* **Bo mạch không có rơ-le và không có bóng đèn**. «K1…K6» trong TMKT là ký hiệu bộ so sánh trên sơ đồ chức năng (hình 21),
  không phải rơ-le; còn «Y1…Y10» chính là У1…У10 (ma trận diode + 140УД1Б).

## 3. Điểm đo đề xuất cho thử trên bàn

Cấp +27 В (chân 6), ±12,6 В (chân 13/7), КОРПУС (chân 1); các chân КОНТР. còn lại lấy từ nguồn chỉnh được qua trở hạn dòng.
Nên cấp ±12,6 В trước rồi mới cấp +27 В (У5…У10 lấy −Uп từ chân 7).

| # | Điểm | Mong đợi / mục đích |
|---|---|---|
| TP1 | Д1.к (R10/R12/R13/R16) | ≈ +9 В |
| TP2 | Д19.а (R55/R57/R60/R61) | ≈ −9 В |
| TP3 | Д3.к = У5 chân 7 | đo thực tế — làm rõ Д3 nối đâu (§4) |
| TP4 | con chạy R5…R9, R46…R50 | mức chung các kênh ở danh định (chưa có số chuẩn) |
| TP5 | У2 10/11 và У1 10/11 | min(+) + ~0,6 В và max(+) − ~0,6 В |
| TP6 | У3 10/11 và У4 10/11 | tương tự cho nhánh âm |
| TP7 | У5.10, У6.(9), У7.10, У8.(9) | 4 ngưỡng; chỉnh bằng R15, R17, R58, R59 |
| TP8 | ra У5, У6, У7, У8 (chân 5; У8 in «6») | thấp khi bình thường, cao khi kênh lệch |
| TP9 | R22/R23 (У9.10), con chạy R24, R25 | chuẩn 2,45 В; chỉnh R24/R25 tại 22,95 В / 29,70 В |
| TP10 | T1.б, T1.к | T1 mở khi 27 В thấp |
| TP11 | T2.б, T3.к, T4.э | chuỗi cắt nguồn; T4.э cao khi tác động |
| TP12 | chân 4 | lệnh ИСПОЛН. УСТР-ВО (tải giả, đo áp khi tác động) |
| TP13 | C3 + (T5.к) | lên dần sau bật; xả khi có lỗi |
| TP14 | T7.к = T8.б | cao khi tốt |
| TP15 | chân 16 / 10 / 17 | tốt: 5,2 ± 1 В / ≤ 0,5 В / ≤ 0,5 В; hỏng: < 0,5 В / ≥ 15 В / hở |

Thao tác thử: lần lượt kéo từng chân КОНТР. ra ngoài ngưỡng (lên/xuống) → kiểm chân 4 và chân 16/10/17;
cấp mức cao vào chân 8 / chân 18 để giả tín hiệu từ A-313-12; hạ/nâng 27 В để thử У9/У10 và khoá T1.

## 4. Chưa chắc / thiếu

1. **Trang 211 không có ảnh** ⇒ thiếu loại/trị số **R24…R51** (28 điện trở, gồm biến trở R24, R25, R46…R50 và R26, R27…R45, R51).
   Các giá trị như R51 ≈ 1,8k chỉ là đoán theo đối xứng — chưa ghi vào danh mục.
2. **Д7** có trong danh mục (Д5…Д10, 6 cái) nhưng **không tìm thấy trên sơ đồ**. Không có Д23 trong danh mục lẫn sơ đồ.
3. **R17.2 / Д3.а**: bản vẽ nối hai chân này với nhau, dây đi qua bus КОРПУС **không có chấm**.
   Theo đối xứng với nhánh âm (R58.2 = КОРПУС) và vai trò ổn áp nguồn У5 của R14 + Д3, rất có thể nút này là КОРПУС. Phải đo.
4. **Chân 4 (общий) của У5–У6 và У7–У8** chỉ nối từng cặp với nhau, không thấy nối mát (У9, У10 có chân 4 nối mát). Nghi thiếu nối trên bản vẽ.
5. **R22/R23 ↔ У9.10/У10.9**: giao cắt không chấm; đã ghi là nối (suy luận theo chức năng).
6. **Cực gốc T7** không có dây vẽ vào; đã ghi nối T6.к (suy luận theo TMKT).
7. **R37 + R41**: dây chung chỉ nối hai điện trở này, cắt dây +27 В và +12,6 В không chấm ⇒ chưa rõ nguồn nuôi.
8. **Nét chấm-gạch T1.к/R18 ↔ R27.1**: không rõ là dây thật, dây tuỳ chọn hay vệt photocopy.
   Nếu là dây thật thì khi lưới thấp T1 cũng chặn cả tín hiệu quá áp.
9. **У9.7 nối thẳng +27 В** theo bản vẽ (các OA khác lấy +12,6 В hoặc nút Д3) — vượt mức nguồn danh định của 140УД1Б; cần kiểm.
10. Chân IN− của У5…У8 in hình «8» (У5 giống «0»); У9/У10 in «9». Chân ra của У8 in «6» (các con khác «5»). Netlist giữ số in.
11. Cực tính C2 không in; ghi «+» về phía +27 В theo suy luận. Dấu «+» của C3 có in.
12. Д1, Д15, Д19: danh mục in «Д818Е», có chữ «Д» viết tay phía trên ⇒ ghi Д818Д. R17 in «СП-3» (các biến trở khác «СП5-3»).
13. Sơ đồ chụp nghiêng/gấp; lề trái chỉ có dây mát nối hai nửa, không thấy linh kiện bị cắt. Mép phải (bảng đầu nối) đầy đủ 18 dòng.
14. Trị số ngưỡng tuyệt đối (mức chung của con chạy) không có trong tài liệu — phải lấy từ quy trình chỉnh hoặc đo trên khối tốt.
