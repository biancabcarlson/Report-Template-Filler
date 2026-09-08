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
    {"heading": "Suspected Fraud Dates", "fields": ["start", "end"]},
    {"heading": "Findings", "fields": ["summary", "key_observations"]},
    {"heading": "Transactions Captured", "fields": ["transactions_captured", "transactions_total"]},
    {"heading": "Documents Collected", "fields": ["documents_collected"]},
    {"heading": "Paste other tools output here", "fields": ["tool_output"]},
    {"heading": "Disposition (If Confirmed Fraud)", "fields": ["outcome", "next_steps"]}
  ]
}

Input (answers.json) — SYNTHETIC EXAMPLE:
{
  "case_id": "CASE-DEMO-0091",
  "date_opened": "2026-08-29",
  "investigator": "J. Rivera",
  "account_holder": "Jane Doe",
  "account_age": "1 yr 7 months",
  "account_status": "Active, under review",
  "start": "2026-08-29",
  "end": "2026-08-31",
  "summary": "Account showed a self-service password reset followed by a 2FA method downgrade, a successful login from a foreign IP, and a large withdrawal request to a newly added payee.",
  "key_observations": "2FA changed from SMS to email on 8/30, login succeeded from an untrusted device in Bucharest minutes later, and a $4,800 withdrawal to a new payee was submitted the next day.",
  "transactions_captured": "Aug 31 ACH Withdrawal $4,800.00 (Ref ACH-88300, pending); Aug 31 Crypto Withdrawal $4,590.00 (new wallet)",
  "transactions_total": "$9,390.00",
  "documents_collected": "August 2026 account statement\nID on file (CA Driver's License, IDVerify Co.)\nAccount agreement (signed Jan 14, 2025)",
  "tool_output": "(paste results from other tools here, e.g. Case Timeline Builder's Copy Timeline button)",
  "outcome": "Confirmed — ATO",
  "next_steps": "Secure the account and correct any changed PII with the True Party's information."
}

Note: the web demo renders Transactions Captured as an editable totals
block (see index.html) rather than free-text fields, since it's a running
total pulled from the case's transaction data. The CLI has no concept of
"fixed" vs. "editable" fields — it's fully generic — so the example above
models the same section as two ordinary text fields instead. Swap in
whatever fields fit your own template. Fields with one item per line
(like "documents_collected" above) are rendered as plain text by this
CLI — the web demo's bulleted-list rendering is a display-only difference,
not a data-format one.
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
