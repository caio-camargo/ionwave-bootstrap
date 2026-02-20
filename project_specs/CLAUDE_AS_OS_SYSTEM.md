# Claude-as-OS System Specification

**Version:** 1.0.0
**Date:** 2026-02-11
**Author:** Caio + Danilo
**Status:** Planning
**Related TUPs:** M35, M36, M37, M40

---

## Vision

**"Claude Code as the primary operational interface for Trade execution"**

The operator, Studio 3 oversight, and VP capital interface all work THROUGH Claude rather than scattered spreadsheets, Slack threads, and manual status updates. Claude maintains an auditable scorecard, knows exactly where everything is (standardized passet folder structure), ingests live data (APIs), and can answer "what's next?", "are we on schedule?", "what are the red flags?"

This operationalizes M39's "Virtual Twin" concept - Claude as the operational twin of the Trade with complete mutual information.

---

## Core Principles

1. **All deliverables = documents in passet folders** (or links if deployed externally like Shopify)
2. **Standardized structure** across ALL Trades (same folder schema, same scorecard format)
3. **Claude = primary interface** (operator asks Claude, Studio 3 asks Claude, VP asks Claude)
4. **Auditable + version controlled** (Git, passet folders, no data in Slack/email black holes)
5. **Automated data ingestion** where possible (Shopify API, Meta Ads API → passet folders daily)
6. **Query-based oversight** (Studio 3 doesn't maintain dashboards, asks Claude for status)
7. **Highly concentrated work** (operator role = intense, full-time+, deployment-focused)
8. **LLM Legibility Guarantee** — The system must guarantee that all structured data, documentation, and operational artifacts remain legible to LLMs across model versions, providers, and context window sizes. This means: plain text and markdown over proprietary formats; consistent semantic structure (headers, sections, lists); self-contained documents with inline context; no reliance on a single LLM provider (the system should work with Claude, OpenClaw, or future models). LLM legibility is not a nice-to-have — the system *requires* LLMs to function, and any artifact the system produces that an LLM cannot parse is a system failure. See also: Integration Design Principles (AI Context Window Optimization).

---

## TUP Coverage Map

This system spans 4 TUPs:

| TUP | Focus | Deliverables |
|-----|-------|-------------|
| **M40 Navigation** | WHERE everything is, HOW to find it | Passet folder structure, navigation schema, query interface library, role entry points |
| **M35 Execution Plans** | WHAT happens WHEN | Week 1-12 choreography, timeline + dependencies, daily task lists, phase checklists, scorecard template |
| **M36 Operational Infra** | HOW systems work | API integrations (Shopify/Meta/GA), data maintenance protocols, knowledge management, quality systems |
| **M37 AI & Automation** | Automation patterns | Daily data ingestion scripts, scorecard auto-update, red flag detection, operator coaching prompts |

**Build Order:** M40 (foundation) → M35 (choreography) → M36 (infra) → M37 (automation)

---

## Stakeholder Use Cases

### Operator Use Cases

**"What's next?"**
- Claude: "Week 3 Day 2. Priority 1: Upload 10 ad creatives to Meta (due today). Priority 2: Review supplier CoA (arrived yesterday, needs approval). Priority 3: Prep influencer outreach emails (due Friday). Blocked: Logo design (waiting on designer)."

**"What do my next 3-5 days look like?"**
- Claude: "Days 16-20 (Week 3). Mon-Tue: Ad testing sprint (upload 10 creatives, monitor first 24hr results). Wed: Supplier decision (approve CoA or escalate quality concerns). Thu-Fri: Influencer outreach prep (draft 15 emails, schedule sends Week 4)."

**"How do I approve a supplier CoA?"**
- Claude: "See `/passets/product/supplier_coa_checklist.md`. Check 11 test requirements (heavy metals <10ppb As, micro <10 CFU/mL, etc.). If PASS: update `/passets/product/supplier_status.md` to 'approved', move to inventory order. If FAIL: escalate to Studio 3 immediately (kill criteria risk)."

**"Am I on track?"**
- Claude: "🟡 YELLOW. 2 days behind schedule. Supplier CoA delayed (was due Monday, now Thursday). This pushes first inventory order from Week 2 to Week 3. Soft launch risk: moderate (can compress Week 3-4 if CoA approved by Friday). No kill criteria triggered."

### Studio 3 Oversight Use Cases

**"Is IonWave on schedule?"**
- Claude: "⚠️ 2 days behind. Week 3 Day 2 vs planned Week 3 Day 4. Delay: supplier CoA (quality testing took 6 days vs expected 3 days). Critical path impact: inventory order delayed to Week 3, soft launch window compressed by 2 days. Recovery plan: operator can work weekend to compress Week 3-4. Kill criteria: not triggered (2/3 ad angles converting >5%)."

**"What are the red flags?"**
- Claude: "2 red flags. 🔴 CAC $60 (target $35, 71% over). Testing 5 angles, only 2 converting >5% (Missing Mineral 12% CTR $52 CAC, Comparison 9% CTR $58 CAC). Need 3 more days data before kill/scale decision. 🟡 Logo finalization blocked (designer missed Friday deadline, now Monday). Impacts: packaging timeline at risk, soft launch may need to use temp logo."

**"Should we intervene?"**
- Claude: "NOT YET. Operator is executing well (all tasks completed on time except external dependencies). Delays are supplier-side (CoA testing) and vendor-side (logo designer). Recommend: 1) Give operator until Friday to resolve logo blocker. 2) Monitor CAC through Weekend (if still >$50 Monday, consider pivot or kill). 3) Weekly check-in sufficient (no daily intervention needed)."

**"What does the operator need help with?"**
- Claude: "1 ask. Logo designer unresponsive (missed Friday deadline). Operator needs: Studio 3 escalation to designer OR backup designer recommendation. Blocking: packaging finalization, product photography, soft launch creative. Timeline risk: HIGH if not resolved by Monday."

### VP Capital Interface Use Cases

**"What metrics do I report to investors this week?"**
- Claude: "Week 4 metrics: $2,847 ad spend (95% of $3K budget), 47 orders ($60 CAC vs $35 target), 0% repeat rate (too early, need 30 days), $0.52 COGS confirmed (target $0.55, ✅ validated). Narrative: Testing 5 angles, 2 showing promise (Missing Mineral 12% CTR, Comparison 9% CTR). CAC high but expected in testing phase. Kill criteria not triggered (need 10+ purchases per creative, currently 4-7 range). Next milestone: Scale decision Week 5 (if CAC drops <$45, scale to $10K/month)."

**"How much runway do we have?"**
- Claude: "$28,450 remaining of $50K raise. Burn rate: $3,500/week (ads $3K + tools $300 + misc $200). Runway: 8.1 weeks at current burn. Next capital need: Week 8-10 (inventory order $15K) OR Week 12 (scale ads to $10K/month if validated). Fundraising trigger: Week 6 check-in (if CAC <$40 stable, begin Series Seed conversations for $100-200K)."

**"Should we raise more capital now?"**
- Claude: "NOT YET. Current status: Testing phase (Week 4 of 7-week validation sprint). CAC $60 (high but expected during testing). Kill criteria check: PASS (2/3 angles converting, 47 orders shipped, no fatal product issues). Recommendation: Wait until Week 6 decision gate. If CAC drops <$40 and repeat rate >20%, THEN raise $100-200K for scale. If CAC stays >$50 or repeat <10%, KILL or PIVOT (don't raise). Capital on hand sufficient through Week 12."

---

## System Components

### 1. Passet Folder Structure (M40)

**Standardized structure for ALL Trades:**

```
/passets/
  /product/
    formulation_spec.md (M5)
    supplier_contracts/ (M6)
    supplier_coa_checklist.md (M6)
    supplier_status.md (M6 - UPDATED BY OPERATOR)
    regulatory_compliance_log.md (M7)

  /brand/
    brand_identity_guide.md (M8)
    logo_files/ (M8 - links to design files)
    packaging_specs/ (M8)
    messaging_framework.md (M8)

  /creative/
    vsl_scripts/ (M11)
    ad_creative_library/ (M12)
    landing_page_copy/ (M15)
    creative_performance_tracker.md (M12 - UPDATED DAILY via API)

  /operations/
    fulfillment_sops/ (M24)
    support_playbooks/ (M20)
    ecommerce_setup_log.md (M9)

  /metrics/
    shopify_daily.json (AUTO-UPDATED via API)
    meta_ads_daily.json (AUTO-UPDATED via API)
    ga_weekly.json (AUTO-UPDATED via API)
    cohort_analysis_weekly.csv (GENERATED by Claude)

  /timeline/
    gantt_week_1_12.md (M35 - critical path)
    task_dependencies.md (M35)
    milestone_tracker.md (M35 - UPDATED BY OPERATOR + Claude)
    daily_task_lists/ (M35 - GENERATED by Claude from gantt)

  /scorecard/
    weekly_snapshot_YYYY_MM_DD.md (M35 - MAINTAINED BY CLAUDE)
    kpi_definitions.md (M35)
    red_flag_thresholds.md (M35)
    kill_criteria.md (M35 - from M0 trade thesis)

  /decisions/
    decision_log.md (ALL - operator + Studio 3 decisions)
    escalations.md (M35 - operator asks for help)
    kill_criteria_checks.md (M35 - weekly evaluation)
```

**[STANDARD]** = applies to all Trades
**[IONWAVE-SPECIFIC]** = customize per Trade (KPIs, kill criteria, phase gates)
**[AUTO-UPDATED]** = API integration
**[OPERATOR-UPDATED]** = manual input required
**[CLAUDE-GENERATED]** = derived from other data sources

### 2. Scorecard Template (M35)

**Weekly snapshot maintained by Claude:**

```markdown
# IonWave Weekly Scorecard — Week [N] ([Date Range])

**Overall Status:** 🟢 GREEN / 🟡 YELLOW / 🔴 RED

**Status Definition:**
- 🟢 GREEN: On schedule, all KPIs in target range, no blockers
- 🟡 YELLOW: 1-3 days behind OR 1-2 KPIs outside target OR minor blockers (recoverable)
- 🔴 RED: >3 days behind OR 3+ KPIs outside target OR major blockers OR kill criteria risk

---

## This Week Summary

**Completed:**
- [x] Task 1 (due Mon) - completed Mon
- [x] Task 2 (due Wed) - completed Tue (1 day early)
- [x] Task 3 (due Fri) - completed Fri

**In Progress:**
- [ ] Task 4 (due next Mon) - 60% complete
- [ ] Task 5 (due next Wed) - blocked (waiting on external vendor)

**Blockers:**
- 🚧 Logo designer unresponsive (blocking packaging, product photos)
- 🚧 Supplier CoA delayed 6 days (quality testing took longer than expected)

**Decisions Made:**
- Approved Missing Mineral angle for scale (12% CTR, $52 CAC, 15 purchases)
- Paused Authority angle (4% CTR, $85 CAC, 3 purchases after 5 days)

---

## Metrics Dashboard

| Metric | Actual | Target | Variance | Status | Trend |
|--------|--------|--------|----------|--------|-------|
| **Ad Spend** | $2,847 | $3,000 | -5% | 🟢 | → |
| **Orders** | 47 | 50 | -6% | 🟡 | ↗ |
| **CAC** | $60 | $35 | +71% | 🔴 | ↘ |
| **COGS** | $0.52 | $0.55 | -5% | 🟢 | → |
| **Repeat Rate** | 0% | N/A | N/A | ⚪ | (too early) |
| **Inventory** | 0 units | TBD | N/A | 🟡 | (CoA pending) |

**Trend Legend:** ↗ improving, → stable, ↘ declining

---

## Next Week Priorities (Week [N+1])

1. **P0 (Critical):** Approve supplier CoA, place inventory order ($15K) - BLOCKS soft launch
2. **P0 (Critical):** Resolve logo blocker (escalate to Studio 3 or find backup designer)
3. **P1 (High):** Scale Missing Mineral angle if CAC drops <$50 by Monday
4. **P2 (Medium):** Launch Comparison angle variant test (3 new hooks)
5. **P3 (Low):** Begin influencer outreach prep (draft 15 emails for Week [N+2])

---

## Kill Criteria Check

| Criteria | Threshold | Actual | Status | Notes |
|----------|-----------|--------|--------|-------|
| Ad angles converting | ≥2 of 5 with >5% CTR | 2 of 5 | ✅ PASS | Missing Mineral 12%, Comparison 9% |
| Min purchases per creative | ≥10 after 7 days | 4-15 range | 🟡 WATCH | 2 creatives >10, 3 creatives <10 (need 3 more days) |
| CAC below threshold | <$75 (kill if >$75 after 14 days) | $60 | ✅ PASS | High but acceptable in testing phase |
| Product quality issues | 0 critical defects | 0 | ✅ PASS | No customer complaints, no returns yet |
| Repeat purchase rate | >10% after 30 days | 0% | ⚪ N/A | Too early (only 10 days since first orders) |

**Overall Kill Criteria Status:** ✅ PASS (no kill triggers)

---

## Escalations

**None this week.**

(If escalations exist, format:)
- **[PRIORITY]** [Brief description] - [What operator needs from Studio 3] - [Timeline]

---

## Studio 3 Notes

(Space for Danilo/Nilo to add observations, decisions, guidance)

---

**Scorecard Maintained By:** Claude (auto-updated from `/passets/metrics/` + operator inputs)
**Last Updated:** [Timestamp]
**Next Update:** [Next Monday 9am]
```

### 3. Timeline + Task System (M35)

**Gantt Chart (Week 1-12 Critical Path):**

Maintained in `/passets/timeline/gantt_week_1_12.md` as markdown table:

```markdown
# IonWave Launch Timeline — Week 1-12 Critical Path

| Week | Phase | Key Milestones | Critical Tasks | Dependencies | Owner | Status |
|------|-------|---------------|----------------|--------------|-------|--------|
| **1** | Setup | Supplier locked, brand finalized, store live | Lock supplier (CoA review), finalize logo, deploy Shopify | M5/M6/M7/M8/M9 complete | Operator | 🟡 |
| **2** | Pre-Launch | Inventory ordered, ads built, influencers contacted | Place inventory order ($15K), upload 10 ad creatives, draft influencer emails | Week 1 supplier | Operator | 🔴 |
| **3** | Soft Launch | First ads live, first sales, war room active | Launch $3K ad test, ship first 50 orders, daily war room | Week 2 inventory | Operator | ⏳ |
| **4** | Testing | Angle validation, CAC optimization | Test 5 angles, kill losers, scale winners | Week 3 data | Operator | ⏳ |
| ... | ... | ... | ... | ... | ... | ... |
```

**Daily Task Lists:**

Auto-generated by Claude from gantt + dependencies in `/passets/timeline/daily_task_lists/`:

```markdown
# IonWave Daily Tasks — Week 3 Day 2 (Feb 11, 2026)

**Today's Date:** Tuesday, February 11, 2026
**Week:** 3 of 12 (Soft Launch phase)
**Overall Status:** 🟡 YELLOW (2 days behind, recoverable)

---

## Priority 0 (CRITICAL - Must Complete Today)

- [ ] **Upload 10 ad creatives to Meta** (due today)
  - Location: `/passets/creative/ad_creative_library/week_3/`
  - SOP: See `/passets/operations/meta_ads_upload_sop.md`
  - Blocker: None
  - Time estimate: 2 hours

- [ ] **Review supplier CoA** (arrived yesterday, needs approval by EOD)
  - Location: `/passets/product/supplier_coa_biocean_batch_001.pdf`
  - Checklist: `/passets/product/supplier_coa_checklist.md`
  - Decision: APPROVE → place inventory order / REJECT → escalate to Studio 3
  - Time estimate: 1 hour

---

## Priority 1 (HIGH - Complete This Week)

- [ ] **Prep influencer outreach emails** (due Friday)
  - Location: `/passets/creative/influencer_outreach/`
  - Target: Draft 15 emails
  - Time estimate: 3 hours (spread over Wed-Fri)

- [ ] **Monitor first 24hr ad performance** (launched yesterday)
  - Check `/passets/metrics/meta_ads_daily.json` at 9am, 3pm, 9pm
  - Flag to Studio 3 if CTR <3% or CPC >$2 after 24 hours
  - Time estimate: 30 min per check

---

## Priority 2 (MEDIUM - Next Week OK)

- [ ] **Begin packaging mockup review** (blocker: logo not finalized)
  - Waiting on: Logo designer (escalated to Studio 3)
  - Can't proceed until logo delivered
  - Move to P0 once logo arrives

---

## Blocked Tasks

- 🚧 **Finalize packaging** - BLOCKED by logo designer (missed Friday deadline)
  - Escalation: Studio 3 contacting designer today
  - Backup plan: Find new designer if no response by Wednesday

- 🚧 **Product photography** - BLOCKED by packaging + logo
  - Dependency chain: Logo → Packaging mockup → Photography shoot
  - Timeline risk: If logo delayed >3 days, soft launch uses temp packaging

---

## Completed Today

(Claude updates this section as operator checks off tasks)

---

**Total Work Today:** ~6-7 hours (P0: 3 hrs, P1: 3-4 hrs)
**Tomorrow Preview:** Ad performance review (if CTR >8%, begin scale prep), continue influencer emails, packaging review if logo arrives
```

### 4. Query Interface Library (M40)

**Operator Queries:**

| Query | Response Pattern | Data Sources |
|-------|------------------|--------------|
| "What's next?" | Prioritized task list (P0/P1/P2) from today's daily task list | `/passets/timeline/daily_task_lists/` |
| "What do my next 3-5 days look like?" | Timeline view (next 3-5 days from gantt) | `/passets/timeline/gantt_week_1_12.md` |
| "How do I [task]?" | SOP retrieval | `/passets/operations/[task]_sop.md` |
| "Am I on track?" | Scorecard status + timeline variance | `/passets/scorecard/` + `/passets/timeline/` |
| "What's blocked?" | List of blocked tasks + escalation recommendations | `/passets/timeline/daily_task_lists/` |

**Studio 3 Oversight Queries:**

| Query | Response Pattern | Data Sources |
|-------|------------------|--------------|
| "Is IonWave on schedule?" | Timeline variance + blocker summary + recovery plan | `/passets/timeline/` + `/passets/scorecard/` |
| "What are the red flags?" | Red/yellow scorecard items + kill criteria proximity | `/passets/scorecard/` |
| "Should we intervene?" | Intervention recommendation (yes/no/wait) + reasoning | `/passets/scorecard/` + `/passets/decisions/escalations.md` |
| "What does the operator need help with?" | Escalation list + asks | `/passets/decisions/escalations.md` |
| "How is [metric]?" | Metric trend + variance + context | `/passets/metrics/` |

**VP Capital Interface Queries:**

| Query | Response Pattern | Data Sources |
|-------|------------------|--------------|
| "What metrics do I report to investors this week?" | Weekly metrics + narrative + next milestones | `/passets/scorecard/` + `/passets/metrics/` |
| "How much runway do we have?" | Cash remaining + burn rate + runway weeks + next capital need | `/passets/scorecard/` (financial section) |
| "Should we raise more capital now?" | Raise recommendation (yes/no/wait) + reasoning + timing | `/passets/scorecard/` + kill criteria |

### 5. API Integration Architecture (M36)

**Automated Data Ingestion:**

| API | Frequency | Data Collected | Output Location | Error Handling |
|-----|-----------|----------------|-----------------|----------------|
| **Shopify Orders API** | Daily (2am) | Orders, revenue, AOV, returns | `/passets/metrics/shopify_daily.json` | If API fails, flag in scorecard, operator manually exports |
| **Meta Ads API** | Daily (3am) | Spend, impressions, clicks, CTR, CPC, purchases, CAC | `/passets/metrics/meta_ads_daily.json` | If API fails, flag in scorecard, operator manually exports from Ads Manager |
| **Google Analytics 4 API** | Weekly (Mon 4am) | Sessions, bounce rate, conversion rate, traffic sources | `/passets/metrics/ga_weekly.json` | If API fails, flag in scorecard, operator manually exports |

**Data Maintenance Protocols:**

- **Daily (4am):** Claude ingests new data → updates scorecard metrics section → flags anomalies (CAC spike >20%, CTR drop >30%, etc.)
- **Weekly (Mon 9am):** Claude generates weekly scorecard → archives previous week → pings operator for manual inputs (decisions, blockers, escalations)
- **On-demand:** Operator can ask "refresh metrics" to force re-ingest (if checking mid-day performance)

**Lightweight Automation Options:**

- **Option A:** Google Apps Script (free, runs on Google account, can hit APIs + write to Google Drive passet folder)
- **Option B:** GitHub Actions (runs on schedule, writes to passet folder, commits to Git)
- **Option C:** Zapier/Make (no-code, operator sets up once, runs automatically)
- **Option D:** Custom Python script (runs on operator's machine or server, most flexible)

**[DECISION NEEDED: Which automation approach to use?]**

### 6. Week 1-12 Baseline Choreography (M35)

**Phase Breakdown:**

| Phase | Weeks | Key Objective | Success Criteria | Kill Criteria |
|-------|-------|---------------|------------------|---------------|
| **SETUP** | 1-2 | Supplier locked, brand finalized, store live, ads built | Store live, 10 ad creatives uploaded, influencer list ready | Can't lock supplier with acceptable COGS (<$0.60), can't finalize brand (no logo after 2 weeks) |
| **SOFT LAUNCH** | 3-4 | First sales, angle testing, war room active | 50+ orders, 2+ angles converting >5%, CAC <$75 | 0 angles converting >5% after 2 weeks, CAC >$100, product quality issues |
| **VALIDATION** | 5-7 | CAC optimization, repeat rate emerging, scale decision | CAC <$40 stable, repeat rate >15%, clear winner angles | CAC stuck >$60 after 5 weeks, repeat rate <5%, no clear winners |
| **SCALE PREP** | 8-9 | Inventory scaled, creative replenishment system, ops tightened | Inventory for 500 units/month, creative production flow, fulfillment <2 day TAT | Can't secure inventory, creative fatigue, fulfillment breaking |
| **SCALE** | 10-12 | Ad spend $10K+/month, subscription optimization, PMF confirmation | $15K MRR, 40% subscription rate, <10% churn | Revenue plateau, CAC creep, churn >15% |

**Week-by-Week Critical Path:**

(Detailed choreography in M35 workshop - what MUST happen each week to stay on critical path)

---

## Open Questions for Q&A

### Infrastructure Questions

1. **API automation approach** - Which option (Google Apps Script / GitHub Actions / Zapier / Python)? Trade-offs?

2. **Passet folder location** - Currently using Google Drive shared folder. Should we:
   - Stay on Google Drive (easy sharing, no Git)
   - Move to Git repo (version control, harder for non-technical operator)
   - Hybrid (Git for code/specs, Drive for operator-facing docs)?

3. **Scorecard update frequency** - Weekly is baseline, but should Claude also do:
   - Daily micro-updates (just metrics, no narrative)?
   - On-demand (operator asks "update scorecard now")?
   - Event-driven (auto-update when kill criteria proximity detected)?

4. **Claude interface** - How does operator interact with Claude?
   - Claude Code CLI (current approach, requires terminal comfort)
   - Custom web app (chat interface, more accessible, requires build)
   - Slack/Discord bot (familiar, but data scattered)?

### Execution Model Questions

5. **Operator role definition** - Is operator:
   - **Full-stack solo** (does everything from ads to fulfillment to support)?
   - **Ads-focused specialist** (ads + creative primary, outsources fulfillment/support)?
   - **Generalist manager** (coordinates freelancers/agencies, doesn't execute)?

6. **Studio 3 oversight intensity** - How often does Danilo/Studio 3 check in?
   - Weekly sync call (30-60 min)?
   - Daily async check (Danilo queries Claude, no meeting)?
   - Event-driven only (Claude flags red flags, otherwise hands-off)?

7. **VP role boundaries** - Does VP:
   - Just interface with capital (raise money, report to investors)?
   - Also provide strategic guidance (pricing, positioning, hiring)?
   - Have veto power over operator decisions (or just advisory)?

### Content Questions

8. **M35 choreography specificity** - Should Week 1-12 choreography be:
   - **Prescriptive** ("Day 1: Do X, Day 2: Do Y") - easier for operator, less flexible
   - **Milestone-based** ("Week 1: Achieve X, Y, Z however you want") - flexible, requires judgment
   - **Hybrid** (prescriptive for Week 1-2, milestone-based after)?

9. **SOPs granularity** - How detailed should `/passets/operations/` SOPs be?
   - **Step-by-step screenshots** (easy for operator, high maintenance)
   - **Checklist + principles** (faster to create, requires operator judgment)
   - **Video walkthroughs** (best for complex tasks, harder to update)?

10. **OpKit reusability** - Should OpKits be optimized for:
    - **IonWave completeness** (everything IonWave needs, specific)
    - **Cross-Trade generalizability** (works for ANY supplement brand)
    - **Future Studio 3 Trades** (works for ANY D2C Trade, even non-supplement)?

---

## Success Metrics for This System

**Operator Efficiency:**
- **Time to answer "what's next?"** - Target: <10 seconds (ask Claude vs 5-10 min searching docs)
- **Decision confidence** - Target: Operator feels confident on 90%+ of decisions (Claude provides context + SOP)
- **Blocked task resolution time** - Target: <24 hours (Claude flags, Studio 3 responds same-day)

**Studio 3 Oversight Efficiency:**
- **Time to assess Trade status** - Target: <5 min (query Claude vs 30 min digging through Slack/email)
- **Intervention precision** - Target: 0 false alarms (Claude only escalates real issues, not noise)
- **Multi-Trade scalability** - Target: Studio 3 can monitor 5+ Trades without proportional time increase

**System Reliability:**
- **Scorecard accuracy** - Target: 95%+ (Claude-maintained scorecard matches manual audit)
- **API uptime** - Target: 99%+ (daily data ingestion succeeds, fallback to manual if API down)
- **Audit trail completeness** - Target: 100% of decisions logged in `/passets/decisions/`

---

## Next Steps

1. **Document this spec** (DONE)
2. **Enter Q&A mode** - Caio questions Danilo on open questions above
3. **Workshop M40 Navigation** (foundation first)
4. **Workshop M35 Execution Plans** (choreography + timeline)
5. **Workshop M36 Operational Infra** (API integrations + maintenance)
6. **Workshop M37 AI & Automation** (document patterns we built)
7. **Test with IonWave operator** (once hired, validate system works in practice)
8. **Iterate based on operator feedback** (v1 → v2 → canonical)

---

## APPENDIX A: IP Protection Options

**DECISION NEEDED: How important is protecting system IP from operator cloning?**

### The IP Protection Problem

**Core IP to protect:**
- TWP-001 methodology (11-phase workshop protocol)
- OpKits (30+ reusable frameworks)
- CLAUDE_AS_OS_SYSTEM architecture (this document)
- Process documents (00_START_HERE, all processes/, protocols/)

**Operator needs:**
- Claude guidance (ask questions, get task lists, understand what to do next)
- Access to THEIR deliverables (/passets/ionwave/)
- SOPs for execution (how to upload ads, approve CoAs, etc.)

**The tension:** Claude needs full system context to guide operator, but operator working in Claude Code can see/copy ALL files.

---

### Option A: Accept Risk (No IP Protection)

**Approach:** Operator gets full access, we accept they could clone everything.

**Justification:**
- Methodology without execution = worthless (operator can't replicate Studio 3 without doing the work)
- OpKits are examples, not proprietary tech (competitive advantage is DOING it, not HAVING the docs)
- Legal protection via contract (operator signs NDA, non-compete for supplement space)

**Pros:**
- ✅ Simple (no technical barriers)
- ✅ Operator can use Claude Code (best UX)
- ✅ No custom development needed

**Cons:**
- ❌ Operator could clone entire system
- ❌ Could sell to competitors or build competing studio
- ❌ Lost IP leverage if operator leaves

**Recommendation:** If Danilo believes execution >> documentation, this is fine.

---

### Option B: Two-Tier Folder Partition (Partial Protection)

**Approach:** Operator uses claude.ai web (NOT Code), gets Google Drive access to `/passets/ionwave/operator_view/` only. Studio 3 uploads system docs as Claude Project Knowledge (not files).

**Folder structure:**
```
OPERATOR ACCESS (Google Drive shared folder):
/passets/ionwave/operator_view/
  daily_tasks.md
  scorecard_input.md
  escalations.md
  sops/ (read-only)

NO OPERATOR ACCESS (Studio 3 only):
/system/
  00_START_HERE.md
  processes/TWP-001.md
  project_specs/CLAUDE_AS_OS_SYSTEM.md
  data/opkits/ (all 30+ OpKits)
```

**How it works:**
- Studio 3 creates Claude Project with system docs uploaded as Knowledge
- Operator shares this Project (can chat with Claude, can't browse system files)
- Operator gets Drive folder with ONLY their workspace
- Claude generates daily tasks/guidance from system Knowledge (operator sees outputs, not source)

**Pros:**
- ✅ Moderate protection (operator can't bulk clone system files)
- ✅ No custom development (uses native Claude features)
- ✅ Operator still gets full Claude guidance

**Cons:**
- ❌ Operator could screenshot Claude responses (slow IP leak)
- ❌ Knowledge upload limits (may not fit all docs)
- ❌ Web interface less powerful than Code (no file editing, terminal)

**Recommendation:** If Danilo wants "good enough" protection without custom build.

---

### Option C: Custom Operator Interface (Full Protection)

**Approach:** Build thin web app wrapper around Claude API with server-side context loading.

**Architecture:**
```
Operator Interface (custom app):
  ↓ Chat window
  ↓ Asks: "What's next?"
Backend (Node.js + Claude API):
  ↓ Loads system context server-side (operator never sees)
  ↓ Loads operator deliverables from Google Drive
  ↓ Calls Claude API with full context
  ↓ Returns response to operator chat window
```

**Pros:**
- ✅ 100% IP protection (operator never touches system files)
- ✅ Clean chat UX (no file browsing confusion)
- ✅ Multi-tenant ready (same app for multiple Trades)
- ✅ Becomes Studio 3's proprietary operator platform

**Cons:**
- ❌ Requires custom development (~2-3 weeks for MVP)
- ❌ Requires hosting/maintenance (server costs, uptime monitoring)
- ❌ Operator can't work offline
- ❌ More complex to debug/update

**Recommendation:** If Danilo plans multiple Trades and wants long-term platform, worth the investment. If IonWave is one-off experiment, overkill.

---

### Option D: Hybrid Evolution (Phase 1 → Phase 2)

**Approach:** Start with Option B (folder partition + web interface), migrate to Option C (custom app) once model is proven.

**Phase 1 (Week 1-12 IonWave launch):**
- Use Option B (two-tier folders, claude.ai web)
- Validate system works, operator can execute
- Accept minor IP risk during validation

**Phase 2 (Post-PMF, multiple Trades):**
- Build custom operator interface (Option C)
- Migrate proven architecture to proprietary platform
- 100% IP protection for future Trades

**Pros:**
- ✅ Launch fast (no custom build delays IonWave)
- ✅ Validate before investing (don't build platform for unproven model)
- ✅ Evolutionary (folder structure designed for future API wrapping)
- ✅ IP protected where it matters most (proven system for Trades 2-5, not experimental Trade 1)

**Cons:**
- ❌ IonWave operator could clone (but IonWave is validation, not scaling)
- ❌ Requires building custom app later (but only if model succeeds)

**Recommendation:** BEST option if Danilo is uncertain about execution model and wants to validate fast.

---

### Decision Matrix

| Criterion | Option A (Accept Risk) | Option B (Folder Partition) | Option C (Custom App) | Option D (Hybrid) |
|-----------|----------------------|----------------------------|---------------------|------------------|
| **IP Protection** | ❌ None | 🟡 Moderate | ✅ Full | 🟡→✅ (evolves) |
| **Time to Launch** | ✅ Immediate | ✅ 1 week | ❌ 2-3 weeks | ✅ 1 week |
| **Development Cost** | ✅ $0 | ✅ $0 | ❌ $15-30K | ✅→❌ ($0 now, $15-30K later) |
| **Operator UX** | ✅ Best (Code) | 🟡 Good (web) | ✅ Best (custom) | 🟡→✅ (improves) |
| **Multi-Trade Scalable** | 🟡 Manual per Trade | 🟡 Manual per Trade | ✅ Platform | 🟡→✅ (evolves) |
| **Maintenance Burden** | ✅ Low | ✅ Low | ❌ High | ✅→❌ (increases) |

**Caio's recommendation:** **Option D (Hybrid Evolution)** unless Danilo has strong IP concerns, then jump straight to **Option C (Custom App)**.

---

### Open Question for Danilo

**"How important is protecting system IP from operator cloning?"**

**If answer is:**
- **"Not very - execution matters more than docs"** → Use Option A (accept risk)
- **"Moderately - don't want easy bulk clone"** → Use Option B (folder partition)
- **"Critical - this is our competitive moat"** → Use Option C (custom app)
- **"Unsure - let's validate first"** → Use Option D (hybrid evolution)

**This decision affects M35/M40 workshop design** (folder structure, access patterns, query interface architecture).

---

**Status:** ✅ Spec complete, IP protection options documented
**Next:**
1. Get Danilo's answer on IP protection importance
2. Get Danilo's write-up on execution model
3. Then proceed with M40 Navigation workshop
