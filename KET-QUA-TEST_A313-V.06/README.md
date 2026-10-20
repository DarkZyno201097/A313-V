# Ảnh kết quả test A313-V.06

Ảnh gốc được sao chép từ các tệp người thực hiện gửi, không chỉnh sửa. Đã kiểm tra SHA-256 bản lưu khớp bản gốc. Mã bài theo quy trình ở thư mục cha. Ngày trên màn hình thiết bị không dùng làm ngày thực hiện đã xác minh.

| Bài | Điểm đo/nội dung | Số đọc | Ảnh |
|---|---|---|---|
| B00 | Mặt linh kiện, DC11/DC12 | Nhận dạng tấm | [Ảnh](B00_Mat-linh-kien_DC11_DC12.png) |
| B03 | Nguồn HMP4040, CH1–CH4 | 112,9 / 113,8 / 5,4 / 5,5 mA | [Ảnh](B03_Dong-nguon_HMP4040_CH1-CH4.png) |
| B04 | U14 chân 5, đầu ra | Amplitude 19,67 V; 400 Hz | [Ảnh](B04_U14_chan-5_OUT_Amplitude-19p67V_400Hz.png) |
| B04 | U15 chân 5, đầu ra | Amplitude 19,73 V; 400 Hz | [Ảnh](B04_U15_chan-5_OUT_Amplitude-19p73V_400Hz.png) |
| B04 | U14 chân 9, đầu vào | Amplitude 1,361 V; cursor ΔV≈1,408 V | [Ảnh](B04_U14_chan-9_IN_Amplitude-1p361V.png) |
| B04 | U15 chân 9, đầu vào | Amplitude 1,675 V; cursor ΔV≈1,734 V | [Ảnh](B04_U15_chan-9_IN_Amplitude-1p675V.png) |
| B05 | DC11.A6, xung | Amplitude trên ảnh 3,480 V; người thực hiện ghi 3,408 V | [Ảnh](B05_DC11_A6_Amplitude-3p480V.png) |
| B05 | DC11.A7, M | Amplitude 26,29 V; 400 Hz | [Ảnh](B05_DC11_A7_M_Amplitude-26p29V_400Hz.png) |
| B05 | DC11.A8, M̄ | Amplitude 26,35 V; 400 Hz | [Ảnh](B05_DC11_A8_Mbar_Amplitude-26p35V_400Hz.png) |
| B05 | Đồng thời A7 vàng / A8 xanh | Amplitude 26,27 / 26,26 V; cả hai 400 Hz; bù trạng thái | [Ảnh](B05_DC11_A7-vang_A8-xanh_Dong-thoi_400Hz.png) |
| B10 | Đầu ra khi Vin=+1 V; chưa ghi mã kênh | CH2 Amplitude 1,975 V | [Ảnh](B10_OUT_Vin-plus1V_Amplitude-1p975V_Kenh-chua-ghi.png) |
| B10 | Đầu ra khi Vin=+4 V; chưa ghi mã kênh | CH2 Amplitude 7,957 V | [Ảnh](B10_OUT_Vin-plus4V_Amplitude-7p957V_Kenh-chua-ghi.png) |

Hai ảnh chân 5 ban đầu được gọi nhầm là chân 9; người thực hiện đã xác nhận và sửa lại. Giữ đúng tên chân đã sửa trong tên tệp.

Hai ảnh chân 9 là dạng sin. Amplitude là tên phép đo trên máy, không tự đổi thành Vrms/Vpp. Phép đo tần số có cảnh báo Low amplitude; không lấy 1,689 MHz trên ảnh U15.9 làm tần số tham chiếu. B04 xác nhận được dạng tín hiệu, chưa chốt dung sai biên độ.

B05: các mức A6/A7/A8 gần dự kiến. Frequency tự động 351,3 kHz của A6 không đại diện chu kỳ xung lớn trên ảnh; cursor chưa đặt đúng một chu kỳ. Ảnh đồng thời mới đã xác nhận A7/A8 bù trạng thái ở phần ổn định, cùng 400 Hz; chưa đánh giá chồng dẫn ngắn tại sườn. Tiếp theo đo đồng thời A7/A6 để kiểm pha theo nhật ký trong file quy trình.

Cập nhật sau: người thực hiện chấp nhận phần còn lại B05, xác nhận B06/B07 đạt; B09/B10 đã thử toàn bộ kênh, các mức ra tương đồng. Hai ảnh B10 là ảnh đại diện, không thay thế số đo riêng từng kênh. Mức âm có dạng đảo lại theo xác nhận, chưa có ảnh riêng. B11/B12 mới kiểm tra chọn mẫu. Kết luận và phạm vi được tổng hợp trong BAO-CAO_KIEM-TRA_A313-V.06.docx ở thư mục cha.
