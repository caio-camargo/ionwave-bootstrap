# Claude Agent Instructions

## Session Startup Protocol

When starting a new session, always:
1. Read `./ACTIVE_WORK.md` — check for concurrent work that might conflict with this session
2. Read `./00_start_here.md`
3. Follow the session startup instructions documented there (including claiming your scope in ACTIVE_WORK.md)
4. Run the commit guard: `bash scripts/check_uncommitted.sh` — if uncommitted changes exist, surface them to the operator before starting new work
5. Wait for user confirmation before proceeding with any work

This ensures consistency across all sessions, proper context loading, and prevents concurrent edit conflicts between operators.

## Session Closing Protocol

Before ending any session, always:
1. Ensure all new/modified files are committed: `bash scripts/check_uncommitted.sh`
2. If uncommitted files exist, ask the operator: "Session is ending — there are N uncommitted files. Should I commit them now?"
3. Standard commit pattern: `git add data/ tracking/ SESSION_LOG.md ACTIVE_WORK.md` then commit + push
4. Clear your claim from `ACTIVE_WORK.md`
5. Add a SESSION_LOG.md entry

**Never end a session with uncommitted workshop output.**
The GitHub Actions workflow (`.github/workflows/check_uncommitted.yml`) runs daily as a backstop,
but the primary check must happen at session close.

## TUP Workshop Protocol

When workshopping a TUP (Trade Unit Project), always:
1. Read `./processes/TUP_Workshop_Protocol.md` — this is the canonical process
2. Follow the 11 phases documented there (Load → Gather → Checkpoint → Research → Fill → Dialogue → Self-Grade → OpKit → Register → Cross-Ref → Log)
3. Track progress in `./tracking/TUP_Workshop_Tracker.md`

Every TUP workshop produces two outputs: IonWave-specific content AND a reusable OpKit.
The protocol includes expert persona dialogue to saturation, source quality hierarchy, and self-grading.
