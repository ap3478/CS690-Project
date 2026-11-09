# Gap check adjudication: S-3

Each question from `S-3-gap-check-reply.md` is marked **Real gap** (then decided in `S-3.md`, or added to §8 as an open question) or **Answered** (naming the section that already answered it). Section references are to the trimmed two-page `S-3.md` (LEDGER entry 17).

| # | Verdict | Resolution in S-3.md |
| --- | --- | --- |
| 1 | Answered | Status line: designed and tested only; not built in M1. |
| 2 | Real gap | §9: skipped, with a reason that names the AC (`"AC-n: S-3 not built in Milestone 1"` in the test file). |
| 3 | Real gap | §9 lists only the AC tests. |
| 4 | Answered | §8 OQ-1 (ties are open) and the status line (not built). |
| 5 | Real gap | §8 D2: fit score is the only sort key within a group. |
| 6 | Real gap | §4 names the exceptions; §8 D3: they subclass `ValueError` and keep their constructor arguments as attributes. |
| 7 | Real gap | §8 D3: all input is validated first; the first problem in list order is raised. |
| 8 | Real gap | §8 D3: duplicate IDs are exact string matches. |
| 9 | Real gap | §5: `bool` scores are not accepted; §4 raises `InvalidFitScore`. |
| 10 | Real gap | §5: every skill is non-empty after trimming; §4 raises `InvalidSkill`. |
| 11 | Real gap | §8 D1: equal-after-normalizing required skills count as one. §5: listed once. |
| 12 | Real gap | §5: the trimmed spelling. |
| 13 | Real gap | §5: sorted case-insensitively. |
| 14 | Real gap | §6 R1: `casefold()`. §8 D1: no Unicode normalization. |
| 15 | Real gap | §6 R1: `strip()`. §8 D1: inner spaces are not collapsed. |
| 16 | Answered | §4 gives the exact parameter types. |
| 17 | Real gap | §8 D4: the endpoint is built with S-4, whose score store feeds it. |
| 18 | Real gap | Same as 17. |
| 19 | Real gap | New open question OQ-4. |
| 20 | Real gap | Merged into OQ-4. |
| 21 | Real gap | Deferred with the endpoint (§8 D4). |
| 22 | Answered | §7 covers the empty list for the function; HTTP is deferred (D4). |
| 23 | Real gap | Deferred with the endpoint (§8 D4). |
| 24 | Real gap | §8 D4: FastAPI per `AGENTS.md`. |
| 25 | Real gap | §8 D4: no authentication (A-4). |
| 26 | Real gap | §8 D4: no pagination. |
| 27 | Real gap | §4: a JSON list, with `flag` `null` when absent. |
| 28 | Real gap | §9: AC-8 checks R6 through the S-1 pipeline endpoint. |
| 29 | Answered | §3: scores are input from S-4. The S-1 interface is in `S-1.md` §4. |
| 30 | Real gap | §6 R6: the input list is unchanged. |

Totals: 25 real gaps (23 decided or deferred, plus 2 merged into OQ-4) and 5 already answered.
