# Claude Project Configuration — Best Practices

**Version**: 1.0.0
**Author**: Caio, Claude
**Date Created**: 2026-03-02
**Last Updated**: 2026-03-02
**AI Model**: claude-sonnet-4-5-20250929
**Purpose**: Best practices for configuring Claude across multiple repos, submodules, and Claude.ai Projects
**Status**: Active
**Related**: CLAUDE_AS_OS_SYSTEM.md, INTEGRATION_DESIGN_PRINCIPLES.md

---

## Why This Document Exists

When a project spans multiple repositories, submodules, and deployment surfaces (Claude Code vs Claude.ai Projects), the question becomes: **how does each participant get the right context without assuming a specific Claude interface?**

This document captures what works, what doesn't, and what to do about it.

---

## 1. CLAUDE.md Is a Pointer, Not a Manual

### The Problem

CLAUDE.md competes for context tokens. A 500-line CLAUDE.md burns context before the session even starts. And if the repo has submodules, those CLAUDE.md files may not load at all.

### The Pattern

CLAUDE.md should be **short and procedural** — a bootstrap sequence that points to real documentation:

```markdown
# Claude Agent Instructions

## Session Startup
1. Read `./00_start_here.md`
2. Follow the instructions there

## Key Protocol
When doing X, read `./processes/X_protocol.md`
```

**What goes IN CLAUDE.md:**
- Session lifecycle (startup, closing)
- Pointers to canonical process docs
- Hard constraints that must never be violated (e.g., "never commit without running the guard")

**What stays OUT of CLAUDE.md:**
- Architecture descriptions (put in a start_here or README)
- Process details (put in dedicated process docs)
- Domain knowledge (put in data files that get loaded on-demand)

### Why

1. **Context budget** — shorter CLAUDE.md = more room for actual work
2. **Portability** — the pointed-to files work whether read by Claude Code, Claude.ai Projects, or a human
3. **No Claude lock-in** — the real documentation doesn't assume it will be read by CLAUDE.md auto-loading. It's useful to anyone who opens it.

---

## 2. How Claude Actually Loads Files

### Claude Code (CLI / IDE)

| Source | When Loaded | Behavior |
|--------|------------|----------|
| Root `CLAUDE.md` | Session startup | Always loaded, full content |
| Ancestor `CLAUDE.md` (parent dirs) | Session startup | Loaded if Claude Code launched from subdirectory |
| Subdirectory `CLAUDE.md` | On-demand | Supposed to load when Claude reads files in that directory — **currently bugged** (issues #2571, #3529) |
| Submodule `CLAUDE.md` | **Never auto-loaded** | Submodules are invisible to glob/grep/ls by default (issue #7852) |
| `.claude/rules/*.md` | Session startup | Modular rules, can be path-scoped with frontmatter |
| `@path` imports in CLAUDE.md | Session startup | Recursively expanded (max 5 hops), first-time approval dialog |

**Key implication**: If your project has submodules, their CLAUDE.md files are effectively invisible to the parent session. Don't rely on them for cross-module coordination.

### Claude.ai Projects (Web)

| Source | When Loaded | Behavior |
|--------|------------|----------|
| Custom Instructions | Every conversation | Text field in project settings, always in context |
| Uploaded files | On-demand / referenced | Uploaded to project knowledge base, available but not always in active context |
| CLAUDE.md | **Not a concept** | No file auto-loading — must be pasted into Custom Instructions or uploaded |

**Key implication**: Claude.ai Projects have no CLAUDE.md equivalent. The "Custom Instructions" field IS the system prompt. Files are uploaded separately. This means any CLAUDE.md-based workflow must be **translated** for Projects users.

---

## 3. The Portability Principle

### Don't assume CLAUDE.md will be read

Any documentation that matters should work as a standalone document a human could read. CLAUDE.md is a convenience layer, not the source of truth.

**Test**: If you deleted CLAUDE.md entirely, could a new team member (human or AI) still figure out how to work in this repo by reading the files that CLAUDE.md points to?

If yes → good architecture.
If no → you've buried critical information in a Claude-specific config file.

### Design for the weakest reader

The recruiting cascade has four node types with decreasing technical sophistication:

| Node | Interface | CLAUDE.md? | Reads docs how? |
|------|-----------|-----------|----------------|
| Caio (oversight) | Claude Code | Yes, auto-loaded | Via repo + CLI |
| VA | Claude.ai Project | No | Uploaded files + Custom Instructions |
| MBA intern | Claude.ai Project | No | Uploaded files + Custom Instructions |
| VP | Claude.ai Project (or Code) | Maybe | Depends on technical comfort |

The documents must work for ALL of these. That means:
- Self-contained role briefs (don't reference CLAUDE.md)
- Process docs that make sense without the bootstrap sequence
- A clear "start here" pattern that works as both a CLAUDE.md pointer AND a standalone orientation doc

---

## 4. Multi-Repo Configuration Patterns

### Pattern A: Pointer CLAUDE.md + Rich Start File (Current — IonWave Bootstrap)

```
repo-root/
  CLAUDE.md              ← 47 lines. Points to 00_start_here.md
  00_start_here.md       ← 562 lines. Full orientation, architecture, conventions
  project_specs/         ← Design principles (read on-demand)
  submodule-a/           ← Has its own CLAUDE.md (not auto-loaded by parent)
  submodule-b/           ← Same
```

**Pros**: Clean separation. Start file works for humans too. CLAUDE.md is tiny.
**Cons**: Two files to maintain (CLAUDE.md + start_here). Submodule CLAUDE.md ignored.
**When to use**: Projects where Claude Code is the primary interface and submodules are repositories that also work independently.

### Pattern B: Modular Rules (`.claude/rules/`)

```
repo-root/
  CLAUDE.md              ← Minimal bootstrap
  .claude/
    rules/
      commit-conventions.md
      code-style.md
      testing.md
      api-design.md       ← Scoped: only loads for src/api/**
```

Rules files can have path-scoped frontmatter:
```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API Design Rules
Always use...
```

**Pros**: Modular. Path-scoped rules don't waste context when working elsewhere.
**Cons**: Only works in Claude Code. Rules directory doesn't translate to Claude.ai Projects.
**When to use**: Large codebases where different directories have different conventions.

### Pattern C: Import-Based (`@path` syntax)

```markdown
# CLAUDE.md
@./docs/session-protocol.md
@./docs/coding-standards.md
@~/.claude/personal-preferences.md
```

**Pros**: Single entry point, content lives in real docs, personal overrides possible.
**Cons**: Import approval dialog on first use. Max 5 hops. Only works in Claude Code. Relative path resolution can be confusing.
**When to use**: When you want CLAUDE.md to feel like a "config file" that assembles context from multiple sources.

### Pattern D: Workspace Config for Claude.ai Projects

For non-Code users (VA, MBA intern, etc.), you need a **translation layer**:

```
repo-root/
  data/rollout/va_package/
    role_brief.md          ← Upload to Project
    sourcing_playbook.md   ← Upload to Project
    screening_criteria.md  ← Upload to Project
    outreach_templates.md  ← Upload to Project
    bilateral_contract.md  ← Upload to Project
  data/rollout/va_workspace/
    project_instructions.md  ← Paste into Custom Instructions
    upload_manifest.md       ← Checklist: what to upload, in what order
    test_script.md           ← Scenarios to verify the Project works
```

**The `project_instructions.md` file is the Claude.ai Projects equivalent of CLAUDE.md.** It should be:
- Self-contained (no `@path` imports, no file references that assume auto-loading)
- Written as a system prompt (imperative, second-person: "You are helping a VA...")
- Include deadline logic, escalation rules, deliverable formats
- Version-controlled in the repo even though it lives as text in Claude.ai

**Pros**: Works for non-technical users. Version-controlled. Testable.
**Cons**: Manual sync — changes to project_instructions.md must be re-pasted into the Project.
**When to use**: Any Claude.ai Project deployment where participants aren't using Claude Code.

---

## 5. Settings Files — What Goes Where

| File | Shared? | Purpose | Context cost |
|------|---------|---------|-------------|
| `CLAUDE.md` | Yes (git) | Session instructions | Yes — every token counts |
| `CLAUDE.local.md` | No (gitignored) | Personal overrides | Yes |
| `.claude/settings.json` | Yes (git) | Tool permissions, MCP servers, env vars | No |
| `.claude/settings.local.json` | No (gitignored) | Local permission overrides | No |
| `.claude/rules/*.md` | Yes (git) | Modular, path-scoped rules | Yes (only matching paths) |
| `~/.claude/CLAUDE.md` | N/A (home dir) | Global personal instructions | Yes |
| `~/.claude/settings.json` | N/A (home dir) | Global personal settings | No |

**Rule of thumb**: If it's instructions/context → it costs tokens. If it's configuration/permissions → it doesn't.

---

## 6. Anti-Patterns

### Don't: Monolith CLAUDE.md
A 400-line CLAUDE.md with architecture docs, coding standards, process descriptions, and domain knowledge. Burns context, hard to maintain, impossible to translate to Claude.ai Projects.

### Don't: Assume submodule CLAUDE.md is loaded
Claude Code doesn't auto-load submodule CLAUDE.md. If you put critical instructions there, parent sessions won't see them. Put cross-module coordination in the parent CLAUDE.md or start_here.

### Don't: Duplicate between CLAUDE.md and Custom Instructions
If the same project serves both Claude Code and Claude.ai Projects users, maintain one canonical source (e.g., `project_instructions.md`) and derive both CLAUDE.md pointers and Custom Instructions from it.

### Don't: Put secrets or credentials in CLAUDE.md
CLAUDE.md is committed to git. It's a public document within the repo. Never put API keys, passwords, or sensitive config there. Use environment variables via `.claude/settings.json` or `.env`.

### Don't: Write CLAUDE.md for Claude only
If a human can't read your CLAUDE.md and understand what to do, it's too Claude-specific. The best CLAUDE.md files are good onboarding docs that happen to also work as AI instructions.

---

## 7. Checklist: Setting Up a New Claude-Integrated Project

### For Claude Code (developer/operator)
- [ ] Create `CLAUDE.md` at repo root (< 100 lines, pointers only)
- [ ] Create `00_start_here.md` or equivalent orientation doc
- [ ] Set up `.claude/settings.json` with tool permissions
- [ ] If multi-operator: create `ACTIVE_WORK.md` + `SESSION_LOG.md` coordination files
- [ ] If submodules: document the commit pattern in CLAUDE.md (submodules need their own commit cycle)
- [ ] Test: start a fresh Claude Code session and verify the bootstrap works

### For Claude.ai Projects (non-technical participant)
- [ ] Write `project_instructions.md` as standalone system prompt
- [ ] Create `upload_manifest.md` listing exactly which files to upload
- [ ] Create `test_script.md` with 3-4 role-play scenarios
- [ ] Test: create the Project, paste instructions, upload files, run test scenarios
- [ ] Document the setup steps so it's reproducible (VA leaves → new VA can set up same Project)

### For both
- [ ] Verify the portability principle: delete CLAUDE.md mentally — can someone still work?
- [ ] Check context budget: are you loading more than ~200 lines of instructions?
- [ ] Version control everything: even Claude.ai Custom Instructions should live as files in the repo

---

## 8. IonWave-Specific Application

### Current state (working well)
- Root CLAUDE.md → 47 lines, points to 00_start_here.md
- 3 submodules (ionwave, execution, tup-system) with their own context
- Caio uses Claude Code for all oversight and TUP workshop work

### What needs building (for the rollout cascade)
- `va_workspace/project_instructions.md` — Custom Instructions for the VA's Claude.ai Project
- `va_workspace/upload_manifest.md` — what to upload
- `va_workspace/test_script.md` — trial scenarios
- Same pattern replicable for `mba_workspace/` and `vp_workspace/` when those nodes activate

### Why not a separate repo for the VA?
The VA doesn't need a repo. They need a Claude.ai Project (web-based, zero git knowledge required). The repo remains the **source of truth** for what goes into that Project, but the VA never sees the repo. Caio sets up the Project, the VA uses it.

If deliverable submission via git becomes necessary later (Phase 2), a lightweight public/private repo could serve as a delivery container. But Phase 1 is: VA sends work via WhatsApp/email → Caio places it in the repo.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-02 | Initial document — multi-repo patterns, CLAUDE.md behavior, portability principles |
