#!/usr/bin/env python3
"""
spell_check.py
맞춤법 자동 검사 (기본 규칙 기반)
"""

import sys
import re
from pathlib import Path

# 자주 틀리는 맞춤법 패턴
COMMON_ERRORS = {
    r'되요\b': '돼요',
    r'됬': '됐',
    r'않되': '안 돼',
    r'만나뵙게되어': '만나 뵙게 되어',
    r'할수있': '할 수 있',
    r'못했읍니다': '못했습니다',
}

def check_spelling(content):
    """맞춤법 체크"""
    issues = []
    
    for pattern, correction in COMMON_ERRORS.items():
        matches = list(re.finditer(pattern, content))
        for match in matches:
            # 라인 번호 찾기
            line_num = content[:match.start()].count('\n') + 1
            issues.append({
                'line': line_num,
                'error': match.group(),
                'correction': correction
            })
    
    return issues

def main():
    if len(sys.argv) < 2:
        print("Usage: spell_check.py <file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"❌ 파일 없음: {file_path}")
        sys.exit(1)
    
    print(f"📝 맞춤법 검사: {file_path.name}")
    
    content = file_path.read_text(encoding='utf-8')
    issues = check_spelling(content)
    
    if issues:
        print(f"⚠️  {len(issues)}개 맞춤법 오류 발견")
        for issue in issues[:5]:  # 최대 5개만 출력
            print(f"   라인 {issue['line']}: '{issue['error']}' → '{issue['correction']}'")
        
        if len(issues) > 5:
            print(f"   ... 외 {len(issues)-5}개")
    else:
        print("✅ 맞춤법 오류 없음")

if __name__ == "__main__":
    main()
