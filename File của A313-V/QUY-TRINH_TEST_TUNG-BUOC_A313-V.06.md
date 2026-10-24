# QUY TRÌNH TEST TỪNG BƯỚC TẤM A313-V.06

Phiên bản 1.0 — 17/09/2026. Người dùng thực hiện trên bàn; trợ lý đọc kết quả, chọn phép đo tiếp theo và lập kết luận. Cơ sở: BV.22–BV.25 trong `BVTK-A313-V.06.pdf` và phân tích Rev.C trong `PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md`.

## 1. Cách thực hiện

**Bắt đầu Bài 00. Chỉ làm một bài hoặc một lượt kênh được giao, gửi kết quả rồi dừng. Không tự chạy hết tài liệu.** Các bài phía sau là kế hoạch đầy đủ để biết trước cần chuẩn bị gì. Nếu phát hiện bất thường, chuyển sang nhánh chẩn đoán phù hợp; sau sửa phải đo lại bài đã lỗi rồi mới tiếp tục.

Mỗi lần báo kết quả cần ghi mã bài, số hiệu tấm, nguồn và tín hiệu thực đo, điểm đo, đơn vị, cấu hình đầu dò, ảnh toàn màn hình máy hiện sóng nếu có. Không chỉ báo “đúng” hoặc “sai”. Có thể trả lời “không đo được” kèm lý do.

Trợ lý trả lời theo mẫu: **nhận xét → kết luận tạm thời → điểm còn chưa phân biệt → đúng một bài/lượt tiếp theo**. Không kết luận hỏng IC chỉ từ dạng sóng đầu ra. Muốn chốt linh kiện phải loại trừ nguồn, đường mạch, tải và các linh kiện cùng nút; trường hợp đo trong mạch chưa phân biệt được sẽ cần tháo một chân hoặc thay thử có kiểm soát khi đã tắt điện.

Các giá trị “dự kiến” dưới đây là tính theo sơ đồ, không phải toàn bộ dung sai nghiệm thu của nhà chế tạo. Sai số nhỏ được đánh giá cùng dung sai linh kiện, sai số thiết bị và tải thực; không dùng ngưỡng tự đặt để loại tấm.

## 2. Quy ước đấu nối áp dụng cho mọi bài

### 2.1. Nhận dạng chân trước khi đấu

`DC11.A5` nghĩa là hàng A, vị trí 5 của giắc DC11; `U19.10` nghĩa là chân 10 của U19. Chữ a/b của tên kênh trong tài liệu này tương ứng а/б trên sơ đồ.

Phải xác nhận hàng A/B/C và vị trí 1 bằng ký hiệu trên giắc, bản vẽ và đo thông mạch khi mất điện. **Không xác định số chân bằng cách nhìn ảnh rồi đếm theo trái/phải:** phía hàn và phía cắm có thể bị soi gương. Chân IC cũng phải xác định theo dấu định hướng và bản vẽ chân, không suy từ vị trí trên ảnh.

Các chân cùng nhóm dưới đây nối chung trên tấm. Dùng các tiếp điểm nguồn song song theo thiết kế bộ gá; đường đo tín hiệu chỉ cần một tiếp điểm đã xác minh. Không đưa những nguồn khác nhau vào các chân cùng nhóm.

### 2.2. Bốn đường nguồn nuôi — cấu hình P

| Đường | Điện áp DC so với GND | Chân trên tấm | Cách đấu cực nguồn cách ly phù hợp |
|---|---:|---|---|
| P+ | +12,6 V | DC12.A4/B4/C4 | Cực + đến nhóm A4; cực − đến GND |
| P− | −12,6 V | DC12.A3/B3/C3 | Cực − đến nhóm A3; cực + đến GND |
| PK | −23,0 V | DC12.A2/B2/C2 | Cực − đến nhóm A2; cực + đến GND |
| PL | +3,50 V | DC11.A3/B3/C3 | Cực + đến nhóm A3; cực − đến GND |
| GND | 0 V | DC11.A1/B1/C1, A31/B31/C31, A32/B32/C32; DC12.A1/B1/C1 và A30/B30/C30 đến A32/B32/C32 | Điểm chung của hệ thống đo và nguồn |

Đấu đảo cực như bảng chỉ áp dụng cho đầu ra cho phép nổi/cách ly và chịu được cách nối đó. Kiểm tra nối đất và khả năng mắc nối tiếp của nguồn trước. Sorensen DCS40-75E trong ảnh là một nguồn DC; ảnh không chứng minh có đủ bốn đường nguồn độc lập.

**Không cấp nguồn +5 V vào DC11.A2/B2/C2 hoặc +6,3 V vào DC11.A4/B4/C4:** các đường này không sử dụng trên tấm. Đặc biệt, nguồn +3,5 V ở DC11.A3 khác nguồn −12,6 V ở DC12.A3.

Giới hạn dòng, khả năng bật/tắt đồng bộ và cách bảo vệ phải được chốt từ thiết bị thực tế ở Bài 00, trước Bài 03. Hồ sơ chưa đủ để đặt một trị số giới hạn dòng áp dụng an toàn cho mọi bộ gá. Không lấy 18 lần dòng tĩnh một OA làm dòng tiêu thụ toàn tấm. Không tự thử thứ tự bật riêng từng rail; cặp ±12,6 V cần phối hợp, cấu hình bốn rail phải được xem xét trước khi bật.

**Phiếu cấu hình P phải điền trước lần cấp điện đầu:**

| Rail | Thiết bị/kênh cấp | Điện áp đặt | Giới hạn dòng đã chọn | Cách bật/tắt phối hợp |
|---|---|---:|---:|---|
| P+ | … | +12,6 V | … mA | … |
| P− | … | −12,6 V | … mA | … |
| PK | … | −23,0 V | … mA | … |
| PL | … | +3,50 V | … mA | … |

### 2.3. Tín hiệu tham chiếu — chỉ chọn một cấu hình

| Cấu hình | Đưa vào DC11.A5/B5/C5 so với GND | Mục đích |
|---|---|---|
| R0 | 0 V, nguồn phát ngắt và đầu vào nối GND | Kiểm tra nguồn; không bảo đảm chọn được pha nào |
| RAC | Sin 400 Hz, 5,00 V RMS, DC offset 0 V | Kiểm tra làm việc động; tương đương ±7,071 V đỉnh, 14,142 Vpp, T=2,500 ms |
| R+ | +5,00 V DC | Dự kiến giữ pha G+, đầu ra cùng dấu Vin |
| R− | −5,00 V DC | Dự kiến giữ pha G−, đầu ra ngược dấu Vin |

Máy California Instruments 2003RP trong ảnh đặt 5,0 V và 400,0 Hz tương ứng điện áp AC RMS và tần số. Chọn **một pha** và đường về tương ứng theo nhãn đầu ra/manual; đưa pha đó đến nhóm DC11.A5 và đường về đến GND sau khi xác minh cấu hình cách ly. **A5/B5/C5 của giắc là ba tiếp điểm cùng một tín hiệu, không phải ba pha nguồn.** Ảnh mặt trước chưa cho biết cọc đầu ra phía sau, không tự suy tên/số cọc.

R+/R− cần một nguồn DC cách ly phù hợp hoặc máy phát có chế độ DC offset thực sự, đo xác nhận tại chân vào. Không coi 2003RP là nguồn ±5 V DC. Tắt đầu ra và tháo hẳn dây nguồn AC trước khi chuyển sang nguồn DC; không mắc song song hai máy phát. Nếu chưa có nguồn DC phù hợp, báo ở Bài 00 để thiết lập phương án; phần kiểm tra tĩnh chưa được coi là đã hoàn thành.

Tài liệu máy: [2003RP User and Programming Manual, Rev.N](https://www.programmablepower.com/-/media/project/ameteksxa/basesite/ametekprogrammablepowerv2/power-documents-here/ac-power-sources/rp-series/manuals/2003rp-user-and-programming-manual-rev--n.pdf), mục SOURce:VOLTage. Phải đo điện áp thực tại tấm, không chỉ tin số đặt, nhất là ở mức thấp 5 V.

### 2.4. Ngõ vào/ra và thiết bị đo

Trong tất cả bài, trừ khi ghi khác:

- 16 đầu vào kênh DC12.A7/C7 đến A14/C14 nối GND. Khi thử một kênh, chỉ tháo dây nối GND của đúng đầu vào ấy rồi nối nguồn Vin; 15 kênh còn lại giữ 0 V.
- Các đầu ra DC12.A17/C17 đến A24/C24 để hở tải, chỉ nối DMM trở kháng cao hoặc đầu dò máy hiện sóng. Không nối đầu ra vào GND, nguồn phát hay ngõ vào 50 Ω.
- Vin là nguồn **DC** có thể đặt 0; +1; −1; +4; −4 V so với GND. Mỗi giá trị phải đo thực tại chân vào tấm. Nếu đảo dây để đổi dấu, tắt nguồn trước và chỉ dùng nguồn cho phép nổi.
- Máy hiện sóng: đầu dò ×10, khai báo ×10 đúng trong máy, đầu vào 1 MΩ, DC coupling; đo đúng kênh đang nối. Kẹp mass chỉ ở GND chung; không kẹp vào −23 V, −12,6 V, M, M̄ hoặc đầu ra. Chọn đầu dò chịu được toàn dải điện áp đang đo.
- Mọi đổi dây, gắn tải, chuyển giắc và đặt kẹp đo trong vùng chân IC dày phải thực hiện khi tắt nguồn. Dùng điểm hàn thuận tiện đã xác nhận cùng net nếu chạm chân IC dễ chập.
- Đo Ω/diode/thông mạch chỉ khi tất cả nguồn và máy phát đã tháo, tụ đã xả; kiểm tra bằng thang V trước. Không xả tụ bằng cách chập thẳng.
- Khi xuất hiện sai cực nguồn, nguồn vào chế độ giới hạn dòng kéo dài, điện áp sụp, nóng tăng nhanh, mùi hoặc khói: tắt toàn bộ, ghi hiện tượng, dừng bài. Không tăng giới hạn dòng để ép tấm chạy.

## 3. Bài 00 — Chuẩn bị và nhận dạng, CHƯA CẤP ĐIỆN

**Nguồn/tín hiệu:** tất cả OFF; chưa nối nguồn vào tấm. **Tải:** tháo tải ngoài.

1. Ghi số hiệu/phiên bản tấm, tình trạng ban đầu, lỗi được báo và việc đã sửa trước đây.
2. Chụp hai mặt tấm đủ rõ mã U/R/Q, hai giắc DC11/DC12 và dấu hàng/số chân. Nếu không thấy dấu định hướng, ghi rõ, chưa suy đoán.
3. Liệt kê nguồn dự kiến cấp bốn rail, số kênh, giới hạn dòng nhỏ nhất đặt được, đầu ra có cách ly hay không, khả năng tracking/bật đồng thời. Ghi nguồn tạo Vin DC và nguồn tạo tham chiếu ±5 V DC.
4. Ghi model DMM, đầu dò, số kênh oscilloscope; chụp đầu ra thực tế của 2003RP và cách nối hiện tại.
5. Chuẩn bị một điện trở tải 1 kΩ, ít nhất 0,5 W, dây gá và điểm GND chung. Chưa lắp tải.

**Báo cáo B00:** `Tấm=…; lỗi ban đầu=…; nguồn bốn rail=…; khả năng cách ly/đồng bộ/giới hạn dòng=…; nguồn Vin=…; nguồn ±5 V tham chiếu=…; máy đo=…; ảnh kèm=…; đã sửa=…`.

**Dừng:** trợ lý kiểm tra chiều giắc, phương án nguồn và điền cấu hình P. Thiếu thông tin chỉ dừng bước phụ thuộc thông tin ấy; không đấu thử để đoán.

## 4. Bài 01 — Kiểm tra nguội và bộ gá

**Nguồn/tín hiệu:** tháo tất cả. **Tải:** không tải, tháo dây máy đo/máy phát ngoài trước khi đo Ω.

1. Kiểm tra cháy, nứt, tụ hỏng, chân IC cong, mối hàn cầu, giắc oxy hóa; ghi đúng ký hiệu nghi ngờ.
2. Đo thông mạch xác nhận GND DC11.A1 ↔ DC12.A1 và các nhóm GND. Xác nhận DC11.A5/B5/C5 nối chung; không nhầm với DC12.A5.
3. Đo xác nhận từng nhóm chân nguồn ở §2.2 và dây bộ gá tương ứng. Kiểm tra dây nguồn không chập nhau do bộ gá.
4. Đo Ω giữa từng rail và GND ở cả hai chiều que; ghi giá trị ban đầu và sau khoảng 10 s. Đo thêm P+ ↔ P−. Tụ nạp và tiếp giáp bán dẫn có thể làm số thay đổi; tiếng beep đơn lẻ chưa đủ kết luận chập.
5. Kiểm tra R24 ghi 2,05 kΩ; R124 là điện trở 0 Ω ở nhánh tham chiếu U14. Không nhầm với R63=180 Ω ở đầu ra kênh 5a. Số đo trong mạch khác trị số chưa chứng minh điện trở hỏng.

| Cặp đo | Ω chiều 1 ban đầu / 10 s | Ω đảo que ban đầu / 10 s |
|---|---|---|
| DC12.A4 ↔ GND | … / … | … / … |
| DC12.A3 ↔ GND | … / … | … / … |
| DC12.A2 ↔ GND | … / … | … / … |
| DC11.A3 ↔ GND | … / … | … / … |
| DC12.A4 ↔ DC12.A3 | … / … | … / … |

**Báo cáo B01:** bảng trên, kết quả thông mạch, ảnh vùng nghi ngờ, mã DMM. Nếu có điện trở gần điện trở dây đo và không tăng theo thời gian, cần tách bộ gá/tấm để kiểm tra trước khi cấp điện. Không có một ngưỡng Ω chung để kết luận tất cả rail tốt.

## 5. Bài 02 — Đo nguồn và máy phát khi CHƯA NỐI TẤM

**Nguồn:** cấu hình P, đo ở đầu giắc bộ gá rời tấm. **Tham chiếu:** RAC, sau đó kiểm tra riêng R+/R−. **Vin:** kiểm tra riêng 0; ±1; ±4 V. Không nối các nguồn thử với nhau ngoài điểm chung đã duyệt.

1. Kiểm tra thực đo các đầu dây dự kiến đến DC12.A4=+12,6; A3=−12,6; A2=−23,0; DC11.A3=+3,50 V so với GND. Xác nhận cực tính bằng DMM.
2. Kiểm tra trạng thái ON/OFF phối hợp đã chốt và giới hạn dòng hiển thị. Nếu chưa chốt cấu hình P, chưa bật bộ gá.
3. Đo một pha 2003RP: CH2 nối dây tín hiệu dự kiến vào DC11.A5, mass GND; 2 V/div, 1 ms/div là thiết lập khởi đầu. Chọn phép đo Frequency, RMS và Peak-to-Peak trên CH2.
4. Dự kiến sin 5,00 Vrms, 14,14 Vpp, 400 Hz; khoảng cách hai đỉnh dương liền nhau 2,50 ms. Không dùng nghịch đảo Δt nếu hai cursor không bao đúng một chu kỳ. Ảnh trước của người dùng có Δt≈6,23 ms qua 2,5 chu kỳ, không có nghĩa tần số là 160,53 Hz.
5. Tắt/tháo AC. Đo riêng đầu dây nguồn R+ đạt +5 V DC và R− đạt −5 V DC. Đo riêng nguồn Vin tại từng mức.
6. Tắt tất cả trước khi nối tấm.

**Báo cáo B02:** `P+=…; P−=…; PK=…; PL=… V; I-limit từng rail=…; RAC RMS/Vpp/f/offset=…; R+=…; R−=…; Vin 0/+1/−1/+4/−4 thực đo=…; ảnh sóng=…`.

## 6. Bài 03 — Cấp nguồn tấm lần đầu, chưa đưa sin

**Nguồn:** P = +12,6/−12,6/−23/+3,5 V vào đúng chân §2.2, theo cấu hình đã duyệt. **Tham chiếu:** R0 ở DC11.A5. **Vin:** cả 16 kênh 0 V. **Đầu ra:** không tải.

1. Khi OFF, lắp tấm, các dây GND và kẹp đo. Bật theo phương án đã chốt B00/B02, theo dõi ngay dòng và điện áp. Ghi thời điểm đo, không sờ linh kiện khi đang cấp điện để dò nóng.
2. Đo bốn rail ngay tại giắc tấm; ghi dòng riêng từng rail lúc ổn định và có báo CC hay không.
3. Đo U19.7=+12,6 V, U19.1=−12,6 V, U19.4=0 V; lặp ở U14 và U34 để kiểm tra đường cấp tới các vùng xa. Đặt kẹp khi OFF, bật lại để đọc nếu không có điểm đo an toàn.
4. Đo DC12.A17 khi Vin=0. Chụp nếu có dao động hoặc ra gần rail. R0 chưa xác định pha, nên chưa dùng bài này để đánh giá chuyển mạch.

**Báo cáo B03:** bảng điện áp/dòng bốn rail; điện áp chân 1/4/7 của U14/U19/U34; Vo A17; hiện tượng nhiệt/CC/dao động. **Dừng nếu nguồn bất thường; chuyển D-P.**

## 7. Bài 04 — Tham chiếu 400 Hz khi đã nối tấm

**Nguồn:** P. **Tham chiếu:** RAC 5 Vrms/400 Hz vào DC11.A5, return GND. **Vin:** toàn bộ 0 V. **Tải:** không tải.

1. Khi OFF đổi R0 sang RAC. Bật theo cấu hình đã chốt, đo lại CH2 ở DC11.A5: RMS, Vpp, f, offset, hình sin.
2. Đo U14.9 so với GND: dự kiến sin cùng tần số, 0,517 Vrms, khoảng 1,462 Vpp.
3. Đo U15.9: dự kiến 0,640 Vrms, khoảng 1,811 Vpp. Ghi tỉ số so với điện áp tham chiếu thực đo; dự kiến tương ứng 0,1034 và 0,1280.
4. Quan sát sụt biên độ hoặc méo khi nối tấm. Không kết luận R24 đúng chỉ vì thấy xung 400 Hz ở bước sau.

**Báo cáo B04:** `A5 RMS/Vpp/f/offset=…; U14.9 RMS/Vpp=…; U15.9 RMS/Vpp=…; ảnh=…`. Sai nhánh nào chuyển D-G1.

## 8. Bài 05 — Ba đầu ra điều khiển chung

**Nguồn:** P. **Tham chiếu:** RAC 5 Vrms/400 Hz tại DC11.A5. **Vin:** tất cả 0 V. **Tải:** không tải; các chân sau chỉ ĐO, không cấp tín hiệu vào.

| Điểm đo | Dạng dự kiến |
|---|---|
| DC11.A6 (B6/C6 cùng net) | Xung 400 Hz, mức thấp gần 0 V, cao gần +3,5 V |
| DC11.A7 (B7/C7 cùng net), M | Xung 400 Hz, hai mức gần −23 V và +3,5 V |
| DC11.A8 (B8/C8 cùng net), M̄ | Xung 400 Hz, bù trạng thái M ở phần ổn định |

1. Đo từng tín hiệu: mức cao/thấp, chu kỳ, duty, có mất xung hay không. Với M/M̄, bắt đầu 5 V/div; không cắt mất phần −23 V khỏi màn hình.
2. Đo đồng thời M và M̄ để xác nhận phần ổn định đối nhau. Phóng to sườn nếu nghi chồng dẫn; không suy ra thời gian chồng dẫn từ datasheet đơn lẻ.
3. Đo đồng thời M tại A7 và xung tại A6. Đặt cursor ở hai sườn cùng chiều tương ứng, dùng mức giữa riêng của từng xung; dự kiến M sớm hơn khoảng 0,358 ms ở tham chiếu 5 Vrms. Ghi cả sườn lên và xuống. Đây là dự đoán mô hình, không phải cửa sổ dung sai nghiệm thu đã được phê duyệt.

**Báo cáo B05:** `A6 H/L/f/duty=…; A7 H/L/f/duty=…; A8 H/L/f/duty=…; M sớm/trễ A6 lên=… µs, xuống=… µs; ảnh đồng thời=…`. Sai chung chuyển D-G2, chưa chạy 16 kênh.

## 9. Bài 06+ và 06− — Xác nhận giữ pha tĩnh

Đây là **hai lượt riêng**, làm 06+ rồi gửi; chỉ làm 06− khi được giao. Cần xác nhận thực tế vì trạng thái khóa với chân đế thả nổi không được đảm bảo chỉ từ bảng datasheet.

**Nguồn:** P. **Vin:** toàn bộ 0 V. **Đầu ra:** không tải. **Tham chiếu:** tháo hẳn nguồn AC; 06+ cấp +5,00 V DC, 06− cấp −5,00 V DC vào DC11.A5 so với GND.

| Điểm | 06+ dự kiến | 06− dự kiến |
|---|---:|---:|
| U14.9 | +0,517 V | −0,517 V |
| U15.9 | +0,640 V | −0,640 V |
| U14.10 = H14 | −0,351 V | +0,351 V |
| U15.10 = H15 | +0,351 V | −0,351 V |
| DC11.A7 = M | +3,5 V | −23 V |
| DC11.A8 = M̄ | −23 V | +3,5 V |

Đo các giá trị trên bằng DMM, đồng thời kiểm tra M/M̄ bằng scope để chắc chắn là mức DC ổn định chứ không phải DMM đang lấy trung bình xung. H14 và H15 là **hai nút riêng**, không nối chúng với nhau.

**Báo cáo B06+/B06−:** `Vref thực=…; U14.9=…; U15.9=…; H14=…; H15=…; M=…; M̄=…; có dao động=…`.

## 10. Bài 07+ và 07− — Xác nhận đường khóa trên kênh 1a

Mỗi dấu là một lượt. **Nguồn:** P. **Tham chiếu:** R+ cho 07+, R− cho 07−, vào DC11.A5. **Vin:** +1,000 V DC vào DC12.A7; 15 đầu vào khác nối GND. **Đầu ra DC12.A17:** chỉ DMM/scope, không tải.

| Điểm đo | 07+ dự kiến | 07− dự kiến |
|---|---:|---:|
| DC12.A7 = Vin | +1 V | +1 V |
| U1.2, gate shunt | +3,5 V | −23 V |
| U2.6, gate nối tiếp | −23 V | +3,5 V |
| S = U2.7 = U1.3 = đầu R37 phía khóa | gần +1 V | gần 0 V |
| U19.10 | gần S, có sai lệch do dòng bias qua R37 | gần S |
| U19.9 | gần U19.10 khi vòng hồi tiếp làm việc | gần U19.10 |
| DC12.A17 | gần +1 V | gần −1 V |

Ghi số thực, không yêu cầu hai đầu OA bằng tuyệt đối. Nếu S sai mà gate đúng, cần phân biệt khóa với chập/rò/tải ở S; chưa kết luận ngay U1/U2 hỏng. Nếu S đúng mà Vo sai, chuyển D-K.

**Báo cáo B07+/B07−:** `Vin=…; U1.2=…; U2.6=…; S=…; U19.10=…; U19.9=…; Vo=…; ảnh nếu dao động=…`.

### Hướng dẫn thao tác chi tiết B07+ — chỉ kênh 1a

Mục tiêu: giữ trạng thái cùng dấu, đưa +1 V DC vào kênh 1a và kiểm tra tín hiệu đi qua khóa tới đầu ra. Mọi số đo dưới đây so với GND, không đo chênh giữa hai chân IC. B07+ dùng tín hiệu DC ổn định, không dùng sin 400 Hz.

**Bước 1 — Tắt đầu ra các nguồn trước khi đổi dây.** Tắt và tháo dây máy cấp AC 400 Hz khỏi DC11.A5/B5/C5. Nếu đang giữ cấu hình B06−, đổi nguồn tham chiếu về +5,00 V DC khi đầu ra OFF. Không nối máy cấp AC và DC vào cùng đầu vào.

**Bước 2 — Giữ cách đấu bốn nguồn nuôi đã xác nhận:**

| Điểm cấp trên tấm | Điện áp DC so GND |
|---|---:|
| DC12.A4/B4/C4 | +12,6 V |
| DC12.A3/B3/C3 | −12,6 V |
| DC12.A2/B2/C2 | −23,0 V |
| DC11.A3/B3/C3 | +3,50 V |

GND chung có thể lấy tại DC12.A1, cùng net DC11.A1. Không yêu cầu đo lại nguồn đã được xác nhận.

**Bước 3 — Đấu hai tín hiệu DC độc lập:**

| Tín hiệu | Mức đặt | Dây tín hiệu tới | Dây về |
|---|---:|---|---|
| Tham chiếu giữ pha G+ | +5,00 V DC | DC11.A5 (B5/C5 cùng net) | GND |
| Vin kênh 1a | +1,000 V DC | DC12.A7 | GND |

Tháo dây nối GND trực tiếp của DC12.A7 trước khi nối nguồn Vin; không để nguồn Vin bị chập xuống GND. Giữ 15 đầu vào khác ở 0 V: DC12.C7; A8/C8; A9/C9; A10/C10; A11/C11; A12/C12; A13/C13; A14/C14. DC12.A17 là đầu ra, để hở tải, chỉ nối thiết bị đo trở kháng cao. Phân biệt DC11.A7 là M để đo, DC12.A7 mới là chân cấp Vin; không đưa nguồn +1 V vào DC11.A7.

**Bước 4 — Bật theo cấu hình nguồn đã dùng ở B06.** Khi bốn nguồn nuôi ổn định, cho phép hai nguồn tín hiệu DC xuất mức trên. Dùng DMM6500 ở VDC; que đen cố định GND, que đỏ lần lượt tới các điểm trong bảng. Chỉ đưa tín hiệu khi tấm đã có nguồn; tắt tín hiệu trước khi ngắt nguồn nuôi.

| Thứ tự | Que đỏ / đầu dò tín hiệu tới | Dự kiến B07+ | Ý nghĩa |
|---|---|---:|---|
| 1 | DC11.A5 | +5,00 V DC | Đúng tham chiếu giữ pha |
| 2 | DC12.A7 | +1,000 V DC | Vin thực tại tấm |
| 3 | DC11.A7, rồi U1 chân 2 | Cả hai gần +3,5 V DC | M tới gate khóa shunt |
| 4 | DC11.A8, rồi U2 chân 6 | Cả hai gần −23 V DC | M̄ tới gate khóa nối tiếp |
| 5 | U2 chân 7 **hoặc** U1 chân 3 **hoặc** đầu R37 phía khóa | Gần +1 V DC | Cùng một nút S, chỉ cần đo một vị trí |
| 6 | U19 chân 10, cũng là đầu R37 phía OA | Gần +1 V DC | Đầu vào không đảo sau R37 |
| 7 | U19 chân 9 | Gần điện áp chân 10 | Đầu vào đảo, kiểm tra hồi tiếp |
| 8 | DC12.A17 | Gần +1 V DC | Đầu ra kênh 1a cùng dấu Vin |

Nếu bước 1–4 sai rõ rệt, dừng tại đó và gửi số, chưa suy lỗi tầng khuếch đại. Nút S nằm trước R37; U19.10 nằm sau R37, không coi là cùng net. Không yêu cầu các số gần +1 V bằng đúng 1,000 V; ghi nguyên số đo để đánh giá offset và sụt áp.

**Bước 5 — Kiểm tra có thật sự giữ mức DC.** Giữ nguyên tín hiệu, scope DC coupling, đầu vào 1 MΩ, đầu dò ×10 và khai báo khớp. Kiểm tra M/M̄ và DC12.A17: phải là mức ổn định, không tiếp tục chuyển qua lại 400 Hz. Với OUT có thể bắt đầu 500 mV/div, 1 ms/div và đặt vị trí để thấy +1 V. Với M/M̄ dùng khoảng 5 V/div, chỉnh vị trí phù hợp. Nếu khó tiếp cận chân IC, tắt đầu ra nguồn trước khi đặt/đổi kẹp rồi bật lại theo cấu hình cũ; không rê đầu dò qua các chân sát nhau khi đang cấp điện.

**Gửi kết quả rồi dừng, chưa chuyển R−:**

```text
B07+ kênh 1a, không tải
DC11.A5 = … V
DC12.A7 = … V
DC11.A7 / U1.2 = … / … V
DC11.A8 / U2.6 = … / … V
S (đo tại …) = … V
U19.10 = … V
U19.9 = … V
DC12.A17 = … V
M/M̄ và OUT ổn định DC hay có xung/dao động: …
```

Sau khi B07+ được đánh giá, B07− giữ Vin=+1 V ở DC12.A7 và chỉ đổi tham chiếu DC11.A5 sang −5 V DC khi nguồn tín hiệu OFF. Các mức dự kiến theo bảng đầu §10; không tự thực hiện B07− trước khi báo B07+.

## 11. Bài 08 — Đặc tuyến DC của 16 kênh, từng kênh từng pha

**Một bài giao cụ thể có dạng B08-1a+ hoặc B08-1a−, không phải toàn bộ 16 kênh.** Thứ tự: 1a+, 1a−, 1b+, 1b− … 8b+, 8b−. Sau mỗi lượt gửi kết quả và chờ chẩn đoán.

**Nguồn mỗi lượt:** P. **Tham chiếu:** dấu + dùng R+ (+5 V DC); dấu − dùng R− (−5 V DC), đều vào DC11.A5. **Vin:** đưa lần lượt 0 → +1 → −1 → +4 → −4 → 0 V DC vào chân IN đúng hàng bên dưới. **Đầu ra:** đo chân OUT cùng hàng, không tải. 15 đầu vào khác nối GND.

Chỉ thay giá trị trên nguồn đã nối đúng; nếu cần đổi dây để đảo dấu, tắt trước. Sau mỗi mức chờ ít nhất 1 s, xác nhận scope ổn định rồi đọc DMM. Nếu ở ±1 V đã bão hòa/dao động/nóng, dừng, chưa tăng lên ±4 V.

| Kênh | IN DC12 | OUT DC12 | OA | Shunt / chân S / gate | Khóa nối tiếp / chân IN → S / gate |
|---|---|---|---|---|---|
| 1a | A7 | A17 | U19 | U1A / 3 / 2 | U2B / 5 → 7 / 6 |
| 1b | C7 | C17 | U20 | U1B / 7 / 6 | U2D / 12 → 14 / 13 |
| 2a | A8 | A18 | U21 | U1C / 10 / 9 | U3B / 5 → 7 / 6 |
| 2b | C8 | C18 | U22 | U1D / 14 / 13 | U3D / 12 → 14 / 13 |
| 3a | A9 | A19 | U23 | U4A / 3 / 2 | U5B / 5 → 7 / 6 |
| 3b | C9 | C19 | U24 | U4B / 7 / 6 | U5D / 12 → 14 / 13 |
| 4a | A10 | A20 | U25 | U4C / 10 / 9 | U6B / 5 → 7 / 6 |
| 4b | C10 | C20 | U26 | U4D / 14 / 13 | U6D / 12 → 14 / 13 |
| 5a | A11 | A21 | U27 | U7A / 3 / 2 | U9B / 5 → 7 / 6 |
| 5b | C11 | C21 | U28 | U7B / 7 / 6 | U8B / 5 → 7 / 6 |
| 6a | A12 | A22 | U29 | U7C / 10 / 9 | U9D / 12 → 14 / 13 |
| 6b | C12 | C22 | U30 | U7D / 14 / 13 | U8D / 12 → 14 / 13 |
| 7a | A13 | A23 | U31 | U10A / 3 / 2 | U11B / 5 → 7 / 6 |
| 7b | C13 | C23 | U32 | U10B / 7 / 6 | U11D / 12 → 14 / 13 |
| 8a | A14 | A24 | U33 | U10C / 10 / 9 | U12B / 5 → 7 / 6 |
| 8b | C14 | C24 | U34 | U10D / 14 / 13 | U12D / 12 → 14 / 13 |

Mức ra dự kiến ở G+: 0, +1, −1, +4, −4, 0 V; ở G−: 0, −1, +1, −4, +4, 0 V. Đo actual Vin để loại sai số nguồn.

**Mẫu báo cáo cho MỖI lượt:**

```text
Bài B08-…; tấm …; ngày …
P+ / P− / PK / PL thực: … / … / … / … V
R+ hoặc R− thực tại DC11.A5: … V; M/M̄: … / … V
Kênh …; IN DC12.…; OUT DC12.…; không tải
Vin đặt | Vin thực (V) | Vo thực (V) | dao động/ghi chú
0       |              |             |
+1      |              |             |
−1      |              |             |
+4      |              |             |
−4      |              |             |
0 lại   |              |             |
```

Trợ lý tính gain từ hai điểm thực ±4 V: `G = [Vo(+4) − Vo(−4)] / [Vin(+4) − Vin(−4)]`; offset bằng điểm Vin=0 hoặc nội suy đúng dữ liệu; kiểm tra ±1 V có nằm trên cùng đường thẳng không. Pha âm có gain danh định −Rfb/Rin. Hai điện trở 1% riêng rẽ đã cho tỉ số khoảng 0,9802…1,0202, chưa tính OA và khóa; vì thế lệch 1% không tự động là hỏng. Ghi lệch ở cả hai dấu để phân biệt gain với offset. Không tự chỉnh điện trở để che lỗi chưa tìm được.

## 12. Bài 09 — Động 400 Hz, từng kênh

Thứ tự B09-1a … B09-8b; **mỗi lượt một kênh rồi báo**. **Nguồn:** P. **Tham chiếu:** RAC 5 Vrms, 400 Hz, offset 0 vào DC11.A5. **Vin:** 0 → +1 → −1 → +4 → −4 V DC vào IN của kênh ở bảng §11; 15 IN khác 0 V. **Đầu ra:** không tải.

1. Đo OUT với CH1, M tại DC11.A7 với CH2; dùng trigger M. Bắt đầu 1 ms/div, chỉnh V/div theo mức đang đo; chọn đúng nguồn phép đo Frequency.
2. Với Vin=0, ghi ripple/offset và nhiễu chuyển mạch. Với +1 V, kiểm tra có hai mức gần +1/−1 V và chu kỳ 2,5 ms. Khi M cao, OUT dự kiến cùng dấu Vin; M thấp thì ngược dấu.
3. Đổi Vin=−1 V: OUT đảo dấu tương ứng trong cùng pha. Chỉ tăng đến ±4 V khi mức thấp đã ổn. Với +4 V, hai vùng xác lập dự kiến gần +4/−4 V, Vpp khoảng 8 V nếu không tính xung nhọn ở sườn. Ghi riêng đỉnh xung nhọn và mức plateau.
4. Phóng to sườn để ghi overshoot, ringing, thời gian ổn định; không buộc sóng ra phải là sin hay vuông lý tưởng. Mạng hồi tiếp có Rfb·Cfb≈100 µs và đường truyền trực tiếp từ S; không mô tả toàn bộ sườn bằng một hàm mũ đơn giản.
5. Nếu cần dò: đo S tại chân trong bảng §11 đồng thời với OUT. Với Vin dương, S dự kiến chuyển giữa 0 và Vin. Sóng S đúng nhưng OUT sai hướng sang OA/đệm/hồi tiếp.

**Báo cáo B09-kênh:** `IN/OUT=…; Vref RMS/f=…; mỗi Vin thực=…; OUT mức cao/thấp/Vpp/f=…; pha theo M=…; overshoot/ringing=…; ảnh một khung toàn chu kỳ và một khung phóng sườn=…`.

RMS toàn dạng sóng ra không bằng RMS riêng thành phần cơ bản 400 Hz; không lấy số đo RMS bất kỳ để đối chiếu biên độ fundamental mà chưa biết chế độ đo.

## 13. Bài 10 — Khả năng cấp tải thuần trở, từng kênh

Chỉ làm sau khi kênh đó qua B08/B09. Thứ tự B10-1a … B10-8b, mỗi lượt một kênh.

**Nguồn:** P. **Tham chiếu:** RAC 5 Vrms/400 Hz tại DC11.A5. **Vin:** +1 → +4 → −4 V DC vào IN của kênh theo §11, các IN khác 0. **Tải:** một điện trở 1 kΩ ≥0,5 W từ OUT cùng hàng đến GND; tất cả OUT khác không tải. Tắt điện khi lắp/tháo.

1. Đo trị số tải khi rời mạch. Lắp tải, thử +1 V trước. Nếu ổn mới lên +4 và −4 V.
2. Đo plateau, dạng sườn, ringing, rail tại tấm, dòng nguồn; đối chiếu với không tải B09 ở cùng Vin.
3. Đo Y ở phía transistor của R_ra, OUT ở phía giắc; hai đầu dò cùng mass GND, lấy hiệu bằng Math hoặc đọc điện áp DC khi giữ pha. Không kẹp mass vào một đầu R_ra. `I_Rra=(Y−OUT)/R_ra`; dòng này bao gồm cả nhánh hồi tiếp, không chỉ dòng điện trở tải.
4. Ở plateau |OUT|≈4 V, riêng tải 1 kΩ lấy khoảng 4 mA; đây là tải kiểm tra ban đầu, không thay thế tải СКТ thực. Nếu có sụp một nửa chu kỳ, chuyển D-K, không giảm điện trở để “thử mạnh hơn”.

**Báo cáo B10-kênh:** `Rload thực=…; Vin=…; OUT H/L không tải và có tải=…; Y/OUT hoặc ảnh Math=…; dòng bốn rail=…; ringing/nhiệt=…`.

## 14. Bài 11 — Kiểm tra ảnh hưởng sang kênh khác

Làm từng kênh kích thích theo thứ tự §11, mỗi lượt báo riêng. **Nguồn:** P. **Tham chiếu:** RAC 5 Vrms/400 Hz. **Vin kênh kích thích:** chuyển 0 → +4 V DC vào IN ở bảng §11; 15 IN còn lại nối GND chắc chắn. **OUT:** tất cả không tải.

Đo OUT của 15 kênh còn lại lần lượt ở cả hai trạng thái Vin kích thích; ghi giá trị DC, Vpp và có thành phần 400 Hz hay không. So sánh với nền đã đo ở B09 Vin=0. Ghi mã kênh bị ảnh hưởng, không chỉ ghi “nhiễu”. Kiểm tra lại dây GND/đầu dò nếu tất cả cùng tăng nhiễu. Chưa có giới hạn xuyên kênh chính thức nên số đo nhỏ phải được đánh giá theo yêu cầu hệ thống, không tự coi mọi gợn nhỏ là hỏng.

**Báo cáo B11-kênh kích thích:** `IN=…; Vin 0/+4 thực=…; bảng 15 OUT: DC/Vpp trước–sau=…; ảnh kênh thay đổi nhiều nhất=…`.

## 15. Bài 12 — Tải thực và chạy đồng thời, chỉ sau khi biết tải

**Không tự nối tải СКТ chưa rõ thông số.** Trước bài này phải có sơ đồ nối tải, trở kháng ở 400 Hz, mức dòng cho phép, quan hệ pha, số kênh hoạt động đồng thời và tiêu chuẩn sai số của hệ thống. Tải cảm không thể thay bằng kết luận từ điện trở 1 kΩ.

Khi dữ liệu đủ, trợ lý điền phiếu sau thành một bài cụ thể rồi mới thực hiện. Điện áp nuôi vẫn P; tham chiếu vẫn RAC 5 Vrms/400 Hz tại DC11.A5. Mỗi Vin DC và OUT phải ghi bằng chân DC12 cụ thể từ §11; không tự nối nhiều OUT với nhau.

```text
B12 phiên bản được giao: …
Tải/model/sơ đồ: …; Z tại 400 Hz: …; dòng cho phép: …
Kênh …: Vin … V DC vào DC12.…; tải nối DC12.… tới …
Các kênh đồng thời khác: …; thứ tự kích thích: …
Giới hạn dòng nguồn và cách giám sát đã chốt: …
Thời gian chạy theo yêu cầu thử: …
Tiêu chí biên độ/pha/nhiệt/ringing theo tài liệu: …
Kết quả tại đầu, giữa, cuối thời gian chạy: …
```

Nếu chưa có thông tin này, kết luận chỉ ở phạm vi **chức năng trên bàn không tải và tải 1 kΩ**, chưa xác nhận đáp ứng tải làm việc thực. Không giữ toàn bộ tiến trình chẩn đoán linh kiện lại chỉ vì thiếu tải thực.

## 16. Các bài chẩn đoán rẽ nhánh — chỉ làm bài được giao

### D-P — Nguồn hoặc đường cấp nguồn bất thường

**D-P1:** tất cả OFF, tháo tấm khỏi bộ gá. Lặp B01 trên bộ gá và tấm riêng. Nếu bộ gá chập/sai chân, sửa bộ gá trước. Đo tụ lọc và đường rail theo BV.22; C41 nằm giữa +12,6 và −12,6 V, không mặc định mọi tụ đều xuống GND.

**D-P2:** chỉ khi đã loại chập và được giao, P với giới hạn dòng đã xác lập; R0, toàn bộ Vin=0, OUT hở. Đo cùng một rail tại giắc và chân nguồn OA vùng lỗi: Ux.7 là +12,6; Ux.1 là −12,6; Ux.4 là GND. Có điện ở giắc nhưng mất ở chân IC hướng đến đường mạch/mối hàn; có sụt toàn rail cần phân biệt tải chập với nguồn không đủ khả năng.

Không bơm dòng lớn vào rail hoặc tự dùng nguồn 75 A tìm điểm nóng. Nếu cần cô lập nhánh/linh kiện, trợ lý phải chỉ rõ điểm ngắt theo đường mạch thực tế và phép đo nguội tiếp theo.

**Báo cáo:** điểm đo, Ω/điện áp và trạng thái nguồn, vị trí nóng nếu có dữ liệu nhiệt, kết quả khi tháo bộ gá.

### D-G1 — Sai biên độ tín hiệu vào U14/U15

**Nguồn:** P; **tham chiếu:** RAC 5 Vrms/400 Hz tại DC11.A5; **Vin:** tất cả 0; **OUT:** hở.

Đo lần lượt DC11.A5, đầu vào/đầu ra R124 và R20 tới U14.9; nhánh U15 đo R119, R24 tới U15.9. Đo rail trước để loại nguồn sai. Nhánh U14 chia bởi R20=2,61 kΩ/R21=301 Ω, nhánh U15 bởi R24=2,05 kΩ/R25=301 Ω. Các cầu 0 Ω liên quan là R124/R117 và R119/R120.

Nếu có chỗ mất tín hiệu, OFF và đo thông mạch/điện trở tại chính đoạn ấy. Điện trở đo trong mạch nghi sai cần tách một chân để xác nhận, ghi vị trí và phục hồi sau đo. Đầu vào đã đúng nhưng điện áp ở chân OA bị kéo lệch cũng có thể do rò IC hoặc mối hàn, chưa chắc do điện trở chia.

**Báo cáo:** RMS/Vpp từng đầu R, giá trị Ω nguội nếu được giao; ảnh vị trí linh kiện.

### D-G2 — Mất xung, sai mức hoặc sai pha chung

Mỗi hàng dưới là một lượt đo, không tự làm hết. **Nguồn:** P; **tham chiếu:** RAC 5 Vrms/400 Hz; **Vin:** tất cả 0; **OUT:** hở. Điểm đo đều so GND. Khi cần giữ trạng thái, trợ lý giao riêng R+ hoặc R− tại DC11.A5 và vẫn giữ P/Vin/tải như trên.

| Lượt | Điểm đo cụ thể | Mục đích phân biệt |
|---|---|---|
| D-G2a | U16.1 hoặc .8; U16.7 hoặc .14 | Hai nguồn ngưỡng dự kiến −0,351 và +0,351 V; kiểm R22/R23 và R28/R29 cùng cầu 0 Ω nếu sai |
| D-G2b | U14.9/.10/.5; U15.9/.10/.5 | Input đã đúng? H14/H15 có đối nhau? OA có đổi trạng thái? Không coi đầu ra OA phải sát rail |
| D-G2c | U17.2, U17.3=A, U17.12=B | U14.5 qua R26=4,7 kΩ đến U17.2; A/B dự kiến luân phiên gần −23/+3,5 V; kiểm R32/R33=10 kΩ nếu mức sai |
| D-G2d | U16.2/.13 và U16.6/.9; H14=U14.10, H15=U15.10 | Gate nhóm A/D nhận B, nhóm B/C nhận A; ngưỡng H14/H15 được chọn ngược dấu, không nối chung |
| D-G2e | U15.5, hai đầu R30, U18.2, U18.1=M | Phân biệt OA, R30=4,7 kΩ, U18A và R35=10 kΩ kéo xuống −23 V |
| D-G2f | U18.13=M, U18.14=M̄, U18.12=+3,5 V | Phân biệt U18D, R36=10 kΩ và đường ra M̄ |
| D-G2g | U17.5/.10 và DC11.A6; U17.6/.9=A | Nhánh xung 0/+3,5 V: R34=1,8 kΩ kéo lên, U17B/C kéo xuống; đối chiếu đường nối giắc |

**Báo cáo từng lượt:** mức cao/thấp, tần số, ảnh đồng thời với tín hiệu điều khiển ở ngay trước khối. Có 400 Hz nhưng sai pha vẫn là dấu hiệu cần điều tra; R24 lắp sai lớn có thể còn xung nhưng sai cơ chế chuyển trạng thái.

### D-K — Một kênh sai

Chọn đúng dòng kênh ở §11 và §17. Ví dụ kênh 1a dùng U19/Q1/Q2/R37/R39; kênh khác thay đúng ký hiệu, không đo theo vị trí tương tự trên tấm.

**D-K1 — Kiểm tra đường khóa:** P; tham chiếu R+ rồi R−, **hai lượt báo riêng**; Vin=+1 V DC ở IN của kênh; OUT không tải. Đo Vin, M tại gate shunt, M̄ tại gate nối tiếp và S theo bảng §11. G+ dự kiến S≈Vin; G− dự kiến S≈0. Gate sai cục bộ thì dò đường từ DC11.A7/A8 tới gate trước khi kết luận khóa. Gate đúng/S sai: kiểm shunt rò, nối tiếp hở, tải bất thường tại S, cầu hàn. Không cấp điện áp ngoài trực tiếp vào gate để cưỡng bức trạng thái.

**D-K2 — Kiểm tra OA và hồi tiếp:** P; R+ hoặc R− đúng pha đang lỗi; Vin=+1 V DC; không tải. Đo Ux.1/.7/.4 trước, rồi S, Ux.10, Ux.9, Ux.5, Y trước R_ra và OUT sau R_ra. Nếu S đúng nhưng chân 10 khác nhiều, kiểm R_bias/đường vào. Nếu hai đầu vào OA chênh lớn và đầu ra bị ghim, kiểm hồi tiếp Rfb/Cfb, nguồn, tầng đệm và tải trước khi kết luận OA. Rfb/Cfb hồi tiếp từ OUT **sau** R_ra.

**D-K3 — Phân biệt NPN/PNP và R_ra:** P; giữ R+; Vin lần lượt +1 và −1 V DC, hai lượt nếu có bất thường; ban đầu OUT hở, sau đó chỉ lắp tải 1 kΩ ≥0,5 W khi trạng thái không tải ổn. Đo base chung=Ux.5; emitter chung=Y; collector NPN dự kiến +12,6 V, collector PNP dự kiến −12,6 V; OUT phía sau R_ra. Dùng BV.22/datasheet để xác định chân vật lý transistor, không giả định pinout theo vỏ giống nhau. Ghi `VBE_N=Vbase−Y`, `VEB_P=Y−Vbase`; khoảng 0,6–0,8 V chỉ gợi ý tiếp giáp silic đang dẫn, không phải tiêu chí duy nhất. Khi tải thuần trở lấy dòng dương nghi nhánh NPN nếu mất khả năng cấp dòng; chiều âm nghi PNP. Chưa áp dụng suy luận dấu điện áp này cho tải cảm.

**D-K4 — Xác nhận linh kiện khi mất điện:** tắt/tháo mọi nguồn, xả tụ, đo V trước. Đo R_in/R_fb/R_bias/R_ra/R_bal đúng bảng §17. Nếu đường song song làm số đo không rõ, tách một đầu linh kiện nghi ngờ rồi đo lại. Với transistor, đo B–E/B–C hai chiều và C–E sau khi đủ cách ly khỏi đường song song; chập/hở được xác nhận ngoài ảnh hưởng mạch mới chốt transistor. Với Cfb/Ccorr, đo chập/rò hoặc điện dung sau khi tách phù hợp; tụ không chập DC vẫn có thể gây lỗi động.

**D-K5 — Xác nhận sau sửa/thay:** ghi mã linh kiện cũ/mới, trị số, lý do thay và phép đo chứng minh. Lặp đúng bài lỗi với cùng nguồn/tín hiệu/tải, sau đó B08 hai pha, B09 và B10 của kênh đó. Nếu thay IC dùng chung, kiểm tra lại mọi kênh chung vỏ; nếu sửa bộ tạo xung/nguồn, kiểm tra lại tất cả kênh. Không thay nhiều linh kiện cùng lúc rồi khẳng định từng linh kiện đều hỏng.

**Báo cáo D-K:** `mã kênh/lượt=…; P/Vref/Vin/tải=…; các điểm đo và số thực=…; phép đo nguội/cách ly=…; đã thay gì=…; kết quả trước/sau=…`.

## 17. Bảng linh kiện phục vụ chẩn đoán chính xác

Đơn vị mặc định: R_bal/R_in/R_fb=10 kΩ; R_bias=4,7 kΩ; R_corr=56 Ω; R_ra=180 Ω; Cfb/Ccorr=10 nF. Q lẻ là NPN 2Т312Б; Q chẵn là PNP 2Т203Б. OA U19…U34 là 140УД1Б: chân 1=−12,6; 4=GND; 5=ra; 7=+12,6; 9=IN−; 10=IN+; 12=mạng hiệu chỉnh.

| Kênh | R_bal | R_in | R_fb | R_bias | R_corr | R_ra | Cfb/Ccorr | NPN/PNP | Khóa nhánh tải phụ |
|---|---|---|---|---|---|---|---|---|---|
| 1a | R4 | R85 | R86 | R37 | R38 | R39 | C1/C2 | Q1/Q2 | U2A |
| 1b | R5 | R87 | R88 | R40 | R41 | R42 | C5/C6 | Q3/Q4 | U2C |
| 2a | R6 | R89 | R90 | R43 | R44 | R45 | C7/C8 | Q5/Q6 | U3A |
| 2b | R7 | R91 | R92 | R46 | R47 | R48 | C9/C10 | Q7/Q8 | U3C |
| 3a | R8 | R93 | R94 | R49 | R50 | R51 | C11/C12 | Q9/Q10 | U5A |
| 3b | R9 | R95 | R96 | R52 | R53 | R54 | C13/C14 | Q11/Q12 | U5C |
| 4a | R10 | R97 | R98 | R55 | R56 | R57 | C15/C16 | Q13/Q14 | U6A |
| 4b | R11 | R99 | R100 | R58 | R59 | R60 | C17/C18 | Q15/Q16 | U6C |
| 5a | R12 | R101 | R102 | R61 | R62 | R63 | C19/C20 | Q17/Q18 | U9A |
| 5b | R13 | R103 | R104 | R64 | R65 | R66 | C21/C22 | Q19/Q20 | U8A |
| 6a | R14 | R105 | R106 | R67 | R68 | R69 | C23/C24 | Q21/Q22 | U9C |
| 6b | R15 | R107 | R108 | R70 | R71 | R72 | C25/C26 | Q23/Q24 | U8C |
| 7a | R16 | R109 | R110 | R73 | R74 | R75 | C27/C28 | Q25/Q26 | U11A |
| 7b | R17 | R111 | R112 | R76 | R77 | R78 | C29/C30 | Q27/Q28 | U11C |
| 8a | R18 | R113 | R114 | R79 | R80 | R81 | C31/C32 | Q29/Q30 | U12A |
| 8b | R19 | R115 | R116 | R82 | R83 | R84 | C33/C34 | Q31/Q32 | U12C |

Nhánh tải phụ dùng tiếp điểm A: Vin ở chân 3, chân 1 qua R_bal xuống GND; tiếp điểm C: Vin ở chân 10, chân 8 qua R_bal xuống GND. Gate A=2, C=9 nhận M̄. Nhánh này không nối thẳng tới S; hỏng nhánh có thể làm thay đổi tải nhìn từ nguồn Vin. Đo sụt Vin và hai đầu R_bal ở R+/R− nếu nghi lỗi phụ thuộc trở kháng nguồn.

Chân 4 và 11 của 168КТ2 trên tấm để không nối; không tự bổ sung dây “sửa nguồn”. Chân 12 OA đi qua R_corr rồi Ccorr xuống GND, không phải base transistor. Chỉ đo nút hiệu chỉnh nếu được giao và đầu dò phù hợp; chưa có biên độ chuẩn đủ tin cậy để loại OA bằng riêng điểm này.

Nhóm lỗi dùng để chọn điểm đo, chưa phải bằng chứng hỏng:

- 1a/1b/2a/2b chung shunt U1; 3a/3b/4a/4b chung U4; 5a/5b/6a/6b chung U7; 7a/7b/8a/8b chung U10.
- Cặp nối tiếp: U2=1a/1b; U3=2a/2b; U5=3a/3b; U6=4a/4b; **U9=5a/6a, U8=5b/6b**; U11=7a/7b; U12=8a/8b.
- Tất cả kênh sai cùng kiểu: đo lại nguồn, tham chiếu, M/M̄ và bộ gá trước khi đo từng OA.

## 18. Bài 13 — Chốt kết quả

Không cấp thêm nguồn cho việc lập biên bản; dùng các phép đo đã hoàn thành. Nếu cần chạy xác nhận, phải gọi đúng mã bài và cấu hình ở trên.

| Hạng mục | Kết quả / mã báo cáo chứng minh |
|---|---|
| Nhận dạng và bộ gá, B00–B02 | … |
| Bốn rail trên tấm, B03 | … |
| Chia áp tham chiếu, B04 | … |
| Xung/M/M̄ và pha, B05 | … |
| Giữ hai pha và đường khóa, B06/B07 | … |
| 16 kênh DC cả hai pha, B08 | … |
| 16 kênh động 400 Hz, B09 | … |
| 16 kênh tải 1 kΩ, B10 | … |
| Ảnh hưởng chéo, B11 | … |
| Tải thực/chạy đồng thời, B12 hoặc lý do chưa làm | … |
| Linh kiện/đường mạch lỗi đã xác nhận, phép đo cách ly | … |
| Sửa và kiểm tra lại | … |

Chốt một trong ba trạng thái, ghi rõ phạm vi:

1. **Đạt chức năng trên bàn trong điều kiện đã thử:** nguồn, điều khiển và 16 kênh làm đúng chức năng, số đo phù hợp các tiêu chí đã thống nhất từ tài liệu và sai số đo; liệt kê tải đã thử. Chỉ chốt đủ điều kiện làm việc hệ thống khi B12 và yêu cầu nghiệm thu tương ứng được thỏa mãn.
2. **Không đạt, lỗi đã xác nhận:** nêu kênh/chức năng, mã linh kiện hoặc đoạn đường mạch, số đo chứng minh và kết quả sau sửa nếu có. Nếu chỉ khoanh vùng được, ghi “nghi cụm …, chưa phân biệt linh kiện”, không điền tên IC như kết luận chắc chắn.
3. **Chưa đủ dữ liệu để kết luận:** ghi đúng bài còn thiếu, điểm đo còn thiếu hoặc tiêu chuẩn/tải chưa biết. Tách phần đã xác nhận tốt khỏi phần chưa kiểm tra.

**Tiến trình hiện tại: đã tổng hợp kết quả chức năng. B09/B10 được người thực hiện xác nhận đã thử lần lượt toàn bộ kênh, mức ra tương đồng; B11/B12 thử một số điểm không thấy vấn đề. Đánh giá tấm hoạt động tốt trong phạm vi đã thử. B08 chưa có bảng Vin/Vo định lượng; chưa coi B11/B12 là nghiệm thu đầy đủ mọi tổ hợp tải. Báo cáo Word: BAO-CAO_KIEM-TRA_A313-V.06.docx.**

### Nhật ký thực hiện — B00

- Tấm A313-V.06; người thực hiện không yêu cầu theo dõi số riêng.
- Đã nhận ảnh mặt linh kiện, thấy giắc DC11 và DC12; chỉ có ảnh mặt này. Ảnh không thay thế phép đo điện.
- Người thực hiện xác nhận tất cả nguồn/bộ cấp sẵn sàng và cách nối chuẩn, yêu cầu không đi sâu lại phần thiết lập. Tiếp tục trên cơ sở xác nhận này; chưa có số đo nguồn hay trị số giới hạn dòng được báo.
- DMM: Keithley DMM6500. Oscilloscope: Tektronix MSO44 theo thông tin người thực hiện.
- Tải đã chuẩn bị, chưa lắp.
- Bài được giao tiếp: B01 kiểm tra nguội; chưa giao cấp điện.

### Nhật ký thực hiện — B01/B02 và B03 ban đầu

- Người thực hiện xác nhận B01 và B02 đã thông qua toàn bộ; không gửi bảng số đo chi tiết. Không yêu cầu làm lại.
- Đã cấp nguồn B03. Ảnh nguồn Rohde & Schwarz HMP4040: CH1 12,600 V / 112,9 mA; CH2 12,600 V / 113,8 mA; CH3 23,000 V / 5,4 mA; CH4 3,500 V / 5,5 mA.
- Ảnh chỉ thể hiện điện áp giữa hai cực từng kênh nguồn; không tự chứng minh dấu điện áp so với GND tấm hoặc CH1/CH2 tương ứng rail nào. Chênh dòng CH1/CH2 là 0,9 mA, khoảng 0,8% giá trị trung bình. Hai dòng khá cân bằng nhưng chưa chứng minh tấm tốt.
- B03 còn cần: xác nhận R0 tại DC11.A5, các Vin=0 và OUT không tải; đo bốn rail tại giắc, chân 1/4/7 U14/U19/U34 và DC12.A17; ghi dòng có ổn định, CC hoặc nóng bất thường không. Chưa chuyển B04.

### Nhật ký thực hiện — B03 nguồn xác nhận / B04 cần xác minh điểm đo

- Người thực hiện xác nhận nguồn đúng tại tất cả điểm đo, yêu cầu không khảo sát nguồn sâu thêm. Không yêu cầu đo lại nguồn. Chưa có số Vo tại DC12.A17 khi Vin=0 được báo riêng.
- Ảnh được người thực hiện gán U14.9: CH1 Amplitude 19,67 V, Frequency 400,0 Hz, xung vuông; cursor mức khoảng +10,409/−9,196 V.
- Ảnh được gán U15.9: CH1 Amplitude 19,73 V, Frequency 400,0 Hz, xung vuông; cursor khoảng +10,637/−9,160 V. Amplitude tự động là độ chênh mức cao/thấp, không phải Vrms hoặc biên độ một phía.
- Theo sơ đồ, ở tham chiếu sin 5 Vrms: U14.9 dự kiến sin 1,462 Vpp; U15.9 sin 1,811 Vpp. Hai ảnh giống dạng đầu ra comparator chân 5 hơn đầu vào chân 9, nhưng đây chỉ là giả thuyết vị trí đo, chưa xác nhận nhầm chân hay lỗi tấm. Không suy pha tương đối từ hai ảnh chụp riêng với trigger riêng.
- Lượt kế tiếp B04-X1: giữ nguồn và tham chiếu sin 5 Vrms/400 Hz, Vin các kênh=0, OUT hở; tắt điện xác định nút chung R20/R21 nối U14.9 và nút U14.5 phía trước R26 bằng thông mạch. Bật lại, đo hai nút so với GND bằng cùng đầu dò với hệ số khai báo khớp thực tế. Gửi dạng sóng và biên độ mỗi nút; nút R20/R21 dự kiến sin nhỏ, nút U14.5 có thể là xung vuông cỡ biên độ ảnh đã gửi. Chỉ sau kết quả này mới chọn bước tiếp.

### Nhật ký thực hiện — B04 xác nhận lại chân và lưu ảnh

- Người thực hiện xác nhận hai ảnh 19,67/19,73 V là U14.5/U15.5, không phải chân 9. Các ghi nhận nghi vấn trước đó được giải quyết bằng xác nhận này; không xem là lỗi phần cứng.
- Ảnh mới U14.9: dạng sin; CH1 Amplitude 1,361 V; cursor +673,441/−734,417 mV, ΔV khoảng 1,408 V. Phép đo Frequency báo Low amplitude; ảnh ở trạng thái Preview.
- Ảnh mới U15.9: dạng sin; CH1 Amplitude 1,675 V; cursor +808,812/−925,634 mV, ΔV khoảng 1,734 V. Frequency hiển thị 1,689 MHz kèm Low amplitude, không dùng làm tần số sin. Ảnh ở trạng thái Stopped.
- Không đồng nhất Amplitude tự động với Peak-to-Peak hoặc RMS của sin. Cursor chưa được xác nhận đặt đúng cực trị nên ΔV cũng chỉ là số đọc tại hai vị trí. Hai dạng sin phù hợp về hình dạng và thứ tự biên độ; chưa đủ chốt độ chính xác chia áp. Khi cần đánh giá định lượng, đo actual tham chiếu và hai chân 9 bằng cùng phép đo RMS/Peak-to-Peak, chỉnh thang đứng phù hợp và xác nhận chu kỳ khoảng 2,5 ms.
- Đã lưu nguyên bản sáu ảnh B00/B03/B04, kiểm tra SHA-256 khớp nguồn; xem [danh mục ảnh](KET-QUA-TEST_A313-V.06/README.md). Tên ảnh ghi mã bài, IC và chân đo; số Amplitude giữ đúng nhãn máy, không đổi thành Vpp.
- Bài tiếp theo B05-A6: P; sin 5 Vrms/400 Hz vào DC11.A5, các Vin=0, OUT hở; chỉ đo DC11.A6 so GND, dự kiến xung khoảng 0/+3,5 V, T≈2,5 ms. Gửi ảnh và mức H/L/chu kỳ; sau đó mới giao M/M̄.

### Nhật ký thực hiện — B05 ảnh riêng DC11.A6/A7/A8

- Đã lưu ba ảnh gốc theo tên bài/chân vào thư mục kết quả, SHA-256 bản sao khớp nguồn.
- DC11.A6: người thực hiện ghi 3,408 V; ảnh hiển thị CH1 Amplitude 3,480 V. Cursor H≈3,530 V, L≈58,995 mV. Dạng xung phù hợp mức 0/+3,5 V. Frequency tự động 351,3 kHz không phù hợp chu kỳ xung lớn nhìn trên ảnh; có nhiễu trên plateau, chưa xác định nguyên nhân của số đo tự động. Cursor Δt=2,618 ms không đặt tại hai sườn cùng chiều tương ứng nên 381,97 Hz chưa là kết quả đo tần số hợp lệ. Chưa chốt tần số A6 bằng số này.
- DC11.A7 (M): Amplitude 26,29 V; Frequency 400,0 Hz; cursor L≈−23,075 V, H≈+3,155 V.
- DC11.A8 (M̄): Amplitude 26,35 V; Frequency 400,0 Hz; cursor L≈−23,212 V, H≈+3,190 V.
- Mức A7/A8 gần các rail dự kiến, đã thấy chuyển mạch 400 Hz. Hai ảnh lấy riêng theo trigger riêng không chứng minh cùng pha hoặc ngược pha. Chưa kết luận bộ điều khiển đạt hoàn toàn hay linh kiện hỏng. Chưa đo độ sớm M so A6.
- Lượt kế tiếp B05-M/Mbar: giữ P và RAC sin 5 Vrms/400 Hz vào DC11.A5; Vin các kênh=0, OUT không tải. Đo đồng thời CH1→DC11.A7, CH2→DC11.A8, cả hai mass về GND, đầu dò ×10 với khai báo khớp, DC coupling/1 MΩ; 5 V/div và 500 µs/div, chỉnh vị trí để thấy đủ hai mức. Trigger CH1 sườn lên, ngưỡng khoảng −10 V. Gửi ảnh hai trace chung một lần thu, đo T giữa hai sườn lên liên tiếp của CH1. Dự kiến khi A7 cao thì A8 thấp và ngược lại, T≈2,5 ms. Phóng to sườn sẽ được giao riêng nếu cần; ảnh toàn chu kỳ không đủ loại trừ chồng dẫn ngắn.

### Nhật ký thực hiện — B05 đo đồng thời A7/A8

- Ảnh mới người thực hiện xác nhận CH1 vàng=DC11.A7 (M), CH2 xanh=DC11.A8 (M̄). Lưu nguyên bản tại [ảnh A7/A8](KET-QUA-TEST_A313-V.06/B05_DC11_A7-vang_A8-xanh_Dong-thoi_400Hz.png), kiểm SHA-256 khớp nguồn. Dùng ảnh mới này cho phép đo đồng thời, không dùng ảnh một trace trong tin nhắn bị ngắt trước đó.
- CH1 Amplitude 26,27 V, Frequency 400,0 Hz; CH2 Amplitude 26,26 V, Frequency 400,0 Hz. Cursor CH2 tại hai vị trí cho khoảng +3,380 V và −22,872 V, ΔV≈26,252 V.
- Quan sát chung trục thời gian: A7 cao thì A8 thấp và ngược lại ở phần ổn định. Chức năng bù trạng thái phù hợp, T=1/400≈2,50 ms. Ảnh 1 ms/div không đủ xác nhận không chồng dẫn hoặc định lượng trễ ngắn tại sườn. Δt cursor 1,309 ms không phải phép đo trễ giữa hai kênh; 763,94 Hz từ 1/Δt không thay thế Frequency 400 Hz.
- Lượt tiếp theo B05-PHA: P giữ +12,6/−12,6/−23/+3,5 V theo §2.2; sin 5 Vrms/400 Hz tại DC11.A5; các Vin=0, OUT hở. Giữ CH1 tại DC11.A7, chuyển CH2 sang DC11.A6 khi tắt đầu ra nguồn để đổi kẹp. Hai mass GND; DC coupling, 1 MΩ, đầu dò ×10 khai báo đúng. CH1 khoảng 5 V/div, CH2 khoảng 1 V/div; 500 µs/div; trigger CH1 sườn lên mức khoảng −10 V. Đo Δt giữa sườn lên A7 tại mức giữa khoảng −10 V và sườn lên A6 tại khoảng +1,75 V; ghi rõ tín hiệu nào đi trước. Dự kiến A7 sớm khoảng 0,358 ms theo mô hình với sin 5 Vrms, không phải dung sai nghiệm thu cứng. Gửi ảnh cả hai trace và nếu được chu kỳ A6 giữa hai sườn lên liên tiếp. Sau kết quả mới chọn bước tiếp.

### Nhật ký thực hiện — Chốt B05/B06, giao B07+

- Người thực hiện chấp nhận các thông số còn lại của B05 và kết luận B05 tốt. Phần chưa có số đo/ảnh, gồm pha A7 so A6, được ghi là người thực hiện chấp nhận; không tự điền giá trị 0,358 ms thành kết quả thực đo.
- Người thực hiện xác nhận đã đo B06 và tín hiệu tốt. Ghi B06 đạt theo xác nhận, không có số đo từng chân/ảnh bổ sung; không yêu cầu làm lại.
- Theo yêu cầu hướng dẫn rõ hơn, đã bổ sung thao tác B07+ chi tiết tại §10: bốn nguồn nuôi, +5 V DC giữ pha tại DC11.A5, +1 V DC vào DC12.A7, đầu ra DC12.A17 hở tải, trình tự đo từ gate tới S và OA. Chỉ giao B07+, chờ báo cáo trước B07−.

### Nhật ký thực hiện — B07+ đạt, giao B07−

- Người thực hiện xác nhận tất cả giá trị đo của B07+ đúng như bảng dự kiến. Ghi đạt theo xác nhận, không có số đo chi tiết/ảnh bổ sung; các mức danh định dưới đây không phải số thực đo được cung cấp.
- Điều kiện bài đã giao: bốn nguồn nuôi P; tham chiếu +5 V DC tại DC11.A5; Vin=+1 V DC tại DC12.A7; các Vin khác=0; OUT không tải. Kết quả được xác nhận phù hợp: M/gate U1.2 cao gần +3,5 V; M̄/gate U2.6 thấp gần −23 V; S, U19.10, U19.9 và OUT DC12.A17 gần +1 V. Đường truyền pha cùng dấu kênh 1a phù hợp tại mức thử này; chưa kết luận toàn dải hoặc toàn tấm.
- Bài tiếp theo B07−: tắt các đầu ra tín hiệu trước, tắt nguồn nuôi khi cần đổi dây. Giữ bốn nguồn nuôi đã xác nhận và cách đấu GND; đổi riêng tham chiếu DC11.A5 từ +5 sang −5,00 V DC, không dùng sin. Giữ Vin DC12.A7=+1,000 V DC, không đổi dấu Vin. Các đầu vào còn lại nối GND, DC12.A17 không tải. Bật nguồn nuôi theo cấu hình cũ rồi bật tín hiệu.
- Đo VDC so GND theo thứ tự: DC11.A5≈−5 V; DC12.A7≈+1 V; DC11.A7 và U1.2≈−23 V; DC11.A8 và U2.6≈+3,5 V; S=U2.7≈0 V; U19.10≈0 V (có sai lệch bias); U19.9 gần U19.10; DC12.A17≈−1 V. Nếu tham chiếu/Vin/gate sai rõ, dừng báo trước khi suy lỗi OA. Scope tại OUT, DC coupling/1 MΩ, 500 mV/div và 1 ms/div, chỉnh vị trí để thấy −1 V: dự kiến mức DC ổn định, không chuyển mạch 400 Hz.
- Chờ báo cáo B07− với số đo từng điểm và trạng thái đầu ra. Chưa giao B08, chưa tăng Vin lên ±4 V.

### Nhật ký thực hiện — B07− đạt, giao B08-1a+

- Người thực hiện xác nhận B07− có các giá trị gần bảng dự kiến, sai lệch không đáng kể. Ghi đạt theo xác nhận; chưa có số đo riêng để tính sai số. Không gán mức danh định làm số thực đo.
- Kênh 1a đã xác nhận chức năng cùng dấu và đảo dấu ở Vin=+1 V, không tải; chưa xác nhận đặc tuyến toàn dải hoặc các kênh khác.
- Lượt tiếp theo B08-1a+: giữ nguồn P, OUT DC12.A17 không tải, 15 đầu vào khác=0; đổi tham chiếu DC11.A5 về +5,00 V DC (tắt tín hiệu trước khi đổi, tắt nguồn nuôi nếu cần đổi dây). DC12.A7 nhận Vin lần lượt 0 → +1 → −1 → +4 → −4 → 0 V DC. Bật nguồn nuôi trước tín hiệu. Không dùng sin 400 Hz. Xác nhận M=DC11.A7 gần +3,5 V, M̄=DC11.A8 gần −23 V sau đổi pha, không lặp đo các chân nội bộ đã đạt B07 nếu chưa có bất thường.
- DMM VDC, que đen GND DC12.A1; mỗi mức chờ ít nhất 1 s, đo Vin thực tại DC12.A7 rồi Vo thực tại DC12.A17. Scope đầu ra DC coupling/1 MΩ, đầu dò đúng khai báo, khoảng 2 V/div và 1 ms/div; ghi dao động nếu có. Nếu ở ±1 V có đầu ra sai lớn/bão hòa/dao động, dừng trước ±4 V.
- Yêu cầu bảng số thực Vin/Vo sáu hàng để tính gain/offset/độ tuyến tính, không chỉ xác nhận gần đúng. OUT danh định lần lượt 0/+1/−1/+4/−4/0 V. Sau bảng này mới giao B08-1a−; chưa chuyển kênh khác.

### Nhật ký thực hiện — Tổng hợp B09 đến B12 và báo cáo chức năng

- Người thực hiện thông báo đã đo lần lượt hết các điểm/các kênh trong B09 và B10. B09: mức điện áp ra gần giống nhau. B10: có ảnh tại +1 V và +4 V; mức −1 V và −4 V có dạng tương tự nhưng đảo lại theo xác nhận. Không có bảng số riêng từng kênh; không tự gán ảnh đại diện cho kênh 1a hay kênh cụ thể khác.
- Ảnh B10 mức +1 V: CH2 Amplitude 1,975 V; cursor khoảng −1,082/+1,011 V, ΔV≈2,092 V. Frequency có Low amplitude; không dùng 883,06 Hz từ 1/Δt cursor làm tần số tín hiệu.
- Ảnh B10 mức +4 V: CH2 Amplitude 7,957 V; cursor +3,970/−3,821 V, ΔV≈7,791 V. Frequency hiển thị 400,0 Hz kèm Low amplitude; chỉ dùng cùng dạng sóng làm bằng chứng chức năng, không coi là phép chứng nhận tần số chính xác. Không dùng 763,94 Hz từ cursor làm tần số tín hiệu.
- Đã lưu hai ảnh nguyên bản trong thư mục KET-QUA-TEST_A313-V.06, tên có B10, mức Vin và nhãn kênh chưa ghi; bản sao SHA-256 khớp nguồn. Tải bài B10 theo quy trình là 1 kΩ ≥0,5 W; người thực hiện chưa gửi trị số tải thực đo. Không suy ra mã kênh từ giấy ghi “PC-24 08” trong ảnh.
- B11/B12: người thực hiện thử vài điểm và không thấy vấn đề. Ghi kết quả chọn mẫu, chưa có ma trận điểm, mô tả tải thực hoặc thời gian chạy. Không ghi thành đã thử đủ mọi kênh/mọi tải đồng thời.
- Chốt kết quả theo yêu cầu: tấm hoạt động tốt về chức năng trong phạm vi phép thử đã thực hiện; chưa phát hiện bằng chứng để chỉ định linh kiện hỏng. B08 chưa có số liệu chi tiết; không lập sai số gain/offset giả định.
- Đã lập báo cáo Word dưới 10 trang, trình bày vai trò .04 → .05 → .06 → ngoại vi, phân tích cụm tạo điều khiển và kênh điển hình, phương pháp thử, ảnh thực tế, ma trận phạm vi và kết luận có giới hạn phù hợp. Bằng chứng phân biệt số đo ảnh, kết quả người thực hiện xác nhận và mức lý thuyết.
