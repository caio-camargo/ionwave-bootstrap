#!/usr/bin/env python3
"""
Master Aggregated TUP Report Generator

Generates a single comprehensive report containing ALL migrated TUP content.
Includes metadata summary, hypotheses section, and full content from all TUPs.

Usage:
    python scripts/generate_master_aggregated_report.py

Output:
    reports/IonWave_Complete_TUP_Aggregation.md (full content, 500+ pages)
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional


def json_to_nested_bullets(data: Any, indent_level: int = 0) -> List[str]:
    """Convert JSON data to nested bullet list format."""
    lines = []
    indent = "  " * indent_level

    if isinstance(data, dict):
        for key, value in data.items():
            formatted_key = key.replace("_", " ").title()

            if isinstance(value, (dict, list)):
                lines.append(f"{indent}- **{formatted_key}:**")
                lines.extend(json_to_nested_bullets(value, indent_level + 1))
            elif value is None:
                lines.append(f"{indent}- **{formatted_key}:** _(not set)_")
            elif isinstance(value, bool):
                lines.append(f"{indent}- **{formatted_key}:** {value}")
            elif isinstance(value, str) and len(value) > 100:
                lines.append(f"{indent}- **{formatted_key}:**")
                lines.append(f"{indent}  > {value}")
            else:
                lines.append(f"{indent}- **{formatted_key}:** {value}")

    elif isinstance(data, list):
        if not data:
            lines.append(f"{indent}- _(empty list)_")
        else:
            for item in data:
                if isinstance(item, (dict, list)):
                    lines.append(f"{indent}- ")
                    sub_lines = json_to_nested_bullets(item, indent_level + 1)
                    if sub_lines and sub_lines[0].strip().startswith("-"):
                        sub_lines[0] = sub_lines[0].replace("-", " ", 1)
                    lines.extend(sub_lines)
                else:
                    lines.append(f"{indent}- {item}")
    else:
        lines.append(f"{indent}- {data}")

    return lines


def read_json_file(filepath: Path) -> Optional[Dict]:
    """Read and parse a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return None


def read_markdown_file(filepath: Path) -> Optional[str]:
    """Read a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None


def generate_master_report(data_dir: Path, output_path: Path):
    """Generate complete aggregated report with all TUP content."""

    print("Generating Master Aggregated TUP Report...")
    print("This will include ALL content from all migrated TUPs.\n")

    report_lines = []

    # === HEADER ===
    report_lines.append("# IonWave Trade #84 - Complete TUP Aggregation")
    report_lines.append("")
    report_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("**Project:** IonWave Bootstrap (Studio 3 Imagination Generation System)")
    report_lines.append("**Purpose:** Complete aggregation of all migrated TUP content for operator review")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # === TABLE OF CONTENTS ===
    report_lines.append("## 📑 Table of Contents")
    report_lines.append("")
    report_lines.append("1. [Executive Summary](#executive-summary)")
    report_lines.append("2. [Business Hypotheses System](#business-hypotheses-system)")
    report_lines.append("3. [Complete TUP Content](#complete-tup-content)")
    report_lines.append("")

    # Get all TUP directories
    tup_dirs = sorted([p.parent for p in data_dir.glob("*/_meta.json")])

    for i, tup_dir in enumerate(tup_dirs, start=1):
        meta_path = tup_dir / "_meta.json"
        meta = read_json_file(meta_path)
        if meta:
            tup_id = meta.get("tup_id", tup_dir.name).upper()
            tup_name = meta.get("tup_name", "Unknown")
            report_lines.append(f"   {i}. [TUP {tup_id}: {tup_name}](#tup-{tup_id.lower()}-{tup_name.lower().replace(' ', '-').replace('&', 'and')})")

    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # === EXECUTIVE SUMMARY ===
    report_lines.append("## Executive Summary")
    report_lines.append("")
    report_lines.append(f"This comprehensive report aggregates **all content** from {len(tup_dirs)} migrated Trade Unit Projects (TUPs).")
    report_lines.append("")
    report_lines.append("**What's Included:**")
    report_lines.append("- Complete business hypotheses registry with grades and kill criteria")
    report_lines.append("- Full TUP metadata (quality scores, workshop details, intelligence gaps)")
    report_lines.append("- All JSON files converted to human-readable nested bullet lists")
    report_lines.append("- All markdown files included verbatim")
    report_lines.append("- Dependencies, next actions, and OpKit references")
    report_lines.append("")
    report_lines.append("**Navigation:**")
    report_lines.append("- Use the Table of Contents to jump to specific TUPs")
    report_lines.append("- Each TUP section is self-contained")
    report_lines.append("- Search (Ctrl+F) for specific topics across all TUPs")
    report_lines.append("")

    # Quality overview
    report_lines.append("### Quality Overview")
    report_lines.append("")
    report_lines.append("| TUP | Name | Quality | Status |")
    report_lines.append("|-----|------|---------|--------|")

    for tup_dir in tup_dirs:
        meta = read_json_file(tup_dir / "_meta.json")
        if meta:
            tup_id = meta.get("tup_id", "?").upper()
            tup_name = meta.get("tup_name", "Unknown")
            quality = meta.get("current_quality", "N/A")
            status = meta.get("status", "unknown")
            report_lines.append(f"| {tup_id} | {tup_name} | {quality}/10 | {status} |")

    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # === HYPOTHESES SECTION ===
    report_lines.append("## Business Hypotheses System")
    report_lines.append("")
    report_lines.append("The IonWave business model is built on testable hypotheses that drive validation tracking.")
    report_lines.append("")

    # Read hypotheses data
    hyp_registry_path = data_dir / "hypotheses" / "registry.json"
    if hyp_registry_path.exists():
        hyp_data = read_json_file(hyp_registry_path)
        if hyp_data and "hypotheses" in hyp_data:
            report_lines.append("### Hypothesis Registry")
            report_lines.append("")

            # Get metadata
            meta = hyp_data.get("_meta", {})
            report_lines.append(f"**Total Hypotheses:** {meta.get('total_hypotheses', 'N/A')}")
            report_lines.append(f"**Top-Level:** {meta.get('top_level_hypotheses', 'N/A')} | **Sub-Hypotheses:** {meta.get('sub_hypotheses', 'N/A')}")
            report_lines.append("")

            by_state = meta.get("by_state", {})
            report_lines.append("**By State:**")
            for state, count in by_state.items():
                report_lines.append(f"- {state}: {count}")
            report_lines.append("")

            by_severity = meta.get("by_severity", {})
            report_lines.append("**By Severity:**")
            for sev, count in by_severity.items():
                report_lines.append(f"- {sev}: {count}")
            report_lines.append("")

            by_grade = meta.get("by_grade", {})
            report_lines.append("**By Confidence Grade:**")
            for grade, count in by_grade.items():
                report_lines.append(f"- {grade}-grade: {count}")
            report_lines.append("")
            report_lines.append("---")
            report_lines.append("")

            # List is array, not dict
            for hyp in hyp_data["hypotheses"]:
                hyp_id = hyp.get("id", "?")
                report_lines.append(f"#### {hyp_id}: {hyp.get('name', 'Unknown')}")
                report_lines.append("")
                report_lines.append(f"- **Description:** {hyp.get('description', 'N/A')}")

                # Get latest revision for current value/grade
                revisions = hyp.get("revisions", [])
                if revisions:
                    latest = revisions[-1]
                    report_lines.append(f"- **Value:** {latest.get('value', 'N/A')}")
                    report_lines.append(f"- **Grade:** {latest.get('grade', 'N/A')}")

                report_lines.append(f"- **Severity:** {hyp.get('impact_severity', 'N/A')}")
                report_lines.append(f"- **Status:** {hyp.get('current_state', 'N/A')}")

                kill_criteria = hyp.get("kill_criteria", {})
                if kill_criteria and "criteria" in kill_criteria:
                    report_lines.append(f"- **Kill Criteria:** {kill_criteria['criteria']}")

                children = hyp.get("children", [])
                if children:
                    report_lines.append(f"- **Sub-Hypotheses:** {', '.join(children)}")

                report_lines.append("")

    report_lines.append("---")
    report_lines.append("")

    # === COMPLETE TUP CONTENT ===
    report_lines.append("## Complete TUP Content")
    report_lines.append("")
    report_lines.append("Each TUP section below contains:")
    report_lines.append("- Metadata (status, quality, workshop details)")
    report_lines.append("- All JSON files (converted to nested bullets)")
    report_lines.append("- All markdown files (full content)")
    report_lines.append("- Dependencies and next actions")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # Process each TUP
    for tup_dir in tup_dirs:
        meta_path = tup_dir / "_meta.json"
        meta = read_json_file(meta_path)

        if not meta:
            continue

        tup_id = meta.get("tup_id", tup_dir.name).upper()
        tup_name = meta.get("tup_name", "Unknown")

        print(f"Processing TUP {tup_id}: {tup_name}...")

        # TUP Header
        report_lines.append(f"# TUP {tup_id}: {tup_name}")
        report_lines.append("")

        # Status badges
        status = meta.get("status", "unknown")
        quality = meta.get("current_quality", "N/A")
        version = meta.get("current_version", "N/A")
        cluster = meta.get("cluster", "N/A")
        cluster_name = meta.get("cluster_name", "N/A")

        report_lines.append(f"**Status:** {status} | **Quality:** {quality}/10 | **Version:** {version}")
        report_lines.append(f"**Cluster:** {cluster} ({cluster_name})")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

        # Overview
        report_lines.append("## Overview")
        report_lines.append("")

        revisions = meta.get("revisions", [])
        if revisions:
            latest = revisions[-1]
            report_lines.append(f"- **Workshop Date:** {latest.get('date', 'N/A')}")
            report_lines.append(f"- **Actor:** {latest.get('actor', 'N/A')}")
            report_lines.append(f"- **Protocol Used:** {latest.get('protocol_used', 'N/A')}")

            dialogue_ref = latest.get("dialogue_ref", {})
            if dialogue_ref:
                personas = dialogue_ref.get("personas", [])
                report_lines.append(f"- **Personas:** {', '.join(personas)}")
                report_lines.append(f"- **Dialogue Rounds:** {dialogue_ref.get('rounds', 'N/A')}")
                report_lines.append(f"- **Saturated:** {dialogue_ref.get('saturated', False)}")
                report_lines.append(f"- **Upgrades:** {dialogue_ref.get('upgrades', 0)}")

            report_lines.append("")
            report_lines.append(f"**Quality Score:** {latest.get('quality_score', 'N/A')}/10")
            report_lines.append(f"**Rationale:** {latest.get('quality_rationale', 'N/A')}")

        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

        # Content Files Index
        report_lines.append("## Content Files")
        report_lines.append("")

        files_data = meta.get("files", {})
        if isinstance(files_data, dict):
            for filename, description in files_data.items():
                file_type = "MD" if filename.endswith(".md") else "JSON"
                report_lines.append(f"- **[{file_type}] {filename}**")
                report_lines.append(f"  > {description}")
        elif isinstance(files_data, list):
            for filename in files_data:
                if filename != "_meta.json":
                    file_type = "MD" if filename.endswith(".md") else "JSON"
                    report_lines.append(f"- **[{file_type}] {filename}**")

        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

        # JSON Files (Structured Data)
        json_files = sorted([f for f in tup_dir.glob("*.json") if f.name != "_meta.json"])

        if json_files:
            report_lines.append("## Structured Data (JSON)")
            report_lines.append("")

            for json_file in json_files:
                data = read_json_file(json_file)
                if data:
                    report_lines.append(f"### {json_file.name}")
                    report_lines.append("")
                    bullet_lines = json_to_nested_bullets(data)
                    report_lines.extend(bullet_lines)
                    report_lines.append("")
                    report_lines.append("---")
                    report_lines.append("")

        # Markdown Files (Narrative Content)
        md_files = sorted(tup_dir.glob("*.md"))

        if md_files:
            report_lines.append("## Narrative Content (Markdown)")
            report_lines.append("")

            for md_file in md_files:
                content = read_markdown_file(md_file)
                if content:
                    report_lines.append(f"### {md_file.name}")
                    report_lines.append("")
                    report_lines.append(content)
                    report_lines.append("")
                    report_lines.append("---")
                    report_lines.append("")

        # Dependencies
        report_lines.append("## Dependencies & Relationships")
        report_lines.append("")

        feeds_into = meta.get("feeds_into", [])
        requires = meta.get("requires", [])

        report_lines.append("**Feeds Into:**")
        if feeds_into:
            for item in feeds_into:
                report_lines.append(f"- {item}")
        else:
            report_lines.append("- _(No downstream dependencies)_")

        report_lines.append("")
        report_lines.append("**Requires:**")
        if requires:
            for item in requires:
                report_lines.append(f"- {item}")
        else:
            report_lines.append("- _(No upstream dependencies)_")

        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

        # Intelligence Gaps
        report_lines.append("## Intelligence Gaps")
        report_lines.append("")

        gaps = meta.get("intelligence_gaps", [])
        if gaps:
            for gap in gaps:
                if isinstance(gap, str):
                    report_lines.append(f"- {gap}")
                elif isinstance(gap, dict):
                    report_lines.append(f"- **{gap.get('gap', 'Unknown gap')}**")
                    if 'upgrade_path' in gap:
                        report_lines.append(f"  - Upgrade Path: {gap['upgrade_path']}")
                    if 'priority' in gap:
                        report_lines.append(f"  - Priority: {gap['priority']}")
        else:
            report_lines.append("_No intelligence gaps documented._")

        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

        # Next Actions
        report_lines.append("## Next Actions")
        report_lines.append("")

        next_action = meta.get("next_action", "")
        key_blockers = meta.get("key_blockers", [])

        if next_action:
            report_lines.append(next_action)
        else:
            report_lines.append("_No next actions documented._")

        if key_blockers:
            report_lines.append("")
            report_lines.append("**Key Blockers:**")
            if isinstance(key_blockers, list):
                for blocker in key_blockers:
                    report_lines.append(f"- {blocker}")
            else:
                report_lines.append(f"- {key_blockers}")

        report_lines.append("")
        report_lines.append("")
        report_lines.append("=" * 80)
        report_lines.append("")
        report_lines.append("")

    # Footer
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## Report Metadata")
    report_lines.append("")
    report_lines.append(f"- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"- **Total TUPs:** {len(tup_dirs)}")
    report_lines.append(f"- **Total Lines:** {len(report_lines)}")
    report_lines.append(f"- **Generator:** scripts/generate_master_aggregated_report.py")
    report_lines.append("")
    report_lines.append("_End of Master Aggregated Report_")

    # Write to file
    print(f"\nWriting report to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))

    # Calculate file size
    file_size_kb = output_path.stat().st_size / 1024

    print(f"\nDone!")
    print(f"Report saved to: {output_path}")
    print(f"File size: {file_size_kb:.1f} KB")
    print(f"Total lines: {len(report_lines)}")
    print(f"Total TUPs: {len(tup_dirs)}")


def main():
    """Main execution function."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    data_dir = project_root / "data"
    output_dir = project_root / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "IonWave_Complete_TUP_Aggregation.md"

    generate_master_report(data_dir, output_path)


if __name__ == "__main__":
    main()
