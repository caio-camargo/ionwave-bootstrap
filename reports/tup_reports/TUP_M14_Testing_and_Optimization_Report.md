# TUP M14: Testing & Optimization

**Status:** migrated | **Quality:** 7.5/10 | **Version:** 1.0.0
**Cluster:** BCL-3 (N/A)

---

## 📋 Overview

- **Workshop Date:** 2026-02-06
- **Actor:** Caio + Claude (claude-opus-4-6)
- **Protocol Used:** N/A
- **Change Type:** initial_workshop

### Workshop Dialogue
- **Personas Used:** CRO Statistician, Bootstrapped DTC Founder, Growth Hacker (Performance Marketer)
- **Rounds:** 4
- **Saturated:** True
- **Upgrades Applied:** 9
- **Unresolved Issues:** 0

### Quality Assessment
- **Score:** 7.5/10
- **Rationale:** N/A

---

## 📁 Content Files


---

## 🔧 Structured Data

_JSON files converted to human-readable format_

### 📊 experimentation_framework.json

- ** Meta:**
  - **Tup:** M14
  - **Tab:** 3 of 6
  - **Title:** Experimentation Framework
  - **Version:** 1.0.0
  - **Date:** 2026-02-06
  - **Author:** Caio, Claude (collaborative)
  - **Ai Model:** claude-opus-4-6
  - **Status:** AI Draft
  - **Hypothesis Links:**
    - HYP-001
    - HYP-002
    - HYP-004
  - **Danilo Source:** ops_model_v10_dump/377_experimentation_framework.json
  - **Danilo Assessment:** Template only — experiment card + empty log. No methodology, no decision rules, no learning system.
  - **Cross References:**
    - **M10 Price Testing:** data/m10_pricing_offer/price_testing_framework.md — price tests use M10 protocol, NOT this framework
    - **M12 Creative Testing:**
      > ops_model_v10_dump/348_creative_testing_protocol1.json — creative testing specifics live in M14 creative_testing_protocol.md
- **Core Philosophy:**
  - **Tagline:** Every experiment produces learning, not just winners.
  - **Principles:**
    - 
        **Id:** P1
      - **Name:** Learning over winning
      - **Description:**
        > A test that confirms 'no difference' is not a failure — it eliminates a hypothesis and frees resources. The only failed test is one with no learning documented.
      - **Anti Pattern:** Declaring tests 'inconclusive' and moving on without documenting what was learned.
    - 
        **Id:** P2
      - **Name:** Big swings before small tweaks
      - **Description:**
        > Test fundamentally different approaches (different angles, different formats, different audiences) before optimizing details (button color, font size). At low traffic, you can't detect small effects — so only test things that COULD produce large effects.
      - **Anti Pattern:** Testing button colors when you haven't validated your headline or offer.
    - 
        **Id:** P3
      - **Name:** Sequential price, parallel creative
      - **Description:**
        > Price tests must run one at a time (they contaminate each other). Creative tests and presentation tests can run in parallel because they don't interact. See M10 Price Testing Framework for price-specific protocol.
      - **Anti Pattern:** Running two price tests simultaneously, or blocking creative tests behind a price test queue.
    - 
        **Id:** P4
      - **Name:** Document everything, even failures
      - **Description:**
        > Every test gets a card filed in the test log before launch. Every test gets results + learning documented after completion. This builds institutional knowledge that compounds.
      - **Anti Pattern:** Running tests ad-hoc in the ad platform and never recording results.
    - 
        **Id:** P5
      - **Name:** Match method to traffic
      - **Description:**
        > At <100 visitors/day, traditional A/B testing cannot detect modest effects. Use qualitative judgment, pre/post testing, or Bayesian methods. Don't pretend you have statistical power you don't have.
      - **Anti Pattern:**
        > Waiting 3 months for 'statistical significance' on a landing page test when you could have shipped the obvious winner in week 1.
    - 
        **Id:** P6
      - **Name:** Test the hypothesis, not the tactic
      - **Description:**
        > Frame every test as a hypothesis about customer behavior, not a preference between creative executions. 'Users trust UGC more than founder content' is testable. 'This ad looks cool' is not.
      - **Anti Pattern:** Testing random variations without a hypothesis about WHY the variant should win.
- **Experiment Card:**
  - **Description:** Every experiment must have a card filed BEFORE launch. No exceptions.
  - **Schema:**
    - **Test Id:**
      - **Format:** {TYPE}-{NNN}
      - **Types:**
        - **Pt:** Price test (M10 protocol — sequential only)
        - **Ct:** Creative/ad test
        - **Lp:** Landing page test
        - **At:** Audience test
        - **Em:** Email/SMS test
        - **Ck:** Checkout/cart test
        - **Gn:** General experiment (anything else)
    - **Hypothesis:** If we [change X], then [metric Y] will [increase/decrease] because [reason Z]
    - **Test Type:** One of: price | creative | landing_page | audience | email | checkout | general
    - **Variants:**
      - **Control:** Current/default state (A)
      - **Challenger:** Proposed change (B)
      - **Additional Variants:** Optional (C, D — only if traffic supports it)
    - **Primary Metric:** The ONE metric that decides the winner
    - **Secondary Metrics:** Diagnostic metrics that help explain WHY
    - **Sample Size Target:** Minimum visitors/impressions per variant before decision
    - **Duration:** Planned test duration (min/max)
    - **Traffic Split:** Percentage allocation per variant
    - **Kill Criteria:** When to stop early (optional — for sequential analysis)
    - **Launch Date:** When the test starts
    - **Decision Date:** When we commit to reading results
    - **Owner:** Who monitors this test and makes the call
  - **Example:**
    - **Test Id:** CT-001
    - **Hypothesis:**
      > If we use a 'tired by 2pm' hook instead of '78 minerals' hook, CTR will increase by >30% because fatigue is a more visceral problem than mineral count
    - **Test Type:** creative
    - **Variants:**
      - **Control:** '78 minerals your body is missing' hook — UGC format
      - **Challenger:** 'Tired by 2pm? Your electrolytes are wrong.' hook — same UGC format
    - **Primary Metric:** CTR (click-through rate)
    - **Secondary Metrics:**
      - CPC
      - Hook rate (3-sec view %)
      - ROAS
    - **Sample Size Target:** 1,000 impressions per variant minimum
    - **Duration:** 3-5 days or 2,000 total impressions (whichever first)
    - **Traffic Split:** 50/50
    - **Kill Criteria:** Kill variant if CTR <0.5% after 1,000 impressions
    - **Launch Date:** 2026-03-01
    - **Decision Date:** 2026-03-05
    - **Owner:** Caio
- **Decision Framework:**
  - **Description:** How to decide what to test, and how to interpret results at different traffic levels.
  - **Testing Priority Matrix:**
    - **Description:** What to test first. Ordered by expected impact × ease of testing.
    - **Priority Tiers:**
      - 
          **Tier:** 1
        - **Name:** Test FIRST — Highest impact, fastest learning
        - **Items:**
          - 
              **Element:** Ad creative hooks (first 3 seconds)
            - **Impact:** HIGHEST
            - **Ease:** Easy
            - **Why First:**
              > Hook determines if anyone sees your ad. 70-80% of performance is in the first 3 seconds. Testable with $50-100 per variant.
            - **Domain:** creative
          - 
              **Element:** Offer/price point
            - **Impact:** HIGHEST
            - **Ease:** Medium
            - **Why First:**
              > $10 price change = ~17% revenue swing per order. Use M10 protocol (sequential, RPV as primary metric).
            - **Domain:** price
            - **Cross Ref:** data/m10_pricing_offer/price_testing_framework.md
          - 
              **Element:** Headline (landing page)
            - **Impact:** HIGH
            - **Ease:** Easy
            - **Why First:** First text visitors read. Can produce 20-50% conversion lift from one change.
            - **Domain:** landing_page
      - 
          **Tier:** 2
        - **Name:** Test SECOND — High impact, moderate effort
        - **Items:**
          - 
              **Element:** Ad creative angle/message
            - **Impact:** HIGH
            - **Ease:** Medium
            - **Why:** Same format, different persuasion approach (health benefit vs social proof vs fear of missing out).
            - **Domain:** creative
          - 
              **Element:** Creative format
            - **Impact:** HIGH
            - **Ease:** Medium
            - **Why:**
              > UGC vs founder-to-camera vs lifestyle B-roll vs static image. Format determines ad production investment.
            - **Domain:** creative
          - 
              **Element:** Hero image/video (landing page)
            - **Impact:** HIGH
            - **Ease:** Medium
            - **Why:** Product shot vs lifestyle vs ingredient close-up. Visual hierarchy drives attention.
            - **Domain:** landing_page
          - 
              **Element:** Subscription vs one-time default
            - **Impact:** HIGH
            - **Ease:** Easy
            - **Why:** Which is the pre-selected option? Can dramatically shift subscription rate (HYP-002).
            - **Domain:** checkout
            - **Cross Ref:** M10 PT-006 in test queue
      - 
          **Tier:** 3
        - **Name:** Test LATER — Medium impact, or requires more traffic
        - **Items:**
          - 
              **Element:** Social proof placement
            - **Impact:** MEDIUM
            - **Ease:** Easy
            - **Domain:** landing_page
          - 
              **Element:** Page length (long-form vs short-form)
            - **Impact:** MEDIUM
            - **Ease:** Hard
            - **Domain:** landing_page
          - 
              **Element:** CTA text and color
            - **Impact:** MEDIUM
            - **Ease:** Easy
            - **Domain:** landing_page
          - 
              **Element:** Email subject lines
            - **Impact:** MEDIUM
            - **Ease:** Easy
            - **Domain:** email
          - 
              **Element:** Audience targeting segments
            - **Impact:** MEDIUM
            - **Ease:** Medium
            - **Domain:** audience
      - 
          **Tier:** NEVER_EARLY
        - **Name:** Do NOT test in first 6 months
        - **Items:**
          - 
              **Element:** Button colors
            - **Why Not:** Effect size too small to detect at low traffic. Any 'winner' is noise.
          - 
              **Element:** Font changes
            - **Why Not:** No meaningful conversion impact at any traffic level.
          - 
              **Element:** Minor copy tweaks
            - **Why Not:** Difference between 'Buy Now' and 'Add to Cart' is <1% — undetectable without 50K+ visitors.
          - 
              **Element:** Multiple simultaneous page redesigns
            - **Why Not:** If you change 10 things, you learn nothing about what worked.
  - **Traffic Based Methodology:**
    - **Description:**
      > Match your testing methodology to your actual traffic. Don't pretend to have statistical power you don't have.
    - **Tiers:**
      - 
          **Tier:** Phase 0: Pre-launch / <30 visitors per day
        - **Methodology:** QUALITATIVE JUDGMENT
        - **Approach:**
          > No A/B testing. Ship your best guess and iterate based on qualitative signals (heatmaps, session recordings, customer feedback, sales conversations).
        - **Tools:**
          - Hotjar free plan (heatmaps, recordings)
          - Customer interviews
          - Founder intuition
        - **When To Use:**
          > Pre-launch through Month 1. Also for any change where the 'right answer' is obvious (fixing a broken flow, adding missing information).
        - **Key Rule:**
          > If a change is obviously better (e.g., fixing a 404, adding a missing CTA), JUST SHIP IT. Don't 'test' obvious improvements.
      - 
          **Tier:** Phase 1: 30-100 visitors per day (Month 1-3)
        - **Methodology:** PRE/POST + BAYESIAN
        - **Approach:**
          > For landing page changes: implement the change and compare 2-week windows (before vs after). For ad creative: use platform-native testing (Meta A/B, TikTok split test) which has enough volume from ad delivery. For critical decisions: use Bayesian analysis with informative priors.
        - **Tools:**
          - Meta Ads A/B test feature (free)
          - GA4 cohort comparison
          - Bayesian calculator
        - **Sample Size Guidance:**
          - **Ad Creative Test:** 1,000+ impressions per variant (achievable in 2-3 days at $50/day)
          - **Landing Page Test:** 200+ visitors per variant (7-14 days at 30-100/day)
          - **Note:**
            > At these volumes, you can detect LARGE effects (>30% relative change) but NOT moderate effects (<15%).
        - **Key Rule:**
          > Only test big swings. If you think a change might improve things by 5%, don't bother testing — just ship it.
      - 
          **Tier:** Phase 2: 100-500 visitors per day (Month 3-6)
        - **Methodology:** STANDARD A/B + BAYESIAN
        - **Approach:**
          > Traditional A/B testing becomes viable for high-impact elements. Use Bayesian for faster decisions on creative tests. Sequential analysis for price tests (M10 protocol).
        - **Tools:**
          - Shopify A/B app
          - Meta Ads testing
          - GA4 experiments
        - **Sample Size Guidance:**
          - **Ad Creative Test:** 2,000+ impressions per variant
          - **Landing Page Test:** 500+ visitors per variant (5-10 days)
          - **Price Test:** 2,000+ visitors per variant (use M10 protocol, 14-30 days)
        - **Key Rule:**
          > You can now detect ~15-20% relative effects. Run 2-4 tests per month across ad creative + landing page.
      - 
          **Tier:** Phase 3: 500+ visitors per day (Month 6+)
        - **Methodology:** FULL EXPERIMENTATION PROGRAM
        - **Approach:**
          > Multiple concurrent tests across ad creative, landing page, email, and checkout. Price tests still sequential (M10). Creative tests scaled to 5-10 new variants per week.
        - **Tools:**
          - Full testing stack
          - Dedicated analytics
        - **Key Rule:** Testing velocity is now your competitive advantage. Aim for 8-12 tests per month.
- **Statistical Decision Rules:**
  - **Frequentist:**
    - **Confidence Threshold:** 95% (p < 0.05)
    - **Power:** 80%
    - **When To Use:** Price tests, checkout changes — anywhere a wrong decision has high financial impact.
    - **Minimum Test Duration:** 14 days (to capture day-of-week variance)
    - **Peeking Policy:** No peeking before planned sample size. Use sequential analysis if early stopping needed.
    - **Sample Size Table:**
      - **Description:** Required visitors PER VARIANT at 95% confidence, 80% power
      - **Note:** These are per-variant numbers. Double for total test traffic.
      - **Table:**
        - 
            **Baseline Cvr:** 2%
          - **Mde Relative:** 30%
          - **Sample Per Variant:** 4300
          - **Total:** 8600
        - 
            **Baseline Cvr:** 2%
          - **Mde Relative:** 20%
          - **Sample Per Variant:** 9800
          - **Total:** 19600
        - 
            **Baseline Cvr:** 3%
          - **Mde Relative:** 30%
          - **Sample Per Variant:** 2800
          - **Total:** 5600
        - 
            **Baseline Cvr:** 3%
          - **Mde Relative:** 20%
          - **Sample Per Variant:** 6500
          - **Total:** 13000
        - 
            **Baseline Cvr:** 5%
          - **Mde Relative:** 30%
          - **Sample Per Variant:** 1600
          - **Total:** 3200
        - 
            **Baseline Cvr:** 5%
          - **Mde Relative:** 20%
          - **Sample Per Variant:** 3800
          - **Total:** 7600
  - **Bayesian:**
    - **Prior:**
      > Weakly informative — Beta(1,1) for new tests, Beta(alpha, beta) from previous test data for iterations
    - **Decision Threshold:** 95% probability that variant beats control
    - **When To Use:**
      > Creative testing, email subject lines, audience tests — anywhere faster decisions are worth the trade-off of slightly less certainty.
    - **Advantages At Low Traffic:**
      - Can declare results sooner (no fixed sample size)
      - Intuitive probability output ('93% chance variant B is better')
      - Handles early stopping without inflating false positive rate
      - Can incorporate prior knowledge from previous tests
    - **Practical Note:**
      > At 500 impressions per variant, Bayesian can often give you 80%+ confidence on a 30%+ effect. Frequentist would say 'not enough data.' For creative testing where the cost of a wrong decision is low (just run another creative), 80% is good enough.
    - **Error Rate Disclosure:**
      - **Note:**
        > DIALOGUE UPGRADE UPG-1: Be explicit about what each confidence threshold COSTS you in false decisions.
      - **Thresholds:**
        - **95%:**
          - **False Positive Rate:** ~5%
          - **Use When:**
            > Pricing, checkout, subscription terms — anywhere a wrong decision costs revenue. MANDATORY for all M10 price tests.
        - **90%:**
          - **False Positive Rate:** ~10%
          - **Use When:** Landing page changes, offer framing — moderate stakes, moderately reversible.
        - **80%:**
          - **False Positive Rate:** ~20%
          - **Use When:**
            > Ad creative selection — low stakes, easily reversible. At 5 creatives/month, expect ~1 false winner per quarter. Acceptable because: (a) creative swaps are instant, (b) the 'wrong' creative still ran at near-breakeven, (c) you'll detect the error within days of scaling.
        - **75%:**
          - **False Positive Rate:** ~25%
          - **Use When:**
            > ONLY for creative screening (kill/continue decisions on Day 3). NOT for final ship/no-ship decisions.
  - **The Just Ship It Threshold:**
    - **Description:** Not everything needs a test. Use judgment when:
    - **Criteria:**
      - The change is obviously better (fixing broken UX, adding missing info)
      - The potential downside of being wrong is tiny (email copy tweak)
      - You'd need 6+ months of traffic to detect the effect size
      - You're deciding between two options and neither is risky
      - Customer feedback overwhelmingly points in one direction
    - **Warning:**
      > Never 'just ship it' on: price changes, subscription terms, checkout flow changes, or anything that affects revenue per visitor. These always get tested.
- **Testing Velocity Benchmarks:**
  - **Description:** How many tests per month by growth stage
  - **Benchmarks:**
    - 
        **Stage:** Pre-launch
      - **Monthly Visitors:** <1,000
      - **Tests Per Month:** 0-1 on-site, 2-4 ad creative
      - **Focus:** Ad creative testing only (platform has the traffic). Ship best-guess site.
    - 
        **Stage:** Early (Month 1-3)
      - **Monthly Visitors:** 1,000-3,000
      - **Tests Per Month:** 1-2 on-site, 4-8 ad creative
      - **Focus:** Find winning creative angles. Test 1 landing page element per month (big changes only).
    - 
        **Stage:** Growing (Month 3-6)
      - **Monthly Visitors:** 3,000-15,000
      - **Tests Per Month:** 2-4 on-site, 8-12 ad creative
      - **Focus:** Testing program becomes systematic. Run creative and landing page tests in parallel.
    - 
        **Stage:** Scaling (Month 6+)
      - **Monthly Visitors:** 15,000+
      - **Tests Per Month:** 4-8 on-site, 12-20 ad creative
      - **Focus:** Full experimentation program. Iterating on email, checkout, upsell in addition to creative + LP.
- **Learning System:**
  - **Description:** How we capture and compound knowledge from every test
  - **Components:**
    - 
        **Name:** Test Log
      - **File:** data/m14/test_log.json
      - **Purpose:** Chronological record of every experiment with results and learnings
    - 
        **Name:** Knowledge Library
      - **Purpose:** Accumulated learnings organized by domain (creative, landing page, email, audience)
      - **Structure:** Each learning has: domain, finding, confidence, source_test_id, date, implications
    - 
        **Name:** Quarterly Review
      - **Purpose:**
        > Every 3 months, review test log. Identify: (1) what domains produced most wins, (2) what testing assumptions were wrong, (3) what to test next quarter.
      - **Cadence:** Q1: Month 3, Q2: Month 6, etc.
  - **Naming Conventions:**
    - **Test Ids:** {TYPE}-{NNN} where TYPE is PT/CT/LP/AT/EM/CK/GN and NNN is sequential
    - **Creative Ids:** C{NNN} — every creative variant gets a unique ID for lifetime tracking
    - **Ad Naming:** {HOOK_THEME}_{ANGLE}_{FORMAT}_{CREATOR}_{VERSION} e.g. 'tired2pm_energy_ugc_sarah_v1'
    - **Note:**
      > Naming convention enables filtering, searching, and pattern recognition across hundreds of tests over time.
- **Anti Patterns:**
  - **Description:** Common experimentation mistakes that destroy learning
  - **Mistakes:**
    - 
        **Name:** The HiPPO
      - **Description:**
        > Highest Paid Person's Opinion overrides test data. 'I don't like blue buttons' trumps data showing blue converts better.
      - **Fix:**
        > Pre-register the decision rule before the test starts. Document: 'If variant B wins by X%, we implement it regardless of aesthetic preference.'
    - 
        **Name:** Peeking and stopping
      - **Description:**
        > Checking results daily and stopping the test as soon as one variant is 'ahead.' This inflates false positives to 20-30%.
      - **Fix:**
        > Set sample size and duration BEFORE launch. Use sequential analysis methods if early stopping is needed.
    - 
        **Name:** Testing too many things at once
      - **Description:**
        > Changing headline + image + CTA + layout simultaneously. Even if the new version wins, you don't know WHY.
      - **Fix:**
        > One variable at a time for learning. Only test multiple changes when you need speed over insight (and accept reduced learning).
    - 
        **Name:** The button color trap
      - **Description:**
        > Spending limited testing bandwidth on low-impact elements. Button color differences are <1% — undetectable at IonWave's traffic for months.
      - **Fix:**
        > Priority matrix (Tier 1 first). If the expected effect is <10%, don't test it until you have 500+ daily visitors.
    - 
        **Name:** Survivorship bias in creative
      - **Description:** Only studying winning creatives. The losers teach you equally — they show what DOESN'T resonate.
      - **Fix:** Document learnings from losers in the test log. Pattern-match across failures to find anti-patterns.
    - 
        **Name:** No documentation
      - **Description:**
        > Running tests in ad platforms without recording hypotheses, results, or learnings. Institutional knowledge = zero.
      - **Fix:** Experiment card filed BEFORE launch. Results + learning filed WITHIN 48 hours of test completion.
- **Intelligence Gaps:**
  - 
      **Id:** GAP-1
    - **Description:** No real test data yet — all frameworks are theoretical
    - **Current Grade:** D
    - **Upgrade Path:**
      > Run first 5 creative tests → calibrate kill criteria, sample sizes, and velocity benchmarks with real IonWave data
    - **Priority:** CRITICAL — first 30 days
  - 
      **Id:** GAP-2
    - **Description:** Bayesian priors not calibrated for marine plasma supplement category
    - **Current Grade:** D
    - **Upgrade Path:**
      > After 10+ tests, build category-specific priors from IonWave's own data. Until then, use weakly informative priors.
    - **Priority:** Medium — Month 3+
  - 
      **Id:** GAP-3
    - **Description:** Creative fatigue rates unknown for this category
    - **Current Grade:** D
    - **Upgrade Path:** Track winning creative lifespan. After 5 winners decay, we'll have our own fatigue curve.
    - **Priority:** Medium — Month 3+

### 📊 test_log.json

- ** Meta:**
  - **Tup:** M14
  - **Tab:** 5 of 6
  - **Title:** Experiment Test Log
  - **Version:** 1.0.0
  - **Date:** 2026-02-06
  - **Author:** Caio, Claude (collaborative)
  - **Ai Model:** claude-opus-4-6
  - **Status:** AI Draft
  - **Hypothesis Links:**
    - HYP-001
    - HYP-002
    - HYP-004
  - **Danilo Source:** ops_model_v10_dump/378_ab_test_log.json
  - **Danilo Assessment:** Template with 1 example row. Good schema concept but empty.
  - **Purpose:**
    > Chronological record of every experiment. This is the institutional memory of what we've tested, what we've learned, and why.
- **Test Id Scheme:**
  - **Format:** {TYPE}-{NNN}
  - **Types:**
    - **Pt:**
      - **Name:** Price Test
      - **Protocol:** M10 Price Testing Framework (sequential only)
      - **Cross Ref:** data/m10_pricing_offer/price_testing_framework.md
    - **Ct:**
      - **Name:** Creative/Ad Test
      - **Protocol:** M14 Creative Testing Protocol
    - **Lp:**
      - **Name:** Landing Page Test
      - **Protocol:** M14 AB Testing Framework
    - **At:**
      - **Name:** Audience Test
      - **Protocol:** M14 Audience Testing Strategy
    - **Em:**
      - **Name:** Email/SMS Test
      - **Protocol:** TBD — M17/M18 when workshopped
    - **Ck:**
      - **Name:** Checkout/Cart Test
      - **Protocol:** M14 AB Testing Framework
    - **Gn:**
      - **Name:** General Experiment
      - **Protocol:** M14 Experimentation Framework
- **Completed Tests:**
  - 
      **Test Id:** PT-000
    - **Type:** price
    - **Launch Date:** 2026-01-15
    - **End Date:** 2026-01-29
    - **Hypothesis:** Higher price signals premium quality in marine plasma category
    - **Control:** $39/box
    - **Variant:** $49/box
    - **Primary Metric:** RPV (Revenue Per Visitor)
    - **Results:**
      - **Control Cvr:** 3.2%
      - **Variant Cvr:** 2.8%
      - **Control Rpv:** $1.25
      - **Variant Rpv:** $1.37
      - **Winner:** Variant ($49)
      - **Lift:** +23% RPV
      - **Confidence:** 95%
      - **Sample Size:** ~2,500 total
    - **Learning:**
      > In the marine plasma category, price INCREASES conversion (up to a point). $39 triggered 'too cheap to be real' skepticism for a product claiming 78 ocean minerals. Premium price anchored quality perception.
    - **Action Taken:** Implemented $49 as base price. Queued PT-001 ($49 vs $59) to find ceiling.
    - **Knowledge Tags:**
      - pricing
      - premium_positioning
      - price_quality_signal
    - **Source:** tracking/Price_Testing_Log.md
    - **Cross Ref:** data/m10_pricing_offer/price_testing_framework.md
    - **Statistical Note:**
      > DIALOGUE UPGRADE UPG-7: At ~2,500 total visitors and ~75 conversions (37-38 per variant), the +23% RPV lift is DIRECTIONAL, not definitive at 95% frequentist confidence. Standard sample size for detecting 23% relative effect at 3% CVR requires ~6,500/variant. PT-000 was large enough to detect the direction with high confidence, but the exact magnitude (+23%) has wide confidence intervals. Treat as 'very likely better' not 'precisely 23% better.'
- **Active Tests:**
  - 
      **Test Id:** PT-001
    - **Type:** price
    - **Launch Date:** 2026-02-15
    - **Hypothesis:** $59 maintains RPV advantage over $49
    - **Control:** $49/box
    - **Variant:** $59/box
    - **Primary Metric:** RPV
    - **Progress:** 1,647/4,000 visitors (41%)
    - **Expected Completion:** ~2 weeks
    - **Stakes:** CRITICAL — entire M10 offer architecture assumes $59. If $49 wins, full revision needed.
    - **Cross Ref:** data/m10_pricing_offer/price_testing_framework.md
- **Planned Tests:**
  - **Description:** Queue of tests prioritized by expected impact. Tests move to active_tests when launched.
  - **Queue:**
    - 
        **Priority:** 1
      - **Test Id:** CT-001
      - **Type:** creative
      - **Hypothesis:** Problem-aware hooks ('Tired by 2pm') outperform ingredient-aware hooks ('78 minerals') on CTR
      - **Control:** '78 minerals your body is missing' — UGC format
      - **Variant:** 'Tired by 2pm? Your electrolytes are wrong.' — UGC format
      - **Primary Metric:** CTR
      - **Est Duration:** 3-5 days
      - **Est Budget:** $100-200
      - **Prerequisite:** None — can run immediately
      - **Rationale:**
        > Validates whether ICP responds to problem framing or ingredient framing. Informs all creative direction.
    - 
        **Priority:** 2
      - **Test Id:** CT-002
      - **Type:** creative
      - **Hypothesis:** UGC format outperforms founder-to-camera format on ROAS for first purchase
      - **Control:** Founder (Caio/Danilo) to camera with same script
      - **Variant:** UGC creator with same script
      - **Primary Metric:** ROAS
      - **Est Duration:** 5-7 days
      - **Est Budget:** $200-300
      - **Prerequisite:** UGC content produced (M22 creator program)
      - **Rationale:**
        > Format determines production investment. If founder content works as well, saves $500-2K/month on UGC.
    - 
        **Priority:** 3
      - **Test Id:** LP-001
      - **Type:** landing_page
      - **Hypothesis:** Subscription-first default layout increases subscription rate by >15%
      - **Control:** One-time purchase as default, subscription as option
      - **Variant:** Subscription as default (pre-selected), one-time as downgrade
      - **Primary Metric:** Subscription rate (% of orders that are subscription)
      - **Est Duration:** 14-21 days
      - **Prerequisite:** PT-001 complete (need stable base price first)
      - **Rationale:** Directly tests HYP-002 (subscription conversion target 50% → 60%). See also M10 PT-006.
      - **Cross Ref:** M10 PT-006
    - 
        **Priority:** 4
      - **Test Id:** AT-001
      - **Type:** audience
      - **Hypothesis:** Biohacker/optimization audience converts at higher rate than general health-conscious audience
      - **Control:** Broad health + supplements interest targeting
      - **Variant:** Narrow biohacker + optimization + fasting interest targeting
      - **Primary Metric:** CVR (conversion rate)
      - **Est Duration:** 7-14 days
      - **Est Budget:** $300-500
      - **Prerequisite:** CT-001 winner determined (need stable creative first)
      - **Rationale:** Validates ICP prioritization (M27). Biohackers are hypothesized as early adopters.
- **Velocity Tracking:**
  - **Current Month:**
    - **Tests Launched:** 1
    - **Tests Completed:** 0
    - **Tests Active:** 1
    - **Win Rate:** N/A
    - **Avg Lift From Winners:** N/A
  - **All Time:**
    - **Tests Launched:** 2
    - **Tests Completed:** 1
    - **Win Rate:** 100%
    - **Avg Lift From Winners:** +23% RPV
    - **Total Learning Entries:** 1
    - **Note:** Extremely early — sample too small to draw conclusions about test program effectiveness.
- **Knowledge Library:**
  - **Description:** Accumulated learnings organized by domain. Updated after each test completion.
  - **Entries:**
    - 
        **Id:** KL-001
      - **Domain:** pricing
      - **Finding:**
        > In marine plasma category, price increase from $39 to $49 INCREASED RPV by 23%. Price signals quality.
      - **Confidence:** B
      - **Source Test:** PT-000
      - **Date:** 2026-01-29
      - **Implications:**
        > Sets floor at $49. Ceiling unknown (PT-001 testing $59). Category has strong price-quality association.

---

## 📝 Narrative Content

### 📄 ab_testing_framework.md

# A/B Testing Framework — M14: Testing & Optimization

**TUP**: M14 | **Tab**: 4 of 6
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-001 (CAC), HYP-002 (Subscription Conversion), HYP-004 (Gross Margin)
**Danilo Sources**: ops_model_v10_dump/379_ab_testing_framework.json, 380_ab_testing_framework1.json, 381_ab_testing_framework2.json (CONSOLIDATED — 3 near-duplicate tabs merged into 1 authoritative framework)
**Cross-references**: data/m10_pricing_offer/price_testing_framework.md (price tests — use M10, NOT this), data/m14/experimentation_framework.json (parent framework)

---

## 1. Purpose & Scope

This framework covers **on-site A/B testing** for landing pages, product pages, checkout flow, and other website elements. It does NOT cover:
- **Price testing** → Use M10 Price Testing Framework (sequential protocol, RPV as primary metric)
- **Ad creative testing** → Use M14 Creative Testing Protocol (platform-native testing)
- **Email/SMS testing** → Will be covered in M17/M18

### 1.1 The Traffic Reality

IonWave's early traffic (~50-100 visitors/day, 1,500-3,000/month) makes traditional A/B testing of on-site elements difficult. The framework below accounts for this by:
1. Recommending qualitative methods at very low traffic
2. Using Bayesian methods for faster decisions when possible
3. Reserving frequentist A/B testing for high-impact decisions
4. Matching test methodology to traffic tier

---

## 2. What to Test On-Site (Priority Order)

### 2.1 Testing Priority Matrix

| Priority | Element | Expected Impact | Traffic Needed | Method |
|----------|---------|----------------|---------------|--------|
| 1 | **Headline** | 20-50% CVR lift possible | 500+ per variant | Bayesian A/B |
| 2 | **Hero image/video** | 15-40% CVR lift | 500+ per variant | Bayesian A/B |
| 3 | **Subscription-first default** | 15-30% sub rate change | 500+ per variant | Bayesian A/B |
| 4 | **Price/offer display** | Variable (use M10) | 2,000+ per variant | Sequential (M10) |
| 5 | **Social proof placement** | 5-15% CVR lift | 1,000+ per variant | Bayesian A/B |
| 6 | **Page length** (long vs short) | 5-20% CVR lift | 1,000+ per variant | Pre/post |
| 7 | **CTA text** | 3-10% CVR lift | 2,000+ per variant | Bayesian A/B |
| 8 | **Testimonial format** (video vs text) | 5-15% CVR lift | 1,000+ per variant | Pre/post |

### 2.2 Do NOT Test (First 6 Months)

| Element | Why Not |
|---------|---------|
| Button colors | <1% effect — undetectable without 50K+ visitors |
| Font changes | No meaningful conversion impact at any traffic level |
| Minor copy tweaks ("Buy Now" vs "Add to Cart") | <1% effect |
| Multiple simultaneous redesign changes | Learn nothing about what worked |
| Navigation layout micro-changes | Use heatmaps, then just fix problems |
| Checkout flow details | Too few conversions to measure. Fix obvious issues without testing. |

---

## 3. Statistical Methodology

### 3.1 When to Use Each Method

| Traffic Level | Method | Decision Rule |
|--------------|--------|---------------|
| <30 visits/day | **Qualitative judgment** | Heatmaps, session recordings, customer feedback. Ship best guess. |
| 30-100 visits/day | **Pre/post + Bayesian** | Run version A for 2 weeks, then version B. Or use Bayesian with early-stopping. |
| 100-500 visits/day | **Standard A/B (Bayesian)** | Simultaneous split test. Bayesian for faster results. |
| 500+ visits/day | **Full A/B (frequentist or Bayesian)** | Standard experimentation program with statistical rigor. |

### 3.2 Frequentist A/B Testing

**When to use**: Price tests, checkout changes, subscription terms — anywhere a wrong decision has high financial impact.

| Parameter | Setting |
|-----------|---------|
| Confidence threshold | 95% (p < 0.05) |
| Statistical power | 80% |
| Minimum test duration | 14 days (captures day-of-week variance) |
| Peeking policy | No peeking before planned sample size |

**Sample Size Requirements** (per variant, 95% confidence, 80% power):

| Baseline CVR | 30% relative MDE | 20% relative MDE | 15% relative MDE |
|-------------|------------------|------------------|------------------|
| 2% | 4,300 | 9,800 | 17,400 |
| 3% | 2,800 | 6,500 | 11,500 |
| 5% | 1,600 | 3,800 | 6,700 |

**Practical implication**: At 3% CVR and 2,000 monthly visitors, detecting a 20% relative effect requires 6,500 visitors per variant = 6.5 months. Only test elements where you expect 30%+ relative improvement.

### 3.3 Bayesian A/B Testing

**When to use**: Landing page elements, headline tests, social proof tests — anywhere faster decisions are worth the slight trade-off in certainty.

| Parameter | Setting |
|-----------|---------|
| Prior | Weakly informative Beta(1,1) for new tests. Informed priors from previous tests for iterations. |
| Decision threshold | 95% probability variant beats control |
| Practical threshold | If expected loss of choosing wrong variant is <0.1% absolute CVR, ship it |

**Why Bayesian is better at low traffic**:
- No fixed sample size — check results any time without inflating false positives
- Intuitive output: "93% chance variant B is better" (vs. "p = 0.07, not significant")
- Expected loss framework: "If I'm wrong, I lose 0.05% CVR" — helps make decisions when sample is small
- Can incorporate prior knowledge from previous tests

**Practical rule** (Stucchio framework): Run until 100+ total conversions or a time limit. Then check:
1. P(B > A) > 75% AND expected loss < 0.5% absolute CVR → Ship B
2. P(B > A) between 50-75% after time limit → Effect probably too small to matter
3. P(B > A) < 50% → Keep A

**Expected loss thresholds for IonWave:**
- Landing page changes: ship if expected loss < 0.1% absolute CVR
- Creative decisions: ship if expected loss < 0.5% absolute CVR
- Price/checkout changes: use frequentist (95%), not Bayesian

**Low-conversion warning** *(Dialogue upgrade UPG-4)*: Bayesian analysis with <30 conversions per variant is **directional only** — it tells you which way the wind blows, not where the ball lands. At 500 visitors and 3% CVR = 15 conversions per variant, treat Bayesian results as "probably better" not "confidently better." Only use to choose between two options when the cost of being wrong is low and reversible.

### 3.4 Pre/Post Testing

**When simultaneous split testing isn't possible** (very low traffic, major redesigns, or Shopify limitations):

1. Run version A for 2-4 weeks. Record daily CVR, RPV, sessions.
2. Switch to version B for 2-4 weeks.
3. Compare metrics while controlling for: day-of-week patterns, ad spend levels, traffic source mix, promotions, and seasonality.
4. Change only ONE thing between periods.

**Limitations**: Confounding variables (traffic mix, seasonality) weaken conclusions. Use for directional signals, not definitive answers.

### 3.5 The "Just Ship It" Threshold

Not everything needs a test. Ship without testing when:
- The change is obviously better (fixing broken UX, adding missing CTA)
- The potential downside is tiny (email copy tweak)
- You'd need 6+ months to detect the effect size
- Customer feedback overwhelmingly points in one direction
- You're choosing between two options and neither is risky

**Never "just ship it" on**: Price changes, subscription terms, checkout flow changes, or anything affecting revenue per visitor. These always get tested.

---

## 4. Testing Tools — Post-Google Optimize

**Google Optimize was shut down September 2023.** Danilo's original framework referenced it. Below is the current landscape.

### 4.1 Recommended Tool Stack by Phase

#### Phase 0: $0/month (Pre-revenue, <100 visitors/day)

| Function | Tool | Cost |
|----------|------|------|
| Session recordings + heatmaps | Microsoft Clarity | $0 (unlimited, fully free) |
| Analytics | Shopify Analytics + GA4 | $0 |
| Statistical significance | ABTestGuide.com calculator | $0 |
| On-site "testing" | Manual sequential (change page, compare in GA4) | $0 |

#### Phase 1: $0-50/month (100+ visitors/day, 3,000+/month)

| Function | Tool | Cost |
|----------|------|------|
| On-site A/B testing | Neat A/B Testing (Shopify app) | Free plan or $29/month |
| Landing page testing | Shoplift (Shopify app, Bayesian methodology) | Free plan or $49/month |
| Email A/B testing | Klaviyo built-in | $0 beyond Klaviyo sub |

#### Phase 2: $50-200/month (Revenue > $5K/month)

| Function | Tool | Cost |
|----------|------|------|
| Price A/B testing | Intelligems | ~$99/month |
| On-site A/B testing | Neat A/B ($49-99 tier) or Shoplift ($49 tier) | $49-99/month |

[Confidence: B | Source: Shopify App Store, tool documentation. Pricing should be verified — tools change plans frequently.]

### 4.2 Tool Comparison

| Tool | Cost | Free Plan | Real Price Testing | Shopify Native | Statistical Method |
|------|------|-----------|-------------------|---------------|-------------------|
| **Neat A/B** | $0-199 | Yes | No | Yes | Frequentist |
| **Shoplift** | $0-149 | Yes | No | Yes | Bayesian |
| **Intelligems** | $99-399 | No (trial) | **Yes** | Yes | Frequentist (RPV) |
| **Trident AB** | $0-29 | Yes | No | Yes | Frequentist |
| Convert.com | $199+ | No | Display only | No (JS snippet) | Both |
| VWO | $99-199+ | No | Display only | No (JS snippet) | Bayesian |

**Key insight**: Intelligems is the only Shopify-native tool that does real price testing (different actual prices in cart/checkout). This is what M10's price testing framework needs for PT-002 onwards.

### 4.3 Analytics & Attribution

| Tool | Cost | When It's Worth It |
|------|------|--------------------|
| Shopify Analytics + GA4 | $0 | Always (baseline) |
| Microsoft Clarity | $0 | Always (session recordings, heatmaps) |
| Triple Whale | $100-300/month | When ad spend > $15-20K/month |
| Northbeam | $400-1K+/month | When ad spend > $50K/month |

**Under $10K/month ad spend**: UTM parameters + GA4 + Shopify Analytics + a spreadsheet is sufficient. Attribution tools optimize the marginal 5-15% — not enough savings to justify the cost.

---

## 5. Testing Velocity by Stage

| Stage | Monthly Visitors | On-Site Tests/Month | Ad Creative Tests/Month | Focus |
|-------|-----------------|---------------------|------------------------|-------|
| Pre-launch | <1,000 | 0-1 | 2-4 | Creative testing only (platform has traffic) |
| Early (Mo 1-3) | 1K-3K | 1-2 | 4-8 | Find winning creative angles. 1 LP change/month. |
| Growing (Mo 3-6) | 3K-15K | 2-4 | 8-12 | Systematic program. Creative + LP in parallel. |
| Scaling (Mo 6+) | 15K+ | 4-8 | 12-20 | Full program: creative + LP + email + checkout. |

---

## 6. Landing Page Testing Playbook

### 6.1 IonWave Landing Page Test Queue

| Priority | Test ID | Element | Control | Variant | Expected Effect | Method |
|----------|---------|---------|---------|---------|----------------|--------|
| 1 | LP-001 | Headline | "Marine Electrolytes — 78 Ocean Minerals" | "Your Body Runs on Ocean Minerals. Give It What It Needs." | 20-40% CVR change | Bayesian |
| 2 | LP-002 | Hero visual | Product pack shot on white | Product dissolving in water (dynamic) | 15-30% CVR change | Bayesian |
| 3 | LP-003 | Sub-first default | One-time default, sub as option | Subscription pre-selected, one-time as downgrade | 15-30% sub rate change | Bayesian |
| 4 | LP-004 | Social proof | Reviews below fold | Reviews in hero section + sticky review bar | 10-20% CVR change | Pre/post |
| 5 | LP-005 | Page length | Full long-form (ingredient science, founder story, FAQ) | Short-form (hero + benefits + reviews + CTA) | Variable | Pre/post |

### 6.2 Testing Rules for Landing Pages

1. **One test at a time on the same page** — unless the tests affect completely independent sections
2. **Minimum 14-day duration** — captures day-of-week variance
3. **All traffic sources in the same test** — no paid-only or organic-only splits
4. **Document the hypothesis BEFORE launching** — file the experiment card in test_log.json
5. **Exclude returning customers from first-impression tests** — they've already formed opinions

---

## 7. Audience Testing Strategy

### 7.1 IonWave Audience Tiers (from Danilo tab 376 — expanded)

| Tier | Audience | Description | Testing Priority |
|------|----------|-------------|-----------------|
| **Core** | Health-conscious 25-45 | Broad health + supplements interest | Test FIRST — this is the broadest viable audience |
| **Expansion 1** | Athletes / fitness | CrossFit, running, endurance sports, gym | Test at Month 2-3 after core is validated |
| **Expansion 2** | Biohackers / optimization | Fasting, nootropics, quantified self | Test at Month 2-3 — potentially highest CVR but smallest pool |
| **Expansion 3** | Wellness parents | Family health, organic food, clean living | Test at Month 4+ |
| **Lookalikes** | Based on purchasers | 1% lookalike of first 100+ customers | Available only after 100+ purchases |

### 7.2 Audience Testing Rules

1. **Test CREATIVE first, audiences LAST.** At $1-2K/month, you cannot afford to dilute creative testing budget with audience tests.
2. **Use broad targeting initially.** Let Meta's algorithm find your audience. Interest stacking at low spend restricts the algorithm's ability to optimize.
3. **Only test audiences when you have a proven creative winner.** Hold creative constant, change only the audience.
4. **1% Lookalike is the unlock.** Once you have 100+ customers, build a 1% Lookalike of purchasers. This typically outperforms interest targeting.

### 7.3 Audience Test Protocol

```
Prerequisite: At least 1 creative winner (CT-XXX graduated to scaling)

Test structure:
  ABO campaign, $20-30/day per ad set
  Same winning creative in every ad set
  Ad Set 1: Core audience (health-conscious, broad)
  Ad Set 2: Expansion audience being tested
  Duration: 7-14 days
  Primary metric: CPA
  Secondary: CVR, subscription rate, AOV

Decision:
  Expansion CPA ≤ 1.2x Core CPA → Add to targeting rotation
  Expansion CPA > 1.5x Core CPA → Kill this audience for now
  Between 1.2-1.5x → Iterate (narrow further or test different interests)
```

---

## 8. Intelligence Gaps

| ID | Gap | Grade | Upgrade Path |
|----|-----|-------|-------------|
| GAP-1 | Google Optimize recommended in Danilo original — now dead | FIXED | Replaced with current tool recommendations |
| GAP-2 | 3 duplicate A/B tabs provided no net new methodology | FIXED | Consolidated into single authoritative framework |
| GAP-3 | No IonWave on-site test data exists | D | Run first 3 LP tests. Calibrate benchmarks. |
| GAP-4 | Shopify app pricing may have changed since research | C | Verify Neat A/B, Shoplift, Intelligems pricing before purchase |
| GAP-5 | Bayesian priors not calibrated for marine plasma supplement | D | After 10+ tests, build category-specific priors |


---

### 📄 audience_testing_strategy.md

# Audience Testing Strategy — M14: Testing & Optimization

**TUP**: M14 | **Tab**: 2 of 6
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-001 (CAC), HYP-009 (Pre-Launch Demand)
**Danilo Source**: ops_model_v10_dump/376_audience_strategy.json (5 rows — skeleton with audience tiers only)
**Cross-references**: data/m27_customer_research/ (ICP analysis, customer archetypes), data/m14/creative_testing_protocol.md (creative tests before audience tests)

---

## 1. Core Principle

**Test creative FIRST, audiences LAST.**

At $500-2K/month ad spend, audience testing competes for the same limited budget as creative testing. Creative variables (hook, angle, format) have 3-5x more impact on CPA than audience targeting at this budget. Meta's algorithm is better at finding your audience than manual interest stacking — if you give it good creative.

**When to start audience testing:**
- You have at least 1 proven creative winner (graduated from testing to scaling)
- Monthly ad spend is ≥ $1,500 (enough to allocate $300-500 to audience tests)
- You have at least 4 weeks of campaign data

---

## 2. Audience Tiers

### 2.1 Tier Architecture

| Tier | Audience | Description | Est. Size (US) | Test Priority | Expected CPA vs Core |
|------|----------|-------------|----------------|--------------|---------------------|
| **0: Broad** | 25-55, US, all interests | Let Meta's algorithm optimize | 100M+ | DEFAULT — use from Day 1 | Baseline |
| **1: Core** | Health-conscious, supplement buyers | Interest: health, supplements, nutrition, wellness | 20-40M | Month 1-2 | 0.8-1.0x |
| **2A: Athletes** | Fitness enthusiasts, endurance athletes | Interest: CrossFit, running, triathlon, gym, Strava | 15-25M | Month 2-3 | 0.9-1.2x |
| **2B: Biohackers** | Optimization community | Interest: fasting, nootropics, biohacking, quantified self | 3-8M | Month 2-3 | 0.7-1.0x (potentially best) |
| **3: Wellness parents** | Family health decision makers | Interest: organic food, clean living, family wellness | 10-20M | Month 4+ | 1.0-1.3x |
| **4: Lookalike 1%** | Statistically similar to buyers | Based on first 100+ purchasers | Varies | After 100+ customers | 0.6-0.9x (typically best) |
| **5: Lookalike 3-5%** | Broader lookalike | Wider net for scaling | Varies | After Lookalike 1% proven | 0.8-1.1x |

### 2.2 Danilo's Original vs. Expanded

Danilo listed 5 audiences in a single row each. Expanded:

| Danilo Original | What Was Missing | What We Added |
|----------------|-----------------|--------------|
| "Health-conscious 25-45" | No targeting details, no size estimate | Interest stack, estimated reach, CPA expectation |
| "Athletes, fitness enthusiasts" | No sub-segmentation | Split CrossFit/endurance vs gym-general |
| "Biohackers, optimization community" | No size estimate | Estimated 3-8M US reach, flagged as potentially highest CVR |
| "Wellness moms, family health" | Gender assumption | Broadened to "wellness parents," deferred to Month 4+ |
| "Lookalikes" | No threshold for when to build | Specified: 100+ customers minimum for viable 1% LAL |

---

## 3. Testing Protocol

### 3.1 Prerequisites

Before running any audience test:
- [ ] At least 1 creative winner exists (CT-XXX graduated to scaling campaign)
- [ ] Monthly ad spend ≥ $1,500
- [ ] 4+ weeks of campaign performance data
- [ ] Creative held CONSTANT across all audience tests (same winning creative in every ad set)

### 3.2 Standard Audience Test Structure

```
Campaign: ABO (Ad Set Budget Optimization)
Budget: $20-30/day per ad set
Duration: 7-14 days

Ad Set 1: Control audience (Tier 0 Broad or Tier 1 Core)
  → Same winning creative
Ad Set 2: Test audience (the audience being evaluated)
  → Same winning creative
Ad Set 3: (Optional) Second test audience
  → Same winning creative

Primary metric: CPA
Secondary: CVR, subscription rate, AOV, ROAS
Diagnostic: CPM (audience cost), CTR (message-audience fit)
```

### 3.3 Decision Rules

| Outcome | Criteria | Action |
|---------|----------|--------|
| **Add to rotation** | Test CPA ≤ 1.2x Control CPA | Include in scaling campaign targeting |
| **Iterate** | Test CPA 1.2-1.5x Control CPA | Try narrower interest stack or different creative angle for this audience |
| **Kill** | Test CPA > 1.5x Control CPA | This audience doesn't respond at current price. Revisit at $5K+ spend. |
| **Replace control** | Test CPA < 0.8x Control CPA | This audience is better than your current default. Switch. |

### 3.4 Audience × Creative Interaction

The most powerful tests combine audience AND creative — a specific message for a specific audience:

| Audience | Best Creative Angle (Hypothesis) |
|----------|--------------------------------|
| Athletes | Performance + recovery ("Replace what you sweat out with 78 minerals") |
| Biohackers | Ingredient science + completeness ("78 trace elements. Zero fillers.") |
| Wellness parents | Purity + family safety ("From the deep ocean, not a lab") |
| Health-conscious general | Problem → solution ("Tired by 2pm? Your electrolytes are incomplete.") |

These are hypotheses to test, not facts. The creative testing protocol may surface different winning angles for each audience.

---

## 4. Phased Rollout

### Phase 0: Month 1-2 (Launch) — Passive Audience Learning

*(Dialogue upgrade UPG-6)*

- **Targeting**: Broad (Tier 0) only
- **Why**: Let Meta's algorithm learn with no constraints. Interest stacking at low spend restricts the algorithm.
- **Ad spend**: 100% of budget on creative testing with broad targeting.
- **Passive learning**: You don't need dedicated audience tests to learn about your audience. After 7+ days of broad targeting, Meta's reporting gives you FREE audience data:
  1. **Ads Manager → Breakdown → By Age**: Which age groups convert? Tells you whether to narrow later.
  2. **Breakdown → By Gender**: Does one gender convert at meaningfully different CPA?
  3. **Breakdown → By Placement**: Feed vs Reels vs Stories — where does your creative work?
  4. **Breakdown → By Region**: Any geographic patterns?
  5. **Breakdown → By Platform**: Instagram vs Facebook performance gap?

  **Action**: Review breakdowns weekly. Build a profile of "who is actually buying" from real data. This replaces explicit audience tests at Phase 0 — Meta already tested the audiences for you. Only run formal audience tests (Phase 1+) when breakdowns show clear segmentation opportunities the algorithm isn't exploiting.

### Phase 1: Month 2-3 (First Audience Tests)
- **Test**: Core (Tier 1) vs Broad (Tier 0)
- **Then**: Athletes (Tier 2A) vs Core (Tier 1)
- **And**: Biohackers (Tier 2B) vs Core (Tier 1)
- **Budget**: 20-30% of monthly spend on audience tests

### Phase 2: Month 4-6 (Lookalike + Expansion)
- **Build**: 1% Lookalike of purchasers (requires 100+ customers)
- **Test**: Lookalike 1% vs best-performing interest audience
- **Test**: Wellness parents (Tier 3) vs Core
- **Budget**: 15-25% of spend on audience tests (the rest on creative iteration)

### Phase 3: Month 6+ (Scaling)
- **Scale**: Best 2-3 audiences with proven creative
- **Test**: Lookalike 3-5% for broader reach
- **Begin**: Audience × creative interaction tests
- **Budget**: Systematic allocation based on CPA by audience

---

## 5. Retargeting Audiences

### 5.1 When to Start Retargeting
- **Minimum**: 1,000 monthly site visitors (enough for a viable retargeting pool)
- **At $500-1K/month total spend**: Skip dedicated retargeting. Meta Advantage+ handles this automatically.
- **At $2K+/month**: Consider 5-10% of budget on retargeting

### 5.2 Retargeting Audiences (When Ready)

| Audience | Window | Priority |
|----------|--------|----------|
| Site visitors (non-purchasers) | 7 days | 1 — hottest leads |
| Add-to-cart abandoners | 7 days | 1 — highest intent |
| Site visitors (non-purchasers) | 30 days | 2 |
| Page viewers (product page) | 14 days | 2 |
| Video viewers (75%+ watched) | 30 days | 3 — brand-aware |
| Instagram/Facebook engagers | 30 days | 3 |

### 5.3 Retargeting Creative

Retargeting creative should be DIFFERENT from prospecting:
- Prospecting: Problem/benefit hooks to generate interest
- Retargeting: Objection-handling (price justification, testimonials, guarantee), urgency (limited stock), social proof (review compilations)

---

## 6. Intelligence Gaps

| ID | Gap | Grade | Upgrade Path |
|----|-----|-------|-------------|
| GAP-1 | No IonWave audience data exists | D | First 4 weeks of Meta ads provide initial audience signals. CPA by age/gender/interest from Meta reporting. |
| GAP-2 | Biohacker audience size estimate unverified | C | Verify reach in Meta Ads Manager audience builder before test launch. |
| GAP-3 | Lookalike requires 100+ customers | D | Track customer count. At ~$45 CPA, need ~$4,500 in total spend to reach 100 customers. |
| GAP-4 | Audience × creative interaction is hypothesis only | D | Validated by testing each audience with the angle hypothesized above vs. generic winner. |


---

### 📄 creative_testing_protocol.md

# Creative Testing Protocol — M14: Testing & Optimization

**TUP**: M14 | **Tab**: 1 of 6
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-001 (CAC), HYP-002 (Subscription Conversion)
**Danilo Sources**: ops_model_v10_dump/375_creative_testing_protocol.json (5 rows — skeleton), ops_model_v10_dump/348_creative_testing_protocol1.json (37 rows — M12 reference, more substantive)
**Cross-references**: data/m22/ugc_brand_brief.md (approved claims), data/m22/ugc_creator_program.json (creator economics)

---

## 1. Testing Philosophy

### 1.1 Core Principle
**Creative is the #1 lever for a bootstrapped DTC brand on Meta/TikTok.** At $500-2K/month ad spend, you cannot out-bid competitors. You can only out-create them. Every creative test is a hypothesis about what resonates with your ICP — not a random variation.

### 1.2 Budget Reality Check

| Monthly Ad Spend | Daily Budget | Testable Creatives/Month | Meaningful Winners Expected |
|-----------------|-------------|--------------------------|----------------------------|
| $500 | ~$16/day | 3-4 | 0-1 (survival mode) |
| $1,000 | ~$33/day | 4-6 | 0-1 |
| $1,500 | ~$50/day | 6-8 | 1 |
| $2,000 | ~$66/day | 8-10 | 1-2 |

[Confidence: B | Source: DTC practitioner consensus, Common Thread Collective, Foxwell Digital]

**At 10% hit rate and 5 creatives/month tested, expect ~1 winner every 2 months.** This is why iteration on proven angles matters more than constant net-new concepts at low budget.

### 1.3 Hit Rates by Creative Type

| Creative Type | Hit Rate (% becoming "winners") | Notes |
|--------------|--------------------------------|-------|
| Net-new concepts (different angle/format) | 5-15% | High risk, high learning value |
| Iterations on proven winners (new hook, same concept) | 20-35% | Lower risk, compounds learning |
| Hook variations on winning body | 25-40% | Cheapest to produce, fastest iteration |

[Confidence: C | Source: Agency case studies, Motion analytics platform data]

---

## 2. Testing Hierarchy — What to Test First

### 2.1 Priority Order (Highest Impact First)

**Tier 1: CONCEPT / ANGLE** — The biggest lever

> "What story are we telling? What pain point? What desire?"

Test fundamentally different persuasion approaches before anything else. At IonWave's budget, you cannot afford to waste test slots on minor variations until you've found a concept that resonates.

IonWave concept candidates:
- **Ocean purity origin**: "From 2,000 feet deep in the Pacific"
- **Athletic performance**: "Why athletes are switching from lab-made electrolytes"
- **Anti-synthetic ingredients**: "78 minerals. Zero synthetic fillers."
- **Daily wellness ritual**: "This changed my morning routine"
- **Problem → solution**: "Tired by 2pm? Your electrolytes are incomplete."

**Tier 2: FORMAT** — Second biggest lever

| Format | Best For | Production Cost | Testing Priority |
|--------|---------|----------------|-----------------|
| UGC testimonial | Social proof, relatability | $50-150/video (M22 creator program) | HIGH — test early |
| Founder-to-camera | Trust, origin story, premium positioning | $0 (in-house) | HIGH — free to produce |
| Product demo | Visual differentiation (ocean minerals dissolving) | $0-50 (in-house) | MEDIUM |
| Static image | Quick production, headline testing | $0-25 (Canva/AI) | MEDIUM |
| Carousel | Educational, ingredient breakdowns | $0-25 | LOW at launch |

**Tier 3: HOOK** — Third in impact, but fastest to test

The first 3 seconds (Meta) or 1-2 seconds (TikTok) determine if anyone sees your ad. Once you have a winning concept + format, hook testing is the cheapest way to iterate.

Hook frameworks (from M22 UGC brand brief):
1. **Problem statement**: "Tired by 2pm? Your electrolytes are wrong."
2. **Counter-intuitive**: "Why your electrolytes are making you MORE dehydrated"
3. **Social proof**: "I quit [popular brand] for this and here's why"
4. **Question**: "Did you know your body is missing 75 essential minerals?"
5. **Demonstration**: [Product dissolving in water — visual hook]
6. **Authority**: "My nutritionist told me to stop taking synthetic electrolytes"
7. **Comparison**: "3 minerals vs 78 minerals — which would you choose?"
8. **Urgency/FOMO**: "This sold out twice last month"

**Tier 4+: BODY, CTA, AUDIENCE** — Test AFTER tiers 1-3

Body content, call-to-action text, and audience targeting should be iterated only after concept, format, and hook have been validated. At $1-2K/month, audience testing is wasteful — let Meta's algorithm find your audience.

### 2.2 Is "Isolate One Variable" Practical at Low Budget?

**No.** At 3-5 creatives per month, strict single-variable testing would take 6+ months to learn what a smarter approach teaches in 6 weeks.

**The pragmatic alternative:**
- **Month 1-2**: Test 3-4 fundamentally different concepts simultaneously. You're looking for the concept that resonates, not isolating variables.
- **Month 2-3**: Take the winning concept and test 3-4 variations of hook/format. Now you're closer to single-variable testing.
- **Month 3+**: Hook velocity testing — 3-5 new hooks per week on the proven body.

---

## 3. Meta Ads Testing Framework

### 3.1 Campaign Structure

```
TESTING CAMPAIGN (ABO, 30-40% of budget)
  Purpose: Find winners
  Budget: Ad Set Budget Optimization (NOT CBO)
  Reason: CBO starves underperformers before data accumulates
  Structure:
    Ad Set 1: Creative A ($15-20/day)
    Ad Set 2: Creative B ($15-20/day)
    Ad Set 3: Creative C ($15-20/day)
  Targeting: Broad (US, 25-55, no interest stacking)
  Duration: 3-7 days per batch

SCALING CAMPAIGN (CBO or Advantage+, 60-70% of budget)
  Purpose: Spend efficiently on proven winners
  Budget: Campaign Budget Optimization
  Structure:
    Ad Set: Broad (graduated winners only)
      Winning Creative 1
      Winning Creative 2
      Winning Creative 3

RETARGETING (optional, 0-10% of budget)
  Only when site traffic > 1,000/month
  At $1K/month total spend, skip — Advantage+ handles this
```

[Confidence: B | Source: Foxwell Digital, DTC practitioner consensus]

**2025-2026 Advantage+ caveat**: Meta is progressively pushing Advantage+ Shopping Campaigns. If manual ABO becomes unavailable, use Advantage+ for scaling and a manual campaign for testing.

### 3.2 ABO vs CBO for Testing

| Approach | Testing | Scaling |
|----------|---------|---------|
| **ABO** | PREFERRED — gives each creative equal spend | Less efficient |
| **CBO** | BAD — allocates 80%+ to one ad set at $33/day | Good for scaling winners |

### 3.3 Dynamic Creative Testing (DCT)

**Not recommended at IonWave's budget.** DCT optimizes for Meta's chosen combination but obscures which element won. At $30/day, it becomes a black box with no actionable learning. Exception: testing 5+ static image headline variations in a single DCT ad set works as a lightweight screen.

---

## 4. Kill/Scale Decision Framework

### 4.1 IonWave-Specific Thresholds

Calibrated for $59 subscription product, ~$45 target CPA:

**Stage 1: Leading Indicators (Day 3 — BEFORE conversion data exists)**

| Metric | Kill Threshold | Data Minimum |
|--------|---------------|-------------|
| CTR (link) | < 0.5% | 1,000+ impressions |
| Hook rate (video) | < 20% 3-sec view rate | 1,000+ impressions |
| CPM | > $40 (audience cost too high) | 1,000+ impressions |
| Frequency | > 2.5 | Any time |

**Stage 2: Conversion Indicators (Day 5-7 — after 50+ link clicks)**

*(Dialogue upgrade UPG-3: At $59 AOV and 3% CVR, you need ~33 clicks for 1 conversion. At $1.50-3.00 CPC, that's $50-100 for your FIRST conversion. Never kill based on CPA until you have 50+ link clicks — otherwise you're killing creatives that simply haven't had a chance to convert yet.)*

| Metric | Kill Threshold | Data Minimum |
|--------|---------------|-------------|
| CPA | > $67 (1.5x target) | **50+ link clicks** (not just spend) |
| Add to Cart rate | < 3% of link clicks | 50+ link clicks |
| ROAS | < 1.0x | $100+ spent AND 50+ clicks |

[Confidence: B | Source: Agency consensus frameworks, adjusted for IonWave economics]

### 4.2 Day-by-Day Decision Protocol (Two-Stage)

```
Day 1-2: DO NOTHING.
  Let Meta exit learning phase. Don't touch anything.

Day 3: STAGE 1 CHECK (leading indicators only).
  < 500 impressions → Budget or targeting issue. Increase budget or broaden.
  CTR < 0.5%        → Hook is dead. KILL.
  Hook rate < 20%    → First frame isn't stopping scrollers. KILL.
  CTR ≥ 0.8%        → Creative is engaging. CONTINUE regardless of conversions.

Day 5: STAGE 2 CHECK (conversion indicators — IF 50+ link clicks).
  < 50 link clicks   → Don't make CPA decisions yet. Continue to Day 7.
  50+ clicks, 0 conv → Landing page issue OR audience mismatch. Check LP before killing.
  50+ clicks, CPA ≤ $45 → Strong signal. Continue to Day 7 for confirmation.
  50+ clicks, CPA > $67 → KILL.

Day 7: FINAL DECISION.
  CPA ≤ target ($45)          → GRADUATE to scaling campaign.
  CPA 1-1.3x target ($45-59)  → ITERATE (new hook on same body).
  CPA > 1.3x target ($59+)    → KILL.
  < 50 link clicks at Day 7   → Budget too low or creative not engaging. KILL or extend 3 days.
```

### 4.3 Sunk Cost Discipline

*(Dialogue upgrade UPG-8)*

The hardest decision at $500-1K/month is killing a creative that's "almost working." Every dollar feels precious. This leads to the worst possible behavior: continuing to spend on marginal creatives hoping they'll turn around.

**The rule**: Once you've spent 1.5x target CPA ($67) with zero conversions AND 50+ link clicks, the money is gone regardless. Killing doesn't waste the spend — it prevents MORE waste. The learning from a killed creative (what DIDN'T work) has the same value as a winner (what DID work) if you document it.

**Reframe**: You're not spending $67 to "see if this works." You're spending $67 to learn whether this creative angle resonates. Either outcome is information. The only waste is spending $67 and learning nothing because you didn't record the result.

### 4.4 What a "Winner" Looks Like

| Tier | Criteria | Action |
|------|----------|--------|
| **Winner** (top 10%) | CPA < $45, CTR > 1.5%, holds 7+ days | Scale: increase budget 20-30% every 3 days |
| **Performer** (top 25%) | CPA $45-55, CTR > 1.0%, holds 5+ days | Maintain + iterate with new hooks |
| **Marginal** (50th pctl) | CPA $55-70, CTR 0.8-1.0% | Test 2-3 hook variations before killing |
| **Loser** (bottom 50%) | CPA > $70 or CTR < 0.8% | Kill after $50-70 spent |

---

## 5. Creative Scaling Protocol

*(Dialogue upgrade UPG-9)*

### 5.1 From Testing to Scaling

When a creative graduates from the testing campaign (CPA ≤ $45, CTR > 1.5%, Day 7):

```
STEP 1: GRADUATE (Day 7-8)
  Move winning creative to scaling campaign (CBO or Advantage+).
  Initial scaling budget: 2x testing budget for that creative.
  Example: tested at $15/day → scale to $30/day.

STEP 2: RAMP (Day 8-20)
  Increase budget 20-30% every 3 days IF CPA stays within target.
  $30 → $40 → $52 → $67 → $87...
  Monitor CPA daily. If CPA spikes >20% after a budget increase,
  hold for 48 hours before increasing again.

STEP 3: STABILIZE (Day 20+)
  When budget increase causes CPA to rise above 1.3x target ($59),
  you've hit the creative's ceiling. HOLD at the last stable budget.
  This is the creative's "cruising altitude."

STEP 4: MAINTAIN (ongoing)
  At cruising altitude, monitor weekly:
  - CPA trending up? → Early fatigue. Start producing replacement.
  - CTR declining? → Audience saturation. Expand targeting or refresh hook.
  - ROAS stable? → Don't touch it. Let it run.
```

### 5.2 When to Stop Scaling

| Signal | Meaning | Action |
|--------|---------|--------|
| Budget increase causes CPA > 1.3x target | Hit the creative's spend ceiling | Hold at last stable level |
| Frequency > 3.0 in broad targeting | Audience exhaustion at this budget | Can't scale further without new audiences |
| CPA rising 3 days in a row | Beginning of fatigue cycle | Reduce budget 30%, start replacement |
| Adding $100/day yields <$100 incremental revenue | Diminishing returns | Maintain, don't scale |

---

## 6. Creative Fatigue

### 5.1 Decay Rates at Low Spend

| Monthly Spend | Typical Creative Lifespan |
|--------------|--------------------------|
| $500-1K | 4-8 weeks |
| $1K-3K | 3-6 weeks |
| $3K-10K | 2-4 weeks |
| $10K+ | 1-3 weeks |

[Confidence: C | Source: Motion analytics data, DTC practitioner reports]

### 5.2 Fatigue Signals

**Early warning (act within 3-5 days):**
1. Frequency climbing above 2.5
2. CTR declining 20%+ from peak
3. CPM increasing 15-25%+ from baseline

**Confirmed fatigue (act immediately):**
4. CPA increasing 30%+ over 5-7 day moving average
5. CTR drops below 0.7% from 1.2%+ baseline
6. ROAS drops below breakeven

**Response protocol**: Reduce budget 30-50% to extend life while preparing replacement. Launch replacement in testing campaign. Never increase budget on a fatigued creative.

### 5.3 New Creative Volume Required

| Monthly Spend | New Creatives/Month | Mix |
|--------------|---------------------|-----|
| $500-1K | 3-5 | 1-2 new concepts + 2-3 iterations |
| $1K-2K | 5-8 | 2-3 new concepts + 3-5 iterations |
| $2K-5K | 8-15 | 3-5 concepts + 5-10 iterations |

"New creative" includes lightweight production: re-cutting a winning video with a new hook (30 min), turning a UGC screenshot into a static ad, changing a headline overlay on a proven format.

---

## 6. Creative Brief → Test → Learn → Iterate Loop

### 6.1 Two-Week Cycle

```
PHASE 1: BRIEF (Day 1)
  Define concept/angle being tested
  Write hypothesis: "We believe [audience] will respond to
    [message] because [reason]"
  Specify format, hook approach, CTA, offer
  Reference prior learnings
  Assign naming convention code

PHASE 2: PRODUCE (Day 2-5)
  Create asset (video, image, copy)
  Video: film/edit with 2-3 hook variations
  Static: create 2-3 headline variations
  Quality check against M22 UGC Brand Brief (approved claims)

PHASE 3: TEST (Day 5-12)
  Launch in testing campaign (ABO, $15-20/day per creative)
  Follow Day-by-Day Decision Protocol (Section 4.2)

PHASE 4: LEARN (Day 12-13)
  Log outcome in test_log.json (Winner/Performer/Marginal/Loser)
  Write 1-2 sentence learning
  Compare to prior tests for emerging patterns

PHASE 5: ITERATE (Day 13-15)
  Winner → Graduate to scaling, plan 2-3 hook variations
  Performer → Test 2 new hooks on same body
  Marginal → Test different format with same concept
  Loser → Archive learnings, next concept
```

**Cycle time**: 2 weeks per loop. **Monthly cadence**: 2 full loops minimum.

### 6.2 Naming Convention

```
[Date]_[Platform]_[Format]_[Concept]_[HookVariant]_[Version]

Examples:
2026-02_META_UGC_OceanPurity_HookA_v1
2026-02_META_STATIC_AthletePerformance_Headline3_v2
2026-02_TT_SPARK_MorningRoutine_HookB_v1
```

### 6.3 Per-Creative Tracking Fields

Every creative gets logged in test_log.json with:
- Creative ID (naming convention), launch/kill dates, platform, campaign
- Format, concept/angle, hook, CTA, offer, target audience
- Performance: spend, impressions, CPM, clicks, CPC, CTR, purchases, CPA, ROAS, hook rate, hold rate
- Outcome: Winner / Performer / Marginal / Loser
- Learning: 1-2 sentences
- Next action: Scale / Iterate (what specifically?) / Kill

---

## 7. TikTok-Specific Testing

### 7.1 Key Differences from Meta

| Dimension | Meta | TikTok |
|-----------|------|--------|
| Creative style | Polished UGC, direct response | Raw/authentic, entertainment-first |
| Hook window | 3 seconds | 1-2 seconds (faster scroll) |
| Sound | Often off (Feed) | Almost always ON |
| Creative lifespan | 4-8 weeks at low spend | 2-4 weeks (faster cycle) |
| Attribution | Generally reliable with CAPI | View-through attribution inflated |
| Min daily budget | $5/ad set ($15-20 recommended) | $20/ad group (platform-enforced) |

### 7.2 Budget Allocation

**Start 100% Meta. Add TikTok later.**

| Phase | Timeline | Meta | TikTok |
|-------|----------|------|--------|
| Launch | Month 1-3 | 100% | 0% (organic/Spark only) |
| Expansion | Month 4-6 | 70-80% | 20-30% |
| Diversification | Month 6+ | 50-60% | 30-40% |

Exception: If strong TikTok-native UGC is available, consider $200-300/month Spark Ads test in Month 2-3.

### 7.3 Spark Ads Strategy

Send product to 5-10 micro-creators (1K-50K followers in wellness/fitness). Have them post organically. If a post gets organic traction (500+ views, good engagement), boost with Spark Ads. Cheapest way to test creative concepts on TikTok.

---

## 8. IonWave Month 1 Action Plan ($1,000 Budget)

1. **Meta only.** Do not split budget.
2. **Produce 4 creatives** testing fundamentally different concepts:
   - Ocean purity / deep sea origin (UGC or founder video)
   - Athletic performance / electrolyte switch (UGC testimonial)
   - Daily wellness ritual / morning routine (lifestyle UGC)
   - Anti-synthetic / clean label (static comparison ad)
3. **Sequential batches, NOT all at once.** *(Dialogue upgrade UPG-2: At $1K/month = $33/day, you can only fund 1-2 ad sets at $15-20/day simultaneously. Run Batch 1 (2 creatives, $15/day each) for 5-7 days. Kill losers. Run Batch 2 (2 creatives) for 5-7 days.)*
4. **1 ABO testing campaign**, $15-20/day per ad set (max 2 ad sets simultaneously at $1K budget), broad targeting (US, 25-55).
5. **Follow two-stage kill protocol (Section 4.2).** Don't kill on CPA until 50+ link clicks.
6. **Set up creative test log on day 1.** Track everything from the start.

### 8.1 Critical Note for $59 Subscription Model

First-purchase ROAS of 1.0-1.8x is normal and expected for premium subscription DTC. Profitability comes from month 2+ subscription revenue. A creative generating $50 CPA customers who retain for 6 months vastly outperforms one generating $35 CPA that cancel after month 1. Optimize for LTV-to-CAC ratio over time, not just first-purchase CPA.

---

## 9. Benchmarks — DTC Supplement on Meta

| Metric | Low | Median | Good | Excellent |
|--------|-----|--------|------|-----------|
| CPM | $25-35 | $15-25 | $10-18 | <$10 |
| CPC (link) | $3.00+ | $1.50-3.00 | $0.80-1.50 | <$0.80 |
| CTR (link) | <0.8% | 0.8-1.5% | 1.5-2.5% | >2.5% |
| CVR (LP→purchase) | <1.5% | 1.5-3.0% | 3.0-5.0% | >5.0% |
| CPA (first purchase) | >$80 | $40-80 | $25-45 | <$25 |
| ROAS (first purchase) | <1.0x | 1.0-2.0x | 2.0-3.5x | >3.5x |

[Confidence: C | Source: Varos, Revealbot, Databox benchmark reports. IonWave-adjusted: higher CPM ($18-28) for premium US health audience, lower CVR (2-3%) for $59 price point.]

---

## 10. Intelligence Gaps

| ID | Gap | Grade | Upgrade Path |
|----|-----|-------|-------------|
| GAP-1 | No IonWave creative performance data exists | D | Run first 5 creative tests. Calibrate all thresholds with real data. |
| GAP-2 | Creative fatigue rates are category benchmarks, not IonWave-specific | D | Track actual lifespan of first 3 winning creatives. |
| GAP-3 | Meta Advantage+ interface evolving rapidly | C | Verify current ABO availability and test structure monthly. |
| GAP-4 | TikTok benchmarks may not apply to premium supplement | C | Defer TikTok until Month 4+. Validate with small test budget first. |


---

### 📄 dialogue_summary.md

# Persona Dialogue Summary — M14: Testing & Optimization

**TUP**: M14
**Version**: 1.0.0
**Date**: 2026-02-06
**Rounds**: 4
**Saturated**: Yes (Round 4 — all personas confirmed no further upgrades)
**Upgrades Applied**: 9
**Unresolved**: 0

---

## Personas

| Persona | Role | Focus |
|---------|------|-------|
| **CRO Statistician** | Statistical rigor challenger | Sample sizes, methodology, confidence thresholds, error rates |
| **Bootstrapped DTC Founder** | Practicality challenger | Budget constraints, opportunity cost, tool spending, psychology of testing |
| **Growth Hacker (Performance Marketer)** | Tactical challenger | Meta campaign structure, kill criteria, scaling, audience strategy |

---

## Round-by-Round Summary

### Round 1 (3 upgrades)

**CRO Statistician**: 75% Bayesian threshold = 25% false positive rate. Need explicit error disclosure by confidence level.
→ **UPG-1**: Added error_rate_disclosure to experimentation_framework.json with domain-specific thresholds.

**Bootstrapped DTC Founder**: Month 1 action plan math broken — can't run 4-5 ad sets at $15-20/day on $33/day budget.
→ **UPG-2**: Fixed to sequential batches of 2 creatives, not 4-5 simultaneous.

**Growth Hacker**: Kill criteria kills at CPA threshold before creatives can even convert. At 3% CVR and $1.50-3 CPC, first conversion needs $50-100 spend.
→ **UPG-3**: Two-stage kill protocol — Day 3 on leading indicators (CTR/hook rate), Day 5-7 on CPA only after 50+ link clicks.

### Round 2 (3 upgrades)

**CRO Statistician**: Bayesian at 500 visitors / 3% CVR = only 15 conversions per variant. That's directional, not confident.
→ **UPG-4**: Added low-conversion Bayesian warning (<30 conversions = directional only) to ab_testing_framework.md.

**Bootstrapped DTC Founder**: Intelligems at $99/month is 10-20% of a $500-1K ad budget. Need explicit tool-spend-as-%-of-budget guideline.
→ **UPG-5**: Added 5% max tool spend discipline table to testing_infrastructure.md.

**Growth Hacker**: Audience testing section too rigid — Meta's broad targeting IS the audience test. Read breakdowns for free.
→ **UPG-6**: Added passive audience learning section to audience_testing_strategy.md Phase 0.

### Round 3 (3 upgrades)

**CRO Statistician**: PT-000's reported 95% confidence at ~75 total conversions can't reliably detect 23% relative effect. Directional, not definitive.
→ **UPG-7**: Added statistical_note to PT-000 entry in test_log.json.

**Bootstrapped DTC Founder**: Missing psychological discipline — hardest part is killing "almost working" creatives at low budget.
→ **UPG-8**: Added sunk cost discipline section to creative_testing_protocol.md.

**Growth Hacker**: Missing creative scaling protocol — what happens AFTER a winner is found?
→ **UPG-9**: Added 4-step scaling protocol (graduate → ramp → stabilize → maintain) to creative_testing_protocol.md.

### Round 4 (0 upgrades — SATURATED)

All three personas confirmed satisfaction. No further upgrades requested.

**CRO Statistician**: "The framework is honest about what it can and can't measure at low traffic."
**Bootstrapped DTC Founder**: "The sunk cost discipline and tool-spend guideline are exactly what was missing."
**Growth Hacker**: "The creative scaling protocol fills the last gap. Benchmark calibration note is informational, not an upgrade."

---

## Upgrade Register

| ID | File Modified | Change | Persona |
|----|--------------|--------|---------|
| UPG-1 | experimentation_framework.json | Error rate disclosure by confidence threshold (75-95%) | CRO Statistician |
| UPG-2 | creative_testing_protocol.md | Month 1 budget math fix — sequential batches, not simultaneous | DTC Founder |
| UPG-3 | creative_testing_protocol.md | Two-stage kill protocol with 50+ link click minimum | Growth Hacker |
| UPG-4 | ab_testing_framework.md | Low-conversion Bayesian warning (<30 conv = directional) | CRO Statistician |
| UPG-5 | testing_infrastructure.md | Tool spend ≤5% of ad budget discipline table | DTC Founder |
| UPG-6 | audience_testing_strategy.md | Passive audience learning (Meta breakdown reports) | Growth Hacker |
| UPG-7 | test_log.json | PT-000 statistical note (directional, not definitive) | CRO Statistician |
| UPG-8 | creative_testing_protocol.md | Sunk cost discipline section | DTC Founder |
| UPG-9 | creative_testing_protocol.md | Creative scaling protocol (4-step graduate→maintain) | Growth Hacker |


---

### 📄 opkit_testing_optimization.md

# OpKit OK-M14-001: Testing & Optimization Kit

**OpKit ID**: OK-M14-001
**Type**: Production
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Source TUP**: M14 (Testing & Optimization)
**Graded Example**: IonWave Trade #84 (Quality: 7.5/10)

---

## Purpose

Complete experimentation system for DTC consumable brands on Shopify. Covers creative testing on Meta/TikTok, on-site A/B testing, audience strategy, testing infrastructure selection, and the learning system that compounds knowledge over time.

Designed specifically for bootstrapped DTC brands at <5,000 monthly visitors where traditional A/B testing is underpowered.

---

## When to Use This OpKit

Use this when a Trade needs to:
- Set up a testing program from zero
- Choose A/B testing tools for Shopify
- Design creative testing protocols for Meta/TikTok
- Build an audience testing strategy
- Decide between Bayesian and frequentist methodology at their traffic level

---

## Kit Contents

### 1. Experimentation Framework (`experimentation_framework.json`)
**What**: The philosophical backbone — testing principles, experiment card schema, priority matrix, traffic-based methodology, statistical decision rules, learning system.
**Key concepts**: Learning over winning, big swings before small tweaks, match method to traffic, document everything.
**Reusable for any Trade**: Yes — the framework is brand-agnostic. Adjust the priority matrix elements for the specific product category.

### 2. Creative Testing Protocol (`creative_testing_protocol.md`)
**What**: Ad creative testing for Meta/TikTok — testing hierarchy (concept → format → hook), campaign structure (ABO testing → CBO scaling), two-stage kill/scale criteria, creative fatigue management, scaling protocol.
**Key concepts**: Sequential batches at low budget, two-stage kill (leading indicators Day 3, conversion Day 5-7 with 50+ click minimum), sunk cost discipline.
**Reusable for any Trade**: Yes — adjust CPA targets, benchmark thresholds, and creative concepts for the specific product. Campaign structure and kill protocol are universal.

### 3. Audience Testing Strategy (`audience_testing_strategy.md`)
**What**: Phased audience rollout — passive audience learning (Phase 0), formal audience tests (Phase 1+), retargeting (when ready).
**Key concepts**: Test creative FIRST, audiences LAST. Use Meta breakdowns for free audience data. Only run formal audience tests after winning creative exists.
**Reusable for any Trade**: Yes — replace audience tiers with product-specific segments. Protocol and phasing are universal.

### 4. A/B Testing Framework (`ab_testing_framework.md`)
**What**: On-site testing — when to use Bayesian vs frequentist vs pre/post, sample size requirements, tool comparison (post-Google Optimize), landing page test queue.
**Key concepts**: Low-conversion Bayesian warning (<30 conversions = directional only), "just ship it" threshold, explicit error rates at each confidence level.
**Reusable for any Trade**: Yes — sample size tables and methodology selection are universal. Update tool recommendations as landscape changes.

### 5. Test Log (`test_log.json`)
**What**: Operational test log — completed tests, active tests, planned queue, velocity tracking, knowledge library.
**Reusable for any Trade**: Yes — use the schema directly. Clear existing IonWave entries and start fresh.

### 6. Testing Infrastructure (`testing_infrastructure.md`)
**What**: Phased tool stack ($0 → $200/month), Shopify limitations, integration architecture, setup checklist.
**Key concepts**: Tool spend ≤ 5% of ad budget. Free tools first (Clarity, GA4, Meta A/B). Neat A/B or Shoplift for on-site. Intelligems for price testing.
**Reusable for any Trade**: Yes — tool recommendations are Shopify-specific. Update pricing periodically.

---

## How to Use (Step-by-Step for Any Trade)

### Step 1: Assess Traffic Level
Read `experimentation_framework.json` → `traffic_based_methodology`. Identify which tier your Trade falls into (<30/day, 30-100/day, 100-500/day, 500+). This determines which testing methods are viable.

### Step 2: Set Up Infrastructure
Follow `testing_infrastructure.md` → Phase 0 setup checklist. Install GA4, Clarity, configure Meta pixel. Budget $0 in tools until ad spend exceeds $1K/month.

### Step 3: Launch Creative Testing
Follow `creative_testing_protocol.md`:
1. Produce 3-4 creatives testing different concepts
2. Run sequential batches (2 at a time at low budget)
3. Follow two-stage kill protocol (Day 3 leading indicators, Day 5-7 conversions)
4. Graduate winners to scaling campaign

### Step 4: Build the Learning System
File experiment cards in `test_log.json` BEFORE launching. Record results + learnings WITHIN 48 hours of completion. Review knowledge library monthly.

### Step 5: Expand Testing
Once winning creative exists and traffic grows:
- Add on-site A/B testing (AB testing framework)
- Add audience testing (Audience testing strategy)
- Add price testing (M10 protocol, separate OpKit)

---

## Key Findings from IonWave Graded Example

1. **Low-traffic reality**: At <100 visitors/day, formal on-site A/B testing is mostly theater. Creative testing on Meta (where impression volume is 10-100x site traffic) is the real testing engine.
2. **Two-stage kill**: Never kill a creative based on CPA until 50+ link clicks. At $59 AOV and 3% CVR, you need ~33 clicks for your first conversion. Early CPA kills destroy potentially viable creatives.
3. **Bayesian at low conversions**: With <30 conversions per variant, Bayesian results are directional, not definitive. Useful for creative screening, not for pricing decisions.
4. **Tool spend discipline**: 5% of ad budget max on testing tools. At $1K/month ad spend, that's $50 — free tools plus maybe Neat A/B at $29.
5. **Passive audience learning**: Meta's algorithm tests audiences for you via broad targeting. Read the breakdown reports weekly instead of running dedicated audience tests at low spend.
6. **Document everything**: The only failed test is one with no learning recorded. A killed creative teaches you what doesn't resonate — same value as a winner if documented.

---

## Quality Checklist for Future Trades

- [ ] Traffic tier identified and methodology matched
- [ ] Testing infrastructure set up (GA4, Clarity, Meta pixel at minimum)
- [ ] Experiment card schema adopted or adapted
- [ ] Creative testing protocol adapted for product category
- [ ] Kill/scale thresholds calibrated for product economics (CPA target, AOV, CVR)
- [ ] Test log template initialized
- [ ] First 3-4 creative concepts produced and queued
- [ ] Tool spend budget set at ≤5% of ad spend
- [ ] Learning system cadence established (per-test logging, monthly review)


---

### 📄 testing_infrastructure.md

# Testing Infrastructure — M14: Testing & Optimization

**TUP**: M14 | **Tab**: 6 of 6
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-001 (CAC), HYP-002 (Subscription Conversion), HYP-004 (Gross Margin)
**Danilo Source**: None (NEW tab — Danilo's original had no infrastructure guidance. Google Optimize was recommended in the A/B framework tabs but was shut down September 2023.)
**Cross-references**: data/m14/ab_testing_framework.md (tool recommendations by phase)

---

## 1. Purpose

This tab documents the complete testing technology stack for IonWave, phased by growth stage and budget. It replaces Danilo's Google Optimize recommendation with current alternatives and provides a decision framework for tool investment.

---

## 2. Phased Testing Stack

### Phase 0: $0/month — Qualitative + Manual (Pre-revenue, <100 visitors/day)

**This is where IonWave starts.** The goal is maximum learning at zero tool cost.

| Function | Tool | Cost | Setup Effort |
|----------|------|------|-------------|
| **Session recordings + heatmaps** | Microsoft Clarity | $0 (fully free, unlimited sessions) | 10 min — add tracking script to Shopify theme |
| **Web analytics** | Google Analytics 4 (Enhanced Ecommerce) | $0 | 30 min — Shopify GA4 integration |
| **Shopify analytics** | Shopify Analytics (built-in) | $0 | Already included |
| **Ad creative testing** | Meta Ads Manager A/B Test tool | $0 (beyond ad spend) | Part of Meta Business Suite |
| **Significance calculator** | ABTestGuide.com/calc | $0 | Bookmark — no setup |
| **Competitor ad research** | Meta Ad Library | $0 | Browse at ads.tiktok.com/business/creativecenter and facebook.com/ads/library |
| **On-site "testing"** | Manual sequential (change page, compare 2-week windows in GA4) | $0 | Discipline, not software |
| **User testing** | 5-user hallway tests + customer interviews | $0-75/study (Lyssna for remote) | Per study |
| **Email testing** | Klaviyo built-in A/B | $0 (included in Klaviyo plan) | Configure in Klaviyo |

**Setup priority (Day 1)**:
1. GA4 Enhanced Ecommerce tracking confirmed working
2. Microsoft Clarity installed and recording
3. Meta Business Suite configured with pixel + Conversions API
4. Creative test log template created (test_log.json)

### Tool Spend Discipline

*(Dialogue upgrade UPG-5)*: Never spend more than 5% of your monthly ad budget on testing tools. Spend on TRAFFIC (which generates data), not on tools (which analyze data you don't have enough of).

| Monthly Ad Spend | Max Tool Budget | What You Can Afford |
|-----------------|----------------|-------------------|
| $500 | $25 | Free tools only (Clarity, GA4, Meta A/B) |
| $1,000 | $50 | Neat A/B free plan or $29 tier |
| $2,000 | $100 | Intelligems ($99) OR Neat A/B paid tier — not both |
| $5,000 | $250 | Intelligems + Neat A/B or Shoplift paid tier |
| $10,000+ | $500 | Full Phase 2-3 stack |

### Phase 1: $0-50/month — First A/B Tests (100+ visitors/day, 3,000+/month)

**Add when**: Monthly visitors exceed 3,000 consistently.

| Function | Tool | Cost | Why This One |
|----------|------|------|-------------|
| **On-site A/B testing** | Neat A/B Testing (Shopify app) | $0 (free plan) or $29/month | Best value entry point. WYSIWYG editor. No coding. |
| **Landing page testing** | Shoplift (Shopify app) | $0 (free plan) or $49/month | Bayesian methodology (better for low traffic). AI suggestions. |
| **Post-purchase surveys** | KnoCommerce or Fairing | ~$50-100/month | Attribution: "How did you hear about us?" Critical for understanding channel mix. |

**Decision**: Choose Neat A/B OR Shoplift, not both. Neat for simplicity, Shoplift if you want Bayesian reporting and AI suggestions.

### Phase 2: $50-200/month — Price Testing + Serious Infrastructure (Revenue > $5K/month)

**Add when**: Revenue exceeds $5K/month and price testing queue (M10) becomes the priority.

| Function | Tool | Cost | Why This One |
|----------|------|------|-------------|
| **Price A/B testing** | Intelligems | ~$99/month | Only Shopify-native tool that shows real different prices through checkout. Required for M10 test queue (PT-002+). |
| **Upgraded on-site testing** | Neat A/B ($49-99 tier) or Shoplift ($49 tier) | $49-99/month | Higher traffic limits, more concurrent tests. |

**Total Phase 2 budget**: ~$150-200/month in testing tools.

### Phase 3: $200-500/month — Scaling Infrastructure (Revenue > $20K/month)

**Add when**: Ad spend exceeds $10K/month and testing velocity is a bottleneck.

| Function | Tool | Cost | Why This One |
|----------|------|------|-------------|
| **Attribution** | Triple Whale (Pixel plan) | $100-300/month | First-party pixel, multi-touch attribution. Worthwhile when multi-channel confusion costs real money. |
| **Creative analytics** | Motion | $99-199/month | Creative performance dashboard across Meta + TikTok. Worth it at 20+ creatives in rotation. |
| **Advanced on-site testing** | Convert.com | ~$199/month | Full CRO platform with sequential testing, multivariate. For dedicated CRO programs. |

---

## 3. Tool Integration Architecture

### 3.1 Data Flow

```
                    ┌──────────────────┐
                    │   Meta Ads        │
                    │   (Creative tests) │
                    └────────┬─────────┘
                             │
                             ▼
┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
│ Shopify Store │◄───│  Visitor arrives   │───►│ GA4 tracking  │
│              │    │  (with UTM params) │    │              │
└──────┬───────┘    └──────────────────┘    └──────┬───────┘
       │                                           │
       ▼                                           ▼
┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
│ A/B test app  │    │ Microsoft Clarity │    │ GA4 Reports   │
│ (Neat/Shoplift│    │ (session replay)  │    │ (funnels,     │
│  /Intelligems)│    │                  │    │  conversions)  │
└──────┬───────┘    └──────────────────┘    └──────────────┘
       │
       ▼
┌──────────────┐
│ test_log.json │ ← Manual: record hypothesis, results, learnings
│ (M14 system)  │
└──────────────┘
```

### 3.2 GA4 Custom Dimensions for Testing

Set up these custom dimensions in GA4 to track experiment variant assignments:

| Dimension | Scope | Purpose |
|-----------|-------|---------|
| `experiment_id` | Session | Which test is this visitor in (e.g., LP-001) |
| `experiment_variant` | Session | Which variant (A, B, C) |
| `creative_id` | Session | Which ad creative drove this visit (from UTM) |
| `audience_tier` | Session | Which audience tier (from UTM) |

**Note**: Most Shopify A/B testing apps push variant data to GA4 automatically or via Google Tag Manager. Verify integration during setup.

---

## 4. Shopify-Specific Limitations

| Limitation | Impact | Workaround |
|-----------|--------|-----------|
| No native A/B testing | Must use third-party apps | Neat A/B, Shoplift, or Intelligems |
| Checkout locked (non-Plus) | Cannot test checkout flow | Fix obvious checkout issues without testing. Upgrade to Plus ($2,300/month) if checkout optimization becomes critical. |
| No RPV in Shopify Analytics | Primary metric (M10) must be calculated manually | Export data to spreadsheet or use GA4 exploration |
| Theme duplication ≠ A/B test | Swapping themes introduces time-based confounding | Use app-based testing, not theme swaps |
| Limited custom reporting | Cannot segment by test variant natively | Use A/B testing app's built-in reporting + GA4 |

---

## 5. Free Tools Deep Dive

### 5.1 Microsoft Clarity

**Why it matters**: At low traffic, qualitative insights beat quantitative testing. Clarity provides:
- **Session recordings**: Watch real visitors navigate your site. See where they hesitate, scroll back, or leave.
- **Heatmaps**: Click maps, scroll maps, attention maps. Identify what visitors actually see and click.
- **Rage clicks**: Automatic detection of frustrated clicking (usually indicates UX problem).
- **Dead clicks**: Elements that look clickable but aren't.
- **Smart Events**: AI-categorized user behaviors.

**100% free with no usage caps.** No reason not to install this on Day 1.

**How to use for testing decisions**:
1. Watch 20-30 session recordings per week
2. Identify top 3 friction points (where users hesitate, abandon, or get confused)
3. Fix the worst friction point each week
4. Check heatmap monthly: is the CTA getting seen? Are visitors reading the social proof?

### 5.2 Meta Ad Library + TikTok Creative Center

**For competitive creative research (free)**:
- Browse all active ads from any advertiser on Meta
- Filter by category (Health & Wellness), region, platform
- See ad duration (longer-running ads = likely winners)
- TikTok Creative Center: top-performing ads by category, trending hooks, keyword insights

**Weekly habit**: Spend 15 minutes browsing competitor supplement ads. Save winning hooks to a swipe file. Note formats that appear repeatedly (= validated by performance).

---

## 6. What NOT to Buy

| Tool | Why Not (At This Stage) |
|------|------------------------|
| **Optimizely** | $36K+/year. Enterprise only. |
| **Northbeam** | $400+/month. Need $50K+ ad spend to justify. |
| **Hyros** | Better for info products/high-ticket, not DTC consumables |
| **Foreplay** | $49-99/month for ad swipe files. Use Meta Ad Library + screenshots (free). |
| **Pencil (AI creative)** | $99-400/month. Unproven performance prediction. UGC/founder video can't be AI-generated. |
| **Multiple A/B tools simultaneously** | Conflicting test populations. Use ONE tool per test domain. |

---

## 7. Setup Checklist (Day 1)

- [ ] GA4 Enhanced Ecommerce tracking installed and confirmed working
- [ ] Microsoft Clarity installed (tracking script in Shopify theme)
- [ ] Meta Pixel + Conversions API configured
- [ ] UTM parameter convention established (see creative_testing_protocol.md naming convention)
- [ ] test_log.json template reviewed and ready for first entry
- [ ] Creative test brief template saved (from creative_testing_protocol.md Section 6)
- [ ] ABTestGuide.com/calc bookmarked for significance checking
- [ ] Meta Ad Library bookmarked for weekly competitive review

---

## 8. Intelligence Gaps

| ID | Gap | Grade | Upgrade Path |
|----|-----|-------|-------------|
| GAP-1 | Shopify app pricing changes frequently | C | Verify all pricing in Shopify App Store before purchasing. Current prices from early 2025 research. |
| GAP-2 | Intelligems integration with Loop Subscriptions unverified | C | Intelligems claims subscription app compatibility. Verify with Intelligems support before committing. Cross-ref: M22 flagged Loop+Smile gap. |
| GAP-3 | GA4 Enhanced Ecommerce setup quality varies | B | Standard Shopify integration exists. Verify purchase events fire correctly with test orders. |
| GAP-4 | Meta Advantage+ changes may affect testing campaign structure | C | Check Meta Business Suite monthly. The ABO testing campaign may need adjustment as Meta forces Advantage+. |


---

## 🔗 Dependencies & Relationships

### Feeds Into
- _No downstream dependencies_

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

_No intelligence gaps documented._

---

## 🎯 Next Actions

_No next actions documented._


---

---

_Report generated: 2026-02-09 17:49:42_

_Source: `data\m14`_