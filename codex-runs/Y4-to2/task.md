Nhiệm vụ: chép netlist từ ảnh sơ đồ nguyên lý (Э3) рис.5, tờ 2/2 — tấm Y4 "Устройство программного управления"
(ЕУ3.057.138), khối A-313-3.

NGUỒN — CHỈ ĐỌC ĐÚNG 1 FILE SAU, KHÔNG MỞ/ĐỌC FILE/FOLDER NÀO KHÁC:
E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\A313-3_CONTROL\Y4\RE_tr159_a251.jpg

OUTPUT — tạo đúng 1 file:
E:\Alitum\Tự học Altium\Projects\MODULE\A313\BO TLTK DAU A\2.BO TLTK DAU A_A313-V\tmp\pdfs\review\a313-3\e3\ric05_to2_raw.csv

Cột: ref,pin,noi_toi,note — mỗi dòng = một chân linh kiện.
- ref: ký hiệu in trên ảnh (У16, R5, C1, Пэ1…). Phần tử trong vỏ ghi theo vỏ: «У7.2» → ref = У7.
- pin: số chân in cạnh chân.
- noi_toi: chân đó nối tới đâu, chỉ một trong ba dạng:
  - các chân khác nối cùng dây, cách nhau `;`, ví dụ `У21.5;У30.2`
  - nhãn mũi tên in trên ảnh, chép nguyên văn, ví dụ `П1/4(1) Испр.пит.` hoặc `У39/6(1)`
  - `a` hoặc `б` nếu nối thanh nguồn có chữ đó
- note: để trống nếu đọc chắc; không chắc thì ghi `?` + vùng ảnh + lý do.

QUY TẮC ĐỌC:
- Không chắc thì ghi `?`, không đoán, không lấy số chân theo datasheet.
- Không suy ra hai chân nối nhau chỉ vì cùng tên tín hiệu, nếu không thấy dây nối rõ trên ảnh.
- Bỏ qua chân 7 và 14 của vi mạch.
- Phần tử bị gạch chéo: vẫn ghi các chân, note = "gạch bỏ trên bản vẽ".
- Ưu tiên đủ chân hơn đọc đẹp: thà để noi_toi = `?` còn hơn bỏ sót chân.

Trả lời cuối: tổng số dòng, số dòng có `?`, danh sách phần tử bị gạch chéo.
Xong thì dừng, không sửa file nào khác, không chạy script khác.
