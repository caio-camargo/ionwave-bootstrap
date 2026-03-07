# Project Nerve Center
**Version**: 1.0.0
**Author**: Caio, Claude (collaborative)
**Date Created**: 2026-03-07
**AI Model**: claude-opus-4-6
**Purpose**: Single aggregated view of everything that could fall through the cracks — open decisions, pre-launch blockers, intelligence gaps, data discrepancies, and stale items
**Status**: Active
**Related Files**: manifest.json, SESSION_LOG.md, Open_Questions.md, TUP_Workshop_Tracker.md, Reconciliation_Decision_Log.md

---

**This document exists because the project is too large for any one person to hold in their head.** It aggregates state that is otherwise scattered across 100+ files, 45 tracking logs, and 30+ session log entries. It answers one question: **what needs attention right now?**

**How to use**: Scan Section 1 (decisions) and Section 2 (pre-launch blockers) at the start of every session. Everything else is reference.

**Maintenance**: Update this document whenever a decision is resolved, a blocker is cleared, or a discrepancy is fixed. This is a live document, not versioned.

---

## Table of Contents

1. [Open Decisions Register](#1-open-decisions-register)
2. [Pre-Launch Critical Path](#2-pre-launch-critical-path)
3. [Intelligence Gap Summary](#3-intelligence-gap-summary)
4. [Data Integrity Issues](#4-data-integrity-issues)
5. [Stale Items Sweep](#5-stale-items-sweep)
6. [Project Status Summary](#6-project-status-summary)
7. [Dependency Map](#7-dependency-map)

---

## 1. Open Decisions Register

**Every decision waiting on human input, aggregated from all sources.**

### CRITICAL — Blocks Multiple Work Streams

| # | ID | Decision | Owner | First Raised | Source | What It Blocks |
|---|-----|----------|-------|-------------|--------|----------------|
| 1 | Q1 / REC-001 | **Gross margin: 40% (Danilo) vs 67% (Bootstrap).** Root cause identified as definitional (product GM vs fully-loaded GM). M3 uses 60% working baseline. Needs final lock pending: (1) fulfillment strategy, (2) shipping absorption policy, (3) return rate confirmation. | Danilo | 2026-02-02 | Open_Questions, Reconciliation_Decision_Log, 7+ sessions | M3 Financial Model lock, M11/M13 break-even CPA, M25 dual-margin treatment, investor pitch margin claims. $88K Y1 swing. |
| 2 | Q9 | **Positioning-economics tension.** Marine plasma positioning appeals to $300K-$1.5M sub-segment, but $30K MRR requires drawing from $1.5B electrolyte market. Which positioning? | Danilo | 2026-02-04 | Open_Questions | Product Strategy, Brand Messaging, Creative Strategy, Investor Narrative coherence. |
| 3 | Q10 / Q11 | **Capital sufficiency + revenue target.** Is $30-50K raise enough? Is $30K MRR in 12 months realistic, or should target be $15K/12mo or $30K/18mo? | Danilo + Caio | 2026-02-05 | Open_Questions | Fundraising (M4), Financial Model (M3), all downstream planning. |
| 4 | M2-DEC | **Founder equity split** — undecided. Blocks cap table, first SAFE, entity formation. | Danilo | M2 workshop | M2 _meta.json | Entity formation, fundraising, all equity-based compensation. |
| 5 | M2-DEC | **Studio 4 holding company vs standalone** — must decide before first SAFE. | Danilo | M2 workshop | M2 _meta.json | Entity structure, cap table, investor legal docs. |
| 6 | DEC-CHAIN-003 | **Approval authority at cascade handoffs** — fully autonomous / Claude-assisted / Caio backstop / VP-only gate. Flagged as "most critical open decision." | Danilo + Caio | 2026-02-27 | chain_specification.md | Rollout recruiting cascade activation. Quality control model for entire chain. |
| 7 | DEC-CHAIN-007 | **Pre-entity equity instruments** — how to commit equity (SAFE / convertible / promise letter / deferred grant) before legal entity exists. | Danilo + Legal | 2026-02-27 | chain_specification.md | MBA and VP compensation, rollout cascade activation. |

### HIGH — Blocks Specific Areas

| # | ID | Decision | Owner | First Raised | Source | What It Blocks |
|---|-----|----------|-------|-------------|--------|----------------|
| 8 | Q2 | Single SKU or multiple flavors at launch? | Danilo | 2026-02-04 | Open_Questions | Inventory, unit economics, creative strategy, production complexity. |
| 9 | Q3 | DTC-only or retail partnership at launch? | Danilo | 2026-02-04 | Open_Questions | Pricing, unit economics, packaging, cash flow. |
| 10 | DEC-2026-02-17-002 | **Canonical home: GitHub vs Google Drive vs Hybrid** — 59 files uncommitted. | Caio + Danilo | 2026-02-17 | Decision_Log | Monitoring/automation system, all future workflow. |
| 11 | DEC-2026-02-17-003 | **Monitoring system architecture: GitHub Actions vs Apps Script** — blocked by canonical home decision. | Caio | 2026-02-17 | Decision_Log | Automated reviews (WBR, MBR, parameter checks). |
| 12 | DEC-CHAIN-005 | VA budget amount (cash, amount TBD). | Danilo | 2026-02-27 | chain_specification.md | VA hiring, cascade activation. |
| 13 | DEC-CHAIN-004 | Chain parallelization — sequential vs overlapping allowed. | Danilo | 2026-02-27 | chain_specification.md | Timeline: 4-6 months (parallel) vs 6-9 months (sequential). |
| 14 | DEC-CHAIN-006 | Fallback at MBA-to-VP link failure. | Danilo | 2026-02-27 | chain_specification.md | Risk mitigation for hardest cascade link. |
| 15 | CM-DEC | CM authority model activation threshold — at what MRR/complexity? | Danilo | 2026-02-17 | M36 session | Governance model scaling. |

### MEDIUM — Partially Resolved or Deferrable

| # | ID | Decision | Owner | Status |
|---|-----|----------|-------|--------|
| 16 | Q4 | Subscription incentive: discount % or free shipping? | Offer Strategy | NEEDS TESTING |
| 17 | Q6 | Influencer strategy: macro (100K+) or micro (10K-50K)? | Marketing | NEEDS ANALYSIS |
| 18 | DEC-CHAIN-001 | MBA equity amount (type resolved as equity, amount TBD). | Danilo | PARTIALLY RESOLVED |
| 19 | DEC-CHAIN-002 | VP equity amount (5-10% confirmed, exact TBD). | Danilo | PARTIALLY RESOLVED |
| 20 | ISS-001 | HYP-004 target revision: 67% GM structurally unachievable with subscription discount. Recommended 62-64%. | Caio + Danilo | NEEDS CONFIRMATION |

### DEFERRED

| # | ID | Decision | Notes |
|---|-----|----------|-------|
| 21 | Q5 | Content marketing strategy role in acquisition. | Lower priority than paid channels. |
| 22 | Q7 | International shipping at launch or US-only. | Enable post-launch. |
| 23 | Q8 | SMS cadence/aggressiveness. | Post-launch, based on email engagement data. |
| 24 | M37 | AI & Automation TUP — when to revisit. | Deferred until 10+ sessions of operational practice. |

---

## 2. Pre-Launch Critical Path

**Everything that must happen before you can sell a product, pulled from all TUPs.**

### LEGAL & COMPLIANCE (Must complete — regulatory risk)

| # | Item | TUP Source | Effort | Cost | Status |
|---|------|-----------|--------|------|--------|
| 1 | **Pre-launch attorney review** of all marketing (labels, website, VSL, ads, emails) | M7 | External | $5K-$10K | NOT STARTED |
| 2 | **Fix M11 VSL FTC violations** — 7 violations, $420K-$2M exposure. P0 corrections. | M7, M11 | 4 hours | $0 | NOT STARTED |
| 3 | **Replace fictional testimonials** (Marcus, Jennifer, David) with real reviews or remove | M7, M11, M15 | 2 hours | $0 | NOT STARTED |
| 4 | **FDA Structure/Function Notification** — file within 30 days of first sale | M7 | 1 hour | $0 | NOT STARTED |
| 5 | **Adverse event reporting system** — serious AEs to FDA within 15 business days, train CS | M7, M20 | 4 hours | $0 | NOT STARTED |
| 6 | **Trademark clearance for "IonWave"** — USPTO search + attorney | M8 | External | $1-2K | NOT STARTED |
| 7 | **Prop 65 heavy metal testing** — cannot sell in California without testing or warning | M5, M8, M15 | External | $500-2K | NOT STARTED |
| 8 | **Founder equity split + entity formation** — blocks first SAFE, cap table, all contracts | M2 | Decision | — | BLOCKED on Decision #4 |

### SUPPLIER & PRODUCT (Must complete — no product without these)

| # | Item | TUP Source | Effort | Cost | Status |
|---|------|-----------|--------|------|--------|
| 9 | **Supplier outreach** to Biocean/Actimar/Quinton for CoAs, pricing, MOQ, lead times | M5, M6 | 5-10 hours | $0 | NOT STARTED — all supplier data is [VOID] |
| 10 | **Lab-verified Supplement Facts Panel** — FDA requirement for packaging | M5, M8 | External | $500-2K | NOT STARTED — requires CoA from #9 |
| 11 | **COGS validation** — actual supplier quotes needed to lock pricing model | M3, M6, M10, M25 | Requires #9 | — | BLOCKED on supplier outreach |
| 12 | **Taste testing** with 50-100 users (Week 3-4 after supplier engagement) | M5 | 2-4 weeks | $500-1K | BLOCKED on #9 |

### BRAND & CREATIVE (Must complete — cannot build website/ads without these)

| # | Item | TUP Source | Effort | Cost | Status |
|---|------|-----------|--------|------|--------|
| 13 | **Logo design** — cannot launch without brand mark | M8 | External | $500-2K | NOT STARTED |
| 14 | **Photography / photoshoot** — needed for website, ads, packaging, social | M8 | External | $3-5K | NOT STARTED |
| 15 | **Domain acquisition** — ionwave.com or fallback | M8 | 1 hour | $10-5K | NOT STARTED |

### TECH & INTEGRATIONS (Must verify)

| # | Item | TUP Source | Effort | Status |
|---|------|-----------|--------|--------|
| 16 | **Loop Subscriptions + Smile.io/ReferralCandy integration** — verify before committing | M22 | 2-4 hours | NOT VERIFIED |
| 17 | **Synder vs A2X connector** — test with ReCharge sample transactions | M25 | 2-4 hours | NOT TESTED |

### FINANCIAL (Must resolve)

| # | Item | TUP Source | Effort | Status |
|---|------|-----------|--------|--------|
| 18 | **Lock gross margin** — REC-001 resolution (see Decision #1) | M3 | Decision | BLOCKED |
| 19 | **3PL fulfillment cost quotes** | M24, M25 | External | NOT STARTED |
| 20 | **Bioavailability claim decision** — commission RCT ($50-200K) OR pivot all claims to structure/function language | M5, M7, M11 | Decision by Month 6 | DEFERRED — can launch with structure/function language |

### ESTIMATED PRE-LAUNCH COST SUMMARY

| Category | Low Estimate | High Estimate |
|----------|-------------|---------------|
| Attorney review | $5,000 | $10,000 |
| Trademark | $1,000 | $2,000 |
| Prop 65 testing | $500 | $2,000 |
| Lab / Supplement Facts | $500 | $2,000 |
| Logo | $500 | $2,000 |
| Photography | $3,000 | $5,000 |
| Domain | $10 | $5,000 |
| Taste testing | $500 | $1,000 |
| **TOTAL** | **$11,010** | **$29,000** |

---

## 3. Intelligence Gap Summary

**Aggregated from 33 workshopped TUPs. Total: ~180 intelligence gaps across all TUPs.**

### Gaps by Count (Top 10 TUPs)

| TUP | Gap Count | Quality | Key Theme |
|-----|-----------|---------|-----------|
| M8 Brand Identity | 14 | 7.8 | Creative assets (logo, photos, domain) all VOID |
| M35 Execution Plans | 13 | 8.2 | All execution timing is pre-launch estimate (C/D) |
| M2 Entity & Legal | 9 | 8.2 | Equity split, Studio 4 structure, attorney review |
| M19 Customer Lifecycle | 8 | 8.4 | CRM model untested, churn formula unvalidated |
| M28 Market Expansion | 8 | 8.3 | COGS, science citations, subscription conversion unknown |
| M31 Hiring | 8 | 8.0 | All hiring timing C/D-grade (pre-launch) |
| M20 Customer Support | 7 | 8.6 | Adverse event protocol, support volume unknown |
| M39 Philosophical | 7 | 7.5 | All protocols untested, advisor procurement blocked |
| M15 Landing Pages | 6 | 8.2 | Conversion rates unknown until launch |
| M5 Formulation | 6 | 8.5 | Supplier CoA, taste, bioavailability, stability all VOID |

### Gap Categories

**Can validate BEFORE launch (human action needed now):**
- All supplier data — CoA, pricing, MOQ, lead times (M5, M6, M8)
- FTC compliance corrections on M11/M15 (4 hours, $0)
- Legal entity formation (M2 — blocked on equity decision)
- Logo, photography, domain, trademark (M8)
- Integration verification — Loop+Smile.io, Synder/A2X (M22, M25)
- 3PL quotes (M24, M25)

**Validates WITH launch execution (Week 1-12 actuals):**
- CAC for IonWave (M13 — placeholder benchmarks)
- Creative fatigue timeline (M12 — industry 2-4 week standard)
- Platform-specific ROAS (M13)
- Subscription conversion rate (M21, M28)
- Support volume and churn rate (M19, M20)
- Solo founder capacity / time budget (M35, M36)
- WBR efficacy for solo founder (M35)

**Cannot validate past C/D grade (structural uncertainty):**
- Market saturation (HYP-006 dependency, mitigated by M28 expansion triggers)
- Solo founder burnout (individual psychology, mitigated by Day 180 capacity gate)
- Bioavailability advantage of ocean vs synthetic minerals (requires RCT, $50-150K)

---

## 4. Data Integrity Issues

**Discrepancies between manifest.json, TUP_Workshop_Tracker.md, and _meta.json files.**

### Manifest Header Count Errors

| Field | Claims | Actual | Action |
|-------|--------|--------|--------|
| `migrated_tups` | 29 | 33 migrated + 1 workshopped = 34 done | Update header |
| `migration_metadata.migrated_tup_count` | 13 | 33 | Severely stale — reflects early February |
| `migration_metadata.pending_tup_count` | 25 | 7 | Severely stale |
| `migration_metadata.last_migration_event` | 2026-02-08 | Should be ≥ 2026-02-17 | Update |

### Status Discrepancies

| TUP | Manifest | Tracker | Issue |
|-----|----------|---------|-------|
| **M10** | `workshopped` | DONE (7.4/10) | Manifest never updated to `migrated` |
| **M12** | `not_migrated` (stub) | DONE (8.2/10) | **Critical**: fully workshopped but manifest is a bare stub — no quality, no dependencies, no metadata |
| M32, M33, M37 | `not_migrated` | DEFERRED | Manifest has no `deferred` status concept |

### Missing Dependency Data (Workshopped TUPs with empty feeds_into/requires in manifest)

| TUP | Status | Problem |
|-----|--------|---------|
| M19 (Customer Lifecycle) | migrated | Missing dependency data in manifest |
| M30 (Analytics) | migrated | Missing dependency data in manifest |
| M31 (Hiring) | migrated | Missing dependency data in manifest |
| M36 (Operational Infra) | migrated | Missing dependency data in manifest |

### Quality Score Format Inconsistency

Some TUPs store quality as `"8.2/10"` (string), others as `8.2` (number). Affects: M28, M30, M35, M36.

### ACTIVE_WORK.md Stale Claim

A claim from **2026-03-01** (Claude session: Rollout hypotheses & risk analysis) was never cleared. Files listed at risk: `registry.json`, `validation_log.json`, `index.json`, `Rollout_Risk_Analysis.md`.

---

## 5. Stale Items Sweep

**Items open since early February that need resolution or explicit deferral.**

| Item | Open Since | Age (days) | Status | Recommendation |
|------|-----------|------------|--------|----------------|
| REC-001 gross margin dispute | 2026-02-02 | 33 | Workaround in place (dual-margin) | **Resolve or formally accept dual-margin as permanent treatment** |
| Q9 positioning-economics tension | 2026-02-04 | 31 | ACTIVE | **Decide: this affects all marketing work** |
| Q10 capital sufficiency | 2026-02-05 | 30 | Analyzed but not decided | **Decide or defer with documented rationale** |
| Q11 financial model validation | 2026-02-05 | 30 | Analyzed but not decided | **Same — $30K MRR target drives everything downstream** |
| README.md review | 2026-02-03 | 32 | Flagged, never done | Low priority — do when convenient |
| 01_Studio3_Context.md missing | 2026-02-03 | 32 | Flagged, never created | Low priority — decide if actually needed |
| REC-002a-f implementation debt | 2026-02-05 | 30 | Decided, not built | Implement when doing systems architecture work |
| DOCUMENTATION_INDEX.md stale paths | 2026-02-04 | 31 | References old paths (data/01_strategic_foundation/) | **Fix: paths changed during TUP migration** |
| ACTIVE_WORK.md stale claim | 2026-03-01 | 6 | Never cleared | **Clear now** |

---

## 6. Project Status Summary

### Cluster Completion

| Cluster | Status | Done | Remaining | Notes |
|---------|--------|------|-----------|-------|
| BCL-1 Product & Science | **COMPLETE** | 4/4 | — | M5, M6, M7, M8 |
| BCL-2 Money & Legal | **COMPLETE** | 4/4 | — | M2, M3, M4, M25. REC-001 margin unresolved. |
| BCL-3 DR & Creative | **COMPLETE** | 5/5 | — | M11, M12, M13, M14, M15 |
| BCL-4 Retention & Lifecycle | **COMPLETE** | 6/6 | — | M17-M22 |
| BCL-5 Growth & Market | **COMPLETE** | 7/7 | — | M10, M16, M23, M26-M29 |
| BCL-6 Operations & Infra | 7/8 (87.5%) | 7 | M37 (deferred) | M1, M9, M24, M30, M31, M35, M36 done |
| BCL-0 Thesis & Meta | 2/5 (40%) | 2 | M34, M38, M40 | M0, M39 done. M38 is XL (44 tabs). |
| BCL-7 Governance & School | DEFERRED | 0/2 | M32, M33 | By decision |
| **TOTAL** | | **35/41** | **3 active + 3 deferred** | |

### Quality Distribution (33 TUPs with scores)

| Range | Count | TUPs |
|-------|-------|------|
| 9.0+ | 1 | M11 (9.2) |
| 8.5-8.9 | 6 | M7 (8.7), M18 (8.7), M20 (8.6), M1 (8.6), M5 (8.5), M9 (8.5) |
| 8.0-8.4 | 16 | M25, M16, M17, M19, M6, M24, M28, M4, M30, M10, M3, M2, M12, M14, M15, M35 |
| 7.5-7.9 | 3 | M8 (7.8), M29 (7.6), M39 (7.5) |
| 7.0-7.4 | 2 | M10 (7.4), M22 (7.0) |
| Below 7.0 | 3 | M0 (6.5), M27 (6.5), M26 (5.5) |
| **Average** | | **~8.0/10** |

### Remaining Work Estimate

| Item | Estimate |
|------|----------|
| M34 Trade Architecture (L) | ~3-4 hours |
| M38 Strategic Frameworks (XL) | ~5-6 hours |
| M40 Navigation & Command (L) | ~3-4 hours |
| **Total workshop time remaining** | **~11-14 hours** |
| Manifest/tracker cleanup | ~1-2 hours |
| Pre-launch human tasks (supplier outreach, legal, creative) | 20-40 hours + external vendors |

---

## 7. Dependency Map

**Cross-TUP dependencies extracted from _meta.json files. Arrow = "feeds into".**

### Core Foundation Layer (everything depends on these)
```
M0 (Trade Thesis) → M2, M5, M6, M8, M10, M11, M12, M13, M16, M17, M21, M22, M23, M25, M26, M27, M29, M31, M35, M36
```
M0 is the most depended-upon TUP. Its quality (6.5/10) is the lowest of any foundation document.

### Product → Compliance → Creative Chain
```
M5 (Formulation) → M6 (Supply Chain) → M24 (Fulfillment)
M5 → M7 (Regulatory) → M11 (VSL), M15 (Landing Pages), M14 (Testing)
M5 → M8 (Brand) → M11, M12 (Ad Creative), M15, M23 (Influencer), M29 (PR)
```

### Financial Chain
```
M2 (Entity) → M3 (Financial Model) → M4 (Fundraising) → M2 (circular: cap table)
M5, M6, M10, M13, M19, M21, M24, M25, M30 → M3 (many inputs to financial model)
M3 → M0 (Trade Thesis), M4 (Fundraising), M25 (Financial Ops), M30 (Analytics)
```

### Retention & Growth Chain
```
M17 (Email) → M18 (Lifecycle Flows) → M19 (CRM) → M20 (Support)
M19 → M21 (Subscriptions), M25 (Financial Ops), M27 (Customer Research)
M16 (Content) → M12, M13, M14, M17, M22, M23
```

### Operational Chain
```
M35 (Execution Plans) → M40 (Navigation), all operational TUPs
M36 (Operational Infra) → M9, M25, M30, M31
M31 (Hiring) → all TUPs requiring human labor
```

### Critical Path to Launch
```
Decision: Equity split (M2) → Entity formation → First SAFE → Capital
Supplier outreach → CoA → Supplement Facts Panel → Packaging → Launch
Logo + Photography → Website + Ads → Launch
Attorney review → Compliant VSL/Landing Pages → Launch
```

All four chains must complete. The **longest chain** is supplier outreach → CoA → taste testing → packaging → launch (estimated 6-8 weeks from first supplier contact).

---

## Appendix: Implementation Debt (Decided but Not Built)

These reconciliation decisions were made but the corresponding data/architecture changes were never implemented:

| ID | What | Status |
|----|------|--------|
| REC-011 | Add `passet: imagination` to manifest; add `danilo_tup` + `danilo_cluster` fields; create crosswalk.json | Partially done (crosswalk exists, manifest fields added) |
| REC-002a | Formalize controller layer; reconcile bifurcation parameters with hypothesis kill thresholds | NOT BUILT |
| REC-002b | Formalize 10 PMF signals as individual Metrics; define Observer schema | NOT BUILT |
| REC-002c | Define Controller, Observer, OpKit, Metric schemas; build Claude OpKit navigation | NOT BUILT |
| REC-002d | Register anti-goals as boundary conditions; register temptation triggers as parameters | NOT BUILT |
| REC-002f | Register thesis structure checklist as M0 OpKit; populate from Bootstrap answers | NOT BUILT |

---

*Generated 2026-03-07 by Claude (Opus 4.6) from audit of: SESSION_LOG.md (30+ sessions), manifest.json (41 TUPs), 33 _meta.json files, Open_Questions.md (11 questions), Reconciliation_Decision_Log.md (11 decisions), Decision_Log.md (3 decisions), chain_specification.md (7 decisions), TUP_Workshop_Tracker.md, DOCUMENTATION_INDEX.md.*
