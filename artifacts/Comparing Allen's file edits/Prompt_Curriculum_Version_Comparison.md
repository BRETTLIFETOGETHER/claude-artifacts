# Reusable Prompt — Curriculum Version Comparison & Edit Log

Paste the block below into a new chat with **both DOCX versions attached**. Replace the bracketed line with the tier you're checking. Everything else stays as written.

---

I'm attaching two versions of the same curriculum document: **[Generous Living — Student Edition / Elementary Leader Guide / Preschool Leader Guide / Off Script scripts / 40-Day Devotional]**. One is a live working file, one is an older snapshot. An editorial collaborator made changes and did not use tracked changes. I need to know exactly what changed, where, and what's now broken.

Work as my senior editor, not as a diff tool. I want judgment, not just a list.

**Method**

Convert both files with `pandoc -t markdown --wrap=none file.docx -o file.md`, then run a standard `diff`. Before that, unzip each DOCX and check `word/document.xml` for `<w:ins`, `<w:del`, and `<w:commentReference` in case there is a redline record I don't know about, and check `docProps/core.xml` for author and revision metadata.

Determine which file is newer by looking at the direction of the edits rather than the filename, and tell me what the evidence was. Cleanup moves — added punctuation, repaired garbled sentences, corrections that only make sense in one direction — reveal which way the work flowed.

For page numbers, render the current file to PDF and extract text per page, then map each change to a page. Tell me the total page count so I can sanity-check against Word. If the document contains more than one guide in a single file, identify the boundary page and label every change by guide and session, since shared content appears twice and I need both locations.

**What I need to know first**

Separate structural change from line editing. Did anything get added, deleted, reordered, or restructured — headings, locked titles and subtitles, fill-in blanks, assessment items, day listings, scripture references? Say so plainly up front. If it's purely a line-editing pass, say that too.

**Audit against these standing rules**

Flag any change that violates or introduces a violation of:

- Em-dashes and en-dashes are prohibited in original prose. Search for both characters separately; they are easy to miss with one search.
- "Legacy" is retired from published, viewer-facing session-level titles and replaced with "Impact." Internal alignment tags and devotional day titles are exempt.
- Self-help language is excluded from original prose.
- Triplet rhetorical structures are avoided in original prose.
- Psalm 24:1 cannot appear; it is anchored in the companion Master Your Money study.
- Scripture is NIV unless a documented exception applies to this tier. Flag any silent substitution.
- All LifeTogether interviewees are anonymized by default. Flag inconsistent anonymization phrasing.
- No guilt-driven generosity framing.
- Icebreaker questions must match the video's actual opening.
- Discussion questions create tension rather than deliver conclusions.

Beyond the rule list, catch what a careful editor catches: typos introduced, find-and-replace collateral damage, tense and parallelism breaks inside numbered assessment blocks, sentences left grammatically incomplete, number-style drift, and any half-finished global replacement where some instances were caught and others weren't.

**Where the same content appears in more than one place, check sync.** Scripts, stories, questions, and assessments that are supposed to be word-for-word identical across guides or across tiers must still match after the edits. A half-applied pass that leaves a leader reading one thing while the room reads another is the most expensive error in this document, and it is invisible in a normal read.

**Deliverable**

A single markdown file containing:

1. A short header stating what was compared, which file is newer, the paragraph-level change count, and whether structure moved.
2. A fix list at the top — every change that introduces an error, in a table, with page numbers, the exact was/now wording, and one line on why it's a problem. Anything I have to act on goes here so I don't have to read the full log to work.
3. The full log, grouped by guide and session, each entry showing page number, a locator such as "Item 4" or "Welcome script" or "Leader cue," and the was/now wording with enough surrounding words that I can find it in the file. Merge adjacent edits inside one paragraph into a single coherent revision rather than fragmenting them.
4. An appendix for any global pass that was started and not finished, listing every surviving instance with page number and section.

Flag entries inline: **[FIX]** for errors to correct, **[EVE]** or a comparable tag for changes that are part of an intentional pass I should keep but complete.

**Discipline**

Don't reconstruct project history from inference. If you're unsure whether something is an error or a deliberate call I made, say so and ask rather than assuming. If a change is defensible and I'd likely disagree with reverting it, say that too — I want your read on which of these are improvements, not a list of everything that moved.

Close with any cross-tier implication: if a change here is really a campaign-wide voice or style decision, name it and tell me which other tiers it touches before they lock.

---

## Notes for reuse

**Devotionals and scripts need one change.** The devotional has no Leader/Participant split, so drop the boundary-detection line and add: *check that anchor titles and locked title/subtitle pairings are preserved word-for-word across format versions.* For Off Script scripts, add: *flag any prohibited word appearing in on-screen or viewer-facing copy as distinct from spoken script.*

**Google Docs exports carry no redline.** Every file exported from Google Docs will come back clean on the tracked-changes check. That's expected, not a sign nothing was edited. If you want a real redline going forward, the fix is upstream: have collaborators work in Word with track changes on, or pull the version history from Google Docs directly before exporting.

**If the two files came from Google Docs version history,** the named-version timestamp in the filename is the reliable marker of which is older, but confirm it against edit direction anyway. Filenames get copied and renamed.
