# SESSION LOG
**Purpose**: Persistent record of all changes to the IonWave Bootstrap documentation system
**Scope**: Claude Code sessions + manual changes
**Format**: Reverse chronological (newest first)

---

## How to Use This Log

**Claude Code**: At the start of each session, read the **last 3 entries** for recent context (focus on the most recent Next Steps). Then create a new entry at the top of the log (below this section). Update it as work progresses. Mark it complete at the end. Only read older entries if you need context on a specific past decision.

**Manual changes**: Add an entry using the template below with `Source: Manual` instead of `Source: Claude Code`.

### Entry Template

```
## Session YYYY-MM-DD — [Brief Title]
**Source**: Claude Code | Manual
**User**: [Name — who directed this session]
**AI Model**: [Model used, e.g. claude-sonnet-4-5-20250929, claude-opus-4-6, or N/A for manual]
**Status**: In Progress | Complete

### Summary
[1-3 sentences: what was accomplished and why]

### Decisions Made
- [Key decisions and rationale]

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | [created/moved/edited/archived/deleted] | `filename` | [what changed] |

### Next Steps
- [ ] [Follow-up items identified during this session]
```

**Note:** Session entries use date + title only (no sequence numbers). With multiple operators, sequence numbers collide. Date + title is sufficient for identification.

---

## Session 2026-02-17 — M36 Operational Infrastructure Workshop (Complete)

**Operator**: Caio
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M36 — Operational Infrastructure
**Quality**: 8.1/10
**Status**: Complete

### Summary

Completed M36 Operational Infrastructure workshop (Phases 1-11) following TWP-001 v2.0.0 protocol. Workshop completed 3 content files previously started by another agent (risk_and_continuity, performance_monitoring) plus the OpKit, _meta.json, and all registrations. Key innovation: company-as-a-system with 7 subsystems as the conceptual spine of all M36 content. BCL-6 now 7/8 complete (87.5%).

### Decisions Made
- CM authority model documented as two explicit variants (Solo Founder vs CM Model) — activation threshold DECISION TBD
- Phase 1/Phase 2 monitoring architecture: Phase 1 (manual, repo-based) active now; Phase 2 blocked on DEC-2026-02-17-003
- Risk register: R001 (supplier) correctly elevated to CRITICAL (L×I = 3×5 = 15)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created |  | 548 lines. R001-R006 risk register, 6 contingency playbooks, business continuity baseline, pre-launch checklist |
| 2 | created |  | 406 lines. 5 operating parameters (CAC <0, ROAS >2.0x, Safety Stock 14d, SLA <4hr, Test 00), 4-cadence review, Phase 1/2 architecture |
| 3 | created |  | 439 lines. 8 components: company-as-a-system, operating parameters, decision authority, risk register template, monitoring, knowledge management, capabilities maturity, continuity checklist |
| 4 | created |  | Full metadata with quality assessment, intelligence gaps, decision TBDs, feeds_into, requires |
| 5 | updated |  | M36 registered (migrated), migrated_tups 28→29 |
| 6 | updated |  | OK-M36-001 added to unmapped_tups.m36 |
| 7 | updated |  | M36 DONE, count 34→35, BCL-6 6/8→7/8 |
| 8 | updated |  | M36 claim cleared |

### Next Steps
- [ ] Expert review of risk register with Danilo (especially R001 supplier and R005 key person insurance)
- [ ] Decision: CM authority model activation threshold (at what MRR/complexity?)
- [ ] Decision: DEC-2026-02-17-003 — Phase 2 monitoring system architecture (GitHub Actions vs Apps Script)
- [ ] Key person insurance: define coverage amount and provider before launch

## Session 2026-02-16 — M31 Hiring Workshop (Complete 11 Phases)

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M31 — Hiring
**Quality**: 8.0/10
**Status**: Complete

### Summary

Completed M31 Hiring workshop (Phases 1-11) following TWP-001 v2.0.0 protocol. Green-field build from 31 Danilo tabs (640-670, 617 rows). Consolidated into 8 files (~2,400 lines): hiring_strategy, hiring_processes, job_specifications, compensation_framework, industry_perspectives, dialogue_summary, quality_assessment, workshop_summary. Registered in manifest.json, opkits/registry.json, TUP_Workshop_Tracker.md. **BCL-6 now 6/8 complete (75%)**.

**Key Innovations**: PM Competence Framework (18-question scorecard >60 before ad spend), operator equity 10-25%, 3-4 PM maximum constraint, pipeline-building 4-6 weeks early, hybrid creative sprint model, community engagement sourcing.

### Actions Taken

| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1-8 | Created | `data/m31/*.md` | 8 content files (~2,400 lines) |
| 9 | Created | `data/m31/_meta.json` | Workshop metadata, quality 8.0/10 |
| 10 | Created | `data/opkits/OK-M31-001_Hiring_Framework.md` | 14-step OpKit |
| 11 | Updated | `data/manifest.json` | M31 migrated, count 27→28 |
| 12 | Updated | `tracking/TUP_Workshop_Tracker.md` | 33→34 done, BCL-6 6/8 |
| 13 | Created | `SESSION_LOG.md` | This entry |

### Next Steps

- [ ] Month 1-2: Post operator role, build pipeline
- [ ] Operator Day 1: PM Competence >60 before ad spend
- [ ] Month 3-4: Hire Creative PM if $15-25K MRR
- [ ] Maintain 3-4 PM maximum constraint

---

## Session 2026-02-17 — M36 Operational Infrastructure Workshop (Complete)

**Operator**: Caio
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M36 — Operational Infrastructure
**Quality**: 8.1/10
**Status**: Complete

### Summary

Completed M36 Operational Infrastructure workshop (Phases 1-11) following TWP-001 v2.0.0 protocol. Workshop completed 3 content files previously started by another agent (risk_and_continuity, performance_monitoring) plus the OpKit, _meta.json, and all registrations. Key innovation: company-as-a-system with 7 subsystems as the conceptual spine of all M36 content. BCL-6 now 7/8 complete (87.5%).

### Decisions Made
- CM authority model documented as two explicit variants (Solo Founder vs CM Model) — activation threshold DECISION TBD
- Phase 1/Phase 2 monitoring architecture: Phase 1 (manual, repo-based) active now; Phase 2 blocked on DEC-2026-02-17-003
- Risk register: R001 (supplier) correctly elevated to CRITICAL (L×I = 3×5 = 15)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created |  | 548 lines. R001-R006 risk register, 6 contingency playbooks, business continuity baseline, pre-launch checklist |
| 2 | created |  | 406 lines. 5 operating parameters (CAC <0, ROAS >2.0x, Safety Stock 14d, SLA <4hr, Test 00), 4-cadence review, Phase 1/2 architecture |
| 3 | created |  | 439 lines. 8 components: company-as-a-system, operating parameters, decision authority, risk register template, monitoring, knowledge management, capabilities maturity, continuity checklist |
| 4 | created |  | Full metadata with quality assessment, intelligence gaps, decision TBDs, feeds_into, requires |
| 5 | updated |  | M36 registered (migrated), migrated_tups 28→29 |
| 6 | updated |  | OK-M36-001 added to unmapped_tups.m36 |
| 7 | updated |  | M36 DONE, count 34→35, BCL-6 6/8→7/8 |
| 8 | updated |  | M36 claim cleared |

### Next Steps
- [ ] Expert review of risk register with Danilo (especially R001 supplier and R005 key person insurance)
- [ ] Decision: CM authority model activation threshold (at what MRR/complexity?)
- [ ] Decision: DEC-2026-02-17-003 — Phase 2 monitoring system architecture (GitHub Actions vs Apps Script)
- [ ] Key person insurance: define coverage amount and provider before launch

## Session 2026-02-16 — M35 Execution Plans Registration (Phases 9-11)

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0 (Phases 9-11 only)
**TUP**: M35 — Execution Plans & Rhythms
**Quality**: 8.2/10
**Status**: Complete

### Summary

Completed M35 Execution Plans registration (Phases 9-11) following TWP-001 v2.0.0 protocol. M35 content was already produced on 2026-02-15 (Phases 1-8 complete: 25 Danilo tabs consolidated into 5 core content files + industry perspectives + dialogue + quality assessment + OpKit, totaling ~3,900 lines). This session completed final registration phases: verified content completeness, updated manifest.json (status → migrated, quality 8.2/10, full metadata), registered OK-M35-001 in opkits/registry.json, updated TUP_Workshop_Tracker.md (32→33 TUPs, BCL-6 now 5/8 at 63%), documented hypothesis cross-references (HYP-001, HYP-003, HYP-004, HYP-006), and created SESSION_LOG entry.

**Key Context**: M35 Execution Plans is a green-field build (Bootstrap files 04/28/31 archived, no usable sources). 25 Danilo tabs (773-797, 801) covering 30/90/365-day plans, operating rhythms (Amazon WBR-inspired), meeting cadences, SOPs, and phase checklists. All industry research A-grade (Amazon WBR structure, First Round PMF levels framework, D2C 2026 execution trends). IonWave-specific adaptation C/D-grade (pre-launch assumptions). 6 dialogue rounds with 8 upgrades applied. 2 unresolved gaps flagged (solo founder burnout, market saturation). OpKit: OK-M35-001 Execution Planning Framework (universal, production maturity, high reusability).

### Decisions Made

- **M35 registered as migrated** in manifest.json with quality 8.2/10, status "migrated", 25 Danilo tabs → 5 core content files + 4 supporting files
- **OK-M35-001 registered** in opkits/registry.json: "Execution Planning Framework" with 12-step universal process, production maturity, high reusability
- **BCL-6 cluster progress updated**: 5/8 complete (63%) — M1/M9/M24/M30/M35 done, M31/M36 remaining (M37 deferred)
- **Hypotheses cross-referenced**: HYP-001 (Team Velocity via operating rhythms), HYP-003 (Churn via PMF gates), HYP-004 (Margin via financial close SOP), HYP-006 (Differentiation via market saturation gap)
- **Novel innovations documented**: Choreography framework (feed-forward loops), phase-gated strictness (objective LTV:CAC >3.0, NPS >40%, churn <15%), crisis mode protocol (circuit breaker pauses loops), hour-by-hour Week 1 Day-by-Day granularity, kill discipline (WBR forcing function), pre-launch supplier work (Week -2 CoA requests), dual LTV gate (LTV:CAC + Month 3 retention >60%)
- **13 intelligence gaps flagged**: All IonWave-specific execution content C/D-grade (pre-launch). Upgrade paths documented for 11 gaps (actuals Week 1-180). 2 gaps unresolvable (burnout D-grade individual psychology, market saturation C-grade HYP-006 dependency)
- **Key blockers**: NONE. All critical path items have fallback plans documented

### Actions Taken

| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Verified | `data/m35/*.md`, `data/m35/_meta.json` | Content completeness check: 9 files present (~3,900 lines), quality 8.2/10, all Phases 1-8 complete |
| 2 | Updated | `data/manifest.json` | M35 entry: status "not_migrated" → "migrated", added full metadata (version 1.0.0, quality 8.2, workshopped_date 2026-02-15, protocol TWP-001 v2.0.0, 25 Danilo sheets, 9 output files, consolidation note, opkits OK-M35-001, hypothesis_links, feeds_into, requires, key_concepts, 13 intelligence_gaps, key_blockers, next_action, danilo_source_note) |
| 3 | Updated | `data/manifest.json` | migrated_tups count: 26 → 27, last_updated: 2026-02-11 → 2026-02-16 |
| 4 | Registered | `data/opkits/registry.json` | OK-M35-001 entry: name "Execution Planning Framework", type production, maturity production, reusability high, 6 components (30/90/365 plans, operating rhythms, phase checklists, meeting templates, detailed timelines, industry perspectives), 12-step instructions, graded example IonWave 8.2/10, workshop notes (8 upgrades, 2 unresolved gaps, novel innovations) |
| 5 | Updated | `tracking/TUP_Workshop_Tracker.md` | Workshopped count: 32 → 33, Remaining: 9 → 8, BCL-6 section: 4/8 → 5/8 (63%), M35 row: NOT STARTED → DONE (8.2/10) with full workshop notes, Summary scoreboard: BCL-6 4→5 done, 4→3 remaining, ~15→~11 hrs, TOTAL 31→33 done, 10→8 active |
| 6 | Created | `SESSION_LOG.md` | This entry documenting M35 Phases 9-11 registration completion |

### Workshop Stats (from 2026-02-15 session)

- **Total content lines**: ~3,900 (across 9 files)
- **Dialogue rounds**: 6 (to saturation)
- **Upgrades applied**: 8 (CAC phasing, supplier pre-work, MBR scaling, dual LTV gate, 3PL timing, kill discipline, crisis mode, hour-by-hour Week 1)
- **Unresolved gaps**: 2 (solo founder burnout D-grade, market saturation C-grade)
- **OpKits created**: 1 (OK-M35-001, production maturity, high reusability)
- **Quality score**: 8.2/10
- **Evidence grade**: A (industry research), C/D (IonWave adaptation pre-launch)
- **Time investment**: ~4 hours workshop (L-effort TUP) + 20 min registration

### Key Content Highlights

**30/90/365-Day Plans** (339 lines):
- Week 1 Day-by-Day with hour-by-hour granularity (e.g., "9:00-10:00 call lawyer, 10:00-11:00 Mercury application")
- Day 30/90/180 checkpoints with objective kill criteria
- Rolling 30-day lock protocol (lock next 30, flex 31-90, strategic 91-365)

**Operating Rhythms & Loops** (417 lines):
- Choreography framework (daily → weekly → monthly → quarterly feed-forward)
- Amazon WBR-inspired structure (metrics, ROTC, decisions, action items)
- Crisis mode circuit breaker (pause loops when existential blocker hits)
- Phase-gated meeting cadences (solo → team scaling)

**Phase Checklists & SOPs** (458 lines):
- LAUNCH → PMF → SCALE objective gates (LTV:CAC >3.0, NPS >40%, churn <15%, Month 3 retention >60%)
- 5 core SOPs (fulfillment, CX, ad review, financial close, creative production)
- First Round PMF levels framework applied to supplements

**Meeting Templates** (622 lines):
- WBR/MBR/QBR/Daily Standup templates (copy-paste ready)
- Communication norms (async/sync, Slack channels, email SLAs)
- Knowledge management (document storage, decision logging, kill tracking)

**Industry Perspectives** (377 lines):
- Amazon WBR structure (commoncog.com)
- First Round PMF levels (firstround.com/levels)
- D2C 2026 execution trends (Shopify, cascade.app, practicahq.com)
- 3 contrarian takes (choreography underrated, D2C gates stricter than SaaS, loops = insurance against founder blindness)

### Intelligence Gaps Documented (13 total)

**Pre-Launch (C/D-grade, upgrade to B/A with execution)**:
- Solo founder capacity (D) | Supplier CoA lead time (C) | CAC for IonWave (C) | 3PL breakpoint (C) | PMF 40% NPS threshold (C) | LTV:CAC >3.0 sustainability (B) | Meeting time budget (C) | WBR efficacy solo founder (D) | Choreography ROI (D) | Crisis mode necessity (D) | Phase gate strictness (C)

**Structural Limits (Cannot upgrade past C/D)**:
- Market saturation (C-grade, HYP-006 dependency, mitigated by M28 expansion triggers)
- Solo founder burnout (D-grade, individual psychology, mitigated by Day 180 capacity gate)

### Next Steps

- [ ] **Execute Week 1 Day-by-Day** — validate time estimates, supplier CoA timing, founder capacity (upgrade 7 gaps from D to B with Week 1 actuals)
- [ ] **First WBR at Day 7** — validate rhythm efficacy, choreography feed-forward, kill discipline forcing function
- [ ] **Day 30 checkpoint** — CAC validation ($30-60 benchmark), first 10 orders, soft launch learnings
- [ ] **Day 90 LAUNCH → PMF gate decision** — pass/fail/iterate based on objective criteria (LTV:CAC >3.0 AND Month 3 retention >60%)
- [ ] **Month 3 3PL quotes** — validate breakpoint (trigger at 150/month OR founder time >10 hrs/week)
- [ ] **Day 180 PMF validation** — NPS >40%, churn <15%, Month 6 cohort LTV data validates 12-month projection
- [ ] **Extract OpKit learnings** — post-execution, document what worked/failed, upgrade IonWave-specific content from C/D to B/A
- [ ] **Test OpKit with 2nd Trade** — validate reusability, adjust scaffolds based on cross-Trade testing

---

## Session 2026-02-11 — M39 Conceptual & Philosophical Foundations Workshop

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0 (Phases 4-11)
**TUP**: M39 — Conceptual & Philosophical Foundations
**Quality**: 7.5/10 (calibrated from raw 8.0/10)
**Status**: Complete

### Summary

Completed TWP-001 Phases 4-11 for M39, documenting the theoretical foundations (Christopher Alexander, David Bohm, Giulio Tononi, W. Ross Ashby) that generate IonWave's operational protocols. Created 6 content files (~2,450 lines), 1 OpKit (OK-M39-001), conducted 7-round expert dialogue to saturation (12 upgrades applied), and registered M39 in system. This is the 32nd TUP workshopped and 2nd BCL-0 TUP complete (40% cluster progress).

### Key Findings

**Theoretical Convergence**: All four theorists (Alexander, Bohm, Tononi, Ashby) converge on same insight: living systems = high-Φ systems (integrated information) = requisite variety systems = explicate order systems. Theory provides pattern languages that compress complexity.

**Operational Protocols Generated**:
- 75 Questions Protocol (context transfer via structured interrogation)
- 5-6 Bullets Protocol (compress complexity without loss)
- 3-Gate Review Model (parallel validation: Feasibility/Viability/Desirability)
- Virtual Twin Specification (Claude agent with maximal mutual information)
- Verification Strategy (four trust dimensions: Strategic/Domain/Execution/Vibes)
- Pattern Language Application (Alexander methodology → OpKit extraction)

**Novel Concepts**:
- Requisite variety via TUP decomposition (41 TUPs match 41 market complexity dimensions)
- Love as mutual information (high-MI teams have high I(Team Members) = tight coupling)
- Aliveness scoring (Trade quality measurable via Alexander's 15 properties)
- Implicate/explicate ratio (track unfoldment: 31/41 TUPs = 76% documented)

**Evidence Quality**: Theory B-grade (well-sourced), operational translations C/D-grade (logical but unvalidated). All protocols marked experimental, requiring deployment + outcome measurement to upgrade.

**Expert Dialogue**: 7 rounds with 3 personas (Philosophy Professor, Pragmatic Operator, Systems Thinker) to saturation, 12 upgrades applied (theory compression nuance, speculation warnings, time/ROI estimates, adoption tactics, integration-variety balance, external feedback protocol, theory-reality conflict protocol).

### Decisions Made

- **Evidence Grading Conservative**: Theory B (compression loses nuance), operational translations C/D (logical but untested)
- **Epistemological Stance**: Instrumentalism (theory as useful pattern language, not truth claims)
- **Deployment Sequence**: VOID → Bullets → 3-Gate → 75Q → Twin → Verification → Patterns (30/90/180 day roadmap)
- **Maturity Path**: Experimental → Proven (3+ Trades) → Canonical (10+ Trades + published validation)
- **When to Use M39**: Founding stage, stable operations, retrospective, strategic planning. NOT for crisis mode, early validation, resource-constrained contexts.

### Actions Taken

| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Created | `data/m39/theoretical_foundations.md` | 540 lines: Alexander 15 properties, Bohm implicate/explicate, Tononi IIT, Ashby requisite variety with IonWave translations |
| 2 | Created | `data/m39/operational_protocols.md` | 640 lines: 6 protocols (75Q, 5-6 bullets, 3-gate, Virtual Twin, verification, pattern language), deployment roadmap, evidence grading |
| 3 | Created | `data/m39/advisor_and_expert_strategy.md` | 420 lines: 4 trust dimensions, advisor hit list, social capital mapping, engagement protocols, 90-day procurement roadmap |
| 4 | Created | `data/m39/textbook_and_ma_strategy.md` | 370 lines: Textbook project concept, M&A strategy, exit scenarios, acquisition readiness, PE/strategic landscape |
| 5 | Created | `data/m39/love_as_mutual_information.md` | 320 lines: Tononi IIT interpretation, high-MI teams, operator-Trade integration, measurement proxies, failure modes |
| 6 | Created | `data/m39/workshop_summary.md` | 160 lines: Workshop deliverables, key findings, integration with IonWave, evidence assessment, next steps |
| 7 | Created | `data/m39/opkit_theoretical_operations.md` | 430 lines: OK-M39-001 generalizable framework, 4 theoretical foundations, operational protocol template, industry adaptation guide |
| 8 | Created | `data/m39/_meta.json` | Workshop metadata, quality score (7.5/10), intelligence gaps, key blockers, feeds_into, next_steps |
| 9 | Created | `data/m39/dialogue_summary.md` | 7 rounds with 3 personas (Philosophy Professor, Pragmatic Operator, Systems Thinker), 12 upgrades applied, saturation achieved |
| 10 | Updated | `data/manifest.json` | Added M39 entry with status "migrated", quality 7.5/10, opkits reference, feeds_into, key_blockers; updated migrated_tups 25→26 |
| 11 | Updated | `data/opkits/registry.json` | Registered OK-M39-001 (Theoretical Operations Framework) with maturity: experimental, reusability: high |
| 12 | Updated | `tracking/TUP_Workshop_Tracker.md` | Marked M39 DONE (7.5/10), updated workshopped count 31→32, BCL-0 progress 1/5→2/5 (40%) |

### Workshop Stats

- **Total content lines**: ~2,450 (across 6 content files)
- **Dialogue rounds**: 7 (to saturation)
- **Upgrades applied**: 12
- **OpKits created**: 1 (OK-M39-001, experimental maturity)
- **Quality score**: 7.5/10 (calibrated)
- **Evidence grade**: B/C (theory B, practice C/D)
- **Time investment**: ~4 hours (M-effort TUP)

### Key Blockers Identified

1. **Protocols untested** (HIGH) — all experimental, need deployment to validate
2. **Virtual Twin requires full TUP context** (MEDIUM) — need to load M5-M37
3. **Advisor procurement requires network mapping** (MEDIUM) — need Danilo/Nilo to document connections
4. **Cross-Trade validation blocked** (LOW) — only 1 Trade in IonWave portfolio currently
5. **Risk of over-theory, under-execution** (MEDIUM) — M39 could become distraction from operational grind

### Intelligence Gaps Documented

- Optimal TUP count unknown (41 is educated guess, not derived from market complexity analysis)
- Mutual information not practically measurable (proxy metrics invented, not validated)
- Alexander's 15 properties not validated as Trade success predictors (hypothesis only)
- Protocol reusability unknown (need cross-Trade testing)
- [VOID — requires Trade execution: must build Trade to validate theory-practice translations]
- [VOID — requires advisor network: need actual procurement outcomes to validate strategy]
- [VOID — requires empirical testing: implement proxy metrics, track 12 months, correlate with outcomes]

### Next Steps

- [ ] Deploy VOID Protocol (audit existing TUPs for unmarked gaps, formalize usage)
- [ ] Deploy 5-6 Bullets (apply to SESSION_LOG, investor updates, measure satisfaction)
- [ ] Deploy 3-Gate Review (apply to next product decision, score all three gates in parallel)
- [ ] Load full Virtual Twin context (read M5-M37 systematically to complete context)
- [ ] Begin advisor procurement (network mapping with Danilo/Nilo, strategic trust outreach)
- [ ] Validate protocols empirically (measure outcomes over 90 days, iterate based on evidence)
- [ ] Cross-Trade testing (apply protocols to future IonWave Trades when available, test reusability)
- [ ] Workshop M40 Navigation & Command (next BCL-0 TUP, completes sequencing + command center foundations)

---

## Session 2026-02-11 — M4 Fundraising Workshop (Phases 4-11 Completion)

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M4 — Fundraising & Investors
**Quality**: 8.3/10
**Status**: Complete

### Summary

Completed M4 Fundraising workshop Phases 4-11 following TWP-001 v2.0.0 protocol. M4 content was already produced (Phases 1-8 done by previous session: 9 Danilo tabs consolidated into 5 files totaling 2,620 lines, plus dialogue summary and self-grade assessment). This session completed final registration phases: manifest.json update, opkits/registry.json registration of OK-M4-001, TUP_Workshop_Tracker.md update (29→30 TUPs, BCL-2 now 3/4 at 75%), hypothesis cross-referencing (HYP-003, HYP-006), and SESSION_LOG entry.

**Key Context**: M4 Fundraising had exceptionally high-quality Danilo source material (9 tabs, all directly usable: 15-slide pitch deck rated A-grade, 7-stage investor CRM framework, negotiation playbook, term sheet guide, exit preparation, diligence Q&A, backup funding plan, investor FAQ, monthly update template). Phase 4 research covered 2026 D2C fundraising landscape (5 web searches: Carta Q3 2025 data showing $7.7M median pre-seed valuation with 92% SAFEs and 61% cap-only structure, D2C funding down 97% from 2021 peak, micro-seed dynamics, pitch deck best practices).

### Decisions Made

- **M4 registered as migrated** in manifest.json with quality 8.3/10, status "migrated", 9 source tabs → 5 content files
- **OK-M4-001 registered** in opkits/registry.json: "D2C Seed Fundraising Framework" with 5-component system (fundraising strategy, pitch deck framework, investor relations CRM, term negotiation, diligence & exit)
- **BCL-2 cluster progress updated**: 3/4 complete (75%) — M2/M4/M25 done, M3 Financial Model remains blocked by REC-001 margin dispute
- **Hypotheses cross-referenced**: HYP-003 (churn/retention drives exit valuation at 4-6x EBITDA), HYP-006 (marine plasma differentiation is pitch foundation)
- **Novel concept documented**: Trade-as-pitch (investors interact with Claude agent vs static deck) flagged as experimental D-grade, recommend testing with 3-5 friendly investors before scaling
- **6 intelligence gaps flagged**: Investor response data [VOID], micro-raise comparables (C), Trade-as-pitch validation (D), TAM/SAM/SOM sizing (C), SAFE liquidity in bootstrap scenario (C), Brazil-US legal structure (C)
- **4 key blockers documented**: Pre-revenue status (HIGH), investor interest unknown (HIGH), solo founder risk (MEDIUM), M3 margin dispute REC-001 (MEDIUM)

### Actions Taken

| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | registered | `data/manifest.json` | Updated M4 entry from "not_migrated" to "migrated" with full metadata: quality 8.3/10, 9 Danilo tabs → 5 files, opkits reference OK-M4-001, feeds_into (M2/M3/M5), depends_on (M0/M3/M2), hypothesis_links (HYP-003, HYP-006), 4 key blockers, 6 intelligence gaps, next_action |
| 2 | edited | `data/manifest.json` | Updated migrated_tups count from 23 → 24 |
| 3 | registered | `data/opkits/registry.json` | Added OK-M4-001 entry in unmapped_tups.m4 with complete component breakdown: fundraising_strategy.md (650 lines), pitch_deck_framework.md (430 lines), investor_relations.md (550 lines), term_sheet_and_negotiation.md (520 lines), diligence_and_exit.md (470 lines), graded IonWave example 8.3/10 |
| 4 | edited | `tracking/TUP_Workshop_Tracker.md` | Updated workshopped count 29→30, remaining 12→11, BCL-2 section from "2/4 done" to "3/4 done (75%)" with full M4 row entry including 650-line strategy file, pitch deck analysis, 2026 fundraising research, SAFE structure (post-money cap-only 92% standard), warm intro tactics, backup funding plan, novel Trade-as-pitch concept, 6 intelligence gaps, 4 blockers |
| 5 | created | `SESSION_LOG.md` | This entry documenting M4 Phases 9-11 completion |

### Next Steps

- [ ] **M3 Financial Model** remains CRITICAL PATH but blocked by REC-001 (margin dispute: Danilo 40% vs Bootstrap 67%) — requires human decision or Bootstrap margin validation before M3 can be workshopped
- [ ] **BCL-2 at 75%** (3/4 complete: M2/M4/M25 done, M3 pending) — one of the most complete clusters alongside BCL-1 (100%), BCL-3 (100%), BCL-4 (100%), BCL-5 (100%)
- [ ] **30/41 TUPs workshopped** (73% complete) — 11 remaining (M3, M31, M32, M33, M34, M35, M36, M37, M38, M39, M40)
- [ ] **M39 Conceptual** recommended as next workshop target (12 tabs, Medium effort, no blockers, BCL-0 cluster warm-up before tackling massive M38 Strategic Frameworks with 44 tabs)
- [ ] **Consider testing Trade-as-pitch concept** with 3-5 friendly investors to validate novel fundraising approach before broader adoption
- [ ] **Fundraising sprint timeline**: If Danilo proceeds with $30-50K SAFE raise, execute 7-week sprint (Week 1-2 warm intro outreach, Week 3-4 pitch meetings, Week 5-6 due diligence, Week 7 close & validation sprint kickoff)

---

## Session 2026-02-11 — M5 Formulation Registration (Phases 9-11)

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M5 — Formulation
**Quality**: 8.5/10
**Status**: Complete

### Summary

M5 Formulation workshop was completed on 2026-02-10 with high quality (8.5/10) but not yet registered in the system tracking files. This session completed Phases 9-11: registered M5 in manifest.json, opkits/registry.json, and TUP_Workshop_Tracker.md, plus documented in SESSION_LOG.md. **BCL-1 Product & Science cluster is now 4/4 COMPLETE (100%)** — M5/M6/M7/M8 all done, making this the 3rd fully complete cluster after BCL-4 and BCL-5.

### Decisions Made

- **Registration Scope**: M5 was already workshopped (Phases 4-8 complete) — only system registration needed, not content creation
- **BCL-1 Status**: Now 100% complete (4/4 TUPs done), making IonWave launch-ready for product formulation, supply chain, regulatory compliance, and brand identity
- **OpKit Count**: 30 OpKits now registered across 26 TUPs (M5 adds OK-M5-001)
- **Workshop Quality**: 8.5/10 reflects exceptional confidence honesty (9.5/10 — all supplier-dependent data marked [VOID — requires CoA]), strong evidence for core electrolytes, honest about gaps
- **Cluster Completion**: BCL-1, BCL-4, and BCL-5 are now the three fully complete clusters (17/41 TUPs in complete clusters)

### Actions Taken

| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Updated | `data/manifest.json` | M5 status not_migrated→migrated, migrated_tups 21→22, added full M5 metadata (version 1.0.0, quality 8.5/10, protocol TWP-001 v2.0.0, sheet_count 15, consolidation "15 tabs → 5 files + dialogue + OpKit", opkits ["OK-M5-001"], feeds_into [m7,m6,m3,m8], requires [m0,m26], 5 key_blockers, next_action for Week 1-2 supplier outreach) |
| 2 | Updated | `data/opkits/registry.json` | Registered OK-M5-001 in unmapped_tups.m5 with full metadata: name "Mineral-Based Supplement Formulation Framework", type "production", 6-phase framework description, components (instructions/grading rubric/scaffold/graded example), status "workshopped", decision "TWP-001 v2.0.0 2026-02-10", comprehensive notes (15 tabs → 5 files with line counts, green-field build with 5 web searches, 6 rounds/22 upgrades, key innovations, quality breakdown, BCL-1 complete) |
| 3 | Updated | `tracking/TUP_Workshop_Tracker.md` | Workshopped 26→27, Remaining 15→14, BCL-1: 3/4→4/4 COMPLETE with ✅, M5 row filled with full workshop summary (15→5 files with line counts, research sources, core content, 6 rounds/22 upgrades, exceptional confidence honesty 9.5/10, pre-launch blockers, 100% complete note), OpKits 29→30, Summary Scoreboard updated (BCL-1 moved from "75% complete" to "✅ COMPLETE (3rd cluster done)" with note "IonWave launch-ready for formulation/supply/regulatory/brand"), Change Log entry added |
| 4 | Created | `SESSION_LOG.md` entry | This session log documenting M5 registration completion (Phases 9-11) |

### M5 Workshop Output (Completed 2026-02-10)

**Content Files** (5, total 2,247 lines):
- `formulation_specification.md` (323 lines) — Complete mineral profile (Na 1000mg, K 200mg, Mg 60mg + 78 trace minerals), bioavailability data (ionic chloride 66-90%+ vs synthetic 9-105%), quality markers (CoA requirements, heavy metal limits, microbiological standards), formulation development pathway, cost breakdown ($0.48-0.72 COGS, target $0.55), regulatory compliance
- `scientific_substantiation.md` (628 lines) — Clinical studies library (Quinton research, marine plasma studies), mechanism of action (cellular hydration, isotonic delivery), evidence hierarchy, FDA/FTC-compliant claims framework, competitor claims audit (LMNT/Liquid IV/Seaonic), gaps marked honestly
- `product_development.md` (577 lines) — Formulation comparison table (IonWave vs competitors), taste engineering (unflavored purist → lemon-lime mass market → variety SKUs), stability and shelf life (18-24 month target, moisture sensitivity, packaging requirements PET/ALU/PE laminate), development phases, cost per serving
- `usage_protocols_and_stacking.md` (557 lines) — Dosing protocols by situation (general/keto/fasting/workout/travel/hangover), supplement stacking guidance, safety contraindications (blood pressure meds, ACE inhibitors, kidney issues), customer education framework, medical disclaimer requirements
- `dialogue_summary.md` (162 lines) — 6-round expert dialogue to saturation with 3 personas (Formulation Scientist, Skeptical Nutritionist, Regulatory/Claims Auditor), 22 upgrades applied, saturation signal documented

**Meta Files** (1):
- `_meta.json` — Complete workshop metadata with quality scores (overall 8.5/10, confidence honesty 9.5/10), intelligence gaps (14 total: exact trace minerals, taste acceptability, shelf life, bioavailability RCT, microplastics, heavy metal variability), feeds_into/requires, key_blockers, next_action

**OpKit** (1):
- `OK-M5-001_Mineral_Supplement_Formulation.md` — 6-phase framework (Research & Benchmarking → Specification Development → Scientific Substantiation → Product Development → Validation & Testing → Registration & Launch) applicable to ANY mineral-based supplement (electrolytes, trace minerals, alkalizing blends, marine-derived products)

**Research Phase** (Phase 4):
- 5 web searches completed: marine plasma bioavailability/ionic minerals, ocean-sourced vs synthetic electrolytes, Quinton marine plasma clinical research, FDA DSHEA structure/function claims 2026, magnesium chloride vs citrate bioavailability 2025

**Dialogue Phase** (Phase 6):
- 6 rounds to saturation with 22 upgrades including: marine biocenosis reality check, bioavailability trade-off analysis (full spectrum vs maximum single-nutrient absorption), value proposition clarity (ocean sourcing = values-based, not purely evidence-based), heavy metal testing every batch (not random sampling), microplastic testing protocol (quarterly, $2-5K), hangover protocol disclaimer, kidney disease contraindication specificity (eGFR <60), ACE inhibitor warning strength, RCT outcome scenarios, adverse event surveillance protocol

### Key Findings (M5 Content)

**Core Formulation**:
- Primary electrolytes: Na 1000mg, K 200mg, Mg 60mg (LMNT-validated 5:1:0.3 ratio)
- 78-trace-mineral claim reality check: Only 20 elements biochemically required for humans, rest is marketing standard from marine plasma suppliers (Quinton/Biocean/Actimar) but lacks peer-reviewed RDA validation
- Ocean-sourced ionic minerals bioavailability: 66-90%+ (chloride forms, passive diffusion) vs synthetic 9-105% (variable by form, active transport)
- Natural ratios matching human plasma (isotonic 9 g/L salt delivery)

**Evidence & Confidence**:
- Exceptional confidence honesty (9.5/10): ALL supplier-dependent data marked as [VOID — requires CoA from Week 1-2]
- A/B/C/D confidence grades on all claims (no grade inflation)
- Evidence gaps marked honestly: marine plasma bioavailability lacks head-to-head RCT vs synthetic, most trace minerals beyond 20 essentials lack absorption studies

**Compliance & Safety**:
- FDA DSHEA compliant: structure/function claims only (no disease claims), required disclaimers
- Heavy metal limits: <10 ppb As, <5 ppb Pb, <3 ppb Hg (FDA/Prop 65 compliant)
- Microbiological standards: <10 CFU/mL total plate count
- Safety contraindications: blood pressure meds, ACE inhibitors (DO NOT USE without physician), kidney disease (eGFR <60)

**Development Pathway**:
- MVP launch: Isotonic liquid ampules (10 mL, unflavored purist positioning)
- Month 2-3: Powder expansion (lemon-lime + stevia, mass market appeal)
- Month 4-6: Line extension (berry/citrus/watermelon variety pack, hypertonic performance SKU)
- Cost breakdown: $0.48-0.72 COGS per serving (target $0.55), retail $2.50-3.50

### CRITICAL Pre-Launch Blockers (M5)

**Week 1-2 (Supplier-Dependent)**:
1. Supplier CoA validation — ALL exact trace mineral amounts are [VOID] until CoA received from Biocean/Actimar/Quinton
2. Heavy metal testing confirmation — Verify <10/<5/<3 ppb limits for As/Pb/Hg
3. Microbiological validation — Confirm <10 CFU/mL with cold microfiltration 0.22µm

**Week 3-4 (Taste Testing)**:
4. Beta taste testing — Recruit 50-100 keto/fasting users, target ≥70% rating 7/10+ for mass market SKUs

**Month 3-6 (Stability & Validation)**:
5. Accelerated stability testing — 40°C/75% RH for 6 months (simulates 24-month shelf life)
6. Real-time stability — 25°C/60% RH for 24 months (confirm predictions)

**Q3 2026 (Clinical Evidence, Optional)**:
7. Bioavailability RCT — Head-to-head ocean-sourced vs synthetic electrolytes with plasma absorption curves ($50-150K cost, 6-12 months)

### BCL-1 Completion Status

**✅ BCL-1 Product & Science: 4/4 COMPLETE (100%)**

All four TUPs done:
- M5 Formulation (8.5/10) — Core product specification
- M6 Supply Chain (8.4/10) — Supplier vetting, ocean sourcing, CoA framework
- M7 Regulatory & FDA (8.7/10) — DSHEA compliance, claims framework, FTC audit
- M8 Brand Identity (7.8/10) — Positioning, voice, packaging, messaging

**IonWave Launch Readiness**: Product formulation, supply chain, regulatory compliance, and brand identity are all production-ready (execution-ready once supplier CoA received Week 1-2).

**Cluster Average Quality**: 8.35/10 (highest average of any complete cluster)

### Next Steps

- [x] M5 registration complete in all tracking files
- [ ] Week 1-2: Execute supplier outreach (Biocean/Actimar/Quinton) to obtain CoAs with exact trace mineral amounts
- [ ] Week 3-4: Prepare taste testing protocol and recruit 50-100 keto/fasting beta users
- [ ] Month 3: Apply for NSF Certified for Sport (12-16 week buffer before Month 6 launch)
- [ ] Month 3-6: Initiate accelerated stability testing (40°C/75% RH)
- [ ] Next workshop: M12 Ad Creative (26 tabs, XL effort, ~4 hours) to complete BCL-3 DR & Creative cluster (currently 4/5, 80%)

---

## Session 2026-02-10 — M8 Brand Identity Workshop (Phases 8-11)

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M8 — Brand Identity
**Quality**: 7.8/10
**Status**: Complete

### Summary

Completed Phases 8-11 of M8 Brand Identity workshop (Phases 1-7 completed in prior session): OpKit creation (OK-M8-001), system registration (_meta.json + manifest.json + opkits/registry.json updates), hypothesis cross-reference (no direct impact — foundational infrastructure), and SESSION_LOG.md entry. M8 delivers 7 integrated brand identity files covering positioning, voice, packaging, naming, messaging, and visual systems for IonWave's marine plasma supplement brand.

### Decisions Made

- **OpKit Scope**: OK-M8-001 is a 14-step brand identity workshop kit applicable to any D2C supplement brand (greens, protein, capsules, adaptogens), with IonWave as graded example (7.8/10)
- **Grading Rubric**: 5 dimensions (Positioning Clarity, Voice Consistency, Visual Cohesion, Packaging Compliance, Storytelling Strength) using 1-10 scale
- **Scaffold Templates**: 4 production-ready templates (Positioning Canvas, Voice Principles Worksheet, Packaging Compliance Checklist, Industry Perspectives Framework)
- **Hypothesis Impact**: None direct (M8 is foundational infrastructure). Secondary relevance to HYP-003 (marine plasma category viability depends on positioning clarity) and HYP-006 (churn may benefit from strong brand voice/unboxing)
- **BCL-1 Status**: Now 3/4 complete (75%) — M6/M7/M8 done, only M5 (Formulation) remains. BCL-1 is launch-ready for brand, packaging, regulatory compliance, and supply chain.

### Actions Taken

| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Created | `data/m8/opkit_brand_identity.md` | OK-M8-001: Complete brand identity workshop kit with 14-step instructions, 5-dimension grading rubric (A-F scale + 1-10 scale), 4 scaffold templates, IonWave graded example (7.8/10), adaptation guide for different supplement types and budgets, 8 universal principles |
| 2 | Created | `data/m8/_meta.json` | M8 metadata with TUP versioning (1.0.0), quality score (7.8/10), revision history (dialogue ref: 9 rounds, 5 upgrades, 0 unresolved), 14 intelligence gaps (6 CRITICAL, 4 HIGH, 4 MEDIUM), hypothesis links (secondary only), feeds_into/requires |
| 3 | Updated | `data/manifest.json` | Migrated count 20→21, M8 status not_migrated→migrated, added full M8 metadata (version, quality, protocol, sheet_count, consolidation, opkits, feeds_into, requires, key_blockers, next_action) |
| 4 | Updated | `data/opkits/registry.json` | Registered OK-M8-001 in tup_to_opkit.m8 with full metadata (description, components, status, decision, notes) |
| 5 | Updated | `tracking/TUP_Workshop_Tracker.md` | Workshopped count 25→26, BCL-1 cluster 2/4→3/4 (75% complete), M8 row added with full workshop summary (16→7 files, 9 rounds, 5 upgrades, 6 CRITICAL blockers, quality 7.8/10), OpKit count 28→29, Summary Scoreboard updated (BCL-1: 3 done, 1 remaining, ~3 hrs), Change Log entry added |
| 6 | Created | `SESSION_LOG.md` entry | This session log documenting Phases 8-11 completion |

### Key Deliverables (M8 Workshop Output)

**Content Files** (7):
- `brand_strategy.md` (7.3/10) — Positioning, differentiation, brand promise, 3-phase evolution, competitor audit
- `brand_voice_tone.md` (7.2/10) — 5 voice principles, 6 tone contexts, writing guidelines, word banks
- `packaging_design.md` (6.5/10) — Sachet/box/mailer architecture, FDA compliance, Prop 65, unboxing flow
- `brand_naming_domain.md` (6.0/10) — IonWave evaluation, domain/trademark strategy
- `brand_messaging_storytelling.md` (7.4/10) — Brand story, awareness ladder, 3 taglines, 5 social pillars
- `remaining_brand_systems.md` (7.0/10) — Logo/typography/color/photo briefs, iconography, metrics
- `industry_perspectives.md` (8.0/10) — D2C 2026 trends, best-in-class audit, 3 contrarian takes

**Meta Files** (2):
- `dialogue_summary.md` — 9 rounds, 5 upgrades (sachet/box split, CoA escalation, absorption softening, tagline separation, progress tracker)
- `m8_workshop_summary.md` — Complete overview with tab coverage map, intelligence gaps prioritized, OpKit preview

**OpKit** (1):
- `opkit_brand_identity.md` (OK-M8-001) — 14-step instructions, 5-dimension rubric, 4 scaffold templates, IonWave example, adaptation guide

### CRITICAL Blockers (6)

All must be resolved Week 1-2 (launch blockers):
1. **Logo design** — Can't launch without logo (packaging, website, ads). Commission designer ($500-2K).
2. **Photography** — Can't build website/ads/packaging mockups without images. Book photoshoot ($3-5K).
3. **Lab-verified Supplement Facts Panel** — Can't print packaging without exact mineral values (FDA requirement). Supplier CoA + third-party ICP-MS analysis.
4. **Prop 65 heavy metal testing** — Can't sell in California without testing or warning. Third-party lab test (lead, cadmium, arsenic).
5. **Trademark clearance** — Can't print "IonWave" on packaging without USPTO clearance. USPTO search + attorney consult ($1-2K).
6. **Domain acquisition** — Can't launch without ionwave.com or fallback. Check availability, acquire or negotiate.

### Next Steps

- [ ] M5 (Formulation, 15 tabs, L effort) — Only remaining BCL-1 TUP
- [ ] Execute M8 CRITICAL blockers (6 items above) in Week 1-2 of Trade #84 launch
- [ ] Legal review of all M8 label copy (FDA consultant $2-5K)
- [ ] Founder interview for brand story completion
- [ ] Build voice example library (50+ graded samples for copywriter onboarding)

---

## Session 2026-02-10 — M7 Regulatory & FDA Workshop

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M7 — Regulatory & FDA
**Quality**: 8.7/10 (exceeds 8.5-9.0 target)
**Status**: Complete

### Summary
Workshopped M7 (Regulatory & FDA) through full TWP-001 v2.0.0 protocol (Phases 5-11 — context already loaded per task description). 11 Danilo tabs consolidated into 2 comprehensive files (FDA/FTC framework 41 pages + claims guidance/IonWave audit 39 pages) + dialogue summary + self-grade + OpKit. Quality 8.7/10 (exceeds target). Embedded expert dialogue (Regulatory Attorney + FTC Enforcement Officer per TWP v2.0 — no separate rounds). IonWave M11 VSL + M15 Landing Pages audit flagged 12 compliance violations with $420K-$2M total FTC exposure. P0 corrections: 4 hours editing, $0 cost. Second BCL-1 TUP completed (Product & Science cluster now 50% done).

### Decisions Made
- **Embedded expert dialogue per TWP-001 v2.0**: Phase 6 allows embedded expert perspectives during Phase 5 writing (no separate dialogue rounds). Regulatory Attorney + FTC Enforcement Officer lenses applied continuously. 6 key tensions resolved: bioavailability substantiation, fictional testimonials, comparative claims, Quinton research, DSHEA vs FTC jurisdictions, compliance as competitive advantage.
- **2026 regulatory updates integrated**: FDA DSHEA disclaimer now only once per label (not every panel with claims) per January 2026 enforcement discretion memo. FTC consumer review enforcement increased 340% in 2025 — fake reviews = $53,088 per violation (2026 inflation-adjusted rate).
- **IonWave M11/M15 audit as graded example**: Rather than sanitize draft marketing, documented actual compliance violations as teaching example (7 in M11 VSL, 5 in M15 Landing Pages) with penalty estimates and correction paths. Shows PM exactly what NOT to do.
- **Substantiation hierarchy from FTC case law**: Performance claims require RCT (FTC v. POM Wonderful 2016 precedent), testimonials require real customers + "results vary" disclaimer (16 CFR Part 465), mechanism claims require peer-reviewed literature (competent and reliable scientific evidence standard), factual claims require COA/verifiable facts.
- **Conservative grading (8.7/10 not 9.3/10)**: Raw score 9.3/10 (5 dimensions weighted average) adjusted down 0.6 points: -0.3 for OpKit not cleanly separated from IonWave audit (Part 3 should be standalone case study for 5/5 reusability), -0.3 for two upgrade paths lacking vendor specifics (state compliance, competitor audit). Calibrated against pharma-grade brands (Thorne = 10/10).
- **Compliance as competitive moat**: While competitors make aggressive unsubstantiated claims (risking FTC enforcement), IonWave builds defensible positioning through conservative claims. Pre-launch attorney review ($5K-$10K) prevents $500K+ FTC settlement. P0 edits (4 hours, $0 cost) eliminate $420K-$2M exposure.

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| **M7 CONTENT (TWP-001 Phases 5-6)** |
| 1 | Created | `data/m7/fda_ftc_compliance_framework.md` | 41-page comprehensive compliance framework covering FDA DSHEA (pre-market notification, NDI determination for marine plasma, structure/function vs disease claims with 50+ examples, required label elements with 2026 disclaimer update, cGMP requirements for co-manufacturer, adverse event reporting within 15 days, FDA registration verification) and FTC advertising (substantiation doctrine with hierarchy by claim type, deceptive advertising 3-part test, consumer review compliance with 2026 enforcement update +340%, influencer disclosure requirements with 2026 crackdown on vague hashtags, comparison to LMNT factual vs performance distinction). 12-month compliance calendar (Pre-Launch / M1 / M3 / M6 / Y1 gates with owners/deadlines). Compliance audit log template. Intelligence gaps: NDI status attorney opinion needed, co-manufacturer FDA registration pending M6 verification, RCT cost/timeline for bioavailability claim. |
| 2 | Created | `data/m7/claims_guidance_and_ionwave_audit.md` | 39-page claims guidance + IonWave compliance audit: 50+ structure/function vs disease claim examples across 9 categories (hydration, energy, cognitive, recovery, sleep, immune, cardiovascular, digestive, detox), FTC substantiation hierarchy (absolute performance requires RCT, comparative requires head-to-head study, testimonials require real customers, general benefits require peer-reviewed studies, mechanism requires literature, factual requires COA), **IonWave M11 VSL audit flagged 7 violations** (3 fictional testimonials = $159K penalty, unsubstantiated "98% bioavailable" = $100K-$1M risk, quantified "HRV +15 points" unsubstantiated, oversimplified mechanism, uncited "90% deficient" stat, disparaging "chemical plant" language, pre-launch social proof), **M15 Landing Pages audit flagged 5 violations** (98% bioavailable repeated, 10K+ users placeholder, template testimonials, uncited stats, missing DSHEA disclaimer), total FTC exposure $420K-$2M if no corrections. P0 corrections: 4 hours, $0 cost. Competitor audit framework (4-category checklist for LMNT/Seaonic/Liquid IV). Pre-launch audit checklist (8 steps: label, website, VSL, ads, email, substantiation, risk summary, sign-off). |
| **DIALOGUE (Phase 6 — Embedded)** |
| 3 | Created | `data/m7/dialogue_summary.md` | Audit trail documenting embedded expert perspectives (Regulatory Attorney + FTC Enforcement Officer) applied during Phase 5 writing per TWP-001 v2.0. 6 key tensions resolved: (1) Bioavailability claims — Quinton historical use ≠ modern FTC substantiation, requires RCT OR soften language. (2) Fictional testimonials — even if labeled "examples," 16 CFR Part 465 prohibits, $53K+ per violation. (3) Comparative claims — factual (3 minerals vs 78) allowed, performance ("works better") requires study. (4) Quinton research — 1897 finding is history not proof, "98% identical" oversimplifies, needs context OR removal. (5) DSHEA disclaimer ≠ FTC protection — two separate jurisdictions, DSHEA protects from drug classification, doesn't exempt from FTC substantiation. (6) Conservative vs aggressive claims — compliance = competitive advantage, aggressive competitors creating FTC risk not opportunity. Saturated (no separate rounds per TWP v2.0). |
| **SELF-GRADE (Phase 7)** |
| 4 | Created | `data/m7/self_grade_assessment.md` | TWP-001 5-dimension grading: Evidence Coverage 5/5 (2 files 80 pages, 50+ examples, 12 violations flagged, all claims sourced 21 CFR/16 CFR/FTC case law), Confidence Honesty 5/5 (80% A-grade statutes, 15% B-grade inference with validation paths, 5% C-grade benchmarks, 0% D-grade, intelligence gaps explicit), Upgrade Path Quality 4/5 (P0/P1/P2 with cost/timeline, two gaps lack vendor specifics: state compliance $10K / competitor audit TBD), Actionability 5/5 (PM can execute today: compliance calendar, audit checklist, P0 edits 4 hours eliminate $420K risk), OpKit Reusability 4/5 (80% reusable framework, 20% IonWave-specific audit as graded example, not cleanly separated). Weighted average 4.65/5 = 9.3/10 raw. Calibrated to 8.7/10 (conservative adjustment for OpKit separation + vendor gaps). Exceeds 8.5-9.0 target. Grade honesty check: compared to Thorne/Pure Encapsulations pharma-grade (10/10), IonWave with M7 is strong but not pharma-grade. External attorney + Regulatory Attorney + FTC Officer would agree with 8.5-9.0 range. |
| **OPKIT (Phase 8)** |
| 5 | Created | `data/m7/opkit_supplement_regulatory_compliance.md` | OK-M7-001 — 6-step pre-launch compliance framework for ANY supplement brand: Step 1 determine FDA status (NDI decision tree), Step 2 design DSHEA-compliant label (Supplement Facts panel, DSHEA disclaimer once per label, structure/function claims notification template), Step 3 verify manufacturing compliance (co-manufacturer FDA registration FEI check, cGMP audit report, COA system), Step 4 audit marketing for FTC compliance (4-part audit: disease claims, testimonials, performance claims, social proof), Step 5 set up compliance systems (FDA notification template, adverse event reporting protocol, 12-month calendar), Step 6 attorney review ($5K-$10K package). 4 comprehensive checklists (pre-launch marketing audit 8 steps, compliance budget template, 12-month calendar, claims library 50+ examples). Substantiation hierarchy by claim type. Competitor audit framework (4 categories). IonWave graded example 8.7/10. Reusable for any DTC/retail/wholesale supplement (capsules, powders, liquids). |
| **REGISTRATION (Phases 9-11)** |
| 6 | Created | `data/m7/_meta.json` | TUP metadata: 11 Danilo tabs → 5 files (2 content + dialogue + self-grade + OpKit), quality_score 8.7, revisions array with dialogue_ref (embedded method, 6 tensions resolved, 4 unresolved gaps: NDI attorney opinion, co-manufacturer M6 verification, RCT cost quotes, Seaonic competitor audit). feeds_into m11/m15/m14/m22/m8, requires m6. key_blockers: none — launch-ready. next_action: FLAG M11 VSL non-compliant, execute P0 edits 4 hours, attorney review $5K-$10K. |
| 7 | Edited | `data/manifest.json` | M7 migrated, full metadata (version 1.0.0, quality 8.7/10, 0 sheets/11 Danilo tabs, consolidation note, opkits OK-M7-001, feeds_into, requires, key_blockers, next_action) |
| 8 | Edited | `data/opkits/registry.json` | OK-M7-001 registered in tup_to_opkit (moved from unmapped_tups): 6-step framework, 4 checklists, substantiation hierarchy, competitor framework, IonWave graded example 8.7/10. Note: 11→2 comprehensive files, embedded dialogue, IonWave M11 VSL 7 violations flagged ($420K-$2M exposure), P0 corrections 4 hours $0 cost, 2026 updates (FDA disclaimer once/label, FTC consumer review +340%). |
| 9 | Edited | `tracking/TUP_Workshop_Tracker.md` | BCL-1: 1/4→2/4 (50% complete), M7 DONE with full details (11→2 files, 8.7/10, embedded dialogue, IonWave audit, compliance calendar, OpKit). Counts: 24→25 TUPs workshopped, 17→16 remaining. |
| 10 | Edited | `ACTIVE_WORK.md` | (will clear M7 claim at session close) |
| 11 | Created | `SESSION_LOG.md` | This entry |

### Key Findings
1. **IonWave M11 VSL has 7 critical FTC violations** — 3 fictional testimonials (Marcus, Jennifer, David) = $159K penalty under 16 CFR Part 465, unsubstantiated "98% bioavailable" claim = $100K-$1M FTC risk (requires RCT), quantified "HRV +15 points" unsubstantiated, oversimplified mechanism ("body doesn't know what to do with synthetic minerals"), uncited "90% deficient" stat, potentially disparaging "chemical plant" language re: LMNT, pre-launch social proof (10K+ users don't exist yet). **Total exposure if published as-is: $420K-$2M+**.
2. **P0 corrections are cheap and high-ROI** — 4 hours of editing eliminates $420K-$2M FTC risk. Remove 3 fake testimonials, soften "98% identical" to "similar mineral composition," remove quantified HRV claim, add USDA citation for 90% stat OR soften language, change "chemical plant" to "lab-synthesized," remove pre-launch user counts. $0 cost, 4 hours, prevents FTC enforcement.
3. **2026 regulatory landscape changed** — FDA: DSHEA disclaimer now only ONCE per label (not every panel), enforcement discretion memo January 2026. FTC: Consumer review enforcement +340% in 2025, fake reviews = $53,088 per violation (2026 inflation-adjusted), influencer disclosure crackdown (vague hashtags no longer acceptable). Supplement brands are high-priority FTC targets.
4. **Quinton historical research ≠ modern substantiation** — René Quinton's 1897 finding ("98% identical blood plasma to seawater") is accurate history but doesn't satisfy FTC "reasonable basis" standard for 2026 performance claims. Historical use supports non-NDI position (different legal context) but not bioavailability claims without RCT.
5. **Structure/function vs disease claims is bright line** — FDA 21 CFR 101.93 bright line: "supports hydration" (allowed), "treats dehydration" (prohibited drug claim). "Helps maintain energy levels" (allowed), "cures chronic fatigue" (prohibited). 50+ examples provided across 9 categories. Single disease claim makes entire product an unapproved drug.
6. **Compliance = competitive moat** — While competitors make aggressive unsubstantiated claims (creating FTC risk), IonWave differentiates through transparency and defensible positioning. Attorney review ($5K-$10K) prevents $500K+ FTC settlement. Conservative claims + proper substantiation = brand trust + regulatory safety.
7. **M6 dependency critical** — M7 requires co-manufacturer FDA registration verification (FEI number), cGMP audit report, COA system. All flagged as M6 Supply Chain TUP dependency. Pre-launch gate: verify co-manufacturer compliance before claiming "FDA-registered facility" in marketing.

### Next Steps
- [ ] **CRITICAL — M11/M15 Flagging**: Immediately flag M11 VSL script (ionwave_vsl_script_graded.md) as NON-COMPLIANT — DO NOT PRODUCE as-is. Flag M15 Landing Pages (copy_and_headlines.md) testimonials as PLACEHOLDERS ONLY. Both documents already contain compliance warnings but must be explicitly blocked from production until corrections made.
- [ ] **P0 Edits (Pre-Launch Blocker)**: Execute 4 hours of corrections to M11 VSL before production: (1) Remove Marcus/Jennifer/David fictional testimonials, (2) Soften "98% identical" to "similar mineral composition," (3) Remove "HRV +15 points" quantified claim, (4) Add USDA citation for "90% deficient" OR soften to "many Americans," (5) Change "chemical plant" to "lab-synthesized," (6) Remove pre-launch user counts. Estimated time: 4 hours. Cost: $0. Risk reduction: $420K-$2M FTC exposure eliminated.
- [ ] **Attorney Review (Strongly Recommended)**: Pre-launch attorney review of all marketing (label, website, VSL, ads, emails) — $5K-$10K for full package. Upgrades M7 from 8.7/10 to 9.5/10. Provides opinion letter showing good faith compliance (reduces penalties if FTC investigates). Catches violations Claude missed.
- [ ] **FDA Structure/Function Notification**: File within 30 days of first sale (template provided in fda_ftc_compliance_framework.md Part 3.1). Email to ONPLDS@fda.hhs.gov with product name, structure/function claims text, manufacturer name/address.
- [ ] **Adverse Event System Setup**: Set up AE reporting protocol pre-launch (serious AEs to FDA within 15 business days per 21 CFR Part 117). Train CS team to recognize serious vs non-serious. Template: FDA Form 3500A. Escalation: CS → Legal → FDA filing. Log: Zendesk integration or spreadsheet.
- [ ] **Month 3 Actions**: Begin real customer testimonial collection with signed release forms. Replace M15 Landing Page placeholder testimonials with real post-launch customers. "Individual results may vary" disclaimer required.
- [ ] **Month 6 Decision Point**: Commission RCT for bioavailability claim if scaling to 7-figures and performance claims are core to differentiation. Cost: $50K-$200K. Timeline: 6-12 months (IRB + recruitment + data + publication). Alternative: Accept conservative claims positioning (structure/function only).
- [ ] **BCL-1 Completion**: Continue Product & Science cluster (2/4 done): M5 (Formulation, 15 tabs, L) OR M8 (Brand Identity, 16 tabs, L). M5 = ingredients/bioavailability/stability/dosing (deep science). M8 = brand guidelines/packaging/tone/naming (creative).
- [ ] **Cross-TUP Integration**: When M11 VSL is corrected, update M11 meta.json to reference M7 compliance audit. When M15 Landing Pages are corrected, update M15 meta.json to reference M7 claims library.

---

## Session 2026-02-10 — M6 Supply Chain Workshop

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M6 — Supply Chain
**Quality**: 8.4/10
**Status**: Complete

### Summary
Workshopped M6 (Supply Chain) through full TWP-001 v2.0.0 protocol. 13 Danilo tabs (4 with structure, 9 void/minimal) consolidated into 4 production files covering supplier vetting, ocean sourcing, quality control/COA, and restock framework. 6-round expert dialogue with 3 personas (Operations Expert, Skeptical Investor, Regulatory Auditor) produced 12 upgrades (5 critical). Quality 8.4/10 (appropriate for pre-launch TUP with execution dependencies). First BCL-1 TUP completed (Product & Science cluster).

### Decisions Made
- **IonWave-specific content + generalized OpKit**: Supplier research targets IonWave's marine plasma suppliers (Biocean, Actimar, Quinton) but OpKit extracts generalizable supplement supply chain method
- **Honest pre-launch gaps**: All supplier data marked [VOID — requires human outreach Week 1-2] rather than fabricating quotes
- **Prop 65 as quality standard**: California Prop 65 heavy metal limits (stricter than FDA) adopted as IonWave standard to avoid warning labels and signal premium quality
- **21-day safety stock for Phase 1**: Conservative buffer for learning period (vs 14 days standard) due to 50-day lead time and single-source supplier risk
- **Kill criteria explicit**: COGS >$0.60 per 10ml sachet triggers pricing pivot OR margin acceptance OR Trade pivot; supplier exclusivity blocking all Tier 1/2 suppliers escalates to Nilo immediately
- **M13 integration**: Cross-referenced Media Buying (never scale ads >30%/week without 90 days inventory confirmation) to prevent stockouts during growth

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| **M6 CONTENT (TWP-001 Phases 1-6)** |
| 1 | Read | Danilo sources (230-246) | Loaded 4 structural (P, C, IP, V) + 13 content tabs |
| 2 | Created | `data/m6/supplier_research_and_landscape.md` | Comprehensive supplier vetting: 3 Tier 1 suppliers (Biocean/Actimar/Quinton) with real contacts, 7-criteria evaluation scorecard (Quality 30%, MOQ 20%, Lead Time 15%, Unit Economics 15%, Transparency 10%, Packaging 5%, Exclusivity 5%), outreach email template with 10 supplier questions, COGS calculation template (backed into $0.55 max per 10ml from 45-67% margin scenarios), backup supplier activation decision tree with time gates (5-day/10-day escalation), supplier qualification checklist (22 items, must check ≥18), supplier audit checklist (post-contract validation), intelligence gaps (5 listed with upgrade paths) |
| 3 | Created | `data/m6/ocean_sourcing.md` | Marine plasma sourcing strategy: shallow-to-mid depth plankton blooms (20-30m) vs deep ocean water (600m+) — marine plasma targets nutrient-dense phytoplankton not depth, 5 established sources (Hawaii Kona 2-3K ft, Japan Muroto 1K+ m, Korea Gangwon 600-1500m, Taiwan 600m+, Iceland varies), supplier-specific sourcing (Quinton France 20-30m plankton blooms, Biocean NATURA 2000 Atlantic, Plasma Marino Gulf Stream 25-30m), IonWave Option 1 (use supplier's existing source — most likely) vs Option 2 (Bay of Biscay direct sourcing — Year 2+ only), 13 questions for suppliers (GPS coordinates, depth, extraction method, processing, COA samples), 5 red flags (won't disclose location, no third-party tests, vague depth, no facility visit, price too good), competitor benchmarking (Seaonic Bay of Biscay claim unvalidated, Quinton transparent 125+ year brand) |
| 4 | Created | `data/m6/quality_control_and_coa.md` | FDA cGMP + Prop 65 compliance framework: COA requirements table (11 test categories — Identity 2, Heavy Metals 4, Microbial 4, Contaminants 1), COA tracker template (batch-by-batch with pass/fail, traceability to IonWave lot #), COA template for supplier (FDA-compliant format with Prop 65 limits explicitly noted), contaminant limits reference table (Lead <0.5 ppm Prop 65 vs no FDA explicit limit, Mercury <0.1 ppm FDA, Cadmium <0.5 ppm Prop 65, Arsenic <10 ppb FDA), batch/lot tracking system (IonWave lot format IW-YYMMDD-XXX, traceability map supplier batch → IonWave lot → customer orders for 24-hour recall lookup per FDA 21 CFR 111.465), restock-COA integration (adds 5-7 days to lead time, increases safety stock calculation), supplier quality issue protocol (3 scenarios: replacement batch + CAP, dispute with third-party re-test, ocean contamination event), recall protocol if failed batch already shipped (voluntary recall within 24 hours, 2x refund, FDA notification if health risk) |
| 5 | Created | `data/m6/restock_framework.md` | Formula-based inventory replenishment: Reorder Point = (Daily Sales × Lead Time) + Safety Stock, baseline variables (50 units/day D-grade estimate from M3, 50-day lead time including 5-day COA approval, 21-day safety stock for Phase 1), example calculation (reorder at 3,550 units for 50 units/day), Order Quantity formula with constraints (cash, MOQ, storage), restock tracker template (PO log with expected vs actual delivery, days early/late tracking for formula adjustment), weekly inventory check protocol (Monday 9 AM, compare to reorder point, decision tree for PO placement), demand forecasting upgrade path (simple 14-day average → weighted moving average → exponential MA → seasonal adjustment → Shopify apps by revenue tier), cash flow integration with M25 (pre-order cash check, payment terms impact, $5K buffer requirement), supplier constraints (MOQ negotiation strategy, lead time variability mitigation, quarterly review), 3 stress test scenarios (sales spike from viral campaign → emergency PO + expedited production + slow ad spend, sales collapse → cancel/delay PO + liquidation options + Trade kill criteria check, supplier stockout → activate backup + air freight + slow sales + product substitution) |
| **DIALOGUE (Phase 6)** |
| 6 | Applied | U1-U12 across 4 files | 12 upgrades from 6-round dialogue (5 critical) |
| 7 | Created | `data/m6/dialogue_summary.md` | Full dialogue audit trail with 3 personas, 6 rounds to saturation, 12 upgrades (U1 kill criteria for supplier unavailability, U2 escalated timeline Week 1-2, U3 FDA registration mandatory, U4 COGS kill criteria >$0.60, U5 lead time validation protocol, U6 safety stock 21 days Phase 1, U7 M13 ad spend integration, U8 backup activation decision tree, U9 30-day contingency delay vs pivot, U10 Prop 65 rationale visibility, U11 COA template Prop 65 notation, U12 COA format review pre-contract), 0 unresolved gaps (all execution-dependent) |
| **REGISTRATION (Phases 7-11)** |
| 8 | Created | `data/m6/opkit_supplement_supply_chain.md` | OK-M6-001 — 8-step generalizable framework: Step 1 define supply chain requirements (product specs, financial constraints, timeline, sourcing preferences), Step 2 research 3-5 suppliers (Google, industry directories, competitor analysis, trade shows), Step 3 supplier outreach (email template with 10 questions, 5-day follow-up protocol), Step 4 evaluate with scorecard (7 criteria, 1-5 scale, weighted total, 80%+ = primary / 60-79% = backup / <60% = disqualify), Step 5 supplier qualification (22-item checklist, must check ≥18), Step 6 COA requirements (template + tracking system), Step 7 restock formula (reorder point calculation, weekly check protocol, monthly review), Step 8 backup plan + quality protocol (decision tree, CAP request, recall plan). Grading rubric A-F scale across 5 dimensions. IonWave as graded example (8.4/10). Adaptation guide for capsules/powders/US-only/B2B. |
| 9 | Created | `data/m6/_meta.json` | TUP metadata with dialogue_ref, quality_score 8.4, revisions array |
| 10 | Edited | `data/manifest.json` | M6 migrated, full metadata (version 1.0.0, quality 8.4/10, 13 sheets, consolidation, opkits, feeds_into, key_blockers, intelligence_gaps, danilo_source_note) |
| 11 | Edited | `data/opkits/registry.json` | OK-M6-001 registered with full component mapping (instructions, scorecard, COA template, restock formula, graded example) |
| 12 | Edited | `tracking/TUP_Workshop_Tracker.md` | BCL-1: 0/4→1/4, M6 DONE, counts 23→24 TUPs, 27→28 OpKits |
| 13 | Edited | `ACTIVE_WORK.md` | Cleared M6 claim |
| 14 | Created | `SESSION_LOG.md` | This entry |

### Key Findings
1. **Danilo tab 233 (Supplier Research) had real IonWave supplier targets** — Biocean (Canada/France, GMP, NATURA 2000, contact: Myriam/Marc Biss), Actimar (sister company to Biocean), Quinton (Spain, 125+ year brand, pharma-grade) — this was the strongest Danilo content across all 13 tabs
2. **Marine plasma sourcing ≠ deep ocean water** — Industry uses shallow-to-mid depth plankton blooms (20-30m) for nutrient density, not 600m+ deep ocean strategy (clarifies sourcing claims vs Deep Ocean Water category like Kona Deep)
3. **California Prop 65 is stricter than FDA** — Lead <0.5 ppm Prop 65 vs no explicit FDA limit (ALARA only); adopting Prop 65 as standard avoids warning labels and signals premium quality
4. **MOQ/lead time research from web sources** — 2,500-10,000 units first order typical, 50-75% MOQ for reorders, 14-18 weeks first production / 6-10 weeks reorders (all unconfirmed for IonWave suppliers, pending outreach)
5. **Pre-launch context requires honest [VOID] marking** — All 4 content files have supplier-specific data marked [VOID — requires human outreach] rather than fabricating quotes; appropriate for 8.4/10 quality (will upgrade to 9-10/10 after execution)

### Next Steps
- [ ] **CRITICAL PATH**: Execute supplier outreach campaign within Week 1-2 of Trade #84 kickoff (Biocean, Actimar, Quinton) using templates from supplier_research_and_landscape.md
- [ ] Apply Supplier Evaluation Scorecard (7 criteria) to all quotes received
- [ ] Confirm FDA registration, MOQ, pricing (<$0.55 per 10ml target), lead time (50 days baseline), exclusivity status for top 3 candidates
- [ ] Select primary supplier + 1 backup supplier by Week 3
- [ ] Complete Supplier Qualification Checklist (22 items) before contract signature
- [ ] Update M3 Financial Model with actual COGS after quotes received (currently using D-grade estimates)
- [ ] Continue BCL-1 sprint: M5 (Formulation, 15 tabs, L), M7 (Regulatory, 11 tabs, M), or M8 (Brand Identity, 16 tabs, L)

---

## Session 2026-02-09 — M11 VSL Production Workshop (Session J - interrupted, now closed)

**Operator**: Caio (Claude)
**Model**: claude-sonnet-4-5-20250929
**Protocol**: TWP-001 v2.0.0
**TUP**: M11 — VSL Production
**Quality**: 9.2/10
**Status**: Complete (administrative cleanup completed 2026-02-10)

### Summary
Workshopped M11 (VSL Production) through full TWP-001 v2.0.0 protocol. 14 Danilo tabs with heavy duplication (tabs 311/317, 312/319) consolidated into 8 production files. 6-round expert dialogue with 3 personas (D2C Creative Director, Performance Media Buyer, FTC Compliance Attorney) produced 15 upgrades, all applied. Quality 9.2/10. Session interrupted before administrative cleanup — completed in subsequent session.

### Decisions Made
- **VSL-as-Trade framework**: VSLs are products, not ads — systematic iteration beats heroic launches
- **Angle vs hook clarity**: ANG-01 (marine plasma mechanism) is one angle; 10 hooks test different entry points
- **Winner rate realism**: 10-20% (not 20-40%) for cold supplement VSLs — adjusted financial model accordingly
- **Founder video deferred to Phase 2+**: B-roll+VO first for cheap hook testing; founder on-camera later once hook proven
- **Platform allocation**: 50% Meta, 35% YouTube, 15% TikTok (28-45 demo skews older than pure TikTok play)
- **FTC compliance rigor**: "98% identical to blood plasma" flagged as unsubstantiated — requires RCT OR structure/function pivot
- **Fictional testimonials flagged**: Current IonWave VSL script uses fictional names — cannot go live per FTC Consumer Review Rule
- **Testing kill criteria**: $150 spend + minimum 10 purchases (avoids small-sample false positives)
- **CPA creep thresholds**: <15% green, 15-30% yellow, >30% red (triggers immediate creative refresh)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| **M11 CONTENT (TWP-001 Phases 1-6)** |
| 1 | Read | Danilo sources (309-322) | Loaded 4 structural + 14 content tabs |
| 2 | Created | `data/m11/vsl_as_trade_framework.md` | VSL philosophy, lifecycle phases, anti-hero launch mindset |
| 3 | Created | `data/m11/script_architecture.md` | 8-section VSL structure, hook-to-close flow, FTC disclaimers |
| 4 | Created | `data/m11/hook_library.md` | 10 hook frameworks (5 types × 2 variants), ANG-01 examples |
| 5 | Created | `data/m11/testing_protocol.md` | Statistical kill criteria, winner rate, CPA creep thresholds |
| 6 | Created | `data/m11/production_spec.md` | B-roll checklist, FTC compliance, founder video phasing |
| 7 | Created | `data/m11/financial_model.md` | Cost structures, ROI scenarios (10-20% winner rate) |
| 8 | Created | `data/m11/iteration_system.md` | Version tracking, post-mortem template, portfolio dashboard |
| 9 | Created | `data/m11/ionwave_vsl_script_graded.md` | Existing 4-min script graded (5/10 with 7 compliance flags) |
| **DIALOGUE (Phase 6)** |
| 10 | Applied | U1-U15 across 8 files | 15 upgrades from 6-round dialogue |
| 11 | Created | `data/m11/dialogue_summary.md` | Full dialogue audit trail |
| **REGISTRATION (Phases 7-11)** |
| 12 | Created | `data/m11/opkit_vsl_production.md` | OK-M11-001 — 9-step instructions, grading rubric, scaffold |
| 13 | Created | `data/m11/_meta.json` | TUP metadata with dialogue_ref |
| 14 | Edited | `data/manifest.json` | M11 migrated, full metadata |
| 15 | Edited | `data/opkits/registry.json` | OK-M11-001 registered |
| **CLEANUP (2026-02-10)** |
| 16 | Edited | `ACTIVE_WORK.md` | Cleared M11 claim |
| 17 | Edited | `tracking/TUP_Workshop_Tracker.md` | BCL-3: 2/5→3/5, M11 DONE |
| 18 | Created | `SESSION_LOG.md` | This entry |

### Key Findings
1. **FTC compliance gaps in source material** — Danilo tabs had minimal FTC guidance. "98% bioavailable" claim appears in multiple sources but is unsubstantiated.
2. **Fictional testimonials cannot go live** — Current IonWave VSL script uses fake customer names ("Sarah M. from Denver") — FTC violation risk.
3. **Winner rate expectations too optimistic** — Source tabs implied 20-40%, but cold supplement VSL reality is 10-20%.
4. **Hook vs angle confusion** — Source tabs mixed terminology. Clarified: 1 angle (marine plasma mechanism), 10 hooks (different entry points).
5. **Heavy duplication in testing tabs** — Tabs 311/317 (script architecture) and 312/319 (testing protocol) were near-duplicates.

### Next Steps
- [x] Administrative cleanup (completed 2026-02-10)
- [ ] Post-launch Month 1: Test 5 hook variants on ANG-01 with $1,200 budget
- [ ] Commission RCT for bioavailability OR pivot all claims to structure/function language
- [ ] Replace fictional testimonials with real customer reviews (Month 2+)
- [ ] Continue BCL-3 sprint: M13 (Media Buying, 14 tabs) next

---

## Session 2026-02-09 — M15 Landing Pages & Conversion Workshop (Session K)

**Operator**: Caio (Claude)
**Model**: claude-opus-4-6
**Protocol**: TWP-001 v2.0.0
**TUP**: M15 — Landing Pages & Conversion
**Quality**: 8.2/10

### Summary
Workshopped M15 (Landing Pages & Conversion) through full TWP-001 v2.0.0 protocol. 18 Danilo tabs (~738 rows) with heavy duplication (Psychology ×3, Headlines ×3, Templates ×3, Checkout ×3) consolidated into 5 production files. 6-round expert dialogue with 3 personas produced 25 upgrades (23 applied, 3 critical — FTC negative option rule, Prop 65 CoA testing, click-to-cancel rule). Also fixed carried-over M1 HYP-001 hypothesis index references from prior session.

### Decisions Made
- **Conversion equation is the core framework**: `Conversion = Desire − Friction − Anxiety` — reducing one anxiety beats increasing ten desires
- **Test architecture before copy**: 10x impact vs 2x impact — finding the right funnel shape is far more valuable than the right headline
- **8 funnel architectures (A-H)**: Added LP+VSL Hybrid (Architecture H) during dialogue. IonWave priority: PDP + LP first, then Hybrid + Advertorial
- **Shop Pay is the single biggest conversion lever**: Up to 50% lift over guest checkout, 91% mobile conversion lift
- **Subscription rate elevated to tier-1 CRO metric**: 3.7x LTV difference (subscriber $305 vs one-time $83) — more valuable than AOV optimization
- **FTC/DSHEA compliance framework added**: Source tabs had zero compliance content — this is a green-field addition covering disclaimers, claim types, testimonials, negative option rule, click-to-cancel, Prop 65
- **7 corrections applied**: Fictional testimonials (Marcus T., Jennifer R., David K.) flagged as CANNOT go live; 98% bioavailable claim needs citation; 10,000+ optimizers is pre-launch fiction; 127 reviews / 4.8 stars is placeholder; René Quinton blood plasma claim reworded; guarantee language changed; deduplication consolidated
- **Emma Relief: cautionary reference**: Replicate funnel architecture (~$4M/year supplement brand), avoid aggressive practices (BBB F rating)
- **M15 cluster corrected**: _meta.json originally said BCL-6; manifest.json correctly lists M15 under BCL-3 (DR & Creative)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| **M15 CONTENT (TWP-001 Phases 1-6)** |
| 1 | Read | Danilo sources (383-403, 404) | Loaded 4 structural + 18 content tabs |
| 2 | Created | `data/m15/landing_page_psychology.md` | Conversion equation, 5-second test, page flow, visual hierarchy, psychological elements, anxiety mapping, mobile-first, page speed budget |
| 3 | Created | `data/m15/copy_and_headlines.md` | 17 headline formulas, section templates, IonWave LP + PDP copy references, copy testing protocol |
| 4 | Created | `data/m15/checkout_optimization.md` | Cart abandonment, checkout checklist, recovery system, AOV boosters, subscription-first design, post-purchase optimization |
| 5 | Created | `data/m15/funnel_architecture.md` | 8 funnel architectures (A-H), testing framework, traffic routing, Emma Relief reference, VSL architecture |
| 6 | Created | `data/m15/cro_testing_framework.md` | CRO testing, FTC/DSHEA compliance, Prop 65, subscription rules, metrics dashboard, sprint calendar |
| **DIALOGUE (Phase 6)** |
| 7 | Applied | U1-U25 across 5 files | 25 upgrades (23 applied, 3 critical). 3 personas: D2C CRO Director, FTC Compliance Attorney, Shopify Plus Architect |
| 8 | Created | `data/m15/dialogue_summary.md` | 6 rounds, 3 personas, 25 upgrades, 8 key themes |
| **REGISTRATION (Phases 7-11)** |
| 9 | Created | `data/m15/opkit_landing_pages_and_conversion.md` | OK-M15-001 — 12-step instructions, grading rubric, scaffold, adaptation guide |
| 10 | Created | `data/m15/_meta.json` | TUP metadata |
| 11 | Edited | `data/m15/_meta.json` | Fixed cluster BCL-6 → BCL-3 |
| 12 | Edited | `data/manifest.json` | M15 migrated, full metadata |
| 13 | Edited | `data/opkits/registry.json` | OK-M15-001 registered with full component mapping |
| 14 | Edited | `tracking/TUP_Workshop_Tracker.md` | BCL-3: 1/5→2/5, M15 DONE, counts 20→21 TUPs, 24→25 OpKits |
| 15 | Edited | `data/hypotheses/index.json` | +5 M15 docs (HYP-001 15, HYP-002 16, HYP-004 13), +2 M1 docs (carried fix), +2 dialogues, metadata updated (75 docs, 20 context, 157 refs) |
| 16 | Created | `SESSION_LOG.md` | This entry |
| 17 | Edited | `ACTIVE_WORK.md` | Cleared M15 claim |

### Key Findings
1. **Heavy duplication in source material** — 18 Danilo tabs had extensive duplication (Psychology ×3, Headlines ×3, Templates ×3, Checkout ×3). Consolidated 18 → 5 files by deduplicating and merging unique content.
2. **FTC compliance was completely missing** — Danilo's source tabs had zero FTC/DSHEA compliance content for a supplement landing page. This is existential risk. Added comprehensive framework.
3. **Fictional testimonials cannot go live** — Marcus T., Jennifer R., David K. are fictional. FTC Consumer Review Rule: $53,088+ per violation for fake reviews.
4. **Emma Relief is both a model and a warning** — ~$4M/year supplement brand using VSL funnel. Replicate funnel architecture (7 stages), but BBB F rating from aggressive subscription/upsell practices shows what NOT to do.
5. **VSL length calibration** — Emma Relief uses 30-min VSL for ~$184 avg order. IonWave at $47-59 → 3-5 min short-form VSL is more appropriate.

### Next Steps
- [ ] Build actual landing page using funnel_architecture.md (start with Architecture A: Direct PDP for warm traffic)
- [ ] Attorney review for FTC/DSHEA compliance before any page goes live
- [ ] Prop 65 CoA testing for marine plasma before selling in California
- [ ] Replace all fictional testimonials with real customer reviews post-launch
- [ ] Continue BCL-3 sprint: M11 (VSL, 14 tabs), M13 (Media Buying, 14 tabs), or pivot to another cluster

---

## Session 2026-02-09 — M1 Labor Chain & Deployment Workshop (Session J)

**Operator**: Caio (Claude)
**Model**: claude-opus-4-6
**Protocol**: TWP-001 v2.0.0
**TUP**: M1 — Labor Chain & Deployment
**Quality**: 8.6/10

### Summary

Workshopped M1 (16 Danilo tabs → 5 production files). Highly conceptual/proprietary TUP covering: Role Engineering (7 dimensions), Labor Sequencing (Founder → VA → CoS → Recruiter → Operator), Overdetermined Coordination, Trustee Framework, Operator System (comp/cert/onboarding/contract/offboarding), CM system, contract templates, Company-as-CRM.

Expert dialogue (3 personas, 6 rounds) produced 34 upgrades including 5 critical: contractor misclassification risk, Trustee authority legal basis, CM independence (reporting line fix), equity instrument specification, and offboarding protocol (missing from all Danilo tabs).

Key corrections: 7-week sprint → 12-week (industry standard), single-trigger → double-trigger equity acceleration, work-for-hire → explicit IP assignment for contractors.

### Files Created/Modified

- `data/m1/role_engineering_and_coordination.md` (NEW)
- `data/m1/labor_chain_and_sequencing.md` (NEW)
- `data/m1/operator_system.md` (NEW)
- `data/m1/hiring_and_onboarding.md` (NEW)
- `data/m1/relationships_and_compensation.md` (NEW)
- `data/m1/dialogue_summary.md` (NEW)
- `data/m1/opkit_labor_chain_and_deployment.md` (NEW)
- `data/m1/_meta.json` (NEW)
- `data/manifest.json` (UPDATED: migrated_tups 18→19, M1 entry)
- `data/opkits/registry.json` (UPDATED: OK-M1-001)
- `tracking/TUP_Workshop_Tracker.md` (UPDATED: 20/41, BCL-6 4/8, 24 OpKits)

### Progress

20/41 TUPs (48.8%), 24 OpKits, BCL-6 at 4/8. Next: continue BCL-6 sprint.

---

## Session 2026-02-09 — M24 Fulfillment & Inventory Workshop (Session I)

**Operator**: Caio (Claude)
**Model**: claude-opus-4-6
**Protocol**: TWP-001 v2.0.0
**TUP**: M24 — Fulfillment & Inventory
**Quality**: 8.4/10
**Duration**: ~60 min active

### Actions

| # | Action | Detail |
|---|--------|--------|
| 1 | Claimed ACTIVE_WORK.md | M24 workshop scope (BCL-6) |
| 2 | Found M24 structural files | 516_p, 517_c, 518_ip, 529_v — P-tab confirms "Fulfillment & Inventory", 10 content tabs |
| 3 | Read all 10 content tabs | 519-528: 4 GOOD, 3 THIN, 2 TEMPLATE, 1 GOOD. No Bootstrap source 15 (green-field build) |
| 4 | Cross-TUP reads | M9 (Shopify 3PL integration), M25 (COGS $20 landed), M28 (international gating) |
| 5 | Phase 3 Checkpoint | 10→4 file consolidation, 5 corrections, 10 cross-TUP alignments |
| 6 | Research (Phase 4) | 3PL pricing 2026, FDA supplement storage, subscription fulfillment, Shopify integrations, shipping optimization, lot tracking, unboxing, self→3PL transition |
| 7 | Created 3pl_and_fulfillment.md | Phase-gated fulfillment (self→3PL→multi-node), 2026 3PL comparison, supplement compliance, SLA monitoring, damaged/lost protocol, unboxing |
| 8 | Created launch_operations.md | War room (T-48 to T+12hr), go/no-go matrix, 72hr scorecard (MER-aligned), first 10 orders playbook, founder thank-you template |
| 9 | Created inventory_management.md | Two-stream demand model (sub + one-time), reorder points, lot tracking (FEFO), seasonal calendar, financial integration (M25 alignment) |
| 10 | Created international_and_scaling.md | US-first strategy (4 phases), Canada/UK compliance, scaling milestones, free shipping economics, returns policy |
| 11 | Phase 6 Dialogue | 3 personas (3PL Ops Specialist, Inventory Analyst, Launch Strategist), 6 rounds to saturation, 27 upgrades |
| 12 | Applied U1: Contract negotiation checklist | Red flags, minimum terms, hidden fee detection |
| 13 | Applied U2: Temperature excursion protocol | Supplement-specific 3PL requirement |
| 14 | Applied U3: Insurance requirements | Product liability + cargo transit at 3PL |
| 15 | Applied U4/U13: MOQ analysis + First PO framework | ≤25% of cash reserves, conservative 3-month forecast |
| 16 | Applied U5: Statistical safety stock | Z × σ × √lead_time after 60 days of data |
| 17 | Applied U6/U14: Cohort decay model + Renewal clustering | Month 2 churn highest (20-30%), billing date spread |
| 18 | Applied U7/U8: Abort/restart + Soft launch | 10-20 friends/family before hard launch |
| 19 | Applied U9: Day 1 ad budget cap | $100-200 max, prevents burning on system failures |
| 20 | Applied U10/U19/U20: Kitting, packaging audit, inbound SOP | Mystery order audits, receiving checklist |
| 21 | Applied U11: Carrier diversification | Dual-carrier strategy, rate shopping |
| 22 | Applied U12/U18: Returns cost + Free shipping at scale | $3.50-9/return, 8% revenue trigger |
| 23 | Applied U16: Site-down emergency protocol | 15-min response, maintenance page |
| 24 | Applied U17: Post-launch retrospective | Structured template for Day 7 review |
| 25 | Applied U21: Dead stock liquidation | 5-option priority ladder |
| 26 | Applied U22/U26: Ad spend→demand linkage + Inventory turnover | 6-8x/year target |
| 27 | Applied U23: First negative review protocol | Response template, internal investigation |
| 28 | Applied U24: Inventory depletion in 72hr scorecard | Added to monitoring metrics |
| 29 | Applied U25: Batch-level cost tracking | For landed cost accuracy |
| 30 | Applied U27: Founder energy management | Physical presence schedule during launch |
| 31 | Self-grade: 8.4/10 | Strong fulfillment coverage + supplement-specific compliance |
| 32 | Created OpKit OK-M24-001 | 12-step instructions, grading rubric, adaptation guide |
| 33 | Updated manifest.json | M24: migrated, 8.4/10, migrated_tups 17→18 |
| 34 | Updated registry.json | OK-M24-001 registered |
| 35 | Updated TUP_Workshop_Tracker | M24 DONE, BCL-6 3/8, 19/41 workshopped, 23 OpKits |
| 36 | Updated hypotheses/index.json | HYP-002 +1 ref (→14), HYP-004 +1 ref (→11), +4 docs, +1 context doc |
| 37 | Session close | Cleared ACTIVE_WORK.md, logged session |

### Key Decisions

1. **Green-field build** — Bootstrap source 15 not found. Built entirely from Danilo tabs + research + cross-TUP references.
2. **Deliverr/Flexport merged** — Danilo listed separately; Deliverr acquired by Flexport 2022. Single entry now.
3. **Amazon FBA excluded as D2C 3PL** — Per M28: FBA is Amazon channel only. MCF uses Amazon-branded packaging.
4. **72hr scorecard: MER not ROAS** — Aligned with M30 framework. Danilo used "ROAS" incorrectly.
5. **Two-stream demand model added** — Subscription (cohort decay) + One-time (ad-driven). Missing from Danilo entirely.
6. **Supplement compliance section added** — FDA 21 CFR Part 111, temperature 59-86°F, humidity <60% RH, FEFO, lot tracking. Absent from Danilo.
7. **Phase-gated fulfillment**: Self-fulfill (0-50 orders/mo) → 3PL (50+) → Optimized (200+) → Multi-node (1000+).
8. **Day 1 ad budget cap**: $100-200 max prevents burning capital on undiscovered system failures.
9. **Soft launch protocol**: 10-20 friends/family for 2-3 days before hard launch with paid traffic.

### Innovations (for future OpKit/TUP use)

- **Subscription cohort decay model**: Flat churn rates distort inventory forecasts. Month 2 churn 20-30%, stabilizes at 8-12% by Month 6+.
- **First PO decision framework**: ≤25% of cash reserves, conservative 3-month forecast, negotiate CM MOQ.
- **Temperature excursion protocol**: Supplement-specific requirement — 3PL must document, quarantine, and report any deviation.
- **Contract negotiation red flags**: "Market rate adjustments", no inbound receiving SOP, no lot tracking capability.
- **Abort/restart protocol**: Clear criteria for when to kill a launch attempt and restart with fixes.
- **Founder energy management**: Physical presence schedule during launch week to prevent burnout.
- **Dead stock liquidation ladder**: 5-option priority (bundle → discount → donate → destroy → write off).

### Next Steps

- Continue BCL-6 sprint: M1 Labor (16 tabs, L), M31 Hiring (30 tabs, XL), M35 Execution Plans (25 tabs, L), M36 Operational Infra (43 tabs, XL), M15 Ads (not yet assessed)
- Total progress: 19/41 TUPs (46.3%), 23 OpKits, 2 complete clusters (BCL-4, BCL-5), BCL-6 at 3/8

---

## Session 2026-02-09 — M18 Email Lifecycle Flows Workshop (Session H)

**Operator**: Caio (Claude)
**Model**: claude-opus-4-6
**Protocol**: TWP-001 v2.0.0
**TUP**: M18 — Email Lifecycle Flows (corrected from "SMS")
**Quality**: 8.7/10
**Duration**: ~45 min active

### Actions

| # | Action | Detail |
|---|--------|--------|
| 1 | Claimed ACTIVE_WORK.md | M18 workshop scope |
| 2 | Found M18 structural files | 432_p, 433_c, 434_ip, 447_v — discovered P-tab says "Email Lifecycle Flows" not "SMS" |
| 3 | Read all 12 content tabs | 435-446: 3 IonWave-specific (strong), 6 generic templates, 2 win-back, 1 lifecycle map |
| 4 | Read M17 sms_strategy.md | Confirmed SMS scope already in M17. M18 is pure email. |
| 5 | Phase 3 Checkpoint | 12→4 file consolidation, 5 corrections, 6 cross-TUP alignments |
| 6 | Research (Phase 4) | Klaviyo 2026 features, deliverability requirements, D2C benchmarks, cart recovery rates, win-back best practices |
| 7 | Created welcome_and_nurture.md | Track A (subscriber) + Track B (purchaser) welcome flows, full IonWave email copy, deliverability checklist |
| 8 | Created cart_recovery.md | 3-email cart abandonment, discount escalation rules, IonWave copy |
| 9 | Created post_purchase_and_retention.md | 7-email post-purchase, replenishment, subscription upsell |
| 10 | Created winback_and_lifecycle.md | 4-email win-back, sunset/list hygiene, master lifecycle automation map (13 flows, 42 emails) |
| 11 | Phase 6 Dialogue | 3 personas (Klaviyo Architect, Copywriter, Retention Strategist), 6 rounds to saturation, 14 upgrades |
| 12 | Applied U1: Abandoned Checkout flow | Separate from cart (15-min trigger, higher intent) |
| 13 | Applied U2/U12: Founder voice | "Nilo" replaces "The IonWave Team" across all files |
| 14 | Applied U3: PP6/PP7 → campaigns | Removed from post-purchase flow, moved to subscriber segment campaigns |
| 15 | Applied U4: Klaviyo consent + profile properties | consent_status, flow_status tracking |
| 16 | Applied U5/U6: AC2 rewrite + AC3 auto-apply | Objection handling lead with result; free shipping auto-applied (no code) |
| 17 | Applied U7: Pre-churn intervention | Subscription cancel/payment failure triggers within 1-2 hours |
| 18 | Applied U8: Viewed Product tracking Day 1 | For Month 2 browse abandonment flow data |
| 19 | Applied U9: Flag PP5 statistics | Aspirational (Confidence: D) until validated |
| 20 | Applied U10: Subscription Conversion Decision Tree | Maps every subscription touchpoint across all flows |
| 21 | Applied U11: Engagement segments | Engaged 30d/90d for campaign targeting, deliverability protection |
| 22 | Applied U13: Domain warm-up protocol | 2-4 week gradual volume increase from new domain |
| 23 | Applied U14: Single-question survey | PP7 reduced from 3 questions to 1 for 3-4x response rate |
| 24 | Self-grade: 8.7/10 | Highest M18 quality. Strong IonWave copy + lifecycle orchestration |
| 25 | Created OpKit OK-M18-001 | 14-step instructions, grading rubric, adaptation guide |
| 26 | Updated manifest.json | M18: migrated, 8.7/10, corrected name, 12 sheets |
| 27 | Updated registry.json | OK-M18-001 registered |
| 28 | Updated TUP_Workshop_Tracker | M18 DONE, BCL-4 COMPLETE (2nd cluster), 18/41 workshopped, 22 OpKits |
| 29 | Updated hypotheses/index.json | HYP-002 +1 ref (13), HYP-006 +1 ref (13), +2 docs, +1 context doc |
| 30 | Session close | Cleared ACTIVE_WORK.md, logged session |

### Key Decisions

1. **M18 is "Email Lifecycle Flows", not "SMS"** — corrected across all system files. SMS content stays in M17.
2. **Product format standardized to "sachet"** — Danilo tabs 442/443 said "scoop", corrected throughout.
3. **Two welcome tracks are non-negotiable** — subscriber (Track A, 7 emails) vs. purchaser (Track B, 5 emails) must be separate flows.
4. **Founder voice everywhere** — "Nilo" not "The IonWave Team" across all flow emails.
5. **PP6/PP7 moved to campaigns** — not part of post-purchase flow; depend on business timing, not customer lifecycle.
6. **BCL-4 is now COMPLETE** — 2nd cluster finished (after BCL-5). 6/6 TUPs done.

### Innovations (for future OpKit/TUP use)

- **Subscription Conversion Decision Tree**: Maps every subscription touchpoint across all flows with escalation logic and fatigue rules
- **Pre-Churn Intervention**: Cancel-reason-specific retention emails within 1-2 hours (vs. waiting 60 days for win-back)
- **Abandoned Checkout as separate flow**: Higher intent → faster cadence (15 min vs 1 hr)
- **Auto-apply incentives**: No discount codes. Pre-applied free shipping converts 15-20% better.
- **Domain warm-up protocol**: 2-4 week gradual volume increase from new sending domain
- **Engagement segments as deliverability armor**: Campaigns target Engaged 30d/90d only

### Next Steps

- BCL-4 complete. Consider BCL-6 next (2/8 done: M9, M10). Or BCL-3 (3/8 done: M14, M25, M26).
- Total progress: 18/41 TUPs (43.9%), 22 OpKits

---

## Session 2026-02-09 — M9 Ecommerce Infrastructure Workshop (Session G cont.)
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Workshopped M9 Ecommerce Infrastructure — 10 Danilo tabs (274 rows) consolidated into 4 production files, quality 8.5/10. Created OpKit OK-M9-001. 6-round persona dialogue with 14 upgrades applied. BCL-6 now 2/8 complete. Total: 17/41 TUPs workshopped, 21 OpKits.

### Decisions Made
- **10→4 consolidation**: Merged 285/288 (duplicate tool stacks), 289/290 (duplicate page speed checklists). 292 (credentials) absorbed into tech stack. 291/293/294 merged into operations governance
- **MER > ROAS correction**: Danilo tab 287 referenced "blended ROAS" as north star — corrected to MER per M30 U2 alignment
- **Google Optimize replaced**: Shut down Sep 2023. Replaced with Shoplift/Intelligems ($74/mo) as Shopify-native alternatives
- **INP replaces FID**: Updated Core Web Vitals targets to 2026 standards (INP replaced FID March 2024)
- **Theme performance budget**: Hard limits — 8 apps max, 500KB JS, 3 external scripts, 2 custom fonts
- **Week 1 Setup Sequence**: Day-by-day priority order to prevent 3-week launch delays
- **Subscription-first UX**: Toggle > dropdown (15-20% conversion lift), subscription price shown first, pre-selected
- **Phase-gated governance**: Month 0-1 essentials only. Quarterly audits unlock at Month 3
- **Ad account hijacking**: Elevated as #1 real threat for D2C. Meta spend cap at 2x daily budget
- **Do Not Install list**: SEO apps, currency converters, social proof pop-ups — all redundant with Shopify native

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | claimed | `ACTIVE_WORK.md` | Session G: M9 Ecommerce Infra workshop |
| 2 | read | `295_v_m9.json`, `283_c_m9.json`, `284_ip_m9.json` | Structural tabs (V, C, IP) |
| 3 | read | `285-294` (all 10 content tabs) | Inventoried: 3 STRONG, 1 GOOD, 1 Moderate, 2 DUPLICATE, 1 THIN, 1 Template, 1 Scaffold |
| 4 | checkpoint | Phase 3 | 10→4 consolidation approved |
| 5 | researched | Web | Shopify 2026 pricing, CWV 2026, A/B testing alternatives, server-side tracking |
| 6 | created | `data/m9/tech_stack_and_tools.md` | Phase-gated stack (Core/Growth/Scale), costs, credential template, performance budget |
| 7 | created | `data/m9/store_setup_and_launch.md` | Week 1 sequence, 8-section checklist, subscription UX, CWV targets, speed optimization |
| 8 | created | `data/m9/tracking_and_attribution.md` | MER north star, pixel+CAPI, UTMs, attribution, consent management |
| 9 | created | `data/m9/operations_governance.md` | Security, ad hijacking prevention, folder structure, naming, phase-gated governance |
| 10 | dialogue | 3 personas × 6 rounds | 14 upgrades, 0 unresolved. Saturation at Round 6 |
| 11 | edited | All 4 content files | Applied 14 dialogue upgrades (U1-U14) |
| 12 | created | `data/m9/dialogue_summary.md` | Summary of dialogue, upgrades, themes |
| 13 | graded | Phase 7 | 8.5/10 — strong actionability and cross-TUP alignment |
| 14 | created | `data/m9/opkit_ecommerce_infrastructure.md` | OK-M9-001 with 14 steps, rubric, scaffold, adaptation guide |
| 15 | created | `data/m9/_meta.json` | Full metadata |
| 16 | edited | `data/manifest.json` | M9: status→migrated, 8.5/10, migrated_tups 15→16 |
| 17 | edited | `data/opkits/registry.json` | OK-M9-001 registered, unmapped_tups M9 updated |
| 18 | edited | `tracking/TUP_Workshop_Tracker.md` | M9 DONE (8.5/10), BCL-6 2/8, workshopped 17/41, 21 OpKits |
| 19 | edited | `data/hypotheses/index.json` | HYP-001 +1 ref (→14), HYP-002 +1 ref (→12), +2 doc entries, +1 context doc. Metadata: 60→62 docs, 142→144 refs |
| 20 | cleared | `ACTIVE_WORK.md` | M9 workshop complete |

### Next Steps
- [ ] Continue BCL-6: Next recommended — M24 (Fulfillment, 10 tabs, M size) or M1 (Labor, 16 tabs, L size)
- [ ] BCL-4 nearly complete: Only M18 (SMS) remains (scope reduced, M17 absorbed most)
- [ ] Consider M24 Fulfillment next — same cluster, moderate size, clean scope

---

## Session 2026-02-08 — M30 Analytics & Dashboards Workshop (Session G)
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Started**: ~2026-02-08
**Status**: ✅ Complete

### Summary
Started BCL-6 (Operations & Infra) cluster. Workshopped M30 (Analytics & Dashboards) using TWP-001 v2.0.0 protocol — all 11 phases completed. M30 is the measurement backbone — defines how all other TUPs' strategies are monitored. 9 tabs consolidated to 4 files. Total workshopped: 16/41 TUPs, 20 OpKits.

### What Happened
1. **M30 Phase 1-2**: Loaded 9 Danilo content tabs (627-635, ~161 rows). Significant duplication across dashboard tabs (629/630/631).
2. **M30 Phase 3**: Checkpoint — proposed 9→4 consolidation. User approved.
3. **M30 Phase 4-5**: Created 4 output files:
   - `data_dictionary.md` (tab 627) — 50+ metrics with formulas, sources, cadences, known limitations
   - `dashboards_and_reporting.md` (tabs 628, 629, 630, 631) — MVD, daily pulse, weekly/monthly/quarterly reports
   - `red_flags_and_validation.md` (tabs 632, 633) — Kill criteria, escalation, validation rules
   - `data_governance.md` (tabs 634, 635) — Freshness cadences, evidence logging, source hierarchy
4. **M30 Phase 6**: 6-round persona dialogue (D2C Operator, Growth Engineer, Skeptical Investor). 13 upgrades, 0 unresolved. Saturation at Round 6.
5. **Applied 13 upgrades**: U1 (MVD — 7 metrics for Phase 1), U2 (MER primary over ROAS), U3 (existential vs monitoring kill criteria), U4 (awareness vs conversion attribution), U5 (simplified MBR for Months 1-3), U6 (Google Sheets MVD template OpKit), U7 (data source known limitations), U8 (V0 master consistency check), U9 (email revenue % phase-gated to Month 3+), U10 (subscription conversion diagnostic tree), U11 (graceful degradation), U12 (vanity metrics ban), U13 (monthly hypothesis prompt).
6. **M30 Phase 7**: Self-grade 8.2/10.
7. **M30 Phase 8-9**: OpKit OK-M30-001 (Analytics & Measurement Kit) created, registered.
8. **M30 Phase 10**: Hypothesis cross-reference — HYP-001 (+2 refs to 13), HYP-003 (+2 refs to 13). Added 3 document_to_hypotheses entries + 1 context document.
9. **M30 Phase 11**: Session log, ACTIVE_WORK.md cleared.

### Key Decisions
- **MVD (7 metrics only for Phase 1)**: Revenue, Orders, Ad Spend, CAC, Subscription Rate, Cash, MER. Everything else phase-gated.
- **MER over ROAS**: MER (Total Revenue / Total Marketing) is primary efficiency metric. ROAS demoted to "platform context only" — overstates by 20-40% post-iOS 14.5.
- **Existential vs Monitoring**: 3 existential kill criteria (Cash Runway <30 days, CAC >$60 for 14 days, Contribution Margin negative 30 days). All other 9 are monitoring.
- **Attribution model**: Awareness attribution (survey — how they found you) vs conversion attribution (UTM — what drove the click). Disagreement = multi-touch, not error.
- **Simplified MBR**: Months 1-3 = 4 questions, 1 hour max. Full 8-section MBR at Month 4+.
- **V0 Master Consistency Check**: Kill criteria source of truth (M0 Thesis) must match M30 Red Flag Dashboard thresholds — checked FIRST every month.
- **Graceful degradation**: Daily Pulse is NON-NEGOTIABLE (5 min/day). Everything else can be recovered.
- **Vanity metrics banned from Phase 1**: Social followers, pageviews, engagement rate, "brand awareness" metrics.
- **Email Revenue % phase-gated**: Don't track until 1K+ subscribers AND 60+ days of sending.

### Files Changed

| # | Action | File | What Changed |
|---|--------|------|-------------|
| 1 | created | `data/m30/data_dictionary.md` | 50+ metrics, attribution model (U2, U4) |
| 2 | created | `data/m30/dashboards_and_reporting.md` | MVD (U1), daily pulse, MBR (U5), vanity ban (U12), hypothesis prompt (U13), email phase-gate (U9) |
| 3 | created | `data/m30/red_flags_and_validation.md` | Existential/monitoring (U3), diagnostic tree (U10), V0 check (U8) |
| 4 | created | `data/m30/data_governance.md` | Source hierarchy + limitations (U7), graceful degradation (U11) |
| 5 | created | `data/m30/dialogue_summary.md` | 6 rounds, 13 upgrades, saturation at Round 6 |
| 6 | created | `data/m30/opkit_analytics_measurement.md` | OK-M30-001: 14-step how-to, rubric, scaffold, graded example |
| 7 | created | `data/m30/_meta.json` | TUP metadata |
| 8 | edited | `data/manifest.json` | M30 status→migrated, quality 8.2/10, migrated_tup_count 15 |
| 9 | edited | `data/opkits/registry.json` | OK-M30-001 registered, unmapped_tups M30 updated |
| 10 | edited | `tracking/TUP_Workshop_Tracker.md` | M30 DONE (8.2/10), BCL-6 1/8, workshopped 16/41, 20 OpKits |
| 11 | edited | `data/hypotheses/index.json` | HYP-001 +2 refs (13 total), HYP-003 +2 refs (13 total), +3 doc entries, +1 context doc |
| 12 | edited | `ACTIVE_WORK.md` | Claimed then cleared M30 scope |

### Next Steps
- [ ] Continue BCL-6: M9 (Ecommerce Infra, 10 tabs) or M24 (Fulfillment, 10 tabs)
- [ ] Consider M35 (Execution Plans, 25 tabs, L) or M1 (Labor, 16 tabs, L) for deeper BCL-6 progress
- [ ] Avoid M31 (30 tabs, XL) and M36 (43 tabs, XL) until ready for heavy sessions

---

## Session 2026-02-08 — M28 Market Expansion Workshop (Session F continuation)
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Started**: ~2026-02-08
**Status**: ✅ Complete

### Summary
Continued session F (previously completed M23 Influencer & Creator). Workshopped M28 (Market Expansion) using TWP-001 v2.0.0 protocol — all 11 phases completed. M28 is the largest TUP workshopped to date (20 content tabs, ~464 rows). This completes BCL-5 cluster (7/7), the first fully finished cluster. Total workshopped: 15/41 TUPs, 19 OpKits.

### What Happened
1. **M28 Phase 1-2**: Loaded 20 Danilo content tabs (592-611, ~464 rows). Significant duplication identified (606/607 Amazon near-duplicates, 608/609/610 Amazon-adjacent).
2. **M28 Phase 3**: Presented checkpoint — proposed 20→9 output file consolidation. User approved.
3. **M28 Phase 4-5**: Created 9 output files:
   - `strategic_landscape.md` (tabs 592, 593, 594) — SWOT, vulnerability inventory, science library
   - `channel_strategy.md` (tabs 595, 610) — 13-channel matrix, PPC architecture
   - `expansion_paths.md` (tabs 596, 597) — 8-path matrix, new product readiness
   - `constraint_scenarios.md` (tabs 598, 599) — 4 extreme scenarios, portfolio reality check
   - `product_development.md` (tabs 600, 601, 602) — taste, mixability, feature requests
   - `moonshot_lab.md` (tab 603) — 20 creative ideas, evaluation framework
   - `b2b_wholesale.md` (tabs 604, 605) — B2B segments, partnerships, pricing
   - `amazon_playbook.md` (tabs 606, 607, 608, 609) — Amazon economics, listing, reviews, PPC
   - `retail_readiness.md` (tab 611) — 5 retail tiers, readiness checklist, economics
4. **M28 Phase 6**: 7-round persona dialogue (Skeptical Investor, Growth Engineer, Retail/Channel Veteran). 14 upgrades, 0 unresolved. Saturation at Round 7.
5. **Applied 14 upgrades**: U1 (Amazon price parity & anti-cannibalization), U2 (multi-touch attribution), U3 (B2B reorder automation), U4 (capital requirements for retail), U5 (VOC pipeline for product triggers), U6 (Amazon cold start strategy), U7 (moonshot activation lock), U8 (SEO sequencing revised to Phase 2), U9 (MAP pricing policy), U10 (planned vs unplanned concentration), U11 (white label guardrails), U12 (subscription conversion sensitivity), U13 (product iteration cycle), U14 (B2B unit economics model).
6. **M28 Phase 7**: Self-grade 8.3/10.
7. **M28 Phase 8-9**: OpKit OK-M28-001 (Market Expansion Kit) created, registered in registry.json, manifest.json, tracker.
8. **M28 Phase 10**: Hypothesis cross-reference — HYP-002 (+2 refs to 11), HYP-004 (+3 refs to 10), HYP-006 (+3 refs to 12). Added 7 document_to_hypotheses entries + 1 context document.
9. **M28 Phase 11**: Session log, ACTIVE_WORK.md cleared.

### Key Decisions
- **Anti-cannibalization strategy**: D2C subscription always best deal > Amazon S&S > wholesale MAP. Price parity enforced. Bridge card in Amazon shipments.
- **Amazon cold start**: 4-phase plan (seed from D2C email list → long-tail PPC → Vine program → broaden PPC after 50+ reviews)
- **MAP pricing**: $44.10 floor (10% below $49 MSRP). Violation = warning → 30-day hold → termination. Required in all wholesale agreements.
- **B2B auto-reorder**: Default = auto-ship. One-click reorder link. 5% discount for auto-reorder. Target <20% quarterly churn (vs 60-70% without).
- **B2B unit economics**: $200 acquisition, $588/mo revenue, $275/mo net margin, 13.2x LTV:CAC at 80% retention.
- **Moonshot activation lock**: <$50K MRR = READ-ONLY (capture ideas only), $50-100K = evaluate 2 hrs/week max, >$100K = 1 experiment/quarter capped at 5% monthly revenue.
- **White label guardrails**: Never hero SKU, 1K min volume, territory exclusions, annual review clause, cost-plus pricing only, $100K MRR gate.
- **SEO timing**: Phase 2 (Month 3-6), NOT pre-launch. Every pre-launch hour must drive Day 1 revenue.
- **Subscription conversion sensitivity**: Viable to 30%, YELLOW at 20%, crisis at 10%.
- **Planned vs unplanned concentration**: Month 1-3 = planned concentration (no alerts), Month 6+ = standard rules.
- **Product iteration**: Quarterly review cadence + annual deep review. Reformulation gate: >60% "equal or prefer" in 50+ subscriber blind test.

### Files Changed

| # | Action | File | What Changed |
|---|--------|------|-------------|
| 1 | created | `data/m28/strategic_landscape.md` | SWOT analysis, vulnerability inventory, science library with claims hierarchy |
| 2 | created | `data/m28/channel_strategy.md` | 13-channel matrix, PPC architecture, attribution model (U2), concentration rules (U10) |
| 3 | created | `data/m28/expansion_paths.md` | 8-path matrix, new product readiness, white label guardrails (U11) |
| 4 | created | `data/m28/constraint_scenarios.md` | 4 extreme scenarios, sensitivity table, SEO sequencing (U8), subscription sensitivity (U12) |
| 5 | created | `data/m28/product_development.md` | Taste profiles, mixability specs, VOC pipeline (U5), iteration cycle (U13) |
| 6 | created | `data/m28/moonshot_lab.md` | 20 ideas, evaluation framework, activation lock (U7) |
| 7 | created | `data/m28/b2b_wholesale.md` | B2B segments, MAP policy (U9), auto-reorder (U3), unit economics (U14) |
| 8 | created | `data/m28/amazon_playbook.md` | Amazon economics, anti-cannibalization (U1), cold start (U6), listing, reviews |
| 9 | created | `data/m28/retail_readiness.md` | 5 retail tiers, capital requirements (U4), margin waterfall, distributor guide |
| 10 | created | `data/m28/dialogue_summary.md` | 7-round dialogue, 14 upgrades, saturation at Round 7 |
| 11 | created | `data/m28/opkit_market_expansion.md` | OK-M28-001: 14-step how-to, rubric, scaffold, graded example |
| 12 | created | `data/m28/_meta.json` | TUP metadata |
| 13 | edited | `data/manifest.json` | M28 status→migrated, quality 8.3/10, migrated_tup_count 14 |
| 14 | edited | `data/opkits/registry.json` | OK-M28-001 registered, unmapped_tups M28 updated |
| 15 | edited | `tracking/TUP_Workshop_Tracker.md` | M28 DONE (8.3/10), BCL-5 7/7 COMPLETE, workshopped 15/41, 19 OpKits |
| 16 | edited | `data/hypotheses/index.json` | HYP-002 +2 refs (11 total), HYP-004 +3 refs (10 total), HYP-006 +3 refs (12 total), +7 doc entries, +1 context doc |
| 17 | edited | `ACTIVE_WORK.md` | Cleared M28 claim |

### Next Steps
- [ ] Start BCL-6 (Operations & Infra) — largest untouched cluster (148 tabs)
- [ ] Complete M7 (Regulatory) to unblock M23 Pre-Launch Compliance Package
- [ ] Update Summary Scoreboard in tracker to reflect current state
- [ ] Consider BCL-1 or BCL-2 (Strategic Foundation clusters) next

---

## Session 2026-02-08 — M23 Influencer & Creator Workshop (Session F continuation)
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Started**: ~2026-02-08
**Status**: ✅ Complete

### Summary
Continued session F (previously completed M17 Email & SMS). Provided TUP tracker overview at user's request before selecting next TUP. Workshopped M23 (Influencer & Creator) using TWP-001 v2.0.0 protocol — all 11 phases completed. BCL-5 now 6/7 done (only M28 remains).

### What Happened
1. **Tracker assessment**: Reviewed TUP_Workshop_Tracker at user's request. Noted stale Summary Scoreboard. Provided cluster-by-cluster status and recommended next targets.
2. **M23 Phase 1-2**: Loaded 15 Danilo content tabs (500-514, ~377 rows). Heavy duplication identified (tabs 500/508, 501/509, 503/511, 505/506/514 are near-duplicates).
3. **M23 Phase 3**: Presented checkpoint — proposed 15→7 output file consolidation. User approved.
4. **M23 Phase 4-5**: Created 7 output files:
   - `influencer_creator_strategy.md` (tabs 500, 501, 508, 509)
   - `creator_ugc_playbook.md` (tabs 502, 507)
   - `vetting_scorecard.md` (tabs 501, 510)
   - `influencer_map.md` (tab 513)
   - `contract_templates.md` (tabs 503, 504, 511)
   - `pipeline_operations.md` (tabs 505, 506, 514)
   - `influencer_database_scaffold.md` (tab 512)
5. **M23 Phase 6**: 8-round persona dialogue (Skeptical Investor, Growth Engineer, Regulatory/Compliance Auditor). 6 upgrades, 0 unresolved. Saturation at Round 8.
6. **Applied 6 upgrades**: U1 (attribution framework), U2 (FTC compliance package — GATING requirement), U3 (Phase 0/1/2 distinction), U4 (content retirement policy), U5 (pre-outreach competitive screening), U6 (revised repurposing multiplier + compliance checkpoints).
7. **M23 Phase 7**: Self-grade 8.0/10.
8. **M23 Phase 8-9**: OpKit OK-M23-001 created, registered in registry.json, manifest.json, tracker.
9. **M23 Phase 10**: Hypothesis cross-reference — HYP-006 (+2 refs to 9), HYP-001 (+1 ref to 11). Added 3 document_to_hypotheses entries + 1 context document.
10. **M23 Phase 11**: Session log, ACTIVE_WORK.md cleared.

### Key Decisions
- **Attribution framework**: Track both direct (code redemptions) and indirect (branded search lift) to avoid undercounting influencer value
- **Pre-Launch Compliance Package**: 4-component package (talking points, prohibited claims, monitoring, violation response) is NON-NEGOTIABLE gating requirement before any seeding
- **Phase 0/1/2 distinction**: Phase 0 = product seeding (COGS only), Phase 1 = UGC creators (IS the ad creative budget), Phase 2 = paid influencer deals (gated by >1.5x ROAS)
- **Content retirement policy**: Semi-annual UGC audit, retire problematic content, archive inactive
- **Repurposing multiplier**: Revised down from 8-12 to 6-10 assets per video (primary vs secondary derivatives)

### Files Changed

| # | Action | File | What Changed |
|---|--------|------|-------------|
| 1 | created | `data/m23/influencer_creator_strategy.md` | Master strategy: influencer vs creator distinction, tiers, deal structures, Founder Mode phasing with Phase 0/1/2 gates |
| 2 | created | `data/m23/creator_ugc_playbook.md` | UGC sourcing, briefing, repurposing system with compliance checkpoints |
| 3 | created | `data/m23/vetting_scorecard.md` | Weighted 7-criteria scorecard, red flags, vetting tools |
| 4 | created | `data/m23/influencer_map.md` | IonWave-specific Tier 1/2/3 influencer targets with competitive screening |
| 5 | created | `data/m23/contract_templates.md` | Influencer + creator contract templates with FTC compliance package |
| 6 | created | `data/m23/pipeline_operations.md` | Pipeline stages, trackers, attribution framework, operational cadence |
| 7 | created | `data/m23/influencer_database_scaffold.md` | Performance database schema (VOID — needs real data) |
| 8 | created | `data/m23/dialogue_summary.md` | 8-round dialogue, 6 upgrades, saturation at Round 8 |
| 9 | created | `data/m23/opkit_influencer_creator.md` | OK-M23-001: 14-step how-to, rubric, scaffold, graded example |
| 10 | created | `data/m23/_meta.json` | TUP metadata |
| 11 | edited | `data/manifest.json` | M23 status→migrated, quality 8.0/10, migrated_tup_count 13 |
| 12 | edited | `data/opkits/registry.json` | OK-M23-001 registered, unmapped_tups M23 updated |
| 13 | edited | `tracking/TUP_Workshop_Tracker.md` | M23 DONE (8.0/10), BCL-5 6/7, workshopped 14/41, 18 OpKits |
| 14 | edited | `data/hypotheses/index.json` | HYP-006 +2 refs (9 total), HYP-001 +1 ref (11 total), +3 doc entries, +1 context doc |
| 15 | edited | `ACTIVE_WORK.md` | Cleared M23 claim |

### Next Steps
- [ ] Workshop M28 (Market Expansion, 20 tabs, L) to complete BCL-5
- [ ] Start BCL-6 (Operations & Infra) — largest untouched cluster (148 tabs)
- [ ] Complete M7 (Regulatory) to unblock M23 Pre-Launch Compliance Package
- [ ] Update Summary Scoreboard in tracker to reflect current state

---

## Session 2026-02-07 — M19 Customer Lifecycle & CRM Workshop
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Duration**: Extended session (continued across 3 context windows)
**Status**: COMPLETE

### Summary
Completed full TWP-001 workshop for M19 (Customer Lifecycle & CRM). 13 Danilo content tabs (232 rows) consolidated into 4 production content files + dialogue summary + OpKit. Quality: 8.4/10. 5-round persona dialogue with 8 upgrades applied, 0 unresolved. BCL-4 cluster now 5/6 complete (only M18 SMS remaining).

### Key Innovations
- **"Model IS the CRM" architecture**: Every customer-facing TUP is a node in a single CRM system — no separate CRM platform needed at launch
- **Non-linear lifecycle paths (U3)**: Shortcuts (influencer impulse buy skips Aware→Interested→Considering), oscillations (At-Risk ↔ Retained), and skip-ahead transitions acknowledged
- **Minimum Viable CRM (U2)**: Only 3 flows for Day 1 (Welcome, Post-Purchase, Abandoned Cart) — 8-11 hours setup vs. 3 weeks for all 10 flows
- **At-risk sub-segmentation (U5)**: Split into At-Risk (Product), At-Risk (Budget), At-Risk (Attention) with distinct intervention strategies
- **Churn risk score formula (U7)**: Phase 1 (simple days-since-purchase ratio) and Phase 2 (4-signal weighted model: purchase velocity 30%, email engagement 25%, subscription modifications 25%, support sentiment 20%)
- **Confidence intervals on cohort data (U1)**: 50 customers = ±14% CI at 40% retention — can't distinguish healthy from concerning at small sample sizes
- **Customer-count tool triggers (U4)**: Analytics tools gated on 500+ customers, not revenue milestones ($149/month at $5K/month revenue = 3% overhead)
- **Founder daily 5-minute CRM check-in (U8)**: Shopify Home (1 min), Klaviyo Dashboard (1 min), Gorgias Inbox (2 min), Recharge Dashboard (1 min)
- **Seasonality in churn metrics (U6)**: January resolution fade, summer routine disruption. 3-month rolling averages for channel grading
- **Dual-layer segmentation**: Behavioral (8 segments for daily automation) + RFM (10 segments for advanced targeting at 500+ customers)

### Files Created
- `data/m19/crm_architecture.md` — CRM philosophy, phase-gated stack, 10-stage lifecycle, cross-TUP data flows, 19-field customer data model
- `data/m19/lifecycle_and_segmentation.md` — 8 lifecycle stages, 10 email flows, MVC, behavioral + RFM segmentation, at-risk sub-segments
- `data/m19/ltv_and_cohort_analysis.md` — 3 LTV methods, LTV by source, cohort framework with confidence intervals, churn risk formula
- `data/m19/crm_metrics_and_dashboards.md` — Funnel health + relationship depth metrics, decision triggers, daily/weekly/monthly/quarterly dashboards
- `data/m19/dialogue_summary.md` — 5 rounds, 3 personas, 8 upgrades, saturation achieved
- `data/m19/opkit_customer_lifecycle.md` — OK-M19-001: 8-step instruction doc, grading rubric, 3 scaffolds
- `data/m19/_meta.json` — Full metadata with 8 intelligence gaps

### System Files Updated
- `data/manifest.json` — M19 status → migrated, quality 8.4/10, migrated_tups 12→13
- `data/opkits/registry.json` — OK-M19-001 registered with 6 components
- `data/hypotheses/index.json` — 4 M19 documents + 1 context document added; total_documents 43→47, total_context_documents 11→12, total_references 113→127
- `tracking/TUP_Workshop_Tracker.md` — M19 DONE, workshopped 13/41, BCL-4 5/6, 17 OpKits across 13 TUPs
- `ACTIVE_WORK.md` — Claimed at start, cleared at end

### Hypothesis Impact
- **HYP-001 (CAC)**: LTV:CAC measurement framework enables channel-level acquisition efficiency decisions
- **HYP-002 (Subscription)**: Lifecycle stage transitions define subscription conversion points; segmentation identifies high-propensity targets
- **HYP-003 (Churn)**: Multi-signal churn risk formula, at-risk sub-segmentation, and churn prevention priority stack
- **HYP-005 (LTV)**: Three LTV calculation methods with progression path; LTV by acquisition source tracking
- **HYP-006 (Retention)**: Cohort analysis framework with confidence intervals; retention benchmarks by month

### Next Steps
- **M18 (SMS)** is the last remaining BCL-4 TUP — M17 absorbed most SMS scope, so M18 may be a thin supplement or marked absorbed
- **BCL-4 completion**: 5/6 done. Completing M18 would make BCL-4 the first fully workshopped cluster
- **M23 (Influencer & Creator)** workshop claimed by Session F — in progress concurrently

---

## Session 2026-02-07 — M16 Merge + M29 PR Workshop + M17 Email Workshop
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Duration**: Extended session (continued from context-compacted session)
**Status**: COMPLETE

### Work Performed

**1. M16 Content & SEO Merge (completed in prior context)**
- Merged Session A's unique content into Session B's canonical M16 files
- Added Content Conversion Funnel (§4.5), MVC section, content calendar, content measurement
- Updated seo_strategy.md with organic target revisions and ROI breakeven calibration
- Preserved both session's dialogue summaries
- Deleted duplicate m16_content_seo/ directory

**2. M29 PR & Communications Workshop (completed in prior context)**
- 7 Danilo tabs (208 rows) → 4 production files
- Quality: 7.6/10, OK-M29-001 registered
- 5-round dialogue, 5 upgrades, 0 unresolved
- Key: weekly PR time budget, tiered media targets, podcast deferral, crisis playbook

**3. M17 Email & SMS Workshop (completed in this context)**
- 27 Danilo source files (~600+ rows, 11 content tab groups) → 9 production files + dialogue + OpKit
- Quality: 8.4/10, OK-M17-001 registered
- 7-round dialogue (Skeptical Investor, Growth Engineer, Operations Expert), 5 upgrades, 0 unresolved
- **Key innovations:**
  - Founder Mode build order: 3 flows at launch (Cart, Welcome, Post-Purchase Basic), expand monthly
  - Discount defense policy: different incentive types per flow (% off ≠ free shipping ≠ big discount), time-gated escalation, no code stacking
  - FTC compliance checklist for supplement health claims in post-purchase emails
  - Segmentation trigger thresholds (don't segment until data warrants: source >30% AND list >500)
  - Maintenance time budget (1.5 hrs/month for 3 launch flows, 3-4 hrs/month at full 12 flows)
  - Source of Truth policy (markdown = build blueprint, Klaviyo = live source of truth)
  - SMS deferred to Month 3+ (collect opt-ins from Day 1, send from 500+ subscribers)
  - Box insert kit from Day 1 ($0.50-0.70/package, referral ROI 7.8x)
  - M17 absorbed SMS scope from M18 — M18 may be reduced to thin supplement

### Files Created
- `data/m17/email_flow_architecture.md` — 12-flow lifecycle engine with build order, benchmarks, maintenance budget
- `data/m17/email_segmentation.md` — lifecycle + engagement + source segments with trigger thresholds
- `data/m17/email_welcome_series.md` — canonical 5-email welcome with production copy
- `data/m17/email_abandoned_cart.md` — 3-email cart recovery with discount defense policy
- `data/m17/email_post_purchase.md` — 7-email onboarding with FTC compliance checklist
- `data/m17/email_winback.md` — 4-email re-engagement + sunset sequence
- `data/m17/email_subject_lines.md` — 11 formula types, flow-specific variants, A/B framework
- `data/m17/sms_strategy.md` — TCPA compliance, channel selection, templates, timeline
- `data/m17/physical_touchpoints.md` — box insert kit + direct mail strategy
- `data/m17/dialogue_summary.md` — 7 rounds, 5 upgrades, saturation at Round 7
- `data/m17/opkit_email_lifecycle.md` — OK-M17-001 reusable kit
- `data/m17/_meta.json` — TUP metadata

### System Files Updated
- `data/manifest.json` — M17 status → migrated, quality 8.4/10, migrated_tups → 12
- `data/opkits/registry.json` — OK-M17-001 registered, unmapped_tups updated
- `tracking/TUP_Workshop_Tracker.md` — M17 DONE, workshopped 12/41, 16 OpKits across 12 TUPs
- `data/hypotheses/index.json` — Added M17 references to HYP-001 (+1), HYP-002 (+1), HYP-003 (+2), HYP-005 (+1), dialogue as context document. Total: 43 docs, 11 context docs, 113 references
- `ACTIVE_WORK.md` — Claimed M17 at start, cleared at end

### Hypothesis Impact
- **HYP-001 (CAC)**: Email flows reduce blended CAC by generating $0 marginal acquisition cost conversions
- **HYP-002 (Subscription)**: Post-purchase Email 4 is primary subscription conversion touchpoint
- **HYP-003 (Churn)**: Post-purchase onboarding is primary churn prevention; win-back recovers lapsed
- **HYP-005 (LTV)**: Email lifecycle engine drives LTV through 12 automated retention + upsell touchpoints

### Next Steps
- **M18 (SMS)** may be reduced scope — M17 absorbed SMS strategy. Evaluate if M18 is still needed or can be marked as "absorbed into M17."
- **M19 (Customer Lifecycle)** is the last remaining BCL-4 TUP — would complete the first full cluster
- **BCL-4 status**: 5/6 done (M17, M20, M21, M22 workshopped + M18 scope reduced). Close to first complete cluster.
- **Legal review needed**: FTC compliance checklist in email_post_purchase.md flags health claims that need review before launch

---

## Session 2026-02-07 — M20 Customer Support Workshop Complete
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Workshopped M20 (Customer Support) through full TWP-001 protocol. 9 Danilo content tabs (468-476, ~204 total rows) consolidated into 3 production files. Quality 8.6/10. Green-field build (no Bootstrap sources, only Danilo shell). Key achievements: Founder Mode vs Team Mode phase-gated escalation framework (solo founder reality for Month 0-6 vs team activation), chargeback monitoring section (Stripe 0.75% threshold — existential risk caught by persona dialogue), behavioral activation criteria (4 measurable criteria, self-report removed as gating), minimum viable support stack ($60/month vs $1,300/month with full tools), FDA adverse event reporting protocol (A-grade compliance), open-ended-first win/loss survey methodology with decision triggers and minimum sample sizes, expected outcomes timeline for marine plasma supplements, 6 support macros including adverse reaction escalation. Research agent deployed for DTC supplement support best practices (benchmarks, tool stacks, supplement-specific issues, refund policies, NPS/CSAT, retention impact, crisis management).

### Actions Taken
1. Read all 13 M20 source files (4 structural + 9 content tabs)
2. Presented Phase 3 Checkpoint (scope, consolidation plan, boundary decisions)
3. Ran Phase 4 Research (7 topics, 146 graded findings)
4. Created `data/m20/support_operations.md` — escalation, macros, refund policy, chargeback monitoring, adverse events, issue tracking, scorecard
5. Created `data/m20/customer_feedback_system.md` — NPS, CSAT, win/loss analysis with action playbooks and decision triggers
6. Created `data/m20/customer_success_playbook.md` — journey touchpoints, expected outcomes, activation criteria, at-risk signals, 11-star framework
7. Ran Phase 6 Dialogue (8 rounds, 3 personas — Skeptical Investor, Operations Expert, Customer Anthropologist): 6 UPGRADED, 2 RESOLVED, 0 UNRESOLVED
8. Applied 6 upgrades: U1 (expected outcomes timeline), U2 (Founder Mode/Team Mode), U3 (survey methodology + decision triggers), U4 (chargeback monitoring), U5 (behavioral activation), U6 (minimum viable stack)
9. Created `data/m20/dialogue_summary.md`
10. Self-graded at 8.6/10
11. Created `data/m20/opkit_customer_support.md` (OK-M20-001)
12. Created `data/m20/_meta.json`
13. Updated manifest.json (M20: not_migrated → migrated, counts 10→11)
14. Updated opkits/registry.json (OK-M20-001 registered)
15. Updated hypotheses/index.json (+3 M20 documents, +1 dialogue context doc, refs 95→107)
16. Updated TUP_Workshop_Tracker.md (BCL-4: 2/6→3/6, Wave 3 M20 crossed off)

### Key Findings
1. **Chargeback risk** — Supplements are high-risk for payment processors. Stripe's 0.75% dispute threshold can shut down payments. This was completely missing from Danilo's content.
2. **Premature tool spending** — Full support stack costs $1,300+/month. Minimum viable stack is $60/month (Gorgias Basic + Klaviyo flows).
3. **Behavioral activation** — Self-reported "noticing a difference" is unmeasurable at scale. Replaced with 4 behavioral criteria: received product, 3+ email engagements, no complaints by Day 14, confirmed 2nd order.
4. **FDA adverse event compliance** — 15-day SAE reporting is a legal requirement, not optional. Label must include domestic contact for AE reporting.
5. **Win/loss methodology** — Open-ended questions first, then categories. Category-first surveys confirm marketing messaging instead of revealing real purchase drivers.

### Next Steps
- Continue Wave 3: M17 (Email, 11 tabs), M18 (SMS, 12 tabs), M19 (Customer Lifecycle, 13 tabs)
- BCL-4 at 3/6 — 3 mediums remaining to complete the cluster
- M20 pre-launch priorities: legal review of adverse event protocol (CRITICAL), Gorgias setup, win/loss data collection after 100 orders

---

## Session 2026-02-06 — M25 Financial Operations Workshop Complete
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Workshopped M25 (Financial Operations / Bookkeeping) through full TWP-001 protocol. 6 Danilo content tabs (533-538, ~105 total rows) consolidated into 3 production files. Quality 8.8/10. Green-field build (no Bootstrap sources). Key achievements: dual-margin REC-001 treatment (gross margin for P&L reporting, contribution margin for channel payback decisions — resolves the dispute for M25 without picking a side), Day 1 Essentials 18-account chart of accounts (prevents overwhelm), Survival Five condensed MBR scorecard for solo founders in Month 2-6, phase-gated sales tax strategy (Shopify Tax → TaxJar → Avalara), 13-week cash forecast with example numbers, Synder/A2X connector gap elevated to CRITICAL priority with pre-launch validation step. Research agent deployed for DTC bookkeeping topics (Shopify+QBO integration, sales tax automation, ASC 606 revenue recognition, inventory accounting, chart of accounts best practices). Persona dialogue (8 rounds, 3 personas — Skeptical Investor, Operations Expert, Growth Engineer) produced 6 upgrades and reached saturation.

### Key Findings
1. **REC-001 resolution insight**: Danilo's 45% margin is likely contribution margin (including fulfilment + platform fees), not gross margin. Both numbers are correct for different decisions.
2. **Synder over A2X for subscription-first brands**: Synder handles recurring revenue recognition natively; A2X is summary-only. But this needs pre-launch validation (CRITICAL gap).
3. **Solo founder MBR is too long at 10 metrics**: Survival Five (cash runway, blended CAC, MRR, monthly churn, subscription attach) is sufficient for Month 2-6.
4. **40+ account chart overwhelms**: 18-account Day 1 Essentials subset is the right starting point. Add accounts as the business complexity grows.
5. **13-week cash forecast**: Describing it is not enough — founders need example numbers to replicate. Flagged Google Sheets template as Track B (requires human to build).

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Created | `data/m25/bookkeeping_setup.md` | QBO + Synder stack, chart of accounts (Day 1 Essentials + full), FIFO inventory, ASC 606 subscription revenue, monthly checklist, common mistakes |
| 2 | Created | `data/m25/unit_economics_tracking.md` | Channel economics dashboard, payback period (3 margin scenarios), monthly reporting, attribution, scale/hold/kill framework |
| 3 | Created | `data/m25/business_review_cadence.md` | Weekly cash check + 13-week forecast, MBR (Survival Five + full 10-metric), QBR (OKR framework), annual planning, hypothesis integration |
| 4 | Created | `data/m25/dialogue_summary.md` | 8 rounds, 3 personas, 6 upgrades, 0 unresolved |
| 5 | Created | `data/m25/opkit_financial_ops.md` | OK-M25-001: instructions, rubric, graded example (8.8/10), scaffolds for all 3 content types |
| 6 | Created | `data/m25/_meta.json` | Full metadata with revisions, dialogue ref, intelligence gaps |
| 7 | Updated | `data/manifest.json` | M25: not_migrated → migrated, migrated_tups 8→9, pending 33→32 |
| 8 | Updated | `data/opkits/registry.json` | OK-M25-001 registered, unmapped_tups.m25 → MIGRATED |
| 9 | Updated | `data/hypotheses/index.json` | 3 M25 docs added (bookkeeping, unit economics, business reviews), dialogue added to context_documents, total_documents 32→35, total_context_documents 7→8, total_references 78→92 |
| 10 | Updated | `tracking/TUP_Workshop_Tracker.md` | BCL-2: 0/4→1/4, M25 DONE, Wave 2 updated, scoreboard updated, change log added |
| 11 | Updated | `ACTIVE_WORK.md` | Cleared M25 claim |

### Next Steps
- [ ] Continue Wave 2: M29 (PR & Communications, 7 tabs) — in progress in separate session
- [ ] Pre-launch CRITICAL: Test Synder vs A2X with ReCharge sample transactions
- [ ] Pre-launch: Get 3PL fulfillment cost quotes
- [ ] Ask Danilo about the origin of 45% gross margin in tabs 534-535 (REC-001 clarification)
- [ ] Wave 3: M20 (Support, 9 tabs), M17 (Email, 11 tabs), M18 (SMS, 12 tabs)

---

## Session 2026-02-06 — M16 Content & SEO Workshop Complete
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Workshopped M16 (Content & SEO) through full TWP-001 protocol. 9 Danilo content tabs (408-415 + bonus 507, ~225 total rows) consolidated into 7 production files. Quality 8.4/10. Key achievements: YMYL/E-E-A-T infrastructure for supplement content, HARO replaced with current alternatives (Qwoted, Featured.com — Connectively/HARO shut down March 2025), marine plasma identified as uncontested SEO keyword territory, realistic Founder Mode publishing cadence (2 posts/month for solo founder), phase-gated channel activation preventing premature spend, native ads labeled as optional. 3 research agents deployed (DTC supplement SEO, content strategy, Shopify tools). Persona dialogue (8 rounds, 3 personas — Growth Engineer, Skeptical Investor, Category Expert) produced 5 material upgrades and reached saturation.

### Decisions Made
- Consolidated 8 Danilo tabs → 7 files (408 GTM + 409 Calendar merged into content_strategy.md; 414 Link Building + 415 Native Ads merged into seo_link_building.md)
- HARO (dead since March 2025) replaced with Qwoted, Featured.com, Terkel, SourceBottle
- Local SEO explicitly excluded (IonWave is national DTC, no physical location)
- Native ads phase-gated as optional (most DTC brands under $50K/month never use them)
- Founder Mode publishing tier: 2 posts/month at 4-5 hrs/week (realistic for solo founder)
- Publishing sequence corrected: pillar page first (Week 1), marine plasma content second (Week 2), LMNT Alternative moved to Week 3-4 (needs trust signals before comparison content)
- Marine plasma content justified via triple-purpose rationale: brand protection + topical authority + high CVR
- Conservative CVR scenario added to ROI projections (1.5% vs 3% base case)
- Google Merchant Center free product listings added to technical SEO checklist

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Created | `data/m16/content_strategy.md` | 10-channel strategy, phase-gated activation, weekly rhythm, AI content workflow, distribution, measurement |
| 2 | Created | `data/m16/seo_strategy.md` | SEO timeline, E-E-A-T infrastructure, competitive analysis, budget, ROI projections with conservative scenario |
| 3 | Created | `data/m16/seo_keyword_research.json` | 23 keywords in 3 phases by intent and KD, 6 keyword categories, tool recommendations |
| 4 | Created | `data/m16/seo_content_strategy.md` | 5 pillar/cluster models (34 cluster articles), 12-post launch sequence, blog templates, Founder Mode cadence |
| 5 | Created | `data/m16/seo_link_building.md` | 8 link building tactics ranked, native ads playbook (optional), quality criteria, monthly targets |
| 6 | Created | `data/m16/technical_seo_checklist.md` | Shopify-specific checklist, schema types, Google Merchant Center, tool stack |
| 7 | Created | `data/m16/content_repurposing.md` | Content waterfall model, checklists, library structure, tagging, production workflow |
| 8 | Created | `data/m16/dialogue_summary.md` | 8-round persona dialogue, 5 upgrades, 4 unresolved gaps |
| 9 | Created | `data/m16/opkit_content_seo.md` | OK-M16-001 instructions, rubric, scaffold, graded example |
| 10 | Created | `data/m16/_meta.json` | TUP metadata with revisions, quality score, intelligence gaps |
| 11 | Updated | `data/manifest.json` | M16 status not_migrated→migrated, full metadata, migrated_tups 7→8 |
| 12 | Updated | `data/opkits/registry.json` | OK-M16-001 registered with 9 components, unmapped_tups.m16 → MIGRATED |
| 13 | Updated | `data/hypotheses/index.json` | 5 M16 docs added to document_to_hypotheses (HYP-006, HYP-001), dialogue added to context_documents, metadata updated (27→32 docs, 6→7 context docs, 68→78 refs) |
| 14 | Updated | `tracking/TUP_Workshop_Tracker.md` | BCL-5: 3/7→4/7, M16 marked DONE, scoreboard 8 done/31 active/12 OpKits, Wave 2 M16 crossed off |
| 15 | Cleared | `ACTIVE_WORK.md` | M16 work zone claim removed |

### Key Findings
1. **HARO is dead** — Connectively (HARO's successor) shut down March 2025. Replacement platforms identified with realistic conversion rates (5-10% for unknown founders).
2. **Marine plasma = uncontested SEO territory** — Almost zero competition for marine plasma keyword terms. IonWave should build topical authority here first, then ladder into competitive terms.
3. **YMYL requires expert review infrastructure** — Every health claim needs PubMed citations, named authors with credentials, and expert review badges. Cost: $50-150 per article from freelance RD.
4. **Founder Mode is the honest starting cadence** — 1 post/week assumes a content hire or dedicated time block. Solo founder realistically produces 2 posts/month.
5. **SEO ROI is real but delayed** — Even conservative scenario (1.5% CVR) shows organic revenue exceeding cumulative investment by Month 24. The key is starting from Month 1.

### Next Steps
- [ ] Next TUP workshop: M29 (PR & Communications, 7 tabs — last small TUP in Wave 2) or M25 (Bookkeeping, 6 tabs)
- [ ] Verify keyword volumes with Google Keyword Planner or Ubersuggest post-launch
- [ ] Run PageSpeed Insights after Shopify theme selection
- [ ] Publish first blog post: "The Complete Guide to Electrolytes" (pillar page)

---

## Session 2026-02-06 — M14 Testing & Optimization Workshop Complete
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Workshopped M14 (Testing & Optimization) through full TWP-001 protocol. Near green-field build — Danilo's 7 tabs had only ~50 unique rows with 3 near-duplicates (379/380/381). Produced 6 content files, 1 dialogue summary, 1 OpKit (OK-M14-001). Quality 7.5/10. Google Optimize recommendation replaced with current Shopify-native tool landscape. 3 research agents deployed (low-traffic testing methodology, Shopify tool landscape, creative testing frameworks). Persona dialogue (4 rounds, 3 personas — CRO Statistician, Bootstrapped DTC Founder, Growth Hacker — 9 upgrades) reached saturation. Key innovations: two-stage kill criteria with 50+ click minimum, traffic-based methodology selection, tool spend ≤5% discipline, passive audience learning from Meta breakdowns.

### Decisions Made
- Near green-field build approach (Danilo source too thin for enhancement — built from research + first principles)
- Consolidated 3 near-duplicate A/B testing tabs (379/380/381) into single `ab_testing_framework.md`
- Google Optimize (shut down Sep 2023) replaced with Neat A/B, Shoplift, Intelligems
- Price testing deferred to M10 protocol (already exists) — M14 covers everything else
- Two-stage kill criteria: leading indicators at Day 3 (1,000+ impressions), conversion at Day 5-7 (50+ link clicks minimum)
- Traffic-based methodology: Phase 0 (<30/day) qualitative → Phase 1 (30-100/day) Bayesian → Phase 2 (100-500/day) standard A/B → Phase 3 (500+/day) full experimentation
- Tool spend discipline: never exceed 5% of monthly ad budget on testing tools

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Read | Danilo sources (372-382) | Loaded all M14 project, contract, IP, verification, and 7 content tabs |
| 2 | Created | `data/m14/experimentation_framework.json` | Core philosophy, experiment card, priority matrix, traffic-based methodology, statistical rules |
| 3 | Created | `data/m14/test_log.json` | Operational log with PT-000 results, PT-001 active, 4-test planned queue |
| 4 | Created | `data/m14/creative_testing_protocol.md` | Ad creative testing hierarchy, Meta campaign structure, kill/scale protocol, benchmarks |
| 5 | Created | `data/m14/ab_testing_framework.md` | On-site A/B testing (consolidated from 3 duplicate tabs), tool comparison |
| 6 | Created | `data/m14/audience_testing_strategy.md` | 6 audience tiers, phased rollout, retargeting, passive learning |
| 7 | Created | `data/m14/testing_infrastructure.md` | Phased tool stack ($0→$200/mo), setup checklist, tool spend discipline |
| 8 | Applied | UPG-1 to UPG-9 | 9 dialogue upgrades across 5 content files |
| 9 | Created | `data/m14/dialogue_summary.md` | 4 rounds, 3 personas, 9 upgrades, saturation |
| 10 | Created | `data/m14/opkit_testing_optimization.md` | OK-M14-001 — Testing & Optimization Kit |
| 11 | Created | `data/m14/_meta.json` | TUP metadata with revision history |
| 12 | Edited | `data/hypotheses/validation_log.json` | Added LOG-021 (M14→HYP-001 evidence contribution) |
| 13 | Edited | `data/hypotheses/index.json` | Added 3 M14 documents to document_to_hypotheses, M14 dialogue to context_documents, updated HYP-001 references (7→9), updated metadata (27 docs, 6 context, 68 refs) |
| 14 | Edited | `tracking/TUP_Workshop_Tracker.md` | BCL-3: 0/5→1/5, M14 row DONE, scoreboard 7 done / 32 active, 11 OpKits |
| 15 | Edited | `data/manifest.json` | M14 migrated, migrated_tups 6→7 |
| 16 | Edited | `data/opkits/registry.json` | OK-M14-001 registered with full component mapping |
| 17 | Edited | `ACTIVE_WORK.md` | Cleared M14 claim |

### Key Findings
1. **Danilo source quality was lowest of any TUP** — 7 tabs but 3 near-duplicates and ~50 unique rows. Treated as green-field build with extensive web research.
2. **Google Optimize is dead** — Danilo recommended it (shut down Sep 2023). Current landscape: Neat A/B (free/$29), Shoplift (free/$49, Bayesian), Intelligems ($99, real price testing).
3. **Low-traffic A/B testing is largely impractical** — At 2,000 monthly visitors / 3% CVR, detecting 20% effect requires 6.5 months. Traffic-based methodology tiers are the solution.
4. **PT-000 was directional, not definitive** — +23% RPV at ~2,500 visitors / ~75 conversions. Standard requirement: ~6,500/variant for 23% effect detection at 3% CVR.
5. **Premature creative kills are the #1 testing mistake** — Two-stage kill criteria with 50+ link click minimum prevents killing creatives before they've had enough data to convert.

### Next Steps
- [ ] Run CT-001 (problem vs ingredient hooks) — can run immediately, $100-200 budget
- [ ] Await PT-001 completion ($49 vs $59) before LP-001 (subscription-first layout test)
- [ ] Next Wave 2 TUPs: M29 (PR), M16 (Content & SEO), M25 (Bookkeeping)

---

## Session 2026-02-06 — M22 Referral & Community Workshop Complete
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Workshopped M22 (Referral & Community) through full TWP-001 protocol across two context windows. Produced 6 content files, 1 dialogue summary, 1 OpKit (OK-M22-001). Quality 7.0/10. M22 covers three operational disciplines: referral programs, community building, and UGC content production. Key findings: LMNT comparative claim removed (Lanham Act legal risk), Geneva community platform discontinued (acquired by Bumble), $500/month UGC budget is survival mode not testing, and Loop+Smile.io integration is an unverified CRITICAL gap. Persona dialogue (4 rounds, 3 personas, 6 upgrades) reached saturation.

### Decisions Made
- **$10/$10 store credit referral** validated as optimal for bootstrapped DTC — referral CAC $13.40 vs $35 paid
- **Referral amplifies PMF, doesn't create it** — core principle added, referral launches only at Month 2-3 with PMF signals
- **Geneva DISCONTINUED** — Danilo's community platform recommendation invalidated. Circle recommended for Phase 2 ($100K+ revenue). No platform pre-$100K.
- **"More complete than LMNT" REMOVED** — contradicts Danilo's own DON'T rule; Lanham Act liability, C&D risk. Replaced with unnamed comparisons.
- **"Body is 70% ocean" flagged** — not a legal problem but credibility risk for science-forward brand. Added accuracy note.
- **Creator Compliance Acknowledgment** added — paper trail protection if creators go off-script
- **Loop/Smile integration gap elevated to CRITICAL** — two key platforms (subscription + referral) that may not integrate
- **UGC budget tiers annotated**: $500 = survival mode, $1K = minimum viable testing

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| **M22 CONTENT (TWP-001 Phases 1-6)** |
| 1 | created | `data/m22/referral_program.json` | Referral architecture: $10/$10, phased rollout (manual→Smile.io→optimize), benchmarks, best-in-class examples |
| 2 | created | `data/m22/community_strategy.md` | 7-platform evaluation, phased strategy (email-first→test→Circle), Geneva discontinued |
| 3 | created | `data/m22/ugc_brand_brief.md` | Creator guidelines: approved/prohibited claims, FTC compliance, visual guidelines |
| 4 | created | `data/m22/ugc_library.json` | UGC tracking database with rights status, quality grading, performance tracking |
| 5 | created | `data/m22/ugc_brief_template.md` | Production-ready creator brief with 8 hook frameworks, content flow, revision policy |
| 6 | created | `data/m22/ugc_creator_program.json` | Creator economics, sourcing platforms, budget tiers, hit rates, creative fatigue |
| 7 | created | `data/m22/dialogue_summary.md` | 4-round persona dialogue: Skeptical Investor, Growth Hacker, Regulatory Counsel. 6 upgrades. |
| **DIALOGUE UPGRADES** |
| 8 | edited | `data/m22/ugc_brand_brief.md` | UPG-1: Changed unqualified superlative to qualified comparison; UPG-4: Added science accuracy note |
| 9 | edited | `data/m22/ugc_library.json` | UPG-1: Fixed organic rights consent — "does NOT constitute consent for commercial use" |
| 10 | edited | `data/m22/ugc_creator_program.json` | UPG-5: Budget tier annotations; UPG-6: Creator compliance acknowledgment |
| 11 | edited | `data/m22/referral_program.json` | UPG-3: Core principle added; UPG-6: Loop/Smile integration elevated to CRITICAL |
| **REGISTRATION (TWP-001 Phases 7-11)** |
| 12 | created | `data/m22/opkit_referral_community_ugc.md` | OpKit OK-M22-001: Referral, Community & UGC Growth Kit |
| 13 | created | `data/m22/_meta.json` | TUP metadata with revisions[] pattern, quality 7.0/10 |
| 14 | edited | `data/hypotheses/validation_log.json` | Added LOG-020 (M22→HYP-006 evidence contribution) |
| 15 | edited | `data/hypotheses/index.json` | HYP-006 +3 refs, 3 M22 docs in document_to_hypotheses, M22 dialogue in context_documents, metadata updated |
| 16 | edited | `data/manifest.json` | M22 status→migrated, migrated_tups 5→6, full sheet/opkit/hypothesis data |
| 17 | edited | `data/opkits/registry.json` | OK-M22-001 registered with full component mapping |
| 18 | edited | `tracking/TUP_Workshop_Tracker.md` | BCL-4: 1/6→2/6, M22 DONE, scoreboard updated (6 done, 33 active), OpKit count 9→10 |
| 19 | edited | `ACTIVE_WORK.md` | Cleared session B (M22) claim |

### Artifacts Produced
- 9 new files in `data/m22/`
- 1 OpKit (OK-M22-001)
- 1 validation log entry (LOG-020)
- Quality score: 7.0/10

### Key Findings
1. **Referral programs amplify PMF — they don't create it.** Building referral infrastructure before product-market fit is premature spending. Phased approach: manual codes at Month 2-3, Smile.io at Month 3-12.
2. **LMNT comparative claim is a legal trap.** Danilo's brand brief had "More complete than LMNT" as a key talking point while his own DON'T list said "No competitor bashing by name." Lanham Act liability for a bootstrapped brand.
3. **$500/month UGC produces 0-1 winners.** At 5-10% hit rate, $500/month is survival-mode creative, not a testing program. $1K/month is minimum viable testing.
4. **Geneva is dead.** Acquired by Bumble mid-2024, shut down community features. Danilo's recommendation invalidated.
5. **Loop + Smile.io integration unverified.** Two critical platforms (subscription + referral) that may not talk to each other. Needs verification before committing.

### Next Steps
- [ ] Verify Loop Subscriptions + Smile.io/ReferralCandy integration (CRITICAL — before committing to referral platform)
- [ ] Continue Wave 2: M14 (Testing, 7 tabs), M29 (PR, 7 tabs), M16 (Content & SEO, 8 tabs), M25 (Bookkeeping, 6 tabs)
- [ ] Wave 1 complete: M10, M21, M22 all done
- [ ] Await PT-001 completion — may require M10 revision if $49 wins
- [ ] ISS-001: Resolve HYP-004 open issue (67% → 62-64% margin target)
- [ ] Mine Seaonic Trustpilot/Amazon review text for HYP-003.1 upgrade C→B

---

## Session 2026-02-06 — M10 Pricing & Offer Workshop Complete
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Workshopped M10 (Pricing & Offer) through full TWP-001 protocol. Produced 6 content tabs, 1 dialogue summary, 1 OpKit (OK-M10-001). Quality 7.4/10. Key architectural decisions: $59 base price (conditional on PT-001), 15% subscription discount, subscription-first checkout, wave-gated SKU expansion, and standardized price testing framework. Persona dialogue produced 4 upgrades including flagging HYP-004 for target revision (67% → 62-64%). Post-workshop: implemented `open_issues[]` system on hypotheses (architecture v1.2.0) and attached ISS-001 to HYP-004.

### Decisions Made
- **$59 base price as working assumption** — conditional on PT-001 result (running, 41% complete). If $49 wins, full revision needed.
- **15% subscription discount** ($50.15/month) — based on ProfitWell optimal range. Below Seaonic's 28% — deliberate strategy to attract quality subscribers.
- **Subscription-first checkout** — subscription is the default, one-time is the "downgrade" option.
- **Wave-gated SKU expansion**: Wave 1 (hero SKU only), Wave 2 (flavors + starter kit at Month 6+), Wave 3 (premium tier at Month 12+), Wave 4 (ecosystem at Month 18+). Each wave requires validation gates passed.
- **Price testing discipline**: sequential price tests, parallel UX/presentation tests allowed. RPV as primary metric, not CVR.
- **HYP-004 target revision flagged**: 67% gross margin target structurally unachievable with subscription discount. Recommended revision to 62-64%.

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Mapped M10 hypotheses in index | `data/hypotheses/index.json` | HYP-002, HYP-004, HYP-005, HYP-003.4 linked to M10 |
| 2 | Updated M10 manifest entry | `data/manifest.json` | Added feeds_into, requires, hypothesis_links |
| 3 | Wrote Tab 1: Offer Strategy | `data/m10_pricing_offer/offer_strategy.md` | Pricing architecture, subscription pricing, anchoring, unit economics, competitive map |
| 4 | Wrote Tab 2: Price Testing Framework | `data/m10_pricing_offer/price_testing_framework.md` | Test protocol, sample sizing, decision rules, test queue |
| 5 | Wrote Tab 3: Product Customization | `data/m10_pricing_offer/product_customization.md` | Subscription frequency, flavor rotation (Wave 2+), personalization |
| 6 | Wrote Tab 4: SKU Architecture | `data/m10_pricing_offer/sku_architecture.md` | Hero SKU definition, bundle strategy, wave expansion, naming conventions |
| 7 | Wrote Tab 5: Product Roadmap | `data/m10_pricing_offer/product_roadmap.md` | 4-wave validation-gated expansion with gates and milestones |
| 8 | Wrote Tab 6: Upsell Page Copy | `data/m10_pricing_offer/upsell_page_copy.md` | Cart, checkout, post-purchase, portal upsell frameworks |
| 9 | Ran persona dialogue (8 rounds) | `data/m10_pricing_offer/dialogue_summary.md` | 4 upgrades, 0 unresolved. Saturated at round 8. |
| 10 | Applied dialogue upgrades | `offer_strategy.md`, `price_testing_framework.md` | U1: $49 positioning contingency, U2: LMNT comparison talking point, U4: test type classification |
| 11 | Created _meta.json | `data/m10_pricing_offer/_meta.json` | Full TUP metadata with revision history |
| 12 | Registered OpKit | `data/opkits/registry.json` | OK-M10-001 Pricing & Offer Design Kit |
| 13 | Updated TUP Workshop Tracker | `tracking/TUP_Workshop_Tracker.md` | M10 → DONE, counts updated |
| 14 | Added validation log entries | `data/hypotheses/validation_log.json` | LOG-018 (HYP-004 margin tension), LOG-019 (HYP-002 pricing-side evidence) |
| 15 | Cleared ACTIVE_WORK claim | `ACTIVE_WORK.md` | Session A (M10) removed |
| 16 | Implemented `open_issues[]` system | `standards/Hypotheses_Architecture_Standards.md` | v1.1.0 → v1.2.0: new Open Issues System section, issue types, severity levels, lifecycle, resolution protocol |
| 17 | Added ISS-001 to HYP-004 | `data/hypotheses/registry.json` | HIGH severity target_mismatch: 67% margin unachievable with subscription pricing |
| 18 | Converted LOG-018 to ISSUE_FLAGGED | `data/hypotheses/validation_log.json` | New event type, links to ISS-001 |

### Artifacts Produced
- 8 new files in `data/m10_pricing_offer/`
- 1 OpKit (OK-M10-001)
- 2 validation log entries (LOG-018 as ISSUE_FLAGGED, LOG-019)
- 1 architecture upgrade (Hypotheses Architecture Standards v1.2.0)
- 1 open issue (ISS-001 on HYP-004)
- Quality score: 7.4/10

### Key Finding
Subscription discount creates structural margin tension: blended margin 62.7% vs HYP-004's 67% target. The 67% was set before subscription economics were modeled. Financial model may need updating. Kill threshold (60%) is still cleared with room. This led to creating the `open_issues[]` system — a mechanism for flagging hypothesis problems without immediately revising the hypothesis, making unresolved issues visible at the point of read.

### Next Steps
- [ ] Await PT-001 completion — may require full M10 revision if $49 wins
- [ ] ISS-001: Resolve HYP-004 open issue — formally revise target from 67% to 62-64% (needs operator confirmation)
- [ ] M22 (Referral) is next in Wave 1 queue

---

## Session 2026-02-06 #10 — TUP Workshop System + M21 Complete
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Built the TUP Workshop Tracker and TUP Workshop Protocol (TWP-001), then workshopped the first TUP (M21 Subscriptions) end-to-end through all 11 phases. Produced 5 content files, 1 OpKit, 1 dialogue summary, and full hypothesis cross-referencing. Also implemented TUP versioning (revisions[] pattern matching hypothesis versioning) and retroactively created the M21 persona dialogue summary that was missing from the prior session. Completed hypothesis cross-reference (Phase 10) — M21 evidence now linked to HYP-002, HYP-003, and 4 sub-hypotheses.

### Decisions Made
- **TWP-001 created as canonical 11-phase workshop protocol**, absorbing CI protocol methodology (source hierarchy, persona dialogue, saturation, self-grade). Positioned CI protocol as "first worked example."
- **Spreadsheets deprecated** — all TUP content produced as markdown (narrative) or JSON (structured data)
- **TUP versioning**: Deprecated top-level `version` field in `_meta.json`. Replaced with `revisions[]` array (semver: Major=re-workshop, Minor=evidence upgrade, Patch=correction). Each revision carries `dialogue_ref.tup_version` to tie persona dialogues to specific versions.
- **Dialogue summary is a required output** of Phase 6 (added to TWP-001). Must be saved to `data/m{N}/dialogue_summary.md`, not just run in context.
- **M21 findings**: Danilo's Skio recommendation invalidated (6x price increase). Loop Subscriptions recommended. Danilo's discount ladder (10%→30%) identified as anti-pattern — replaced with education-first win-back strategy.
- **M37 (AI & Automation) deferred** — content is self-referential and better written after operational experience
- **M0/M26/M27 NOT retroactively migrated** to revisions[] pattern — low-value busywork, will migrate when next touched

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| **TRACKER & PROTOCOL** |
| 1 | created | `tracking/TUP_Workshop_Tracker.md` | v1.1.0: All 41 TUPs with effort estimates, Danilo tab counts, OpKit tracking, 11 workshop waves |
| 2 | created | `processes/TUP_Workshop_Protocol.md` | v2.0.0: 11-phase protocol absorbing CI methodology. Updated to v2.1.0 with TUP versioning spec and dialogue save requirement |
| 3 | edited | `CLAUDE.md` | Added TUP Workshop Protocol section |
| 4 | edited | `00_start_here.md` | Added TUP workshop and tracker to "Finding Things" |
| **M21 WORKSHOP (TWP-001 Phases 1-11)** |
| 5 | created | `data/m21/subscription_platform.json` | Platform comparison: Loop (rec), Recharge (backup), Skio (NOT rec — $599/mo), Stay AI (Month 6+) |
| 6 | created | `data/m21/subscription_psychology.md` | Why people subscribe/cancel supplements. Psychological retention levers. |
| 7 | created | `data/m21/churn_prediction.json` | Retention curve, 9 churn signals, composite risk scoring, dunning model |
| 8 | created | `data/m21/win_back_offer_ladder.md` | Education-first win-back replacing Danilo's discount ladder |
| 9 | created | `data/m21/retention_playbook.md` | 15-tactic prioritized playbook (3 tiers), scenario modeling, implementation timeline |
| 10 | created | `data/m21/opkit_subscription_retention.md` | OpKit OK-M21-001: Subscription & Retention Design Kit for any DTC consumable Trade |
| 11 | created | `data/m21/dialogue_summary.md` | Persona dialogue transcript: 6 rounds, 3 personas, 3 upgrades, saturated |
| 12 | created | `data/m21/_meta.json` | TUP metadata with revisions[] pattern (first TUP to use new versioning) |
| **SYSTEM REGISTRATION** |
| 13 | edited | `data/manifest.json` | M21 status → migrated, migrated_tups: 3→4 |
| 14 | edited | `data/opkits/registry.json` | Added OK-M21-001, removed M21 from unmapped |
| 15 | edited | `tracking/TUP_Workshop_Tracker.md` | BCL-4: 0/6→1/6, total: 3→4 workshopped, OpKit count: 7→8 |
| **HYPOTHESIS CROSS-REFERENCE (Phase 10)** |
| 16 | edited | `data/hypotheses/validation_log.json` | Added LOG-016 (M21→HYP-003 evidence) and LOG-017 (M21→HYP-002 evidence). New event type: TUP_EVIDENCE_CONTRIBUTION |
| 17 | edited | `data/hypotheses/index.json` | HYP-002 +2 refs, HYP-003 +4 refs. 5 M21 files added to document_to_hypotheses. M21 dialogue added to context_documents. Total refs: 57→68+ |
| **TUP VERSIONING** |
| 18 | edited | `processes/TUP_Workshop_Protocol.md` | Added TUP Versioning section to Phase 9 with semver spec, revision schema, dialogue_ref linkage |
| 19 | edited | `processes/TUP_Workshop_Protocol.md` | Phase 6 output now requires saving dialogue_summary.md (not just in-context) |
| 20 | edited | `data/m21/_meta.json` | Converted from `version: "1.0.0"` to `revisions[]` pattern with dialogue_ref |

### Next Steps
- [ ] Continue Wave 1: Workshop M22 (Referral, 6 tabs) and M10 (Pricing, 6 tabs)
- [ ] Wave 2 after: M14 (Testing, 7 tabs), M29 (PR, 7 tabs), M16 (Content & SEO, 8 tabs), M25 (Bookkeeping, 6 tabs)
- [ ] Wave 3: M20, M17, M18 to complete BCL-4 (first full cluster)
- [ ] REC-001 (BCL-2 Money & Legal) — PENDING (margin crisis: Danilo 40% vs Bootstrap 67%)
- [ ] Mine Seaonic Trustpilot/Amazon review text for HYP-003.1 upgrade C→B (2-3 hrs)
- [ ] Apply CSP to HYP-001 (CAC) — most CRITICAL primitive hypothesis
- [ ] Migrate M0/M26/M27 _meta.json to revisions[] pattern when next touched

---

## Session 2026-02-06 #9 — CSP Registry Integration (Completing Interrupted Work)
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Completed registry integration for two CSP (Constraint Scenario Protocol) runs from interrupted Session #8. The case studies and protocol were already committed but the hypothesis data layer was never updated. Integrated: HYP-006 decomposition (5 sub-hypotheses), HYP-003 decomposition (4 sub-hypotheses), HYP-003.1 proxy evidence upgrade (D→C), HYP-009 creation (Pre-Launch Demand), and all validation log entries.

### Decisions Made
- All CSP work from Session #8 integrated per CSP-001 Step 10 (Update Registry and Close)
- Registry version bumped 1.0.0 → 2.0.0 (major: sub-hypothesis system now live)
- Index version bumped 1.0.1 → 1.1.0 (minor: new documents and hypotheses)
- HYP-006 relationship to HYP-001 reframed: `mitigates` → `portfolio_diversifies`
- Cross-hypothesis sub-link established: HYP-006.5 depends_on HYP-003.1

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | edited | `data/hypotheses/registry.json` | Added HYP-006 parent updates: `has_children`, `composite_scoring`, revision #2 (decomposition), reframed relationship |
| 2 | created | `data/hypotheses/registry.json` | Added HYP-006.1 through HYP-006.5 (5 sub-hypotheses with weights, validation plans, CSP origin) |
| 3 | edited | `data/hypotheses/registry.json` | Added HYP-003 parent updates: `has_children`, `composite_scoring` (1.40), revision #3 (decomposition) |
| 4 | created | `data/hypotheses/registry.json` | Added HYP-003.1 through HYP-003.4 (4 sub-hypotheses). HYP-003.1 at grade C (Seaonic proxy evidence) |
| 5 | created | `data/hypotheses/registry.json` | Added HYP-009 (Pre-Launch Demand Generation) — surfaced by CSP-001 SC-02 |
| 6 | edited | `data/hypotheses/registry.json` | Updated `_meta`: v2.0.0, 19 total hypotheses (9 top-level, 9 sub, 1 new) |
| 7 | edited | `data/hypotheses/index.json` | Added CSP case study references to HYP-003 and HYP-006 entries |
| 8 | created | `data/hypotheses/index.json` | Added HYP-009 entry, added CSP case study documents to `document_to_hypotheses` |
| 9 | edited | `data/hypotheses/index.json` | Updated metadata: v1.1.0, 10 hypotheses, 15 documents, 57 references |
| 10 | edited | `data/hypotheses/validation_log.json` | Added LOG-012 (CSP-001 HYP-006), LOG-013 (HYP-009 created), LOG-014 (CSP-002 HYP-003), LOG-015 (HYP-003.1 proxy upgrade D→C) |
| 11 | edited | `SESSION_LOG.md` | Documented interrupted Session #8 and this Session #9 |

### Next Steps
- [ ] REC-001 (BCL-2 Money & Legal) — PENDING (margin crisis: Danilo 40% vs Bootstrap 67%)
- [ ] Mine Seaonic Trustpilot/Amazon review text for HYP-003.1 upgrade C→B (2-3 hrs)
- [ ] Apply CSP to HYP-001 (CAC) — most CRITICAL primitive hypothesis
- [ ] Reconcile bifurcation parameters with hypothesis kill thresholds (REC-002a)
- [ ] Formalize 10 PMF signals as individual Metrics (REC-002b)
- [ ] Continue migrating remaining 38 TUPs (M1-M40, excluding M0/M26/M27)
- [ ] Design pre-launch demand campaign (validates HYP-009)
- [ ] Update dashboard hypotheses-tracker to render sub-hypotheses

---

## Session 2026-02-06 #8 — CSP Protocol Creation & Hypothesis Decomposition (Interrupted)
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete (registry integration deferred to #9)

### Summary
Created Constraint Scenario Protocol (CSP-001), a new Meta-Control Protocol for stress-testing hypotheses through extreme constraint scenarios. Executed two CSP runs: CSP-001 on HYP-006 (decomposed into 5 sub-hypotheses, surfaced HYP-009) and CSP-002 on HYP-003 (decomposed into 4 sub-hypotheses, applied Seaonic proxy evidence to HYP-003.1). Updated Hypotheses Architecture Standards with sub-hypothesis system. **Session was interrupted due to folder move — case studies committed but registry integration not completed (done in Session #9).**

### Decisions Made
- CSP-001 is a Meta-Control Protocol (MC-002) — operates on the hypothesis system itself
- HYP-006 decomposed: Referral (0.35), SEO (0.25), Influencer (0.20), PR (0.10), WOM (0.10)
- HYP-003 decomposed: Efficacy (0.40), Early-Life Churn (0.30), Retention Infrastructure (0.20), Consumption-Cadence (0.10)
- HYP-003.1 upgraded D→C using Seaonic proxy evidence (4.5★ Trustpilot, subscriptions at $69/box)
- HYP-009 (Pre-Launch Demand Generation) surfaced as missing hypothesis
- "Churn is a product hypothesis in disguise" — key strategic reframe
- HYP-001 relationship with HYP-006 reframed: mitigation → portfolio diversification
- Cross-hypothesis sub-link: HYP-006.5 depends on HYP-003.1

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `protocols/CSP-001_Constraint_Scenario_Protocol.md` | 10-step protocol: select target, identify scenarios, 3-question drill, synthesize, decompose, composite score, surface new hypotheses, update graph, document, close |
| 2 | created | `protocols/case_studies/CSP-001_HYP-006_2026-02-06.md` | First CSP run: HYP-006 decomposed, HYP-009 surfaced, HYP-001 relationship reframed |
| 3 | created | `protocols/case_studies/CSP-002_HYP-003_2026-02-06.md` | Second CSP run: HYP-003 decomposed, Seaonic proxy evidence applied, early-life churn identified as kill zone |
| 4 | edited | `standards/Hypotheses_Architecture_Standards.md` | v1.0.0 → v1.1.0: Added Sub-Hypothesis System section with schema, composite scoring, decomposition rules |
| 5 | edited | `00_START_HERE.md` | Added protocols/ directory reference |
| 6 | edited | `DOCUMENTATION_INDEX.md` | Added CSP protocol and case studies |

### Session Commits (all pushed)
- Commit `61293cf`: CSP-001 Protocol + HYP-006 Case Study
- Commit `413b3e0`: CSP-002 HYP-003 Churn Decomposition
- Commit `ac46ffc`: HYP-003.1 Updated with Proxy Evidence

### Next Steps (completed in Session #9)
- [x] Register sub-hypotheses in registry.json
- [x] Update parent hypotheses with has_children, composite scoring
- [x] Create HYP-009 in registry
- [x] Update index.json with CSP document links
- [x] Add validation log entries
- [x] Update session log

---

## Session 2026-02-06 #7 — Session Log Attribution & Model Tracking
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-opus-4-6
**Status**: Complete

### Summary
Added Operator and AI Model fields to all session log entries for multi-user attribution (project now shared with Danilo). Updated entry template. All prior sessions attributed to Caio on claude-sonnet-4-5-20250929. This is the first session on claude-opus-4-6.

### Decisions Made
- Added `**User**:` and `**AI Model**:` fields to session log template and all 12 existing entries
- All prior sessions: Operator = Caio, AI Model = claude-sonnet-4-5-20250929
- Session #7 is the first using claude-opus-4-6

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | edited | `SESSION_LOG.md` | Updated entry template with Operator and AI Model fields |
| 2 | edited | `SESSION_LOG.md` | Added `Operator: Caio` and `AI Model: claude-sonnet-4-5-20250929` to all 12 existing entries (#1-#6, 2026-02-03 through 2026-02-06) |
| 3 | created | `SESSION_LOG.md` | Session #7 entry using new format |

### Next Steps
- [ ] REC-001 (BCL-2 Money & Legal) — PENDING (margin crisis: Danilo 40% vs Bootstrap 67% - needs dedicated reconciliation)
- [ ] Reconcile bifurcation parameters with hypothesis kill thresholds (REC-002a)
- [ ] Formalize 10 PMF signals as individual Metrics (REC-002b)
- [ ] Continue migrating remaining 38 TUPs (M1-M40, excluding M0/M26/M27)
- [ ] Update DOCUMENTATION_INDEX.md with new standards document and TUP migration notes

---

## Session 2026-02-06 #6 — Architecture Formalization & MAJOR TUP Migration & OpKit Registry
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
**Three major accomplishments in one session:**

**Part 1 - Architecture Formalization:**
Established CLAUDE.md for automatic session startup. Extracted formal definitions of 11 ontological primitives from Sprint_STAGE_5 document into `standards/Systems_Architecture_Standards.md`. Updated 00_START_HERE.md v2.3.0 with expanded primitives.

**Part 2 - TUP Migration (MAJOR):**
Completed full migration from Bootstrap file numbering (01-38) to TUP-based organization (M0-M40). Deprecated Bootstrap files, migrated 3 TUPs to JSON, rebuilt manifest.json with TUP codes as primary keys, updated entire dashboard to TUP navigation, updated all documentation. This is a fundamental architectural shift in how the project organizes knowledge.

**Part 3 - OpKit Registry:**
Created comprehensive OpKit registry linking TUPs to their production support bundles. Registered 9 OpKits across M0 (4 OpKits), M26 (1 OpKit), M27 (2 OpKits). Updated all TUP _meta.json files with OpKit associations. Completed REC-002c requirement to "register OpKit associations per TUP in data layer".

### Decisions Made

**Architecture:**
- Sprint_STAGE_5 treated as historical reference with relevant architecture extracted
- No cross-referencing between Sprint_STAGE_5 hypotheses (H1-H13, Studio) and Bootstrap hypotheses (8 business, Trade) - different scopes
- Created comprehensive Systems Architecture Standards document
- 00_START_HERE updated to v2.3.0 (architecture), then v2.4.0 (TUP migration)

**TUP Migration:**
- **Deprecated Bootstrap file numbers (01-38)** as primary organizational structure
- **Adopted TUP codes (M0-M40)** from Danilo's system as canonical organization
- **3 TUPs migrated**: M0 (Trade Thesis), M26 (Competitive Intel), M27 (Customer Research - merged 03A+03B)
- **38 TUPs pending**: M1-M40 (excluding M0, M26, M27)
- **Bootstrap XLSX files (04-38)** archived as reference - unmigrated files superseded by Danilo's TUP files
- **Manifest.json rebuilt** with TUP codes as primary keys (41 TUPs total)
- **Dashboard completely updated** to TUP-based navigation
- **Documentation updated** to reflect TUP structure (00_START_HERE.md v2.4.0)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| **ARCHITECTURE FORMALIZATION** |
| 1 | created | `CLAUDE.md` | Automatic session startup instructions for Claude agents |
| 2 | read | `Caio __ Danilo, Rhen Sprint_STAGE_5.md` | Foundational Studio 3 architecture document (1521 lines) |
| 3 | created | `standards/Systems_Architecture_Standards.md` | Formalized 11 ontological primitives with full definitions |
| 4 | moved | `Sprint_STAGE_5.md` → `archive/historical-reference/` | Archived after extraction |
| 5 | edited | `00_start_here.md` | v2.2.0 → v2.3.0: Expanded Ontological Primitives, added Systems Architecture reference |
| **TUP MIGRATION** |
| 6 | archived | All Bootstrap XLSX (01-38, 42 files total) → `archive/bootstrap-xlsx-pre-tup-migration/` | Complete archive of original Bootstrap files |
| 7 | renamed | `data/01_strategic_foundation/` → `data/m0_trade_thesis/` | TUP M0 migration |
| 8 | renamed | `data/02_market_intelligence/` → `data/m26_competitive_intel/` | TUP M26 migration |
| 9 | renamed | `data/03a_customer_research_icp/` → `data/m27_customer_research/` | TUP M27 base |
| 10 | merged | `data/03b_customer_research_voc/` → `data/m27_customer_research/` | Merged 03B into M27, removed 03B folder |
| 11 | edited | `data/m0_trade_thesis/_meta.json` | file_id→tup_id: "m0", added tup_name, version 1.3.0→1.4.0, migration notes |
| 12 | edited | `data/m26_competitive_intel/_meta.json` | file_id→tup_id: "m26", added tup_name, version 1.0.0→1.1.0, migration notes |
| 13 | created | `data/m27_customer_research/_meta.json` | New merged meta: tup_id "m27", combined 12 sheets from 03A+03B, version 2.0.0 |
| 14 | rebuilt | `data/manifest.json` | Complete rebuild: TUP codes as primary keys, 41 TUPs (3 migrated, 38 not_migrated), all dependencies updated |
| **DASHBOARD UPDATES** |
| 15 | edited | `dashboard/index.html` | Stats ribbon updated to show TUP counts, file cards→TUP cards (M0, M26, M27), all TUP navigation |
| 16 | renamed | `dashboard/views/strategic-foundation.html` → `m0-trade-thesis.html` | TUP-based view naming |
| 17 | renamed | `dashboard/views/market-intelligence.html` → `m26-competitive-intel.html` | TUP-based view naming |
| 18 | renamed | `dashboard/views/customer-research.html` → `m27-customer-research.html` | Unified M27 view (merged ICP+VOC) |
| 19 | edited | `dashboard/views/m0-trade-thesis.html` | Updated FILE_ID to m0_trade_thesis, title to "M0 TRADE THESIS", nav bar updated |
| 20 | edited | `dashboard/views/m26-competitive-intel.html` | Updated FILE_ID to m26_competitive_intel, title to "M26 COMPETITIVE INTEL", nav bar updated |
| 21 | edited | `dashboard/views/m27-customer-research.html` | Completely restructured for unified M27 (merged ICP+VOC), single FILE_ID, nav bar updated |
| 22 | edited | All dashboard nav bars (tup-navigator, hypotheses-tracker, financial-forecast, hypothesis-detail) | Updated to use new TUP-based URLs |
| **DOCUMENTATION UPDATES** |
| 23 | edited | `00_start_here.md` | v2.3.0 → v2.4.0: Complete rewrite of Data Layer section (TUP-based), added Archived Bootstrap Files section, updated Dashboard section (TUP views), updated Finding Things (TUP references), updated Current Work Focus (TUP Migration), added v2.4.0 to version history |
| 24 | edited | `SESSION_LOG.md` | Created comprehensive session #6 summary with TUP migration details |
| **OPKIT REGISTRY** |
| 25 | created | `data/opkits/registry.json` | Complete OpKit registry: 9 OpKits mapped to M0 (4), M26 (1), M27 (2), plus 38 unmapped TUPs. Includes OpKit types (Production/Foundation), component definitions, source file locations |
| 26 | edited | `data/m0_trade_thesis/_meta.json` | Added opkits array: 4 OpKits (Thesis Structure Checklist, Computational PMF Observer, Anti-Goals, Bifurcation Points) with sources and decisions |
| 27 | edited | `data/m26_competitive_intel/_meta.json` | Added opkits array: CI Protocol OpKit (Bootstrap canon, superior to Danilo's) |
| 28 | edited | `data/m27_customer_research/_meta.json` | Added opkits array: ICP Analysis Framework, VOC Protocol (both Bootstrap canon) |
| 29 | edited | `SESSION_LOG.md` | Updated session #6 with OpKit registry completion |

### Session Complete ✅

**All commits pushed to origin/main:**
- Commit `c539947`: MAJOR TUP Migration (1264 files changed, 265,600 insertions)
- Commit `7033fa7`: OpKit Registry (5 files, 269 insertions)

**Session #5 Items Completed:**
- ✅ Formalize Controller/Observer/OpKit schemas → `standards/Systems_Architecture_Standards.md`
- ✅ Register OpKit associations per TUP → `data/opkits/registry.json` + TUP _meta.json updates

### Next Session Priorities
- [ ] REC-001 (BCL-2 Money & Legal) — PENDING (margin crisis: Danilo 40% vs Bootstrap 67% - needs dedicated reconciliation)
- [ ] Reconcile bifurcation parameters with hypothesis kill thresholds (REC-002a)
- [ ] Formalize 10 PMF signals as individual Metrics (REC-002b)
- [ ] Continue migrating remaining 38 TUPs (M1-M40, excluding M0/M26/M27)
- [ ] Update DOCUMENTATION_INDEX.md with new standards document and TUP migration notes

---

## Session 2026-02-05 #5 — TUP System Dashboard Integration & Reconciliation Completion
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Continued from prior session (context compacted). Integrated the TUP/Cluster system from Danilo's `IonWave_Ops_Model_v10_Protocol.xlsx` reconciliation into the live dashboard. Created a new TUP Navigator view, added cluster overview to Mission Control, updated all nav bars, fixed a Google Drive-induced git corruption issue, consolidated git branches from master+main to main only, added a Session Closing Protocol to 00_START_HERE.md, and updated DOCUMENTATION_INDEX.md with all missing dashboard views.

### Decisions Made
- TUP Navigator created as a dedicated dashboard view (not merged into Mission Control — it's substantial enough to warrant its own page)
- Mission Control gets a compact 4-column cluster map as a quick overview with link to full navigator
- Each cluster assigned a distinct color for visual identification across all views
- Git branches consolidated: deleted remote `master`, renamed local to `main`, single branch going forward
- Session Closing Protocol formalized as a 5-step checklist in 00_START_HERE.md
- Google Drive `desktop.ini` corruption fixed by grafting history and rewriting with filter-branch

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `dashboard/views/tup-navigator.html` | Full TUP Navigator: stats ribbon, ontological primitives (6 cards), 8 cluster cards, per-cluster TUP tables, reconciliation status with decision distribution and coverage gaps |
| 2 | edited | `dashboard/index.html` | Added TUP Navigator to nav bar, added Cluster Map section (4-col grid), added TUP/cluster badges to file cards |
| 3 | edited | `dashboard/css/styles.css` | Added `.grid-4` layout, `.cluster-card` and `.cluster-card-mini` hover styles |
| 4 | edited | `dashboard/views/strategic-foundation.html` | Updated nav bar (added TUP Navigator, fixed `../../` path to `../`) |
| 5 | edited | `dashboard/views/market-intelligence.html` | Updated nav bar (added TUP Navigator, fixed `../../` path to `../`) |
| 6 | edited | `dashboard/views/customer-research.html` | Updated nav bar (added TUP Navigator, fixed `../../` path to `../`) |
| 7 | edited | `dashboard/views/financial-forecast.html` | Updated nav bar (added TUP Navigator) |
| 8 | edited | `dashboard/views/hypotheses-tracker.html` | Updated nav bar (added TUP Navigator) |
| 9 | edited | `dashboard/views/hypothesis-detail.html` | Updated nav bar (added TUP Navigator) |
| 10 | edited | `00_START_HERE.md` | Fixed branch ref (master→main), added TUP Navigator to dashboard views, added Session Closing Protocol |
| 11 | edited | `DOCUMENTATION_INDEX.md` | Added 4 missing dashboard views (tup-navigator, hypotheses-tracker, hypothesis-detail, financial-forecast) |
| 12 | fixed | `.git/` | Removed Google Drive desktop.ini files from git objects/refs, grafted corrupt ancestor, rewrote history with filter-branch |
| 13 | deleted | `origin/master` | Consolidated to single `main` branch |
| 14 | committed+pushed | All above | Commit `25b5740` (dashboard+data), commit `2e59927` (docs) — both pushed to `origin/main` |

### Next Steps
- [ ] REC-001 (BCL-2 Money & Legal) — still PENDING. Margin crisis: Danilo's model shows 40% margin vs Bootstrap's assumed 67%. Needs dedicated reconciliation session.
- [ ] Formalize Controller, Observer, OpKit, Metric schemas in a systems architecture doc (per REC-002c)
- [ ] Reconcile bifurcation parameters with hypothesis kill thresholds (per REC-002a)
- [ ] Register OpKit associations per TUP in data layer (per REC-002c)
- [ ] Formalize 10 PMF signals as individual Metrics (per REC-002b)
- [ ] Consider removing debug logging from data-loader.js (carried from session #4)
- [ ] Continue Tier 2 file JSON migration

---

## Session 2026-02-05 #4 — Dashboard Troubleshooting & Jekyll Fix
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Troubleshot dashboard view pages (Strategic Foundation, Market Intelligence, Customer Research) that were hanging with infinite "Loading..." state. Root cause: GitHub Pages uses Jekyll by default, which ignores files starting with underscores (like `_meta.json`), causing 404 errors. Added `.nojekyll` file to disable Jekyll processing and allow all data files to be served. Also added debug logging to data-loader.js and view pages to aid future troubleshooting.

### Decisions Made
- Added `.nojekyll` to repository root to disable Jekyll processing on GitHub Pages
- Kept debug logging in data-loader.js for future troubleshooting (logs pathname, fetch URLs, response status)
- Verified git branch structure: local `master` pushes to `origin/main` (GitHub Pages deploys from main)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `.nojekyll` | Empty file to disable Jekyll processing on GitHub Pages, allowing underscore-prefixed files to be served |
| 2 | edited | `dashboard/js/data-loader.js` | Added console.log statements for pathname detection, fetch URLs, response status, cache hits/misses |
| 3 | edited | `dashboard/views/strategic-foundation.html` | Added console.log statements at script load and DOMContentLoaded to verify execution |
| 4 | committed | `.nojekyll` | Git commit 2ea6acb: "Add .nojekyll to serve underscore-prefixed files" |
| 5 | committed | Debug logging changes | Git commit e889bd9: "Add debug logging to troubleshoot data loading" |
| 6 | pushed | origin master:main | Both commits pushed to GitHub, triggering Pages rebuild (~1-2 min deploy time) |

### Next Steps
- [ ] Consider removing debug logging from data-loader.js once dashboard is stable (optional - useful for diagnostics)
- [ ] Continue work from Session 2026-02-05 #1: Review financial model findings, address Q9 positioning tension, Tier 2 files
- [ ] Consider adding hypothesis metadata field to all future analysis deliverables (hypotheses_referenced: [])

---

## Session 2026-02-05 #3 — Integrate Hypotheses System into Initial Flow
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Updated 00_START_HERE.md to integrate hypotheses architecture into the initial workflow and documentation discovery. Added hypotheses system section to Mission Control dashboard home page with 3 prominent cards linking to tracker, audit, and validation log. Users now have clear entry points to hypothesis documentation from both START_HERE and the dashboard landing page.

### Decisions Made
- Hypotheses system positioned as core architecture primitive (same level as data/ and dashboard/)
- START_HERE.md v2.0.0 → v2.1.0 (minor version bump for new system addition)
- Dashboard home page gets dedicated "🧪 Hypotheses System" section above Analysis Deliverables
- All hypothesis discovery paths documented in "Finding Things" section
- Hypothesis confidence grading integrated into Quality Standards section

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | edited | `00_START_HERE.md` | Updated version to v2.1.0, last_updated to 2026-02-05 |
| 2 | edited | `00_START_HERE.md` | Added `data/hypotheses/` to data layer structure diagram with 3 files (registry, index, validation_log) |
| 3 | edited | `00_START_HERE.md` | Added hypotheses architecture bullet to Key Points section under data layer |
| 4 | edited | `00_START_HERE.md` | Expanded Dashboard section to include hypotheses-tracker.html and financial-forecast.html views with key features list |
| 5 | edited | `00_START_HERE.md` | Added "Key Analysis Deliverables" subsection under Documentation Folders listing 6 major deliverables including Hypothesis_Dependency_Audit.md |
| 6 | edited | `00_START_HERE.md` | Expanded Quality Standards section with full hypotheses architecture details (registry, index, validation log, state machine, grading, dependencies) |
| 7 | edited | `00_START_HERE.md` | Added 5 hypothesis-related entries to "Finding Things" section (hypotheses/assumptions, evidence mapping, critical questions, tracker links) |
| 8 | edited | `00_START_HERE.md` | Updated JSON Data Layer Migration status to mention hypotheses architecture establishment |
| 9 | edited | `00_START_HERE.md` | Added v2.1.0 entry to Version History documenting all hypotheses system additions |
| 10 | edited | `dashboard/index.html` | Added "🧪 Hypotheses System" section with 3 cards (Hypotheses Tracker, Dependency Audit, Validation Log) above Analysis Deliverables |
| 11 | edited | `dashboard/css/styles.css` | Added .card-footer, .card-title, and .btn-primary styles for new homepage cards |
| 12 | committed | Git commit 3a96401 | "Add Hypotheses System section to Mission Control home page" - 2 files, 90 insertions |

### Next Steps
- [ ] Create standards/Hypotheses_Architecture_Standards.md documenting the hypothesis system architecture and usage
- [ ] Add hypothesis validation templates to processes/ for Month 1-2 testing documentation
- [ ] Update core/04_Working_Principles_updated.md to reference hypothesis tracking workflow
- [ ] Consider adding hypothesis metadata field to all future analysis deliverables (hypotheses_referenced: [])
- [ ] Continue Tier 2 file migration or address Q9 (Positioning-Economics Tension)

---

## Session 2026-02-05 #2 — Hypotheses Architecture System Implementation
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Implemented comprehensive Hypotheses Architecture system as an ontological primitive per user directive: "This needs to be a systems architecture primitive I think. An ontological entity at least." Created central registry tracking 8 core business hypotheses (CAC, conversion rate, churn, margins, LTV, organic lift, timeline, capital sufficiency) with full revision history, confidence grading (A/B/C/D), validation plans, dependency tracking, and risk assessment. Built dedicated dashboard view with filtering and visualization. Changed terminology from "assumptions" to "hypotheses" to reflect evolving, testable nature.

### Decisions Made
- **Hypotheses as ontological primitives**: Central registry architecture with bidirectional document linking
- **State machine**: ASSUMED → TESTING → VALIDATED/INVALIDATED (with transitions documented)
- **Confidence grading**: A/B/C/D system to detect weak links transparently
- **Impact severity**: CRITICAL/HIGH/MEDIUM/LOW for risk prioritization
- **Revision history**: Full array of iterations with grade, date, reasoning, supporting documents
- **Validation plans**: Method, cost, timeline, success criteria for each hypothesis
- **Dependencies**: feeds_into and depends_on relationships to show hypothesis chains
- **Terminology**: "Hypotheses" not "assumptions" to reflect evolving nature (per original studio architecture)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `data/hypotheses/registry.json` | Central hypothesis registry with 8 core hypotheses (HYP-001 through HYP-008): CAC ($30-45), subscription rate (50% target 60%), churn (12%), gross margin (67%), blended LTV ($64-159), organic lift (10%), timeline (18 months), capital ($75-100K staged). Each includes full revision history, validation plan, dependencies, risk assessment. Current state: all ASSUMED; grades: 1 B-grade, 4 C-grade, 3 D-grade |
| 2 | created | `data/hypotheses/index.json` | Bidirectional index linking hypotheses to documents (hypothesis_to_documents) and documents to hypotheses (document_to_hypotheses). Maps 8 hypotheses across 3 documents with relevance tagging (PRIMARY/SUPPORTING/RELATED) |
| 3 | created | `data/hypotheses/validation_log.json` | Chronological event log with 11 entries tracking hypothesis creation, revisions, and architecture establishment. Event types: HYPOTHESIS_CREATED (8), HYPOTHESIS_REVISED (2), ARCHITECTURE_ESTABLISHED (1) |
| 4 | created | `dashboard/views/hypotheses-tracker.html` | Dedicated dashboard view with: summary stats (total hypotheses, critical count, low-grade count, validated count), filtering by severity/grade/state, hypothesis cards with color-coded confidence grades, revision history display, validation plans, dependency visualization, risk assessments |
| 5 | edited | `dashboard/index.html` | Added "🧪 Hypotheses Tracker" and "📊 Financial Forecast" to navigation bar |
| 6 | edited | `dashboard/views/financial-forecast.html` | Updated navigation to include Hypotheses Tracker; fixed nav paths |
| 7 | edited | `data/manifest.json` | Added hypotheses_system metadata section documenting registry structure, version 1.0.0, architecture note |
| 8 | committed | Git commit 2d570ad | "Implement Hypotheses Architecture system as ontological primitive" — 7 files changed, 1789 insertions |

### Next Steps
- [ ] Update existing documents to include `assumptions_referenced: ["HYP-001", ...]` metadata
- [ ] As new documents are created, link them to relevant hypotheses in index.json
- [ ] When hypotheses are tested/validated, update state and add validation_log entries
- [ ] When hypotheses are revised (new evidence, new reasoning), add revision to registry with reasoning
- [ ] Review and grade hypothesis confidence quarterly to detect degrading evidence quality
- [ ] Build contextual hypothesis displays in other dashboard views (show relevant hypotheses on each file view)
- [ ] Consider building hypothesis dependency graph visualizer (D3.js or similar)

---

## Session 2026-02-05 #1 — Financial Model Revenue Validation & Dashboard Deployment
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Built comprehensive financial model (3 scenarios, month-by-month cohort analysis) to validate revenue targets and capital sufficiency. Key finding: $30K MRR in Year 1 NOT achievable under base case assumptions — requires 18-24 months and $75-100K capital (not $30-50K). Deployed Mission Control dashboard to GitHub Pages with Critical Open Questions section now live. Documented Q10 and Q11 answers in tracking/Open_Questions.md. Dashboard troubleshooting: fixed data paths, committed data/ directory to repo, resolved GitHub Pages deployment issues.

### Decisions Made
- **$30K MRR timeline**: 18 months (base case), NOT 12 months — Year 1 target should be revised to $15-23K MRR
- **Capital sufficiency**: $30-50K raise INSUFFICIENT for base case — need $75-100K total or staged approach ($30-50K initial + $40-50K follow-on at Month 6)
- **CAC is highest-impact variable**: $30 CAC → 6 months to target; $35 CAC → 18 months; $45 CAC → not viable (kill)
- **Staged financing recommended**: Validate assumptions Months 1-6 with $30-50K, then raise $40-50K if metrics hit
- **Go/No-Go checkpoints**: Month 2 (after $3K ad spend), Month 6 (follow-on capital decision)
- File 08 audit complete: Has tactical 60-day cash flow + VSL economics, but missing strategic multi-year revenue model
- Q10 (Capital Sufficiency) status: ACTIVE → ANALYZED
- Q11 (Revenue Path Validation) status: ACTIVE → ANALYZED
- Dashboard deployment: Mission Control now live at https://caio-camargo.github.io/ionwave-dashboard/

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `tracking/Open_Questions.md` | Added Q9, Q10, Q11 to CRITICAL section with full evidence, options, decision criteria |
| 2 | edited | `tracking/Open_Questions.md` | Updated Q10 & Q11 status from ACTIVE to ANALYZED with reference to financial model |
| 3 | created | `IonWave/Financial_Model_Revenue_Validation.md` | 662-line comprehensive analysis: 3 scenarios (optimistic/base/conservative), month-by-month cohort model, capital burn analysis, sensitivity analysis, go/no-go framework, answers Q10 & Q11 |
| 4 | edited | `dashboard/index.html` | Added "🔴 Critical Open Questions" section to Mission Control; fixed asset paths for root-level deployment |
| 5 | edited | `dashboard/js/data-loader.js` | Fixed path detection to use absolute paths from repo root; added loadTracking() for markdown files; added parseOpenQuestions() parser |
| 6 | edited | `dashboard/views/strategic-foundation.html` | Fixed nav link to point to root index.html (was ../index.html) |
| 7 | edited | `dashboard/views/market-intelligence.html` | Fixed nav link to point to root index.html |
| 8 | edited | `dashboard/views/customer-research.html` | Fixed nav link to point to root index.html |
| 9 | created | `index.html` | Root-level index for GitHub Pages (copy of dashboard/index.html with corrected paths) |
| 10 | committed | `data/` directory | Pushed all JSON data layer files (01, 02, 03A, 03B) to GitHub repo for dashboard access |
| 11 | committed | All documentation (84 files) | Added all previously untracked files: IonWave/*.md analysis deliverables, core/, standards/, systems/, processes/, ci-protocol/, tracking/ (42 files), root docs |
| 12 | created | `dashboard/views/financial-forecast.html` | New dedicated dashboard view for financial model with 3 scenarios, recommendations, sensitivity analysis, go/no-go frameworks |

### Next Steps
- [ ] Review Financial Model findings with Danilo — validate base case assumptions, discuss staged capital strategy
- [ ] Decide on revenue target revision: $30K MRR in 18 months OR $15K MRR in 12 months
- [ ] Line up follow-on capital sources for Month 6 decision point (angels, seed funds, RBF options)
- [ ] Address Q9 (Positioning-Economics Tension) — strategic decision on marine plasma vs. broader electrolyte positioning
- [ ] Continue to Tier 2 files: File 05A (Product Strategy), File 04 (Planning & Roadmaps), or File 06 (Unit Economics audit)
- [ ] Update ODD-1 thesis with revised timeline and capital plan based on financial model
- [ ] Build ad testing plan for CAC discovery (Months 1-2) with $5K allocation and kill criteria

---

## Session 2026-02-04 #3 — Marine Plasma Market Sizing & Seaonic Revenue Estimation
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Estimated Seaonic's revenue (~$100-180K/year) via five-signal triangulation (Trustpilot reviews, Amazon BSR, Loox reviews, website traffic, operational profile). Mapped the full marine plasma competitive landscape (13+ brands across 3 segments). Sized the marine plasma DTC sachet sub-segment at $300K-$1.5M/year (US). Key finding: the segment alone is too small for ODD-1's $100K MRR target; thesis reframed — marine plasma is a differentiation tool within the $1.5B US electrolyte sachet market, not a market definition.

### Decisions Made
- Seaonic revenue converges at ~$100-180K/year across 5 independent signals
- Marine plasma DTC sachet segment (US) estimated at $300K-$1.5M/year — too small for $100K MRR target alone
- Thesis reframed: marine plasma = differentiation tool (positioning), not market definition (TAM)
- $30K MRR Year 1 target is achievable IF drawing from broader electrolyte market (~500 monthly orders = 0.03% of US electrolyte sachet market)
- Gap 5 (sub-segment sizing) upgraded from D → C+ confidence
- 01_Strategic_Foundation quality score: 6/10 → 6.5/10

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `IonWave/Marine_Plasma_Market_Sizing.md` | Full 3-section deliverable: Seaonic revenue triangulation, segment sizing, competitive landscape (13+ brands), thesis reframing |
| 2 | edited | `IonWave/Strategic_Foundation_Analysis.md` | v1.1.0 → v1.2.0: Gap 5 updated to "PARTIALLY FILLED" with sizing data; capital tension revenue target updated; scorecard thesis clarity 6→6.5; upgrade shopping list updated |
| 3 | edited | `data/01_strategic_foundation/_meta.json` | v1.2.0 → v1.3.0: quality 6→6.5/10; market_sizing reference added; blockers and next_action updated |
| 4 | edited | `data/manifest.json` | 01 quality 6→6.5/10; market_sizing field added |
| 5 | edited | `processes/Dependency_Map.md` | 01 quality updated; sub-segment sizing feedback loop RESOLVED; Market Sizing added to Analysis Deliverables table |
| 6 | edited | `DOCUMENTATION_INDEX.md` | Marine_Plasma_Market_Sizing.md added; SF Analysis version bumped; counts 41→42, 103→104 |

### Next Steps
- [ ] Research Female Wellness ICP (3-4 hrs Track A)
- [ ] Collect fasting-specific VOC (2-3 hrs Track A)
- [ ] Research alternative marine plasma suppliers (1-2 hrs Track A) — Ibiza & Formentera identified as potential alternative to Biocean
- [ ] Build/audit 08_Financial_Model — CRITICAL (2-8 hrs Track A+B) — validate $30K MRR target
- [ ] Model unit economics by segment to resolve positioning-economics tension
- [ ] Populate 02_Market_Intelligence Market Data sheet with competitive landscape data from Marine_Plasma_Market_Sizing.md

---

## Session 2026-02-04 #2 — Persona Dialogues (ICP + Strategic Foundation)
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Ran full CI Protocol persona dialogues on both ICP Analysis (ICP-2026-02-04-001) and Strategic Foundation Analysis (SF-2026-02-04-001). Each dialogue ran 8 rounds to saturation. Applied all upgrades to deliverable .md files, xlsx sheets, JSON data layer, and tracking documents. Also created dialogue summary traceability documents.

### Decisions Made
- Both dialogues ran to saturation (8 rounds each, 3 consecutive RESOLVED at end)
- ICP Analysis: 4 upgrades applied (job vs switch trigger distinction, Weekend Warrior softened, Job 3 downgraded from "strongest opening" to "most promising hypothesis to test first", positioning-economics tension flagged)
- Strategic Foundation Analysis: 5 upgrades applied (sub-segment sizing gap, hypothesis framing, kill criterion sharpened to "50 email opt-ins from marine plasma landing page," replacement financial narrative $30K MRR, Right to Win reframed as singular)
- Quality scores updated: 01 from ~5.5/10 → ~6/10, 03A from ~6.5/10 → ~7/10
- Three previously OPEN feedback loops resolved; two new OPEN loops added (positioning-economics tension, sub-segment sizing)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `IonWave/ICP_Dialogue_Summary.md` | Full traceability record: 8 rounds, 4 tensions, saturation log, key insights |
| 2 | created | `IonWave/Strategic_Foundation_Dialogue_Summary.md` | Full traceability record: 8 rounds, 5 tensions, saturation log, key insights |
| 3 | edited | `IonWave/ICP_Analysis.md` | v1.0.0 → v1.1.0: applied 4 dialogue upgrades (job/switch distinction, Weekend Warrior, Job 3, positioning-economics) |
| 4 | edited | `IonWave/Strategic_Foundation_Analysis.md` | v1.0.0 → v1.1.0: applied 5 dialogue upgrades (sub-segment sizing, hypothesis framing, kill criterion, financial narrative, Right to Win) |
| 5 | edited | `IonWave/03A_Customer_Research_ICP.xlsx` | Updated ICP Analysis sheet: Job 3, strategic implications, gap 5 completed, gap 6 added, dialogue metadata |
| 6 | edited | `IonWave/01_Strategic_Foundation.xlsx` | Updated Analysis Summary sheet: quality score, dialogue results, Gap 5 added, persona dialogue status |
| 7 | edited | `data/01_strategic_foundation/_meta.json` | v1.1.0 → v1.2.0: quality 5.5→6/10, analysis_deliverable updated with dialogue run, blockers/next_action updated |
| 8 | edited | `data/03a_customer_research_icp/_meta.json` | v1.0.0 → v1.1.0: quality 6.5→7/10, strategic_implications updated, analysis_deliverable added with dialogue run, gaps updated |
| 9 | edited | `data/manifest.json` | 01 quality 5.5→6/10 + persona_dialogue field; 03A quality 6.5→7/10 + analysis_deliverable + persona_dialogue field |
| 10 | edited | `processes/Dependency_Map.md` | Tier 1 rows updated (01 + 03A quality, blockers, next actions); 3 feedback loops RESOLVED; 2 new OPEN loops added; Analysis Deliverables table updated |
| 11 | edited | `DOCUMENTATION_INDEX.md` | Added ICP_Dialogue_Summary.md and Strategic_Foundation_Dialogue_Summary.md; version bumped ICP Analysis and SF Analysis; counts 39→41, 101→103 |

### Next Steps
- [ ] Research Female Wellness ICP (3-4 hrs Track A)
- [ ] Collect fasting-specific VOC (2-3 hrs Track A)
- [ ] Estimate Seaonic revenue for sub-segment sizing (2-3 hrs Track A)
- [ ] Research alternative marine plasma suppliers (1-2 hrs Track A)
- [ ] Build/audit 08_Financial_Model — CRITICAL (2-8 hrs Track A+B)
- [ ] Model unit economics by segment to resolve positioning-economics tension
- [ ] Validate $30K MRR Year 1 target via financial modeling
- [ ] Continue JSON migration (Tier 2+ files as they're worked on)
- [ ] Phase 4: Apply metadata to methodologies (carried from Session #4)
- [ ] Review README.md for outdated content (carried)
- [ ] Find or recreate 01_Studio3_Context.md (carried)

---

## Session 2026-02-04 #1 — Dashboard Creation & Deployment
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Created a static HTML dashboard ("Mission Control") for the IonWave Bootstrap project, deployed it to GitHub Pages, and expanded it with output module visualizations. The dashboard provides a visual interface for Danilo and the team to see project status, Porter's Five Forces analysis, ICP personas, and unit economics at a glance.

### Decisions Made
- Dashboard architecture: single HTML file, all CSS/JS inline, zero dependencies, dark mission-control aesthetic
- Data approach: hardcoded from current tracking file state (static snapshot, regenerated on demand)
- Hosting: GitHub Pages (free, auto-deploys on push) at https://caio-camargo.github.io/ionwave-dashboard/
- Layout: 3-column project status view + full-width sections for Porter's, ICP, Unit Economics
- Update workflow: tell Claude "update the dashboard" and it reads tracking files, edits HTML, pushes to GitHub

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | created | `dashboard.html` | Full mission control dashboard with project status (phases, blockers, discrepancies, questions, sprint priorities) |
| 2 | created | `DASHBOARD_UPDATE_GUIDE.md` | How-to guide for updating and deploying the dashboard |
| 3 | edited | `DOCUMENTATION_INDEX.md` | Added dashboard.html and DASHBOARD_UPDATE_GUIDE.md to Category 1 table and Quick Reference |
| 4 | edited | `00_START_HERE.md` | Added dashboard link as first item in Finding Things section |
| 5 | created | `C:\Users\caioa\repos\ionwave-dashboard\` | Local git repo for GitHub Pages deployment |
| 6 | deployed | GitHub Pages | Live at https://caio-camargo.github.io/ionwave-dashboard/ |
| 7 | expanded | `dashboard.html` | Added Porter's Five Forces (5 force gauges, competitor table, strategic implications), ICP & Personas (3 persona cards, JTBD matrix, archetype validation), Unit Economics (3 scenarios, kill triggers, break-even) |

### Next Steps
- [ ] Update dashboard when tracking files change (say "update the dashboard")
- [ ] Consider adding more output modules as new analyses are completed
- [ ] Dashboard could eventually auto-generate from .md files via a build script

---

## Session 2026-02-03 #5 — Context Loading & Strategic Foundation Audit
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: In Progress

### Summary
Read all required docs (00_START_HERE, 02_Glossary, 03_What_We_Did, 04_Working_Principles). Reviewed session log and Dependency Map. Performed detailed audit of 01_Strategic_Foundation.xlsx to assess current state before deciding next work priorities.

### Decisions Made
- Strategic Foundation audit captured here for cross-session persistence (avoids creating separate files)

### 01_Strategic_Foundation.xlsx — Audit Results

**5 sheets, overall ~4.5/10:**

| Sheet | Content Summary | Quality |
|-------|----------------|---------|
| Thesis (Sheet 5) | Falsifiable hypothesis ("room for #2 in marine plasma at 10-15% below Seaonic"), real competitor data (LMNT $66M rev, Seaonic details), 5 kill criteria with thresholds, honest differentiation assessment (price arbitrage=WEAK, flavored=STRONGEST) | ~6-7/10 |
| ODD-1 Complete Thesis (Sheet 4) | Full investment thesis — TAM/SAM/SOM ($5B+/$500M/$50M), problem/solution, why now, the ask ($30-50K). First-pass pitch, less self-aware than Sheet 5 | ~4-5/10 |
| Assumptions Register (Sheet 1) | 5 assumptions: CAC <$40 (Med), LTV >$120 (Low), sub rate >50% (Med), churn <8% (Low), margin >65% (High). Clean but thin | ~5/10 |
| Narrative Hypothesis Table (Sheet 3) | 6 narratives to test (e.g., "78 minerals vs just 3"). Good framework, all "Testing" status, zero evidence filled in | ~3/10 |
| Interview Insights Synthesis (Sheet 2) | 100% empty template — headers for pain points, JTBD, segments, quotes. Every data cell blank or placeholder | ~1/10 |

**Key Gaps Identified:**
1. Two conflicting theses — ODD-1 (broad $5B electrolyte market) vs Thesis (narrow marine plasma #2 behind Seaonic). Need reconciliation.
2. Interview Insights entirely hollow — VOC work done in 03B not connected back here.
3. Narrative Hypotheses have zero evidence despite framework existing.
4. "Right to Win" is assertion-only (no past results, team credentials, or portfolio evidence).
5. No linkage between Assumptions Register and 06_Unit_Economics or 08_Financial_Model.

**Strongest Asset:** Sheet 5 (Thesis) — kill criteria, competitive honesty, and falsifiable framing are investor-grade thinking.

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Read | `00_START_HERE.md`, `core/02_Glossary.md`, `core/03_What_We_Did.md`, `core/04_Working_Principles_updated.md` | Required session reading |
| 2 | Read | `SESSION_LOG.md` | Last 3 entries for context |
| 3 | Read | `processes/Dependency_Map.md` | Work sequence and dependencies |
| 4 | Audited | `IonWave/01_Strategic_Foundation.xlsx` | Full 5-sheet quality assessment (results above) |
| 5 | Edited | `00_START_HERE.md` | Added "Applying expert frameworks" and "Structuring a deliverable" routing entries to Finding Things section |
| 6 | Edited | `DOCUMENTATION_INDEX.md` | Added "Applying expert frameworks" routing entry to Quick Reference table |
| 7 | Read | `standards/Deliverable_Structure_Standards.md` | Output format requirements for 3-section deliverable |
| 8 | Audited | `IonWave/02_Market_Intelligence.xlsx` | 9-sheet baseline assessment — no Porter's exists yet |
| 9 | Researched | Web sources | Market size, supplier landscape, DTC costs, LMNT lawsuits, DIY substitutes, Liquid IV/Unilever |
| 10 | Created | `IonWave/Porter_Five_Forces_Analysis.md` | Full Porter's Five Forces v1.0.0 — 3-section deliverable (Main + 5 Gaps + Scorecard). Overall grade: B- |
| 11 | Read | `ci-protocol/04_PERSONA_DIALOGUE.md` | Dialogue protocol, saturation rules, round logging format |
| 12 | Executed | Persona Dialogue PFF-2026-02-04-001 | 8 rounds, saturation reached. 5 UPGRADED, 3 RESOLVED. Upgrades: category creation framing, supplier exclusivity vs forward integration, lawsuit opportunity downgrade, DIY moat softening, survival rate + capital tension |
| 13 | Updated | `IonWave/Porter_Five_Forces_Analysis.md` | v1.0.0 → v1.1.0: Applied 5 upgrades from persona dialogue. Added Gap 2A (alternative suppliers). Refined Force 3, Force 4, Force 5, and Scorecard |
| 14 | Created | `IonWave/Porter_Five_Forces_Dialogue_Summary.md` | Traceability record of persona dialogue — full round log, tensions surfaced, key insights, "what would have been missed" |
| 15 | Created | `processes/Porter_Five_Forces_Protocol.md` | Step-by-step protocol document for producing Porter's analysis. 5 phases, prerequisites, quality checklist, lessons from first application. Proper metadata per Document_Metadata_Standards |
| 16 | Edited | `DOCUMENTATION_INDEX.md` | Added Porter's Protocol to processes category, analysis deliverables to IonWave section, protocol routing to Quick Reference table |
| 17 | Added sheet | `IonWave/02_Market_Intelligence.xlsx` | New "Porters Five Forces" sheet (10th sheet). Includes: summary verdict table with per-force grades, strategic implications, 6 intelligence gaps with upgrade paths to A-grade (Track A/B labeled), procedure & traceability section, cross-references to dependent files |
| 18 | Enhanced | `processes/Dependency_Map.md` | Added 3 new sections: Execution Sequence (8-tier prioritized table of all 38 files with quality status, blockers, track, next action), Feedback Loops (3 active loops where downstream challenges upstream), Analysis Deliverables (tracking table for non-xlsx deliverables). Updated Last Updated date |
| 19 | Audited | `IonWave/03A_Customer_Research_ICP.xlsx` | Full 6-sheet quality assessment (~5.5/10). Strengths: specific primary ICP, 5 differentiated archetypes, lifecycle segmentation, strategic "not ICP" section. Gaps: Sheets 4+5 overlap, no confidence grades/source citations, no 03B VOC cross-reference, no JTBD framework, no 3-section deliverable format |
| 20 | Updated | `processes/Dependency_Map.md` | Updated 03A row in Execution Sequence: quality ~5.5/10, audited ✅, blockers and next actions specified |
| 21 | Created | `IonWave/ICP_Analysis.md` | Full ICP analysis v1.0.0 — 3-section deliverable (Main + 5 Gaps + Scorecard). JTBD framework applied to 3 consolidated profiles. VOC cross-referenced (11 of 31 LMNT quotes). Overall grade: B-. Key finding: Job 3 (Daily Wellness/Energy) is strongest opening |
| 22 | Modified | `IonWave/03A_Customer_Research_ICP.xlsx` | Deleted overlapping Sheets 4+5; created consolidated "Psychographic Profiles (Consolidated)" sheet with JTBD mapping, VOC validation, and language sections from both originals |
| 23 | Added sheet | `IonWave/03A_Customer_Research_ICP.xlsx` | New "ICP Analysis" sheet with archetype validation table, JTBD market jobs matrix, strategic implications, 5 intelligence gaps with upgrade paths, procedure & traceability, cross-references |
| 24 | Edited | `DOCUMENTATION_INDEX.md` | Added ICP_Analysis.md to Analysis Deliverables section |
| 25 | Created | `IonWave/Strategic_Foundation_Analysis.md` | Full Strategic Foundation analysis v1.0.0 — 3-section deliverable. Thesis reconciliation (narrow validated), Interview Insights backfill (proxy), Narrative Hypothesis evidence fill, capital tension analysis, Assumptions Register update. Before: ~4.5/10 → After: ~5.5/10 |
| 26 | Backfilled | `IonWave/01_Strategic_Foundation.xlsx` Sheet 2 | Interview Insights Synthesis populated with LMNT proxy data: 4 pain points, 4 JTBD, 5 segment insights, 5 surprising findings, 5 marketing quotes. Explicitly labeled as proxy. |
| 27 | Filled | `IonWave/01_Strategic_Foundation.xlsx` Sheet 3 | Narrative Hypothesis Table: Evidence For, Evidence Against, Confidence, and Status filled for all 6 narratives using Porter's + ICP + VOC data |
| 28 | Reclassified | `IonWave/01_Strategic_Foundation.xlsx` Sheet 4 | ODD-1 Complete Thesis: added "v0 — SUPERSEDED BY THESIS SHEET" header. Retained for TAM/SAM/SOM and capital plan reference |
| 29 | Updated | `IonWave/01_Strategic_Foundation.xlsx` Sheet 1 | Assumptions Register: added new "addressable demand" assumption + capital tension flag from Porter's analysis |
| 30 | Added sheet | `IonWave/01_Strategic_Foundation.xlsx` | New "Analysis Summary" sheet with thesis reconciliation table, capital tension matrix, intelligence gaps, procedure & traceability |
| 31 | Synced | `data/01_strategic_foundation/*.json` | Synced 5 JSON files to match xlsx upgrades: interview_insights (proxy backfill), narrative_hypotheses (evidence fills), odd1_thesis (v0 superseded), assumptions_register (capital tension + new assumption), _meta (quality 4.5→5.5, feedback loops resolved) |
| 32 | Updated | `data/manifest.json` | Updated 01_strategic_foundation quality to 5.5/10, added analysis_deliverable reference, updated 3 feedback loop statuses (1 flagged, 1 resolved, 1 resolved_with_proxy) |
| 33 | Reviewed | Git setup, JSON migration, dashboard | Reviewed refactoring done in parallel instance: git repo (caio-camargo/ionwave-dashboard), .gitignore (xlsx excluded), JSON data layer (data/), dynamic dashboard (dashboard/), migration guide. 00_START_HERE.md and DOCUMENTATION_INDEX.md already updated by other instance |
| 34 | Edited | `00_START_HERE.md` | Added "Version Control — Git / GitHub" section documenting repo, branching, .gitignore policy, what gets committed vs not, deployment |

### Decisions Made
- Strategic Foundation audit captured here for cross-session persistence (avoids creating separate files)
- Porter's Five Forces analysis produced as standalone .md file (not embedded in xlsx) to enable persona dialogue and version control
- Persona dialogue surfaced capital tension: $30-50K raise may be insufficient given structural forces (rising CPMs, category creation costs, zero switching costs) — flagged for Strategic Foundation review
- Created narrow Porter's Protocol (not broader "Expert Framework Protocol") per Caio's direction; other frameworks may already have undergone this process

### Next Steps
- [ ] Review `README.md` for outdated content (carried from Session #4)
- [ ] Find or recreate `01_Studio3_Context.md` (carried from Session #4)
- [x] ~~Phase 3: Enhance `processes/Dependency_Map.md` with sequencing~~ — DONE (8-tier execution sequence, feedback loops, analysis deliverables added)
- [ ] Phase 4: Apply metadata to methodologies (carried from Session #4)
- [x] ~~Phase 5: Execute Porter's Five Forces analysis on 02_Market_Intelligence~~ — DONE (v1.1.0 with persona dialogue)
- [x] ~~Integrate Porter's Five Forces into 02_Market_Intelligence.xlsx as a new sheet~~ — DONE (10th sheet added with grades, procedure, upgrade paths)
- [ ] Execute Gap 1: Contact Actimar/Biocean for supplier pricing (CRITICAL — human task)
- [ ] Execute Gap 2: Research Seaonic's supplier relationship (1-2 hours)
- [ ] Execute Gap 2A: Research alternative marine plasma suppliers outside Actimar/Biocean family (HIGH — from persona dialogue)
- [x] ~~Evaluate capital tension~~ — DONE (flagged in Assumptions Register + Analysis Summary sheet; new demand-existence assumption added)
- [x] ~~Reconcile two conflicting theses~~ — DONE (narrow thesis validated by Porter's + ICP evidence; ODD-1 reclassified as v0)
- [x] ~~Connect 03B VOC to Interview Insights~~ — DONE (proxy backfill: 4 pain points, 4 JTBD, 5 segments, 5 findings, 5 marketing quotes; labeled as LMNT proxy)
- [x] ~~Fill Narrative Hypothesis Table~~ — DONE (all 6 narratives now have Evidence For/Against + Confidence + Status from Porter's/ICP/VOC)
- [ ] Build/audit financial model (08_Financial_Model.xlsx) linking assumptions to revenue — CRITICAL, capital tension unresolvable without this
- [ ] Strategic Foundation: Run persona dialogue stress-test
- [ ] Strategic Foundation: Document Right to Win evidence (needs Caio input)
- [x] ~~Audit 03A_Customer_Research_ICP~~ — DONE (~5.5/10; 6 sheets, substantive but lacks quality system compliance)
- [x] ~~Upgrade 03A: Consolidate Sheets 4+5~~ — DONE (merged into single "Psychographic Profiles (Consolidated)" sheet)
- [x] ~~Upgrade 03A: Apply JTBD framework~~ — DONE (3-layer mapping for all 3 profiles + 4 market jobs)
- [x] ~~Upgrade 03A: Cross-reference 03B VOC quotes~~ — DONE (11 of 31 quotes mapped to personas; validation matrix produced)
- [x] ~~Upgrade 03A: Add confidence grades~~ — DONE (full ICP_Analysis.md with A/B/C/D grades throughout)
- [ ] ICP Analysis: Run persona dialogue stress-test (pending — Priority 5 in upgrade list)
- [ ] ICP Analysis: Research Female Wellness secondary ICP (Track A, 3-4 hours)
- [ ] ICP Analysis: Collect fasting-specific VOC (Track A, 2-3 hours)

---

## Session 2026-02-03 #4 — Folder Reorganization
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Reorganized all files from flat root directory into categorized folders. Created 7 new directories (core/, standards/, systems/, tracking/, processes/, ci-protocol/, IonWave/). Archived duplicates, old versions, historical extraction docs, and old process xlsx files. Updated all cross-references in DOCUMENTATION_INDEX.md and 00_START_HERE.md.

### Decisions Made
- Folder names match DOCUMENTATION_INDEX categories for consistency
- Trade xlsx files go in `IonWave/` (user's choice over `trades/`)
- CI Protocol (10 numbered files 00-09) gets its own folder — was previously unlisted in index
- Extra xlsx files (LMNT, Competitive Intelligence, etc.) archived as old process outputs per user
- Category 7 extraction docs archived (all historical)
- Old duplicates archived: Model_Orchestration.md, Discrepancy_Register.md, README_START_HERE.md, README_START_HERE (1).md
- 5 files stay in root: 00_START_HERE.md, SESSION_LOG.md, DOCUMENTATION_INDEX.md, README.md, Master_Index.md
- Quality_Architecture_Integration_v2.md placed in standards/ (not previously categorized)
- DOCUMENTATION_INDEX.md bumped to v2.0.0 with folder structure map and CI Protocol as new Category 7

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Created dirs | `core/`, `standards/`, `systems/`, `tracking/`, `processes/`, `ci-protocol/`, `IonWave/` | 7 new folders |
| 2 | Moved to archive | `Model_Orchestration.md` | Superseded by _updated |
| 3 | Moved to archive | `Discrepancy_Register.md` | Superseded by _updated |
| 4 | Moved to archive | `README_START_HERE (1).md` | Duplicate |
| 5 | Moved to archive | `README_START_HERE.md` | Outdated |
| 6 | Moved to core/ | `02_Glossary.md`, `03_What_We_Did.md`, `04_Working_Principles_updated.md` | Category 2 |
| 7 | Moved to standards/ | `Document_Metadata_Standards.md`, `VERSION_MANIFEST.md`, `Deliverable_Structure_Standards.md`, `Model_Orchestration_updated.md`, `Manifest_Verification_Workflow.md`, `Quality_Architecture_Integration_v2.md` | Category 3 |
| 8 | Moved to systems/ | 7 system overview files | Category 4 |
| 9 | Moved to tracking/ | 42 tracking/log files | Category 5 |
| 10 | Moved to processes/ | `DEMO_How_System_Works.md`, `Dependency_Map.md`, `Knowledge_Logistics_Audit.md`, `Workbook_Generation_Summary.md` | Category 6 |
| 11 | Moved to ci-protocol/ | 10 CI Protocol files (00_INDEX through 09_RUNTIME) | New Category 7 |
| 12 | Moved to IonWave/ | 42 Trade xlsx files | Trade files |
| 13 | Moved to archive | 7 extra xlsx files | Old process outputs |
| 14 | Moved to archive | 6 extraction docs | Category 8 (historical) |
| 15 | Rewrote | `DOCUMENTATION_INDEX.md` | v2.0.0 — folder paths, CI Protocol category, updated counts |
| 16 | Edited | `00_START_HERE.md` | All file references updated with folder paths |
| 17 | Edited | `archive/obsolete-2026-02-03/README.md` | Added all newly archived files |

### Next Steps
- [ ] Review `README.md` for outdated content
- [ ] Find or recreate `01_Studio3_Context.md`
- [ ] Phase 3: Enhance `processes/Dependency_Map.md` with sequencing
- [ ] Phase 4: Apply metadata to methodologies
- [ ] Phase 5: Execute Porter's Five Forces analysis

---

## Session 2026-02-03 #3 — Archive Cleanup Process Docs
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Archived the 4 documentation cleanup process files now that cleanup is complete. Updated the archive README to document them.

### Decisions Made
- All 4 cleanup docs archived (none kept in root) — cleanup work is done, docs serve only as historical reference now

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Moved to archive | `CLAUDE_CODE_CLEANUP_PROMPT.md` | Cleanup execution instructions — completed |
| 2 | Moved to archive | `Documentation_Cleanup_Action_Plan.md` | Cleanup planning doc — completed |
| 3 | Moved to archive | `Documentation_Cleanup_COMPLETE.md` | Cleanup summary — completed |
| 4 | Moved to archive | `01-04_Audit_Report.md` | Core docs audit findings — acted on |
| 5 | Edited | `archive/obsolete-2026-02-03/README.md` | Added cleanup process docs section |

### Next Steps
- [ ] Review `README.md` and `README_START_HERE.md` for outdated content
- [ ] Review `01_Studio3_Context.md` for outdated references
- [ ] Phase 3: Enhance `Dependency_Map.md` with sequencing
- [ ] Phase 4: Apply metadata to methodologies
- [ ] Phase 5: Execute Porter's Five Forces analysis

---

## Session 2026-02-03 #2 — Session Log Setup
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Created SESSION_LOG.md for cross-session persistence and added logging instructions to 00_START_HERE.md so future sessions know to use it.

### Decisions Made
- Log lives in root directory (not archive/) for visibility
- Replaced outdated "For Claude Code Users" section in 00_START_HERE.md with session logging instructions
- Log format: reverse chronological, session summaries + granular action tables, supports both Claude Code and manual entries

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Created | `SESSION_LOG.md` | Persistent action log with template and backfilled Session #1 |
| 2 | Edited | `00_START_HERE.md` | Replaced "For Claude Code Users" section with "Session Logging (Required)" instructions |

### Next Steps
- [ ] Review `README.md` and `README_START_HERE.md` for outdated content
- [ ] Review `01_Studio3_Context.md` for outdated references
- [ ] Phase 3: Enhance `Dependency_Map.md` with sequencing
- [ ] Phase 4: Apply metadata to methodologies
- [ ] Phase 5: Execute Porter's Five Forces analysis

---

## Session 2026-02-03 #1 — Documentation Cleanup Execution
**Source**: Claude Code
**User**: Caio
**AI Model**: claude-sonnet-4-5-20250929
**Status**: Complete

### Summary
Executed documentation cleanup based on completed audit. Archived 3 obsolete/duplicate files, verified updated core docs were already in place, and updated the documentation index to reflect current state.

### Decisions Made
- Modified the original cleanup plan: 2 of 4 listed obsolete files (`01_Studio3_Context.md`, `Market_Landscape_Bootstrap_Plan__1_.md`) were not found in the directory — skipped rather than erroring
- Updated core docs (00_START_HERE, 02_Glossary, 03_What_We_Did) were already in place with correct content — no archive-and-replace needed
- Filename correction: `CM_System_Overview (1).md` (actual) vs `CM_System_Overview__1_.md` (listed in plan)

### Actions Taken
| # | Action | File(s) | Detail |
|---|--------|---------|--------|
| 1 | Created directory | `archive/obsolete-2026-02-03/` | Archive structure for deprecated docs |
| 2 | Moved to archive | `00_MASTER_CONTROL.md` | Obsolete — referenced v10 681-sheet structure |
| 3 | Moved to archive | `00_IMPLEMENTATION_GUIDE.md` | One-time historical change log |
| 4 | Moved to archive | `CM_System_Overview (1).md` | Duplicate of `CM_System_Overview.md` |
| 5 | Created | `archive/obsolete-2026-02-03/README.md` | Archive contents and rationale |
| 6 | Edited | `DOCUMENTATION_INDEX.md` | Updated status of archived files, summary counts, action items |
| 7 | Verified | `00_START_HERE.md` | Confirmed v1.0.0 already in place |
| 8 | Verified | `02_Glossary.md` | Confirmed "Documentation Standards" section present |
| 9 | Verified | `03_What_We_Did.md` | Confirmed "What Happened Since" section present |
| 10 | Created | `SESSION_LOG.md` | This file — persistent action log |

### Next Steps
- [ ] Review `README.md` and `README_START_HERE.md` for outdated content
- [ ] Review `01_Studio3_Context.md` for outdated references
- [ ] Phase 3: Enhance `Dependency_Map.md` with sequencing
- [ ] Phase 4: Apply metadata to methodologies
- [ ] Phase 5: Execute Porter's Five Forces analysis
