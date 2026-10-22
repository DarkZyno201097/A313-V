"""Tính dải chỉnh ngưỡng của У24 (рис.19) từ trị số danh mục. Chạy: python3 e3_ric19_tinh.py
Giả thiết: Uст Д818Д = 9 В, Д814Д = 13 В (danh định), bỏ qua tải 47k/120k và sụt áp diode
(диод 2Д510А bù sụt áp ma trận diode nên triệt tiêu xấp xỉ)."""
VZ, P = 9.0, 4.7  # Д818Д, СП5-3 4,7 kΩ

def kmax(rs):  # hệ số chia lớn nhất: biến trở 4,7k (chạy hết) nối tiếp rs từ đầu nóng
    return P / (rs + P)

print('Kênh dương/âm: U_danh, R nối tiếp, U con chạy tối đa (đầu dưới biến trở = КОРПУС)')
for u, rs, r in [(5, 0, 'R5/R46'), (6.3, 1.8, 'R1+R6 / R51?+R47'), (10, 4.7, 'R2+R7 / R52+R48'),
                 (12.6, 5.6, 'R3+R8 / R53+R49'), (20, 12, 'R4+R9 / R54+R50')]:
    print(f'  {u:5.1f} В  {r:18s} Rs={rs:4.1f}k  Uдв.max={u*kmax(rs):5.2f} В  (k_max={kmax(rs):.3f})')
print(f'Ngưỡng thấp (+): R12 4,7k + R15 4,7k từ {VZ} В -> con chạy 0..{VZ*P/(4.7+P):.2f} В')
print(f'Ngưỡng cao (+): R16 5,1k + R17 4,7k từ {VZ} В (nếu R17.2 = КОРПУС) -> 0..{VZ*P/(5.1+P):.2f} В')
print(f'Ngưỡng (−): R57 5,1k + R58 4,7k -> −{VZ*P/(5.1+P):.2f}..0 В; R60 4,7k + R59 4,7k -> −{VZ*P/(4.7+P):.2f}..0 В')
print(f'R22 15k / R23 5,6k từ Vref {VZ} В -> {VZ*5.6/(15+5.6):.2f} В (chuẩn so sánh của У9/У10)')
print(f'I(Д1) = (27−9)/1,5k = {(27-9)/1.5:.1f} mA, P(R10) = {(27-9)**2/1500:.3f} W')
print(f'I(Д19) = (12,6−9)/0,33k = {(12.6-9)/0.33:.1f} mA, P(R55) = {(12.6-9)**2/330:.3f} W')
print(f'Nếu Д3.а = КОРПУС: I(R14) = (27−13)/1k = {(27-13)/1:.1f} mA, P(R14) = {(27-13)**2/1000:.3f} W')
print(f'27 В −15 % = {27*0.85:.2f} В; +10 % = {27*1.1:.2f} В')
