#!/bin/bash
# hooks/errorOccurred.sh
# 오류 발생 시 처리

set -e

PROJECT_DIR="${1:-$(pwd)}"
ERROR_TYPE="$2"
ERROR_MSG="$3"

echo "❌ Error Occurred: $ERROR_TYPE"
echo "   Message: $ERROR_MSG"

# 에러 로그 저장
ERROR_LOG="$PROJECT_DIR/.novel-studio/errors.log"
mkdir -p "$(dirname $ERROR_LOG)"
echo "[$(date)] $ERROR_TYPE: $ERROR_MSG" >> "$ERROR_LOG"

# 에러 타입별 처리
case "$ERROR_TYPE" in
    "quality_failure")
        echo "⚠️  품질 기준 미달"
        echo "   → 재작성 필요"
        ;;
    "consistency_conflict")
        echo "⚠️  설정 충돌 감지"
        echo "   → 수동 해결 필요"
        ;;
    "rate_limit")
        echo "⚠️  API 제한"
        echo "   → 잠시 후 재시도"
        ;;
    *)
        echo "⚠️  알 수 없는 오류"
        ;;
esac

echo "📋 에러 로그: $ERROR_LOG"
