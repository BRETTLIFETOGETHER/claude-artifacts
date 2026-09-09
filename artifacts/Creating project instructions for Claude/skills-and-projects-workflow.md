# How to Turn Your Repeated Work Into Skills + Projects

A repeatable process for consultants managing multiple books, curricula, and clients in Claude.

---

## Part 1 — Turn a repeated process into a Skill

A Skill is a folder of instructions Claude reads before doing a task, so you stop re-explaining your format every chat.

**Steps:**
1. **Name the repeated process.** Pick one: a format, a structure, or a voice. Don't combine all of them into one skill on the first try — narrow beats broad.
2. **Decide where the pattern comes from.** Either pull it from work you've already produced (fast, but inherits any gaps in that sample), or paste 2–3 sentences of your own raw writing (slower, but more accurate).
3. **Draft the SKILL.md.** Structure:
   - `name` + a **pushy** `description` (states exactly when to trigger — Claude under-triggers skills by default, so be explicit and a little insistent)
   - Body: the actual rules, patterns pulled from real examples, a word bank (reach for / avoid), and a short self-check list
   - Flag any known gaps instead of pretending the pattern is finished
4. **Package it.** A `.skill` file installs in one click; a plain `.md` file works too if you want to edit the text yourself first.
5. **Install:** Settings → Capabilities → enable Code execution and file creation → Customize → Skills → upload.
6. **Test it live** in any chat — no need to name the skill, just ask for the task normally.
7. **Iterate.** When the output feels close but not quite right, paste a corrected example back and ask Claude to re-derive the rule from it — that's more reliable than describing the fix in the abstract.

---

## Part 2 — Set up a Project to hold context

A Project is the ongoing memory for one specific body of work — a book, a client, a curriculum library. It holds files and standing instructions so you don't re-explain the work every time you open a new chat inside it.

**Steps:**
1. **Create a Project** per distinct body of work (one per book, one per client, one per curriculum library — not one giant Project for everything).
2. **Upload reference files**: drafts, brand docs, prior outputs, anything Claude should be able to read without you re-pasting it.
3. **Write Project Instructions** (Project settings → Edit instructions). Good instructions cover:
   - Standing context (who/what this project is, any positioning constraints)
   - Fixed structural rules (e.g., "every campaign = 6 weeks, with X, Y, Z outputs")
   - Which Skill(s) should auto-apply inside this project
   - A running-state tracker (what's drafted, what's approved, what's still brainstorm)
4. **Keep the tracker current.** Ask Claude to update the state section as work progresses so future chats in the Project pick up exactly where you left off.

---

## When to repeat this

- **New Skill** whenever you notice yourself re-explaining the same format, structure, or voice rule across chats — even in different Projects.
- **New Project** whenever you start a genuinely separate body of work (new book, new client, new curriculum line).

Skills travel across Projects. Projects don't travel across bodies of work — keep them separate.
