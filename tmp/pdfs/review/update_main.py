from pathlib import Path

root=Path('.')
p=root/'PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md'
s=p.read_text(encoding='utf-8')

def section(start,end,new):
    global s
    a=s.index(start); b=s.index(end,a)
    s=s[:a]+new.strip()+'\n\n---\n\n'+s[b:]

log=r'''
## 0. NHẬT KÝ PHẢN BIỆN (Rev. C)

**Ngày: 16/09/2026.** Phản biện độc lập từ BV.22, bắt đầu bằng dựng kết nối vector, sau đó kiểm ảnh 400 dpi. Không thực hiện phép đo trên phần cứng. Sáu kết luận khai thác tại §9 được giữ nguyên. `[XÁC MINH]` về topo nghĩa là xác minh trên bản vẽ; không thay thế kiểm tra trên mạch thật. Các giá trị lý tưởng luôn tách khỏi giới hạn nghiệm thu.

**Quy ước bằng chứng:** tọa độ `(x,y)` tính bằng pt từ góc trên trái trang 1, khổ 1190,64 × 842,04 pt. Ảnh: [kênh 1а](tmp/pdfs/review/channel1.png), [U14–U18](tmp/pdfs/review/generator.png), [lọc nguồn](tmp/pdfs/review/power.png), [DC11](tmp/pdfs/review/DC11.png), [DC12](tmp/pdfs/review/DC12.png). Bằng chứng số: [net hình học](tmp/pdfs/review/netlist.json), [tọa độ chữ](tmp/pdfs/review/text-coordinates.txt), [kiểm đủ 16 dòng](tmp/pdfs/review/channel-audit.csv), [tính toán](tmp/pdfs/review/calculations.json). Hai script cùng thư mục tái tạo kết quả và chạy các assertion về nút, kênh, trạng thái DC và số học.

| Mã | Khẳng định | Kết luận | Bằng chứng | Đã sửa ở mục |
|---|---|---|---|---|
| A1 | R38+C2 là mạng коррекция xuống mát | [XÁC MINH] | Chân 12 đi lên rồi sang R38; giao `(344,82)` với đường chân 5 không có chấm; chấm base ở `(347,7;81,8)` riêng biệt. C2 đầu dưới mang nhãn a. | §6.1, §6.3, §10.6 |
| A2 | Chân 5 lái base chung; emitơ chung qua R39 | [XÁC MINH] | Net hình học 2062: U19.5/base; net 2079: hai emitơ/R39 trái, chấm `(361,7;81,8)`; colector về ±12,6 V. | §6.1 |
| A3 | R86 và C1 hồi tiếp sau R39 | [XÁC MINH] | Net 2091: đầu phải R39, hai dây hồi tiếp lên trên, chấm `(393,3;81,8)`; khác net 2079 trước R39. | §6.1, §6.3 |
| A4 | Nhãn a là GND | [XÁC MINH] | a ở DC11 `(1134,7;392,7)`, DC12 `(1127,7;468,0)` cùng thanh nối ký hiệu корпус; a của 16 shunt, chân 4 và tụ коррекция lặp lại. C1 KHÔNG nối mát: đường chân 4 cắt đường C1 không chấm. | §0.1, §6.1 |
| A5 | U1A shunt, U2B nối tiếp, U2A–R4 tải phụ | [XÁC MINH] | U1A.3 = S; U1A.1 = a; U2B.5 = Vin, .7 = S; U2A.3 = Vin, .1 → R4 → a, vùng `(80…260,80…110)`. Ý đồ cân bằng tải xem E1. | §6.1, §6.3 |
| A6 | Hệ số +1/−1 | [XÁC MINH] | KCL: Vo=(1+k)S−kVin; S=Vin hoặc 0, k=R86/R85=1 danh định. Đây là mức xác lập; chuyển tiếp không phải bộ lọc thông thấp đơn giản. | §6.2–6.3 |
| A7 | Gate −23 V dẫn, +3,5 V ngắt | [KHÔNG ĐỦ DỮ LIỆU] | Datasheet gốc 168kt2.pdf tr.2 đo Ron với gate −15 V, đế +5 V; phù hợp suy luận gate âm dẫn. Đế tấm này thả nổi; chưa đo xác nhận hai mức trên toàn dải ±4 V. | §5.3, §12.2 |
| A8 | U14.10 và U15.10 chung N_ref | [BÁC BỎ] | Net 2097: U14.10 `(934,1;175,5)` ↔ U16A.3/U16B.5. Net 1872: U15.10 `(934,1;299,1)` ↔ U16C.10/U16D.12. Hai dây dọc x=916,6 tách bởi khoảng y=214,7…253,9. | §3, §5.2, §10.5 |
| B1 | Bảng chân DC11 | [XÁC MINH] | Crop DC11: theo dây đứng tới số chân, A/B/C1…8 đúng; X từ 9…30; GND 31…32. Không gán theo tâm chữ. | §2.1 |
| B2 | Bảng chân DC12 | [XÁC MINH] | Crop DC12: cả 32 dây tín hiệu khớp A/C7…14 và A/C17…24; nhãn xoay nằm bên trái dây. GND 30…32. | §2.2 |
| B3 | Toàn bộ 16 dòng ánh xạ kênh | [XÁC MINH] | 16/16 dòng CSV PASS; đối chiếu 8 crop ch-0/1-0/2/4/6, không chỉ suy từ công thức. Vị trí từng dòng có trong §0.1. | §7 giữ đủ bảng |
| B4 | Chia sẻ vỏ khoá, thứ tự U8/U9 | [XÁC MINH] | U27 tại `(656,7;70,5)` dùng U9A/B; U28 `(656,7;142,8)` dùng U8A/B; U29 dùng U9C/D; U30 dùng U8C/D. Các nhóm còn lại đúng. | §7.1 |
| B5 | Phân bố C35…C46, C41 nối chéo | [XÁC MINH] | Crop nguồn `(866…1022,38…110)`: C41 trên rail +12,6, dưới rail −12,6; C40 từ a tới −12,6; C42 từ −12,6 tới корпус. Các tụ còn lại khớp §4. | §4 |
| B6 | U17B/C song song | [XÁC MINH] | U17B.5/U17C.10 = xung400Hz; .7/.8 = GND; .6/.9 = A, vùng `(1020…1125,202…258)`. | §5.3 |
| B7 | Pinout 140УД1Б, chân 4 là общий | [XÁC MINH] | Datasheet gốc 140ud1B.pdf tr.1, bảng chân; BV.22 U19.4 có nhãn a. 12 ghi контрольный; vai trò коррекция được chứng minh bởi mạch ngoài. | §5.1; datasheet 02 |
| C1 | Hệ số chia U14 0,1034 | [XÁC MINH] | 301/2911=0,103400893; R124/R117=0 Ω. | §5.1 |
| C2 | Hệ số chia U15 0,1280 | [XÁC MINH] | 301/2351=0,128030625; R24=2,05 kΩ theo xác nhận thực tế. | §5.1 |
| C3 | Ngưỡng 0,3511 V | [SỬA LẠI] | 12,6×301/10801=0,351134 V đúng; là hai nguồn chia áp rồi chọn ra H14/H15 đối dấu, không phải một nút chung. | §5.2 |
| C4 | Ngưỡng quy đầu vào 3,396/2,743 V | [XÁC MINH] | Trị tuyệt đối 3,395852/2,742579 V trong mô hình danh định không tải; dấu/ngữ cảnh chuyển mạch xem §5.2. | §5.2 |
| C5 | Cả hai trễ; Δ=5,9°/9,5° | [BÁC BỎ] | H14/H15 đối dấu: U15 chuyển TRƯỚC zero, U14 chuyển SAU zero; phải CỘNG góc: 51,5228°/76,0441° = 357,797/528,084 µs. | §5.2, §10.5, §12 |
| C6 | RC 100 µs mô tả toàn bộ sườn ra | [SỬA LẠI] | RC=100 µs, fc=1591,55 Hz đúng. Vo=[(2+sτ)/(1+sτ)]S−Vin/(1+sτ); đường truyền trực tiếp từ S tạo bước tức thời trong mô hình lý tưởng. | §6.3, §10.6 |
| C7 | RC коррекция 0,56 µs, 284 kHz | [SỬA LẠI] | Tích RC=0,56 µs và 1/(2πRC)=284205 Hz đúng; không đủ suy ra cực vòng kín/băng thông hay biên độ chân 12. | §6.3, §10.6 |
| C8 | Dòng ngắn mạch ≈66 mA | [SỬA LẠI] | 11,9/180=66,111 mA chỉ là mô hình base lên tới rail; thực tế phụ thuộc swing OA, β, tải và giới hạn dòng. R39 không phải bảo vệ ngắn mạch. | §6.3, §11; datasheet 00/03/04 |
| C9 | Bỏ R37 gây lệch đầu ra 45 mV | [BÁC BỎ] | 9 µA×5 kΩ=45 mV quy đầu vào; noise gain=2 → đầu ra tới 90 mV do riêng Ib−. Không áp dụng cho R37 đứt hở. | §6.3, §10.4; datasheet 02 |
| C10 | Tải ≥400 Ω là đủ | [SỬA LẠI] | 4/10 mA=400 Ω chưa tính dòng hồi tiếp tới 0,4 mA và headroom trên 180 Ω; giới hạn bảo thủ dòng emitơ cho tải thuần trở >417 Ω, vẫn chưa đủ bảo đảm swing/ổn định. | §10.6, §12.2; datasheet 00/04 |
| C11 | Số lượng vỏ/khoá/OA/Q/tụ | [XÁC MINH] | 12×4=48=16×3; 18=16+2; 32=16×2; 34=16×2+2. Giữ nguyên sửa BOM đã chốt. | §8 |
| D1 | Đóng băng bằng ±5 V DC | [SỬA LẠI] | Mô hình topo cho trạng thái duy nhất ổn định: +5 → H14 âm/H15 dương → M cao → G+; −5 đảo lại. Không có cơ chế bắt buộc tự dao động. Chỉ đưa vào ATE sau xác nhận thực, xem §10.4. | §10.3–10.4, §11 |
| D2 | Ngưỡng +0,3%/−1%/đối xứng1%/offset50mV | [BÁC BỎ] | Hai R1% cho tỉ số 0,980198…1,020202; Vos×2 tới14mV đã vượt12mV tại4V; offset bảo thủ khoảng49,8mV theo giả thiết 9µA/2,5µA, chưa tính mọi lỗi. | §10.4; datasheet 02 |
| D3 | Dạng sóng TP1–TP8 | [SỬA LẠI] | TP3 sụt Ib×4,7k có thể42,3mV; TP5=Y±VBE khi Q dẫn; Y=Vo+180I; TP8 không đủ mô hình nội để dự đoán biên độ. RMS fundamental ≠ peak. | §10.6; datasheet 03 |
| D4 | Chẩn đoán hỏng khoá/R/Q | [SỬA LẠI] | Khoá hở để S nổi không bắt buộc DC ±Vin; Rfb hở thường bão hòa, Rin hở vẫn truyền S. R24=2,05MΩ vẫn có thể làm U15 lật theo H15 đổi dấu. | §9.1, §10.7, §11 |
| D5 | Dòng nguồn 100–200 mA | [SỬA LẠI] | 18×10mA=180mA chỉ giả thiết dòng IC; tài liệu gốc 140ud1B.pdf tr.2 ghi12mA ở±13,9V →216mA; còn dòng Q/tải/hồi tiếp. Chưa biết biến thể/lô thực. | §5.1, §10.3; datasheet 02 |
| E1 | R4 cân bằng tải, tránh răng cưa S&H | [SỬA LẠI] | Tải pha + là R4+Ron, pha − là Rin; cân bằng gần đúng có cơ sở KCL. Mục tiêu thiết kế và hiệu quả trên .05 là suy luận, không chứng minh chỉ từ BV.22. | §6.3 |
| E2 | Hàng B trống để chống xuyên nhiễu | [KHÔNG ĐỦ DỮ LIỆU] | B7…14/B17…24 thực sự bỏ trống, nhưng không có thuyết minh ý đồ hay đo xuyên nhiễu; cần hồ sơ thiết kế/đo với đồ gá. | §2.2 |
| E3 | C1 giảm sóng hài vào СКТ | [SỬA LẠI] | Giảm thành phần cao tần của nhánh hồi tiếp là suy luận hợp lý; có đường truyền trực tiếp S nên không triệt sườn hoàn toàn; mục đích với СКТ chưa được chứng minh. | §6.3 |
| E4 | R39 hạn dòng, cách ly tải dung | [SỬA LẠI] | Điện trở nối tiếp hạn chế dòng/cách ly tức thời; hồi tiếp sau R39 giảm tác dụng điện trở ra ở tần số thấp, không làm nó bằng0 và không bảo đảm ổn định tải dung. | §6.3 |
| E5 | Hai hệ số chia khác nhau cố ý tạo lệch pha | [SỬA LẠI] | Khác trị số là sự kiện; lệch pha còn do H14/H15 đối dấu. Ngay cả chia áp bằng nhau vẫn có khoảng sớm–trễ; ý đồ “cố ý” cần hồ sơ thiết kế. | §5.1–5.2 |
| E6 | Chọn Б15V/В25V vì swing26,5V | [BÁC BỎ] | Datasheet 168kt2.pdf tr.3 định mức điện áp so với подложка, không phải Vpp giữa drain/source. Đế đang thả nổi: không suy được biên an toàn 30−26,5=3,5V. | §5.3; datasheet 00/01 |

### 0.1. Kết nối độc lập và giới hạn phương pháp

Đọc được đúng **4422 đối tượng line nâu/đỏ**, nhưng chỉ **2121 đoạn có chiều dài >0,05 pt**; nhiều đối tượng là điểm dài0. Có **239 curve magenta**, không phải250; không có rect magenta bổ sung. Ghép đầu đoạn theo khoảng cách ≤0,78pt để vượt các khe xuất PDF khoảng0,3…0,7pt, nối tại chấm và rà10 T-junction: **546 thành phần hình học**. Ngưỡng ≤0,43pt cho1038 thành phần vì bỏ sót nhiều khe. Vì vậy số “~635 net” không phải chuẩn đúng/sai; số này phụ thuộc snap, điểm suy biến và cách ghép nhãn. Không tự nối mọi giao cắt hay gán nhãn bằng chữ gần nhất. Net hình học chưa gộp nhãn a/nguồn/М lặp trên trang; số hiệu net chỉ phục vụ tái kiểm script này.

Các T-junction được ghi tọa độ trong JSON và đối chiếu crop: đều thuộc chân nguồn/корпус. М và М̄ tại y=290,070 và293,085 vẫn khác net (1789/1532); giao dây R36 với М không có chấm. Ảnh quyết định những giao cắt quan trọng.

Netlist chức năng đã kiểm ảnh:

```text
VIN1 = U2A.3 = U2B.5 = R85 phía vào
GND(a) = U1A.1 = R4 phía trái = U19.4 = C2 phía dưới
S = U1A.3 = U2B.7 = R37 phía trái
U2A.1 -> R4 -> GND; S -> R37 -> U19.10
U19.9 = R85 phía phải = R86 phía dưới = C1 phía trái
U19.5 = Q1.B = Q2.B; Y = Q1.E = Q2.E = R39 phía trái
OUT1 = R39 phía phải = R86 phía trên = C1 phía phải
U19.12 -> R38 -> C2 -> GND   (tách khỏi U19.5)
Vref− = R22 phía phải = R23 phía phải = U16A.1 = U16C.8
Vref+ = R28 phía trái = R29 phía trái = U16B.7 = U16D.14
H14 = U14.10 = U16A.3 = U16B.5
H15 = U15.10 = U16C.10 = U16D.12
A = U17A.3 = U17D.13 = U17B.6 = U17C.9 = U16B.6 = U16C.9
B = U17D.12 = U16A.2 = U16D.13
```

Ranh giới kiểm16 dòng: cột trái x≈66…421, cột phải x≈410…765; y đầu các dòng trái ≈43;115,3;187,7;260,0;332,3;404,7;477,0;549,4, dòng phải cộng≈3,0pt. Mỗi vùng cao69pt. CSV ghi đủ linh kiện quan sát được của từng kênh. Chữ PDF `Rr63` được kiểm ảnh là R63. Đọc số chân đầu nối theo dây đứng (bước chân≈3,51pt), không lấy chữ nhãn lệch trái làm vị trí chân.

**Nguồn linh kiện:** ưu tiên bản PDF gốc cục bộ `Datasheet/168kt2.pdf` tr.1–3 và `Datasheet/140ud1B.pdf` tr.1–2. Bản 140ud1B.pdf là nhãn dòng **140УД1БВК**, khác tập thông số sổ tay cũ trong Rev. B; chưa xác nhận đồng nhất lô IC trên tấm. Không thay mọi giới hạn cũ bằng thông số ВК như thể đã đo. Thông số Iк 10mA của2Т203Б được đối chiếu với [thẻ nhà sản xuất trên Optochip](https://optochip.org/series/card/129200); pinout/điều kiện thử khoá có trong [datasheet nhà sản xuất 168КТ2](https://eandc.ru/pdf/mikroskhema/168kt2.pdf).
'''

s=s.replace('**Phiên bản:** Rev. B — 16/09/2026.', '**Phiên bản:** Rev. C — 16/09/2026. Phản biện độc lập và sửa topo U16, pha, sai số và quy trình test. Rev. B trước đó')
pos=s.index('## 1. VỊ TRÍ')
s=s[:pos]+log.strip()+'\n\n---\n\n'+s[pos:]
s=s.replace('Cấp mức "đóng khoá" cho U17/U18','Mức cao của tầng dịch mức; quy luật dẫn/ngắt cần xác nhận theo §5.3')
s=s.replace('hàng B bỏ trống (chống xuyên nhiễu giữa 2 kênh liền kề).','hàng B bỏ trống. Giảm xuyên nhiễu là giả thuyết về ý đồ thiết kế, chưa có bằng chứng định lượng (E2).')
s=s.replace('U14 (140УД1Б, so sánh Schmitt)','U14 (140УД1Б, Schmitt)')
s=s.replace('U15 (140УД1Б, so sánh Schmitt)','U15 (140УД1Б, ngưỡng đổi dấu)')
s=s.replace('mạng trễ ±0,351 V (hysteresis)','chọn H14/H15 đối dấu ±0,351 V')

section('### 5.2.','### 5.3.',r'''
### 5.2. U16 chọn HAI ngưỡng đối dấu, hồi tiếp Schmitt qua U14

**H14 và H15 là hai nút riêng**, không được chập chung khi làm đồ gá:

* H14 = U14 chân10 = U16A chân3 = U16B chân5.
* H15 = U15 chân10 = U16C chân10 = U16D chân12.
* R22 (10,5k từ −12,6V) và R23 (301Ω về GND) chia sẵn Vref−; nút này tới U16A.1/U16C.8.
* R28 (10,5k từ +12,6V) và R29 (301Ω về GND) chia sẵn Vref+; nút này tới U16B.7/U16D.14.
* A điều khiển U16B/C; B điều khiển U16A/D. Cặp A/B do U14→U17 tạo, không do U15.

Với giả thiết khoá dẫn khi gate âm (§5.3):

| U14.5 | A | B | Khoá dẫn | H14 | H15 |
|---|---|---|---|---|---|
| Âm | Cao | Thấp | U16A + U16D | −h | +h |
| Dương | Thấp | Cao | U16B + U16C | +h | −h |

`h = 12,6×301/(10500+301) = 0,351134 V` là giá trị danh định không tải. U16 chỉ chọn các nguồn đã chia áp; Ron không nối tiếp10,5k/301Ω để tạo tỉ số này. Ron và dòng vào OA gây thêm sụt áp sau bộ chia. Trở Thévenin mỗi bộ chia≈292,6Ω; nếu giả thiết Ron≤100Ω, Ib≤9µA thì riêng sụt do Ib có thể≈3,53mV. Thêm dung sai nguồn/R và Vos; không nghiệm thu theo ±0,351134V tuyệt đối.

U14 có hồi tiếp dương: khi đầu vào tăng vượt +h, đầu ra chuyển âm và H14 đổi từ +h sang −h, giữ trạng thái. U15 nhận ngưỡng **đối dấu với H14**, không phải một Schmitt độc lập có cùng hồi tiếp.

| Nhánh | Hệ số chia | Trị tuyệt đối ngưỡng tại chân9 | Trị tuyệt đối quy đầu vào |
|---|---|---|---|
| U14 | 0,103400893 | h | 3,395852 V |
| U15 | 0,128030625 | h | 2,742579 V |

**Diễn tiến nửa chu kỳ sin đi lên:** sau đỉnh âm, U14.5 dương nên H14=+h, H15=−h. U15 đổi sang âm khi sin còn âm tại −2,742579V → М lên cao. Qua zero rồi tới +3,395852V, U14 mới đổi sang âm → xung400Hz lên cao, H14=−h/H15=+h. Lúc này chân9 U15≈+0,435V đã lớn hơn+h, nên U15 không lật lại. Nửa chu kỳ đi xuống đối xứng.

| Chuẩn | Uđỉnh | U14 trễ sau zero | U15 sớm trước zero | М sớm hơn xung400Hz (hai sườn cùng chiều) |
|---|---|---|---|---|
| 5 Vrms | 7,071068V | 28,7015° | 22,8214° | **51,5228° = 357,797µs** |
| 5 Vđỉnh | 5V | 42,7789° | 33,2653° | **76,0441° = 528,084µs** |

`Δθ = asin(h/(k14·Uđỉnh)) + asin(h/(k15·Uđỉnh))` — **cộng hai góc**, không lấy hiệu. Đây là mô hình linh kiện lý tưởng, chưa gồm trễ OA/khoá và bất đối xứng. Duty50% chỉ là danh định với sin và ngưỡng đối xứng. Thực tế phải đo. Biên độ tại chân9 vẫn≈0,731Vđỉnh/0,905Vđỉnh khi chuẩn5Vrms.
''')
s=s.replace('> Hai nhánh cố ý **khác hệ số chia** (0,1034 và 0,1280) để hai xung ra có **điểm chuyển mạch lệch pha nhau** — xem §5.2.', '> Hai nhánh **khác hệ số chia** là sự kiện. Lệch pha còn do hai ngưỡng H14/H15 đối dấu; ý đồ lựa chọn trị số chưa có thuyết minh thiết kế (E5).')
s=s.replace('Tham số 140УД1Б: Uп = ±12,6 V, K_u = 1350…12000, I_vào ≤ 9 µA, U_ra ≥ 6 V, f_cắt ≈ 0,1 MHz.', 'Thông số sổ tay cũ dùng làm giả thiết tính: K_u=1350…12000, Ib≤9µA, ΔIb≤2,5µA, Vos≤7mV. PDF gốc cục bộ 140ud1B.pdf tr.2 cho dòng 140УД1БВК: A=2000…10500, Ib≤8µA, ΔIb≤1,5µA, Icc≤12mA ở±13,9V, swing +8/−6,3V với RL=5,05kΩ. Chưa xác nhận biến thể/lô trên tấm; không coi hai bộ giới hạn là một.')
s=s.replace('**Quy luật khoá 168КТ2:** khoá **DẪN khi chân затвор (điều khiển) ở mức âm (−23 V)**, **HỞ khi ở +3,5 V**.', '**Giả thiết làm việc của 168КТ2:** gate −23V dẫn, gate +3,5V ngắt. Có cơ sở từ điều kiện thử datasheet và topo nhưng **chưa xác minh trên tấm thật**; mọi bảng pha dưới đây phụ thuộc giả thiết này.')
s=s.replace('⇒ **М và М̄ là cặp bù, biên độ −23 V ↔ +3,5 V, tần số 400 Hz.**','⇒ **М và М̄ bù nhau ở trạng thái xác lập**, mức danh định −23V/+3,5V, 400Hz; mức cao có sụt do Ron và tải kéo xuống. Không có bằng chứng bảo đảm không overlap trong chuyển tiếp.')
s=s.replace('> М, М̄ và xung400Hz **được đưa ra DC11**', '> Định mức Б15V/В25V là điện áp so với подложка, không phải swing26,5V giữa hai đầu kênh. Chân11 thả nổi là sự kiện đã chốt; cơ chế phân cực bên trong và dự trữ điện áp thực chưa được chứng minh. Không tự nối chân11 để “sửa” mạch.\n\n> М, М̄ và xung400Hz **được đưa ra DC11**')

section('### 6.1.','## 7.',r'''
### 6.1. Sơ đồ chức năng đúng của kênh 1а

```text
Vin = ВЫХ.1А= ── R85 10k ──● N = U19.9 (−)
                           │
Vo = ВЫХ.1А== ── R86 10k ──┤
Vo ───────────── C1 10nF ──┘

Vin ── U2B(5→7) ──● S ── R37 4,7k ── U19.10 (+)
                  │
              U1A(3→1) ── GND(a)
Vin ── U2A(3→1) ── R4 10k ── GND(a)

U19.5 ── base chung Q1/Q2
Q1 collector → +12,6V; Q2 collector → −12,6V
Q1/Q2 emitơ chung = Y ── R39 180Ω ── Vo
U19.12 ── R38 56Ω ── C2 10nF ── GND(a)
U19.1 → −12,6V; U19.7 → +12,6V; U19.4 → GND(a)
U1A gate2 ← М; U2A gate2/U2B gate6 ← М̄
```

R38 không ở đường base. Nhãn a gần C1 thuộc đường chân4; C1 nối **N–Vo**, không nối mát. Hồi tiếp R86/C1 lấy **sau R39**.

### 6.2. Cơ chế ±1 ở trạng thái xác lập

| Pha | М | М̄ | U1A | U2A/U2B | S | Vo lý tưởng |
|---|---|---|---|---|---|---|
| P1 | +3,5V | −23V | Ngắt | Dẫn | Vin | +Vin |
| P2 | −23V | +3,5V | Dẫn | Ngắt | 0 | −(R86/R85)Vin |

Đặt `k=R86/R85`. Với OA lý tưởng, KCL cho `Vo=(1+k)S−kVin`. Ở P1, chân9≈chân10≈Vin nên dòng Rin/Rfb gần0; ở P2, chân9 là đất ảo nên G=−k. Với k=1, hai mức bằng±Vin. Linh kiện thực có sai số, offset, headroom và chuyển tiếp; xem §10.4/10.6.

### 6.3. Vai trò linh kiện và giới hạn suy luận

| Linh kiện | Trị số | Chức năng và giới hạn |
|---|---|---|
| U2B | 168КТ2Б | Đường nối tiếp Vin→S ở P1 |
| U2A + R4 | Khoá +10kΩ1% | Nhánh tải Vin→U2A→R4→GND ở P1, **không nối vào S**. So với tải Rin ở P2, cân bằng gần đúng là suy luận có cơ sở; Ron/dung sai làm hai tải khác nhau. Mục tiêu chống răng cưa S&H chưa được xác minh. |
| U1A | 168КТ2Б | Shunt S xuống GND ở P2 |
| R85/R86 | 10kΩ1% | Xác định G−=−k; hai sai số độc lập1% cho k=0,980198…1,020202 |
| C1 | 0,01µF | Song song R86; τ=100µs, 1/(2πτ)=1,59155kHz. Mô hình động bên dưới; không được mô tả toàn bộ kênh như bộ lọc thông thấp một cực. |
| R37 | 4,7kΩ5% theo BV.22 | Bù gần đúng trở kháng vào đảo5kΩ. Nếu thay bằng dây0Ω, riêng Ib−9µA tạo offset đầu ra90mV, không phải45mV. R37 hở là lỗi khác: chân10 mất đường DC. |
| U19 | 140УД1Б | OA sai lệch; chân4 mát; tham số đúng biến thể phải xác nhận |
| R38+C2 | 56Ω +0,01µF | Nhánh коррекция; RC=0,56µs, tần số bằng trở kháng R/Xc≈284kHz. Không suy trực tiếp cực vòng kín hay dạng sóng chân12 từ tích RC. |
| Q1/Q2 | 2Т312Б/2Т203Б | Lặp emitơ bù lớpB trong hồi tiếp; transistor dẫn theo **chiều dòng**. Chỉ với tải thuần trở mới thường tương ứng nửa điện áp dương/âm. |
| R39 | 180Ω | Hạn chế dòng và tạo cách ly nối tiếp là hệ quả vật lý. Hồi tiếp bù sụt áp trong băng thông và headroom cho phép; trở kháng ra không bằng0. **Không phải bảo vệ ngắn mạch.** |

**Mô hình động danh định:** `Zf=R86/(1+sτ)`; `Vo=(1+Zf/R85)S−(Zf/R85)Vin`. Khi Vin giữ DC và k=1:

`Vo(s)=[(2+sτ)/(1+sτ)]S(s)−Vin(s)/(1+sτ)`.

Khi S nhảy0→Vin, Vo có bước tức thời bằngVin trong mô hình OA lý tưởng, rồi phần còn lại tiến theo hàm mũτ. Mạch thực làm hữu hạn sườn đó bởi băng thông, коррекция, slew và tải. C1 có tác dụng giảm hài của nhánh hồi tiếp, nhưng kết luận “vo tròn hoàn toàn/triệt gai để bảo vệ СКТ” là quá mạnh.

**Ngắn mạch:** `(12,6−0,7)/180=66,11mA` là ước lượng khi base lên sát rail, không phải dòng bảo đảm/đo được. Thực tế `I≈(|V5|−|VBE|)/180`, còn giới hạn bởi khả năng lái base/β. Không thử chập đầu ra. Công suất Q phải tính `|VCE|·|IC|`, không lấy12V×66mA đồng thời với giả thiết emitơ lên11,9V.

R_fb/C_fb sau R39 giúp giảm méo của tầngQ khi vòng còn điều khiển được. Một Q hở thường làm sai rõ chiều dòng tương ứng; với tải phản kháng không quy trực tiếp theo dấu điện áp.
''')

s=s.replace('thiết kế dựa vào đế nội bộ của vi mạch.','**chưa đủ tài liệu để kết luận cơ chế phân cực đế nội bộ**. Không thay đổi đấu nối đã được xác nhận.')
s=s.replace('U15 không bao giờ lật ⇒ mất М/М̄ ⇒ **chết cả 16 kênh**','H15 vẫn đổi dấu do U14/U16 ⇒ U15 **có thể vẫn lật**, nhưng theo ngưỡng đổi dấu, gây sai pha nghiêm trọng; không suy ra mất cả16 tín hiệu')
s=s.replace('Mạch làm việc đúng ✔','Phù hợp mô hình pha danh định ở §5.2 (còn cần kiểm thật)')

section('### 10.3.','### 10.5.',r'''
### 10.3. Bước 1 — Cấp nguồn và ghi dòng tĩnh

1. Tấm tháo khỏi hệ thống; nối GND chung chắc chắn, các đầu vào Vin=0, đầu ra chỉ nối thiết bị đo trở kháng cao. Nguồn đã đặt đúng cực/tất cả mức trước khi bật; **bật/tắt đồng thời hai ray±12,6V**, không cố ý cấp một ray rồi mới cấp ray kia. Trình tự bốn nguồn phải xác lập trên đồ gá/tấm chuẩn; chưa có căn cứ cho thứ tự riêng đã ghi ở Rev.B.
2. Giới hạn dòng theo tấm chuẩn và tải thực; đo riêng từng ray bằng thiết bị, không dùng tay sờ IC đang cấp điện để quyết định dừng. Dòng vượt1,5×mốc ở cùng chế độ là dấu hiệu cần ngắt và kiểm, không phải chuẩn linh kiện tổng quát.
3. **Dòng IC:** giả thiết10mA/con cho18con là180mA, không suy ra dải100–200mA mỗi ray của toàn tấm. PDF140ud1B.pdf ghi12mA tại±13,9V cho БВК, tương ứng216mA riêng18IC; cần xác nhận lô/điều kiện. Cộng dòng tầngQ, base, mạng chia/hồi tiếp và tải. Ví dụ16 tải thuần trở1kΩ cùng mức4V cần riêng dòng tải64mA trên ray đang cấp/hút, chưa kể phần còn lại. Với điều chế đối xứng, chia dòng trung bình theo duty; đo cả đỉnh.
4. Bốn điện trở kéo10k giữa−23V và nút cao+3,5V lấy≈2,65mA/nhánh đang cao. Bình thường hai nhánh cao cho≈5,3mA DC từ+3,5 sang−23V; cộng chuyển mạch/tải ngoài và nhánh R34 (≈1,94mA khi bị kéo thấp). Không lấy5–15mA làm chuẩn nghiệm thu cứng.
5. Đo+12,6/−12,6/−23/+3,5V. DKKT đoạn kiểm nguồn thứ cấp liệt kê±5% cho+5,±12,6,−23,+6,3V; **không nêu riêng+3,5V**, nên phải lấy chuẩn của ray này từ hồ sơ nguồn/tấm chuẩn.
6. Ghi offset từng đầu ra ở cả hai pha tĩnh (§10.4). Mốc50mV chỉ sàng lọc tham khảo; offset lớn không riêng do OA, còn khoá, R_bias, rò và nguồn.

### 10.4. Bước 2 — Kiểm tra TĨNH bằng ±5 V DC tại ngõ chuẩn

**Kết luận D1:** khả thi theo topo trong điều kiện mạch khỏe và giả thiết chiều khoá đúng. Không có vòng nào bắt buộc dao động khi chuẩnDC ở±5V. Đây chưa phải chứng nhận thử trên phần cứng; phải xác nhận các nút sau trước khi dùng làm bài ATE tự động.

| Chuẩn đưa vào DC11 A5/B5/C5 | U14.9 | U15.9 | H14/H15 | U14.5/U15.5 | A/B | М/М̄ | G |
|---|---|---|---|---|---|---|---|
| +5V DC | +0,5170V | +0,6402V | −h/+h | Âm/âm | Cao/thấp | Cao/thấp | +1 |
| −5V DC | −0,5170V | −0,6402V | +h/−h | Dương/dương | Thấp/cao | Thấp/cao | −1 |

“Cao/thấp” là mức gần+3,5V/−23V, không phải GPIO3,3V. Với+5V, U14.9 vượt cả hai ngưỡng nên đầu ra âm bất kể trạng thái ban đầu; U16A/D dẫn. U15.9>+h nên U15 cũng âm, hệ tự giữ. Với−5V ngược lại. Dự trữ danh định so với h: U14≈0,166V, U15≈0,289V; cần xét dung sai/offset/Ron trước khi hạ mức chuẩn. Ở chuẩn0V, trạng thái phụ thuộc lịch sử; không dùng0 để chọn pha.

**Thực hiện:**

1. Tách nguồn sin và các kết nối ngoài có thể cùng lái DC11; tuyệt đối không đấu song song nguồnDC với đầu ra bộ tạo chuẩn. Cấp đủ4nguồn đúng mức trước khi bơm tín hiệu, tắt tín hiệu trước khi tắt nguồn. ±5V là điện áp tại đầu nối; điện áp vào OA đã được chia như bảng.
2. Đầu ra không tải ngoài DMM, các Vin không đo nốiGND. Chuyển chuẩn±5V, quan sát U14/U15.5, H14/H15, М/М̄ bằng scope: phải đứng yên, đúng bảng, không tự kích. Nếu sai, dừng quét DC; sửa cụm tạo xung/kiểm chiều khoá trước. Không ép М/М̄ từ ngoài chống tầngU18.
3. Đo Vo với Vin=+4,−4,+1,0V ở mỗi pha. Chờ xác lập theo trace;10ms có thể dùng làm giá trị khởi đầu, tăng nếu tấm chưa ổn. Mong đợi mức gần+Vin hoặc−Vin, **không áp sẵn cửa sổ±60mV** cho mọi linh kiện1%.
4. Lặp16kênh, ghi cả Vin thực và Vo. Từ hai cực tính lấy `Gp=[Vo(+4)−Vo(−4)]/8` và `Op=[Vo(+4)+Vo(−4)]/2`, riêng p=P1/P2; đo thêm Vo(0) để kiểm phi tuyến/offset. Cách này tách gain khỏi offset.

**Ngân sách sai số D2 (trở thuần, tải nhẹ, trạng thái xác lập):**

* Rin/Rfb độc lập1%: `kmin=0,99/1,01=0,980198`, `kmax=1,01/0,99=1,020202`. G− có thể lệch−1,9802…+2,0202% chỉ do trở; tại4V là≈80,81mV. Không thể bảo đảm1% hoặc±60mV.
* G+ lý tưởng bằng1 dù k sai. OA có gain hữu hạn gây sai số gần`(1+k)/A` (với đệm lý tưởng): A≥1350 cho≈0,15%, nhưng Vos đến7mV tạo noise gain≈2 →14mV, tương đương0,35% tại4V, đã vượt0,3% nếu dùng phép chia một điểm chưa khử offset.
* Offset DC xấp xỉ `E=(1+k)Vos+Rfb·Ib−−(1+k)(Rbias+Ron)·Ib+`. Không được lấy `(5−4,7)k×ΔIb` để thay tất cả sai số bias. Với giả thiết cũ Ib≤9µA, ΔIb≤2,5µA, Rbias±5%, Rin/Rfb±1%, Ron0…100Ω, cận bảo thủ riêng các hạng này≈**49,8mV**. Chưa gồm rò, trở nguồn, biến thiên Ron trong chế độ đế thả nổi, CMRR, nhiệt và gain hữu hạn/tầngQ. Với thông số БВК8µA/1,5µA, cận nhỏ hơn; không trộn hai tập tham số.
* Vì vậy50mV là mốc tham khảo sát ngân sách, không phải bảo đảm chung. Cận cộng đơn giản tại4V pha− theo giả thiết cũ đã khoảng80,8+49,8+6≈137mV, chưa gồm mọi lỗi. Đây là **ngân sách tính**, không tự nâng thành dung sai sản phẩm.

| Chỉ tiêu cần ghi | Công thức/diễn giải | Cách đặt giới hạn |
|---|---|---|
| G+ | Hệ số từ hai cực tính, so với+1 | 0,3% có thể là mục tiêu đã hiệu chuẩn, chưa phải bảo đảm toàn tấm |
| G− | Hệ số từ hai cực tính, so với−1 | Không đòi≤1% với hai R1% độc lập; cần đo/chọn cặp hoặc đặc tả chính thức |
| Mất đối xứng gain | `abs(G+ + G−)` | Có thể tới≈2,02% riêng do tỉ sốR;1% chỉ dùng nếu có tuyển/hiệu chuẩn |
| Offset | Op và Vo(0), cả hai pha | Ghi tấm chuẩn theo nhiệt độ;50mV chỉ mốc khảo sát |
| Tuyến tính | So Vo(±1) với đường thẳng từ±4, đã trừ offset | 0,2% chưa có bảo đảm từ dữ liệu đang có |

Giá trị vượt mốc gợi ý chưa tự chứng minh tấm hỏng. Chỉ khóa giới hạn pass/fail khi đã có đặc tả áp dụng và phân bố đo của tấm chuẩn. BàiDC không kiểm được overlap, pha400Hz hay ổn định tải phản kháng.
''')

section('### 10.5.','### 10.7.',r'''
### 10.5. Bước 3 — Kiểm tra U14/U15/U16/U17/U18 với sin400Hz

Cấp chuẩn tại DC11 A5/B5/C5, ghi rõ biên độ đo thực làVrms hayVđỉnh.

| # | Điểm đo | Mong đợi theo mô hình danh định | Nếu sai, kiểm |
|---|---|---|---|
| 3.1 | U14.9 | Sin=0,1034009×chuẩn,≈0,731Vđỉnh khi5Vrms | R20/R21/R124/R117 |
| 3.2a | U14.10=H14 | Gần±0,351V, đổi sau zero; theo trạng tháiU14 | U16A/B, hai nguồn chiaáp |
| 3.2b | U15.10=H15 | Gần±0,351V **đối dấu H14**, không chung nút | U16C/D, R22/R23/R28/R29 và cầu0Ω |
| 3.3 | U14.5 | Xung bão hòa; sườn sau zero theo§5.2 | U14, nguồn, hồi tiếpU16/U17, R27/C3 |
| 3.4 | A=U17A.3 | Gần−23/+3,5V | U17A/R32/R26 |
| 3.5 | B=U17D.12 | Bù A ở xác lập | U17D/R33 |
| 3.6 | DC11 A6/B6/C6 | xung400Hz gần0/+3,5V; duty≈50% nếu sin/ngưỡng đối xứng | U17B/C/R34 |
| 3.7 | U15.9 | Sin=0,1280306×chuẩn,≈0,905Vđỉnh khi5Vrms | R24=2,05kΩ, R25/R119/R120 |
| 3.8 | U15.5 | Xung bão hòa; sườn **trước zero** danh định | U15 vàH15; R31/C4 |
| 3.9 | DC11 A7/B7/C7 | М gần−23/+3,5V | U18A/R35/R30 |
| 3.10 | DC11 A8/B8/C8 | М̄ bù ở xác lập; **đo**, không giả định overlap bằng0 | U18D/R36 và tải điều khiển |
| 3.11 | Hai sườn cùng chiều của М và xung400Hz | М sớm≈357,8µs(5Vrms) hoặc528,1µs(5Vđỉnh), chưa gồm sai số/trễ | H14/H15, tỉ số chia, biên độchuẩn, chiều khoá |

Ghi hai sườn riêng và so với zero của sin. Các con số là mô hình danh định, không phải cửa sổ nghiệm thu. М/М̄ cùng mức dẫn có thể gây dòng xung từVin qua haiRon xuốngGND; mức hại phụ thuộc nguồn/trởkháng và thời gian. Đo cả hai gate và S/Vin để xác định chồng dẫn thực; ngưỡng logic tùy chọn không thay thế ngưỡng dẫn linh kiện.

### 10.6. Bước 4 — Kiểm tra ĐỘNG từng kênh

Chuẩn400Hz, Vin=+4V; khởi đầu không tải ngoài đầu đo. Đo **8 điểm** kênh1а, GND đầu đo vềGND tấm (không kẹp mát scope vào rail âm).

| TP | Vị trí | Mong đợi và giới hạn |
|---|---|---|
| TP1 | DC12 A7, ВЫХ.1А= | DC+4V; đo gợn thực, chưa có chuẩn “vài mV” được bảo đảm |
| TP2 | S=U2B.7=R37 trái | Gần0↔4V; Ron, rò, overlap làm sai lệch |
| TP3 | U19.10 | TheoS nhưng chênh DC có thểIb×4,7k≈42,3mV với giả thiết9µA; không coi bằnghệtTP2 |
| TP4 | U19.9 | GầnTP3 khi vòng ổn định; sai khác phụ thuộcVos/gain; ở sườn có thể tăng |
| TP5 | U19.5, baseQ1/Q2 | KhiQ dẫn: `V5≈Y+VBE(NPN)` hoặc `Y−abs(VBE(PNP))`; không phải chỉ±4V. Khu vực chuyển dòng có méo/vùngchết; phụ thuộc tải |
| TP6 | Y=emitơQ1/Q2 | `Y=Vo+180·I_R39`; khi không tải vẫn có dòngRfb/Cfb. Sườn gồm phần truyền trực tiếp và phần quá độ, không chỉ hàm mũ100µs |
| TP7 | DC12 A17, ВЫХ.1А== | Mức xác lập gần±4V; khácY theo dòng quaR39. So mô hình§6.3 và trace tấmchuẩn |
| TP8 | U19.12, đầu trênR38 | **Chưa đủ dữ liệu dự đoán dạng/biênđộ.** MạngRC nối đất không chứng minh nhỏ hơnTP5. Dùng đầu đo điện dung thấp, ghi tải đầu đo và tracechuẩn; không dùng biênđộ suy đoán làm pass/fail |

**Tải:** bắt đầu bằng≥1kΩ thuầntrở đã biết côngsuất, thửtừngkênh; chỉ thêm tải tươngđươngСКТ khi biết trởkháng theo tầnsố/pha. Không tự chọn1–2kΩ//0,1µF làm tải chuẩn: cạnh có thể tạo dòngC·dV/dt và gây mất ổnđịnh. Mốc sụt≤2% chỉ là mục tiêu cần xác nhận, chưa suy được từ bảnvẽ.

400Ω ở4V đã lấy10mA tải; pha− còn≈0,4mA quaRfb, nên dòngemitơ≈10,4mA. Cận bảo thủ để tổngemitơ≤10mA làRL≥4/(10−0,4)mA≈417Ω, nhưng **vẫn phải kiểm swing, β, nhiệt, quáđộ và SOA**. Với RL=400Ω, cần Y≈5,872V và base≈6,57V (VBE0,7V); vượt swing âm6,3V được bảo đảm ở điều kiện thử của PDFБВК. Vì vậy không chứng nhận tải400Ω bằng phépchia4V/10mA.

**Thành phần400Hz:** với mô hình lý tưởng§6.3 và duty50%, `V1_peak/abs(Vin)=(2/π)·abs((2+jωτ)/(1+jωτ))≈1,24455`; `V1_rms≈0,88003·abs(Vin)`. VớiVin4V: khoảng4,978Vđỉnh,3,520Vrms riêngthànhphầncơbản. Không nhầm vớiRMS toàn dạngsóng hay với mứcplateau4V. FFT phải ghi chuẩn peak/RMS; đo qua lọcdải phải hiệu chỉnh gainbộlọc. Mạchthực cần ghi tracechuẩn, vìOA/коррекция/tải chưa nằm trong mô hìnhnày.
''')

section('### 10.7.','## 11.',r'''
### 10.7. Chẩn đoán theo topo (nguyên nhân là giả thuyết cần đo tiếp)

| Triệu chứng | Nguyên nhân khả dĩ / phép phân biệt |
|---|---|
| Cả16kênh không cònAC, Vin bìnhthường | ĐoМ/М̄,4nguồn, chuẩn400Hz, U14/U15/H14/H15. Mất điều chế có thể để lạiDC±Vin, không đồngnghĩa Vo=0 |
| Cả16kênh Vo≈+Vin DC | KiểmМcao/М̄thấp, U18A/R35, U15.5 vàchuẩn. Không chỉ một linhkiện gây được |
| Cả16kênh Vo≈−Vin DC | KiểmМthấp/М̄cao, U18A/D/R35/R36 vàU15; không gán riêng М̄kẹt |
| Nhóm4kênh cùng bấtthường | KiểmvỏshuntU1/U4/U7/U10 vàdâyМ. Shunt hở đểS nổi trongpha−: có thể giữđiện, trôi, méo; không bắtbuộc+VinDC |
| Cặp2kênh cùng bấtthường | KiểmvỏU2/U3/U5/U6/U8/U9/U11/U12 vàМ̄. Khoá nối tiếphở đểS nổi trongpha+, không tựtạo−VinDC |
| Mộtkênh Vo≈0 dùTP2 bìnhthường | ĐoTP3/4/5/Y vàRra. Rfb hở thườngmất hồi tiếpDC/bãohòa; Rin hở cònđườngS→OA nên không giảđịnhVo=0; haiQ hở cònđường hồi tiếptớiđầu đo |
| Kênh hụt chiều dòngdương/âm với tải thuầntrở | NPN/PNP tươngứng hở/yếu hoặc mấtnguồncụcbộ; thửtảiđãbiết. Với tải phảnkháng, dấuđiệnáp không xácđịnh Qđangdẫn |
| Kênh bãohòa, khôngtheoVin | QchậpC-E, hồitiếpRfb hở, mấtnguồn/GND hoặcOA; điệnáp khôngnhấtthiết±12V |
| Mấtđốixứng plateau | ĐoRfb/Rin,offsettừngpha, Ron/Rbias vàVin tại chântấm. Rbal hở chỉtácđộng rõ qua trởkhángnguồn; nguồnáp lýtưởng khôngtựđổiG |
| Sườn/chuyển tiếp bấtthường, fundamental thấp | Cfb tăng/rò, bandwidthOA, коррекция, tầngQ hoặc tải; phânbiệt ròCfb (đổiDC gain) với chỉtăngC |
| Tựkíchcao tần | KiểmRcorr/Ccorr, lọcnguồn, tải dung, hồi tiếp, Qthaythế; Rcorr/Ccorr hở là một khả năng, không điều kiện đủ |
| Gai tại sườn | Khoá/overlap, Cfb, nốiđất, đầu đo vàtải; không kếtluận chargeinjection tăng chỉ từ mộtgai |
| Offset nhiều kênh | Nguồn, GND, rò/khoá, sai chếđộ đo; sauđó mới soOA/Rbias |
| Sụt mạnh khi tải | Thiếuheadroom, Q/Rra, vònghồi tiếp, giới hạndòngnguồn; Rra trôi chỉ gây sụt rõ khi bùkhông đủ |
| Vin gợn400Hz | Chồngdẫn М/М̄, trởkhángnguồn, Rbal sai/hở, trởnốichung hoặcS&H; đo đồngthờiS/Vin/gate |
| −23V tiêu thụ tăng | Chập khoá, R32/R33/R35/R36 sai, gate/tảingoài, trạngthái khôngbù; khoanhvùng qua sụt áp từngR |
| R24 lắp nhầm2,05MΩ | BiênđộU15.9 rất nhỏ nhưngH15 vẫn đổi dấu doU14: U15 có thể vẫnphát400Hz, **sai pha**; kiểmpha vàtrịsố thay vì chỉ kiểm cóxung |
''')

section('## 11.','## 12.',r'''
## 11. GỢI Ý THIẾT KẾ ATE CHO TẤM A313-V.06

```text
PC → controller FPGA/MCU
 ├─ DAC ±4V + mux →16 Vin (kênh không đo được đưa vềGND)
 ├─ Nguồn chuẩn cách ly/chuyển mạch sin400Hz ↔ +5VDC ↔ −5VDC
 ├─4nguồn +12,6/−12,6/−23/+3,5V, đo dòng riêng
 ├─Mux+ADC: đoDC hai pha, đođộng đồngbộ400Hz
 └─Đầu vào bảo vệ/dịchmức: М,М̄,xung400Hz, sinchuẩn
```

**Bài tĩnh:** chỉ chạy sau khi đã xácnhận trạngthái§10.4 trên tấmchuẩn; đo±4,±1,0V và khửoffset để tínhgain. Phủ16kênh không đồngnghĩa phủ100%lỗi. Muxkhông được để các Vin còn lại thảnổi.

**Bài động:** đo fundamental/pha bằng tínhiệuthamchiếu vàgiữ trace sườn. ADC100kS/s có bước10µs, phùhợp thànhphần400Hz nhưng không bắtchắc gai/overlap dướiµs; dùngscope hoặcđường capture/comparator đủnhanh cho phépđó. Không quy gai vượtngưỡng thànhkhoáhỏng mà bỏqua tải/đầuđo.

**Overlap:** bộso sánh phải chuyển mức−23/+3,5V antoàn vềlogic, ngưỡng chọn theo quan hệgate–kênh vàphépđothực. Hai cựcđại datasheet t_on≤0,3µs, t_off≤0,7µs **không cho phép lấy hiệu0,4µs làm overlap dựđoán**, cũng không chứngminh ngưỡng vài chụcns hợp lý. Chốt cửa sổchấpnhận từđothực và dòngxung vàoS&H.

**Nguồn/tải:** bật/tắt±12,6V đồngthời; trìnhtự bốn nguồn vàgiớihạndòng phải qua xácnhận đồgá/tấmchuẩn. Các giátrị400mA/50mA cũ chưa có ngânsách kiểmchứng nên không dùng làmchuẩn cốđịnh. Tải thực, chếđộ16kênh và dòngkhởiđộng quyếtđịnh mứcđặt. Không chậpđầu ra: R180Ω khôngbảo vệQ. Không cấp+5V/+6,3V vào railkhôngdùng, không tựnối chân4/11 của168КТ2. Mức±5VDC của bàiđóngbăng là **tínhiệu chuẩn**, không phải rail+5V bịbỏ.

R24 phải2,05kΩ theo xácnhận thực; nếu lắpnhầm2,05MΩ cóthể vẫncó400Hz nhưngsai pha (§9.1/10.7). Đầu vàoDI/ADC cầnchịu mứcđiệnáp thực vàtrạngthái nguồnchưasẵn, không nốithẳngМ/М̄ vàoGPIO.
''')

s=s.replace('Quyết định góc trễ sườn xung: 28,7°/22,8° (5 Vrms) hay 42,8°/33,3° (5 V đỉnh) — §5.2','Quyết định độ sớm М so với xung400Hz: khoảng357,8µs (5Vrms) hoặc528,1µs (5Vđỉnh) trong mô hình danh định — §5.2')
s=s.replace('Thiết kế tải giả — lưu ý tải **không được nhỏ hơn 400 Ω** do giới hạn I_к = 10 mA của 2Т203Б','Thiết kế tải giả theo Z(f), pha, dòngđỉnh vàheadroom;400Ω không phải tải được bảo đảm — §10.6')
s=s.replace('t_вкл = 0,3 µs < t_выкл = 0,7 µs của 168КТ2 ⇒ về nguyên lý có thể chồng lấn ~0,4 µs; cần đo để đặt ngưỡng chấp nhận (§10.5, §11)','Hai thời gian0,3/0,7µs là các cựcđại ở điều kiện thử; không trừ để suy overlap. Đo gate/S/Vin và dòngquáđộ để chốt ngưỡng (§10.5, §11)')
s=s.replace('*Rev. B — 16/09/2026.', '*Rev. C — 16/09/2026.')
s=s.replace('*Các sai sót hồ sơ ở §9 đã được xác nhận với người thiết kế/khai thác. Các hạng mục còn treo được liệt kê tập trung ở §12.2 — mọi kết luận khác trong tài liệu đã nhất quán với 6 điểm đã chốt.*','*Giữ nguyên sáu kết luận khai thác§9. Nhật ký§0 ghi riêng bằng chứng topo, tính toán, giả thiết và phần chưa đo. Rev.C không phải biên bản nghiệm thu phần cứng.*')
s=s.replace('### 12.1. ✅ Đã hoàn thành (Rev. B)','### 12.1. ✅ Các kết luận đã chốt từ Rev. B (giữ nguyên trong Rev. C)')
# Cold resistance measurements are topology-dependent, not insulation certification.
s=s.replace('**> 100 kΩ** mỗi ray (chiều thuận), không được < 1 kΩ','Đo hai chiều, chờ tụ nạp, so tấm chuẩn; IC/đường kéo có thể cho trị số thấp. Không có cận100kΩ/1kΩ tổng quát từ sơ đồ; không dùng megohmmeter cao áp')
s=s.replace('| > 100 kΩ |','| So tấm chuẩn sau quá trình nạp tụ; đường bán dẫn làm phép đo phụ thuộc cực tính |')
s=s.replace('≈ vài kΩ, **16 kênh phải gần bằng nhau** (lệch > 20 % ⇒ nghi kênh đó)','So tương đối16kênh trong cùng điều kiện; chưa xác nhận ngưỡng20% hay trị sốvàikΩ')
s=s.replace('16 kênh gần bằng nhau (≈ 10–20 kΩ)','So16kênh; không cốđịnh10–20kΩ vì khoá mấtnguồn/đếnổi và đường bán dẫn')
p.write_text(s,encoding='utf-8')
print('Updated',p)
