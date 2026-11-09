"""Assemble report/REPORT.md from the repository files (stdlib only).

Usage:  python report/build_report.py
The PDF is rendered from REPORT.md separately (see report/README.md).
"""
from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "[TODO: GitHub repository URL]"  # set before submission


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def demote(md: str, by: int = 2, drop_title: bool = True) -> str:
    """Push headings down `by` levels; optionally drop the file's first H1."""
    out, dropped = [], False
    in_code = False
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and drop_title and not dropped and line.startswith("# "):
            dropped = True
            continue
        if not in_code and re.match(r"^#{1,5} ", line):
            line = "#" * by + line
        out.append(line)
    return "\n".join(out).strip() + "\n"


def sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "[commit SHA]"


def trace_table() -> str:
    rows = list(csv.reader((ROOT / "traceability/traceability.csv").open(encoding="utf-8")))
    head = "| Evidence ID | Story ID | AC ID | Test name |\n| --- | --- | --- | --- |\n"
    body = "".join(f"| {r[0].replace(';', ', ')} | {r[1]} | {r[2]} | `{r[3]}` |\n" if r[3] != "Not yet written"
                   else f"| {r[0].replace(';', ', ')} | {r[1]} | {r[2]} | Not yet written |\n" for r in rows[1:])
    return head + body


TOC = [
    ("d1", "1. Proposal follow-up", "this PDF"),
    ("d2", "2. User interviews (questions, notes, participation, compliments and predictions, lesson)", "docs/interviews/"),
    ("d3", "3. Evidence log", "evidence/evidence_log.md"),
    ("d4", "4. Backlog (stories, trace, INVEST, AC, ranking)", "backlog/backlog.md"),
    ("d5", "5. Design docs S-1 and S-3, with gap checks", "docs/design/"),
    ("d6", "6. Repository, tests, first story (6e test output in this PDF)", "README.md, AGENTS.md, docs/plans/S-1-plan.md, src/, tests/"),
    ("d7", "7. Traceability matrix", "traceability/traceability.csv"),
    ("d8", "8. Provenance ledger", "LEDGER.md, prompts/"),
    ("d9", "9. Contribution statements (individual, submitted separately)", "contribution/"),
]


def build() -> str:
    p: list[str] = []
    p.append("# CS 690 Project Milestone 1: Internal Jobs Board Portal\n")
    p.append("Team: Ketan Verma, Aditya Pothuri, Abraham Eapen  \n"
             f"Repository: {REPO_URL}  \nSubmitted commit: `{sha()}`\n")

    p.append('## Table of contents {#toc}\n')
    p.append("| Deliverable | Page | Repository path |\n| --- | --- | --- |\n" +
             "".join(f"| [{t}](#{a}) | <a class='pageref' href='#{a}'></a> | `{path}` |\n" for a, t, path in TOC))

    p.append('\n## 1. Proposal follow-up {#d1}\n\nNo items.\n')

    p.append('\n## 2. User interviews {#d2}\n')
    p.append("### 2a. Interview questions\n" + demote(read("docs/interviews/questions.md"), 2))
    p.append("### 2b. Participation table\n" + demote(read("docs/interviews/participation.md"), 2))
    for n in range(1, 6):
        p.append(f"### 2c. Raw notes: {read(f'docs/interviews/INT-0{n}.md').splitlines()[0][2:]}\n"
                 + demote(read(f"docs/interviews/INT-0{n}.md"), 2))
    p.append("### 2d. Compliments and predictions\n" + demote(read("docs/interviews/compliments_predictions.md"), 2))
    p.append("### 2e. AI summaries\n\nNone. No interview was transcribed or summarized by an AI tool.\n")
    p.append("### Most useful thing we learned\n" + demote(read("docs/interviews/lesson.md"), 2))

    p.append('\n## 3. Evidence log {#d3}\n' + demote(read("evidence/evidence_log.md"), 1))
    p.append('\n## 4. Backlog {#d4}\n' + demote(read("backlog/backlog.md"), 1))

    p.append('\n## 5. Design docs {#d5}\n')
    for s in ("S-1", "S-3"):
        p.append(f"### Design doc {s} (`docs/design/{s}.md`)\n" + demote(read(f"docs/design/{s}.md"), 2))
        p.append(f"### Gap check for {s}: model reply (`docs/design/{s}-gap-check-reply.md`)\n"
                 + demote(read(f"docs/design/{s}-gap-check-reply.md"), 2))
        p.append(f"### Gap check for {s}: adjudication\n" + demote(read(f"docs/design/{s}-gap-adjudication.md"), 2))

    p.append('\n## 6. Repository and first story {#d6}\n\n'
             "Repository items: `README.md` (install and the one test command `python -m pytest -q`), "
             "`AGENTS.md`, `docs/design/`, `docs/plans/S-1-plan.md`, `src/jobsboard/`, `tests/`, `LEDGER.md`, `prompts/`. "
             "S-1 was built in four bounded tasks (LEDGER entries 10 to 13).\n\n"
             "### 6e. Test output on a fresh clone\n\n"
             "`git clone … && python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt && .venv/bin/python -m pytest -q`\n\n"
             "```text\n" + read("report/test_output_6e.txt").strip() + "\n```\n")

    p.append('\n## 7. Traceability matrix {#d7}\n\n' + trace_table())
    p.append('\n## 8. Provenance ledger {#d8}\n\nSee `LEDGER.md` at the repository root and `prompts/`.\n')
    p.append('\n## 9. Contribution statements {#d9}\n\nSubmitted individually by each member on Canvas; source in `contribution/`.\n')
    return "\n".join(p)


if __name__ == "__main__":
    (ROOT / "report/REPORT.md").write_text(build(), encoding="utf-8")
    print("wrote report/REPORT.md")
