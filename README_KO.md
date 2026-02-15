# 📚 Novel Studio for Copilot CLI - 멀티 에이전트 소설 창작 시스템

> **Copilot CLI가 코딩 도구일 뿐이라고?** 다시 생각해 보세요.  
> **GitHub Copilot CLI는 최고의 소설 창작 스튜디오입니다.**  
> 이 저장소를 클론하고, Copilot을 열고, *"소설 써줘"* 라고 말하세요 — 그게 끝입니다.

**[English README](README.md)**

---

## 🎯 개요

Novel Studio for Copilot CLI는 **13개의 전문 AI 에이전트**가 협업하여 출판급 소설을 자동으로 창작하는 시스템입니다. **GitHub Copilot CLI** 위에서 네이티브로 동작합니다.

`"소설 써줘"` 한마디면 기획, 집필, 편집, 품질 관리까지 에이전트 팀이 모든 것을 처리합니다.

### 💡 왜 Copilot CLI인가?

다른 CLI 도구는 코드 생성과 터미널 명령에 한정됩니다. **GitHub Copilot CLI는 코딩을 넘어** 소설 창작 같은 창의적 워크플로우를 가능하게 하는 완전한 에이전트 오케스트레이션 플랫폼입니다:

- **Agent Mode** — 단순 Q&A가 아닌 자율적 멀티스텝 실행
- **`AGENTS.md` 자동 로드** — 프로젝트를 여는 순간 시스템이 활성화
- **`@agent` 호출** — 13개 전문가가 `@name` 참조로 협업
- **Hooks 라이프사이클** — 모든 파일 작업에 자동 품질 체크 실행
- **모델 선택** — Copilot 설정에서 AI 모델(GPT-4o, Claude, Gemini 등)을 직접 선택하여 속도, 품질, 비용을 조절
- **VS Code Copilot Chat 통합** — 동일한 `@agent` 호출과 채팅 기반 워크플로우가 VS Code의 GitHub Copilot Chat 패널에서도 그대로 동작

### 특징

- ✅ **완전 자동화**: "소설 써줘" 한마디면 시작
- ✅ **전문 팀 구성**: 13개 전문 에이전트 (기획 6개 + 집필 4개 + 품질 3개)
- ✅ **장면별 전문화**: 대화/액션/감정 장면마다 전문 작가 배정
- ✅ **검증된 품질**: 91/100점 출판급 소설 생성 (실제 프로젝트)
- ✅ **Human-in-the-Loop**: 중요 시점에만 개입 (5-7회)
- ✅ **자동 품질 관리**: 일관성 체크, 맞춤법 검사, 백업
- ✅ **모델 유연성**: Copilot에서 제공하는 모든 AI 모델 선택 가능 (GPT-4o, Claude, Gemini 등)
- ✅ **VS Code + CLI**: Copilot CLI 터미널과 VS Code Copilot Chat 모두에서 동작 — 동일한 에이전트, 동일한 워크플로우

---

## ⚙️ Copilot CLI 연동 메커니즘

이 프로젝트는 **Copilot CLI 네이티브** 멀티 에이전트 시스템입니다.

### 1. `AGENTS.md` — 자동 로드 진입점

Copilot CLI가 프로젝트 루트의 `AGENTS.md`를 **custom_instruction**으로 자동 읽어들입니다. 이 파일이 **영업 담당** 에이전트 역할을 하여, 사용자를 맞이하고 요구사항을 수집하여 전문 에이전트에게 라우팅합니다.

### 2. `.github/agents/*.agent.md` — 전문 에이전트 프로필

13개 에이전트가 각각 `.agent.md` 파일로 정의되어 있습니다. Copilot CLI가 이 디렉토리를 인식하여 `@에이전트명` 구문으로 호출할 수 있습니다:

```
@main-writer    → .github/agents/main-writer.agent.md
@story-writer   → .github/agents/story-writer.agent.md
...
```

### 3. Hooks — 라이프사이클 자동화

| Hook | 실행 시점 | 기능 |
|------|----------|------|
| `sessionStart.sh` | 세션 시작 | 이전 컨텍스트 로드 |
| `preToolUse.sh` | 파일 수정 전 | 일관성 체크 |
| `postToolUse.sh` | 파일 저장 후 | 맞춤법/가독성/백업 |
| `errorOccurred.sh` | 오류 발생 | 로깅 및 알림 |

### 4. 활용한 Copilot CLI 기능

| 기능 | 활용 방식 |
|------|----------|
| `AGENTS.md` 자동 로드 | 진입점 에이전트 자동 활성화 |
| `.github/agents/` 디렉토리 | 13개 전문 에이전트 `@name`으로 호출 |
| `@agent` 호출 | 에이전트 간 위임 체인 |
| Hooks (`hooks/`) | Pre/Post 자동화, 세션 초기화 |
| Agent Mode | 파일 생성, 스크립트 실행, 멀티스텝 작업 |
| Tool use (bash/python) | 품질 스크립트 자동 실행 |

---

## 📋 사전 요구사항

### 필수 사항
1. **GitHub Copilot CLI** — [설치 가이드](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
   ```bash
   gh extension install github/gh-copilot
   ```

### 선택 사항 (자동 품질 관리용)
- **Python 3.8+**: 맞춤법 검사 및 일관성 분석 스크립트 실행용
- **Bash**: `hooks/` 시스템을 통한 자동화 기능을 사용하려는 경우 필수
- **Git**: 생성된 소설의 버전 관리를 원하는 경우

---

## 🚀 Quick Start

### Step 1: 클론 및 이동

```bash
git clone https://github.com/tiny-flowlab/copilot-novel-agent-team.git
cd copilot-novel-agent-team
```

### Step 2: Copilot CLI 실행

VS Code에서 GitHub Copilot과 함께 프로젝트를 열거나 CLI 사용:

```bash
gh copilot
```

> 💡 이 디렉토리에서 Copilot CLI가 시작되면 `AGENTS.md`가 자동 로드되어 에이전트 시스템이 활성화됩니다.

### Step 3: 소설 요청

```
"대학생 로맨스 소설 써줘"
```

### Step 4: 안내에 따라 진행

```
Novel Studio for Copilot CLI (영업 담당):
  안녕하세요! 몇 가지 확인하겠습니다...

  1️⃣ 프로젝트명은?      → 예: "first_love"
  2️⃣ 작업 모드는?        → auto / review (추천) / manual

사용자: "first_love, review"

Novel Studio:
  ✅ 접수 완료! @main-writer에게 전달합니다...

  📋 Phase 1: 기획
    ✓ @story-writer: 플롯 구성 완료
    ✓ @character-writer: 캐릭터 설계 완료
    ✓ @setting-writer: 배경 설정 완료
    ✓ @genre-specialist: 장르 분석 완료

  🔔 Phase 1 승인이 필요합니다. [A]승인 / [R]수정 / [M]변경?

사용자: A

Novel Studio:
  ✍️ Phase 2: Chapter 1 집필 중...
    → @dialogue-writer 대화 장면 처리
    → @emotion-writer 감정 장면 처리
    → @prose-writer 서술 처리
    ...
```

### Step 5: 결과물 확인

```
projects/first_love/
├── phase1_planning/       ← 플롯, 캐릭터, 배경 문서
├── phase2_chapters/       ← 챕터 초고 & 완성본
├── phase3_final/          ← 통합 원고 + 편집 리포트
└── .novel-studio/                ← 상태 추적 & 백업
```

---

## 🏗️ 시스템 구성

### 에이전트 팀 (13개)

| 단계 | 에이전트 | 역할 | 품질 기준 |
|------|---------|------|----------|
| **기획** | Main Writer | 프로젝트 총괄 & 품질 관리 | 85/100 |
| | Story Writer | 플롯 구성, 서사 전개 | 75/100 |
| | Character Writer | 인물 창조, 관계도 | 75/100 |
| | Setting Writer | 세계관, 배경 설정 | 75/100 |
| | Genre Specialist | 장르 분석, 트로프 전략 | 75/100 |
| | Pacing Manager | 템포 조절, 리듬 관리 | — |
| **집필** | Dialogue Writer | 대화 장면 전문 | 75/100 |
| | Action Writer | 액션/전투 장면 전문 | 75/100 |
| | Emotion Writer | 감정/내면 묘사 전문 | 75/100 |
| | Prose Writer | 일반 문장 작성 | 75/100 |
| **품질** | Editorial Team | 교정, 교열, 일관성 | — |
| | Feedback Agent | 독자 관점 평가 | — |
| | Research Agent | 고증, 사실 확인 | — |

---

## 📋 워크플로우

### Phase 1: 기획

```
사용자 요청 → @main-writer 분석
    ↓
병렬 실행 (4개 에이전트):
  ├─ @story-writer      → 플롯 구성
  ├─ @character-writer   → 캐릭터 설계
  ├─ @setting-writer     → 배경 설정
  └─ @genre-specialist   → 장르 분석 & 트로프
    ↓
@pacing-manager → 전체 템포 설계
    ↓
@main-writer → 통합 및 조율
    ↓
체크포인트 → 사용자 승인
```

### Phase 2: 집필 (챕터별 반복)

```
@story-writer → 상세 개요
    ↓
장면 유형별 전문 작가 배정:
  ├─ @dialogue-writer → 대화 장면
  ├─ @action-writer   → 액션 장면
  ├─ @emotion-writer   → 감정 장면
  └─ @prose-writer     → 일반 서술
    ↓
@main-writer → 장면 통합
    ↓
@pacing-manager → 템포 검증
    ↓
@editorial-team → 교정 및 피드백
    ↓
체크포인트 → 사용자 승인 (Review 모드)
```

### Phase 3: 완성

```
@main-writer → 전체 원고 통합
    ↓
@editorial-team → 최종 교정
    ↓
@feedback-agent → 독자 평가 (5가지 관점)
    ↓
최종 승인 → 출판 준비 완료
```

---

## 🎛️ 작업 모드

| 모드 | 개입 횟수 | 체크포인트 | 추천 대상 |
|------|----------|-----------|----------|
| ⭐ **Review** (추천) | 5-7회 | Phase 1, 각 챕터, 최종 | 대부분의 사용자 |
| 🚀 **Auto** | 3회 | 시작, Phase 1, 최종 | 빠른 프로토타입 |
| 🎨 **Manual** | 15-20회 | 모든 단계 | 세밀한 통제 |

---

## 💡 사용 예시

**기본:**
```
"대학 캠퍼스 로맨스 소설 써줘"
```

**상세:**
```
프로젝트명: campus_love
아이디어: 공대생과 인문대생의 첫사랑. 벚꽃 계절 배경.
모드: review
분량: 3챕터
```

**이어쓰기:**
```
"first_love 프로젝트 이어서 써줘"
```

**재작성:**
```
"first_love의 Chapter 2를 다시 써줘. editorial_notes.md의 피드백을 반영해서."
```

**특정 에이전트 호출:**
```
@prose-writer phase2_chapters/chapter_02/outline.md를 읽고 본문을 작성해줘.
```

---

## 📊 실전 검증 결과

### first_love_001 프로젝트

| 항목 | 결과 |
|------|------|
| 분량 | 11,900자 / 3챕터 (한국어 산문) |
| 품질 점수 | **91/100** (출판급) |
| 소요 시간 | 4시간 |
| 특징 | 벚꽃→신록→여름 계절 변화로 감정선 표현 |

**다관점 평가:**

| 평가자 | 점수 |
|--------|------|
| 장르 전문가 | 85/100 |
| 일반 독자 | 80/100 |
| 편집자 | 90/100 |
| 작법 전문가 | 82/100 |
| 타겟 독자 | 88/100 |

---

## 📈 성과 비교: v1.0으로의 진화

| 항목 | 베타 (수동) | v1.0 (현재) | 개선 |
|------|------------|------------|------|
| 에이전트 수 | 8개 | 13개 | +5개 |
| 개입 횟수 | 20회 | 5-7회 | **-70%** |
| 자동화 | 0% | 70% | **+70%** |
| 소요 시간 | 4시간 | 3시간 | **-25%** |
| 장면 전문화 | ❌ | ✅ | 신규 |
| 장르 분석 | ❌ | ✅ | 신규 |
| 자동 일관성 체크 | ❌ | ✅ | 신규 |
| 자동 맞춤법 검사 | ❌ | ✅ | 신규 |
| 자동 백업 | ❌ | ✅ | 신규 |

---

## 📄 라이센스

[MIT License](LICENSE)

---

## 👥 제작

**Novel Studio for Copilot CLI — by [tiny_flowlab](https://github.com/tiny-flowlab)**

- 버전: 1.0
- 상태: Production Ready ✅

---

**Novel Studio for Copilot CLI**  
*"당신의 이야기를, 우리가 완성합니다."*
