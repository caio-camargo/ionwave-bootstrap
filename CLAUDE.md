# Claude Agent Instructions

## Session Startup Protocol

When starting a new session, always:
1. Read `./ACTIVE_WORK.md` — check for concurrent work that might conflict with this session
2. Read `./00_start_here.md`
3. Follow the session startup instructions documented there (including claiming your scope in ACTIVE_WORK.md)
4. Run the commit guard: `bash execution/scripts/check_uncommitted.sh` — if uncommitted changes exist, surface them to the operator before starting new work
5. Wait for user confirmation before proceeding with any work

This ensures consistency across all sessions, proper context loading, and prevents concurrent edit conflicts between operators.

## Session Closing Protocol

Before ending any session, always:
1. Ensure all new/modified files are committed: `bash execution/scripts/check_uncommitted.sh`
2. If uncommitted files exist, ask the operator: "Session is ending — there are N uncommitted files. Should I commit them now?"
3. Standard commit pattern: `git add ionwave/data/ execution/tracking/ SESSION_LOG.md ACTIVE_WORK.md` then commit + push (submodules require their own commit first — see below)
4. Clear your claim from `ACTIVE_WORK.md`
5. Add a SESSION_LOG.md entry

**Never end a session with uncommitted workshop output.**
The GitHub Actions workflow (`.github/workflows/check_uncommitted.yml`) runs daily as a backstop,
but the primary check must happen at session close.

**Submodule commit pattern** — changes inside a submodule must be committed and pushed from within the submodule directory first, then the parent repo updated to reference the new commit:
```bash
# 1. Commit inside submodule (e.g., ionwave data change)
cd ionwave && git add data/ IonWave/ && git commit -m "..." && git push && cd ..
# OR for execution tracking:
cd execution && git add tracking/ && git commit -m "..." && git push && cd ..
# 2. Update parent reference
git add ionwave  # or execution, tup-system
git commit -m "Update submodule ref: ionwave" && git push
```

## Open Decisions & Project Nerve Center

**When any operator asks about open decisions, blockers, what needs attention, or project status:**

1. Read `./PROJECT_NERVE_CENTER.md` — this is the single aggregated view of all open items
2. Present the relevant section based on what the operator asks:
   - "What decisions need my input?" → Show Section 1 (Open Decisions Register), filtered to decisions owned by or needing that operator
   - "What's blocking launch?" → Show Section 2 (Pre-Launch Critical Path)
   - "What's the project status?" → Show Section 6 (Project Status Summary)
   - "What's stale?" → Show Section 5 (Stale Items Sweep)
   - General "what needs attention?" → Show the CRITICAL decisions from Section 1, then pre-launch blockers from Section 2

3. **Before presenting options**: Read `./DECISION_PREANSWERS.md` — this contains pre-loaded answers written in Danilo's thinking style (adaptive structures, requisite variety, meta-level reasoning). Present the pre-answer as "Here's how I think you'd answer this" and let the operator confirm, adjust, or push back. Follow the dependency order and session flow instructions at the bottom of that file.

4. **When resolving a decision**: Walk the operator through the options, capture their decision with rationale, then:
   - Update the decision's status in `PROJECT_NERVE_CENTER.md` (mark resolved, record rationale and date)
   - Update the source file where the decision originated (e.g., `Open_Questions.md`, `chain_specification.md`, relevant `_meta.json`)
   - Check if resolving this decision unblocks other items — surface those next
   - Commit changes

5. **Decision resolution format** — when an operator locks a decision, record it as:
   ```
   **RESOLVED [date]**: [Decision text]. Rationale: [why]. Decided by: [who].
   ```

**The Nerve Center is a live document.** Update it whenever decisions are resolved, blockers are cleared, or new items are discovered. It should always reflect current reality.

## TUP Workshop Protocol

When workshopping a TUP (Trade Unit Project), always:
1. Read `./tup-system/processes/TUP_Workshop_Protocol.md` — this is the canonical process
2. Follow the 11 phases documented there (Load → Gather → Checkpoint → Research → Fill → Dialogue → Self-Grade → OpKit → Register → Cross-Ref → Log)
3. Track progress in `./execution/tracking/TUP_Workshop_Tracker.md`

Every TUP workshop produces two outputs: IonWave-specific content AND a reusable OpKit.
The protocol includes expert persona dialogue to saturation, source quality hierarchy, and self-grading.
