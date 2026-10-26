r"""Đọc tệp .MNL (OrCAD Layout V7.00, nhị phân) của bàn kiểm Nga: danh sách linh kiện + net.

Cấu trúc suy ra bằng đối chiếu (CHƯA có tài liệu định dạng, đây là kỹ thuật đảo ngược):
  chuỗi  = 05 00 <len:2> <bytes>\0 (len gồm cả \0)
  net    = chuỗi(tên net) + 0b 00 2c 00 <40 byte> + n × [chuỗi(số chân) + 0c 00 24 00 <32 byte>]
           trong 32 byte pin: offset 22 (u32) = chỉ số linh kiện, offset 26... (u32 field2) = chỉ số net
  linh kiện = chuỗi(ref) + chuỗi(package) + chuỗi rỗng + chuỗi(tên part)
Mọi kết luận phải được kiểm bằng cách đối chiếu với bộ chép tay (ric*_net.csv), xem mnl_check.py.
"""
import re, struct, sys, collections
from pathlib import Path

REF = re.compile(rb"^[A-Z]{1,3}\d+(?:-\d+)?$")

def strings(b):
    out = []
    i = 0
    n = len(b)
    while i < n - 4:
        if b[i] == 5 and b[i + 1] == 0:
            ln = b[i + 2] | (b[i + 3] << 8)
            if 1 <= ln <= 120 and i + 4 + ln <= n and b[i + 3 + ln] == 0:
                s = b[i + 4:i + 3 + ln]
                if all(32 <= c < 256 for c in s):
                    out.append((i, s))
                    i += 4 + ln
                    continue
        i += 1
    return out

def parse(path):
    b = Path(path).read_bytes()
    st = strings(b)
    # ---- nets: chuỗi tên + header 0b 00 2c 00
    nets = []
    for k, (off, name) in enumerate(st):
        e = off + 4 + len(name) + 1
        if b[e:e + 4] == b"\x0b\x00\x2c\x00":
            nets.append((off, e, name))
    # pin: chuỗi + 0c 00 24 00
    pins = []
    for off, name in st:
        e = off + 4 + len(name) + 1
        if b[e:e + 4] == b"\x0c\x00\x24\x00":
            pins.append((off, e + 4, name))
    # gắn pin vào net theo vị trí
    net_of = {}
    res_nets = collections.OrderedDict()
    ni = -1
    allrec = sorted([(o, 'n', nm, e) for o, e, nm in nets] + [(o, 'p', nm, d) for o, d, nm in pins])
    cur = None
    for o, t, nm, e in allrec:
        if t == 'n':
            cur = nm.decode('cp1251')
            res_nets.setdefault(cur, [])
        elif cur is not None:
            data = b[e:e + 32]
            comp = struct.unpack_from('<I', data, 22 - 4 + 0)[0] if False else None
            res_nets[cur].append((nm.decode('cp1251'), data))
    return b, st, res_nets

def components(b, st):
    comps = []
    for k in range(len(st) - 1):
        off, s = st[k]
        off2, s2 = st[k + 1]
        if REF.match(s) and off2 == off + 4 + len(s) + 1:
            comps.append((s.decode(), s2.decode('cp1251')))
    return comps

if __name__ == "__main__":
    b, st, nets = parse(sys.argv[1])
    comps = components(b, st)
    print("strings", len(st), "nets", len(nets), "pins", sum(len(v) for v in nets.values()), "comps", len(comps))
    print(comps[:12])
    for nm, pl in list(nets.items())[:4]:
        print(nm, [(p, d[:32].hex()) for p, d in pl][:3])
