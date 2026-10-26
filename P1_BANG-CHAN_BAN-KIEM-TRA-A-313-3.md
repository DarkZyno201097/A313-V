# BẢNG CHÂN P1 — BÀN KIỂM TRA A-313-3 MỚI

**File sinh tự động** từ `tmp/pdfs/review/ban-kiem-tra/p1_pin_assignment.csv` bằng `p1_md.py`; sửa dữ liệu bằng `p1_assign.py`, không sửa tay file này.

Nguồn chân khối: `A313-3_ket-noi-toan-khoi.xlsx`; hướng: [A3] Bảng 4–5; chân FPGA/bank: tài liệu A7-Lite (Microphase) + Vivado 2022.1 `xc7a35tfgg484-2`.

**Trạng thái: đề xuất để đánh giá khả thi, CHƯA dùng để đặt mạch** (xem P1 §9, các cổng G1–G6).

## Tóm tắt

| Chỉ tiêu | Giá trị |
|---|---|
| Chân FPGA dùng | **77** / 86 dùng được (88 GPIO trừ U22 PUDC_B và V22 EMCCLK) → dư **9** |
| JP1 bank 16 | 38 chân |
| JP2 bank 14 | 39 chân |
| Tín hiệu khối vào FPGA | 66 (+ 22 quan sát 3Ш7; 4 không nối) |
| IC đệm 8 bit | BA1×8, BA2×8, BA3×8, BA4×8, BI1×8, BI2×8, BI3×8, BI4×3, BA5×2, BB1×1, LV1×4, SR1×8, SR2×8, SR3×6 → 13 IC đệm/dịch + 4 mạch chia áp (LV1) |

**Mức bằng chứng hướng tín hiệu (trong cột Ghi chú):** [A] bảng/văn bản HDSDKT nói thẳng; [B] suy từ biểu thức hoặc mô tả chức năng trong HDSDKT/Э4; [C] suy từ tên, **chưa xác minh**. Đường [C] chỉ vào nhóm nhận một chiều hoặc Hi-Z nên không thể lái ngược khối.

## Nhóm A — khối → bàn (đệm một chiều, FPGA chỉ đọc) — 34 đường

| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |
|---|---:|---|---|---|---|---:|---|---|---|
| 3Ш1 | 2 | КШЗП 0Р | out | BA1.1 | JP1 | 1 | F13 | 16 | [A] Bảng 5 |
| 3Ш1 | 3 | КШЗП 1Р | out | BA1.2 | JP1 | 2 | F14 | 16 | [A] Bảng 5 |
| 3Ш1 | 4 | КШЗП 2Р | out | BA1.3 | JP1 | 3 | E13 | 16 | [A] Bảng 5 |
| 3Ш1 | 5 | КШЗП 3Р | out | BA1.4 | JP1 | 4 | E14 | 16 | [A] Bảng 5 |
| 3Ш1 | 6 | КШЗП 4Р | out | BA1.5 | JP1 | 5 | D14 | 16 | [A] Bảng 5 |
| 3Ш1 | 7 | КШЗП 5Р | out | BA1.6 | JP1 | 6 | D15 | 16 | [A] Bảng 5 |
| 3Ш1 | 8 | КШЗП 6Р | out | BA1.7 | JP1 | 7 | E16 | 16 | [A] Bảng 5 |
| 3Ш1 | 9 | КШЗП 7Р | out | BA1.8 | JP1 | 8 | D16 | 16 | [A] Bảng 5 |
| 3Ш1 | 10 | КШЗП 8Р | out | BA2.1 | JP1 | 9 | D17 | 16 | [A] Bảng 5 |
| 3Ш1 | 11 | КШЗП 9Р | out | BA2.2 | JP1 | 10 | C17 | 16 | [A] Bảng 5 |
| 3Ш1 | 12 | КШЗП 10Р | out | BA2.3 | JP1 | 13 | C13 | 16 | [A] Bảng 5 |
| 3Ш1 | 13 | КШЗП 11Р | out | BA2.4 | JP1 | 14 | B13 | 16 | [A] Bảng 5 |
| 3Ш1 | 14 | КШЗП 12Р | out | BA2.5 | JP1 | 15 | A13 | 16 | [A] Bảng 5 |
| 3Ш1 | 15 | КШЗП 13Р | out | BA2.6 | JP1 | 16 | A14 | 16 | [A] Bảng 5 |
| 3Ш1 | 16 | КШЗП 14Р | out | BA2.7 | JP1 | 17 | C14 | 16 | [A] Bảng 5 |
| 3Ш1 | 17 | КШЗП 15Р | out | BA2.8 | JP1 | 18 | C15 | 16 | [A] Bảng 5 |
| 3Ш1 | 18 | КШЗП 16Р | out | BA3.1 | JP1 | 19 | A15 | 16 | [A] Bảng 5 |
| 3Ш1 | 19 | КШЗП 17Р | out | BA3.2 | JP1 | 20 | A16 | 16 | [A] Bảng 5 |
| 3Ш1 | 21 | КША-7Р | out | BA3.3 | JP1 | 21 | B15 | 16 | [A] Bảng 5 |
| 3Ш1 | 22 | КША-8Р | out | BA3.4 | JP1 | 22 | B16 | 16 | [A] Bảng 5 |
| 3Ш1 | 23 | КША-9Р | out | BA3.5 | JP1 | 23 | F16 | 16 | [A] Bảng 5 |
| 3Ш1 | 24 | КША-10Р | out | BA3.6 | JP1 | 24 | E17 | 16 | [A] Bảng 5 |
| 3Ш1 | 25 | КША-11Р | out | BA3.7 | JP1 | 25 | A18 | 16 | [A] Bảng 5 |
| 3Ш1 | 26 | КША-12Р | out | BA3.8 | JP1 | 26 | A19 | 16 | [A] Bảng 5 |
| 3Ш1 | 27 | КША-13Р | out | BA4.1 | JP1 | 27 | B17 | 16 | [A] Bảng 5 |
| 3Ш1 | 28 | КША-14Р | out | BA4.2 | JP1 | 28 | B18 | 16 | [A] Bảng 5 |
| 3Ш1 | 29 | КША-15Р | out | BA4.3 | JP1 | 31 | B20 | 16 | [A] Bảng 5 |
| 3Ш2 | 23 | ¬ЧТ. УВВ | out | BA4.4 | JP2 | 34 | V19 | 14 | [A] Bảng 5 |
| 3Ш2 | 24 | ¬ЗП УВВ | out | BA4.5 | JP2 | 35 | V17 | 14 | [A] Bảng 5 |
| 3Ш2 | 25 | ¬Вр. М1 | out | BA4.6 | JP2 | 36 | W17 | 14 | [A] Bảng 5 |
| 3Ш2 | 26 | ВРМ2 | out | BA4.7 | JP2 | 37 | U17 | 14 | [A] Bảng 5 |
| 3Ш2 | 27 | СБОЙ | out | BA4.8 | JP2 | 38 | U18 | 14 | [C] СБОЙ mod 2 do khối tạo (HDSDKT hình 16); Э4 không ghi địa chỉ đích; nhận một chiều nên an toàn dù sai |
| 3Ш2 | 32 | ПРЕДВАРИТ.ОТКАЗ | out | BA5.1 | JP2 | 39 | P14 | 14 | [C] tên «cảnh báo hỏng sớm»; Э4 không ghi địa chỉ; nhận một chiều nên an toàn dù sai |
| 3Ш2 | 44 | ЗП.КПА | out | BA5.2 | JP2 | 40 | R14 | 14 | [B] «yêu cầu Чт, Зп ЦВУ, Зп КПА» do khối tạo (HDSDKT hình 12) |

## Nhóm B — bàn → khối (đệm một chiều, OE do DRV_EN_UUT_N) — 27 đường

| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |
|---|---:|---|---|---|---|---:|---|---|---|
| 3Ш2 | 2 | КШЧТ 0Р | in | BI1.1 | JP2 | 1 | W21 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 3 | КШЧТ 1Р | in | BI1.2 | JP2 | 2 | W22 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 4 | КШЧТ 2Р | in | BI1.3 | JP2 | 3 | N17 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 5 | КШЧТ 3Р | in | BI1.4 | JP2 | 4 | P17 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 6 | КШЧТ 4Р | in | BI1.5 | JP2 | 5 | P19 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 7 | КШЧТ 5Р | in | BI1.6 | JP2 | 6 | R19 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 8 | КШЧТ 6Р | in | BI1.7 | JP2 | 7 | R18 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 9 | КШЧТ 7Р | in | BI1.8 | JP2 | 8 | T18 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 10 | КШЧТ 8Р | in | BI2.1 | JP2 | 9 | T21 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 11 | КШЧТ 9Р | in | BI2.2 | JP2 | 10 | U21 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 12 | КШЧТ 10Р | in | BI2.3 | JP2 | 15 | Y21 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 13 | КШЧТ 11Р | in | BI2.4 | JP2 | 16 | Y22 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 14 | КШЧТ 12Р | in | BI2.5 | JP2 | 17 | AA20 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 15 | КШЧТ 13Р | in | BI2.6 | JP2 | 18 | AA21 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 16 | КШЧТ 14Р | in | BI2.7 | JP2 | 19 | AB21 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 17 | КШЧТ 15Р | in | BI2.8 | JP2 | 20 | AB22 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 18 | КШЧТ 16Р | in | BI3.1 | JP2 | 21 | AA19 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 19 | КШЧТ 17Р | in | BI3.2 | JP2 | 22 | AB20 | 14 | [A] Bảng 4 [A3] |
| 3Ш2 | 21 | ¬ИВЧ | in | BI3.3 | JP2 | 23 | U20 | 14 | [A] Bảng 4: ИВЧ; tải sink lớn, xem P1 §9.3 |
| 3Ш2 | 22 | ¬ИКО | in | BI3.4 | JP2 | 24 | V20 | 14 | [A] tr.24 [A3] «kết thúc chu kỳ… từ A-313-2 đưa ra ИКО», Bảng 4 (Bảng 5 cũng ghi ИКО: coi là ghi trùng, kiểm khi đo) |
| 3Ш2 | 40 | Рг К1 КПА | in | BI3.5 | JP2 | 25 | Y18 | 14 | [B] biểu thức РгПр∧(РМКПА∨РгК1КПА∨РгК2КПА) [A3]: tín hiệu từ КПА (= ПС17-318) |
| 3Ш2 | 41 | Рг К2 КПА | in | BI3.6 | JP2 | 26 | Y19 | 14 | [B] như 40 |
| 3Ш2 | 42 | Рг М КПА | in | BI3.7 | JP2 | 27 | W19 | 14 | [B] như 40 |
| 3Ш2 | 45 | ЗАПРЕТ.ОБРАЩ. | in | BI3.8 | JP2 | 28 | W20 | 14 | [B] công tắc ЗАПРЕТ trên bàn Nga (HDSDKT bước 8); biểu thức СТРОБ∧ЗАПРЕТ ВрМ |
| 3Ш2 | 46 | ЗАПРЕТ.ВРМ | in | BI4.1 | JP2 | 31 | AA18 | 14 | [B] như 45; Э4 ghi thêm đích 3Ш4/52 |
| 3Ш2 | 47 | ЗАПРЕТ.РМ | in | BI4.2 | JP2 | 32 | AB18 | 14 | [B] như 45 |
| 3Ш2 | 48 | ВХОД ПР."П" Т.Т.Л | in | BI4.3 | JP2 | 33 | V18 | 14 | [B] «Вх "П" ТТл» là lệnh đơn nhanh đưa vào BUS (HDSDKT, bộ điều khiển lệnh) |

## Nhóm C — hai chiều/chưa rõ ai lái (DIR, mặc định Hi-Z) — 1 đường

| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |
|---|---:|---|---|---|---|---:|---|---|---|
| 3Ш2 | 20 | ПРИНУДИТ.ЗАПУСК | bi | BB1.1 | JP2 | 43 | P16 | 14 | [C] Э4: У1П2/47; chưa biết ai lái; mặc định Hi-Z |

## Nhóm F — đường mức không phải TTL (chia áp/kẹp rồi vào FPGA; chỉ đọc) — 4 đường

| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |
|---|---:|---|---|---|---|---:|---|---|---|
| 3Ш2 | 35 | ИСПР.ПИТАНИЯ ЦВУ | lvl | LV1.1 | JP2 | 44 | R17 | 14 | [B] Y24 tạo: tốt = 5,2±1 V, hỏng < 0,5 V (HDSDKT, mạch Y24); vượt 5,5 V → chia áp |
| 3Ш2 | 36 | НАПР.ВЫШЕ НОРМЫ | lvl | LV1.2 | JP2 | 45 | N13 | 14 | [C] Э4: У24/8; mức chưa có số; chia áp trước, đo thật |
| 3Ш2 | 37 | НАПР.НИЖЕ НОРМЫ | lvl | LV1.3 | JP2 | 46 | N14 | 14 | [C] Э4: У24/18; mức chưa có số; chia áp trước, đo thật |
| 3Ш2 | 39 | ИСПРАВН.ПИТ.ППЗУ | lvl | LV1.4 | JP2 | 47 | P15 | 14 | [B] Y24: tốt ≤ 0,5 V, hỏng ≥ 15 V (HDSDKT); **tới 15 V → bắt buộc chia áp/kẹp** |

## Nhóm N — không nối (Э4 gạch xoá), chân khối để hở — 4 đường

| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |
|---|---:|---|---|---|---|---:|---|---|---|
| 3Ш2 | 28 | ВНЕШН.ПРЕРЫВ | - |  |  |  |  |  | [B] Э4: dòng bị gạch xoá, địa chỉ У16КП1/32 để trống; không nối, giữ chân dự phòng |
| 3Ш2 | 29 | ВНЕШН.ПРЕРЫВ | - |  |  |  |  |  | [B] như 28 (У16КП1/33) |
| 3Ш2 | 30 | ВНЕШН.ПРЕРЫВ | - |  |  |  |  |  | [B] như 28 (У16КП1/34) |
| 3Ш2 | 31 | ВНЕШН.ПРЕРЫВ | - |  |  |  |  |  | [B] như 28 (У16КП1/35) |

## Nhóm D — quan sát 3Ш7 (thanh ghi dịch vào, chỉ đọc) — 22 đường

| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |
|---|---:|---|---|---|---|---:|---|---|---|
| 3Ш7 | 8 | СТРОБ1 | obs | SR1.1 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 9 | СТРОБ1-1 | obs | SR1.2 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 10 | СТРОБ2 | obs | SR1.3 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 11 | СТРОБ3 | obs | SR1.4 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 12 | 0р. СчК | obs | SR1.5 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 13 | 1р. СчК | obs | SR1.6 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 14 | 2р СчК | obs | SR1.7 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 15 | 3р СчК | obs | SR1.8 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 16 | 4р. СчК | obs | SR2.1 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 17 | 5Р СЧК | obs | SR2.2 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 18 | 6Р СЧК | obs | SR2.3 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 19 | 7Р СЧК | obs | SR2.4 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 20 | 8Р СЧК | obs | SR2.5 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 21 | 9Р СЧК | obs | SR2.6 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 22 | 10Р СЧК | obs | SR2.7 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 23 | 11Р СЧК | obs | SR2.8 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 24 | 12Р СЧК | obs | SR3.1 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 34 | УПР. К1 | obs | SR3.2 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 35 | УПР. К2 | obs | SR3.3 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 36 | УПР. К3 | obs | SR3.4 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 37 | УПР. К4 | obs | SR3.5 |  |  |  |  | đọc nối tiếp, chỉ quan sát |
| 3Ш7 | 40 | БЛОКИРОВКА ЗАЩИТЫ | obs | SR3.6 |  |  |  |  | đọc nối tiếp, chỉ quan sát |

## Nhóm E — điều khiển bàn trên JP1 — 11 đường

| Đầu nối | Chân khối | Tín hiệu | Hướng | IC.kênh | Header | Chân header | Chân FPGA | Bank | Ghi chú |
|---|---:|---|---|---|---|---:|---|---|---|
| BÀN |  | DRV_EN_UUT_N | out |  | JP1 | 32 | A20 | 16 | OE cho nhóm B-in; kéo lên bằng điện trở ngoài để Hi-Z khi FPGA chưa nạp (PUDC_B) |
| BÀN |  | DIR_BB1 | out |  | JP1 | 33 | F19 | 16 | DIR đệm hai chiều BB1 (1 đường: ПРИНУДИТ.ЗАПУСК) |
| BÀN |  | OE_BB_N | out |  | JP1 | 34 | F20 | 16 | OE nhóm C-bi; kéo lên ngoài |
| BÀN |  | SR_CLK | out |  | JP1 | 35 | E19 | 16 | SPI/nối tiếp mở rộng 3Ш7: SCK |
| BÀN |  | SR_LOAD_N | out |  | JP1 | 36 | D19 | 16 | tải song song SR1…SR3 |
| BÀN |  | SR_MISO | in |  | JP1 | 37 | C18 | 16 | dữ liệu nối tiếp về |
| BÀN |  | ESTOP_IN | in |  | JP1 | 38 | C19 | 16 | nút ngắt khẩn cứng (mức an toàn khi mất dây) |
| BÀN |  | RES_1 | - |  | JP1 | 39 | F18 | 16 | dự phòng |
| BÀN |  | RES_2 | - |  | JP1 | 40 | E18 | 16 | dự phòng |
| BÀN |  | RES_3 | - |  | JP1 | 43 | D20 | 16 | dự phòng |
| BÀN |  | RES_4 | - |  | JP1 | 44 | C20 | 16 | dự phòng |

## Chân không nối vào FPGA (ghi để không gán nhầm)

- 3Ш1: 9 chân КОРПУС (1, 20, 30, 31, 44, 45, 47, 49, 50) và 14 chân rail (+20, +6,3 ×2, +5 ×7, +10, −6,3, −10, −5 В: chân 32–43, 46, 48). Khối nối rail ra đầu nối này: **không nối vào bàn P1**, chỉ đo bằng đầu dò khi cần (xem P1 §9 G5).
- 3Ш2: 4 chân КОРПУС (1, 38, 49, 50) và chân 33, 34 = **+27 В** (hướng chưa rõ, không nối).
- 3Ш7: 1 chân КОРПУС (1) và 7 chân Упр./УПР rail (26–32), không nối FPGA.
- Header A7-Lite: chân 11, 12, 29, 30, 41, 42 là nguồn/mát (không GPIO), không dùng làm tín hiệu.
- FPGA: U22 (PUDC_B) và V22 (EMCCLK) trên JP2 chân 13, 14 — tránh gán tín hiệu để không ảnh hưởng cấu hình.
