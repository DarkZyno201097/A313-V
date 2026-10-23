# S01 — Kiểm kê VT34 và VT28

Ngày 2026-10-23. Chỉ kiểm kê nguồn quét, không phân tích kỹ thuật hoặc chép nội dung mạch/bảng.

## 1. Phạm vi và cách đọc

55 PDF, 429 trang: VT34 252 trang chính + 7 sơ đồ rời; VT28 170 trang.
Mỗi trang có đúng một dòng `vt_pages.csv`, ảnh render 120 dpi; đã xem hết từng ảnh và phóng vùng chân trang khi cần.
Hash nguồn được ghi trong `vt_files.csv`, kiểm lại trước/sau thao tác. Không sửa nguồn, không đưa nguồn vào Git.

**Hai hệ số trang không được trộn:** VT34 có số đóng/in liên tục ở mép trên (dùng trong `trang_in` cho sách chính), ngoài số theo mục ở chân trang. VT28 có số viết tay tương ứng tên file nhưng `trang_in` lấy số IN ở chân trang; số này chạy lại theo phần (mở đầu, mô tả, 101…, 201…, phụ lục). Số dạng `5/6` giữ nguyên như trên giấy, không biến thành hai trang PDF. Sơ đồ rời VT34 chỉ có số viết tay được ghi trong ghi chú, không điền thay số in.

`loai` chỉ thể hiện loại nổi bật; một trang có thể vừa bảng vừa hình. `tieu_de` ghi tiêu đề nhận diện tiếng Nga, không chép nội dung; một số mã bản vẽ/ký hiệu công thức không chép đủ, ghi rõ ở phần giới hạn. Tiêu đề tiếp diễn được giữ để tra bảng nhiều trang. Ô trống có thể do không có chú thích hoặc mép quét bị cắt, không có nghĩa chưa xem.

## 2. Bảng file: số theo tên so với PDF

`—` nghĩa tên không có khoảng trang. Dung lượng MB dùng 1 000 000 byte; hash và dung lượng chi tiết ở CSV.

| Sách | File | Theo tên | PDF | Lệch | Giải thích |
|---|---|---:|---:|---:|---|
| VT34 | TR 1-55.pdf | 55 | 55 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT34 | TR 56-83.pdf | 28 | 28 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT34 | TR 85-140.pdf | 56 | 56 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT34 | TR 141-221.pdf | 81 | 81 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT34 | TR 223.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT34 | TR 225-259.pdf | 35 | 31 | -4 | Bốn số 248, 251, 254, 258 nằm trên các sơ đồ rời 3–6 (số viết tay). |
| VT34 | ẢNH SƠ ĐỒ/1.pdf | — | 1 | — | Một tờ sơ đồ rời. |
| VT34 | ẢNH SƠ ĐỒ/2.pdf | — | 1 | — | Một tờ sơ đồ rời. |
| VT34 | ẢNH SƠ ĐỒ/3.pdf | — | 1 | — | Một tờ sơ đồ rời. |
| VT34 | ẢNH SƠ ĐỒ/4.pdf | — | 1 | — | Một tờ sơ đồ rời. |
| VT34 | ẢNH SƠ ĐỒ/5.pdf | — | 1 | — | Một tờ sơ đồ rời. |
| VT34 | ẢNH SƠ ĐỒ/6.pdf | — | 1 | — | Một tờ sơ đồ rời. |
| VT34 | ẢNH SƠ ĐỒ/7.pdf | — | 1 | — | Một tờ sơ đồ rời. |
| VT28 | TR 1-9.pdf | 9 | 10 | 1 | Hai mặt bìa + 8 trang có nội dung (số viết tay 1, 3–9); số 2 ở file riêng. |
| VT28 | TR 2.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 10-23.pdf | 14 | 16 | 2 | 14 trang văn bản (số in 2–15) + mảnh sơ đồ viết tay 74 ở đầu + một trang trắng. |
| VT28 | TR 10.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 24-66.pdf | 43 | 40 | -3 | Không thấy số viết tay 25, 26, 35, 36; thêm một trang trắng: 43 − 4 + 1 = 40. Trang viết tay 66 thực tế là phụ lục trang in 62, lặp với TR 97-98. |
| VT28 | TR 67-69.pdf | 3 | 4 | 1 | Ba tờ theo số viết tay 67–69, trong đó tờ 68 được quét lặp. |
| VT28 | TR 70.pdf | 1 | 2 | 1 | Một tờ gấp được quét thành hai ảnh chồng lấn. |
| VT28 | TR 71.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 72.pdf | 1 | 2 | 1 | Một tờ gấp được quét thành hai ảnh chồng lấn. |
| VT28 | TR 73.pdf | 1 | 2 | 1 | Một tờ gấp được quét thành hai ảnh chồng lấn. |
| VT28 | TR 75.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 76.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 77.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 78.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 79-80.pdf | 2 | 2 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 81.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 82.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 83.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 84-85.pdf | 2 | 2 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 86.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 87.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 88.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 89.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 90.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 91.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 92.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 93.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 94.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 95-96.pdf | 2 | 2 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 97-98.pdf | 2 | 2 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 99.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 100-102.pdf | 3 | 3 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 103-104.pdf | 2 | 2 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 105.pdf | 1 | 2 | 1 | Một tờ gấp được quét thành hai ảnh chồng lấn. |
| VT28 | TR 106-108.pdf | 3 | 3 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 109.pdf | 1 | 2 | 1 | Một tờ gấp được quét thành hai ảnh chồng lấn. |
| VT28 | TR 110-113.pdf | 4 | 4 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 114-115.pdf | 2 | 2 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 116-117.pdf | 2 | 2 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |
| VT28 | TR 118-121.pdf | 4 | 5 | 1 | Bốn ảnh nội dung, gồm hai bản trang in 101, cộng một trang trắng. |
| VT28 | TR 122-143.pdf | 22 | 40 | 18 | 23 ảnh nội dung + 17 trang trắng = 40; có một bảng trang in 128 không mang số viết tay rõ và một ảnh cắt hai trang ở cuối. Không coi +18 là 18 trang in mới. |
| VT28 | TR 144.pdf | 1 | 1 | 0 | Khớp số lượng; không bảo đảm liên tục số trang in. |

## 3. Trang thiếu, trang trùng và tờ gấp

### VT34

Dãy số đóng/in của 252 trang chính thiếu **84, 222, 224, 248, 251, 254, 258** so với 1–259. Cả bảy số xuất hiện dạng viết tay trên bảy sơ đồ rời; vì vậy chưa có bằng chứng mất hẳn các tờ này trong tổng nguồn. Đối chiếu hình 1201–1205 ở dưới là **suy theo vị trí và trang chú thích**, không phải số рис. đọc trực tiếp từ các tờ rời 1–6.

| Sơ đồ rời | PDF | Số viết tay | Số in đọc được | Nội dung nhận diện |
|---|---:|---:|---|---|
| 1.pdf | 1 | 222 | — | suy рис.1201, лист 1 из 2; bản vẽ dây lắp |
| 2.pdf | 1 | 224 | — | suy рис.1201, лист 2 из 2; bản vẽ dây lắp |
| 3.pdf | 1 | 248 | — | suy рис.1202; sơ đồ nguyên lý |
| 4.pdf | 1 | 251 | — | suy рис.1203; sơ đồ nguyên lý |
| 5.pdf | 1 | 254 | — | suy рис.1204; sơ đồ nguyên lý |
| 6.pdf | 1 | 258 | — | suy рис.1205; sơ đồ nguyên lý |
| 7.pdf | 1 | 84 | 345/346 | Временная диаграмма цикла работы блока А-313-3. Рис.307 |

Các trang chính 221, 223, 247, 250, 253, 257 có chú thích hình nhưng vùng hình để trắng; bản vẽ ở tờ rời. Trang 15 cũng có chú thích рис.1 nhưng không thấy hình trong vùng chính. Bảng 1207 ở các số đóng 203–220 gồm các cặp trái/phải của bảng rộng, mỗi phần là một trang PDF; không được gộp hoặc xoá như bản trùng.

Quét dhash không xác nhận cặp trùng VT34. Ứng viên TR 141-221 PDF 15/17 (d=19) thực tế là hai trang khác nhau: số đóng 155/157, chân trang 801/1001.

### VT28

- Không có file TR 74, nhưng **số viết tay 74 xuất hiện ở TR 10-23 PDF 1**, chú thích рис.4 лист 2 из 3. Chân trang bị cắt nên `trang_in` để trống. **Suy** TR 10.pdf là phần tiếp của cùng tờ dựa trên hàng П1…П15 và các cột nối tiếp РК1; không phải bản lặp toàn ảnh. Chưa khẳng định toàn bộ tờ đã đủ mép.
- TR 2.pdf là trang in 1 của `Перечень действующих страниц`; TR 1-9 PDF 4 là trang in 2. **Không trùng**. Số trang in 1 tái xuất hiện ở các phần khác là cách đánh số của sách, không phải bằng chứng lặp.
- Thiếu trong chuỗi quét phần mô tả: **trang in 17–18 và 27–28** (số viết tay tương ứng nghi là 25–26 và 35–36); quan sát trực tiếp các bước nhảy 16→19, 26→29. Chưa thấy рис.10/11 ở phần mô tả.
- Phụ lục: chưa thấy đầy đủ các số **43/44** (danh mục cho рис.7), **69/70** (рис.13), **107–110** (рис.21 và danh mục); đây là khoảng nghi thiếu theo chuỗi và số hình, chưa đối chiếu bản chuẩn. Các số **7/8, 75/76** có thể thuộc các tờ bị cắt chân (TR 67-69 PDF 4, TR 105); không gán số suy vào CSV. Trang **135 / рис.33** chỉ có mảnh hình ở nửa phải TR 122-143 PDF 37, không đủ chú thích/số in để xác nhận. Các khoảng đơn lẻ 114/124 có thể là mặt trắng hoặc trang chưa quét; chưa kết luận thiếu nội dung.
- TR 24-66 PDF 39 (viết tay 66) là phụ lục trang in 62, cùng nội dung TR 97-98 PDF 2 (viết tay 98): **trùng giữa hai file**, dhash d=18/256 bit.
- TR 67-69 PDF 2/3: **trùng trong file**, cùng рис.2, trang in 5/6, d=15.
- TR 118-121 PDF 3/4: **trùng trong file**, cùng trang in 101, số viết tay 120/121 khác nhau, d=4.
- TR 122-143 PDF 36/37: lặp **một phần** рис.32; PDF 37 còn mảnh trang kế bên, không phải lặp toàn trang.
- Các tờ TR 70, 72, 73, 105, 109 đều chia thành hai ảnh chồng lấn. TR 109 đọc được cùng số in 81/82 ở cả hai phần. Các phần không có số in giữ trống, không sao chép số từ ảnh kế bên.

Dhash 256 bit toàn ảnh, ngưỡng ứng viên ≤24; các cặp bảng khác nhau nhưng cùng bố cục đã được loại bằng mắt. Đây là bộ lọc hỗ trợ, không chứng minh không còn trùng khi ảnh bị cắt/xoay. Khoảng cách tối thiểu của TR 2 so với TR 1-9 là 91; TR 10 so với TR 10-23 là 86. Cả hai cần kết luận bằng hình, không dựa riêng ngưỡng.

## 4. Trang không ghi được số in

- **VT34: 6 trang PDF**; phân loại: to_gap=6.
  ẢNH SƠ ĐỒ/1.pdf PDF 1; ẢNH SƠ ĐỒ/2.pdf PDF 1; ẢNH SƠ ĐỒ/3.pdf PDF 1; ẢNH SƠ ĐỒ/4.pdf PDF 1; ẢNH SƠ ĐỒ/5.pdf PDF 1; ẢNH SƠ ĐỒ/6.pdf PDF 1.
- **VT28: 31 trang PDF**; phân loại: bia=1, trang_trang=21, to_gap=8, hinh=1.
  TR 1-9.pdf PDF 1; TR 1-9.pdf PDF 2; TR 10-23.pdf PDF 1; TR 10-23.pdf PDF 2; TR 10.pdf PDF 1; TR 24-66.pdf PDF 40; TR 67-69.pdf PDF 4; TR 70.pdf PDF 2; TR 72.pdf PDF 2; TR 73.pdf PDF 2; TR 105.pdf PDF 1; TR 105.pdf PDF 2; TR 118-121.pdf PDF 5; TR 122-143.pdf PDF 2; TR 122-143.pdf PDF 4; TR 122-143.pdf PDF 6; TR 122-143.pdf PDF 8; TR 122-143.pdf PDF 10; TR 122-143.pdf PDF 12; TR 122-143.pdf PDF 14; TR 122-143.pdf PDF 16; TR 122-143.pdf PDF 18; TR 122-143.pdf PDF 20; TR 122-143.pdf PDF 22; TR 122-143.pdf PDF 24; TR 122-143.pdf PDF 26; TR 122-143.pdf PDF 28; TR 122-143.pdf PDF 37; TR 122-143.pdf PDF 38; TR 122-143.pdf PDF 39; TR 122-143.pdf PDF 40.

VT34: sáu tờ không thấy số in, chỉ có số viết tay; không phải sáu trang chưa xem. VT28 gồm bìa/trang trắng và các ảnh cắt mất chân. Toàn bộ đã được xem.

## 5. Danh sách рис./табл. nhận diện

Đếm **số hiệu khác nhau** có trong tiêu đề, không đếm mỗi tờ/ảnh lặp; loại trừ nhắc рис. trong tiêu đề danh mục linh kiện và bảng dây. Ở VT28 số hình bắt đầu lại trong phụ lục nên tổng số hiệu khác nhau không phải tổng số hình vật lý. Có tính chú thích hình dù vùng hình trống (VT34). Không tính số hình suy của sáu sơ đồ rời.

- VT34: **17 số рис.**, **32 số табл.**
  Рис.: 1, 301, 302, 303, 304, 305, 306, 307, 308, 402, 501, 502, 1201, 1202, 1203, 1204, 1205.
  Табл.: 1, 2, 301, 302, 303, 304, 305, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 701, 1001, 1002, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208.
- VT28: **34 số рис.**, **14 số табл.**
  Рис.: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 201.
  Табл.: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.

Mười ví dụ (năm mỗi sách):

| Sách | File / PDF | Số trang | Tiêu đề |
|---|---|---|---|
| VT34 | TR 1-55.pdf / 47 | 47 | Схема соединений блоков к КПА для автономной проверки блока А-313-3. Рис.301 |
| VT34 | TR 56-83.pdf / 3 | 58 | Диаграмма обмена информацией блоков А-313-3 и А-313-2. Рис.304 |
| VT34 | TR 56-83.pdf / 7 | 62 | Временные соотношения сигналов управления, обеспечивающих коммутацию аналоговых сигналов и разовых команд. Рис.305 |
| VT34 | TR 85-140.pdf / 12 | 96 | Эскиз на доработку платы контроля и сигнализации ЕУ2.072.139. Рис.402 |
| VT34 | ẢNH SƠ ĐỒ/7.pdf / 1 | 345/346 | Временная диаграмма цикла работы блока А-313-3. Рис.307 |
| VT28 | TR 10-23.pdf / 6 | 5 | Устройство ввода, вывода и питания А-313-3. Общий вид. Рис.1; 1.4. Структурное построение; Структурное построение блока А-313-3. Рис.2 |
| VT28 | TR 10-23.pdf / 9 | 8 | Временная диаграмма цикла. Рис.4 |
| VT28 | TR 10-23.pdf / 12 | 11 | Генератор тактовых импульсов. Схема электрическая принципиальная. Рис.6 |
| VT28 | TR 24-66.pdf / 31 | 203 | Схема проверки блока А-313-3. Рис.201 |
| VT28 | TR 122-143.pdf / 32 | 130 | Преобразователь РК II. Маркировочный чертеж ВШ2.068.054-01 Д7. Рис.28 |

## 6. Kiểm chứng và chạy lại

Yêu cầu Python, Pillow, Poppler (`pdfinfo`, `pdftoppm`) trên PATH. Chạy từ root:

```powershell
python tmp/pdfs/review/a313-3/vt/kiemke_vt.py --render
python tmp/pdfs/review/a313-3/vt/kiemke_vt.py --check --duplicates
```

`--render` chỉ sinh ảnh thiếu, giữ trường đọc tay. Script chặn nguồn khác hash và CSV bị sửa song song; `--check` không ghi, assert số file/trang, khoá duy nhất, loại hợp lệ, đủ ảnh render và không còn CHUA_XEM. Render không stage, được ignore. Không chạy bằng Python `-O` vì sẽ bỏ assert.

Output kiểm cuối:

Lượt resume ngày 2026-10-23 đã phóng lại chú thích рис.7 và рис.12 VT28, sửa рис.12 thành «Временная диаграмма формирования запросов». Kiểm lại bằng script: số hiệu hình/bảng đúng các tổng ở §5; TR 122-143 có 23 ảnh nội dung và 17 trang trắng. `--check --duplicates` thoát mã 0 sau sửa CSV. Lần chạy `--render` trước checkpoint cũng thoát mã 0 và giữ nguyên byte của cả hai CSV.

```
FILES 55; SHA256 55/55; VT34 252 + ANH 7; VT28 170; PAGES 429; UNIQUE 429
CHUA_XEM 0
EMPTY_PRINTED_PAGE {'VT34': 6, 'VT28': 31}
CHECK OK
```

## 7. Giới hạn và phần chưa làm

Đã xem đủ 429 trang, nhưng chưa có bản chuẩn để chứng minh mọi số trang in đều đầy đủ. Sáu tờ VT34 chưa có chú thích рис. đọc trực tiếp; liên hệ với 1201–1205 vẫn là suy. Một số tiêu đề chỉ chép phần nhận diện đọc chắc, bỏ mã bản vẽ hoặc ký hiệu công thức quá nhỏ/mờ; không dùng CSV làm bản chép nguyên văn hoàn chỉnh. Chưa phân tích hoặc kiểm tra kỹ thuật mạch, không OCR toàn nội dung. Dhash có giới hạn với tờ cắt/xoay như đã nêu.

JARVIS chưa có project/coverage A313 đã đăng ký; không nạp tài liệu A32 sang kho khác trong S01. Chủ đề chờ nạp sau đăng ký: kiểm kê/hashes, quy ước số trang, tờ rời/thiếu/trùng, kiểm tra chạy lại. Checkpoint giữ cục bộ ngoài commit S01 theo giới hạn chỉ năm file của nhiệm vụ.
