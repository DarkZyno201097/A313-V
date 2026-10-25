"""Generator for ric12_13_{bom,net,conn}.csv — one on-page transcription of
A313-3_CONTROL/Y14/RE_tr188_a184.jpg (= byte-identical Y15 copy), shared between
рис.12 (Y15, Преобразователь РК II) and рис.13 (Y14, Преобразователь РК I),
per user confirmation. CSV note fields are Vietnamese (matches ric14_bom/net/conn.csv
convention); ric12_13_mota.md narrative is Russian (matches ric14_mota.md).

Run: python ric12_13_gen.py   (writes the three CSV files in this directory)
"""
import csv
from pathlib import Path

D = Path(__file__).resolve().parent
PHOTO = "RE_tr188_a184.jpg"
PAGE = 188
UNREAD_TYPE = "Không có chữ loại/trị số in trên sơ đồ, đã kiểm bằng cách soi kỹ nhiều độ phóng đại."
UNTRACED = "НЕ ПРОСЛЕЖЕНО "

# ---------------------------------------------------------------- BOM -----
BOM = []

def bom(ref, name, qty, note):
    BOM.append([ref, name, str(qty), str(PAGE), note])

# --- Ячейка РК 1...4 (không bị gạch chéo, đang hoạt động) ---
bom("У1-1", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"Đọc trực tiếp: khối 'У1-1', chân 14 (vào), 13 (lên thanh bus chung), 2 (ra qua Р1вых). {UNREAD_TYPE}")
bom("У1-2", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"Đọc trực tiếp: khối 'У1-2', chân 4 (vào), 3 (lên thanh bus chung), 12 (ra qua Р2вых). {UNREAD_TYPE}")
bom("У1-3", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"Đọc trực tiếp: khối 'У1-3', chân 11 (vào), 10 (ra qua Р4вых), 5 (lên thanh bus chung). {UNREAD_TYPE}")
bom("У1-4", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"Đọc trực tiếp: khối 'У1-4', chân 7 (vào), 6 (bắc cầu với chân 9 → Р3вых), 9 (bắc cầu với chân 6). {UNREAD_TYPE}")
bom("Д1", "Диод (không ghi loại)", 1,
    f"Diode mắc song song cùng 2 nút Б/А với điện trở Р1вх (đọc trực tiếp từ cách vẽ 2 ký hiệu song song), phía trước chân 14 của У1-1. {UNREAD_TYPE}")
bom("Д2", "Диод (không ghi loại)", 1,
    f"Diode mắc song song cùng 2 nút Б/А với điện trở Р2вх, phía trước chân 7 của У1-4. {UNREAD_TYPE}")
bom("Р1вх", "Резистор (không ghi trị số)", 1,
    "Điện trở vào giữa 2 nút 'Б' và 'А' (nút А → У1-1 chân 14). LƯU Ý: hậu tố 'вх' do CHÚNG TÔI thêm để phân biệt — trên sơ đồ chỉ ghi 'Р1' một chữ, trùng tên với điện trở ra Р1вых (vị trí khác hẳn trên trang). " + UNREAD_TYPE)
bom("Р2вх", "Резистор (không ghi trị số)", 1,
    "Điện trở vào giữa 2 nút 'Б' và 'А' (nút А → У1-4 chân 7), cạnh Д2. Hậu tố 'вх' do CHÚNG TÔI thêm — trên sơ đồ chỉ ghi 'Р2', trùng tên với Р2вых. " + UNREAD_TYPE)
bom("Р1вых", "Резистор (không ghi trị số)", 1,
    "Điện trở ra từ У1-1 chân 2, đi sang phải. Hậu tố 'вых' do CHÚNG TÔI thêm — trên sơ đồ chỉ ghi 'Р1', trùng tên với Р1вх (vị trí khác). Đầu phải bị cắt ở rìa ảnh gốc (mép trang/nếp gấp), chưa truy được điểm đến. " + UNREAD_TYPE)
bom("Р2вых", "Резистор (không ghi trị số)", 1,
    "Điện trở ra từ У1-2 chân 3, đi sang phải. Hậu tố 'вых' do CHÚNG TÔI thêm — trùng tên Р2вх. Đầu phải ngoài khung ảnh đã chụp zoom, chưa truy được điểm đến. " + UNREAD_TYPE)
bom("Р3вых", "Резистор (không ghi trị số)", 1,
    f"Điện trở ra từ nút chung (У1-4 chân 6+9 bắc cầu) tới điểm có nhãn số '8' bên phải. {UNREAD_TYPE}")
bom("Р4вых", "Резистор (không ghi trị số)", 1,
    f"Điện trở ra từ У1-3 chân 10 tới điểm có nhãn số '7' bên phải. {UNREAD_TYPE}")

# --- Nhóm У3 (gạch chéo chữ X lớn trên bản vẽ = không lắp/deprecated, theo quy ước đã lập của dự án) ---
bom("У3-2", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"BỊ GẠCH CHÉO chữ X lớn. Khối 'У3-2' (chữ số đọc tin cậy — hình dạng khớp với 'УЗ-1' ở relay Исправн đọc rõ ràng), chân 4,3,12. {UNREAD_TYPE}")
bom("У3-3", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"BỊ GẠCH CHÉO chữ X lớn. Khối 'У3-3', chân 5,11,10. {UNREAD_TYPE}")
bom("У3-4", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"BỊ GẠCH CHÉO chữ X lớn. Khối 'У3-4', chân 7,6,9; vào từ Д3/Р3у3, chân 6 → nhãn 'Корпус' (dây gần đó ghi 'П1/41'). {UNREAD_TYPE}")
bom("Д3", "Диод (không ghi loại)", 1,
    f"BỊ GẠCH CHÉO (trong khối У3 bị gạch). Diode song song 2 nút Б/А với Р3у3, trước chân 7 của У3-4. {UNREAD_TYPE}")
bom("Р3у3", "Резистор (không ghi trị số)", 1,
    "BỊ GẠCH CHÉO. Điện trở vào 2 nút Б/А trước Д3→У3-4 chân 7; hậu tố 'у3' do CHÚNG TÔI thêm — trên sơ đồ chỉ ghi 'Р3', trùng tên với Р3вых ở nhóm Ячейка РК1...4 (vị trí khác hẳn trên trang). " + UNREAD_TYPE)
bom("Р5", "Резистор (không ghi trị số)", 1, f"BỊ GẠCH CHÉO. Ở phần dưới khối У3 bị gạch, chưa truy được chân cụ thể nối tới (xem ric12_13_net.csv). {UNREAD_TYPE}")
bom("Р6", "Резистор (không ghi trị số)", 1,
    f"BỊ GẠCH CHÉO HAI LẦN: gạch X chung của khối + một NÉT GẠCH CHÉO RIÊNG đè ngay lên ký hiệu điện trở — ở đầu vào từ 'П1/1 +5В'. {UNREAD_TYPE}")
bom("Р7", "Резистор (không ghi trị số)", 1, f"BỊ GẠCH CHÉO (gạch X chung của khối). Cạnh Р5/Р12, chưa truy được chân cụ thể nối tới. {UNREAD_TYPE}")
bom("Р8", "Резистор (không ghi trị số)", 1, f"BỊ GẠCH CHÉO. Giữa chân 4 khối У3-2 và nút 'Режим/П1/42' (xem net). {UNREAD_TYPE}")
bom("Р9", "Резистор (không ghi trị số)", 1, f"BỊ GẠCH CHÉO. Giữa khối У3-3/У3-2 và Р12 (xem net). {UNREAD_TYPE}")
bom("Р10", "Резистор (không ghi trị số)", 1, f"BỊ GẠCH CHÉO. Từ nút (У3-4 chân 9) tới khối У3-3 (chân 5), tiếp đến Р9. {UNREAD_TYPE}")
bom("Р12", "Резистор (không ghi trị số)", 1, f"BỊ GẠCH CHÉO. Cạnh chân 3 khối У3-2, dẫn tới 'Режим'/'+6,3В' (П1/26 hoặc /27 — xem conn.csv, chữ số không chắc chắn). {UNREAD_TYPE}")

# --- У3-1 — relay 'Исправн' vẽ riêng (KHÔNG bị gạch chéo, đang hoạt động) ---
bom("У3-1", "Ключ (ký hiệu vòng tròn + mũi tên kiểu emitter; không ghi loại)", 1,
    f"KHÔNG bị gạch chéo — vẽ tách riêng khỏi khối У3-2..4 (vị trí khác trên trang), phục vụ tín hiệu 'Исправн'. Chữ 'УЗ-1' đọc rõ ràng, tin cậy cao (soi ở độ phóng đại 3x). Chân 14 (vào, từ 'П1/43 Исправн'), 13 ('Корпус'), 2 (ra qua Р13). {UNREAD_TYPE}")
bom("Р13", "Резистор (không ghi trị số)", 1,
    f"Từ У3-1 chân 2 tới nút chung giữa '+5В' và 'П1/9 Упр.\"Исправн\"'. {UNREAD_TYPE}")

# --- Ma trận 16 kênh relay РК-1 .. РК-16 ---
# Đã kiểm trực tiếp cả 16 nhãn 'РК-N' và 'Упр.N' (4 khối x 4), không chỉ chọn mẫu vài cái.
for n in range(1, 17):
    bom(f"РК-{n}", "Реле / nhóm tiếp điểm (ký hiệu trong ma trận; không ghi loại/trị số cuộn dây)", 1,
        f"Ô thứ {n} trong ma trận 16 kênh (4 khối x 4, đã soi trực tiếp đủ cả 16 nhãn 'РК-N', không suy luận từ vài ô mẫu). Đầu vào điều khiển là tín hiệu 'Упр.{n}' (xem ric12_13_conn.csv). Đầu chung/tiếp điểm chuyển mạch đi về nhóm 'Ячейка РК x...y' — chưa truy được nối tới ô cụ thể nào (xem net). {UNREAD_TYPE}")

with (D / "ric12_13_bom.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ref", "name", "qty", "page", "note"])
    w.writerows(BOM)

print(f"BOM rows written: {len(BOM)}")

# ---------------------------------------------------------------- NET -----
NET = []

def net(ref, pin, value, note):
    NET.append([ref, pin, value, note])

def untraced(ref, pin, note):
    net(ref, pin, f"{UNTRACED}{ref}.{pin}", note)

OVERLAP = ("Nhiều nét gần như song song/chồng khít (<10px ở ảnh gốc) chạy dọc "
           "suốt chiều cao khối, không tách được từng chân riêng dù đã soi ở "
           "độ phóng đại 2-3x.")
CROSSED_BY_X = ("Đường dây bị nét gạch chéo chữ 'X' lớn (ký hiệu không lắp) "
                "của khối cắt ngang qua đúng vị trí giao điểm, không phân biệt "
                "được dây nào thuộc X với dây mạch thật.")

# --- У1-1 ---
net("У1-1", "14", "Nút А (Р1вх // Д1)", "Đọc trực tiếp, nét nối thẳng không bắc cầu.")
untraced("У1-1", "13", f"Lên thanh bus dọc chung với У1-2/У1-3/У1-4. {OVERLAP}")
net("У1-1", "2", "Р1вых (điện trở ra)", "Đọc trực tiếp, nét nối thẳng không bắc cầu.")

# --- У1-2 ---
untraced("У1-2", "4", f"Chân vào; chưa xác định nối với Р1вх hay Р2вх — cả 2 tổ hợp "
         f"input (Р1вх/Д1 và Р2вх/Д2) đều có 2 nút 'Б'/'11' chạy dọc suốt khối, "
         f"dây từ 4 vòng tròn đầu cuối (1,2,3,4) bên trái khối bắt chéo nhau trước "
         f"khi tới từng chân. {OVERLAP}")
net("У1-2", "12", "Р2вых (điện trở ra)", "Đọc trực tiếp, nét nối thẳng không bắc cầu.")
untraced("У1-2", "3", f"Lên thanh bus dọc chung với У1-1/У1-3/У1-4. {OVERLAP}")

# --- У1-3 ---
untraced("У1-3", "11", f"Chân vào; cùng lý do chưa xác định như У1-2 chân 4 (xem ghi chú đó). {OVERLAP}")
net("У1-3", "10", "Р4вых (điện trở ra)", "Đọc trực tiếp, nét nối thẳng không bắc cầu.")
untraced("У1-3", "5", f"Lên thanh bus dọc chung với У1-1/У1-2/У1-4. {OVERLAP}")

# --- У1-4 ---
net("У1-4", "7", "Nút А (Р2вх // Д2)", "Đọc trực tiếp, nét nối thẳng không bắc cầu.")
net("У1-4", "6", "Bắc cầu với chân 9 → Р3вых", "Chấm nối rõ giữa chân 6 và chân 9, cùng ra Р3вых.")
net("У1-4", "9", "Bắc cầu với chân 6 → Р3вых", "Chấm nối rõ giữa chân 6 và chân 9, cùng ra Р3вых.")

# --- Д1 / Р1вх (2 nút Б/А, song song) ---
untraced("Д1", "Б", "Nguồn phía trên nút Б chưa xác định; nét kéo dài ra khỏi vùng đã chụp zoom.")
net("Д1", "А", "У1-1 chân 14 (song song với Р1вх)", "Đọc trực tiếp từ cách vẽ 2 ký hiệu song song giữa cùng 2 nút.")
untraced("Р1вх", "Б", "Nguồn phía trên nút Б chưa xác định; nét kéo dài ra khỏi vùng đã chụp zoom.")
net("Р1вх", "А", "У1-1 chân 14", "Đọc trực tiếp, nét nối thẳng.")

# --- Д2 / Р2вх (2 nút Б/А, song song) ---
untraced("Д2", "Б", "Nguồn phía trên nút Б chưa xác định; nét kéo dài ra khỏi vùng đã chụp zoom.")
net("Д2", "А", "У1-4 chân 7 (song song với Р2вх)", "Đọc trực tiếp từ cách vẽ 2 ký hiệu song song giữa cùng 2 nút.")
untraced("Р2вх", "Б", "Nguồn phía trên nút Б chưa xác định; nét kéo dài ra khỏi vùng đã chụp zoom.")
net("Р2вх", "А", "У1-4 chân 7", "Đọc trực tiếp, nét nối thẳng.")

# --- Р1вых / Р2вых / Р3вых / Р4вых (đầu ra, điểm đến bị cắt khung ảnh) ---
net("Р1вых", "trái", "У1-1 chân 2", "Đọc trực tiếp, nét nối thẳng.")
untraced("Р1вых", "phải", "Đầu phải bị cắt ở rìa vùng đã chụp zoom (ric1213/output_resistors.png); chưa chụp lại vùng mở rộng để xác nhận điểm đến.")
net("Р2вых", "trái", "У1-2 chân 3", "Đọc trực tiếp, nét nối thẳng (xác nhận ở output_resistors.png).")
untraced("Р2вых", "phải", "Đầu phải bị cắt ở rìa vùng đã chụp zoom; chưa chụp lại vùng mở rộng để xác nhận điểm đến.")
net("Р3вых", "trái", "У1-4 chân 6+9 (nút chung)", "Đọc trực tiếp, xác nhận ở output_resistors.png.")
net("Р3вых", "phải", "Đầu nối có nhãn số '8'", "Đọc trực tiếp, mũi tên số 8 ngay cạnh đầu dây.")
net("Р4вых", "trái", "У1-3 chân 10", "Đọc trực tiếp, xác nhận ở output_resistors.png.")
net("Р4вых", "phải", "Đầu nối có nhãn số '7'", "Đọc trực tiếp, mũi tên số 7 ngay cạnh đầu dây.")

# --- У3-2, У3-3, У3-4 (khối bị gạch chéo) ---
net("У3-4", "7", "Nút А (Р3у3 // Д3)", "Đọc trực tiếp, nét nối thẳng (ric1213/crossed_top.png).")
net("У3-4", "6", "Корпус (П1/41)", "Đọc trực tiếp: dây ra ngay cạnh có nhãn 'Корпус' và 'П1/41' (ric1213/crossed_top.png).")
net("У3-4", "9", "Qua Р10 → chân 5 của У3-3", "Đọc trực tiếp, nét nối thẳng xuống Р10 (ric1213/crossed_mid.png).")
untraced("У3-3", "11", f"{CROSSED_BY_X} Vùng xung quanh У3-3 chân 11/У3-2 chân 2/7 có thêm nhiều nét chồng nhau.")
net("У3-3", "5", "Qua Р10 ← chân 9 của У3-4", "Đọc trực tiếp (xem У3-4 chân 9).")
net("У3-3", "10", "Qua Р9 → hướng khối У3-2", "Đọc trực tiếp nét nối tới Р9, nhưng điểm đến cụ thể bên khối У3-2 (chân 4 hay 3 hay 12) chưa phân biệt được do nhiều nét chồng khít + bị gạch X cắt ngang.")
net("У3-2", "4", "Qua Р8 → 'Режим'/П1/42 (hướng)", "Đọc trực tiếp hướng đi của Р8 nhưng điểm cuối chính xác (nút nào trong cụm Режим/+6,3В) chưa phân biệt do chữ số П1/26 hay /27 không chắc chắn — xem ric12_13_conn.csv.")
untraced("У3-2", "3", f"{CROSSED_BY_X}")
untraced("У3-2", "12", f"{CROSSED_BY_X}")

# --- Д3 / Р3у3 ---
untraced("Д3", "Б", "Nguồn phía trên (vùng input connector 'Упр.В1/В/В2') chưa truy được chân cụ thể nối vào — 3 dây song song sát nhau.")
net("Д3", "А", "У3-4 chân 7 (song song với Р3у3)", "Đọc trực tiếp từ cách vẽ 2 ký hiệu song song giữa cùng 2 nút.")
untraced("Р3у3", "Б", "Nguồn phía trên (vùng input connector 'Упр.В1/В/В2') chưa truy được chân cụ thể nối vào — 3 dây song song sát nhau.")
net("Р3у3", "А", "У3-4 chân 7", "Đọc trực tiếp, nét nối thẳng.")

# --- Р5, Р6, Р7, Р8(đã ghi ở trên qua У3-2.4), Р9, Р10, Р12 ---
untraced("Р5", "trái", f"{CROSSED_BY_X}")
untraced("Р5", "phải", f"{CROSSED_BY_X}")
net("Р6", "trái", "П1/1 +5В", "Đọc trực tiếp, nhãn 'П1/1 +5В' ngay đầu dây trái (ric1213/crossed_bottom.png).")
untraced("Р6", "phải", "Điện trở có NÉT GẠCH CHÉO RIÊNG đè lên ký hiệu (không lắp); đầu phải nối tiếp vào vùng nhiều nét chồng khít, chưa phân biệt được điểm đến.")
untraced("Р7", "trái", f"{CROSSED_BY_X}")
untraced("Р7", "phải", f"{CROSSED_BY_X}")
net("Р8", "trái", "Khối У3-2 (hướng, xem У3-2 chân 4)", "Xem ghi chú ở dòng У3-2.4.")
untraced("Р8", "phải", "Nối tiếp vào vùng nhãn 'Режим'/'П1/42' nhưng điểm nút chính xác chưa phân biệt do nhiều nét chồng khít.")
untraced("Р9", "trái", f"Nối từ hướng Р10/khối У3-3 nhưng điểm chân chính xác chưa phân biệt. {OVERLAP}")
untraced("Р9", "phải", f"{CROSSED_BY_X}")
net("Р10", "trái", "У3-4 chân 9", "Đọc trực tiếp, nét nối thẳng (ric1213/crossed_mid.png).")
net("Р10", "phải", "У3-3 chân 5", "Đọc trực tiếp, nét nối thẳng (ric1213/crossed_mid.png).")
untraced("Р12", "trái", f"Cạnh chân 3 khối У3-2 nhưng điểm nối chính xác chưa phân biệt. {OVERLAP}")
net("Р12", "phải", "Hướng 'Режим'/'+6,3В' (П1/26 hoặc /27)", "Đọc hướng đi chung nhưng chữ số pin chính xác không chắc chắn — xem ric12_13_conn.csv phần 'Chú ý đọc số'.")

# --- У3-1 (relay Исправн, KHÔNG gạch) ---
net("У3-1", "14", "П1/43 Исправн", "Đọc trực tiếp, mũi tên nhãn 'Исправн' và 'П1/43' ngay đầu dây vào (ric1213/small_relay.png).")
net("У3-1", "13", "Корпус", "Đọc trực tiếp, nhãn 'Корпус' ngay trên đường dây dọc cạnh chân 13.")
net("У3-1", "2", "Р13 (điện trở ra)", "Đọc trực tiếp, nét nối thẳng xuống Р13.")

# --- Р13 ---
net("Р13", "trái", "У3-1 chân 2", "Đọc trực tiếp.")
net("Р13", "phải", "Nút chung '+5В' và 'П1/9 Упр.\"Исправн\"'", "Đọc trực tiếp: điểm nối (chấm rõ) đồng thời chạm thanh dọc '+5В' và dây có mũi tên 'П1/9 Упр.\"Исправн\"' (ric1213/small_relay.png).")

# --- Ma trận 16 kênh РК-1..16: 2 dòng/relay (đầu điều khiển Упр.N đã rõ; đầu chung chưa truy) ---
for n in range(1, 17):
    ref = f"РК-{n}"
    net(ref, "упр", f"Упр.{n} (xem ric12_13_conn.csv để lấy đúng số chân П1)",
        "Đọc trực tiếp nhãn 'Упр.N' ngay trên dây vào của ô relay (ric1213/right_matrix.png + matrix_left_labels.png).")
    untraced(ref, "chung", f"Đầu chung/tiếp điểm (các chân 1-4 phía trái mỗi khối) đi về nhóm "
             f"'Ячейка РК x...y' tương ứng (1-4 → Ячейка РК1...4; 5-8 dự đoán → khối У3 bị gạch, "
             f"CHƯA XÁC NHẬN được tên nhóm chính thức cho RK9-16) nhưng không tách được RK cụ thể nào "
             f"nối tới cực cụ thể nào của khối У vì {OVERLAP.lower()}")

with (D / "ric12_13_net.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ref", "pin", "net", "note"])
    w.writerows(NET)

print(f"NET rows written: {len(NET)}")

# ---------------------------------------------------------------- CONN ----
CONN = []

def conn(table, pin, signal, note):
    CONN.append([table, pin, signal, PHOTO, note])

TABLE = "П1"
STD_NOTE = "Đọc trực tiếp từ bảng 'П1' (2 hàng viết tay: Конт / Цепь) ở đầu trang."

rows = [
    (41, "Корпус"), (33, "+27В"), (2, "+27В Б/С"), (26, "-6,3В"), (1, "+5В"),
    (28, "Упр.1"), (16, "Упр.2"), (30, "Упр.3"), (15, "Упр.4"),
    (14, "РК-1"), (29, "РК-2"), (3, "РК-3"), (31, "РК-4"),
    (17, "Упр.5"), (6, "Упр.6"), (18, "Упр.7"), (4, "Упр.8"),
    (37, "РК-5"), (5, "РК-6"), (32, "РК-7"), (19, "РК-8"),
    (35, "Упр.9"), (36, "Упр.10"), (8, "Упр.11"), (34, "Упр.12"),
    (39, "РК-9"), (7, "РК-10"), (20, "РК-11"), (21, "РК-12"),
    (38, "Упр.13"), (10, "Упр.14"), (24, "Упр.15"), (22, "Упр.16"),
    (25, "РК-13"), (23, "РК-14"), (12, "РК-15"), (40, "РК-16"),
    (9, 'Упр."Исправн"'), (43, "Исправн."), (42, "Режим."), (27, "+6,3В"),
    (13, "Упр.В-2"), (11, "Упр.В-"),
]
for pin, sig in rows:
    note = STD_NOTE
    if pin == 33:
        note += (" LƯU Ý: chữ số có thể đọc nhầm '33' <-> '43' (nét viết tay rất giống nhau); "
                  "chọn '33' vì khớp với nhãn 'П1/33 +27В' thấy trực tiếp trên dây vào khối У3 "
                  "(ric1213/crossed_top.png), tránh trùng với pin 43='Исправн.' đã xác nhận riêng.")
    if pin == 27:
        note += (" LƯU Ý: chữ số có thể là '26' hoặc '27' (nét viết tay mơ hồ ở vùng này); "
                  "bảng gốc đọc '27', trong khi nhãn dây trong thân sơ đồ gần khối У3 "
                  "(ric1213/crossed_bottom.png) đọc giống '26' — CHƯA GIẢI QUYẾT được mâu thuẫn này, "
                  "ghi theo bảng П1 vì đó là nguồn chính thức hơn, không tự suy luận khớp.")
    if sig in ("Упр.В-2", "Упр.В-"):
        note += (" LƯU Ý: nhãn dây trong thân sơ đồ (ric1213/crossed_top.png) ghi 'Упр.В1', 'Упр.В', "
                  "'Упр.В2' tại П1/27, П1/14, П1/13 — không khớp hoàn toàn số chân với bảng П1 ở đây "
                  "(П1/13, П1/11). CHƯA GIẢI QUYẾT được sai khác này; có thể do đọc nhầm chữ số viết tay "
                  "ở một trong hai chỗ, ghi trung thực cả hai, không tự ý sửa cho khớp.")
    conn(TABLE, str(pin), sig, note)

with (D / "ric12_13_conn.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["table", "pin", "signal", "photo", "note"])
    w.writerows(CONN)

print(f"CONN rows written: {len(CONN)}")
