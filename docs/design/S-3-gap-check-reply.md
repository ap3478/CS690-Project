# Gap check reply: S-3.md (verbatim)

- Model: Claude Code subagent, Claude Opus 5.5 (claude-opus-5-5), 2026-11-09
- Input: `prompts/gap_check_prompt.md` plus `docs/design/S-3.md` at commit a5d472e only. The agent was told not to read any other file.
- Adjudication of each question: `docs/design/S-3-gap-adjudication.md`

---

1. The status says "Not built in Milestone 1" and the tests are skipped. Am I building this now, or only writing the skipped tests? If I build it, do the tests stay skipped?
2. Does `tests/test_s3_ranking.py` already exist, or do I write it? What is the exact wording or format of the skip reason that "names the AC"?
3. Do the edge cases in section 7 need their own tests, or is covering AC-6, AC-7 and AC-8 enough?
4. Ties in `fit_score` (OQ-1) need some order, because any sort produces one. Should I keep the input order (stable sort), sort by `application_id`, or not build at all until someone answers? Does "stop and ask" block the whole story?
5. Within the flagged group, should anything break ties or set order besides score, such as the number of missing required skills? Or is score the only key?
6. In which module are `InvalidFitScore` and `DuplicateApplication` defined? What base class do they use (ValueError, a custom base)? Are `application_id` and `fit_score` stored as attributes with those names? What should the message say?
7. Are all candidates checked before anything is returned? If one input has both an invalid score and a duplicate ID, which exception wins? Does the first error found in list order win?
8. Is a duplicate ID an exact string match, or are IDs normalized (trimmed, case-folded) before comparing?
9. Should `bool` scores be rejected (`True` is an `int` in Python)? What about floats like `50.0` or other non-int types? If so, which exception?
10. The data rules say each skill must be a non-empty string. Do I validate that? If a skill is empty or only whitespace (which becomes empty after trimming), what is raised: `ValueError`, a new exception, or is it silently ignored?
11. Two required skills can become the same after normalizing (for example `"Java"` and `" java "`). Is that one requirement or two? If one is missing, which spelling goes in `missing_required`, and does it appear once or twice?
12. Does "the posting's spelling" in `missing_required` mean the raw string with its whitespace, or the trimmed one?
13. Is the alphabetical sort of `missing_required` case-sensitive (Python's default) or case-insensitive?
14. What exactly does "ignoring case" mean: `str.lower()` or `str.casefold()`? Should Unicode normalization (NFC/NFKC) apply?
15. What exactly does "trimming whitespace" cover: only leading and trailing ASCII spaces, or all Unicode whitespace? Is internal whitespace collapsed (`"machine  learning"` vs `"machine learning"`)?
16. Should `rank_applicants` accept any iterable or set for `required_skills` and any sequence for `candidates`, or enforce the declared types exactly?
17. For the HTTP endpoint, where do a posting's required skills and its applications' skills come from? Which repository or store, and which module or function do I call?
18. Where do the fit scores come from at request time if S-4 is not built? Do I call S-4 code, read a stored score, or stub it? What does a stub return?
19. What happens to an application that has no fit score yet? Excluding it breaks R5, and there is no defined error.
20. Does "every applicant" include applications in every stage (rejected, withdrawn, hired), or only active ones?
21. If a stored score is out of range or a stored application is duplicated, what HTTP status and body comes back: 500, 422, or something else?
22. Does a posting with zero applications return 200 with `[]`? Do closed or archived postings return the list or 404?
23. What is the type and format of `posting_id`? Does a badly formed ID return 404 `posting_not_found` or the framework's 422?
24. Which web framework and app or router do I register the route in? The `{"detail": ...}` shape suggests FastAPI, but the doc never says.
25. Is there authentication or authorization on this endpoint (recruiters only)? If so, what do unauthorized callers get?
26. Is there pagination or a size limit on the ranked list?
27. Should `missing_required` be a JSON array and `flag` a JSON `null`? Should response keys follow exactly the listed order?
28. For R6, which S-1 endpoint is "the S-1 pipeline response", and what request do I compare before and after? Does AC-8 test this through HTTP or at the domain level?
29. Can I assume S-1 (stages) and S-4 (scores) exist and have known interfaces I can depend on, or must I mock them? If I mock them, with what shapes?
30. Is the input `candidates` list allowed to be mutated, or must it stay untouched? The doc implies no side effects but only states that for stages.
