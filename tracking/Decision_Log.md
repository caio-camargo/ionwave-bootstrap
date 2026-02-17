# IonWave Decision Log

**Purpose:** Append-only history of decisions with full context, rationale, and impact  
**Format:** Each decision gets a unique ID: YYYY-MM-DD-###  
**Usage:** Reference decisions by ID in other tracking documents

---

## 2026-02-17-002: Canonical Home — GitHub vs Google Drive

**Status:** TBD — requires Danilo input before deciding

**Context:**
The IonWave Bootstrap currently lives in a Google Drive shared folder (`G:\Drives compartilhados\Studio 3\IonWave\IonWave Bootstrap`) AND is connected to a GitHub repo (`github.com/caio-camargo/ionwave-dashboard`). This is an accidental hybrid — not a deliberate architecture decision. The tension surfaced during M36 workshop planning when designing the monitoring/automation system.

**Current State (discovered 2026-02-17):**
- Repo: `github.com/caio-camargo/ionwave-dashboard` (origin/main)
- Git is active and tracking: 16 total commits, `main` branch + 3 local branches (`angry-solomon`, `cool-cohen`, `kind-volhard`)
- **59 files modified since last commit** (all TUP workshop work from sessions 7+: M36, M31, M35, M4, M39, and all registration updates to manifest.json, opkits/registry.json, TUP_Workshop_Tracker.md, SESSION_LOG.md)
- These changes exist only locally — NOT pushed to GitHub
- The HTML dashboard is deployed to GitHub (gh-pages presumably)
- Both Caio and Danilo access via Google Drive shared folder + their own Claude Code sessions

**What's working:**
- Claude Code operates directly against the Drive-mounted path — functional
- Danilo can access all files via Drive without needing git knowledge
- GitHub exists as a backup/deployment target for the dashboard

**What's broken:**
- No version control on 34+ TUPs of workshop work (all done since last commit)
- Accidental hybrid: git exists but isn't being used systematically
- Automation design (monitoring system, GitHub Actions) blocked until canonical home decided
- Danilo's workflow with the repo is unknown — he uses his own Claude Code but hasn't deeply engaged yet

---

**Option A: GitHub as Canonical Home (structured data + automation)**

```
GitHub Repo (source of truth for structured data)
├── data/           all JSON + markdown TUP content
├── tracking/       workshop tracker, session log, decision log
├── processes/      protocols, prompts
├── scripts/        automation, GitHub Actions workflows
└── dashboard/      generated HTML views

Google Drive (human-facing deliverables only)
├── Deliverables/   PDFs, slides, final outputs
├── Reference/      content shared with operators, advisors
└── Media/          images, video, design assets
```

**Pros:**
- Proper version control — every change tracked, attributable, reversible
- Claude Code works natively (already does)
- GitHub Actions for automation (free, robust, debuggable — see DEC-2026-02-17-003)
- Pull requests if Danilo/Caio want review workflows
- 59 uncommitted changes would get versioned immediately

**Cons:**
- Danilo needs GitHub comfort level for writing (reading is easy via browser)
- Non-technical stakeholders (operators, advisors) can't edit directly
- Multimedia assets need Drive or LFS anyway

**Requires:** Danilo uses git (or works exclusively via Claude Code which handles git)

---

**Option B: Google Drive as Canonical Home**

```
Google Drive (source of truth for everything)
├── IonWave Bootstrap/    all structured data (current state)
├── Deliverables/         outputs, reference models
└── Media/                assets

GitHub (deployment target only)
└── dashboard/            HTML dashboard synced from Drive
```

**Pros:**
- Zero friction for Danilo — he already has Drive access
- Familiar to non-technical collaborators
- Native multimedia support
- Google Apps Script for automation (free, native, no git required)

**Cons:**
- No real version control (Drive's history is weak)
- Automation (Apps Script) is less powerful than GitHub Actions
- Claude Code's Drive integration is a workaround, not native
- If a file gets corrupted or overwritten, recovery is manual

---

**Option C: Deliberate Hybrid (current state, made intentional)**

```
GitHub (structured data + automation + version control)
├── data/           JSON + markdown — source of truth
├── tracking/       logs, trackers
└── .github/        automation workflows

Google Drive (human collaboration layer)
├── Deliverables/   final outputs generated from GitHub content
├── Working Docs/   Google Docs for collaborative editing
└── Media/          assets

Sync rule: GitHub → Drive for deliverables (one-way, automated)
          Drive → GitHub never (humans don't write to the data layer)
```

**Pros:**
- Best of both: version control for data, Drive for human access
- Danilo can read everything in Drive without git
- Automation lives in GitHub where it belongs
- Deliverables automatically published to Drive from GitHub

**Cons:**
- More complex — two systems to maintain
- Sync logic needs building (small but non-trivial)
- Risk of confusion about which is "real" if discipline breaks down

---

**Recommendation (Claude's assessment):**
**Option C (Deliberate Hybrid)** with a clear rule: **GitHub is the source of truth for data, Drive is for human consumption.** Humans never write directly to the data layer — only Claude Code sessions do, via git.

This works because:
- Danilo and operators interact via Claude Code (which handles git natively) or read Drive outputs
- The 59 uncommitted changes should be committed and pushed immediately regardless of which option is chosen
- Automation (monitoring system) lives in GitHub Actions — simpler, more powerful than Apps Script
- Drive deliverables become *outputs* of the system, not inputs

**The key question for Danilo:** Does he want to write TUP content directly into files (needs Drive or git comfort), or interact with the system exclusively through Claude Code conversations (git is invisible to him)? If the latter, Option C or A both work fine.

---

**Blocking decisions:**
- [ ] Which option (A, B, or C)?
- [ ] Commit and push the 59 uncommitted files regardless (should happen now)
- [ ] Danilo's workflow preference (write directly vs Claude Code mediated)

**Owner:** Caio + Danilo
**Due:** Before building monitoring/automation system
**Logged By:** Claude
**Date:** 2026-02-17

**Related:**
- DEC-2026-02-17-003 (Monitoring System Architecture)
- M36 Operational Infrastructure workshop (operational parameters monitoring)
- ACTIVE_WORK.md (M36 workshop in progress)

---

## 2026-02-17-003: Monitoring System Architecture — GitHub Actions vs Google Apps Script

**Status:** TBD — blocked by DEC-2026-02-17-002 (canonical home decision)

**Context:**
M36 Operational Infrastructure defines hard operating parameters (CAC <$40, ROAS >2x, Safety stock 14 days, SLA 4hr, ad test budget $100/ad) and operating rhythms (daily parameter checks, weekly WBR, monthly MBR). The vision is Claude-powered management — but Claude has no native scheduling capability. A trigger mechanism is needed.

**The problem:** Periodic reviews need to *actually happen* without:
- Claude spontaneously initiating (impossible)
- Caio manually remembering each week (founder cognitive load)
- Heavy custom infrastructure (fragile, expensive)

**Design principle:** Simple, robust, easy to debug. Output back to the repo (repo = HQ).

---

**Two viable options:**

**Option A: GitHub Actions (preferred if GitHub = canonical home)**

How it works: YAML workflow files define schedules. On trigger, a Python script fetches data, calls Claude API, commits output to `tracking/reviews/`.

```yaml
# .github/workflows/wbr_weekly.yml
on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday 9am
```

```
scripts/
  fetch_data.py         # Pull from Shopify/Meta/Klaviyo APIs (post-launch)
  run_wbr.py            # Feed data + prompt → Claude API → markdown output
  run_param_check.py    # Check operating parameters against thresholds
prompts/
  wbr_prompt.md         # WBR template (version-controlled with data)
  param_check_prompt.md # Threshold definitions
.github/workflows/
  param_check_daily.yml # Daily: CAC, ROAS, inventory check
  wbr_weekly.yml        # Monday: full WBR
  mbr_monthly.yml       # 1st of month: MBR
```

Output: committed to `tracking/reviews/wbr_YYYY-MM-DD.md` in the repo.

**Pros:** Free, version-controlled prompts, full run logs in GitHub UI, re-run manually with one click, scales naturally
**Cons:** Requires Anthropic API key (simple setup, ~$0.05/run), Python script (~100 lines)
**Debuggability:** High — every run is a GitHub Actions log entry, visible in browser

---

**Option B: Google Apps Script (if Google Drive = canonical home)**

How it works: Apps Script runs on Google's infrastructure with native time-based triggers. Calls Claude API via UrlFetchApp, writes output to a Google Doc or Sheet.

```javascript
// Runs every Monday at 9am (set via Apps Script trigger UI)
function runWeeklyWBR() {
  const data = fetchShopifyData();  // UrlFetchApp to Shopify API
  const response = callClaudeAPI(data, WBR_PROMPT);
  writeToGoogleDoc(response);  // Or Sheet, or Drive file
}
```

**Pros:** Free, no git required, native Google ecosystem, trigger UI is non-technical
**Cons:** Output lands in Google Docs/Sheets, not the repo (extra sync step needed), 6-min execution limit, less powerful than Python
**Debuggability:** Medium — Apps Script has execution logs but less precise than GitHub Actions

---

**Two-phase implementation (regardless of option chosen):**

**Phase 1 (Now — pre-launch, buildable today):**
- Input: repo data files (manifest.json, _meta.json files, tracking/*.md)
- Claude reviews planning data: open questions, hypothesis staleness, workshop gaps, blocking decisions
- Output: `tracking/reviews/project_health_YYYY-MM-DD.md`
- No external APIs needed

**Phase 2 (Post-launch):**
- Input: Phase 1 + live Shopify/Meta/Klaviyo API data
- Claude reviews operating parameters against thresholds
- Output: `tracking/reviews/wbr_YYYY-MM-DD.md` + parameter alerts

Phase 1 is immediately useful and builds the exact infrastructure Phase 2 extends.

---

**Operating parameters to monitor (from M36):**

| Parameter | Threshold | Frequency | Data Source |
|-----------|-----------|-----------|-------------|
| CAC | <$40 (kill above) | Daily | Meta API (post-launch) |
| ROAS | >2x (scale above) | Daily | Meta API (post-launch) |
| Safety stock | >14 days | Weekly | Shopify inventory (post-launch) |
| Support SLA | <4hr response | Daily | Gorgias/email (post-launch) |
| Ad test budget | $100/ad before kill | Per campaign | Meta API (post-launch) |
| Workshop progress | 41 TUPs complete | Weekly | manifest.json (now) |
| Open decisions | 0 blocking | Weekly | Decision_Log.md (now) |
| Hypothesis staleness | <30 days since update | Monthly | hypotheses/registry.json (now) |

**Recommendation:** GitHub Actions + Claude API. Simpler, more powerful, version-controlled, output lives in the repo. Build Phase 1 immediately once DEC-2026-02-17-002 is resolved.

**Anthropic API:** Not yet set up. Setup: console.anthropic.com → create key → add to GitHub Secrets. Cost: ~$0.05/WBR run at claude-haiku-3-5 pricing. Negligible.

**Blocking decisions:**
- [ ] DEC-2026-02-17-002 resolved (canonical home determines which option)
- [ ] Anthropic API key created and stored securely
- [ ] Phase 1 scope confirmed (which reviews to automate first)

**Owner:** Caio
**Due:** After DEC-2026-02-17-002 resolved
**Logged By:** Claude
**Date:** 2026-02-17

**Related:**
- DEC-2026-02-17-002 (Canonical Home decision)
- M36 Operational Infrastructure (operating parameters source)
- M35 Execution Plans (WBR/MBR templates)

---

## 2026-02-02-001: Gross Margin Discrepancy Discovered

**Status:** IN RESOLUTION (not yet decided)

**Context:**
During bootstrap improvement work on Market Landscape, discovered critical discrepancy:
- Unit Economics sheet assumes 70% gross margin
- Landed Cost Breakdown shows 40% gross margin (based on actual supplier quotes)
- This 30 percentage point gap has massive downstream impacts

**Investigation:**
- Loaded Landed Cost Breakdown sheet
- Supplier quotes show $12 COGS for 30-serving bottle
- At $59 retail price point = ($59 - $12) / $59 = 79.7% margin... wait
- Need to verify actual calculation in sheet
- **Root Cause:** Unit Economics used industry benchmark (supplements typically 70-80%)
- Landed Cost used actual supplier quotes (marine plasma more expensive than synthetic)

**Options Under Consideration:**
1. **Accept 40% margin reality:**
   - Pro: Based on real supplier data
   - Con: Much lower than industry standard
   - Con: May not support desired unit economics
   - Impact: Need higher price OR volume to hit targets

2. **Negotiate COGS down to enable 70% margin:**
   - Target COGS: ~$8 instead of $12 (33% reduction)
   - Pro: Aligns with industry benchmarks
   - Con: May not be achievable with marine plasma
   - Action: Need supplier negotiation or alternative sourcing

3. **Increase price point:**
   - Target: $79-89 retail (vs current $59)
   - Pro: Improves margin at current COGS
   - Con: May reduce conversion rate
   - Con: Positions above LMNT ($45 for 30 servings)

**Impact Analysis:**
- **Unit Economics:** Must be rebuilt with correct margin
- **Offer Strategy:** Pricing strategy may need complete revision
- **Financial Model:** Revenue projections could drop ~30%
- **W Formula Score:** May affect viability if margin kills profitability
- **Competitive Positioning:** Price point affects positioning vs LMNT/Seaonic

**Affected Sheets/Models:**
- Unit Economics (primary)
- Landed Cost Breakdown (source of truth)
- Offer Strategy
- Financial Model
- Pricing decisions

**Next Actions:**
- [ ] Verify exact COGS calculation in Landed Cost sheet
- [ ] Verify exact margin calculation in Unit Economics sheet
- [ ] Model all three scenarios (accept, negotiate, price up)
- [ ] Get Danilo's decision on path forward
- [ ] Update all affected sheets once decided
- [ ] Document decision rationale

**Owner:** Danilo (decision maker) + Caio (analysis support)  
**Due:** Within 48 hours (blocks multiple streams)  
**Logged By:** Claude  
**Date:** 2026-02-02

**Related:**
- Discrepancy_Register.md #D1
- Open_Questions.md #Q1
- MASTER_CONTROL.md (Critical Dependencies section)

---

## 2026-02-02-002: Bootstrap Methodology - Track A vs Track B

**Status:** DECIDED

**Context:**
Working on improving IonWave Market Landscape from 4-6/10 to 8-9/10 quality. Need to determine what work can be done immediately (Track A) vs what requires data collection tools (Track B).

**Decision:**
Split improvement work into two tracks:

**Track A (Strategic Analysis - No Tools):**
- Apply expert frameworks (Porter's Five Forces, Skeptical Investor lens)
- Mine customer voice from free web search (Reddit, Trustpilot, reviews)
- Competitive response scenario planning
- Strategic gap analysis
- Time: 4-6 hours
- Cost: $0
- Quality impact: 4/10 → 6-7/10

**Track B (Data Collection - Tools Required):**
- SEMrush traffic verification
- Paid market research reports
- Extensive competitor coverage (expand from 2 to 10-12)
- Time: 15-20 hours
- Cost: Tool subscriptions + labor
- Quality impact: 6-7/10 → 8-9/10

**Rationale:**
- Can make significant quality improvements without waiting for data
- Clear workflow choreography: Track A first, then decide if Track B needed
- Separates strategic thinking from data gathering
- Lets Operator (Caio) make immediate progress

**Impact:**
- Market Landscape improvement can start immediately
- Sets pattern for other deliverable improvements
- Informs OpKit development approach

**Next Actions:**
- [x] Execute Track A work on Market Landscape
- [ ] Document what worked for methodology extraction
- [ ] Decide if Track B needed after Track A complete

**Owner:** Caio + Claude  
**Date:** 2026-02-02  
**Logged By:** Claude

**Related:**
- Market_Landscape_Bootstrap_Plan.md
- 03_What_We_Did.md (Track A/B discovery)

---

## TEMPLATE FOR FUTURE DECISIONS

```
## YYYY-MM-DD-###: [Decision Title]

**Status:** [DECIDED | IN DISCUSSION | DEFERRED | REVERSED]

**Context:**
[What situation prompted this decision? What was happening?]

**Decision:**
[What was decided? Be specific and clear.]

**Options Considered:**
1. [Option 1 with pros/cons]
2. [Option 2 with pros/cons]
3. [Option 3 with pros/cons]

**Rationale:**
[Why this option? What factors tipped the decision?]

**Impact Analysis:**
[What does this affect? Downstream consequences?]

**Affected Sheets/Models:**
[List specific sheets/models that need updates]

**Next Actions:**
- [ ] [Action item 1]
- [ ] [Action item 2]

**Owner:** [Who owns execution]  
**Date:** [When decided]  
**Logged By:** [Who logged it]

**Related:**
[Links to other tracking documents]
```

---

**Log Maintenance:**
- Append new decisions to bottom (reverse chronological at top)
- Never delete entries (historical record)
- Update status as decisions evolve
- Reference by ID in other documents
