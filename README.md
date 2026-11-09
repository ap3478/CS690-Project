# Internal Jobs Board Portal — CS 690 Project, Milestone 1

An internal jobs board for mid-size companies. HR recruiters post roles, employees apply, and recruiters move each applicant through a status pipeline (Applied → Screened → Interview → Offer, or Rejected). Recruiters will later see applicants ranked by fit against the job description.

Team: Ketan Verma, Aditya Pothuri, Abraham Eapen.

**Milestone 1 builds one story, S-1 (status pipeline).** Story S-3 (ranked applicants) is designed and tested, but its tests are skipped because it is not built yet.

## Requirements

- Python 3.11 or later (developed on 3.12)
- Dependencies pinned in `requirements.txt` (FastAPI, httpx, pytest, uvicorn)

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run all the tests (one command)

```bash
python -m pytest -q
```

Expected at the Milestone 1 commit: all S-1 tests pass, and the S-3 tests are reported as skipped, each with a reason that names its AC ID.

## Run the API locally (optional)

```bash
uvicorn jobsboard.api:app --app-dir src --reload
```

Then open `http://127.0.0.1:8000/docs`.

## Repository map

| Path | What it holds | Deliverable |
| --- | --- | --- |
| `docs/proposal_followup.md` | Approval items and scope changes since the proposal | 1 |
| `docs/interviews/` | Interview questions, raw notes INT-01 to INT-05, participation table, compliments and predictions, lesson learned | 2 |
| `evidence/evidence_log.md` | E, A, and Q evidence log | 3 |
| `backlog/backlog.md` | Stories S-1 to S-14, evidence trace, INVEST, AC-1 to AC-20, ranking and cut line | 4 |
| `docs/design/` | Design docs `S-1.md` and `S-3.md`, gap-check replies and adjudication | 5 |
| `docs/plans/S-1-plan.md` | Agent-written build plan for S-1 | 6c |
| `src/jobsboard/` | Application code | 6d |
| `tests/` | Acceptance tests (AC ID in each test name) | 6b |
| `traceability/traceability.csv` | Evidence → story → AC → test | 7 |
| `LEDGER.md`, `prompts/` | Provenance ledger and every prompt it references | 8 |
| `report/REPORT.md` | Source for the submitted PDF | all |
| `AGENTS.md` | Standing instructions for the AI coding tool | 6a |
