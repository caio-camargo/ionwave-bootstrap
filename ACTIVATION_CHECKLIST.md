# Cascade Activation Checklist

> **Purpose:** Everything that must be true before Danilo hands the VA Package to the first VA. This is the pre-flight checklist. No activation without every item checked.
>
> **Status:** NOT READY — 3 blockers remain (see Section 1)
>
> **Last updated:** 2026-03-06

---

## 1. Blocking Decisions (Must Resolve Before Activation)

These are decisions only Danilo can make. The cascade cannot start until all three are resolved.

| # | Decision | ID | Status | What Danilo Needs to Decide | Recommended Default |
|---|----------|----|--------|----------------------------|-------------------|
| 1 | **VA budget** | DEC-CHAIN-005 | OPEN | Hourly vs retainer? How much? | $500-1,000/mo retainer. VA is a 3-5 day/week part-time role. |
| 2 | **Approval authority at handoffs** | DEC-CHAIN-003 | OPEN | Who makes the final call when VA picks MBA intern, when MBA picks VP, when VP picks Operator? Options: (A) fully autonomous, (B) Claude-assisted autonomy, (C) Caio reviews finalists, (D) human gate at VP→Operator only | Option D — autonomous at lower links, calibration session at VP→Operator. Minimizes bottlenecks where stakes are low, adds human judgment where stakes are highest. |
| 3 | **Pre-entity equity instruments** | DEC-CHAIN-007 | OPEN | How to commit equity to MBA intern and VP before an LLC exists? Options: (A) SAFE, (B) promise letter with conversion terms, (C) deferred grant with vesting from start date, (D) wait for entity formation | Option B — promise letter with defined conversion terms. Lightweight, legally defensible with a lawyer review, doesn't require entity formation. Convert to real equity docs within 30 days of entity formation. |

### Partially Resolved (defined but not specific)

| # | Decision | ID | Status | What's Resolved | What's Still Open |
|---|----------|----|--------|----------------|------------------|
| 4 | MBA intern comp | DEC-CHAIN-001 | PARTIAL | Equity (not cash) — confirmed by Danilo | Exact percentage TBD. Recommend 0.5-1%. |
| 5 | VP comp | DEC-CHAIN-002 | PARTIAL | Equity — confirmed | Exact percentage (5-10% range). Retainer (yes/no, amount). |

### Not Blocking Activation (can resolve during cascade)

| # | Decision | ID | Status | Notes |
|---|----------|----|--------|-------|
| 6 | Chain parallelization | DEC-CHAIN-004 | OPEN | Sequential is the default. Parallelization is an optimization, not a prerequisite. |
| 7 | Fallback at MBA→VP link | DEC-CHAIN-006 | OPEN | Only relevant if the link breaks. Danilo has acknowledged his emergency valve. |

---

## 2. Documents Ready (All Complete)

Every node in the cascade has a Day 1 kickoff package. These are built and pushed.

| # | Document | Node | Status |
|---|----------|------|--------|
| 1 | `VA_KICKOFF_PACKAGE.md` | VA (L1) | Done |
| 2 | `MBA_INTERN_KICKOFF_PACKAGE.md` | MBA Intern (L2) | Done |
| 3 | `VP_KICKOFF_PACKAGE.md` | VP (L3) | Done |
| 4 | `TRADE_EXECUTION_PATH.md` | Reference (all nodes) | Done |
| 5 | Trade Pitch One-Pager | Pitch material (all nodes) | Done (in `ionwave/data/rollout/`) |
| 6 | Chain Specification | System design | Done (in `ionwave/data/rollout/`) |
| 7 | Deliverable Registry | Compliance agent reference | Done (in `ionwave/data/rollout/compliance/`) |
| 8 | Agent Specification | Compliance agent design | Done (in `ionwave/data/rollout/compliance/`) |

---

## 3. System Infrastructure Ready

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | `chain_state.json` initialized | Done | All nodes at `not_started`. 15 deliverables tracked. Event log started. |
| 2 | Deliverable registry defined | Done | 15 deliverables across VA (5), MBA (5), VP (5). Triggers, deadlines, eval criteria all specified. |
| 3 | Compliance agent spec | Done | Claude-as-workspace model. Escalation levels L0-L3. Pattern detection flags. |
| 4 | Tooling requirements | Done | Phase 1: git repo + Claude sessions. No external tools needed. |

---

## 4. Source Materials Ready

The VA doesn't need to understand the Trade — they need the VA Package and the One-Pager. But the downstream packages reference these materials, so they must exist.

| # | Material | Who Needs It | Status |
|---|----------|-------------|--------|
| 1 | VA Package (5 files) | VA | Done (`ionwave/data/rollout/va_package/`) |
| 2 | MBA Brief (6 files) | MBA Intern | Done (`ionwave/data/rollout/mba_brief/`) |
| 3 | VP Brief (5 files) | VP | Done (`ionwave/data/rollout/vp_brief/`) |
| 4 | Trade Pitch One-Pager | All downstream | Done (`ionwave/data/rollout/`) |
| 5 | M0 Trade Thesis | VP + Operator | Done (`ionwave/data/m0_trade_thesis/`) |
| 6 | M1 Operator System | VP + Operator | Done (`ionwave/data/m1/`) |
| 7 | M4 Fundraising | VP | Done (`ionwave/data/m4/`) — if migrated |
| 8 | M35 Execution Plans | VP + Operator | Done (`ionwave/data/m35/`) — if migrated |

---

## 5. Activation Sequence (When All Blockers Cleared)

When Danilo resolves the 3 blocking decisions, activation is a single-day process:

### Day 0: Activate

1. **Update `chain_state.json`:**
   - Set `cascade_status` → `active`
   - Set `cascade_started` → today's date
   - Clear `activation_blockers` array
   - Set `nodes.va.status` → `hiring`
   - Log activation event

2. **Update compensation fields:**
   - `nodes.va.compensation.amount` → resolved VA budget
   - `nodes.mba.compensation.amount` → resolved MBA equity %
   - `nodes.vp.compensation.amount` → resolved VP equity %

3. **Update transition approval authority:**
   - Set `transitions[*].approval_authority` → resolved per DEC-CHAIN-003

4. **Prepare VA handoff package:**
   - Print/export `VA_KICKOFF_PACKAGE.md`
   - Print/export Trade Pitch One-Pager
   - Prepare bilateral contract with resolved compensation
   - Prepare Claude workspace access (if applicable)

5. **Danilo hands off to VA:**
   - One meeting or async handoff
   - VA receives: kickoff package, one-pager, bilateral contract, Claude access
   - Update `chain_state.json`: `nodes.va.status` → `active`, `nodes.va.start_date` → today
   - DEL-VA-001 clock starts (48 hours)

### That's it. The cascade is live.

From here, the compliance agent (Claude) monitors deliverables per the registry. Each node finds the next. The chain unfolds from a single handoff.

---

## 6. Post-Activation: Compliance Rhythm

Once the cascade is active, the compliance agent follows this rhythm:

| Frequency | Action |
|-----------|--------|
| **Daily** | Check if any deliverable is overdue. If yes, send appropriate nudge/warning per escalation level. |
| **Weekly** | Generate chain status summary: which node is active, deliverable status, pipeline metrics, alerts. |
| **At each transition** | Verify transition deliverable is complete. Apply approval authority per DEC-CHAIN-003. Update `chain_state.json`. Activate next node. |
| **On alert** | Flag pattern-detected issues (low response rates, missed deadlines, pipeline stalls) per deliverable registry specs. |

### Status Report Format (weekly)

```
## Cascade Status — Week [X]
**Active node:** [VA / MBA / VP / Operator]
**Person:** [Name]
**Days active:** [X]

### Deliverable Status
| ID | Name | Status | Due | Notes |
|----|------|--------|-----|-------|
| DEL-XX-00X | ... | pending/submitted/accepted/overdue | date | ... |

### Pipeline
- Contacted: [X]
- Screened: [X]
- Advanced: [X]

### Alerts
- [Any pattern-detected flags or escalations]

### Next Expected Event
- [What should happen next and when]
```

---

## 7. Kill Switches

The cascade can be paused or terminated at any point. These are the triggers:

| Trigger | Action | Who Decides |
|---------|--------|-------------|
| Node fails to deliver after L3 escalation | Activate fallback protocol per chain_specification.md Section 4 | Danilo (via Caio) |
| VA fails to find MBA intern after 6 weeks | Replace VA, expand criteria, or Danilo direct | Danilo |
| MBA fails to find VP after 12 weeks | Replace, pivot (MBA finds Operator directly), Danilo introduces, or pause | Danilo |
| VP fails to find Operator after 6 weeks | Expand search, Danilo refers, or VP operates temporarily | Danilo + VP |
| VP integration artifact fails after 2 attempts | Reconsider VP placement | Danilo |
| Any node misrepresents credentials or work | Immediate termination of that node | Danilo |
| External event (legal, market, funding) changes viability | Pause entire cascade | Danilo |

---

## Quick Status

```
Cascade:     PRE-ACTIVATION
Blockers:    3 (DEC-003, DEC-005, DEC-007)
Documents:   8/8 complete
Nodes ready: 4/4 (VA, MBA, VP, Operator packages built)
State file:  Initialized
Next step:   Danilo resolves 3 blocking decisions → activate
```
