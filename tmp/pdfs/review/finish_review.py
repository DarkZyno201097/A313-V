"""Editorial cleanup and structural checks for the six reviewed Markdown files."""
from pathlib import Path
import re

files=[Path('PHAN-TICH_A313-V.06_KHUECH-DAI-TIN-HIEU-RA.md'),*sorted(Path('Datasheet').glob('*.md'))]
# Restore spaces in Vietnamese prose; do not change identifiers, URLs or numbers.
pairs='''
điệnáp|điện áp
tínhiệu|tín hiệu
tínhiệuthamchiếu|tín hiệu tham chiếu
dòngđiện|dòng điện
dòngđỉnh|dòng đỉnh
dòngquáđộ|dòng quá độ
quáđộ|quá độ
chuyểnmạch|chuyển mạch
chủngloại|chủng loại
chủngloạigốc|chủng loại gốc
trạngthái|trạng thái
linhkiện|linh kiện
thànhphầncơbản|thành phần cơ bản
thànhphần|thành phần
thành phầncơbản|thành phần cơ bản
biênđộ|biên độ
tầnsố|tần số
thời gianthử|thời gian thử
nghiệmthu|nghiệm thu
kiểmchứng|kiểm chứng
kiểmtra|kiểm tra
kiểmđịnh|kiểm định
kiểmchuẩn|kiểm chuẩn
kiểmthực|kiểm thực
kiểmthật|kiểm thật
bảovệ|bảo vệ
bảovệngắn|bảo vệ ngắn
antoàn|an toàn
bộlọc|bộ lọc
lọcdải|lọc dải
lọcnguồn|lọc nguồn
lọcnguồn|lọc nguồn
đồgá|đồ gá
tấmchuẩn|tấm chuẩn
tảingoài|tải ngoài
tảidòng|tải dòng
tảithực|tải thực
tảichuẩn|tải chuẩn
phảnkháng|phản kháng
thuầntrở|thuần trở
trởkháng|trở kháng
cốđịnh|cố định
giảđịnh|giả định
giảthiết|giả thiết
bấtthường|bất thường
giớihạn|giới hạn
giớihạndòng|giới hạn dòng
địnhmức|định mức
ngânsách|ngân sách
chếđộ|chế độ
chuẩntĩnh|chuẩn tĩnh
điềukiện|điều kiện
điệnthế|điện thế
điện dungthấp|điện dung thấp
thảnổi|thả nổi
đếnổi|đế nổi
thaythế|thay thế
phụthuộc|phụ thuộc
khôngtự|không tự
khôngphải|không phải
khôngthể|không thể
khôngcó|không có
khôngđược|không được
khôngđồng|không đồng
khôngđủ|không đủ
khôngbảo|không bảo
chứngminh|chứng minh
đồngnghĩa|đồng nghĩa
đốixứng|đối xứng
mấtđối|mất đối
thựctế|thực tế
đothực|đo thực
đothật|đo thật
đothựcvà|đo thực và
đothực|đo thực
đothì|đo thì
đođộng|đo động
đođồng|đo đồng
đođộc|đo độc
đồngbộ|đồng bộ
đồngthời|đồng thời
toànbộ|toàn bộ
thôngsố|thông số
sổtay|sổ tay
giátrị|giá trị
trịsố|trị số
mứcđặt|mức đặt
mứcđiện|mức điện
nguồncụcbộ|nguồn cục bộ
cụcbộ|cục bộ
mấtnguồn|mất nguồn
mấtổnđịnh|mất ổn định
ổnđịnh|ổn định
lýtưởng|lý tưởng
tuyến tínhhữu|tuyến tính hữu
bấtcân|bất cân
vònghồi|vòng hồi
hồitiếp|hồi tiếp
trởhồi|trở hồi
trởnguồn|trở nguồn
trởthuần|trở thuần
nguồnáp|nguồn áp
nguồnDC|nguồn DC
ngõchuẩn|ngõ chuẩn
chuẩnDC|chuẩn DC
chuẩn400|chuẩn 400
sinchuẩn|sin chuẩn
tần sốchuẩn|tần số chuẩn
biênđộchuẩn|biên độ chuẩn
đúngbảng|đúng bảng
theobảng|theo bảng
từngpha|từng pha
từngkênh|từng kênh
haipha|hai pha
thửtừng|thử từng
cùngmức|cùng mức
cùnglúc|cùng lúc
tụđiện|tụ điện
địnhlượng|định lượng
độnghọc|động học
nhấtthiết|nhất thiết
theoVin|theo Vin
khôngtheo|không theo
phaP1|pha P1
phaP2|pha P2
trongpha|trong pha
trongvòng|trong vòng
vùngchết|vùng chết
phânbiệt|phân biệt
đọcđược|đọc được
trướckhi|trước khi
trướcđó|trước đó
sauđó|sau đó
chỉtính|chỉ tính
chỉkiểm|chỉ kiểm
chỉtácđộng|chỉ tác động
hiệu chỉnhgain|hiệu chỉnh gain
khửoffset|khử offset
trừoffset|trừ offset
táchgain|tách gain
chọngate|chọn gate
đườngtruyền|đường truyền
đườngtải|đường tải
đườngnạp|đường nạp
đườngDC|đường DC
thiếtheadroom|thiếu headroom
bảngchân|bảng chân
đầuđo|đầu đo
đầura|đầu ra
đầuvào|đầu vào
đầunối|đầu nối
basechung|base chung
nútchung|nút chung
nốichung|nối chung
nốithẳng|nối thẳng
chântrái|chân trái
chântấm|chân tấm
chânphải|chân phải
nốitầng|nối tầng
thờigian|thời gian
tiếptới|tiếp tới
điểmđo|điểm đo
điểmqua|điểm qua
gócpha|góc pha
cậntrên|cận trên
congốc|con gốc
đúngbiến|đúng biến
biếnthể|biến thể
thông sốgiả|thông số giả
nhãnЛСАР|nhãn ЛСАР
theoАЕЯР|theo АЕЯР
theođúng|theo đúng
theođo|theo đo
phầnRC|phần RC
phầnDC|phần DC
phầnAC|phần AC
trong§|trong §
xem§|xem §
Xem§|Xem §
theo§|theo §
số§|số §
chuẩn§|chuẩn §
lập§|lập §
đúng§|đúng §
định§|định §
của§|của §
chân§|chân §
trongmô|trong mô
hình§|hình §
chuẩnđúng|chuẩn đúng
trìnhtự|trình tự
trìnhtự|trình tự
kiểm vỏshunt|kiểm vỏ shunt
kiểmvỏ|kiểm vỏ
Kiểmvỏ|Kiểm vỏ
nhưmột|như một
đượcbảo|được bảo
chếttoàn|chết toàn
đổidấu|đổi dấu
đượchiệu|được hiệu
kiểmpha|kiểm pha
đượcđo|được đo
đượcđặt|được đặt
chốtngưỡng|chốt ngưỡng
chấpnhận|chấp nhận
xácnhận|xác nhận
xácđịnh|xác định
phát400|phát 400
thìb|thì b
đođược|đo được
lấymẫu|lấy mẫu
gaitại|gai tại
liêntục|liên tục
vẫncó|vẫn có
vẫnphát|vẫn phát
cóthể|có thể
sai pha|sai pha
R180|R 180
R4,7|R 4,7
mạngRC|mạng RC
noisegain|noise gain
gainhữu|gain hữu
gateâm|gate âm
cựctính|cực tính
cựcđại|cực đại
nửa chu kỳâm|nửa chu kỳ âm
dòngâm|dòng âm
dòngdương|dòng dương
nguồnâm|nguồn âm
nguồndương|nguồn dương
vai tròthực|vai trò thực
nhánhcũ|nhánh cũ
nhánhmới|nhánh mới
nạpđủ|nạp đủ
nhiệtđộ|nhiệt độ
côngsuất|công suất
kênhkhỏe|kênh khỏe
giữđiện|giữ điện
đểS|để S
khônggiả|không giả
đổiDC|đổi DC
chỉtăng|chỉ tăng
giảđịnhVo|giả định Vo
địnhVo|định Vo
khoáhỏng|khoá hỏng
khoáâm|khoá âm
khoáchập|khoá chập
khoá nối tiếphở|khoá nối tiếp hở
Shunt hởđể|Shunt hở để
thấpcao|thấp cao
kẹtdẫn|kẹt dẫn
cháyhỏng|cháy hỏng
ngắnmạch|ngắn mạch
ghépcặp|ghép cặp
cảcặp|cả cặp
cảvòng|cả vòng
chỉvì|chỉ vì
mộtQhỏng|một Q hỏng
nếuđổi|nếu đổi
dòngbase|dòng base
dònglái|dòng lái
dòngkhởiđộng|dòng khởi động
khởiđộng|khởi động
cửa sổchấp|cửa sổ chấp
khóanguồn|khoá nguồn
chuẩnloại|chuẩn loại
chữký|chữ ký
gầnđúng|gần đúng
theotrace|theo trace
tracechuẩn|trace chuẩn
Rbiasđứt|Rbias đứt
railkhôngdùng|rail không dùng
railkhông|rail không
trạng thái nguồnchưasẵn|trạng thái nguồn chưa sẵn
giữađầu|giữa đầu
phíaGND|phía GND
nốiđất|nối đất
doU14|do U14
doU16|do U16
quaU17|qua U17
vàU15|và U15
hoặcOA|hoặc OA
theoOA|theo OA
dùngA|dùng A
từngR|từng R
bốnnguồn|bốn nguồn
nguồnchuẩn|nguồn chuẩn
thườngmất|thường mất
làVin|là Vin
nguồn/trởkháng|nguồn/trở kháng
nhầmR|nhầm R
thảnổi|thả nổi
sin/ngưỡngđối|sin/ngưỡng đối
thụđộng|thụ động
vàgiới|và giới
vàpha|và pha
vàtải|và tải
vàdòng|và dòng
vàtrị|và trị
vàchuẩn|và chuẩn
vàngưỡng|và ngưỡng
vàtrace|và trace
vàgiữ|và giữ
vàphép|và phép
vàđúng|và đúng
hoặctải|hoặc tải
hoặcđường|hoặc đường
hoặcnguồn|hoặc nguồn
quađầu|qua đầu
giátrị400|giá trị 400
Rfb/Cfb|Rfb/Cfb
điện trởkéo|điện trở kéo
bộso|bộ so
đổichủng|đổi chủng
chậpC-E|chập C-E
chậpđầu|chập đầu
tựtạo|tự tạo
tựkích|tự kích
Tựkíchcao|Tự kích cao
tựnối|tự nối
sin400|sin 400
đoDC|đo DC
ngưỡngđổi|ngưỡng đổi
độđỉnh|độ đỉnh
mứcplateau|mức plateau
kênhđo|kênh đo
cầntra|cần tra
chưađo|chưa đo
đoĐiện|đo điện
mấtđường|mất đường
chứckhông|chứ không
tiếptớiđầu|tiếp tới đầu
chỉtừ|chỉ từ
nguồnchưa|nguồn chưa
chưasẵn|chưa sẵn
quanhzero|quanh zero
theochiều|theo chiều
trongmạch|trong mạch
ngoàimạch|ngoài mạch
vượtngưỡng|vượt ngưỡng
bỏqua|bỏ qua
giảthiếtcũ|giả thiết cũ
Ron0|Ron 0
Rev.C|Rev. C
Rev.B|Rev. B
PDFБВК|PDF БВК
PDF140|PDF 140
tr.1|tr. 1
tr.2|tr. 2
tr.3|tr. 3
tầngQ|tầng Q
tầngU|tầng U
haiRon|hai Ron
xuốngGND|xuống GND
nốiGND|nối GND
vềGND|về GND
vềlogic|về logic
vàoGPIO|vào GPIO
vàoDI|vào DI
vàoS&H|vào S&H
vàМ|và М
ĐoМ|Đo М
KiểmМ|Kiểm М
Мcao|М cao
Мthấp|М thấp
М̄cao|М̄ cao
М̄thấp|М̄ thấp
М̄kẹt|М̄ kẹt
vàdây|và dây
dâyМ|dây М
trạng tháiU|trạng thái U
hồi tiếpU|hồi tiếp U
hồi tiếpR|hồi tiếp R
hồi tiếpDC|hồi tiếp DC
hồi tiếpRC|hồi tiếp RC
mạngRC|mạng RC
MạngRC|Mạng RC
Mộtkênh|Một kênh
bìnhthường|bình thường
chiaáp|chia áp
biên độchuẩn|biên độ chuẩn
TheoS|Theo S
bằnghệtTP|bằng hệt TP
GầnTP|Gần TP
thuộcVos|thuộc Vos
baseQ|base Q
KhiQ|Khi Q
dòngRfb|dòng Rfb
khácY|khác Y
quaR|qua R
trênR|trên R
hơnTP|hơn TP
tươngđương|tương đương
đươngСКТ|đương СКТ
dòngC|dòng C
bảnvẽ|bản vẽ
dòngemitơ|dòng emitơ
tổngemitơ|tổng emitơ
phépchia|phép chia
tưởng§|tưởng §
VớiVin|Với Vin
riêngthành|riêng thành
vớiRMS|với RMS
dạngsóng|dạng sóng
gainbộ|gain bộ
Mạchthực|Mạch thực
mô hìnhnày|mô hình này
cònAC|còn AC
4nguồn|4 nguồn
lạiDC|lại DC
vỏshunt|vỏ shunt
shuntU|shunt U
bắtbuộc|bắt buộc
VinDC|Vin DC
tiếphở|tiếp hở
ĐoTP|Đo TP
bãohòa|bão hòa
cònđườngS|còn đường S
cònđường|còn đường
haiQ|hai Q
tươngứng|tương ứng
thửtảiđãbiết|thử tải đã biết
dấuđiện|dấu điện
Qđangdẫn|Q đang dẫn
Qchập|Q chập
khôngnhất|không nhất
Mấtđối|Mất đối
ĐoRfb|Đo Rfb
offsettừng|offset từng
khángnguồn|kháng nguồn
tựđổiG|tự đổi G
bandwidthOA|bandwidth OA
KiểmR|Kiểm R
Qthay|Q thay
kếtluận|kết luận
chargeinjection|charge injection
mộtgai|một gai
soOA|so OA
Thiếuheadroom|Thiếu headroom
hạndòngnguồn|hạn dòng nguồn
bùkhông|bù không
Chồngdẫn|Chồng dẫn
trởnối|trở nối
hoặcS&H|hoặc S&H
thờiS|thời S
khôngbù|không bù
khoanhvùng|khoanh vùng
Biênđộ|Biên độ
nhưngH|nhưng H
cóxung|có xung
tínhgain|tính gain
Muxkhông|Mux không
phùhợp|phù hợp
bắtchắc|bắt chắc
dùngscope|dùng scope
đủnhanh|đủ nhanh
phépđó|phép đó
thànhkhoá|thành khoá
quan hệgate|quan hệ gate
phépđo|phép đo
dựđoán|dự đoán
chụcns|chục ns
từđo|từ đo
dòngxung|dòng xung
làmchuẩn|làm chuẩn
quyếtđịnh|quyết định
bàiđóngbăng|bài đóng băng
bịbỏ|bị bỏ
lắpnhầm|lắp nhầm
nhưngsai|nhưng sai
cầnchịu|cần chịu
vàtrạng|và trạng
thẳngМ|thẳng М
BàiDC|Bài DC
bằng0|bằng 0
gần0|gần 0
gần1|gần 1
haiR|hai R
đúngđiều|đúng điều
dẫnkhoá|dẫn khoá
trênmạch|trên mạch
choБ|cho Б
dùngБ|dùng Б
dùngВ|dùng В
sogate|so gate
soGND|so GND
nguồnđã|nguồn đã
khôngép|không ép
cựcđại|cực đại
phầnkhác|phần khác
đothử|đo thử
chânđế|chân đế
đãđo|đã đo
đãbiết|đã biết
I_кliên|I_к liên
củaPNP|của PNP
hơnNPN|hơn NPN
củaNPN|của NPN
ngưỡngđiện|ngưỡng điện
điệnáp|điện áp
hợpMOS|hợp MOS
cảRfb|cả Rfb
tínhIC|tính IC
giảthiết|giả thiết
vượtgiới|vượt giới
áp dụngngay|áp dụng ngay
Hệsố|Hệ số
thửchập|thử chập
chỉvới|chỉ với
nhưng cònheadroom|nhưng còn headroom
gầnrail|gần rail
chânmát|chân mát
đọcPDF|đọc PDF
chọncặp|chọn cặp
nguồn/trởkháng|nguồn/trở kháng
thửđế|thử đế
datasheetgốc|datasheet gốc
hai cậnthời|hai cận thời
chưađược|chưa được
phầncòn|phần còn
cao/thấpđúng|cao/thấp đúng
dảiVin|dải Vin
đểsửa|để sửa
tương ứngdatasheet|tương ứng datasheet
TheoVo|Theo Vo
nghiPNP|nghi PNP
khảnăng|khả năng
thôngsố|thông số
vàpinout|và pinout
thông sốsổ|thông số sổ
trởnguồn|trở nguồn
vàođảo|vào đảo
tầngđệm|tầng đệm
vòngSchmitt|vòng Schmitt
nguồnáp|nguồn áp
Khôngbắt|Không bắt
theonửa|theo nửa
10mA|10 mA
haiđầu|hai đầu
hai cựctính|hai cực tính
bộso|bộ so
dòngIC|dòng IC
đúngbiến|đúng biến
trởđộc|trở độc
phảiđo|phải đo
đủ4|đủ 4
100%lỗi|100% lỗi
5VDC|5 V DC
trongmạch|trong mạch
chân5|chân 5
chân10|chân 10
chân12|chân 12
168КТ2thực|168КТ2 thực
168КТ2—|168КТ2 —
'''
mapping=[tuple(x.split('|')) for x in pairs.strip().splitlines()]
mapping.sort(key=lambda x:len(x[0]),reverse=True)

for p in files:
    s=p.read_text(encoding='utf-8')
    lines=[]; fence=False
    for line in s.splitlines():
        if line.startswith('```'): fence=not fence
        if not fence and not line.startswith('```') and 'http' not in line:
            for a,b in mapping: line=line.replace(a,b)
        lines.append(line)
    s='\n'.join(lines)+'\n'
    # Restore literal source filenames/identifiers that editorial regex must not alter.
    s=s.replace('140ud 1B.pdf','140ud1B.pdf').replace('168kt 2.pdf','168kt2.pdf')
    s=s.replace('Rev. B trước đó Đã','Rev. B trước đó đã')
    # Repair the first editorial pass's overly broad Unicode range. Use known
    # words, not a letter range that also includes Cyrillic/Greek/capital letters.
    words='CHỨC NĂNG KIỂM CỤM KHUẾCH ĐẠI HIỆU NHẬT PHẢN BIỆN VỊ KHỐI DIỆN ĐIỆN BẢNG ĐẦU NỐI TỔNG NGUỒN LỌC TẠO ĐIỀU MỘT KIỆN THỐNG ĐỐI CHIẾU CHỐT TĨNH ĐỘNG GỢI THIẾT TẤM MỤC VIỆC LẠI TẦNG ĐỆM MỨC TƯƠNG CỦA CỨU CHUYỂN MẠCH DỤNG VỎ GIỚI HẠN TRỌNG NHẤT CẦN ĐƯƠNG KHẢO THUẬT ĐẶC ĐIỂM TRỘN BIẾN CHỈNH TẦN CẢNH LƯỠNG CỰC SUẤT SỬA DỮ LIỆU XÁC BÁC BỎ KHÔNG ĐỦ DẪN HỞ NGẮT CẢNH QUYẾT THỰC CHẮC CHẮN SỐ LƯỢNG GIỮ NGUYÊN'.split()
    words+=['TRƯỚC','CỘNG','SAU','Với','Vì','Ví','Vị','Vỏ','Vào','Vẫn','Vừa','Vậy','Vượt','Về','Và']
    for word in sorted(words,key=len,reverse=True):
        bad=re.sub(r'([à-ỹ])(?=[A-Z])',r'\1 ',word)
        bad=re.sub(r'(V|A|Ω|µs|mV|mA)(?=[à-ỹ])',r'\1 ',bad)
        if bad!=word: s=s.replace(bad,word)
    s=re.sub(r'168\s*КТ\s*2(?:\s*([АБВ]))?',lambda m:'168КТ2'+(m[1] or ''),s)
    s=re.sub(r'140\s*УД\s*(101|1)\s*([АБВ])',lambda m:'140УД'+m[1]+m[2],s)
    s=re.sub(r'К\s+(?=140УД)','К',s)
    s=re.sub(r'2\s*Т\s*(203|312)\s*([АБВГД])',lambda m:'2Т'+m[1]+m[2],s)
    s=re.sub(r'КТ\s*(203|312)\s*([АБВГД])',lambda m:'КТ'+m[1]+m[2],s)
    s=re.sub(r'([1-8])\s+([аАбБ])(?=[=*, …|)]|$)',r'\1\2',s)
    s=s.replace('h 21 э','h21э').replace('Δ Ib','ΔIb')
    s=s.replace('xung 400 Hz','xung400Hz').replace('ВЫХ.1 А','ВЫХ.1А')
    s=re.sub(r'([1-8]) +([аАбБ])(?=\W|$)',r'\1\2',s)
    s=re.sub(r'168КТ2(?=[a-zđ]|[àáạảãăâèéẹẻẽêìíịỉĩòóọỏõôơùúụủũưỳýỵỷỹ])','168КТ2 ',s)
    s=s.replace('168КТ2|','168КТ2 |').replace('168КТ2(','168КТ2 (')
    s=s.replace('channel 1.png','channel1.png').replace('Rr 63','Rr63')
    s=s.replace('К 140 УД 1','К140УД1').replace('КР 140 УД 1','КР140УД1').replace('КР 140УД1','КР140УД1')
    s=s.replace('R 56 |','R56 |').replace('R 56+','R56+').replace('R 56,','R56,')
    s=s.replace('168КТ2Т 1 ВК','168КТ2Т1ВК').replace('401.14-5.07 НБ','401.14-5.07НБ').replace('401.14-5 М','401.14-5М')
    for a,b in [('Swingra','Swing ra'),('swingOA','swing OA'),('trịsổ','trị sổ'),('riêngVos','riêng Vos'),('riêngIb','riêng Ib'),('cùngIb','cùng Ib'),('cộngRon','cộng Ron'),('sai sốcòn','sai số còn'),('60lần','60 lần'),('củaRin','của Rin'),('củaRbias','của Rbias'),('kiệnPDF','kiện PDF'),('tíchRev.','tích Rev.'),('hoặcC','hoặc C'),('mạngкоррекция','mạng коррекция'),('sách§','sách §'),('168КТ2đ','168КТ2 đ')]:
        s=s.replace(a,b)
    p.write_text(s,encoding='utf-8')

main=files[0].read_text(encoding='utf-8')
codes=[f'{c}{i}' for c,n in [('A',8),('B',7),('C',11),('D',5),('E',6)] for i in range(1,n+1)]
journal=main[main.index('## 0.'):main.index('### 0.1.')]
for code in codes:
    assert len(re.findall(r'^\| '+code+r' \|',journal,re.M))==1,code
for h in ['## 0. NHẬT KÝ PHẢN BIỆN (Rev. C)','### 2.1.','### 2.2.','## 7.','### 7.1.','## 8.','## 10.','### 10.7.']:
    assert h in main,h
assert len(re.findall(r'^\| \*\*[1-8][аба]?',main,re.M))>=16
assert all('Rev. C — 16/09/2026' in p.read_text(encoding='utf-8') for p in files)
print('PASS: all 37 review IDs once, required sections and 16-channel table retained; six Rev. C files')
