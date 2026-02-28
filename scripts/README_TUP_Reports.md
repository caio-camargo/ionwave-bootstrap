# TUP Report Generator - Quick Reference

## Purpose
Generate human-readable markdown reports from TUP data (JSON + MD files).

## Basic Usage

```bash
# From project root
cd "G:\Drives compartilhados\Studio 3\IonWave\IonWave Bootstrap"

# Generate all migrated TUPs
python scripts/generate_tup_reports.py

# Generate specific TUPs
python scripts/generate_tup_reports.py m21 m26 m27

# Custom output directory
python scripts/generate_tup_reports.py --output-dir ./custom_location
```

## Output Location
Default: `reports/tup_reports/`

Each TUP gets one file: `TUP_{ID}_{Name}_Report.md`

## What You Get

Each report includes:
- ✅ TUP metadata (status, quality score, version)
- ✅ Workshop summary (dialogue, personas, saturation)
- ✅ **JSON files converted to nested bullet lists** (human-readable)
- ✅ Markdown files included verbatim
- ✅ Dependencies & relationships
- ✅ Intelligence gaps with upgrade paths
- ✅ Next actions & blockers

## Example Output

For M21 (Subscription & Retention):
- Total length: ~1,000 lines
- Includes 2 JSON files (subscription_platform, churn_prediction) converted to bullets
- Includes 5 MD files (psychology, playbook, win-back, dialogue, opkit)
- All metadata, gaps, and next actions

## Common Workflows

### After Workshop Completion
```bash
python scripts/generate_tup_reports.py m{N}
# Review the report in reports/tup_reports/
```

### Batch Generation
```bash
# Generate all TUPs in a cluster (e.g., BCL-4: Retention)
python scripts/generate_tup_reports.py m17 m19 m21
```

### Full Export
```bash
# Generate everything migrated
python scripts/generate_tup_reports.py
```

## Troubleshooting

**"No valid _meta.json"**
→ TUP not migrated yet. Only migrated TUPs work.

**JSON parse error**
→ Fix JSON syntax errors in the source file.

**Missing content in report**
→ Update the `files` dict in `_meta.json` to document the files.

## Documentation
Full workflow: `processes/TUP_Report_Generation_Workflow.md`
Script: `scripts/generate_tup_reports.py`
