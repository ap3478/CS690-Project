# Gap check adjudication: S-3

Each question from `S-3-gap-check-reply.md` is marked **Real gap** (then decided in section 8 of `S-3.md`, or added there as an open question) or **Answered** (naming the section that already answers it).

| # | Verdict | Resolution |
| --- | --- | --- |
| 1 | Answered | Status line under the story: designed and tested only; tests skipped in M1. |
| 2 | Real gap | Decided, §9: the skip reason format is `"AC-n: S-3 not built in Milestone 1"`. |
| 3 | Real gap | Decided, §9: only the AC tests in M1. |
| 4 | Answered | §8 OQ-1 (ties are open) and the status line (not built). AC-7 uses distinct scores. |
| 5 | Real gap | Decided, §8 D5: within a group, fit score is the only sort key. |
| 6 | Real gap | Decided, §8 D6: exceptions live in `jobsboard.ranking`, subclass `ValueError`, and keep their constructor arguments as attributes. |
| 7 | Real gap | Decided, §8 D6: all input is validated before ranking; the first problem in list order is raised. |
| 8 | Real gap | Decided, §8 D6: duplicate IDs are an exact string match. |
| 9 | Real gap | Decided, §8 D6: `bool` and non-`int` scores raise `InvalidFitScore`. |
| 10 | Real gap | Decided, §8 D6: an empty or whitespace-only skill raises `InvalidSkill(skill)`. |
| 11 | Real gap | Decided, §8 D1: required skills equal after normalizing are one requirement, listed once. |
| 12 | Real gap | Decided, §8 D1: `missing_required` uses the trimmed spelling. |
| 13 | Real gap | Decided, §8 D1: sorted case-insensitively. |
| 14 | Real gap | Decided, §8 D1: `str.casefold()`; no Unicode normalization. |
| 15 | Real gap | Decided, §8 D1: `str.strip()` (leading and trailing whitespace); inner whitespace is not collapsed. |
| 16 | Answered | §4 Interface gives the exact parameter types. |
| 17 | Real gap | Decided, §8 D7: the HTTP endpoint is built with S-4, which adds the score store; M1 covers only `rank_applicants`. |
| 18 | Real gap | Same as 17, §8 D7. |
| 19 | Real gap | Added as open question OQ-4 (applications with no score, and which stages are listed). |
| 20 | Real gap | Added to OQ-4. |
| 21 | Real gap | Deferred with the endpoint, §8 D7. |
| 22 | Answered | §7 covers the empty list for the function; the HTTP behavior is deferred (D7). |
| 23 | Real gap | Deferred with the endpoint, §8 D7. |
| 24 | Real gap | Decided, §8 D7: FastAPI per `AGENTS.md`. |
| 25 | Real gap | Decided, §8 D7: no authentication in M1 (A-4). |
| 26 | Real gap | Decided, §8 D7: no pagination. |
| 27 | Real gap | Decided, §8 D7: a JSON array and `null`; key order does not matter. |
| 28 | Real gap | Decided, §9: AC-8 creates the application through the S-1 HTTP API, calls `rank_applicants`, then checks that `GET /postings/{id}/pipeline` still lists it under Applied. |
| 29 | Answered | §3 Non-goals: scores are input (no S-4 dependency); the S-1 interface is in `S-1.md` §4. |
| 30 | Real gap | Decided, §8 D6: the input list is not mutated. |

Totals: 25 real gaps (23 decided or deferred, plus 2 merged into the new open question OQ-4) and 5 already answered.
