from pathlib import Path

D=Path('Datasheet')

def read(pattern):
    p=next(D.glob(pattern)); return p,p.read_text(encoding='utf-8')
def part(s,start,end,new):
    a=s.index(start);b=s.index(end,a);return s[:a]+new.strip()+'\n\n---\n\n'+s[b:]
def save(p,s):
    header='**Phiên bản: Rev. C — 16/09/2026.** Đồng bộ phản biện A313-V.06; các giới hạn suy luận/đo thực được ghi riêng.\n\n'
    pos=s.index('\n\n')+2;s=s[:pos]+header+s[pos:]
    p.write_text(s,encoding='utf-8');print(p)

p,s=read('00_*.md')
s=part(s,'### ⚠ Hệ quả thiết kế quan trọng','## 3.',r'''
### Hệ quả đối với phép thử A313-V.06

1. Iк liên tục10mA của2Т203Б là giới hạn quan trọng, **không chứng minh tải400Ω an toàn**: tải4V/400Ω đã10mA, còn dòngRfb tới0,4mA, headroom180Ω, nhiệt và quá độ. Bắt đầu đo với≥1kΩ thuần trở; tảiСКТ thực phải xác địnhZ(f)/pha. Xem§10.6 tài liệu phân tích Rev.C.
2. Không thử chập đầu ra. **66,11mA** là kết quả mô hình `(12,6−0,7)/180` với base lên sát rail, không phải dòng được bảo đảm. Thực tế phụ thuộc swingOA/β/giới hạn nguồn. Không suy thời gian “hỏng tức thì” chỉ từ phép tính này.
3. Chênh lệch f_гр giữa NPN/PNP không đủ dự đoán sườn âm chậm hơn: vòng hồi tiếp, mạngRC và tải cùng quyết định. Dẫn NPN/PNP theo chiều dòng; với tải phản kháng, không quy chỉ theo dấu điện áp.
''')
s=s.replace('**Biên độ điều khiển затвор:** −23 V ↔ +3,5 V = 26,5 V, nằm trong giới hạn U_зп max = −30 V của 168КТ2 (dự trữ ~3,5 V — **không nhiều**, cần giữ nguồn −23 V đúng trị số).','**Biên độ điều khiển:**26,5V là swing soGND. U_зп là điệnáp gate–подложка; chân11 thả nổi nên **chưa tính được dự trữ điện áp thực** bằng30−26,5. Quy luật gateâm dẫn đang được dùng làm giả thiết, chưa đo trực tiếp trên tấm.')
s=s.replace('Đế để thả nổi, mạch dựa vào phân cực đế nội bộ của vi mạch.','Đế để thả nổi là sự kiện đã chốt cho tấm. **Cơ chế phân cực đế nội bộ chưa được chứng minh**; không tự nối chân11 để sửa ngược kết luận thực tế.')
save(p,s)

p,s=read('01_*.md')
s=part(s,'**⇒ Vì sao A313-V.06 dùng cả Б lẫn В:**','## 4.',r'''
**Sự kiện:** U1…U12 dùngБ; U16/U17/U18 dùngВ. Datasheet gốc `168kt2.pdf` tr.3 cho U_сп/U_ип so vớiподложка:15V(Б),25V(В); gate–подложка định mức30V. Các con số này **không phải điệnáp đỉnh–đỉnh giữa hai đầu khoá**.

**Suy luận chưa đủ:** swing−23/+3,5V=26,5V không tự chứng minh lý do chọnВ, cũng không chứng minh vượt/đạt định mức25V. Đế đang thả nổi; chưa biết điện thế thực. Không suy dự trữ3,5V bằng30−26,5. Giữ đúng chủng loại gốc; thay Б↔В phải kiểm toàn bộ điều kiện, không chỉ điện áp.
''')
s=s.replace('Khoá là **MOSFET kênh p**:', '**Giả thiết có cơ sở:** hành vi gate âm dẫn phù hợp MOSFET kênh p và điều kiện thử datasheet. Chưa đo trên tấm thực; điện thế gate phải xét so với kênh/đế, không chỉ so GND:')
s=s.replace('Biên độ điều khiển 26,5 V, dự trữ so với U_зп max = 30 V chỉ còn **3,5 V** ⇒ **phải giữ nguồn −23 V đúng trị số, quá âm sẽ phá затвор.**','Hai mức trên là mô hình làm việc của tấm, cần xác nhận trên toàn dảiVin±4V. Điện áp đế thả nổi chưa biết nên không tính được dự trữ gate–đế từ swing26,5V. Giữ nguồn đúng trị số; không tự đổi đấu nối chân11.')
s=part(s,'### Lưu ý về tốc độ','## 6.',r'''
### Lưu ý về tốc độ

Datasheet ghi **t_вкл≤0,3µs và t_выкл≤0,7µs** ở điều kiện thử đế+5V; đây là hai cận trên, không phải cặp thời gian đo của một con. Không lấy hiệu0,4µs làm overlap, không khẳng định ngắt luôn chậm hơn dẫn. Trên tấm thật còn U18 nối tầng, tải gate, trở kéo10k và đế thả nổi. Đo М/М̄ cùngS/Vin để xác định chồng dẫn và dòng xung thực; chưa có chuẩn “vài chụcns”.
''')
s=s.replace('**3,2 µV** — rất nhỏ, nên **nếu thấy trôi hàng chục mV thì chắc chắn khoá đã hỏng nặng hoặc tụ rò**.','**3,2 mV** — chỉ tính riêng dòng rò giả thiết; không kết luận khoá hỏng chỉ từ tổng độ trôi khi còn các đường tải khác.')
s=s.replace('47 ms > chu kỳ 0,15 s ⇒ **kênh không nạp kịp, biên độ ra bị hụt**. Đây là triệu chứng điển hình của khoá suy giảm.','47ms < chu kỳ0,15s; thời gian cửa sổ nạp mới quyết định nạp có kịp hay không, không phải chỉ chu kỳ làm tươi. Chưa tính các điện trở nối tiếp khác của tấm.05.')
s=s.replace('2 khoá **nối tiếp** (nối tín hiệu vào) — điều khiển bằng **М̄**','1 khoá nối tiếpVin→S và1 khoá tải phụVin→R_bal→GND — cùng điều khiển bằng **М̄**')
s=s.replace('**U16** — mạng tạo trễ (hysteresis) ±0,351 V cho 2 bộ so sánh','**U16** — chọn hai ngưỡng **H14/H15 riêng biệt, đối dấu** gần±0,351V: H14=U16A.3/U16B.5; H15=U16C.10/U16D.12. A điều khiểnB/C, B điều khiểnA/D; hồi tiếp Schmitt quaU14')
s=s.replace('mạch dựa vào phân cực đế nội bộ của vi mạch.','chưa đủ tài liệu để kết luận cơ chế phân cực đế nội bộ.')
s=s.replace('nhưng đó là điều kiện đo tham số, không phải yêu cầu đấu nối bắt buộc trong ứng dụng.','đó là điều kiện bảo đảm tham số thử; không tự suy mọi tham số vẫn được bảo đảm với đế thả nổi, và không sửa ngược đấu nối thực tế đã chốt.')
s=s.replace('Đưa chân затвор lên **+3,5 V**, đo điện áp','Quan sát gate ở **+3,5V** do mạch tạo; không ép nguồn ngoài chống driver, đo điện áp')
s=s.replace('Đưa затвор xuống **−23 V**, đo sụt áp','Quan sát gate ở **−23V** do mạch tạo, đo sụt áp')
s=s.replace('≤ 100 Ω | Sụt lớn','Theo điều kiện thử/trace chuẩn;100Ω chưa bảo đảm ở đế thả nổi | Sụt lớn')
s=s.replace('**và nhất là không được có hiện tượng "break-before-make" ngược** (đóng chậm hơn mở gây overlap).','kiểm chồng dẫn thực. Break-before-make nghĩa là ngắt nhánh cũ trước khi dẫn nhánh mới; không suy tính năng này chỉ từ hai cận thời gian datasheet.')
s=s.replace('MOSFET không có tiếp giáp p-n để "đo diode" như transistor lưỡng cực.','phép diode-test đơn giản không xác minh đầy đủ chức năng MOS; vẫn có các tiếp giáp với đế và điện tích gate ảnh hưởng phép đo.')
s=s.replace('Nguồn DC −5V ──[10 kΩ]', 'Nguồn DC −5V ──[50 kΩ]')
s=s.replace('| **Điện trở kênh mở** | Bơm dòng 0,1 mA qua kênh đang mở, đo sụt áp | ≤ 10 mV (≈ 100 Ω) | > 50 mV ⇒ suy giảm |','| **Điện trở kênh mở** | Đo dòng thực và sụt áp khi khoá dẫn; không bơm nguồn chống mạch đang lái |100Ω chỉ đối chiếu khi điều kiện tương ứng datasheet | So tấm chuẩn và kiểm ngoài mạch nếu nghi |')
save(p,s)

p,s=read('02_*.md')
s=s.replace('**Hệ số khuếch đại hở mạch thấp** (1350…12000)', '**Hệ số khuếch đại hở mạch thấp** (sổ tay cũ1350…12000; PDFБВК2000…10500)')
s=part(s,'## 3. THAM SỐ','## 4.',r'''
## 3. THAM SỐ ĐIỆN — KHÔNG TRỘN BIẾN THỂ

**Nguồn gốc ưu tiên:** `140ud1B.pdf` tr.1–2 là nhãnЛСАР.431130.011ЭТ của **140УД1БВК/140УД101БВК**, theoАЕЯР.431130.171-01ТУ. Chưa xác định đồng nhất với lô140УД1Б trên tấm; thông sốsổtay cũ chỉ dùng làm giả thiết bảo thủ có ghi rõ.

| Đại lượng | PDF140УД1БВК tr.2 | Giá trịsổtay Rev.B / phạm vi áp dụng |
|---|---|---|
| Nguồn danh định | ±12,6V; RL=5,05kΩ | Phù hợp ray tấm |
| Swingra | +8V/−6,3V tại UI=±100mV | Không suy đối xứng; không suy lên sát rail |
| Vos | −7…+7mV | Phù hợp giả thiết±7mV |
| Ib | −8…+8µA | Rev.B dùng9µA; cần đúng biến thể |
| ΔIb | −1,5…+1,5µA | Rev.B dùng2,5µA; cần đúng biến thể |
| Icc | −12…+12mA tại Uo=0, nguồn±13,9V | Rev.B dùng10mA;18IC có thể216mA theo điều kiệnPDF, chưa có dòng tầngQ/tải |
| A | 2000…10500 | Rev.B dùng1350…12000 |
| Common-mode, unity bandwidth, slew, CMRR | Không được nêu trong PDF nhãn này | Các số±6V,0,1MHz,3,5V/µs,60dB của Rev.B chưa được xác minh ở đúng biến thể; không dùng để chứng nhận ATE |

Với noise gain≈2, riêngVos có thể tạo≈14mV đầu ra. ΔIb phải nhân trởhồi tiếp khi quy đầu ra: giả thiết2,5µA×10kΩ=25mV, không phải12,5mV đầu ra. Phần gainhữu hạn xấp xỉ2/A chỉ đúng khi tầngđệm/vòng còn tuyến tính và không quá tải.
''')
s=s.replace('⇒ tần số gãy ≈ 284 kHz.','⇒ 1/(2πRC)≈284kHz là tần số|Xc|=R của nhánh ngoài, không phải cực vòng kín đã được xác minh.')
s=s.replace('**Nếu R 56 Ω hở hoặc C hở ⇒ mạch tự kích cao tần**,','**Nếu R56Ω hoặcC hở có thể mất bù, gây tự kích**,')
s=s.replace('**Nếu C chập ⇒ chân 12 nối mát qua 56 Ω ⇒ khuếch đại giảm mạnh / mất tín hiệu.**','**Nếu C chập, chân12 nối mát qua56Ω**; hậu quả định lượng phải kiểm theo mạch nội/đo, không mặc định mất tín hiệu.')
a=s.index('**Vì sao R 4,7 kΩ ở chân 10:**'); b=s.index('### 5.2.',a)
s=s[:a]+r'''**Vì sao R4,7kΩ ở chân10:** Rin∥Rfb=5kΩ, nên4,7k cộngRon bù gần đúng trở nguồn vàođảo. Với `k=Rfb/Rin`, offset đầu ra:

`E≈(1+k)Vos+Rfb·Ib−−(1+k)(4,7k+Ron)·Ib+`.

Nếu thay Rbias bằng dây0Ω và bỏ quaRon, riêngIb−9µA gây **90mV đầu ra** (45mV quy đầu vào). Ở trị số danh định, cùngIb9µA gây bấtcân bằng≈5,4mV; chênh dòng2,5µA còn có thể tạo thêm tới25mV theo cận bảo thủ. Không thể kết luận sai sốcòn0,75mV hay giảm60lần. Rbias đứt hở là lỗi khác, làm mất đườngDC tới chân10.

Ngân sách góc dung sai1% củaRin/Rfb,5% củaRbias, Ron0…100Ω và thông sốgiảthiết cũ9µA/2,5µA cho cận các hạng offset≈49,8mV, chưa tính mọi sai số. Với thông sốPDFБВК, tính riêng bằng8µA/1,5µA. Xem§10.4 tài liệu phân tíchRev.C.

''' +s[b:]
s=s.replace('### 5.2. U14, U15 — bộ so sánh Schmitt của cụm tạo xung','### 5.2. U14 Schmitt và U15 với ngưỡng đối dấu')
s=s.replace('Dùng ở chế độ **hở vòng** (không hồi tiếp âm), so sánh tín hiệu chuẩn 400 Hz với ngưỡng ±0,351 V lấy từ mạng U16.','Không có hồi tiếp âm tuyến tính: U14 có hồi tiếp dương quaU17/U16. U14.10=H14 vàU15.10=H15 **không nối chung**, hai ngưỡng đối dấu gần±0,351V doU16 chọn. U15 không có vòngSchmitt độc lập. M sớm hơn xung400Hz≈357,8µs(5Vrms) hoặc528,1µs(5Vđỉnh) trong mô hình danh định; xem§5.2 tài liệu phân tíchRev.C.')
s=s.replace('K_u = 1350…12000 ⇒','Dùng A theo đúng biến thể (§3) ⇒')
s=s.replace('**U_вх синф ≤ ±6 V** | Bơm quá ±6 V vào chân 9 hoặc 10 ⇒ "khoá cứng" (latch) hoặc hỏng tầng vi sai. **Khi test A313-V.06 tuyệt đối không đưa quá ±6 V vào chân `Вых.n=` của DC12.** Dải làm việc chỉ ±4 V.','Giới hạn đúng biến thể cần tra thêm | Giữ phép thử kênh trong±4V theo dải làm việc. ±6V sổtay chưa được xác minh, không xem đó là ngưỡng hỏng hoặc được phép thử.')
s=s.replace('| Dạng sóng chân 12 | có tín hiệu, không tự kích | có sin cao tần ⇒ hỏng mạng коррекция |','| Dạng sóng chân12 | Chưa có mô hình biên độ/dạng; ghi trace chuẩn bằng đầu đo điện dung thấp | Tự kích có nhiều nguyên nhân, kiểm mạngкоррекция và vòng/tải |')
s=s.replace('| Chân 5 khi đầu vào = 0 V | gần 0 V | Bão hoà ±12 V ⇒ OA chết hoặc hồi tiếp hở |','| Chân5 khi Vin=0 | So trace chuẩn; base có thể lệch theo chiều dòngQ dùVo gần0 | Bão hòa: kiểm OA, nguồn, vòng và tải |')
s=s.replace('| Vin | Vout tốt |','| Vin | Vout danh định (chưa có cửa sổ nghiệm thu) |')
s=s.replace('| 0 V | |Vout| ≤ 20 mV |','| 0V | Gần0; đo offset, so ngân sách§5.1 |')
s=s.replace('−4,00 V ± 40 mV','Gần−4V; tỉ số haiR1% có thể lệch≈2,02% trước khi cộng offset')
s=s.replace('+4,00 V ± 40 mV','Gần+4V; đo hai cực tính để táchgain/offset')
s=s.replace('−1,00 V ± 15 mV','Gần−1V; so tuyến tính sau khi trừoffset')
s=s.replace('**dòng tiêu thụ ≤ 10 mA mỗi ray**; nếu > 15 mA ⇒ loại bỏ.','**dòng từng ray ở điều kiện xác định**; dùng giới hạn đúng biến thể (§3), không tự đặt10/15mA làm chuẩn loại mọi140УД1Б.')
save(p,s)

p,s=read('03_*.md')
s=s.replace('← dẫn khi tín hiệu ra DƯƠNG','← dẫn khi cấp dòng ra tải')
s=s.replace('← dẫn khi tín hiệu ra ÂM','← dẫn khi hút dòng từ tải')
s=s.replace('**2Т312Б dẫn ở nửa chu kỳ dương** của sóng vuông 400 Hz, cấp dòng từ +12,6 V ra tải.','**2Т312Б dẫn khi cấp dòng từ+12,6V ra tải**. Với tải thuần trở thường là nửa điện áp dương; tảiСКТ phản kháng có thể lệch dấu dòng/áp.')
s=s.replace('chỉ khi **một trong hai transistor hỏng hở** thì mới lộ rõ','khi **một trong hai transistor hỏng hở** thường lộ rõ; méo cũng có thể do thiếuheadroom, tải hay mấtổnđịnh')
s=s.replace('12,6 − 4 ≈ **8,6 V** — an toàn so với 30 V','Ở tải1kΩ, Vo4V: I_R39≈4mA(P1) hoặc4,4mA(P2); Y≈4,72…4,792V, |VCE|≈7,88…7,808V; chưa tính động')
s=s.replace('≈ 4 mA — an toàn so với 30 mA','≈4…4,4mA khi tính cảRfb, chưa tínhCfb/tải phản kháng')
s=s.replace('8,6 V × 4 mA ≈ **34 mW** — an toàn so với 225 mW','≈31,5…34,4mW xác lập với các giả thiết trên; tínhIC≈IE là xấp xỉ')
s=s.replace('I ≈ (12,6 − 0,7)/180 ≈ **66 mA** ⇒ **vượt I_к max 30 mA**, P ≈ 780 mW ⇒ **hỏng nhanh**','Mô hình base sát rail cho66,11mA, chưa phải dòng thực. P_Q=|VCE|·IC: tạiY≈11,9V thìVCE≈0,7V, không phải12V; đườngtảiR180 có cựcđại xấp xỉ12,6²/(4×180)=220,5mW nếuIC≈IE. Vẫn có thể quá dòng/nhiệt; không thửchập')
s=s.replace('Vuông ±4 V có bậc ±0,6 V ở sườn','V5≈Y±VBE theo Q đang dẫn; Y=Vo+180I_R39, không chỉ±4V')
s=s.replace('Vuông vo tròn ±4 V','TheoVo+180I_R39; chuyển tiếp gồm đường truyền trực tiếp và phầnRC')
s=s.replace('Chỉ có nửa chu kỳ âm ⇒ **2Т312Б hở**','Hụt chiều dòngdương với tải thuần trở: nghi2Т312Б, đo phân biệt với mấtnguồn/tải')
s=s.replace('**Bắt buộc thay cả cặp NPN + PNP cùng lúc** và chọn cặp bù có h_FE tương đương, nếu không hai nửa chu kỳ sẽ mất đối xứng.','Thay đúng linh kiện đã xác định hỏng; thay cảcặp/đổi chủng loại cần kiểm ổn định, dònglái và pinout. βkhác không tự gây mất đối xứng khi hồi tiếp còn bù được.')
save(p,s)

p,s=read('04_*.md')
s=s.replace('**Tải giả ≥ 400 Ω** | Với biên độ 4 V: 4 V / 400 Ω = 10 mA = đúng định mức','**Không coi400Ω là tải được bảo đảm; khởi đầu≥1kΩ thuần trở** | 400Ω lấy10mA ngoài, còn tới0,4mA hồi tiếp. Cận tổngIE10mA cho≈417Ω nhưng còn headroom,β,nhiệt vàquáđộ; xem§10.6 tài liệu chính')
s=s.replace('Dòng ngắn mạch qua R 180 Ω ≈ **66 mA** = 6,6 lần định mức ⇒ hỏng ngay','66,11mA là mô hình base sát rail, không phải dòngđothực; có nguy cơ vượt giới hạn, R180Ω không phải bảovệ ngắn mạch')
s=s.replace('Một lần chạm chập là mất 1 transistor','Tránh gây ngắn mạch quá dòng; mức hư hại phụ thuộc chếđộ/thời gian, không có cận antoàn đã xácnhận')
s=part(s,'### Ảnh hưởng của f_гр thấp','## 6.',r'''
### Giới hạn suy luận từ f_гр

f_гр củaPNP thấp hơnNPN là tham số linh kiện. **Không đủ** suy sườn âm chắc chắn chậm hơn hay coi sườn méo là “bình thường”: OA, hồi tiếpRC, tải phảnkháng và chiều dòng cùng quyết định. So trace tấm chuẩn ở đúng tải; kiểm ổn định khi thay chủng loại.
''')
s=s.replace('← dẫn khi tín hiệu ra ÂM','← dẫn khi hút dòng từ tải')
s=s.replace('**2Т203Б dẫn ở nửa chu kỳ âm** của sóng vuông 400 Hz, hút dòng từ tải về −12,6 V.','**2Т203Б hút dòng từ tải về−12,6V**. Với tải thuần trở thường ở nửa điện áp âm; tải phảnkháng phải xét chiều dòng.')
s=s.replace('12,6 − 4 ≈ **8,6 V** — an toàn so với 30 V','Tính cảR180Ω: |Y|≈4,72…4,792V, |VCE|≈7,88…7,808V cho tải1kΩ, hai phaP1/P2')
s=s.replace('≈ 4 mA — còn dự trữ so với 10 mA','≈4…4,4mA kể dòngRfb, chưa gồm quá độ/tảiC')
s=s.replace('≈ 34 mW — an toàn so với 150 mW','≈31,5…34,4mW xác lập, IC≈IE; còn phải xét nhiệt độ')
s=s.replace('Vuông vo tròn ±4 V, cân đối','Y=Vo+180I_R39; so trace ở tải xác định')
s=s.replace('**Chỉ còn nửa chu kỳ dương ⇒ 2Т203Б hở**','Hụt chiều dòngâm với tải thuần trở: nghiPNP, kiểm nguồn/tải để phân biệt')
s=s.replace('**Quy tắc phân biệt nhanh nửa chu kỳ nào hỏng:**','**Gợi ý với tải thuần trở, không phải kết luận duy nhất:**')
s=s.replace('Thay cặp bù **NPN + PNP cùng lúc**, chọn h_FE tương đương nhau.','Không bắt buộc thay cảcặp chỉ vìmộtQhỏng; nếuđổi chủng loại phải kiểm cả vòng, pinout, headroom vàdòngbase.')
s=s.replace('Lợi ích: nâng I_к max từ 10 mA lên 100+ mA ⇒ khả năng tải và khả năng chịu ngắn mạch tăng rõ rệt.','DòngđịnhmứcQmới cao hơn khôngtự chứngminh khả năng tải/chịu ngắn mạch của toàn mạch: OA, R180Ω, nhiệt và SOA vẫn giới hạn.')
save(p,s)
