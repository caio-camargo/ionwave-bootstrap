# Implementation Passet System — README

**Version**: 1.0.0
**Created**: 2026-02-11
**Status**: Prototype (Week 1 built, system tested)
**Purpose**: Operational execution system for IonWave (and future Trades)

---

## What Is This?

The **Implementation Passet** is the operational cockpit for executing IonWave. It transforms the Imagination Passet (domain-organized strategic playbooks) into time-organized execution tasks.

**Two Passets Exist**:
1. **Imagination Passet** (this Bootstrap repo `/data/`) — The textbook, 41 TUPs, domain-organized
2. **Implementation Passet** (`/passets/`) — The semester schedule, time-organized, extracted from Imagination

---

## System Architecture

```
/passets/
├── icl-0_pre-launch/         (Month 1, Weeks 1-4)
│   ├── week-1/
│   │   ├── tasks.md          ← Simple task list
│   │   ├── tasks_nested.md   ← Deeply nested tasks with subtasks
│   │   ├── dependencies.json ← Dependency graph for critical path
│   │   └── status.md         ← Progress tracking, Claude query responses
│   ├── week-2/ [not yet built]
│   ├── week-3/ [not yet built]
│   ├── week-4/ [not yet built]
│   └── month-1-summary/ [not yet built]
├── icl-1_soft-launch/        (Month 2, Weeks 5-8) [not yet built]
├── icl-2_validation/         (Month 3, Weeks 9-12) [not yet built]
├── icl-3_scale/              (Months 4-6) [not yet built]
├── icl-4_optimize/           (Months 7-12) [not yet built]
├── icl-5_expand/             (Months 13-18) [not yet built]
├── icl-6_ongoing-ops/        (Repeating cadences) [not yet built]
├── reference/                (Bridge documents to Imagination Passet)
│   └── m5-formulation-guide.md  ← Example bridge document (1 page)
└── dashboards/ [not yet built]
```

---

## Current Build Status

**✅ Week 1 Complete** (Prototype):
- 10 tasks extracted from M2, M5, M6, M8, M9
- 65 subtasks with action checklists
- Dependency graph (critical path extraction)
- Status tracking file
- 1 bridge document (M5 Formulation)

**⏳ Remaining**:
- Weeks 2-72 (to be extracted from Imagination Passet)
- Bridge documents for other TUPs
- Dashboard templates
- Extraction protocol documentation

---

## How to Use This System

### For Operators

**Daily Question**: "What's next?"

**Claude Response** (example):
```
Looking at week-1/status.md...

Your next task is IMP-M2-001: File Delaware C-Corp Incorporation.
- Duration: 3 hours
- Priority: P0 (CRITICAL PATH)
- No blockers (can start immediately)
- First step: Check name availability at Delaware Division of Corporations

Once complete, this unblocks 3 tasks:
- IMP-M2-002 (Obtain EIN)
- IMP-M2-006 (Prepare Legal Docs)
- IMP-M9-001 (Shopify Setup)
```

**How Claude Knows**:
1. Read `week-1/status.md` → See all tasks Not Started
2. Read `week-1/dependencies.json` → Find tasks with `dependencies: []`
3. Sort by `priority` → IMP-M2-001 is P0
4. Present first step from `week-1/tasks_nested.md` → "Check name availability"

### For Intermediary (Oversight)

**Daily Question**: "Is Week 1 on track?"

**Claude Response** (example):
```
Reading week-1/status.md...

Week 1 Status: 🟢 Green

Progress: 3/10 tasks complete (30%)
- IMP-M2-001: ✅ Done
- IMP-M2-002: ✅ Done
- IMP-M2-003: 🔵 In Progress
- IMP-M2-004: 🟡 Blocked (waiting on lawyer - IMP-M2-006)

Critical Path: On track (entity formation progressing)
Blockers: 1 active (lawyer docs delayed by 1 day)
Risks: None

Recommendation: Follow up with lawyer on IMP-M2-006 (due yesterday).
```

### For Studio 3 / Nilo

**Quarterly Question**: "How is IonWave execution vs plan?"

**Claude Response** (example):
```
Reading all completed time-block summaries...

ICL-0 (Pre-Launch Foundation): ✅ Complete
ICL-1 (Soft Launch): 🔵 In Progress (Week 6 of 8)
ICL-2 (Validation): ⏳ Not Started

Key Metrics vs Plan:
- Launch date: On track (April 1, 2026)
- Budget: 5% under ($42K spent vs $45K planned)
- Team: Fully staffed (CoS, Media Buyer, CX Agent hired)

Risks:
- ROAS validation (Week 9-12) is gate for ICL-3 Scale
- Current ROAS: 2.6x (target: 2.5x minimum)
- Status: 🟢 Green (on track to validate)
```

---

## File Types Explained

### 1. `tasks.md` (Simple Task List)
**Purpose**: Flat list of tasks for human readability
**Format**: Markdown checklist
**Use**: Quick reference, printable task list

**Example**:
```markdown
## Week 1 Tasks

### CoS / Founder
- [ ] IMP-M2-001: File Delaware C-Corp
- [ ] IMP-M2-002: Obtain EIN
- [ ] IMP-M5-001: Lock Formulation
```

### 2. `tasks_nested.md` (Nested Task Structure)
**Purpose**: Detailed subtasks with action checklists
**Format**: Hierarchical markdown
**Use**: Execution guide, Claude navigation

**Example**:
```markdown
### IMP-M2-001: File Delaware C-Corp
**Subtasks**:
- [ ] 1.1: Check name availability
  - [ ] Search Delaware Division of Corporations
  - [ ] Primary: "IonWave, Inc."
  - [ ] Backup: "IonWave Labs, Inc."
- [ ] 1.2: Check trademark conflicts
  - [ ] Search USPTO database
```

**Why Both?**
- `tasks.md` = overview for humans
- `tasks_nested.md` = execution detail for Claude + operators

### 3. `dependencies.json` (Dependency Graph)
**Purpose**: Machine-readable dependency tracking
**Format**: JSON
**Use**: Critical path extraction, "what's next" queries

**Key Fields**:
- `dependencies`: Array of task IDs that must complete first
- `blocks`: Array of task IDs that this task gates
- `critical_path`: Boolean (is this on critical path?)
- `priority`: P0 (must), P1 (should), P2 (nice-to-have)

**Query Patterns**:
```json
{
  "what_is_next": "Find tasks where dependencies=[all completed]",
  "what_is_blocking_me": "For current task, show uncompleted dependencies",
  "critical_path": "Follow critical_path=true in order"
}
```

### 4. `status.md` (Progress Tracking)
**Purpose**: Week-level completion state
**Format**: Markdown with tables
**Use**: Daily standup, oversight, Claude queries

**Key Sections**:
- Completion Summary (X/Y tasks done)
- Task Status Table (task ID, status, blockers)
- Critical Path Progress
- What's Next (immediate actions)
- Blockers (what's stuck)
- Issues / Risks
- Week Health (🟢🟡🔴)

**Update Frequency**: Daily (operator updates as tasks complete)

### 5. `/reference/mX-guide.md` (Bridge Documents)
**Purpose**: Quick reference to Imagination Passet TUPs
**Format**: 1-page markdown summary
**Use**: "Why are we doing this?" lookups, supplier coordination

**Structure**:
- 30-second summary
- Critical numbers (for this TUP)
- Common questions
- When to reference full TUP files
- Red flags to watch for

**Example**: `m5-formulation-guide.md` summarizes 5 M5 files (~2000 lines) into 1 page

---

## Integration Principles Applied

Per `/project_specs/INTEGRATION_DESIGN_PRINCIPLES.md`:

✅ **1. Embed Action**: Subtasks have specific steps, not just goals
- Example: "File Certificate of Incorporation" → 5 sub-steps with exact URLs, field names, costs

✅ **2. Self-Awareness**: `status.md` models completion state
- Progress %, blockers, critical path progress visible at-a-glance

✅ **3. Adjacent Reflection**: Reflection prompts on each task
- "What did you learn?" "Any issues?" "Would you do it differently?"

✅ **4. Accumulation**: Notes field creates thinking record
- Decisions logged, blockers documented, learnings captured

✅ **5. Structured Departures**: Bridge documents for Imagination Passet
- Context for WHY, WHERE to go, WHAT to look for, HOW to return

✅ **6. Isomorphic Structure**: Time-clustered matches work cadence
- Week-by-week folders = how operators actually work
- Not domain-clustered (which would scatter related tasks)

**Result**: High-phi information architecture where Claude can effectively guide operators.

---

## Critical Path Extraction (How It Works)

**Algorithm**:
1. Read `dependencies.json`
2. Filter `critical_path: true`
3. Sort by dependency order (tasks with no dependencies first)
4. Follow `blocks` field to find next critical path task

**Week 1 Critical Path** (example):
```
IMP-M2-001 (File C-Corp)
    ↓
IMP-M2-002 (Obtain EIN)
    ↓
IMP-M2-006 (Prepare Legal Docs) — parallel to 002
    ↓
IMP-M2-004 (Organizational Meeting)
    ↓
IMP-M2-005 (Issue Stock & 83(b))

PARALLEL TRACK:
IMP-M5-001 (Lock Formulation) — gates Week 2 supplier work
```

**Completion Time**: 15.5 hours (entity track) + 4 hours (formulation track, parallel) = **15.5 hours critical path**

---

## Dependency Tracking (How It Works)

**Each task has**:
- `dependencies`: ["IMP-M2-001", "IMP-M2-002"] — must complete BEFORE starting this task
- `blocks`: ["IMP-M2-004", "IMP-M9-001"] — this task GATES these tasks

**Example**:
```json
{
  "id": "IMP-M2-002",
  "name": "Obtain Federal EIN",
  "dependencies": ["IMP-M2-001"],
  "blocks": ["IMP-M2-003", "IMP-M2-004", "IMP-M9-001"]
}
```

**Meaning**:
- Cannot start IMP-M2-002 until IMP-M2-001 is Done
- Completing IMP-M2-002 unblocks 3 tasks

**Claude Query**:
```
Operator: "Can I work on IMP-M9-001 (Shopify setup)?"
Claude: [checks dependencies: ["IMP-M2-001", "IMP-M2-002"]]
        [checks status.md: both tasks status=Done]
        "Yes! IMP-M9-001 is unblocked. You can start now."
```

---

## Task Nesting (How It Works)

**3-Level Hierarchy**:
- **Level 1**: Parent task (IMP-M2-001: File C-Corp)
- **Level 2**: Subtasks (1.1: Check name availability, 1.2: Check trademark)
- **Level 3**: Sub-subtasks (under 1.1: Search Delaware database, Primary: "IonWave, Inc.", Backup: "IonWave Labs")

**Why Nested?**:
- **Backend**: Full detail for execution (65 subtasks)
- **Frontend**: Claude can flatten for presentation

**Example**:
```
Operator: "What's the first step for IMP-M2-001?"
Claude: [reads tasks_nested.md, finds IMP-M2-001, extracts subtask 1.1]
        "First step: Check name availability. Go to Delaware Division of
        Corporations website. Search for 'IonWave, Inc.' If taken, try
        backups: 'IonWave Labs, Inc.' or 'IonWave Health, Inc.'"
```

**Flattening Algorithm**:
1. Find parent task by ID
2. Extract first unchecked subtask
3. If subtask has sub-subtasks, extract first unchecked one
4. Present to operator as "First step: [action]"

---

## Extraction Protocol (How Week 1 Was Built)

**7-Step Process** (per `/project_specs/PASSET_FOLDER_STRUCTURE.md`):

1. **Take verified Imagination TUP** (M2 Entity & Legal, grade B+)
2. **Read content tabs** (M2-04-Entity-Formation-Guide)
3. **Extract actions** ("File Certificate of Incorporation" from formation guide)
4. **Assign time block** (Week 1, Day 1-3 for entity formation)
5. **Assign owner role** (CoS / Founder)
6. **Identify dependencies** (EIN requires C-Corp first)
7. **Place into time-block folder** (`week-1/tasks_nested.md`)

**Mapping Patterns**:
- **Many-to-One**: M2 + M5 + M6 → "Get product made" (15 tasks across Week 1-4)
- **One-to-Many**: M5 (Formulation) → Week 1 (lock spec) + Week 2 (supplier) + Week 4 (CoA validation)

**Result**: 10 parent tasks, 65 subtasks, extracted from 5 Imagination TUPs (M2, M5, M6, M8, M9)

---

## Next Steps (To Complete System)

### Phase 1: Complete ICL-0 (Weeks 2-4)
- Extract tasks from M6 (Supply Chain), M7 (Regulatory), M8 (Brand), M9 (Ecommerce)
- Build dependency graphs for Weeks 2-4
- Create bridge documents for M6, M7, M8, M9
- Estimated: 8-10 hours

### Phase 2: Build ICL-1 through ICL-2 (Weeks 5-12)
- Extract tasks for Soft Launch (Weeks 5-8) and Validation (Weeks 9-12)
- Sources: M11 (VSL), M12 (Ad Creative), M13 (Media Buying), M15 (Landing Pages), M17 (Email), M19 (CRM), M20 (Support)
- Estimated: 12-16 hours

### Phase 3: Build ICL-3 through ICL-6 (Months 4-18)
- Extract tasks for Scale, Optimize, Expand phases
- Monthly granularity (less detail than weekly)
- Estimated: 16-20 hours

### Phase 4: Build Dashboards & OpKit ✅ COMPLETE (2026-02-12)
- ✅ Dashboard templates (`/dashboards/daily_pulse.md`)
- ✅ Data pipeline architecture (`/dashboards/data_pipeline_spec.md`)
- ✅ Control system architecture:
  - 12 controllers (`/dashboards/controller_registry.md`)
  - 12 parameter sets (`/dashboards/parameter_registry.md`)
  - 15 reactive protocols (`/dashboards/reactive_protocols.md`)
  - System overview (`/dashboards/control_system_overview.md`)
- ⏳ Extraction protocol OpKit (deferred to Phase 5)

**Total Remaining Work**: ~36-46 hours to complete Weeks 2-72 extraction

---

## Success Metrics

**System is successful if**:
1. Operator can ask "What's next?" and Claude gives actionable answer in <10 seconds
2. Critical path is always visible (no guessing "what's blocking me?")
3. Week completion status is self-evident (no ambiguity on "are we done?")
4. Learnings accumulate (reflection prompts capture why things worked/didn't)
5. Future Trades can reuse structure (just swap TUP content, keep time architecture)

**Early Indicators** (Week 1 prototype):
- ✅ Critical path extractable from dependencies.json
- ✅ "What's next?" answerable from status.md + dependencies
- ✅ Tasks have embedded action (subtasks with specific steps)
- ✅ Bridge documents enable structured departures
- ✅ Time-clustered architecture matches workflow

---

## Relationship to M35/M36/M37/M40

**Original Plan**: Workshop these as 4 separate TUPs
**New Approach**: These TUPs ARE the Implementation Passet system

- **M35 (Execution Plans)** = Task extraction + timeline choreography (this system)
- **M36 (Operational Infra)** = API integrations + dashboard protocols + **control system (COMPLETE)**
- **M37 (AI & Automation)** = Claude query patterns + automation (deferred, will emerge)
- **M40 (Navigation)** = Navigation system + bridge documents (this system)

**M36 Control System Components** (formalized 2026-02-12):
- **Controllers**: 12 monitoring mechanisms (C-001 through C-012) that execute Sense → Compare → Detect → Act → Report loop
- **Parameters**: Numeric thresholds (VI-2 through VI-4) that define green/yellow/red status
- **Reactive Protocols**: 15 standardized responses (RP-001 through RP-015) triggered when metrics exceed tolerances
- **Meta-Control**: Quarterly review process that tunes parameters, updates protocols, improves system based on logs

**Why This Is Better**:
- **Integrated** (not disintegrated across 4 separate documents)
- **Testable** (we built Week 1, can validate system works)
- **Operational** (creates REAL execution system, not just reference docs)
- **Reusable** (OpKit for extraction protocol applies to all future Trades)

---

## Version History

**v1.0.0 (2026-02-11)**:
- Initial system build
- Week 1 prototype complete (10 tasks, 65 subtasks)
- Dependency tracking system
- Status tracking template
- 1 bridge document (M5 Formulation)
- System README (this document)

**v1.1.0 (2026-02-12)**:
- M36 Control System formalized:
  - Controller registry (12 controllers)
  - Parameter registry (12 parameter sets with VI ratings)
  - Reactive protocols (15 standardized response procedures)
  - Control system overview (architecture + integration documentation)
- Daily Pulse dashboard integrated with controller outputs
- Data pipeline specification complete (API → Google Apps Script → Google Sheet)
- Meta-Control learning layer documented

---

## Related Documents

- **System Architecture**: `/project_specs/PASSET_FOLDER_STRUCTURE.md` (v2.0.0)
- **Design Principles**: `/project_specs/INTEGRATION_DESIGN_PRINCIPLES.md` (v1.0.0)
- **Claude-as-OS Vision**: `/project_specs/CLAUDE_AS_OS_SYSTEM.md` (v1.0.0)
- **Workshop Protocol**: `/processes/TUP_Workshop_Protocol.md` (TWP-001 v2.0.0)
- **Control System**:
  - `/passets/dashboards/control_system_overview.md` (architecture + integration)
  - `/passets/dashboards/controller_registry.md` (12 controllers)
  - `/passets/dashboards/parameter_registry.md` (thresholds + VI ratings)
  - `/passets/dashboards/reactive_protocols.md` (15 response procedures)
  - `/passets/dashboards/daily_pulse.md` (operator dashboard)
  - `/passets/dashboards/data_pipeline_spec.md` (API integrations)

---

**Questions? Issues? Feature Requests?**
Log in `/passets/decisions/decision_log.md` or escalate to Intermediary/Studio 3.
