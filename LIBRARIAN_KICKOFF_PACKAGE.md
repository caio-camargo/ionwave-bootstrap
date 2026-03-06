# Librarian Kickoff Package

> **You were just hired. This is everything you need to execute Day 1.**
>
> Read this document top to bottom. By the end, you will know exactly what your job is, what you maintain, how you distribute, when you escalate, and what "done" looks like.

---

## 0. Role Parameters

| Parameter | Value |
|-----------|-------|
| **Role Title** | Librarian |
| **Canonical Name** | Librarian |
| **Aliases** | Information Architect, Registrar, Trade Custodian |
| **Role Type** | Persistent (full production cycle) |
| **Delegation Depth** | D2 (executes from documented process) |
| **Reports To** | Founder (Nilo/Danilo) |
| **Interfaces With** | Conductor, MC, all Flash Team members |
| **Duration** | Full cycle (12+ weeks) |
| **Time Commitment** | 2-3 hrs/day (grows as team scales, shrinks as system stabilizes) |
| **Compensation** | $100-200/week + 0.5-2% equity |

> **Modularity note:** This package is parameterized. The role-invariant framework (Sections 6-9) is shared across all Studio Phase roles. The role-specific parameters (Sections 1-5) are what change if this scope is reassigned.

---

## 1. Your Mission

You are the custodian of the Trade — the 900+ tab operating system that contains the complete imagination for IonWave. Your job is pure custody: maintain, distribute, update, track. No judgment. No strategy. No teaching. You file and distribute.

**Your win condition:** Every person who touches the Trade can find what they need instantly, and the master file always reflects the current state of all work.

**The chain:** Founder + Claude produce the Trade → You learn it → You distribute it → Everyone else executes from it.

You are the bridge between the creators (Nilo + Claude) and the flash team that will build from it.

### What you own

- Maintain the master Trade (read-only reference copy)
- Set up and maintain the Google Drive structure
- Extract TUP slices into per-person working folders
- Update the master Trade when work returns graded/revised
- Track the status of every TUP across the system
- Answer "where is X?" instantly for anyone
- Route cross-cluster dependencies between flash team members
- Prepare INSTRUCTIONS.md for every new hire's working folder

### What you don't touch

- Content decisions (what goes in a TUP — that's the PM co-founder)
- Grading or review (that's the Expert Reviewer)
- Hiring or sourcing (that's the Conductor)
- Conversations or content production (that's the MC)
- Strategy, thesis, or brand decisions (that's Nilo)

---

## 2. Week 1 Onboarding — Learning the Trade

You don't read 900+ tabs. You read three:

| Tab | What It Tells You |
|-----|-------------------|
| **Directory** | The full list of all tabs, organized by cluster |
| **Taxonomy** | The 3-level structure: Business Clusters (BCL), Content Layers (CL), Strategic Layers (SL) |
| **Role Rosters** | Who owns what — which roles are assigned to which clusters |

That's enough to know the architecture: 3 levels, 18 clusters, 103 TUPs, who owns what.

### Week 1 Tasks

| # | Task | Done When |
|---|------|-----------|
| 1 | Read Directory, Taxonomy, Role Rosters | You can describe the 3-level structure from memory |
| 2 | Set up Google Drive: master folder (read-only) | Folder exists, Trade uploaded, permissions set |
| 3 | Set up Google Drive: empty working folders (one per role slot) | Folder structure matches the role registry |
| 4 | Confirm with Nilo: master Trade is current version | Nilo confirms "this is the file" |
| 5 | Create TUP Status Tracker (see Section 4) | Tracker exists with all 103 TUPs listed |
| 6 | Hire the Conductor (coordinate with Nilo) | Conductor candidate identified or posted |

---

## 3. Ongoing Operations — The Distribution Cycle

Every time a new person flashes into the system, you execute this cycle:

### Flash Team Member Onboarding (Your Part)

```
Conductor sources person → MC has entrance conversation →
  YOU PREPARE THEIR FOLDER → They sprint → They submit →
    YOU UPDATE THE MASTER → MC has exit conversation → They dissolve
```

### Folder Preparation Checklist

When a new flash team member is confirmed (post-MC conversation):

- [ ] **Create their working folder** in Google Drive (named: `[Role] — [Name] — [Cluster]`)
- [ ] **Extract their TUP tabs** from the master Trade into the folder
  - P-tabs (project plans) for their assigned TUPs
  - C-tabs (contracts/compliance) relevant to their scope
  - IP-tabs (intellectual property) they'll produce
  - V-tabs (verification criteria) so they know what "done" looks like
- [ ] **Write INSTRUCTIONS.md** for their folder:
  - What they're producing
  - What "done" looks like (from V-tab criteria)
  - Who they hand off to (you, for master update)
  - How to reach you (email/Slack for "where is X?" questions)
  - Link to full Trade (read-only) for context
- [ ] **Grant read-only access** to the full Trade
- [ ] **Grant read-write access** to their working folder only
- [ ] **Add a SUBMIT subfolder** in their working folder (where they drop finished work)
- [ ] **Notify the person**: "Your folder is ready. Start with INSTRUCTIONS.md."

### Work Return Cycle

When a flash team member submits work:

1. **Check SUBMIT folder** — confirm deliverables match what was requested
2. **Update master Trade** — merge their work into the canonical version
3. **Update TUP Status Tracker** — move TUP from "in production" to "in review" (or "verified" if expert already graded)
4. **Notify Expert Reviewer** (if assigned) — "TUPs X, Y, Z are ready for review"
5. **Notify Conductor** — "Sprint complete, person is dissolving"

### Cross-Cluster Dependency Routing

If BCL-3 needs output from BCL-1:

1. Check if the BCL-1 output exists in the master
2. If yes: extract and place in BCL-3 person's working folder
3. If no: flag to Conductor — "BCL-3 is blocked on BCL-1 output, ETA needed"
4. Track the dependency in the TUP Status Tracker

---

## 4. TUP Status Tracker

Maintain this for all 103 TUPs. Update daily.

| TUP ID | Cluster | TUP Name | Status | Assigned To | Sprint Start | Sprint End | Expert Reviewer | Expert Grade | Notes |
|--------|---------|----------|--------|-------------|-------------|-----------|-----------------|-------------|-------|
| M5 | BCL-1 | | ___ | ___ | ___ | ___ | ___ | ___ | |
| M6 | BCL-1 | | ___ | ___ | ___ | ___ | ___ | ___ | |

### Status definitions

| Status | Meaning |
|--------|---------|
| **Not started** | TUP exists in master, no one assigned yet |
| **Folder prepared** | Working folder created, waiting for person to start |
| **In production** | Flash team member is actively working |
| **Submitted** | Work dropped in SUBMIT folder, pending your merge |
| **In review** | Expert reviewer has the TUP |
| **Revision needed** | Expert gave C or D grade, PM flashing back in |
| **Verified** | Expert gave A or B grade |
| **Locked** | V-tab confirmed, TUP is final — no more edits |

### Daily status summary (Slack DM to Nilo)

> **Day [X] Librarian Update:**
> - TUPs: [X] locked / [X] verified / [X] in production / [X] not started
> - Today: [What you did — folders prepared, masters updated, dependencies routed]
> - Blockers: [Anything you need, or "None"]

---

## 5. Role-Specific Screening (If Hiring a Replacement)

Use this if you need to find a replacement Librarian or the Conductor is sourcing one.

| # | Dimension | What You're Looking For | Critical? |
|---|-----------|------------------------|-----------|
| 1 | **Spreadsheet fluency** | Comfortable navigating large spreadsheets (900+ tabs). Not intimidated by scale. | YES |
| 2 | **Organizational rigor** | Evidence of maintaining complex file systems, databases, or knowledge bases. | YES |
| 3 | **Reliability** | Daily updates, no missed days. The system depends on this person being consistent. | YES |
| 4 | **Communication clarity** | Can write clear INSTRUCTIONS.md files. "Where is X?" answers are fast and precise. | YES |
| 5 | **Comfort with ambiguity** | Doesn't need to understand the business strategy — just needs to know where things are. | No |

**Profile:** Library science student, executive assistant, project coordinator, virtual assistant, knowledge management specialist.

**Career booster:** "I was the information architect for a 900-tab venture studio launch."

---

## 6. Escalation Guide

> *This section is role-invariant — identical framework across all Studio Phase roles.*

### Green — Handle autonomously
- Prepare working folders for confirmed flash team members
- Update the master Trade when work is submitted
- Update the TUP Status Tracker
- Answer "where is X?" questions from anyone in the system
- Route cross-cluster dependencies using existing master outputs
- Send daily status updates to Nilo

### Yellow — Ask Nilo first
- A flash team member wants to modify the master Trade directly (not through their folder)
- A cross-cluster dependency can't be resolved from existing outputs
- You're unsure which version of a TUP is canonical
- An expert grade and a PM's work are in conflict
- You want to change the folder structure or naming convention

### Red — Flag immediately (same day)
- Master Trade file is corrupted or accidentally edited
- A flash team member claims their folder is missing tabs
- Two people are working on the same TUP simultaneously
- You discover the Directory doesn't match the actual tab structure
- Any external or legal inquiry about the Trade's contents

### Escalation format (Slack DM to Nilo)

> **ESCALATION:**
> - **What:** [Brief description]
> - **Why:** [Why you can't handle it with the tools you have]
> - **My recommendation:** [What you think should happen]
> - **Urgency:** [Same day / 24 hrs / When convenient]

---

## 7. Handoff Checklist

> *This section is role-invariant — identical framework across all Studio Phase roles.*

### If you're being replaced mid-cycle

Prepare for your replacement:

- [ ] **TUP Status Tracker** — current, all statuses accurate
- [ ] **Google Drive access** — document all folder locations, permissions, sharing links
- [ ] **Master Trade location** — confirm which file is canonical
- [ ] **Active sprints** — list who is mid-sprint, what they're working on, expected completion
- [ ] **Pending dependencies** — any cross-cluster routing in progress
- [ ] **INSTRUCTIONS.md template** — the template you've been using for new folders
- [ ] **Your daily routine** — what you do first, second, third each day
- [ ] **Open questions** — anything you've been unsure about that the replacement should know

### End-of-cycle handoff (when imagination passet locks)

- [ ] **All 103 TUPs verified** — every TUP has A or B grade
- [ ] **Master Trade locked** — confirmed with Nilo, no further edits
- [ ] **Final TUP Status Tracker** — complete history of all sprints, grades, revisions
- [ ] **Google Drive archived** — all working folders preserved, master marked LOCKED
- [ ] **Lessons learned** — what worked, what didn't, what the next Librarian should know

---

## 8. Your Milestones

| Week | Milestone | Kill Criteria |
|------|-----------|--------------|
| W1 | Trade learned. Drive set up. TUP tracker created. Conductor hired/posting. | — |
| W2 | First 2-3 working folders prepared. First flash team members onboarded. | Can't navigate the Trade after 2 weeks → escalate |
| W4 | 10+ TUPs in production. Cross-cluster routing working. Daily updates consistent. | — |
| W8 | 50+ TUPs verified or in review. System running smoothly. | — |
| W12 | All 103 TUPs locked. Imagination passet complete. End-of-cycle handoff done. | Significant TUPs still unverified at W12 → escalate |

---

## 9. Quick Reference

| Question | Answer |
|----------|--------|
| Who do I report to? | Nilo |
| How do I communicate? | Slack DM, daily 2-3 sentence update |
| What's my budget? | $0 — Google Drive is free |
| What are the three tabs I need to know? | Directory, Taxonomy, Role Rosters |
| How many TUPs total? | 103 across 18 clusters |
| What if I can't find a tab? | Check Directory first, then ask Nilo |
| What if two people need the same output? | Extract it into both working folders from the master |
| When am I done? | When all 103 TUPs are locked and end-of-cycle handoff is complete |

---

## Sources

This package was synthesized from the following tabs in the IonWave ops model (v10):

| Source | Sheet # | What It Contributed |
|--------|---------|-------------------|
| Librarian Role | 10 | Full role spec, custody model, comp, sequence, profile |
| Flash Teams Model | 3 | Persistent vs flash roles, librarian as platform operator |
| Launch Narrative | 4 | Week-by-week sequence, Elaine's specific responsibilities |
| Revised Roles | 6 | Librarian role in flash teams registry, equity, duration |
| Role Engineering | 144 | 7-dimension framework, delegation depth, decision authority |
| Recruiting Funnel | 85 | Onboarding flow, folder preparation step |
| Trade Execution Path | — | Cross-reference for phase sequencing |
