# 3. Evidence log

Scheme from Assignment 3. **E** = something a real interviewee said or described. **A** = an assumption our team is making that the interviews did not establish. **Q** = an open question that must be answered before a related decision is settled.

Status: **Observed** (a specific past event someone described), **Stated** (a rule or fact someone asserted), **Assumption** (A entries), **Open** (Q entries).
Sources are interview paragraphs in `docs/interviews/INT-0n.md`. No entry cites an AI model, a synthetic user, or the compliments and predictions list.

Counts: 24 E, 7 A, 9 Q.

Owners: **AP** = Aditya Pothuri (Project Lead), **KV** = Ketan Verma (Tech Lead), **AE** = Abraham Eapen (QA & DevOps Lead).

## E entries

| ID | Claim | Source | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | After applying for an internal role, the applicant's portal showed only "Submitted" the whole time; she waited about five weeks before anyone contacted her. | INT-05:P08 | Observed | AP |
| E-2 | After three weeks without an update, the applicant messaged the recruiter on Teams; the recruiter had to check with the hiring manager, and the applicant felt awkward chasing colleagues. | INT-05:P09 | Observed | AP |
| E-3 | The applicant had two interviews, then heard nothing for three weeks, then got a short rejection email. | INT-05:P03 | Observed | AP |
| E-4 | The rejection was the generic template that external candidates get, with no feedback; she got pointers only by asking the hiring manager personally. | INT-05:P11 | Observed | AP |
| E-5 | A recruiter's weekly pipeline report took about 2.5 hours on a weekend, because ATS stages were wrong for about a third of candidates and had to be fixed by hand in a spreadsheet. | INT-01:P07 | Observed | AE |
| E-6 | For a compliance audit, the ATS export did not separate withdrawn candidates from rejected ones; the director and a coordinator spent about 30 hours cleaning it and submitted on the deadline day. | INT-02:P06 | Observed | AE |
| E-7 | The recruiter keeps a spreadsheet tab per req tracking who was contacted, when, and the next step, because the ATS pipeline view does not show who she owes a follow-up today. | INT-01:P05 | Stated | AP |
| E-8 | The applicant told her current manager the week she applied, because she worried the manager would hear it elsewhere; she still does not know whether the system notifies managers, and there was no guidance on it. | INT-05:P07, INT-05:P10 | Observed | AP |
| E-9 | By process, the applicant's current manager is not automatically informed; the manager is told only after the candidate is shortlisted for the offer. | INT-04:P12 | Stated | AP |
| E-10 | Last spring the applicant did not apply for a role she liked, because the posting did not say whether it was open to her level or location, and the slow process and risk with her manager did not seem worth it. | INT-05:P12 | Observed | AP |
| E-11 | A hiring manager screened about 60 resumes over two evenings; about 3 had real [domain] trading-system work, and 1 had written [the niche database language]. He fell behind on sprint work. | INT-03:P03 | Observed | KV |
| E-12 | The recruiter screened on keywords and years of experience; the hiring manager rejected 5 of the recruiter's 8 picks because many had no trading exposure, and the job description was old. | INT-03:P05 | Observed | KV |
| E-13 | The slowest part of screening is judging how a candidate's experience maps to the role, especially for internal candidates whose transferable experience does not overlap the job description word for word. | INT-04:P06 | Stated | KV |
| E-14 | Minimum requirements are defined by technical or core skills; a borderline candidate met the technical minimum but fell short on soft skills, and the hiring manager moved ahead with them. | INT-04:P07 | Observed | KV |
| E-15 | The hiring manager keeps a personal Excel sheet of candidates and scores because the hiring system shows one candidate at a time and cannot compare them side by side. | INT-03:P08 | Stated | KV |
| E-16 | The posting was a PDF on the intranet, and its Apply link went to the external careers site, so the details lived in two places. | INT-05:P04 | Observed | AP |
| E-17 | The applicant could not use the portal on her phone; on her laptop she had to create a separate candidate account although she is an employee, and retype her work history. | INT-05:P05 | Observed | AE |
| E-18 | The portal rejected the applicant's .docx resume, so she exported it from Google Docs to PDF; there was nowhere to point to internal projects. | INT-05:P06 | Observed | AE |
| E-19 | In the hiring manager's company the portal accepts only PDF or Word files; for a resume in an unusual format, they ask HR to get it in a proper format. | INT-04:P08 | Stated | AE |
| E-20 | After her rejection, the applicant wondered whether her application stays on file or whether other hiring managers can see it; she found no information and let it go. | INT-05:P13 | Observed | AE |
| E-21 | Late interviewer feedback cost time and candidates: two interviewers submitted scorecards a week late after three reminders and the candidate accepted another offer (INT-01:P03); a hiring manager chased two panelists for three days (INT-03:P06). | INT-01:P03, INT-03:P06 | Observed | AP |
| E-22 | Buying the last recruiting tool needed the head of people, IT security review (a SOC 2 report and an SSO integration), and procurement; it took 14 weeks from first demo to go-live. | INT-02:P05 | Observed | KV |
| E-23 | An AI sourcing tool was cancelled after two months because it was built for tech hiring and did not sync with the ATS, so recruiters had to re-enter every candidate. | INT-02:P02 | Observed | KV |
| E-24 | A hiring manager sent HR a candidate's resume and a reference letter explaining the fit; HR later rejected the candidate for [an eligibility requirement]. | INT-04:P13 | Observed | KV |

## A entries

| ID | Claim | Source | Status | Owner |
| --- | --- | --- | --- | --- |
| A-1 | We assume the pipeline stages are Applied → Screened → Interview → Offer, plus Rejected (from our proposal). No interviewee listed their stage names; INT-04:P03 and INT-04:P05 describe HR screen → hiring-manager interview → offer, which fits but does not confirm the names. | Team | Assumption | AP |
| A-2 | We assume a recruiter moves an applicant forward one stage at a time, or to Rejected from any open stage, and never skips or moves backward. No interviewee described skipping or reversing a stage. | Team | Assumption | AP |
| A-3 | We assume Rejected is final: once rejected, an application never moves again. No interviewee described reopening a rejected application. | Team | Assumption | AP |
| A-4 | We assume simple role-based accounts (Recruiter, Applicant) without SSO are acceptable for this project, although INT-02:P05 shows a real security review asked for SSO. | Team | Assumption | KV |
| A-5 | We assume "meets minimum" means the applicant's skills include every required skill on the posting, matched by name after trimming and ignoring case. INT-04:P07 shows hiring managers sometimes move ahead with candidates who fall short on non-technical skills. | Team | Assumption | KV |
| A-6 | We assume resumes and supporting documents are in English (from our proposal). | Team | Assumption | AE |
| A-7 | We assume recruiters would read and trust a short machine-written explanation of an applicant's fit. No interviewee described using one; INT-04:P13 describes a hiring manager writing their own reference letter. | Team | Assumption | KV |

## Q entries

| ID | Claim | Source | Status | Owner |
| --- | --- | --- | --- | --- |
| Q-1 | Which stage names should an applicant see: every internal stage (Screened, Interview), or a coarser status? When does a rejection become visible to them? | INT-05:P08, INT-05:P11 | Open | AP |
| Q-2 | **Disagreement:** INT-04:P10 says internal candidates can track progress in the system, but INT-05:P08 says the portal showed only "Submitted" the whole time. Which is typical, and what exactly can applicants see today? | INT-04:P10, INT-05:P08 | Open | AP |
| Q-3 | What happens to an application at Offer when the offer is declined or rescinded: does it move to Rejected, to a new stage, or stay at Offer? | Team | Open | AP |
| Q-4 | Who can set an application to Withdrawn (the applicant, the recruiter, or both), and can a withdrawn application be reopened? | INT-02:P06, INT-05:P15 | Open | AE |
| Q-5 | Can a recruiter override the "Does not meet minimum" flag for an applicant with transferable experience, and should an overridden applicant then rank with those who meet the minimum? | INT-04:P06, INT-04:P07 | Open | KV |
| Q-6 | How should applicants with equal fit scores be ordered in the ranked list? | Team | Open | KV |
| Q-7 | At which stage, if any, should the system tell the applicant's current manager, and who triggers it? | INT-04:P12, INT-05:P10 | Open | AP |
| Q-8 | Who approves a new hiring tool at our target companies, and is SSO required before go-live? | INT-02:P05 | Open | KV |
| Q-9 | Should a skill synonym count as a match for a required skill (for example "Postgres" for "PostgreSQL", or "Word" for "Microsoft Word")? | INT-03:P03 | Open | KV |
