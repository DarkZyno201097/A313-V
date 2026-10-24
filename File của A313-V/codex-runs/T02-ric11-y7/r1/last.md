### 1. Tóm tắt

Đã hoàn thành T02:

- BOM: 166 ref vật lý, gồm 153 điện trở và 13 vi mạch.
- Netlist: 462 chân, 51 net nội bộ.
- `e3_check.py`: exit 0, рис.11 không cần ngoại lệ.
- Э3↔Э4: 105 chân khớp, 0 lệch tên; chỉ Э4 có `П2/1 КОРПУС`.
- Không có ô `?` trong hai CSV.

### 2. File tạo/sửa

- Tạo [ric11_bom.csv](<E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/ric11_bom.csv>)
- Tạo [ric11_net.csv](<E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/ric11_net.csv>)
- Sửa [e3_check.py](<E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/e3_check.py>) — thêm рис.11 vào tuple kiểm tra.
- Tạo [e3_vs_e4.py](<E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/e3_vs_e4.py>)
- Sinh [ric11_vs_e4.csv](<E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/ric11_vs_e4.csv>)
- Tạo [ric11_mota.md](<E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/ric11_mota.md>)

`git diff --check` không báo lỗi. Không sửa nguồn ảnh hoặc CSV Э4.

### 3. Kết quả chạy 2 script

`python tmp/pdfs/review/a313-3/e3/e3_check.py` — exit 0:

```text
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

`python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py` — exit 0:

```text
E3 connector pins 105 | E4 connector pins 106
match 105 | name mismatch 0 | only E3 0 | only E4 1
only E4: П2/1 КОРПУС — bảng đầu nối có chân này, Э3 không vẽ nhánh tới chân linh kiện
wrote E:/Alitum/Tự học Altium/Projects/MODULE/A313/BO TLTK DAU A/A313-V_codex/tmp/pdfs/review/a313-3/e3/ric11_vs_e4.csv
```

### 4. Chỗ chưa chắc / “?”

| Ref, chân | Ảnh | Vùng | Lý do |
|---|---|---|---|
| Khung tên Э3 | #180 | Mép ngoài tờ gấp | Ảnh không chứa khung tên; định danh рис.11/trang 184 dựa trên `trang.csv`, T01 và ПЭ #179. |
| 5У1.7/.8/.9 | #180, #242 | Ячейка 5; vùng 5У1 | Э3 bỏ секция thứ ba, ПЭ ghi R7–R9 tổng 12 và bản lắp không có 5R7–5R9. Đã ghi `Н.С.`; chưa đo thông mạch trên tấm thật. |
| П2/1 | #180 | Bảng đầu nối góc phải | Đọc được `КОРПУС`, nhưng phần mạch chính không vẽ nhánh tới chân linh kiện. |

Không có trường `?` trong BOM/netlist vì không có ký hiệu linh kiện hoặc chân đã chép nào còn không đọc được.

### 5. Lệch e3↔e4 và giải thích

Chỉ có một khác biệt:

| Chân | Э3 | Э4 | Giải thích |
|---|---|---|---|
| П2/1 | Không có hàng chân linh kiện | `КОРПУС` | Bảng đầu nối trên #180 và Э4 đều ghi `КОРПУС`, nhưng sơ đồ chính không vẽ chân linh kiện nào nối tới đây. Không tạo ref giả trong netlist; giữ nguyên cả hai nguồn. |

Không có lệch tên tín hiệu: 105/105 chân hiện diện trong Э3 khớp Э4 sau chuẩn hoá `ВХ.`↔`ВХОД`, `ВЫХ.`↔`ВЫХОД` và Latin↔Cyrillic.

### 6. Phần chưa làm và lý do

- Không commit hoặc push: đúng yêu cầu Claude sẽ kiểm và commit.
- Không sửa `PROJECT_HANDOFF.md`, JARVIS ledger hoặc lưu AgentMemory: ngoài phạm vi file được phép; AgentMemory cũng bị approval policy từ chối.
- Chưa đo thông mạch tấm У7 thật; kết quả hiện chỉ xác nhận bản chép từ #179/#180/#242 và đối chiếu Э4.

Rủi ro còn lại: trạng thái không nối của `5У1.7/.8/.9` và quan hệ `П2/1 КОРПУС` chưa được kiểm bằng phép đo trên phần cứng.