# Novel Studio Hooks System

## 📚 개요

Hooks 시스템은 Novel Studio의 자동화 파이프라인을 구성하는 핵심 컴포넌트입니다.
각 작업 단계에서 자동으로 실행되어 품질 관리, 일관성 검증, 상태 추적을 수행합니다.

---

## 🔗 Hook 유형

### 1. sessionStart.sh
**실행 시점**: 세션 시작 시
**목적**: 이전 컨텍스트 로드 및 재개 지원

**동작**:
- 프로젝트 상태 로드 (.novel-studio/status.json)
- 이전 세션 요약 표시 (session_summary.md)
- 다음 작업 제안
- 환경 변수 설정

**사용 예시**:
```bash
./hooks/sessionStart.sh /path/to/project
```

---

### 2. preToolUse.sh
**실행 시점**: 파일 수정 전
**목적**: 일관성 검증 및 충돌 방지

**동작**:
- 캐릭터/설정 파일 수정 감지
- 일관성 체크 스크립트 실행 (check_consistency.py)
- 경고 메시지 출력

**사용 예시**:
```bash
./hooks/preToolUse.sh /path/to/project character_profiles.md edit
```

---

### 3. postToolUse.sh
**실행 시점**: 작업 완료 후
**목적**: 자동 검증 및 백업

**동작**:
- 맞춤법 검사 (spell_check.py)
- 가독성 분석 (readability.py)
- 자동 백업 (.novel-studio/backups/)
- 상태 업데이트 (update_status.py)

**사용 예시**:
```bash
./hooks/postToolUse.sh /path/to/project chapter_01.md write
```

---

### 4. errorOccurred.sh
**실행 시점**: 오류 발생 시
**목적**: 오류 로깅 및 복구 안내

**동작**:
- 오류 로그 저장 (.novel-studio/errors.log)
- 오류 타입별 처리 안내
- 복구 방법 제시

**사용 예시**:
```bash
./hooks/errorOccurred.sh /path/to/project quality_failure "Chapter 2: 65/100"
```

**오류 타입**:
- `quality_failure`: 품질 기준 미달
- `consistency_conflict`: 설정 충돌
- `rate_limit`: API 제한

---

## 🛠️ 지원 스크립트

### scripts/check_consistency.py
캐릭터/설정 일관성 자동 검증

**기능**:
- 캐릭터 프로필 로드
- 이름, 나이 일관성 체크
- 불일치 항목 보고

**사용**:
```bash
python3 scripts/check_consistency.py /path/to/project target_file.md
```

---

### scripts/spell_check.py
맞춤법 자동 검사 (규칙 기반)

**기능**:
- 자주 틀리는 맞춤법 패턴 탐지
- 라인 번호와 수정안 제시

**체크 패턴**:
- 되요 → 돼요
- 됬 → 됐
- 않되 → 안 돼
- 할수있 → 할 수 있

**사용**:
```bash
python3 scripts/spell_check.py chapter_01.md
```

---

### scripts/readability.py
가독성 분석

**기능**:
- 글자 수, 문장 수, 평균 문장 길이 계산
- 표현 반복 탐지 (5회 이상)

**사용**:
```bash
python3 scripts/readability.py chapter_01.md
```

**출력 예시**:
```
📊 가독성 분석: chapter_01.md
   총 글자 수: 3,850
   문장 수: 127
   평균 문장 길이: 12.3단어

⚠️  반복 표현 (3개):
   '떨렸다': 8회
   '보았다': 6회
   '느꼈다': 6회
```

---

### scripts/update_status.py
프로젝트 상태 자동 업데이트

**기능**:
- 진행률 자동 계산
- Phase 전환 감지
- 작업 이력 기록 (.novel-studio/status.json)

**사용**:
```bash
python3 scripts/update_status.py /path/to/project write chapter_01.md
```

**상태 파일 구조**:
```json
{
  "project_id": "first_love_001",
  "phase": "phase2",
  "progress": 45,
  "last_updated": "2026-02-14T12:00:00",
  "completed_tasks": [
    {
      "operation": "write",
      "file": "chapter_01.md",
      "timestamp": "2026-02-14T12:00:00"
    }
  ]
}
```

---

## 🔧 설치 및 설정

### 1. 실행 권한 부여
```bash
chmod +x hooks/*.sh
chmod +x scripts/*.py
```

### 2. Python 의존성
```bash
# 기본 Python 3만 필요 (추가 패키지 불필요)
python3 --version  # 3.8 이상 권장
```

### 3. 프로젝트 구조
```
project/
├── .novel-studio/
│   ├── status.json         # 프로젝트 상태
│   ├── backups/            # 자동 백업
│   └── errors.log          # 오류 로그
├── phase1_planning/
├── phase2_chapters/
└── session_summary.md      # 세션 요약
```

---

## 🧪 테스트

### 1. sessionStart 테스트
```bash
# 테스트 프로젝트 생성
mkdir -p test_project/.novel-studio
echo '{"project_id":"test","phase":"phase1"}' > test_project/.novel-studio/status.json

# Hook 실행
./hooks/sessionStart.sh test_project
```

**예상 출력**:
```
🚀 Novel Studio Session Starting...
📂 Project: test_project
📊 프로젝트 상태:
  "project_id": "test"
  "phase": "phase1"
✅ 세션 준비 완료
```

### 2. 일관성 체크 테스트
```bash
# first_love_001로 테스트
python3 scripts/check_consistency.py projects/first_love_001 \
  projects/first_love_001/phase2_chapters/chapter_01.md
```

### 3. 통합 테스트
```bash
# 전체 워크플로우
./hooks/sessionStart.sh projects/first_love_001
./hooks/preToolUse.sh projects/first_love_001 character_profiles.md edit
./hooks/postToolUse.sh projects/first_love_001 chapter_01.md write
```

---

## 📈 효과 측정

### Before (베타 수동)
- 20회 수동 개입
- 일관성 체크: 수동
- 맞춤법 검사: 수동
- 백업: 수동

### After (v1.0 Hooks)
- 5-7회 개입
- 일관성 체크: **자동** ✅
- 맞춤법 검사: **자동** ✅
- 백업: **자동** ✅
- 상태 추적: **자동** ✅

**개선**: 70% 작업 자동화 🚀

---

## 🔜 향후 개선

### Phase 2
- [ ] 고급 맞춤법 검사 (AI 기반)
- [ ] 플롯 홀 자동 탐지
- [ ] 감정 곡선 시각화

### Phase 3
- [ ] 실시간 모니터링 대시보드
- [ ] Slack/Discord 알림 통합
- [ ] 버전 비교 및 롤백

---

**작성자**: Novel Studio Development Team
**최종 업데이트**: 2026-02-14
**버전**: 1.0
