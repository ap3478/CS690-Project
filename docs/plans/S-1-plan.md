# Plan: S-1 status pipeline

Written by Claude Code (Claude Opus 5.5) from `prompts/s1_plan_prompt.md`, before any code was edited. Reviewed by Abraham Eapen. Struck-out steps were not asked for and were removed before work began.

## How

**Files that change**
- `src/jobsboard/pipeline.py` (new). `Stage` enum, `Application` frozen dataclass, `PipelineError`, `ApplicationNotFound`, `InvalidTransition`, the `_ALLOWED` transition table, `allowed_next()`, `ApplicationStore`, and `move_stage()` (S-1.md §4, D10).
- `src/jobsboard/api.py` (new). FastAPI `app`, the module-level `ApplicationStore`, Pydantic request bodies (`applicant_id: str`, `to_stage: Stage`), and the three routes in S-1.md §4. Domain errors map to 404 and 409 (D5, D9).
- `src/jobsboard/__init__.py` already exists and is empty. It is not changed.

**Files that must not change:** `tests/`, `docs/`, `backlog/`, `evidence/`, `LEDGER.md`, `prompts/`, `AGENTS.md`, `requirements.txt`.

**Data storage:** in memory (D4). `ApplicationStore` holds a `dict[str, Application]` keyed by `application_id`. Python dicts keep insertion order, which gives creation order for `list_for_posting` (D10). A move replaces the frozen record under the same key. There is no database and no file I/O.

## Tasks

1. **AC-1. Forward move Applied → Screened is listed under Screened.** Create `pipeline.py` with `Stage`, `Application`, the store, `allowed_next` holding the full R1 table (D6: Offer → empty set), and `move_stage`. Create `api.py` with all three routes. Check: `test_ac1_applied_to_screened_listed_under_screened` passes.
2. **AC-2. A skip move Applied → Interview is refused with 409 naming both stages, and the pipeline is unchanged.** Map `InvalidTransition` to 409 `{"error": "invalid_transition", "from_stage", "to_stage"}`. Check: `test_ac2_skip_applied_to_interview_refused` passes.
3. **AC-3. Interview → Rejected is listed under Rejected.** Confirm that the R1 table allows Rejected from Interview. Check: `test_ac3_interview_to_rejected_listed_under_rejected` passes.
4. **AC-4. Rejected → Screened is refused, and the application stays under Rejected.** Confirm that Rejected maps to an empty set (D3) and that `ApplicationNotFound` maps to 404. Check: `test_ac4_rejected_to_screened_refused` passes, and the full suite shows 4 passed and 3 skipped.

## Struck before work began

- ~~Add a `GET /applications/{application_id}` endpoint for convenience.~~ Not in S-1.md §4 (D11).
- ~~Add a `moved_at` timestamp to `Application` for auditing.~~ A non-goal in S-1.md §3.
- ~~Add `Offer → Rejected` to the transition table.~~ This depends on OQ-1 (Q-3): stop and ask.
