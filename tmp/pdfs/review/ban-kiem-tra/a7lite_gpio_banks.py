"""Tạo a7lite_gpio_banks.csv: chân header JP1/JP2 của A7-Lite -> chân FPGA -> bank.
  a7lite_manual.txt : văn bản trang Microphase 'A7-LITE Reference Manual' (tải bằng urllib ngày 26/10/2026)
  xc7a35tfgg484_pkgpins.csv : Vivado 2022.1 (pkgpins.tcl), thuộc tính BANK của từng chân gói xc7a35tfgg484-2
"""
import csv, re
from pathlib import Path
D = Path(__file__).parent
t = (D / "a7lite_manual.txt").read_text(encoding="utf-8")
bank = {r[0]: r[1] for r in csv.reader(open(D / "xc7a35tfgg484_pkgpins.csv"))}
i, j, k = t.find("JP1: Pin"), t.find("JP2 Pin"), t.rfind("○Power")
assert 0 < i < j < k
rx = re.compile(r"(\d+) (GPIO[12]_\d+[PN]|VCC_5V|GND|VCC_3V3|VCCIO_A|NC)(?: ([A-Z]{1,2}\d{1,2})| -)?(?= \d+ |\s*$| ○)")
def parse(seg, jp):
    return [(jp, int(m.group(1)), m.group(2), m.group(3) or "") for m in rx.finditer(seg + " ")]
rows = parse(t[i:j], "JP1") + parse(t[j:k] + " ", "JP2")
for jp in ("JP1", "JP2"):
    got = sorted(r[1] for r in rows if r[0] == jp)
    assert got == list(range(1, 51)), (jp, sorted(set(range(1, 51)) - set(got)))
with open(D / "a7lite_gpio_banks.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(["jp", "jp_pin", "signal", "fpga_pin", "bank"])
    for jp, n, s, fp in sorted(rows):
        w.writerow([jp, n, s, fp, bank.get(fp, "") if fp else ""])
import collections
c = collections.Counter((r[0], bank[r[3]]) for r in rows if r[2].startswith("GPIO"))
print(sorted(c.items()))
