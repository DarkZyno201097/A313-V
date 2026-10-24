### 1. Tóm tắt

Có một xung đột phạm vi cần giải quyết trước: `e3_vs_e4.py` hiện chỉ hỗ trợ **У5 và У7**, nhưng bạn chỉ cho sửa `ric06_*` và tuple trong `e3_check.py`.

| Ảnh | Tờ | Căn cứ hiện đã kiểm |
|---|---|---|
| #232 | 1/3 | Đọc được «Рис.6 (лист 1 из 3)», ЕУ3.057.136 Э3 |
| #155–#158, #231 | Chưa xác định trực tiếp | Mới tra danh mục, chưa kiểm ảnh |

### 2. File sửa

Chưa sửa hoặc tạo file.

### 3. Output kiểm

`python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 6 У3` — **exit 1**:

```text
AssertionError: chưa biết file Э4 của У3
```

Chưa chạy các lệnh còn lại.

### 4. `?` còn lại

Chưa tạo netlist nên chưa có số đếm.

### 5. Lệch/ONLY_E4

Chưa đối chiếu được vì script chưa hỗ trợ У3.

### 6. Chưa làm

Chưa chép BOM/netlist và kiểm các tờ còn lại. Để đáp ứng lệnh kiểm bắt buộc, cần cho phép sửa thêm đúng một dòng trong `e3_vs_e4.py`:

```python
E4_FILES = {"У3": "p151.csv", "У5": "p151.csv", "У7": "p152.csv"}
```

**Bạn cho phép mở rộng phạm vi bằng thay đổi một dòng này chứ?**

Chưa kiểm đầy đủ nguồn ảnh; chưa có kết luận về topology hoặc độ đầy đủ của рис.6.