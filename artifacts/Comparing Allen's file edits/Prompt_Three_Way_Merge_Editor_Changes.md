# Reusable Prompt — Three-Way Merge: Porting an Editor's Changes Into a Reformatted File

Paste the block below into a new chat with **all three files attached**. Label them clearly in the upload or name them in the first line so the roles are unambiguous.

---

I'm attaching three files. They are three points on a branching history, not three drafts in a line, and I need you to treat them that way.

**File A — BASE.** The untouched original. Neither branch has touched it. This is the common ancestor.

**File B — EDITOR BRANCH.** File A after my collaborator Allen made an editorial pass. He did not use tracked changes, so his work exists only as untracked differences from File A.

**File C — CURRENT.** File A after my team reformatted it and made our own separate edits. This is the live file and the one everything ships from. It never saw Allen's work and Allen never saw it.

The two branches diverged from File A independently. I need to know what Allen actually changed, and then, for every one of those changes, whether it still applies to File C and whether I should take it.

This is a three-way merge with judgment attached. Do not simply diff File B against File C — that would mix Allen's changes together with my team's reformatting and I would not be able to tell whose work is whose.

---

## Method

**Step 1 — Derive Allen's changeset.**

Convert all three files with `pandoc -t markdown --wrap=none file.docx -o file.md`. Diff File A against File B. That difference, and only that difference, is Allen's changeset. Nothing from File C enters at this stage.

Before diffing, unzip each DOCX and check `word/document.xml` for `<w:ins`, `<w:del`, and `<w:commentReference`, in case any file carries a real redline or margin comments I don't know about. Also check `docProps/core.xml` for author and revision metadata. Report what you find, including finding nothing — a clean file is expected from a Google Docs export and is not evidence that no edits were made.

Confirm the direction of File A to File B from the edits themselves rather than from filenames, and tell me what the evidence was. Cleanup moves that only make sense in one direction — added punctuation, repaired sentences, corrections — reveal which way the work flowed. If the direction contradicts what I've told you, say so and stop.

Merge adjacent edits inside a single paragraph into one coherent revision rather than fragmenting them into separate entries.

**Step 2 — Establish pagination for File C.**

Render File C to PDF, extract text per page, and report the total page count so I can sanity-check it against Word. All page numbers in your output refer to File C, because File C is the file I will be editing. Where useful, also give me the File B page number so I can look at Allen's version in context, but make clear which is which.

If File C contains more than one guide in a single document, identify the boundary page and label every entry by guide and session. If the reformat split what used to be one file into several, say so and map accordingly.

**Step 3 — Test every Allen change against File C.**

For each change in Allen's changeset, search File C for both the File A wording and Allen's replacement wording. The reformat may have changed line breaks, spacing, styling, and pagination, so match on normalized text — collapse whitespace, normalize quotes and dashes, strip formatting markup — and use fuzzy paragraph matching rather than exact string comparison. Sort each change into one of four buckets:

**ALREADY PRESENT** — Allen's wording, or a functionally equivalent rewrite, is already in File C. My team made the same call independently. No action. List these compactly; I only need to confirm the count and scan for surprises.

**STILL OPEN** — File C carries the File A wording unchanged. Allen's edit ports cleanly and mechanically. Give me the File C page number, the current wording, and Allen's replacement, and your recommendation on whether to take it.

**SUPERSEDED** — Neither the File A wording nor Allen's wording is in File C, because that passage was rewritten during the reformat. This is where the real work is. For each one, show me the File A wording, Allen's change, and the current File C wording side by side, then tell me what Allen was actually trying to fix and whether that problem still exists in the new sentence. If it does, write me the specific replacement wording for the current sentence rather than telling me to think about it. If it doesn't, say the concern is resolved and move on.

**REMOVED** — The passage Allen edited no longer exists in File C at all. Confirm it's genuinely gone rather than relocated before you put anything in this bucket. List these briefly so I know his work there is dead.

**Step 4 — Separate policies from one-off edits.**

Some of Allen's changes are individual wording improvements. Others are systematic passes he applied across the document — a global replacement, a parallelism fix repeated in every instance, a formatting convention. Identify every systematic pass, state the rule he was applying, and count how many instances he caught.

Do not port a systematic pass instance by instance. Re-run the rule against the whole of File C and give me a complete list of every place in File C where it should apply, including places that did not exist in File A and that Allen therefore never saw. Note anywhere he applied the rule inconsistently or left it half-finished, and tell me how many instances he missed in his own file, since that tells me how much to trust the pass.

---

## Do not port these

Six of Allen's changes introduce errors. They exist only in File B. Verify each one is absent from File C, flag it if it somehow made it in, and never recommend porting it:

1. "Plan on 75 to 90 minutes" changed to "Plan **spending** on 75 to 90 minutes." Find-and-replace collateral damage.
2. "son was in first grade, and the school ran" changed to "son was in first grade,**.** The school ran." Comma followed by period.
3. "what we already carry, the hours" changed to "what we already carry **–** the hours." Dash introduced into original prose.
4. "the giving was already set, already gone" changed to "the giving was already set **–** already gone." Dash introduced into original prose.
5. "start sharing **that** the business model simply cannot explain" changed to "start sharing **–** the business model simply cannot explain." The dash breaks the sentence; it no longer says what it cannot explain.
6. Assessment item: "I **have** the honest money conversations" changed to "I **have had** the honest money conversations." Breaks tense parallelism with the five surrounding items and changes what a low score means.

Note on 3, 4, and 5: those are **en dashes**, not em dashes. Search for both characters separately. A search for an em dash will not find them.

---

## Audit File C independently while you're in there

Separately from the merge, flag anything in File C that violates these standing rules, including violations my own team introduced during the reformat:

- Em-dashes and en-dashes are prohibited in original prose. Search both characters.
- "Legacy" is retired from published, viewer-facing session-level titles and replaced with "Impact." Internal alignment tags and devotional day titles are exempt.
- Self-help language is excluded from original prose.
- Triplet rhetorical structures are avoided in original prose.
- Psalm 24:1 cannot appear; it is anchored in the companion Master Your Money study.
- Scripture is NIV unless a documented exception applies to this tier. Flag any silent substitution.
- All LifeTogether interviewees are anonymized by default. Flag inconsistent anonymization phrasing.
- No guilt-driven generosity framing.
- Icebreaker questions must match the video's actual opening.
- Discussion questions create tension rather than deliver conclusions.

Also catch what a careful editor catches: typos, find-and-replace collateral damage, tense and parallelism breaks inside numbered assessment blocks, grammatically incomplete sentences, number-style drift, and half-finished global replacements.

**Check sync.** Where the same content appears in more than one place — a leader guide and a participant guide, a script and its printed version, parallel tiers — content that is supposed to be word-for-word identical must still match. A half-applied pass that leaves a leader reading one thing while the room reads another is the most expensive error in this document and it is invisible in a normal read, because each copy reads fine on its own.

---

## Deliverable

A single markdown file containing, in this order:

1. **Header.** What was compared, confirmed direction of File A to File B, total changes in Allen's changeset, File C page count, and whether the reformat moved structure or only presentation.

2. **Decision list.** Every STILL OPEN and SUPERSEDED item, which are the only ones requiring action from me. Table or entry format, each showing: File C page number, locator such as "Item 4" or "Welcome script" or "Leader cue," the current File C wording, Allen's change, and your recommendation with one line of reasoning. Order by page so I can work straight through the file.

3. **Systematic passes.** Each rule Allen applied, how completely he applied it, and the full list of File C locations where it should apply, with page numbers.

4. **Already present.** Compact list, page numbers only, confirming what needs no action.

5. **Removed.** Brief list of Allen's work that died in the reformat.

6. **Independent audit of File C.** Rule violations and editorial errors found in the current file regardless of the merge, with page numbers.

7. **Cross-tier flags.** Anything that is really a campaign-wide voice or style decision rather than a change to this file, named as a decision, with the other tiers it touches.

Give me the specific replacement wording everywhere a decision is needed. Do not hand me a problem without a proposed fix.

---

## Discipline

Do not reconstruct project history from inference. If you cannot tell whether something in File C was a deliberate choice by my team or an error introduced during the reformat, say so and ask rather than assuming. Where Allen's change is defensible and I would likely disagree with taking it, say that too. I want your read on which of these are genuine improvements, not a mechanical list of everything that differs.

If any file turns out not to be what I've said it is — if File C did not come from File A, or if Allen's branch already contains reformat work — tell me before doing the analysis. The whole method depends on File A being the true common ancestor.

---

## Notes for reuse

**If Allen left margin comments in the Google Doc,** they will not survive a DOCX export and are not in any of these files. They're still in the live Google Doc and have to be pulled from there. Worth checking before assuming the inline edits were everything he gave you.

**If the reformat split one file into several,** attach all pieces of File C and say so in the first line. The prompt handles it, but the model needs to know the boundary is a file boundary rather than a page boundary.

**For the devotional,** add: *check that anchor titles and locked title/subtitle pairings are preserved word-for-word across all format versions.* For Off Script scripts, add: *distinguish spoken script from on-screen and viewer-facing copy, and flag prohibited words in the latter separately.*
