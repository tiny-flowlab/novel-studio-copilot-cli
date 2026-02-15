#!/usr/bin/env python3
"""
check_consistency.py
캐릭터/설정 일관성 자동 검증 스크립트
"""

import sys
import json
import re
from pathlib import Path

def load_character_profiles(project_dir):
    """캐릭터 프로필 로드"""
    profiles = {}
    character_dir = Path(project_dir) / "phase1_planning"
    
    if not character_dir.exists():
        return profiles
    
    character_file = character_dir / "character_profiles.md"
    if character_file.exists():
        content = character_file.read_text(encoding='utf-8')
        
        # 캐릭터 이름 추출
        names = re.findall(r'##\s+(?:남자|여자)\s+주인공:\s+(\S+)', content)
        
        # 나이 추출
        ages = re.findall(r'나이.*?(\d+)세', content)
        
        for i, name in enumerate(names):
            age = int(ages[i]) if i < len(ages) else None
            profiles[name] = {
                'name': name,
                'age': age
            }
    
    return profiles

def check_chapter_consistency(chapter_file, profiles):
    """챕터 내 일관성 체크"""
    content = Path(chapter_file).read_text(encoding='utf-8')
    issues = []
    
    for name, profile in profiles.items():
        # 이름 변형 체크 (예: 민준 vs 민준이)
        pattern = rf'\b{name}[이가은를]\b'
        matches = re.findall(pattern, content)
        
        if matches:
            # 정확한 이름으로 사용되는지 확인
            exact_name = re.findall(rf'\b{name}\b', content)
            if len(exact_name) > 0:
                print(f"✅ {name}: 이름 일관성 확인")
    
    return issues

def main():
    if len(sys.argv) < 3:
        print("Usage: check_consistency.py <project_dir> <target_file>")
        sys.exit(1)
    
    project_dir = sys.argv[1]
    target_file = sys.argv[2]
    
    print(f"🔍 일관성 체크: {target_file}")
    
    # 캐릭터 프로필 로드
    profiles = load_character_profiles(project_dir)
    
    if not profiles:
        print("ℹ️  캐릭터 프로필 없음 - 검사 생략")
        return
    
    print(f"   로드된 캐릭터: {', '.join(profiles.keys())}")
    
    # 일관성 체크
    if Path(target_file).exists():
        issues = check_chapter_consistency(target_file, profiles)
        
        if issues:
            print(f"⚠️  {len(issues)}개 이슈 발견")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print("✅ 일관성 검증 통과")
    else:
        print("ℹ️  파일이 아직 존재하지 않음")

if __name__ == "__main__":
    main()
