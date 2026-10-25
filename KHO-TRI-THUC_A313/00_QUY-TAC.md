---
id: quy-tac
loai: quy-tac
ap-dung: A-313
tu-khoa: [kho tri thức, quy tắc, cách tra, cách thêm mục]
cap-nhat: 2026-10-25
---
# Quy tắc kho tri thức A313

Kho dùng chung cho mọi AI (Claude, Codex, Hermes) và người làm dự án A-313 (A313-V, A-313-3).
Kho **không chép dữ liệu**: mỗi mục tóm tắt và liên kết tới file gốc (ảnh quét, netlist, phân tích).

## Cách tra
1. Mở [00_INDEX.md](00_INDEX.md): bảng 24 tấm, bảng «hỏi gì đọc đâu», danh sách từ khoá.
2. Hoặc tìm theo từ khoá: `rg -i "<từ khoá>" KHO-TRI-THUC_A313`.
3. Đọc mục trong kho, rồi **mở file nguồn được liên kết** trước khi dùng con số hay kết nối nào.

## Mức tin cậy (trường `do-tin-cay`, và nhãn trong thân bài)
| Mức | Nghĩa |
|---|---|
| `HDSD` | lấy từ hướng dẫn sử dụng kỹ thuật (bản dịch tiếng Việt, có thể mất đơn vị/hình) |
| `da-kiem-cheo` | đã đối chiếu ≥ 2 nguồn độc lập hoặc bằng script |
| `chep-tu-anh` | chép tay từ ảnh sơ đồ, chưa kiểm chéo đầy đủ |
| `suy-luan` | suy luận của người/AI, cần kiểm trên tài liệu hoặc phần cứng |

Trong thân bài, mỗi khẳng định gắn nguồn trong ngoặc vuông, ví dụ «[HDSD A-313-3 §2.1]», «[ảnh a250]», «[suy luận]».

## Cấu trúc
| Thư mục | Nội dung |
|---|---|
| `tong-quan/` | tổng quan thiết bị A-313 và khối A-313-3 |
| `tam/Y01.md … Y24.md` | mỗi tấm một trang: phần viết tay ở trên, phần **tự sinh** dưới dòng `<!-- AUTO -->` |
| `tra-cuu/` | (chưa có) thuật ngữ, tín hiệu, đầu nối — chỉ thêm khi người dùng cho phép |
| `tools/kb_check.py` | kiểm liên kết, sinh phần AUTO của trang tấm và bảng trong 00_INDEX.md |

## Cách thêm hoặc sửa mục
- **Chỉ thêm file mới vào kho khi người dùng cho phép hoặc yêu cầu.**
- Mỗi file bắt đầu bằng khối khai báo `id, loai, ap-dung, tu-khoa, nguon, do-tin-cay, cap-nhat`.
- Liên kết dùng đường dẫn tương đối, đặt trong `< >` khi có dấu cách: `[ảnh](<../../A313-3_CONTROL/Y4/RE_tr158_a250.jpg>)`.
- Không sửa phần dưới `<!-- AUTO -->` bằng tay; chạy lại script.
- Sau khi sửa: `python KHO-TRI-THUC_A313/tools/kb_check.py` phải thoát mã 0 (không liên kết hỏng, không ảnh/netlist nào bị bỏ sót).
- Dấu thập phân là dấu phẩy. Tài liệu gốc chỉ-đọc (xem `AGENTS.md` / `CLAUDE.md` §3).
