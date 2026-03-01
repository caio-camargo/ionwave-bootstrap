# Active Work Coordination

**Purpose**: Prevent concurrent edit conflicts between operators (Caio, Danilo) and their Claude sessions.
**Rule**: Check this file at session start. Claim your zone before working. Clear it when done.

---

## How to Use

**Before starting work:**
1. Read this file
2. Check if anyone is working on files you plan to touch
3. Add your claim below with name, date, and scope
4. If there's a conflict, coordinate with the other person before proceeding

**When done:**
1. Remove your claim from the table
2. If you left anything mid-way, note it in `unresolved` below

**Claude agents**: Follow these same steps. If you see an active claim overlapping your intended work, stop and ask the operator how to proceed.

---

## Currently Active

| Operator | Started | Scope | Files at risk |
|----------|---------|-------|---------------|
| Claude (Session 2026-03-01) | 2026-03-01 | Rollout hypotheses & risk analysis — creating HYP-010+ in registry.json, risk analysis doc in ionwave/IonWave/ | `ionwave/data/hypotheses/registry.json`, `ionwave/data/hypotheses/validation_log.json`, `ionwave/data/hypotheses/index.json`, `ionwave/IonWave/Rollout_Risk_Analysis.md` |

---

## Conflict Zones (files that are tightly coupled — editing one usually means editing the others)

| Zone | Files | Why they're coupled |
|------|-------|-------------------|
| **Hypothesis data layer** | `data/hypotheses/registry.json`, `index.json`, `validation_log.json` | IDs, counts, cross-references must stay in sync |
| **Manifest + TUP meta** | `data/manifest.json`, `data/*/_ meta.json` | Quality scores, migration status, dependency chains |
| **Dashboard + data** | `dashboard/**`, `data/**` | Dashboard reads from data layer — structural changes break rendering |
| **Session log + startup docs** | `SESSION_LOG.md`, `00_START_HERE.md`, `DOCUMENTATION_INDEX.md` | Session log references doc state; startup docs must reflect reality |

If you're touching files in a conflict zone, claim the **whole zone**, not just one file.

---

## Unresolved (mid-flight work from interrupted sessions)

*Nothing currently unresolved.*
