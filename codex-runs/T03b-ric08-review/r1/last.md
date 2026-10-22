### 1. Tóm tắt

T03b hoàn thành **một phần**, chưa nghiệm thu toàn bộ рис.8.

- Dòng có `?`: **187 → 169**.
- ONLY_E4: **42 → 36**.
- Đối chiếu рис.8: **121 khớp / 3 lệch tên / 0 chỉ Э3 / 36 chỉ Э4**.
- Рис.11 giữ nguyên **105/0/0/1**.
- Sửa nhầm phía tín hiệu của R1–R11, địa chỉ У8.10 và các chân У14.3/.5; bổ sung những nối đọc chắc.
- Không commit.

### 2. File sửa

Trong `tmp/pdfs/review/a313-3/e3/`:

- `ric08_net.csv`
- `ric08_vs_e4.csv`
- `ric08_mota.md`

Không sửa BOM, script, Э4 hoặc ảnh gốc.

### 3. Output 3 lệnh kiểm

Cả ba lệnh **exit 0**. Output checker dưới đây giữ nguyên dấu thập phân do script hiện có xuất ra.

`python tmp/pdfs/review/a313-3/e3/e3_check.py`

```text
ric08: bom 86 ref, net 948 chân, 372 net (108 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —
ric11: bom 166 ref, net 462 chân, 159 net (51 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —
ric19: bom 111 ref, net 290 chân, 89 net (72 N#)
  trong bom không có trong net: ['Д7']
  trong net không có trong bom: —
  N# < 2 chân: —
ric20: bom 44 ref, net 98 chân, 26 net (22 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —
ric21: bom 46 ref, net 102 chân, 25 net (21 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —
ric22: bom 43 ref, net 99 chân, 23 net (19 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —
ric23: bom 50 ref, net 113 chân, 25 net (21 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —
ric24: bom 40 ref, net 95 chân, 27 net (19 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —
ric25: bom 164 ref, net 397 chân, 63 net (53 N#)
  trong bom không có trong net: ['R28', 'Д3', 'Д4']
  trong net không có trong bom: —
  N# < 2 chân: —
ric26: bom 47 ref, net 106 chân, 25 net (21 N#)
  trong bom không có trong net: —
  trong net không có trong bom: —
  N# < 2 chân: —

рис.24
  −5 В: Vдвижка R4 = −4.35 В → движок ở 0.48 hành trình R4 từ корпус
        dải chỉnh ≈ −0.65 … −9.65 В (giới hạn thêm bởi đầu vào −12,6 В)
  Iст Д1 (R1, R4) ≈ 7.66 − 1.91 = 5.74 мА
  Iст Д3 (R6, R8+R9) ≈ 7.66 − 2.81 = 4.85 мА
  Iст Д4 (R12, R15+R16) ≈ 7.66 − 2.00 = 5.66 мА
  +10 В: hệ số chia R11/R20 = 2.00; Vw cần = 4.35 В; dải Vw 3.375…9.0 В → Vout 8.05…19.30 В (thực tế ≤ ~10,6 В do đầu vào +12,6 В)
        dòng phân áp R11+R20 = 3.33 мА
  −10 В: |Vw| 6.00…9.00 В → движок R21 k = 0.665…0.965 (tỉ lệ từ корпус lên −10 В); dòng R21 = 4.55 мА
  +3,5 В: Uвх 6.3 В → Vб(T11) không tải = 3.15 В (Д5 4,7 В không dẫn) → Vout ≈ 2.50 В; R_Thevenin 110 Ом
  +3,5 В: Uвх 5.0 В → Vб(T11) không tải = 2.50 В (Д5 4,7 В không dẫn) → Vout ≈ 1.85 В; R_Thevenin 110 Ом

рис.26
  buck-boost đảo, CCM lý tưởng: D = U/(U+Uвх) = 0.318; Uвх 24…29,7 В → D 0.298…0.344
  điện áp ngược trên T6/Д2 ≈ Uвх+U = 39.6 В (Uвх 29,7 → 42.3 В)
  dòng trung bình qua Др2 ≈ Iн/(1−D) = 1.47 А tại 1 А
  điểm cân bằng: U = Vz·(R2+R3+R4)/(R4+k·R3); cần (R2+R3+R4)/(R4+kR3) = 1.400 — R2…R4 thiếu (tr. 238)
  ngưỡng bảo vệ: Iкз ≈ Vbe(T9)·(R17+R18)/(R17·R_Др3) — R17, R18, R_Др3 chưa biết
ngoại lệ đã biết ric19: Д7 có trong перечень, không có trên Э3
ngoại lệ đã biết ric25: R28, Д3, Д4 có trong перечень, không có trên Э3 (góc ảnh #233 bị che)
```

`python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 8 У5`

```text
E3 connector pins 124 | E4 connector pins 160
match 121 | name mismatch 3 | only E3 0 | only E4 36
wrote E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/ric08_vs_e4.csv
```

`python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 11 У7`

```text
E3 connector pins 105 | E4 connector pins 106
match 105 | name mismatch 0 | only E3 0 | only E4 1
only E4: П2/1 КОРПУС — bảng đầu nối có chân này, Э3 không vẽ nhánh tới chân linh kiện
wrote E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/ric11_vs_e4.csv
```

### 4. `?` còn lại

**169 hàng**. “Chưa soát hết” không đồng nghĩa ảnh không đọc được.

| Ref | Chân | Ảnh, vùng | Lý do/trạng thái |
|---|---|---|---|
| R1 | 2 | #168 trái dưới; #167 bảng nối | Nối đã xác nhận; dấu gạch trên tên chưa chắc |
| R11 | 2 | #168 trái trên; #167 П1 | Chữ РГР/ПРП chưa phân định |
| У8 | 2, 3, 4, 6, 8, 10, 11, 12 | #168 trái trên | .10 đã sửa địa chỉ, còn tên sửa tay; các chân khác chưa soát hết |
| У9, У10 | 2, 3, 5, 6, 8, 9, 11, 12 | #168 trái trên | Chưa soát hết từng chân |
| У11 | 1, 3–5, 8–13 | #168 trái giữa/đáy | Chưa soát hết |
| У12 | 1–6, 8–13 | #168 trái dưới | Chưa soát hết |
| У13 | 3–6, 8–13 | #168 trái | Chưa soát hết |
| У14 | 8 | #167 phải dưới | Chữ Nоб БК/NАБбк chưa phân định |
| У15, У16 | 1–6, 8–13 | #168 giữa/đáy | Chưa soát hết |
| У17 | 2, 3, 5, 6, 8, 12 | #168 trái | Chưa soát hết |
| У18 | 3, 5, 8, 12 | #168 gần nếp gấp | Chưa soát hết |
| У19, У21 | 3–6, 8, 11–13 | #168 đáy | Chưa soát hết |
| У20, У22–У25 | 1–6, 8–13 | #168 đáy | Chưa soát hết; cần kiểm cả số chân kế thừa T03 |

### 5. Lệch/ONLY_E4 còn lại + giải thích

| Chân | Э3 | Э4 | Kết luận |
|---|---|---|---|
| П1/10 | ВХОД РГР ТТЛ | ВХОД ПРП ТТЛ | Chữ viết tay chưa quyết định được; giữ cả hai |
| П3/42 | Nоб БК | NАБбк | Chưa phân định ký tự; giữ cả hai |
| П2/2 | Отв.Д | ОТВ.Д R15 | Nhánh У8.10 ghi Отв.Д; bảng có gạch xoá và R15 |

36 ONLY_E4 còn lại:

- П1: 2–9, 22–24, 44, 50–52.
- П2: 3, 48, 49.
- П3: 3, 4, 27, 28, 34–41, 55, 56, 62–65.

`mota` §3 đã liệt kê riêng từng chân và phần cần truy tiếp. Riêng П2/48 trở thành ONLY_E4 sau khi bỏ gán sai vào У8.10. Các hàng còn lại chưa đủ căn cứ để kết luận không có nhánh.

### 6. Chưa làm

Chưa hoàn tất truy từng đường cho 36 ONLY_E4 và soát từng chân của toàn bộ 169 hàng `?`; các phần này được ghi rõ là chưa hoàn tất trong `mota`.

Chưa kiểm phần cứng. Checker pass chỉ xác nhận cấu trúc dữ liệu; netlist còn chưa được nghiệm thu để dùng đấu dây.