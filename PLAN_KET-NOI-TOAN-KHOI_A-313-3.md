# PLAN — Lập bảng kết nối toàn khối A-313-3 (giao Codex thực hiện)

> Mẫu tham chiếu: `Excel center control/a313.xlsx`, sheet `ket_noi_chung` — bảng kết nối của khối
> **A-313-2** (cùng họ máy tính dẫn đường, kiến trúc tài liệu giống A-313-3). File đích sẽ làm
> cho khối **A-313-3**. Người dùng sẽ phản biện Codex qua nhiều vòng trước khi chốt — plan này là
> bản giao việc **vòng 1**, không phải đặc tả cuối cùng.

---

## 0. Bối cảnh bắt buộc đọc trước khi làm

1. `AGENTS.md` §3 (luật cứng), §5 (phương pháp trích netlist từ PDF, bẫy font).
2. `KE-HOACH_KIEM-TRA_A-313-3.md` §1.5 — **Y16 là tấm sườn/backplane, không có linh kiện**; Э4
   là sơ đồ kết nối ĐẦY ĐỦ toàn khối (đầu cắm ngoài ↔ Y16 ↔ các tấm ↔ tấm-tấm trực tiếp qua cáp bẹ).
3. `SO-DO-DAU-NOI_E4_A-313-3.md` — danh mục cấp khối đã chốt (mã У12/У13 đảo, У14/У15 mâu thuẫn,
   У21 = −20V, У24 = ЕУ2.072.139), §3 các chỗ chưa khớp.
4. `tmp/pdfs/review/a313-3/e4/matrix_notes.md` — toàn bộ cách đọc ma trận nội bộ Y16 (tr.153–157),
   5 số đọc chưa chắc, 2 lỗi bản vẽ nghi vấn, quy ước П1…П15 ↔ КПn ↔ tên tấm.
5. `tools/CODEX_ORCHESTRATION.md` — Codex **không được** tự ý chép/dựng lại netlist từ ảnh gốc nếu
   chưa có trong CSV đã duyệt (đã từng từ chối T04 vì lý do chính sách thiết bị quân sự — nhiệm vụ
   này KHÔNG yêu cầu đọc ảnh, chỉ xử lý dữ liệu CSV đã chép sẵn, nên không thuộc phạm vi đã từ chối;
   nói rõ điều này trong brief gửi Codex để tránh từ chối nhầm).

---

## 1. Dữ liệu nguồn — ĐÃ CÓ, chỉ đọc, không chép lại từ ảnh

| File | Nội dung | Dùng để |
|---|---|---|
| `tmp/pdfs/review/a313-3/e4/e4_all.csv` | **2877 dòng, 58 bảng** (tr.142–152): `page,photo,table,pin,signal,address,wire,note`. Đã merge + chuẩn hoá khoá bởi `e4_check.py`. | Nguồn chính để ghép net theo cột `address` (cơ chế giống `kiem_dinh_cap_chan`/`ket_noi_chung` của a313.xlsx) |
| `tmp/pdfs/review/a313-3/e4/e4_mismatch.csv` | 20 dòng kiểm chéo hai chiều KHÔNG khớp | Đưa vào sheet cảnh báo, không tự ý sửa |
| `tmp/pdfs/review/a313-3/e4/matrix_nets.csv` | **282 net đã ghép sẵn** (tr.153–157, ma trận nội bộ Y16): cột `net,members,note` (`members` = danh sách `Пn/chân` cách nhau `;`) | Nguồn chính cho phần ma trận Y16 — **đã ghép, không ghép lại** |
| `tmp/pdfs/review/a313-3/e4/p153_157_matrix.csv` | 622 điểm cắt thô (nguồn sinh ra matrix_nets.csv) | Chỉ tham chiếu khi cần truy ngược |
| `tmp/pdfs/review/a313-3/e4/matrix_notes.md` | Giải thích đầy đủ cách đọc, 5 số chưa chắc, 2 nghi lỗi bản vẽ | Đưa nguyên văn các điểm nghi vấn vào sheet cảnh báo |
| `SO-DO-DAU-NOI_E4_A-313-3.md` §2 | Danh mục 24 tấm đã chốt | Map tên bảng (У1П1, У2П1…) ↔ tên tấm (Y1, Y2…) ↔ chức năng |
| `Excel center control/Danh-muc-24-tam_A-313-3.xlsx` | Trạng thái tư liệu từng tấm (đã làm ở phiên trước) | Tham chiếu chéo, không sửa |
| `A313-3_CONTROL/KHOI_So-do-dau-noi/RE_tr142_a136.jpg`…`RE_tr152_a149.jpg` + `A313-3_CONTROL/Y16/RE_tr153_a150.jpg`…`RE_tr157_a154.jpg` | 16 ảnh gốc (11 trang Э4 khối + 5 trang Э3 ma trận Y16, 2 tài liệu khác nhau — sửa 2026-10-24) | Chỉ xem khi cần đối chiếu trực quan một ô cụ thể, không chép lại hàng loạt |

**Quan trọng — không dẫm lên dữ liệu đã chốt:** 11 chỗ sửa trong `e4_sua.py` và danh mục cấp khối
trong `SO-DO-DAU-NOI_E4_A-313-3.md` §2 là bản đã người dùng duyệt. Nếu matrix mới phát hiện mâu
thuẫn với các chỗ này, ghi vào sheet cảnh báo, **không tự sửa ngầm**.

---

## 2. Cấu trúc cột — điểm cần phản biện đầu tiên với người dùng

A313-2 (`a313.xlsx`) dùng **20 cột panel**, mỗi cột là một đầu nối vật lý riêng biệt (ПА1, ПА2,
ПА3, ПУ1-3, ОШ1-2, ПШ, У5, У6, 2Ш1-8). A-313-3 có **58 bảng** trong `e4_all.csv`, chia 3 nhóm:

| Nhóm | Ví dụ | Số bảng |
|---|---|---|
| (a) Đầu cắm ngoài khối | 3Ш1, 3Ш2, 3Ш3, 3Ш3В, 3Ш4, 3Ш4В, 3Ш7, 3Ш5 (harness У17) | 8 |
| (b) Đầu nối trên Y16 hướng về từng tấm | У16КП1…КП15 (trừ КП6, КП14) | 13 |
| (c) Đầu nối riêng của từng tấm | У1П1/П2/П3, У2П1-П3, …, У24 (một số tấm chỉ có 1 đầu, không chia П1/П2/П3) | ~37 |

**Đề xuất vòng 1 (Codex làm theo, nhưng phải trình bày để người dùng duyệt/phản biện):**
Dùng **mỗi TẤM là một cột** (gộp У1П1+У1П2+У1П3 thành một cột "Y1"), ô ghi giá trị dạng
`П<n>/<chân>` để không mất thông tin đầu nối con — giữ đúng tinh thần "cột = panel" như a313.xlsx
nhưng khớp quy ước Y1…Y24 đã dùng xuyên suốt dự án này. Cột cho nhóm (a) đầu cắm ngoài giữ nguyên
tên gốc (3Ш1…3Ш7). Nhóm (b) У16КПn **không làm cột riêng** — dùng để kiểm chéo rồi bỏ, vì nó chỉ
là ảnh gương của nhóm (c) (xem `matrix_notes.md` §3: đã kiểm 261/278 khớp).

**Phương án khác người dùng có thể chọn khi phản biện:** giữ nguyên 58 bảng = 58 cột (chi tiết hơn,
không mất thông tin П1/П2/П3 nhưng bảng rất rộng); hoặc ngược lại, gộp tất cả thành 2 cột
"Đầu nối A" / "Đầu nối B" như kiểu long-format thay vì ma trận ngang — **liệt kê rõ 3 phương án
này cho người dùng chọn ở vòng phản biện đầu tiên, đừng tự quyết một mình.**

---

## 3. Thuật toán ghép NET (tái dùng logic `e4_check.py`, không viết lại từ đầu)

1. Đọc toàn bộ `e4_all.csv` (đã là bản chuẩn hoá, khoá `(table, pin)` duy nhất).
2. Với mỗi dòng, parse cột `address` bằng đúng hàm `addrs()` + `parse_addr()` + `resolve()` trong
   `e4_check.py` (đã test bằng assert ở đầu file — **tái sử dụng nguyên hàm**, không viết hàm mới).
3. Dùng **union-find** trên tập `(table, pin)`: hai ô cùng một net nếu A trỏ `address` sang B
   HOẶC B trỏ `address` sang A (một chiều cũng đủ gộp — khác với kiểm tra "khớp hai chiều" của
   `e4_check.py` vốn chỉ để phát hiện sai sót, không phải điều kiện gộp net). Việc này giống logic
   `can_doi_chieu`/`kiem_dinh_cap_chan` trong a313.xlsx: **1 chiều vẫn đưa vào bảng nhưng đánh dấu
   cảnh báo**, không loại bỏ.
4. Với các net thuộc tr.153–157 (ma trận Y16), **lấy thẳng từ `matrix_nets.csv`** (đã ghép), map
   mỗi `Пn/chân` sang `(У16КПn, chân)` qua bảng tương ứng ở `matrix_notes.md` §1 (danh sách
   П1↔КП1…П15↔КП15, trừ П6/П14) rồi hợp nhất (union) với kết quả bước 3 bằng key `(У16КПn, chân)`
   chung.
5. Tên tín hiệu (`Tín hiệu`, cột đầu bảng) lấy theo **đa số phiếu** trong các dòng cùng net; nếu
   chia phiếu đều hoặc lệch nhiều cách viết, ghi tên dài nhất/đầy đủ nhất + liệt kê biến thể trong
   cột ghi chú (xem cách a313.xlsx xử lý ở `matrix_notes.md` cách gọi — ví dụ СИ/СИ1-1).
6. Mỗi net → một DÒNG trong sheet `ket_noi_chung`; mỗi tấm/đầu-cắm trong net → giá trị ở đúng CỘT.
7. **Net chỉ có 1 thành viên** (không ghép được với ai) → vẫn giữ dòng, đánh dấu cột "Số chiều
   tham chiếu" = "Một chiều/Không xác định" (xem mẫu `can_doi_chieu` của a313.xlsx).

---

## 4. Cấu trúc workbook đích — mirror a313.xlsx, đặt tên theo A-313-3

File đích: `Excel center control/A313-3_ket-noi-toan-khoi.xlsx` (file MỚI, không ghi đè
`a313.xlsx` — file đó là của A-313-2, giữ nguyên).

| Sheet | Nội dung | Nguồn | Ghi chú định dạng |
|---|---|---|---|
| `ky_hieu_chung` | Danh sách cột (Y1…Y24, 3Ш1…3Ш7) ↔ mã ký hiệu ↔ chức năng | `SO-DO-DAU-NOI_E4_A-313-3.md` §2 | Giống `ky_hieu_chung` của a313.xlsx |
| **`ket_noi_chung`** | **Bảng chính** — cột 1 = Tín hiệu, các cột sau = tấm/đầu cắm, ô = số chân | Thuật toán §3 | Excel **Table** (ListObject), header fill `#12304A` chữ trắng đậm, `TableStyleLight2` (banded rows), `AutoFilter` bật sẵn trên mọi cột — đúng như a313.xlsx `Table1` |
| `chi_tiet_tu_anh` | Bản phẳng từng dòng gốc (= gần như `e4_all.csv` import nguyên) | `e4_all.csv` | Dùng để truy ngược 1 ô trong `ket_noi_chung` về đúng ảnh/trang nguồn |
| `can_doi_chieu` | Các cặp chỉ có tham chiếu MỘT CHIỀU (chưa chắc cùng net) | Thuật toán §3 bước 3 | Giống `can_doi_chieu` của a313.xlsx |
| `canh_bao_quan_trong` | Toàn bộ mâu thuẫn/nghi vấn đã biết: 20 dòng `e4_mismatch.csv`, 5 số đọc chưa chắc + 2 nghi lỗi bản vẽ (`matrix_notes.md` §3-4), mâu thuẫn Y14/Y15 (`SO-DO-DAU-NOI` §2), −20V/−23V (У21) | Tổng hợp nhiều nguồn | Giống `canh_bao_quan_trong` của a313.xlsx — **copy nguyên văn cảnh báo cũ, không diễn giải lại** |
| `ghi_chu_nguon` | Thống kê: số dòng, số bảng, số net, ngày build, phiên bản script | Tự sinh | |
| `nhat_ky_ra_soat_1` | Log review VÒNG 1 — để trống khung, chờ người dùng + Codex điền khi phản biện | — | Cấu trúc cột giống `nhat_ky_ra_soat_2` của a313.xlsx: `STT, Net sửa, Giá trị trước, Giá trị sau, Căn cứ, Trạng thái` |

Các sheet `nhat_ky_ra_soat_N` tiếp theo (2, 3, …) sẽ được **thêm mới theo từng vòng phản biện**,
không sửa đè sheet vòng trước — đúng cách a313.xlsx đã làm (`nhat_ky_ra_soat_2` → `_3` →
`tong_hop_ra_soat_3` → `xac_minh_lan_4`).

---

## 5. Script thực thi — yêu cầu bắt buộc

1. Viết **một script Python** (ví dụ `tmp/pdfs/review/a313-3/e4/build_ket_noi_toan_khoi.py`),
   chạy từ gốc repo, **tự sinh lại toàn bộ workbook** từ CSV nguồn — không build tay trong Excel.
   Lý do: mỗi khi có ảnh mới/sửa CSV nguồn, chạy lại 1 lệnh là xong (đúng nguyên tắc đã áp dụng
   cho `Danh-muc-24-tam_A-313-3.xlsx`).
2. Dùng `openpyxl`. Tái sử dụng các hàm `key()`, `parse_addr()`, `addrs()`, `resolve()` từ
   `e4_check.py` bằng cách `import` trực tiếp (không copy-paste logic).
3. In ra **thống kê kiểm chứng** cuối script (số net, số dòng một-chiều, số tấm có cột, tổng số ô
   có giá trị) — giống cách `tong_hop_ra_soat_3` của a313.xlsx tổng kết.
4. Trước khi ghi đè file đích, kiểm tra không có `~$...xlsx` (file đang mở trong Excel) — xem
   `legacy-schematic-photo-archive` skill mục 8 (bài học đã gặp ở phiên này).
5. Output đặt ở `Excel center control/A313-3_ket-noi-toan-khoi.xlsx`, báo cáo bằng Markdown ngắn
   (không quá 1 trang) tóm tắt: đã sinh bao nhiêu net, bao nhiêu cảnh báo, điểm nào cần người dùng
   quyết định (đặc biệt §2 — chọn phương án cột).

---

## 6. Việc Codex KHÔNG được làm trong vòng 1

* Không tự ý "sửa" dữ liệu trong `e4_all.csv`/`matrix_nets.csv` để hết cảnh báo — mọi mâu thuẫn
  đưa vào `canh_bao_quan_trong`, giữ nguyên trạng để người dùng quyết.
* Không gộp net chỉ dựa trên tên tín hiệu giống nhau nếu không có tham chiếu `address` nào nối
  chúng (tránh lỗi "gộp nhầm nguồn/mass" đã cảnh báo trong `canh_bao_quan_trong` của chính a313.xlsx
  — ví dụ "Корпус trỏ tới +5В: nguy cơ gộp nguồn/mass sai").
* Không đọc lại ảnh gốc để bổ sung dữ liệu — mọi dữ liệu lấy từ CSV đã duyệt trong bảng §1.
* Không xoá/sửa `a313.xlsx` (file mẫu, không đụng tới) hay bất kỳ file trong
  `ЕУ.048.002.РЭ(A313-3)/` (chỉ-đọc theo AGENTS.md §3).

---

## 7. Checklist bàn giao vòng 1 (Codex tự chấm trước khi báo cáo)

- [ ] Script chạy từ gốc repo, idempotent (chạy lại không đổi kết quả nếu CSV nguồn không đổi).
- [ ] Workbook có đủ 7 sheet ở bảng §4, `ket_noi_chung` là Table có AutoFilter.
- [ ] Mọi cảnh báo cũ (20 mismatch + 5 chưa chắc + 2 nghi lỗi + Y14/Y15 + −20/−23V) đều xuất hiện
      trong `canh_bao_quan_trong`, không bị bỏ sót.
- [ ] Báo cáo cuối liệt kê rõ 3 phương án cột ở §2 để người dùng chọn ở vòng phản biện kế tiếp.
- [ ] Không chỉnh sửa file nguồn trong `tmp/pdfs/review/a313-3/e4/` (chỉ đọc, trừ khi người dùng
      yêu cầu sửa trực tiếp).
