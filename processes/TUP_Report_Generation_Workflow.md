# TUP Report Generation Workflow

**Version**: 1.0.0
**Created**: 2026-02-09
**Purpose**: Generate human-readable markdown reports for migrated TUPs
**Owner**: Danilo (operator review), Caio (automation)
**Status**: Active

---

## Overview

This workflow converts TUP data (JSON + Markdown files) into comprehensive, human-readable reports for operator review.

**Input:** TUP directories in `data/m*/` with `_meta.json` and content files
**Output:** Unified markdown reports in `reports/tup_reports/`
**Format:** One report per TUP, JSON converted to nested bullet lists

---

## Quick Start

### Generate All Migrated TUPs

```bash
cd "G:\Drives compartilhados\Studio 3\IonWave\IonWave Bootstrap"
python scripts/generate_tup_reports.py
```

### Generate Specific TUPs

```bash
python scripts/generate_tup_reports.py m21 m26 m27
```

### Custom Output Directory

```bash
python scripts/generate_tup_reports.py --output-dir ./custom_reports
```

---

## What Gets Generated

Each TUP report contains:

### 1. Header & Status
- TUP ID, name, status badges
- Quality score, version, cluster assignment

### 2. Overview Section
- Workshop metadata (date, actor, protocol)
- Dialogue summary (personas, rounds, saturation status)
- Quality assessment with rationale

### 3. Content Files Index
- List of all files with descriptions from `_meta.json`
- File type indicators (📄 MD / 🔧 JSON)

### 4. Structured Data (JSON → Human-Readable)
- All `.json` files (except `_meta.json`) converted to **nested bullet lists**
- Each JSON file gets its own subsection
- Example transformation:
  ```json
  {
    "platform": "Loop",
    "pricing": {
      "free_plan": "Up to 50 subscribers"
    }
  }
  ```
  Becomes:
  ```
  - **Platform:** Loop
  - **Pricing:**
    - **Free Plan:** Up to 50 subscribers
  ```

### 5. Narrative Content (Markdown Files)
- All `.md` files included verbatim
- Each file gets its own subsection

### 6. Dependencies & Relationships
- **Feeds Into**: Downstream TUPs
- **Requires**: Upstream TUPs

### 7. Intelligence Gaps
- All documented gaps from `_meta.json`
- Upgrade paths and priorities where available

### 8. Next Actions & Blockers
- `next_action` field from metadata
- Key blockers list

### 9. OpKits
- Registered OpKit IDs

### 10. Footer
- Generation timestamp
- Source directory reference

---

## Output Structure

```
reports/
└── tup_reports/
    ├── TUP_M0_Trade_Thesis_Report.md
    ├── TUP_M21_Subscription_and_Retention_Report.md
    ├── TUP_M26_Competitive_Intel_Report.md
    └── ...
```

---

## Use Cases

### 1. Operator Review (Primary Use Case)
**Who:** Danilo
**When:** After TUP workshop completion
**Why:** Review all content in one place without switching between JSON/MD files

**Workflow:**
1. Workshop completes (Phase 11 of TUP Workshop Protocol)
2. Run: `python scripts/generate_tup_reports.py m{N}`
3. Open report in markdown editor
4. Review all sections sequentially
5. Note any corrections needed → feed back to Claude for updates

---

### 2. Quality Audit
**Who:** Caio or Danilo
**When:** Periodic quality checks
**Why:** Spot-check intelligence gaps, confidence grades, evidence quality

**Workflow:**
1. Generate all reports: `python scripts/generate_tup_reports.py`
2. Search across reports for patterns (e.g., grep "D-grade", "intelligence gap")
3. Prioritize upgrades based on findings

---

### 3. Cross-TUP Analysis
**Who:** Operator or Claude
**When:** Looking for patterns across multiple TUPs
**Why:** Find common gaps, validate assumptions across domains

**Workflow:**
1. Generate reports for relevant cluster (e.g., all BCL-4 TUPs)
2. Use text search across reports
3. Extract patterns (e.g., "subscription platforms mentioned across M17, M19, M21")

---

### 4. Stakeholder Sharing
**Who:** Danilo
**When:** Sharing specific TUP analysis with advisors/investors
**Why:** Clean, professional format without raw JSON

**Workflow:**
1. Generate specific TUP: `python scripts/generate_tup_reports.py m0`
2. Review and optionally redact sensitive sections
3. Share PDF export or markdown file

---

## Integration with TUP Workshop Protocol

### Recommended Addition to Phase 11 (Session Log)

After completing a TUP workshop, add this step:

```markdown
**PHASE 11: SESSION LOG**

1. Record what was done in `SESSION_LOG.md`
2. **Generate human-readable report:**
   ```bash
   python scripts/generate_tup_reports.py m{N}
   ```
3. Share report path with operator for review
```

This makes report generation a standard post-workshop deliverable.

---

## Maintenance

### When to Regenerate Reports

Reports are **static snapshots**. Regenerate when:

- TUP content is updated (new version, evidence upgrade)
- `_meta.json` is modified (quality score changes, new intelligence gaps)
- Operator needs latest view for review

### Batch Regeneration

After a batch workshop session:

```bash
python scripts/generate_tup_reports.py m14 m16 m17 m18 m19 m20
```

---

## Customization

### Modify Output Format

Edit `scripts/generate_tup_reports.py`:

- **Change bullet nesting depth**: Modify `json_to_nested_bullets()` indent logic
- **Add/remove sections**: Edit `generate_tup_report()` section blocks
- **Change section order**: Reorder report_lines.append() blocks
- **Custom formatting**: Modify markdown formatting in any section

### Add New Data Sources

If new metadata fields are added to `_meta.json`:

1. Edit `generate_tup_report()` function
2. Add new section extracting the field
3. Format as needed (bullets, tables, prose)

---

## Troubleshooting

### "No valid _meta.json" Error
**Cause:** TUP not migrated yet
**Fix:** Only process migrated TUPs, or migrate the TUP first

### JSON Parse Error
**Cause:** Malformed JSON file
**Fix:** Check JSON syntax with `jsonlint` or VS Code, fix errors

### Missing Files in Report
**Cause:** Files exist but not documented in `_meta.json`
**Fix:** Update `files` dictionary in `_meta.json`

### Report Too Long
**Cause:** Large JSON files (e.g., VOC databases)
**Fix:** Consider excluding specific files or summarizing large datasets

---

## Future Enhancements (Optional)

- [ ] HTML output option with collapsible sections
- [ ] PDF export with table of contents
- [ ] Filtering: Include/exclude specific sections (e.g., `--no-narrative`)
- [ ] Diff mode: Compare two versions of same TUP
- [ ] Summary dashboard: One-page overview of all TUPs
- [ ] Integration with dashboard (auto-generate on TUP update)

---

## Related Documents

| Document | Relationship |
|----------|-------------|
| `processes/TUP_Workshop_Protocol.md` | Parent process — this workflow is Phase 11 deliverable |
| `scripts/generate_tup_reports.py` | Implementation script |
| `tracking/TUP_Workshop_Tracker.md` | Tracks which TUPs are ready for report generation |
| `data/manifest.json` | Source of TUP metadata |
| `standards/Deliverable_Structure_Standards.md` | Content quality standards |

---

## Change Log

| Date | Version | Change |
|------|---------|--------|
| 2026-02-09 | 1.0.0 | Initial workflow created. Script supports all migrated TUPs, nested bullet lists for JSON, full markdown inclusion. |
