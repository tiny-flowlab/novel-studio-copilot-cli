# 📖 Novel Studio v1.0 - Workflow Guide

**Multi-Agent Novel Creation System - Copilot CLI Native Workflow**

[🇺🇸 English](#english) | [🇰🇷 한국어](#korean)

---

<a name="english"></a>
## 🇺🇸 English Version

This document defines the novel creation workflow that GitHub Copilot CLI reads and executes directly.

---

### 🎯 Overview

#### Purpose
Copilot CLI automatically creates novels by sequentially calling 13 specialized agents.

#### How to Execute
```
@copilot Read WORKFLOW_GUIDE.md, 
and write a novel about "[idea]" as project "[project_name]" in [mode] mode.

Example:
@copilot Read WORKFLOW_GUIDE.md,
and write a novel about "college students' first love" as project "first_love" in review mode.
```

---

### 🏗️ Project Structure

When starting the workflow, create the following directory structure:

```
projects/<project_name>/
├── phase1_planning/
│   ├── story_structure.md
│   ├── character_profiles.md
│   ├── setting_world.md
│   ├── genre_analysis.md
│   ├── pacing_plan.md
│   └── final_plan.md
├── phase2_chapters/
│   ├── chapter_01/
│   │   ├── outline.md
│   │   ├── draft.md
│   │   └── final.md
│   ├── chapter_02/
│   └── chapter_03/
├── phase3_final/
│   ├── final_novel.md
│   ├── editorial_report.md
│   └── feedback_report.md
└── .novel-studio/
    ├── status.json
    ├── checkpoints/
    └── backups/
```

---

### 🎬 Phase 1: Planning

#### Goal
Complete the basic design of the novel.

#### Step 1.1: Analyze User Request (Main Writer)

**Agent**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**Input**: User's novel idea  
**Task**:
```
Analyze the user request to determine:
1. Genre (Romance, Fantasy, SF, etc.)
2. Target audience
3. Expected length (default: 3 chapters)
4. Core message
5. Concept summary

Save the result to projects/<project_name>/phase1_planning/concept.md
```

**Output**: `concept.md`

---

#### Step 1.2: Parallel Planning (4 agents running simultaneously)

##### 1.2.1 Plot Structure (Story Writer)

**Agent**: `@story-writer` ([English](/.github/agents/story-writer.agent.md#english) | [한국어](/.github/agents/story-writer.agent.md#korean))  
**Input**: `concept.md`  
**Task**:
```
Read concept.md and construct the plot:

1. Three-act structure design
   - Act 1: Setup (Chapter 1)
   - Act 2: Development/Climax (Chapter 2)
   - Act 3: Resolution (Chapter 3)

2. Chapter-by-chapter outline
   - Key events
   - Emotional curve (%)
   - Expected length (3000-4000 characters)

3. Foreshadowing and twist design

Save the result to projects/<project_name>/phase1_planning/story_structure.md

Quality standard: 75/100 or higher
```

**Output**: `story_structure.md`

---

##### 1.2.2 Character Design (Character Writer)

**Agent**: `@character-writer` ([English](/.github/agents/character-writer.agent.md#english) | [한국어](/.github/agents/character-writer.agent.md#korean))  
**Input**: `concept.md`  
**Task**:
```
Read concept.md and design the characters:

1. Main character profile
   - Name, age, appearance
   - Personality (including MBTI)
   - Backstory
   - Goals and motivations
   - Distinctive habits (e.g., "adjusting glasses")

2. Supporting character profiles (1-2 characters)

3. Character relationship map

4. Dialogue tone definition
   - Speech patterns
   - Formal/informal language rules

Save the result to projects/<project_name>/phase1_planning/character_profiles.md

Quality standard: 75/100 or higher
```

**Output**: `character_profiles.md`

---

##### 1.2.3 Setting Design (Setting Writer)

**Agent**: `@setting-writer` ([English](/.github/agents/setting-writer.agent.md#english) | [한국어](/.github/agents/setting-writer.agent.md#korean))  
**Input**: `concept.md`  
**Task**:
```
Read concept.md and design the setting:

1. Temporal and spatial background
   - Time: Year, season, time of day
   - Space: 3-5 major locations

2. Detailed description of each location
   - Using all five senses
   - Atmosphere
   - Symbolic meaning

3. World-building rules

Save the result to projects/<project_name>/phase1_planning/setting_world.md

Quality standard: 75/100 or higher
```

**Output**: `setting_world.md`

---

##### 1.2.4 Genre Analysis (Genre Specialist)

**Agent**: `@genre-specialist` ([English](/.github/agents/genre-specialist.agent.md#english) | [한국어](/.github/agents/genre-specialist.agent.md#korean))  
**Input**: `concept.md`  
**Task**:
```
Read concept.md and establish genre strategy:

1. Genre classification and subgenres
   - Main genre + supporting genre
   - Re-validate target audience

2. Genre-specific trope recommendations
   - 3-5 essential tropes
   - Clichés to avoid
   - Fresh variations to consider

3. Genre conventions
   - Expected elements
   - Ending direction
   - Style/tone recommendations

4. Genre-specific quality standards

Save the result to projects/<project_name>/phase1_planning/genre_analysis.md

Quality standard: 75/100 or higher
```

**Output**: `genre_analysis.md`

---

#### Step 1.3: Planning Integration (Main Writer)

**Agent**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**Input**: 
- `story_structure.md`
- `character_profiles.md`
- `setting_world.md`
- `genre_analysis.md`

**Task**:
```
Read all four planning documents and create an integrated plan:

1. Verify consistency
2. Resolve conflicts
3. Write final planning document

Save the result to projects/<project_name>/phase1_planning/final_plan.md
```

**Output**: `final_plan.md`

---

#### Step 1.4: Pacing Design (Pacing Manager)

**Agent**: `@pacing-manager` ([English](/.github/agents/pacing-manager.agent.md#english) | [한국어](/.github/agents/pacing-manager.agent.md#korean))  
**Input**: 
- `final_plan.md`
- `story_structure.md`

**Task**:
```
Read the integrated plan and design overall pacing:

1. Chapter-by-chapter tempo analysis
   - Tension curve (0-100%)
   - Scene length balance
   - Rest/tension rhythm

2. Emotional change curve
   - Emotional intensity per chapter
   - Climax timing

3. Information delivery speed
   - Foreshadowing placement timing
   - Revelation/twist positions

4. Improvement recommendations

Save the result to projects/<project_name>/phase1_planning/pacing_plan.md

Quality standard: 75/100 or higher
```

**Output**: `pacing_plan.md`

---

#### Step 1.5: Checkpoint - Phase 1 Approval

**Checkpoint ID**: `phase1_approval`

**Review Mode**:
```
🔔 Phase 1 Complete! Approval required.

Generated files:
- phase1_planning/story_structure.md
- phase1_planning/character_profiles.md
- phase1_planning/setting_world.md
- phase1_planning/genre_analysis.md
- phase1_planning/pacing_plan.md
- phase1_planning/final_plan.md

Choose:
[A]pprove / [R]eject / [M]odify
```

**Upon approval**: Proceed to Phase 2

---

### ✍️ Phase 2: Writing

#### Goal
Complete each chapter (default: 3 chapters).

#### Iteration: For each chapter (Chapter 1, 2, 3)

---

#### Step 2.1: Chapter Outline (Story Writer)

**Agent**: `@story-writer` ([English](/.github/agents/story-writer.agent.md#english) | [한국어](/.github/agents/story-writer.agent.md#korean))  
**Input**: 
- `phase1_planning/final_plan.md`
- Previous chapters (if any)

**Task**:
```
Read final_plan.md and create a detailed outline for Chapter X:

1. Scene composition (3-5 scenes)
2. Foreshadowing/setup
3. Climax design (for Act 2)

Save the result to projects/<project_name>/phase2_chapters/chapter_0X/outline.md
```

**Output**: `chapter_0X/outline.md`

---

#### Step 2.2: Write Content (Scene-Type-Specific Writers)

**Workflow**:
1. Analyze scene types in `outline.md`
2. Assign specialized writers for each scene type
3. Write each scene and integrate

---

##### 2.2.1 Dialogue-Focused Scenes (Dialogue Writer)

**Agent**: `@dialogue-writer` ([English](/.github/agents/dialogue-writer.agent.md#english) | [한국어](/.github/agents/dialogue-writer.agent.md#korean))  
**Condition**: When scene is dialogue-focused (character interactions, arguments, confessions, etc.)  
**Input**:
- `chapter_0X/outline.md`
- `phase1_planning/character_profiles.md`

**Task**:
```
Write dialogue-focused scenes:

1. Natural dialogue flow
   - Consistent speech patterns per character
   - Varied dialogue tags
   - Include non-verbal communication

2. Subtext
   - Unspoken emotions
   - Create tension

3. Balance dialogue and action (60:40)

Save the result to scene_XX_dialogue.md
```

---

##### 2.2.2 Action Scenes (Action Writer)

**Agent**: `@action-writer` ([English](/.github/agents/action-writer.agent.md#english) | [한국어](/.github/agents/action-writer.agent.md#korean))  
**Condition**: For action/combat/chase scenes  
**Input**:
- `chapter_0X/outline.md`
- `phase1_planning/setting_world.md`

**Task**:
```
Write action scenes:

1. Dynamic descriptions
   - Short, powerful sentences
   - Continuous action flow
   - Clear spatial awareness/distance

2. Use all five senses
   - Focus on sound, touch, sight
   - Maintain tension

3. Tempo control
   - Slow motion for key moments
   - Fast pace for climax

Save the result to scene_XX_action.md
```

---

##### 2.2.3 Emotion-Focused Scenes (Emotion Writer)

**Agent**: `@emotion-writer` ([English](/.github/agents/emotion-writer.agent.md#english) | [한국어](/.github/agents/emotion-writer.agent.md#korean))  
**Condition**: For internal monologues, emotional outbursts, flashbacks, etc.  
**Input**:
- `chapter_0X/outline.md`
- `phase1_planning/character_profiles.md`

**Task**:
```
Write emotion-focused scenes:

1. Internal expression
   - Show, Don't Tell (90%+)
   - Express emotions through physical reactions
   - Use metaphors/symbols

2. Emotion layering
   - Surface emotion vs. internal emotion
   - Express complex emotions

3. Induce reader empathy

Save the result to scene_XX_emotion.md
```

---

##### 2.2.4 General Narrative Scenes (Prose Writer)

**Agent**: `@prose-writer` ([English](/.github/agents/prose-writer.agent.md#english) | [한국어](/.github/agents/prose-writer.agent.md#korean))  
**Condition**: For general narrative, setting descriptions, transition scenes  
**Input**:
- `chapter_0X/outline.md`
- `phase1_planning/final_plan.md`

**Task**:
```
Write general narrative scenes:

1. Style rules
   - Show, Don't Tell (80%+)
   - Descriptive writing using five senses

2. Balanced narrative
   - Harmony of dialogue/action/description

3. Maintain character consistency

Save the result to scene_XX_prose.md
```

---

##### 2.2.5 Scene Integration (Main Writer)

**Agent**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**Input**: All `scene_XX_*.md` files

**Task**:
```
Integrate written scenes into one chapter:

1. Natural transitions between scenes
2. Ensure stylistic unity
3. Length adjustment: target 3000-4000 characters
4. Verify overall flow

Save the result to projects/<project_name>/phase2_chapters/chapter_0X/draft.md

Quality standard: 75/100 or higher
```

**Output**: `chapter_0X/draft.md`

---

#### Step 2.3: Pacing Verification (Pacing Manager)

**Agent**: `@pacing-manager` ([English](/.github/agents/pacing-manager.agent.md#english) | [한국어](/.github/agents/pacing-manager.agent.md#korean))  
**Input**: 
- `chapter_0X/draft.md`
- `phase1_planning/pacing_plan.md`
- Previous chapters (if any)

**Task**:
```
Verify the pacing of the completed chapter:

1. Analyze actual tempo vs. planned tempo
   - Check tension curve
   - Scene length balance

2. Inter-chapter connection flow
   - Tempo change from previous chapter
   - Preparation for next chapter

3. Improvement recommendations
   - Parts to expand
   - Parts to condense

Save the result to projects/<project_name>/phase2_chapters/chapter_0X/pacing_notes.md
```

**Output**: `chapter_0X/pacing_notes.md`

---

#### Step 2.4: Editing and Feedback (Editorial Team)

**Agent**: `@editorial-team` ([English](/.github/agents/editorial-team.agent.md#english) | [한국어](/.github/agents/editorial-team.agent.md#korean))  
**Input**: `chapter_0X/draft.md`

**Task**:
```
Edit draft.md:

1. Spelling/grammar
2. Consistency verification
3. Readability
4. Structural issues

Output:
- projects/<project_name>/phase2_chapters/chapter_0X/editorial_notes.md
- projects/<project_name>/phase2_chapters/chapter_0X/final.md

Reflect pacing recommendations in the revision.
```

**Output**: 
- `chapter_0X/editorial_notes.md`
- `chapter_0X/final.md`

---

#### Step 2.5: Checkpoint - Chapter Approval

**Checkpoint ID**: `chapter_0X_approval`

**Review Mode**:
```
🔔 Chapter X Complete! Approval required.

Generated files:
- chapter_0X/final.md (3,421 characters)

Quality score: 82/100 ✅
Pacing score: 78/100 ✅

Choose: [A]pprove / [R]ewrite / [E]dit
```

**Upon approval**: Next chapter (or Phase 3)

---

#### After Iteration Complete

When all chapters (1, 2, 3) are complete, proceed to Phase 3.

---

### 🎯 Phase 3: Completion

#### Step 3.1: Overall Integration (Main Writer)

**Agent**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**Input**: All `chapter_0X/final.md`

**Task**:
```
Integrate all chapters into one complete novel:

1. Check chapter connections
2. Overall consistency
3. Generate final novel

Save the result to projects/<project_name>/phase3_final/novel.md
```

**Output**: `phase3_final/novel.md`

---

#### Step 3.2: Final Editing (Editorial Team)

**Agent**: `@editorial-team` ([English](/.github/agents/editorial-team.agent.md#english) | [한국어](/.github/agents/editorial-team.agent.md#korean))  
**Input**: `phase3_final/novel.md`

**Task**:
```
Final editing of the completed novel:

1. Overall spelling/grammar
2. Unity
3. Overall flow
4. Final quality score (0-100)

Output:
- projects/<project_name>/phase3_final/editorial_report.md
- projects/<project_name>/phase3_final/novel_final.md
```

**Output**:
- `phase3_final/editorial_report.md`
- `phase3_final/novel_final.md`

---

#### Step 3.3: Reader Perspective Feedback (Feedback Agent)

**Agent**: `@feedback-agent` ([English](/.github/agents/feedback-agent.agent.md#english) | [한국어](/.github/agents/feedback-agent.agent.md#korean))  
**Input**: `phase3_final/novel_final.md`

**Task**:
```
Evaluate the completed novel from 5 perspectives:

1. Genre expert
2. General reader
3. Editor
4. Writing craft expert
5. Target audience

Calculate average score.

Save the result to projects/<project_name>/phase3_final/feedback_report.md
```

**Output**: `phase3_final/feedback_report.md`

---

#### Step 3.4: Final Approval

**Checkpoint ID**: `final_approval`

```
╔══════════════════════════════════════════════════════════════╗
║          🎉 Novel Creation Complete!                        ║
╚══════════════════════════════════════════════════════════════╝

📊 Final Statistics:
   Total length: 11,247 characters
   Chapters: 3
   Quality score: 85/100 ✅

📁 Generated files:
   projects/<project_name>/phase3_final/novel_final.md

Choose: [A]ccept / [R]evise / [R]ewrite
```

---

### 🎛️ Mode-Specific Behavior

#### Auto Mode
- **Interventions**: 3 times (start, Phase 1, final)
- **Checkpoints**: Auto-approved
- **Use when**: Fast prototyping

#### Review Mode ⭐ (Recommended)
- **Interventions**: 5-7 times (start, Phase 1, each chapter, final)
- **Checkpoints**: Approval required at key points
- **Use when**: Most production work

#### Manual Mode
- **Interventions**: 15-20 times (before/after every agent call)
- **Checkpoints**: Approval for all steps
- **Use when**: Fine-grained control needed

---

### 🔄 Continue Writing

To resume an interrupted project:

```
@copilot Read WORKFLOW_GUIDE.md,
and continue project "<project_name>".

1. Read projects/<project_name>/.novel-studio/status.json to check interruption point
2. Resume from the last completed step
```

---

### 🎯 Quick Start

#### First Novel Generation (Review Mode)

```
@copilot Hello! Please read WORKFLOW_GUIDE.md.

Then write a novel about 
"first love story of two college students on campus" 
as project "my_first_novel" in review mode.

Show me the results at each step and wait for approval.
```

---

<a name="korean"></a>
## 🇰🇷 한국어 버전

이 문서는 GitHub Copilot CLI가 직접 읽고 실행하는 소설 창작 워크플로우를 정의합니다.

---

### 🎯 개요

#### 목적
Copilot CLI가 13개의 전문 에이전트를 순차적으로 호출하여 자동으로 소설을 창작합니다.

#### 실행 방법
```
@copilot WORKFLOW_GUIDE.md를 읽고, 
"[프로젝트명]" 프로젝트로 "[아이디어]" 소설을 [모드]로 써줘.

예시:
@copilot WORKFLOW_GUIDE.md를 읽고,
"first_love" 프로젝트로 "대학생 남녀의 첫사랑" 소설을 review 모드로 써줘.
```

---

### 🏗️ 프로젝트 구조

워크플로우 시작 시 다음 디렉토리를 생성하세요:

```
projects/<프로젝트명>/
├── phase1_planning/
│   ├── story_structure.md
│   ├── character_profiles.md
│   ├── setting_world.md
│   ├── genre_analysis.md
│   ├── pacing_plan.md
│   └── final_plan.md
├── phase2_chapters/
│   ├── chapter_01/
│   │   ├── outline.md
│   │   ├── draft.md
│   │   └── final.md
│   ├── chapter_02/
│   └── chapter_03/
├── phase3_final/
│   ├── final_novel.md
│   ├── editorial_report.md
│   └── feedback_report.md
└── .novel-studio/
    ├── status.json
    ├── checkpoints/
    └── backups/
```

---

### 🎬 Phase 1: 기획 단계 (Planning)

#### 목표
소설의 기본 설계를 완성합니다.

#### Step 1.1: 사용자 요청 분석 (Main Writer)

**에이전트**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**입력**: 사용자의 소설 아이디어  
**작업**:
```
사용자 요청을 분석하여:
1. 장르 파악 (로맨스, 판타지, SF 등)
2. 타겟 독자층
3. 예상 분량 (기본 3챕터)
4. 핵심 메시지
5. 콘셉트 요약

결과를 projects/<프로젝트명>/phase1_planning/concept.md로 저장.
```

**출력**: `concept.md`

---

#### Step 1.2: 병렬 기획 (4개 에이전트 동시 실행)

##### 1.2.1 플롯 구성 (Story Writer)

**에이전트**: `@story-writer` ([English](/.github/agents/story-writer.agent.md#english) | [한국어](/.github/agents/story-writer.agent.md#korean))  
**입력**: `concept.md`  
**작업**:
```
concept.md를 읽고 플롯을 구성하세요:

1. 3막 구조 설계
   - 1막: 발단 (Chapter 1)
   - 2막: 전개/절정 (Chapter 2)
   - 3막: 결말 (Chapter 3)

2. 각 챕터별 개요
   - 핵심 사건
   - 감정 곡선 (%)
   - 예상 분량 (3000-4000자)

3. 복선 및 반전 설계

결과를 projects/<프로젝트명>/phase1_planning/story_structure.md로 저장.

품질 기준: 75/100 이상
```

**출력**: `story_structure.md`

---

##### 1.2.2 캐릭터 설계 (Character Writer)

**에이전트**: `@character-writer` ([English](/.github/agents/character-writer.agent.md#english) | [한국어](/.github/agents/character-writer.agent.md#korean))  
**입력**: `concept.md`  
**작업**:
```
concept.md를 읽고 캐릭터를 설계하세요:

1. 주인공 프로필
   - 이름, 나이, 외모
   - 성격 (MBTI 포함)
   - 배경 스토리
   - 목표와 동기
   - 특징적 습관 ("안경 올리기" 등)

2. 주요 조연 프로필 (1-2명)

3. 캐릭터 관계도

4. 대사 톤 정의
   - 말투 특징
   - 존댓말/반말 규칙

결과를 projects/<프로젝트명>/phase1_planning/character_profiles.md로 저장.

품질 기준: 75/100 이상
```

**출력**: `character_profiles.md`

---

##### 1.2.3 배경 설정 (Setting Writer)

**에이전트**: `@setting-writer` ([English](/.github/agents/setting-writer.agent.md#english) | [한국어](/.github/agents/setting-writer.agent.md#korean))  
**입력**: `concept.md`  
**작업**:
```
concept.md를 읽고 배경을 설정하세요:

1. 시공간 배경
   - 시간: 년도, 계절, 시간대
   - 공간: 주요 장소 3-5곳

2. 각 장소 상세 묘사
   - 5감 활용
   - 분위기
   - 상징적 의미

3. 세계관 규칙

결과를 projects/<프로젝트명>/phase1_planning/setting_world.md로 저장.

품질 기준: 75/100 이상
```

**출력**: `setting_world.md`

---

##### 1.2.4 장르 분석 (Genre Specialist)

**에이전트**: `@genre-specialist` ([English](/.github/agents/genre-specialist.agent.md#english) | [한국어](/.github/agents/genre-specialist.agent.md#korean))  
**입력**: `concept.md`  
**작업**:
```
concept.md를 읽고 장르 전략을 수립하세요:

1. 장르 분류 및 하위 장르
   - 주 장르 + 보조 장르
   - 타겟 독자층 재검증

2. 장르별 트로프 제안
   - 필수 트로프 3-5개
   - 피해야 할 클리셰
   - 신선한 변주 제안

3. 장르 컨벤션
   - 기대되는 요소들
   - 결말 방향성
   - 문체/톤 권장사항

4. 장르별 품질 기준

결과를 projects/<프로젝트명>/phase1_planning/genre_analysis.md로 저장.

품질 기준: 75/100 이상
```

**출력**: `genre_analysis.md`

---

#### Step 1.3: 기획 통합 (Main Writer)

**에이전트**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**입력**: 
- `story_structure.md`
- `character_profiles.md`
- `setting_world.md`
- `genre_analysis.md`

**작업**:
```
4개 기획서를 읽고 통합 기획서를 작성하세요:

1. 일관성 검증
2. 충돌 해결
3. 최종 기획서 작성

결과를 projects/<프로젝트명>/phase1_planning/final_plan.md로 저장.
```

**출력**: `final_plan.md`

---

#### Step 1.4: 페이싱 설계 (Pacing Manager)

**에이전트**: `@pacing-manager` ([English](/.github/agents/pacing-manager.agent.md#english) | [한국어](/.github/agents/pacing-manager.agent.md#korean))  
**입력**: 
- `final_plan.md`
- `story_structure.md`

**작업**:
```
통합 기획서를 읽고 전체 페이싱을 설계하세요:

1. 챕터별 템포 분석
   - 긴장도 곡선 (0-100%)
   - 장면 길이 밸런스
   - 휴식/긴장 리듬

2. 감정 변화 커브
   - 챕터별 감정 강도
   - 클라이맥스 타이밍

3. 정보 전달 속도
   - 복선 배치 타이밍
   - 폭로/반전 위치

4. 개선 권장사항

결과를 projects/<프로젝트명>/phase1_planning/pacing_plan.md로 저장.

품질 기준: 75/100 이상
```

**출력**: `pacing_plan.md`

---

#### Step 1.5: 체크포인트 - Phase 1 승인

**체크포인트 ID**: `phase1_approval`

**Review 모드**:
```
🔔 Phase 1 완료! 승인이 필요합니다.

생성된 파일:
- phase1_planning/story_structure.md
- phase1_planning/character_profiles.md
- phase1_planning/setting_world.md
- phase1_planning/genre_analysis.md
- phase1_planning/pacing_plan.md
- phase1_planning/final_plan.md

선택:
[A]pprove / [R]eject / [M]odify
```

**승인 시**: Phase 2로 진행

---

### ✍️ Phase 2: 집필 단계 (Writing)

#### 목표
각 챕터를 완성합니다 (기본 3챕터).

#### 반복: 각 챕터마다 (Chapter 1, 2, 3)

---

#### Step 2.1: 챕터 개요 작성 (Story Writer)

**에이전트**: `@story-writer` ([English](/.github/agents/story-writer.agent.md#english) | [한국어](/.github/agents/story-writer.agent.md#korean))  
**입력**: 
- `phase1_planning/final_plan.md`
- 이전 챕터들 (있는 경우)

**작업**:
```
final_plan.md를 읽고 Chapter X의 상세 개요를 작성하세요:

1. 장면 구성 (3-5개 장면)
2. 복선/떡밥
3. 클라이맥스 설계 (2막인 경우)

결과를 projects/<프로젝트명>/phase2_chapters/chapter_0X/outline.md로 저장.
```

**출력**: `chapter_0X/outline.md`

---

#### Step 2.2: 본문 작성 (장면 유형별 전문 작가)

**작업 흐름**:
1. `outline.md`에서 장면 유형 분석
2. 각 장면 유형에 맞는 전문 작가 배정
3. 장면별 작성 후 통합

---

##### 2.2.1 대화 중심 장면 (Dialogue Writer)

**에이전트**: `@dialogue-writer` ([English](/.github/agents/dialogue-writer.agent.md#english) | [한국어](/.github/agents/dialogue-writer.agent.md#korean))  
**조건**: 장면이 대화 중심일 때 (캐릭터 간 상호작용, 논쟁, 고백 등)  
**입력**:
- `chapter_0X/outline.md`
- `phase1_planning/character_profiles.md`

**작업**:
```
대화 중심 장면을 작성하세요:

1. 자연스러운 대화 흐름
   - 캐릭터별 말투 일관성
   - 대화 태그 다양화
   - 비언어적 커뮤니케이션 포함

2. 하위 텍스트 (Subtext)
   - 말하지 않는 감정
   - 긴장감 조성

3. 대화와 행동 균형 (60:40)

결과를 scene_XX_dialogue.md로 저장.
```

---

##### 2.2.2 액션 장면 (Action Writer)

**에이전트**: `@action-writer` ([English](/.github/agents/action-writer.agent.md#english) | [한국어](/.github/agents/action-writer.agent.md#korean))  
**조건**: 액션/전투/추격 장면일 때  
**입력**:
- `chapter_0X/outline.md`
- `phase1_planning/setting_world.md`

**작업**:
```
액션 장면을 작성하세요:

1. 역동적인 묘사
   - 짧고 강렬한 문장
   - 연속적인 동작 흐름
   - 공간감/거리감 명확히

2. 5감 활용
   - 소리, 촉각, 시각 중심
   - 긴장감 유지

3. 템포 조절
   - 중요 순간은 슬로우 모션
   - 클라이맥스는 빠르게

결과를 scene_XX_action.md로 저장.
```

---

##### 2.2.3 감정 중심 장면 (Emotion Writer)

**에이전트**: `@emotion-writer` ([English](/.github/agents/emotion-writer.agent.md#english) | [한국어](/.github/agents/emotion-writer.agent.md#korean))  
**조건**: 내면 독백, 감정 폭발, 회상 등  
**입력**:
- `chapter_0X/outline.md`
- `phase1_planning/character_profiles.md`

**작업**:
```
감정 중심 장면을 작성하세요:

1. 내면 표현
   - Show, Don't Tell (90% 이상)
   - 신체 반응으로 감정 표현
   - 은유/상징 활용

2. 감정 레이어링
   - 표면 감정 vs 내면 감정
   - 복합적 감정 표현

3. 독자 공감 유도

결과를 scene_XX_emotion.md로 저장.
```

---

##### 2.2.4 일반 서술 장면 (Prose Writer)

**에이전트**: `@prose-writer` ([English](/.github/agents/prose-writer.agent.md#english) | [한국어](/.github/agents/prose-writer.agent.md#korean))  
**조건**: 일반적인 서술, 배경 묘사, 전환 장면  
**입력**:
- `chapter_0X/outline.md`
- `phase1_planning/final_plan.md`

**작업**:
```
일반 서술 장면을 작성하세요:

1. 문체 규칙
   - Show, Don't Tell (80% 이상)
   - 5감 활용한 묘사

2. 균형잡힌 서술
   - 대화/행동/묘사 조화

3. 캐릭터 일관성 유지

결과를 scene_XX_prose.md로 저장.
```

---

##### 2.2.5 장면 통합 (Main Writer)

**에이전트**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**입력**: 모든 `scene_XX_*.md` 파일들

**작업**:
```
작성된 장면들을 하나의 챕터로 통합하세요:

1. 장면 간 자연스러운 전환
2. 문체 통일성 확보
3. 분량 조절: 3000-4000자 목표
4. 전체 흐름 검증

결과를 projects/<프로젝트명>/phase2_chapters/chapter_0X/draft.md로 저장.

품질 기준: 75/100 이상
```

**출력**: `chapter_0X/draft.md`

---

#### Step 2.3: 페이싱 검증 (Pacing Manager)

**에이전트**: `@pacing-manager` ([English](/.github/agents/pacing-manager.agent.md#english) | [한국어](/.github/agents/pacing-manager.agent.md#korean))  
**입력**: 
- `chapter_0X/draft.md`
- `phase1_planning/pacing_plan.md`
- 이전 챕터들 (있는 경우)

**작업**:
```
완성된 챕터의 페이싱을 검증하세요:

1. 계획 대비 실제 템포 분석
   - 긴장도 곡선 확인
   - 장면 길이 밸런스

2. 챕터 간 연결 흐름
   - 이전 챕터와의 템포 변화
   - 다음 챕터 준비도

3. 개선 권장사항
   - 늘려야 할 부분
   - 축약해야 할 부분

결과를 projects/<프로젝트명>/phase2_chapters/chapter_0X/pacing_notes.md로 저장.
```

**출력**: `chapter_0X/pacing_notes.md`

---

#### Step 2.4: 교정 및 피드백 (Editorial Team)

**에이전트**: `@editorial-team` ([English](/.github/agents/editorial-team.agent.md#english) | [한국어](/.github/agents/editorial-team.agent.md#korean))  
**입력**: `chapter_0X/draft.md`

**작업**:
```
draft.md를 교정하세요:

1. 맞춤법/문법
2. 일관성 검증
3. 가독성
4. 구조적 문제

결과:
- projects/<프로젝트명>/phase2_chapters/chapter_0X/editorial_notes.md
- projects/<프로젝트명>/phase2_chapters/chapter_0X/final.md

페이싱 권장사항을 반영하여 수정.
```

**출력**: 
- `chapter_0X/editorial_notes.md`
- `chapter_0X/final.md`

---

#### Step 2.5: 체크포인트 - 챕터 승인

**체크포인트 ID**: `chapter_0X_approval`

**Review 모드**:
```
🔔 Chapter X 완료! 승인이 필요합니다.

생성된 파일:
- chapter_0X/final.md (3,421자)

품질 점수: 82/100 ✅
페이싱 점수: 78/100 ✅

선택: [A]pprove / [R]ewrite / [E]dit
```

**승인 시**: 다음 챕터로 (또는 Phase 3로)

---

#### 반복 완료 후

모든 챕터 (1, 2, 3) 완료 시 Phase 3로 진행.

---

### 🎯 Phase 3: 완성 단계 (Completion)

#### Step 3.1: 전체 통합 (Main Writer)

**에이전트**: `@main-writer` ([English](/.github/agents/main-writer.agent.md#english) | [한국어](/.github/agents/main-writer.agent.md#korean))  
**입력**: 모든 `chapter_0X/final.md`

**작업**:
```
모든 챕터를 하나의 완성된 소설로 통합하세요:

1. 챕터 연결부 확인
2. 전체 일관성
3. 최종 소설 생성

결과를 projects/<프로젝트명>/phase3_final/novel.md로 저장.
```

**출력**: `phase3_final/novel.md`

---

#### Step 3.2: 최종 교정 (Editorial Team)

**에이전트**: `@editorial-team` ([English](/.github/agents/editorial-team.agent.md#english) | [한국어](/.github/agents/editorial-team.agent.md#korean))  
**입력**: `phase3_final/novel.md`

**작업**:
```
완성된 소설을 최종 교정하세요:

1. 전체 맞춤법/문법
2. 통일성
3. 전체 흐름
4. 최종 품질 점수 (0-100)

결과:
- projects/<프로젝트명>/phase3_final/editorial_report.md
- projects/<프로젝트명>/phase3_final/novel_final.md
```

**출력**:
- `phase3_final/editorial_report.md`
- `phase3_final/novel_final.md`

---

#### Step 3.3: 독자 관점 피드백 (Feedback Agent)

**에이전트**: `@feedback-agent` ([English](/.github/agents/feedback-agent.agent.md#english) | [한국어](/.github/agents/feedback-agent.agent.md#korean))  
**입력**: `phase3_final/novel_final.md`

**작업**:
```
완성된 소설을 5가지 관점에서 평가하세요:

1. 장르 전문가
2. 일반 독자
3. 편집자
4. 작법 전문가
5. 타겟 독자층

평균 점수 산출.

결과를 projects/<프로젝트명>/phase3_final/feedback_report.md로 저장.
```

**출력**: `feedback_report.md`

---

#### Step 3.4: 최종 승인

**체크포인트 ID**: `final_approval`

```
╔══════════════════════════════════════════════════════════════╗
║          🎉 소설 생성 완료!                                 ║
╚══════════════════════════════════════════════════════════════╝

📊 최종 통계:
   총 분량: 11,247자
   챕터 수: 3개
   품질 점수: 85/100 ✅

📁 생성된 파일:
   projects/<프로젝트명>/phase3_final/novel_final.md

선택: [A]ccept / [R]evise / [R]ewrite
```

---

### 🎛️ 모드별 동작

#### Auto 모드
- **개입**: 3회 (시작, Phase 1, 최종)
- **체크포인트**: 자동 승인
- **사용 시기**: 빠른 프로토타입

#### Review 모드 ⭐ (추천)
- **개입**: 5-7회 (시작, Phase 1, 각 챕터, 최종)
- **체크포인트**: 주요 시점 승인 필요
- **사용 시기**: 대부분의 실전 창작

#### Manual 모드
- **개입**: 15-20회 (모든 에이전트 호출 전후)
- **체크포인트**: 모든 단계 승인
- **사용 시기**: 세밀한 통제

---

### �� 이어쓰기 (Continue)

중단된 프로젝트 재개:

```
@copilot WORKFLOW_GUIDE.md를 읽고,
"<프로젝트명>" 프로젝트를 이어서 써줘.

1. projects/<프로젝트명>/.novel-studio/status.json 읽어서 중단 시점 확인
2. 마지막 완료된 단계 이후부터 재개
```

---

### 🎯 Quick Start

#### 첫 소설 생성 (Review 모드)

```
@copilot 안녕! WORKFLOW_GUIDE.md를 읽어줘.

그리고 "my_first_novel" 프로젝트로 
"대학 캠퍼스에서 만난 두 남녀의 첫사랑 이야기" 소설을
review 모드로 작성해줘.

각 단계마다 결과를 보여주고, 승인을 기다려줘.
```

---

**Document Version**: v1.0-bilingual  
**Last Updated**: 2026-02-15  
**Authors**: Novel Studio for Copilot CLI — [tiny_flowlab](https://github.com/tiny-flowlab)
