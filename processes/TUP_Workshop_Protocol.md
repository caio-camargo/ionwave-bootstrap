# TUP Workshop Protocol (TWP-001)

**Version**: 2.0.0
**Type**: Process Protocol
**Author**: Caio, Claude (collaborative)
**Date Created**: 2026-02-06
**Last Updated**: 2026-02-06
**AI Model**: claude-opus-4-6
**Purpose**: Standard operating procedure for workshopping a TUP from preliminary Danilo structure to production-quality IonWave content + reusable OpKit
**Status**: Active
**Trigger**: When a TUP is selected for workshopping (see `tracking/TUP_Workshop_Tracker.md` for queue)
**Owner Role**: Operator + Claude
**Supersedes**: `ci-protocol/` (CI protocol is now a worked example of this general protocol applied to competitive intelligence)

---

## Overview

Every TUP in the system starts as Danilo's preliminary structural shell: a Project Plan (P), Contract (C), Industry Perspectives (IP), Verification checklist (V), and a set of content tabs that are mostly void spaces to fill.

This protocol turns that shell into two outputs:
1. **IonWave Content** — filled void spaces with graded evidence, validated assumptions, and quality content for Trade #84
2. **OpKit** — reusable production bundle (instruction + rubric + graded examples + scaffold) so any future Trade can execute this TUP excellently

**This protocol is invoked by Claude whenever a TUP is selected for workshopping.** It replaces ad-hoc approaches with a consistent, repeatable process.

**Lineage**: This protocol generalizes the methodology proven in `ci-protocol/` (competitive intelligence), which remains as a worked example. The core patterns — source quality hierarchy, expert persona dialogue to saturation, confidence grading, self-grade rubric — originated there and are now universal.

---

## State Tracker

*Update this as you work. This survives context compaction.*

```
TUP_ID: [M{N}]
TUP_NAME: [name]
CLUSTER: [BCL-{N}]
PHASE: [LOAD | GATHER | CHECKPOINT | RESEARCH | FILL | DIALOGUE | OPKIT | REGISTER | CROSSREF | LOG]
DANILO_TABS: [count]
BOOTSTRAP_SOURCES: [list]
PERSONA_ROUNDS: [0]
PERSONA_SATURATED: [no]
OPKIT_REGISTERED: [no]
QUALITY_SCORE: [pending]
LAST_UPDATED: [timestamp]
```

---

## Inputs

| Input | Location | Purpose |
|-------|----------|---------|
| Danilo's TUP files (P, C, IP, V + content tabs) | `ops_model_v10_dump/{number}_{type}_m{N}.json` | Structural shell and scope definition |
| Bootstrap source files (if any) | `archive/bootstrap-xlsx-pre-tup-migration/` or `data/` | Existing analytical work to build on |
| Existing analysis deliverables (if any) | `IonWave/*.md` | Prior analysis that may feed into this TUP |
| Existing tracking logs (if any) | `tracking/*.md` | Live data relevant to this TUP |
| TUP Workshop Tracker | `tracking/TUP_Workshop_Tracker.md` | Current status, effort estimate, notes |
| Manifest | `data/manifest.json` | TUP metadata, dependencies, blockers |
| Hypotheses Registry | `data/hypotheses/registry.json` | Business hypotheses this TUP may touch |

---

## Protocol Steps

### PHASE 1: LOAD CONTEXT

Read the TUP's Danilo files to understand scope and expectations.

**Actions:**
1. Read the **Project Plan** (`_p_m{N}.json`) — scope, phases, deliverables
2. Read the **Contract** (`_c_m{N}.json`) — accountability, success criteria
3. Read the **Industry Perspectives** (`_ip_m{N}.json`) — research questions, contrarian takes
4. Read the **Verification** (`_v_m{N}.json`) — deliverable checklist, what "done" means
5. Skim all **content tabs** — understand the void spaces
6. Check `manifest.json` for `feeds_into`, `requires`, `key_blockers`, `next_action`
7. Check `data/hypotheses/registry.json` for entries referencing this TUP

**Output:** Mental model of what this TUP is, what it needs, and where it fits.

---

### PHASE 2: GATHER BOOTSTRAP MATERIAL

Check what already exists from prior work.

**Actions:**
1. Check `manifest.json` → `source_files` for Bootstrap mappings
2. Check `IonWave/*.md` for analysis deliverables covering this domain
3. Check `tracking/*.md` for relevant tracking logs
4. Check `data/opkits/registry.json` for any existing OpKit registrations

**Output:** Inventory of existing material. Note what can be reused vs. net-new.

---

### PHASE 3: WORKSHOP CHECKPOINT

Before producing content, align with the user on approach.

**Present to user:**
1. **Scope summary**: "This TUP covers [X]. Danilo has [N] content tabs. Bootstrap has [Y]."
2. **Key questions**: Priority tabs? Anything to skip? Specific concerns?
3. **Dependencies**: Unfinished upstream work? Blockers?
4. **OpKit angle**: What's the reusable artifact? (e.g., "A subscription model design kit")
5. **Industry perspective**: What does Danilo's IP tab ask? What research questions need answering?

**Decision gate:** User confirms or redirects. Do NOT proceed without confirmation.

---

### PHASE 4: RESEARCH & INDUSTRY BEST PRACTICES

Before filling void spaces, ground the work in real-world knowledge.

**This phase generalizes the methodology from `ci-protocol/02_RESEARCH_PHASE.md`.**

**Actions:**
1. **Identify research questions** from Danilo's IP tab and the content tab structure
2. **Search for industry best practices** — how do the best companies in the world handle this TUP's domain?
3. **Find reference models** — real examples (A-grade companies) that demonstrate excellence
4. **Collect data points** — pricing, benchmarks, standards, frameworks used in the industry

**Source Quality Hierarchy** (from `ci-protocol/02_RESEARCH_PHASE.md`):

| Tier | Source Type | Confidence Floor |
|------|------------|-----------------|
| 1 | Audited filings / official disclosures | A |
| 2 | Primary company pages (verified live) | A/B |
| 3 | Third-party corroboration (3+ sources agree) | B |
| 4 | Industry reports / analyst coverage | B/C |
| 5 | Single credible source | C |
| 6 | Social media / forums / reviews | C (B if 3+ corroborate) |
| 7 | Derived calculations | C/D |
| 8 | Industry benchmarks (generic) | C |
| 9 | Best guess / no source | D |

**For each data point collected:**
- Tag with confidence grade: `[Confidence: X | Source: Y | Date: Z]`
- If source is blocked or paywalled, mark D-grade with explicit upgrade path

**Output:** Research notes with graded sources. Reference models identified.

---

### PHASE 5: FILL THE VOID SPACES

Work through Danilo's content tabs, producing quality content in the project's native formats.

**Output format**: Spreadsheets are deprecated. All content is produced as:
- **Markdown** (`.md`) — for analysis deliverables, narrative content, playbooks, and anything humans read
- **JSON** (`.json`) — for structured data (metrics, comparisons, registries, machine-readable content)

Danilo's spreadsheet tabs define the **scope** (what topics to cover), not the format. Each tab becomes one or more files in `data/m{N}/`.

**For each content tab:**
1. Read Danilo's template/structure to understand scope and intent
2. Apply research from Phase 4
3. Produce content in the appropriate format (markdown for narrative, JSON for structured data):
   - Inline confidence grading on every claim
   - Evidence over opinion
   - Intelligence gaps explicitly documented with validation paths
4. Where Bootstrap material exists, integrate and upgrade it
5. Where content requires human data collection (Track B), mark as `[VOID — requires: {what}]` with upgrade path

**Quality standard per tab:**
- Every claim has a confidence grade (A/B/C/D)
- Sources cited inline
- Intelligence gaps noted with validation paths
- No filler — if we can't produce quality content, leave the void marked

**Output:** Markdown and/or JSON files in `data/m{N}/` directory, one or more files per Danilo content tab.

---

### PHASE 6: EXPERT PERSONA DIALOGUE

Stress-test the filled content through multi-perspective dialogue.

**This phase generalizes the methodology from `ci-protocol/04_PERSONA_DIALOGUE.md` and `ci-protocol/07_FRAMEWORKS.md`.**

#### The Expert Personas

**Select 3 personas appropriate to this TUP's domain.** The CI protocol used Skeptical Investor / Customer Anthropologist / Competitive Strategist. For other TUPs, select from this roster or create domain-specific personas:

**Universal Personas (available for any TUP):**
- **Skeptical Investor** — "Show me evidence, not estimates. Would I write a check based on this?"
- **Customer Anthropologist** — "What are actual customers saying? Show me their words."
- **Competitive Strategist** — "Why hasn't someone already done this?"

**Domain-Specific Personas (select when relevant):**
- **Operations Expert** — "What breaks at scale? Where are the single points of failure?"
- **Category Expert** — "What does best-in-class look like in this domain? What are you missing?"
- **Regulatory/Compliance Auditor** — "What could get you sued, fined, or shut down?"
- **Growth Engineer** — "What's the unit economics of this? What's the compounding mechanism?"
- **Brand Strategist** — "Is this coherent with the brand promise? What does this signal?"
- **Technical Architect** — "What's the system design? Where are the integration points?"

**Selection rule:** Pick the 3 personas that create the most productive tension for this TUP. The Skeptical Investor is almost always one of them (financial grounding). The other two should match the domain.

#### Dialogue Structure

**Per round:**
1. **Persona A** reviews content and raises 1-2 challenges
2. **Persona B** responds — confirms with evidence or raises counter-challenge
3. **Persona C** synthesizes — resolves tension or escalates as genuine gap

**Outcomes per round:**
- **RESOLVED** — tension addressed by existing evidence
- **UPGRADED** — gap found, can be filled from research. Update content.
- **UNRESOLVED** — genuine gap. Document in intelligence gaps.

**Round logging:**
```
ROUND [N]:
  CHALLENGE: [1 sentence]
  RESPONSE: [1 sentence]
  SYNTHESIS: [1 sentence]
  OUTCOME: [RESOLVED / UPGRADED / UNRESOLVED]
  ACTION: [what changed]
```

#### Saturation Framework

**Saturation = dialogue producing diminishing returns.**

Detection rules (any triggers saturation):
- 3 consecutive RESOLVED rounds
- Last 2 UNRESOLVED gaps are restatements of documented gaps
- All 3 personas agree content is coherent

**Hard stop: 8 rounds maximum.**

If hard stop hit without saturation, flag for human review.

**Output:** Save `data/m{N}/dialogue_summary.md` with full round log, saturation log, upgrades applied, unresolved gaps, and "what would have been missed" section. This file is the audit trail — it must be saved, not just run in context.

---

### PHASE 7: SELF-GRADE

Grade the TUP's content before finalizing.

**This phase generalizes the methodology from `ci-protocol/06_SELF_GRADE.md`.**

**Grading dimensions:**

| Dimension | Score 5 | Score 3 | Score 1 |
|-----------|---------|---------|---------|
| **Evidence Coverage** | Every tab filled with sourced content | Several tabs at D-grade | Mostly guesses/framework |
| **Confidence Honesty** | Every grade defensible against source hierarchy | Several generous grades | Grades are meaningless |
| **Upgrade Path Quality** | Every below-A item has actionable upgrade path | Half the paths are vague | No upgrade paths |
| **Actionability** | Content enables decisions | Content informs but doesn't guide | Content is informational only |
| **OpKit Reusability** | OpKit works for any Trade in this domain | OpKit is IonWave-specific | No OpKit produced |

**Quality score = average of 5 dimensions, mapped to X/10.**

Be honest — inflated grades undermine the entire system.

---

### PHASE 8: BUILD THE OPKIT

Create the reusable production bundle.

**OpKit components (minimum viable):**
1. **Instruction Doc** — Step-by-step how-to for producing this TUP's deliverables in any Trade
2. **Grading Rubric** — A/B/C/D/F criteria for quality assessment
3. **Scaffold** — 95% pre-built template that an operator fills in
4. **Graded Examples** (if available) — IonWave's content serves as the first graded example (grade it honestly)

**Register the OpKit:**
- Add entry to `data/opkits/registry.json` under `tup_to_opkit`
- Remove TUP from `unmapped_tups`
- Link OpKit to TUP's `_meta.json`

---

### PHASE 9: REGISTER IN SYSTEM

Formalize the TUP in the data layer.

**Actions:**
1. Create `data/m{N}/_meta.json` with standard fields (see TUP Versioning below)
2. Update `data/manifest.json` — status → "migrated", add full metadata, update counts
3. Update `tracking/TUP_Workshop_Tracker.md` — status → DONE, note OpKit status

#### TUP Versioning

TUPs use a `revisions[]` array (same pattern as hypothesis versioning). No top-level `version` field — the current version is derived from the latest revision entry.

**Semver for TUPs:**
- **Major** (X.0.0): Re-workshopped with new data source (e.g., post-launch real data replaces benchmarks)
- **Minor** (1.X.0): Content upgraded from external evidence (e.g., review mining upgrades a key claim)
- **Patch** (1.0.X): Fixes, clarifications, dialogue-driven corrections that don't change substance

**Each revision entry:**
```json
{
  "version": "1.0.0",
  "date": "YYYY-MM-DD",
  "actor": "who",
  "change_type": "initial_workshop | evidence_upgrade | re_workshop | correction",
  "protocol_used": "TWP-001 vX.Y.Z",
  "what_changed": "description",
  "quality_score": 8.0,
  "quality_rationale": "why this score",
  "dialogue_ref": {
    "file": "dialogue_summary.md",
    "tup_version": "1.0.0",
    "personas": [],
    "rounds": 6,
    "saturated": true,
    "upgrades": 3,
    "unresolved": 0
  },
  "hypotheses_affected": ["HYP-NNN"]
}
```

**Key rule:** The `dialogue_ref.tup_version` field ties each persona dialogue to the specific version of the TUP it stress-tested. When a TUP is re-workshopped, a new dialogue runs against the new version.

**Required _meta.json fields:** `tup_id`, `tup_name`, `cluster`, `cluster_name`, `status`, `revisions[]`, `current_version`, `current_quality`, `sheet_count`, `sheets`, `files`, `opkits`, `feeds_into`, `requires`, `key_blockers`, `next_action`, `intelligence_gaps`

---

### PHASE 10: HYPOTHESIS CROSS-REFERENCE

Check if content affects business hypotheses.

**Actions:**
1. Review content for claims relating to hypotheses in `data/hypotheses/registry.json`
2. If evidence found, add to `data/hypotheses/validation_log.json`
3. Update `data/hypotheses/index.json` with new links
4. If no hypothesis relevance, note "No hypothesis impact" and move on

---

### PHASE 11: SESSION LOG

Record what was done in `SESSION_LOG.md`.

---

## Interrupt Handling

Borrowed from `ci-protocol/00_INDEX.md`:

| Type | When | Action | Blocking? |
|------|------|--------|-----------|
| **(a) Blocked source** | Can't access data | Mark D-grade, add upgrade path, continue | No |
| **(b) Large discrepancy** | Finding contradicts expectations | Pause, present to user, wait | Yes |
| **(c) Qualitative judgment** | Requires human interpretation | Pause, present options, wait | Yes |
| **(d) Strategic decision** | Requires human strategic call | Pause, present analysis, wait | Yes |
| **Scoping checkpoint** | Phase 3 | Ask clarifying questions | Yes |
| **Surprise** | Unexpected finding during research | Present to user, ask questions | Yes |

---

## Quality Gates

A TUP workshop is **complete** when:

- [ ] All content tabs either filled or marked `[VOID — requires: {what}]`
- [ ] Expert persona dialogue run to saturation (or hard stop)
- [ ] Self-grade completed honestly
- [ ] At least 1 OpKit registered in `data/opkits/registry.json`
- [ ] `_meta.json` created in `data/m{N}/`
- [ ] `manifest.json` updated (status: migrated)
- [ ] `TUP_Workshop_Tracker.md` updated (status: DONE)
- [ ] Hypothesis cross-reference checked
- [ ] Session log entry created

---

## Scaling Notes

**S-effort TUPs (≤6 tabs):** Phases 4-6 are compressed. Research may be a quick industry scan. Persona dialogue may saturate in 2-3 rounds. Expect ~30-45 min.

**M-effort TUPs (8-15 tabs):** Full protocol. Phase 5 is the bulk. Expect ~1-2 hrs.

**L/XL-effort TUPs (15+ tabs):** Phase 5 should be broken into sub-sessions with intermediate checkpoints. Consider running persona dialogue per content group rather than waiting until all tabs are filled. Expect multiple hours.

**Batch processing:** When workshopping multiple S-effort TUPs in one session, Phases 1-2 can be parallelized.

---

## Relationship to CI Protocol

The `ci-protocol/` directory contains the **first worked example** of this general methodology, applied specifically to competitive intelligence analysis. It remains as reference material and a graded example:

| CI Protocol File | TWP Phase | Relationship |
|-----------------|-----------|-------------|
| `00_INDEX.md` | Overall | Event-driven routing pattern (generalized here) |
| `01_SCOPING_CHECKPOINT.md` | Phase 3 | Workshop checkpoint pattern |
| `02_RESEARCH_PHASE.md` | Phase 4 | Source quality hierarchy (adopted verbatim) |
| `03_BENCHMARK_CHECK.md` | Phase 4 | Benchmark validation (domain-specific for CI) |
| `04_PERSONA_DIALOGUE.md` | Phase 6 | Dialogue + saturation framework (generalized here) |
| `05_ASSEMBLY.md` | Phase 5 | Deliverable structure (domain-specific for CI) |
| `06_SELF_GRADE.md` | Phase 7 | Self-grade rubric (generalized here) |
| `07_FRAMEWORKS.md` | Phase 6 | Expert frameworks (domain-specific for CI; each TUP gets its own) |

The CI protocol files are not deprecated — they're the OpKit for competitive intelligence (M26). This TWP is the meta-protocol that all TUP-specific OpKits follow.

---

## Related Documents

| Document | Relationship |
|----------|-------------|
| `tracking/TUP_Workshop_Tracker.md` | Queue management and progress tracking |
| `processes/JSON_Migration_Guide.md` | Technical JSON structure reference (Phase 5 output format) |
| `ci-protocol/` | First worked example of this methodology (competitive intelligence) |
| `data/opkits/registry.json` | OpKit registration target (Phase 8) |
| `data/manifest.json` | TUP metadata target (Phase 9) |
| `data/hypotheses/registry.json` | Hypothesis cross-reference (Phase 10) |
| `standards/Deliverable_Structure_Standards.md` | Quality standards for content |
| `protocols/CSP-001_Constraint_Scenario_Protocol.md` | Can stress-test hypotheses surfaced during workshop |
| `core/04_Working_Principles_updated.md` | Core quality philosophy |

---

## Change Log

| Date | Version | Change |
|------|---------|--------|
| 2026-02-06 | 2.0.0 | Major rewrite: absorbed CI protocol methodology (source hierarchy, persona dialogue, saturation framework, self-grade rubric), added domain-specific persona roster, added state tracker, added interrupt handling, added scaling notes, established CI protocol as worked example |
| 2026-02-06 | 1.0.0 | Initial protocol created |
