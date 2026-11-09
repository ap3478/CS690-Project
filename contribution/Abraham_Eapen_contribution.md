# Contribution Statement: Project Milestone 1

**Name:** Abraham Eapen, QA & DevOps Lead
**Team:** Internal Jobs Board Portal (Ketan Verma, Aditya Pothuri, Abraham Eapen)

## 1. Personal authorship

- I took part in two of the team's interviews: **INT-04** (hiring manager, [senior manager, technology governance]) and **INT-05** (internal applicant, product manager). For both, I wrote the interview questions (Guide A and Guide B in `docs/interviews/questions.md`, revised from our proposal's Appendix C) and the raw notes of the interviewees' answers. These notes are the source for `docs/interviews/INT-04.md` and `docs/interviews/INT-05.md`.
- I made the project decisions the AI tool asked me for: the INT-01 to INT-05 numbering, the "No items" proposal follow-up, the Python + FastAPI + pytest stack, the choice to build S-1 (status pipeline) and design S-3 (ranking), the gap-check method, and per-task approval of the build.

## 2. AI-assisted authorship

All of the following were produced with Claude Code (Claude Opus 5.5, `claude-opus-5-5`) on 2026-11-09. I reviewed each item and approved it before it was committed.

| Artifact | LEDGER entries |
| --- | --- |
| Transcription of the team's five sets of interview notes into P-numbered files; compliments and predictions list; lesson paragraph | 1 |
| Evidence log (24 E, 7 A, 9 Q) | 2 |
| Backlog: S-1 to S-13, INVEST, AC-1 to AC-19, ranking and cut line | 3 |
| Design docs `S-1.md` and `S-3.md` | 4 |
| Gap checks of both design docs (run in a separate subagent) and their adjudication | 5, 6 |
| `README.md`, `AGENTS.md`, `requirements.txt`, `pytest.ini` | 7 |
| Acceptance tests written before the code (AC-1 to AC-4 passing; AC-6 to AC-8 skipped) | 8 |
| Build plan `docs/plans/S-1-plan.md` and the bounded-task prompts | 9 |
| S-1 code in four bounded tasks (`src/jobsboard/pipeline.py`, `api.py`) | 10, 11, 12, 13 |
| Traceability matrix, report builder, report PDF, this statement's first draft | 14, 15 |

## 3. Review

- **AI tool's work.** Before each of the four bounded tasks, I read the agent's plan and approved it. I approved striking three steps from the build plan that were not asked for: a `GET /applications/{id}` endpoint, a `moved_at` timestamp, and an `Offer → Rejected` move that depends on open question Q-3. I reviewed the drafts of the evidence log, backlog, and design docs and approved them as drafted. The gap check found 24 real gaps in S-1 and 25 in S-3. They were resolved as section 8 decisions or new open questions (OQ-4 in each doc), not guesses. During the build, the edge-case checks I reviewed after Task 1 showed that unknown application IDs and same-stage moves returned HTTP 500 instead of the 404 and 409 the design doc specifies. Both were fixed in Tasks 2 and 4 (LEDGER entries 11 and 13).
- **Teammates' work.** *[TODO before signing: describe what you reviewed of Ketan's and Aditya's work, for example their INT-01 to INT-03 notes, and what you found. If you did not review a teammate's work, say so.]*

I confirm that this statement is accurate, and that I can explain any part of the submission I am credited with.

**Signature:** ______________________________  **Date:** ____________
