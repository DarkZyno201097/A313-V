# Рис.18 — Усилители выходные (Y10 của A-313-3), ЕУ2.032.463 Э3

Người chép: Claude, 2026-10-25. Dữ liệu sinh bằng `ric18_gen.py` → `ric18_bom.csv` (82 ref), `ric18_conn.csv`
(П1, 53 chân), `ric18_net.csv` (425 chân). Kiểm: `e3_check.py` (рис.18 PASS, không ngoại lệ), `e3_vs_e4.py 18 У10`.

**Trạng thái: ĐÃ CHÉP ĐỦ MỘT TỜ.** 0 «НЕ ПРОСЛЕЖЕНО»; một số chỗ chưa chắc ghi `?` ở cột note (mục 5).

## 1. Nguồn
| Ảnh | Nội dung | Dùng |
|---|---|---|
| `A313-3_CONTROL/Y10/RE_tr206_a208.jpg` (3386×2292) | Э3 trang 206, 1 tờ: 16 kênh, khối tạo М/~М, tụ nguồn, ô mẫu «Ячейка усилителя 1…16», ghi chú 1–2 | **nguồn chính** (nét hơn) |
| `A313-3_CONTROL/Y10/RE_tr206_a271.jpg` (1536×2048, chụp lại) | cùng tờ, chụp xoay | đối chiếu |
| `A313-3_CONTROL/Y10/Y10.jpg` | ảnh tấm thật (mặt linh kiện, hai vỏ 302НР3 «3848», nhãn ЕУ6.730.163-9) | tham khảo |
| `ЕУ.048.002.РЭ(A313-3)/RE_tr207_a209.jpg`, `RE_tr208_a210.jpg` | ПЭ рис.18 (Приложение лист 74–75) | BOM |

## 2. Cấu trúc (giống hệt A313-V.06 về topo)
- **16 kênh điều chế cân bằng.** Mỗi kênh n: khoá nối tiếp 2 section (168КТ2Б, gate = ~М, П1/41) nối Вх.n → nút S;
  section thứ hai nối Вх.n → R tải 10 kΩ (R4…R19) → đất; khoá song song 1 section (gate = М, П1/34) kéo S xuống đất;
  ô khuếch đại УМn (+ = S, − = điểm giữa mạng điện trở 302НР3 У19/У20, ra = Вых.n). Ở pha ~М: Vo = +Vin; pha М: Vo = −Vin
  (tỉ số mạng 302НР3) ⇒ sóng vuông 400 Hz mang biên độ và dấu.
- **Ô УМ** (ПЭ vị trí R1…R16): У13 140УД1Б + tầng đẩy kéo T1 2Т312Б / T2 2Т203Б, R2 180 Ω ra, R3 4,7 kΩ vào +,
  R1 56 Ω + C1 hiệu chỉnh chân 12, C2 68 pF hồi tiếp. C1 sửa tay 3300 → **6800 pF** («Дополнение I»).
- **Khối tạo М / ~М / xung 400 Hz:** chuẩn ~5 В 400 Гц (П1/8) qua phân áp R20 2,61 k / R21 301 Ω vào У14(−), R24 **2,05 kΩ**
  / R25 301 Ω vào У15(−); trễ ±h từ R22/R23 và R28/R29 (10,5 k / 301 Ω, ±12,6 В) chọn bởi У16.1/У16.2 qua hai nút A, B;
  У17 (168КТ2В) tạo A, B và kéo «⎍400Гц» (П1/13, R34 1,8 k lên +3,5 В) xuống «Корпус»; У18 tạo М (П1/34) và ~М (П1/41)
  với R35/R36 10 k xuống −23 В.
- **Ghi chú 1 trên Э3:** chân 4 của У13/У14/У15 → «общий провод»; chân 1 → −12,6 В; chân 7 → +12,6 В;
  **chân 11 (подложка) của У1…У12 → +6,3 В, của У16…У18 → +3,5 В.**

## 3. Đối chiếu bảng П1 ↔ Э4 (У10П1, `e4/p148.csv`)
`e3_vs_e4.py 18 У10`: **39 khớp / 4 lệch tên / 0 chỉ-Э3 / 1 chỉ-Э4**.
| Chân | Э3 (a208) | Э4 | Ghi chú |
|---|---|---|---|
| 34 | М | УПР МОД.1 | cùng tín hiệu — HDSD A-313-3 gọi «УПР. МОД 1/2» |
| 41 | ~М | УПР МОД.2 | như trên |
| 13 | ⎍400Гц | ⊓ 400Гц | chỉ khác ký hiệu xung |
| 21 | −23В | −20В | trùng vấn đề Y21 (bản vẽ −20 В, khối lắp −02 = −23 В), xem ric22_mota |
| 36 | trống | «6р СЧК» | Э3 không vẽ nhánh tới chân này |

Kiểm chéo nội bộ: cả 16 nhãn «П1/xx Вх.n» và «Вых.n» trên sơ đồ khớp đúng bảng chân П1.

## 4. So với A313-V.06 (đáng chú ý cho sửa chữa)
- Cùng topo kênh và khối tạo xung (U14…U18 của .06 ↔ У14…У18 của Y10).
- **ПЭ Y10 ghi R24 = 2,05 kΩ rõ ràng** ⇒ thêm bằng chứng cho kết luận A313-V.06 §9.1 (R24 = 2,05 kΩ, bản vẽ .06 ghi sai đơn vị).
- **Khác: đế (chân 11) 168КТ2.** Y10 nối +6,3 В (khoá kênh) và +3,5 В (khoá tạo xung); A313-V.06 để thả nổi
  (`File của A313-V/Datasheet/01_…168KT2…md`). Cần xem xét khi so hành vi khoá hai khối [suy-luan].
- Tầng đệm ra: .06 dùng R 180 Ω + Q NPN/PNP; Y10 cũng vậy (trong ô УМ).

## 5. Chỗ chưa chắc (ghi `?` trong `ric18_net.csv`)
| Mục | Lý do |
|---|---|
| Ký hiệu đất (vạch đậm) ở R4…R19, khoá song song, C3, C4 → net `ĐẤT ⊥` | Sơ đồ không ghi tên; chưa rõ là «Общий провод» (П1/27) hay «Корпус» (П1/48) |
| Kênh 14: chân đất khoá song song У10.2 | Đọc giống «3»; theo quy luật section 2 của 168КТ2 lấy 5 |
| Kênh 3: chân Vin của mạng У19.3 | Đọc «71»/«21» — lấy 21 |
| Kênh 12: vỏ khoá nối tiếp | Nhãn đọc «Уg.2»; У9.2 đã dùng ở kênh 11 ⇒ У8.2 |
| C5 chân 1, C8 chân 1 | Chấm nối trên dây +12,6 В không rõ |
| C14, C15, C16 | Có trên Э3, **không có trong ПЭ** tr.207–208 |
| Ghi chú 1 «chân 1 → −12,6 В» vs ô mẫu vẽ R1 ở chân 12 | Không mâu thuẫn: R1–C1 nối chân 12 (hiệu chỉnh), chân 1 là nguồn âm theo ghi chú |
| Chân nguồn của ô УМ | Mô hình hoá thành `V+` / `V-` theo hình ô mẫu; bên trong ô không chép thành netlist riêng |
