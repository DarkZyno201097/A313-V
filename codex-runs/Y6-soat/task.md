Nhiệm vụ: soát lại các chân chưa rõ của netlist рис.7 — tấm Y6 (ЕУ3.057.140 Э3, 3 лист), khối A-313-3.

NGUỒN — CHỈ ĐỌC ĐÚNG 4 FILE SAU, KHÔNG MỞ FILE/FOLDER NÀO KHÁC:
E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\tmp\pdfs\review\a313-3\e3\ric07_net.csv
E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\A313-3_CONTROL\Y6\RE_trXXX_a255.jpg   (л.1/3)
E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\A313-3_CONTROL\Y6\RE_trXXX_a256.jpg   (л.2/3)
E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\A313-3_CONTROL\Y6\RE_trXXX_a257.jpg   (л.3/3, chụp xoay ngang)

VIỆC: với MỖI dòng của ric07_net.csv có dấu `?` (ở cột net hoặc note), phóng to đúng vùng ảnh đó và đọc lại.

OUTPUT — tạo đúng 1 file:
E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\tmp\pdfs\review\a313-3\e3\ric07_soat_raw.csv

Cột: ref,pin,net_cu,ket_qua,noi_toi,note — mỗi dòng `?` của ric07_net.csv đúng một dòng (giữ ref, pin, net_cu y như file gốc).
- ket_qua: `ro` (đã đọc chắc) hoặc `van_chua_ro`.
- noi_toi (khi ket_qua = ro), một trong ba dạng:
  - các chân khác nối cùng dây, cách nhau `;`, ví dụ `У21.5;У30.2`
  - nhãn mũi tên in trên ảnh, chép nguyên văn, ví dụ `П1/14(1) 8рРМ` hoặc `У35/11(3)`
  - `a` hoặc `б` nếu nối thanh nguồn có chữ đó
- note: лист + vùng ảnh; nếu van_chua_ro thì ghi lý do (mờ / mép cắt / nếp gấp / chữ nhỏ).

QUY TẮC:
- Không đoán, không lấy chân theo datasheet. Không suy hai chân nối nhau chỉ vì cùng tên tín hiệu.
- Không sửa ric07_net.csv hay file nào khác.

Trả lời cuối: tổng số dòng `?` đã xét, số `ro`, số `van_chua_ro`. Xong thì dừng.
