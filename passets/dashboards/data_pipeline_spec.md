# Data Pipeline Specification — IonWave Dashboards

**Version**: 1.0.0
**Purpose**: Document how data flows from source systems → dashboards
**Audience**: Operator (for setup), Intermediary (for troubleshooting), Future developers
**Status**: Specification (not yet implemented)

---

## Overview

**Problem**: Dashboards need data from 5+ systems (Shopify, Meta, Bank, 3PL, Support). Manually checking each system = 30+ min/day.

**Solution**: Automated data pipeline syncs data daily → populates Google Sheet → powers dashboards.

**Design Principle**: Start simple (Google Apps Script), scale later (custom dashboards at $50K+ MRR).

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     SOURCE SYSTEMS (APIs)                       │
├─────────────────────────────────────────────────────────────────┤
│  Shopify API    Meta API    Bank API    3PL API    Support API │
│  (revenue,      (ad spend,  (balance)   (inventory) (tickets)  │
│   orders)       ROAS)                                           │
└────────┬────────────┬─────────┬──────────┬────────────┬─────────┘
         │            │         │          │            │
         └────────────┴─────────┴──────────┴────────────┘
                              │
                    ┌─────────▼──────────┐
                    │  GOOGLE APPS       │
                    │  SCRIPT            │
                    │  (data sync)       │
                    │  Runs daily 6 AM   │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │  GOOGLE SHEET      │
                    │  (database)        │
                    │  - Daily metrics   │
                    │  - Historical data │
                    └─────────┬──────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
┌────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
│ Daily Pulse     │ │ Weekly Report   │ │ Red Flag        │
│ Dashboard       │ │ Dashboard       │ │ Dashboard       │
│ (daily_pulse.md)│ │ (weekly.md)     │ │ (red_flags.md)  │
└─────────────────┘ └─────────────────┘ └─────────────────┘
         │                    │                    │
         └────────────────────┴────────────────────┘
                              │
                     ┌────────▼─────────┐
                     │  OPERATOR VIEW   │
                     │  (5-min morning  │
                     │   check)         │
                     └──────────────────┘
```

---

## Data Sources Specification

### 1. Shopify (Revenue, Orders, Customers)

**API**: Shopify Admin API (REST + GraphQL)
**Auth**: API key + password (stored in Google Apps Script Properties)
**Docs**: https://shopify.dev/docs/api/admin-rest

**Endpoints Used**:

| Data Needed | Endpoint | Method | Parameters |
|-------------|----------|--------|------------|
| Orders (yesterday) | `/admin/api/2024-01/orders.json` | GET | `created_at_min=[yesterday]&status=any&fields=id,total_price,created_at,customer` |
| Revenue (yesterday) | Calculated from orders | — | Sum `total_price` minus `total_refunds` |
| New Customers | `/admin/api/2024-01/customers.json` | GET | `created_at_min=[yesterday]&fields=id,orders_count` + filter `orders_count=1` |
| AOV | Calculated | — | `total_revenue / total_orders` |

**Rate Limits**: 2 requests/second (Shopify Basic), 4 req/sec (Shopify Plus)
**Error Handling**: If 429 rate limit → wait 500ms, retry up to 3x

**Sample Request** (cURL):
```bash
curl -X GET \
  'https://ionwave.myshopify.com/admin/api/2024-01/orders.json?created_at_min=2026-02-11T00:00:00-05:00&status=any' \
  -H 'X-Shopify-Access-Token: YOUR_TOKEN'
```

**Sample Response**:
```json
{
  "orders": [
    {
      "id": 5001,
      "total_price": "44.95",
      "created_at": "2026-02-11T08:30:00-05:00",
      "customer": {"id": 12345, "orders_count": 1}
    }
  ]
}
```

---

### 2. Meta Ads Manager (Ad Spend, ROAS, CPA)

**API**: Meta Marketing API (Graph API)
**Auth**: OAuth 2.0 access token (90-day expiration, requires refresh)
**Docs**: https://developers.facebook.com/docs/marketing-api

**Endpoints Used**:

| Data Needed | Endpoint | Method | Parameters |
|-------------|----------|--------|------------|
| Ad Account Insights | `/act_{ad_account_id}/insights` | GET | `date_preset=yesterday&fields=spend,purchase_roas,cost_per_action_type,impressions,clicks,ctr` |

**Rate Limits**: 200 API calls/hour per ad account
**Error Handling**: If 80% of limit reached → pause sync, resume in 1 hour

**Sample Request** (cURL):
```bash
curl -X GET \
  'https://graph.facebook.com/v18.0/act_123456789/insights?date_preset=yesterday&fields=spend,purchase_roas,cost_per_action_type,impressions,clicks,ctr&access_token=YOUR_TOKEN'
```

**Sample Response**:
```json
{
  "data": [
    {
      "spend": "412.30",
      "purchase_roas": [{"action_type": "offsite_conversion.fb_pixel_purchase", "value": "3.10"}],
      "cost_per_action_type": [{"action_type": "offsite_conversion.fb_pixel_purchase", "value": "38.45"}],
      "impressions": "42314",
      "clicks": "550",
      "ctr": "1.30"
    }
  ]
}
```

**Important Notes**:
- `purchase_roas` is platform-reported (overstates by 20-40% post-iOS 14.5)
- Use for ad optimization, NOT business-level decisions (use MER instead)
- `cost_per_action_type` with `action_type: offsite_conversion.fb_pixel_purchase` = CPA

---

### 3. Bank / Cash Balance

**Option A: Stripe Treasury API** (if using Stripe for banking)
**API**: Stripe API
**Auth**: API key (secret key, stored in Google Apps Script Properties)
**Docs**: https://stripe.com/docs/api/treasury

**Endpoints Used**:

| Data Needed | Endpoint | Method |
|-------------|----------|--------|
| Account Balance | `/v1/treasury/financial_accounts/{id}` | GET |

**Sample Request**:
```bash
curl https://api.stripe.com/v1/treasury/financial_accounts/fa_xxx \
  -u sk_live_YOUR_SECRET_KEY:
```

**Sample Response**:
```json
{
  "id": "fa_xxx",
  "balance": {
    "cash": {"usd": 3845000}
  }
}
```
Note: Balance in cents, divide by 100 → $38,450.00

---

**Option B: Plaid API** (if using traditional bank)
**API**: Plaid Balance API
**Auth**: Plaid client ID + secret + access token
**Docs**: https://plaid.com/docs/api/products/balance/

**Endpoints Used**:

| Data Needed | Endpoint | Method |
|-------------|----------|--------|
| Account Balance | `/balance/get` | POST |

**Sample Request**:
```bash
curl -X POST https://production.plaid.com/balance/get \
  -H 'Content-Type: application/json' \
  -d '{
    "client_id": "YOUR_CLIENT_ID",
    "secret": "YOUR_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN"
  }'
```

**Sample Response**:
```json
{
  "accounts": [
    {
      "account_id": "xxx",
      "balances": {
        "current": 38450.00
      }
    }
  ]
}
```

---

**Option C: Manual CSV Export** (fallback if API unavailable)
- Download CSV from bank daily
- Upload to Google Drive folder
- Google Apps Script reads CSV and extracts balance
- **Downside**: Requires manual action daily (not fully automated)

---

### 4. 3PL / Inventory

**API**: Varies by 3PL provider (ShipBob, Fulfil, ShipMonk, etc.)
**Example**: ShipBob API
**Docs**: https://developer.shipbob.com/

**Endpoints Used**:

| Data Needed | Endpoint | Method |
|-------------|----------|--------|
| Inventory Levels | `/1.0/inventory` | GET |

**Sample Request**:
```bash
curl -X GET https://api.shipbob.com/1.0/inventory \
  -H 'Authorization: Bearer YOUR_TOKEN'
```

**Sample Response**:
```json
{
  "inventory": [
    {
      "product_id": "12345",
      "name": "IonWave Electrolyte Powder",
      "total_fulfillable_quantity": 420
    }
  ]
}
```

**Calculate Inventory Days**:
```
Inventory Days = total_fulfillable_quantity / avg_daily_units_sold
```
Example: 420 units / 14 units/day = 30 days inventory

**Error Handling**: If API unavailable, use yesterday's value + note "Stale data - check 3PL manually"

---

### 5. Support Platform (Tickets)

**API**: Varies by platform (Gorgias, Zendesk, etc.)
**Example**: Gorgias API
**Docs**: https://developers.gorgias.com/

**Endpoints Used**:

| Data Needed | Endpoint | Method | Parameters |
|-------------|----------|--------|------------|
| Open Tickets | `/api/tickets` | GET | `status=open&created_datetime__gte=[24hrs_ago]` |

**Sample Request**:
```bash
curl -X GET 'https://ionwave.gorgias.com/api/tickets?status=open' \
  -H 'Authorization: Bearer YOUR_TOKEN'
```

**Sample Response**:
```json
{
  "data": [
    {
      "id": 1001,
      "status": "open",
      "created_datetime": "2026-02-11T14:30:00Z"
    }
  ],
  "meta": {"total_count": 3}
}
```

**Calculate Support Backlog**:
- Count tickets with `status=open` AND `created_datetime` > 24 hours ago
- If count >10 → 🟡 Yellow flag
- If count >20 → 🔴 Red flag

---

## Google Apps Script Implementation

### File Structure

```
/passets/dashboards/scripts/
├── daily_sync.gs              ← Main sync script (runs daily at 6 AM)
├── shopify_api.gs              ← Shopify API wrapper functions
├── meta_api.gs                 ← Meta Marketing API wrapper
├── bank_api.gs                 ← Bank/Plaid API wrapper
├── 3pl_api.gs                  ← 3PL inventory API wrapper
├── support_api.gs              ← Support platform API wrapper
├── config.gs                   ← API keys/tokens (uses Properties Service)
└── utils.gs                    ← Helper functions (date formatting, etc.)
```

### Main Sync Script (`daily_sync.gs`)

**Trigger**: Time-driven trigger, daily at 6:00 AM EST

**Pseudo-code**:
```javascript
function dailySync() {
  try {
    // 1. Get yesterday's date
    const yesterday = getYesterday();

    // 2. Fetch Shopify data
    const shopifyData = fetchShopifyMetrics(yesterday);
    // Returns: {revenue, orders, newCustomers, aov}

    // 3. Fetch Meta Ads data
    const metaData = fetchMetaMetrics(yesterday);
    // Returns: {spend, roas, cpa, impressions, ctr}

    // 4. Fetch Bank balance
    const cashBalance = fetchBankBalance();
    // Returns: {balance}

    // 5. Fetch 3PL inventory
    const inventoryData = fetch3PLInventory();
    // Returns: {totalUnits, inventoryDays}

    // 6. Fetch Support tickets
    const supportData = fetchSupportTickets();
    // Returns: {openTickets, backlogCount}

    // 7. Write to Google Sheet
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Daily Metrics');
    const newRow = [
      yesterday,
      shopifyData.revenue,
      shopifyData.orders,
      shopifyData.newCustomers,
      shopifyData.aov,
      metaData.spend,
      metaData.roas,
      metaData.cpa,
      metaData.impressions,
      metaData.ctr,
      cashBalance.balance,
      inventoryData.totalUnits,
      inventoryData.inventoryDays,
      supportData.openTickets,
      supportData.backlogCount
    ];
    sheet.appendRow(newRow);

    // 8. Calculate runway
    const runway = calculateRunway(cashBalance.balance);

    // 9. Check for red flags
    const redFlags = checkRedFlags(shopifyData, metaData, cashBalance, inventoryData);

    // 10. Send Slack notification (if red flags)
    if (redFlags.length > 0) {
      sendSlackAlert(redFlags);
    }

    // 11. Update dashboard file (optional - can be manual)
    // updateDashboardMarkdown(shopifyData, metaData, cashBalance);

    Logger.log('Daily sync complete: ' + yesterday);

  } catch (error) {
    Logger.log('ERROR in dailySync: ' + error);
    sendErrorEmail(error);
  }
}
```

### API Wrapper Example (`shopify_api.gs`)

```javascript
function fetchShopifyMetrics(date) {
  const config = getConfig(); // Loads from Properties Service
  const shopUrl = config.SHOPIFY_STORE_URL; // e.g., "ionwave.myshopify.com"
  const accessToken = config.SHOPIFY_ACCESS_TOKEN;

  // Format date for API (ISO 8601)
  const dateStart = Utilities.formatDate(date, 'America/New_York', "yyyy-MM-dd'T'00:00:00XXX");
  const dateEnd = Utilities.formatDate(date, 'America/New_York', "yyyy-MM-dd'T'23:59:59XXX");

  // Fetch orders
  const ordersUrl = `https://${shopUrl}/admin/api/2024-01/orders.json?created_at_min=${dateStart}&created_at_max=${dateEnd}&status=any`;
  const response = UrlFetchApp.fetch(ordersUrl, {
    headers: {
      'X-Shopify-Access-Token': accessToken
    },
    muteHttpExceptions: true
  });

  if (response.getResponseCode() !== 200) {
    throw new Error('Shopify API error: ' + response.getContentText());
  }

  const data = JSON.parse(response.getContentText());
  const orders = data.orders;

  // Calculate metrics
  const revenue = orders.reduce((sum, order) => sum + parseFloat(order.total_price), 0);
  const orderCount = orders.length;
  const newCustomers = orders.filter(order => order.customer && order.customer.orders_count === 1).length;
  const aov = orderCount > 0 ? revenue / orderCount : 0;

  return {
    revenue: revenue,
    orders: orderCount,
    newCustomers: newCustomers,
    aov: aov
  };
}
```

### Configuration (`config.gs`)

**DO NOT hardcode API keys in scripts.** Use Properties Service (encrypted storage).

**Setup** (one-time):
```javascript
function setConfig() {
  const scriptProperties = PropertiesService.getScriptProperties();

  scriptProperties.setProperties({
    'SHOPIFY_STORE_URL': 'ionwave.myshopify.com',
    'SHOPIFY_ACCESS_TOKEN': 'shpat_xxxxx',
    'META_ACCESS_TOKEN': 'EAAxxxxx',
    'META_AD_ACCOUNT_ID': 'act_123456789',
    'STRIPE_SECRET_KEY': 'sk_live_xxxxx',
    '3PL_API_KEY': 'xxxxx',
    'GORGIAS_API_KEY': 'xxxxx',
    'SLACK_WEBHOOK_URL': 'https://hooks.slack.com/services/xxxxx'
  });
}

function getConfig() {
  return PropertiesService.getScriptProperties().getProperties();
}
```

**Security**: Properties Service is encrypted. Only project editors can view.

---

## Google Sheet Structure

**Sheet Name**: "Daily Metrics"

| Column | Metric | Data Type | Formula/Source |
|--------|--------|-----------|----------------|
| A | Date | Date | API sync |
| B | Revenue | Currency | Shopify API |
| C | Orders | Number | Shopify API |
| D | New Customers | Number | Shopify API |
| E | AOV | Currency | =B/C |
| F | Ad Spend | Currency | Meta API |
| G | ROAS (platform) | Number | Meta API |
| H | CPA | Currency | Meta API |
| I | Impressions | Number | Meta API |
| J | CTR | Percentage | Meta API |
| K | Cash Balance | Currency | Bank API |
| L | Inventory Units | Number | 3PL API |
| M | Inventory Days | Number | =L/AVG(C2:C8) |
| N | Open Tickets | Number | Support API |
| O | Backlog Tickets (>24hrs) | Number | Support API |
| P | Runway (days) | Number | =K/AVG(daily burn) |

**Historical Data**: Keep all rows (never delete). Allows trend analysis, cohort tracking.

**Backup**: Google Sheets auto-saves. Also export to CSV weekly → store in `/passets/dashboards/backups/`.

---

## Error Handling & Monitoring

### API Failure Scenarios

**Scenario 1: Single API fails (e.g., Meta API down)**
- **Action**: Use yesterday's value for that metric
- **Note**: Add column "Data Quality" with note "Meta API stale - manual check required"
- **Alert**: Email operator with subject "⚠️ Meta API sync failed"

**Scenario 2: Multiple APIs fail (2+)**
- **Action**: Abort sync, send critical alert
- **Alert**: Email + Slack with subject "🚨 CRITICAL: Data pipeline failure"
- **Fallback**: Operator manually updates dashboard from source systems

**Scenario 3: Rate limit exceeded**
- **Action**: Wait and retry (exponential backoff: 1s, 2s, 4s)
- **Max retries**: 3 attempts
- **If still failing**: Skip that API for today, alert operator

### Monitoring & Alerts

**Daily Health Check** (part of sync script):
```javascript
function checkDataQuality() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Daily Metrics');
  const lastRow = sheet.getLastRow();
  const todayData = sheet.getRange(lastRow, 1, 1, 16).getValues()[0];

  // Check for zeros (likely API failure)
  if (todayData[1] === 0 || todayData[5] === 0) {
    sendSlackAlert('⚠️ Data quality issue: Zero values detected. Check API sync logs.');
  }

  // Check for stale data (no new row added today)
  const lastDate = new Date(todayData[0]);
  const today = new Date();
  const daysDiff = Math.floor((today - lastDate) / (1000 * 60 * 60 * 24));

  if (daysDiff > 1) {
    sendSlackAlert('🚨 CRITICAL: Daily sync has not run for ' + daysDiff + ' days!');
  }
}
```

**Alert Channels**:
1. **Email**: Operator's email address
2. **Slack**: #ionwave-alerts channel (if team exists)
3. **Google Apps Script Logs**: View logs at script.google.com/home

---

## Setup Checklist (One-Time)

**Week 2 (after entity formation, bank account, Shopify, Meta setup)**:

- [ ] **1. Create Google Sheet**
  - Name: "IonWave Operations Dashboard"
  - Sheet 1: "Daily Metrics" (columns A-P as specified above)
  - Sheet 2: "Weekly Summary" (aggregated metrics)
  - Sheet 3: "Red Flags" (kill criteria tracking)

- [ ] **2. Set up Google Apps Script project**
  - Extensions → Apps Script
  - Create files: `daily_sync.gs`, `shopify_api.gs`, `meta_api.gs`, `bank_api.gs`, `config.gs`, `utils.gs`
  - Paste script code from templates

- [ ] **3. Configure API credentials**
  - Run `setConfig()` function once
  - Enter all API keys/tokens in Properties Service
  - Test each API wrapper function individually

- [ ] **4. Test sync script**
  - Run `dailySync()` manually
  - Check: Google Sheet populates with yesterday's data
  - Check: No errors in Logs (View → Executions)

- [ ] **5. Set up time-driven trigger**
  - Triggers → Add Trigger
  - Function: `dailySync`
  - Event source: Time-driven
  - Type: Day timer
  - Time: 6:00 AM - 7:00 AM
  - Failure notification: Email me immediately

- [ ] **6. Configure Slack webhook (optional)**
  - Slack: Settings → Incoming Webhooks
  - Create webhook for #ionwave-alerts channel
  - Add `SLACK_WEBHOOK_URL` to Properties Service

- [ ] **7. Test error handling**
  - Temporarily break one API (wrong token)
  - Verify: Error email sent, sync continues with other APIs
  - Fix API token, retest

- [ ] **8. Backfill historical data (optional)**
  - Manually run sync for past 7 days
  - Provides baseline for "vs 7-day avg" calculations

- [ ] **9. Document credentials location**
  - Store backup of API keys in 1Password vault "IonWave-Production"
  - Document: Which APIs are set up, where to refresh tokens

- [ ] **10. Train operator on dashboard**
  - Show: How to open Google Sheet
  - Show: How to read Daily Pulse dashboard
  - Show: What to do if red flags appear
  - Show: How to manually update if sync fails

**Estimated Setup Time**: 4-6 hours (Week 2, after APIs are available)

---

## Maintenance & Updates

**Weekly**:
- [ ] Check: Trigger is running daily (View → Executions)
- [ ] Check: No repeated errors in logs

**Monthly**:
- [ ] Review: API token expiration dates (especially Meta OAuth, expires 90 days)
- [ ] Refresh: Meta access token if <30 days until expiration
- [ ] Backup: Export Google Sheet to CSV → save in `/passets/dashboards/backups/`

**Quarterly**:
- [ ] Review: Are new metrics needed? (e.g., LTV, cohort retention)
- [ ] Update: Script to add new metrics if needed
- [ ] Audit: Are all APIs still the cheapest/best option?

**When to Upgrade to Custom Dashboard** (Phase 2+):
- Revenue >$50K MRR
- Team grows beyond solo operator (need role-specific dashboards)
- Attribution needs more complex than blended CAC/MER
- Manual data entry is >10 min/day

**Upgrade Options**:
- **Triple Whale**: $300/mo, D2C-focused, great for supplements
- **Polar Analytics**: $250/mo, spreadsheet-like interface
- **Northbeam**: $500+/mo, advanced attribution (overkill until $100K+ MRR)

---

## Version History

**v1.0.0 (2026-02-11)**:
- Initial data pipeline specification
- Google Apps Script architecture
- API integration specs for Shopify, Meta, Bank, 3PL, Support
- Error handling and monitoring protocols
- Setup checklist for Week 2 implementation
