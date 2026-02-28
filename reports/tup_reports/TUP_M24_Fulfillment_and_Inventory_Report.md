# TUP M24: Fulfillment & Inventory

**Status:** unknown | **Quality:** N/A/10 | **Version:** N/A
**Cluster:** BCL-6 (N/A)

---

## 📋 Overview


---

## 📁 Content Files


---

## 🔧 Structured Data

_JSON files converted to human-readable format_

_No JSON files in this TUP._

---

## 📝 Narrative Content

### 📄 3pl_and_fulfillment.md

# M24: 3PL Selection & Fulfillment Operations

**TUP**: M24 — Fulfillment & Inventory
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 519, 520, 521; M9 store_setup_and_launch.md; M25 bookkeeping_setup.md; 3PL industry benchmarks 2026

---

## 1. Fulfillment Phase Strategy

IonWave's fulfillment evolves in three distinct phases. The key insight: self-fulfillment isn't a compromise — it's a learning phase. You learn more about your product, packaging, and customer expectations in 30 days of packing boxes than in 6 months of 3PL reports.

| Phase | Trigger | Duration | Method | Focus |
|-------|---------|----------|--------|-------|
| **Phase 0: Self-Fulfill** | Pre-launch through ~50 orders/month | Month 1-2 | Home/office, Shopify Shipping | Learn packaging, unboxing, carrier performance |
| **Phase 1: 3PL Onboard** | >50 orders/month OR founder time >10 hrs/week on fulfillment | Month 2-4 | ShipBob or ShipMonk | Transition, parallel running, SLA establishment |
| **Phase 2: 3PL Optimized** | >200 orders/month, stable SLAs | Month 4+ | Primary 3PL, rate optimization | Cost reduction, multi-SKU, subscription optimization |
| **Phase 3: Multi-Node** | >1,000 orders/month OR 2-day becomes competitive requirement | Month 12+ | Multi-warehouse 3PL or regional split | Zone optimization, faster delivery |

[Confidence: B | Source: D2C fulfillment scaling benchmarks]

### Phase 0: Why Self-Fulfill First

Self-fulfillment at launch provides:

1. **Product learning** — You discover packaging issues, damage patterns, and sizing problems before a 3PL does (and charges you for it)
2. **Customer closeness** — You read every order note, handle every inquiry, feel the pulse of demand
3. **Cost baseline** — You know exactly what fulfillment costs per order before comparing 3PL quotes
4. **Flexibility** — You can include handwritten notes, adjust packaging, test inserts with zero lead time
5. **Speed** — No onboarding delay. Ship Day 1.

**Switch signal**: When you spend >10 hours/week on fulfillment AND order volume is >50/month, it's time. Don't switch earlier — the learning is too valuable. Don't wait longer — the founder's time is worth more than $15/hour.

[Confidence: C | Source: D2C founder consensus]

---

## 2. Self-Fulfillment Setup (Phase 0)

### Minimum Viable Fulfillment Station

| Item | Cost | Where to Buy |
|------|------|-------------|
| Shipping scale (digital, lb/oz) | $25-40 | Amazon |
| Label printer (thermal, 4x6) | $150-200 | Rollo or DYMO 4XL |
| Poly mailers OR boxes (sized for sachet box) | $0.30-0.80/unit | Uline, EcoEnclose |
| Branded sticker (2" circle) | $0.05-0.10/unit | Sticker Mule |
| Insert card (thank-you + QR to portal) | $0.08-0.15/unit | Vistaprint, Moo |
| Packing tape (branded optional) | $3-8/roll | Uline |
| Bubble wrap or kraft paper | $0.05-0.15/order | Uline |

**Total setup**: ~$200-300 one-time + $0.50-1.20/order in materials

### Self-Fulfillment SOP

1. **Order received** → Shopify notification (check 3x daily: 8am, 12pm, 5pm)
2. **Pick product** → Check lot number, expiration date, quantity
3. **Pack** → Product + insert card + branded sticker on exterior. Kraft paper fill for protection.
4. **Weigh** → Record weight. Compare to shipping label weight class.
5. **Label** → Print shipping label from Shopify Shipping. Apply to package.
6. **Ship** → Schedule pickup or drop at carrier location.
7. **Update** → Verify tracking number synced to Shopify. Customer receives tracking email automatically.
8. **Log** → Record lot number shipped per order (for recall traceability)

**Same-day cutoff**: Orders placed by 2:00 PM ET ship same day. After 2:00 PM → next business day.

[Confidence: C | Source: D2C self-fulfillment best practices]

### Carrier Selection for Phase 0

| Carrier | Best For | Cost (1 lb, Zone 3-5) | Speed | Notes |
|---------|----------|----------------------|-------|-------|
| **USPS First Class** | Under 16 oz | $4.50-6.00 | 3-5 days | Best for single sachet boxes |
| **USPS Priority** | 1-5 lbs | $8.00-12.00 | 2-3 days | Includes $50 insurance, free boxes |
| **UPS Ground** | >5 lbs or multi-box | $9.00-14.00 | 3-6 days | Negotiable at volume |
| **FedEx Ground** | >5 lbs or multi-box | $9.00-14.00 | 3-6 days | Negotiable at volume |

**IonWave recommendation**: USPS First Class for single-box orders (majority at launch). USPS Priority for multi-box or time-sensitive. Use Shopify Shipping for discounted rates (up to 77% off retail).

**Dimensional weight warning**: 2026 carriers all use DIM weight pricing. IonWave sachets in a box should be well under DIM thresholds, but verify: DIM weight = (L × W × H) / 139 for FedEx/UPS, /166 for USPS. If DIM weight > actual weight, you pay DIM.

[Confidence: B | Source: Carrier rate cards 2026, Shopify shipping discounts]

---

## 3. 3PL Selection (Phase 1)

### 3PL Comparison — Updated 2026

| 3PL | Best For | Pick/Pack | Storage | Min Monthly | Shopify Integration | Supplement Capable | IonWave Fit |
|-----|----------|-----------|---------|-------------|--------------------|--------------------|-------------|
| **ShipBob** | Growing D2C, 2-day shipping | $5.25-6.50/order | $40/pallet/mo | ~$275/mo | Excellent (native) | Yes (temp-controlled available) | **Recommended — Phase 1** |
| **ShipMonk** | Startups, lower volume | $3.00-4.50/order | $25/pallet/mo | Low (volume-tiered) | Good (native) | Yes | Good alternative |
| **ShipHero** | Tech-forward brands | $5.00-6.00/order | $35/pallet/mo | ~$500/mo | Good | Yes | Good for tech needs |
| **Flexport** | Scale brands (ex-Deliverr) | $4.00-5.50/order | Included in fee | ~$5,000/mo | Good | Yes | **Too expensive at launch** |
| **Amazon FBA** | Amazon channel ONLY | $3.00-5.00/order | $0.87/cu ft/mo (standard) | None | Manual (MCF for non-Amazon) | Limited temp control | **Amazon channel only — NOT for D2C** |
| **Local/Regional 3PL** | Personal service | $2.50-4.00/order | Negotiable | Varies | Custom integration | Varies | Evaluate if supplement-specialized |

**Correction from Danilo**: Deliverr was acquired by Flexport in 2022. They are now one entity. Flexport's $5,000/month minimum prices out early-stage IonWave. Remove from consideration until >500 orders/month.

**Correction from Danilo**: Amazon FBA is NOT a 3PL alternative for D2C orders. Per M28, FBA is for the Amazon sales channel only. Multi-Channel Fulfillment (MCF) from Amazon is technically possible but comes with Amazon-branded packaging — which destroys brand experience. Do not use FBA for Shopify orders.

[Confidence: B | Source: 3PL pricing research 2026, updated from Danilo tab 519]

### IonWave 3PL Recommendation

**Primary: ShipBob**
- Native Shopify integration (real-time inventory sync)
- 2-day shipping network (35+ fulfillment centers)
- Supplement-friendly (temperature monitoring available)
- $275/month minimum is accessible at 50+ orders/month
- Dedicated account manager for growing brands

**Backup: ShipMonk**
- Lower per-order cost ($3-4 vs $5-6)
- Good for brands that want to optimize cost over speed
- Less fulfillment center coverage (fewer 2-day zones)

### 3PL Evaluation Scorecard

Before signing with any 3PL, score them on these 8 dimensions:

| Dimension | Weight | Questions to Ask | Min Score |
|-----------|--------|-----------------|-----------|
| **Supplement compliance** | 25% | FDA-registered warehouse? cGMP procedures? Temperature monitoring? Lot tracking? Expiration management? | 4/5 |
| **Shopify integration** | 20% | Native app? Real-time inventory sync? Subscription order handling (Recharge/Skio)? | 3/5 |
| **Shipping speed** | 15% | What % of US reaches in 2 days? Processing time SLA? Cutoff time? | 3/5 |
| **Accuracy** | 15% | What is their reported accuracy rate? Error resolution process? | 4/5 |
| **Pricing** | 10% | All-in cost per order (pick/pack + storage + shipping)? Hidden fees? | 3/5 |
| **Scalability** | 5% | Can they handle 10x volume? Multi-warehouse? International? | 2/5 |
| **Service** | 5% | Dedicated account manager? Response time? Hours of support? | 3/5 |
| **References** | 5% | Similar brand references? Supplement brand experience? | 2/5 |

**Minimum qualifying score**: 3.5/5.0 weighted average. Below that, look elsewhere.

[Confidence: C | Source: 3PL evaluation frameworks, supplement industry requirements]

### Supplement-Specific 3PL Requirements

This is non-negotiable for IonWave. Your 3PL MUST have:

| Requirement | Why | Verification |
|-------------|-----|-------------|
| **FDA-registered facility** | Required for storing dietary supplements (21 CFR Part 111) | Ask for FDA registration number |
| **Temperature monitoring** | Supplements degrade in heat. IonWave sachets need 59-86°F (15-30°C) | Ask for temp monitoring logs |
| **Humidity control** | Moisture damages packaging and product integrity. Target <60% RH | Ask for facility specs |
| **Lot tracking (FEFO)** | First Expired, First Out — not just FIFO. Prevents shipping near-expiration product | Ask for WMS lot management demo |
| **Expiration date management** | Alerts when inventory approaches expiration. Quarantine expired stock | Ask for expiration alert workflow |
| **Recall capability** | Must be able to identify and quarantine all units from a specific lot within 24 hours | Ask for recall drill history |
| **Pest control program** | Regular pest monitoring and treatment. Required for food/supplement facilities | Ask for pest control records |
| **Inventory count reconciliation** | Regular cycle counts. Must match Shopify within ±1% | Ask for count frequency and accuracy history |

**FEFO vs FIFO**: For supplements with expiration dates, FEFO (First Expired, First Out) is critical. Standard FIFO can result in newer stock being shipped while older stock sits and expires. FEFO reduces waste from 10-18% to under 3% for supplement brands.

[Confidence: A | Source: FDA 21 CFR Part 111, USP <1079> storage guidelines]

---

## 4. 3PL Contract, Insurance & Compliance (U1, U2, U3)

### Contract Negotiation Checklist (U1)

Before signing any 3PL contract, negotiate these terms:

| Term | What to Negotiate | Red Flag |
|------|-------------------|----------|
| **Initial commitment** | 3-month trial period, not 12 months | Auto-renewal without 30-day out clause |
| **SLA breach exit** | 30-day termination right if SLAs missed for 2+ consecutive weeks | No SLA-based exit clause |
| **Peak season surcharges** | Cap at 15% above standard rates. Written in contract. | "Market rate" language with no cap |
| **Storage fee increases** | Cap annual increase at 5% or CPI, whichever is lower | Unlimited increase provision |
| **Supplement compliance** | Temperature monitoring, lot tracking, FEFO as SLA-level commitments | Listed as "best effort" or not in contract |
| **Minimum fees** | Understand monthly minimum. Ensure achievable at your volume. | Minimum fee >2x your expected monthly cost |
| **Data ownership** | You own all order, inventory, and customer data | 3PL retains data rights or charges for export |
| **Transition assistance** | 3PL provides 30-day transition support if you leave | No data export provision or inventory return timeline |

[Confidence: A | Source: 3PL contract negotiation best practices]

### Insurance Requirements (U3)

Your 3PL must carry (verify certificates before signing):

| Insurance Type | Minimum Coverage | What It Covers |
|---------------|-----------------|----------------|
| **General liability** | $1M per occurrence | Premises injuries, general business liability |
| **Product liability** | $1M (name IonWave as additional insured) | Damage from products stored/shipped |
| **Bailee's coverage** | Value of your inventory | Loss/damage to inventory while in 3PL custody |
| **Workers' compensation** | Per state requirements | Employee injuries during fulfillment operations |

**IonWave's own coverage**: Verify product liability insurance covers inventory stored at a third-party facility. Consult insurance broker before signing.

[Confidence: B | Source: 3PL insurance frameworks]

### Temperature Excursion Protocol (U2)

For supplements, temperature excursions can compromise product integrity:

| Condition | Protocol |
|-----------|----------|
| **Excursion >86°F for <2 hours** | Log incident. No action needed. |
| **Excursion >86°F for 2-4 hours** | Log. 3PL must notify brand within 2 hours. Monitor product. |
| **Excursion >86°F for >4 hours** | Quarantine affected inventory. Request COA re-test. Do NOT ship until cleared. |
| **Excursion >100°F any duration** | Quarantine immediately. Product likely compromised. Write off (M25 account 5040). |
| **HVAC failure** | 3PL must have backup climate control or move inventory to controlled area within 4 hours |

3PL must provide temperature monitoring logs on request. Monthly summary recommended.

[Confidence: B | Source: USP <1079> Good Storage Practice, supplement stability guidelines]

---

## 5. 3PL Onboarding Protocol

### Pre-Onboarding (Week -2 to -1)

| Step | Task | Owner | Duration |
|------|------|-------|----------|
| 1 | Contract signed with SLA terms | Founder | 1-3 days |
| 2 | Shopify app/integration installed and connected | Ops | 1 hour |
| 3 | Products created in 3PL system (SKU mapping) | Ops | 1-2 hours |
| 4 | Shipping rates configured (carrier preferences, zones) | Ops | 1-2 hours |
| 5 | Branded packing slip designed and uploaded | Ops | 1-2 hours |
| 6 | Insert card/materials sent to 3PL | Ops | Ship time |
| 7 | Inbound shipment of inventory arranged (from manufacturer or self-storage) | Ops | 3-7 days |

### Onboarding (Week 0)

| Step | Task | Verification |
|------|------|-------------|
| 8 | Inventory received and counted at 3PL | Count matches shipment manifest ±0 |
| 9 | Lot numbers and expiration dates entered in WMS | Spot-check 3 random SKU/lots |
| 10 | Test order #1: Place from Shopify, verify it routes to 3PL | Order appears in 3PL dashboard |
| 11 | Test order #2: Verify pick, pack, label, ship | Receive package, check contents + packing slip |
| 12 | Test order #3: Verify tracking syncs back to Shopify | Customer-facing tracking updates correctly |
| 13 | Returns process configured and tested | Return label generated, RMA workflow works |
| 14 | Subscription order test (Recharge/Skio → Shopify → 3PL) | Recurring order creates and ships correctly |
| 15 | **Go live**: Route all new orders to 3PL | Monitor first 10 orders closely |

### Parallel Running Period

**Do NOT cut over instantly.** Run parallel for 3-7 days:

1. Self-fulfill any orders that were in-progress
2. Route all NEW orders to 3PL
3. Monitor 3PL orders for accuracy, speed, tracking sync
4. Compare self-fulfillment quality to 3PL quality
5. After 10+ successful 3PL orders with zero issues → full cutover

**Inventory transfer strategy**: Don't ship existing inventory to 3PL. Instead:
- Sell through self-fulfillment stock (continue packing at home)
- Send NEW production run directly from manufacturer → 3PL warehouse
- This avoids transfer costs and prevents inventory confusion

[Confidence: C | Source: D2C 3PL transition best practices]

---

## 6. 3PL SLA Monitoring

### Weekly SLA Scorecard

Track these metrics weekly. Review with 3PL account manager monthly.

| Metric | Target | Yellow Flag | Red Flag | Action on Red |
|--------|--------|-------------|----------|---------------|
| **Ship within 48hr** | >95% | 90-95% | <90% | Escalate to account manager. Written warning. |
| **Order accuracy** | >99% | 97-99% | <97% | Root cause analysis within 48hr. Corrective action plan. |
| **Damage rate** | <1% | 1-2% | >2% | Packaging review. Possible carrier or packing change. |
| **Inventory accuracy** | >99% | 97-99% | <97% | Demand cycle count. Review receiving process. |
| **Tracking sync** | >99% | 95-99% | <95% | Integration audit. May need support ticket with 3PL. |
| **Return processing** | <72hr | 72-120hr | >120hr | Review returns SOP with 3PL. |

### Monthly SLA Review

| Review Item | What to Check |
|-------------|---------------|
| All-in cost per order | Total 3PL invoice ÷ total orders. Trending up or down? |
| Average ship time | Actual transit days (label to delivery). Compare to carrier SLA. |
| Customer complaints (fulfillment-related) | Categorize: late, damaged, wrong item, missing item |
| Carrier performance by zone | Which zones are slow? Consider zone-based carrier switching |
| Subscription order reliability | Are renewal orders shipping on time? Any processing delays? |
| Inventory shrinkage | Missing units not explained by orders or returns? |

### 3PL Escalation Protocol

| Level | Trigger | Action | Timeline |
|-------|---------|--------|----------|
| **Level 1: Notice** | Single metric yellow for 2+ weeks | Email account manager with data | 24hr response expected |
| **Level 2: Warning** | Any metric red, or 3+ metrics yellow | Formal meeting. Written corrective action plan. | 1 week to resolve |
| **Level 3: Review** | Red metric persists >2 weeks after warning | Contract review. Begin evaluating alternatives. | 30-day improvement window |
| **Level 4: Transition** | Persistent failure or critical error (wrong product shipped, data breach) | Begin 3PL transition process. Do NOT wait. | Immediate parallel evaluation |

[Confidence: B | Source: 3PL SLA management frameworks]

---

## 7. Damaged & Lost Shipment Protocol

### Customer Reports Damage

**Principle**: Replace first, investigate later. The customer's experience is more important than the $20 product cost.

| Step | Action | Timeline | Owner |
|------|--------|----------|-------|
| 1 | Customer reports damage (email, chat, or phone) | — | Customer |
| 2 | Request photo of damage (not required — trust the customer) | Within 4 hours of report | Support |
| 3 | Ship replacement immediately | Same business day | Ops |
| 4 | Send tracking for replacement + apology | Immediately after shipping | Support |
| 5 | Do NOT request return of damaged product (not worth the cost) | — | — |
| 6 | File carrier claim (if carrier damage, not product defect) | Within 48 hours | Ops |
| 7 | Log incident: product, lot number, carrier, damage type | Same day | Ops |
| 8 | If 3+ reports from same lot → escalate to quality review | Immediately | Founder |

### Customer Reports Lost Shipment

| Step | Action | Timeline | Owner |
|------|--------|----------|-------|
| 1 | Customer reports non-delivery | — | Customer |
| 2 | Check tracking status in carrier system | Within 4 hours | Support |
| 3 | If "Delivered" but customer says no → ask to check with neighbors, building office, porch | Within 4 hours | Support |
| 4 | If still missing after 48 hours → ship replacement | Same business day | Ops |
| 5 | File carrier claim for lost package | Within 48 hours | Ops |
| 6 | Log incident: carrier, zone, date, tracking number | Same day | Ops |

### Damage/Loss Budget

Budget 1-2% of orders for damage/loss replacement at launch. This is a cost of doing business:

| Volume | Monthly Orders | Expected Replacements | Cost (product + shipping) |
|--------|---------------|----------------------|--------------------------|
| Early (Month 1-3) | 100 | 1-2 | $40-80 |
| Growing (Month 4-6) | 500 | 5-10 | $200-400 |
| Scaling (Month 7-12) | 1,000+ | 10-20 | $400-800 |

**Fraud monitoring**: If a single customer reports 3+ damage/loss incidents, flag for review. Pattern abuse is rare but real. Handle diplomatically — call rather than accuse.

[Confidence: C | Source: D2C customer experience practices, carrier claim procedures]

---

## 8. Unboxing Experience

### IonWave Packaging Strategy

The unboxing experience is where IonWave's brand comes alive. For a marine plasma product, the packaging should feel clean, premium, and intentional.

| Component | Phase 0 (Self-Fulfill) | Phase 1 (3PL) | Phase 2 (Optimized) |
|-----------|----------------------|---------------|---------------------|
| **Outer packaging** | White poly mailer or kraft box | Branded mailer (logo on exterior) | Custom printed box |
| **Product protection** | Kraft paper fill | Same | Same (sachets are durable) |
| **Insert card** | Thank-you card with QR to portal + founder note | Same design, printed at scale | Seasonal/rotating inserts |
| **Branded sticker** | 2" circle on exterior | Same | May upgrade to branded tape |
| **Sachet presentation** | Neat arrangement | Same | Custom inner tray (at volume) |
| **Surprise element** | Handwritten note (first 100 orders) | None — not scalable | Free sample of new product |

**Cost per package**:
- Phase 0: $0.50-1.00 (mailer + insert + sticker + fill)
- Phase 1: $1.00-2.00 (branded mailer + insert + sticker)
- Phase 2: $2.00-4.00 (custom box + insert + branded fill)

**IonWave insert card must include**:
1. Founder thank-you (2-3 sentences, first person — "I started IonWave because...")
2. QR code → customer portal / subscription management
3. Usage reminder: "One sachet. Every morning. Tear, pour, drink."
4. Social handle + branded hashtag
5. Referral code (FRIEND15 — per M18 referral program)

[Confidence: C | Source: D2C packaging benchmarks, M22 referral integration]

---

## 9. Kitting & Packaging Compliance (U10, U19)

### Standard Kit Configuration

IonWave standard fulfillment kit:
- 1x product box (30 sachets)
- 1x insert card (thank-you + QR + referral code)
- 1x branded sticker (2" circle, applied to exterior)

### Kit Change Orders (U10)

Any changes to the kit (new insert, seasonal card, added sample) require:
1. Submit "Kit Change Order" to 3PL **5+ business days** before next subscription billing cycle
2. Include: new item specifications, placement instructions, quantity needed
3. Kitting fee: typically $0.25-0.75 per additional item per order
4. Track kitting accuracy separately from pick/pack accuracy

### Packaging Compliance Audit (U19)

3PL packaging quality degrades over time without verification:
- **Monthly mystery order**: Place 1-2 test orders per month, shipped to your address
- **Verify**: Correct insert, branded sticker applied, product orientation, no damage
- **Photo audit**: Ask 3PL to photograph first 5 orders of each kit change
- **Escalation**: 2+ packaging failures → formal SLA discussion (brand damage, not just ops error)

### Inbound Shipment Receiving SOP (U20)

For each new inventory shipment to the 3PL:
1. Send ASN (Advance Shipping Notice) 48 hours before arrival: PO number, lot numbers, quantities, expiration dates
2. 3PL counts and confirms within 24 hours of receipt
3. Any discrepancy >1% triggers investigation with carrier and manufacturer
4. COA must be on file before 3PL makes inventory "available for sale"
5. Lot numbers and expiration dates entered in WMS — spot-check 3 random items

---

## 10. Carrier Strategy (U11)

### Dual-Carrier Configuration

Never rely on a single carrier. Configure your 3PL with at least 2 active carriers:

| Primary | Secondary | When to Use Secondary |
|---------|-----------|----------------------|
| USPS First Class/Priority | UPS Ground | USPS transit >5 days, peak season congestion |
| UPS Ground | FedEx Ground | UPS service disruption, zone-specific delays |

### Rate Shopping

Enable per-order rate shopping at the 3PL:
- System selects cheapest carrier meeting delivery SLA for each order
- During peak season (Nov-Jan), pre-approve UPS/FedEx as fallback if USPS transit times degrade
- Monitor carrier performance weekly: % on-time by carrier → shift volume to best performer

[Confidence: B | Source: Multi-carrier fulfillment best practices]

---

## 11. Cross-TUP References

- **M9 store_setup_and_launch.md**: Shopify 3PL integration (task 6.6), inventory tracking setup (task 3.4), shipping rates (task 4.5). M9 references M24 for fulfillment specifics.
- **M25 bookkeeping_setup.md**: COGS structure — Product COGS ($20 landed), 3PL fees (account 6110), Outbound Shipping (6120), Return Shipping (6130), COGS-Freight In (5030). Shipping is OpEx, not COGS.
- **M28 expansion_paths.md**: International shipping gated to $100K+ MRR. Amazon FBA for Amazon channel only. Multi-Channel Fulfillment NOT recommended for D2C.
- **M20 support_operations.md**: Customer support handles damaged/lost shipment tickets. 4-hour response time SLA. Escalation protocol for chargebacks.
- **M18 cart_recovery.md**: Free shipping as cart recovery incentive (AC3). Auto-apply, no code friction.
- **M22 referral.md**: FRIEND15 referral code on insert cards.

---

*3PL selection is a critical operational decision. Start with self-fulfillment to learn, transition at 50+ orders/month, and optimize from there. See `launch_operations.md` for the launch day protocol and `inventory_management.md` for forecasting.*


---

### 📄 dialogue_summary.md

# M24 Dialogue Summary — Fulfillment & Inventory

**Rounds**: 6 (to saturation)
**Personas**: 3 (3PL Operations Specialist, Inventory Planning Analyst, D2C Launch Strategist)
**Upgrades**: 27
**Unresolved**: 0 (5 deferred to execution — CM MOQ, ShipBob contract terms, product liability insurance, billing date spreading, temperature stability profile)

---

## Key Themes

1. **Contract and legal protections were absent** — Danilo focused on operational mechanics with zero guidance on contract negotiation, insurance, or legal protections when engaging a 3PL
2. **First purchase order is the hardest decision** — Forecasting assumes sales data exists, but the biggest cash commitment happens pre-revenue. Dedicated decision framework created.
3. **Subscription demand is non-linear and clusters** — Flat 12% churn distorts forecasts. Cohort decay model and renewal clustering warning added.
4. **Launch protocol needed failure-mode coverage** — Strong on "everything works" path, weak on abort, site-down, and first-complaint scenarios
5. **Soft launch before paid traffic is critical** — Going straight to ads risks burning money on undiscovered system failures
6. **Ad spend and inventory are not independent** — Explicit linkage needed: budget caps, demand correlation, inventory-gating on scaling
7. **Ongoing 3PL quality verification is essential** — Trust-but-verify: mystery orders, photo audits, inbound receiving SOP
8. **Dead stock is as dangerous as stockout for cash-constrained startups** — Liquidation protocol and inventory turnover tracking added

## Upgrade Registry

| # | Upgrade | Persona | Applied To |
|---|---------|---------|------------|
| U1 | Contract negotiation checklist and red-flag terms | 3PL Ops | 3pl_and_fulfillment.md |
| U2 | Temperature excursion protocol | 3PL Ops | 3pl_and_fulfillment.md |
| U3 | 3PL insurance requirements (liability, bailee's, additional insured) | 3PL Ops | 3pl_and_fulfillment.md |
| U4 | Manufacturing MOQ analysis and cash trap risk | Inventory | inventory_management.md |
| U5 | Statistical safety stock formula (replaces flat 14-day buffer after 60 days) | Inventory | inventory_management.md |
| U6 | Subscription cohort decay model (month-by-month vs flat rate) | Inventory | inventory_management.md |
| U7 | Launch abort and restart protocol | Launch | launch_operations.md |
| U8 | Soft launch / friends-and-family protocol before hard launch | Launch | launch_operations.md |
| U9 | Day 1 ad budget hard cap ($100-200) with daily ramp schedule | Launch | launch_operations.md |
| U10 | Kitting/assembly instructions and kit change order process | 3PL Ops | 3pl_and_fulfillment.md |
| U11 | Carrier diversification strategy (dual carrier, rate shopping) | 3PL Ops | 3pl_and_fulfillment.md |
| U12 | Returns processing cost analysis by phase | 3PL Ops | international_and_scaling.md |
| U13 | First PO decision framework (sizing, cash commitment, 25% rule) | Inventory | inventory_management.md |
| U14 | Subscription renewal clustering warning for Months 1-3 | Inventory | inventory_management.md |
| U15 | Expiration risk analysis for oversized first POs | Inventory | inventory_management.md |
| U16 | Site down emergency protocol for launch day | Launch | launch_operations.md |
| U17 | Post-launch retrospective template at Hour 72 | Launch | launch_operations.md |
| U18 | Free shipping cost modeling at scale (8% revenue trigger) | Launch | international_and_scaling.md |
| U19 | Branded packaging compliance audit (mystery orders) | 3PL Ops | 3pl_and_fulfillment.md |
| U20 | Inbound shipment receiving SOP (ASN, count, COA) | 3PL Ops | 3pl_and_fulfillment.md |
| U21 | Dead stock liquidation protocol (flash sale → donate → destroy) | Inventory | inventory_management.md |
| U22 | Ad spend → inventory demand correlation model (0.6-0.8x multiplier) | Inventory | inventory_management.md |
| U23 | First negative review protocol (founder response, systemic vs subjective) | Launch | launch_operations.md |
| U24 | Inventory depletion tracking in 72-hour scorecard | Launch | launch_operations.md |
| U25 | Batch/lot-level cost tracking for 3PL invoices | 3PL Ops | 3pl_and_fulfillment.md |
| U26 | Inventory turnover ratio target (6-8x/year) | Inventory | inventory_management.md |
| U27 | Founder energy management note for launch week | Launch | launch_operations.md |


---

### 📄 international_and_scaling.md

# M24: International Shipping & Fulfillment Scaling

**TUP**: M24 — Fulfillment & Inventory
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tab 522; M28 expansion_paths.md; M9 operations_governance.md

---

## 1. International Strategy: US First, Then Expand

### The Rule

**US only at launch. Full stop.**

International shipping adds customs, duties, VAT, regulatory compliance, longer transit, and more customer service complexity. None of this is worth it until US operations are proven and profitable.

| Phase | Geography | Trigger | Estimated Timeline |
|-------|-----------|---------|-------------------|
| **Phase 1** | US only (contiguous 48 states) | Launch | Month 1-9 |
| **Phase 1.5** | US + Alaska/Hawaii (USPS Priority) | Customer demand | Month 3+ |
| **Phase 2** | US + Canada | US MRR >$50K, proven unit economics | Month 9-12 |
| **Phase 3** | US + Canada + UK | US MRR >$100K, international demand signal | Month 12-18 |
| **Phase 4** | Additional markets (EU, Australia) | US MRR >$250K, dedicated ops capacity | Month 18+ |

[Confidence: B | Source: M28 expansion_paths.md, D2C international expansion benchmarks]

### Why Not International at Launch

| Reason | Detail |
|--------|--------|
| **Customs/duties complexity** | DDP (Delivered Duty Paid) vs DDU (Delivered Duty Unpaid) — choose wrong and customers refuse delivery |
| **Regulatory** | Health Canada requires NPN (Natural Product Number) for supplements. UK requires MHRA notification. |
| **Shipping cost** | $15-35 per order international vs $5-12 domestic |
| **Returns** | International returns are expensive and slow |
| **Customer service** | Time zone differences, currency conversion, local expectations |
| **Focus** | Every hour on international ops is an hour not spent proving the US model |

---

## 2. Phase 2: Canada Expansion

### When to Enter Canada

**Trigger**: US MRR >$50K with stable unit economics (contribution margin >30%)

### Canada Fulfillment Options

| Option | Pros | Cons | Best For |
|--------|------|------|----------|
| **Cross-border from US 3PL** | No Canadian warehouse needed. Simple. | Higher shipping cost ($15-20). Duties at border. 7-14 day transit. | Low volume (<50 Canadian orders/month) |
| **Canadian 3PL** (ShipBob Toronto, ShipMonk Canada) | Fast delivery (2-4 days). No border issues. | Requires Canadian inventory. Higher ops complexity. | High volume (>50 Canadian orders/month) |
| **Hybrid** | Cross-border initially, Canadian 3PL when volume justifies | Transition overhead | Growing Canadian demand |

### Canada Compliance Checklist

| Requirement | Details | Cost |
|-------------|---------|------|
| **Health Canada NPN** | Natural Product Number required for supplement sales in Canada | $2,000-5,000 + 6-12 months processing |
| **Bilingual labeling** | All labels must be in English AND French (Consumer Packaging and Labelling Act) | Packaging redesign cost |
| **GST/HST** | 5-15% depending on province. Must collect and remit if selling from Canadian entity or meeting revenue threshold. | Accounting setup |
| **Customs classification** | HS Code for dietary supplements: 2106.90 (typical) | One-time classification |
| **De minimis threshold** | Canada: CAD $20 (below this, no duties). IonWave products exceed this. | Duties apply |

### Canada Shipping Costs

| Method | Cost | Transit | Notes |
|--------|------|---------|-------|
| USPS First Class International | $15-18 | 7-14 days | No tracking end-to-end |
| USPS Priority International | $25-35 | 6-10 days | Includes tracking |
| UPS/FedEx International Ground | $18-25 | 5-8 days | Best tracking, most reliable |
| Canada Post (from Canadian 3PL) | $8-12 | 2-5 days | Cheapest if using Canadian warehouse |

**IonWave recommendation**: Start with cross-border USPS Priority International. Absorb into product pricing (increase Canadian price by $5-10). Switch to Canadian 3PL when Canadian orders exceed 50/month.

[Confidence: C | Source: Cross-border D2C benchmarks, Canada supplement regulation summary]

---

## 3. Phase 3: UK Expansion

### When to Enter UK

**Trigger**: US MRR >$100K AND Canadian expansion stable

### UK Compliance Checklist

| Requirement | Details | Cost |
|-------------|---------|------|
| **MHRA notification** | Supplements must be notified to the Medicines and Healthcare products Regulatory Agency | Free to submit, but formulation review needed |
| **UK-specific labeling** | Different nutrition information format than US/Canada. SI units. UK-specific allergen warnings. | Packaging redesign |
| **VAT registration** | 20% VAT. Required if selling >£85,000/year from UK entity (or immediately if storing in UK). | £0 to register, ongoing compliance cost |
| **IOSS or UK VAT scheme** | For direct shipments under £135, seller must collect VAT at checkout | Shopify supports this natively |
| **Customs** | Post-Brexit, UK is a separate customs territory from EU. HS code + commercial invoice required. | Per-shipment documentation |

### UK Shipping Costs

| Method | Cost | Transit | Notes |
|--------|------|---------|-------|
| USPS Priority International (from US) | $25-35 | 7-12 days | Reliable but slow |
| UPS/FedEx International Express | $35-55 | 3-5 days | Expensive but fast |
| UK 3PL (ShipBob London, local) | $5-8 per order | 1-3 days | Requires UK inventory |
| Fulfillment by Amazon UK (for Amazon UK channel) | $3-5 per order | 1-2 days | Amazon channel only |

**IonWave recommendation**: Only enter UK with a local 3PL. Cross-border shipping from US is too expensive ($25-55) and too slow (7-12 days) for a competitive customer experience. This means UK entry requires dedicated inventory allocation — a significant commitment.

[Confidence: C | Source: UK supplement regulations, post-Brexit D2C considerations]

---

## 4. Fulfillment Scaling Milestones

### Growth Stage Matrix

| Stage | Orders/Month | Revenue/Month | Fulfillment Model | Key Focus |
|-------|-------------|---------------|-------------------|-----------|
| **Startup** | 0-100 | $0-5K | Self-fulfill | Learn, iterate, personal touch |
| **Traction** | 100-500 | $5-25K | Single 3PL | Reliability, SLA establishment |
| **Growth** | 500-2,000 | $25-100K | Single 3PL, optimized | Cost optimization, carrier negotiation |
| **Scale** | 2,000-5,000 | $100-250K | Multi-node 3PL or 2 warehouses | Zone optimization, 2-day coverage |
| **Enterprise** | 5,000+ | $250K+ | Multi-warehouse + international nodes | Full US + international coverage |

### When to Add a Second Warehouse

**Trigger**: >2,000 orders/month AND significant volume in multiple shipping zones

**Why**: A single warehouse in, say, California means East Coast orders take 5-6 days via ground. A second node in the East (NJ, PA, or GA) gets most of the US within 2-3 days.

| Warehouse Pair | US Coverage (2-day) | Typical Choice |
|---------------|-------------------|----------------|
| CA + NJ | ~85% of US | Best for balanced East/West demand |
| TX + NJ | ~80% of US | Good if Midwest is strong |
| CA + GA | ~75% of US | Good if Southeast is strong |

**ShipBob advantage**: They operate 35+ fulfillment centers and can auto-route inventory to optimize zone coverage. This is why they're the recommended Phase 1 3PL — built-in multi-node when you're ready.

### Cost Optimization Opportunities by Stage

| Stage | Optimization | Expected Savings |
|-------|-------------|-----------------|
| **Traction** | Negotiate shipping rates based on volume | 5-15% on carrier costs |
| **Traction** | Optimize box size to avoid DIM weight surcharges | $0.50-1.00/order |
| **Growth** | Zone-based carrier selection (USPS for zones 1-4, UPS for zones 5-8) | 10-20% on shipping |
| **Growth** | Batch processing (3PL picks multiple orders in one pass) | Reduced pick/pack fees |
| **Scale** | Multi-warehouse inventory split | Reduced avg shipping distance and cost |
| **Scale** | Carrier contract negotiation (volume discounts) | 15-25% on shipping |
| **Enterprise** | Rate shopping per order (auto-select cheapest carrier/service) | 10-15% on shipping |

[Confidence: C | Source: D2C fulfillment scaling frameworks]

---

## 5. Free Shipping Economics

### The Free Shipping Threshold

Free shipping is the #1 conversion driver for D2C ecommerce. But it must be economically viable.

| Scenario | Threshold | Margin Impact | Conversion Lift |
|----------|-----------|---------------|-----------------|
| **No free shipping** | N/A | Full margin | Baseline |
| **Free shipping over $49** | $49 | -$5-8 per qualifying order | +15-25% conversion |
| **Free shipping over $75** | $75 | -$5-8 per qualifying order | +10-15% conversion (less impactful) |
| **Free shipping on all orders** | $0 | -$5-8 on EVERY order | +25-35% conversion but margin risk |
| **Free shipping for subscribers** | Subscription | -$5-8 per subscription order | Strong subscription conversion driver |

### IonWave Recommendation

| Customer Type | Shipping Policy | Rationale |
|---------------|----------------|-----------|
| **Subscribers** | Free shipping always | Subscription incentive. Absorb $5-8 into margin. |
| **One-time, 1 box** | $5.99 flat rate | Covers most of carrier cost |
| **One-time, 2+ boxes (>$75)** | Free shipping | Encourages multi-unit purchase. AOV increase offsets shipping cost. |
| **Cart recovery (M18 AC3)** | Free shipping auto-applied | Per M18: no code, auto-apply. Converts 15-20% better than discount codes. |

**Break-even analysis**:
- IonWave one-time price: ~$49
- Gross margin at $49: ~$29 (60% after $20 COGS)
- Shipping cost: ~$6 average
- Gross margin after free shipping: ~$23 (47%)
- Still viable, but narrows. Only offer free shipping where the conversion lift justifies it.

[Confidence: B | Source: D2C free shipping economics, M10 pricing, M25 COGS]

---

## 6. Returns & Exchanges

### Return Policy

For supplement brands, returns are tricky because opened product can't be resold. IonWave's policy:

| Scenario | Policy | Action |
|----------|--------|--------|
| **Unopened, within 30 days** | Full refund. Customer pays return shipping. | Inspect and restock at 3PL. |
| **Opened, within 30 days** | Full refund. No return required. | Destroy. Customer goodwill > product cost. |
| **Opened, after 30 days** | No refund. Offer discount on next order. | Support handles diplomatically. |
| **Damaged in transit** | Full replacement. No return required. | See Damaged Protocol in 3pl_and_fulfillment.md. |
| **Wrong product shipped** | Full replacement + apology. Return label provided. | 3PL error → escalate to SLA review. |
| **Subscription cancellation** | Refund if product hasn't shipped. No refund after shipment. | Per M21 subscription terms. |

### Return Processing SOP

1. Customer contacts support (email/chat)
2. Support determines reason and applies policy above
3. If return needed: generate return label in Shopify → email to customer
4. Product returned to 3PL → inspect → restock (if sealed) or destroy (if opened)
5. Refund processed within 3-5 business days of receipt
6. Log return reason in tracking sheet

### Return Rate Benchmark

| Category | Industry Average | IonWave Target |
|----------|-----------------|----------------|
| D2C Supplement | 3-5% | <5% |
| Subscription (cancel + return) | 5-8% | <5% |
| Amazon (for comparison) | 8-12% | N/A |

**High return rate warning**: If return rate exceeds 5%, investigate: product quality issue? Expectation mismatch (packaging vs reality)? Buyer's remorse (pricing too high)? Address root cause, not symptoms.

### Returns Processing Cost at 3PL (U12)

Returns at a 3PL incur processing fees:

| Fee | Typical Cost |
|-----|-------------|
| Return receiving | $2-5 per return |
| Inspection/restock | $1-3 per return |
| Destruction (if opened) | $0.50-1.00 per unit |
| **Total per return** | **$3.50-9.00** |

**Monthly cost projection**:
| Volume | Return Rate (5%) | Monthly Returns | Monthly Cost |
|--------|-----------------|----------------|-------------|
| 200 orders/mo | 10 | 10 | $35-90 |
| 500 orders/mo | 25 | 25 | $88-225 |
| 1,000 orders/mo | 50 | 50 | $175-450 |

Factor return processing fees into all-in fulfillment cost calculations. [Confidence: C | Source: 3PL return processing fee ranges]

[Confidence: C | Source: D2C supplement return benchmarks]

---

## 7. Free Shipping Cost at Scale (U18)

Free shipping is a conversion driver but becomes a significant cost as you scale:

| Monthly Orders | Sub Rate | Free Ship Orders | Monthly Cost (@$6/order) | Annual Cost | % of Revenue |
|---------------|----------|-----------------|------------------------|-------------|-------------|
| 200 | 40% | ~120 | $720 | $8,640 | ~4% |
| 500 | 40% | ~300 | $1,800 | $21,600 | ~5% |
| 1,000 | 40% | ~600 | $3,600 | $43,200 | ~5.5% |
| 2,000 | 40% | ~1,200 | $7,200 | $86,400 | ~6% |

*Assumes: subscribers = free shipping, one-time over threshold = free shipping (~50% of one-time orders qualify)*

**Trigger**: If free shipping cost exceeds **8% of revenue**, take action:
1. Renegotiate carrier rates (volume leverage)
2. Adjust free shipping threshold upward ($49 → $59)
3. Optimize packaging to reduce DIM weight
4. Evaluate subscription-only free shipping (remove from one-time)

---

## 8. Cross-TUP References

- **M28 expansion_paths.md**: International expansion triggers ($50K MRR for Canada, $100K for UK, $250K for other). Expansion sequence: D2C → Amazon → B2B → International.
- **M9 operations_governance.md**: File structure includes 3PL/ folder for contracts, SOPs, SLAs and Inventory/ folder for counts and reorder triggers.
- **M10 pricing_and_offers.md**: Free shipping threshold economics. Subscription pricing must absorb shipping cost.
- **M18 cart_recovery.md**: AC3 free shipping auto-applied for cart recovery.
- **M21 subscriptions.md**: Subscription terms, cancellation policy, refund policy alignment.
- **M25 bookkeeping_setup.md**: Shipping revenue (4020) vs outbound shipping expense (6120) accounting treatment.

---

*International expansion is a later-stage play. Master US fulfillment first. When the time comes, enter Canada cross-border, then UK with a local 3PL. See `inventory_management.md` for forecasting and `3pl_and_fulfillment.md` for provider details.*


---

### 📄 inventory_management.md

# M24: Inventory Management — Forecasting, Reorder Points, Seasonal Planning

**TUP**: M24 — Fulfillment & Inventory
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 526, 527, 528; M10 pricing_and_offers.md; M25 bookkeeping_setup.md; M19 customer_lifecycle.md

---

## 1. Inventory Forecasting Framework

### The Core Formula

```
Reorder Point = (Daily Sales Rate × Lead Time in Days) + Safety Stock
```

This formula drives everything. Get the inputs right, and you'll never stock out or overstock.

| Variable | How to Calculate | Early-Stage Source | Mature Source |
|----------|-----------------|-------------------|---------------|
| **Daily Sales Rate** | Total units sold ÷ days in period | First 14 days of sales data | 30-day rolling average |
| **Lead Time** | Days from PO to inventory available at fulfillment location | Manufacturer quote + freight time + receiving | Tracked historical average |
| **Safety Stock** | Buffer for demand variability and supply variability | Fixed 14-day buffer | Calculated: Z × σ × √(lead time) |

### IonWave-Specific Variables

| Variable | Launch Estimate | Notes |
|----------|----------------|-------|
| Daily sales (conservative) | 5 units/day | ~150/month |
| Daily sales (moderate) | 15 units/day | ~450/month |
| Daily sales (optimistic) | 30 units/day | ~900/month |
| Manufacturing lead time | 21-28 days | Biocean or equivalent CM lead time |
| Freight to 3PL | 5-7 days | Domestic ground from CM to warehouse |
| 3PL receiving | 2-3 days | Inbound processing at warehouse |
| **Total lead time** | **28-38 days** | Manufacture + ship + receive |
| Safety stock | 14 days of sales | Conservative buffer for a new brand |

[Confidence: B for lead time estimates | Source: Supplement CM industry averages]

### Reorder Scenario Calculator

| Scenario | Daily Sales | Lead Time | Safety Stock (14 days) | Reorder Point |
|----------|-------------|-----------|----------------------|---------------|
| **Conservative** | 5/day | 35 days | 70 units | **245 units** |
| **Growing** | 15/day | 35 days | 210 units | **735 units** |
| **Scaling** | 30/day | 35 days | 420 units | **1,470 units** |
| **Hyper-Growth** | 50/day | 35 days | 700 units | **2,450 units** |

**Order quantity**: When you hit the reorder point, how much do you order?

```
Order Quantity = (Daily Sales Rate × Days Until Next Order) + Safety Stock Top-Up
```

For early-stage IonWave, order in 30-day supply batches at minimum. This keeps per-unit cost down (manufacturer MOQs) and provides buffer.

### Manufacturing MOQ Analysis (U4)

Contract manufacturers have minimum order quantities (MOQs) that create a cash trap for early-stage brands:

| CM MOQ | At 5 units/day (150/mo) | Cash Commitment ($20/unit) | Months of Stock |
|--------|------------------------|---------------------------|-----------------|
| 500 units | 3.3 months supply | $10,000 | 3.3 |
| 1,000 units | 6.7 months supply | $20,000 | 6.7 |
| 2,000 units | 13.3 months supply | $40,000 | 13.3 |

**Solution**: Negotiate lower MOQ for first 2-3 POs. Many CMs will do 500-unit runs for new brands at a 10-15% per-unit premium. Worth it to preserve cash.

**Cash rule**: First PO should not exceed 25% of available cash reserves. [Confidence: A | Source: Supplement CM industry practices]

### First Purchase Order Decision Framework (U13)

The first PO (before any sales data) is the hardest inventory decision:

```
First PO = (Conservative Monthly Forecast × 3 months) + Safety Stock
         = (150 × 3) + 70 = 520 units (conservative)
```

But check against CM MOQ:
- If MOQ = 500 → order 520 (just above MOQ) ✓
- If MOQ = 1,000 → order 1,000 but plan for 6+ months of stock (cash trap risk)
- If MOQ = 2,000 → negotiate down or find different CM

| Decision Factor | Consideration |
|----------------|---------------|
| Cash available | First PO ≤ 25% of cash reserves |
| CM MOQ | Negotiate for lowest possible first order |
| Shelf life | Verify ≥18 months expiration on first batch (U15) |
| Storage cost | 1,000+ units at 3PL = $40+/month in storage before revenue |

**Expiration risk (U15)**: Track months-of-stock vs months-to-expiration for each lot. If months-of-stock > (months-to-expiration − 6), reduce next PO. Never accept inventory with <12 months remaining shelf life.

[Confidence: A | Source: Pre-revenue inventory planning frameworks]

### Statistical Safety Stock (U5)

Evolve from flat buffer to data-driven safety stock:

| Phase | Method | Formula |
|-------|--------|---------|
| **Days 0-60** | Flat 14-day buffer | SS = Daily Rate × 14 |
| **Days 60+** | Statistical | SS = Z × σ_demand × √(lead_time_days) |

Where:
- Z = 1.65 for 95% service level (recommended for IonWave)
- σ_demand = standard deviation of daily sales (trailing 30 days)
- This prevents over-stocking (if demand stabilizes) and under-stocking (if volatile)

[Confidence: B | Source: Inventory management statistical methods]

---

## 2. Subscription vs One-Time Inventory Forecasting

This is the critical gap in Danilo's source material. IonWave is a subscription-first brand, which means inventory forecasting must account for two distinct demand streams.

### Two-Stream Demand Model

```
Total Daily Demand = Subscription Demand + One-Time Demand + Growth Buffer

Subscription Demand = Active Subscribers × (1 - Churn Rate) × Units Per Order
One-Time Demand = (New One-Time Orders Per Day) × Units Per Order
Growth Buffer = Total × Growth Rate Multiplier
```

### Subscription Forecasting (Predictable Demand)

Subscription orders are the easiest to forecast because they repeat on a fixed schedule:

| Input | Source | Calculation |
|-------|--------|-------------|
| Active subscribers | Recharge/Skio dashboard | Count of active subscriptions |
| Billing cycle | Shopify/Recharge settings | 30 days for IonWave (monthly supply) |
| Units per subscription | Product config | 1 box per subscription (30 sachets) |
| Churn rate (monthly) | M19 lifecycle analytics | Start at 15% estimate, refine with data |
| Skip/pause rate | Recharge analytics | Budget 5-10% per cycle |

**Monthly subscription inventory need**:
```
Subscription Units = Active Subscribers × (1 - Monthly Churn) × (1 - Skip Rate) × Units Per Order
```

Example at Month 3:
- 200 active subscribers
- 12% monthly churn (M19 estimate)
- 7% skip rate
- 1 box per order

```
= 200 × 0.88 × 0.93 × 1 = 164 units for subscription renewals
```

### One-Time Forecasting (Variable Demand)

One-time orders are harder to predict. They depend on ad spend, seasonality, and conversion rate:

| Input | Source | Variability |
|-------|--------|------------|
| Daily ad spend | Media buying budget (M13) | Can change daily |
| Conversion rate | GA4 / Shopify | 1-3% typical for supplement |
| Average units per order | Shopify analytics | Usually 1.0-1.3 for single-SKU |
| Organic/email orders | Attribution model (M30) | Grows over time |

**Monthly one-time inventory need**:
```
One-Time Units = (Ad Spend / CPA) × Avg Units Per Order × (1 + Organic Multiplier)
```

### Ad Spend → Inventory Demand Linkage (U22)

Marketing and inventory are NOT independent domains:
- When marketing increases ad spend by 50%+, inventory team must be notified **2 weeks in advance**
- Demand multiplier: if ad spend increases X%, expect unit demand increase of **0.6-0.8X%** (not 1:1 due to diminishing returns)
- **Inventory gate**: If inventory is in CAUTION or REORDER zone, marketing should NOT scale ad spend until replenished
- Add this as a standing item in weekly ops sync

### Subscription Cohort Decay Model (U6)

> **Flat churn rates are misleading.** Subscription churn is NOT uniform — Month 2 churn is highest (20-30%), then drops to 8-12% by Month 6+.

Apply cohort-based decay to each month's new subscriber cohort:

| Month Since Signup | Retention Rate | Cumulative Retention |
|-------------------|---------------|---------------------|
| Month 1 → 2 | 80% | 80% |
| Month 2 → 3 | 85% | 68% |
| Month 3 → 4 | 88% | 60% |
| Month 4 → 5 | 90% | 54% |
| Month 5 → 6 | 92% | 50% |
| Month 6+ | 93%+ | Stabilizing |

This produces a more accurate (and usually lower) inventory forecast than a flat 12% churn rate. [Confidence: B | Source: DTC subscription cohort benchmarks, M19 lifecycle data]

### Subscription Renewal Clustering Warning (U14)

At launch, most subscribers sign up within the same week, so they all renew within the same 5-day window:

- **Months 1-3**: Expect 70%+ of subscription renewals clustered in a 5-day window
- **Plan inventory**: Ensure enough stock is available for the renewal cluster, not spread evenly across the month
- **After Month 6**: Renewals naturally distribute more evenly as acquisition spreads out
- **If Recharge/Skio supports billing date spreading**: Consider enabling it after Month 3 to smooth demand

### Combined Forecast Template

| Month | Sub Renewals | New Subs | One-Time | **Total Units** | On Hand | Gap |
|-------|-------------|----------|----------|-----------------|---------|-----|
| Month 1 | 0 | 80 | 70 | **150** | [X] | [ ] |
| Month 2 | 64 | 100 | 80 | **244** | [X] | [ ] |
| Month 3 | 131 | 120 | 90 | **341** | [X] | [ ] |
| Month 4 | 204 | 100 | 85 | **389** | [X] | [ ] |
| Month 5 | 260 | 100 | 85 | **445** | [X] | [ ] |
| Month 6 | 310 | 100 | 85 | **495** | [X] | [ ] |

*Assumptions: 40% subscription rate, 12% monthly churn, 7% skip rate, moderate growth*

[Confidence: C | Source: Subscription demand modeling frameworks + M19 churn estimates]

---

## 3. Real-Time Inventory Dashboard

### Inventory Position (Check Daily)

| Metric | Value | Where to Find |
|--------|-------|--------------|
| **On Hand (at 3PL)** | [X] units | 3PL dashboard / Shopify inventory |
| **In Transit (to 3PL)** | [X] units, ETA: [Date] | Shipping tracking |
| **On Order (manufacturing)** | [X] units, ETA: [Date] | CM purchase order |
| **Committed (open orders)** | [X] units | Shopify unfulfilled orders |
| **Available to Sell** | = On Hand - Committed | Calculated |
| **Daily Sell Rate (14-day avg)** | [X] units/day | Shopify analytics |
| **Days of Stock Remaining** | = Available / Daily Rate | Calculated |
| **Reorder Point** | [X] units | From scenario calculator |
| **Status** | SAFE / CAUTION / REORDER NOW | Calculated |

### Stock Status Thresholds

| Status | Condition | Action |
|--------|-----------|--------|
| **🟢 SAFE** | Days of stock > Reorder Point + 14 | No action needed |
| **🟡 CAUTION** | Days of stock ≤ Reorder Point + 14 | Begin preparing PO with manufacturer |
| **🔴 REORDER NOW** | Days of stock ≤ Reorder Point | Place PO immediately |
| **⚫ STOCKOUT RISK** | Days of stock ≤ Lead Time | Emergency: expedite shipping, reduce ad spend, notify customers |

### Stockout Prevention Protocol

If you enter ⚫ STOCKOUT RISK:

1. **Immediately**: Reduce ad spend by 50% to slow new customer acquisition
2. **Same day**: Contact manufacturer about expedited production (expect premium pricing)
3. **Same day**: Contact 3PL about expedited inbound receiving
4. **If stockout is imminent**: Turn off ads completely. Switch site to "pre-order" mode. Email existing subscribers with transparency: "Your next box may arrive 3-5 days late. We're scaling production to meet demand."
5. **Never**: Silently charge and not ship. This creates chargebacks (M20 existential risk: Stripe 0.75% threshold).

### Overstock Warning

Overstock is as dangerous as stockout for a cash-constrained startup:

| Warning Sign | Threshold | Action |
|-------------|-----------|--------|
| Days of stock >90 | With stable/declining sales | Reduce next PO by 30% |
| Expiration approaching | <90 days to expiration on any lot | Run flash sale, bundle, or donate |
| Cash tied in inventory | >40% of cash reserves in inventory | Reduce PO frequency |

**Cash impact**: At $20 landed cost, 1,000 excess units = $20,000 tied up in inventory. For a pre-revenue startup, this can be a cash flow crisis.

[Confidence: B | Source: Inventory management frameworks + M25 cash flow alignment]

---

## 4. Lot Tracking & Expiration Management

### Why Lot Tracking Matters for Supplements

FDA requires supplement brands to be able to trace any unit back to its production batch. This isn't optional — it's a legal requirement that protects you from liability in a recall scenario.

### Lot Tracking Protocol

| Data Point | What to Record | Where to Record |
|------------|---------------|----------------|
| **Lot number** | Manufacturer-assigned batch ID | 3PL WMS, internal spreadsheet |
| **Production date** | Date lot was manufactured | COA from manufacturer |
| **Expiration date** | Date lot expires (typically 24-36 months from production) | 3PL WMS, Shopify metafield |
| **Quantity received** | Units received in this lot | 3PL receiving report |
| **COA** (Certificate of Analysis) | Lab testing results for this lot | Filed in Ops folder |
| **Storage location** | Which warehouse / shelf position | 3PL WMS |
| **Units shipped** | Running total of units shipped from this lot | 3PL ship log |
| **Units remaining** | Current inventory for this lot | 3PL WMS |

### FEFO (First Expired, First Out) Protocol

**Critical**: Supplements MUST use FEFO, not FIFO. This means the lot closest to expiration ships first, regardless of when it was received.

| Situation | FIFO Result | FEFO Result |
|-----------|-------------|-------------|
| Lot A: 500 units, expires Dec 2027, received Jan 2026 | Ship Lot A first (received first) | Ship Lot A first (expires first) ✓ |
| Lot B: 300 units, expires Sep 2027, received Mar 2026 | Ship Lot A first (received first) ❌ | Ship Lot B first (expires first) ✓ |

FEFO reduces waste from 10-18% to under 3% for supplement brands. Configure this in your 3PL's WMS from Day 1.

### Expiration Alert System

| Alert | Trigger | Action |
|-------|---------|--------|
| **Yellow** | Lot has <6 months to expiration | Monitor. No action needed. |
| **Orange** | Lot has <3 months to expiration | Do NOT accept new inventory of this lot. Prioritize shipping. |
| **Red** | Lot has <30 days to expiration | Quarantine remaining units. Do NOT ship to customers. |
| **Black** | Lot has expired | Destroy or donate (per local regulations). Log write-off in accounting (M25 account 5040). |

### Recall Procedure

If a quality issue is discovered with a specific lot:

| Step | Action | Timeline | Owner |
|------|--------|----------|-------|
| 1 | Identify affected lot number(s) | Immediately | Quality |
| 2 | Quarantine all remaining units of affected lot(s) at 3PL | Within 2 hours | Ops |
| 3 | Pull shipping records: which customers received affected lot? | Within 4 hours | Ops |
| 4 | Determine severity: voluntary recall or mandatory (FDA classification) | Within 24 hours | Founder + Legal |
| 5 | Notify affected customers (email + phone for Class I) | Within 48 hours | Support |
| 6 | Arrange returns or safe disposal instructions | Within 72 hours | Ops |
| 7 | Notify FDA if required (mandatory for Class I, voluntary for Class II/III) | Per FDA timeline | Legal |
| 8 | Root cause analysis with manufacturer | Within 1 week | Quality |
| 9 | Corrective action documented | Within 2 weeks | Quality |

**FDA recall classifications**:
- **Class I**: Serious health risk. Mandatory recall. Requires FDA notification.
- **Class II**: Temporary or reversible health risk. Voluntary recall recommended.
- **Class III**: No health risk, but product doesn't meet specs. Voluntary.

[Confidence: A | Source: FDA 21 CFR Part 111, FDA recall guidance]

---

## 5. Seasonal Planning Calendar

### 2026 Supplement Seasonal Calendar

IonWave's demand is driven by health/wellness seasonality. Key: inventory prep must START 6-8 weeks before the demand peak (manufacturing lead time + safety stock).

| Date | Event | Relevance | Marketing Angle | Inventory Prep | Prep Start |
|------|-------|-----------|----------------|---------------|------------|
| **Jan 1** | New Year | ★★★★★ | Resolution/health campaign. Biggest supplement month. | +50% inventory | Nov 15 |
| Feb 14 | Valentine's Day | ★★ | Gift angle (health for loved one) | Normal | Jan 15 |
| **Apr** | Tax Refund Season | ★★★ | "Invest in yourself" | Normal | Mar 15 |
| **May (2nd Sun)** | Mother's Day | ★★★ | Gift for wellness-focused moms | +20% | Apr 1 |
| **May (last Mon)** | Memorial Day | ★★★ | Summer kickoff sale | +30% | Apr 15 |
| **Jul 4** | Independence Day | ★★★ | Summer hydration push | +30% | Jun 1 |
| **Sep (1st Mon)** | Labor Day | ★★★ | Back-to-routine, end of summer | Normal | Aug 1 |
| **Nov (4th Thu+)** | BFCM Week | ★★★★★ | Biggest sale of year | +100% | Sep 1 |
| **Dec 25** | Christmas | ★★★ | Gift sets, last ship dates | +50% | Oct 1 |
| **Dec 31** | NYE | ★★★★ | Resolution pre-launch | +50% | Nov 1 |

### Quarterly Planning Guide

| Quarter | Demand Trend | Inventory Strategy | Marketing Theme |
|---------|-------------|-------------------|-----------------|
| **Q1 (Jan-Mar)** | HIGHEST — New Year resolutions | Stock heavy. January is peak. Order extra in November. | Health reset, new habits, fresh start |
| **Q2 (Apr-Jun)** | MODERATE — Summer prep | Stable. Build for Memorial Day and July 4. | Outdoor/active, summer body, hydration |
| **Q3 (Jul-Sep)** | MODERATE — Summer + back to school | Stable. Manage summer lull (August). | Routine, hydration, performance |
| **Q4 (Oct-Dec)** | HIGH — BFCM + holidays | Stock HEAVY. BFCM is make-or-break. Order in September. | Gifting, deals, year-end health |

### BFCM Inventory Planning (Critical)

BFCM (Black Friday / Cyber Monday) is the single biggest inventory challenge:

| Timeline | Action |
|----------|--------|
| **Sep 1** | Place PO for BFCM inventory. Target 2x normal monthly volume. |
| **Oct 1** | Inventory received and confirmed at 3PL. Verify lot numbers and expiration dates. |
| **Oct 15** | BFCM promotional plan finalized (M17/M18 alignment). Know exact offers. |
| **Nov 1** | Pre-BFCM campaign begins (email warm-up, early access for subscribers) |
| **Nov 15** | Final inventory audit. If short, expedite from manufacturer. |
| **BFCM Week** | Monitor inventory daily. If approaching stockout, cap orders or end sale early. |
| **Dec 1** | Post-BFCM audit. Reorder for holiday + January surge. |

**BFCM shipping cutoffs**:
- Standard shipping (USPS First Class): Order by Dec 14 for Christmas delivery
- Priority shipping (USPS Priority): Order by Dec 18
- Express shipping (USPS Express): Order by Dec 22
- Communicate cutoffs clearly on site, in emails, and in ads starting Dec 1.

[Confidence: B | Source: Supplement seasonal data, shipping carrier 2026 cutoff projections]

---

## 6. Inventory Financial Integration

### How Inventory Hits the Books (M25 Alignment)

| Event | Accounting Treatment | Account |
|-------|---------------------|---------|
| Purchase inventory from CM | Asset: Inventory (Balance Sheet) | 1300 Inventory |
| Freight from CM to 3PL | Capitalize into inventory cost (COGS-Freight In) | 5030 COGS — Freight In |
| Customer order ships | COGS recognized (matches revenue) | 5000/5010 COGS — Product |
| 3PL fees charged | Operating expense | 6110 3PL/Fulfillment Fees |
| Outbound shipping cost | Operating expense | 6120 Outbound Shipping |
| Inventory expires/destroyed | Write-off (COGS loss) | 5040 Loss on Expired Inventory |
| Inventory count discrepancy | Shrinkage (COGS or expense) | 5040 or 6900 |

**Key principle**: Inventory is an ASSET until sold. COGS is recognized when the product ships to a customer, not when you buy it from the manufacturer. This matters for cash flow planning — you pay cash up front but don't see the expense until later.

### Landed Cost Calculation (Per Unit)

| Component | Cost | Source |
|-----------|------|--------|
| Product cost (from CM) | $14-16 | Biocean/CM quote |
| Third-party testing (COA) | $0.50-1.50 | Per batch, amortized per unit |
| Freight to 3PL | $1.00-2.00 | Ground shipping, per unit |
| Packaging (box, insert, sachet wrapping) | $2.00-3.00 | Packaging supplier |
| **Total Landed Cost** | **$17.50-22.50** | **M25 uses $20 as baseline** |

[Confidence: B | Source: M25 bookkeeping_setup.md, HYP-004 unit economics]

---

## 7. Performance Targets

| Metric | Phase 0 (Month 1-2) | Phase 1 (Month 3-6) | Phase 2 (Month 7+) |
|--------|---------------------|---------------------|---------------------|
| Ship within 48hr | >90% (self-fulfill) | >95% (3PL) | >98% |
| Order accuracy | >99% | >99% | >99.5% |
| Damage rate | <2% | <1% | <0.5% |
| Inventory accuracy | >95% | >99% | >99.5% |
| Stockout incidents | 0 | 0 | 0 |
| Days of stock remaining | >30 | >45 | >60 |
| Fulfillment cost per order | <$8 (self) | <$12 (3PL all-in) | <$10 (optimized) |
| **Inventory turnover (U26)** | N/A (too early) | 6-8x/year | 6-8x/year |

### Inventory Turnover Ratio (U26)

```
Inventory Turnover = Annual COGS / Average Inventory Value
```

| Turnover Rate | Interpretation | Action |
|--------------|---------------|--------|
| <4x/year | Too much cash tied in inventory | Investigate overordering. Reduce next PO. |
| **6-8x/year** | **Healthy for supplement brand** | **Target range** |
| >12x/year | Running too lean | Stockout risk increasing. Increase safety stock. |

Track monthly starting Month 3 (need at least 90 days of data for meaningful ratio).

---

## 8. Dead Stock Liquidation Protocol (U21)

If any lot has >120 days of stock remaining AND is approaching the 6-month expiration window:

| Priority | Option | When to Use |
|----------|--------|-------------|
| 1 | **Flash sale** (20-30% off, email blast to non-subscribers) | Lot value >$500, >90 days to expiration |
| 2 | **Bundle** (buy 2 get 1 free) | Accelerate sell-through of slow lot |
| 3 | **Subscription upgrade** (gift free box to subscribers who refer) | Aligns with M22 referral program |
| 4 | **Donate** to health-focused charity | Tax deduction + brand goodwill |
| 5 | **Destroy and write off** | Last resort. M25 account 5040. |

**Decision rule**: If lot value <$500, choose fastest option. If >$500, prioritize margin recovery.

---

*Inventory management is the bridge between marketing and customer experience. Forecast accurately, reorder early, and never stock out. See `3pl_and_fulfillment.md` for provider details and `international_and_scaling.md` for growth milestones.*


---

### 📄 launch_operations.md

# M24: Launch Operations — War Room, 72-Hour Protocol, First 10 Orders

**TUP**: M24 — Fulfillment & Inventory
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 523, 524, 525; M9 store_setup_and_launch.md; M30 analytics_dashboards.md

---

## 1. Launch Day War Room

### The Philosophy

Launch day is a controlled experiment, not a celebration. Every minute matters. The war room protocol ensures every system is monitored, every order is tracked, and every problem is caught before the customer notices.

**Who's in the war room**: At IonWave's scale, the "war room" is Nilo + any active collaborator monitoring a shared Slack/Discord channel. No physical room needed — just phones on, notifications on, response time <15 minutes.

### Pre-Launch Checklist (T-24 to T-0)

| Time | Task | Verification | Owner |
|------|------|-------------|-------|
| **T-48** | Pre-launch inventory audit | Physical count matches Shopify. Lot numbers logged. | Ops |
| **T-24** | Final inventory check (at 3PL or self-storage) | Units available = planned launch quantity | Ops |
| **T-24** | Test complete customer journey (browse → cart → checkout → order confirmation) | Order appears in Shopify + triggers fulfillment | Founder |
| **T-24** | Verify email flows armed and live (M18 alignment) | Welcome, order confirm, shipping confirm all trigger | Ops |
| **T-12** | Verify all tracking pixels firing (Meta, GA4, Klaviyo) | Use pixel helper extensions. Check Events Manager. | Ops |
| **T-12** | Confirm ad creatives approved in Meta/Google | All ads in "Active" status, not "In Review" | Founder |
| **T-6** | Confirm payment processing active (Shopify Payments + PayPal) | Test transaction $1 → refund | Ops |
| **T-6** | Confirm discount codes active (if applicable) | Test code → verify discount applies at checkout | Ops |
| **T-2** | Alert team: launch imminent. Everyone on phones. | Confirmation from all war room contacts | Founder |
| **T-1** | Final go/no-go decision | All T-24 through T-2 checks GREEN | Founder |

### Go/No-Go Decision Matrix

| Check | GREEN (Go) | RED (No-Go) |
|-------|-----------|-------------|
| Inventory | Available and confirmed | Inventory discrepancy >5% |
| Payment processing | Test transaction successful | Payment processor issue |
| Email flows | All flows tested and live | Welcome or order confirm not firing |
| Tracking pixels | All pixels verified | Meta pixel not firing (can't measure ROAS) |
| Ads | All approved and ready | Primary ads still in review |
| 3PL/Fulfillment | Ready to process orders | 3PL not onboarded or integration broken |
| Website | Load time <3s, checkout works | Checkout errors or site down |

**Rule**: If ANY check is RED, delay launch until fixed. There are no partial launches. A broken checkout or unfiring pixel on Day 1 wastes the most expensive traffic you'll ever buy.

### Launch Abort & Restart Protocol (U7)

If a go/no-go check is RED and launch is aborted:

1. **Communicate immediately**: Email/message any early-access or waitlist members: "We're putting the finishing touches on IonWave. Launch is coming soon — we want to make sure everything is perfect."
2. **Do NOT rush**: Minimum 48 hours between abort and next go/no-go attempt
3. **Reset all checks**: Re-verify ALL T-48 through T-1 checks, not just the failed one (cascading failures are common)
4. **Document**: Log what caused the abort, who caught it, and the fix applied
5. **Re-clear**: Fresh go/no-go decision with all checks GREEN before proceeding

[Confidence: A | Source: D2C launch protocols]

### Soft Launch Protocol — Friends & Family (U8)

**Do NOT go straight from checklist to paid traffic.** Run a soft launch first:

| Day | Action | Purpose |
|-----|--------|---------|
| **T-3** | Open store to a hand-picked list (10-20 people: friends, family, beta testers) | Smoke-test the system with friendly users |
| **T-3 to T-1** | They place real orders, go through real checkout, receive real product | Catch payment, fulfillment, email, and tracking issues before they cost money |
| **T-1** | Fix any issues discovered during soft launch | |
| **T-0** | Hard launch with ads (only after soft launch is clean) | |

**Who to include**: People who will honestly report problems, not just say "looks great." Ideal: 5 family/friends + 5 people who match the ICP (health-focused, willing to give candid feedback).

**What to verify from soft launch orders**:
- Payment processed correctly
- Order confirmation email received
- Fulfillment triggered (3PL or self-pack)
- Tracking email sent and updates correctly
- Product arrives in good condition with correct packaging
- Post-purchase email flow begins (M18 Welcome Track B)

[Confidence: B | Source: D2C launch best practices]

### Launch Sequence (T-0 Forward)

| Time | Action | What to Monitor | Escalation Trigger |
|------|--------|----------------|-------------------|
| **T+0** | Turn on ads (Meta first, Google second) | Ad status = "Active" | Ad rejected → review creative, resubmit |
| **T+5m** | Verify ads are serving impressions | Impressions >0 in Ads Manager | Zero impressions after 10 min → check targeting, budget |
| **T+15m** | Check first impressions and reach | CPM within expected range ($15-40 for supplement) | CPM >$60 → pause, review audience |
| **T+30m** | Monitor CTR on ads | CTR >0.8% | CTR <0.5% → creative problem. Swap creative. |
| **T+1hr** | Check first site visits | GA4 real-time shows traffic from ads | Zero site traffic → tracking issue or ad serving issue |
| **T+1hr** | Check add-to-cart events | Any ATC events in GA4/Meta? | Zero ATC after 100+ visits → landing page problem |
| **T+2hr** | Check for first orders | Any orders in Shopify? | Zero orders after 200+ visits → checkout problem or pricing |
| **T+4hr** | Verify fulfillment triggered | First orders showing in 3PL/packing queue | Orders stuck in Shopify → integration issue |
| **T+4hr** | Verify order confirmation emails sent | Klaviyo shows email delivered | Emails not sending → Klaviyo trigger check |
| **T+8hr** | Mid-day performance review | Revenue, orders, CAC, MER (M30 alignment) | CAC >$75 → concern. CAC >$100 → consider pausing. |
| **T+12hr** | End of Day 1 report | Full day metrics logged | — |

### War Room Contact Sheet

| Role | Name | Phone | Backup |
|------|------|-------|--------|
| Founder / Decision Maker | [Nilo] | [Phone] | — |
| Ops / Technical | [TBD] | [Phone] | [Email] |
| 3PL Emergency | [3PL account manager] | [Phone] | [Support email] |
| Shopify Support | — | — | support@shopify.com |
| Payment Processor | — | — | [Stripe/Shopify Payments support] |

**Communication cadence**: Update Slack/Discord channel at T+1hr, T+4hr, T+8hr, T+12hr minimum. More often if issues arise. All data goes in one channel — no DMs.

### Day 1 Ad Budget Cap (U9)

**Hard cap Day 1 spend: $100-200.** Enough to validate, not enough to bleed.

| Day | Max Spend | Condition to Increase |
|-----|-----------|----------------------|
| Day 1 | $100-200 | Do NOT increase regardless of results |
| Day 2 | 1.5x Day 1 ($150-300) | Only if Day 1 metrics are GREEN |
| Day 3 | 2x Day 1 ($200-400) | Only if Day 1+2 metrics are GREEN |

**Why cap Day 1**: "Everything looks great for 2 hours, spend $500, then discover tracking was broken" is the #1 launch day money-burning scenario. Cap prevents this. Verify data quality before scaling.

### Site Down Emergency Protocol (U16)

| Scenario | Diagnosis | Action | Timeline |
|----------|-----------|--------|----------|
| **Shopify platform down** | Check status.shopify.com | Wait. Pause all ads immediately. | <5 min to pause ads |
| **Your store specifically down** | Disable third-party apps one by one | Identify conflicting app. Contact Shopify support. | <15 min |
| **Checkout broken but site up** | Test checkout from guest browser | Switch to "password" page. Pause all ads. Fix before resuming. | <5 min to pause |
| **Payment processor down** | Test with alternate card/method | Switch to backup processor. If none, pause ads. | <10 min |

**Rule**: Every minute of paid traffic to a broken site is burned money. Speed of ad pausing is critical.

### Founder Energy Management (U27)

Launch week is a marathon, not a sprint:
- **Sleep**: Minimum 6 hours per night. Non-negotiable. Bad decisions from Day 2 fatigue cost more than missed monitoring.
- **Meals**: Pre-prepare or order. Don't skip meals to watch dashboards.
- **Offline window**: 1 hour completely offline per day. Delegate monitoring to a trusted person during this window.
- **DND with exceptions**: Phone on Do Not Disturb with exceptions only for war room contacts.

[Confidence: B | Source: D2C launch protocols, M9 launch checklist alignment]

---

## 2. Post-Launch 72-Hour Protocol

### The Three Phases

The first 72 hours determine whether your launch is a signal or a fluke. Monitor aggressively, but don't over-react. Give each ad and channel at least $50-100 of spend before making kill decisions.

### Phase 1: Survival Mode (Hour 0-24)

**Monitoring cadence**: Every 2 hours during waking hours

| Check | Target | Data Source |
|-------|--------|-------------|
| Ads serving | Impressions >0, no rejections | Meta Ads Manager, Google Ads |
| Orders processing | All orders in "Fulfilled" or "Unfulfilled" (not stuck) | Shopify Orders |
| No checkout errors | Error rate = 0% | Shopify Analytics → Live View |
| Payment processing | All payments captured | Shopify Payments dashboard |
| Email flows firing | Welcome + order confirm delivered | Klaviyo flow analytics |
| Site performance | Load time <3s | Google PageSpeed / Shopify Analytics |

**Critical Hour 0-24 metrics**:

| Metric | Target | Source | Note |
|--------|--------|--------|------|
| CTR (ads) | >1% | Meta/Google Ads | Below 0.5% = creative problem |
| CPC | <$2.00 | Meta/Google Ads | Supplement vertical avg $1.50-2.50 |
| Any purchases | >0 | Shopify | Even 1 purchase = system works |
| Fulfillment | 100% of orders processed | 3PL/Self-fulfill | Any stuck order = investigate immediately |

**Red flags requiring immediate action**:
- Ad rejected → Review and resubmit. Don't launch new creative — fix the flagged one.
- Checkout broken → Take site to "password" mode if necessary. Fix before any more traffic.
- Tracking not firing → Pause ads. Fix tracking. Do NOT burn money on unmeasured traffic.
- 3PL not processing → Switch to self-fulfill temporarily. Escalate to 3PL immediately.

### Phase 2: Stabilize (Hour 24-48)

**Monitoring cadence**: Every 4 hours

| Check | Target | Action |
|-------|--------|--------|
| Performance trends | Metrics improving or stable (not declining) | If declining, investigate before spending more |
| Ad kill decisions | Kill any ad set with MER <0.5x after $50 spend | Per M30: MER is the north star, not platform ROAS |
| First orders shipped | Verify first orders shipped from 3PL | Check tracking numbers sync to Shopify |
| Customer support | Respond to any tickets within 4 hours (M20 SLA) | Log all questions — they're product/site feedback |
| Subscription rate | Track what % of orders are subscription | Target: >40% subscription at launch (per M10) |

**Key decision at Hour 48**: Are we seeing signal?

| Signal | Interpretation | Action |
|--------|---------------|--------|
| Orders >10, CAC <$50, some subs | Strong signal | Increase budget 20% on winning ad sets |
| Orders 5-10, CAC $50-75 | Moderate signal | Hold budget. Optimize creatives and audiences. |
| Orders <5, CAC >$75 | Weak signal | Review: landing page, offer, audience, creative. Do NOT scale. |
| Zero orders | No signal | Pause ads. Full audit: checkout, tracking, offer, targeting. |

### Phase 3: Optimize (Hour 48-72)

**Monitoring cadence**: 3x daily (morning, midday, evening)

| Check | Target | Action |
|-------|--------|--------|
| Scale winners | MER >1.5x | Increase budget 20% per day (max) |
| Kill losers | MER <1.0x after $100 spend | Pause. Reallocate budget. |
| Fulfillment audit | All orders from Day 1-2 shipped and tracking | Any delays → escalate |
| Customer feedback | Read every email, DM, review | Log patterns. Feed back to product/site. |
| Document hypotheses | What's working? What's not? Why? | Write in SESSION_LOG or dedicated launch log |

### 72-Hour Launch Scorecard

| Metric | Green | Yellow | Red | Actual |
|--------|-------|--------|-----|--------|
| Total Orders | 15+ | 8-14 | <8 | [ ] |
| Revenue | $500+ | $250-499 | <$250 | [ ] |
| CAC | <$50 | $50-75 | >$75 | [ ] |
| MER | >1.0x | 0.5-1.0x | <0.5x | [ ] |
| Subscription Rate | >40% | 25-40% | <25% | [ ] |
| Fulfillment Rate | 100% | 95-100% | <95% | [ ] |
| Support Response | <4hr | 4-8hr | >8hr | [ ] |
| Pixel/Tracking | All firing | 1 minor issue | Major tracking gap | [ ] |

**Decision at 72 hours**:
- 6+ GREEN → Continue scaling. You have product-market fit signal.
- 4-5 GREEN → Continue but optimize. Focus on RED/YELLOW areas.
- <4 GREEN → Pause and regroup. Don't throw money at a broken funnel.

### Inventory Depletion Tracking (U24)

Add to the 72-hour scorecard:

| Metric | Value | Calculation |
|--------|-------|-------------|
| Units sold (72hr) | [ ] | Shopify orders |
| Sell rate (units/hour) | [ ] | Total units ÷ hours of active selling |
| Days of stock at current rate | [ ] | Available inventory ÷ daily sell rate |
| Stockout risk? | [ ] | If days-of-stock < 30, begin PO immediately |

**Early stockout warning**: If 72-hour sell rate extrapolates to stockout within 30 days, initiate PO with manufacturer immediately. Do not wait for the standard reorder point — ad-driven launch demand can deplete inventory faster than steady-state.

### Post-Launch Retrospective (U17)

Schedule a 1-hour retrospective at Hour 72 or Day 4:

| Question | Notes |
|----------|-------|
| What worked? | [ ] |
| What broke? | [ ] |
| What surprised us? | [ ] |
| What would we do differently? | [ ] |
| Specific action items | [ ] |

**Feed findings to**: M14 (testing hypotheses), M30 (analytics baseline), M20 (support refinements), M24 (fulfillment updates). This becomes the first entry in an ongoing Launch Log.

[Confidence: B | Source: D2C launch benchmarks, M30 MER framework]

---

## 3. First 10 Orders Playbook

### Why First 10 Matter

The first 10 orders are not just sales — they're data. Each order tells you something about who your customer is, how they found you, and whether your system works. Treat them with extreme attention.

### Per-Order Checklist

For each of the first 10 orders, personally verify:

| Check | What to Look For |
|-------|-----------------|
| ☐ Order processed correctly in Shopify | Payment captured, no errors, correct product/variant |
| ☐ Fulfillment triggered (3PL or self) | Order appears in fulfillment queue. Not stuck. |
| ☐ Correct product picked and packed | Right SKU, right quantity, lot number logged |
| ☐ Tracking email sent to customer | Klaviyo or Shopify transactional email delivered |
| ☐ Acquisition channel noted | UTM source → how did they find us? |
| ☐ Product/variant purchased | Which SKU? Any pattern? |
| ☐ Subscription or one-time? | Track ratio from Day 1 |
| ☐ AOV recorded | Higher or lower than projected $49? |
| ☐ Any support questions? | Log every question — they reveal friction |
| ☐ Personal thank-you email sent | Founder writes. Not automated. First 10 only. |
| ☐ Feedback request planted | Ask: "Would you be willing to share your experience after trying IonWave for a week?" |

### First 10 Orders Tracker

| # | Date | Channel | Product | Sub? | AOV | Ship? | Feedback? | Notes |
|---|------|---------|---------|------|-----|-------|-----------|-------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |
| 6 | | | | | | | | |
| 7 | | | | | | | | |
| 8 | | | | | | | | |
| 9 | | | | | | | | |
| 10 | | | | | | | | |

### Founder Thank-You Email (Template)

> Subject: Thank you — personally
>
> Hey {{first_name}},
>
> This is Nilo. I'm the founder of IonWave.
>
> You're one of our very first customers, and I want you to know that means something.
>
> Your order is on its way. When it arrives, tear open a sachet and pour it into a glass of water. That's it. One sachet, every morning. Let the minerals do their work.
>
> If anything is off — the taste, the packaging, the experience — reply to this email. I read everything.
>
> Thank you for taking a chance on us.
>
> — Nilo
>
> P.S. After a week, I'd love to hear how you're feeling. I'll check in.

**Stop sending at**: Order #10. After that, the automated Welcome Track B (M18) takes over. But make notes on what questions people ask — those feed M14 (testing) and M20 (support).

### Learnings Template (Complete After Order #10)

| Question | Answer |
|----------|--------|
| Most common acquisition channel | [ ] |
| Subscription vs one-time ratio | [ ] / [ ] |
| Average order value | $[ ] |
| Most popular product/variant | [ ] |
| Any fulfillment issues? | [ ] |
| Common questions/concerns | [ ] |
| What surprised us? | [ ] |
| Immediate changes needed | [ ] |

**Feed learnings to**:
- M30 Analytics → Update baseline assumptions
- M14 Testing → First optimization hypotheses
- M19 CRM → Customer profile validation
- M13 Media Buying → Channel performance baseline

### First Negative Review Protocol (U23)

The first complaint is inevitable — and it's the most valuable feedback you'll receive:

1. **Founder responds personally within 4 hours.** Not a template. Not a support agent. Nilo.
2. **Do NOT be defensive.** Acknowledge → Apologize → Resolve.
3. **Determine type**:
   - **Systemic** (packaging damaged, product taste off, delivery issue): Escalate immediately. Fix the root cause.
   - **Subjective** (didn't like taste, didn't feel different): Offer full refund, no questions asked. Learn from it.
4. **Log in detail**: Product, lot number, complaint category, resolution, time to resolve
5. **Follow up**: Check back in 1 week. Did the resolution satisfy them?

**Applies to**: Email complaints, social media mentions, review platforms, DMs. Monitor all channels daily during first 30 days.

[Confidence: C | Source: D2C first-customer best practices, Danilo tab 525]

---

## 4. Cross-TUP Launch Alignment

Multiple TUPs have launch day dependencies. This is the integration map:

| TUP | Launch Day Dependency | Status Check |
|-----|----------------------|-------------|
| **M9** | Shopify store live, checkout works, payment processing active | T-24 verification |
| **M13** | Ads approved and ready to activate | T-6 verification |
| **M17/M18** | Email flows armed (welcome, order confirm, shipping confirm) | T-12 verification |
| **M30** | Analytics dashboard live (GA4, Shopify Analytics, ad platforms) | T-24 verification |
| **M20** | Support channels active (email, chat if applicable) | T-12 verification |
| **M24** | Inventory confirmed, fulfillment ready (3PL or self) | T-48 verification |
| **M14** | Pixel tracking verified for future optimization | T-12 verification |

**Critical path for launch**: M9 (store) → M24 (inventory) → M13 (ads) → Launch. If any of these three aren't ready, everything else is moot.

---

*Launch day is a system test, not a celebration. Monitor aggressively for 72 hours, treat every order as a learning opportunity, and don't scale until you see signal. See `3pl_and_fulfillment.md` for fulfillment details and `inventory_management.md` for ongoing inventory operations.*


---

### 📄 opkit_fulfillment_and_inventory.md

# OpKit: Fulfillment & Inventory

**ID**: OK-M24-001
**Source TUP**: M24 — Fulfillment & Inventory
**Version**: 1.0.0
**Date**: 2026-02-09
**Quality**: 8.4/10

---

## Purpose

Build a complete fulfillment and inventory management system for a D2C subscription brand. Covers self-fulfillment at launch, 3PL selection and transition, launch day operations, inventory forecasting (subscription + one-time), lot tracking, seasonal planning, and international scaling milestones.

---

## Instructions (12 Steps)

### Pre-Launch (Week -6 to -2)

1. **Set up self-fulfillment station** — Shipping scale, thermal label printer, packaging materials, branded inserts. Budget ~$200-300 setup. Establish same-day cutoff (e.g., 2 PM ET). Create lot tracking spreadsheet.

2. **Place first purchase order with manufacturer** — Size using conservative 3-month forecast + safety stock. Do NOT exceed 25% of cash reserves. Negotiate lower MOQ for first 2-3 POs if needed. Verify ≥18 months shelf life on batch.

3. **Configure Shopify shipping** — Set shipping rates (free for subscribers, flat rate for one-time, free above threshold). Enable Shopify Shipping discounts. Configure inventory tracking and low-stock alerts.

4. **Begin 3PL evaluation** — Score 3-5 providers on 8-dimension scorecard (supplement compliance, Shopify integration, speed, accuracy, pricing, scalability, service, references). Minimum score: 3.5/5.0 weighted. Verify FDA registration, temperature monitoring, FEFO capability.

### Pre-Launch (Week -1)

5. **Execute soft launch** — Open store to 10-20 hand-picked friends/family/beta testers for 2-3 days. Verify end-to-end: payment → fulfillment → tracking → email flows. Fix issues before hard launch.

6. **Prepare war room** — Complete T-48 through T-1 pre-launch checklist. Set up communication channel (Slack/Discord). Establish go/no-go matrix. Configure Day 1 ad budget cap ($100-200).

### Launch Week

7. **Execute launch day protocol** — Follow war room timeline (T+0 through T+12hr). Monitor ads, orders, fulfillment, email flows, support. Pause ads within 5 minutes of any system failure.

8. **Run 72-hour protocol** — Survival (0-24hr) → Stabilize (24-48hr) → Optimize (48-72hr). Track scorecard metrics. Execute post-launch retrospective at Hour 72.

9. **Run First 10 Orders playbook** — Personally verify each order. Send founder thank-you emails. Track channel, product, subscription rate, AOV. Complete learnings template after order #10.

### Month 2-4

10. **Transition to 3PL** — Sign contract (negotiate 3-month trial, SLA-based exit, surcharge caps). Onboard: product setup, inventory transfer, test orders. Run parallel for 3-7 days. Full cutover after 10+ clean orders.

11. **Establish SLA monitoring** — Weekly scorecard (ship time, accuracy, damage, inventory, tracking). Monthly review. Escalation protocol (notice → warning → review → transition). Monthly mystery order audit.

### Month 4+

12. **Optimize and scale** — Implement statistical safety stock (after 60 days of data). Build subscription cohort decay model. Negotiate carrier rates. Evaluate multi-warehouse when >2,000 orders/month. Plan BFCM inventory 8 weeks in advance.

---

## Grading Rubric

| Grade | Criteria |
|-------|----------|
| **A (9-10)** | All 12 steps complete. 3PL SLAs consistently met. Subscription demand model active. Inventory turnover 6-8x/year. Zero stockouts. International expansion underway. BFCM executed flawlessly. |
| **B (7-8)** | Self-fulfill → 3PL transition complete. SLA monitoring active. Basic inventory forecasting in place. Launch operations executed cleanly. Seasonal planning active. |
| **C (5-6)** | 3PL selected and onboarding in progress. Basic inventory tracking. Launch happened but with some operational issues. No subscription demand model. |
| **D (3-4)** | Self-fulfilling past the 50-order threshold. No 3PL evaluation started. Inventory managed reactively. No lot tracking. |
| **F (0-2)** | No fulfillment system. Shipping inconsistently. No inventory tracking. No lot management. Stockouts or overstocks. |

---

## Scaffold (4 Files)

| File | Contents |
|------|----------|
| `3pl_and_fulfillment.md` | Self-fulfillment setup, 3PL comparison, evaluation scorecard, supplement compliance, contract negotiation, insurance, temperature protocol, onboarding, SLA monitoring, damaged/lost protocol, unboxing, kitting, carrier strategy |
| `launch_operations.md` | War room protocol (T-48 to T+12hr), go/no-go matrix, soft launch protocol, budget caps, site-down emergency, 72-hour protocol (3 phases + scorecard), first 10 orders playbook, retrospective template, first negative review protocol |
| `inventory_management.md` | Forecasting framework (reorder points, safety stock), MOQ analysis, first PO framework, subscription demand modeling (two-stream, cohort decay, renewal clustering), real-time dashboard, lot tracking (FEFO), recall procedure, seasonal calendar, dead stock liquidation |
| `international_and_scaling.md` | US-first strategy, Canada/UK compliance + shipping, scaling milestones (5 stages), multi-warehouse triggers, free shipping economics, returns policy + cost modeling, cost at scale projections |

---

## IonWave Graded Example: 8.4/10

**What IonWave did well**:
- Phase-gated fulfillment strategy (self-fulfill → 3PL → optimized → multi-node) with clear triggers
- Supplement-specific 3PL requirements (FDA registration, temperature, FEFO, lot tracking, recall capability)
- Two-stream demand model (subscription with cohort decay + one-time with ad spend linkage)
- Complete launch operations (soft launch, war room, 72hr protocol, first 10 playbook)
- Contract negotiation guidance with red flags (3-month trial, SLA exit, surcharge caps)
- 27 dialogue upgrades applied (contract, insurance, temperature, MOQ, safety stock, cohort decay, soft launch, budget caps, site-down protocol, etc.)
- Strong cross-TUP integration (M9, M25, M28, M18, M20, M30)

**What could be improved**:
- No Bootstrap source available (green-field build) — some content is benchmark-based rather than primary-sourced
- 3PL pricing needs real-time verification (market changes quarterly)
- CM MOQ and IonWave product stability data are TBD (execution-stage data)
- International compliance (NPN, MHRA) at summary level — needs legal review before execution
- No visual packaging specifications (text-only content)

---

## Adaptation Guide

### For Non-Subscription D2C
- Remove subscription demand forecasting section (§2 subscription portions)
- Remove renewal clustering warning (U14)
- Free shipping threshold economics remain the same
- Replenishment timing reminders shift to email marketing (not inventory system)

### For Multi-SKU Brands
- Add per-SKU reorder point tracking (not just aggregate)
- Kitting becomes more complex — kit configurations multiply
- FEFO applies per SKU independently
- 3PL storage costs scale faster (more pallet positions)
- Seasonal planning varies by product (some SKUs peak summer, others winter)

### For Perishable Products (Shorter Shelf Life)
- Increase FEFO monitoring frequency (weekly → daily)
- Reduce safety stock to prevent expiration waste
- Tighten first PO sizing (90-day supply max, not 180)
- Add cold chain requirements to 3PL evaluation

### For High-Volume Brands (>5,000 orders/month)
- Multi-warehouse is mandatory (not optional)
- Zone-based carrier optimization drives major savings
- Negotiated carrier rates (enterprise contracts) become priority
- Automated reorder with EDI/API integration to manufacturer
- Dedicated inventory analyst role (not founder-managed)

---

## Universal Principles

1. **Self-fulfill first to learn**: You learn more in 30 days of packing boxes than in 6 months of 3PL reports. Switch at 50+ orders/month.
2. **FEFO, not FIFO**: For supplements with expiration dates, First Expired First Out reduces waste from 10-18% to under 3%.
3. **First PO ≤ 25% of cash**: The biggest inventory risk for a startup is overordering pre-revenue. Preserve cash.
4. **Soft launch before hard launch**: 10-20 friendly testers catch system failures before paid traffic.
5. **Day 1 ad budget cap**: $100-200 max. Verify data quality before scaling.
6. **Inventory gates marketing**: If stock is in CAUTION/REORDER zone, do not scale ad spend.
7. **Replace first, investigate later**: For damaged/lost shipments, the customer's experience > $20 product cost.


---

## 🔗 Dependencies & Relationships

### Feeds Into
- _No downstream dependencies_

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

- **IonWave CM exact MOQ**
  - Upgrade Path: Confirm with Biocean/CM during contract negotiation
- **IonWave product temperature stability profile**
  - Upgrade Path: Request stability testing data from manufacturer
- **ShipBob 2026 actual contract terms**
  - Upgrade Path: Verify during 3PL sales process
- **Canada NPN processing time (6-12 months estimate)**
  - Upgrade Path: Confirm with Health Canada or regulatory consultant
- **Recharge/Skio billing date spreading feature**
  - Upgrade Path: Verify during subscription platform setup (M21)

---

## 🎯 Next Actions

_No next actions documented._


---

## 🧰 OpKits

- OK-M24-001

---

---

_Report generated: 2026-02-09 17:49:44_

_Source: `data\m24`_