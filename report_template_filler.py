#!/usr/bin/env python3
"""
report_template_filler.py
Fills a user-defined report template with case-specific answers to produce
a consistently formatted report. Applies no logic about what a report should
contain — the template and its fields are entirely defined by the user.

Live demo: https://biancabcarlson.github.io/Report-Template-Filler/

Usage:
    python report_template_filler.py template.json answers.json -o report.md

Input (template.json) — SYNTHETIC EXAMPLE:
{
  "title": "Case Investigation Report",
  "sections": [
    {"heading": "Case Information", "fields": ["case_id", "date_opened", "investigator"]},
    {"heading": "Account Summary", "fields": ["account_holder", "account_age", "account_status"]},
    {"heading": "Findings", "fields": ["summary", "key_observations"]},
    {"heading": "Disposition", "fields": ["outcome", "next_steps"]}
  ]
}

Input (answers.json) — SYNTHETIC EXAMPLE:
{
  "case_id": "CASE-DEMO-0091",
  "date_opened": "2026-08-29",
  "investigator": "J. Rivera",
  "account_holder": "Jane Doe",
  "account_age": "19 months",
  "account_status": "Active, under review",
  "summary": "Account showed a self-service password reset followed by a 2FA method downgrade, a successful login from a foreign IP, and a large withdrawal request to a newly added payee.",
  "key_observations": "2FA changed from SMS to email on 8/30, login succeeded from an untrusted device in Bucharest minutes later, and a $4,800 withdrawal to a new payee was submitted the next day.",
  "outcome": "Escalated for further review",
  "next_steps": "Await compliance response"
}
"""

import json
import argparse
from datetime import datetime, timezone


def build_report(template, answers):
    lines = [f"# {template.get('title', 'Report')}", ""]
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append("")

    for section in template.get("sections", []):
        heading = section.get("heading", "Section")
        fields = section.get("fields", [])
        lines.append(f"## {heading}")
        for field in fields:
            value = answers.get(field, "_Not provided_")
            label = field.replace("_", " ").title()
            lines.append(f"**{label}:** {value}")
        lines.append("")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Fill a user-defined report template with case answers.")
    ap.add_argument("template", help="Path to template JSON file")
    ap.add_argument("answers", help="Path to answers JSON file")
    ap.add_argument("-o", "--output", default="report.md")
    args = ap.parse_args()

    with open(args.template) as f:
        template = json.load(f)
    with open(args.answers) as f:
        answers = json.load(f)

    report = build_report(template, answers)

    with open(args.output, "w") as f:
        f.write(report)

    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
