### 1. Tóm tắt (≤ 5 dòng)

- **Chưa tấm nào đủ căn cứ để xếp “Đủ” cho việc chép hoàn chỉnh Э3**: Y4 chưa thấy sơ đồ; các tấm khác còn vấn đề tờ gấp, định danh hoặc độ bao phủ ảnh.
- Có перечень bản giấy được lập danh mục cho **cả Y1–Y7**; Э4 cũng có bảng chân của cả bảy tấm.
- Đã kiểm tra sự tồn tại của ảnh theo CSV và mở sáu ảnh đại diện; các nhận xét còn lại được ghi rõ là theo danh mục.
- Đề xuất chép: **Y7 → Y5 → Y3 → Y2 → Y1 → Y6 → Y4**, đồng thời yêu cầu bổ sung sơ đồ Y4 trước.
- Căn cứ tổng hợp: `DANH-MUC_ANH_RE_A-313-3.md`, dòng 27–33, 64–72; `SO-DO-DAU-NOI_E4_A-313-3.md`, dòng 28–35.

### 2. Bảng Y1–Y7

Quy ước dẫn nguồn dưới đây đều tính từ **gốc worktree hiện tại**:

- **D** = `DANH-MUC_ANH_RE_A-313-3.md`.
- **T** = `tmp/pdfs/review/a313-3/kiemke/trang.csv`.
- **E** = `SO-DO-DAU-NOI_E4_A-313-3.md`.
- **C150/C151/C152** = `tmp/pdfs/review/a313-3/e4/p150.csv`, `p151.csv`, `p152.csv`.
- **PDF** = `A313 original/A-313-3.HDSDKT.pdf`; số trang PDF là chỉ số trang trong tệp.
- **Ảnh #n** tra tên tệp tại **T, dòng n+1**, nằm trong `ЕУ.048.002.РЭ_A313-3/`.

“Đủ” ở đây đòi hỏi xác định được tờ sơ đồ, có nội dung chụp trọn và перечень để đối chiếu. “Có перечень” không đồng nghĩa đã kiểm từng dòng hoặc có đủ bộ спецификация lắp ráp.

| Tấm | рис. | Trang РЭ | Ảnh | Перечень | Э4 | Mức đầy đủ (Đủ/Thiếu một phần/Thiếu) | Căn cứ |
|---|---|---|---|---|---|---|---|
| **Y1** | 10 | Э3: 179; tờ khác chưa rõ trang. ПЭ: 181–183. Trang 180 chưa thấy | Э3 #175 và #75; ПЭ #176–178 | Có bản giấy theo danh mục; chưa có trong phần cuối bản dịch đã đọc | Có У1П1/П2/П3, tr.150, #147 | **Thiếu một phần** | D:32, 64–72; T:76, 176–179; C150:6–182; PDF tr.89–90 |
| **Y2** | 9 | Э3: 175–176; ПЭ: 177–178 | Э3 #171–172; ПЭ #173–174 | Có bản giấy; bản dịch tr.88–89 | Có У2П1/П2/П3, tr.150, #147 | **Thiếu một phần** | D:31, 64–65; T:172–175; C150:183–360; PDF tr.88–89 |
| **Y3** | 6 | Э3: 158–161; ПЭ: 162–163; ảnh chụp lại chưa rõ trang | Э3 #155–158; tờ 1 chụp lại #231/#232; ПЭ #159–160 | Có bản giấy; bản dịch tr.80–82 | Có У3П1/П2/П3, tr.151, #148 | **Thiếu một phần** | D:28, 58, 64–65; T:156–161, 232–233; C151:108–283; PDF tr.79–82 |
| **Y4** | 5 | Chưa xác định trang Э3; số trang ПЭ chưa chốt | Chưa thấy ảnh Э3; ПЭ #137–139 | Có bản giấy theo danh mục; bản dịch tr.78–79 | Có У4П1/П2/П3, tr.151, #148 | **Thiếu** — thiếu nguồn Э3 | D:27, 70–72; T:138–140; C151:284–459; PDF tr.77–79 |
| **Y5** | 8 | Э3: 171–172; ПЭ: 173–174 | Э3 #167–168; ПЭ #169–170 | Có bản giấy; bản dịch tr.86–87 | Có У5П1/П2/П3, tr.151, #148 | **Thiếu một phần** | D:30; T:168–171; ảnh #167/#168 đã xem; C151:460–635; PDF tr.86–87 |
| **Y6** | 7 | Э3: 164–166; thiếu 167. ПЭ: 168–170 | Э3 #161–163; ПЭ #164–166 | Có bản giấy; bản dịch tr.83–85 | Có У6П1/П2/П3, tr.152, #149 | **Thiếu một phần** | D:29, 64–69; T:162–167; C152:161–336; PDF tr.82–85 |
| **Y7** | 11; lắp ráp 27 | Э3: 184; ПЭ: 185; lắp ráp: 241 | Э3 #180; ПЭ #179; lắp ráp #242 | Có; đã xem trực tiếp tiêu đề ПЭ рис.11 tại #179 | Có У7П1/П2, tr.152, #149 | **Thiếu một phần** — chưa xác nhận trọn tờ/khung tên | D:33, 49, 64–65; T:180–181, 243; C152:337–442; ảnh #179/#180 đã xem |

**Kiểm tra mới đối với CSV Э4:** script chỉ đọc xác nhận mỗi bảng П1/П2 của Y1–Y7 có đủ số chân 1–53, không trùng; П3 của Y1–Y6 có đủ 1–70, không trùng. Đây là **độ phủ số chân trong bản chép**, không xác nhận tên tín hiệu, cực tính hay địa chỉ nối đúng. Căn cứ: các đoạn C150/C151/C152 trong bảng; kết quả lệnh `INLINE_ASSERTS_PASS`.

### 3. Thiếu / chưa dùng được (mỗi dòng có căn cứ)

- **Y4:** chưa thấy Э3 рис.5; không thể dựng kết nối từ перечень và Э4 thay cho sơ đồ. Bản dịch chỉ còn tiêu đề hai tờ. **Căn cứ:** D:27, 70–71; PDF tr.77.
- **Y6:** danh mục ghi thiếu trang 167, “рис.7 tờ 3”; #161–163 nằm trong nhóm tờ gấp chụp thiếu. Riêng T ánh xạ **#161 → 164, #162 → 166, #163 → 165**; #161/#163 còn ghi “рис.7 ?”. Không được gán trang theo thứ tự ảnh. **Căn cứ:** D:29, 64–69; T:162–164.
- **Y1:** chưa thấy trang 180; #75 chưa đọc được số trang, #175 còn dấu hỏi về рис.10 trong CSV. Đã xem trực tiếp: #75 bị khuất/cắt phần bảng bên phải; #175 không có khung tên trong vùng chụp. Chưa chứng minh hai ảnh ghép lại đủ hai tờ. **Căn cứ:** D:32, 69, 72; T:76, 176; `ЕУ.048.002.РЭ_A313-3/20261021_084249.jpg` (#75), `20261021_102004.jpg` (#175).
- **Y2:** #171/#172 được danh mục xếp vào nhóm bị cắt mép/khung tên; CSV chưa đọc được số рис. trên chính ảnh. Độ mờ từng vùng **chưa xác minh trực tiếp trong T01**. **Căn cứ:** D:64–65; T:172–173.
- **Y3:** #156–158 được ghi nhận chụp thiếu; #231/#232 chỉ là ảnh chụp lại **tờ 1**, chưa có căn cứ coi chúng bù được phần thiếu của tờ khác. **Căn cứ:** D:28, 58, 64–65; T:232–233.
- **Y5:** dù không nằm trong danh sách cảnh báo D:65, ảnh #167/#168 đã xem đều không hiện khung tên; vùng trái sát mép ảnh, #168 có chữ nhỏ kém rõ và nếp gấp ngang. Chưa kết luận mất linh kiện cụ thể, nhưng chưa thể chứng nhận trọn tờ. **Căn cứ:** `ЕУ.048.002.РЭ_A313-3/20261021_101555.jpg` (#167, tr.171), `20261021_101653.jpg` (#168, tr.172); T:168–169.
- **Y7:** #180 cho thấy sơ đồ các ячейка và bảng П1/П2, nhưng không thấy khung tên; danh mục cũng cảnh báo ảnh này chụp thiếu mép. **Căn cứ:** D:64–65; `ЕУ.048.002.РЭ_A313-3/20261021_102209.jpg` (#180, tr.184).
- **Э4 còn dữ liệu chưa chắc:** ví dụ У1П1/1 chưa rõ địa chỉ; У2П2 có các hàng được gióng theo quy luật do ảnh cong; biểu thức У6П1/37–40 chỉ đọc gần đúng. Không được coi đủ hàng CSV là đủ dữ liệu đáng tin. **Căn cứ:** C150:6, 255–258; C152:197–200.
- **Bản dịch không thay được ảnh Э3:** phần đã trích có tên hình và bảng linh kiện, nhiều ký tự Việt/Nga bị mất khi lấy text. Nhận định “không còn nét vẽ” là ghi nhận của kế hoạch; T01 chưa render PDF để kiểm độc lập toàn bộ nhận định này. **Căn cứ:** PDF tr.77–90; `KE-HOACH_KIEM-TRA_A-313-3.md`:43–45.

**Các ghi nhận không đồng nhất cần giữ cả hai phía:**

- Kế hoạch ghi Y1/Y7 “thiếu danh mục”; danh mục ảnh ghi đã có ПЭ tại tr.181–183 và 185. Kế hoạch dùng bản dịch, danh mục dùng ảnh bản giấy; không được mang kết luận thiếu của bản dịch áp cho toàn repo. **Căn cứ:** `KE-HOACH_KIEM-TRA_A-313-3.md`:43–60; D:32–33.
- T ghi #137 đọc số viết tay “140”, trùng #133; D để số trang ПЭ Y4 chưa xác định. **Không chốt #137 là trang 140.** **Căn cứ:** T:138; D:16, 27.
- E:31 ghi ma trận tr.153–157 “chưa chép”, nhưng E:102–106 mô tả bản CSV đã chép; `PROJECT_HANDOFF.md` §11 cũng ghi đã chép. Các tệp ma trận hiện có, nhưng trạng thái “đã kiểm hết” không suy ra từ sự tồn tại đó. **Căn cứ:** E:31, 102–106; `tmp/pdfs/review/a313-3/e4/p153_157_matrix.csv`, `matrix_nets.csv`.
- Đường У1П1/39 ghi tới У14/66, trong khi bảng У14 có tín hiệu tương ứng ở chân 9 và chỉ tới chân 43. Giữ nguyên hai cách ghi để đối chiếu khối thật. **Căn cứ:** C150:29; E:77–81.

### 4. Cần xác minh

| Việc xác minh | Nguồn/đối tượng cần kiểm | Căn cứ |
|---|---|---|
| Tìm đủ hai tờ Э3 Y4, đọc mã bản vẽ và số tờ | Bản giấy рис.5; chụp toàn tờ và khung tên | PDF tr.77; D:27, 70–72 |
| Xác định #75 thuộc tờ nào; trang 180 có phải phần chưa chụp hay đã nằm trong ảnh khác | Bản giấy рис.10, đối chiếu #75/#175 | D:32, 69; T:76, 176 |
| Chốt các ảnh Y3/Y6 ứng với tờ nào, phần nào bị cắt | Khung tên và vùng chồng lấn của рис.6/7; bổ sung tr.167 | D:28–29, 64–69; T:156–164, 232–233 |
| Chốt độ bao phủ Y5/Y7; đọc rõ các vùng nếp gấp, mép ảnh | Bản giấy рис.8/11, đối chiếu #167/#168/#180 | Các ảnh đã xem nêu ở §3 |
| Chốt số trang ПЭ Y4 và quan hệ “trang viết tay / лист phụ lục” | #137–139 và bản giấy; không dùng một hệ số lệch trang chung | T:138–140; D:72 |
| Kiểm tên tín hiệu, dấu đảo, địa chỉ còn nghi vấn | Bản giấy Э4 tr.150–152, rồi đối chiếu nhãn/đường nối trên khối thật khi được giao | C150:6, 29, 255–258; C151:320–333; C152:197–200 |

### 5. Thứ tự đề xuất và lý do

Đây là **thứ tự chép theo dữ liệu hiện có**, chưa phải thứ tự kiểm tra phần cứng:

1. **Y7:** có Э3, ПЭ và bản lắp ráp; đã xem sơ đồ và ПЭ. Thuận lợi nhất để thử quy trình chép–đối chiếu, nhưng phải xác minh khung tên trước khi chốt. **Căn cứ:** D:33, 49; ảnh #179/#180.
2. **Y5:** có hai ảnh sơ đồ, ПЭ bản giấy và bản dịch để đối chiếu; ưu tiên kiểm độ phủ mép ảnh rồi chép. **Căn cứ:** D:30; PDF tr.86–87; ảnh #167/#168.
3. **Y3:** có ПЭ hai nguồn và ảnh chụp lại tờ 1; còn phải phân loại vùng thiếu trên các tờ khác. **Căn cứ:** D:28, 58, 64–65; PDF tr.80–82.
4. **Y2:** có hai ảnh sơ đồ và ПЭ hai nguồn, nhưng định danh trên ảnh và mép tờ còn chưa chắc. **Căn cứ:** D:31, 64–65; T:172–175; PDF tr.88–89.
5. **Y1:** có hai ảnh ứng viên và ПЭ, nhưng còn vấn đề trang 180, tờ #75 và vùng bảng bị khuất. **Căn cứ:** D:32, 69, 72; ảnh #75/#175.
6. **Y6:** thiếu trang 167, thứ tự ảnh không theo thứ tự trang, một số biểu thức Э4 chưa đọc chắc. **Căn cứ:** D:29, 69; T:162–164; C152:197–200.
7. **Y4:** chưa thể chép Э3 vì chưa tìm thấy sơ đồ. **Yêu cầu bổ sung Y4 ngay**, không đợi chép xong sáu tấm còn lại. **Căn cứ:** D:27, 70–71; PDF tr.77.

### 6. Lệnh/đã đọc những gì

**Trạng thái checkout đã kiểm:** nhánh `codex/y1-y7-audit`, HEAD `86074a739c597e276ac6503f7e4eb80d6d436c10`; `git status --short` đầu/cuối đều không có đầu ra.

**Tài liệu đã đọc:**

- `AGENTS.md`, `README.md`, `PROJECT_HANDOFF.md`.
- Danh mục ảnh; kế hoạch kiểm tra; tài liệu Э4; phần đầu tài liệu nguồn.
- Các đoạn hướng dẫn liên quan của tài liệu phân tích/quy trình tấm .06.
- `kiemke/trang.csv`; đầu `kiemke/kiemke.csv`; C150/C151/C152.
- Mẫu `e3/ric21_bom.csv`, `ric21_net.csv`; vị trí đọc/ghi trong `e4_check.py`, `e3_check.py`.
- PDF tr.73–90 bằng `pdftotext`.
- Sáu ảnh: **#75, #167, #168, #175, #179, #180**.
- Quy tắc JARVIS và skill tra cứu; tìm memory cục bộ nhưng không dùng ghi nhận tấm .06 làm bằng chứng cho Y1–Y7.

**Nhóm lệnh đã chạy:**

```powershell
git status --short
git branch --show-current
git rev-parse HEAD
git rev-parse --show-toplevel

Get-Content <file>
rg -n <pattern> <file>
rg --files -uu tmp/pdfs/review/a313-3
rg --files -uu
Get-Command python,py,pdftotext,markitdown -ErrorAction SilentlyContinue
py -0p

pdftotext -f 73 -l 90 -layout 'A313 original/A-313-3.HDSDKT.pdf' -
```

Đã chạy Python nội tuyến bằng `python -B -`, chỉ đọc: ánh xạ CSV sang tệp ảnh, kiểm sự tồn tại ảnh, thống kê bảng chân và assert độ phủ/không trùng số chân. Kết quả: **không thiếu tệp ảnh nào đã được kê trong CSV**, và `INLINE_ASSERTS_PASS`. Điều này không chứng minh mọi trang sách đều đã được chụp.

Các lần thử không thành công: Python thiếu `fitz`; pipeline PowerShell ban đầu làm hỏng ký tự Cyrillic; sửa mã nội tuyến sang Unicode escape rồi chạy lại thành công. Không lấy kết quả `exists=False` của lần lỗi mã hóa làm bằng chứng thiếu ảnh.

### 7. Phần chưa làm được và lý do

- Chưa kiểm từng linh kiện, net, toàn bộ ảnh hoặc từng ô перечень: T01 chỉ đánh giá độ đầy đủ và yêu cầu mở vài ảnh đại diện.
- Chưa xác nhận bộ **спецификация lắp ráp đầy đủ**; mới xác định được перечень và bản lắp ráp Y7 theo danh mục.
- Không chạy các script ghi CSV, không tạo báo cáo/checkpoint, không lưu memory hoặc cập nhật JARVIS: đúng phạm vi chỉ đọc và vai trò Executor.

AgentMemory và MarkItDown MCP bị cơ chế phê duyệt công cụ từ chối với thông báo `MCP tool call requires approval, but approval policy is never`; đã tiếp tục bằng tài liệu cục bộ và `pdftotext`.

**Chưa kiểm bản giấy hoặc khối thật. Rủi ro còn lại: có ảnh và đủ hàng CSV vẫn có thể thiếu mép sơ đồ hoặc đọc sai chân/tín hiệu.**