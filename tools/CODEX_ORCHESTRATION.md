# Điều phối Claude (Orchestrator) ↔ Codex (Executor) — cách vận hành

Kiểm thử thật trên máy này ngày 2026-10-22: `codex-cli 0.163.0`, đăng nhập ChatGPT
(`codex login status` → "Logged in using ChatGPT"). Không dùng API key trả phí.

## 1. Kênh đã chọn: `codex exec` (CLI)

| Kênh | Giao việc | Nhận kết quả | Tiếp phiên cũ | Kết luận |
|---|---|---|---|---|
| `codex exec --json -o FILE` | stdin | `-o` ghi câu trả lời cuối; `--json` ghi sự kiện + `thread_id` | `codex exec resume <thread_id>` — đã thử, nhớ đúng ngữ cảnh | **Mặc định** |
| `codex queue --thread X --message` | đẩy tin vào phiên Desktop | không trả về gì | — | Chỉ để nhắn, không đủ cho vòng kiểm tra |
| `codex app-server` / `remote-control` | experimental | — | — | Chưa dùng |

## 2. Quy trình một nhiệm vụ

1. Claude viết `codex-runs/<ID>/task.md`: bối cảnh, file nguồn, việc phải làm, ràng buộc,
   **định dạng báo cáo bắt buộc**, tiêu chí đạt.
2. Claude chạy (Codex làm trong worktree riêng, không chung file với Claude):
   ```bash
   tools/codex_run.sh codex-runs/<ID>/task.md ../A313-V_codex codex-runs/<ID>/r1
   ```
   `CODEX_SANDBOX=workspace-write` khi nhiệm vụ cần sửa file; mặc định `read-only`.
3. Kết quả trong `r1/`: `last.md` (báo cáo), `events.jsonl`, `thread_id`, `git_status.txt`, `git_diff.txt`.
4. Claude kiểm tra: mở lại từng trích dẫn (file/trang/ảnh), chạy script kiểm, xem diff.
5. Chưa đạt → `task_fix.md` nêu đúng chỗ sai, giao lại **cùng phiên**:
   ```bash
   tools/codex_run.sh codex-runs/<ID>/fix1.md ../A313-V_codex codex-runs/<ID>/r2 "$(cat codex-runs/<ID>/r1/thread_id)"
   ```
6. Đạt → Claude ghi checkpoint `PROJECT_HANDOFF.md`, commit trên nhánh của Codex, sang nhiệm vụ sau.

## 3. Giới hạn an toàn

- Tối đa **2 lượt sửa** mỗi nhiệm vụ; quá thì dừng, báo người dùng.
- `exit≠0` (124 = hết giờ, lỗi đăng nhập, hết usage) → không giao lại tự động; ghi handoff, báo người dùng.
- Không merge vào `main`, không force push, không reset/xoá. Push chỉ khi người dùng xác nhận.
- Kết luận kỹ thuật chỉ nhận khi có căn cứ (bản vẽ, số chân, đường nối, kết quả script);
  ô Codex ghi "chưa xác minh" giữ nguyên, Claude không lấp.

## 4. Worktree

```bash
git worktree add -b codex/<việc> ../A313-V_codex main   # tạo
git worktree list                                       # xem
```

## 5. Cổng phê duyệt (người dùng yêu cầu 2026-10-22)

Sau MỖI nhiệm vụ Codex: Claude thu kết quả → đọc file/diff → chạy lại kiểm tra → lưu thread_id/nhánh/commit →
cập nhật handoff → commit checkpoint → soạn đề xuất nhiệm vụ kế → **DỪNG**. Không tự giao nhiệm vụ mới, không tự
giao lượt sửa khi chưa được người dùng đồng ý. Không dừng/restart Codex đang chạy.
Báo cáo theo mẫu: Task ID · Trạng thái PASS/PARTIAL/FAIL · Đã hoàn thành · File thay đổi · Kết quả kiểm tra ·
Chưa hoàn thành · Git checkpoint · Codex session ID/resume · Nhiệm vụ đề xuất tiếp theo.

## 6. Bài học

- T03 (рис.8, 2 tờ, 947 chân) vượt `CODEX_TIMEOUT=3600` → exit 124, file vẫn còn nhưng không có `last.md`.
  Tấm số lớn: đặt `CODEX_TIMEOUT=7200` hoặc chia nhiệm vụ theo tờ; muốn tiếp phiên thì `resume` cùng thread_id.

- T04 (2026-10-22): Codex **từ chối** chép/tái dựng netlist A-313-3 vì là thiết bị avionics quân sự; nó tự hoàn nguyên thay đổi. Không viết lại prompt để lách. Chỉ giao Codex việc kiểm kê tài liệu, kiểm định dạng CSV.
- Đề bài phải cấp đủ quyền sửa cho mọi lệnh kiểm nó yêu cầu chạy (T04 lượt 1 bị chặn vì `e3_vs_e4.py` chưa hỗ trợ У3).
