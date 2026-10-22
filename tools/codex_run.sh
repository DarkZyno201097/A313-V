#!/usr/bin/env bash
# Giao một nhiệm vụ cho Codex CLI và gom kết quả để Claude kiểm tra.
# Dùng:  tools/codex_run.sh TASK.md WORKDIR OUTDIR [SESSION_ID]
#   TASK.md   đề bài (đọc qua stdin)
#   WORKDIR   thư mục repo (thường là "."); không sửa file song song khi Codex đang chạy
#   OUTDIR    nơi ghi events.jsonl, last.md (báo cáo), thread_id, git_status.txt, git_diff.txt
#   SESSION_ID có thì `codex exec resume` phiên cũ (giữ ngữ cảnh), không có thì mở phiên mới
# Biến môi trường: CODEX_SANDBOX (mặc định read-only), CODEX_TIMEOUT giây (mặc định 1800).
# Dùng đăng nhập ChatGPT sẵn có của Codex; không đặt OPENAI_API_KEY.
set -euo pipefail
task=$(realpath "$1"); wd=$2; out=$(mkdir -p "$3" && realpath "$3"); sid=${4:-}
sandbox=${CODEX_SANDBOX:-read-only}
cd "$wd"
args=(--json -o "$out/last.md" -c "sandbox_mode=\"$sandbox\"")
set +e
if [ -z "$sid" ]; then
  timeout "${CODEX_TIMEOUT:-1800}" codex exec "${args[@]}" - <"$task" >"$out/events.jsonl" 2>"$out/stderr.txt"
else
  timeout "${CODEX_TIMEOUT:-1800}" codex exec resume "$sid" "${args[@]}" - <"$task" >"$out/events.jsonl" 2>"$out/stderr.txt"
fi
rc=$?
set -e
grep -o '"thread_id":"[^"]*"' "$out/events.jsonl" | head -1 | cut -d'"' -f4 >"$out/thread_id" || true
git status --short >"$out/git_status.txt"
git diff >"$out/git_diff.txt"
echo "exit=$rc thread=$(cat "$out/thread_id") report=$out/last.md changed=$(wc -l <"$out/git_status.txt")"
# 124 = hết giờ; khác 0 = lỗi/hết usage -> Claude dừng an toàn, ghi handoff, không giao lại tự động.
exit $rc
