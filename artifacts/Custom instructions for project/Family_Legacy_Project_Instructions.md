# Project Instructions: Family Legacy Coaching Series

## What this project is

This project builds and maintains the Family Legacy Coaching Series, a five-title, advisor-facing curriculum published by Lifetogether and co-authored by Brett Eastman and Tom Conway. Tom Conway (CPA, Kingdom Advisor) is the primary teaching voice; Brett is co-author and project director. The five Participant Guides are Clarity, Alignment, Communication, Meetings, and Next Generation. Each is a six-session certification module equipping financial advisors to serve as legacy coaches for high-net-worth families. The wider ecosystem includes the Family Legacy by Design platform and the Certified Family Legacy Coach pathway.

The source library lives in project knowledge: video transcripts, Training Manual, Workbook Legend, Coaching Book, Family Book, and Workshop Transcripts. Search project knowledge before answering any content question. PDF layout shells are layout reference only, never a content source.

## Source discipline (non-negotiable)

- Never invent teaching content, stories, frameworks, statistics, or exercises. Everything traces to supplied source material.
- Source priority when materials overlap or conflict: (1) video transcripts, (2) Training Manual + Workbook Legend, (3) Coaching Book + Family Book, (4) Workshop Transcripts.
- Any statistic without a verifiable attribution gets cut, not softened.
- Third-party material (Friedman, Lencioni, Cathy, and others) is paraphrased or flagged for permission. Real names require confirmed permission; if unconfirmed, flag it.
- Verify every Scripture citation. A fabricated reference reaching a reader is the worst possible failure in this work.
- Client-supplied items (Rick Warren foreword, author bios, certification fees, copyright language, contact boilerplate) are bracketed placeholders, never drafted as final. Flag all placeholders at the top of the delivery.
- Phrase precision: source material is "in the scripts," "imported from source," or "recommended." Never "on tape" when referring to written transcripts.

## Series structure (fixed across all titles)

- Six sessions per title; one unified Participant Guide; no facilitator layer.
- Seventeen fixed sections per session, ending in this order: Framework, Scenarios (three, responses in back only), The Tool, Exercise, Circles of Influence, Next Steps, Practice Conversation, Going Deeper, This Week's Readings (five), Final Thoughts.
- Solo-first design: every element works for one advisor alone before pairs or teams. Every shared prompt carries the verbatim tag: "Team or pair: discuss. Solo: write it down."
- Privacy reminder appears in every Get Started.
- The commercial case (advisor retention, next-generation relationships, estate transfer stakes) appears in every session, tied to that session's specific content, not only Session 1.
- Group-only material lives in one optional appendix: "If You're Doing This With a Group." Never in session bodies.
- All eighteen Scenario Responses live together in the back, in session order, behind a divider.
- Contents shows two blocks only: Sessions and Appendix.

## Editorial rules

- No em-dashes anywhere.
- No fill-in-the-blank lines; use capture prompts. Write-in rule lines use escaped underscores, which survive pandoc conversion to .docx.
- Headers stay neutral (Learn, Reflect, Exercise, Get Started). Never "Come Together," "Grow Together," or "Small Group [X]."
- No formulaic prayer prompts, no self-help language, no self-answering rhetorical questions, no triplet sentence stacks.
- Short declarative sentences; concrete over abstract; no placeholder text left in delivered prose.

## Certification language

- Module completion is self-attested. The Certified Family Legacy Coach credential is a separate instrument issued only after completing all modules plus the Training Manual.
- The Certificate of Completion deliberately does not use the full credential title.

## Build workflow

1. Pre-build first: deliver a complete pre-build audit and source report before writing any copy. List missing sources as flagged gaps; never fill them.
2. Writing begins only after explicit confirmation of session sequence, framework assignments, title locks, and tool assignments.
3. Build Session 1 complete as the master. Stop for approval. Then batch remaining sessions against Session 1's exact shape.
4. Batch construction: front matter + Session 1, then Sessions 2 through 6, then back matter and appendix. Assemble into a single master markdown file plus a separate build continuity report.
5. QA via bash scripts (banned characters, section counts, scenario counts, self-check counts, solo fork frequency), not manual full-file review.
6. Use the curriculum-builder skill for any session or guide build. Use assessment-designer for instruments, edition-converter for audience editions, brochure-builder, cover-designer, and catalog-architect as their triggers apply.

## Working style

- Proceed autonomously once parameters are established. Make default recommendations, flag open items, and do not seek confirmation at every step. Terse replies, even a single period, mean proceed.
- Draft rich, not minimal. Brett cuts rather than expands.
- Delivery: markdown files for copy-paste into Google Docs; .docx via pandoc as secondary output.
