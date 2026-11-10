# Contribution Statement: Project Milestone 1

**Name:** Abraham Eapen, QA & DevOps Lead
**Team:** Internal Jobs Board Portal (Ketan Verma, Aditya Pothuri, Abraham Eapen)

## 1. Personal authorship

- I ran two of the team's five interviews, **INT-04** (hiring manager, [senior manager, technology governance]) and **INT-05** (internal applicant, product manager). Both were in person in the week of 2026-11-02. For both, I wrote the interview questions (Guide A and Guide B in `docs/interviews/questions.md`, revised from our proposal's Appendix C) and the handwritten raw notes of the interviewees' answers. These notes are the source for `docs/interviews/INT-04.md` and `docs/interviews/INT-05.md`.
- I made every project decision the AI tool asked me for:
  - the INT-01 to INT-05 numbering;
  - the "No items" proposal follow-up;
  - the Python + FastAPI + pytest stack;
  - building S-1 (status pipeline) and designing S-3 (ranking);
  - the gap-check method and approving each build task;
  - the scope changes (S-14 below the cut line, S-12 kept below it, moves out of Offer made a non-goal);
  - the public-repository redactions;
  - the participation details.

## 2. AI-assisted authorship

All of the following were produced with Claude Code (Claude Opus 5.5, `claude-opus-5-5`) on 2026-11-09. I reviewed each item and approved it before it was committed.

| Artifact | LEDGER entries |
| --- | --- |
| Transcription of the team's five sets of interview notes into P-numbered files; compliments and predictions list; lesson paragraph | 1 |
| Evidence log (24 E, 7 A, 9 Q) | 2 |
| Backlog (stories, INVEST, acceptance criteria, ranking and cut line; now S-1 to S-14 and AC-1 to AC-20) | 3, 17 |
| Design docs `S-1.md` and `S-3.md`, later trimmed to two pages | 4, 17 |
| Gap checks of both design docs (run in a separate subagent) and their adjudication | 5, 6, 17 |
| `README.md`, `AGENTS.md`, `requirements.txt`, `pytest.ini` | 7 |
| Acceptance tests written before the code (AC-1 to AC-4 passing; AC-6 to AC-8 skipped) | 8 |
| Build plan `docs/plans/S-1-plan.md` and the bounded-task prompts | 9 |
| S-1 code in four bounded tasks (`src/jobsboard/pipeline.py`, `api.py`) | 10, 11, 12, 13 |
| Traceability matrix, report builder, report PDF, this statement's drafts | 14, 15 |
| Ledger SHA roll-ups and fixes | 16, 19 |
| Fixes from the audit against the handout and proposal: Q-4 narrowed, S-14, scope changes in `docs/proposal_followup.md` | 17 |
| Participation table and interview headers, filled from my answers | 18, 21 |
| Public-repository redactions and the git-history rewrite to my GitHub no-reply email | 20 |

## 3. Review

- **AI tool's work.**
  - **Build plan.** Before each of the four bounded tasks, I read the agent's plan and approved it. I approved striking three steps from the build plan that were not asked for: a `GET /applications/{id}` endpoint, a `moved_at` timestamp, and an `Offer → Rejected` move that depends on open question Q-3.
  - **Edge cases.** In the edge-case checks I reviewed after Task 1, unknown application IDs and same-stage moves returned HTTP 500 instead of the 404 and 409 the design doc specifies. Both were fixed in Tasks 2 and 4 (LEDGER entries 11 and 13).
  - **Audit.** I asked the agent to audit the repository against the handout and the proposal. It found that the design docs exceeded two pages, that AC-16 quietly settled part of Q-4, and that two proposal scope items were changed without being recorded. I made the decisions that resolved each one (LEDGER entry 17).
  - **Sensitive data.** I asked about data sensitivity before publishing, and approved generalizing identifying details and rewriting the commit history (LEDGER entry 20).
- **Evidence log.** I compared the 15 E entries that come from my own interviews against my INT-04 and INT-05 notes: E-1 to E-4, E-8 to E-10, E-13, E-14, E-16 to E-20, and E-24. I have not personally checked the 9 E entries that come from INT-01 to INT-03 (E-5 to E-7, E-11, E-12, E-15, E-21 to E-23); they need a check by Aditya or Ketan against their own notes.
- **Teammates' work.** I reviewed Aditya Pothuri's INT-01 and INT-02 notes and Ketan Verma's INT-03 notes. I found minor gaps:
  - INT-02 has no closing "who else should we talk to?" answer.
  - INT-01 and INT-02 used a role-specific question set rather than our shared Guide A.

I confirm that this statement is accurate, and that I can explain any part of the submission I am credited with.

**Signature:** /s/ Abraham Eapen  **Date:** 2026-11-09
