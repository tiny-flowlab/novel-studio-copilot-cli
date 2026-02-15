#!/usr/bin/env python3
"""
update_status.py
프로젝트 상태 업데이트 스크립트
"""

import sys
import json
from pathlib import Path
from datetime import datetime

def update_status(project_dir, operation, completed_file):
    """상태 업데이트"""
    status_file = Path(project_dir) / ".novel-studio" / "status.json"
    status_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 기존 상태 로드
    if status_file.exists():
        status = json.loads(status_file.read_text())
    else:
        status = {
            'project_id': Path(project_dir).name,
            'created_at': datetime.now().isoformat(),
            'phase': 'init',
            'progress': 0,
            'completed_tasks': []
        }
    
    # 상태 업데이트
    status['last_updated'] = datetime.now().isoformat()
    status['last_operation'] = operation
    status['last_file'] = completed_file
    
    # 진행률 계산 (간단한 버전)
    if 'character_profiles' in completed_file:
        status['phase'] = 'phase1'
        status['progress'] = 30
    elif 'chapter' in completed_file:
        status['phase'] = 'phase2'
        # 챕터 번호 추출
        import re
        match = re.search(r'chapter_?(\d+)', completed_file)
        if match:
            chapter_num = int(match.group(1))
            status['progress'] = 30 + (chapter_num * 15)  # 각 챕터 15%
    elif 'final' in completed_file:
        status['phase'] = 'phase3'
        status['progress'] = 90
    
    status['completed_tasks'].append({
        'operation': operation,
        'file': completed_file,
        'timestamp': datetime.now().isoformat()
    })
    
    # 저장
    status_file.write_text(json.dumps(status, indent=2, ensure_ascii=False))
    
    print(f"📊 상태 업데이트: {status['phase']} ({status['progress']}%)")

def main():
    if len(sys.argv) < 4:
        print("Usage: update_status.py <project_dir> <operation> <file>")
        sys.exit(1)
    
    project_dir = sys.argv[1]
    operation = sys.argv[2]
    completed_file = sys.argv[3]
    
    update_status(project_dir, operation, completed_file)

if __name__ == "__main__":
    main()
