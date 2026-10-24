"""Kiểm riêng ric15 (Интегратор, рис.15) KHÔNG sửa e3_check.py gốc.

Chạy: python3 tmp/pdfs/review/a313-3/e3/check_ric15.py
"""
import sys
from pathlib import Path

D = Path(__file__).parent
sys.path.insert(0, str(D))
from e3_check import check  # noqa: E402

ok = check(15)
print("check(15) ->", "PASS" if ok else "FAIL")
