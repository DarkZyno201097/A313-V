# Prompt chuyển giao: Codex tiếp tục dự án A313-V / A-313-3

> Dán nguyên khối dưới đây vào Codex (CLI hoặc Desktop) tại thư mục repo `A313-V`.
> Soạn 2026-10-22 bởi Claude (phiên Local). Trạng thái tham chiếu: nhánh `main` (đã gộp `codex/y1-y7-audit`), thư mục repo `2.BO TLTK DAU A_A313-V`.

---

Bạn tiếp nhận toàn bộ dự án A313-V từ Claude. Từ giờ bạn làm trực tiếp với người dùng, không qua Claude.

## Bối cảnh (nói thẳng, không lược bớt)

Đây là repo private của kỹ sư sửa chữa Phân xưởng 5 — Nhà máy A32. Đối tượng là khối máy tính dẫn đường
A313-V của máy bay Su-27 (bản Việt Nam chế tạo lại) và khối gốc Nga A-313-3 đang được khôi phục làm dự phòng.
Công việc: đọc tài liệu kỹ thuật (bản vẽ Э3, перечень, bảng đầu nối Э4), chép thành CSV, kiểm chéo bằng script,
để phục vụ chẩn đoán và sửa chữa thiết bị đang hỏng.

Lưu ý trung thực: ngày 2026-10-22, ở nhiệm vụ T04 (chép sơ đồ рис.6), Codex đã từ chối tiếp tục vì đây là thiết
bị avionics quân sự (`codex-runs/T04-ric06-y3/r2/last.md`). Nếu bạn vẫn giữ quyết định đó cho một phần việc nào,
hãy nói rõ ngay phần nào làm được, phần nào không, rồi làm phần làm được. Không cần xin lỗi dài.

## Đọc trước, theo thứ tự

1. `AGENTS.md` — luật cứng §3 (tài liệu gốc chỉ-đọc, repo private, mọi con số phải có script), §4.9.
2. `PROJECT_HANDOFF.md` — đọc kỹ §11, §12, §12.1 (trạng thái A-313-3 và các nhiệm vụ T01–T04).
3. `tools/CODEX_ORCHESTRATION.md` §5–6 — bài học từ các lượt trước.
4. `tmp/pdfs/review/a313-3/e3/ric11_mota.md`, `ric08_mota.md`, `ric06_mota.md` — ba hình đã chép.
5. `DANH-MUC_ANH_RE_A-313-3.md` — tra trang ↔ ảnh ↔ рис. (tên file ảnh: `tmp/pdfs/review/a313-3/kiemke/trang.csv`).

Kiểm thực tế trước khi tin bất kỳ con số nào trong handoff: `git status`, `git log --oneline -8`, chạy lại các lệnh kiểm dưới đây.

## Trạng thái hiện tại (đã kiểm 2026-10-22)

| Hình | Tấm | Kết quả | Còn lại |
|---|---|---|---|
| рис.19–26 | nguồn + У24 | PASS (phiên cloud) | 2 ngoại lệ bản vẽ đã biết |
| рис.11 | Y7 | PASS — 166 ref, 462 chân, Э3↔Э4 khớp 105/105 | — |
| рис.8 | Y5 | PARTIAL — 948 chân, 169 dòng `?`, Э3↔Э4 121 khớp / 3 lệch / 36 chỉ-Э4 | Soát У8–У25 trên ảnh #168 (vùng nếp gấp) |
| рис.6 | Y3 | PARTIAL (Claude chép) — 818 chân, 166 «НЕ ПРОСЛЕЖЕНО», Э3↔Э4 125/32/1/9 | Lần các thanh dọc tờ 2, tờ 3 |
| рис.5, 7, 9, 10 | Y4, Y6, Y2, Y1 | chưa chép | Y4 thiếu hẳn Э3; Y6 thiếu trang 167; Y1 thiếu trang 180 |
| Э4 | Y16 | đã chép, ~240 ô `?` chưa soát | |

Nghi vấn mở: ảnh #155/#156 có R5–R8, C7, C8 nhưng ПЭ рис.6 không có ⇒ có thể không thuộc рис.6 (chưa sửa danh mục).

## Việc tiếp theo, theo ưu tiên

1. **Chờ người dùng chụp lại** tờ 2/3 рис.6 và ảnh #168 рис.8. Khi có ảnh mới: soát các dòng `?`/«НЕ ПРОСЛЕЖЕНО»
   của `ric06_net.csv` và `ric08_net.csv`. Với рис.6, sửa trong `ric06_gen.py` (dữ liệu sinh từ script), không sửa CSV tay.
2. **Chép рис.9 (Y2)**: ảnh Э3 #171/#172 (trang 175–176), ПЭ #173/#174; Э4 bảng `У2П1/П2/П3` ở `e4/p150.csv`.
   Theo đúng mẫu `ric11_*` / `ric06_*`; thêm `9` vào tuple và nếu cần vào `KNOWN` của `e3_check.py`.
3. Sau đó рис.10 (Y1), рис.7 (Y6, phần có ảnh), rồi soát ô `?` của Э4.

## Quy tắc làm việc (bắt buộc)

- KHÔNG đoán. Chỗ không đọc được: ghi `?` kèm số ảnh + vùng; chân thấy mà không lần được: net `НЕ ПРОСЛЕЖЕНО <ref>.<pin>`.
  Không lấy tên/chân từ Э4 hay datasheet để lấp Э3. Mâu thuẫn giữa các nguồn: giữ cả hai, ghi vào mota.
- Tài liệu gốc (ảnh, PDF A32, `ЕУ.048.002.РЭ_A313-3/`) chỉ-đọc.
- Đọc ký hiệu: phóng to vùng ảnh (PIL crop, ghi ra thư mục tạm ngoài repo), xoay ảnh cho chữ thẳng.
- Kết quả рис.11 (105/0/0/1), рис.8 (121/3/0/36), рис.6 (125/32/1/9) **không được đổi** trừ khi bạn chủ động sửa
  hình đó và giải thích trong mota.
- Sau mỗi nhiệm vụ: chạy lệnh kiểm, commit checkpoint trên nhánh làm việc, cập nhật `PROJECT_HANDOFF.md` §12.1,
  báo cáo cho người dùng theo mẫu dưới, rồi **dừng chờ người dùng duyệt** trước nhiệm vụ kế.
- Không `git push`, không merge vào `main`, không force/reset khi người dùng chưa đồng ý.
- Trả lời tiếng Việt, dấu thập phân là dấu phẩy.

## Lệnh kiểm (chạy từ gốc repo)

```
python tmp/pdfs/review/a313-3/e3/ric06_gen.py tmp/pdfs/review/a313-3/e3
python tmp/pdfs/review/a313-3/e3/e3_check.py
python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 6 У3
python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 8 У5
python tmp/pdfs/review/a313-3/e3/e3_vs_e4.py 11 У7
python tmp/pdfs/review/a313-3/e4_check.py
```

## Mẫu báo cáo sau mỗi nhiệm vụ

TASK REPORT — Task ID · Trạng thái PASS/PARTIAL/FAIL · Đã hoàn thành · File thay đổi · Kết quả kiểm tra (dán output) ·
Chưa hoàn thành (số `?` trước/sau) · Git checkpoint (nhánh, commit) · Nhiệm vụ đề xuất tiếp theo.

Bắt đầu: đọc theo thứ tự trên, chạy lệnh kiểm, rồi tóm tắt cho người dùng trong 10 dòng (trạng thái, việc dở,
việc kế tiếp) và chờ người dùng chọn nhiệm vụ.
