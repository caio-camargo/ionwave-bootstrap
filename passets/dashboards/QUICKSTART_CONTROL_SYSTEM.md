# Control System Quick Start Guide

**For**: IonWave Operator (Chief of Staff / Founder)
**Purpose**: Get started with the dashboard + controller system in 5 minutes
**Version**: 1.0.0
**Date**: 2026-02-12

---

## What Is This?

The IonWave control system automatically monitors your business health and tells you **exactly what to fix** when something goes wrong.

Think of it like the check engine light in your car, but instead of one vague light, you get:
- **12 specific indicators** (revenue, ROAS, cash, inventory, etc.)
- **Automatic alerts** when something exceeds safe thresholds
- **Step-by-step playbooks** to fix each issue

---

## Your Daily Routine (5 Minutes)

**Every morning at 8:00 AM**:

### Step 1: Open the Dashboard (2 min)
Open `/passets/dashboards/daily_pulse.md`

You'll see:
```
### 💰 Revenue & Orders (Yesterday)
| Metric | Value | vs 7-Day Avg | Status |
|--------|-------|--------------|--------|
| Revenue | $1,247 | +2% | 🟢 |
| Orders | 28 | +5% | 🟢 |
| ROAS | 2.1x | -16% | 🟡 |  ← YELLOW = Watch closely
| Cash Runway | 73 days | — | 🟢 |
```

### Step 2: Check Status Indicators (1 min)
- **🟢 Green**: All good, no action needed
- **🟡 Yellow**: Watch zone, may need action today
- **🔴 Red**: Problem detected, fix immediately

### Step 3: Read "One Thing to Fix Today" (2 min)
Bottom of dashboard shows:
```
### 🎯 One Thing to Fix Today
> ROAS below target (2.1x vs 2.5x). Monitor for creative fatigue.
> If drops below 1.5x, execute RP-005 (ROAS Recovery Protocol).
```

**If all green**: Proceed with your planned work (check `week-X/tasks.md`)

**If any red**: That becomes your #1 priority. Everything else waits.

---

## What Happens When Something Goes Red?

**Example: ROAS drops to 1.3x (below 1.5x threshold)**

### You'll Get:
1. **Email alert** (6:15 AM): "🔴 ROAS Alert: 1.3x (target: 2.5x)"
2. **Slack notification**: "Execute RP-005 (ROAS Recovery Protocol)"
3. **Dashboard update**: "One Thing to Fix Today: ROAS Recovery"

### What You Do:
1. **Open reactive protocol**: `/passets/dashboards/reactive_protocols.md`
2. **Find RP-005**: ROAS Recovery Protocol
3. **Follow the steps**:
   - Step 1: Diagnostic (10 min) → Which campaigns underperforming?
   - Step 2: Pause bottom 30% of campaigns by ROAS
   - Step 3: Launch 3 new creative angles
   - Step 4: Expand audiences
4. **Document what you did**: Log in `/passets/dashboards/controller_logs/RP-005-2026-02-12.md`
5. **Monitor**: Check ROAS tomorrow. If improved, you're done. If still red, continue protocol.

---

## The 3 Core Documents You Need

### 1. Daily Pulse Dashboard (`daily_pulse.md`)
**What**: Your morning health check (5-minute read)
**When**: Every morning at 8:00 AM
**Shows**: Metrics, status indicators (🟢🟡🔴), fires & issues, what to fix today

---

### 2. Reactive Protocols (`reactive_protocols.md`)
**What**: Step-by-step playbooks when red flags appear
**When**: Only when controller fires (dashboard shows 🔴)
**Contains**: 15 protocols (RP-001 through RP-015), one for each type of issue

**Most Common Protocols**:
- RP-001: Revenue Recovery (revenue drops >30%)
- RP-005: ROAS Recovery (ROAS <1.5x)
- RP-006: Ad Spend Pause (ROAS <1.5x for 3+ days) **CRITICAL**
- RP-010: Cash Crisis (runway <30 days) **CRITICAL**
- RP-015: Stockout Prevention (inventory <3 days) **CRITICAL**

---

### 3. Controller Registry (`controller_registry.md`)
**What**: Technical reference - how the system works
**When**: Read once to understand, reference when troubleshooting
**Contains**: 12 controllers, what they monitor, when they trigger

**You rarely need this** - it's the "engine manual" for the system. The dashboard shows you the outputs.

---

## How the System Works (Simple Version)

```
1. DATA SYNC (6:00 AM, automatic)
   APIs (Shopify, Meta, Bank, 3PL) → Google Apps Script → Google Sheet

2. CONTROLLERS RUN (6:05 AM, automatic)
   Read metrics → Compare to thresholds → Detect if out of bounds

3. ALERTS SENT (6:15 AM, automatic)
   If 🔴 Red detected → Email + Slack notification to you

4. YOU ACT (8:00 AM, manual)
   Read dashboard → Execute reactive protocol if red → Log outcome

5. META-CONTROL LEARNS (Quarterly, MSO + CM)
   Review logs → Tune thresholds → Improve system
```

---

## Status Indicator Meanings

### 🟢 Green = Healthy
- Revenue: Within ±15% of 7-day average
- ROAS: >2.5x
- CPA: <$45
- Cash Runway: >60 days
- Inventory: >14 days supply

**Action**: None. System operating normally.

---

### 🟡 Yellow = Watch Zone
- Revenue: -15% to -30% vs 7-day average
- ROAS: 1.5x - 2.5x
- CPA: $45-60
- Cash Runway: 30-60 days
- Inventory: 7-14 days supply

**Action**: Flag for review. May need action today. Monitor closely.

---

### 🔴 Red = Problem
- Revenue: <-30% vs 7-day average OR <$100/day
- ROAS: <1.5x
- CPA: >$60
- Cash Runway: <30 days
- Inventory: <7 days supply

**Action**: Execute reactive protocol immediately. This is your #1 priority.

---

## Example Scenarios

### Scenario 1: All Green (Normal Day)
**Dashboard shows**:
- Revenue: $1,247 (+2%) 🟢
- ROAS: 2.7x 🟢
- Cash: 73 days 🟢

**What you do**: Nothing dashboard-related. Proceed with planned work from `week-X/tasks.md`.

**Time spent**: 5 minutes (dashboard review only)

---

### Scenario 2: Yellow Flag (Warning)
**Dashboard shows**:
- Revenue: $1,050 (-18%) 🟡  ← YELLOW
- ROAS: 2.3x 🟡  ← YELLOW
- Cash: 73 days 🟢

**What you do**:
- Note the yellow flags
- Monitor closely today
- If ROAS drops further tomorrow (to 🔴), execute RP-005
- If revenue stays yellow for 3+ days, investigate (likely related to ROAS)

**Time spent**: 10 minutes (dashboard + brief review of ad performance)

---

### Scenario 3: Red Flag (Action Required)
**Dashboard shows**:
- Revenue: $850 (-32%) 🔴  ← RED
- ROAS: 1.3x 🔴  ← RED
- Cash: 73 days 🟢

**What you do**:
1. **Read alert**: Email says "Execute RP-001 (Revenue Recovery) and RP-005 (ROAS Recovery)"
2. **Prioritize**: ROAS is likely causing revenue drop → Fix ROAS first
3. **Execute RP-005** (2-4 hours):
   - Pause underperforming campaigns
   - Launch new creatives
   - Expand audiences
4. **Monitor**: Check ROAS tomorrow
5. **Log**: Document in `controller_logs/RP-005-2026-02-12.md`

**Time spent**: 2-4 hours (fixing the issue) + 5 min dashboard tomorrow (check if resolved)

---

## Critical Protocols (High Priority)

### RP-006: Ad Spend Pause (CRITICAL)
**Trigger**: ROAS <1.5x for 3+ consecutive days
**What it does**: Immediately reduce ad spend by 80% to stop cash burn
**Urgency**: P0 (execute within 1 hour)
**Authority**: Requires CM + Studio 3 approval

---

### RP-010: Cash Crisis (CRITICAL)
**Trigger**: Cash runway <30 days
**What it does**: Emergency expense cuts + revenue acceleration + fundraising plan
**Urgency**: P0 (decision within 24 hours)
**Authority**: Operator + CM + Studio 3

---

### RP-011: Existential Cash Protocol (CRITICAL)
**Trigger**: Cash runway <14 days
**What it does**: Emergency meeting, decision to fundraise / fire sale / wind down
**Urgency**: P0 (decision within 48 hours)
**Authority**: Studio 3 + Venture Partner

---

### RP-015: Stockout Prevention (CRITICAL)
**Trigger**: Inventory <3 days supply
**What it does**: Pause ad spend, set up waitlist, emergency supplier escalation
**Urgency**: P0 (immediate action)
**Authority**: Operator (executes immediately)

---

## FAQ

**Q: What if the dashboard shows a red flag but I think it's wrong?**
A: Check the data source (Shopify, Meta, Bank). If data is correct, the flag is valid. If data sync failed, fix the sync and re-run controller. Document in controller_logs/ so Meta-Control can adjust thresholds if needed.

**Q: What if I'm too busy to execute a reactive protocol today?**
A: **Don't ignore red flags.** They indicate business-threatening issues. If you can't execute, escalate to CM immediately. Yellow flags can wait, red flags can't.

**Q: How do I know if a reactive protocol worked?**
A: Check the dashboard the next day. If status returns to 🟡 Yellow or 🟢 Green, the protocol worked. If still 🔴 Red, continue protocol or escalate to CM.

**Q: What if a yellow flag stays yellow for a week?**
A: That's a structural issue, not a daily fluctuation. Escalate to CM for root cause analysis. The system may need parameter tuning.

**Q: Can I turn off controllers if they're too noisy?**
A: No. Controllers protect the business. If you're getting too many false positives, report to CM → Meta-Control will tune thresholds quarterly. Don't ignore alerts.

**Q: What happens during the data sync at 6:00 AM?**
A: Google Apps Script fetches data from Shopify, Meta, Bank, 3PL APIs and writes to Google Sheet. Controllers read from Sheet and update dashboard. If sync fails, you'll get an email alert to manually update.

---

## Getting Help

**Dashboard questions**: Read `control_system_overview.md` (detailed architecture)

**Protocol execution issues**: Log in `/passets/decisions/decision_log.md`, tag CM

**False positives / System improvements**: Report to CM → Meta-Control will review quarterly

**Urgent escalations**:
- 🔴 Red flag you can't handle → Alert CM immediately
- P0 protocols (RP-006, RP-010, RP-011, RP-015) → Alert CM + Studio 3

---

## Your Action Checklist

**Before Launch** (Week 1-4):
- [ ] Familiarize with daily_pulse.md format
- [ ] Read all 15 reactive protocols (skim, know what exists)
- [ ] Test data pipeline (run Google Apps Script once manually)
- [ ] Set up email alerts (Gmail filter for controller notifications)

**Week 1 of Launch**:
- [ ] Check dashboard daily at 8:00 AM
- [ ] Expect mostly 🟢 Green (new ads, fresh audience)
- [ ] Document any yellow/red flags in controller_logs/

**Weeks 2-4 of Launch**:
- [ ] Continue daily dashboard checks
- [ ] You'll likely see first 🟡 Yellow flags (creative fatigue around Day 14-21)
- [ ] Execute reactive protocols as needed
- [ ] Report any false positives to CM

**Month 2+**:
- [ ] Dashboard becomes muscle memory (3-min review)
- [ ] You'll recognize patterns ("ROAS drops Friday, recovers Monday = weekend variance, not red flag")
- [ ] Proactive actions reduce red flags (creative refresh before fatigue, reorder before stockout)

---

## Version History

**v1.0.0 (2026-02-12)**:
- Initial quick start guide
- 5-minute daily routine documented
- Status indicator meanings explained
- Example scenarios illustrated
- Critical protocols highlighted
- FAQ added

---

## Next: Read the Full System

Once you're comfortable with the daily routine, read:
1. **control_system_overview.md** — How controllers work, Meta-Control process, system maturity roadmap
2. **controller_registry.md** — Technical details of each controller
3. **parameter_registry.md** — Numeric thresholds, why they were chosen, how they evolve

But you don't need those to get started. This quick start guide + daily_pulse.md + reactive_protocols.md are enough for daily operations.

**Ready? Open daily_pulse.md and start your first 5-minute check.**
