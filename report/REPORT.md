# CS 690 Project Milestone 1: Internal Jobs Board Portal

Team: Ketan Verma, Aditya Pothuri, Abraham Eapen  
Repository: [TODO: GitHub repository URL]  
Report built from commit: `e28dc0f`

## Table of contents {#toc}

| Deliverable | Page | Repository path |
| --- | --- | --- |
| [1. Proposal follow-up and scope changes](#d1) | <a class='pageref' href='#d1'></a> | `docs/proposal_followup.md` |
| [2. User interviews (questions, notes, participation, compliments and predictions, lesson)](#d2) | <a class='pageref' href='#d2'></a> | `docs/interviews/` |
| [3. Evidence log](#d3) | <a class='pageref' href='#d3'></a> | `evidence/evidence_log.md` |
| [4. Backlog (stories, trace, INVEST, AC, ranking)](#d4) | <a class='pageref' href='#d4'></a> | `backlog/backlog.md` |
| [5. Design docs S-1 and S-3, with gap checks](#d5) | <a class='pageref' href='#d5'></a> | `docs/design/` |
| [6. Repository, tests, first story (6e test output in this PDF)](#d6) | <a class='pageref' href='#d6'></a> | `README.md, AGENTS.md, docs/plans/S-1-plan.md, src/, tests/` |
| [7. Traceability matrix](#d7) | <a class='pageref' href='#d7'></a> | `traceability/traceability.csv` |
| [8. Provenance ledger](#d8) | <a class='pageref' href='#d8'></a> | `LEDGER.md, prompts/` |
| [9. Contribution statements (individual, submitted separately)](#d9) | <a class='pageref' href='#d9'></a> | `contribution/` |


## 1. Proposal follow-up {#d1}
**Items from the approval feedback:** No items.

**Scope changes since the proposal.** The approval asked for none; we record them here so a reviewer can check the backlog against the proposal.

| Proposal commitment | Change | Why | Where |
| --- | --- | --- | --- |
| "Apply with documents" covers PDF, DOCX, and JPEG/PNG scans with OCR | Split in two. PDF and DOCX upload stays above the cut line (S-8). Scanned images with text extraction became S-14, below the cut line. | Only one interviewee mentioned unusual formats, and that company sends them back to HR rather than reading them (E-19, INT-04:P08). | `backlog/backlog.md` S-8, S-14, §4e |
| LLM-written fit explanation, dropped only if extraction accuracy fails by Milestone 2 | Moved below the cut line now (S-12). The rule-based fit score (S-4) and ranking (S-3) stay above it. | No interview supports it; it rests only on A-7. | `backlog/backlog.md` S-12, §4e |
| Erasure completes "within 5 minutes" | Kept as the named setting `ERASURE_MAX_MINUTES` (AC-15). | No interviewee or Legal contact confirmed the number. | `backlog/backlog.md` §4 settings table |
| Fit score as the core feature | The status pipeline (S-1) is built first. | Applicant silence and unreliable stage data were the strongest evidence (E-1, E-2, E-5, E-6). | `docs/interviews/lesson.md` |


## 2. User interviews {#d2}

### 2a. Interview questions
We started from the five recruiter questions in the proposal (Appendix C) and revised them following the Mom Test. We ask about specific past events, we don't pitch the idea, and we listen more than we talk. Each guide follows the shape from lecture: **open with the person's situation → dig into one real event → close by asking who else we should talk to.**

`[PE]` marks a question about a specific past event. Both guides have more than the five such questions the handout requires.

#### Guide A: HR recruiter or hiring manager (used for INT-04; INT-01 to INT-03 used role-specific variants, recorded verbatim in their notes)

**Opening: their situation**

1. What's your role, and roughly how many internal openings are you working on right now?
2. In a typical month, how much of your time goes to internal candidates compared with outside hires?

**Digging into one real event**

3. `[PE]` Tell me about the last internal role you filled. Walk me through it from the day the role was approved to the offer. *(kept from proposal Q1)*
4. `[PE]` For that role, how did the internal applications reach you? How many came through the ATS, and how many by email, Teams or in person? *(proposal Q2, made more specific)*
5. `[PE]` Once an application arrived, what did you do with it? Where did the resume go, and what did you have open next to it?
6. `[PE]` The last time you screened a batch of resumes against a job description, what took the longest? *(kept from proposal Q3)*
7. `[PE]` In that batch, how did you decide someone didn't meet the minimum requirements? Tell me about a borderline candidate and what you did.
8. `[PE]` Think of the last time you got a resume in an awkward format, like a scan, a phone photo or an unusual file. What did you do with it?
9. `[PE]` Tell me about a time a strong internal candidate was overlooked or found late. What happened? *(kept from proposal Q4)*
10. `[PE]` The last time an applicant asked about the status of their application, how did they contact you, and what did you do? *(split out of proposal Q5)*
11. `[PE]` Tell me about the most recent time someone asked for their application or personal data to be removed, or Legal asked how candidate data was handled. What happened? *(split out of proposal Q5)*
12. `[PE]` Think of the last time an employee applied internally and didn't want their current manager to know. How was that handled, and when did the manager find out? *(new: covers the easy-to-miss stakeholder in proposal Appendix B)*
13. `[PE]` The last time you sent a shortlist to a hiring manager, what did you send, and what did they come back asking?
14. What have you tried so far to make screening or tracking easier, such as spreadsheets, ATS features or templates? What happened with it?

**Closing**

15. Who else should we talk to? For example, a hiring manager, someone in IT or privacy/Legal, or an employee who recently applied internally.

#### Guide B: internal job applicant (used for INT-05)

**Opening: their situation**

1. What's your current role, and how long have you been at the company?
2. Over the past year or two, how often have you looked at internal openings? What usually prompted you to look?

**Digging into one real event**

3. `[PE]` Tell me about the last time you applied for an internal role. Walk me through it from when you first heard about the opening to the last time you heard anything back.
4. `[PE]` How did you first find out about that opening? Where did you go to see the details?
5. `[PE]` When you sat down to apply, what did you actually do, step by step? Which device were you on, and where did you go?
6. `[PE]` What did you have to prepare or upload, such as a resume, cover letter or certificates? Was anything hard to find, update or get into the right format?
7. `[PE]` Was there a point in the process where you weren't sure what to do next, or almost gave up? What happened?
8. `[PE]` After you applied, how did you find out where things stood? How long did you wait before hearing anything?
9. `[PE]` The last time you wanted an update and didn't have one, what did you do? Who did you ask, and how?
10. `[PE]` Thinking about that application, who knew you had applied, and when did they find out? How did you feel about your current manager knowing?
11. `[PE]` If you weren't selected, tell me how you found out. What did you learn, if anything, about why?
12. `[PE]` Tell me about a time you thought about applying internally but didn't. What stopped you?
13. `[PE]` Have you ever wondered what happened to the resume or personal details you submitted? Tell me about that time and what, if anything, you did about it.
14. `[PE]` Tell me about a time you applied for a job outside the company. How did that process compare with applying internally?

**Closing**

15. Who else should we talk to? For example, a colleague who recently moved roles internally, or someone who tried and didn't get the role.

#### Weak question we dropped

- *"Would you use a tool that automatically ranks resumes against the job description?"* It asks about the future and pitches our idea. We replaced it with Guide A Q6.

### 2b. Participation table
All interviews were with real people in, or closely involved in, the target user group. None were with an AI model, a teammate, or a member of another CS 690 team. Every interviewee was told at the start that this is a graduate class project, how the notes would be used, and that they could stop at any time. No interview was recorded. No names or identifying details are kept.

Each team member took part in at least one interview: Aditya Pothuri (INT-01, INT-02), Ketan Verma (INT-03), Abraham Eapen (INT-04, INT-05). Dates given as a week were not recorded to the day.

| Interview ID | Interviewee's role | Date | Team members who took part | Format |
| --- | --- | --- | --- | --- |
| INT-01 | Senior recruiter | Week of 2026-11-02 | Aditya Pothuri | In person, ~30–45 min, handwritten notes typed up afterward |
| INT-02 | Director of talent acquisition | Week of 2026-11-02 | Aditya Pothuri | In person, ~30–45 min, handwritten notes typed up afterward |
| INT-03 | Senior developer and hiring manager, [financial-services firm] (1 open role) | 2026-11-04 | Ketan Verma | In person, 20 min, handwritten notes |
| INT-04 | Hiring manager ([senior manager, technology governance]; 1–2 open roles) | Week of 2026-11-02 | Abraham Eapen | In person, ~20–30 min, handwritten notes typed up afterward |
| INT-05 | Internal applicant (product manager, [a few] years at company) | Week of 2026-11-02 | Abraham Eapen | In person, ~20–30 min, handwritten notes typed up afterward |

#### Optional items not used

- **2e. AI summaries:** none. Every interview was summarized by hand from the raw notes.
- **2f. Synthetic users:** none were used.

### 2c. Raw notes: INT-01 — Senior Recruiter
- **Cite as:** INT-01, senior recruiter
- **Source file:** `CS690 - Project - Senior Recruiter Answers.docx` (team's original notes)
- **Date:** week of 2026-11-02 (exact day not recorded)
- **Format:** in person, about 30–45 minutes; handwritten notes, typed up afterward; no recording
- **Team member:** Aditya Pothuri
- **Consent:** at the start, the interviewee was told this is a graduate class project, how the notes would be used, and that they could stop at any time (as reported by the team)
- No names or identifying details are kept. Quotes are as recorded in the original notes.

#### Raw notes

**Q1. Walk me through the last role you filled, from req open to signed offer.**

P01: "A senior engineering role. It took about 7 weeks from open to signed. The intake meeting got pushed twice, so I started sourcing off an old job description. In week one I sent around 140 outreach messages and got 19 replies. Eight passed my phone screen, five went to the hiring manager, three made the onsite, one offer, one acceptance. The onsite alone took 11 days to schedule because four interviewers' calendars never lined up."

**Q2. Which part took the most time? How do you know?**

P02: "Scheduling and chasing feedback. I keep a rough tally in my sheet, and last month I logged about 9 hours a week on scheduling, rescheduling and status pings. Sourcing takes time too, but at least that feels like real work."

**Q3. Tell me about the last time a great candidate dropped out.**

P03: "A few weeks ago. A strong senior candidate finished our onsite early in the week. Two interviewers didn't submit scorecards until the following week, even after three reminders from me. A couple of days later the candidate accepted another offer, and told me we were the slowest of their four processes."

**Q4. What tools did you touch during that hire? Where did you copy-paste?**

P04: "A sourcing tool, our ATS, email, calendar, a scheduling-link tool, team chat, and my spreadsheet. I copy candidate profiles from the sourcing tool into the ATS by hand, and interview times from the calendar into ATS notes. Feedback often comes in as chat messages, so I paste that into the ATS too, otherwise it doesn't exist."

**Q5. What spreadsheets or side systems do you keep outside the ATS? Why?**

P05: "One spreadsheet with a tab per req. It tracks who I've contacted, when, the next step, and my gut-feel notes. I started it a couple of years ago because the ATS pipeline view doesn't show who I owe a follow-up today. I also keep a notes file of email templates because the ATS ones are clunky to edit."

**Q6. When did you last get pushback from a hiring manager?**

P06: "Last week. A manager said the last five candidates were 'not senior enough.' When I asked what senior meant, it was mostly system-design depth, which never came up in intake. We re-ran intake, and that req lost about two weeks."

**Q7. How did you report on your pipeline last week? Who asked, and how long did it take?**

P07: "My manager wanted pipeline status for all my reqs before the weekly leadership meeting. I exported from the ATS, then cleaned it in my sheet because the stages were wrong for about a third of candidates, and built a summary. About 2.5 hours, on the weekend."

**Q8. Have you tried to fix any of this? What happened?**

P08: "I tried the ATS's automated feedback reminders. Managers muted the emails within a week. I also built a chat reminder workflow, which helped for about a month until a workspace change broke it. Nobody owned fixing it."

**Closing.**

P09: Agreed to a 30-minute screen-share of the tracking spreadsheet and to introduce two hiring managers.

### 2c. Raw notes: INT-02 — Director of Talent Acquisition
- **Cite as:** INT-02, director of talent acquisition
- **Source file:** `CS690 - Project - Senior Recruiter Answers.docx`, second interview in that file (team's original notes)
- **Date:** week of 2026-11-02 (exact day not recorded)
- **Format:** in person, about 30–45 minutes; handwritten notes, typed up afterward; no recording
- **Team member:** Aditya Pothuri
- **Consent:** at the start, the interviewee was told this is a graduate class project, how the notes would be used, and that they could stop at any time (as reported by the team)
- No names or identifying details are kept. Quotes are as recorded in the original notes, except that confidential figures and identifying details are generalized in [brackets] for the public repository.

#### Raw notes

**Q1. What recruiting tools does your team pay for today? How did each one get bought?**

P01: "Our ATS is about [a six-figure sum] a year. IT picked it during an HR system rollout before I joined. Job boards run around [six figures], background checks about [five figures], a skills-assessment tool [five figures], and a scheduling add-on [five figures]. I bought the last two myself after recruiters complained loudly enough. The rest I inherited."

**Q2. Tell me about the last tool you cancelled or didn't renew. Why?**

P02: "An AI sourcing tool, about [five figures] a year, cancelled earlier this year. Usage was strong for two months, then dropped to two recruiters. Most of our roles are [frontline], and it was built for tech hiring. It also didn't sync with the ATS, so recruiters had to re-enter every candidate."

**Q3. What metric were you last asked to report to leadership? What happened when it looked bad?**

P03: "Time to fill for [one frontline role family], at a recent exec review. The ATS said [one number], but I knew it was wrong because reqs get reopened instead of new ones being created. My team spent two days reconciling by hand and landed on [a number about 10 days higher]. Finance leadership asked why we had two numbers, and I didn't have a great answer."

**Q4. When was the last time a hire went badly wrong? What changed afterward?**

P04: "Earlier this year we lost [nearly half of a group of] new hires at one location within 90 days. Exit interviews said the shift schedule wasn't what they'd been told during recruiting. We now make recruiters read from a written shift-expectations script, but I can't verify that they use it."

**Q5. Who has to sign off on a new recruiting tool? Walk me through the last time.**

P05: "For the scheduling add-on, it was me, then our head of people, then IT security review, then procurement. Security asked for a SOC 2 report and an SSO integration. It took 14 weeks from the first demo to go-live. Anything over [a set amount] also needs finance leadership."

**Q6. What's the most recent compliance or audit question you had to answer? How did you pull the data?**

P06: "Last quarter a compliance audit asked for applicant flow data by role and by demographic. The ATS export didn't separate withdrawn candidates from rejected ones. A coordinator and I spent about 30 hours cleaning it, and we submitted on the deadline day."

### 2c. Raw notes: INT-03 — Hiring Manager, Senior Developer Role ([financial-services firm])
- **Cite as:** INT-03, senior developer and hiring manager, [financial-services firm]
- **Source file:** `CS690 - Project - Software Developer Role.docx` (team's original notes; that file labeled this interview INT-01, renumbered here to INT-03 because INT-01 was already used). Identifying details are generalized in [brackets] for the public repository.
- **Interviewee:** senior developer (individual contributor), [trading-systems team at a financial-services firm]; hiring manager for 1 role
- **Date:** 2026-11-04
- **Team member:** Ketan Verma
- **Format:** 20-minute informal face-to-face conversation, in person; notes taken by hand, no recording
- **Consent script used:** "This is an NJIT graduate class project. Notes stay anonymous and are used only for our report. You can stop at any time. OK if I jot down a few notes?"
- **Role being hired (context):** 1 senior developer, 15+ years; prior trading-technology experience; strong [domain] trading knowledge; [built core trading-system components]; [a niche database language] and Java.

#### Raw notes

**Q1. What do you build, and how much of your week goes to hiring?**

P01: Individual contributor on the [trading-systems] team; builds [market-data and trading] services. Hiring 1 senior developer. "Hiring eats about a day a week for me."

**Q2. Walk me through your last hire, from headcount approval to start date.**

P02: Last hire started [earlier this year]. Headcount approval took ~3 weeks (finance, tech risk). Req open ~9 weeks to signed offer.

**Q3. Which step took most of your time? How do you know?**

P03: Resume screening. "Around 60 resumes, maybe 3 had real [domain] trading-system work, and only 1 had actually written [the niche database language]." Took two evenings; fell behind on sprint tickets.

**Q4. Tell me about the last strong candidate who dropped out. What happened?**

P04: [Recently], a strong candidate took another offer. "Our offer took 11 days because comp needed HR and director approval."

**Q5. When did you last disagree with the recruiter on a shortlist? What about?**

P05: Recruiter screened on keywords and years. Many 15+ year picks had no trading exposure. "I rejected 5 of [the recruiter's] 8 picks. The JD was old."

**Q6. How did your last interview panel share feedback and decide?**

P06: Panel: [niche-language] coding, Java + [domain] system design, behavioral, hiring manager. Decision made in Teams, not the hiring system. "Two people never filled in the form. I chased them for three days."

**Q7. When did compliance or background checks last delay a hire?**

P07: Background and credit check took 12 business days; start date slipped two weeks. "I can only email HR for updates."

**Q8. What do you track outside the hiring system, and why?**

P08: Keeps a personal Excel sheet of candidates and scores. "The system shows one candidate at a time. I can't compare side by side."

**Q9. What have you tried to fix, and why did it stop?**

P09: Shared a OneNote scoring rubric last year. "Used for a month, then stopped. Nobody owned it."

**Q10. Who else should we talk to?**

P10: The team's technical recruiter, and [another trading team's] lead who "hires way more than I do."

Compliments and predictions from this interview are moved to `docs/interviews/compliments_predictions.md` and are not numbered as evidence paragraphs.

### 2c. Raw notes: INT-04 — Hiring Manager, [Senior Manager, Technology Governance]
- **Cite as:** INT-04, hiring manager ([senior manager, technology governance])
- **Source file:** `CS690 - Project - Hiring Manager Answers.docx` (team's original notes)
- **Date:** week of 2026-11-02 (exact day not recorded)
- **Format:** in person, about 20–30 minutes; handwritten notes, typed up afterward; no recording
- **Team member:** Abraham Eapen
- **Consent:** at the start, the interviewee was told this is a graduate class project, how the notes would be used, and that they could stop at any time (as reported by Abraham Eapen)
- No names or identifying details are kept; some details are generalized in [brackets] for the public repository. Answers are as recorded in the original notes; questions with no recorded answer are marked so.

#### Raw notes

**Opening. What's your role, and roughly how many internal openings are you working on right now?**

P01: [Senior manager – technology governance]. "I am interviewing for roughly 1-2 open spots."

**In a typical month, how much of your time goes to internal candidates compared with outside hires?**

P02: "It varies – based on the interest from the internal candidates. The roles are available for both internal and external candidates to apply."

**Tell me about the last internal role you filled. Walk me through it from the day the role was approved to the offer.**

P03: "The last role filled internally was back in [2025]. The role was approved a couple months prior. The role is opened both externally and internally where candidates apply to. After the initial HR assessment, candidates are passed on to the hiring managers where interviews are scheduled. Once the candidate is selected, an offer is sent subjected to background check clearance. The entire process ranges from a few weeks to a couple of months."

**For that role, how did the internal applications reach you? How many came through the ATS, and how many by email, Teams or in person?**

P04: "Three internal candidates reached out via teams message and scheduled a quick call to understand the job posting and role responsibilities."

**Once an application arrived, what did you do with it? Where did the resume go, and what did you have open next to it?**

P05: "The applications are first screened by HR and passed on to the hiring manager based on their qualifications and job requirements. Those shortlisted candidates are then reviewed and set for an interview."

**The last time you screened a batch of resumes against a job description, what took the longest?**

P06: "The longest part is determining how someone's experience translates to the requirements of the role. Especially with internal candidates because they might have strong organizational skills and transferable experience, but the resume wouldn't exactly overlap with the job description."

**In that batch, how did you decide someone didn't meet the minimum requirements? Tell me about a borderline candidate and what you did.**

P07: "Minimum requirements are defined based on their technical skills or core skills. A candidate displayed the minimum required technical skills but fell short on the soft skills. Considering these were transferable skills we decided to move ahead with the candidate."

**Think of the last time you got a resume in an awkward format, like a scan, a phone photo or an unusual file. What did you do with it?**

P08: "Generally, the resumes are first screened by HR and come in a standard format as the portal only allows pdf or word documents. In cases where a resume is received in an unusual format, we'd ask HR to get the information in proper format."

**Tell me about a time a strong internal candidate was overlooked or found late. What happened?**

P09: "NA"

**The last time an applicant asked about the status of their application, how did they contact you, and what did you do?**

P10: "For internal candidates, progress can be tracked via the system. For external candidates, the progress is usually communicated by HR."

**Tell me about the most recent time someone asked for their application or personal data to be removed, or Legal asked how candidate data was handled. What happened?**

P11: "NA"

**Think of the last time an employee applied internally and didn't want their current manager to know. How was that handled, and when did the manager find out?**

P12: "As per the process, the current manager is not automatically informed. They are informed after the candidate is shortlisted for the offer to understand the current rating of the candidate and to set up the transition and move if the offer is accepted."

**The last time you sent a shortlist to a hiring manager, what did you send, and what did they come back asking?**

P13: "A reference needs to be submitted through a portal so that HR is involved and progress is tracked appropriately. I sent the candidates' resume, a reference letter on why the candidate was a good fit for the role. HR informed later on that the candidate was rejected due [an eligibility requirement]."

**What have you tried so far to make screening or tracking easier, such as spreadsheets, ATS features or templates? What happened with it?**

P14: No answer recorded.

**Closing. Who else should we talk to?**

P15: No answer recorded.

### 2c. Raw notes: INT-05 — Internal Job Candidate (Product Manager)
- **Cite as:** INT-05, internal applicant, product manager
- **Source file:** `CS690 - Project - Job Candidate Answers.docx` (team's original notes)
- **Date:** week of 2026-11-02 (exact day not recorded)
- **Format:** in person, about 20–30 minutes; handwritten notes, typed up afterward; no recording
- **Team member:** Abraham Eapen
- **Consent:** at the start, the interviewee was told this is a graduate class project, how the notes would be used, and that they could stop at any time (as reported by Abraham Eapen)
- No names or identifying details are kept; some details are generalized in [brackets] for the public repository. Answers are as recorded in the original notes.

#### Raw notes

**Opening. What's your current role, and how long have you been at the company?**

P01: "I'm a Product Manager on [a product team]. I've been here [a few] years[, most of them as a PM, after an earlier non-PM role]."

**Over the past year or two, how often have you looked at internal openings? What usually prompted you to look?**

P02: "Maybe once every month or two, usually after a reorg, a performance review, or when a colleague moves on. I don't browse regularly because there's no easy place to look, and I can't save a search or get alerts."

**Tell me about the last time you applied for an internal role. Walk me through it from when you first heard about the opening to the last time you heard anything back.**

P03: "About eight months ago I applied for a Senior PM role on [another product team]. A friend mentioned it on Teams. I found the posting on the intranet, applied through the career's portal, and got an automated confirmation. About five weeks later a recruiter emailed me for a screen. I had two interviews, then nothing for three weeks, then a short rejection email."

**How did you first find out about that opening? Where did you go to see the details?**

P04: "Word of mouth. The posting was on the intranet as a PDF. When I clicked 'Apply' it sent me to the external careers site, so the details lived in two places."

**When you sat down to apply, what did you actually do, step by step? Which device were you on, and where did you go?**

P05: "I started on my phone during a commute, but the portal wasn't usable on mobile, so I gave up and finished on my laptop that night. I had to create a separate candidate account, even though I'm already an employee, and retype my work history."

**What did you have to prepare or upload? Was anything hard to find, update or get into the right format?**

P06: "I had to upload a resume and a cover letter. My resume was out of date, and I had to export it from Google Docs to PDF because the portal rejected the .docx. There was nowhere to point to my internal projects or performance history."

**Was there a point in the process where you weren't sure what to do next, or almost gave up? What happened?**

P07: "Yes, at the 'Do you require sponsorship?' and 'How did you hear about us?' questions. They clearly weren't written for internal people. I also didn't know if I was supposed to tell my manager first, and there was no guidance on that."

**After you applied, how did you find out where things stood? How long did you wait before hearing anything?**

P08: "I couldn't. The portal just said 'Submitted' the whole time. I waited about five weeks before anyone contacted me."

**The last time you wanted an update and didn't have one, what did you do? Who did you ask, and how?**

P09: "I messaged the recruiter on Teams after three weeks. She said she'd check with the hiring manager. I felt awkward chasing it because I didn't want to seem pushy with people I work with."

**Thinking about that application, who knew you had applied, and when did they find out? How did you feel about your current manager knowing?**

P10: "I told my manager the week I applied because I was worried, she'd hear it from someone else. I still don't know if the system tells managers automatically. That uncertainty made me nervous."

**If you weren't selected, tell me how you found out. What did you learn, if anything, about why?**

P11: "A generic email, the same template external candidates get. There was no feedback. I later asked the hiring manager directly and got useful pointers, but only because I knew him."

**Tell me about a time you thought about applying internally but didn't. What stopped you?**

P12: "Last spring there was a role I liked, but the posting didn't say whether it was open to my level or location. The previous process had been so slow that I didn't think it was worth the effort or the risk with my manager."

**Have you ever wondered what happened to the resume or personal details you submitted? Tell me about that time and what, if anything, you did about it.**

P13: "Yes. After the rejection I wondered if my application stays on file, or if other hiring managers can see it. I couldn't find any information, so I let it go."

**Tell me about a time you applied for a job outside the company. How did that process compare with applying internally?**

P14: "Applying externally was easier. LinkedIn Easy Apply took two minutes, and I got status updates. Internally it felt like a worse version of the external process, even though I'm a known employee."

**Closing. Who else should we talk to?**

P15: "A colleague on the data team who moved internally last quarter and had a smooth experience. Also, an engineer who withdrew mid-process because of manager concerns."

### 2d. Compliments and predictions
Nothing on this list may be cited as evidence. No E entry, story, or acceptance criterion cites it.

| # | Interview | Type | Quote |
| --- | --- | --- | --- |
| CP-1 | INT-03 | Compliment | "That sounds really useful for managers like me." |
| CP-2 | INT-03 | Prediction | "I'd probably use side-by-side comparison if [the firm] approved it." |

We re-read INT-01, INT-02, INT-04, and INT-05 for compliments about our idea or predictions about future use and found none. One borderline line is not on the list because it describes a past comparison, not our idea: INT-05:P14 ("Applying externally was easier…").

### 2e. AI summaries

None. No interview was transcribed or summarized by an AI tool.

### Most useful thing we learned
The most useful thing we learned is that the applicant's worst moment is not screening but silence. INT-05 applied, saw "Submitted" for five weeks (INT-05:P08), chased the recruiter on Teams and felt awkward doing it (INT-05:P09), and was rejected with the external template (INT-05:P11). On the recruiter side, stage data is unreliable enough that one recruiter rebuilt a pipeline report by hand because the stages were wrong for about a third of candidates (INT-01:P07), and a director spent 30 hours separating withdrawn from rejected applicants for an audit (INT-02:P06). Our proposal ranked the AI fit score as the core feature. These interviews moved the **status pipeline**, an accurate stage that the recruiter moves under fixed rules and the applicant can see, to the first story we build (S-1). The fit-score ranking is now the second design-doc story, and we will not build it until its open questions are answered (Q-5, Q-6).


## 3. Evidence log {#d3}
Scheme from Assignment 3. **E** = something a real interviewee said or described. **A** = an assumption our team is making that the interviews did not establish. **Q** = an open question that must be answered before a related decision is settled.

Status: **Observed** (a specific past event someone described), **Stated** (a rule or fact someone asserted), **Assumption** (A entries), **Open** (Q entries).
Sources are interview paragraphs in `docs/interviews/INT-0n.md`. No entry cites an AI model, a synthetic user, or the compliments and predictions list.

Counts: 24 E, 7 A, 9 Q.

Owners: **AP** = Aditya Pothuri (Project Lead), **KV** = Ketan Verma (Tech Lead), **AE** = Abraham Eapen (QA & DevOps Lead).

### E entries

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

### A entries

| ID | Claim | Source | Status | Owner |
| --- | --- | --- | --- | --- |
| A-1 | We assume the pipeline stages are Applied → Screened → Interview → Offer, plus Rejected (from our proposal). No interviewee listed their stage names; INT-04:P03 and INT-04:P05 describe HR screen → hiring-manager interview → offer, which fits but does not confirm the names. | Team | Assumption | AP |
| A-2 | We assume a recruiter moves an applicant forward one stage at a time, or to Rejected from any open stage, and never skips or moves backward. No interviewee described skipping or reversing a stage. | Team | Assumption | AP |
| A-3 | We assume Rejected is final: once rejected, an application never moves again. No interviewee described reopening a rejected application. | Team | Assumption | AP |
| A-4 | We assume simple role-based accounts (Recruiter, Applicant) without SSO are acceptable for this project, although INT-02:P05 shows a real security review asked for SSO. | Team | Assumption | KV |
| A-5 | We assume "meets minimum" means the applicant's skills include every required skill on the posting, matched by name after trimming and ignoring case. INT-04:P07 shows hiring managers sometimes move ahead with candidates who fall short on non-technical skills. | Team | Assumption | KV |
| A-6 | We assume resumes and supporting documents are in English (from our proposal). | Team | Assumption | AE |
| A-7 | We assume recruiters would read and trust a short machine-written explanation of an applicant's fit. No interviewee described using one; INT-04:P13 describes a hiring manager writing their own reference letter. | Team | Assumption | KV |

### Q entries

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


## 4. Backlog {#d4}
Evidence IDs refer to `evidence/evidence_log.md`. Stages are written as in A-1: Applied, Screened, Interview, Offer, Rejected.
Named settings stand for values the interviews did not settle. No criterion picks a number for them.

| Setting | Meaning | Open because |
| --- | --- | --- |
| `APPLICANT_STAGE_LABELS` | Map from each internal stage to the label an applicant sees | Q-1 |
| `ERASURE_MAX_MINUTES` | Longest time between an erasure request and full removal | Our proposal says 5; no interviewee or Legal contact has confirmed it |
| `EXPLANATION_MAX_WORDS` | Maximum length of a fit explanation | A-7; no evidence |

### 4a, 4b. Stories and evidence trace

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
| S-14 | As an **HR recruiter**, I want text extracted from resumes uploaded as scanned images (JPEG or PNG), so that I don't have to send applicants or HR back for a file in a proper format. | E-19. Rests also on A-6 (English documents). |

### 4c. INVEST check

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
| S-14 | **Fail:** depends on S-8's upload path. | P | P | **Fail:** OCR accuracy on phone photos is unknown until we test it on sample scans. | P | P |

### 4d. Acceptance criteria

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
| AC-20 | S-14 | an applicant uploads a PNG scan of a resume whose text includes "PostgreSQL" | the recruiter opens the application | the application's extracted text includes "PostgreSQL" |

Q entries are not quietly settled. AC-2 and AC-4 apply A-2 and A-3, which are explicit, logged assumptions. AC-16 records Withdrawn separately from Rejected, which E-6 supports; it leaves open who sets it and whether it can be reopened (Q-4). No criterion moves an application out of Offer (Q-3), orders tied scores (Q-6), overrides a flag (Q-5), matches synonyms (Q-9), or picks a stage at which a manager is told (Q-7). AC-10 covers only submission, which INT-04:P12 supports.

### 4e. Ranking and cut line

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
| 11 | S-14 | Below the line: only one interviewee mentioned unusual formats (E-19), and that company sends them back to HR instead of reading them. Split out of the proposal's "Apply with documents" scope item. |
| 12 | S-13 | Below the line: needs a feedback process the interviews did not describe. |
| 13 | S-11 | Below the line: useful (E-15), but S-3's ranked list covers most of the need. |
| 14 | S-12 | Below the line: rests only on A-7, so it moved below the line ahead of the proposal's Milestone 2 accuracy check (see Deliverable 1). |


## 5. Design docs {#d5}

### Design doc S-1 (`docs/design/S-1.md`)
**S-1.** As an HR recruiter, I want to move each applicant forward one stage at a time (Applied → Screened → Interview → Offer), or to Rejected, with any other move refused, so that the pipeline shows each applicant's true stage and I don't rebuild stage data by hand for reports and audits.

#### 1. Problem
Wrong stages forced a hand-built weekly report (E-5), an audit export took 30 hours to clean (E-6), and next steps live in a side spreadsheet (E-7).

#### 2. Scope
Three endpoints only: create an application (at Applied; S-7 adds accounts and documents), move its stage (R1), and list a posting's applications by stage.

#### 3. Non-goals
- No authentication (A-4), applicant view (S-2), notifications (S-5), or Withdrawn stage (S-10).
- No moves out of Offer (OQ-1), persistence (S-6), move history, or automatic moves.

#### 4. Interface
`jobsboard.pipeline`:
- `Stage(str, Enum)`: `"Applied"`, `"Screened"`, `"Interview"`, `"Offer"`, `"Rejected"`; `allowed_next(stage: Stage) -> frozenset[Stage]` never raises.
- `move_stage(store: ApplicationStore, application_id: str, to_stage: Stage) -> Application`. Raises `ApplicationNotFound(application_id)` or `InvalidTransition(from_stage, to_stage)`.
- `ApplicationStore`: `create(posting_id: str, applicant_id: str) -> Application`, `get(application_id: str) -> Application` (`ApplicationNotFound`), `list_for_posting(posting_id: str) -> list[Application]`.

`jobsboard.api:app` (FastAPI). An Application is returned as JSON `{application_id, posting_id, applicant_id, stage}`, all strings.
- `POST /postings/{posting_id}/applications` with `{"applicant_id": str}` returns 201 with an Application. 422 if `applicant_id` is missing, blank, or not a string.
- `POST /applications/{application_id}/stage` with `{"to_stage": str}` returns 200 with an Application. Returns 422 for a bad body or an inexact stage name; 404 `{"detail": {"error": "application_not_found", "application_id"}}`; or 409 `{"detail": {"error": "invalid_transition", "from_stage", "to_stage"}}`.
- `GET /postings/{posting_id}/pipeline` returns 200 `{"posting_id", "stages": {"Applied": [ids], "Screened", "Interview", "Offer", "Rejected"}}`.

#### 5. Data
- `application_id: str`: server-set `uuid4().hex`, unique within a run. `stage: Stage`: `Applied` at creation.
- `posting_id: str` (any non-empty; no posting entity until S-6), `applicant_id: str` (non-empty); stored as given, no length limit. Only `stage` ever changes.

#### 6. Rules
- **R1 (transitions; A-2, A-3).** `allowed_next`: Applied → {Screened, Rejected}; Screened → {Interview, Rejected}; Interview → {Offer, Rejected}; Offer → {}; Rejected → {}.
- **R2 (precondition).** A move succeeds only if `to_stage ∈ allowed_next(current stage)`. Otherwise it returns 409.
- **R3 (postcondition).** After a successful move, the pipeline lists the application under `to_stage`.
- **R4 (refusal).** A 404, 409, or 422 leaves the pipeline unchanged.
- **R5 (invariant).** Each application of a posting appears in exactly one stage list.

#### 7. Edge cases
- A same-stage (Screened → Screened) or backward (Interview → Screened) move: 409.
- A stage name in the wrong case or unknown (`"screened"`, `"Hired"`): 422, not 409.
- An unknown `application_id`; an empty posting (all five keys present).

#### 8. Decisions (D) and open questions (OQ)
- D1. Stage names match exactly and are case-sensitive (A-1).
- D2. Validation is HTTP-layer only, with FastAPI defaults (422 body, path handling), and runs before the lookup (404); extra fields are ignored.
- D3. Storage is one in-memory `ApplicationStore` in `jobsboard.api`: empty at start, a single worker with no locking, creation order kept; tests isolate by unique `posting_id`. Stack per `AGENTS.md`.
- D4. Types live in `jobsboard.pipeline`; exceptions subclass `PipelineError(Exception)` and keep their constructor arguments as attributes; `Application` is a frozen dataclass.

- OQ-1 (Q-3). When an offer is declined or rescinded, where does the application go? Do not build anything that depends on this. Stop and ask.
- OQ-2 (Q-4). Who may set Withdrawn, and can a withdrawn application be reopened? Do not build anything that depends on this. Stop and ask.
- OQ-3 (Q-1). Which stage labels does an applicant see? Do not build anything that depends on this. Stop and ask.
- OQ-4. Can an applicant apply to one posting twice? Do not build anything that depends on this. Stop and ask.

#### 9. Acceptance tests
`tests/test_s1_pipeline.py`:

- AC-1: `test_ac1_applied_to_screened_listed_under_screened`
- AC-2: `test_ac2_skip_applied_to_interview_refused`
- AC-3: `test_ac3_interview_to_rejected_listed_under_rejected`
- AC-4: `test_ac4_rejected_to_screened_refused`

### Gap check for S-1: model reply (`docs/design/S-1-gap-check-reply.md`)
- Model: Claude Code subagent, Claude Opus 5.5 (claude-opus-5-5), 2026-11-09
- Input: `prompts/gap_check_prompt.md` plus `docs/design/S-1.md` at commit 7583dd4 only. The agent was told not to read any other file.
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

### Gap check for S-1: adjudication
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

### Design doc S-3 (`docs/design/S-3.md`)
**S-3.** As an HR recruiter, I want all applicants for a posting listed by fit score, with anyone missing a required skill flagged "Does not meet minimum" and never ranked above an applicant who meets them all, so that I review qualified candidates first instead of reading every resume.

**Status:** designed and tested only; not built in Milestone 1.

#### 1. Problem
Screening 60 resumes to find 3 took two evenings (E-11), a keyword shortlist was mostly rejected (E-12), and mapping experience to requirements is the slowest step (E-13). Managers still advance candidates short on soft skills, so the system flags and never removes (E-14).

#### 2. Scope
Rank a posting's applicants by required skills and fit score, with a flag and missing skills per entry, also over HTTP.

#### 3. Non-goals
- No fit-score calculation (input from S-4), and no automatic rejection or removal (a proposal non-goal).
- No recruiter override of the flag (OQ-2), and no synonym matching (OQ-3).

#### 4. Interface
`jobsboard.ranking`:
- `Candidate` (frozen dataclass): `application_id: str`, `skills: frozenset[str]`, `fit_score: int`.
- `RankedEntry` (frozen dataclass): `application_id: str`, `fit_score: int`, `meets_minimum: bool`, `flag: str | None`, `missing_required: tuple[str, ...]`.
- `rank_applicants(required_skills: frozenset[str], candidates: list[Candidate]) -> list[RankedEntry]`. It raises `InvalidFitScore(application_id, fit_score)`, `DuplicateApplication(application_id)`, or `InvalidSkill(skill)`.

HTTP: `GET /postings/{posting_id}/ranked` returns 200 with a list of `RankedEntry` as JSON (`flag` is `null` when absent), or 404 `{"detail": {"error": "posting_not_found"}}`.

#### 5. Data
- Every skill is non-empty after trimming; `required_skills` may be empty.
- `fit_score: int`, from 0 to 100 inclusive. A `bool` is not accepted.
- `missing_required`: each unmatched required skill's trimmed spelling, once, sorted case-insensitively.

#### 6. Rules
- **R1 (meets minimum; A-5).** `meets_minimum` is true exactly when `missing_required` is empty. Two skills match when they are equal after `strip()` and `casefold()`.
- **R2 (flag).** `flag` is `"Does not meet minimum"` exactly when `meets_minimum` is false, and `None` otherwise.
- **R3 (invariant).** No entry with `meets_minimum` false appears before an entry with `meets_minimum` true.
- **R4 (order).** Within each group, `fit_score` never increases from one entry to the next.
- **R5 (no one dropped).** The output contains each input `application_id` exactly once.
- **R6 (no side effects).** Ranking leaves the input list and every S-1 stage unchanged.

#### 7. Edge cases
- No required skills (everyone meets the minimum), or every applicant flagged; an empty list.
- A flagged applicant scoring 100 against an unflagged one scoring 0 (R3).
- Skills that differ only in case or outer spaces (`" java "` vs `"Java"`); scores of −1 or 101.

#### 8. Decisions (D) and open questions (OQ)
- D1. There is no Unicode normalization and no collapsing of inner spaces. Required skills that are equal after normalizing count as one requirement.
- D2. Within each group, fit score is the only sort key.
- D3. All input is validated before ranking, raising the first problem in list order. Exceptions subclass `ValueError` and keep their constructor arguments as attributes. Out-of-range scores are rejected, not clamped; duplicate IDs are exact string matches.
- D4. M1 covers only `rank_applicants`; the HTTP endpoint is built with S-4, whose score store feeds it. FastAPI per `AGENTS.md`, no authentication (A-4), no pagination.

- OQ-1 (Q-6). How are equal fit scores ordered? Do not build anything that depends on this. Stop and ask.
- OQ-2 (Q-5). Can a recruiter override the flag, and where does an overridden applicant rank? Do not build anything that depends on this. Stop and ask.
- OQ-3 (Q-9). Do skill synonyms (for example "Postgres" for "PostgreSQL") count as a match? Do not build anything that depends on this. Stop and ask.
- OQ-4. Do applications with no fit score yet, or already Rejected, appear in the list? Do not build anything that depends on this. Stop and ask.

#### 9. Acceptance tests
`tests/test_s3_ranking.py`, each skipped with a reason that names its AC; AC-8 checks R6 via the S-1 pipeline:

- AC-6: `test_ac6_flagged_never_above_qualified`
- AC-7: `test_ac7_qualified_ordered_by_fit_score`
- AC-8: `test_ac8_flagged_applicant_kept_and_stage_unchanged`

### Gap check for S-3: model reply (`docs/design/S-3-gap-check-reply.md`)
- Model: Claude Code subagent, Claude Opus 5.5 (claude-opus-5-5), 2026-11-09
- Input: `prompts/gap_check_prompt.md` plus `docs/design/S-3.md` at commit 7583dd4 only. The agent was told not to read any other file.
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

### Gap check for S-3: adjudication
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


## 6. Repository and first story {#d6}

Repository items: `README.md` (install and the one test command `python -m pytest -q`), `AGENTS.md`, `docs/design/`, `docs/plans/S-1-plan.md`, `src/jobsboard/`, `tests/`, `LEDGER.md`, `prompts/`. S-1 was built in four bounded tasks (LEDGER entries 10 to 13).

### 6e. Test output on a fresh clone

`git clone … && python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt && .venv/bin/python -m pytest -q`

```text
....sss                                                                  [100%]
=============================== warnings summary ===============================
.venv/lib/python3.12/site-packages/starlette/testclient.py:40
  /tmp/claude-0/-root-CS690-Project/cb62ce86-28f0-48df-9c4a-7dc1004098a8/scratchpad/clone/.venv/lib/python3.12/site-packages/starlette/testclient.py:40: DeprecationWarning: The anyio.abc.BlockingPortal alias is deprecated, use anyio.from_thread.BlockingPortal instead.
    _PortalFactoryType = typing.Callable[[], typing.ContextManager[anyio.abc.BlockingPortal]]

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
SKIPPED [1] tests/test_s3_ranking.py:17: AC-6: S-3 not built in Milestone 1
SKIPPED [1] tests/test_s3_ranking.py:37: AC-7: S-3 not built in Milestone 1
SKIPPED [1] tests/test_s3_ranking.py:57: AC-8: S-3 not built in Milestone 1
4 passed, 3 skipped, 1 warning in 0.33s
```


## 7. Traceability matrix {#d7}

| Evidence ID | Story ID | AC ID | Test name |
| --- | --- | --- | --- |
| E-5, E-6, E-7 | S-1 | AC-1 | `tests/test_s1_pipeline.py::test_ac1_applied_to_screened_listed_under_screened` |
| E-5, E-6, E-7 | S-1 | AC-2 | `tests/test_s1_pipeline.py::test_ac2_skip_applied_to_interview_refused` |
| E-5, E-6, E-7 | S-1 | AC-3 | `tests/test_s1_pipeline.py::test_ac3_interview_to_rejected_listed_under_rejected` |
| E-5, E-6, E-7 | S-1 | AC-4 | `tests/test_s1_pipeline.py::test_ac4_rejected_to_screened_refused` |
| E-1, E-2, E-3 | S-2 | AC-5 | Not yet written |
| E-11, E-12, E-13, E-14 | S-3 | AC-6 | `tests/test_s3_ranking.py::test_ac6_flagged_never_above_qualified` |
| E-11, E-12, E-13, E-14 | S-3 | AC-7 | `tests/test_s3_ranking.py::test_ac7_qualified_ordered_by_fit_score` |
| E-11, E-12, E-13, E-14 | S-3 | AC-8 | `tests/test_s3_ranking.py::test_ac8_flagged_applicant_kept_and_stage_unchanged` |
| E-11, E-13 | S-4 | AC-9 | Not yet written |
| E-8, E-9, E-10 | S-5 | AC-10 | Not yet written |
| E-10, E-16 | S-6 | AC-11 | Not yet written |
| E-10, E-16 | S-6 | AC-12 | Not yet written |
| E-16, E-17 | S-7 | AC-13 | Not yet written |
| E-18, E-19 | S-8 | AC-14 | Not yet written |
| E-20 | S-9 | AC-15 | Not yet written |
| E-6 | S-10 | AC-16 | Not yet written |
| E-15 | S-11 | AC-17 | Not yet written |
| A-7 (Assumption) | S-12 | AC-18 | Not yet written |
| E-3, E-4 | S-13 | AC-19 | Not yet written |
| E-19 | S-14 | AC-20 | Not yet written |


## 8. Provenance ledger {#d8}

See `LEDGER.md` at the repository root and `prompts/`.


## 9. Contribution statements {#d9}

Submitted individually by each member on Canvas; source in `contribution/`.
