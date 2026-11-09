# Gap check adjudication: S-1

Each question from `S-1-gap-check-reply.md` is marked **Real gap** (then decided in `S-1.md`, or added to §8 as an open question) or **Answered** (naming the section that already answered it). Section references are to the trimmed two-page `S-1.md` (LEDGER entry 17).

| # | Verdict | Resolution in S-1.md |
| --- | --- | --- |
| 1 | Real gap | §3 non-goal "no moves out of Offer (OQ-1)"; R1 lists Offer → {}. |
| 2 | Real gap | Same as 1. |
| 3 | Real gap | §3: S-1 ships without moves out of Offer; only that behavior waits on OQ-1. |
| 4 | Real gap | §5: `uuid4().hex`, unique within a run. |
| 5 | Real gap | §5: any non-empty `posting_id`; no posting entity until S-6. |
| 6 | Real gap | §4: blank `applicant_id` → 422. §5: stored as given, no length limit. |
| 7 | Real gap | New open question OQ-4. |
| 8 | Real gap | §8 D2: FastAPI's default 422 body. |
| 9 | Real gap | §8 D2: validation runs before the lookup (404). |
| 10 | Real gap | §4: non-string → 422. §8 D2: extra fields are ignored. |
| 11 | Real gap | §4: a bad body → 422. |
| 12 | Answered | §4: the 409 body names the stages; the 404 body echoes `application_id`. |
| 13 | Real gap | §8 D4: all types in `jobsboard.pipeline`; `PipelineError(Exception)` base; attributes are the constructor arguments. |
| 14 | Real gap | §8 D4: `Application` is a frozen dataclass. |
| 15 | Real gap | §8 D4: frozen, so a move stores a replacement record. |
| 16 | Real gap | §8 D2: validation happens only in the HTTP layer. |
| 17 | Real gap | §8 D3: creation order is kept. |
| 18 | Real gap | §8 D3: a module-level store in `jobsboard.api`; tests isolate themselves with a unique `posting_id`. |
| 19 | Real gap | §8 D3: a single worker with no locking. |
| 20 | Real gap | §2: three endpoints only. §4 specifies no headers. |
| 21 | Answered | §4: the `stages` keys are listed in order. |
| 22 | Answered | §4: `allowed_next` takes a `Stage`. |
| 23 | Real gap | §3 non-goal: no move history. |
| 24 | Real gap | §9 and the test file: tests go through HTTP; refusal tests check R4. |
| 25 | Real gap | §9 lists only the AC tests; §7 edge cases are checked by hand and logged in `LEDGER.md`. |
| 26 | Real gap | §8 D3: the stack is the one in `AGENTS.md`. |
| 27 | Answered | IDs are defined in `evidence/evidence_log.md`; §6 and §8 state every constraint that applies. |
| 28 | Real gap | §8 D2: FastAPI default path handling. |

Totals: 24 real gaps (23 decided, 1 new open question) and 4 already answered.
