"""Decoders for the A-313 / A313-V display words + every number quoted in PHAN-TICH_TOAN-KHOI_A313-V.md.

Run from project root:  python tmp/pdfs/review/toan-khoi/tk_codes.py
Writes tmp/pdfs/review/toan-khoi/numbers.json. Every assert below is a figure used in the document.

Bit numbering is the Soviet one used in the manuals: bit 0 = MSB of the 16-bit word.
Sources:
  self-test word ОЗУ 367₈  : A-313-1ok.pdf p.45, Bảng 12 (display groups bits 1-3 'T', 4-7, 8-11, 12-15)
  angle word  ОЗУ 000-037₈ : TMKT&HDSD A313-V Bảng 3 (bit0 good, bit1 180°, bit2 90°, bit3 45°..., bit15 PK)
  linear word               : TMKT Bảng 4 (bit0 good, bit1 unused, bit2 sign, bit3 overflow, bit4 0,5 ...)
"""
import json
from pathlib import Path

OUT = Path('tmp/pdfs/review/toan-khoi')

# Bảng 12: bit -> meaning when the bit is "1" (good). Bits 13, 14 are forced to 1, bit 3 too.
SELFTEST = {1: 'ЦВУ tốt (bộ xử lý)', 3: 'hằng "1"', 5: 'bảng thao tác tốt (liên lạc A313-6M)',
            6: 'УВВ tốt (thiết bị vào-ra, kiểm tra kênh)', 7: 'БЗ ghi-đọc tốt / ППЗУ tốt mod 2 (chế độ chuẩn bị)',
            9: 'ОЗУ ghi-đọc tốt', 10: 'ППЗУ tốt mod 2', 11: 'БЗ tốt mod 2', 13: 'hằng "1"', 14: 'hằng "1"',
            15: 'không mất chu kỳ trong КЦ'}


def selftest(code):
    """'T777000' -> list of good-flags that are missing. Display = 'T' + nibbles bits 4-7, 8-11, 12-15 + '000'."""
    assert code[0] in 'TТ' and len(code) == 7 and code[4:] == '000', code
    word = 0b0101 << 12  # bits 1 and 3 behind the 'T' (ЦВУ good + constant 1)
    for k, ch in enumerate(code[1:4]):
        word |= int(ch, 8) << (8 - 4*k)
    bit = lambda n: (word >> (15 - n)) & 1
    return [SELFTEST[n] for n in sorted(SELFTEST) if not bit(n)]


def angle(octal):
    w = int(str(octal), 8)
    good, pk = w >> 15 & 1, w & 1
    deg = ((w >> 1) & 0x3FFF) * 360 / 2**14  # bits 1..14: 180° ... 360°/2^14
    return dict(good=good, deg=deg, pk=pk)


def angle_lsb_deg(octal):
    """Tolerance written as ±N₈ on the whole word -> degrees (bit 15 is the PK flag, so N/2 angle LSBs)."""
    return int(str(octal), 8) / 2 * 360 / 2**14


def linear(octal):
    w = int(str(octal), 8)
    good, sign, ovf = w >> 15 & 1, w >> 13 & 1, w >> 12 & 1
    mag = (w & 0x0FFF) / 2**12  # bit4 = 0,5 ... (fraction of full scale)
    return dict(good=good, sign=sign, overflow=ovf, value=-mag if sign else mag)


def main():
    n = {}
    # --- self-test codes of A-313-2 Hình 101-111, mapped to failing flags ---
    assert selftest('T777000') == []
    assert selftest('T377000') == [SELFTEST[5]]               # Hình 103: liên lạc bảng điều khiển
    assert selftest('T577000') == [SELFTEST[6]]               # Hình 104: УВВ, kênh tương tự
    assert selftest('T757000') == [SELFTEST[10]]              # Hình 105
    assert selftest('T677000') == [SELFTEST[7]]               # Hình 105
    assert selftest('T657000') == [SELFTEST[7], SELFTEST[10]]  # Hình 105
    assert selftest('T737000') == [SELFTEST[9]]               # Hình 106: ОЗУ ghi-đọc
    assert selftest('T775000') == [SELFTEST[14]]              # Hình 106
    assert selftest('T776000') == [SELFTEST[15]]              # Hình 106: mất chu kỳ КЦ
    assert selftest('T773000') == [SELFTEST[13]]              # Hình 107
    n['selftest'] = {c: selftest(c) for c in ('T777000', 'T377000', 'T577000', 'T757000', 'T677000', 'T657000',
                                               'T737000', 'T775000', 'T776000', 'T773000')}
    # --- encode test (TMKT Bảng 13): 110000₈ or 150000₈ ± 200₈ ---
    a1, a2 = angle(110000), angle(150000)
    assert a1 == dict(good=1, deg=45.0, pk=0) and a2 == dict(good=1, deg=225.0, pk=0)
    assert angle_lsb_deg(200) == 1.40625 and abs(angle_lsb_deg(140) - 1.0546875) < 1e-12
    assert angle_lsb_deg(2) == 360 / 2**14  # 1 LSB = 0,02197°
    n['encode_test'] = dict(code_110000=a1, code_150000=a2, tol_200_deg=angle_lsb_deg(200),
                            tol_140_deg=angle_lsb_deg(140), lsb_deg=360 / 2**14)
    # linear word layout (Bảng 4): good flag + bit 4 (weight 0,5) = 104000₈; sign bit 2 makes it negative
    assert linear(104000) == dict(good=1, sign=0, overflow=0, value=0.5)
    assert linear(124000)['value'] == -0.5 and linear(110000)['overflow'] == 1
    # --- cycle timing: КЦ 0,15 s serves 32 abonents; ОЦ = 32 КЦ ---
    skc, oc = 0.15 / 32, 0.15 * 32
    assert abs(skc - 4.6875e-3) < 1e-12 and abs(oc - 4.8) < 1e-12
    n['cycle'] = dict(KC_s=0.15, SKC_ms=skc*1e3, OC_s=oc, note='TMKT ghi "CKЦ = 4,7s": đúng ra 4,7 ms')
    # --- A313-V.08.02 window: thresholds 2,45 / 2,55 V around 2,5 V ---
    win = (2.55 - 2.5) / 2.5
    assert abs(win - 0.02) < 1e-12
    n['power_monitor'] = dict(nominal_V=2.5, hi_V=2.55, lo_V=2.45, window_pct=win*100, claimed_pct=10)
    # --- A313-V.02 input dividers ---
    div = lambda rs, rp: rp / (rs + rp)
    assert div(5e3, 5e3) == 0.5 and abs(div(10e3, 5e3) - 1/3) < 1e-12 and abs(div(10.15e3, 5e3) - 0.33003) < 1e-5
    v_sct = 8.0
    n['divider_02'] = dict(normal=div(5e3, 5e3), ch12a=div(10e3, 5e3), ch12b=div(10.15e3, 5e3),
                           out_at_8V=v_sct*div(5e3, 5e3), out_at_12V=12*div(5e3, 5e3),
                           ref5V_ch12=5*div(10e3, 5e3),
                           bv09_160ohm_load_ohm=320, bv09_160ohm_peak_mA=v_sct/320*1e3,
                           schdoc_5k_load_ohm=10e3, schdoc_5k_peak_mA=v_sct/10e3*1e3)
    assert n['divider_02']['out_at_8V'] == 4.0 and n['divider_02']['bv09_160ohm_peak_mA'] == 25.0
    # --- A313-V.05 DC output: 330 kΩ pull-up to +12,6 V vs 3 kΩ minimum load (A-313-2 Hình 104) ---
    i_pull = (12.6 - 4.0) / 330e3
    i_load = 4.0 / 3e3
    assert abs(i_pull*1e6 - 26.06) < 0.01 and abs(i_load*1e3 - 1.3333) < 1e-3
    n['out_05'] = dict(pullup_uA_at_4V=i_pull*1e6, load3k_mA_at_4V=i_load*1e3, ratio=i_load/i_pull)
    # --- .05 package budget: 24 L1 + 6 L2 + 2 L3 + 48 cells x 2 follower sections / 4 ---
    pk = 24 + 6 + 2 + 48*2//4
    assert pk == 56
    n['pkg_05'] = dict(L1=24, L2=6, L3=2, follower=24, total=pk, bom=57, unexplained=57-pk)
    # --- inputs on 3Ш3: 15 external analog channels x 2 wires (channel 12 is internal) ---
    assert 15*2 == 30 and 11 + 4 == 15
    (OUT/'numbers.json').write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding='utf8')
    for k, v in n.items():
        print(k, v)


if __name__ == '__main__':
    main()
