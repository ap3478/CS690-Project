# 4. Backlog

Evidence IDs refer to `evidence/evidence_log.md`. Stages are written as in A-1: Applied, Screened, Interview, Offer, Rejected.
Named settings stand for values the interviews did not settle. No criterion picks a number for them.

| Setting | Meaning | Open because |
| --- | --- | --- |
| `APPLICANT_STAGE_LABELS` | Map from each internal stage to the label an applicant sees | Q-1 |
| `ERASURE_MAX_MINUTES` | Longest time between an erasure request and full removal | Our proposal says 5; no interviewee or Legal contact has confirmed it |
| `EXPLANATION_MAX_WORDS` | Maximum length of a fit explanation | A-7; no evidence |

## 4a, 4b. Stories and evidence trace

| ID | Story (Connextra) | Evidence trace |
| --- | --- | --- |
| S-1 | As an **HR recruiter**, I want to move each applicant forward one stage at a time (Applied → Screened → Interview → Offer), or to Rejected, with any other move refused, so that the pipeline shows each applicant's true stage and I don't rebuild stage data by hand for reports and audits. | E-5, E-6, E-7. The move rules rest on A-1, A-2, A-3. |
| S-2 | As an **internal applicant**, I want to see my application's current stage on the board so that I am not left on "Submitted" for weeks or chasing the recruiter for news. | E-1, E-2, E-3 |
| S-3 | As an **HR recruiter**, I want all applicants for a posting listed by fit score, with anyone missing a required skill flagged "Does not meet minimum" and never ranked above an applicant who meets them all, so that I review qualified candidates first instead of reading every resume. | E-11, E-12, E-13, E-14. The meaning of "meets minimum" rests on A-5. |
| S-4 | As an **HR recruiter**, I want each application to show a 0–100 fit score with the required and preferred skills matched and missing, so that I can see quickly how a resume maps to the job description. | E-11, E-13 |
| S-5 | As an **internal applicant**, I want the system not to notify my current manager when I apply, so that I can explore a move without risk to my current role. | E-8, E-9, E-10 |
| S-6 | As an **HR recruiter**, I want to post a job with title, description, level, location, and required and preferred skills on the internal board, so that employees can see in one place whether a role is open to them. | E-10, E-16 |
| S-7 | As an **internal applicant**, I want to apply from the posting with my employee account, without creating a separate candidate account or retyping my work history, so that applying internally is no harder than applying externally. | E-16, E-17 |
| S-8 | As an **internal applicant**, I want to upload my resume as PDF or DOCX, so that I don't have to convert it before applying. | E-18, E-19 |
| S-9 | As an **applicant**, I want to request deletion of my application data and see that it was removed, so that I know my resume does not stay on file. | E-20 |
| S-10 | As an **HR recruiter**, I want withdrawn applicants recorded separately from rejected ones, so that compliance exports don't need cleaning by hand. | E-6 |
| S-11 | As a **hiring manager**, I want to compare shortlisted candidates side by side with their fit scores and matched and missing skills, so that I don't keep a personal spreadsheet. | E-15 |
| S-12 | As an **HR recruiter**, I want a short written explanation of each applicant's fit, so that I can pass the reasoning to the hiring manager. | **Assumption**, rests on A-7. Clarifying question: *"The last time you wrote up why a candidate fit a role, what did you include, who read it, and how long did it take?"* |
| S-13 | As an **internal applicant**, I want a rejection notice that tells me the stage I reached and whom to ask for feedback, so that I can learn why without relying on knowing the hiring manager. | E-3, E-4 |

## 4c. INVEST check

P = pass. Each fail names the specific problem.

| Story | I | N | V | E | S | T |
| --- | --- | --- | --- | --- | --- | --- |
| S-1 | P | P | P | P | P | P |
| S-2 | **Fail:** depends on S-1 being built first; there is no stage to show until a recruiter can change it. | P | P | P | P | P |
| S-3 | **Fail:** depends on S-4 producing fit scores and matched skills. | P | P | **Fail:** cannot size the override work until Q-5 (recruiter override of the flag) is answered. | P | P |
| S-4 | P | P | P | **Fail:** skill extraction method (LLM vs keyword and synonym matching, Q-9) is not chosen. | **Fail:** covers skill extraction, scoring, and display, more than one iteration. Split extraction from scoring. | P |
| S-5 | **Fail:** depends on S-1, because the notify point (Q-7) is a pipeline stage. | P | P | P | P | P |
| S-6 | P | P | P | P | P | P |
| S-7 | P | P | P | **Fail:** effort depends on whether employee sign-in must use SSO (A-4, Q-8). | P | P |
| S-8 | **Fail:** depends on S-7, since a resume is uploaded as part of an application. | P | P | P | P | P |
| S-9 | **Fail:** depends on S-7 and S-8 deciding where application data and files are stored. | P | P | **Fail:** removal across the database and file storage, plus an anonymized audit record, cannot be sized before storage is chosen. | P | P |
| S-10 | **Fail:** depends on S-1's stage model. | **Fail:** blocked by Q-4 (who can set Withdrawn). | P | P | P | P |
| S-11 | **Fail:** depends on S-4 for scores and skills. | P | P | P | P | P |
| S-12 | **Fail:** depends on S-4. | P | **Fail:** value rests only on A-7; no interview supports it. | P | P | **Fail:** "a good explanation" has no objective check beyond length and named skills. |
| S-13 | **Fail:** depends on S-1 (needs the Rejected move). | P | P | P | P | P |

## 4d. Acceptance criteria

| AC | Story | Given | When | Then |
| --- | --- | --- | --- | --- |
| AC-1 | S-1 | an application for posting P is at Applied | the recruiter moves it to Screened | the pipeline view for P lists the application under Screened and no longer under Applied |
| AC-2 | S-1 | an application for posting P is at Applied | the recruiter tries to move it straight to Interview | the request is refused with an "invalid transition" error naming Applied and Interview, and the pipeline view for P still lists it under Applied |
| AC-3 | S-1 | an application for posting P is at Interview | the recruiter moves it to Rejected | the pipeline view for P lists the application under Rejected |
| AC-4 | S-1 | an application for posting P is at Rejected | the recruiter tries to move it to Screened | the request is refused with an "invalid transition" error naming Rejected and Screened, and the pipeline view for P still lists it under Rejected |
| AC-5 | S-2 | the recruiter has moved the applicant's application to Interview | the applicant opens their applications list | the application shows the label `APPLICANT_STAGE_LABELS["Interview"]`, not "Submitted" |
| AC-6 | S-3 | posting P requires {Java, kdb+}; applicant A has both with fit score 40; applicant B has only Java with fit score 90 | the recruiter opens the ranked list for P | A is listed above B, and B shows the flag "Does not meet minimum" while A shows no flag |
| AC-7 | S-3 | posting P requires {Java}; applicants A, B, C all have Java, with fit scores 55, 80, 70 | the recruiter opens the ranked list for P | the list shows B, C, A in that order, with no flags |
| AC-8 | S-3 | posting P requires {Java, kdb+}; applicant B (stage Applied) has only Java | the recruiter opens the ranked list for P | B still appears in the list, flagged "Does not meet minimum", and B's stage is still Applied |
| AC-9 | S-4 | posting P requires {Java, PostgreSQL} and prefers {Kubernetes}; a resume lists Java and Kubernetes | the recruiter opens that application | it shows matched required: Java; missing required: PostgreSQL; matched preferred: Kubernetes; and a fit score from 0 to 100 |
| AC-10 | S-5 | an employee whose current manager is M has an account on the board | the employee submits an application | M's notifications list shows no entry about the application |
| AC-11 | S-6 | a recruiter is signed in | they post a job with title, description, level, location, and required and preferred skills | the internal board lists the posting with its level and location |
| AC-12 | S-6 | a posting is listed on the board | the server restarts | the board still lists the posting with the same fields |
| AC-13 | S-7 | an employee is signed in to the board | they apply to a posting | the application appears in their applications list, and they were not asked to create a separate candidate account |
| AC-14 | S-8 | an applicant has a DOCX resume | they upload it with their application | the recruiter's view of the application lists the file by name, and its download has the same SHA-256 hash as the original |
| AC-15 | S-9 | an applicant has an application with an uploaded resume | they request erasure | within `ERASURE_MAX_MINUTES` the recruiter's pipeline no longer lists them and the resume download returns "not found" |
| AC-16 | S-10 | an application is at Interview | it is recorded as withdrawn | the pipeline export lists it as Withdrawn and not as Rejected |
| AC-17 | S-11 | three applications for P are at Interview | the hiring manager opens the comparison view for P | one view shows all three, each with fit score and matched and missing required skills |
| AC-18 | S-12 | an application has a fit score with at least one matched and one missing required skill | the recruiter opens it | a written explanation of at most `EXPLANATION_MAX_WORDS` words names at least one matched and one missing required skill |
| AC-19 | S-13 | an application is at Interview | the recruiter moves it to Rejected | the applicant's view shows the label `APPLICANT_STAGE_LABELS["Interview"]` as the last stage reached and a named contact for feedback |

Q entries are not quietly settled. AC-2 and AC-4 apply A-2 and A-3, which are explicit, logged assumptions. No criterion moves an application out of Offer (Q-3), orders tied scores (Q-6), overrides a flag (Q-5), matches synonyms (Q-9), or picks a stage at which a manager is told (Q-7). AC-10 covers only submission, which INT-04:P12 supports.

## 4e. Ranking and cut line

| Rank | Story | Why it is above the line |
| --- | --- | --- |
| 1 | S-6 | Every other story needs a posting, and missing level and location stopped a real applicant from applying (E-10). |
| 2 | S-7 | Applications must exist before any pipeline or ranking work, and the separate-account step was a real barrier (E-17). |
| 3 | S-1 | Accurate stages fix the hand cleaning in E-5 and E-6, and S-2, S-5, S-10, and S-13 build on them. |
| 4 | S-2 | Applicant silence was the strongest pain we heard (E-1, E-2). |
| 5 | S-5 | Fear of the current manager finding out stopped or worried a real applicant (E-8, E-10). It is small once S-1 exists. |
| 6 | S-8 | A rejected .docx was a real barrier (E-18), and our proposal's upload-reliability measure depends on it. |
| 7 | S-4 | Hiring managers lose evenings mapping resumes to requirements (E-11, E-13), and S-3 needs its scores. |
| 8 | S-3 | It directly addresses bad keyword shortlists (E-12) and carries our proposal's ranking invariant and accuracy measure. |
| 9 | S-9 | Applicants wonder whether their data stays on file (E-20), and right to erasure is a committed proposal scope item. |
| **— cut line —** | | |
| 10 | S-10 | Below the line: blocked by Q-4. |
| 11 | S-13 | Below the line: needs a feedback process the interviews did not describe. |
| 12 | S-11 | Below the line: useful (E-15), but S-3's ranked list covers most of the need. |
| 13 | S-12 | Below the line: rests only on A-7. Our proposal's cut line drops LLM explanations if extraction accuracy falls short. |
