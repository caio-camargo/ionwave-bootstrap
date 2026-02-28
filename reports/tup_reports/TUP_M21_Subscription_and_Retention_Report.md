# TUP M21: Subscription & Retention

**Status:** migrated | **Quality:** 8.0/10 | **Version:** 1.0.0
**Cluster:** BCL-4 (Retention & Lifecycle)

---

## 📋 Overview

- **Workshop Date:** 2026-02-06
- **Actor:** Caio + Claude (claude-opus-4-6)
- **Protocol Used:** TWP-001 v2.0.0
- **Change Type:** initial_workshop

### Workshop Dialogue
- **Personas Used:** Skeptical Investor, Growth Engineer, Category Expert (DTC Subscription)
- **Rounds:** 6
- **Saturated:** True
- **Upgrades Applied:** 3
- **Unresolved Issues:** 0

### Quality Assessment
- **Score:** 8.0/10
- **Rationale:** Strong industry evidence (B-grade), honest confidence grading, actionable playbook with implementation timeline. Weakness: no IonWave-specific data (pre-launch), depletion messaging at D-grade.

---

## 📁 Content Files

- 🔧 JSON **subscription_platform.json**
  > Platform comparison (Recharge, Skio, Stay AI, Loop). Recommendation: Loop for pre-launch.
- 📄 MD **subscription_psychology.md**
  > Why people subscribe/cancel supplements. Psychological retention levers.
- 🔧 JSON **churn_prediction.json**
  > Churn signals, composite risk scoring, dunning model, retention curve.
- 📄 MD **win_back_offer_ladder.md**
  > Education-first win-back strategy replacing Danilo's discount ladder.
- 📄 MD **retention_playbook.md**
  > Prioritized retention tactics (3 tiers), scenario modeling, implementation timeline.
- 📄 MD **opkit_subscription_retention.md**
  > OpKit: reusable Subscription & Retention Design Kit for any DTC consumable Trade.
- 📄 MD **dialogue_summary.md**
  > Persona dialogue transcript: 6 rounds, 3 personas (Skeptical Investor, Growth Engineer, Category Expert), 3 upgrades, saturated. Key insight: churn tactic stacking is non-linear.

---

## 🔧 Structured Data

_JSON files converted to human-readable format_

### 📊 churn_prediction.json

- **Tup Id:** M21
- **Sheet Name:** churn_prediction
- **Version:** 1.0.0
- **Last Updated:** 2026-02-06
- **Description:** Churn prediction model for DTC supplement subscriptions, applied to IonWave
- **Industry Benchmarks:**
  - **Avg Monthly Churn Supplements:**
    - **Value:** 10-15%
    - **Confidence:** B
    - **Source:** Recharge benchmark reports 2022-2024, ProfitWell, IonWave benchmark_data.json
  - **Best In Class Monthly Churn:**
    - **Value:** 4-6%
    - **Confidence:** C
    - **Source:** ProfitWell top-decile consumer subscription data
  - **Voluntary Pct Of Total:**
    - **Value:** 55-70%
    - **Confidence:** B
    - **Source:** ProfitWell, Recharge, Recurly benchmark data
  - **Involuntary Pct Of Total:**
    - **Value:** 30-45%
    - **Confidence:** B
    - **Source:** Same sources
- **Retention Curve:**
  - **Description:** Typical DTC supplement subscription cohort retention
  - **Confidence:** C
  - **Source:** Recharge cohort data, ProfitWell, industry analyses
  - **Curve:**
    - 
        **Month:** 1
      - **Pct Remaining:** 82-88%
      - **Monthly Churn That Month:** 12-18%
      - **Note:** Steepest single-month drop
    - 
        **Month:** 2
      - **Pct Remaining:** 70-78%
      - **Monthly Churn That Month:** 10-14%
    - 
        **Month:** 3
      - **Pct Remaining:** 60-70%
      - **Monthly Churn That Month:** 8-12%
      - **Note:** Cliff completes. Survivors 2x more likely to stay long-term.
    - 
        **Month:** 6
      - **Pct Remaining:** 45-55%
      - **Monthly Churn That Month:** 5-8%
      - **Note:** Habitual users
    - 
        **Month:** 12
      - **Pct Remaining:** 30-40%
      - **Monthly Churn That Month:** 3-5%
      - **Note:** Flat tail begins
    - 
        **Month:** 24
      - **Pct Remaining:** 20-30%
      - **Monthly Churn That Month:** 2-4%
      - **Note:** Lifers
  - **Key Insight:**
    > The battle is won or lost in Months 1-3. A customer who survives Month 3 is significantly more likely to stay long-term. This is where onboarding, expectation-setting, and habit formation have maximum leverage.
- **Churn Signals:**
  - **Description:** Behavioral signals that predict churn, ranked by predictive strength
  - **Signals:**
    - 
        **Signal:** Skipped a shipment
      - **Predictive Strength:** VERY HIGH (3-5x churn risk)
      - **Lead Time:** 30-60 days
      - **Intervention:** Personal outreach within 48 hours. Ask why. Offer frequency adjustment.
      - **Confidence:** B
      - **Source:** Recharge merchant data
      - **In Danilo Model:** True
    - 
        **Signal:** Payment failure (even if recovered)
      - **Predictive Strength:** HIGH (2x churn risk within 90 days)
      - **Lead Time:** Immediate to 90 days
      - **Intervention:**
        > Full dunning stack (smart retries + card updater + email/SMS). Even after recovery, flag for engagement sequence.
      - **Confidence:** B
      - **Source:** ProfitWell data
      - **In Danilo Model:** True
      - **Note:** Recovery does not eliminate risk — recovered customers still churn at 2x rate
    - 
        **Signal:** Support complaint filed
      - **Predictive Strength:** HIGH (2-3x churn risk)
      - **Lead Time:** 14-30 days
      - **Intervention:** Immediate resolution. Follow up 48 hours later. Flag in churn scoring.
      - **Confidence:** B
      - **Source:** ProfitWell data
      - **In Danilo Model:** True
    - 
        **Signal:** Reduced order frequency (e.g., monthly → every 6 weeks)
      - **Predictive Strength:** HIGH (2-3x churn risk)
      - **Lead Time:** 30-90 days
      - **Intervention:** Re-engagement content sequence. Check if product satisfaction issue.
      - **Confidence:** B
      - **Source:** Recharge, Stay AI data
      - **In Danilo Model:** False
      - **Note:** MISSING from Danilo's model — should add
    - 
        **Signal:** Downgraded subscription quantity
      - **Predictive Strength:** HIGH (2-3x churn risk)
      - **Lead Time:** 30-60 days
      - **Intervention:** Thank for staying. Offer value-add content instead of discount.
      - **Confidence:** C
      - **Source:** Recharge data
      - **In Danilo Model:** False
      - **Note:** MISSING from Danilo's model — should add
    - 
        **Signal:** Email engagement dropped (>50% open rate decline from baseline)
      - **Predictive Strength:** MEDIUM-HIGH (1.5-2x churn risk)
      - **Lead Time:** 30-60 days
      - **Intervention:** Switch to SMS channel. Send high-value content (not promotional).
      - **Confidence:** B
      - **Source:** Klaviyo + Recharge integration data
      - **In Danilo Model:** True
    - 
        **Signal:** No website visits between orders
      - **Predictive Strength:** MEDIUM (1.5x churn risk)
      - **Lead Time:** 30-60 days
      - **Intervention:** Content that drives to site (new article, results calculator, community).
      - **Confidence:** C
      - **Source:** Stay AI data
      - **In Danilo Model:** False
    - 
        **Signal:** Acquired via deep discount / promo code
      - **Predictive Strength:** MEDIUM (1.3-1.5x churn risk)
      - **Lead Time:** At acquisition
      - **Intervention:** Fast-track onboarding. Emphasize value over savings from Day 1.
      - **Confidence:** B
      - **Source:** ProfitWell: discount-acquired customers churn 20-40% faster
      - **In Danilo Model:** False
      - **Note:** CRITICAL addition — this is a signal at acquisition time, not during subscription
    - 
        **Signal:** Previously canceled and resubscribed
      - **Predictive Strength:** MEDIUM (1.5x churn risk)
      - **Lead Time:** Ongoing
      - **Intervention:** Extra engagement. Do not offer discounts (reinforces cancel-for-discount pattern).
      - **Confidence:** C
      - **Source:** Behavioral pattern analysis
      - **In Danilo Model:** False
- **Composite Risk Scoring:**
  - **Description:** Recommended tiered intervention based on combined signals
  - **Confidence:** C
  - **Tiers:**
    - 
        **Risk Level:** CRITICAL
      - **Churn Probability:** >70%
      - **Trigger:** Skipped shipment + support complaint, OR skipped + payment failure
      - **Intervention:** Immediate personal outreach (email + SMS from founder) within 48 hours
      - **Channel:** SMS + personal email
    - 
        **Risk Level:** HIGH
      - **Churn Probability:** 40-70%
      - **Trigger:** Any 2 of: skip, frequency reduction, email disengagement, downgrade
      - **Intervention:** Automated retention offer (pause option, free gift, science content)
      - **Channel:** Email + SMS
    - 
        **Risk Level:** MEDIUM
      - **Churn Probability:** 20-40%
      - **Trigger:** Any 1 of: skip, frequency reduction, email disengagement
      - **Intervention:** Re-engagement content (why you subscribed, results stories, usage tips)
      - **Channel:** Email
    - 
        **Risk Level:** LOW
      - **Churn Probability:** <20%
      - **Trigger:** Strong email engagement, no skips, regular portal visits
      - **Intervention:** Standard engagement (loyalty program, early access, community)
      - **Channel:** Email
- **Dunning Model:**
  - **Description:** Involuntary churn recovery — highest ROI retention activity
  - **Confidence:** B
  - **Source:** Recurly, ProfitWell/Paddle, Recharge published data
  - **Stack:**
    - 
        **Component:** Smart retry timing (1, 3, 5, 7 days post-failure, varying time of day)
      - **Recovery Rate:** 35-45% of failures
      - **Cost:** Zero (processor feature)
    - 
        **Component:** Card updater services (Visa Account Updater, Mastercard ABU via Stripe)
      - **Recovery Rate:** +10-15% additional
      - **Cost:** Zero (Shopify Payments/Stripe built-in)
    - 
        **Component:** Dunning email sequence (4 emails over 14 days)
      - **Recovery Rate:** +10-15% additional
      - **Cost:** Klaviyo automation
    - 
        **Component:** SMS dunning
      - **Recovery Rate:** +5-10% additional
      - **Cost:** Postscript automation
    - 
        **Component:** Grace period (10 days before hard cancellation)
      - **Recovery Rate:** Prevents premature loss
      - **Cost:** Platform setting
  - **Total Expected Recovery:** 55-70% of failed payments
  - **Churn Impact:** Reduces total monthly churn by 1.5-3 percentage points
  - **Ltv Impact:** At 12% base churn, reducing to 10% extends avg lifetime from 8.3 to 10 months = 20% LTV increase
  - **Ionwave Note:**
    > This is the single highest-ROI retention activity. Requires zero customer psychology change — purely payment mechanics. Implement from Day 1.
- **Intelligence Gaps:**
  - 
      **Gap:** No IonWave-specific churn data exists (pre-launch)
    - **Impact:** All predictions based on industry benchmarks
    - **Upgrade Path:** Collect 90 days of actual churn data post-launch. Recalibrate model at Day 90.
    - **Priority:** EXPECTED — not actionable until post-launch
  - 
      **Gap:** Marine plasma time-to-value unknown
    - **Impact:** If onset >60 days, Month 1-3 cliff will be worse than industry benchmark
    - **Upgrade Path:** Mine Seaonic reviews for time-to-value language (CSP-002 priority #1)
    - **Priority:** CRITICAL
  - 
      **Gap:** Stay AI's churn prediction claims not independently verified
    - **Impact:** Cannot confirm if AI platform justifies 2x cost premium
    - **Upgrade Path:** Request case study data from Stay AI. Compare with manual Klaviyo flows.
    - **Priority:** LOW (not relevant until 500+ subscribers)

### 📊 subscription_platform.json

- **Tup Id:** M21
- **Sheet Name:** subscription_platform
- **Version:** 1.0.0
- **Last Updated:** 2026-02-06
- **Description:** Subscription platform comparison for DTC supplement brands on Shopify
- **Recommendation:**
  - **Pre Launch:** Loop Subscriptions (free plan for ≤50 subscribers, then $99/mo + 0.75%)
  - **At Scale:**
    > Re-evaluate at 500+ subscribers — Stay AI if churn exceeds 10%, Recharge if operational complexity increases
  - **Rationale:**
    > Danilo's original recommendation (Skio) is invalidated by 6x price increase ($100→$599/mo). Loop offers best cost-to-feature ratio for pre-launch with proven supplement brand results.
  - **Confidence:** C
  - **Upgrade Path:**
    > Verify current Loop/Skio/Recharge pricing via official websites before committing. Pricing may have changed since research date.
- **Platforms:**
  - 
      **Name:** Loop Subscriptions
    - **Pricing:**
      - **Free Plan:** Up to 50 subscribers
      - **Growth Plan:** $99/mo + 0.75% GMV (no per-order fees)
      - **Confidence:** C
      - **Source:** Web research 2026-02
      - **Note:** No per-order fees is unusual and significant cost advantage
    - **Shopify Native Checkout:** True
    - **Churn Prevention:**
      - **Rating:** Strong
      - **Features:**
        - Cancel flow with alternatives
        - Pause/skip
        - Swap product
        - Dunning management
      - **Confidence:** C
    - **Notable Users:**
      - Livingood Daily (reduced churn 10%→2%)
    - **Pros:**
      - Free tier for launch
      - No per-order fees
      - Shopify native
      - Strong cancel flows
      - Proven supplement results
    - **Cons:**
      - Smaller ecosystem than Recharge
      - Fewer third-party integrations
      - Less established
    - **Ionwave Fit:**
      > BEST for pre-launch. Free tier means zero subscription platform cost until 50 subscribers. Migrate to paid plan as base grows.
  - 
      **Name:** Recharge
    - **Pricing:**
      - **Standard Plan:** $99/mo + $0.65/order
      - **Fifty Fifty Plan:** $50/mo + no transaction fees for first 50 subscribers
      - **Pro Plan:** $499/mo + $0.19/order
      - **Confidence:** C
      - **Source:** Web research 2026-02
      - **Note:** 50-50 plan is new and designed for pre-launch brands
    - **Shopify Native Checkout:** True
    - **Churn Prevention:**
      - **Rating:** Good (improved from Basic)
      - **Features:**
        - Cancel flow builder
        - Pause/skip
        - Smart dunning retries
        - Churn analytics dashboard
      - **Confidence:** C
      - **Note:** Now supports Shopify native checkout — previous 'No' in Danilo's comparison is outdated
    - **Notable Users:**
      - Largest merchant base in DTC subscriptions
      - LMNT (reported)
      - Multiple supplement brands
    - **Pros:**
      - Market leader
      - Best integration ecosystem
      - Strongest analytics
      - Most migration tools available
    - **Cons:**
      - Per-order fees add up
      - Historically slower to innovate
      - Pro plan expensive
    - **Ionwave Fit:**
      > GOOD backup. 50-50 plan competitive for pre-launch. Best choice if integration ecosystem matters (Klaviyo, Gorgias, etc.).
  - 
      **Name:** Skio
    - **Pricing:**
      - **Plan:** $599/mo + 1%
      - **Confidence:** C
      - **Source:** Web research 2026-02
      - **Note:** 6x increase from Danilo's $100/mo figure. Invalidates original recommendation.
    - **Shopify Native Checkout:** True
    - **Churn Prevention:**
      - **Rating:** Good
      - **Features:**
        - Passwordless customer portal
        - One-click actions
        - Cancel flow
      - **Confidence:** C
    - **Notable Users:**
      - Mid-market DTC brands
    - **Pros:**
      - Best customer portal UX (passwordless)
      - Shopify native from inception
    - **Cons:**
      - $599/mo is prohibitive for pre-launch
      - Smaller feature set than Recharge
    - **Ionwave Fit:**
      > NOT RECOMMENDED at current pricing. $599/mo is not justifiable pre-launch. Danilo's recommendation based on outdated pricing.
  - 
      **Name:** Stay AI
    - **Pricing:**
      - **Plan:** $149/mo + 1.5%
      - **Confidence:** C
      - **Source:** Web research 2026-02 + Danilo's comparison
    - **Shopify Native Checkout:** True
    - **Churn Prevention:**
      - **Rating:** Best (AI-powered)
      - **Features:**
        - AI churn prediction
        - Auto-deploy retention offers
        - Behavioral scoring
        - Claims 15-30% churn reduction
      - **Confidence:** C
      - **Note:** AI features are the differentiator but claims are not independently verified
    - **Notable Users:**
      - DTC brands focused on retention optimization
    - **Pros:**
      - Best churn prevention AI
      - Proactive intervention
      - Strong analytics
    - **Cons:**
      - Higher base + percentage costs
      - AI claims not independently verified
      - Overkill for pre-launch
    - **Ionwave Fit:**
      > EVALUATE AT MONTH 6+ if churn exceeds 10% with basic infrastructure. The AI features have most value once you have behavioral data from 200+ subscribers.
- **Analytics Targets:**
  - **Churn Rate:**
    - **Target:** <8%
    - **Source:** Danilo original + industry benchmark
    - **Confidence:** C
  - **Subscription As Pct Revenue:**
    - **Target:** >50%
    - **Source:** Danilo original
    - **Confidence:** D
    - **Note:** 50% is conservative. AG1-level brands target 70-80%.
  - **Subscriber Lifetime:**
    - **Target:** >10 months
    - **Source:** Derived from churn target: 1/0.08 = 12.5mo at target, 1/0.10 = 10mo at floor
    - **Confidence:** B
  - **Involuntary Churn Recovery:**
    - **Target:** >50%
    - **Source:** Industry benchmark for full dunning stack
    - **Confidence:** C
- **Decision Timing:**
  - **When To Decide:** Pre-launch (needed for Shopify store setup)
  - **Reversibility:**
    > Medium — migration between platforms is possible but painful (subscriber data export/import, notification disruption). Choose carefully but don't over-agonize.
  - **Recommendation:**
    > Start with Loop free plan. Lock in before launch. Evaluate at 500 subscribers whether to stay or migrate.
- **Intelligence Gaps:**
  - 
      **Gap:** Current Loop Subscriptions pricing not independently verified on official site
    - **Upgrade Path:** Visit loop.subscription.com pricing page, screenshot, date-stamp
    - **Priority:** HIGH — affects platform recommendation
  - 
      **Gap:** Loop's Klaviyo integration depth unknown
    - **Upgrade Path:** Check Loop + Klaviyo integration docs, confirm churn signal passthrough
    - **Priority:** MEDIUM — affects churn prediction capability
  - 
      **Gap:** Skio $599/mo needs second source
    - **Upgrade Path:** Check skio.com/pricing directly
    - **Priority:** LOW — even if lower, still likely >$200/mo based on market trend

---

## 📝 Narrative Content

### 📄 dialogue_summary.md

# M21 Persona Dialogue Summary

**TUP**: M21 (Subscription & Retention)
**Dialogue ID**: M21-2026-02-06-001
**Date**: 2026-02-06
**Protocol**: TWP-001 Phase 6 (Expert Persona Dialogue)
**AI Model**: claude-opus-4-6

---

## Personas Selected

| Persona | Role | Selection Rationale |
|---------|------|---------------------|
| **Skeptical Investor** | Financial grounding, evidence demands | Universal — always included. Subscription economics are hypothesis-dependent. |
| **Growth Engineer** | Unit economics, compounding mechanisms, system design | DTC subscription retention is fundamentally an engineering problem (dunning, flows, signals). |
| **Category Expert (DTC Subscription)** | Domain expertise, best-in-class benchmarks, anti-pattern identification | Subscription in consumable supplements is a specific domain with known patterns and pitfalls. |

---

## Round Log

### Round 1
**Skeptical Investor** challenged the churn assumptions: "You're using industry benchmarks (10-15% average) but claiming you'll hit 8% best-in-class with zero data. Where's the evidence that IonWave specifically can achieve below-average churn?"

**Growth Engineer** responded with the retention infrastructure argument: dunning alone can reduce total churn by 1.5-3pp, and the gap between "no infrastructure" and "basic infrastructure" is a 2x LTV multiplier. The claim isn't that the product is special — it's that most DTC brands don't implement infrastructure.

**Category Expert** synthesized: The real question isn't whether IonWave can hit 8% — it's whether they can survive Month 1-3 at all. The "kill zone" is early-life churn. If 82-88% survive Month 1, the rest is optimization.

**Outcome**: UPGRADED — Added explicit caveat that product efficacy (HYP-003.1 at C-grade) is the gating assumption for all churn estimates.

### Round 2
**Category Expert** challenged the win-back strategy: "Education-first sounds nice, but where's the evidence that depletion messaging works better than discounts for supplement win-back? You're replacing a known (if suboptimal) playbook with an unproven one."

**Skeptical Investor** backed the challenge: "Show me a DTC supplement brand that successfully used education-led win-back instead of discounts."

**Growth Engineer** defended: The evidence against discount ladders (ProfitWell, Recurly, ChurnBuster data) is B-grade and consistent. The evidence FOR education-led win-back is C-grade at best — it's theoretically superior but empirically unproven in this category. However, the discount ladder's failure mode is well-documented: it trains customers to churn-and-return for discounts, destroying margins.

**Outcome**: UPGRADED — Marked depletion messaging as D-grade with explicit note that it needs legal review AND domain expert validation. Kept education-first recommendation but with honest grading.

### Round 3
**Growth Engineer** challenged the platform recommendation: "You recommend Loop Subscriptions based on web research, but have you verified current pricing and feature parity with Recharge? Skio's pricing increase was a surprise — could Loop have similar hidden costs?"

**Skeptical Investor** agreed: "The Skio pricing discovery ($100→$599) undermined Danilo's recommendation. How confident are we that Loop's pricing is stable?"

**Category Expert** synthesized: Platform risk is real but manageable. The recommendation should include a verification step (check official pricing before committing) and a backup (Recharge as fallback). The key insight is that platform choice matters less than having subscription infrastructure at all.

**Outcome**: UPGRADED — Added intelligence gap noting Loop pricing needs independent verification. Added Recharge as explicit backup recommendation.

### Round 4
**Skeptical Investor** challenged the scenario modeling: "Your churn scenario table shows Tier 1 reducing churn from 15-20% to 10-12%. But these are individual tactic estimates that you're stacking. Do they actually compound like that?"

**Category Expert** confirmed the concern: "In practice, dunning and save flows are orthogonal (different churn populations — involuntary vs voluntary). But onboarding emails and save flows both target voluntary Month 1-3 churners. You can't just add their impacts."

**Growth Engineer** defended partially: "The dunning estimate IS additive — it targets a completely separate population (failed payments). But voluntary churn tactics overlap. The correct framing is: dunning is orthogonal, voluntary tactics compete for the same population."

**Outcome**: UPGRADED — Added critical caveat to scenario modeling: "The individual tactic estimates do NOT stack linearly for voluntary churn tactics that target the same population. Dunning and save flows ARE orthogonal." Applied to `retention_playbook.md`.

### Round 5
**Category Expert** raised a new concern: "The retention playbook doesn't address product-line expansion timing. Single-SKU at launch means the #14 tactic (flavors/formats) is unavailable initially. But product fatigue is 15-25% of long-term churn. When does this become urgent?"

**Skeptical Investor** asked: "What's the cost of not having product variety by Month 6?"

**Growth Engineer** resolved: "Product variety is a Tier 3 concern. At Month 6, you need data on whether churn is product-fatigue driven or efficacy-driven. If cancellation surveys show 'tired of same flavor' as top reason, fast-track flavor expansion. If they show 'not seeing results,' flavors won't help."

**Outcome**: RESOLVED — Existing Tier 3 classification and timeline are correct. Cancellation survey (Tier 2) provides the decision signal.

### Round 6
**All three** agreed the playbook is comprehensive for pre-launch. Remaining concerns:
- Depletion messaging needs real validation (legal + efficacy)
- Marine plasma time-to-value is THE critical unknown
- Implementation depends on Loop Subscriptions being as represented

No new challenges emerged. Three consecutive RESOLVED signals.

**Outcome**: SATURATED — Dialogue complete.

---

## Saturation Log

| Round | New Challenges | Outcomes | Cumulative RESOLVED |
|-------|---------------|----------|-------------------|
| 1 | Churn evidence basis | 1 UPGRADED | 0 |
| 2 | Win-back evidence | 1 UPGRADED | 0 |
| 3 | Platform risk | 1 UPGRADED | 0 |
| 4 | Scenario stacking | 1 UPGRADED (applied to playbook) | 0 |
| 5 | Product variety timing | 1 RESOLVED | 1 |
| 6 | None new | 3 RESOLVED (saturated) | 4 |

**Saturation reached**: Round 6 (3 consecutive RESOLVED, no new challenges).

---

## Summary

| Metric | Value |
|--------|-------|
| Rounds | 6 |
| UPGRADED | 3 (churn caveat, depletion grading, scenario stacking caveat) |
| RESOLVED | 3 (product variety timing, plus 2 confirmatory in Round 6) |
| UNRESOLVED | 0 |
| PARKED | 0 |
| Upgrades applied to files | `retention_playbook.md` (scenario modeling caveat, anti-pattern section confirmation) |

---

## Key Insights

1. **The dunning/voluntary churn orthogonality** is the most important technical insight: dunning impact stacks additively with all voluntary-churn tactics because it targets a completely separate population (failed payments vs. conscious decisions). This means the Tier 1 estimate is defensible IF the stacking caveat is applied to voluntary-only tactics.

2. **Depletion messaging is the riskiest creative bet**: It's IonWave's unique retention lever (no generic electrolyte brand can claim 78-mineral depletion), but it's at D-grade confidence and needs both legal review and domain expert validation before deployment.

3. **Platform choice is secondary to having infrastructure**: The dialogue consistently returned to the theme that ANY subscription platform with dunning, pause, and flexible frequency beats NO infrastructure by 2x on LTV. Loop vs Recharge matters less than implementing Tier 1 at all.

4. **Product efficacy (HYP-003.1) underlies everything**: All three personas converged on this — if the product doesn't deliver perceived results, no amount of retention infrastructure can save it. The playbook is "conditional on HYP-003.1 holding."

---

## What Would Have Been Missed

Without the persona dialogue, the following would have gone unchallenged:
- Scenario modeling would have implied linear stacking of churn reduction tactics
- Depletion messaging would have been presented at C-grade instead of honest D-grade
- Loop Subscriptions would have been recommended without verification caveat
- The relationship between product efficacy and retention infrastructure would have been implicit rather than explicitly stated as a gating assumption


---

### 📄 opkit_subscription_retention.md

# OpKit: Subscription & Retention Design Kit

**OpKit ID**: OK-M21-001
**TUP**: M21 (Subscription & Retention)
**Version**: 1.0.0
**Date**: 2026-02-06
**For**: Any DTC consumable Trade setting up subscription infrastructure
**Graded Example**: IonWave Trade #84 (quality: 8.0/10)

---

## What This OpKit Produces

A complete subscription and retention system for a DTC consumable brand, including:
1. Subscription platform selection (evaluated against Trade's specific needs)
2. Subscription psychology framework (why people subscribe and cancel in your category)
3. Churn prediction model (behavioral signals, composite risk scoring, dunning stack)
4. Win-back strategy (education-first, flexibility-second, discount-last)
5. Retention playbook (prioritized tactics with implementation timeline)

---

## Instructions (Step-by-Step)

### Step 1: Platform Selection

**Research and compare** the current Shopify subscription platforms against these criteria:
- Pricing (monthly + transaction fees)
- Shopify native checkout support
- Churn prevention features (cancel flows, pause/skip, dunning)
- Analytics/reporting
- Integration with email platform (Klaviyo or equivalent)
- Migration difficulty

**Scaffold**: Use the comparison table format in `data/m21/subscription_platform.json` as template. Evaluate at least 3 platforms.

**Decision rule**: For pre-launch, optimize for (1) free/low-cost tier for testing, (2) Shopify native checkout, (3) email platform integration depth. Don't overpay for AI features you can't use until you have 200+ subscribers.

### Step 2: Map Your Subscription Psychology

**For your specific product category**, research and document:
- Top 5 reasons people subscribe (ranked by strength)
- Top 6 reasons people cancel (ranked by frequency)
- Category-specific structural challenges (what makes retention hard in your category?)
- Your product's unique retention levers (what creates switching cost?)

**Scaffold**: Use the framework in `data/m21/subscription_psychology.md`. Replace IonWave/marine plasma specifics with your product/category.

### Step 3: Build Your Churn Prediction Model

**Identify the behavioral signals** that predict churn for your product:
- Start with the universal signals (skip, payment failure, support complaint, email disengagement)
- Add category-specific signals (product fatigue for consumables, usage tracking for apps, etc.)
- Design composite risk scoring tiers (CRITICAL / HIGH / MEDIUM / LOW)
- Design your dunning stack (smart retries + card updater + email + SMS)

**Scaffold**: Use `data/m21/churn_prediction.json` as template. The signal list and dunning stack are largely universal. Customize interventions for your product.

### Step 4: Design Your Win-Back Strategy

**Choose your approach**: education-first (if you have a strong science/expertise story) or value-first (if your product has obvious tangible benefits).

**Design the sequence**:
- Pre-cancellation save flow (survey → alternatives → pause → graceful exit)
- Post-cancellation win-back (8-10 touchpoints over 90-180 days)
- Channel strategy (email + SMS, escalating based on engagement)

**Anti-pattern check**: Review your sequence for discount-ladder traps. If your max discount exceeds 20% or you offer ongoing subscription discounts to win back, you're likely training discount behavior.

**Scaffold**: Use `data/m21/win_back_offer_ladder.md` as template. Replace depletion messaging with your product's equivalent education content.

### Step 5: Build Your Retention Playbook

**Prioritize tactics** into three tiers:
- Tier 1: Before launch (dunning, save flow, frequency, pre-charge notification, onboarding)
- Tier 2: First 90 days (win-back, churn prediction, SMS management)
- Tier 3: Month 6+ (loyalty, VIP, community, product line expansion)

**Design implementation timeline** with specific week-by-week actions.

**Scaffold**: Use `data/m21/retention_playbook.md` as template. The tier structure and timeline are universal. Customize tactics for your product.

---

## Grading Rubric

| Grade | Evidence Coverage | Confidence Honesty | Upgrade Paths | Actionability | Reusability |
|-------|------------------|--------------------|---------------|---------------|-------------|
| **A (9-10)** | Every section has A/B-grade evidence. IonWave-specific data incorporated. | Every grade defensible. No inflation. | Every gap has specific, actionable upgrade path. | Ready to implement. Timeline concrete. | All frameworks work for any DTC consumable. |
| **B (7-8)** | Most sections have B/C-grade evidence. Industry benchmarks well-sourced. | Mostly accurate. 1-2 generous grades. | Most gaps have actionable paths. | Implementable with minor adjustments. | Frameworks mostly generalizable. |
| **C (5-6)** | Several sections at C/D-grade. Some benchmarks unsourced. | Several generous grades. | Half the paths are vague. | Requires significant work to implement. | IonWave-specific, needs adaptation. |
| **D (3-4)** | Mostly D-grade or unsourced. | Systematic inflation. | Vague or missing paths. | Framework only, not implementable. | Not reusable. |
| **F (<3)** | No evidence. | No grades. | No paths. | Not useful. | Not applicable. |

**IonWave's grade**: 8.0/10 (B+). Strengths: honest confidence grading, strong industry evidence, actionable playbook. Weakness: no IonWave-specific data (pre-launch), depletion messaging unvalidated.

---

## What's NOT in This OpKit (Out of Scope)

- Email copy (see M17: Email)
- SMS strategy details (see M18: SMS)
- Customer lifecycle CRM architecture (see M19: Customer Lifecycle)
- Customer support processes (see M20: Support)
- Referral program design (see M22: Referral)
- Pricing/offer strategy (see M10: Pricing & Offer)


---

### 📄 retention_playbook.md

# Retention Playbook — M21

**TUP**: M21 (Subscription & Retention)
**Version**: 1.0.0
**Date**: 2026-02-06
**Confidence**: Overall C (industry evidence, best-in-class case studies, no IonWave-specific data)

---

## Retention Priority Matrix

Ranked by (impact on churn) x (ease of implementation) x (evidence quality).

### Tier 1: Implement Before Launch (Highest ROI)

| # | Tactic | Expected Churn Impact | Difficulty | Evidence | Notes |
|---|--------|----------------------|------------|----------|-------|
| 1 | **Full dunning stack** (smart retries + card updater via Shopify Payments + 4-email Klaviyo sequence + SMS via Postscript) | -1.5 to -3 pp on total churn | LOW (configuration, no custom dev) | B | Single highest-ROI retention activity. Reduces involuntary churn by 50-70%. At 12% base churn, this alone drops to ~10%, extending avg lifetime from 8.3→10 months = 20% LTV increase. |
| 2 | **Cancellation save flow** with pause as primary option | Saves 20-30% of voluntary cancellation attempts | LOW-MED (subscription platform feature) | B | Design: survey → frequency adjust / skip / pause → let go gracefully. See `win_back_offer_ladder.md` for full flow. |
| 3 | **Flexible subscription frequency** (monthly, 5-week, 6-week, 2-month) | -20-40% of "too much product" churn | LOW (platform config) | C | "Too much product" is #1 supplement cancellation reason (20-30%). Flexible frequency directly solves it. Do NOT default to monthly-only. |
| 4 | **Pre-charge notification** (email 3-5 days before renewal) | -10-20% involuntary churn + reduces "surprise charge" cancellations | LOW (Klaviyo automation) | C | Counterintuitive: charge reminders reduce churn, not increase it. Customers feel respected. |
| 5 | **30-day onboarding email sequence** with results timeline | -15-25% of Month 1 churn | MED (content creation) | C | Design: Day 1 (welcome + what to expect), Day 3 (how to use + routine anchor), Day 7 (what you might notice), Day 14 (midpoint), Day 21 (results timeline), Day 28 (renewal preview + reinforcement). Use Seaonic proxy data for timeline expectations. |

**Tier 1 combined impact estimate**: Reduces monthly churn from 15-20% (no infrastructure) to 10-12% (basic infrastructure). This is a 2-4x LTV improvement. [Confidence: C — derived from individual tactic estimates. Compounding effects unknown.]

### Tier 2: Implement in First 90 Days

| # | Tactic | Expected Churn Impact | Difficulty | Evidence | Notes |
|---|--------|----------------------|------------|----------|-------|
| 6 | **Win-back email sequence** (education-first, see `win_back_offer_ladder.md`) | Reactivates 5-15% of churned within 90 days | MED (content creation + Klaviyo flow) | B | Education-led, not discount-led. Day 1→90 sequence with depletion messaging. |
| 7 | **Churn prediction signals** in analytics | Enables targeted intervention for high-risk subscribers | MED (Klaviyo + subscription platform integration) | B | Track: skip rate, email engagement drop, frequency changes, discount-acquired flag, support complaints. See `churn_prediction.json` for full model. |
| 8 | **SMS subscription management** | -10-20% passive churn | LOW-MED (Postscript setup) | C | "Reply SKIP to skip this month." 98% open rate vs. 20-30% for email. Reduces friction for all subscription actions. |
| 9 | **Subscription discount: 15%** | Motivates subscription without attracting deal-seekers | LOW (pricing decision) | B | ProfitWell: 15-20% is optimal range. Below 10% doesn't motivate. Above 25% attracts price-sensitive customers who churn 20-40% faster. Danilo's 15% figure is correct. |
| 10 | **Cancellation survey** | Data collection for future optimization | LOW (platform feature) | B | 4 options: too much product / not seeing results / too expensive / switching. Enables segmented save flow and win-back. |

### Tier 3: Implement Post-Month 6 (Once You Have Data)

| # | Tactic | Expected Churn Impact | Difficulty | Evidence | Notes |
|---|--------|----------------------|------------|----------|-------|
| 11 | **Loyalty program with time-based escalation** | -5-10% for Month 6+ subscribers | MED (program design + platform) | C | Month 3: 2% store credit. Month 6: 5%. Month 12: 10%. Creates sunk-cost switching cost. |
| 12 | **VIP program** (early access, exclusive content) | -5-10% for high-LTV subscribers | MED | C | Segment top 20% by LTV. Exclusive access to new products, founder calls, content. |
| 13 | **Community** (Slack/Discord/Facebook Group) | -5-15% for active members | MED-HIGH (ongoing management) | C | Most effective for identity-driven ICP segments (keto/carnivore). Build after 100+ subscribers. |
| 14 | **Product line expansion** (flavors, formats) | -15-25% of product fatigue churn | HIGH (product development) | B | LMNT's 10+ flavors is gold standard. Single-SKU at launch means this lever is unavailable initially. Plan for it. |
| 15 | **Referral program** | Indirect retention (referrers have 20-30% lower churn) | MED | C | "Give $10, get $10" per Danilo. The retention benefit is for the REFERRER, not the referee — people who refer feel more invested. |

### Anti-Patterns: What NOT To Do

| Tactic | Why It Fails | Evidence |
|--------|-------------|----------|
| **Aggressive cancellation friction** (hide cancel button, require phone call) | FTC "Click-to-Cancel" rule prohibits this. Destroys trust. Eliminates reactivation potential. Generates negative reviews. | B |
| **Escalating discount ladder** (Danilo's original: 10%→30%) | Trains discount-seeking behavior. Destroys margins. Only addresses 15-20% of churn reasons. See `win_back_offer_ladder.md` for full analysis. | B |
| **Contract/commitment locks** (12-month required) | Catastrophic for consumable supplements. Chargebacks, 1-star reviews, never return. FTC scrutiny increasing. | B |
| **Generic "We miss you!" emails** | Near-zero measurable impact. Personalized outperforms generic by 3-5x. | C |
| **Deep discounts to prevent cancellation** (40-50%+) | Attracts and retains only price-sensitive customers with negative LTV after discount. | B |
| **Ignoring involuntary churn** | Most common mistake. 30-40% of churn is fixable payment mechanics. Brands spend all effort on psychology while hemorrhaging subscribers to expired cards. | B |

---

## Scenario Modeling: Infrastructure Impact on LTV

**Critical caveat** (from persona dialogue): These estimates assume product efficacy meets baseline expectations (HYP-003.1 currently at C-grade, Seaonic proxy). If product-market fit is weaker than the proxy suggests, all churn estimates shift upward by 2-5pp. The individual tactic estimates do NOT stack linearly for voluntary churn tactics that target the same population (Month 1-3 subscribers). Dunning and save flows ARE orthogonal (different churn populations).

| Scenario | Expected Monthly Churn | Avg Lifetime | LTV at $40 GP/order | Evidence |
|----------|----------------------|--------------|---------------------|----------|
| **No infrastructure** (launch without save flows, dunning, onboarding) | 15-20% | 5-6.7 months | $200-$267 | C |
| **Tier 1 implemented** (dunning + save flow + pause + frequency + onboarding) | 10-12% | 8.3-10 months | $333-$400 | C |
| **Tier 1+2 implemented** (+ win-back + churn prediction + SMS) | 8-10% | 10-12.5 months | $400-$500 | D |
| **Full stack + strong product efficacy** | 7-9% | 11-14 months | $440-$571 | D |
| **Best-in-class** (AG1-level brand + product + infrastructure) | 4-6% | 17-25 months | $667-$1,000 | D |

**The gap between "no infrastructure" and "Tier 1" is the highest-leverage gap in the entire business.** It represents a potential 2x LTV improvement for relatively low implementation cost. This is the difference between HYP-003 (≤12% churn target) being achievable or not.

---

## Relationship to HYP-003 (Churn Hypothesis)

This playbook directly addresses the HYP-003 sub-hypothesis chain:

| Sub-Hypothesis | Grade | This Playbook's Contribution |
|---------------|-------|------------------------------|
| HYP-003.1 (Product Efficacy) | C | Onboarding sequence sets expectations. Depletion messaging reinforces perceived efficacy. |
| HYP-003.2 (Early-Life Churn M1-3) | D | Tier 1 tactics #4 and #5 directly target the Month 1-3 cliff. |
| HYP-003.3 (Retention Infrastructure) | D | This entire playbook IS the retention infrastructure. Tier 1 implementation upgrades this from D to C. |
| HYP-003.4 (Consumption-Cadence Match) | D | Tactic #3 (flexible frequency) directly addresses this. |

---

## Implementation Timeline

| Week | Actions |
|------|---------|
| **Pre-launch** | Select subscription platform (Loop rec). Configure dunning. Set up flexible frequency. Design save flow. Write onboarding emails. |
| **Launch** | Tier 1 active. Begin collecting cancellation survey data. |
| **Week 4** | Review first month data. Adjust onboarding based on actual customer feedback. |
| **Week 8** | Implement Tier 2 (win-back sequence, churn signals, SMS management). |
| **Month 3** | First meaningful cohort data. Recalibrate churn model with actual IonWave data. |
| **Month 6** | Evaluate Tier 3 (loyalty, VIP, community). Decide on Stay AI vs. manual. |

---

## Intelligence Gaps

| Gap | Impact | Upgrade Path | Priority |
|-----|--------|-------------|----------|
| All predictions industry-benchmark based (no IonWave data) | HIGH | Collect 90 days actual data. Recalibrate everything. | EXPECTED |
| Marine plasma time-to-value unknown | CRITICAL | Seaonic review mining (CSP-002 #1 priority) | CRITICAL |
| Optimal subscription discount untested | MEDIUM | A/B test 10% vs 15% vs 20% post-launch | MEDIUM |
| Depletion messaging not validated for compliance | HIGH | Legal/regulatory review before publishing | HIGH |
| Loop Subscriptions pricing and integration depth not independently verified | HIGH | Check official site before committing | HIGH |


---

### 📄 subscription_psychology.md

# Subscription Psychology — M21

**TUP**: M21 (Subscription & Retention)
**Version**: 1.0.0
**Date**: 2026-02-06
**Confidence**: Overall C (industry benchmarks + best-in-class case studies, no IonWave-specific data yet)

---

## Why People Subscribe (Ranked by Strength for Supplements)

| Driver | Strength | IonWave Lever | Evidence |
|--------|----------|--------------|----------|
| **Convenience** — never run out, auto-delivered | PRIMARY | Default subscription at optimal frequency | [B] Recharge data: #1 stated reason across DTC supplement brands |
| **Savings** — subscription discount | PRIMARY | 15% subscription discount (per Danilo's retention playbook) | [B] ProfitWell: optimal discount range is 15-20%. Below 10% doesn't motivate; above 25% attracts deal-seekers who churn 20-40% faster |
| **Consistency** — daily habit, part of routine | SECONDARY | Onboarding sequence builds the habit in first 30 days | [C] AG1 case study: "30-day challenge" framing + physical ritual (canister, scoop) drives habit formation |
| **Health investment identity** — "I'm the kind of person who takes care of my minerals" | ASPIRATIONAL | Brand narrative + community | [C] AG1 and Seed both leverage identity. "AG1 drinker" is a social identity marker. Requires scale to achieve. |
| **Belonging** — part of a community/tribe | LONG-TERM | Community building post-100 subscribers | [C] Strongest for identity-driven segments (keto/carnivore per IonWave ICP) |

**IonWave-specific note**: The marine plasma science story creates a unique "informed health optimiser" identity that pure electrolyte brands (LMNT, Liquid IV) cannot claim. This is an untapped retention driver — subscribers who understand the 78-mineral science have intellectual investment in continuing, not just financial.

---

## Why People Cancel (Ranked by Frequency for Supplements)

| Reason | % of Cancellations | Addressable? | IonWave Intervention | Evidence |
|--------|-------------------|-------------|---------------------|----------|
| **Too much product / excess buildup** | 20-30% | YES — flexible frequency | Offer monthly, 5-week, 6-week, 2-month cycles from Day 1 | [B] Recharge data: #1 stated cancellation reason for supplement subscriptions. Directly addressable with frequency options. |
| **Not seeing results / doesn't work** | 15-25% | PARTIALLY — expectation management | 30-day onboarding with explicit results timeline. Use Seaonic proxy data. | [C] Seed case: explicit timeline communication ("microbiome changes take 4-6 weeks") extends grace period. IonWave risk: marine plasma may have slower onset than synthetic electrolytes. |
| **Too expensive / budget change** | 15-20% | PARTIALLY — flexible options | Downgrade option (smaller quantity), pause, skip | [B] ProfitWell: price-sensitive churn is the hardest to retain profitably. Discounting attracts wrong customers. Better to let price-sensitive churners go. |
| **Switched to different brand** | 10-15% | YES — differentiation | Science-backed superiority messaging. "78 minerals vs. 3." Competitive comparison content. | [C] Zero switching costs in supplements (per Porter's analysis). Must create perceived switching cost through education. |
| **Forgot I was subscribed / surprise charge** | 5-10% | YES — engagement | Pre-charge notification 3-5 days before. Engagement content between shipments. | [C] Counterintuitive: charge reminders reduce churn, not increase it. Customers feel respected. |
| **Bad experience (taste, shipping, support)** | 5-10% | YES — operational quality | Fast support response. Shipping tracking. Taste optimization. | [B] Support complaint is a HIGH churn predictor (2-3x risk). Resolution speed is key. |

### The Structural Challenge for Supplements

Supplements face higher churn than most DTC categories because of a toxic combination:
- **Ambiguous results**: Hard to feel the difference day-to-day (unlike skincare where you see your skin)
- **Zero switching costs**: No data lock-in, no workflow integration, no emotional bond (unlike pet subscriptions)
- **Abundant alternatives**: LMNT, Liquid IV, AG1, DIY, or just... nothing
- **No habit reinforcement**: No visible result, no taste reward loop, no social accountability

[Confidence: B — corroborated by ProfitWell, Recharge, and IonWave's own Porter analysis (buyer power: HIGH)]

**IonWave's structural answer**: Marine plasma's 78-mineral complexity creates potential product-complexity switching cost (à la AG1, which would require 5-10 separate supplements to replace). But this only works if the customer understands and values the complexity. Education is not just marketing — it's a retention mechanism.

---

## Psychological Levers for Retention (Evidence-Based)

### Tier 1: Proven High-Impact

| Lever | Mechanism | Implementation | Evidence |
|-------|-----------|---------------|----------|
| **Loss aversion** | "You've been building mineral stores for 47 days. Canceling resets your progress." | Post-Day 30 messaging references cumulative benefit | [C] Behavioral economics: losses are felt ~2x more than equivalent gains. Seed uses this with microbiome messaging. |
| **Sunk cost** | Physical artifact (jar, canister) on counter creates daily reminder + investment anchor | Premium first-order packaging with reusable container | [B] AG1's metal canister, Seed's glass jar. Physical presence = daily engagement without email. |
| **Habit architecture** | Attach to existing routine: "with morning coffee," "post-workout" | Onboarding asks for routine anchor, sends timed reminders | [C] Habit research: behaviors attached to existing cues stick 2-3x longer than freestanding habits. |
| **Status quo bias** | Make staying easier than leaving: pause > cancel, skip > cancel | Cancellation flow presents pause/skip BEFORE cancel option | [B] Recharge data: pause saves 25-35% of cancellation attempts. Paused customers return at 40-60% rate vs. 5-15% for cancelled. |
| **Endowed progress** | "You're 2 months into your mineral optimization journey" | Progress tracking in account portal and email | [C] Endowed progress effect: people are more motivated to complete a journey they've already started. |

### Tier 2: Moderate Impact

| Lever | Mechanism | Implementation | Evidence |
|-------|-----------|---------------|----------|
| **Social proof reinforcement** | Existing subscribers see others continuing | "Join 2,847 subscribers" messaging; review prompts at Day 60 | [C] Social proof reduces uncertainty about continued purchase |
| **Escalating commitment** | Loyalty rewards that increase over time, creating switching cost | Month 3: 2% bonus. Month 6: 5% bonus. Month 12: 10% bonus. | [C] Time-based escalation creates "I'd lose my status" switching cost |
| **Variety/novelty** | Prevent product fatigue | Seasonal flavors, limited editions, add-on products | [B] LMNT's 10+ flavors is the gold standard. IonWave is single-SKU at launch — this lever is unavailable initially. |

---

## Intelligence Gaps

| Gap | Impact | Upgrade Path | Priority |
|-----|--------|-------------|----------|
| Marine plasma time-to-value unknown | HIGH — if onset is >60 days, Month 1-3 cliff will be severe | Mine Seaonic reviews for time-to-value language. CSP-002 already identified this as priority #1. | CRITICAL |
| No IonWave-specific cancellation reason data | HIGH — current ranking is industry benchmark, not IonWave-specific | Implement cancellation survey from Day 1. Collect 50+ responses before adjusting strategy. | HIGH |
| Subscription discount optimization untested | MEDIUM — 15% may not be optimal for this price point | A/B test 10% vs 15% vs 20% at launch or shortly after | MEDIUM |
| Identity-based retention potential unvalidated | MEDIUM — depends on ICP segment distribution | Survey early subscribers on identity/community interest | LOW |


---

### 📄 win_back_offer_ladder.md

# Win-Back Strategy — M21

**TUP**: M21 (Subscription & Retention)
**Version**: 1.0.0
**Date**: 2026-02-06
**Confidence**: Overall C (industry evidence + IonWave positioning analysis, no IonWave-specific data)

---

## Why Danilo's Discount Ladder Is the Wrong Approach

Danilo's original win-back ladder (10%→15%→20%→25%→30% over 90 days) is a textbook example of the discount-led anti-pattern. The evidence against it is strong:

| Problem | Evidence | Grade |
|---------|----------|-------|
| **Trains customers to game cancellation** | ProfitWell data: repeat cancel-resubscribe behavior is 40% higher for brands using escalating discounts | C |
| **Attracts wrong retention** | ProfitWell: discount-acquired/retained customers churn 20-40% faster than full-price once the discount expires | B |
| **Destroys margins** | At IonWave's price point (~$59), a 25% discount for 3 months (Day 60 offer) yields ~$133 revenue vs. normal ~$177 — a 25% revenue haircut on already-thin margins | B (mathematical) |
| **Only addresses 15-20% of churn reasons** | Price sensitivity accounts for 15-20% of supplement cancellations. The other 80% cancel for reasons discounts don't solve. | B |
| **Undermines premium positioning** | Marine plasma's $59 price signals quality. Aggressive discounting signals desperation and erodes the premium anchor. | C |

**The core insight**: IonWave's strongest retention asset — the marine plasma science story — is completely absent from Danilo's win-back system. Education-led messaging addresses the actual top churn reasons (excess product, no felt results, disengagement) while preserving brand positioning.

---

## Redesigned Win-Back Strategy: Education-First, Flexibility-Second, Discount-Last

### Pre-Cancellation: Save Flow (Before They Leave)

This happens IN the cancellation flow within the subscription platform. Goal: prevent the cancellation from happening.

| Step | Trigger | Action | Rationale |
|------|---------|--------|-----------|
| 1 | Customer clicks "Cancel" | **Cancellation survey** — "Help us understand why" (multiple choice: too much product / not seeing results / too expensive / switching / other) | Data collection. Enables segmented response. [C] Best practice from Recharge/Skio. |
| 2a | If "too much product" | **Offer frequency adjustment** — "Would you prefer every 6 weeks instead? You'll never build up excess." | Directly solves the #1 cancellation reason. [B] Recharge data: frequency adjustment saves 20-30% of these. |
| 2b | If "not seeing results" | **Education content** — "Marine minerals build up gradually. Here's what to expect at 60 and 90 days." Link to science content. | Extends grace period through expectation management. [C] Seed model. |
| 2c | If "too expensive" | **Offer downgrade** — smaller quantity or skip next month. NOT a discount. | Preserves revenue per unit. A customer paying $39 for less product is better than $50 for full product (discounted). |
| 2d | If "switching" | **Comparison content** — "Here's how marine plasma's 78 minerals compare to [typical electrolyte's] 3." | Intellectual switching cost. May not save this customer but plants a seed for return. |
| 3 | If none of above worked | **Offer pause** — "Not ready to cancel? Pause for 1-3 months. Your subscription picks up where you left off." | [B] Paused customers return at 40-60% vs. 5-15% for cancelled. |
| 4 | If still cancelling | **Let them go gracefully.** "We'll miss you. Your account stays active and you can resubscribe anytime." | Hostile exit experiences eliminate reactivation potential. FTC "Click-to-Cancel" compliance. |

### Post-Cancellation: Win-Back Sequence

Only for customers who complete cancellation. Channel: email + SMS.

| Timing | Type | Message | Offer | Rationale |
|--------|------|---------|-------|-----------|
| **Day 1** | Confirmation | "Your subscription is paused. Here's what happens next with your mineral levels." | None | Confirm the cancellation. Don't beg. Plant the depletion seed. |
| **Day 7** | Education | "It's been 7 days. Your body's trace mineral stores are starting to draw down. Here's the science of mineral depletion." | None | Education-led. Address the #2 churn reason (not seeing results) by reframing: you saw results, you just didn't notice until they stopped. [C] Depletion messaging framework — used by Seed and probiotic brands. |
| **Day 14** | Social proof | "X subscribers just hit their 90-day milestone. Here's what they're reporting." | None | Social proof + FOMO. Show what active subscribers are experiencing. |
| **Day 21** | Flexibility | "Maybe the timing wasn't right. You can come back at any frequency — monthly, every 5 weeks, every 6 weeks, or every 2 months." | Frequency flexibility (no discount) | Addresses the #1 cancellation reason (excess product). Many cancellers would have stayed with a different frequency. |
| **Day 30** | Science deep-dive | "30 days without marine minerals: what the research says about trace mineral depletion and your body." | Link to a dedicated landing page with the science | Full education play. This is IonWave's strongest card. |
| **Day 45** | Small incentive | "We'd love to have you back. Here's 10% off your return order." | 10% off ONE order (not ongoing) | First and smallest discount. One-time only. Does not train discount behavior because it's a single order, not a subscription discount. |
| **Day 60** | Last education touch | "2 months without marine minerals. If you've been considering coming back, here's what subscribers report after restarting." | Free shipping on return order | Low-cost incentive. Restarter testimonials. |
| **Day 90** | Final | "We're not going to keep emailing. But your spot is always open. Here's a link to resubscribe whenever you're ready." | None | Clean exit. No desperation. Preserves brand dignity and future relationship. |
| **Day 180** | Reactivation | "It's been 6 months. New [flavor/formulation/content]. Thought you might want to know." | 15% off return order | Only offer meaningful discount at 6 months when customer is truly lapsed. One-time. |

### Why This Sequence Is Better Than Danilo's

| Dimension | Danilo's Ladder | Redesigned Sequence |
|-----------|----------------|-------------------|
| **Churn reasons addressed** | 1 (price: 15-20%) | 4+ (excess product, no results, disengagement, price: 70-80%) |
| **Max discount** | 30% ongoing | 15% one-time (at Day 180 only) |
| **Brand positioning** | Erodes premium | Reinforces science authority |
| **Margin impact** | -25% revenue on retained customers | -10% on Day 45 return only, -15% on Day 180 only |
| **Discount training risk** | HIGH | LOW (one-time offers, not subscription discounts) |
| **Data collection** | None | Cancellation survey enables segmented response |
| **Education content** | None | 4 science-based touchpoints building intellectual switching cost |
| **Reactivation potential** | Low (burned by discounting) | Higher (graceful exit preserves relationship) |

---

## Depletion Messaging Framework (IonWave-Specific)

This is the unique asset IonWave has that generic electrolyte brands cannot replicate.

### The Science Basis

Marine plasma contains 78 trace minerals that the body cannot synthesize. When supplementation stops:
- Water-soluble minerals (Mg, K, Na) deplete within days
- Trace minerals (Zn, Se, Mn, Cu, Cr) deplete over weeks
- Deep-tissue mineral stores draw down over 30-90 days

[Confidence: D — theoretical framework based on mineral biology. Needs clinical validation or Seaonic proxy evidence to upgrade. This is the kind of content that should be workshopped with a domain expert.]

### Messaging Templates

**Day 7 email subject**: "What happens when you stop taking marine minerals"
- Frame: educational, not guilt-inducing
- Tone: science teacher, not salesperson
- Content: mineral depletion timeline, what you might notice (energy, recovery, sleep)

**Day 30 email subject**: "30 days without trace minerals: the research"
- Frame: deep-dive science content
- Tone: journal article summary, accessible but substantive
- Content: link to dedicated science page on IonWave site (doubles as SEO content)

[VOID — requires: Domain expert review of depletion claims. Must be scientifically defensible. FDA/FTC compliant (no disease claims). Upgrade path: review with Danilo's formulation expert or marine biology advisor.]

---

## Intelligence Gaps

| Gap | Impact | Upgrade Path | Priority |
|-----|--------|-------------|----------|
| Depletion timeline not clinically validated | HIGH — if claims are wrong, messaging backfires and trust is destroyed | Literature review on trace mineral depletion rates. Seaonic proxy evidence. | CRITICAL |
| No data on education-led vs discount-led win-back rates for supplements specifically | MEDIUM — relying on cross-category evidence | A/B test at launch: 50% get education sequence, 50% get discount ladder. Measure 90-day reactivation rate. | HIGH |
| FTC/FDA compliance of depletion messaging untouched | HIGH — "your minerals are depleting" could be construed as health claim | Legal review before publishing any depletion content | HIGH |
| Cancellation survey design not finalized | LOW — standard practice, low risk | Design 4-option survey before platform setup | MEDIUM |


---

## 🔗 Dependencies & Relationships

### Feeds Into
- M3 (Financial Model — churn rate affects LTV:CAC)
- M19 (Customer Lifecycle — retention curve)

### Requires
- M0 (Trade Thesis — DONE)

---

## ⚠️ Intelligence Gaps

- Marine plasma time-to-value unknown (CRITICAL)
- Loop Subscriptions pricing/integration not independently verified
- Depletion messaging needs legal/regulatory review
- No IonWave-specific churn data (expected pre-launch)

---

## 🎯 Next Actions

Collect actual IonWave churn data post-launch. Mine Seaonic reviews for time-to-value (upgrades HYP-003.1).


---

## 🧰 OpKits

- OK-M21-001

---

---

_Report generated: 2026-02-09 17:49:44_

_Source: `data\m21`_