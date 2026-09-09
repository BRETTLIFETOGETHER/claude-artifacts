# Becoming an Expert Claude User — A Personalized Plan for LifeTogether

*Built around your actual work: the 40-day campaign architecture, the blueprint library, Purpose Driven Business, the multi-audience content ladder, and your mobile-first, react-and-refine style.*

---

## How to use this document

This is a 30-day on-ramp followed by a long-term habit system. Don't try to absorb it all at once. Work the 30-day plan (Part 3), keep the prompt templates (Part 5) and checklists (Part 9) open while you work, and treat Parts 1, 7, and 10 as the things you revisit every few weeks to check your growth.

A note up front, because it matters more in ministry than almost any other field: **the single highest-value skill on this entire list is verification** — specifically, catching fabricated Scripture references and misattributed quotes before they reach a congregation. I've put it first in the skill map and given it its own checklist. Everything else makes you faster; this keeps you trustworthy.

---

## Part 1 — The Claude skills to master (mapped to your work)

Think of these in three tiers. You already operate above beginner level on several, so use this to find your gaps rather than starting from zero.

### Tier 1 — Foundation (weeks 1–2)

1. **Verification & theological QC.** Knowing where Claude is reliable (rephrasing, structuring, drafting, summarizing) versus where it confidently invents things (exact Bible citations, quotes attributed to Rick Warren or other real people, statistics, historical claims). This is your non-negotiable core skill.
2. **Clear-instruction prompting.** Naming the task, the audience, the deliverable, the length, and the format in the first line. Your one-line shorthand is already a version of this — the goal is to make it consistent and teachable to Hannah.
3. **Role + context framing.** Telling Claude who it's writing as (a Purpose Driven campaign writer, a youth pastor, a donor-relations director) and who it's writing for (your "Stretched Provider," your 14-year-old freshman centerpoint).
4. **React-and-refine discipline.** You already prefer straw-man drafts over open-ended prompts. The skill is doing it *systematically*: ask for a draft, then steer with specific edits rather than starting over.

### Tier 2 — Intermediate (weeks 3–4)

5. **Examples-driven prompting (few-shot).** Pasting 2–3 examples of your ideal output so Claude matches your house style. This is the fastest way to lock in the LifeTogether voice.
6. **Structured prompting with tags.** Wrapping inputs in labeled sections (`<voice_sample>`, `<doctrine>`, `<audience>`) so Claude knows what each block is. Big quality jump for repeatable work.
7. **Projects & saved context.** Using Claude Projects to hold your brand voice, theological guardrails, and character sheets so you stop re-pasting them every chat.
8. **Prompt chaining.** Splitting a big job into steps (outline → draft → critique → revise) instead of one giant prompt. Each step does one thing well.

### Tier 3 — Advanced / scale (ongoing)

9. **Template and library design.** Turning your best prompts into reusable, parameterized templates — the natural evolution of your master prompt template and shorthand format.
10. **Skills & Artifacts.** Using Claude's Skills (named, reusable instruction sets you trigger by name) and Artifacts (documents/files Claude produces, not just chat text) to make Claude output finished deliverables, not paragraphs you reformat.
11. **Self-critique loops.** Prompting Claude to grade its own draft against a rubric (doctrinal accuracy, pastoral tone, brand fit) before you ever read it.
12. **Automation orchestration.** Wiring Claude into Keyboard Maestro, Stream Deck, and a disciplined file system so a campaign goes from idea to organized draft with minimal manual shuffling. (Parts 8–9.)

---

## Part 2 — Ranked resources (current, with links)

I searched for these so the links are live as of mid-2026. They're ranked by value-for-time *for your specific goals*. Start at the top.

### Free, authoritative, start here

1. **Anthropic's Prompt Engineering documentation.** The official, current source of truth. Read "Be clear and direct," "Use examples," "Chain prompts," and "Use XML tags." → https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
2. **Anthropic's Interactive Prompt Engineering Tutorial.** A 9-chapter, hands-on course with exercises and an answer key. The best structured way to build fundamentals. → https://github.com/anthropics/prompt-eng-interactive-tutorial
3. **Anthropic Academy ("Learn with Claude").** Free courses and guides, including prompt engineering and building with Claude. → https://www.anthropic.com/learn
4. **Anthropic's own prompting best-practices page** for the latest models (covers structuring, examples, thinking). → https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices

### Ongoing learning (subscribe to 2, not 10)

5. **One Useful Thing — Ethan Mollick.** Widely considered the best free newsletter for *applying* AI to real knowledge work. Practical, judgment-focused, not hype. This is the one I'd pick first for you. → oneusefulthing.org
6. **The Batch — Andrew Ng / DeepLearning.AI.** Weekly, authoritative overview with a teacher's clarity. Good for staying current without drowning. → deeplearning.ai/the-batch
7. **A practical-prompts daily** (pick one): *Prompts Daily*, *Superhuman AI*, or *The Neuron* for copy-paste tips and short workflow ideas. Treat as a "skim while having coffee" feed, not homework.

> Tip: if you subscribe to more than three, you'll stop reading them. Two is the sweet spot — one for judgment (Mollick), one for tactics.

### Books

8. ***Co-Intelligence: Living and Working with AI* — Ethan Mollick.** The best single book on the *mindset* of working with AI as a collaborator. Less about prompts, more about how to think. (Verify the current edition; the AI field moves fast and details date quickly.)

### Automation tooling (for Parts 8–9)

9. **Keyboard Maestro** — the macro engine itself, plus its forum (the best place for working examples). → keyboardmaestro.com and forum.keyboardmaestro.com
10. **Asian Efficiency's Keyboard Maestro guide** — solid, current overview of what KM is good at and how to start, including the note that AI can now write macro XML for you. → asianefficiency.com/technology/keyboard-maestro
11. **Sayz Lim's "Integrating ChatGPT into Keyboard Maestro"** — a concrete, replicable pattern for calling an AI API from a KM macro via Apple Shortcuts. The same approach works with Claude's API. → sayzlim.net/chatgpt-keyboard-maestro
12. **Stream Deck + KMLink** — the standard way to trigger any Keyboard Maestro macro from a physical Stream Deck button. Search "KMLink Stream Deck plugin."
13. **Thomas Frank's Mac shortcut/macro library** — a real-world example of someone's full macro/automation stack, useful for ideas you can adapt. → thomasjfrank.com (search "macOS shortcut macro library")

### A caution on resources

Be skeptical of "100 magic prompts" content and anything promising effortless scale. The good material teaches *judgment* (when to use AI, how to verify it); the weak material sells you templates. You'll get more from Mollick's reasoning than from a thousand pre-written prompts.

---

## Part 3 — Your 30-day learning plan

Designed for ~30–45 minutes a day, mobile-friendly, and built so every exercise produces something you could actually use at LifeTogether. Adjust pace freely.

### Week 1 — Foundations + verification habits

- **Day 1:** Read Anthropic's "Be clear and direct." Rewrite three of your recent quick prompts to name task + audience + deliverable + length explicitly. Compare outputs.
- **Day 2:** Read "Use examples." Take one finished LifeTogether piece (a devotional day, a campaign blurb) and use it as a few-shot example to generate a matching one. Note how much closer the voice gets.
- **Day 3 — Verification drill:** Ask Claude to write a 1-day devotional that cites three Bible verses. Then independently check every reference against a real Bible/Bible app. Log any that were wrong, misquoted, or mis-cited. *This is the most important day of the month.*
- **Day 4:** Do chapters 1–3 of Anthropic's interactive tutorial.
- **Day 5:** Build your first "straw-man" workflow deliberately: ask for a rough draft, then steer with 3 rounds of specific edits ("tighten the open," "make the application concrete for a financially-stressed parent," "cut the third point"). Notice this beats re-prompting.
- **Weekend:** Subscribe to One Useful Thing + one tactical newsletter. Read the latest issue.

### Week 2 — Roles, audience, and your house voice

- **Day 8:** Write a reusable **voice brief** for LifeTogether (tone, vocabulary, theology, what you never do). One paragraph. You'll reuse this constantly.
- **Day 9:** Do interactive tutorial chapters 4–6 (roles, formatting, precognition/step-by-step).
- **Day 10:** Re-create one of your character sheets (e.g., the "Stretched Provider") as a context block, and have Claude draft an email *to* that person. Refine until it sounds like you.
- **Day 11:** Repeat for the youth centerpoint (14-year-old freshman). Notice how audience framing changes everything.
- **Day 12 — Verification drill #2:** Ask Claude for a paragraph "in the spirit of Rick Warren." Check that it does **not** fabricate a direct quote attributed to him. Practice rewriting any invented quote as your own paraphrase. (Attributing fake quotes to a real, living author is both a credibility and a legal risk.)
- **Weekend:** Skim the week's newsletters. Save one idea to try.

### Week 3 — Structure, Projects, and chaining

- **Day 15:** Set up a Claude **Project** for "LifeTogether Campaigns." Load your voice brief, theological guardrails, and one character sheet into the project instructions.
- **Day 16:** Learn XML-style tags. Rebuild your master prompt template with labeled blocks: `<voice>`, `<audience>`, `<doctrine>`, `<format>`, `<task>`.
- **Day 17:** Practice **chaining**: Prompt 1 outlines a 40-day campaign theme arc; Prompt 2 drafts week 1; Prompt 3 critiques week 1 against your rubric; Prompt 4 revises. Feel the difference vs. one mega-prompt.
- **Day 18:** Do interactive tutorial chapters 7–9 + the advanced appendix.
- **Day 19:** Take your one-line shorthand format and formalize it: write a one-page "input spec" so Hannah could feed the same shorthand and get consistent blueprints. (This is a real deliverable for your team.)
- **Weekend:** Run a small batch — generate 3 campaign blueprints from shorthand, then QC them. Track error types.

### Week 4 — Scale, self-critique, and your first automation

- **Day 22:** Write a **self-critique prompt**: "Grade this draft A–F on doctrinal accuracy, pastoral tone, brand fit, and clarity; list specific fixes." Run it on a real draft before you read the draft yourself.
- **Day 23:** Turn your three best prompts into parameterized **templates** (Part 5). Save them somewhere you can paste from on mobile (a notes app, a text-expander, or Stream Deck later).
- **Day 24:** Build your **folder structure and naming convention** (Part 9). Migrate one campaign into it.
- **Day 25:** Build your first Keyboard Maestro macro — start trivially simple (a hotkey that pastes your voice brief). Win small, then expand. (Part 8.)
- **Day 26:** Wire one macro to a Stream Deck button (or plan to, if you don't have the hardware yet).
- **Day 27 — Capstone:** Take one rough idea and run it end-to-end through your new pipeline: idea → blueprint → draft → self-critique → human review → organized file. Time it. Note where it dragged.
- **Weekend / Day 30:** Score yourself on the rubric in Part 7. Pick the 2 weakest areas as next month's focus.

---

## Part 4 — Practice exercises (realistic LifeTogether examples)

Use these as drills. They escalate in difficulty.

1. **Voice match:** Give Claude one of your devotional days as an example, then ask for a new one on a different theme. Goal: a reader can't tell which you wrote.
2. **Audience ladder:** Take a single biblical concept (e.g., stewardship) and write it three ways — wonder for kids, identity/honesty for teens, freedom/stewardship for adults — keeping your content-ladder logic. Goal: one idea, three authentic registers.
3. **Shorthand stress-test:** Feed five different one-line shorthand inputs and generate five blueprints. Then audit: did the template hold? Where did Claude drift? Fix the template, not just the outputs.
4. **The Stretched Provider letter:** Draft a campaign-week email *to* that character. Then a donor update *about* serving people like them. Notice how the same audience reframes as recipient vs. subject.
5. **Misquote hunt:** Ask for a teaching outline with five Scripture references and one Rick Warren-style insight. Find every error: wrong verse numbers, paraphrases presented as direct quotes, invented attributions. This trains the most valuable instinct you'll build.
6. **Brochure rescue:** Take rough bullet notes for the next title-catalog brochure and have Claude shape them into your dark-luxury editorial style, then critique its own typography/voice choices.
7. **Purpose Driven Business pitch:** Draft a one-page case-study summary aimed at a C12 or Convene audience, then have Claude red-team it from a skeptical CFO's perspective.

---

## Part 5 — Reusable prompt templates for ministry work

These are parameterized. Replace the `[BRACKETS]`. Keep them somewhere you can paste from quickly. They're written to fit your react-and-refine style — they ask for a draft you then steer.

### Template A — Master campaign blueprint (your core engine)

```
You are a campaign writer in the Purpose Driven / Rick Warren tradition, writing for LifeTogether.

<voice>
[PASTE YOUR LIFETOGETHER VOICE BRIEF]
</voice>

<audience>
[PASTE THE RELEVANT CHARACTER SHEET — e.g., Stretched Provider, or 14-yr-old freshman]
</audience>

<doctrine>
Stay within historic, broadly evangelical orthodoxy. Do NOT invent Bible
references — only cite verses you are confident are correct, and flag any
you are unsure about with [VERIFY]. Never attribute a direct quote to Rick
Warren or any real person; paraphrase ideas instead.
</doctrine>

<task>
Draft a 40-day campaign blueprint on the theme: [THEME].
Include: a one-line big idea, a 6-week arc, weekly focus statements, and
3 sample daily devotional titles per week.
Format: [FORMAT]. Length: [LENGTH].
</task>

Give me a straw-man draft I can react to. Keep it tight; I'll steer from here.
```

### Template B — One-line shorthand expander

```
Using the LifeTogether blueprint template and voice already in this project,
expand each shorthand line below into a full blueprint. Flag any [VERIFY]
Scripture and any place you had to guess at intent.

Shorthand:
[PASTE YOUR ONE-LINE SHORTHAND LINES]
```

### Template C — Audience-ladder rewrite

```
Take this concept: [CONCEPT].
Write three versions following our content ladder:
- Kids edition: wonder
- Teen edition: identity/honesty (centerpoint: 14-yr-old freshman)
- Adult edition: freedom/stewardship (centerpoint: Stretched Provider)
Keep the through-line identical so a family experiences one unified idea.
Draft first; I'll refine.
```

### Template D — Self-critique / QC pass

```
Grade the draft below A–F on each: (1) doctrinal accuracy, (2) pastoral
sensitivity, (3) LifeTogether brand/voice fit, (4) clarity for [AUDIENCE].
Then list the specific fixes. Separately, list every Scripture reference and
mark each as VERIFIED-LOOKS-RIGHT or NEEDS-HUMAN-CHECK. Do not rewrite yet.

Draft:
[PASTE DRAFT]
```

### Template E — Communications (email / social / donor)

```
Audience: [WHO]. Channel: [email / Instagram / donor letter].
Goal: [the one action or feeling you want].
Tone: [warm, pastoral, urgent-but-not-pushy...].
Constraints: [length, must-include, must-avoid].
Draft 2 versions with different strategies (e.g., story-led vs. direct-ask).
I'll pick and refine.
```

### Template F — Rough idea to polished outline

```
Here are my rough, unstructured notes. Don't add new theology or claims —
organize and sharpen what's here. Produce a clean outline, flag gaps where
I need to add content, and mark anything that needs a source.

Notes:
[BRAIN DUMP]
```

> Pattern to internalize: every template ends by inviting your steer ("draft first; I'll refine") and every content template carries the **[VERIFY] / NEEDS-HUMAN-CHECK** instruction. That second habit is what keeps scale safe.

---

## Part 6 — Common mistakes to avoid

- **Trusting Scripture citations.** Claude will produce wrong verse numbers and present paraphrases as direct quotes with total confidence. Check every reference, every time. This is the #1 risk in your field.
- **Letting it invent quotes from real people.** Fabricated Rick Warren (or any author) quotes are a credibility and legal hazard. Paraphrase ideas; never present invented words as someone's quotation.
- **Mega-prompts.** Cramming outline + draft + edit + format into one prompt produces mush. Chain instead.
- **Re-prompting instead of steering.** When a draft is 70% right, fix it with specific edits — don't start over. (You already lean this way; keep it.)
- **Skipping the voice example.** Describing your voice is weaker than *showing* one example of it. Always paste a sample.
- **Scaling before the template is solid.** Don't batch 50 blueprints off a template you haven't QC'd on 3. Errors multiply.
- **Automating judgment.** Automate the *mechanical* steps (paste, file, format). Never automate the *pastoral* or *doctrinal* decision points.
- **No paper trail.** If you don't save the prompt that produced a great output, you can't reproduce or improve it. Capture prompts, not just outputs.
- **Over-polishing in chat.** For finished documents, have Claude produce an Artifact/file rather than reformatting chat text by hand.

---

## Part 7 — Measuring your progress (a simple rubric)

Score yourself 1–5 on each every few weeks. "Expert" is roughly 4+ across the board.

| Skill | 1 (novice) | 3 (competent) | 5 (expert) |
|---|---|---|---|
| **Verification** | Trusts outputs | Spot-checks Scripture | Catches every fabricated cite/quote reflexively |
| **Prompt clarity** | Vague asks | Names task + audience | Consistent, teachable spec others can reuse |
| **Voice control** | Generic AI tone | Sometimes on-brand | Reliably indistinguishable from your hand |
| **Chaining** | One big prompt | Splits some steps | Designs clean multi-step pipelines |
| **Templates** | Re-types each time | A few saved prompts | Parameterized library Hannah can run |
| **Self-critique** | Reads raw output | Occasionally asks for review | Drafts auto-graded before you read them |
| **Automation** | All manual | A macro or two | Idea→organized draft with minimal manual work |
| **Judgment** | Over- or under-uses AI | Knows rough limits | Knows exactly what to automate vs. protect |

Three concrete milestones to aim for:
1. **Reproducibility:** you can hand a prompt template to Hannah and she gets near-identical quality.
2. **Throughput with safety:** you can produce a batch of campaign blueprints *and* your QC catches errors before they ship.
3. **One-touch start:** a single button/hotkey sets up a new campaign with voice, audience, and guardrails pre-loaded.

---

## Part 8 — Automation roadmap (think like a systems designer)

The mindset: **automate the plumbing, never the pastoring.** Macros should move text, files, and prompts around so your human attention is spent only on judgment — theology, tone, the actual ideas.

A realistic progression — don't skip ahead:

**Stage 0 — Text snippets (this week).** Before any macros, put your voice brief, character sheets, and Part 5 templates into a text expander (the built-in one on Mac/iOS, or an app). Typing `;voice` pastes your voice brief. This alone removes most repetitive friction and works on mobile.

**Stage 1 — Simple Keyboard Maestro macros (paste & launch).**
- *"New Campaign" macro:* opens your campaign folder template, your Claude project, and pastes your master blueprint template, all from one hotkey.
- *"Paste Voice Brief" macro:* mapped to a hotkey, types your voice brief into any field.
- *"Paste QC Prompt" macro:* drops Template D so you can grade any draft instantly.
- Tip: you can ask Claude to *write the Keyboard Maestro macro XML* for you in plain English, then import it — the KM community does this routinely now. Always review imported macros before trusting them.

**Stage 2 — Stream Deck buttons (physical, glanceable).**
Use the **KMLink** plugin so a Stream Deck button triggers any KM macro. A practical button layout:
- Button 1: New Campaign setup
- Button 2: Paste Voice Brief
- Button 3: Paste Blueprint Template
- Button 4: Paste QC / Self-Critique prompt
- Button 5: Paste Audience-Ladder prompt
- Button 6: "File this output" (see Stage 3)
- A folder button for "Donor / Comms" prompts vs. "Campaign" prompts

**Stage 3 — File-and-organize automation.**
A macro that takes a finished Artifact, names it by your convention (Part 9), and drops it in the right folder. This is where you reclaim the most time.

**Stage 4 — API-level automation (optional, more technical).**
Following the Sayz Lim pattern, a KM macro can send your clipboard to Claude's API via Apple Shortcuts and return the result — e.g., select rough notes, hit a hotkey, get a cleaned-up draft back in place. There's also a Keyboard Maestro MCP server that lets Claude itself trigger and manage your macros conversationally. Treat Stage 4 as a "once Stages 1–3 are humming" project, and review everything it produces; giving an AI access to run macros warrants caution.

**Hardware note:** Keyboard Maestro and Stream Deck are Mac/desktop tools. Since you work primarily on mobile, lean on text expanders and Claude Projects on mobile, and treat the Mac as your "studio" for heavier batch sessions.

---

## Part 9 — Repeatable systems for ministry resources

Here's the part where you stop doing one-off work and start running pipelines.

### Folder structure & naming conventions

A clean, predictable tree (adapt names to taste):

```
LifeTogether/
├── 00_Brand/                  (voice brief, style guide, logos, guardrails)
├── 01_Character-Sheets/       (Stretched Provider, Freshman, etc.)
├── 02_Prompt-Library/         (your Part 5 templates, versioned)
├── 03_Campaigns/
│   └── [CampaignName]/
│       ├── 0_Brief/
│       ├── 1_Blueprint/
│       ├── 2_Drafts/
│       ├── 3_QC/
│       ├── 4_Final/
│       └── 5_Assets/          (brochure, emails, social, donor)
├── 04_PurposeDrivenBusiness/
└── 99_Templates/              (blank campaign folder to copy)
```

**Naming convention:** `YYYY-MM-DD_Project_Asset_Audience_vNN`
e.g., `2026-07-01_StewardshipCampaign_Devotional_Teen_v03`
Consistent names make automation (and search) trivial and let you sort by date, project, or version at a glance.

### Prompt library discipline

Version your prompts like code. When a template improves, save it as `v04` and note what changed and why. Your best outputs become tomorrow's examples — keep a `Gold/` folder of exemplary results to paste as few-shot samples.

### A content production pipeline (the repeatable flow)

For any resource — campaign, brochure, email series, teaching series, donor update:

1. **Brief** — capture the idea + audience + goal (Template F).
2. **Blueprint/outline** — generate structure (Template A or E).
3. **Draft** — generate content, react-and-refine.
4. **Self-critique** — Claude grades against rubric (Template D).
5. **Human review** — *you or Hannah*: theology, tone, Scripture check, brand.
6. **Finalize** — Claude produces the clean Artifact/file.
7. **File & template-ize** — name it, store it, and if it's excellent, copy the winning prompt into your library.

### Quality-control checklist (run before anything ships)

- [ ] Every Scripture reference independently verified against a real Bible
- [ ] No invented direct quotes attributed to Rick Warren or any real person
- [ ] Doctrine within your stated guardrails
- [ ] Pastoral tone appropriate (especially anything touching grief, money stress, sin, suffering)
- [ ] Brand voice matches the LifeTogether brief
- [ ] Audience fit confirmed (right register for kids/teens/adults)
- [ ] Facts, stats, names, dates checked
- [ ] No accidental AI tells ("As an AI," generic filler, em-dash overload)
- [ ] A human read the whole thing, not just skimmed

### Batching responsibly

- **QC the template on 3 before running 30.** Errors in a template multiply across a batch.
- **Batch the generation, never the review.** It's fine to generate 20 blueprints at once; it's not fine to publish 20 without 20 human reads.
- **Sample-audit large batches:** review 100%, but track error *rates* so you know which templates are reliable and which need work.
- **Keep a "drift log":** note where Claude consistently wanders off-template, then tighten the template.

### Turning outputs into future templates

After each project, ask: *what here is reusable?* Promote winning prompts to your library (versioned), winning outputs to your `Gold/` examples, and recurring fixes into the template itself so you never make the same correction twice. This is the compounding loop — every campaign makes the next one faster.

---

## Part 10 — What to automate, what not to, and where human review matters most

A clear line to hold:

### Safe to automate (mechanical)
- Pasting voice briefs, character sheets, templates
- Setting up campaign folders and naming files
- First-draft generation and outlining
- Reformatting and producing finished file Artifacts
- Summarizing your own notes and transcripts
- Generating *options* for you to choose from (subject lines, titles, social variants)

### Automate with a mandatory human gate
- Anything quoting Scripture (verify before it ships)
- Donor communications and fundraising appeals (trust and stewardship are on the line)
- Anything attributed to a real person
- Public-facing campaign copy and brochures (brand + doctrine)
- Teaching content others will treat as authoritative

### Never automate (human only)
- **Pastoral care and crisis response** — grief, suffering, conflict, confession, anyone in distress. These require a real person, full stop. Don't let a macro draft a reply to someone in pain.
- **Final theological judgment** — what your ministry actually affirms and teaches.
- **Personal, relational messages** — the ones whose value is precisely that *you* wrote them.
- **Decisions about people** — hiring, discipline, membership, leadership.

### Where human review matters most
In order: **(1) Scripture accuracy, (2) pastoral sensitivity, (3) doctrinal soundness, (4) attribution of quotes/claims, (5) brand voice.** If you only have time to check one thing, check the Bible references. If you have time for two, add: does this sound like it loves the reader?

The deeper principle for a ministry: AI can scale your *output*, but it must never scale your *judgment* or stand in for *presence*. Use it to clear the mechanical work off your plate so you and Hannah have more attention for the parts only humans should do — discernment, care, and the actual relationships your content exists to serve.

---

## Your immediate next three steps

1. **Today:** Write your one-paragraph LifeTogether voice brief and run the Day-3 verification drill so you feel the fabrication risk firsthand.
2. **This week:** Set up the "LifeTogether Campaigns" Project with voice + guardrails + one character sheet, and save the Part 5 templates where you can paste them on mobile.
3. **This month:** Work the 30-day plan, then score yourself on Part 7 and pick two areas to deepen.

You're already operating well above beginner level — your shorthand format, character sheets, and content ladder are real systems-thinking. The jump to "expert" here is mostly about three things: ruthless verification habits, turning your good instincts into *documented, repeatable* templates Hannah can run, and building the plumbing so scale stays safe.
