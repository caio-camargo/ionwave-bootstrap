# Integration Design Principles

**Version**: 1.0.0
**Author**: Caio, Claude
**Date Created**: 2026-02-11
**Last Updated**: 2026-02-11
**AI Model**: claude-sonnet-4-5-20250929
**Purpose**: Design principles for integrated document architecture in Studio 3 systems
**Status**: Active
**Source**: Danilo's essay "Designing Content Types for Information Integration, Part 2"
**Related**: PASSET_FOLDER_STRUCTURE.md, CLAUDE_AS_OS_SYSTEM.md

---

## Core Thesis

**Integrated documents serve as surfaces where work happens. Disintegrated documents serve as signposts that point elsewhere.**

For AI-augmented execution systems (like Claude-as-OS), this distinction is critical: **a context window IS a document surface**. Fragmented information architectures create coordination artifacts that break AI's ability to help.

**Design Goal**: Create high-phi information boundaries where all context needed for action exists within a single surface.

---

## The Six Principles (Applied to Studio 3)

### 1. Embed Action

**Principle**: Decision interfaces belong inside the document, not external.

**Anti-pattern (Disintegrated)**:
```markdown
# Week 6 Tasks
- Set up Stripe account
- Configure payment processing
- Return here when done
```
→ Operator must leave the document, context is lost, no record of what happened

**Pattern (Integrated)**:
```markdown
# Week 6 Tasks

## IMP-M9-003: Set up Stripe account
- Source: M9: Ecommerce (M9-Payment Setup tab)
- Owner: CoS
- Due: 2026-02-15
- Dependencies: IMP-M2-001 (C-Corp formation complete)
- Status: In Progress

**Action Checklist**:
- [x] Create Stripe account
- [x] Verify business details
- [ ] Set up webhook endpoints
- [ ] Test payment flow

**API Keys** (record for reference):
- Public Key: pk_live_... (stored in 1Password vault "IonWave-Production")
- Webhook Secret: whsec_... (stored in 1Password vault "IonWave-Production")

**Test Results**:
- Test transaction: $1.00 charged to test card ending 4242
- Webhook received at https://ionwave.com/api/stripe-webhook
- Order created in Shopify: #1001

**Notes**: Payment flow working. Ready to process live transactions.

**Verified**: ☑ (matches M9 specification for payment processing)
```
→ All action context embedded in the document. Nothing external except secure credential storage.

**Operationalization Rules**:
- ✅ Task files include action checklists, not just task names
- ✅ Test results recorded inline, not in separate documents
- ✅ Decisions documented where actions happen
- ✅ API keys referenced (not stored), with pointer to secure vault
- ❌ Never: "See external doc for details"
- ❌ Never: "Update spreadsheet when done"

---

### 2. Self-Awareness

**Principle**: Documents should model their own completion state.

**Anti-pattern (Disintegrated)**:
```
Week 6 folder exists. No way to know if week is complete without checking external tracker.
```

**Pattern (Integrated)**:
```markdown
# Week 6 Status (Feb 10-16, 2026)

**Completion**: 12/15 tasks done (80%)
**Blockers**: 1 active (IMP-M24-003 waiting for 3PL contract signature)
**On Track**: YES (projected completion by EOD Feb 16)

**Phase Progress**:
- ICL-1 Soft Launch: Week 2 of 4 (50% through phase)
- Next milestone: First 100 orders (currently at 67)

**Task Breakdown by Status**:
- Done: 12
- In Progress: 2
- Blocked: 1
- Not Started: 0

**Week Health**: 🟢 Green (all critical path items complete or on track)
```

**Operationalization Rules**:
- ✅ Every time block (week/month) has a status file
- ✅ Status is COMPUTED from task states, not manually entered
- ✅ Completion % visible at-a-glance
- ✅ Blockers surfaced immediately
- ✅ Phase progress contextualized (where are we in the larger arc?)
- ✅ Health indicators (🟢🟡🔴) based on objective criteria
- ❌ Never: Status lives only in someone's head
- ❌ Never: "I think we're done?" uncertainty

**Claude Query Pattern**:
```
Operator: "How's Week 6 going?"
Claude: [reads week-6/status.md] "80% complete, 1 blocker on 3PL contract,
on track for Friday completion. You're at 67/100 orders milestone."
```

---

### 3. Adjacent Reflection

**Principle**: Pair actions with prompts that encourage thinking about outputs.

**Anti-pattern (Disintegrated)**:
```markdown
- [x] Launch first ad campaign
```
→ No reflection, no learning captured

**Pattern (Integrated)**:
```markdown
- [x] **IMP-M13-005**: Launch first ad campaign
  - Creative used: VSL-v1-hook-3 (30-sec)
  - Budget: $100/day
  - Target: Women 25-45, health-conscious, US

  **Reflection Prompts**:
  1. What was your hypothesis for this creative/audience combo?
     → "Hypothesis: The '78 minerals' hook would resonate with health-conscious
        women who already use supplements. Expected CPA ~$45."

  2. What actually happened in first 48 hours?
     → "Actual CPA: $52. CTR: 1.8% (expected 2.5%). Hook didn't land.
        Comments show confusion about 'ocean minerals' vs regular electrolytes."

  3. What would you do differently next time?
     → "Next creative should lead with BENEFIT (performance/energy) not
        INGREDIENT (ocean minerals). Test hook: 'Feel the difference in 20 minutes.'"

  4. Update to strategy/playbook?
     → "Updated M13-Creative-Testing-Log.md: Ingredient-led hooks underperform
        benefit-led hooks by ~30% CPA. Prioritize benefit messaging."
```

**Operationalization Rules**:
- ✅ Every completed task has a "Reflection" or "Learning" section
- ✅ Reflection prompts are STANDARDIZED (same 3-4 questions for all tasks in a category)
- ✅ Learnings feed back into Imagination Passet references (update M13 playbook)
- ✅ Hypothesis → Result → Learning loop is explicit
- ✅ Failed experiments are CELEBRATED (learning captured)
- ❌ Never: Task marked done with no reflection
- ❌ Never: "We tried something and it didn't work" with no documentation of why

**Standard Reflection Templates**:

**For Launch/Test Tasks**:
1. What was your hypothesis?
2. What actually happened?
3. What would you do differently?
4. Update to strategy/playbook?

**For Decision Tasks**:
1. What were the options considered?
2. What decision criteria did you use?
3. Why did you choose this option?
4. What would trigger a reversal of this decision?

**For Blocker Resolution Tasks**:
1. What was the blocker?
2. Root cause analysis - why did it happen?
3. How did you resolve it?
4. How do we prevent this class of blocker in future?

---

### 4. Accumulation

**Principle**: Leave traces—answers, checkboxes, timestamps become a thinking record.

**Anti-pattern (Disintegrated)**:
```
Slack conversations disappear. Email threads get lost. Decisions made verbally.
No record of "why we chose Supplier A over Supplier B."
```

**Pattern (Integrated)**:
```markdown
# decisions/decision_log.md

## 2026-02-12: Supplier Selection (Electrolyte Powder)

**Decision**: Selected Supplier A (NutraCorp) over Supplier B (VitaSource)

**Options Considered**:
- Supplier A (NutraCorp): $8.50/unit, 3-week lead time, MOQ 1000 units
- Supplier B (VitaSource): $7.20/unit, 6-week lead time, MOQ 5000 units

**Decision Criteria** (weighted):
1. Lead time (40%): Need to launch in 8 weeks
2. MOQ (30%): Limited capital for first order
3. Price (20%): Important but not critical for initial validation
4. Quality (10%): Both suppliers have GMP certification (equivalent)

**Analysis**:
- Supplier A: Faster to market (3 weeks vs 6 weeks) = critical for launch timeline
- Supplier A: Lower MOQ (1000 vs 5000) = $8,500 vs $36,000 initial outlay
- Supplier B: 15% cheaper per unit but can't meet timeline

**Decision**: Supplier A (NutraCorp)

**Decided By**: CoS (within authority - supplier selection <$10K)

**Context**:
- Launch date: April 1, 2026 (hard deadline for ad campaign coordination)
- Current capital: $45,000 remaining after entity/legal/brand expenses
- Risk tolerance: High on price, low on timeline (investor check-in at Week 12)

**Reversal Triggers**:
- If Supplier A misses delivery by >1 week → escalate to Intermediary
- If quality issues on first batch → consider Supplier B for reorder
- If we raise additional capital → renegotiate for volume pricing

**Learnings for Next Trade**:
- Early supplier vetting (Week -4) would allow longer lead times
- Build supplier contingency plan before committing to launch date
```

**Operationalization Rules**:
- ✅ ALL decisions logged in `/decisions/decision_log.md` (append-only)
- ✅ Decision log format: Options / Criteria / Analysis / Decision / Context / Reversal Triggers
- ✅ Timestamps on every entry
- ✅ Attribution (who decided, under what authority)
- ✅ Learnings captured for next Trade
- ✅ Cross-references to tasks (e.g., "See IMP-M6-008 for execution")
- ❌ Never: "We discussed this in a call" with no written record
- ❌ Never: Decisions in Slack/email that don't get logged
- ❌ Never: "I think we chose X but I'm not sure why"

**Accumulation Categories**:
1. **Decision log** - All choices made (supplier, strategy, hiring, etc.)
2. **Task notes** - Inline context on every task
3. **Reflection entries** - Learnings from experiments
4. **Status snapshots** - Weekly progress records
5. **Dashboard archives** - Historical KPI data
6. **Meeting notes** - If meetings happen, notes go in relevant time-block folder

---

### 5. Structured Departures

**Principle**: When leaving is necessary, create round-trip return paths with re-entry points.

**Anti-pattern (Disintegrated)**:
```markdown
- [ ] Review M13 Media Buying strategy
```
→ Operator leaves to find M13, gets lost in 928-tab spreadsheet, forgets why they were there

**Pattern (Integrated)**:
```markdown
- [ ] **IMP-M13-002**: Set up Meta Business Manager account
  - Source: M13: Media Buying (M13-Platform-Setup tab)
  - Owner: Media Buyer

  **Context for this task**:
  → You're setting up Meta Business Manager to run IonWave ads
  → Week 6 goal: First campaign live by Friday
  → This task unlocks: IMP-M13-003 (Create first ad set)

  **Departure to Imagination Passet** (for "why" and "how"):
  → Open: `/reference/m13-media-buying-guide.md`
  → Section: "Platform Setup Checklist"
  → Key insight: Use BUSINESS account not personal account (ad spend limits)

  **Return checklist** (complete when you're back):
  - [ ] Business Manager created
  - [ ] Payment method added
  - [ ] Ad account created
  - [ ] IonWave page connected
  - [ ] Pixel installed on ionwave.com

  **Re-entry point**: Mark task complete and move to IMP-M13-003
```

**Operationalization Rules**:
- ✅ Every reference to Imagination Passet includes:
  - WHY you're going there (context)
  - WHERE to go (specific file/section)
  - WHAT to look for (key insight)
  - HOW to return (re-entry checklist)
- ✅ `/reference/` folder contains "bridge documents" that summarize Imagination TUPs for quick lookup
- ✅ Bridge documents are MAX 1 page per TUP (executive summary + action checklist)
- ✅ Full Imagination Passet is ALWAYS available but not required for execution
- ❌ Never: "See M13 for details" with no guidance on what to look for
- ❌ Never: External links without context (what will I find there?)
- ❌ Never: Departure without return path

**Bridge Document Template** (`/reference/m13-media-buying-guide.md`):
```markdown
# M13: Media Buying - Quick Reference

**Full Source**: [Link to M13 in Imagination Passet]
**Last Updated**: 2026-02-11
**Use Case**: Reference when setting up campaigns, troubleshooting ROAS, scaling spend

## 30-Second Summary
M13 covers Meta/Google ad buying for D2C supplement launch. Key: Start $100/day,
validate ROAS ≥2.5x by Week 12, then scale to $2-5K/day in Months 4-6.

## Critical Numbers
- Target ROAS: ≥2.5x (kill if <2.0x by Week 12)
- Starting budget: $100/day (Week 5-8), $500/day (Week 9-12)
- Target CPA: ≤$45 (based on LTV $200, 5:1 LTV:CAC ratio)

## Platform Setup Checklist
- [ ] Meta Business Manager (use BUSINESS account, not personal)
- [ ] Payment method added (credit card with $10K limit minimum)
- [ ] Ad account created (US currency, Pacific timezone)
- [ ] Facebook Page connected to Business Manager
- [ ] Pixel installed (test with Pixel Helper Chrome extension)

## Common Blockers
1. **Ad account suspended**: Usually payment verification. Upload utility bill.
2. **Low delivery**: Audience too narrow. Expand from 500K to 2M+ reach.
3. **High CPA**: Creative problem 80% of time, audience problem 20% of time.

## When to Reference Full M13
- Initial campaign setup (Week 5) → Read M13-Platform-Setup, M13-First-Campaign
- ROAS troubleshooting → Read M13-Optimization, M13-Creative-Testing
- Scaling decisions → Read M13-Scale-Protocol, M13-Budget-Ladder
```

---

### 6. Isomorphic Structure

**Principle**: Document architecture should match work structure.

**Anti-pattern (Disintegrated)**:
```
Work happens in phases (Pre-Launch → Soft Launch → Validation → Scale)
Documents organized by domain (Product / Marketing / Operations)
→ Structure doesn't match workflow
```

**Pattern (Integrated)**:
```
Work happens in phases → Documents organized by phases (ICL-0 through ICL-6)
Work happens weekly → Folders organized weekly (week-1/ week-2/ etc.)
Work happens by role → Tasks grouped by role within each week

Operator mental model: "What's this week's work?"
Document structure: week-6/tasks.md with role sections
→ Perfect isomorphism
```

**Operationalization Rules**:
- ✅ Time-clustered architecture (ICL-0 through ICL-6) matches execution phases
- ✅ Weekly granularity matches operational cadence (weekly check-ins, weekly creative reviews)
- ✅ Monthly summaries match reporting cadence (monthly investor updates)
- ✅ Role sections within tasks match how team actually divides work
- ✅ Dashboard structure matches decision-making needs (daily metrics, weekly narrative)
- ❌ Never: Organize by abstract categories that don't match workflow
- ❌ Never: Force work into pre-existing structure (let structure emerge from work)

**Isomorphism Checklist**:
1. **Does folder structure match time structure of work?**
   → YES: ICL phases = actual execution phases
2. **Does granularity match operational cadence?**
   → YES: Weekly folders = weekly work cycles
3. **Does grouping match team structure?**
   → YES: Role sections = how team divides tasks
4. **Does navigation match mental models?**
   → YES: "What's next?" → current week folder
5. **Does accumulation match learning cycles?**
   → YES: Monthly summaries = monthly reflection cadence

---

## High-Phi Information Architecture

**Information Integration Theory Applied**:

**Phi (Φ)** = measure of information integration within a system. High phi = components interact richly within a boundary.

**Low-Phi Architecture** (Disintegrated):
```
Tasks in Asana
Metrics in Shopify dashboard
Decisions in Slack
Strategy in Google Docs
Timeline in Gantt chart tool
→ Information scattered across 5+ systems
→ Context switches fragment attention
→ AI can't navigate across boundaries
→ Low integration
```

**High-Phi Architecture** (Integrated):
```
/passets/icl-1_soft-launch/week-6/
  ├── tasks.md (tasks + decisions + reflections + test results)
  ├── status.md (completion state + blockers + health)
  └── [links to] /dashboards/weekly-kpi-snapshot.md (metrics)
  └── [links to] /reference/m13-guide.md (strategy context)
→ All information within navigable boundary
→ Context preserved
→ AI can help effectively
→ High integration
```

**Operationalization Rules**:
- ✅ Minimize number of "places" (prefer fewer, richer documents)
- ✅ Maximize information density within each boundary
- ✅ Explicit links between documents (create information paths)
- ✅ Prefer markdown files in Git over external SaaS tools (keeps everything in one context)
- ✅ When external tools necessary (Shopify, Meta), auto-sync data into `/metrics/` folder
- ❌ Never: Scatter related information across disconnected systems
- ❌ Never: "Check 5 different places to get the full picture"

---

## AI Context Window Optimization

**Core Insight**: For AI-augmented systems, a context window IS a document surface.

**Disintegrated Breaks AI**:
```
Operator: "Claude, what should I work on today?"
Claude: "I don't have access to your Asana, Shopify dashboard, or Slack.
Can you paste the information here?"
→ Friction, context lost, AI can't help
```

**Integrated Empowers AI**:
```
Operator: "Claude, what should I work on today?"
Claude: [reads week-6/tasks.md + status.md + weekly-kpi-snapshot.md]
"You have 3 tasks in progress:
1. IMP-M13-005 (Launch first ad campaign) - blocked on creative approval
2. IMP-M24-003 (Finalize 3PL contract) - waiting for signature
3. IMP-M9-008 (Set up abandoned cart flow) - ready to start

Your blocker on #1 just cleared (creative approved per task notes from 2 hours ago).
I recommend: Start the ad campaign launch now (highest priority, unlocks validation).
Then work on abandoned cart flow while waiting for 3PL signature.

Current metrics: 67/100 orders toward Week 8 milestone. ROAS holding at 2.8x.
You're on track."
→ AI has full context, can prioritize, can guide
```

**Operationalization Rules for AI-Friendly Documents**:
- ✅ Use markdown (plain text, easy for AI to parse)
- ✅ Consistent formatting (task template, status template, decision log template)
- ✅ Explicit state tracking (checkboxes, timestamps, status fields)
- ✅ Rich inline context (don't assume AI remembers previous conversations)
- ✅ Self-contained files (each document has enough context to be understood independently)
- ✅ Clear semantic structure (headers, sections, lists)
- ❌ Never: Rely on AI remembering context from previous sessions
- ❌ Never: Assume AI can access external systems
- ❌ Never: Use formats AI can't parse (complex Excel macros, proprietary tools)

---

## Integration Audit Checklist

Use this checklist to evaluate if a document/system follows integration principles:

### 1. Embed Action
- [ ] Can I complete this task without leaving the document?
- [ ] Are decision interfaces inline (checklists, fields, prompts)?
- [ ] Is there a record of what happened, not just what should happen?

### 2. Self-Awareness
- [ ] Can I tell if this task/week/phase is complete by reading the document?
- [ ] Are completion states explicit (%, checkboxes, health indicators)?
- [ ] Is progress contextualized (where am I in the larger arc)?

### 3. Adjacent Reflection
- [ ] Are there prompts that encourage thinking about outputs?
- [ ] Is there space to record hypothesis → result → learning?
- [ ] Do completed tasks have reflection entries?

### 4. Accumulation
- [ ] Does this system leave traces (answers, decisions, timestamps)?
- [ ] Can I reconstruct "why we made this choice" from the record?
- [ ] Are learnings captured for future reference?

### 5. Structured Departures
- [ ] When I reference external docs, is there context for why?
- [ ] Are there re-entry points (how do I return)?
- [ ] Are departures necessary or could info be embedded?

### 6. Isomorphic Structure
- [ ] Does the document structure match how work actually happens?
- [ ] Does granularity match operational cadence?
- [ ] Do navigation patterns match mental models?

### High-Phi Check
- [ ] Is all related information within a navigable boundary?
- [ ] Can AI access everything needed to help with this task?
- [ ] Are context switches minimized?

**Scoring**:
- 15-18 checks: Excellent integration (high phi)
- 10-14 checks: Good integration (some improvement possible)
- 5-9 checks: Fragmented (redesign recommended)
- 0-4 checks: Disintegrated (rebuild from scratch)

---

## Application to IonWave Implementation Passet

Our `/passets/` folder structure is designed with these principles:

✅ **Embed Action**: Task files contain checklists, test results, API key references
✅ **Self-Awareness**: Every week/month has status.md with completion state
✅ **Adjacent Reflection**: Standard reflection prompts in task template
✅ **Accumulation**: Decision log, task notes, weekly summaries create thinking record
✅ **Structured Departures**: `/reference/` bridge documents for Imagination Passet lookups
✅ **Isomorphic Structure**: Time-clustered (ICL-0 through ICL-6) matches execution phases

**Result**: High-phi information architecture where Claude can effectively guide Operator through execution.

---

## Version History

**v1.0.0 (2026-02-11)**:
- Initial extraction of integration principles from Danilo's essay
- Operationalized all 6 principles with rules and examples
- Added AI context window optimization section
- Created integration audit checklist
- Applied principles to IonWave Implementation Passet architecture
