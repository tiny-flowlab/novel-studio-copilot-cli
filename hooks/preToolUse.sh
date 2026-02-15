#!/bin/bash
# hooks/preToolUse.sh
# 파일 수정 전 일관성 체크

set -e

PROJECT_DIR="${1:-$(pwd)}"
TARGET_FILE="$2"
OPERATION="$3"

echo "🔍 Pre-Tool Check: $OPERATION on $TARGET_FILE"

# 캐릭터/설정 파일 수정 시 일관성 체크
if [[ "$TARGET_FILE" == *"character"* ]] || [[ "$TARGET_FILE" == *"setting"* ]]; then
    echo "⚠️  중요 파일 수정 감지"
    
    # 일관성 체크 스크립트 실행
    if [ -f "scripts/check_consistency.py" ]; then
        echo "   → 일관성 검증 중..."
        python3 scripts/check_consistency.py "$PROJECT_DIR" "$TARGET_FILE"
    fi
fi

echo "✅ Pre-Tool Check 완료"
