#!/bin/bash
# hooks/postToolUse.sh
# 작업 완료 후 자동 처리

set -e

PROJECT_DIR="${1:-$(pwd)}"
COMPLETED_FILE="$2"
OPERATION="$3"

echo "✨ Post-Tool Processing: $COMPLETED_FILE"

# 챕터 작성 완료 시
if [[ "$COMPLETED_FILE" == *"chapter"*.md ]]; then
    echo "📝 챕터 작성 완료 감지"
    
    # 1. 맞춤법 검사
    if [ -f "scripts/spell_check.py" ]; then
        echo "   → 맞춤법 검사중..."
        python3 scripts/spell_check.py "$COMPLETED_FILE"
    fi
    
    # 2. 가독성 분석
    if [ -f "scripts/readability.py" ]; then
        echo "   → 가독성 분석중..."
        python3 scripts/readability.py "$COMPLETED_FILE"
    fi
    
    # 3. 백업
    BACKUP_DIR="$PROJECT_DIR/.novel-studio/backups"
    mkdir -p "$BACKUP_DIR"
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    cp "$COMPLETED_FILE" "$BACKUP_DIR/$(basename $COMPLETED_FILE .md)_$TIMESTAMP.md"
    echo "   → 백업 완료: $BACKUP_DIR"
fi

# 4. 상태 업데이트
if [ -f "scripts/update_status.py" ]; then
    python3 scripts/update_status.py "$PROJECT_DIR" "$OPERATION" "$COMPLETED_FILE"
fi

echo "✅ Post-Tool Processing 완료"
