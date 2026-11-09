# Gap check reply: S-1.md (verbatim)

- Model: Claude Code subagent, Claude Opus 5.5 (claude-opus-5-5), 2026-11-09
- Input: `prompts/gap_check_prompt.md` plus `docs/design/S-1.md` at commit a5d472e only. The agent was told not to read any other file.
- Adjudication of each question: `docs/design/S-1-gap-adjudication.md`

---

1. What must `allowed_next(Stage.OFFER)` return? It "never raises", but OQ-1 says to stop and ask about moves out of Offer. Should I return an empty set for now, or stay blocked until OQ-1 is answered?
2. Is Offer → Rejected allowed? R1 leaves Offer out of the table, and D2 lists Rejected as reachable only "from Applied, Screened, or Interview." Is a rescinded offer meant to return 409 for now?
3. Does "Stop and ask" in OQ-1–OQ-3 block the whole story, or only the parts that depend on them? Can I ship S-1 with Offer acting as a final stage in the meantime?
4. What format should `application_id` have: a UUID, a sequential integer as a string, or a prefixed ID? Does "never reused" have to hold across restarts, given that the data is in memory and a counter would restart from 1?
5. Must a posting exist before an application can be created for it, or is any `posting_id` string accepted? There is no posting entity or posting endpoint.
6. Does an `applicant_id` made only of whitespace count as "empty"? Should IDs be trimmed? Are there limits on length or allowed characters for `applicant_id` and `posting_id`?
7. Can the same `applicant_id` apply to the same posting more than once? If not, which status code and error body?
8. What should a 422 response body look like? The doc gives exact bodies for 404 and 409 but not for 422. Is FastAPI's default validation body acceptable?
9. When a request has both an unknown `application_id` and an invalid `to_stage`, should it return 404 or 422? Which check runs first?
10. How should non-string `to_stage` / `applicant_id` values (null, numbers, lists) be handled? Should extra fields in the body be ignored or rejected?
11. Should 422 also cover a missing body, malformed JSON, or the wrong Content-Type?
12. In the 409 body, should `from_stage` and `to_stage` be the plain stage strings (e.g. "Screened")? Should the 404 body echo `application_id` exactly as given in the path?
13. Where should `ApplicationNotFound`, `InvalidTransition` and `Application` live: `jobsboard.pipeline`, or a separate module? What base class should the exceptions extend? What are their attribute names (`.application_id`, `.from_stage`, `.to_stage`)?
14. What kind of type is `Application`: a dataclass, a Pydantic model, or a plain class? Is it mutable or frozen?
15. Does `move_stage` change the stored `Application` in place or replace it? Does `get` return the stored object or a copy that callers cannot change?
16. Should `ApplicationStore.create` check for empty `posting_id` / `applicant_id` itself (and raise what?), or is that check only done in the HTTP layer?
17. What order should `list_for_posting` return? The pipeline lists use "creation order", but the store method has no stated order.
18. How is the store wired into the FastAPI app: a module-level singleton, `app.state`, or a dependency override? How do tests get a fresh, empty store for each test?
19. Do moves need to be safe under concurrent requests (locking), or can I assume a single worker with no races?
20. Should the success response for POST create include a `Location` header? Is any extra endpoint expected, such as `GET /applications/{id}`?
21. Must the `stages` object in the pipeline response always have its keys in the order Applied, Screened, Interview, Offer, Rejected?
22. Should `allowed_next` handle inputs that are not a `Stage` (e.g. the raw string "Applied") without raising, and if so what should it return?
23. The problem statement is about audits. Should moves record a history or timestamp (who moved it, when, from which stage)? Section 5 lists no such fields.
24. What exactly does each acceptance test set up and assert? Only the test names are given. Should they go through HTTP (TestClient) or the domain functions? For the refused moves (AC-2, AC-4), should they check the full 409 body and R4 (pipeline unchanged)?
25. Am I expected to write tests for the edge cases in section 7 and for R3–R5 beyond AC-1–AC-4? Should the tests for the 404/422 cases also go in `tests/test_s1_pipeline.py`?
26. Which Python, FastAPI and Pydantic versions should I target? How is the package laid out (pyproject.toml, src/ layout or not)? Which test runner and HTTP client should I use?
27. What do A-1 to A-4, E-5 to E-7 and Q-1 to Q-7 say? They are cited but not included. Do they hold constraints I would otherwise miss?
28. How should `posting_id` / `application_id` path values with URL-encoded or special characters be handled? Should a trailing slash on a path be accepted?
