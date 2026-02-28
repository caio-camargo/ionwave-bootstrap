# TUP M16: Content & SEO

**Status:** workshopped | **Quality:** 8.4/10 | **Version:** 1.0.0
**Cluster:** BCL-5 (Growth & Market)

---

## 📋 Overview

- **Workshop Date:** 2026-02-06
- **Actor:** claude-opus-4-6
- **Protocol Used:** TWP-001 v2.0.0
- **Change Type:** initial_workshop

### Workshop Dialogue
- **Personas Used:** Growth Engineer, Skeptical Investor, Category Expert (SEO/Content)
- **Rounds:** 8
- **Saturated:** True
- **Upgrades Applied:** 5
- **Unresolved Issues:** 4

### Quality Assessment
- **Score:** 8.4/10
- **Rationale:** Strong: research-grounded, realistic timelines, actionable content, 8-round persona dialogue with 5 material upgrades. Limited by: unverified keyword volumes, no competitor backlink data, no CWV data for Shopify theme. Pre-launch planning — execution will determine final quality.

---

## 📁 Content Files

- 📄 MD **data/m16/content_strategy.md**
- 📄 MD **data/m16/seo_strategy.md**
- 🔧 JSON **data/m16/seo_keyword_research.json**
- 📄 MD **data/m16/seo_content_strategy.md**
- 📄 MD **data/m16/seo_link_building.md**
- 📄 MD **data/m16/technical_seo_checklist.md**
- 📄 MD **data/m16/content_repurposing.md**
- 📄 MD **data/m16/dialogue_summary.md**
- 📄 MD **data/m16/opkit_content_seo.md**
- 🔧 JSON **data/m16/_meta.json**

---

## 🔧 Structured Data

_JSON files converted to human-readable format_

### 📊 seo_keyword_research.json

- ** Meta:**
  - **Tup:** M16
  - **Tab:** 4 of 7
  - **Title:** SEO Keyword Research
  - **Version:** 1.0.0
  - **Date:** 2026-02-06
  - **Author:** Caio, Claude (collaborative)
  - **Ai Model:** claude-opus-4-6
  - **Status:** AI Draft
  - **Hypothesis Links:**
    - HYP-006
    - HYP-001
  - **Danilo Source:** ops_model_v10_dump/411_seo_keyword_research.json (27 rows)
  - **Purpose:**
    > Target keyword list organized by search intent, difficulty, and priority phase. Danilo's keyword volumes are directionally correct but difficulty assessments need calibration for a new domain.
  - **Data Quality Note:**
    > Keyword volumes are estimates from research. Actual volumes should be verified with Google Keyword Planner or Ubersuggest after launch. Marine plasma-specific terms may have lower volume than estimated — monitor GSC impression data.
- **Keyword Categories:**
  - **Description:** Keywords organized by search intent — determines content type and conversion expectation
  - **Categories:**
    - 
        **Category:** Brand
      - **Intent:** Navigational
      - **Conversion Rate:** 5-10% (highest — they're looking for you)
      - **Content Type:** Homepage, About page
      - **Priority:** Automatic (protect your brand)
      - **Note:** Brand keywords should rank #1 automatically. If not, something is wrong technically.
    - 
        **Category:** Product / Transactional
      - **Intent:** Transactional
      - **Conversion Rate:** 3-5% (high intent to buy)
      - **Content Type:** Product pages, landing pages
      - **Priority:** High — but competitive, target Phase 2-3
      - **Note:**
        > Head terms like 'electrolyte powder' are dominated by Amazon and established brands. New domain: 18-24 months to compete.
    - 
        **Category:** Comparison / Commercial
      - **Intent:** Commercial investigation
      - **Conversion Rate:** 2-4% (evaluating options)
      - **Content Type:** Comparison pages, vs posts, 'best of' roundups
      - **Priority:** High — achievable at medium difficulty
      - **Note:**
        > Comparison intent is high-value because the searcher is ready to buy, just deciding between options. 'LMNT alternative' at 2,900 volume / low KD is a prime target.
    - 
        **Category:** Problem / Informational
      - **Intent:** Informational
      - **Conversion Rate:** 0.5-1.5% (learning, not buying yet)
      - **Content Type:** Blog posts, guides
      - **Priority:** Medium — builds authority and email list
      - **Note:**
        > High volume, low direct conversion. Value is in email capture, brand awareness, and SEO authority building.
    - 
        **Category:** How-to / Informational
      - **Intent:** Informational
      - **Conversion Rate:** 0.5-1% (seeking answers)
      - **Content Type:** How-to guides, pillar pages
      - **Priority:** Medium — featured snippet opportunities
      - **Note:** How-to content has featured snippet potential. Format answers clearly with numbered steps.
    - 
        **Category:** Ingredient / Informational
      - **Intent:** Informational
      - **Conversion Rate:** 0.5-1% (researching ingredients)
      - **Content Type:** Blog posts, science deep-dives
      - **Priority:** Medium-High — builds E-E-A-T authority
      - **Note:** Marine plasma and ocean minerals terms are IonWave's competitive moat. Very low competition.
- **Target Keywords:**
  - **Description:**
    > Master keyword list organized by phase (achievability for a new domain). Volumes are estimates — verify post-launch.
  - **Phase 1 Long Tail:**
    - **Description:** Month 1-6: Ultra-long-tail, KD <20, volume <500. These are your first wins.
    - **Target Count:** 15-25 keywords targeted via 12-20 blog posts
    - **Keywords:**
      - 
          **Keyword:** marine plasma electrolyte benefits
        - **Est Volume:** 50-100
        - **Kd:** <10
        - **Intent:** Informational
        - **Target Page:** Blog post (pillar: Natural Health)
        - **Ionwave Advantage:** Almost zero competition — this is YOUR territory
        - **Status:** To create
      - 
          **Keyword:** ocean minerals for hydration
        - **Est Volume:** 100-200
        - **Kd:** <10
        - **Intent:** Informational
        - **Target Page:** Blog post (pillar: Hydration Science)
        - **Ionwave Advantage:** Uncontested niche
        - **Status:** To create
      - 
          **Keyword:** electrolytes for fasting headache
        - **Est Volume:** 100-300
        - **Kd:** 5-15
        - **Intent:** Problem/Informational
        - **Target Page:** Blog post (pillar: Keto & Low-Carb)
        - **Ionwave Advantage:** Specific problem, low competition, high purchase intent
        - **Status:** To create
      - 
          **Keyword:** signs of electrolyte deficiency during fasting
        - **Est Volume:** 100-300
        - **Kd:** 5-15
        - **Intent:** Problem/Informational
        - **Target Page:** Blog post (pillar: Keto & Low-Carb)
        - **Ionwave Advantage:** Specific + fasting audience crossover
        - **Status:** To create
      - 
          **Keyword:** keto electrolyte drink without sugar
        - **Est Volume:** 300-500
        - **Kd:** 15-25
        - **Intent:** Commercial
        - **Target Page:** Landing page (Keto audience)
        - **Ionwave Advantage:** IonWave is sugar-free — direct product fit
        - **Status:** To create
      - 
          **Keyword:** electrolytes for women over 40
        - **Est Volume:** 200-500
        - **Kd:** 10-20
        - **Intent:** Commercial
        - **Target Page:** Blog post (pillar: Natural Health)
        - **Ionwave Advantage:** Female Wellness ICP segment (M27)
        - **Status:** To create
      - 
          **Keyword:** how much sodium during fasting
        - **Est Volume:** 200-400
        - **Kd:** 10-20
        - **Intent:** How-to/Informational
        - **Target Page:** Blog post (pillar: Keto & Low-Carb)
        - **Ionwave Advantage:** Protocol-specific, featured snippet potential
        - **Status:** To create
      - 
          **Keyword:** electrolyte powder vs tablet
        - **Est Volume:** 100-300
        - **Kd:** 10-15
        - **Intent:** Comparison
        - **Target Page:** Blog post (pillar: Comparisons)
        - **Ionwave Advantage:** Powder format advantage for IonWave
        - **Status:** To create
      - 
          **Keyword:** trace minerals supplement benefits
        - **Est Volume:** 200-400
        - **Kd:** 15-25
        - **Intent:** Informational
        - **Target Page:** Blog post (pillar: Natural Health)
        - **Ionwave Advantage:** 78 minerals positioning — unique angle
        - **Status:** To create
      - 
          **Keyword:** LMNT alternative
        - **Est Volume:** 2,900
        - **Kd:** Low
        - **Intent:** Commercial
        - **Target Page:** Comparison page
        - **Ionwave Advantage:** High volume, low competition, comparison intent = high CVR
        - **Status:** HIGH PRIORITY — create early
  - **Phase 2 Medium Tail:**
    - **Description:** Month 6-12: Medium-tail, KD 20-40, volume 500-3,000. Target after building some authority.
    - **Target Count:** 10-15 additional keywords
    - **Keywords:**
      - 
          **Keyword:** best electrolyte for fasting
        - **Est Volume:** 1,000-2,000
        - **Kd:** 25-35
        - **Intent:** Commercial
        - **Target Page:** Pillar page or comparison
        - **Status:** To create
      - 
          **Keyword:** electrolytes for keto diet
        - **Est Volume:** 1,000-3,000
        - **Kd:** 25-40
        - **Intent:** Commercial
        - **Target Page:** Keto landing page
        - **Status:** To create
      - 
          **Keyword:** sugar free electrolyte drink
        - **Est Volume:** 1,000-2,000
        - **Kd:** 25-35
        - **Intent:** Commercial
        - **Target Page:** Product page or landing page
        - **Status:** To create
      - 
          **Keyword:** signs of electrolyte imbalance
        - **Est Volume:** 5,400
        - **Kd:** Low-Medium
        - **Intent:** Informational
        - **Target Page:** Blog post (pillar: Hydration Science)
        - **Note:** Danilo listed this as Low difficulty — may be achievable earlier
        - **Status:** To create
      - 
          **Keyword:** electrolytes for fasting
        - **Est Volume:** 4,400
        - **Kd:** Medium
        - **Intent:** Commercial
        - **Target Page:** Landing page
        - **Status:** To create
      - 
          **Keyword:** ocean minerals benefits
        - **Est Volume:** 1,200
        - **Kd:** Low
        - **Intent:** Informational
        - **Target Page:** Blog post (pillar: Natural Health)
        - **Note:** Danilo listed this correctly — achievable early
        - **Status:** To create
      - 
          **Keyword:** how much sodium on keto
        - **Est Volume:** 3,600
        - **Kd:** Low-Medium
        - **Intent:** How-to
        - **Target Page:** Blog post (pillar: Keto & Low-Carb)
        - **Status:** To create
      - 
          **Keyword:** electrolyte supplement benefits
        - **Est Volume:** 500-1,500
        - **Kd:** 20-30
        - **Intent:** Informational
        - **Target Page:** Pillar page (Hydration Science)
        - **Status:** To create
  - **Phase 3 Head Terms:**
    - **Description:** Month 12-24: Head terms, KD 40+, volume 5,000+. Only after DR 30+ and strong content foundation.
    - **Target Count:** 5-8 aspirational keywords
    - **Keywords:**
      - 
          **Keyword:** best electrolytes
        - **Est Volume:** 12,000
        - **Kd:** High (45-65)
        - **Intent:** Commercial
        - **Target Page:** Comparison page / roundup
        - **Requirements:** DR 40+, 50+ referring domains to page
        - **Status:** Aspirational
      - 
          **Keyword:** electrolyte powder
        - **Est Volume:** 18,000
        - **Kd:** High (55-70)
        - **Intent:** Transactional
        - **Target Page:** Homepage or product page
        - **Requirements:** DR 50+, 100+ referring domains. Amazon dominates.
        - **Status:** Aspirational
      - 
          **Keyword:** electrolyte supplements
        - **Est Volume:** 8,000
        - **Kd:** Medium-High (40-55)
        - **Intent:** Transactional
        - **Target Page:** Product page
        - **Requirements:** DR 40+
        - **Status:** Aspirational
      - 
          **Keyword:** keto electrolytes
        - **Est Volume:** 6,500
        - **Kd:** Medium (30-45)
        - **Intent:** Commercial
        - **Target Page:** Keto landing page
        - **Requirements:** DR 30+, topical authority in keto content cluster
        - **Status:** Aspirational — possibly achievable Month 9-12
      - 
          **Keyword:** trace minerals supplement
        - **Est Volume:** 2,400
        - **Kd:** Medium (25-40)
        - **Intent:** Transactional
        - **Target Page:** Product page
        - **Status:** Aspirational
- **Keyword Research Tools:**
  - **Description:** Tools for ongoing keyword research and monitoring
  - **Free:**
    - 
        **Tool:** Google Search Console
      - **Use:** Real impression/click data for YOUR site. The most accurate keyword data you'll ever get.
      - **Cost:** $0
    - 
        **Tool:** Google Keyword Planner
      - **Use:** Volume estimates (requires Google Ads account, not spend)
      - **Cost:** $0
    - 
        **Tool:** Google Trends
      - **Use:** Relative interest over time, seasonality
      - **Cost:** $0
    - 
        **Tool:** AlsoAsked.com
      - **Use:** People Also Ask questions — content ideas
      - **Cost:** Free tier
    - 
        **Tool:** AnswerThePublic
      - **Use:** Question-based keyword discovery
      - **Cost:** Limited free searches
  - **Paid:**
    - 
        **Tool:** Ubersuggest
      - **Use:** Keyword research, competitor analysis, content ideas
      - **Cost:** $29/month
      - **Recommendation:** Best value for bootstrapped brands
    - 
        **Tool:** Ahrefs Lite
      - **Use:** Comprehensive: keywords, backlinks, competitor analysis, rank tracking
      - **Cost:** $99/month
      - **Recommendation:** Best tool overall, but wait until 20+ pages published
    - 
        **Tool:** SEMrush Pro
      - **Use:** Similar to Ahrefs with additional content marketing features
      - **Cost:** $130/month
    - 
        **Tool:** Keywords Everywhere
      - **Use:** Browser extension showing volume/CPC on search results
      - **Cost:** $1.25/month (10 credits)
      - **Recommendation:** Extremely cheap, good for quick checks
- **Competitive Landscape Note:**
  > The electrolyte/supplement SEO space is extremely competitive. Amazon occupies 2-4 positions on page 1 for transactional terms. Healthline/WebMD dominate informational terms. Affiliate sites (Barbend, etc.) compete aggressively for 'best X' commercial terms. IonWave's competitive advantage: marine plasma positioning creates uncontested keyword territory. Build authority there first, then expand.

---

## 📝 Narrative Content

### 📄 content_calendar.md

# Content Calendar — M16: Content & SEO

**TUP**: M16 | **Tab**: 4 of 6
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift)

---

## 1. Calendar Philosophy

### 1.1 Cadence by Phase

| Phase | Period | Cadence | Total Articles | Focus |
|-------|--------|---------|---------------|-------|
| **Pre-Launch** | Month -1 to 0 | Batch publish | 6-8 | Core pages + launch content |
| **Foundation** | Month 1-3 | 1/week | 12-13 | Pillar pages + Tier 1/2 keywords |
| **Building** | Month 4-6 | 2/week | 24-26 | Topic clusters + Tier 2/3 keywords |
| **Scaling** | Month 7-12 | 2-3/week | 52-78 | Full cluster coverage + refreshes |

**Total Year 1 target**: 90-125 articles

### 1.2 Content Mix

| Content Type | % of Calendar | Rationale |
|-------------|--------------|-----------|
| **Pillar pages** | 5% | High investment, foundational |
| **Cluster articles** | 50% | SEO backbone, builds topic authority |
| **Comparison posts** | 20% | Highest commercial intent, drives purchases |
| **Product education** | 10% | Supports conversion on-site |
| **Seasonal/trending** | 10% | Timely relevance, social sharing |
| **Content refreshes** | 5% | Keep top performers current |

---

## 2. Pre-Launch Content (Batch Publish at Launch)

These pages must be live on Day 1:

| # | Content | Type | Keyword Target | Pillar | Status |
|---|---------|------|---------------|--------|--------|
| L1 | Homepage | Page | "IonWave marine plasma" | — | ⬜ |
| L2 | Product page: Marine Plasma Electrolyte | Product | "marine plasma electrolyte supplement" | — | ⬜ |
| L3 | About / Our Science page | Page | "what is marine plasma" | 1 | ⬜ |
| L4 | FAQ page (with schema) | Page | Long-tail questions | — | ⬜ |
| L5 | IonWave vs LMNT comparison | Blog | "IonWave vs LMNT" | 5 | ⬜ |
| L6 | IonWave vs Liquid IV comparison | Blog | "IonWave vs Liquid IV" | 5 | ⬜ |
| L7 | Seaonic vs IonWave comparison | Blog | "seaonic vs IonWave" | 5 | ⬜ |
| L8 | Best Sugar-Free Electrolytes [2026] | Blog | "best sugar free electrolytes" | 5 | ⬜ |

---

## 3. Month 1-3 Calendar (Foundation)

### Month 1 (4 articles)

| Week | Article | Keyword | Pillar | Type | Words |
|------|---------|---------|--------|------|-------|
| 1 | The Complete Guide to Marine Plasma | "what is marine plasma" | 1 | Pillar | 4,000 |
| 2 | 78 Ocean Minerals: What They Do for Your Body | "78 minerals ocean water" | 1 | Cluster | 1,800 |
| 3 | Marine Plasma vs Regular Electrolytes: Key Differences | "marine plasma vs electrolytes" | 1 | Comparison | 2,000 |
| 4 | Best Electrolytes for Keto [2026] | "best electrolytes for keto" | 3 | Roundup | 2,500 |

### Month 2 (4-5 articles)

| Week | Article | Keyword | Pillar | Type | Words |
|------|---------|---------|--------|------|-------|
| 5 | The Complete Guide to Electrolytes | "electrolyte guide" | 2 | Pillar | 3,500 |
| 6 | Keto Flu: What It Is and How to Prevent It | "keto flu remedy" | 3 | Problem/Solution | 1,800 |
| 7 | When to Take Electrolytes for Best Results | "best time to take electrolytes" | 2 | How-To | 1,500 |
| 8 | Marine Plasma and Blood Plasma: The Isotonic Connection | "isotonic ocean minerals" | 1 | Science | 1,800 |
| 8b | Best Electrolyte Powder vs Tablets | "electrolyte powder vs tablet" | 2 | Comparison | 1,500 |

### Month 3 (4-5 articles)

| Week | Article | Keyword | Pillar | Type | Words |
|------|---------|---------|--------|------|-------|
| 9 | Electrolytes on Keto: The Complete Guide | "keto electrolytes" | 3 | Pillar | 3,500 |
| 10 | Electrolytes for Fasting: What You Need | "electrolytes for fasting" | 3 | Guide | 1,800 |
| 11 | Trace Minerals: The Nutrients Most People Are Missing | "trace minerals benefits" | 1 | Science | 1,800 |
| 12 | René Quinton and the History of Ocean Mineral Therapy | "rené quinton ocean therapy" | 1 | History/Science | 1,800 |
| 12b | Signs of Electrolyte Imbalance: What to Watch For | "electrolyte imbalance symptoms" | 2 | Symptom | 1,500 |

**End of Month 3 total**: ~20-23 articles (including pre-launch batch)

---

## 4. Month 4-6 Calendar (Building — 2x/week)

### Month 4

| Week | Article 1 | Article 2 |
|------|-----------|-----------|
| 13 | Hydration for Athletes: Science-Based Guide (Pillar 4) | Marine Plasma Bioavailability: How Your Body Absorbs Ocean Minerals |
| 14 | How Marine Plasma Is Harvested (sourcing/sustainability) | Why Sports Drinks Are Bad for You |
| 15 | Sodium on Keto: How Much Do You Really Need? | Best Electrolytes for Runners [2026] |
| 16 | Magnesium on Keto: The Overlooked Mineral | Pre-Workout Hydration: What to Drink and When |

### Month 5

| Week | Article 1 | Article 2 |
|------|-----------|-----------|
| 17 | Ocean Minerals & Trace Elements (Pillar 1 expansion) | Post-Workout Recovery: Hydration That Actually Works |
| 18 | Electrolytes and Sleep: The Connection Most People Miss | Marine Plasma vs Himalayan Salt: Which Is Better? |
| 19 | Natural Electrolyte Sources: A Complete Guide | Best Electrolyte Supplements [2026] (comprehensive roundup) |
| 20 | Why Am I Always Tired? The Mineral Deficiency Connection | Keto Hydration Mistakes: 7 Things You're Doing Wrong |

### Month 6

| Week | Article 1 | Article 2 |
|------|-----------|-----------|
| 21 | Best Electrolyte Supplement [2026]: Honest Guide (PILLAR 5) | Is Marine Plasma Safe? Side Effects and Considerations |
| 22 | Morning Hydration Routine for All-Day Energy | Intermittent Fasting Electrolytes: What You Need |
| 23 | Endurance Athlete Electrolyte Needs | LMNT Review: Honest Analysis |
| 24 | CONTENT REFRESH: Update Month 1 articles | Clean Label Electrolytes: What to Look For |

**End of Month 6 total**: ~45-50 articles

---

## 5. Month 7-12 Content Themes

Detailed calendar built monthly based on keyword performance data, but general themes:

| Month | Theme | Content Focus |
|-------|-------|--------------|
| **7** | Athletic deep-dive | Segment-specific guides (CrossFit, marathon, cycling) |
| **8** | Seasonal: Back-to-routine | Fall hydration, school/work routines, seasonal electrolyte needs |
| **9** | Content refresh cycle | Update all Month 1-3 articles with new data, links |
| **10** | Authority plays | Guest post syndication, expert roundups, original research |
| **11** | Holiday content | Gift guides, wellness routines, New Year prep |
| **12** | Year-in-review + planning | Annual roundup, update all "2026" articles to "2027" |

---

## 6. Weekly Content Production Workflow

### 6.1 Single Article Production Cycle

```
DAY 1: PLAN
├── Select keyword from priority queue
├── Research competitor content for that keyword
├── Outline article structure (H2s, key points)
└── Identify unique angle / original contribution

DAY 2-3: DRAFT
├── AI generates initial draft from outline
├── Human adds unique perspective, data, examples
├── Fact-check all claims (especially health claims)
└── Add internal links, CTAs, images

DAY 4: EDIT & OPTIMIZE
├── Editorial review (voice, clarity, flow)
├── SEO optimization (title, meta, headings, keyword density)
├── Add structured data (FAQ schema, HowTo schema)
└── Create social media excerpts

DAY 5: PUBLISH & DISTRIBUTE
├── Publish on Shopify blog
├── Submit URL in Google Search Console
├── Share on social channels
├── Include in next email newsletter
└── Log in content tracker
```

### 6.2 Content Quality Gate

Before publishing, every article must pass:

- [ ] Primary keyword in title, H1, first 100 words, meta description
- [ ] At least 3 internal links to other site content
- [ ] At least 1 external link to authoritative source
- [ ] All health claims cite sources
- [ ] FTC-compliant language (no "cure," "treat," "prevent")
- [ ] Image with alt text
- [ ] FAQ schema or other structured data where applicable
- [ ] Meta description written (<160 chars, with CTA)
- [ ] Mobile preview checked
- [ ] Human editorial review completed

---

## 7. Content Tracking

### 7.1 Article Performance Tracker

Track for every article (monthly review):

| Metric | What It Tells Us |
|--------|-----------------|
| Organic sessions | Is the article driving traffic? |
| Keyword positions | Are we ranking for target keywords? |
| Average position | Overall search visibility for this article |
| Click-through rate | Is the title/description compelling? |
| Bounce rate | Is the content meeting search intent? |
| Time on page | Is the content engaging? |
| Conversions (email signup, purchase) | Is the content driving business value? |

### 7.2 Content Refresh Triggers

Refresh an article when:
- **Position drops** — was top 5, now page 2 (competitor may have published better content)
- **6 months old** — scheduled refresh (update stats, links, year references)
- **New data available** — new research, competitor changes, product updates
- **High impressions, low CTR** — title/description needs optimization
- **High traffic, low conversion** — CTA or content-product alignment needs work

---

## 8. Hypothesis Cross-Reference

| Hypothesis | How Content Calendar Feeds It |
|-----------|------------------------------|
| **HYP-006** (Organic Growth 10%) | Calendar provides the execution rhythm that compounds into organic traffic. 90-125 articles in Year 1 build the content base that SEO needs. |
| **HYP-006.2** (SEO) | Every published article is a keyword ranking opportunity. The calendar ensures consistent publishing cadence — the #1 predictor of SEO success. |
| **HYP-001** (CAC ≤$40) | Content calendar front-loads comparison posts (Pillar 5) which are closest to purchase intent. These articles directly reduce blended CAC by capturing organic BOFU traffic. |

---

*Next: Tab 5 (Link Building & Distribution), Tab 6 (Content Measurement)*


---

### 📄 content_measurement.md

# Content Measurement Framework — M16: Content & SEO

**TUP**: M16 | **Tab**: 6 of 6
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift), HYP-001 (CAC)

---

## 1. Measurement Philosophy

### 1.1 The Content ROI Problem

Content marketing has a delayed return — unlike paid ads where you spend $1 and see a result tomorrow, content investments compound over 6-18 months. This creates a measurement challenge: how do you know if content is working before the compounding kicks in?

**Solution**: Track **leading indicators** (early signals that predict future organic success) alongside **lagging indicators** (actual business outcomes). Don't kill the content program at Month 3 because organic revenue is still tiny — look at whether the leading indicators are trending in the right direction.

### 1.2 Metric Hierarchy

```
LEADING INDICATORS (Months 1-6)
├── Indexed pages growing
├── Search impressions increasing
├── Keywords entering top 100
├── Backlinks accumulating
└── Content production on cadence

MIDDLE INDICATORS (Months 3-9)
├── Organic sessions growing month-over-month
├── Keywords moving to top 10-20
├── Organic CTR improving
├── Time on page / engagement signals
└── Email subscribers from content

LAGGING INDICATORS (Months 6-18)
├── Organic traffic as % of total
├── Revenue attributed to organic
├── Content ROI (revenue ÷ production cost)
├── Blended CAC reduction from organic
└── Customer LTV from organic channel
```

---

## 2. KPI Dashboard

### 2.1 Primary KPIs (Report Monthly)

| KPI | Definition | Source | Month 3 Target | Month 6 Target | Month 12 Target |
|-----|-----------|--------|---------------|----------------|-----------------|
| **Organic sessions** | Unique sessions from organic search | GA4 | 200-500 | 1,000-2,500 | 5,000-10,000 |
| **Organic % of total** | Organic sessions ÷ total sessions | GA4 | 3-5% | 8-12% | 10-20% *(U6)* |
| **Keywords in top 10** | Number of keywords ranking positions 1-10 | Ahrefs/GSC | 5-10 | 20-50 | 50-150 |
| **Referring domains** | Unique domains linking to IonWave | Ahrefs | 15-25 | 30-50 | 75-150 |
| **Content output** | Articles published per month | Internal | 4-5 | 8-10 | 10-12 |
| **Organic revenue** | Revenue from organic traffic | GA4 | <$500 | $500-2,000 | $2,000-8,000 |

### 2.2 Secondary KPIs (Review Monthly)

| KPI | Definition | Healthy Range |
|-----|-----------|--------------|
| **Organic CTR** | Clicks ÷ impressions in Search Console | >3% average |
| **Average position** | Average keyword ranking position | Declining (improving) over time |
| **Bounce rate (organic)** | Single-page sessions from organic | <60% for blog, <40% for product pages |
| **Pages per session (organic)** | Average pages viewed per organic visit | >1.5 |
| **Email signups from content** | Newsletter subscriptions from blog CTAs | 2-5% of organic visitors |
| **Domain Authority** | Moz/Ahrefs domain metric | Growing steadily |

### 2.3 Content-Level KPIs (Per Article)

| Metric | Purpose | Action Trigger |
|--------|---------|---------------|
| **Organic sessions** | Is this article driving traffic? | <10 sessions/month after 3 months → refresh or de-prioritize |
| **Keyword position** | Is it ranking for target keyword? | Not in top 50 after 3 months → content quality issue or keyword too competitive |
| **Avg time on page** | Is the content engaging? | <1 minute → content doesn't match intent or is low quality |
| **Scroll depth** | Are people reading the full article? | <50% → content is too long or front-loaded poorly |
| **CTA click rate** | Is it driving business action? | <1% → CTA misaligned with content intent |
| **Backlinks earned** | Is it attracting natural links? | Any article earning links = signal to create more like it |

---

## 3. Attribution Model

### 3.1 How to Attribute Revenue to Content

Content rarely drives a direct last-click purchase. The typical journey:

```
ORGANIC SEARCH → Blog Article → Exit → (days pass) →
PAID AD → Product Page → Purchase
```

If we only count last-click, content gets zero credit. Instead, use **multi-touch attribution**:

| Model | How It Works | When to Use |
|-------|------------|------------|
| **Last-click** | 100% credit to final touchpoint | Default in GA4 — avoid for content valuation |
| **First-click** | 100% credit to first touchpoint | Good for content: shows which articles introduce new visitors |
| **Linear** | Equal credit to all touchpoints | Good for understanding the full journey |
| **Data-driven** | Google's ML-based attribution | Use when traffic volume is high enough (Month 6+) |

**Recommended**: Use **first-click attribution** to evaluate content's role in customer acquisition. This answers: "Which blog articles bring in people who eventually buy?"

### 3.2 GA4 Setup for Content Attribution

1. **Create content groupings**: Group blog articles by pillar (Pillar 1-5) and type (pillar, cluster, comparison)
2. **Set up conversions**: Track email signup, add-to-cart, and purchase as conversion events
3. **Tag content UTMs**: If sharing content links externally, use UTM parameters for tracking
4. **Exploration reports**: Build a monthly content performance exploration in GA4

### 3.3 Organic Channel Value Calculation

Monthly formula:

```
ORGANIC CHANNEL VALUE =
  (Organic Sessions × CVR × AOV) +
  (Organic Email Signups × Email CVR × AOV × Email Cadence) +
  (Brand Search Lift attributable to content × Paid CPC saved)
```

Simplified version for early stage:

```
ORGANIC VALUE = Organic Revenue (first-click) + Equivalent Paid Traffic Cost
```

Where **Equivalent Paid Traffic Cost** = organic sessions × average CPC you'd pay for those keywords.

**Caveat** *(Dialogue upgrade U4)*: "Equivalent paid traffic cost" is a directional metric, not real revenue. You can't deposit saved CPC. Use it to justify continued investment, but don't confuse it with actual ROI. Real ROI = organic revenue (first-click attributed) ÷ content production cost.

Example at Month 6:
- 2,000 organic sessions × $1.50 avg CPC = $3,000 equivalent paid traffic cost
- Even if organic revenue is only $1,000, the content program is saving $3,000 in ad spend

---

## 4. Reporting Cadence

### 4.1 Weekly (5 min review)

| Check | Source | Action if Abnormal |
|-------|--------|-------------------|
| Content published this week? | Content calendar | If behind, identify blocker |
| Any crawl errors? | Google Search Console | Fix immediately |
| Site speed normal? | PageSpeed Insights | Audit if degraded |

### 4.2 Monthly (30 min review)

| Report | Contents | Owner |
|--------|---------|-------|
| **Organic Traffic Report** | Sessions, % of total, MoM growth, top pages | Operator |
| **Keyword Report** | New rankings, position changes, top 10 count | Operator |
| **Content Performance** | Best/worst articles, refresh candidates | Operator |
| **Backlink Report** | New referring domains, DA growth | Operator |
| **Content Output** | Articles published vs plan, quality gate compliance | Operator |

### 4.3 Quarterly (60 min strategic review)

| Question | Data Sources |
|----------|-------------|
| Is organic traffic trending toward the HYP-006 target (10%)? | GA4 organic % trend |
| Which content pillars are performing best? | GA4 content grouping |
| Are we ranking for priority keywords? | Ahrefs rank tracker |
| Is content ROI improving? | Revenue ÷ production cost trend |
| Should we adjust the content calendar based on data? | All of the above |
| Are there new keyword opportunities from Search Console? | GSC query data |

---

## 5. Benchmarks & Guardrails

### 5.1 Industry Benchmarks (DTC Supplement Brands)

| Metric | Industry Average | IonWave Target | Notes |
|--------|-----------------|---------------|-------|
| Organic % of traffic (Year 1) | 10-20% | 10-20% (base), 15-25% (aggressive) | Revised: 15-25% requires perfect execution *(Dialogue U6)* |
| Blog CVR to email | 2-5% | 3% | Standard for gated content / newsletter CTA |
| Blog CVR to purchase | 0.5-2% | 1% | Content visitors are TOFU — lower CVR expected |
| Content production cost per article | $50-500 | $30-100 | AI-assisted production reduces cost |
| Time to first page ranking (long-tail) | 3-6 months | 3-4 months | Marine plasma keywords are low competition |
| Time to first page ranking (medium) | 6-12 months | 6-9 months | Requires DA 15-25 |
| Content ROI breakeven | 6-12 months | 10-14 months | New brands take longer; AI helps but doesn't eliminate ramp *(Dialogue U4)* |

[Confidence: C | Source: Industry benchmarks compiled from various DTC and content marketing studies. Ranges reflect variance across brands and categories.]

### 5.2 Guardrail Metrics

| Guardrail | Threshold | If Violated |
|-----------|-----------|-------------|
| Content production cadence | ≥80% of planned output | Investigate: resource constraint? quality gate too strict? |
| Organic traffic MoM growth | ≥10% MoM after Month 3 | SEO audit: technical issues? content quality? link building stalled? |
| Core Web Vitals | All green | Fix immediately — CWV affects rankings |
| Crawl errors | <5 total | Fix broken links, check redirects |
| Brand search volume | Growing | If flat, content isn't building awareness |

### 5.3 Kill Criteria (When to Reevaluate Content Strategy)

Consider fundamental strategy review if:
- **Month 6**: Organic traffic still <3% of total despite consistent execution
- **Month 9**: No keywords in top 10 for target terms
- **Month 12**: Content ROI still negative with no improvement trend
- **Any time**: Google algorithm penalty detected (sudden 50%+ traffic drop)

**Important**: Don't kill the program too early. Content SEO is inherently slow to start. The leading indicators (indexed pages, impressions, keyword positions) should be trending positively even if traffic is still small.

---

## 6. SEO Tool Stack (Measurement-Focused)

| Tool | Function | Cost | Priority |
|------|----------|------|----------|
| **Google Search Console** | Indexing, search queries, CTR, position tracking | Free | Day 1 |
| **Google Analytics 4** | Traffic, attribution, conversions, audience | Free | Day 1 |
| **Ahrefs Lite** | Keyword tracking, backlink monitoring, competitor analysis, site audit | $99/month | Month 2-3 |
| **Screaming Frog** | Technical SEO audits (free up to 500 URLs) | Free | Monthly |
| **Google Looker Studio** | Custom dashboards combining GA4 + GSC data | Free | Month 3 |
| **Hotjar / Microsoft Clarity** | Heatmaps, scroll depth, user behavior on content | Free | Month 3 |

**Phase 1 minimum** (Month 0-2): GSC + GA4 = $0
**Phase 2 recommended** (Month 3+): Add Ahrefs + Looker Studio = $99/month

---

## 7. Content Program Health Score

### 7.1 Monthly Health Score (Composite)

Score each dimension 1-5, weight, and calculate composite:

| Dimension | Weight | Score Criteria |
|-----------|--------|---------------|
| **Output consistency** | 20% | 5 = 100% of plan, 3 = 80%, 1 = <50% |
| **Organic traffic growth** | 25% | 5 = >20% MoM, 3 = 10-20%, 1 = flat/declining |
| **Keyword progress** | 20% | 5 = new top-10 rankings, 3 = top-50 progress, 1 = no movement |
| **Link acquisition** | 15% | 5 = exceeding target, 3 = on target, 1 = below target |
| **Content quality** | 10% | 5 = all pass quality gate, 3 = most pass, 1 = quality issues |
| **Technical health** | 10% | 5 = all CWV green, 3 = minor issues, 1 = major issues |

**Composite score**:
- 4.0-5.0: Excellent — content program is on track
- 3.0-3.9: Good — performing but opportunities for improvement
- 2.0-2.9: Warning — specific dimensions need attention
- <2.0: Critical — fundamental issues to address

---

## 8. Hypothesis Cross-Reference

| Hypothesis | How Measurement Framework Feeds It |
|-----------|-----------------------------------|
| **HYP-006** (Organic Growth 10%) | This framework directly tracks whether HYP-006 is being achieved. Monthly organic % of total traffic is the primary metric. If we're not reaching 10% by Month 6-8, we know early. |
| **HYP-006.2** (SEO) | Keyword rankings, DA growth, and content output are the operational metrics for HYP-006.2. This framework provides the evidence basis for confidence upgrades. |
| **HYP-001** (CAC ≤$40) | Organic channel value calculation shows how content reduces blended CAC. As organic traffic grows, blended CAC drops — this framework quantifies the effect. |
| **HYP-005** (Blended LTV) | Content-educated customers may have higher LTV (more informed, higher conviction). Track organic vs paid customer cohort LTV to validate (requires 6+ months of data). |

---

*End of M16 Content & SEO TUP — 6 tabs complete.*


---

### 📄 content_repurposing.md

# Content Repurposing System — M16: Content & SEO

**TUP**: M16
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift), HYP-001 (CAC)
**Danilo Source**: ops_model_v10_dump/507_content_repurposing_system.json (45 rows)
**Cross-Reference**: M22 UGC Creator Program (content input), M14 Creative Testing Protocol (ad creative testing)

---

## Purpose

Maximize ROI from every piece of content by systematically repurposing it across channels. The goal is a **content waterfall**: one pillar asset becomes 10-15 derivative pieces, each optimized for its channel.

**Core principle**: Create once, distribute many. Content creation is expensive (time or money). Distribution is cheap. Most brands create too much original content and distribute too little.

---

## 1. The Content Waterfall Model

### One Pillar Blog Post Becomes:

```
PILLAR CONTENT (1 x 2,000-word blog post)
│
├── SOCIAL (5-8 pieces)
│   ├── Instagram carousel (key takeaways as slides)
│   ├── Instagram Reel (30-60s summary or hook)
│   ├── TikTok video (educational clip, different hook than IG)
│   ├── Twitter/X thread (5-10 tweet breakdown)
│   ├── LinkedIn post (if B2B angle exists)
│   └── Pinterest infographic (data or process visualization)
│
├── EMAIL (2-3 pieces)
│   ├── Newsletter feature (summary + link to full post)
│   ├── Drip sequence addition (if evergreen topic)
│   └── Post-purchase education (if product-relevant)
│
├── PAID (2-4 pieces)
│   ├── Meta ad (educational angle from the content)
│   ├── Native ad headline + advertorial excerpt
│   └── Retargeting creative (for blog visitors who didn't convert)
│
└── SEO (1-3 pieces)
    ├── FAQ section → FAQ schema for rich snippets
    ├── Internal links to/from related posts
    └── Answer box optimization (featured snippet targeting)
```

### One UGC Video Becomes:

```
UGC VIDEO (1 x 60-second creator video)
│
├── AD VARIATIONS (4-6 pieces)
│   ├── Full 60s version
│   ├── 30s cut (hook + key benefit + CTA)
│   ├── 15s cut (hook only — awareness)
│   ├── 3-5 different hooks spliced onto same body
│   └── Static screenshots → image ads
│
├── ORGANIC SOCIAL (3-4 pieces)
│   ├── TikTok post (with brand overlay)
│   ├── Instagram Reel (with CTA in caption)
│   ├── Instagram Story (with link sticker)
│   └── UGC repost on brand feed
│
├── WEBSITE (2-3 pieces)
│   ├── Testimonial quote on product page
│   ├── Video embed on landing page
│   └── Social proof section
│
└── EMAIL (1-2 pieces)
    ├── Testimonial in welcome flow
    └── Social proof in cart abandonment
```

---

## 2. Repurposing Checklists

### For Every Blog Post Published:

| # | Derivative | Channel | Timing | Status |
|---|-----------|---------|--------|--------|
| 1 | Extract 3-5 key takeaways for carousel | Instagram | Same week | ☐ |
| 2 | Record 30-60s summary video | TikTok + Reels | Same week | ☐ |
| 3 | Write thread version | Twitter/X | Same week | ☐ |
| 4 | Include in next newsletter | Email | Next send | ☐ |
| 5 | Add internal links from 2-3 existing posts | Blog (SEO) | Same day | ☐ |
| 6 | Create FAQ schema if post answers questions | Blog (SEO) | Same day | ☐ |
| 7 | Consider for email drip sequence | Email flows | Monthly review | ☐ |
| 8 | Extract ad angle if high-performing | Meta Ads | When proven (30+ day performance) | ☐ |

### For Every UGC/Creator Video:

| # | Derivative | Channel | Timing | Status |
|---|-----------|---------|--------|--------|
| 1 | Create 60s, 30s, 15s cuts | Ads | Within 48 hours of delivery | ☐ |
| 2 | Test 3-5 different hooks on winning body | Ads | During creative testing cycle | ☐ |
| 3 | Extract 2-3 still frames for image ads | Ads | Within 48 hours | ☐ |
| 4 | Pull best quotes for social proof | Website + Email | Within 1 week | ☐ |
| 5 | Post on brand social (credited to creator) | Instagram/TikTok | Coordinated with creator | ☐ |
| 6 | Add to testimonial library | Website | Within 1 week | ☐ |
| 7 | Consider for email welcome flow | Email | Monthly review | ☐ |
| 8 | Consider for retargeting | Ads | When proven (7+ day performance) | ☐ |

### For Winners (Content That Performs):

| # | Action | Why |
|---|--------|-----|
| 1 | Brief new creators with same hook/angle | Proven angles should be iterated, not abandoned |
| 2 | Create variations (different person, same script) | Format × person interactions matter |
| 3 | Test winning angle on different platforms | What works on Meta may work on TikTok (or not) |
| 4 | Expand blog post into ultimate guide or series | Google rewards depth on topics with engagement |
| 5 | Turn blog post into downloadable lead magnet | Email list growth from proven content |
| 6 | Use as reference for future content briefs | Build a "what works" playbook |

---

## 3. Content Library Organization

### Folder Structure

```
/content-library/
│
├── /blog/
│   ├── /published/           ← Live blog posts (by date or pillar)
│   ├── /drafts/              ← In-progress content
│   └── /retired/             ← Content that's been superseded or removed
│
├── /video/
│   ├── /raw/                 ← Original creator deliverables
│   │   └── /{creator-name}/  ← Organized by creator
│   ├── /edited/              ← Cut versions (60s, 30s, 15s)
│   │   └── /{format}/        ← By length/format
│   └── /stills/              ← Screenshot extractions
│
├── /social/
│   ├── /carousels/           ← Instagram carousel graphics
│   ├── /reels/               ← Short-form video for Reels/TikTok
│   └── /threads/             ← Twitter/X thread drafts
│
├── /email/
│   ├── /newsletters/         ← Campaign email content
│   └── /flow-content/        ← Content for automated flows
│
└── /ads/
    ├── /creative/            ← Ad creative assets (see M14 test_log.json)
    └── /advertorial/         ← Native ad landing pages / advertorials
```

### Tagging System

Every piece of content should be tagged with:

| Tag Dimension | Examples | Purpose |
|---------------|----------|---------|
| **Pillar** | hydration-science, keto, performance, natural-health, comparison | Which content pillar it belongs to |
| **Hook type** | problem, curiosity, social-proof, ingredient, transformation | What angle drives engagement |
| **Audience** | biohacker, athlete, keto-dieter, wellness-parent, health-curious | Who it's for |
| **Format** | blog, video-60s, video-30s, carousel, thread, email | What shape it takes |
| **Performance** | winner, promising, average, underperformer | How it performed |
| **Stage** | awareness, consideration, conversion, retention | Where in the funnel |

---

## 4. Content Production Workflow

### Weekly Content Cycle (Bootstrapped)

For a 2-person team spending 5-8 hours/week on content:

| Day | Activity | Time | Output |
|-----|----------|------|--------|
| Monday | Write/finalize 1 blog post | 2-3 hrs | 1 published post |
| Monday | Add internal links + FAQ schema | 15 min | SEO optimization |
| Tuesday | Create social derivatives (carousel, thread) | 1 hr | 2-3 social posts |
| Wednesday | Record/edit 1 short-form video | 1 hr | 1 TikTok/Reel |
| Thursday | Schedule social posts for the week | 30 min | 4-5 scheduled posts |
| Friday | Draft next week's blog post (research + outline) | 1-2 hrs | Outline ready |
| Weekend | Schedule email newsletter (if weekly) | 30 min | 1 email send |

**Month 1-3 target**: 1 blog post/week + 3-5 social posts/week + 1 newsletter/week = ~20 total assets/week from 1 pillar piece

### AI-Assisted Content Production

AI tools can accelerate content creation but require human oversight, especially for health/supplement content (YMYL):

| Task | AI Role | Human Role |
|------|---------|------------|
| Blog post first draft | Generate outline + draft | Fact-check, add experience/expertise, verify claims |
| Meta descriptions | Generate options | Select and refine |
| Social captions | Generate variations | Choose tone, add personality |
| Email subject lines | Generate 10 options | A/B test winners |
| Keyword research | Surface opportunities | Validate with search tools |
| Content repurposing | Reformat content for channels | Review for platform fit |

**Critical rule for YMYL content**: Every health claim in AI-generated content must be verified against published research. Google penalizes unsubstantiated health claims. Add citations to studies. Have content reviewed by someone with relevant credentials where possible.

---

## 5. Content Performance Measurement

### Key Metrics by Channel

| Channel | Primary Metric | Secondary Metrics | Measurement Tool |
|---------|---------------|-------------------|-----------------|
| **Blog/SEO** | Organic sessions | Avg position, CTR, time on page, bounce rate | GA4 + GSC |
| **Social (organic)** | Engagement rate | Reach, saves, shares, profile visits | Platform analytics |
| **Email** | Click rate | Open rate, unsubscribe rate, revenue attributed | Klaviyo |
| **Ads (from content)** | ROAS | CTR, CPC, CPA | Meta Ads Manager |
| **Native ads** | CVR (advertorial → product) | CPC, time on advertorial, scroll depth | GA4 + platform |

### Content ROI Framework

Content ROI is notoriously hard to measure because organic content assists conversions without getting last-click credit. Use this framework:

1. **Direct attribution**: Organic traffic → same-session purchase (GA4 conversion paths)
2. **Assisted attribution**: Content touchpoint → later purchase within 30 days (GA4 attribution models)
3. **CAC reduction**: Track blended CAC monthly. As organic grows, blended CAC should decrease.
4. **Proxy metrics**: If you can't measure revenue directly, track leading indicators:
   - Organic traffic growth rate (target: 10-20% month-over-month)
   - Email list growth from content (target: 50-100 new subscribers/month from organic)
   - Keyword rankings improving (target: 5-10 keywords on page 1 within 6 months)

### Monthly Content Review

| Question | Data Source | Action if Red |
|----------|-----------|---------------|
| Is organic traffic growing? | GA4 | Review keyword strategy, increase publishing cadence |
| Are blog posts converting? | GA4 conversion paths | Add stronger CTAs, improve product integration |
| Which content pillars perform best? | GA4 by blog category tag | Double down on winners, deprioritize losers |
| Is social driving traffic to site? | GA4 traffic sources | Optimize link-in-bio, add CTAs to posts |
| Are repurposed pieces performing? | Platform analytics | Adjust repurposing format/timing |


---

### 📄 content_strategy.md

# Content & Distribution Strategy — M16: Content & SEO

**TUP**: M16
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift), HYP-001 (CAC)
**Danilo Source**: ops_model_v10_dump/408_content_gtm_strategy.json (5 rows), 409_content_calendar.json (8 rows)
**Cross-Reference**: M12 (Ad Creative), M17 (Email), M18 (SMS), M22 (UGC/Community), M14 (Testing)

---

## Purpose

Define IonWave's content strategy: what to create, where to distribute, how often, and how to measure. This file merges Danilo's Content & GTM Strategy (5 rows — barely a skeleton) and Content Calendar (generic day-of-week template) into a unified, actionable content strategy.

**Core principle**: Content is a compounding asset. Every piece makes future pieces more discoverable, more credible, and more efficient. But only if the content is genuinely valuable — Google and audiences punish thin, promotional content equally.

---

## 1. Channel Strategy (Go-To-Market)

### Channel Stack by Priority

| Rank | Channel | Role | Investment | Expected ROI Timeline |
|------|---------|------|-----------|----------------------|
| **1** | **Meta Ads** | Primary acquisition (paid) | 60-80% of marketing budget | Weeks (immediate) |
| **2** | **Email/SMS** | Retention + content distribution | $0-50/mo (Klaviyo free tier) | Immediate |
| **3** | **Blog/SEO** | Organic acquisition (long-term) | Time + $10-20/mo SEO app | 6-12 months |
| **4** | **TikTok (organic)** | Brand awareness, content factory | $0 (time only) | 1-3 months |
| **5** | **Instagram (organic)** | Community, brand identity | $0 (time only) | 3-6 months |
| **6** | **YouTube (Shorts + long-form)** | Search + discovery | $0 (time only) | 6-12 months |
| **7** | **Podcast guesting** | Authority, backlinks | $0 (time only) | 1-3 months to book |
| **8** | **Reddit/niche forums** | Authentic engagement, referral traffic | $0 (time only) | Immediate |
| **9** | **Pinterest** | Long-shelf-life visual content | $0 (time only) | 6-12 months |
| **10** | **Native Ads** (Taboola/Outbrain) | Advertorial-based acquisition | $2K+/mo minimum | Phase 2-3 (Month 6-12+) |

### What Danilo Had vs. What We Need

Danilo's 5-row GTM strategy listed channels correctly but lacked:
- Budget allocation guidance
- ROI timeline expectations
- Phase-gating (when to add each channel)
- Distribution strategy (content flows between channels)

### Phase-Gated Channel Activation

**Phase 0: Launch (Month 1-2)** — 3 channels only
- Meta Ads (paid acquisition)
- Email flows (retention + content distribution)
- Blog (start building SEO foundation — 1 post/week)

**Phase 1: Foundation (Month 2-4)** — Add organic social
- Add TikTok (daily posting — repurpose blog content to video)
- Add Instagram Reels (3-5x/week)
- Continue blog cadence (1 post/week)

**Phase 2: Expansion (Month 4-8)** — Add secondary channels
- Add YouTube Shorts (repurpose TikTok content)
- Start podcast guesting outreach (target 1-2 appearances/month)
- Begin Reddit/forum engagement (authentic, non-promotional)
- Scale blog to 2 posts/week if bandwidth allows

**Phase 3: Diversification (Month 8-12+)** — Add paid content channels
- Evaluate native advertising (only if Meta Ads proven and revenue >$30K/month)
- Add Pinterest (infographics, recipe pins, health tips)
- Consider YouTube long-form educational content
- Evaluate content syndication (Medium, LinkedIn)

---

## 2. Content Calendar Framework

### Weekly Content Rhythm

Danilo's day-by-day calendar was generic. Here's an IonWave-specific framework:

| Day | Blog | Social (TikTok/Reels) | Email | Time Budget |
|-----|------|----------------------|-------|-------------|
| **Monday** | Publish weekly blog post | Repurpose: blog key takeaway as talking-head video | — | 3-4 hrs |
| **Tuesday** | — | Educational content (science, ingredients, how-to) | — | 30 min |
| **Wednesday** | — | UGC repost or creator content | Newsletter (blog recap + 1 tip) | 1 hr |
| **Thursday** | — | Trend-riding or relatable content | — | 30 min |
| **Friday** | Draft next week's blog (research/outline) | Community content (Q&A, poll, behind-scenes) | — | 2 hrs |
| **Saturday** | — | Testimonial/social proof content | Promo email (if running offer) | 30 min |
| **Sunday** | — | Rest (or batch-create for the week) | — | 0-2 hrs |

**Total weekly time commitment**: 8-10 hours for content creation + distribution

### Monthly Content Mix

Target ratio per month (at 1 blog post/week, 5 social posts/week):

| Content Type | Blog | Social | Email |
|-------------|------|--------|-------|
| **Educational/Science** | 2 posts (50%) | 8-10 posts (40%) | 2 sends (50%) |
| **Social proof/Testimonial** | 0 | 4-6 posts (25%) | 1 send (25%) |
| **Product/Promotional** | 1 post (25%) | 3-4 posts (15%) | 1 send (25%) |
| **Community/Behind-scenes** | 0 | 3-4 posts (15%) | 0 |
| **Comparison/Decision-stage** | 1 post (25%) | 1-2 posts (5%) | 0 |

**The 80/20 rule**: 80% of content should educate, entertain, or inspire. 20% can sell. This ratio builds trust and keeps audience engaged. Flipping this ratio (too much selling) kills organic reach and email engagement.

---

## 3. AI-Assisted Content Production

### Google's Stance on AI Content (2025-2026)

Google does **not** ban AI-generated content. They penalize **low-quality, unreviewed mass-produced content** regardless of how it was made. The distinction:

| Approach | Google's Assessment | Risk Level |
|----------|-------------------|------------|
| AI writes first draft → human expert reviews, adds experience, fact-checks, adds citations | Acceptable, can rank well | LOW |
| AI writes entire article → human does light copyedit only | Risky for YMYL health content | MEDIUM |
| AI generates dozens of articles with no human oversight | Will be penalized (scaled content abuse) | HIGH |
| AI writes + human adds original photos, data, expert quotes, personal experience | Best practice — strong E-E-A-T signals | LOW |

### YMYL (Your Money or Your Life) Requirements

IonWave's health supplement content falls under Google's YMYL classification. This means **higher E-E-A-T standards**:

**Required E-E-A-T signals for every blog post:**

1. **Experience**: First-person content — "In our testing...", "When we formulated IonWave...", real customer stories
2. **Expertise**: Named author with credentials (or "Reviewed by [Name], RD/CSCS/MD")
3. **Authoritativeness**: Citations to PubMed studies, NIH resources, peer-reviewed journals (minimum 3-5 per health article)
4. **Trustworthiness**: Clear "About Us" page, editorial policy, supplement disclaimers, transparent sourcing

**What gets penalized:**
- Unsubstantiated health claims ("this supplement cures X")
- Anonymous content (no author attribution)
- Thin content (<500 words on complex health topics)
- Missing FDA disclaimer on supplement content
- Affiliate-first content (selling disguised as information)

### IonWave AI Content Workflow

```
1. RESEARCH (AI + Human)
   AI: Compile research, find relevant studies, generate outline
   Human: Verify studies exist, add IonWave-specific angles

2. FIRST DRAFT (AI)
   AI: Write 2,000-2,500 word draft from outline
   Human: Review for accuracy, voice, brand consistency

3. EXPERIENCE LAYER (Human only — AI cannot do this)
   Add: Personal product experience, customer quotes,
        original photos, lab test data, founder insights

4. EXPERT REVIEW (Human expert)
   Send to: Credentialed reviewer (RD, nutritionist, etc.)
   Cost: $50-150 per article (batch 3-5 for efficiency)
   Add: "Reviewed by [Name], [Credentials]" badge

5. SEO OPTIMIZATION (AI + Human)
   AI: Suggest keyword placement, generate meta description options
   Human: Select best options, add internal links, schema markup

6. PUBLISH + DISTRIBUTE (Human)
   Publish blog → repurpose per waterfall (see content_repurposing.md)
```

**Cost per article (bootstrapped):**
- Founder-written + AI assist: $0 (time only, ~3-5 hours)
- Freelance writer + AI assist: $100-250 per article ($0.05-0.10/word)
- Expert review: $50-150 per article
- **Total per article: $50-400** depending on approach

---

## 4. Content Distribution Strategy

### The Owned-First Principle

Most brands create content and pray for discovery. The right approach:

1. **Publish on owned channels first** (blog, email list)
2. **Repurpose to earned channels** (social, forums, podcasts)
3. **Amplify winners with paid** (boost top-performing organic content)

### Email as Primary Distribution Vehicle

Email is the highest-ROI distribution channel for DTC brands. Every blog post should flow into email:

- **Newsletter format**: 200-300 word summary + "Read the full guide →" link to blog
- **Cadence**: 1 educational email + 1 promotional email per week
- **Segmentation**: By interest (keto, athletic, general wellness) from Day 1
- **Cross-reference**: M17 (Email TUP) for flow architecture, M18 (SMS) for notification-level content

### Social Media Distribution

**TikTok/Reels strategy for supplement brand:**
- **Hook formula**: Problem → Surprising fact → "Here's what most people don't know" → CTA
- **Content types that work**: Science explainers, ingredient breakdowns, "what I take in a day", myth-busting, customer transformations
- **What to avoid**: Direct selling, unsubstantiated health claims, "before/after" without disclaimers
- **FTC compliance**: Disclose if content is promotional. Health claims must follow structure/function rules.

**Reddit/forum engagement:**
- Subreddits: r/keto, r/fasting, r/Supplements, r/electrolytes, r/intermittentfasting
- Rule: Be genuinely helpful first. Never post links in first 10+ comments.
- Goal: Build founder reputation as a knowledgeable contributor, not a salesperson

### Syndication

| Platform | Approach | Timing | SEO Note |
|----------|----------|--------|----------|
| **Medium** | Republish blog posts | 7-14 day delay after original | Use Medium's import tool (not copy-paste) — it sets canonical to your original URL. The delay ensures Google indexes your version first. Shopify's blog doesn't support custom canonical tags per article, so this timing-based approach is essential. |
| **LinkedIn** | Rewrite for professional angle | Same week as blog | Good if any B2B angle (corporate wellness) |
| **Quora** | Answer relevant questions with genuine expertise | Ongoing | Include link only when genuinely relevant |
| **Pinterest** | Create infographic versions of blog content | Same week | Pinterest content has 6-12 month shelf life |

---

## 4.5 Content Conversion Funnel *(Merged from Session A dialogue upgrade U5)*

Content traffic must convert through a defined pipeline. Blog readers don't buy immediately — they need nurturing:

```
BLOG VISITOR (100%)
  │
  ├── 60-70% bounce (single page, leave)
  │
  └── 30-40% engage (read >50%, click internal link)
        │
        ├── 3-5% email signup (lead magnet, newsletter CTA)
        │     │
        │     └── Email nurture sequence (5-7 emails over 14 days)
        │           │
        │           ├── 8-12% purchase from nurture
        │           │     │
        │           │     └── 40-50% subscribe (subscription-first checkout)
        │           │
        │           └── 88-92% don't purchase (yet — remain on list)
        │
        ├── 1-2% direct purchase (comparison/BOFU content)
        │     │
        │     └── 35-45% subscribe
        │
        └── 26-36% leave without converting (retarget via paid)
```

**Estimated conversion math** (per 1,000 organic visitors):
- 35 email signups (3.5%)
- 4 purchases from nurture (35 × 12%)
- 12 direct purchases (1.2% of traffic on BOFU content)
- **Total: ~16 purchases per 1,000 organic visitors** (1.6% blended CVR)
- At $59 AOV: **~$944 revenue per 1,000 organic visitors**

**Lead magnet options for email capture**:
- "The Marine Plasma Guide" (PDF download)
- "Electrolyte Protocol for Keto" (free checklist)
- "7-Day Hydration Challenge" (email drip)
- Newsletter signup (lowest friction, lowest conversion)

**Key integration**: The email nurture sequence lives in M17 (Email). Content generates the leads; email converts them.

[Confidence: C | Source: DTC supplement email conversion benchmarks. 1.6% blended CVR is conservative for quality organic traffic. Actual rates depend on content-product alignment and email sequence quality.]

---

## 5. Content Measurement Framework

### Key Metrics by Channel

| Channel | Primary Metric | Secondary Metrics | Tool |
|---------|---------------|-------------------|------|
| **Blog/SEO** | Organic sessions | Avg position, CTR, engagement time, scroll depth | GA4 + GSC |
| **Email** | Click rate | Open rate, unsubscribe rate, revenue attributed | Klaviyo |
| **Social (organic)** | Engagement rate | Reach, saves, shares, profile visits | Platform analytics |
| **Ads (from content)** | ROAS | CTR, CPC, CPA | Meta Ads Manager |

### Content ROI Attribution

Content ROI is hard to measure because organic content assists conversions without getting last-click credit:

1. **Direct**: Blog → same-session purchase (GA4 conversion paths)
2. **Assisted**: Content touchpoint → later purchase within 30 days (GA4 attribution)
3. **Proxy**: Track blended CAC monthly — as organic grows, blended CAC should decrease

### Monthly Content Review Questions

| Question | Action if Red |
|----------|---------------|
| Is organic traffic growing month-over-month? | Review keyword strategy, increase publishing cadence |
| Are blog posts driving email signups? (Target: 2-5% of visitors) | Add stronger CTAs, pop-ups, lead magnets |
| Which content pillar performs best? | Double down on winners |
| Is social driving site traffic? | Optimize link-in-bio, add stronger CTAs |
| Are repurposed pieces performing? | Adjust format/timing per channel |

### GA4 Setup Essentials

**Custom events to configure:**
- `scroll_depth` (25%, 50%, 75%, 90%, 100%)
- `content_cta_click` (product link, email signup, share)
- `blog_to_product` (source blog → destination product)

**Content groups:**
- By pillar: Hydration Science, Keto & Low-Carb, Athletic Performance, Natural Health, Comparisons
- By type: How-to, Listicle, Comparison, Ultimate Guide, Problem/Solution
- By funnel stage: TOFU (educational), MOFU (comparison), BOFU (product-focused)

**UTM discipline:**
Every distributed content piece needs UTM parameters:
- `utm_source`: platform (email, tiktok, instagram, medium, reddit)
- `utm_medium`: type (organic, paid, syndication, newsletter)
- `utm_campaign`: content_id (blog-keto-electrolytes-guide)
- `utm_content`: variant (carousel-v1, reel-v2)


---

### 📄 dialogue_summary.md

# M16 Persona Dialogue Summary

**TUP**: M16 — Content & SEO
**Date**: 2026-02-06
**Personas**: Growth Engineer, Skeptical Investor, Category Expert (SEO/Content)
**Protocol**: TWP-001 Phase 6
**Files Reviewed**: All 7 M16 files (content_strategy.md, seo_strategy.md, seo_keyword_research.json, seo_content_strategy.md, seo_link_building.md, technical_seo_checklist.md, content_repurposing.md)

---

## Persona Definitions

**Growth Engineer (GE)**: "What's the compounding mechanism? What are the unit economics of each content piece? Where's the growth loop?"

**Skeptical Investor (SI)**: "Show me evidence, not estimates. These traffic projections — are they grounded in comparable brands? Would I fund this content operation?"

**Category Expert — SEO/Content (CE)**: "I've done SEO for 10 DTC supplement brands. What does this strategy miss that the playbook doesn't cover?"

---

## ROUND 1

**CHALLENGE** (Growth Engineer): The SEO ROI projection table in seo_strategy.md shows Month 6 organic revenue at $590 and Month 24 at $26,550 — but the assumptions underlying CVR improvement from 2% to 3% are not grounded in any comparable data. What evidence supports that organic CVR will improve over time?

**RESPONSE** (Category Expert): CVR improvement on organic traffic is well-documented for content-led brands. Early organic traffic is mostly informational (blog readers learning about electrolytes). As the keyword mix shifts toward commercial terms (Phase 2-3), the traffic quality improves. Additionally, retargeting organic visitors with Meta ads creates a second conversion chance. However, 3% organic CVR is optimistic for a supplement brand — 1.5-2.5% is more realistic for blended organic traffic. The projection should be tempered.

**SYNTHESIS** (Skeptical Investor): The projection is directionally sound but the CVR assumption is aggressive. For investor-grade projections, use 1.5% blended organic CVR, not 3%. The Month 24 number drops from $26,550 to ~$13,275 — still excellent ROI against $10,800 cumulative investment, but more honest. Update the projection table.

**OUTCOME**: UPGRADED
**ACTION**: Add a note to seo_strategy.md ROI projection table noting CVR assumptions are optimistic and providing a conservative scenario alongside the base case.

---

## ROUND 2

**CHALLENGE** (Category Expert): The seo_content_strategy.md recommends publishing the "LMNT Alternative" comparison article in Week 1. For a brand-new domain with zero authority, comparison content targeting a competitor's brand name is risky. Google may not trust you to make fair comparisons when you have no track record. Additionally, competitor-brand keywords can trigger legal issues if the comparison is perceived as misleading.

**RESPONSE** (Growth Engineer): The LMNT alternative keyword has 2,900 volume at low KD — it's mathematically the best first target. The risk is that Google suppresses a brand-new site's comparison content. The mitigation: make the article genuinely objective (include 5+ alternatives, not just IonWave), cite ingredient differences factually, and don't trash LMNT. This approach satisfies Google's quality guidelines and avoids legal risk. Wait until you have 3-5 other articles published first, then release the comparison — don't make it literally Week 1.

**SYNTHESIS** (Skeptical Investor): Move "LMNT Alternative" from Week 1 to Week 3-4. Publish 2-3 educational pieces first (marine plasma, electrolyte guide) to establish some trust signal before publishing comparison content. The keyword is too valuable to skip, but publishing sequence matters. Update the first-12-posts launch sequence.

**OUTCOME**: UPGRADED
**ACTION**: Adjust the first-12-posts table in seo_content_strategy.md — move LMNT Alternative to Week 3-4 position, lead with the pillar page (Complete Guide to Electrolytes) in Week 1 and a marine plasma educational piece in Week 2.

---

## ROUND 3

**CHALLENGE** (Skeptical Investor): The content_strategy.md says "8-10 hours/week for content creation + distribution" and the seo_content_strategy.md calls for 1 blog post/week plus social derivatives. Who is doing this? Caio is also running paid ads, managing product, handling logistics, running email marketing, and building the brand. Is 8-10 hours/week for content realistic for a solo founder with no content hire?

**RESPONSE** (Category Expert): It's not realistic for Month 1-3. A more honest assessment: Caio can do 4-5 hours/week on content initially, which supports 2 blog posts/month (not 4). The strategy should include a clear "founder mode" vs. "delegated mode" distinction. In founder mode, cut publishing cadence to biweekly and focus on the highest-value pieces only (pillar pages + LMNT comparison + marine plasma content).

**SYNTHESIS** (Growth Engineer): This is a real constraint. Add a "Founder Mode" tier to the publishing cadence: 2 posts/month (highest-priority keywords only) at 4-5 hours/week. Scale to 1/week only when there's a freelance writer or AI-assisted workflow producing quality output. The current Phase 1 target of "1 post/week = 12 posts in 3 months" should be "6-8 posts in 3 months" in Founder Mode.

**OUTCOME**: UPGRADED
**ACTION**: Add "Founder Mode" publishing tier to seo_content_strategy.md Phase 1 with realistic 2 posts/month cadence. Note that the 1/week cadence assumes at least a freelance writer or dedicated content time block.

---

## ROUND 4

**CHALLENGE** (Growth Engineer): The link building strategy (seo_link_building.md) targets 3-5 new referring domains/month in Phase 1. But expert quote platforms (Qwoted, Featured.com) are the #1 recommended tactic. What's the realistic conversion rate on these platforms for a no-name supplement brand founder? Are there recent data points on success rates?

**RESPONSE** (Skeptical Investor): The conversion rate on expert quote platforms for unknown founders is low — realistically 5-10% of pitches result in placements for new users without established media credibility. Caio would need to pitch 30-50 queries/month to get 2-3 placements. That's feasible at 15-30 min per pitch, but the document should set realistic expectations rather than implying 3-5 placements/month is easy.

**SYNTHESIS** (Category Expert): The tactic ranking is correct — expert quote platforms ARE the highest-ROI link building tactic for bootstrapped brands. But add conversion rate expectations: pitch 5-10/week, expect 1-2 placements/month initially, improving to 3-5/month as you build platform reputation (after 2-3 months). Also note: the first 5-10 pitches will likely fail. Persistence matters. This context helps set expectations without discouraging the tactic.

**OUTCOME**: UPGRADED
**ACTION**: Add expected conversion rates and ramp-up timeline to seo_link_building.md expert quote platform section.

---

## ROUND 5

**CHALLENGE** (Category Expert): The technical_seo_checklist.md is solid but misses one critical Shopify issue: Shopify's blog does not support `rel="canonical"` customization per article. If IonWave ever syndicates content to Medium or other platforms, there's no native way to set the canonical back to your original. This can cause duplicate content issues that dilute SEO value.

**RESPONSE** (Growth Engineer): This is a real technical gap. The content_strategy.md mentions Medium syndication with "use canonical tag pointing to your site" — but that instruction is incomplete because Medium sets its own canonical, and Shopify's blog doesn't let you declare canonical authority easily. The workaround: use Medium's import tool (which honors the original URL as canonical) and delay syndication by 7-14 days to ensure Google indexes the original first.

**SYNTHESIS** (Skeptical Investor): Practical, not critical. Add a note to both the technical SEO checklist and the content strategy syndication section. The real risk is low — Medium's import tool handles it correctly, and the 7-14 day delay is already in the content_strategy.md. Just add the "why" (canonical handling on Shopify) so the reasoning is clear.

**OUTCOME**: RESOLVED (existing 7-14 day delay recommendation already handles this; add explanatory note only)
**ACTION**: Add brief canonical note to syndication section of content_strategy.md.

---

## ROUND 6

**CHALLENGE** (Skeptical Investor): The keyword research file lists "marine plasma electrolyte benefits" with est. volume 50-100 and KD <10. The content strategy is heavily invested in marine plasma as "uncontested territory." But 50-100 monthly searches is tiny. If the real volume is closer to 10-20 (which is possible for such a niche term), IonWave could spend significant effort creating 5-6 marine plasma articles that generate almost no traffic. What's the risk/reward calculation?

**RESPONSE** (Category Expert): The risk is real but the strategy is still sound. Marine plasma content serves THREE purposes, not just organic traffic: (1) SEO — even 50 visits/month from ultra-targeted terms has 3-5% CVR, (2) Brand authority — when anyone Googles "marine plasma electrolyte," IonWave MUST own page 1, (3) Content hub — marine plasma articles build the topical authority needed to rank for broader "electrolyte" terms. The investment is 4-6 articles total, not 20. At 2-3 hours per article with AI assist, that's 10-18 hours total — minimal downside.

**SYNTHESIS** (Growth Engineer): Frame it correctly: marine plasma content is a topical authority investment, not a traffic play. The ROI is measured in (a) brand protection — owning your category's search results, and (b) supporting cluster — marine plasma articles strengthen the Hydration Science and Natural Health pillars, which DO target higher-volume keywords. Add this framing to the natural health pillar description in seo_content_strategy.md so the rationale is explicit.

**OUTCOME**: RESOLVED (existing strategy is sound; add framing clarification)
**ACTION**: Add "triple-purpose" rationale note to the Natural Health pillar section in seo_content_strategy.md.

---

## ROUND 7

**CHALLENGE** (Growth Engineer): The native ads section (seo_link_building.md) gates activation behind "$30K+ monthly revenue." But the document doesn't specify what happens if native ads are never activated because IonWave doesn't reach $30K/month in the relevant timeframe. Is native advertising essential to the M16 strategy, or is it a nice-to-have that can be deprioritized entirely?

**RESPONSE** (Category Expert): Native advertising is absolutely a nice-to-have, not essential. IonWave's core content strategy (blog + SEO + email + social) works without native ads. In fact, most DTC supplement brands under $50K/month revenue never use Taboola/Outbrain. The native ads section was included because Danilo had a full tab on it — but the honest framing is "Phase 3+ only, and many brands skip this entirely."

**SYNTHESIS** (Skeptical Investor): Agreed. Mark native ads as optional in the strategy. The prerequisite gate is correct and sufficient — it naturally prevents premature spend. No change needed beyond adding "Optional — many successful DTC brands never use native ads" to the section header.

**OUTCOME**: RESOLVED
**ACTION**: Add "Optional channel" label to native ads section header.

---

## ROUND 8

**CHALLENGE** (Category Expert): Looking at the full M16 package, I notice there's no mention of Google Business Profile or local SEO — which is correctly excluded for a DTC brand. But there's also no mention of Google Merchant Center / Google Shopping. For a product-based business, Shopping ads and free product listings through Merchant Center are a significant traffic source. Is this covered elsewhere?

**RESPONSE** (Growth Engineer): Google Shopping is a paid advertising channel, which falls under M12 (Ad Creative) and M10 (Pricing/Offer), not M16 (Content & SEO). However, the free Google Shopping listings (which require Merchant Center setup but no ad spend) ARE an SEO-adjacent concern. This is a legitimate gap — free product listings should be mentioned in the technical SEO checklist.

**SYNTHESIS** (Skeptical Investor): Good catch. Add Google Merchant Center setup (for free product listings) to the technical SEO checklist as a post-launch action item. Keep paid Shopping ads in M12's scope. This is a small but real gap that would have been missed.

**OUTCOME**: UPGRADED
**ACTION**: Add Google Merchant Center / free Shopping listings to technical_seo_checklist.md as a post-launch item.

---

## Saturation Assessment

**Round 7**: RESOLVED
**Round 8**: UPGRADED (minor gap)
**Pattern**: Last 3 rounds produced 2 RESOLVED + 1 minor UPGRADED. Challenges are becoming increasingly peripheral (native ads optionality, Google Merchant Center). Core strategy and content are sound.

**Saturation reached at Round 8.** Core content is coherent across all 3 personas. Remaining challenges are edge cases, not structural issues.

---

## Summary of Upgrades Applied

| Round | Upgrade | File Affected |
|-------|---------|---------------|
| 1 | Add conservative CVR scenario to SEO ROI projection | seo_strategy.md |
| 2 | Move LMNT Alternative from Week 1 to Week 3-4; lead with pillar page | seo_content_strategy.md |
| 3 | Add "Founder Mode" publishing tier (2 posts/month, 4-5 hrs/week) | seo_content_strategy.md |
| 4 | Add conversion rate expectations for expert quote platforms | seo_link_building.md |
| 5 | Add canonical handling note for syndication | content_strategy.md |
| 6 | Add triple-purpose rationale for marine plasma content | seo_content_strategy.md |
| 7 | Add "Optional channel" label to native ads | seo_link_building.md |
| 8 | Add Google Merchant Center to technical SEO checklist | technical_seo_checklist.md |

---

## Unresolved Gaps

| Gap | Source | Priority | How to Close |
|-----|--------|----------|-------------|
| Real keyword volumes for marine plasma terms unknown | Round 6 | P1 | Google Search Console data after 1-2 months live |
| Expert quote platform conversion rates are estimates | Round 4 | P2 | Track actual pitch:placement ratio for first 3 months |
| Organic CVR assumptions unverified | Round 1 | P2 | GA4 data after 3+ months of organic traffic |
| Freelance writer quality for YMYL health content untested | Round 3 | P2 | Test 2-3 freelance writers with sample articles before committing |

---

## "What Would Have Been Missed" Without Dialogue

1. **Publishing sequence error**: LMNT Alternative as Week 1 content on a brand-new domain would have undermined the comparison's credibility. Moving to Week 3-4 after establishing trust signals is a material improvement.
2. **Bandwidth realism**: 1 post/week assumed a content team. Founder Mode at 2/month is the honest starting point.
3. **ROI over-projection**: 3% organic CVR was too aggressive. Conservative scenario prevents false expectations.
4. **Google Merchant Center gap**: Free Shopping listings are a zero-cost traffic source that wouldn't have appeared in any M16 content tab from Danilo.
5. **Expert platform expectations**: Without conversion rate context, Caio might abandon the tactic after 10 failed pitches — when persistence through the first month is exactly what's needed.


---

### 📄 dialogue_summary_sessionA.md

# Persona Dialogue Summary — M16: Content & SEO

**TUP**: M16
**Date**: 2026-02-06
**AI Model**: claude-opus-4-6
**Personas**: SEO Strategist, DTC Growth Operator, Content Marketing Skeptic
**Rounds**: 5
**Saturation**: Yes (3 consecutive RESOLVED at rounds 3-5)
**Upgrades Applied**: 6
**Unresolved Issues**: 0

---

## Persona Profiles

| Persona | Perspective | Challenge Focus |
|---------|-----------|----------------|
| **SEO Strategist** | 10+ years SEO experience, managed DA 0→60 builds, Shopify-specific expertise | Technical accuracy, keyword difficulty realism, timeline feasibility |
| **DTC Growth Operator** | Runs a $5M+ DTC supplement brand, manages content team of 3 | Resource realism, ROI expectations, content-to-revenue attribution |
| **Content Marketing Skeptic** | CFO perspective — questions content investment when paid ads are measurable | Content ROI justification, opportunity cost, when to kill the program |

---

## Round 1: SEO Strategist Challenges

### Challenge 1.1: "Your keyword volume estimates for marine plasma are generous"
**Objection**: Marine plasma keywords may have even LESS volume than estimated. "What is marine plasma" could be 50-100 searches/month, not 200-500. You're in a category that doesn't exist yet in consumer search.

**Resolution**: Valid concern. The low volume is actually the POINT — low competition means easy ranking. But we need to be honest: **marine plasma keywords alone won't drive meaningful traffic volume.** The real traffic comes from Pillars 2-5 (electrolytes, keto, comparisons) where volume exists. Marine plasma content builds authority and captures the small-but-growing category search demand. → **UPGRADE U1: Add honest volume caveat to keyword research document.**

**Status**: RESOLVED with upgrade U1.

### Challenge 1.2: "DA growth to 20-35 in 12 months is ambitious without budget"
**Objection**: Getting to DA 20-35 requires 75-150 referring domains. For a bootstrapped brand doing 0-budget link building, that's very aggressive. Realistically, HARO responses have a 5-10% placement rate, guest posts take weeks to negotiate, and podcast appearances require existing credibility.

**Resolution**: Fair. Revise the DA trajectory to be more conservative, especially Month 1-6 when outreach pipeline is being built. → **UPGRADE U2: Adjust DA targets in link building doc — Month 6 target from 10-20 to 10-15, Month 12 from 20-35 to 15-30.**

**Status**: RESOLVED with upgrade U2.

### Challenge 1.3: "Shopify blog SEO is structurally weaker than WordPress"
**Objection**: Shopify's blog is an afterthought compared to WordPress. The forced `/blogs/` URL structure, limited category/tag system, and lack of plugins like Yoast creates a real SEO handicap. Your technical SEO section acknowledges limitations but doesn't address the strategic implication: Shopify blog SEO has a ceiling.

**Resolution**: This is a known tradeoff. Shopify's ecommerce + blog-on-same-domain approach has the advantage of domain authority consolidation (blog links boost product page rankings and vice versa). WordPress would require either a subdomain (bad for authority sharing) or a complex subfolder setup. For IonWave's scale, Shopify blog is sufficient. The ceiling matters at 500+ articles, not 100. → No upgrade needed. Documented tradeoff is acceptable.

**Status**: RESOLVED. No upgrade.

---

## Round 2: DTC Growth Operator Challenges

### Challenge 2.1: "1 article/week in Month 1-3 is unrealistic for a solo founder"
**Objection**: Your content calendar assumes someone is dedicating 5-10 hours/week to content production from Day 1. A solo founder launching a supplement brand is doing product sourcing, Shopify setup, ad creative, customer service, and a hundred other things. Content will be the first thing to slip.

**Resolution**: Critical reality check. The calendar should distinguish between "must-have at launch" content (product pages, 3 comparisons, 1 pillar draft) and "nice-to-have" ongoing content. The weekly cadence can start at Month 2, not Day 1. → **UPGRADE U3: Add "Minimum Viable Content" section to content calendar — what absolutely must be live at launch (6 pages) vs what can wait.**

**Status**: RESOLVED with upgrade U3.

### Challenge 2.2: "Content ROI breakeven at 8-10 months assumes things go well"
**Objection**: Your measurement framework says content ROI breakeven at 8-10 months. In my experience, for a new brand with no existing audience, it's more like 12-18 months before content generates meaningful attributable revenue. The "equivalent paid traffic cost" calculation is a vanity metric — you can't deposit saved CPC.

**Resolution**: Fair pushback on the "equivalent paid traffic cost" metric. It is useful for justifying the investment but shouldn't be the primary ROI measure. Adjust the breakeven expectation. → **UPGRADE U4: Revise content ROI breakeven estimate in measurement framework from 8-10 months to 10-14 months. Add caveat that "equivalent paid traffic cost" is a directional metric, not real revenue.**

**Status**: RESOLVED with upgrade U4.

### Challenge 2.3: "Where's the content-to-subscription pipeline?"
**Objection**: Your content strategy talks about driving traffic but doesn't explicitly map the path from blog reader → email subscriber → customer → subscriber. The subscription pipeline matters because content-acquired customers may have different subscription rates than paid-acquired customers.

**Resolution**: Good catch. The content strategy should include an explicit conversion funnel from content. → **UPGRADE U5: Add "Content Conversion Funnel" section to content strategy doc — Blog → Email Capture (lead magnet or newsletter) → Nurture Sequence → First Purchase → Subscription. Include estimated conversion rates at each stage.**

**Status**: RESOLVED with upgrade U5.

---

## Round 3: Content Marketing Skeptic Challenges

### Challenge 3.1: "Why not spend this time/money on more ads instead?"
**Objection**: If IonWave's paid ads are working at $35-40 CAC, why divert founder time to content that won't pay off for 10-14 months? The opportunity cost of content is real — every hour writing blog posts is an hour not optimizing ad creative, negotiating with suppliers, or talking to customers. At IonWave's stage, focus beats diversification.

**Resolution**: This is the right question. The answer is that content is NOT about Month 1-6 returns — it's about building a **structural advantage** that compounds. Paid ads have no compounding effect; every dollar of ad spend buys one impression. Content creates permanent assets. However, the skeptic is right that content should NOT consume >10-15% of founder time in the first 3 months. The Minimum Viable Content approach (U3) addresses this. → No additional upgrade needed. U3 already handles this.

**Status**: RESOLVED. U3 addresses timing.

### Challenge 3.2: "Your organic traffic targets of 15-25% at Month 12 seem high"
**Objection**: Most new DTC brands I've seen are at 8-12% organic at Month 12, not 15-25%. Your targets assume consistently excellent execution, which rarely happens at a bootstrapped startup. What if organic is only 8-10% — is the content program still worth it?

**Resolution**: Good calibration. Adjust the Month 12 target range to be more conservative. Even at 8-10% organic, the program is valuable: that's $0 marginal CAC traffic. → **UPGRADE U6: Adjust Month 12 organic traffic target from 15-25% to 10-20% across all documents. Keep 15-25% as "aggressive" scenario, 10-15% as "base case."**

**Status**: RESOLVED with upgrade U6.

---

## Round 4: SEO Strategist Follow-Up

### Challenge 4.1: "Your YMYL handling needs a specific process, not just guidelines"
**Objection**: You mention E-E-A-T and YMYL but don't have a specific workflow for health content review. Google is increasingly serious about health content quality. You need an explicit review process, not just "cite sources."

**Resolution**: The content quality gate already covers this (fact-check, FTC compliance, source citations). The existing process is sufficient for IonWave's scale. Adding a separate medical review board process would be overengineering for a brand with 0-50 articles. Revisit when content volume justifies it. → No upgrade needed.

**Status**: RESOLVED. Existing quality gate is sufficient.

---

## Round 5: All Personas — Final Review

All three personas reviewed the upgraded content. No new objections raised. Consensus:

- **SEO Strategist**: "The revised DA targets and volume caveats make this realistic. Good Shopify tradeoff analysis."
- **DTC Growth Operator**: "The Minimum Viable Content approach and content conversion funnel make this executable for a solo founder."
- **Content Skeptic**: "Revised organic targets are more honest. The 10-14 month ROI breakeven is realistic if execution is consistent."

**Status**: SATURATED — 3 consecutive rounds without new substantive objections.

---

## Upgrade Registry

| ID | Source | Change | Applied To | Confidence Impact |
|----|--------|--------|-----------|------------------|
| **U1** | SEO Strategist R1 | Add honest volume caveat for marine plasma keywords | keyword_research.md §2.1 | No grade change — honesty improvement |
| **U2** | SEO Strategist R1 | Revise DA targets: Month 6 to 10-15, Month 12 to 15-30 | link_building.md §1.1 | No grade change — realism improvement |
| **U3** | DTC Growth Operator R2 | Add "Minimum Viable Content" section to content calendar | content_calendar.md (new §2.5) | No grade change — executability improvement |
| **U4** | DTC Growth Operator R2 | Revise content ROI breakeven from 8-10 to 10-14 months | content_measurement.md §5.1 | No grade change — realism improvement |
| **U5** | DTC Growth Operator R2 | Add "Content Conversion Funnel" section | content_strategy.md (new §5.5) | Slight upgrade — adds missing conversion pipeline |
| **U6** | Content Skeptic R3 | Adjust Month 12 organic target from 15-25% to 10-20% | seo_strategy.md §1.1, content_measurement.md §2.1 | No grade change — conservative calibration |

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total challenges raised | 8 |
| Resolved with upgrade | 6 |
| Resolved without upgrade | 2 |
| Unresolved | 0 |
| Rounds to saturation | 5 |
| Consecutive RESOLVED rounds | 3 (rounds 3-5) |


---

### 📄 opkit_content_seo.md

# Content & SEO OpKit — OK-M16-001

**OpKit ID**: OK-M16-001
**Type**: Production
**For TUP**: M16 — Content & SEO
**Version**: 1.0.0
**Date**: 2026-02-06
**Graded Example**: IonWave Trade #84 (quality: 8.4/10)

---

## What This OpKit Produces

A complete content and SEO system for a DTC consumable brand, including:
1. Content strategy (channels, calendar, distribution, measurement)
2. SEO strategy (timeline, E-E-A-T infrastructure, keyword phasing, competitive positioning)
3. SEO keyword research (phased by difficulty for a new domain)
4. SEO content strategy (pillar/cluster model, blog templates, publishing cadence)
5. Link building playbook (tactics, quality criteria, native ads phase-gating)
6. Technical SEO checklist (pre-launch + ongoing maintenance)
7. Content repurposing system (waterfall model, checklists, library structure)

---

## Instructions: How to Produce This For Any Trade

### Step 1: Assess the Starting Position

Before building a content/SEO strategy, document:
- [ ] **Domain age**: New domain (0) or existing domain with history?
- [ ] **Current Domain Rating**: Check with Ahrefs free tool
- [ ] **Existing content**: How many pages are indexed? What's the content quality?
- [ ] **YMYL classification**: Does the product/industry fall under Google's Your Money or Your Life guidelines? (Health, finance, legal, safety = YMYL)
- [ ] **Product type**: Physical product, digital product, SaaS, service?
- [ ] **Budget tier**: Bootstrapped (<$5K/month marketing), growth ($5-25K), scale ($25K+)?
- [ ] **Team capacity**: Solo founder, 2-person team, dedicated content person?

### Step 2: Choose Content Pillars

Identify 3-5 content pillars based on:
1. **Product adjacency**: Topics directly related to your product's use case
2. **Audience interest**: What your target customers search for
3. **Competitive gap**: Topics where you have a unique angle or uncontested territory
4. **Purchase intent mix**: At least 1 high-intent pillar (comparisons) + 2-3 informational pillars

Template:
```
Pillar 1: [Broadest audience topic] → Pillar page: "[Complete Guide to X]"
Pillar 2: [Highest purchase intent niche] → Pillar page: "[X for Y: Everything You Need]"
Pillar 3: [Brand differentiator topic] → Pillar page: "[Your Unique Angle Deep-Dive]"
Pillar 4: [Problem/Solution] → Pillar page: "[Signs of X / How to Fix Y]"
Pillar 5: [Comparisons] → Pillar page: "[Best X Products [Year]]"
```

### Step 3: Build Keyword Research

For each pillar, find 5-10 target keywords using:
1. Free: Google Keyword Planner, Google Search Console (post-launch), AnswerThePublic
2. Paid: Ubersuggest ($29/mo), Ahrefs ($99/mo)

Organize by phase:
- **Phase 1 (Month 1-6)**: KD <20, volume <500 — your first wins on a new domain
- **Phase 2 (Month 6-12)**: KD 20-40, volume 500-3,000 — requires some authority
- **Phase 3 (Month 12+)**: KD 40+, volume 5,000+ — only after DR 30+

### Step 4: Set Up E-E-A-T Infrastructure (If YMYL)

Required for health, finance, legal, or safety products:
- Author bios with credentials on every content piece
- Expert reviewer badge ("Reviewed by [Name], [Credentials]")
- Minimum 3-5 citations to authoritative sources per article
- About page with team credentials
- Editorial policy page
- Supplement/financial/legal disclaimers as required

### Step 5: Create Technical SEO Checklist

Platform-specific (Shopify, WordPress, custom):
- Site speed / Core Web Vitals targets
- Schema markup (Product, Article, FAQ, Organization)
- Crawlability (sitemap, robots.txt, canonical tags)
- Mobile responsiveness
- Security (SSL, trust signals)

### Step 6: Design Content Calendar

Based on team capacity:
- **Solo founder**: 2 posts/month (4-5 hrs/week)
- **Founder + freelancer**: 1 post/week (8-10 hrs/week combined)
- **Dedicated content person**: 2-3 posts/week

### Step 7: Build Link Building Playbook

Prioritize by effort/impact for current stage:
1. Expert quote platforms (Qwoted, Featured.com)
2. Podcast guesting
3. Guest posting
4. Competitor backlink mining
5. Resource page outreach
6. Original research/data content
7. Broken link building

### Step 8: Create Content Repurposing System

Design the waterfall:
- 1 pillar content piece → X derivative assets
- Define checklists per content type (blog post → social + email + SEO)
- Define "winner escalation" protocol for top-performing content

---

## Grading Rubric

| Grade | Criteria |
|-------|---------|
| **A (9-10)** | All pillars data-backed with verified keyword research. E-E-A-T fully implemented. 6+ months of published content with measurable organic traffic growth. Link building producing 5+ new referring domains/month. Content waterfall consistently executed. |
| **B (7-8.5)** | Pillars well-defined with estimated keyword data. E-E-A-T infrastructure in place. Publishing cadence consistent. Some link building traction. Keyword research needs live data verification. |
| **C (5-6.5)** | Pillars defined but keyword research is generic. E-E-A-T partially implemented. Publishing inconsistent. No link building. Content repurposing ad hoc. |
| **D (3-4.5)** | Generic content strategy not tailored to product/market. No keyword research. No E-E-A-T awareness. No publishing cadence. |
| **F (<3)** | No content strategy. No SEO awareness. Random blog posts with no keyword targeting. |

---

## Graded Example: IonWave Trade #84

**Quality Score**: 8.4/10 (B+ — strong content pack limited by unverified keyword data)

**What makes it B+ (not A)**:
- Keyword volumes are estimates, not verified with paid tools (upgrade: GSC + Ubersuggest post-launch)
- No actual Core Web Vitals data for Shopify theme (upgrade: run PageSpeed Insights after theme selection)
- No competitor backlink analysis completed (upgrade: Ahrefs free check on LMNT, AG1)
- No published content yet — strategy is pre-launch planning, not proven execution

**What makes it strong**:
- 7 comprehensive files covering all content/SEO dimensions
- Research-grounded with current data (HARO replacement, YMYL requirements, AI content stance)
- Persona dialogue produced 5 material upgrades
- Realistic timelines calibrated to bootstrapped DTC supplement space
- Founder Mode publishing cadence acknowledges real bandwidth constraints
- Marine plasma identified as uncontested keyword territory with triple-purpose rationale
- Phase-gated channel activation prevents premature spend

**Files in the graded example**:
1. `content_strategy.md` — channel strategy, calendar, AI workflow, distribution, measurement
2. `seo_strategy.md` — timeline, E-E-A-T, competitive analysis, budget, ROI projections
3. `seo_keyword_research.json` — 23 keywords in 3 phases, organized by intent and difficulty
4. `seo_content_strategy.md` — 5 pillar/cluster models, 12-post launch sequence, blog templates
5. `seo_link_building.md` — 8 link building tactics, native ads playbook, monthly action plan
6. `technical_seo_checklist.md` — Shopify-specific checklist, schema types, tool stack
7. `content_repurposing.md` — waterfall model, checklists, library structure, production workflow

---

## Scaffold: Quick-Start Template

For a new Trade implementing M16, copy and customize these section headers:

### Content Strategy Scaffold
```
1. Channel Stack (rank by priority for YOUR product/market)
2. Phase-Gated Channel Activation (what opens when)
3. Content Calendar (weekly rhythm)
4. Content Mix (80/20 educational/promotional)
5. AI-Assisted Workflow (if applicable, with YMYL considerations)
6. Distribution Strategy (owned-first)
7. Measurement Framework (metrics by channel)
```

### SEO Strategy Scaffold
```
1. Why SEO Matters for [Brand] (product-specific case)
2. SEO Timeline Reality (calibrated to domain age + competition)
3. E-E-A-T Infrastructure (if YMYL — required pages, author bios, expert review)
4. SEO Pillars (Technical → On-Page → Content → Link Building)
5. Budget Allocation (by marketing budget tier)
6. ROI Projection (base + conservative scenarios)
7. Success Metrics (monthly tracking with targets)
8. Intelligence Gaps (what you don't know yet)
```

### Keyword Research Scaffold
```json
{
  "keyword_categories": ["Brand", "Transactional", "Commercial", "Informational"],
  "phase_1_long_tail": {"criteria": "KD <20, vol <500", "keywords": []},
  "phase_2_medium_tail": {"criteria": "KD 20-40, vol 500-3000", "keywords": []},
  "phase_3_head_terms": {"criteria": "KD 40+, vol 5000+", "keywords": []}
}
```


---

### 📄 seo_content_strategy.md

# SEO Content Strategy — M16: Content & SEO

**TUP**: M16
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift), HYP-001 (CAC)
**Danilo Source**: ops_model_v10_dump/413_seo_content_strategy.json (21 rows)
**Cross-Reference**: seo_keyword_research.json (keyword targets), content_strategy.md (distribution), content_repurposing.md (asset waterfall)

---

## Purpose

Define IonWave's blog content architecture using a pillar/cluster SEO model — the proven approach for building topical authority in competitive niches. Each pillar page is a comprehensive resource; each cluster article is a supporting piece that links back to it.

**The pillar/cluster model explained**: Google doesn't rank individual pages in isolation. It evaluates topical authority — how comprehensively your site covers a subject. A single "electrolytes for keto" article on a site with no other keto content will lose to a mediocre article on a site with 15 keto-related pages, all interlinked.

---

## 1. Content Pillars & Topic Clusters

### Pillar 1: Hydration Science (Broadest Audience)

**Pillar page**: "The Complete Guide to Electrolytes: What They Are, Why You Need Them, and How to Get Enough"
- Target keyword: "electrolyte guide" / "electrolyte supplement benefits"
- Word count: 3,000-5,000 words
- Format: Ultimate guide with table of contents, infographics, FAQ section
- Target audience: Health-curious, general wellness

**Cluster articles** (8-10 supporting pieces):

| # | Title Pattern | Target Keyword | KD | Phase |
|---|--------------|---------------|-----|-------|
| 1 | Signs of Electrolyte Imbalance (and What to Do) | signs of electrolyte imbalance | Low-Med | 1-2 |
| 2 | Ocean Minerals for Hydration: What Science Says | ocean minerals for hydration | <10 | 1 |
| 3 | Marine Plasma Electrolyte Benefits Explained | marine plasma electrolyte benefits | <10 | 1 |
| 4 | Electrolyte Powder vs. Tablet: Which Is Better? | electrolyte powder vs tablet | 10-15 | 1 |
| 5 | How Much Water Do You Actually Need? (It's Not 8 Glasses) | daily water intake guide | 20-30 | 2 |
| 6 | Trace Minerals Supplement Benefits: Beyond Sodium & Potassium | trace minerals supplement benefits | 15-25 | 1 |
| 7 | Dehydration Symptoms Most People Miss | dehydration symptoms | 25-35 | 2 |
| 8 | Why Your Electrolyte Supplement Might Not Be Working | electrolyte supplement problems | <15 | 1 |
| 9 | The Science Behind Ocean Mineral Sourcing | ocean minerals benefits | Low | 2 |
| 10 | Electrolytes and Sleep: What the Research Shows | electrolytes for sleep | <20 | 1 |

**Internal linking rule**: Every cluster article links back to the pillar page. The pillar page links out to every cluster article. Cross-link between cluster articles when relevant.

---

### Pillar 2: Keto & Low-Carb (Highest Purchase Intent)

**Pillar page**: "Electrolytes on Keto: The Complete Guide to Avoiding Keto Flu and Optimizing Performance"
- Target keyword: "electrolytes for keto" / "keto electrolytes"
- Word count: 3,000-5,000 words
- Format: Guide with protocol tables, dosage charts, FAQ
- Target audience: Keto dieters, fasting practitioners

**Cluster articles** (6-8 pieces):

| # | Title Pattern | Target Keyword | KD | Phase |
|---|--------------|---------------|-----|-------|
| 1 | Electrolytes for Fasting: What to Take and When | electrolytes for fasting headache | 5-15 | 1 |
| 2 | Signs of Electrolyte Deficiency During Fasting | signs of electrolyte deficiency during fasting | 5-15 | 1 |
| 3 | How Much Sodium During Fasting? A Practical Protocol | how much sodium during fasting | 10-20 | 1 |
| 4 | Keto Electrolyte Drink Without Sugar: Your Options | keto electrolyte drink without sugar | 15-25 | 1 |
| 5 | How Much Sodium on Keto? (Hint: More Than You Think) | how much sodium on keto | Low-Med | 2 |
| 6 | Best Electrolyte for Fasting: What to Look For | best electrolyte for fasting | 25-35 | 2 |
| 7 | Why Keto Flu Happens (and Exactly How to Fix It) | keto flu electrolytes | 20-30 | 2 |
| 8 | Carnivore Diet Electrolytes: What Changes? | carnivore diet electrolytes | <15 | 1 |

**IonWave advantage**: Keto and fasting audiences have the highest purchase intent for electrolyte products. IonWave's sugar-free formulation is a perfect product-content fit.

---

### Pillar 3: Athletic Performance

**Pillar page**: "Hydration for Athletes: Science-Based Electrolyte Strategies for Training and Recovery"
- Target keyword: "hydration for athletes" / "electrolytes for athletes"
- Word count: 3,000-4,000 words
- Format: Protocol guide with sport-specific recommendations
- Target audience: Athletes, fitness enthusiasts, gym-goers

**Cluster articles** (6-8 pieces):

| # | Title Pattern | Target Keyword | KD | Phase |
|---|--------------|---------------|-----|-------|
| 1 | Pre-Workout Hydration: How to Start Training Hydrated | pre workout hydration | 15-25 | 2 |
| 2 | Electrolytes After a Workout: Recovery Protocol | post workout electrolytes | 15-25 | 2 |
| 3 | Electrolytes for Running: What Endurance Athletes Need | electrolytes for running | 20-30 | 2 |
| 4 | Creatine and Electrolytes: Do They Work Together? | creatine and electrolytes | <15 | 1 |
| 5 | Sweat Rate and Electrolyte Loss: How to Calculate Yours | sweat electrolyte loss | <10 | 1 |
| 6 | Electrolyte Drink vs Sports Drink: What's the Difference? | electrolyte drink vs sports drink | 15-20 | 2 |

---

### Pillar 4: Natural Health (Brand Differentiator)

**Pillar page**: "Ocean Minerals & Trace Elements: Nature's Complete Mineral Matrix"
- Target keyword: "ocean minerals benefits" / "trace minerals supplement"
- Word count: 3,000-4,000 words
- Format: Science deep-dive with cited studies
- Target audience: Natural health seekers, ingredient-conscious buyers

**Cluster articles** (5-6 pieces):

| # | Title Pattern | Target Keyword | KD | Phase |
|---|--------------|---------------|-----|-------|
| 1 | 78 Trace Minerals: Why Full-Spectrum Matters | trace mineral supplement benefits | 15-25 | 1 |
| 2 | Marine Plasma vs. Synthetic Electrolytes: The Sourcing Difference | marine plasma vs synthetic | <10 | 1 |
| 3 | Electrolytes for Women Over 40: What Changes | electrolytes for women over 40 | 10-20 | 1 |
| 4 | Magnesium Types Explained: Which Form Is Best? | magnesium types comparison | 20-30 | 2 |
| 5 | Clean Label Electrolytes: What to Look For | clean electrolyte supplement | <15 | 1 |
| 6 | How Ocean Minerals Are Harvested (Our Sourcing Process) | ocean mineral sourcing | <10 | 1 |

**IonWave advantage**: This pillar is IonWave's unique territory. Almost zero SEO competition for marine plasma terms. This is where you build unassailable topical authority.

**Triple-purpose rationale** (why invest in low-volume marine plasma content):
1. **Brand protection**: When anyone Googles "marine plasma electrolyte," IonWave MUST own page 1. This is non-negotiable brand infrastructure.
2. **Topical authority**: Marine plasma articles strengthen the Hydration Science and Natural Health pillars, which DO target higher-volume keywords. Google evaluates cluster depth.
3. **Conversion rate**: Ultra-targeted visitors (50-100/month) convert at 3-5%, far above the 1-2% blended average. Low volume, high value per visit.

Total investment: 5-6 articles at 2-3 hours each with AI assist = 10-18 hours. Minimal downside, significant strategic value.

---

### Pillar 5: Product Comparisons (Decision-Stage)

**Pillar page**: "Best Electrolyte Supplements [2026]: An Honest, Ingredient-Level Review"
- Target keyword: "best electrolytes" / "best electrolyte supplements"
- Word count: 4,000-6,000 words (comprehensive roundup)
- Format: Comparison table + individual reviews
- Target audience: Comparison shoppers, high purchase intent

**Cluster articles** (4-5 pieces):

| # | Title Pattern | Target Keyword | KD | Phase |
|---|--------------|---------------|-----|-------|
| 1 | LMNT Alternative: What to Switch To (and Why) | LMNT alternative | Low | **1 — HIGH PRIORITY** |
| 2 | IonWave vs. LMNT: Honest Comparison | IonWave vs LMNT | <10 | 1 |
| 3 | Drip Drop vs. IonWave: Which Electrolyte Is Worth It? | drip drop alternative | Low | 1-2 |
| 4 | Sugar Free Electrolyte Drink: Best Options Compared | sugar free electrolyte drink | 25-35 | 2 |
| 5 | Electrolyte Supplement Buying Guide: What Actually Matters | electrolyte buying guide | <15 | 1 |

**"LMNT alternative" is the #1 priority article to publish.** 2,900 estimated volume at low KD with commercial intent. Create this in Week 1-2 of content publishing.

---

## 2. Blog Post Templates

### Template 1: How-to Guide
- **Title format**: "How to [Achieve X]: A [Audience] Guide"
- **Structure**: Introduction (hook + promise) → Step-by-step instructions → Tips/common mistakes → FAQ → CTA
- **Word count**: 1,500-2,500 words
- **Schema**: HowTo schema for rich snippet eligibility
- **Example**: "How to Prevent Keto Flu: A Step-by-Step Electrolyte Protocol"

### Template 2: Listicle
- **Title format**: "[Number] [Best/Top] [Things] for [Audience/Situation]"
- **Structure**: Introduction → Numbered items with detail → Summary table → CTA
- **Word count**: 1,500-2,000 words
- **Schema**: Article schema
- **Example**: "7 Signs You Need More Electrolytes (Most People Miss #4)"

### Template 3: Comparison
- **Title format**: "[Product A] vs [Product B]: [Honest/Complete] Comparison"
- **Structure**: Quick comparison table → Detailed breakdown by category → Who each is best for → Verdict → CTA
- **Word count**: 2,000-3,000 words
- **Schema**: Article schema with product mentions
- **FTC Note**: Comparisons must be factual. Don't fabricate competitor weaknesses.
- **Example**: "LMNT vs IonWave: Which Electrolyte Is Actually Worth It?"

### Template 4: Ultimate Guide (Pillar Page)
- **Title format**: "The Complete Guide to [Topic]: Everything You Need to Know"
- **Structure**: Table of contents → Section-by-section deep dive → Expert quotes/citations → FAQ → Related articles → CTA
- **Word count**: 3,000-5,000 words
- **Schema**: Article schema + FAQ schema for the FAQ section
- **Example**: "The Complete Guide to Electrolytes: What They Are, Why You Need Them, and How to Get Enough"

### Template 5: Problem/Solution
- **Title format**: "Why You [Have Problem] (and What to Do About It)"
- **Structure**: Empathetic problem description → Root cause explanation → Solution framework → Product integration (natural, not forced) → CTA
- **Word count**: 1,200-1,800 words
- **Schema**: Article schema
- **Example**: "Why You're Still Tired After 8 Hours of Sleep (It Might Be Your Minerals)"

---

## 3. Blog Post Standard Elements

Every blog post published on IonWave's Shopify blog must include:

### Required Elements

| Element | Implementation | Why |
|---------|---------------|-----|
| **Title tag** | <60 chars, primary keyword near front | Ranking factor + click-through |
| **Meta description** | <160 chars, include CTA ("Learn how..." / "Discover why...") | Click-through from SERPs |
| **H1** | One per page, matches/closely mirrors title tag | On-page SEO signal |
| **H2/H3 hierarchy** | Logical outline structure, keywords in H2s where natural | Crawlability + featured snippets |
| **Author byline** | Named author + credentials (via Shopify metafields) | E-E-A-T signal |
| **Expert review badge** | "Reviewed by [Name], [Credentials]" (for health/science content) | YMYL E-E-A-T requirement |
| **Publication + update date** | Visible to readers, structured data | Freshness signal |
| **Featured image** | Original or licensed, descriptive alt text with keyword | Engagement + image search |
| **Internal links** | Minimum 3 per post (to pillar, to related cluster, to product) | Link equity distribution |
| **External citations** | Minimum 3 per health article (PubMed, NIH, peer-reviewed) | YMYL trust signal |
| **FAQ section** | 3-5 related questions at bottom | FAQ schema → rich snippet eligibility |
| **CTA** | One primary CTA per post (product, email signup, or related content) | Conversion |
| **FDA disclaimer** | "These statements have not been evaluated by the FDA..." | Legal requirement for supplement content |

### On-Page SEO Checklist (Per Post)

```
□ Primary keyword in title tag (first 60 chars)
□ Primary keyword in H1
□ Primary keyword in first 100 words
□ Primary keyword in at least one H2
□ Primary keyword in meta description
□ Primary keyword in image alt text (featured image)
□ Secondary keywords naturally distributed throughout
□ URL slug contains primary keyword (short, clean)
□ 3+ internal links (to pillar page + related content + product page)
□ 3+ external citations (PubMed, NIH, or peer-reviewed journals)
□ FAQ section with FAQ schema markup
□ Author bio with credentials visible
□ Expert reviewer badge (for YMYL content)
□ Publication date visible
□ Featured image with descriptive alt text
□ FDA disclaimer present
```

---

## 4. Publishing Cadence

### Phased Approach (Calibrated for Bootstrapped Team)

| Phase | Timeframe | Blog Cadence | Total Posts | Focus |
|-------|-----------|-------------|-------------|-------|
| **Foundation (Founder Mode)** | Month 1-3 | 2 posts/month | 6-8 posts | Pillar pages + highest-priority long-tail clusters. Realistic for a solo founder spending 4-5 hrs/week on content. |
| **Foundation (With Writer)** | Month 1-3 | 1 post/week | 12 posts | Same focus. Requires freelance writer ($100-250/article) or dedicated content time block. |
| **Building** | Month 4-6 | 1-2 posts/week | 12-24 posts | Fill out cluster articles, start comparison content |
| **Scaling** | Month 7-12 | 2 posts/week | 24-48 posts | Medium-tail keywords, expand all pillars |
| **Optimizing** | Month 12+ | 2-3 posts/week + updates | Ongoing | Target competitive keywords, refresh top performers |

**Founder Mode reality check**: Caio is also running paid ads, product, logistics, email, and brand. 1 post/week assumes either a content hire or a dedicated full-day content block. If neither exists, 2 posts/month targeting the highest-value keywords is the honest starting cadence. Quality over quantity — always.

### Minimum Viable Content (MVC) at Launch *(Merged from Session A dialogue upgrade U3)*

Not all content needs to launch simultaneously. Separate "must-have at launch" from "ongoing cadence":

**Must be live on Day 1** (batch-publish before launch):
1. Homepage copy
2. Product page (marine plasma electrolyte)
3. About / Our Science page ("what is marine plasma")
4. FAQ page with schema markup
5. 3 comparison posts (IonWave vs LMNT, vs Liquid IV, vs Seaonic)
6. "Best Sugar-Free Electrolytes [2026]" roundup

**Total**: 6-8 pages. These can be prepared in a single focused week with AI assistance.

**Everything else starts Month 1+**. The weekly/biweekly cadence begins AFTER launch, not before. A solo founder should not try to build a 12-article content library before opening the store — that delays revenue for marginal SEO benefit.

### First 12 Posts (Priority Order)

This is the launch sequence — what to publish in Month 1-3:

| Week | Pillar | Title | Type | Priority Keyword |
|------|--------|-------|------|-----------------|
| 1 | Hydration | The Complete Guide to Electrolytes | Pillar page | electrolyte guide |
| 2 | Natural Health | Marine Plasma vs. Synthetic Electrolytes | Science deep-dive | marine plasma electrolyte benefits |
| 3 | Comparison | LMNT Alternative: What to Switch To | Comparison | LMNT alternative |
| 4 | Keto | Electrolytes for Fasting: What to Take and When | How-to | electrolytes for fasting headache |
| 5 | Keto | Signs of Electrolyte Deficiency During Fasting | Problem/Solution | signs electrolyte deficiency fasting |
| 6 | Hydration | Ocean Minerals for Hydration: What Science Says | Science deep-dive | ocean minerals for hydration |
| 7 | Keto | How Much Sodium During Fasting? Protocol Guide | How-to | how much sodium during fasting |
| 8 | Keto | Keto Electrolyte Drink Without Sugar: Options | Listicle | keto electrolyte drink without sugar |
| 9 | Comparison | IonWave vs LMNT: Honest Comparison | Comparison | IonWave vs LMNT |
| 10 | Natural Health | 78 Trace Minerals: Why Full-Spectrum Matters | Science deep-dive | trace minerals supplement benefits |
| 11 | Hydration | Signs of Electrolyte Imbalance (and What to Do) | Problem/Solution | signs electrolyte imbalance |
| 12 | Athletic | Sweat Rate and Electrolyte Loss: Calculate Yours | How-to | sweat electrolyte loss |

**Rationale**: Lead with the pillar page (Week 1) to establish topical foundation and trust signal. Marine plasma content second (uncontested territory, fast ranking, establishes authority). LMNT Alternative in Week 3 (highest-value comparison keyword, but needs 2+ existing articles for Google to trust a comparison from a new domain). Keto content fills Weeks 4-8 (highest purchase intent). Athletic and general health content fills later.

**Founder Mode sequence** (2 posts/month): If publishing biweekly, prioritize Weeks 1, 3, 4, 6, 8, 10 from the above table — these are the highest-value pieces.

---

## 5. Content Freshness & Updates

### Why Content Updates Matter

Google rewards fresh, accurate content. An updated guide that's 18 months old outranks a brand-new thin article. Build an update cycle:

### Update Schedule

| Frequency | Action | Which Posts |
|-----------|--------|-------------|
| **Quarterly** | Review and update statistics, check broken links | All published posts |
| **Biannually** | Refresh comparison content (prices, features change) | Comparison and "Best of" posts |
| **Annually** | Major update — rewrite sections, add new research | Pillar pages and top 10 traffic drivers |
| **As needed** | Add new sections based on "People Also Ask" data from GSC | Any post showing impression growth |

### Update Signals to Google

When updating a post:
1. Change the visible "Last updated" date
2. Update structured data's `dateModified`
3. Add genuinely new content (don't just change a date)
4. Submit updated URL in Google Search Console for recrawl
5. Reshare on social channels as "Updated guide"

---

## 6. Content Quality Standards

### Minimum Quality Bar

Before publishing any article, it must pass this checklist:

- [ ] **Would I send this to a friend asking about this topic?** (If not, it's not good enough)
- [ ] **Does it answer the search query better than the current #1 result?** (If not, improve or choose different keyword)
- [ ] **Does it contain at least one thing you can't get from any other article?** (Original insight, data, experience, or perspective)
- [ ] **Are all health claims supported by cited research?** (YMYL requirement)
- [ ] **Is the product mention natural, not forced?** (If it reads like an ad, rewrite)
- [ ] **Has a human expert reviewed health/science claims?** (For YMYL content)

### Quality Over Quantity

Danilo's content strategy correctly notes: "One excellent post beats three mediocre ones." This is especially true for YMYL content where Google evaluates quality with higher scrutiny.

**The math**: One well-researched, expert-reviewed 2,500-word guide that ranks #3 for a 1,000-volume keyword drives ~200 visits/month forever. Ten thin 800-word posts that rank nowhere drive zero. Invest in quality.


---

### 📄 seo_link_building.md

# SEO Link Building & Native Ads — M16: Content & SEO

**TUP**: M16
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift), HYP-001 (CAC)
**Danilo Source**: ops_model_v10_dump/414_seo_link_building.json (20 rows), 415_native_ads_playbook.json (38 rows)

---

## Purpose

Define IonWave's approach to earning backlinks (the hardest part of SEO) and using native advertising as a content-driven paid acquisition channel. These are combined because both involve getting IonWave content placed on external sites — one earned, one paid.

**Why link building matters**: Google's ranking algorithm weighs backlinks heavily. A site with 50 quality referring domains will consistently outrank one with 5, even if the content quality is equal. For a new domain, link building is what accelerates you out of the "Google sandbox" phase.

---

## 1. Link Building Tactics (Priority Order)

### Tactic 1: Expert Quote Platforms (Priority: Highest for Bootstrapped)

**What changed**: Danilo's playbook lists HARO (Help A Reporter Out). HARO was acquired by Cision and rebranded as Connectively, which shut down in March 2025. The replacements:

| Platform | How It Works | Cost | Response Time | Link Quality |
|----------|-------------|------|--------------|-------------|
| **Qwoted** | Journalists post queries, you pitch expert quotes | Free tier available | 24-48 hrs to respond | High (editorial, DA 40-80+) |
| **Featured.com** | AI matches you to journalist queries | Free tier (3 pitches/day) | Same-day responses needed | High (Forbes, Business Insider, etc.) |
| **Terkel** | Community Q&A, answers get placed in articles | Free | 48-72 hrs | Medium-High |
| **SourceBottle** | Email-based journalist requests (AU/NZ/US) | Free | Varies | Medium-High |

**IonWave approach**:
- Sign up for Qwoted and Featured.com immediately
- Set alerts for: electrolytes, hydration, supplements, keto, fasting, ocean minerals, nutrition
- Respond to 3-5 relevant queries per week
- Pitch Caio as "Founder of IonWave, marine plasma electrolyte brand" — founder credentials matter
- Expected result: 2-5 placements/month after getting established, each with a backlink

**Realistic conversion expectations**:
- Month 1-2: Pitch 5-10 queries/week → expect 1-2 placements/month (5-10% conversion rate for unknown founders)
- Month 3-4: As platform reputation builds → 2-4 placements/month
- Month 5+: With established profile → 3-5 placements/month
- **The first 5-10 pitches will likely fail.** This is normal. Persistence through Month 1 is critical — don't abandon the tactic after initial rejections.

**Why this is #1**: Lowest time investment (15-30 min per response), highest quality links (real editorial sites), and builds personal brand simultaneously.

---

### Tactic 2: Podcast Guesting (Priority: High)

**How it works**: Appear as a guest on relevant podcasts → show notes include a backlink to your site → audience discovers your brand → builds authority.

**Target podcast categories**:
- Keto/fasting (biggest audience overlap)
- Biohacking/health optimization
- Entrepreneurship/DTC brand building
- Natural health/functional nutrition
- Athletic performance/sports nutrition

**Outreach approach**:
1. Start with smaller shows (500-5K downloads/episode) — easier to book, still valuable links
2. Pitch angle: "The science behind marine plasma electrolytes" or "How we built a supplement brand without synthetic ingredients"
3. Use PodcastGuests.com, MatchMaker.fm, or direct DM on Twitter/LinkedIn
4. Target: 1-2 appearances per month starting Month 3

**Link value**: Podcast show-note links are typically dofollow, from relevant sites, with real traffic. One podcast appearance = 1 quality backlink + audience exposure + content to repurpose (clips for social).

**LMNT case study**: LMNT's podcast sponsorship strategy (sponsoring 50+ health podcasts) turbocharged their domain authority. IonWave can get similar links for free through guesting rather than sponsoring.

---

### Tactic 3: Guest Posting (Priority: High)

**How it works**: Write a valuable article for another site → include a contextual link back to IonWave → their audience + Google see it.

**Target publications** (by tier):

| Tier | DA Range | Examples | Effort | Accept Rate |
|------|----------|---------|--------|-------------|
| **A-tier** | 60+ | Healthline contributors, Men's Health, mindbodygreen | Very High | <5% |
| **B-tier** | 40-60 | Health blogs, fitness publications, nutrition sites | High | 10-20% |
| **C-tier** | 20-40 | Niche keto blogs, supplement review sites, wellness bloggers | Medium | 20-40% |

**Approach for bootstrapped brand**:
1. Start with C-tier sites (easier acceptance, still valuable for a DR 0-10 site)
2. Write genuinely valuable content (not thinly-veiled product pitches)
3. Include 1 contextual link to an IonWave blog post (not product page — editorial sites reject product links)
4. Pitch 5-10 sites per month, expect 1-3 acceptances
5. Scale up to B-tier after you have 3-5 published guest posts to reference

**Topic angles that get accepted**:
- "The Science Behind [Ingredient/Concept]" — educational, non-promotional
- "What Most People Get Wrong About [Topic]" — contrarian, attention-grabbing
- "How to [Achieve X] Without [Common Mistake]" — practical, actionable

---

### Tactic 4: Competitor Backlink Mining (Priority: High)

**How it works**: Use tools to find who links to your competitors → pitch those same sites with your content/angle.

**Process**:
1. Run free Ahrefs backlink checker on LMNT.com, DrinkLMNT.com, Redmond Re-Lyte, Nuun
2. Export referring domains
3. Categorize: blogs, resource pages, podcast show notes, directories, forums
4. Pitch the blogs and resource pages with IonWave's unique angle (marine plasma)
5. Ignore: competitor's paid sponsorships, affiliate sites (they won't switch without commission)

**Budget**: Free (Ahrefs free tier shows top 100 backlinks). Full Ahrefs ($99/mo) for comprehensive analysis when budget allows.

**When to start**: Month 3 (after you have some content to offer as a replacement/addition)

---

### Tactic 5: Resource Page Link Building (Priority: Medium-High)

**How it works**: Find pages that list "best electrolytes" or "keto supplement recommendations" → reach out to get IonWave added.

**Search queries to find targets**:
- `"best electrolytes" + "resources"` or `"recommended products"`
- `"keto supplements" + "our picks"` or `"what we use"`
- `"electrolyte recommendations" + blog`
- `"hydration guide" + "products mentioned"`

**Outreach template concept** (personalize every email):
- Subject: Specific reference to their article
- Body: Note what you liked → mention your product's unique angle (marine plasma, 78 minerals) → suggest adding IonWave as an option
- Include: Link to your best comparison or science article (not just product page)

---

### Tactic 6: Original Research & Data Content (Priority: Medium — High Impact)

**How it works**: Publish original data, surveys, or research that others cite → passive backlinks accumulate over time.

**Content ideas for IonWave**:
- "Electrolyte Content Comparison: We Tested 20 Popular Brands" (lab test actual mineral content)
- "Survey: How Americans Hydrate During Exercise" (commission a simple survey)
- "Marine Plasma Mineral Profile: Full Lab Analysis" (publish your own product's lab results)
- "Electrolyte Calculator: How Much Do You Need?" (interactive tool)

**Why this works**: Bloggers and journalists cite data. If IonWave publishes the most comprehensive electrolyte comparison data, every "best electrolytes" article will reference it.

**Effort**: Very High (original research costs $500-2,000+). Save for Month 6-12 when budget allows. But ONE great data piece can generate 20-50+ backlinks passively.

---

### Tactic 7: Influencer Mentions & Digital PR (Priority: Medium)

**How it works**: Get mentioned (with link) in influencer content, review posts, and online publications.

**Bootstrapped approach**:
- Send product to micro-influencers who write blogs (not just social) — blog posts = backlinks
- Target: health/keto/fitness bloggers who review products (not just Instagram influencers)
- Coordinate with M22 (UGC Creator Program) — some creators have blogs
- Look for "what's in my supplement stack" style content

**Cross-reference**: M22 Creator Program — ask creators who have blogs/websites to include a link to IonWave in their review posts. This doubles the value of creator partnerships.

---

### Tactic 8: Broken Link Building (Priority: Low — Tedious but Works)

**How it works**: Find broken links on relevant sites → offer your content as a replacement.

**Process**:
1. Use Ahrefs broken link checker on health/fitness/keto sites
2. Find broken links that pointed to electrolyte or supplement content
3. Create (or identify existing) IonWave content that covers the same topic
4. Email the site owner: "I noticed a broken link on [page]. I have a resource that covers [topic] — happy to share it as a replacement."

**Success rate**: 5-10% of outreach emails result in a link. It's tedious but reliable.

**When**: Month 6+ when you have enough content to offer as replacements.

---

## 2. Link Quality Standards

### What to Pursue

| Criteria | Target |
|----------|--------|
| **Domain Authority** | >30 (ideally >50) |
| **Relevance** | Health, fitness, nutrition, wellness, or keto/fasting niche |
| **Traffic** | Real site with real organic traffic (check with SimilarWeb free) |
| **Link type** | Dofollow (nofollow has less direct SEO value, but still valuable for brand) |
| **Link placement** | In content body (not footer, sidebar, or author bio only) |
| **Anchor text** | Natural variation — branded ("IonWave"), generic ("this guide"), or topical ("marine plasma electrolytes") |

### What to Avoid

| Red Flag | Why |
|----------|-----|
| **PBNs (Private Blog Networks)** | Google penalty risk. Sites exist only for links, no real audience |
| **Link farms / directories** | Spam signals. Google ignores or penalizes |
| **Paid links** (without nofollow/sponsored tag) | Google link spam policy violation |
| **Irrelevant sites** | A link from a plumbing blog to an electrolyte brand looks unnatural |
| **Links from sites with no organic traffic** | If Google doesn't trust the linking site, the link has no value |
| **Exact-match anchor text manipulation** | Over-optimizing anchor text triggers penalties |

---

## 3. Link Building Targets & Tracking

### Monthly Targets (By Phase)

| Phase | Timeframe | Target New Referring Domains | Cumulative Total | Tactics Focus |
|-------|-----------|------------------------------|------------------|---------------|
| **Foundation** | Month 1-3 | 3-5/month | 10-15 | Expert quote platforms, initial podcast outreach |
| **Building** | Month 4-6 | 5-8/month | 30-50 | + Guest posting, competitor mining, resource pages |
| **Scaling** | Month 7-12 | 8-15/month | 80-150 | + Original research, digital PR, broken links |
| **Maintaining** | Month 12+ | 10-20/month | 200+ | All tactics + passive link acquisition from quality content |

### Link Acquisition Tracker

Track every outreach effort and acquired link:

| Date | Target Site | DA | Tactic | Status | Link URL | Anchor Text |
|------|-----------|-----|--------|--------|----------|-------------|
| (template) | example.com | 45 | Guest post | Pitched / Accepted / Published / Rejected | — | — |

---

## 4. Native Advertising Playbook (Phase 3 — Optional Channel)

**This is an optional channel.** Many successful DTC supplement brands under $50K/month revenue never use native advertising. The core M16 strategy (blog + SEO + email + social) works fully without it. Include native ads only if all prerequisites below are met.

### Prerequisites Before Starting Native Ads

Native advertising (Taboola, Outbrain, etc.) is a legitimate content distribution channel but **NOT for launch**. Only activate when:

- [ ] Meta Ads are proven and profitable (ROAS >2x for 60+ days)
- [ ] Monthly revenue exceeds $30K (native requires $1-2K+/month minimum spend)
- [ ] Email capture is in place and working (native traffic should enter your funnel, not just bounce)
- [ ] You have at least 3 proven advertorial pages (test on Meta first)
- [ ] You understand your unit economics well enough to absorb a learning phase

**Why the gate?** Native ad platforms have high minimum spends, require advertorial-style content (different from social ads), and have a steep learning curve. Starting before you have revenue, a proven funnel, and working email capture = burning money.

### How Native Is Different from Social Ads

| Dimension | Social Ads (Meta) | Native Ads (Taboola/Outbrain) |
|-----------|-------------------|------------------------------|
| **User context** | Interrupting social feed | Blending with editorial content |
| **Creative format** | Video, image, carousel | Thumbnail + headline (looks like article) |
| **Landing page** | Product page or landing page | Advertorial page (long-form content) |
| **User intent** | Low (browsing social) | Medium (consuming content, open to discovery) |
| **Conversion path** | Ad → Product page → Purchase | Ad → Advertorial → Product page → Purchase |
| **Best for** | Direct response, retargeting | Storytelling, education-led conversion |

### Native Ad Funnel Structure

```
Step 1: NATIVE AD (Thumbnail + Headline)
├── Curiosity-driven, not product-focused
├── Looks like an article recommendation
└── Click goes to advertorial page (NOT product page)

Step 2: ADVERTORIAL PAGE (800-1,500 words)
├── Looks like an article, not an ad
├── Story-driven: Problem → Discovery → Solution → Social proof → CTA
├── Multiple CTAs throughout (not just at the end)
├── Must include "Advertisement" or "Sponsored" disclosure (FTC requirement)
└── Click goes to product page or landing page

Step 3: PRODUCT/LANDING PAGE
├── Standard product page (they're pre-sold from advertorial)
├── Or dedicated landing page with offer
└── Email capture as secondary conversion goal
```

### Advertorial Structure Template

1. **Hook headline**: Problem or curiosity-based (not product-focused)
2. **Opening paragraph**: Relatable problem that the reader identifies with
3. **Discovery story**: How the solution was found (founder story, research, etc.)
4. **The science**: Why it works (simplified, with authority signals)
5. **Social proof**: Customer testimonials, expert quotes, usage stats
6. **CTA #1**: Soft ask ("Learn more about IonWave")
7. **Additional benefits**: Secondary value propositions
8. **CTA #2**: Stronger ask ("Try IonWave today")
9. **FAQ / objection handling**: Address common concerns
10. **CTA #3**: Urgency or incentive ("Use code OCEAN for 15% off")

### Headline Formula Categories

**Curiosity + Benefit**:
- "[Professional type] explains why [common practice] is wrong"
- "The [ingredient/mineral] most people have never heard of"
- "Why [unexpected group] are switching to [category]"

**Problem + Intrigue**:
- "Still [experiencing symptom] despite [common solution]? Read this"
- "The real reason you [have problem] (hint: it's not [common assumption])"

**Social proof + News**:
- "The [category] brand that [achievement/stat]"
- "Why [credible group] are switching from [competitor] to this"

### Native Ad Platforms

| Platform | Min Spend | Typical CPCs | Best For | Quality |
|----------|-----------|-------------|----------|---------|
| **Taboola** | ~$2K/mo | $0.30-0.80 | Scale, mainstream publisher sites | Large reach, mixed quality |
| **Outbrain** | ~$2K/mo | $0.40-1.00 | Premium publishers | Higher quality traffic, smaller reach |
| **RevContent** | ~$1K/mo | $0.20-0.50 | Testing, lower budget | More aggressive placements |
| **MGID** | ~$500/mo | $0.15-0.40 | International, cheap testing | Lower traffic quality |

**Recommendation for IonWave**: Start with RevContent ($1K/mo) or Taboola when ready. Test 3 different advertorials with 3 different headlines each. Kill losers after 500 clicks. Scale winners.

### Native Ad Metrics

| Metric | Target | Red Flag |
|--------|--------|----------|
| CTR (ad to advertorial) | >0.3% | <0.15% (headline isn't working) |
| Read rate (advertorial) | >40% scroll to CTA | <20% (opening isn't engaging) |
| CVR (advertorial to product page) | >5% | <2% (advertorial isn't pre-selling) |
| CVR (product page to purchase) | >2% | <1% (product page friction) |
| Blended CPA from native | <$50 | >$70 (unprofitable at IonWave's AOV) |
| ROAS | >2x | <1.5x (not sustainable) |

---

## 5. Combined Monthly Action Plan

### Month 1-3 (Foundation)

| Week | Link Building | Content Distribution | Time |
|------|--------------|---------------------|------|
| Every week | Respond to 3-5 expert quote platform queries | Share blog posts via email newsletter | 2-3 hrs |
| Every week | — | Publish 1 blog post | (counted in content_strategy.md) |
| Month 2 | Start podcast outreach (pitch 5 shows) | — | 2 hrs |
| Month 3 | Run free Ahrefs backlink check on top 3 competitors | — | 1 hr |

### Month 4-6 (Building)

| Week | Link Building | Native Ads | Time |
|------|--------------|-----------|------|
| Every week | Expert quotes + podcast follow-ups | — | 2-3 hrs |
| Biweekly | Pitch 3-5 guest post opportunities | — | 2 hrs |
| Month 4 | Start resource page outreach | — | 1 hr/week |
| Month 6 | Evaluate if native ads prerequisites are met | If yes: write first advertorial, test on Meta before committing to native platform | 4-6 hrs |

### Month 7-12 (Scaling)

| Activity | Cadence | Time |
|----------|---------|------|
| Expert quote platforms | Daily (10 min/day) | 1 hr/week |
| Podcast appearances | 1-2 per month | 2-3 hrs/month |
| Guest posts published | 1-2 per month | 3-5 hrs/month |
| Competitor backlink mining | Monthly audit | 2 hrs/month |
| Resource page outreach | Ongoing, 3-5 pitches/week | 1 hr/week |
| Native ads (if activated) | Ongoing optimization | 2-3 hrs/week |
| Original research content | 1 piece per quarter | 8-12 hrs/quarter |


---

### 📄 seo_strategy.md

# SEO Strategy — M16: Content & SEO

**TUP**: M16
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift), HYP-001 (CAC — organic reduces blended CAC)
**Danilo Source**: ops_model_v10_dump/410_seo_strategy_overview.json (27 rows)

---

## Purpose

Define IonWave's SEO strategy with realistic expectations, proper E-E-A-T infrastructure, and a phased approach calibrated for a bootstrapped DTC supplement brand. SEO is the long game — it compounds over 12-24 months but produces little in the first 6.

**The honest framing**: SEO will NOT be IonWave's primary revenue driver for the first 12 months. Meta Ads will drive acquisition. But every month you delay starting SEO, you push out the compounding payoff. Start building from Month 1, even at minimal investment.

---

## 1. Why SEO Matters for IonWave (Specifically)

Danilo's overview listed generic SEO benefits. Here's the IonWave-specific case:

| Benefit | IonWave Context |
|---------|----------------|
| **Reduces blended CAC** | At $35-45 CAC from paid, even 10-15% organic traffic reduces blended CAC by $3-7. At scale, this is $3K-7K/month in saved ad spend. |
| **Captures high-intent search traffic** | People searching "electrolytes for fasting" or "best keto electrolytes" are ready to buy. Organic captures intent that paid can't. |
| **Builds brand authority** | E-E-A-T signals from quality content make your site more trustworthy to both Google AND customers. |
| **Creates competitive moat** | SEO authority compounds. Established content + backlinks are hard for competitors to replicate quickly. |
| **Diversifies from Meta dependency** | Meta CPMs rose 27% YoY. Organic traffic is insurance against paid channel volatility. |
| **Marine plasma = uncontested territory** | There is virtually NO SEO competition for "marine plasma electrolyte" terms. This is your keyword wedge. |

---

## 2. SEO Timeline Reality (New Domain, Supplement Space)

Danilo's timeline was directionally correct but lacked specifics. Here's the calibrated version:

| Timeframe | What Happens | Realistic Organic Traffic | Investment Focus |
|-----------|-------------|--------------------------|-----------------|
| **Month 1-3** | Google indexes site. Rankings: nowhere or page 5+. Brand terms only. | **50-200 visits/month** | Technical SEO setup, first blog posts, E-E-A-T infrastructure |
| **Month 4-6** | Long-tail articles appear on page 2-3. Site starts earning topical signals. | **200-800 visits/month** | Consistent publishing (1/week), initial link building |
| **Month 7-12** | Long-tail keywords hit page 1. Medium-tail on page 2. Content velocity compounds. | **800-3,000 visits/month** | Scale to 2/week, medium-tail keywords, podcast guesting |
| **Month 12-18** | Medium keywords reach page 1. Organic becomes meaningful traffic source. | **3,000-8,000 visits/month** | Target competitive keywords, digital PR |
| **Month 18-24** | Organic is #2 or #3 traffic source. Some competitive keywords on page 1. | **8,000-20,000 visits/month** | Content authority maintenance, topical clusters |

**The Google sandbox**: Google never confirmed it, but new domains consistently take 6-12 months to gain traction. This is not a penalty — it reflects the time needed for Google to build trust through crawl history, content quality evaluation, and backlink accumulation.

**Key acceleration levers**:
- PR mentions generating backlinks (LMNT's podcast sponsorships turbo-charged their SEO)
- Original research/data content that gets cited by other sites
- Founder podcast appearances generating show-note backlinks

---

## 3. E-E-A-T Infrastructure (Critical for YMYL)

### What is YMYL?

"Your Money or Your Life" — Google's category for content that could impact health, financial stability, or safety. Supplement websites are squarely YMYL. Content is held to a **higher standard** than non-YMYL sites.

### E-E-A-T Breakdown

| Signal | What It Means | IonWave Implementation |
|--------|-------------|----------------------|
| **Experience** | Author has first-hand experience with the topic | Founder-authored content, "In our testing...", real customer stories, product journey documentation |
| **Expertise** | Author has relevant credentials or deep knowledge | Named authors with bios, expert reviewer badge ("Reviewed by [Name], RD") |
| **Authoritativeness** | Site is recognized as an authority | Backlinks from health publications, citations from other sites, consistent topical content |
| **Trustworthiness** | Site is transparent and accurate | Clear About page, editorial policy, source citations, supplement disclaimers |

### Required E-E-A-T Pages (Build Before Publishing Content)

| Page | Priority | What It Contains |
|------|----------|-----------------|
| **About Us** | P0 | Founder story, team credentials, company mission, why marine plasma, photos |
| **Science / Research** | P0 | Marine plasma sourcing rationale, cited studies (PubMed links), formulation transparency |
| **Editorial Policy** | P1 | How content is created, fact-checking process, expert review disclosure |
| **Privacy Policy** | P0 | Required by law + Google trust signal |
| **Terms of Service** | P0 | Legal requirement |
| **Shipping & Returns** | P0 | Ecommerce trust signal |
| **Contact** | P1 | Real phone, email, physical address — trust signals |

### Author Bio Implementation on Shopify

Use Shopify metafields (free, built-in since 2022):

1. Create custom metafields for blog articles:
   - `author_name` (text)
   - `author_credentials` (text, e.g., "Sports Nutritionist, CSCS")
   - `author_bio` (rich text, 2-3 sentences)
   - `reviewer_name` (text)
   - `reviewer_credentials` (text)
   - `last_updated` (date)
   - `sources_count` (number)

2. Surface these in your article template via Liquid code
3. Add "Reviewed by [Name], [Credentials]" badge to article header

**Cost of expert review**: $50-150 per article from a freelance registered dietitian or sports nutritionist. Batch 3-5 articles for efficiency. This is one of the highest-ROI investments in SEO for a supplement brand.

### Supplement-Specific Brands That Rank Well (and Why)

| Brand | Organic Traffic | Key E-E-A-T Signal |
|-------|----------------|---------------------|
| **Examine.com** | 800K+ monthly | Researcher authors, dozens of citations per article, systematic evidence grading |
| **Legion Athletics** | ~500K monthly | Named RD authors, 20-50 citations per article, transparent formulation |
| **LMNT** | Growing rapidly | Science page with cited studies, advisor board with physicians, podcast-generated backlinks |
| **AG1 (Athletic Greens)** | Strong DA | Massive PR-generated backlinks, physician advisor board |

**IonWave's opportunity**: Marine plasma is a genuinely novel ingredient positioning. There is almost zero SEO competition for "marine plasma" terms. Build topical authority in this uncontested space first, then ladder into competitive terms.

---

## 4. SEO Strategy Pillars

### Pillar 1: Technical SEO (Month 1 — One-Time Setup)

See `technical_seo_checklist.md` for complete checklist. Key items:
- Site speed (Core Web Vitals target: 70+ mobile PageSpeed)
- Structured data (Product, Article, FAQ, Organization schema)
- Sitemap submitted to GSC
- Clean URL structure
- Shopify-specific issues addressed (duplicate /collections/ URLs)

### Pillar 2: On-Page SEO (Ongoing)

Every page and blog post must have:
- Unique title tag (<60 chars, include primary keyword)
- Unique meta description (<160 chars, include CTA)
- One H1 per page
- H2-H3 heading hierarchy
- Descriptive image alt text
- Internal links to/from related content (minimum 3 per blog post)
- Schema markup appropriate to content type

### Pillar 3: Content Strategy (Month 2+)

See `seo_content_strategy.md` for full pillar/cluster model. Summary:
- 5 content pillars: Hydration Science, Keto & Low-Carb, Athletic Performance, Natural Health, Product Comparisons
- Pillar pages (3,000-5,000 words) + supporting articles (1,500-2,500 words)
- Publishing cadence: 1/week (Month 1-3) → 2/week (Month 4-6) → 2-3/week (Month 7+)

### Pillar 4: Link Building (Month 3+)

See `seo_link_building.md` for full strategy. Summary:
- Expert quote platforms (Qwoted, Featured.com)
- Podcast guesting
- Original research/data content
- Guest posting on health publications
- Digital PR

### Pillar 5: Local SEO — NOT APPLICABLE

Danilo listed Local SEO as a pillar. **Skip this for IonWave.** Local SEO (Google Business Profile, local citations) is for businesses with a physical location serving local customers. IonWave is a national DTC brand. No Google Business Profile needed.

---

## 5. SEO Budget Allocation

### By Marketing Budget Tier

| Total Marketing Budget | SEO Allocation | What It Buys |
|----------------------|----------------|-------------|
| **$1K/month** | $200 (20%) = mostly your time | Free tools + $10-20 SEO app + founder writes 1 blog/week |
| **$2-3K/month** | $600-900 (30%) | Above + 2-3 expert reviews/month ($150-450) + freelance content assist |
| **$4-5K/month** | $1.6-2K (40%) | Above + freelance writer ($200-400/month) + basic link building outreach + Ahrefs Lite ($99/mo) |
| **$10K+/month** | $2-3K (20-30%) | Full content team, digital PR, comprehensive link building |

**The 60/40 principle for bootstrapped brands**: Spend 60-80% on paid (immediate revenue) and 20-40% on organic (compounding returns). Shift allocation toward organic as it proves out over 12-18 months.

### SEO ROI Projection

Conservative estimate for IonWave, assuming consistent effort:

| Month | Organic Sessions | CVR | Revenue from Organic | Cumulative SEO Investment |
|-------|-----------------|-----|---------------------|--------------------------|
| 6 | 500 | 2% | $590 | $1,800 |
| 12 | 2,500 | 2.5% | $3,688 | $4,200 |
| 18 | 6,000 | 3% | $10,620 | $7,200 |
| 24 | 15,000 | 3% | $26,550 | $10,800 |

Assumptions: $59 AOV, gradual CVR improvement as content quality and targeting improve. By Month 18-24, organic revenue should exceed cumulative SEO investment — after that, it's compounding returns.

**Conservative scenario** (1.5% blended CVR — more realistic for mixed informational + commercial traffic):

| Month | Organic Sessions | CVR | Revenue from Organic | Cumulative SEO Investment |
|-------|-----------------|-----|---------------------|--------------------------|
| 6 | 500 | 1.5% | $443 | $1,800 |
| 12 | 2,500 | 1.5% | $2,213 | $4,200 |
| 18 | 6,000 | 1.5% | $5,310 | $7,200 |
| 24 | 15,000 | 1.5% | $13,275 | $10,800 |

Even in the conservative scenario, organic revenue exceeds cumulative investment by Month 24. The base case assumes CVR improves as the keyword mix shifts from informational to commercial — verify this assumption against GA4 data after Month 6.

**ROI breakeven calibration** *(Merged from Session A dialogue upgrade U4)*: Content ROI breakeven for a new brand with no existing audience is realistically 10-14 months, not 8-10. The "equivalent paid traffic cost" (organic sessions × avg CPC) is a useful directional metric for justifying continued investment, but it's not real revenue — you can't deposit saved CPC. Real ROI = organic revenue (first-click attributed) ÷ content production cost.

**Organic traffic % target calibration** *(Merged from Session A dialogue upgrade U6)*: Month 12 organic traffic as % of total — **base case: 10-15%**, **aggressive case: 15-25%**. Most new DTC brands achieve 8-12% organic at Month 12. Reaching 15%+ requires consistently excellent execution across content, link building, and technical SEO. Even at 10%, the program is valuable: that's $0 marginal CAC traffic.

---

## 6. Success Metrics

### Monthly Tracking Dashboard

| Metric | Tool | Month 3 Target | Month 6 Target | Month 12 Target |
|--------|------|----------------|----------------|-----------------|
| Organic sessions | GA4 | 100+ | 500+ | 2,500+ |
| Indexed pages | GSC | 15+ | 30+ | 60+ |
| Keywords on page 1 | GSC | 2-5 (branded + ultra-long-tail) | 10-20 | 30-50 |
| Keywords on page 1-2 | GSC | 10-15 | 30-50 | 80-120 |
| Domain Rating | Ahrefs (free check) | 5-10 | 15-25 | 25-35 |
| Referring domains | GSC backlinks report | 10-20 | 30-50 | 80-150 |
| Blog posts published | Internal | 12 (1/week) | 24 | 52+ |
| Email subscribers from organic | GA4 events | 50-100 | 200-500 | 1,000-2,000 |
| Organic revenue | GA4 | $0-100 | $200-600 | $2,000-5,000 |

### Red Flags to Watch

| Signal | What It Means | Action |
|--------|-------------|--------|
| Organic traffic declining after initial growth | Possible algorithm update impact, thin content penalties | Audit content quality, check GSC for manual actions |
| Pages indexed < pages published | Crawl issues, noindex tags, thin content | Check GSC Coverage report, fix technical issues |
| High impressions, low CTR (<2%) | Title tags and meta descriptions not compelling | Rewrite meta data for top 10 impression pages |
| Domain Rating stagnant after 6 months | Link building isn't working | Increase outreach effort, try different tactics |
| No keywords on page 1 after 9 months | Content not matching search intent, or too competitive | Refocus on longer-tail keywords, improve content depth |

---

## 7. Intelligence Gaps

| Gap | Impact | How to Close | Priority |
|-----|--------|-------------|----------|
| No real keyword data (only Danilo estimates) | Keyword strategy may be targeting wrong terms | Subscribe to Ubersuggest ($29/mo) or use free Google Keyword Planner after launch | P1 — Month 1 |
| No competitor backlink analysis | Can't identify link building opportunities | Ahrefs free backlink checker for top 3 competitors. Full Ahrefs at $99/mo when budget allows | P2 — Month 3 |
| Unverified Shopify Core Web Vitals | May have speed issues affecting rankings | Run PageSpeed Insights audit immediately after theme selection | P0 — Pre-launch |
| No actual search volume for "marine plasma" terms | May be overestimating the keyword opportunity | Google Search Console will show real impression data after 1-2 months | P1 — Month 2 |


---

### 📄 technical_seo_checklist.md

# Technical SEO Checklist — M16: Content & SEO

**TUP**: M16
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-006 (Organic Growth Lift), HYP-001 (CAC — organic reduces blended CAC)
**Danilo Source**: ops_model_v10_dump/412_technical_seo_checklist.json (34 rows)

---

## Purpose

Pre-launch and ongoing technical SEO checklist for IonWave's Shopify store. Technical SEO is the foundation — if Google can't crawl and index your site properly, no amount of content will help.

**Priority**: Complete before any content publishing. Most items are one-time setup.

---

## 1. Shopify Built-In SEO (What You Get for Free)

Shopify handles several technical SEO fundamentals automatically:

| Feature | Status | Notes |
|---------|--------|-------|
| **SSL/HTTPS** | Included | All Shopify stores get free SSL |
| **CDN** | Included | Cloudflare CDN for all stores |
| **XML Sitemap** | Auto-generated | At /sitemap.xml — auto-updates |
| **Canonical tags** | Auto-generated | Handles product-in-collection duplicates |
| **Robots.txt** | Auto-generated | Customizable via Shopify admin since 2023 |
| **Mobile responsive** | Theme-dependent | Dawn and most 2.0 themes are responsive |
| **Structured data (basic)** | Theme-dependent | Most themes include basic Product schema |

**What Shopify does NOT do well** (and you must handle manually or via apps):
- Blog categorization (tags only, no categories)
- Redirect management at scale
- Custom structured data / rich snippets
- Image alt text (must add manually)
- Meta description optimization (defaults to page content excerpt)
- Internal linking strategy
- Core Web Vitals optimization beyond basics

---

## 2. Pre-Launch Technical Checklist

### 2.1 Site Speed & Core Web Vitals

Core Web Vitals are a confirmed ranking factor. Shopify stores typically score 50-70 on PageSpeed Insights (mobile). Target: 70+ mobile.

| # | Task | Tool | Priority | Status |
|---|------|------|----------|--------|
| 1 | Run PageSpeed Insights audit | [Google PageSpeed Insights](https://pagespeed.web.dev/) | P0 | ☐ |
| 2 | Achieve LCP (Largest Contentful Paint) < 2.5s | Theme optimization | P0 | ☐ |
| 3 | Achieve CLS (Cumulative Layout Shift) < 0.1 | Theme optimization | P0 | ☐ |
| 4 | Achieve INP (Interaction to Next Paint) < 200ms | Minimize JS | P1 | ☐ |
| 5 | Compress all images (WebP format where possible) | Shopify auto-compresses, but upload optimized originals | P0 | ☐ |
| 6 | Enable lazy loading for below-fold images | Most Shopify 2.0 themes have this built-in | P0 | ☐ |
| 7 | Minimize third-party scripts (tracking pixels, chat widgets) | Audit all apps — each adds JS | P1 | ☐ |
| 8 | Use system fonts or limit custom font files | Reduce font load time | P2 | ☐ |

**Shopify-specific speed tips**:
- Every Shopify app you install adds JavaScript. Audit apps quarterly — uninstall unused ones and check that uninstalled apps actually removed their code.
- Hero images are the biggest LCP offender. Use compressed WebP, specify width/height attributes.
- Shopify's Dawn theme is optimized for speed. If using a paid theme, check its PageSpeed score before purchase.
- Avoid excessive Liquid snippets in the theme. Each one adds render time.

### 2.2 Crawlability & Indexation

| # | Task | Tool | Priority | Status |
|---|------|------|----------|--------|
| 1 | Submit sitemap to Google Search Console | GSC → Sitemaps → Add /sitemap.xml | P0 | ☐ |
| 2 | Submit sitemap to Bing Webmaster Tools | Bing Webmaster Tools | P1 | ☐ |
| 3 | Verify robots.txt isn't blocking important pages | Visit /robots.txt directly | P0 | ☐ |
| 4 | Check for noindex tags on important pages | GSC → Coverage or Screaming Frog | P0 | ☐ |
| 5 | Ensure clean URL structure | /products/ionwave-electrolytes not /products?id=123 | P0 | ☐ |
| 6 | Fix Shopify duplicate URL issue | /collections/all/products/X duplicates /products/X — canonical tags handle this, but avoid internal linking to /collections/ URLs | P1 | ☐ |
| 7 | Set up 301 redirects for any changed URLs | Shopify Admin → Navigation → URL Redirects | P1 | ☐ |
| 8 | Eliminate orphan pages (pages with no internal links) | Manual audit or Screaming Frog | P1 | ☐ |

**Known Shopify SEO issues**:
- **Duplicate content from collections**: Shopify creates URLs like `/collections/all/products/product-name` AND `/products/product-name`. Canonical tags handle this for Google, but always use the `/products/` URL in internal links and sitemaps.
- **Paginated collection pages**: `/collections/all?page=2` etc. can create thin content pages. Shopify handles pagination with rel=next/prev.
- **Tag pages**: `/collections/tag-name` creates additional URLs. These can be useful for SEO (e.g., `/collections/keto-electrolytes`) or harmful (thin content). Be intentional about which tags you create.

### 2.3 On-Page Fundamentals

| # | Task | Tool | Priority | Status |
|---|------|------|----------|--------|
| 1 | Write unique title tags for all pages | < 60 characters, include primary keyword | P0 | ☐ |
| 2 | Write unique meta descriptions | < 160 characters, include CTA | P0 | ☐ |
| 3 | One H1 tag per page (product name or article title) | Theme should handle this automatically | P0 | ☐ |
| 4 | Use H2-H3 heading hierarchy in content | Structure for scanability and SEO | P0 | ☐ |
| 5 | Add descriptive alt text to ALL images | Keyword-relevant, not keyword-stuffed | P0 | ☐ |
| 6 | Implement internal linking structure | Blog ↔ product pages, related products | P1 | ☐ |
| 7 | Optimize product descriptions for target keywords | Natural language, not keyword stuffing | P1 | ☐ |

**Title tag formula for IonWave**:
- Homepage: `IonWave — Marine Plasma Electrolytes | 78 Ocean Minerals`
- Product page: `IonWave Electrolyte Powder — 78 Ocean Minerals | [Benefit]`
- Blog post: `[Primary Keyword] — [Benefit or Hook] | IonWave`
- Comparison: `IonWave vs [Competitor] — [Key Difference] | Honest Comparison`

### 2.4 Structured Data / Schema Markup

Structured data helps Google display rich snippets (star ratings, prices, FAQ dropdowns).

| Schema Type | Where | Priority | Status |
|-------------|-------|----------|--------|
| **Product** | Product pages | P0 | ☐ — Most Shopify themes include basic Product schema. Verify with Rich Results Test. |
| **Organization** | Site-wide (JSON-LD in theme head) | P1 | ☐ — Brand name, logo, social profiles |
| **Article / BlogPosting** | Blog posts | P1 | ☐ — Author, date, publisher. Critical for E-E-A-T. |
| **FAQ** | Product pages, key landing pages | P1 | ☐ — Generates FAQ rich snippets in search results |
| **Review** | Product pages | P1 | ☐ — Star ratings in search results. Requires a review app (Judge.me, Loox) |
| **BreadcrumbList** | All pages | P2 | ☐ — Helps Google understand site structure |
| **HowTo** | How-to blog posts | P2 | ☐ — Step-by-step rich snippets |

**Tools for schema on Shopify**:
- **Built-in**: Most 2.0 themes include Product and basic Organization schema
- **Free**: JSON-LD for SEO (Shopify app) — auto-generates schema for products, articles, organization
- **Manual**: Add custom JSON-LD via theme.liquid for Organization and FAQ schema

**Test with**: [Google Rich Results Test](https://search.google.com/test/rich-results)

### 2.5 Security & Trust Signals

| # | Task | Priority | Status |
|---|------|----------|--------|
| 1 | HTTPS active on all pages | P0 — Shopify includes this | ☐ |
| 2 | No mixed content warnings (all resources via HTTPS) | P0 | ☐ |
| 3 | Privacy Policy page published | P0 — Required by law and Google | ☐ |
| 4 | Terms of Service page published | P0 | ☐ |
| 5 | Shipping & Returns policy page published | P0 — Trust signal for ecommerce | ☐ |
| 6 | Contact page with real information | P1 — Phone, email, physical address | ☐ |
| 7 | About page with founder story and credentials | P1 — E-E-A-T signal | ☐ |

---

## 3. Ongoing Technical Maintenance

### Monthly Audit

| Task | Frequency | Tool |
|------|-----------|------|
| Check GSC for crawl errors | Monthly | Google Search Console → Pages |
| Fix broken links (404s) | Monthly | GSC or Screaming Frog free |
| Monitor Core Web Vitals | Monthly | GSC → Core Web Vitals report |
| Review page speed for new pages | Per new page | PageSpeed Insights |
| Update XML sitemap (automatic on Shopify) | Automatic | Verify monthly |
| Check for manual actions | Monthly | GSC → Security & Manual Actions |

### Post-Launch (One-Time)

| Task | When | Tool |
|------|------|------|
| Set up Google Merchant Center + free product listings | Within 2 weeks of launch | Google Merchant Center (free) |
| Connect Shopify product feed to Merchant Center | Same time | Shopify's built-in Google & YouTube channel app |
| Verify product data (images, descriptions, pricing) passes Merchant Center review | After feed submission | Merchant Center Diagnostics |

**Google Merchant Center note**: Even without running paid Shopping ads (which belongs in M12), Merchant Center enables free product listings in Google Shopping search results and the Shopping tab. This is zero-cost organic product visibility. Shopify's Google & YouTube app handles the product feed automatically.

### Quarterly Audit

| Task | Frequency | Tool |
|------|-----------|------|
| Full technical SEO audit | Quarterly | Screaming Frog free (up to 500 URLs) |
| App audit (remove unused apps, check for leftover code) | Quarterly | Manual |
| Schema validation on key pages | Quarterly | Rich Results Test |
| Mobile usability check | Quarterly | GSC → Mobile Usability |

---

## 4. SEO Tool Stack (Bootstrapped)

### Phase 0: Free ($0/month)
- **Google Search Console** — crawl data, keyword performance, index coverage
- **Google Analytics 4** — traffic, user behavior, conversion tracking
- **Google PageSpeed Insights** — Core Web Vitals
- **Google Rich Results Test** — schema validation
- **Bing Webmaster Tools** — Bing-specific crawl data + free Bing SEO recommendations
- **Screaming Frog** (free up to 500 URLs) — technical audit

### Phase 1: Basic ($0-50/month)
- Add: **Ubersuggest** ($29/month) or **Google Keyword Planner** (free with Google Ads account) — keyword research
- Add: **JSON-LD for SEO** (Shopify app, free) — structured data
- Add: **Yoast SEO** or **SEO Manager** (Shopify app, ~$20/month) — meta tag management, redirects

### Phase 2: Growth ($50-150/month)
- Add: **Ahrefs Lite** ($99/month) or **SEMrush Pro** ($130/month) — competitive analysis, backlink monitoring, rank tracking
- Note: Only subscribe when you have enough content (20+ pages) to justify the investment. Don't pay for tools before you have content to optimize.

**Tool spend discipline** (same principle as M14): Don't spend more on SEO tools than you're investing in content creation. $100/month on Ahrefs is wasted if you're publishing 0 blog posts.


---

## 🔗 Dependencies & Relationships

### Feeds Into
- m12
- m13
- m14
- m17
- m22
- m23

### Requires
- m8
- m9

---

## ⚠️ Intelligence Gaps

- **Marine plasma keyword volumes unverified**
  - Priority: P1
- **No competitor backlink analysis**
  - Priority: P2
- **Shopify Core Web Vitals unverified**
  - Priority: P0
- **Organic CVR assumptions untested**
  - Priority: P2

---

## 🎯 Next Actions

Verify keyword volumes with Google Keyword Planner / Ubersuggest post-launch. Run PageSpeed Insights after Shopify theme selection. Publish first blog post (Complete Guide to Electrolytes).


---

## 🧰 OpKits

- OK-M16-001

---

---

_Report generated: 2026-02-09 17:49:43_

_Source: `data\m16`_