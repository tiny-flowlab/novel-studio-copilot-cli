# 📚 Novel Studio for Copilot CLI - Multi-Agent Novel Creation System

> **Is Copilot CLI just a coding tool?**  Think again.  
> **GitHub Copilot CLI is the ultimate novel-writing studio.**  
> Clone this repo, open Copilot, and say *"Write me a novel"* — that's it.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Copilot CLI](https://img.shields.io/badge/Built%20with-GitHub%20Copilot%20CLI-blue)](https://docs.github.com/en/copilot)
[![Agents](https://img.shields.io/badge/Agents-13%20Specialized-green)](.github/agents/)

**[한국어 README](README_KO.md)**

---

## 🎯 Overview

Novel Studio for Copilot CLI is a system where **13 specialized AI agents** collaborate to automatically create publication-quality novels — all orchestrated natively on **GitHub Copilot CLI**.

Just say `"Write me a novel"` and the agent team handles everything: planning, writing, editing, and quality control.

### 💡 Why Copilot CLI?

Other CLI tools are limited to code generation and terminal commands. **GitHub Copilot CLI goes far beyond coding** — it provides a full agent orchestration platform that makes creative workflows like novel writing possible:

- **Agent Mode** — autonomous multi-step execution, not just Q&A
- **`AGENTS.md` auto-loading** — the system activates the moment you open the project
- **`@agent` invocation** — 13 specialists collaborate via `@name` references
- **Hooks lifecycle** — automated quality checks fire on every file operation
- **Model selection** — choose your preferred AI model (GPT-4o, Claude, Gemini, etc.) directly in Copilot settings to balance speed, quality, and cost for each writing session
- **VS Code Copilot Chat integration** — the same `@agent` calls and chat-based workflow work seamlessly in VS Code's GitHub Copilot Chat panel, giving you a full GUI experience alongside the CLI

### Demo: Real Session Log

```
$ cd novel-studio-copilot-cli

  ┌─────────────────────────────────────────────────────────┐
  │  Novel Studio for Copilot CLI (Sales Representative)    │
  │                                                         │
  │  Hello! Welcome to Novel Studio.                        │
  │  What kind of novel would you like?                     │
  └─────────────────────────────────────────────────────────┘

User: "Write me a college romance novel"

  Novel Studio:
    Let me confirm a few details...
    1️⃣ Project name?  → first_love
    2️⃣ Work mode?     → review (recommended)

User: "first_love, review"

  Novel Studio:
    ✅ Request received! Forwarding to @main-writer...

    📋 Phase 1: Planning
      ✓ @story-writer      Plot structure .............. done
      ✓ @character-writer   Character profiles ......... done
      ✓ @setting-writer     World-building ............. done
      ✓ @genre-specialist   Genre analysis ............. done
      ✓ @pacing-manager     Tempo design ............... done

    🔔 Phase 1 complete. [A]pprove / [R]evise / [M]odify?

User: A

  Novel Studio:
    ✍️ Phase 2: Writing Chapter 1 / 3
      → @dialogue-writer   conversation scenes
      → @emotion-writer    emotional scenes
      → @prose-writer      narrative sections
      → @editorial-team    proofreading

    ✍️ Phase 2: Writing Chapter 2 / 3 ...
    ✍️ Phase 2: Writing Chapter 3 / 3 ...

    📦 Phase 3: Finalization
      → @editorial-team    final proofreading
      → @feedback-agent    reader evaluation (5 perspectives)

    ✅ Novel complete!
       Quality: 91/100 (publication-grade)
       Output:  projects/first_love/phase3_final/novel_final.md
```

### Key Features

- ✅ **Fully Automated**: Start with just "Write me a novel"
- ✅ **Specialized Team**: 13 expert agents (6 planning + 4 writing + 3 quality)
- ✅ **Scene-Based Specialization**: Dedicated writers for dialogue / action / emotion scenes
- ✅ **Proven Quality**: 91/100 publication-grade output (validated on real project)
- ✅ **Human-in-the-Loop**: User intervention only at key checkpoints (5-7 times)
- ✅ **Automated QA**: Consistency checks, spell checking, auto-backups via hooks
- ✅ **Model Flexibility**: Choose any AI model available in Copilot (GPT-4o, Claude, Gemini, etc.)
- ✅ **VS Code + CLI**: Works in both Copilot CLI terminal and VS Code Copilot Chat — same agents, same workflow

---

## ⚙️ How It Works with Copilot CLI

This project is designed as a **Copilot CLI-native** multi-agent system. Every component maps directly to a Copilot CLI feature:

### 1. `AGENTS.md` — Auto-Loaded Entry Point

Copilot CLI automatically reads `AGENTS.md` from the project root as a **custom instruction**. This file acts as the **Sales Representative** agent — the front door to the entire system. When a user opens Copilot CLI in this directory, AGENTS.md is injected into the system prompt, enabling the agent to greet the user, gather requirements, and route work to specialized agents.

```
novel-studio-copilot-cli/
└── AGENTS.md          ← Copilot CLI auto-loads this as custom_instruction
```

### 2. `.github/agents/*.agent.md` — Specialized Agent Profiles

Each of the 13 agents is defined as a `.agent.md` file in `.github/agents/`. Copilot CLI recognizes this directory convention and makes each agent invocable via `@agent-name` syntax:

```
@main-writer    → .github/agents/main-writer.agent.md
@story-writer   → .github/agents/story-writer.agent.md
@prose-writer   → .github/agents/prose-writer.agent.md
...
```

The Main Writer orchestrates the workflow by calling other agents with `@agent-name` references, creating a **chain of specialized agents** that collaborate on a single novel.

### 3. Hooks — Lifecycle Automation

Copilot CLI hooks in the `hooks/` directory trigger automation at key lifecycle events:

| Hook | Copilot CLI Event | What It Does |
|------|-------------------|-------------|
| `sessionStart.sh` | Session opens | Loads previous project context & status |
| `preToolUse.sh` | Before file edit | Runs consistency checks on characters/settings |
| `postToolUse.sh` | After file save | Spell check, readability analysis, auto-backup |
| `errorOccurred.sh` | On error | Logs errors and notifies the user |

### 4. Agent Orchestration Pattern

The system uses a **hierarchical delegation pattern** built entirely on Copilot CLI's agent invocation:

```
User → AGENTS.md (Sales Rep, auto-loaded)
         ↓
       @main-writer (coordinator)
         ↓
       @story-writer + @character-writer + @setting-writer  (parallel planning)
         ↓
       @dialogue-writer / @action-writer / @emotion-writer  (scene specialists)
         ↓
       @editorial-team + @feedback-agent  (quality control)
```

### 5. Copilot CLI Features Used

| Feature | How We Use It |
|---------|---------------|
| **`AGENTS.md` auto-load** | Entry-point agent (Sales Rep) loaded automatically |
| **`.github/agents/` directory** | 13 specialized agent profiles, invocable via `@name` |
| **`@agent` invocation** | Inter-agent delegation (`@main-writer` calls `@story-writer`) |
| **Hooks (`hooks/`)** | Pre/post tool-use automation, session initialization |
| **Agent Mode** | Full agentic workflow — file creation, script execution, multi-step tasks |
| **Tool use (bash/python)** | Quality scripts (`check_consistency.py`, `readability.py`) run automatically |
| **`custom_instruction`** | `AGENTS.md` shapes Copilot CLI behavior for the entire project |

---

## 📋 Prerequisites

### Required
1. **GitHub Copilot CLI** — [Installation Guide](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
   ```bash
   gh extension install github/gh-copilot
   ```

### Optional (For Automated Quality Assurance)
- **Python 3.8+**: Runs utility scripts for spell-checking and consistency analysis.
- **Bash**: Required if you want to use the automated `hooks/` system.
- **Git**: For version control of your generated novels.

---

## 🚀 Quick Start (In 30 Seconds)

1. **Clone & Enter**:
   ```bash
   git clone https://github.com/tiny-flowlab/novel-studio-copilot-cli.git
   cd novel-studio-copilot-cli
   ```

2. **Run Copilot**:
   - **CLI**: Run `gh copilot`
   - **VS Code**: Open folder and open **Copilot Chat Panel** (`Ctrl+Alt+I`)

3. **Start Writing**:
   Type: **"Write me a novel"**

   The **Sales Representative** (via `AGENTS.md`) will guide you through project naming, mode selection, and **language selection (English/Korean)**.

---

### 💡 Pro Tips for New Users

- **Environment**: You **must** be in the project root directory for `AGENTS.md` and the 13 agents to be active.
- **First Call**: When the Sales Rep transfers to `@main-writer`, always confirm your preferred language (A: English, B: Korean).
- **Sub-Agents**: You can call specialists directly for advice, e.g., `@genre-specialist What are the typical tropes for Cyberpunk?`

### Step 4: Follow the Guided Process

```
Novel Studio for Copilot CLI (Sales Representative):
  Hello! Let me confirm a few details...

  1️⃣ Project name?        → e.g., "first_love"
  2️⃣ Work mode?           → auto / review (recommended) / manual

User: "first_love, review"

Novel Studio:
  ✅ Request received! Forwarding to @main-writer...

  📋 Phase 1: Planning
    ✓ @story-writer: Plot structure completed
    ✓ @character-writer: Character design completed
    ✓ @setting-writer: World-building completed
    ✓ @genre-specialist: Genre analysis completed

  🔔 Phase 1 complete — approval needed. [A]pprove / [R]evise / [M]odify?

User: A

Novel Studio:
  ✍️ Phase 2: Writing Chapter 1...
    → @dialogue-writer handling conversation scenes
    → @emotion-writer handling emotional scenes
    → @prose-writer handling narrative sections
    ...
```

### Step 5: Get Your Novel

Output is saved to:

```
projects/first_love/
├── phase1_planning/       ← Plot, characters, setting docs
├── phase2_chapters/       ← Chapter drafts & finals
├── phase3_final/          ← Integrated novel + editorial report
└── .novel-studio/                ← Status tracking & backups
```

---

## 🏗️ System Architecture

### Directory Structure

```
novel-studio-copilot-cli/
├── AGENTS.md                    ← Sales Representative (auto-loaded by Copilot CLI)
├── WORKFLOW_GUIDE.md            ← Workflow definitions
├── config.yaml                  ← Agent configuration
├── .github/agents/              ← 13 specialized agents (+ 13 Korean variants)
│   ├── main-writer.agent.md
│   ├── story-writer.agent.md
│   ├── character-writer.agent.md
│   ├── setting-writer.agent.md
│   ├── genre-specialist.agent.md
│   ├── pacing-manager.agent.md
│   ├── dialogue-writer.agent.md
│   ├── action-writer.agent.md
│   ├── emotion-writer.agent.md
│   ├── prose-writer.agent.md
│   ├── editorial-team.agent.md
│   ├── feedback-agent.agent.md
│   ├── research-agent.agent.md
│   └── ko-*.agent.md           ← Korean language variants
├── hooks/                       ← Copilot CLI lifecycle hooks
├── scripts/                     ← Quality assurance utilities
├── templates/                   ← Project templates
└── projects/                    ← Generated novel output
```

### Agent Team (13 Agents)

| Phase | Agent | Role | Quality Target |
|-------|-------|------|----------------|
| **Planning** | Main Writer | Project coordinator & quality gate | 85/100 |
| | Story Writer | Plot construction, narrative arcs | 75/100 |
| | Character Writer | Character creation, relationships | 75/100 |
| | Setting Writer | World-building, environments | 75/100 |
| | Genre Specialist | Genre analysis, trope strategy | 75/100 |
| | Pacing Manager | Tempo control, rhythm management | — |
| **Writing** | Dialogue Writer | Conversation scene specialist | 75/100 |
| | Action Writer | Action/combat scene specialist | 75/100 |
| | Emotion Writer | Emotion/introspection specialist | 75/100 |
| | Prose Writer | General narrative prose | 75/100 |
| **Quality** | Editorial Team | Proofreading, editing, consistency | — |
| | Feedback Agent | Reader perspective evaluation | — |
| | Research Agent | Fact-checking, verification | — |

---

## 📋 Workflow

### Phase 1: Planning

```
User Request → @main-writer analysis
    ↓
Parallel Execution (4 agents):
  ├─ @story-writer      → Plot structure
  ├─ @character-writer   → Character design
  ├─ @setting-writer     → World-building
  └─ @genre-specialist   → Genre analysis & tropes
    ↓
@pacing-manager → Overall tempo design
    ↓
@main-writer → Integration & coordination
    ↓
Checkpoint → User approval
```

### Phase 2: Writing (per chapter)

```
@story-writer → Detailed chapter outline
    ↓
Scene-type specialist assignment:
  ├─ @dialogue-writer → Conversation scenes
  ├─ @action-writer   → Action scenes
  ├─ @emotion-writer   → Emotional scenes
  └─ @prose-writer     → General narrative
    ↓
@main-writer → Scene integration
    ↓
@pacing-manager → Tempo verification
    ↓
@editorial-team → Proofreading & feedback
    ↓
Checkpoint → User approval (Review mode)
```

### Phase 3: Finalization

```
@main-writer → Full manuscript integration
    ↓
@editorial-team → Final proofreading
    ↓
@feedback-agent → Reader evaluation (5 perspectives)
    ↓
Final approval → Publication ready
```

---

## 🎛️ Work Modes

| Mode | Interventions | Checkpoints | Best For |
|------|---------------|-------------|----------|
| ⭐ **Review** (Recommended) | 5-7 times | Phase 1 done, each chapter, final | Most users |
| 🚀 **Auto** | 3 times | Start, Phase 1 done, final | Quick prototypes |
| 🎨 **Manual** | 15-20 times | Every step | Full creative control |

---

## 💡 Usage Examples

**Basic:**
```
"Write me a college campus romance novel"
```

**Detailed:**
```
Project name: campus_love
Idea: First love between an engineering student and humanities student. Cherry blossom season setting.
Mode: review
Length: 3 chapters
```

**Continue an existing project:**
```
"Continue the first_love project"
```

**Rewrite a chapter:**
```
"Rewrite Chapter 2 of first_love. Incorporate feedback from editorial_notes.md."
```

**Call a specific agent:**
```
@prose-writer Read phase2_chapters/chapter_02/outline.md and write the main text.
```

---

## 📊 Real-World Validation

### first_love_001 Project

| Metric | Result |
|--------|--------|
| Length | 11,900 characters / 3 chapters (Korean prose) |
| Quality Score | **91/100** (publication-grade) |
| Duration | 4 hours |
| Feature | Emotional arc via seasonal imagery (cherry blossoms → green → summer) |

**Multi-perspective Ratings:**

| Reviewer | Score |
|----------|-------|
| Genre Specialist | 85/100 |
| General Reader | 80/100 |
| Editor | 90/100 |
| Writing Technique Expert | 82/100 |
| Target Audience | 88/100 |

---

## 📈 Performance: Evolution to v1.0

| Metric | Beta (Manual) | v1.0 (Current) | Improvement |
|--------|---------------|-----------------|-------------|
| Agent Count | 8 | 13 | +5 |
| User Interventions | 20 | 5-7 | **-70%** |
| Automation | 0% | 70% | **+70%** |
| Duration | 4 hrs | 3 hrs | **-25%** |
| Scene Specialization | ❌ | ✅ | New |
| Genre Analysis | ❌ | ✅ | New |
| Auto Consistency Check | ❌ | ✅ | New |
| Auto Spell Check | ❌ | ✅ | New |
| Auto Backup | ❌ | ✅ | New |

---

## 🛠️ Automation Details

### Hooks

| Hook | Trigger | Function |
|------|---------|----------|
| `sessionStart.sh` | Session start | Load previous context |
| `preToolUse.sh` | Before file edit | Consistency check |
| `postToolUse.sh` | After file save | Spell check / readability / backup |
| `errorOccurred.sh` | Error occurs | Logging and notification |

### Quality Scripts

| Script | Function |
|--------|----------|
| `check_consistency.py` | Verify character/setting consistency |
| `spell_check.py` | Spell checking |
| `readability.py` | Repetitive expressions, sentence length analysis |
| `update_status.py` | Auto-update project status |

---

## 📁 Generated Project Structure

```
projects/<project_name>/
├── phase1_planning/
│   ├── concept.md               # Concept overview
│   ├── story_structure.md       # Plot structure
│   ├── character_profiles.md    # Character designs
│   ├── setting_world.md         # World-building
│   └── final_plan.md            # Integrated plan
├── phase2_chapters/
│   ├── chapter_01/
│   │   ├── outline.md           # Detailed outline
│   │   ├── draft.md             # First draft
│   │   ├── editorial_notes.md   # Editorial feedback
│   │   └── final.md             # Final version
│   ├── chapter_02/
│   └── chapter_03/
├── phase3_final/
│   ├── novel.md                 # Integrated manuscript
│   ├── novel_final.md           # Final version
│   ├── editorial_report.md      # Final editorial report
│   └── feedback_report.md       # Reader evaluation report
└── .novel-studio/
    ├── status.json              # Progress status
    ├── checkpoints/             # Checkpoints
    └── backups/                 # Automatic backups
```

---

## 🐛 Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Agent not responding | Not running in Copilot CLI session | Open project in VS Code with Copilot, or run `gh copilot` |
| Consistency errors | Character/setting mismatch between chapters | Check `character_profiles.md`, request chapter rewrite |
| Quality below 75/100 | Draft needs revision | `@prose-writer Rewrite Chapter N. Use editorial_notes.md feedback.` |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [`WORKFLOW_GUIDE.md`](WORKFLOW_GUIDE.md) | Detailed workflow guide |
| [`AGENTS.md`](AGENTS.md) | Sales Representative agent (auto-loaded) |
| [`.github/agents/`](.github/agents/) | All 13 agent profiles |
| [`hooks/README.md`](hooks/README.md) | Hooks system documentation |
| [`config.yaml`](config.yaml) | System configuration |

---

## 🔜 Roadmap

### v1.0 (Current) ✅

- ✅ 13 specialized agent profiles (+ 13 Korean variants)
- ✅ Copilot CLI native architecture (AGENTS.md, .github/agents/, hooks)
- ✅ Scene-based specialization (Dialogue / Action / Emotion)
- ✅ Genre analysis & pacing management
- ✅ Automated hooks & quality scripts
- ✅ Human-in-the-Loop strategy

### v1.1 (Future)

- [ ] Web dashboard for progress monitoring
- [ ] Multi-user collaboration
- [ ] Additional genre specializations
- [ ] E2E integration tests

---

## 🤝 Contributing

Contributions are welcome! You can:

1. Add or improve agent profiles in `.github/agents/`
2. Optimize the workflow in `WORKFLOW_GUIDE.md`
3. Add quality scripts to `scripts/`
4. Improve documentation

---

## 📄 License

[MIT License](LICENSE)

---

## 👥 Credits

**Novel Studio for Copilot CLI — by [tiny_flowlab](https://github.com/tiny-flowlab)**

- Version: 1.0
- Status: Production Ready ✅

---

**Novel Studio for Copilot CLI**  
*"Your Story, Our Craft."*
