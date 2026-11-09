# Gap check adjudication: S-1

Each question from `S-1-gap-check-reply.md` is marked **Real gap** (then decided in section 8 of `S-1.md`, or added there as an open question) or **Answered** (naming the section that already answers it).

| # | Verdict | Resolution |
| --- | --- | --- |
| 1 | Real gap | Decided, §8 D6: `allowed_next(Offer)` returns an empty set until OQ-1 is answered, and no test depends on moves out of Offer. |
| 2 | Real gap | Same as 1, §8 D6. |
| 3 | Real gap | Decided, §8 D6: open questions block only the behavior that depends on them; the rest of S-1 ships. |
| 4 | Real gap | Decided, §8 D7: `application_id` is a UUID4 hex string; "never reused" holds within one run (D4). |
| 5 | Real gap | Decided, §8 D8: any non-empty `posting_id` is accepted; there is no posting entity until S-6. |
| 6 | Real gap | Decided, §8 D8: whitespace-only counts as empty (422); IDs are stored as given; no length limits in M1. |
| 7 | Real gap | Added as open question OQ-4 (duplicate applications). |
| 8 | Real gap | Decided, §8 D9: FastAPI's default 422 body; tests check only the status code. |
| 9 | Real gap | Decided, §8 D9: body validation (422) runs before the lookup (404). |
| 10 | Real gap | Decided, §8 D9: non-string values return 422; extra body fields are ignored. |
| 11 | Real gap | Decided, §8 D9: a missing or malformed body returns 422. |
| 12 | Answered | §4 Interface: the 409 body carries the stage strings shown in the Stage enum, and the 404 body echoes `application_id`. |
| 13 | Real gap | Decided, §8 D10: all types live in `jobsboard.pipeline`; exceptions subclass `PipelineError(Exception)`; attribute names match the constructor parameters in §4. |
| 14 | Real gap | Decided, §8 D10: `Application` is a frozen dataclass. |
| 15 | Real gap | Decided, §8 D10: a move stores a replaced record; `get` returns that frozen record. |
| 16 | Real gap | Decided, §8 D8: input validation happens in the HTTP layer only. |
| 17 | Real gap | Decided, §8 D10: `list_for_posting` returns creation order. |
| 18 | Real gap | Decided, §8 D11: a module-level store in `jobsboard.api`; tests isolate themselves with a unique `posting_id` per test. |
| 19 | Real gap | Decided, §8 D11: a single worker is assumed; no locking. |
| 20 | Real gap | Decided, §8 D11: no `Location` header and no other endpoints. |
| 21 | Answered | §4 Interface lists the `stages` keys in order; D10 also states it. |
| 22 | Answered | §4 Interface: `allowed_next` takes a `Stage`; other input types are outside the contract. |
| 23 | Real gap | Added to §3 Non-goals: no move history or timestamps in M1. |
| 24 | Real gap | Decided, §9: tests go through HTTP (`TestClient`); refused-move tests check the 409 body and an unchanged pipeline (R4). |
| 25 | Real gap | Decided, §9: the file holds only the AC tests; §7 edge cases are checked by hand during each task and logged in `LEDGER.md`. |
| 26 | Real gap | Decided, §8 D11: the stack is given in `AGENTS.md` (Python 3.12, FastAPI, pytest, `src/` layout). |
| 27 | Answered | Evidence IDs are defined in `evidence/evidence_log.md`. The builder was isolated on purpose; §6 and §8 state every constraint that applies. |
| 28 | Real gap | Decided, §8 D9: FastAPI's default path handling; no trailing-slash variants. |

Totals: 24 real gaps (22 decided, 1 new open question, 1 new non-goal) and 4 already answered.
