# TUP M0: Trade Thesis

**Status:** unknown | **Quality:** N/A/10 | **Version:** N/A
**Cluster:** N/A (N/A)

---

## 📋 Overview


---

## 📁 Content Files


---

## 🔧 Structured Data

_JSON files converted to human-readable format_

### 📊 assumptions_register.json

- ** Meta:**
  - **Sheet Name:** Assumptions Register
  - **Parent File:** 01_strategic_foundation
  - **Version:** 1.1.0
  - **Last Updated:** 2026-02-04
  - **Updated By:** claude-opus-4.5
  - **Status:** tension_flagged
  - **Quality Score:** 5.5/10
  - **Data Type:** structured_table
  - **Note:**
    > Updated with capital tension flag from Porter's analysis + new addressable demand assumption. Confidence levels upgraded to A/B/C/D system with evidence-based reassessment.
- **Data:**
  - **Assumptions:**
    - 
        **Assumption:** CAC
      - **Current Value:** <$40
      - **Confidence:**
        - **Level:** C
        - **Original Label:** Medium
        - **Updated Assessment:**
          > Medium-Low — Porter's: Meta CPMs rising 27% YoY; zero switching costs = continuous re-acquisition; category creation (not capture) inflates CAC
        - **Source:** Industry benchmarks + Porter's capital tension analysis
        - **Upgrade Path:** Live ad testing with $5K minimum spend
      - **Validation Method:** Live ad testing
      - **Linked Files:**
        - 06_unit_economics
        - 12_media_acquisition
    - 
        **Assumption:** LTV
      - **Current Value:** >$120
      - **Confidence:**
        - **Level:** D
        - **Original Label:** Low
        - **Updated Assessment:** Low — No new evidence. Porter's: zero switching costs suggest LTV is fragile
        - **Source:** Estimated from competitor benchmarks
        - **Upgrade Path:** Cohort analysis at 6 months post-launch
      - **Validation Method:** Cohort analysis at 6mo
      - **Linked Files:**
        - 06_unit_economics
        - 08_financial_model
    - 
        **Assumption:** Subscription rate
      - **Current Value:** >50%
      - **Confidence:**
        - **Level:** C
        - **Original Label:** Medium
        - **Updated Assessment:**
          > Medium — ICP Analysis: Keto/Carnivore and Biohacker segments are subscription-friendly (identity-driven, daily use). Exhausted Professional is convenience-driven = also subscription-friendly
        - **Source:** DTC subscription benchmarks + ICP Analysis
        - **Upgrade Path:** Checkout data from first 100 orders
      - **Validation Method:** Checkout data
      - **Linked Files:**
        - 06_unit_economics
        - 07_offer_strategy
    - 
        **Assumption:** Monthly churn
      - **Current Value:** <8%
      - **Confidence:**
        - **Level:** D
        - **Original Label:** Low
        - **Updated Assessment:**
          > Low-Medium — ICP JTBD: job stickiness varies: Keto (HIGH), Wellness (MODERATE), Identity (LOW — switches with trends). No comparable marine plasma churn data
        - **Source:** Industry average is 6.5% for DTC supplements + ICP JTBD analysis
        - **Upgrade Path:** Cohort tracking after Month 2
      - **Validation Method:** Cohort tracking
      - **Linked Files:**
        - 06_unit_economics
        - 08_financial_model
    - 
        **Assumption:** Gross margin
      - **Current Value:** >65%
      - **Confidence:**
        - **Level:** B
        - **Original Label:** High
        - **Updated Assessment:**
          > Medium-High — Porter's: supplier concentration risk (Actimar/Biocean oligopoly) could compress margins; alternative suppliers not yet validated
        - **Source:** Preliminary supplier quotes + Porter's supplier analysis
        - **Upgrade Path:** Finalize supplier contracts with Biocean
      - **Validation Method:** Supplier quotes
      - **Linked Files:**
        - 06_unit_economics
        - 05b_formulation_supply
        - 08_financial_model
    - 
        **Assumption:** Addressable demand exists at current awareness
      - **Current Value:** >50 qualified leads from $5K ad spend
      - **Confidence:**
        - **Level:** D
        - **Original Label:** New — added from Porter's capital tension analysis
        - **Updated Assessment:**
          > Low — Marine plasma is not an established consumer category. IonWave must CREATE demand, not just capture it. This tests whether the narrow market has capturable demand at current awareness levels
        - **Source:** Porter's persona dialogue (category creation framing)
        - **Upgrade Path:** Initial Meta ad test targeting marine plasma / premium electrolyte keywords
      - **Validation Method:** Initial Meta ad test
      - **Linked Files:**
        - 08_financial_model
        - 12_media_acquisition
  - **Capital Tension Flag:**
    - **Status:** OPEN
    - **Summary:**
      > $30-50K capital plan faces headwinds from rising CPMs (27% YoY), category creation costs (3-5x capture costs), and zero switching costs. Kill criteria partially address this but don't test market existence.
    - **Source:** Porter's Five Forces persona dialogue + ICP JTBD analysis
    - **Discovered:** 2026-02-04
    - **Resolution Path:** Build/audit 08_Financial_Model.xlsx with scenarios linking these assumptions to revenue projections
    - **See Also:** Strategic_Foundation_Analysis.md

### 📊 interview_insights.json

- ** Meta:**
  - **Sheet Name:** Interview Insights Synthesis
  - **Parent File:** 01_strategic_foundation
  - **Version:** 1.1.0
  - **Last Updated:** 2026-02-04
  - **Updated By:** claude-opus-4.5
  - **Status:** proxy_filled
  - **Quality Score:** 4/10
  - **Data Type:** structured_table
  - **Note:**
    > Backfilled with LMNT proxy data from 03B VOC (31 quotes at saturation). ALL DATA IS LMNT PROXY — not IonWave customer data. Must be validated/replaced with IonWave-specific interviews post-launch.
  - **Data Source:** 03B_Customer_Research_VOC_v1.0.1 (LMNT customer voice)
  - **Upgrade Path:** Conduct 5-10 IonWave-specific customer interviews to replace proxy data
- **Data:**
  - **Pain Points:**
    - 
        **Rank:** 1
      - **Pain Point:** Overwhelming saltiness / taste
      - **Frequency:** 6 quotes (19.4%)
      - **Sample Quote:** jarringly salty (LMNT-001)
      - **Implication:**
        > Product opportunity: marine plasma natural mineral balance; position as 'all the electrolytes, none of the salt bomb'
      - **Confidence:** A
      - **Source:** 03B VOC — 6 directly verified quotes
    - 
        **Rank:** 2
      - **Pain Point:** High price ($500+/yr daily)
      - **Frequency:** 3 quotes (9.7%)
      - **Sample Quote:** over $500 a year just for an electrolyte drink (LMNT-013)
      - **Implication:** Price positioning: 10-15% below Seaonic per thesis; ensure beats LMNT $/serving for daily users
      - **Confidence:** A
      - **Source:** 03B VOC — 3 directly verified quotes
    - 
        **Rank:** 3
      - **Pain Point:** Fasted nausea / stomach issues
      - **Frequency:** 3 quotes (9.7%)
      - **Sample Quote:** Mild nausea and stomach gurgling (LMNT-030)
      - **Implication:** Test marine plasma tolerance on empty stomach; if better, this is a differentiator
      - **Confidence:** A
      - **Source:** 03B VOC — 3 directly verified quotes
    - 
        **Rank:** 4
      - **Pain Point:** Delivery/fulfillment failures
      - **Frequency:** 2 quotes (6.5%)
      - **Sample Quote:** 35 days later and still nothing (LMNT-023)
      - **Implication:** Ensure fulfillment reliable from Day 1; table stakes
      - **Confidence:** A
      - **Source:** 03B VOC — 2 directly verified quotes
  - **Jobs To Be Done:**
    - 
        **Rank:** 1
      - **Job:** Sustained daily energy without caffeine dependency
      - **When:** Morning routine, afternoon slump
      - **Current Solution:** LMNT (positioned sport/fasting, not daily wellness)
      - **Our Opportunity:** HIGHEST — LMNT weakest here; marine plasma wellness story fits
      - **Confidence:** B
      - **Source:** ICP JTBD analysis + LMNT-029, LMNT-011
    - 
        **Rank:** 2
      - **Job:** Prevent keto flu / maintain electrolyte balance on restricted diet
      - **When:** Starting keto, ongoing maintenance
      - **Current Solution:** LMNT, DIY salt water, magnesium supplements
      - **Our Opportunity:** HIGH — strong VOC validation; keto community is accessible
      - **Confidence:** A
      - **Source:** ICP JTBD analysis + LMNT-007, LMNT-010, LMNT-013
    - 
        **Rank:** 3
      - **Job:** Peak cognitive + physical performance throughout day
      - **When:** All day, especially during work
      - **Current Solution:** LMNT, various supplement stacks
      - **Our Opportunity:** MODERATE — competes with broad supplement market, not just electrolytes
      - **Confidence:** B
      - **Source:** ICP Optimizer/Biohacker profile
    - 
        **Rank:** 4
      - **Job:** Identity expression — 'I optimize, therefore I am'
      - **When:** Social media, community, purchasing decisions
      - **Current Solution:** LMNT brand, Seaonic for marine purists
      - **Our Opportunity:** MODERATE — requires brand equity IonWave doesn't yet have
      - **Confidence:** C
      - **Source:** ICP analysis + LMNT-031
  - **Segment Insights:**
    - 
        **Segment:** Keto/Carnivore
      - **Interviewed:** 7+ LMNT quotes (proxy)
      - **Key Insight:**
        > Strongest validated segment; keto flu relief is acute, recurring pain point; community-driven discovery
      - **Willingness To Pay:** HIGH ($1.50-2.00/serving)
      - **Priority:** 1 - Primary
    - 
        **Segment:** Biohackers
      - **Interviewed:** 3-4 LMNT quotes (proxy)
      - **Key Insight:** Demands evidence and 'best-in-class' positioning; will research before buying
      - **Willingness To Pay:** HIGH ($2.00+/serving)
      - **Priority:** 2 - Primary
    - 
        **Segment:** Endurance Athletes
      - **Interviewed:** 2-3 LMNT quotes (proxy)
      - **Key Insight:** Performance improvement validated; high volume subscription-friendly; competes in LMNT territory
      - **Willingness To Pay:** MOD-HIGH ($1.50/serving)
      - **Priority:** 3 - Secondary
    - 
        **Segment:** Exhausted Professionals
      - **Interviewed:** 2-3 LMNT quotes (proxy)
      - **Key Insight:** Energy/wellness job validated; highest strategic opportunity per JTBD; least 'electrolyte-aware'
      - **Willingness To Pay:** MOD ($1.00-1.50/serving)
      - **Priority:** 2 - Primary (highest strategic opportunity)
    - 
        **Segment:** General Health
      - **Interviewed:** 0 specific
      - **Key Insight:** No validated evidence; highest price sensitivity; highest DIY substitute risk
      - **Willingness To Pay:** LOW (<$1.00/serving)
      - **Priority:** 5 - Deprioritize
  - **Surprising Findings:**
    - LMNT's dominant pain is TASTE (19.4%), not price. Customers tolerate price but actively work around saltiness.
    - Customers self-dose at 50% — half-packets, 2x dilution. Market says: 'too much sodium.'
    - Daily wellness job is underserved by everyone. LMNT=sport, Seaonic=purity, Quinton=pharma. Nobody owns daily wellness.
    - LMNT customer service is genuinely excellent — raises the bar for IonWave.
    - Biohackers treat electrolytes as IDENTITY products, not commodity supplements.
  - **Marketing Quotes:**
    - 
        **Theme:** Keto flu relief
      - **Source Expression:** Killed my keto flu symptoms in one day (LMNT-007)
      - **Ionwave Angle:** 78 ocean minerals, zero compromises
    - 
        **Theme:** Morning energy
      - **Source Expression:** Morning grogginess lifted faster (LMNT-029)
      - **Ionwave Angle:** What if your morning water actually woke you up?
    - 
        **Theme:** Taste frustration
      - **Source Expression:** jarringly salty / super salty sewage (LMNT-001, LMNT-004)
      - **Ionwave Angle:** All the minerals. None of the salt bomb.
    - 
        **Theme:** Value justification
      - **Source Expression:** health benefits make it worth every penny (LMNT-014)
      - **Ionwave Angle:** 78 minerals from the ocean. Worth it.
    - 
        **Theme:** Self-dosing
      - **Source Expression:** I typically use half packet (LMNT-018)
      - **Ionwave Angle:** Balanced by nature. No half-measures.

### 📊 narrative_hypotheses.json

- ** Meta:**
  - **Sheet Name:** Narrative Hypothesis Table
  - **Parent File:** 01_strategic_foundation
  - **Version:** 1.1.0
  - **Last Updated:** 2026-02-04
  - **Updated By:** claude-opus-4.5
  - **Status:** evidence_informed
  - **Quality Score:** 4.5/10
  - **Data Type:** hybrid
  - **Note:**
    > Evidence For/Against filled from Porter's v1.1.0, ICP Analysis v1.0.0, and 03B VOC. No A/B test or real-world performance data exists yet.
- **Data:**
  - **Principle:**
    > Narratives aren't just stories - they're hypotheses about what will resonate. Test them systematically. Update based on evidence.
  - **Hypotheses:**
    - 
        **Narrative:** 78 minerals vs just 3
      - **Audience:** Customers
      - **Hypothesis:** Differentiation drives purchase
      - **Evidence For:**
        > Biohacker persona demands 'best-in-class' (ICP); LMNT-031 shows community values premium; 6 taste complaints suggest salt overload from 3-mineral approach
      - **Evidence Against:** No evidence customers understand mineral count; '78 minerals' could confuse; no A/B test data
      - **Confidence:** C+
      - **Status:** Testing — needs ad A/B
    - 
        **Narrative:** Ocean-sourced is better
      - **Audience:** Customers
      - **Hypothesis:** Natural positioning resonates
      - **Evidence For:**
        > Keto dieter worldview: ancestral/natural is better (ICP); Quinton 125yr heritage validates marine plasma; LMNT lawsuits punish 'unnatural'
      - **Evidence Against:** 'Natural' overused in supplements + FTC scrutiny; requires education; no conversion data
      - **Confidence:** C
      - **Status:** Testing — needs LP test
    - 
        **Narrative:** Your body is 70% ocean
      - **Audience:** Customers
      - **Hypothesis:** Science angle builds trust
      - **Evidence For:** Optimizer demands data (ICP); good for podcasts/longform; resonates with 'body as system' worldview
      - **Evidence Against:**
        > Scientifically imprecise (60% water, not ocean); could seem pseudoscience; no evidence outperforms simpler claims
      - **Confidence:** C-
      - **Status:** Testing — HIGH RISK
    - 
        **Narrative:** $2M EBITDA in 24 months
      - **Audience:** Operators
      - **Hypothesis:** Financial outcome motivates
      - **Evidence For:** Standard DTC playbook; math works if assumptions validate
      - **Evidence Against:**
        > Porter's capital tension: $30-50K may be insufficient; category creation costs not factored; $100K MRR may need >50% of sub-segment
      - **Confidence:** D
      - **Status:** Testing — UNDERMINED by Porter's
    - 
        **Narrative:** <10 hrs/week after Month 4
      - **Audience:** Operators
      - **Hypothesis:** Lifestyle outcome motivates
      - **Evidence For:** DTC automation mature (Shopify, Klaviyo, Meta); subscription reduces complexity
      - **Evidence Against:**
        > Ignores category creation work (content, community, education); customer service unpredictable during growth
      - **Confidence:** C-
      - **Status:** Testing — ops only
    - 
        **Narrative:** Copy excellence, execute cleaner
      - **Audience:** Team
      - **Hypothesis:** Methodology creates alignment
      - **Evidence For:**
        > Porter's confirms LMNT proved playbook; can learn strengths (service, community) and avoid weaknesses (taste, maltodextrin)
      - **Evidence Against:** 'Copying' uninspiring for team; doesn't address IonWave novelty; marine plasma IS the novel element
      - **Confidence:** C
      - **Status:** Testing — reframe
  - **Testing Methodology:**
    - A/B test ad copy with different narratives
    - Track which narratives get repeated by customers (word of mouth)
    - Survey customers: 'Why did you buy?'
    - Watch which email subject lines get opens
    - Interview churned customers: What didn't resonate?
  - **Confidence Scale:**
    - **90 Plus:** Strong evidence, core narrative
    - **70 To 90:** Good evidence, use confidently
    - **50 To 70:** Mixed signals, keep testing
    - **30 To 50:** Weak evidence, might pivot
    - **Below 30:** Probably wrong, stop using

### 📊 odd1_thesis.json

- ** Meta:**
  - **Sheet Name:** ODD-1 Complete Thesis
  - **Parent File:** 01_strategic_foundation
  - **Version:** 1.1.0
  - **Last Updated:** 2026-02-04
  - **Updated By:** claude-opus-4.5
  - **Status:** superseded
  - **Quality Score:** 4/10
  - **Data Type:** narrative
  - **Superseded By:** thesis.json
  - **Note:**
    > v0 — SUPERSEDED BY THESIS SHEET. Broad electrolyte market framing conflicts with Thesis sheet's narrow marine plasma positioning. Porter's, ICP, and internal evidence all support narrow thesis. Retained for TAM/SAM/SOM estimates and capital plan reference. See Strategic_Foundation_Analysis.md for reconciliation.
- **Data:**
  - **Executive Summary:**
    > IonWave is a premium D2C electrolyte supplement featuring 78 ocean-sourced trace minerals, targeting the $5B+ electrolyte market through keto, carnivore, and biohacker communities. We aim to reach $100K MRR within 12 months through performance marketing and influencer partnerships.
  - **Investment Headline:**
    - **Investment:** $30-50K
    - **Target:** $100K MRR
    - **Timeline:** 12 months
  - **Market:**
    - **Tam:**
      - **Value:** $5B+ (US electrolyte/hydration)
      - **Confidence:** C
      - **Source:** Industry reports
    - **Sam:**
      - **Value:** $500M (premium supplements)
      - **Confidence:** C
      - **Source:** Competitor analysis
    - **Target Market:**
      - **Value:** $50M (keto/carnivore/biohacker)
      - **Confidence:** D
      - **Source:** Community sizing
    - **Growth Rate:**
      - **Value:** 8-12% CAGR
      - **Confidence:** C
      - **Source:** Industry reports
    - **Key Trend:** Shift from sports drinks to functional hydration
  - **Problem:**
    - **Dehydration Epidemic:**
      - 75% of Americans are chronically dehydrated
      - Modern diets deplete electrolytes (especially keto/carnivore)
      - Symptoms: fatigue, brain fog, muscle cramps, poor recovery
    - **Inadequate Solutions:**
      - Sports drinks: Sugar-laden, synthetic, 3-4 minerals only
      - Premium brands (LMNT): Better but still synthetic, limited minerals
      - Ocean minerals: Scientifically superior but poorly marketed
    - **Trust Gap:**
      - Supplement industry plagued by fake claims, low quality
      - Consumers skeptical, want transparency and science
  - **Solution:**
    - **Description:** IonWave: Ocean-sourced electrolytes with 78 trace minerals
    - **Differentiation:**
      - 78 minerals vs. 3-4 in competitors
      - Ocean-sourced (natural) vs. synthetic
      - Matches human plasma mineral composition
      - Third-party tested, transparent sourcing
    - **Positioning:**
      - Premium price ($49-69) justified by quality
      - Science-backed, not hype-driven
      - Community-focused (keto, carnivore, biohacker)
  - **Why Now:**
    - CATEGORY AWARENESS: LMNT, Liquid IV proved the market
    - DIET TRENDS: Keto/carnivore mainstream, electrolyte need understood
    - D2C INFRASTRUCTURE: Shopify, 3PLs, Meta ads make launch cheap
    - TRUST SHIFT: Consumers want clean labels, transparency
    - INFLUENCER ECOSYSTEM: Health influencers need products to recommend
  - **Right To Win:**
    - OPERATIONAL EXCELLENCE: Studio model with proven D2C playbooks
    - SPEED: Can launch in weeks, not months
    - CAPITAL EFFICIENCY: Lean team, performance marketing focus
    - DIFFERENTIATED PRODUCT: Ocean-sourced is defensible positioning
    - COMMUNITY ACCESS: Relationships in keto/biohacker space
  - **The Ask:**
    - **Raising:** $30-50K
    - **Use Of Funds:**
      - **Inventory:** $15-20K
      - **Ad Spend Testing:** $10-15K
      - **Operations Buffer:** $5-10K
    - **Target Outcome:** $100K MRR within 12 months
    - **Expected Return:** 5-10x in 3-5 years (acquisition or cash flow)

### 📊 thesis.json

- ** Meta:**
  - **Sheet Name:** Strategic Thesis
  - **Parent File:** 01_strategic_foundation
  - **Version:** 1.0.0
  - **Last Updated:** 2026-02-04
  - **Updated By:** claude-opus-4.5
  - **Status:** draft
  - **Quality Score:** 5/10
  - **Data Type:** hybrid
  - **Note:**
    > Narrow marine plasma positioning. Better aligned with Porter's analysis than ODD-1. Kill criteria are well-defined but not yet validated.
- **Data:**
  - **Header:**
    - **Trade Number:** 84
    - **Product:** Premium Liquid Marine Plasma Electrolytes
    - **Status:** HYPOTHESIS - NOT YET VALIDATED
  - **The Bet:**
    - **Primary Hypothesis:**
      > There is room for a #2 player in premium marine plasma electrolytes at 10-15% below Seaonic's price point, targeting the same biohacker/athlete ICP.
    - **Risk Note:**
      > Must identify differentiation beyond price OR accept we're a pure arbitrage play that dies if Seaonic price matches.
  - **Competitive Reality:**
    - 
        **Brand:** Seaonic
      - **Scale Revenue:**
        - **Value:** Unknown revenue (no funding disclosed, ~43 Trustpilot reviews)
        - **Confidence:** D
        - **Source:** Trustpilot review count only
        - **Upgrade Path:** SEMrush traffic estimate, ad library research
      - **Key Intel:** Founder: Lisa (pregnancy-driven origin story)
      - **Action Required:** NEED: Traffic estimate, ad spend, creative library
    - 
        **Brand:** LMNT
      - **Scale Revenue:**
        - **Value:** $66M revenue 2024, $24M cash, 11-50 employees
        - **Confidence:** B
        - **Source:** Industry triangulation, public data
        - **Upgrade Path:** Verify via SEMrush
      - **Key Intel:** Founded 2018, raised $6M, 3.5-4% CVR
      - **Action Required:** Powder format, keto audience, PROVEN category
    - 
        **Brand:** Quinton
      - **Scale Revenue:**
        - **Value:** 125+ year heritage, pharmaceutical positioning
        - **Confidence:** C
        - **Source:** Public brand history
      - **Key Intel:** Glass ampoules, no subscription, $75/30
      - **Action Required:** Legacy brand, not direct competitor
    - 
        **Brand:** Biocean/Actimar
      - **Scale Revenue:**
        - **Value:** Marine plasma SUPPLIER, not competitor
        - **Confidence:** B
        - **Source:** Direct research
      - **Key Intel:** Canada-based, GMP certified
      - **Action Required:** POTENTIAL SUPPLIER - CONTACT DIRECTLY
  - **Kill Criteria:**
    - 
        **Criteria:** Supplier COGS >$0.60/sachet landed
      - **Why It Kills:** Kills margin math entirely
      - **When To Validate:** VALIDATE WEEK 1
      - **How To Validate:** Contact Biocean, Quinton, 3 Alibaba suppliers
    - 
        **Criteria:** Seaonic has exclusive supplier deal
      - **Why It Kills:** Blocked from market entry
      - **When To Validate:** VALIDATE WEEK 1
      - **How To Validate:** Ask suppliers directly about exclusivity
    - 
        **Criteria:** Meta CPM >$20 after $5k spend
      - **Why It Kills:** CAC math impossible
      - **When To Validate:** VALIDATE WEEK 6
      - **How To Validate:** Need 100+ conversions for significance
    - 
        **Criteria:** Landing page CVR <2% after 500 visitors
      - **Why It Kills:** Funnel broken
      - **When To Validate:** VALIDATE WEEK 6
      - **How To Validate:** Test 3+ LP variants before killing
    - 
        **Criteria:** Subscription M1 churn >25%
      - **Why It Kills:** LTV assumption destroyed
      - **When To Validate:** VALIDATE MONTH 2
      - **How To Validate:** Industry avg is 6.5% monthly for DTC
  - **Differentiation Options:**
    - 
        **Strategy:** Price arbitrage only
      - **What It Means:** 10-15% below Seaonic
      - **Upside:** Easy to execute, fast to market
      - **Downside:** No moat, dies on price match
      - **Assessment:** WEAK - need backup
    - 
        **Strategy:** Purity/testing story
      - **What It Means:** 3rd party COA, heavy metal testing
      - **Upside:** Defensible, trust-building
      - **Downside:** Seaonic already claims this
      - **Assessment:** MODERATE
    - 
        **Strategy:** Flavored options
      - **What It Means:** Add natural flavors (Seaonic is unflavored, salty)
      - **Upside:** Clear gap, taste is common complaint
      - **Downside:** Formulation complexity, sourcing
      - **Assessment:** STRONGEST
    - 
        **Strategy:** Format innovation
      - **What It Means:** Concentrate bottle vs sachets
      - **Upside:** Lower COGS, eco-friendly angle
      - **Downside:** Consumer adoption risk
      - **Assessment:** HIGH RISK
    - 
        **Strategy:** Community/content play
      - **What It Means:** Become marine plasma education destination
      - **Upside:** Long-term moat, organic traffic
      - **Downside:** Slow, requires expertise
      - **Assessment:** LONG-TERM ONLY

---

## 📝 Narrative Content

_No markdown files in this TUP._

---

## 🔗 Dependencies & Relationships

### Feeds Into
- 02_market_intelligence
- 03a_customer_research_icp
- 05a_product_strategy
- 06_unit_economics
- 04_planning_roadmaps

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

_No intelligence gaps documented._

---

## 🎯 Next Actions

Build/audit 08_Financial_Model; validate $30K MRR Year 1 target; research Female Wellness ICP; collect fasting-specific VOC

### Key Blockers
- No financial model linked to thesis; Right to Win reframed (singular: marine plasma positioning); sub-segment sized at $300K-$1.5M (thesis reframed — marine plasma = differentiation tool, not market definition)

---

## 🧰 OpKits

- {'opkit_id': 'opkit_m0_thesis_structure', 'name': 'Thesis Structure Checklist', 'source': 'ops_model_v10_dump/1204_m0_thesis_structure.json', 'description': '16-field decision-forcing checklist (ICP, Positioning, Product, Distribution, Finance, Kill Criteria)', 'decision': 'REC-002f'}
- {'opkit_id': 'opkit_m0_computational_pmf', 'name': 'Computational PMF Observer', 'source': 'ops_model_v10_dump/137_computational_pmf.json', 'description': '10 signals → weighted PMF assessment (No PMF/Early/Achieved/Strong)', 'decision': 'REC-002b'}
- {'opkit_id': 'opkit_m0_anti_goals', 'name': 'Anti-Goals Boundary Conditions', 'source': 'ops_model_v10_dump/115_anti_goals.json', 'description': '8 constraints defining what IonWave is NOT', 'decision': 'REC-002d'}
- {'opkit_id': 'opkit_m0_bifurcation_points', 'name': 'Bifurcation Points Controller Stack', 'source': 'ops_model_v10_dump/131_bifurcation_points.json', 'description': 'Early Warning → Bifurcation → Kill controller stack for 8 metrics', 'decision': 'REC-002a'}

---

---

_Report generated: 2026-02-09 17:49:42_

_Source: `data\m0_trade_thesis`_