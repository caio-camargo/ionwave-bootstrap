#!/usr/bin/env python3
"""
TUP Human-Readable Report Generator

Generates comprehensive human-readable markdown reports for migrated TUPs.
Converts JSON files to nested bullet lists and aggregates all TUP content.

Usage:
    python scripts/generate_tup_reports.py                  # Generate all migrated TUPs
    python scripts/generate_tup_reports.py m21 m26         # Generate specific TUPs
    python scripts/generate_tup_reports.py --output-dir ./reports  # Custom output directory

Output:
    reports/TUP_{ID}_{Name}_Report.md for each TUP
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional


def json_to_nested_bullets(data: Any, indent_level: int = 0) -> List[str]:
    """
    Convert JSON data to nested bullet list format.

    Args:
        data: JSON data (dict, list, or primitive)
        indent_level: Current indentation level (0 = root)

    Returns:
        List of formatted markdown lines
    """
    lines = []
    indent = "  " * indent_level

    if isinstance(data, dict):
        for key, value in data.items():
            # Format key nicely (convert snake_case to Title Case)
            formatted_key = key.replace("_", " ").title()

            if isinstance(value, (dict, list)):
                lines.append(f"{indent}- **{formatted_key}:**")
                lines.extend(json_to_nested_bullets(value, indent_level + 1))
            elif value is None:
                lines.append(f"{indent}- **{formatted_key}:** _(not set)_")
            elif isinstance(value, bool):
                lines.append(f"{indent}- **{formatted_key}:** {value}")
            elif isinstance(value, str) and len(value) > 100:
                # Long strings get their own indented block
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
                    # Add sub-items indented
                    sub_lines = json_to_nested_bullets(item, indent_level + 1)
                    if sub_lines and sub_lines[0].strip().startswith("-"):
                        # Remove the leading dash from first sub-item since parent already has it
                        sub_lines[0] = sub_lines[0].replace("-", " ", 1)
                    lines.extend(sub_lines)
                else:
                    lines.append(f"{indent}- {item}")
    else:
        lines.append(f"{indent}- {data}")

    return lines


def read_json_file(filepath: Path) -> Optional[Dict]:
    """Read and parse a JSON file, return None if invalid."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Warning: Could not read {filepath}: {e}")
        return None


def read_markdown_file(filepath: Path) -> Optional[str]:
    """Read a markdown file, return None if invalid."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None


def generate_tup_report(tup_dir: Path, output_dir: Path) -> Optional[Path]:
    """
    Generate a human-readable report for a single TUP.

    Args:
        tup_dir: Path to TUP directory (e.g., data/m21/)
        output_dir: Path to output directory for reports

    Returns:
        Path to generated report file, or None if failed
    """
    # Read _meta.json
    meta_path = tup_dir / "_meta.json"
    meta = read_json_file(meta_path)

    if not meta:
        print(f"Skipping {tup_dir.name}: No valid _meta.json")
        return None

    tup_id = meta.get("tup_id", tup_dir.name)
    tup_name = meta.get("tup_name", "Unknown")

    # Start building the report
    report_lines = []

    # === HEADER ===
    report_lines.append(f"# TUP {tup_id.upper()}: {tup_name}")
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

    # === OVERVIEW ===
    report_lines.append("## 📋 Overview")
    report_lines.append("")

    # Latest revision info
    revisions = meta.get("revisions", [])
    if revisions:
        latest = revisions[-1]
        report_lines.append(f"- **Workshop Date:** {latest.get('date', 'N/A')}")
        report_lines.append(f"- **Actor:** {latest.get('actor', 'N/A')}")
        report_lines.append(f"- **Protocol Used:** {latest.get('protocol_used', 'N/A')}")
        report_lines.append(f"- **Change Type:** {latest.get('change_type', 'N/A')}")

        dialogue_ref = latest.get("dialogue_ref", {})
        if dialogue_ref:
            report_lines.append("")
            report_lines.append("### Workshop Dialogue")
            personas = dialogue_ref.get("personas", [])
            report_lines.append(f"- **Personas Used:** {', '.join(personas)}")
            report_lines.append(f"- **Rounds:** {dialogue_ref.get('rounds', 'N/A')}")
            report_lines.append(f"- **Saturated:** {dialogue_ref.get('saturated', False)}")
            report_lines.append(f"- **Upgrades Applied:** {dialogue_ref.get('upgrades', 0)}")
            report_lines.append(f"- **Unresolved Issues:** {dialogue_ref.get('unresolved', 0)}")

        report_lines.append("")
        report_lines.append("### Quality Assessment")
        report_lines.append(f"- **Score:** {latest.get('quality_score', 'N/A')}/10")
        rationale = latest.get('quality_rationale', 'N/A')
        report_lines.append(f"- **Rationale:** {rationale}")

    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # === CONTENT FILES ===
    report_lines.append("## 📁 Content Files")
    report_lines.append("")

    files_data = meta.get("files", {})

    # Handle both dict format (M21) and list format (M10)
    if isinstance(files_data, dict):
        # Dict format: {filename: description}
        for filename, description in files_data.items():
            file_type = "📄 MD" if filename.endswith(".md") else "🔧 JSON"
            report_lines.append(f"- {file_type} **{filename}**")
            report_lines.append(f"  > {description}")
    elif isinstance(files_data, list):
        # List format: ["filename1", "filename2", ...]
        for filename in files_data:
            if filename == "_meta.json":
                continue  # Skip meta file
            file_type = "📄 MD" if filename.endswith(".md") else "🔧 JSON"
            report_lines.append(f"- {file_type} **{filename}**")
    else:
        report_lines.append("_No files documented in metadata._")

    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # === STRUCTURED DATA (JSON FILES) ===
    report_lines.append("## 🔧 Structured Data")
    report_lines.append("")
    report_lines.append("_JSON files converted to human-readable format_")
    report_lines.append("")

    json_files = sorted(tup_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name != "_meta.json"]

    if json_files:
        for json_file in json_files:
            data = read_json_file(json_file)
            if data:
                report_lines.append(f"### 📊 {json_file.name}")
                report_lines.append("")
                bullet_lines = json_to_nested_bullets(data)
                report_lines.extend(bullet_lines)
                report_lines.append("")
        report_lines.append("---")
        report_lines.append("")
    else:
        report_lines.append("_No JSON files in this TUP._")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

    # === NARRATIVE CONTENT (MARKDOWN FILES) ===
    report_lines.append("## 📝 Narrative Content")
    report_lines.append("")

    md_files = sorted(tup_dir.glob("*.md"))

    if md_files:
        for md_file in md_files:
            content = read_markdown_file(md_file)
            if content:
                report_lines.append(f"### 📄 {md_file.name}")
                report_lines.append("")
                report_lines.append(content)
                report_lines.append("")
                report_lines.append("---")
                report_lines.append("")
    else:
        report_lines.append("_No markdown files in this TUP._")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

    # === DEPENDENCIES & RELATIONSHIPS ===
    report_lines.append("## 🔗 Dependencies & Relationships")
    report_lines.append("")

    feeds_into = meta.get("feeds_into", [])
    requires = meta.get("requires", [])

    report_lines.append("### Feeds Into")
    if feeds_into:
        for item in feeds_into:
            report_lines.append(f"- {item}")
    else:
        report_lines.append("- _No downstream dependencies_")

    report_lines.append("")
    report_lines.append("### Requires")
    if requires:
        for item in requires:
            report_lines.append(f"- {item}")
    else:
        report_lines.append("- _No upstream dependencies_")

    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # === INTELLIGENCE GAPS ===
    report_lines.append("## ⚠️ Intelligence Gaps")
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

    # === NEXT ACTIONS ===
    report_lines.append("## 🎯 Next Actions")
    report_lines.append("")

    next_action = meta.get("next_action", "")
    key_blockers = meta.get("key_blockers", [])

    if next_action:
        report_lines.append(next_action)
    else:
        report_lines.append("_No next actions documented._")

    report_lines.append("")

    if key_blockers:
        report_lines.append("### Key Blockers")
        if isinstance(key_blockers, list):
            for blocker in key_blockers:
                report_lines.append(f"- {blocker}")
        else:
            report_lines.append(f"- {key_blockers}")

    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")

    # === OPKITS ===
    opkits = meta.get("opkits", [])
    if opkits:
        report_lines.append("## 🧰 OpKits")
        report_lines.append("")
        for opkit in opkits:
            report_lines.append(f"- {opkit}")
        report_lines.append("")
        report_lines.append("---")
        report_lines.append("")

    # === FOOTER ===
    report_lines.append("---")
    report_lines.append("")
    report_lines.append(f"_Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")
    report_lines.append("")
    report_lines.append(f"_Source: `{tup_dir.relative_to(tup_dir.parent.parent)}`_")

    # Write to file
    output_filename = f"TUP_{tup_id.upper()}_{tup_name.replace(' ', '_').replace('&', 'and')}_Report.md"
    output_path = output_dir / output_filename

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))

    print(f"[OK] Generated: {output_filename}")
    return output_path


def main():
    """Main execution function."""
    # Parse arguments
    args = sys.argv[1:]

    # Determine project root (assuming script is in scripts/ subdirectory)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    data_dir = project_root / "data"

    # Default output directory
    output_dir = project_root / "reports" / "tup_reports"

    # Check for custom output directory
    if "--output-dir" in args:
        idx = args.index("--output-dir")
        if idx + 1 < len(args):
            output_dir = Path(args[idx + 1])
            args = args[:idx] + args[idx+2:]  # Remove from args

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Determine which TUPs to process
    if args:
        # Specific TUPs requested
        tup_ids = [arg.lower() for arg in args]
        tup_dirs = []
        for tup_id in tup_ids:
            # Try to find directory
            possible_dirs = list(data_dir.glob(f"{tup_id}*"))
            if possible_dirs:
                tup_dirs.append(possible_dirs[0])
            else:
                print(f"Warning: Could not find directory for {tup_id}")
    else:
        # Process all TUPs with _meta.json
        tup_dirs = sorted([p.parent for p in data_dir.glob("*/_meta.json")])

    if not tup_dirs:
        print("No TUPs found to process.")
        return

    print(f"\nGenerating reports for {len(tup_dirs)} TUP(s)...")
    print(f"Output directory: {output_dir}\n")

    # Generate reports
    generated_count = 0
    for tup_dir in tup_dirs:
        result = generate_tup_report(tup_dir, output_dir)
        if result:
            generated_count += 1

    print(f"\nDone! Generated {generated_count} report(s).")
    print(f"Reports saved to: {output_dir}")


if __name__ == "__main__":
    main()
