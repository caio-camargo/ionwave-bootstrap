# Implementation Passet Folder Structure

**Version**: 2.0.0
**Author**: Caio, Claude
**Date Created**: 2026-02-11
**Last Updated**: 2026-02-11
**AI Model**: claude-sonnet-4-5-20250929
**Purpose**: Specification for the Implementation Passet folder structure (time × roles organization)
**Status**: Active
**Source**: `ops_model_v10_dump/08_s4_implementation_spec.json`

---

## Overview

The **Implementation Passet** is the operational cockpit for executing IonWave. It is organized by **TIME × ROLES**, not by domain.

**Two Passets Exist:**

1. **Imagination Passet** (this Bootstrap repository)
   - 103 TUPs organized by DOMAIN
   - "Here's how media buying works"
   - The textbook - locks when complete, never edited again
   - Reference for the "why" and "how"

2. **Implementation Passet** (this folder structure: `/passets/`)
   - ~80 TUPs organized by TIME
   - "Here's what everyone does in Month 2"
   - The semester schedule - updated daily while business runs
   - Extracted from Imagination Passet by CoS

**Relationship**: The Imagination Passet is the brain. The Implementation Passet is the body.

---

## Folder Structure

### 7 Time Clusters (ICL-0 through ICL-6)

```
/passets/
├── icl-0_pre-launch/          (Month 1, Weeks 1-4)
│   ├── week-1/
│   ├── week-2/
│   ├── week-3/
│   ├── week-4/
│   └── month-1-summary/
├── icl-1_soft-launch/         (Month 2, Weeks 5-8)
│   ├── week-5/
│   ├── week-6/
│   ├── week-7/
│   ├── week-8/
│   └── month-2-summary/
├── icl-2_validation/          (Month 3, Weeks 9-12)
│   ├── week-9/
│   ├── week-10/
│   ├── week-11/
│   ├── week-12/
│   └── month-3-summary/
├── icl-3_scale/               (Months 4-6, Weeks 13-24)
│   ├── month-4/
│   ├── month-5/
│   ├── month-6/
│   └── q2-summary/
├── icl-4_optimize/            (Months 7-12, Weeks 25-48)
│   ├── month-7/
│   ├── month-8/
│   ├── month-9/
│   ├── month-10/
│   ├── month-11/
│   ├── month-12/
│   └── h2-summary/
├── icl-5_expand/              (Months 13-18, Weeks 49-72)
│   ├── month-13/
│   ├── month-14/
│   ├── month-15/
│   ├── month-16/
│   ├── month-17/
│   ├── month-18/
│   └── q6-summary/
├── icl-6_ongoing-ops/         (Repeating cadences)
│   ├── weekly-cadences/
│   ├── monthly-cadences/
│   ├── quarterly-cadences/
│   └── annual-cadences/
├── reference/                 (Links back to Imagination Passet TUPs)
└── dashboards/                (Metrics, status tracking, KPIs)
```

**Total**: ~47 time-block folders + 2 utility folders = 49 top-level folders

---

## Time Cluster Specifications

### ICL-0: Pre-Launch Foundation (Month 1)
**Time Block**: Weeks 1-4
**What Happens**: Entity formed. Bank open. Product formulation locked. First inventory ordered. Site live. Brand finalized. First hires made (media buyer, email, CX).
**Key Roles Active**:
- CoS (runs everything)
- Formulator (product)
- Lawyer (entity)
- Designer (brand)

**Folder Contents**:
- `week-1/` through `week-4/` - Weekly task lists
- `month-1-summary/` - Rollup status and learnings

### ICL-1: Soft Launch (Month 2)
**Time Block**: Weeks 5-8
**What Happens**: First ads running. Landing pages live. Email flows active. Fulfillment tested with soft launch orders. Analytics tracking confirmed. First 50-100 orders.
**Key Roles Active**:
- CoS
- Media buyer
- Email/lifecycle
- Fulfillment ops
- CX agent

### ICL-2: Validation (Month 3)
**Time Block**: Weeks 9-12
**What Happens**: ROAS validated or killed. Subscription flow live. Retention metrics baseline established. Creative testing cadence running. Support processes stable.
**Key Roles Active**:
- CoS
- Media buyer
- Email/lifecycle
- Creative
- Support

### ICL-3: Scale (Months 4-6)
**Time Block**: Weeks 13-24
**What Happens**: Scale ad spend from $500/day to $2-5K/day. Influencer partnerships live. Content/SEO started. Referral program launched. Second product consideration.
**Key Roles Active**:
- CoS
- Media buyer
- Influencer mgr
- Content
- Growth

### ICL-4: Optimize (Months 7-12)
**Time Block**: Weeks 25-48
**What Happens**: Profitability targets. LTV:CAC optimization. Retention improvements. Team scaling. Operational efficiency. Market expansion consideration.
**Key Roles Active**:
- CoS
- Full team
- CFO (fractional)
- HR/hiring

### ICL-5: Expand (Months 13-18)
**Time Block**: Weeks 49-72
**What Happens**: New channels. New products. New markets. Series A prep if applicable. Team maturity. Process documentation.
**Key Roles Active**:
- CoS
- Full team
- Nilo (strategic)

### ICL-6: Ongoing Ops (Repeating)
**Time Block**: Recurring (never ends)
**What Happens**: Recurring tasks that never end. Weekly creative reviews. Monthly P&L review. Quarterly strategy. Annual planning.
**Key Roles Active**:
- CoS
- Full team

---

## Task File Template

Each time-block folder contains task files organized by role. Every task has:

| Column | Content | Example |
|--------|---------|---------|
| **Task ID** | Unique identifier | `IMP-M2-001` |
| **Task** | What needs to happen | "File Delaware C-Corp incorporation" |
| **Source TUP** | Which Imagination TUP this comes from | "M2: Entity & Legal" |
| **Source Tab** | Specific tab reference | "M2-Formation" |
| **Owner Role** | Which role is responsible | "CoS" |
| **Owner Name** | Actual person (filled when hired) | "[TBD]" or "Sarah Chen" |
| **Due Date** | When it must be done | "2026-03-15" |
| **Dependencies** | What must be done before this | "IMP-M2-000 (lawyer retained)" |
| **Status** | Progress tracking | "Not Started / In Progress / Blocked / Done" |
| **Notes** | Context, blockers, updates | "Lawyer reviewing draft, expects 48hrs" |
| **Verified** | Does completed task match Imagination spec? | "☐" or "☑" |

### Example Task File: `week-1/tasks.md`

```markdown
# Week 1 Tasks (Feb 3-9, 2026)

## CoS / GM

- [ ] **IMP-M2-001** - File Delaware C-Corp incorporation
  - Source: M2: Entity & Legal (M2-Formation tab)
  - Owner: CoS
  - Due: 2026-02-08
  - Dependencies: IMP-M2-000 (lawyer retained)
  - Status: In Progress
  - Notes: Lawyer reviewing draft, expects 48hrs
  - Verified: ☐

- [ ] **IMP-M9-001** - Set up Shopify store (basic structure)
  - Source: M9: Ecommerce (M9-Platform Setup tab)
  - Owner: CoS
  - Due: 2026-02-09
  - Dependencies: None
  - Status: Not Started
  - Notes: Using Shopify Plus template
  - Verified: ☐

## Formulator

- [ ] **IMP-M5-001** - Finalize electrolyte formulation
  - Source: M5: Formulation (M5-Core Formula tab)
  - Owner: Formulator (Dr. Martinez)
  - Due: 2026-02-07
  - Dependencies: None
  - Status: Done
  - Notes: Formula locked at Na 1000mg, K 200mg, Mg 60mg
  - Verified: ☑

## Designer

- [ ] **IMP-M8-001** - Deliver final brand guidelines
  - Source: M8: Brand Identity (M8-Visual System tab)
  - Owner: Designer (Studio X)
  - Due: 2026-02-08
  - Dependencies: None
  - Status: In Progress
  - Notes: Logo approved, finalizing color palette
  - Verified: ☐
```

---

## Extraction Process (How to Build the Implementation Passet)

The Implementation Passet is **EXTRACTED** from the Imagination Passet, not invented fresh.

### 7-Step Extraction Protocol:

1. **Take each verified Imagination TUP** (V-tab grade A or B)
2. **Read the content tabs and P-tab** (Project Plan)
3. **Extract every action implied** by the model (e.g., "set up Meta account" from M13)
4. **Assign a time block** (when does this action happen relative to launch?)
5. **Assign an owner role** (who does this?)
6. **Identify dependencies** (what must be done first?)
7. **Place into the correct time-block folder**

### Mapping Patterns:

**Many-to-One (Multiple TUPs → Fewer Tasks)**:
- M5 (Formulation) + M6 (Supply Chain) + M7 (Regulatory) → "Get product made" (a sequence of ~15 tasks across Months 1-2)

**One-to-Many (One TUP → Multiple Time Blocks)**:
- M13 (Media Buying) →
  - Month 1: Set up accounts
  - Month 2: Launch first campaigns
  - Month 3: Validate ROAS
  - Months 4-6: Scale spend
  - Ongoing: Weekly creative refresh

---

## Who Builds It

**Primary Builder**: The CoS (Chief of Staff) builds the Implementation Passet as their first act.

**Supporting Roles**:
- **Librarian**: Helps with file management
- **Claude**: Helps with extraction (reading TUPs and generating task lists)

**When**: After the Imagination Passet is graded and approaching lock (Week 10-12 of imagination production cycle).

---

## Reference Folder

The `/reference/` folder contains:
- Links back to source Imagination Passet TUPs
- Mapping documents (which tasks came from which TUPs)
- "Why" explanations (when tasks need context from the Imagination Passet)

**Example**: `reference/m13-media-buying-tasks.md` lists all tasks extracted from M13 with links to the original tabs.

---

## Dashboards Folder

The `/dashboards/` folder contains:
- Weekly KPI snapshots
- Monthly rollup reports
- Quarterly reviews
- Real-time metric tracking (ROAS, CAC, LTV, retention curves)
- Team capacity/velocity tracking

**Purpose**: At-a-glance status for CoS and oversight roles.

---

## Navigation Patterns

### "What should I work on today?"
→ Open current week folder (e.g., `icl-1_soft-launch/week-6/tasks.md`)
→ Filter by your role
→ Work through tasks marked "Not Started" or "In Progress"

### "Why are we doing this task?"
→ Check the task's Source TUP field (e.g., "M13: Media Buying")
→ Go to `/reference/m13-media-buying-tasks.md` for context
→ Consult the Imagination Passet (this Bootstrap repo) for full "why" and "how"

### "What's coming next month?"
→ Open next time cluster folder (e.g., `icl-2_validation/month-3-summary/`)
→ Review upcoming tasks and dependencies

### "Are we on track?"
→ Open `/dashboards/weekly-kpi-snapshot.md`
→ Check status vs plan

---

## File Naming Conventions

- **Time blocks**: `week-N`, `month-N`, `qN-summary`, `hN-summary`
- **Task files**: `tasks.md` (primary), `tasks_ROLE.md` (if role-specific files needed)
- **Status files**: `status_YYYY_MM_DD.md` (daily/weekly snapshots)
- **Summaries**: `summary.md` (rollup at end of time block)

---

## Access Patterns (for Claude-as-OS system)

### Operator Daily Interface:
- **Primary file**: Current week `tasks.md`
- **Secondary**: `/dashboards/weekly-kpi-snapshot.md`
- **Tertiary**: Next week folder (look-ahead)

### Intermediary Oversight:
- **Primary**: Current week status + blockers
- **Secondary**: Monthly summary files
- **Tertiary**: `/dashboards/` for metrics review

### Studio 3 / Nilo:
- **Primary**: Quarterly summaries
- **Secondary**: `/dashboards/` for high-level KPIs
- **Tertiary**: `/reference/` to verify execution matches Imagination intent

---

## Lifecycle States

### 1. SEED (Week 0)
- Imagination Passet exists (this Bootstrap repo)
- Implementation Passet does not exist yet

### 2. PRODUCTION (Weeks 1-8)
- Imagination Passet growing (TUPs being drafted, refined, reviewed)
- Implementation Passet does not exist yet

### 3. GRADING (Weeks 6-10)
- Imagination Passet maturing (V-tabs being filled, quality converging)
- Implementation Passet does not exist yet (but CoS is reading Imagination Passet)

### 4. LOCK (Week 10-12)
- Imagination Passet **LOCKED** (never edited again, published as textbook)
- Implementation Passet **BORN** (CoS extracts tasks from locked Imagination Passet into time-block folders)

### 5. IMPLEMENTATION (Months 3-18)
- Imagination Passet = **REFERENCE** (people consult for "why" and "how", nobody edits)
- Implementation Passet = **ALIVE** (updated daily, tasks checked off, new tasks added, the living document)

### 6. REVIEW (Quarterly)
- Imagination Passet = **REFERENCE** (compared against actual results)
- Implementation Passet = **REVIEW NOTES ADDED** (learnings captured, feeds next Trade)

### 7. NEXT TRADE (when ready)
- Imagination Passet = **ARCHIVED** (this Trade's Imagination Passet is archived, new Trade's Imagination Passet begins)
- Implementation Passet = **CONTINUES** (this Trade's business still operating, new Trade starts fresh)

---

## Version History

**v2.0.0 (2026-02-11)**:
- **BREAKING CHANGE**: Completely redesigned to follow Implementation Passet architecture from ops_model_v10
- Changed from domain-organized structure (product, brand, creative, etc.) to time-organized structure (ICL-0 through ICL-6)
- Added 7 time clusters with 47 time-block folders
- Added task file template specification with 11 required fields
- Added extraction process protocol (7 steps)
- Added lifecycle states (SEED → REVIEW → NEXT TRADE)
- Added navigation patterns for Operator, Intermediary, Studio 3
- Clarified relationship between Imagination Passet (textbook) and Implementation Passet (semester schedule)

**v1.0.0 (2026-02-11)**:
- Initial version (DEPRECATED - incorrect architecture)
- Used domain-organized structure instead of time-organized
- Did not follow ops_model_v10 Implementation Passet specification
