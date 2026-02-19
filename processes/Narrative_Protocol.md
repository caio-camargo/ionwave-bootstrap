# Narrative Protocol

**Version**: 1.0.0
**Type**: Process Protocol
**Author**: Caio, Claude (collaborative)
**Date Created**: 2026-02-19
**Last Updated**: 2026-02-19
**AI Model**: claude-sonnet-4-5-20250929
**Purpose**: Defines what a Narrative is, when to write one, and how to produce one that surfaces real issues
**Status**: Active
**Trigger**: New venture rollout, major phase transition, operational plan requiring stress-testing, onboarding a new team member
**Owner Role**: GM, Operator, or Claude session producing planning deliverables
**Related Files**: `standards/Deliverable_Structure_Standards.md`, `processes/TUP_Workshop_Protocol.md`, `standards/Document_Metadata_Standards.md`

---

## 1. Overview

### What Is a Narrative?

A narrative is a plain-prose telling of what is going to happen: who does what, when, in what order, and what they hand off to whom. It reads like a story of execution — chronological, concrete, and honest about gaps.

### Why Narratives Exist

Timelines show boxes on a Gantt chart. Task lists show checklist items. Spreadsheets show cells. None of these force you to confront the full picture in sequence — they let you process items in isolation and move on.

A narrative can't hide behind cells and columns. When you write "Caio hires Elaine, and Elaine sets up the Drive folders," you're forced to answer: How does Caio find Elaine? What does Elaine need to know? How long does the Drive setup take? What happens if Elaine can't start until Week 2?

The act of writing prose — of telling the story from beginning to end — surfaces ambiguities, dependency gaps, unnamed actors, financial holes, and sequencing problems that remain invisible in structured formats. This is the narrative's primary value: **it is a stress test disguised as a document.**

### How a Narrative Complements Other Planning Docs

| Planning Doc | What It Shows | What It Hides |
|---|---|---|
| **Timeline / Gantt** | Duration, parallelism, milestones | Who does the work, what "done" means, handoff mechanics |
| **Task List / Checklist** | Individual items to complete | Sequencing, dependencies, the story of how items connect |
| **Financial Model** | Numbers, scenarios, thresholds | Who makes the decisions, when triggers fire, what happens operationally |
| **Role Roster** | Who exists, what they own | When they enter, how they're onboarded, what they actually do day-to-day |
| **Narrative** | The full sequence of execution — actors, actions, handoffs, gaps | Precise durations, quantified metrics (those stay in the timeline/model) |

A narrative does not replace any of these. It ties them together into a coherent story and reveals what falls through the cracks between them.

---

## 2. When to Write a Narrative

Write a narrative when:

- **New venture rollout** — A Trade is moving from imagination to implementation and someone needs to understand the full arc of what happens
- **Major phase transition** — Shifting from one operating mode to another (e.g., validation → scaling, imagination passet → implementation passet)
- **Operational plan stress-test** — You have timelines, task lists, and role rosters but haven't checked whether they actually fit together as a coherent sequence
- **Onboarding** — A new team member (human or Claude session) needs to understand not just what exists, but how things will unfold
- **Reconciliation** — Two or more planning sources cover similar ground and need to be unified into a single coherent story

Do NOT write a narrative when:

- A checklist or task list is sufficient (small, scoped, no sequencing complexity)
- The work is already underway and well-understood by all actors (narrative adds value before execution, not during)
- You're trying to avoid doing the actual planning work (a narrative requires inputs — if you don't have timelines, role rosters, or financial models yet, create those first)

---

## 3. Inputs

Before starting, gather:

| Input | Where to Find It | Why You Need It |
|---|---|---|
| **Existing TUPs / knowledge artifacts** | `data/manifest.json`, `data/{tup_id}/` | Domain knowledge the narrative draws from |
| **Timelines / execution plans** | TUP-specific planning docs, `ops_model_v10_dump/` | Week-by-week structure to narrate against |
| **Role definitions** | Role rosters, org charts, ops model tabs | Cast of characters — who does what |
| **Financial models** | `data/m3/`, `IonWave/Financial_Model_Revenue_Validation.md` | Resource constraints, burn rate, runway |
| **Dependency maps** | `processes/Dependency_Map.md`, `data/manifest.json` dependency_chains | What blocks what, critical path |
| **Prior narratives** | `ops_model_v10_dump/04_launch_narrative.json`, external docs | Existing vision to reconcile against |
| **Hypotheses** | `data/hypotheses/registry.json` | Assumptions the narrative depends on — flag uncertainty |
| **Open questions** | `tracking/Open_Questions.md` | Known unknowns that the narrative must acknowledge |

If you're missing critical inputs (no role roster, no financial model), **stop and note the gap**. A narrative written without knowing who does the work or how it's funded is fiction, not planning.

---

## 4. Protocol Phases

### Phase 1: LOAD

**Action:** Read all input documents. Build a mental model of the current state — what exists, what's planned, what's missing.

**Checklist:**
- [ ] Read the relevant TUP data and planning docs
- [ ] Identify the time horizon (how far into the future does this narrative go?)
- [ ] Identify the starting state (where are we right now?)
- [ ] Identify the end state (what does "done" look like?)
- [ ] Note any prior narratives that cover similar ground (these must be reconciled, not ignored)

**Output:** A clear understanding of start state, end state, time horizon, and available inputs. A list of prior narratives to reconcile against.

---

### Phase 2: CAST

**Action:** List every actor who appears in the narrative. An actor is anyone (or any system) that takes action, makes a decision, or produces output.

For each actor, define:

| Actor | Role | When They Enter | What They Own | How They Exit |
|---|---|---|---|---|
| *Name or role title* | *What they do* | *Week/phase they appear* | *Specific deliverables or responsibilities* | *How/when they leave or hand off* |

**The rule:** If someone needs to do something in the narrative and you can't name who, that's a gap. Write "**[UNNAMED — needs: description of required capability]**" and keep going. The pressure-test phase will catch it.

**Output:** Cast of Characters table. Gaps flagged with [UNNAMED] markers.

---

### Phase 3: SEQUENCE

**Action:** Write the narrative. Chronological prose, divided into named phases or stages.

**Writing rules:**

1. **Use active voice with named actors.** Not "the store gets set up" but "Caio sets up the Shopify store using the M9 e-commerce setup SOP."

2. **Anchor to time.** Every phase should be tied to a week, date range, or clear sequencing marker ("after X is complete"). The reader should always know where they are in time.

3. **Name what "done" looks like.** For each beat, what's the output? How do you know this step is finished? "Caio sets up the store" is incomplete. "Caio sets up the Shopify store — product pages live, payment processing connected, test order placed successfully" is a narrative.

4. **Show handoffs explicitly.** When one actor's work feeds into another's, say so: "Caio delivers the brand book to the ad creative team. They use it as the constraint document for all visual assets."

5. **Use evocative phase names.** Follow Danilo's pattern: THE SEED, THE LIBRARIAN, THE CONDUCTOR. Name phases after what's actually happening, not generic labels. "THE FACTORY" beats "Phase 3: Production." The name should tell you what the phase is about before you read the detail.

6. **Don't over-explain what's in other documents.** The narrative tells the story of execution. It references the financial model ("revenue target: $X by Week 12 — see financial model for scenarios") but doesn't reproduce it. It references the task list ("full checklist in M35 execution planning") but doesn't duplicate it.

7. **Write at analysis tempo, not scanning tempo.** Every sentence should survive the question: "Could someone actually do this?" If the answer is "only if they also know X, Y, Z that isn't written here," then write X, Y, Z or flag the gap.

**Output:** Full narrative draft, divided into named phases, with all actors named and handoffs explicit.

---

### Phase 4: PRESSURE-TEST

**Action:** Read the narrative back, specifically looking for problems. This is the phase where the narrative earns its value.

**Scan for:**

| Issue Type | What to Look For | Example |
|---|---|---|
| **Unnamed actor** | "Someone needs to..." or passive voice hiding responsibility | "The ads get reviewed" — by whom? |
| **Undefined handoff** | Actor A finishes, Actor B starts, but no connection between them | Caio builds the store, ads go live — who connects them? |
| **Unresolved dependency** | Step N requires output from Step M, but Step M isn't finished yet or isn't in the narrative | "Launch ads" but creative hasn't been produced yet |
| **Financial gap** | Something costs money but no one has said where the money comes from | "Hire a VA in Week 4" — from what budget? |
| **Timing conflict** | Two things need the same person at the same time, or the timeline is physically impossible | Caio doing supplier negotiation AND store setup AND brand book in the same week |
| **Single point of failure** | One person/system, if unavailable, stops everything | Only one person knows how to run the ad platform |
| **Assumption hiding as fact** | The narrative states something as certain that is actually a hypothesis | "Revenue starts Week 6" — based on what validation? |
| **Missing "done" criteria** | A step ends without clarity on what completion looks like | "Set up analytics" — which metrics? Tracking what? |

**Log every issue found.** Use this format:

```
ISSUE [N]: [Type] — [Description]
Location: [Phase/paragraph where found]
Severity: [Blocker / Risk / Note]
Proposed resolution: [Your best idea, or "needs discussion"]
```

**Output:** Pressure-test log with all issues categorized and severity-rated.

---

### Phase 5: RECONCILE

**Action:** Resolve the issues from Phase 4. For each issue:

1. **If resolvable:** Update the narrative directly. Add the missing actor, clarify the handoff, fix the timing.
2. **If not resolvable without more information:** Move to the Open Questions section of the narrative. Be specific about what's needed: "Open question: Who manages the ad account during Weeks 3-6? Requires a named person with Meta Ads experience and $X/week budget authority."
3. **If it contradicts a source document:** Flag the contradiction. Either the narrative is wrong, the source document is wrong, or they're describing different scenarios. Resolve or escalate.

**Also in this phase:** Cross-reference the narrative against source planning docs.
- Does the timeline in the narrative match the Gantt/timeline doc?
- Does the financial narrative match the financial model?
- Are the roles consistent with the role roster?
- Are the dependencies consistent with the dependency map?

Any inconsistency is either a correction to make or an open question to flag.

**Output:** Updated narrative with issues resolved. Open Questions section populated. Contradictions with source docs resolved or flagged.

---

### Phase 6: REGISTER

**Action:** Finalize the narrative as a deliverable and register it in the system.

**Checklist:**
- [ ] Add standard metadata header (per `standards/Document_Metadata_Standards.md`)
- [ ] File in the appropriate location (typically `data/{tup_id}/` or `IonWave/`)
- [ ] Update `data/manifest.json` if this is a new TUP-level artifact
- [ ] Update `DOCUMENTATION_INDEX.md` if applicable
- [ ] Log in `SESSION_LOG.md`
- [ ] If the narrative surfaced hypothesis-level issues, update `data/hypotheses/` as needed

**Output:** Registered narrative document, indexes updated, session logged.

---

## 5. Narrative Structure Template

The output of this protocol is a markdown document with this structure:

```markdown
# [Narrative Title] — [Venture/Project Name]

**Version**: 1.0.0
**Author**: [Name]
**Date Created**: [Date]
**Last Updated**: [Date]
**AI Model**: [if AI-assisted]
**Purpose**: [What this narrative covers]
**Status**: [Draft | Active | Superseded]
**Time Horizon**: [e.g., "Week 0 through Week 12"]
**Source Documents**: [List of planning docs this draws from]

---

## Preamble

[One paragraph: What this narrative covers, what state the venture/project is in
right now, what it draws from, and what it's for. The reader should know after
this paragraph whether this narrative is relevant to them.]

---

## Cast of Characters

| Actor | Role | Enters | Owns | Exits |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

---

## The Narrative

### [EVOCATIVE PHASE NAME] ([Time Anchor])

[Prose describing what happens in this phase. Named actors, explicit actions,
clear handoffs, defined "done" criteria.]

### [NEXT PHASE NAME] ([Time Anchor])

[Continue chronologically through all phases...]

---

## Open Questions

[Issues surfaced during writing that remain unresolved. Each one specific
enough that someone could act on it.]

1. **[Question]** — [Context, why it matters, what's needed to resolve it]
2. ...

---

## Source Documents

| Document | Relationship to This Narrative |
|---|---|
| ... | ... |
```

---

## 6. Quality Rubric

Self-grade the narrative on 5 dimensions, 1-5 scale:

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|---|---|---|---|
| **Concreteness** | Vague actors, passive voice, no "done" criteria | Most actors named, some handoffs explicit | Every actor named, every handoff explicit, every step has "done" criteria. Someone could execute from this. |
| **Completeness** | Major phases missing, story has gaps | Covers the main arc with some gaps at edges | Full arc from current state to end state, no phase skipped |
| **Honesty** | Gaps glossed over, assumptions hidden, reads like a pitch | Some gaps flagged, some assumptions visible | Every gap flagged in Open Questions, every assumption tagged, ugly parts included |
| **Readability** | Requires deep context to understand, jargon-heavy, disorganized | Readable by someone with project familiarity | A new team member could read this cold and understand the full picture |
| **Alignment** | Contradicts source docs, timeline doesn't match, roles inconsistent | Mostly consistent with minor discrepancies noted | Fully reconciled with all source planning docs, contradictions resolved or explicitly flagged |

**Scoring:**
- **Average 4.0+**: Narrative is ready for use
- **Average 3.0-3.9**: Usable but has known gaps — flag them, iterate when inputs improve
- **Average below 3.0**: Narrative needs more work before it's useful. Identify which dimensions are dragging the score down and address them.

**Self-grade is honest or it's worthless.** A 3 with a clear upgrade path is more valuable than an inflated 5.

---

## 7. Anti-Patterns

**Don't write aspirational fiction.** A narrative describes what will actually happen given real constraints — who you actually have, what money you actually have, what time you actually have. If the plan requires three people and you have one, the narrative says so. It doesn't pretend.

**Don't use passive voice to hide responsibility.** Every time you write "the X gets done," stop and ask: by whom? If you don't know, that's a gap worth flagging — not a sentence worth leaving vague.

**Don't skip the ugly parts.** Financial gaps, role vacancies, timing risks, dependency bottlenecks — these are the most valuable parts of the narrative because they're the things that will actually derail execution. A narrative that only tells the happy path is a pitch deck, not a plan.

**Don't duplicate the timeline or financial model.** The narrative tells the story; the timeline shows the dates; the model shows the numbers. Reference them ("see financial model for scenario analysis"), don't reproduce them.

**Don't write at scanning tempo.** Every sentence should survive: "Could someone actually do this tomorrow?" If the answer is "only if they also know things not written here," then either write those things or flag the gap.

**Don't treat it as permanent.** A narrative is a snapshot of understanding at a point in time. It will need updating as execution reveals new information. Version it, don't carve it in stone.

---

## 8. Relationship to Other Documents

| Document / Protocol | Relationship |
|---|---|
| `processes/TUP_Workshop_Protocol.md` | TUP workshops produce knowledge artifacts; narratives consume them as inputs and weave them into execution stories |
| `protocols/CSP-001_Constraint_Scenario_Protocol.md` | Constraint scenarios stress-test hypotheses; narratives stress-test execution plans. A narrative may reference hypotheses and their confidence grades. |
| `standards/Deliverable_Structure_Standards.md` | Narratives are deliverables. The three-section structure (Main Content, Intelligence Gaps, Scorecard) maps to: The Narrative, Open Questions, Quality Rubric. |
| `processes/Dependency_Map.md` | Dependency maps show what blocks what; the narrative tells the story of how dependencies are resolved in sequence |
| `data/hypotheses/registry.json` | Narratives may depend on unvalidated hypotheses. Flag them: "This assumes HYP-003 (churn < 8%) holds — see registry for current confidence grade." |
| `tracking/Open_Questions.md` | Open questions surfaced during narrative writing should be cross-referenced here |

---

## 9. Worked Examples

Two existing documents serve as reference models for what narratives look like in practice:

### Example A: Danilo's Launch Narrative (`ops_model_v10_dump/04_launch_narrative.json`)

**What it does well:**
- Evocative phase names (THE SEED, THE LIBRARIAN, THE CONDUCTOR, THE MC)
- Named actors with clear roles (Danilo, Caio, Elaine, the Conductor, the MC)
- Explicit handoffs ("Caio takes the raw Trade and cleans it up... Once it's clean, Caio hires Elaine")
- Honest about the creator's role post-launch ("Danilo is not involved post-lock")
- Shows the full arc from imagination to locked passet to implementation

**What it lacks:**
- No Open Questions section (issues not flagged)
- No financial detail (who pays for what, when)
- No "done" criteria for individual phases
- Written before AI-augmented production was proven — timeline assumptions need updating (see Glossary, Imagination Sprint updated estimate)

### Example B: Three Models Implementation Guide (`Studio 3/Doc Dump/three_models_implementation_guide.md`)

**What it does well:**
- Extremely concrete about daily operations (one package per day, specific tab structure, exact tool costs)
- Honest about financial gaps ("what happens during the 3-4 month gap before revenue?")
- Includes failure protocols (what happens if validation fails at Day 91)
- Forces the reader to reconcile every sentence against their own context (system specification methodology)

**What it lacks:**
- Not structured as a chronological narrative (it's a hybrid essay/guide/spec)
- Written for a different venture (Three Models, not IonWave) — requires translation
- Partnership pathways add complexity that a pure narrative would separate out

### What a Good IonWave Narrative Would Combine

The best of both: Danilo's storytelling structure and phase naming + Three Models' operational concreteness and honesty about gaps. Anchored to the current reality (Claude as co-pilot, compressed timelines, actual team composition).

---

## Version History

**v1.0.0 (2026-02-19):**
- Initial protocol created
- Derived from analysis of Danilo's Launch Narrative and Three Models Implementation Guide
- 6-phase process: LOAD → CAST → SEQUENCE → PRESSURE-TEST → RECONCILE → REGISTER
- Quality rubric: 5 dimensions × 1-5 scale
- Template and anti-patterns included
