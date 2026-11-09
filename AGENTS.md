# AGENTS.md — standing instructions for AI coding tools

These rules apply to every AI coding session in this repository (Claude Code, Copilot, or any other agent).

## Stack
- Language: Python 3.12 (3.11+ supported).
- Framework: FastAPI for the HTTP API; plain Python dataclasses and Enums for the domain.
- Tests: pytest, using FastAPI's `TestClient` (httpx) for HTTP tests.
- Source lives in `src/jobsboard/`; tests live in `tests/`.

## Test command
```bash
python -m pytest -q
```
Run it before you say a task is done, and report the exact output.

## Workflow rules
1. **Show a plan and wait.** Before editing any file, list the files you will change and what you will change in each, then stop and wait for explicit approval from a human team member.
2. Work on one bounded task at a time. A task implements one acceptance criterion from a design doc in `docs/design/`.
3. Change only the files the task prompt names.
4. Stop when the check named in the task prompt passes. Do not continue to the next task on your own.
5. If the design doc does not answer something you need, **stop and ask**. Never invent a value for anything listed as an open question in section 8 of a design doc, or as a Q entry in `evidence/evidence_log.md`.

## Files and folders you must not change
- `tests/` — tests are written from acceptance criteria before the code. Never change an expected value, delete a test, or remove a skip marker to make code pass. If you think a test is wrong, stop and say why.
- `docs/design/`, `backlog/`, `evidence/`, `docs/interviews/` — requirements and evidence are owned by the team.
- `LEDGER.md` and `prompts/` — the team writes these.
- `requirements.txt` — ask before adding a dependency.
- `AGENTS.md` — this file.

## Code conventions
- Type hints on every function parameter and return value.
- Domain errors are exception classes in the domain module. The API turns them into the HTTP status codes and JSON bodies given in the design doc.
- No network calls, LLM calls, or databases in Milestone 1. Use the in-memory store.
