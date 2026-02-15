#!/bin/bash
# hooks/sessionStart.sh
# 세션 시작 시 자동 실행되는 Hook

set -e

PROJECT_DIR="${1:-$(pwd)}"
SUMMARY_FILE="$PROJECT_DIR/session_summary.md"
STATUS_FILE="$PROJECT_DIR/.novel-studio/status.json"

echo "🚀 Novel Studio Session Starting..."
echo "📂 Project: $PROJECT_DIR"
echo ""

# 프로젝트 상태 확인
if [ -f "$STATUS_FILE" ]; then
    echo "📊 프로젝트 상태:"
    cat "$STATUS_FILE" | grep -E '"(project_id|status|phase)"' | sed 's/[",]//g'
    echo ""
fi

# 이전 세션 요약 로드
if [ -f "$SUMMARY_FILE" ]; then
    echo "📖 이전 세션 요약:"
    cat "$SUMMARY_FILE"
    echo ""
fi

export NOVEL_STUDIO_PROJECT_DIR="$PROJECT_DIR"
echo "✅ 세션 준비 완료"
