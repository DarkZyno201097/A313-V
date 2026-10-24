"""Kiem tra rieng cho ric17 (рис.17 - Y11, A-313-3), goi truc tiep check(17)
tu e3_check.py (KHONG sua e3_check.py goc).

Chay tu goc repo:  python3 tmp/pdfs/review/a313-3/e3/check_ric17.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from e3_check import check  # noqa: E402

if __name__ == '__main__':
    ok = check(17)
    print('check(17) ->', 'PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)
