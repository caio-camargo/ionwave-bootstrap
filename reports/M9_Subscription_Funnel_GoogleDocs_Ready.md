# Subscription Funnel Architecture (M9)

## Strategic Decision: Subscription-First Design

**Hypothesis Tested:** HYP-002 (40% subscription attach rate target)
**Current Grade:** C (industry directional, not validated with IonWave data)
**Severity:** HIGH (directly affects LTV, which affects unit economics viability)

**Core Thesis:**
Subscribers deliver 6x LTV vs one-time buyers ($159 vs $26, per M21). Subscription revenue creates predictable cash flow and reduces reliance on paid acquisition. The product page must be architected to make subscription the default purchase path, not an afterthought.

---

## Visual: Product Page Widget Pattern

```
┌─────────────────────────────────────────────────────┐
│                                                       │
│  ✓ Subscribe & Save 15%         $41.65/mo           │  ← PRE-SELECTED
│    Delivered every 30 days                           │
│    [30 days ▼] [45 days] [60 days]                  │
│    ↑ TOGGLE (not dropdown)                          │
│                                                       │
│  ○ One-time purchase             $49.00              │  ← Secondary
│    (or save 15% with subscription above)             │
│                                                       │
│               [ ADD TO CART ]                        │
└─────────────────────────────────────────────────────┘
```

---

## 5 UX Rules (Evidence-Backed, Do NOT Deviate)

### Rule 1: Subscription price shown FIRST

**Reasoning:** Anchoring effect. First price seen becomes baseline for value judgment.

**Evidence:** Behavioral economics (prospect theory) + Recharge merchant A/B tests

**Grade:** B (strong theoretical + directional merchant data)

**Impact:** ~5-8% lift in subscription selection vs one-time first

---

### Rule 2: Toggle NOT dropdown

**Reasoning:** Toggles reduce cognitive load for binary choices. Dropdown adds friction (extra click + decision paralysis).

**Evidence:** Recharge/Skio merchant comparison data (2023-2024)

**Grade:** C (merchant-reported, not controlled study)

**Impact:** 15-20% higher conversion than dropdown (reported range)

**Caveat:** Effect diminishes if >2 frequency options. If adding 4+ frequencies, dropdown becomes necessary.

---

### Rule 3: Show savings as BOTH % AND $

**Reasoning:** "$7.35 saved" is concrete. "15%" requires mental math. Dual display captures both value-seekers and convenience-seekers.

**Evidence:** CRO case studies (VWO, Unbounce), DTC supplement brand tests

**Grade:** B (replicated across multiple brands/categories)

**Impact:** ~3-5% lift vs % alone

---

### Rule 4: One-time shown as strikethrough or visually de-emphasized

**Reasoning:** Visual hierarchy signals recommendation without hiding choice (maintains trust).

**Evidence:** Choice architecture research (Thaler & Sunstein), DTC conversion patterns

**Grade:** B (strong theoretical backing)

**Anti-pattern:** Hiding one-time option entirely feels manipulative and reduces trust

---

### Rule 5: Subscription pre-selected by default

**Reasoning:** Default effect (status quo bias). 60-80% of users don't change defaults.

**Evidence:** Behavioral economics (default bias), organ donation studies, DTC merchant data

**Grade:** A (replicated across domains, robust effect)

**Impact:** 40-60 percentage point swing in subscription selection

**Legal requirement:** Must disclose auto-renewal terms clearly. "Cancel anytime" messaging visible.

---

## Why This Pattern (vs Alternatives)

### Alternative 1: Dropdown for purchase type

❌ **Rejected.** Adds friction. Tested 15-20% lower conversion (Recharge data, C-grade)

### Alternative 2: One-time default, subscription upsell in cart

❌ **Rejected.** Misses anchor effect. Cart upsell conversion <10% (M17 email performs better at Day 21)

### Alternative 3: Subscription-only (no one-time option)

❌ **Rejected.** Eliminates flexibility. Some customers want to trial before committing. Forcing subscription increases cart abandonment ~12-18% (reported by brands that tried this, C-grade).

### Why Toggle Specifically:

- Mobile-friendly (large touch targets)
- Visually clear (selected state obvious)
- Fast interaction (single tap, not tap → wait → tap)
- Industry standard (LMNT, Thesis, Ample all use toggle pattern)

**Evidence Grade Summary:**
Pattern overall: **B** (strong merchant directional data, not controlled study)
Individual elements: A (default effect) to C (toggle vs dropdown lift)

---

## Implementation Checklist

### Platform Decision: Loop Subscriptions (see M21 for full comparison)

**Why Loop over Skio/Recharge:**

- ✅ Free up to 50 subscribers (zero cost at launch)
- ✅ $99/mo + 0.75% after (vs Skio $599/mo, Recharge $99/mo + $0.65/order)
- ✅ Shopify native checkout (required for fast checkout)
- ✅ Proven supplement results (Livingood Daily: 10%→2% churn)
- ⚠️ **INTELLIGENCE GAP:** Klaviyo integration depth unverified (M21 CRITICAL gap)

### Configuration:

| Setting                   | Value          | Reasoning                                                           |
| ------------------------- | -------------- | ------------------------------------------------------------------- |
| Default frequency         | 30 days        | Matches consumption rate (30-day supply)                            |
| Additional options        | 45-day, 60-day | Some customers deplete slower (fasting use case)                    |
| Discount %                | 15%            | Industry standard. Test 10% vs 15% once traffic allows (M14 PT-002) |
| Subscription pre-selected | YES            | Non-negotiable (Rule 5)                                             |
| Dunning retries           | 3 over 7 days  | Industry standard for payment recovery                              |
| Notification channels     | SMS + Email    | SMS has 98% open rate vs 20% email for urgent messages              |

**Reasoning on 15% discount:**

- Industry standard: LMNT (15%), AG1 (varies 10-20%), Thesis (15%)
- High enough to incentivize (~$7/month savings = meaningful)
- Low enough to preserve margin (gross margin 67% → contribution margin ~60% with subscription)
- **Blocker:** PT-001 ($49 vs $59 price test) affects discount dollar amount. If $49 wins, 15% = $6.86 vs $7.35 at $59.

---

## Legal & Compliance Requirements

### Supplement-specific disclosure (FTC/FDA):

- ✅ "Cancel anytime" messaging prominent (above fold)
- ✅ Auto-renewal terms in Terms of Service
- ✅ Email notification 3-5 days before each charge (Loop default behavior)
- ✅ One-click access to customer portal (pause/skip/cancel)

**Why this matters:**
FTC sued multiple supplement subscription brands 2022-2024 for "dark patterns" (hiding cancellation, unclear auto-renewal). Compliance is existential, not nice-to-have.

**Reference:** M2 (Legal/Compliance) for full framework [NOT MIGRATED - placeholder]

---

## Success Metrics & Kill Criteria

| Metric                   | Target  | Floor (Yellow) | Kill (Red)            | Source                     |
| ------------------------ | ------- | -------------- | --------------------- | -------------------------- |
| Subscription attach rate | 40%+    | 35%            | <30% after 100 orders | HYP-002, M21, M30          |
| Subscription revenue %   | 50%+    | 40%            | n/a                   | M21 benchmark              |
| Portal access time       | <30 sec | 30-60 sec      | >60 sec               | UX heuristic (abandonment) |
| Failed payment recovery  | >50%    | 40-50%         | <40%                  | M21 dunning benchmark      |

### Interpretation:

**<35% attach rate after 100 orders** → Funnel broken. Check:

1. Is one-time pre-selected by mistake?
2. Discount too low?
3. Subscription messaging unclear?

**<30% attach rate** → Existential. Subscriber LTV assumption ($159) collapses. Revisit unit economics (M3).

---

## Integration Points (Cross-TUP Dependencies)

### Feeds into:

- **M17 (Email flows)** → Subscription conversion email at Day 21 for one-time buyers (10-15% conversion to subscription, C-grade)
- **M21 (Churn prediction)** → Loop must pass churn signals to Klaviyo (subscriber skip, payment failure, etc.)
- **M30 (Analytics)** → Subscription vs one-time tracked separately in MER calculation

### Depends on:

- **M10 (Pricing)** → Subscription discount % decision (15% assumed, pending PT-001 result)
- **M21 (Platform comparison)** → Loop recommendation (Loop vs Recharge vs Skio analysis)
- **M24 (Fulfillment)** → Subscription cohort decay model (affects inventory forecasting)

### Conflict if:

- PT-001 ($49 vs $59) invalidates discount strategy → Would need to recalibrate % to maintain ~$7 savings
- Loop+Klaviyo integration incomplete → Can't track churn signals, invalidates M21 churn prediction model

---

## Known Risks & Mitigations

| Risk                                    | Likelihood                     | Impact      | Mitigation                                                                                                                                                             | Owner                |
| --------------------------------------- | ------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **Loop+Klaviyo integration incomplete** | MEDIUM                         | HIGH        | Verify integration docs before launch. Contact Loop support for churn signal passthrough confirmation. If incomplete, choose Recharge (robust Klaviyo integration).    | M21 intelligence gap |
| **Discount trains "discount seekers"**  | MEDIUM                         | MEDIUM      | Education-first onboarding (M17, M21). Emphasize value (electrolytes + marine plasma) over savings. Track cohort churn by acquisition source (discount vs full-price). | M21, M19             |
| **One-time default kills attach rate**  | LOW (if implemented correctly) | CRITICAL    | Pre-selected subscription is non-negotiable. QA checklist before launch. Monitor first 50 orders for attach rate.                                                      | M9, M24              |
| **Legal/FTC violation**                 | LOW                            | EXISTENTIAL | "Cancel anytime" visible. Auto-renewal terms clear. Email 3-5 days before charge. Customer portal accessible. Legal review before launch.                              | M2 [not migrated]    |

**Worst-case scenario:**
Loop integration broken → Migrate to Recharge mid-launch (painful but survivable). Recharge 50-50 plan ($50/mo, no transaction fees for first 50 subscribers) is viable backup.

---

## Testing Protocol (Pre-Launch Quality Gate)

**These tests are BLOCKING. Do not launch until all pass.**

- [ ] **Place test subscription order** → Subscription created in Loop dashboard
- [ ] **Access customer portal** → Can view/pause/skip/cancel without email support
- [ ] **Verify frequency options** → 30/45/60 day options visible, 30-day pre-selected
- [ ] **Check discount calculation** → $41.65 shown (15% off $49), or adjust if PT-001 changes price
- [ ] **Mobile test (iPhone + Android)** → Full flow works on actual devices (not just browser resize)
- [ ] **Verify Klaviyo sync** → Subscriber tagged in Klaviyo within 60 seconds of order
- [ ] **Legal compliance check** → "Cancel anytime" visible, Terms link accessible, auto-renewal disclosed
- [ ] **Failed payment test** → Trigger failed payment, verify dunning emails fire (3 retries over 7 days)

**Launch rule:** ALL tests must pass. If Klaviyo sync fails, escalate to Loop support immediately (blocking issue).

---

## Dialogue Insights (From M9 Workshop)

### Key insight from Growth Engineer persona:

"Theme performance budget (8 apps max, 500KB JS limit) prevents speed-kills-conversion death spiral. Every app slows the store. Subscription app choice affects page speed—Loop lighter than Recharge."

### Key insight from Skeptical Investor persona:

"Subscription UX pattern (toggle > dropdown) directly impacts HYP-002. 15-20% lift estimate is directional, not validated. Should track attach rate daily for first 2 weeks to detect issues early."

### Key insight from Operations Expert persona:

"Ad account hijacking is #1 actual threat—spend caps at 2x daily budget prevent catastrophic loss. Week 1 Setup Sequence prevents launch delay (Shopify account → theme → apps → testing is critical path)."

---

## What Would Invalidate This Approach?

### Scenario 1: Attach rate <30% after 100 orders

→ Subscription-first funnel isn't working. Possible causes:

1. Product not subscription-worthy (doesn't create habit/routine)
2. Messaging unclear (customers don't understand subscription value)
3. Price point too high (discount insufficient to overcome hesitation)

**Action:** Run PT-002 (subscription discount 10% vs 15% vs 20%). If attach rate still <30%, consider whether marine plasma creates enough recurring value for subscription model.

### Scenario 2: Churn >15% in Month 1

→ Subscribers regret decision (felt pressured by default selection)

**Action:** Add more prominent "one-time" option. Test subscription NOT pre-selected for 1 week. If attach rate drops to <20%, subscription model may not fit marine plasma use case.

### Scenario 3: Legal/FTC violation

→ "Dark pattern" accusation (hiding one-time, unclear auto-renewal)

**Action:** Immediate legal review. Add "What is Subscribe & Save?" explainer. Make one-time option more prominent. Survival > optimization.

---

## Version History

| Version | Date       | Change                                                                              | Actor         |
| ------- | ---------- | ----------------------------------------------------------------------------------- | ------------- |
| 1.0.0   | 2026-02-06 | Initial M9 workshop. Subscription-first UX pattern defined. Loop platform selected. | Caio + Claude |

---

## Related Documents

- **M21 (Subscription & Retention)** → Platform comparison, churn prediction, retention playbook
- **M10 (Pricing & Offer)** → Subscription discount % decision (15% assumed, PT-001 pending)
- **M17 (Email & SMS)** → Day 21 subscription conversion email for one-time buyers
- **M30 (Analytics & Dashboards)** → Subscription attach rate tracking, kill criteria
- **M14 (Testing & Optimization)** → PT-002 (subscription discount testing framework)

---

**Report Generated:** 2026-02-09
**Source TUP:** M9 - Ecommerce Infrastructure
**Workshop Protocol:** TWP-001 v2.0.0
**Quality Grade:** Not formally graded (infrastructure TUP)
