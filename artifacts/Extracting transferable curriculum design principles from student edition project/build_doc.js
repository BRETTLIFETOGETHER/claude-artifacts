const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  LevelFormat, BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType,
  PageBreak, TabStopType, TabStopPosition
} = require("docx");

const TEAL = "0E6E6E";
const TEALDK = "0A5252";
const AMBER = "B26A00";
const INK = "1A1A1A";

// ---------- helpers ----------
function H1(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text })] });
}
function H2(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text })] });
}
function H3(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text })] });
}
function P(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 140, line: 276 },
    children: [new TextRun({ text, ...opts })]
  });
}
// paragraph from runs (for mixed bold)
function PR(runs, opts = {}) {
  return new Paragraph({ spacing: { after: 140, line: 276 }, children: runs, ...opts });
}
function lead(label, body) {
  return new Paragraph({
    spacing: { after: 120, line: 276 },
    children: [
      new TextRun({ text: label + " ", bold: true, color: TEALDK }),
      new TextRun({ text: body })
    ]
  });
}
function bullet(text, level = 0) {
  return new Paragraph({
    numbering: { reference: "bullets", level },
    spacing: { after: 70, line: 268 },
    children: [new TextRun({ text })]
  });
}
function bulletLead(label, text, level = 0) {
  return new Paragraph({
    numbering: { reference: "bullets", level },
    spacing: { after: 70, line: 268 },
    children: [
      new TextRun({ text: label, bold: true }),
      new TextRun({ text: text })
    ]
  });
}
function num(text, level = 0) {
  return new Paragraph({
    numbering: { reference: "nums", level },
    spacing: { after: 70, line: 268 },
    children: [new TextRun({ text })]
  });
}
function rule() {
  return new Paragraph({
    spacing: { before: 60, after: 160 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: TEAL, space: 1 } },
    children: [new TextRun({ text: "" })]
  });
}
function spacer() { return new Paragraph({ children: [new TextRun({ text: "" })], spacing: { after: 60 } }); }

// callout-style block (single-cell shaded table)
function callout(title, lines) {
  const kids = [];
  if (title) kids.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: title, bold: true, color: AMBER })] }));
  lines.forEach((l, i) => kids.push(new Paragraph({ spacing: { after: i === lines.length - 1 ? 0 : 60, line: 268 }, children: [new TextRun({ text: l })] })));
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: 9360, type: WidthType.DXA },
      shading: { fill: "EFF6F6", type: ShadingType.CLEAR },
      borders: {
        top: { style: BorderStyle.SINGLE, size: 2, color: TEAL },
        bottom: { style: BorderStyle.SINGLE, size: 2, color: TEAL },
        left: { style: BorderStyle.SINGLE, size: 14, color: TEAL },
        right: { style: BorderStyle.SINGLE, size: 2, color: TEAL }
      },
      margins: { top: 120, bottom: 120, left: 160, right: 160 },
      children: kids
    })] })]
  });
}

// Q/A block for the "questions with transferable answers" section
function qa(q, a) {
  return [
    new Paragraph({ spacing: { before: 80, after: 40 }, children: [new TextRun({ text: "Q. ", bold: true, color: TEALDK }), new TextRun({ text: q, bold: true })] }),
    new Paragraph({ spacing: { after: 150, line: 276 }, children: [new TextRun({ text: "A. ", bold: true, color: AMBER }), new TextRun({ text: a })] })
  ];
}

// simple 2-col table
function twoColTable(header, rows, w1 = 3120, w2 = 6240) {
  const headerRow = new TableRow({ tableHeader: true, children: header.map((h, i) => new TableCell({
    width: { size: i === 0 ? w1 : w2, type: WidthType.DXA },
    shading: { fill: TEAL, type: ShadingType.CLEAR },
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [new Paragraph({ children: [new TextRun({ text: h, bold: true, color: "FFFFFF" })] })]
  })) });
  const bodyRows = rows.map((r, ri) => new TableRow({ children: r.map((c, i) => new TableCell({
    width: { size: i === 0 ? w1 : w2, type: WidthType.DXA },
    shading: { fill: ri % 2 ? "F2F7F7" : "FFFFFF", type: ShadingType.CLEAR },
    margins: { top: 70, bottom: 70, left: 120, right: 120 },
    children: [new Paragraph({ children: [new TextRun({ text: c, bold: i === 0 })] })]
  })) }));
  return new Table({
    width: { size: w1 + w2, type: WidthType.DXA },
    columnWidths: [w1, w2],
    borders: {
      top: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
      bottom: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
      left: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
      right: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" },
      insideVertical: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" }
    },
    rows: [headerRow, ...bodyRows]
  });
}

const children = [];
const C = (...x) => x.forEach(e => children.push(e));

// ===================== TITLE =====================
C(
  new Paragraph({ spacing: { before: 600, after: 60 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "STUDENT EDITION PLAYBOOK", bold: true, size: 52, color: TEAL })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
    children: [new TextRun({ text: "Transferable Lessons for Building Ron Blue Institute Student Curriculum", size: 26, color: INK })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [new TextRun({ text: "A reusable design system extracted from the God Owns It All Student Edition", italics: true, size: 22, color: "555555" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 240, after: 0 },
    border: { top: { style: BorderStyle.SINGLE, size: 8, color: AMBER, space: 4 } },
    children: [new TextRun({ text: "" })] }),
);

C(spacer(),
  callout("How to read this document", [
    "This is not a copy of God Owns It All. It is the operating manual for the next student edition: the decisions, structures, and corrections that should carry into Master Your Money, Generous Living, Splitting Heirs, or any future title.",
    "God Owns It All examples appear only to illustrate a universal principle. Anything specific to that book (its six themes, verses, titles, and wording) is treated as an example, never as a requirement.",
    "The final section is a ready-to-use Master Student Edition Prompt written for a different book, so a person who never touched this project can start the next one and inherit everything learned here."
  ])
);

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 0. ORIENTATION =====================
C(H1("The Shape of a Student Edition"));
C(P("Before the individual lessons, it helps to hold the whole shape in one frame. A Ron Blue Institute student edition is one track inside a church-wide campaign in which adults, students, and children move through the same themes in the same weeks. That simultaneity is the product. It is what turns six topics into a family conversation and a congregation-wide season rather than a class. Every design choice below serves that larger promise."));
C(P("Within the student track, three books do three different jobs, and a set of supporting assets wraps around them. Keeping the jobs distinct is the single structural idea that prevents the most common failures."));
C(twoColTable(["Component", "Job it does (and only this job)"], [
  ["Student Devotional", "The solo, daily, personal book. A student uses it alone every day. Holds the front matter, the daily readings, and the appendix tools."],
  ["Student Curriculum", "The in-room workbook for the weekly gathering. A student writes in it while the leader teaches. It does not read on its own and is not meant to."],
  ["Leader Guide", "The facilitator book. Holds leader front matter, the near-scripted weekly sessions, the icebreaker bank, facilitator coaching, and the parent assets."],
  ["Parent and family assets", "A per-session parent cue plus a weekly parent email series. Reaches the home, where durable change actually sticks."],
  ["Campaign assets", "Launch and promotion copy, sermon-series alignment, host and daily video. Church-wide, optional, and budget dependent."]
]));
C(spacer());

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 1. PROJECT ASSUMPTIONS =====================
C(H1("1. Project Assumptions"));
C(P("These are settled. A future student edition should inherit them rather than re-litigate them. Each one cost real iteration to reach on God Owns It All, and re-deciding them wastes the same time twice."));

C(H2("Architecture and scope"));
C(bulletLead("Three separate student books. ", "Student Devotional, Student Curriculum, and Leader Guide are distinct deliverables. Combining the devotional and curriculum into one student book is a legitimate alternative (fewer items to lose, cheaper to print), but separation was chosen for cleaner role boundaries. Decide this early in any new project because it drives the no-duplication rule below."));
C(bulletLead("Teaching lives once, reading lives once. ", "The full teaching lives in the Leader Guide. The full daily reading lives in the Devotional. The Curriculum is a do-not-read workbook the student completes live. The only thing intentionally printed in two places is the lightweight streak tracker. Printing the teaching three times is the default trap; the no-duplication rule is the fix."));
C(bulletLead("Whole-church, same-theme-same-week alignment. ", "The student edition is built to run in lockstep with the adult and children editions so families discuss the same theme on the same week. This is assumed, not optional."));
C(bulletLead("A six-part thematic arc, locked and sequenced. ", "A student edition organizes around a fixed sequence of themes, one per week, each building on the one before. The sequence is locked before content is written and is re-verified at the start of every new document. (For God Owns It All the order is Ownership, Contentment, Stewardship, Confidence, Generosity, Impact. The universal point is that the order is load-bearing and gets re-checked constantly.)"));

C(H2("Format and production standard"));
C(bulletLead("Lean daily format. ", "Daily readings run roughly 500 to 650 words total, with an opening story of about 150 to 225 words, a four-minute read, and a sixth to seventh grade reading floor. This beat the fuller multi-page spread because it is research-aligned, cheaper to print, and does not lose the youngest readers. Lock format before batching days."));
C(bulletLead("Near-scripted teaching. ", "Every weekly session is written so an untrained volunteer can deliver it cold. This is the production standard, not a nicety."));
C(bulletLead("Design to the least-resourced room. ", "Every mechanic must work for the church with too few volunteers, the student with no book, and the kid who did not do the reading. If a design only works in a fully-staffed room with prepared students, it is not finished."));
C(bulletLead("No em-dashes, anywhere, in any deliverable. ", "This is a hard formatting rule across all tracks. Alongside it: no self-answering discussion questions, no compound questions joined by dashes, no triplet sentence stacks, no overused parallel structure, no formulaic prayers, no self-help language."));

C(H2("Process"));
C(bulletLead("First piece of each, then batch. ", "Build one finished, approved example of every component (one day, one session, one workbook page, one parent email, one tool) before mass-producing volume. This surfaces template problems while they are cheap to fix."));
C(bulletLead("Audit before batching when a new spec arrives. ", "When an authoritative framework spec lands mid-project, stop and audit existing work against it before producing more. New volume built on an old spec becomes rework."));
C(bulletLead("Paste full reviewer comment sets into the working channel. ", "Relying on exported PDFs of reviewer comments missed comments that were live in the document. Get the complete comment set in text, not a partial export."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 2. CURRICULUM PHILOSOPHY =====================
C(H1("2. Curriculum Philosophy: Adapting Adult Content for Students"));
C(lead("Translate, do not simplify.", "The core conviction is that students are capable. The job is to render adult truth in language a motivated seventh grader can enter, without condescending to a high schooler. Simplifying strips the content; translating keeps the substance and changes the on-ramp."));
C(lead("Keep the truth, drop the mechanism that does not fit.", "Adult financial frameworks carry both a theological truth and a financial mechanism. Keep the truth. Drop the mechanism the audience cannot yet use. For teens this means keeping the heart of a tool while teen-adapting its inputs (for example, replacing an adult-only step with a parent or mentor a student trusts). For children it means dropping the mechanism almost entirely and keeping only the truth underneath, carried by story and object."));
C(lead("Floor and ceiling in every piece.", "Anchor the writing to a fourteen-year-old. Make the entry concrete enough that a twelve-year-old is in immediately, with enough underneath that a seventeen-year-old is not talked down to. This single principle resolves most age-range debates without splitting the edition."));
C(lead("Low-exposure entry.", "Let a student picture people their own age, or a scene, before anything is asked of them personally. Escalate to the word you only after the scene has done its work. Middle schoolers especially will disengage if the first move is personal exposure."));
C(lead("Story before principle.", "A story slips past defenses in a way a principle cannot. Let students feel something true before anyone tells them what to think. Every teaching and every day opens on a scene, not a thesis."));
C(lead("Prefer the author's real stories where they fit.", "Real stories from the source author land harder than invented scenarios and reinforce the church-wide campaign, because students hear the same stories the adults are hearing. Use real where it is age-appropriate, write fresh teen-centered narratives only where the real one does not fit, and keep the author as source rather than subject."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 3. DEVOTIONAL PHILOSOPHY =====================
C(H1("3. Devotional Philosophy"));
C(P("The devotional is not a stand-alone book that happens to sit next to a class. It is one half of a single experience whose other half is the weekly gathering. Each half feeds the other. The reading is where a student notices, feels, writes, and tries on their own. The gathering is where they bring that in and discover they were not the only one. Design the two as one loop."));

C(H2("A fixed daily shape"));
C(P("Every day uses the same shape so the student always knows what is coming. The specific element set that worked, with the reason each one exists:"));
C(bulletLead("Opening Story. ", "A scene the student has likely lived. Disarms before it teaches."));
C(bulletLead("Today's Scripture. ", "Two short passages, one that states the day's point and one that shows it in action. Verses must genuinely fit the day, never sit thematically adjacent."));
C(bulletLead("Big Idea. ", "The whole day in one sentence. If they remember nothing else, this."));
C(bulletLead("Picture This. ", "One image they can see in their head, so the idea outlives the page."));
C(bulletLead("Real Talk. ", "One honest paragraph that names the hard part, where this is actually difficult or bumps into how everyone around them lives."));
C(bulletLead("Try This Today. ", "One small action doable before bed. Not a life change."));
C(bulletLead("Write It Down. ", "A question with space to answer, which forces a real opinion instead of a skim."));
C(bulletLead("Talk About It. ", "One question the student carries into the weekly gathering."));
C(bulletLead("Ask Someone. ", "One question to ask a parent, sibling, friend, or leader. Faith grows when it leaves the student's own head."));
C(bulletLead("Prayer and one-line reminder. ", "A short prayer to close and one repeatable line to carry into tomorrow."));

C(H2("Wiring the solo piece into the social piece"));
C(P("Every daily reading carries one question to bring to group and one to ask a friend or sibling. That is the wire that makes the solo reading the fuel for the room. Without it, the two halves drift apart and the gathering ends up depending on whether anyone did the homework, which it must never do."));

C(H2("The streak, framed honestly"));
C(P("A simple checkbox streak works, but the framing matters more than the boxes. Name out loud that most people want to quit around day four, and call that the exact moment forming begins rather than a sign of failure. Aim for did not quit, not for perfect. A streak with gaps the student came back from beats a streak never started."));

C(H2("When the reader cannot read alone"));
C(P("For children the solo daily model breaks, because the youngest cannot read independently. The daily piece becomes a parent-led family moment of three to five minutes (one truth, one question, one small activity, one prayer), and the rhythm flips from one new idea per day to one big idea per week, repeated with a verse, a song, and a motion. For young children, repetition is the method, not a weakness of it. This is also where the campaign's family-alignment promise actually pays off."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 4. STUDENT ENGAGEMENT =====================
C(H1("4. Student Engagement"));
C(P("These mechanics are reusable across any title. They were tuned to solve real room problems: too few volunteers, students who did not prepare, quiet kids, and the awkwardness of being put on the spot."));

C(H2("Pair-up discussions"));
C(bulletLead("Stand-up, three minutes, after the icebreaker and before the teaching. ", "Standing slows the room down and warms it up. It is the on-ramp into the message, not a separate segment."));
C(bulletLead("Three prompts, not five. ", "Use one thing you noticed, one thing that felt real, one thing you tried. Hold the deeper one person you could ask prompt for the take-home, because it does not work mid-room."));
C(bulletLead("Rotate partners weekly. ", "Do not lock pairs for the whole series; rotation avoids the stuck-with-the-wrong-person problem."));
C(bulletLead("Build the low bar in. ", "A student who did nothing all week can still answer one thing you remember from last week, so no one is excluded."));

C(H2("Small groups"));
C(P("Run discussion as concentric circles that flex by staffing: pairs, then self-directed circles of three or four, then a large-group share. The circles can be student-led with no adult facilitator required, as long as one adult keeps the whole room on track. This is the direct fix for a volunteer shortage. Bigger ministries scale up to facilitated breakouts; small ones still work."));

C(H2("Large groups"));
C(P("Invite a few students to report one good thing my partner or circle said, and add a quick compliment or affirm beat after each share. Reporting someone else's line rather than your own lowers exposure, rewards listening, and pulls the quieter students' best contributions into the room."));

C(H2("Weekly challenges"));
C(bulletLead("A tiered action menu, three levels. ", "Start it (a sixty-second version anyone can do), Stretch it (a real step, often phone-in-hand or with a sibling), and Go all in (the committed version). Avoid crawl, walk, run; it reads babyish to a teenager."));
C(bulletLead("Self-select, do not assign. ", "Say it plainly: nobody does all three, everybody does one. Trying, even awkwardly, even when it flops, is how the idea gets in."));

C(H2("Real-world application"));
C(P("Tie every action to that week's big idea, keep it physical and doable before bed, and allow phone-in-hand steps because that is where students actually live. The point of the action is not to complete a task; it is to move the truth from the page into a single lived moment."));

C(H2("Participation"));
C(bulletLead("Open with answerable-without-self-exposure questions. ", "Start with where do people your age feel the most pressure, then escalate toward the personal once the room is warm."));
C(bulletLead("Have safe formats ready when the room goes quiet. ", "Thumbs up or down, draw your answer, or tell the person next to you all lower the cost of participating."));
C(bulletLead("Give a disengaged student a job. ", "Holding a card, making a sound effect, or leading the verse motion converts restlessness into contribution rather than fighting it."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 5. FRONT MATTER =====================
C(H1("5. Front Matter Requirements"));
C(P("Front matter is the most self-contained piece of a student edition and a good place to start a new project, because it sets the tone for everything and depends on almost nothing. Two distinct front matters exist: one in the Student Devotional and one in the Leader Guide."));

C(H2("Student Devotional front matter"));
C(bulletLead("Why this many days. ", "A short section grounding the length both biblically and developmentally: the difference between a forming number and an informing number, and between a transaction (read it, nod, forget it) and a transformation (a hundred small repeated choices). Include the community dimension, that the whole group moves through it together."));
C(bulletLead("How this study works. ", "Walk the student through every daily element in order and explain why each is there. This is also where you teach the student that the daily reading and the weekly gathering are one experience."));
C(bulletLead("The sessions map. ", "List the weeks, the day ranges, and the one question each week is really asking. State plainly that the order is intentional and builds."));
C(bulletLead("Take one next step. ", "A short, low-pressure nudge: commit, find one friend doing it too, show up, check the box."));
C(bulletLead("The streak tracker. ", "Checkboxes by week, with the honest you will want to quit framing."));

C(H2("Leader Guide front matter"));
C(bulletLead("How to use this guide. ", "The run-of-show, the any-size-room model, and how the three books relate."));
C(bulletLead("Recruiting volunteers. ", "How to pull in adult helpers, including specifically recruiting a finance person (a CPA, accountant, or anyone who works with numbers) as a guest for the relevant week."));
C(bulletLead("Heart of the pastors. ", "A fill-in page for the senior pastor's hopes for the series and the youth pastor's hopes for the students, so the why comes from the top."));
C(bulletLead("Group covenant. ", "A short room-culture agreement (listen well, do not mock, do not gossip), printable, with an option for the group to add one rule of their own in week one."));
C(bulletLead("Pre-launch checklist. ", "The concrete steps and timeline a leader needs before week one."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 6. SESSION STRUCTURE =====================
C(H1("6. Session Structure"));
C(P("Every weekly session inherits one standard eight-segment run-of-show. A single template that all six sessions copy keeps the room predictable, lets a volunteer run any week cold, and makes batching the remaining sessions fast once the first is approved."));

C(H2("The eight segments"));
C(num("Arrival and Icebreaker (5 to 10 min). A themed opener that works as the room fills."));
C(num("Stand-Up Pair-Up (3 min). The devotional check-in and on-ramp, with the rotate-weekly and low-bar rules above."));
C(num("Recap (2 to 3 min). A three to four sentence summary of the week's readings. This is the safety net that makes the session work even for a student who read nothing, has no book, or missed every day."));
C(num("Teaching (15 to 20 min, near-scripted). A volunteer can deliver it cold. It opens with a story, not a thesis. Two things ride along the bottom of every teaching page (see below)."));
C(num("Breakout Discussion (15 to 30 min). Concentric circles that flex by staffing."));
C(num("Try Something (pick one). The three-level action menu."));
C(num("Bring It to Group and Take It Home (3 min). A boxed prompt with write-in lines: one question to bring back, one to ask a friend or sibling. This is where one person you could ask lives."));
C(num("Closing Prayer and Streak Reminder (3 to 5 min). Close, then point them back to today's box."));

C(H2("Two things that ride along every teaching page"));
C(bulletLead("An alternate-metaphor menu. ", "Two or three swappable images for the same idea, so a leader can choose the one that fits their room instead of being stuck with the printed one. (God Owns It All used the horizon, the treadmill, and the leaky bucket for the same contentment point.)"));
C(bulletLead("Age-flex notes. ", "A for-younger note (more concrete, more humor, belonging-framed) and a for-older note (more nuance, more gray area, identity-framed) so one script serves the whole room."));

C(H2("A fixed slot for the leader's own story"));
C(P("Every session reserves a structural slot for the leader's personal money story. It is not optional decoration; a teaching about money lands differently when the person in the room has named their own. Build the slot into the template so it is never skipped."));

C(H2("Timing flex"));
C(P("Publish a timing table that shows the same eight segments at 45, 60, and 90 minutes. The breakout segment absorbs most of the flex. This lets one template serve a short midweek slot and a long retreat session without redesign."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 7. LEADER GUIDE =====================
C(H1("7. Leader Guide Requirements"));
C(P("The Leader Guide is the operational heart of the edition. It should contain everything a volunteer needs and assume the volunteer is busy, untrained, and walking in cold."));
C(bulletLead("Leader front matter. ", "As listed in section 5: how to use, recruiting (including a finance guest), heart of the pastors, group covenant, pre-launch checklist."));
C(bulletLead("Six near-scripted sessions. ", "Built on the one standard template, each opening with a story, each carrying the alternate-metaphor menu and age-flex notes."));
C(bulletLead("An icebreaker bank. ", "More openers than weeks, assigned loosely to sessions so a leader can swap by room. (God Owns It All carried thirty concepts across multiple titles.)"));
C(bulletLead("Per-session breakout-facilitator notes. ", "Each session's discussion questions plus a coaching layer: what to listen for, what to do if the room is silent, and what a breakthrough sounds like. Write these assuming a first-time volunteer and the four problems rooms actually hit (dead silence, one student dominating, oversharing, going off-topic)."));
C(bulletLead("A zero-prep check-in card. ", "The floor option a volunteer can run with no preparation at all, carrying all five check-in prompts with a note on which three to use when time is short."));
C(bulletLead("Visual reinforcement guidance. ", "Where the teaching has named points or a named tool, instruct that the points appear on screen as they are spoken and that a tool is shown and highlighted piece by piece as it is explained. Reviewers asked for this repeatedly on the filmed sessions; it applies equally to room slides."));
C(bulletLead("Volunteer training (church-specific). ", "Onboarding that ties the covenant, the check-in card, the facilitator notes, and the session flow together. Critical caution: never invent a church's safety policies. Background checks, two-adult rules, and mandatory-reporting requirements vary by state and denomination. Leave clearly marked placeholders for the church to complete."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 8. PARENT GUIDE =====================
C(H1("8. Parent Guide Requirements"));
C(P("Parent engagement is treated as central to durable change, not as a courtesy. The home is where a six-week series either takes root or evaporates. Two distinct parent deliverables emerged, and both should carry forward."));

C(H2("Per-session parent guide"));
C(bulletLead("What the student is learning, plainly. ", "One short paragraph naming the week's theme."));
C(bulletLead("Why it matters to the parent too. ", "Name that this is not only a teen problem; the parent feels it as well. This invites the parent in rather than positioning them as enforcer."));
C(bulletLead("One conversation, never homework. ", "A single question a parent can drop into a car ride, a dinner, or a bedtime. One, not a worksheet."));
C(bulletLead("Permission to be confessional. ", "Encourage parents to be honest about their own money struggles and to make it a whole-family conversation. Modeled honesty teaches more than instruction."));

C(H2("Weekly parent email series"));
C(P("A standing email series is a separate, easily-forgotten, and genuinely expected component. It is how most churches actually reach parents. It consists of a kickoff sent a few days before launch, then one email the day before or morning of each session."));
C(bulletLead("A fixed three-part shape. ", "What they are learning, why it matters, and one conversation to have. Nothing more."));
C(bulletLead("Short on purpose. ", "Busy parents skim. Length kills the email."));
C(bulletLead("Customizable fields in brackets. ", "Church name, leader name, meeting day, and links, so a church can personalize in minutes."));
C(bulletLead("Write the emails after the tools exist. ", "An email can say ask your student about their finish line or the habits they learned only once those tools are built, so the email series is naturally the last thing batched."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 9. MS vs HS =====================
C(H1("9. Middle School Versus High School"));
C(P("The central adaptation finding: for the youth band, one edition with age-flex leader notes beats two separate editions. The developmental gap from roughly eleven to eighteen is narrow enough that a single floor-and-ceiling text plus per-segment flex notes serves the whole room. Splitting into two youth books doubles the work for a gap the writing can already bridge."));
C(twoColTable(["Lean younger", "Lean older"], [
  ["Concrete objects and physical scenes", "Abstract and identity-level framing"],
  ["More humor; belonging-framed", "More nuance and gray area; identity-framed"],
  ["The thing they begged for and forgot", "The future, college, body image, am-I-enough"],
  ["Bottom line kept simple", "Can hold an idea like enough is a decision, not a destination"]
]));
C(spacer());
C(lead("Spread the hooks deliberately.", "Some openers land instantly for the younger end (physical, concrete) and some for the older end (future-dread, comparison, legacy). That spread is intentional, not a flaw. The leader note is where a volunteer flexes a lopsided opener live for their actual room."));
C(lead("Children are a different question entirely.", "The gap from five to eleven is wider than eleven to eighteen, so for the children edition a true split (early or preschool versus older elementary) is a real decision rather than a flex-note problem. Do not assume the youth approach transfers; children are not easier teens."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 10. AUTHOR PRESERVATION =====================
C(H1("10. Author Preservation"));
C(P("A student edition adapts a specific author's framework, theology, voice, and progression. Preserving the source faithfully while translating it for students is the line reviewers watch most closely. The following held true across the project and will hold for any title."));
C(bulletLead("Author as source, not subject. ", "Weave the author's quotes and stories in as teaching material. Do not turn the curriculum into a biography of the author, and avoid leaning on repeated the author says framing. The narration is pastoral and direct; the author's material is the evidence, not the topic."));
C(bulletLead("Name the framework tools exactly. ", "Tool names and their composition are non-negotiable with reviewers. If a tool has five parts, it has five, not four. If it has a specific name, use that name, not a paraphrase. Reviewers flag this every time."));
C(bulletLead("Keep tools congruent across every component. ", "A tool must be named and depicted the same way in the devotional, the workbook, the leader script, and the appendix. Reviewers explicitly asked that auxiliary tools be congruent with all the other tools in all the sessions. Build each tool once and reference the single version everywhere."));
C(bulletLead("Scripture must genuinely fit. ", "The dominant reviewer concern across the project was verses that are thematically adjacent but not directly on point. Every verse must earn its place for the specific day or session, with no stretch references. One passage states the truth, one shows it in action, and both are actually about that truth."));
C(bulletLead("Preserve the theological progression and its order. ", "Keep the six-theme arc and its sequence intact, because each theme depends on the one before it. A student cannot honestly answer how much should I give before settling who owns it. Reordering breaks the logic, not just the labels."));
C(bulletLead("Translate the truth, retire the mechanism that does not fit. ", "Keep what is theologically load-bearing. Drop the adult financial machinery a student or child cannot use, and replace teen-inappropriate inputs with age-appropriate ones."));
C(bulletLead("Reconcile source language with curriculum labels. ", "Filmed or written source material may use a word (for example, legacy) that differs from the curriculum's chosen theme label (for example, impact). Reconcile these so the campaign reads as one coherent thing across video, print, and room."));
C(bulletLead("Diversify testimony and explain affiliations plainly. ", "Reviewers flagged over-reliance on a single testimony source and a single advisor channel as a credibility risk. Vary whose stories appear, and where an institutional affiliation matters, explain it in plain language rather than letting it read as a sales channel."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 11. QUESTIONS WITH ANSWERS =====================
C(H1("11. Questions We Asked That Now Have Transferable Answers"));
C(P("Each of these came up during development and now has a settled, reusable answer. Phrased so the answer applies beyond the original book."));
qa("How long should a student daily reading be?",
  "Lean. Roughly 500 to 650 words total, an opening story of 150 to 225 words, a four-minute read, at a sixth to seventh grade floor. Adult-length prose loses the youngest readers and pushes past the attention window. Same total footprint people imagine, rebalanced toward story and action and away from a long block of text.").forEach(e => C(e));
qa("One combined student book, or separate devotional and curriculum?",
  "Either is defensible; decide early because it drives the no-duplication architecture. Combined means one book to carry, fewer to lose, cheaper to print, good for younger students. Separate means cleaner role boundaries. Whichever is chosen, the teaching still lives once and the reading lives once.").forEach(e => C(e));
qa("What if a student does not have the curriculum or did not do the reading?",
  "Presume everyone has at least a digital copy as the universal backstop, and build a tight recap into every session so the gathering never depends on the reading. Do not reprint the devotional inside the curriculum; the only thing that lives in both places is the lightweight tracker.").forEach(e => C(e));
qa("How should the weekly check-in be run?",
  "A three-minute stand-up pair-up right after the icebreaker and before the teaching, using three of the five prompts, with partners rotated weekly and a low-bar option so a student who did nothing can still take part.").forEach(e => C(e));
qa("What is the difference between a hook and a story, and which does a session need?",
  "Both, in different slots. A hook is a relatable you scenario that says this is about your life; it works as the icebreaker. A story is an actual narrative with a character and an arc that shows the truth happening before you teach it; it opens the teaching. Open the teaching with a story and keep the hook as the room opener.").forEach(e => C(e));
qa("What labels should the tiered action menu use?",
  "Start it, Stretch it, Go all in. Avoid crawl, walk, run, which reads babyish to a teenager.").forEach(e => C(e));
qa("How do you handle the daily piece for children who cannot read alone?",
  "Convert it from a solo daily streak into a parent-led family touchpoint of three to five minutes, and flip the rhythm to one big idea per week repeated with a verse, a song, and a motion. Repetition is the method at that age.").forEach(e => C(e));
qa("When the structure is 6 by 7 (42) but the brand is 40, what wins?",
  "Decide the branding-versus-count tension up front rather than letting it drift. Options that worked as live choices: brand it a six-week journey, keep 40 days loosely as the name, or cut to a literal 40. The point is to reconcile it before writing day-level content.").forEach(e => C(e));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 12. OPEN / PROJECT-SPECIFIC =====================
C(H1("12. Questions That Are Still Open or Project-Specific"));
C(P("These should be reconsidered for every new book, because the right answer depends on the source material, the audience, the format, or the church's strategy. Do not inherit the God Owns It All answer; re-decide."));
C(bulletLead("Age band and split. ", "One youth edition with flex notes is settled for youth, but the children band (one K to 5 edition versus a preschool or early split) is a real per-project decision driven by the ministry."));
C(bulletLead("Primary delivery setting. ", "Sunday school, midweek, or family-at-home changes which of the three books leads and how the daily piece is framed."));
C(bulletLead("Day count and branding. ", "Forty versus forty-two versus a six-week frame depends on the outline and the campaign name."));
C(bulletLead("Specific verses and titles. ", "Every verse and title is source-material and reviewer dependent. Re-derive them from the new book's themes; do not port them."));
C(bulletLead("Which author stories are age-appropriate. ", "Depends entirely on the new book's stories. Some adult anecdotes translate to teens, some do not."));
C(bulletLead("Which framework tools translate, and which get dropped. ", "Each book has its own toolset. Decide per tool whether to teen-adapt it, simplify it, or retire it."));
C(bulletLead("Video scope. ", "Host segments and daily inspiration videos are a large, separate body of work that is church and budget dependent. Decide whether the student edition mirrors the adult edition's daily-video pattern early, because it can imply dozens of scripts."));
C(bulletLead("Volunteer training specifics and safety policy. ", "Format (live meeting, self-paced, or video) and the church's required policies must come from the church. Never invent them."));
C(bulletLead("Combined versus separate student books. ", "Re-confirm with the team for each title."));
C(bulletLead("Campaign and sermon alignment. ", "The launch kit and the tie between weekend messages and the six themes depend on each church's strategy."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 13. COMMON MISTAKES =====================
C(H1("13. Common Mistakes to Avoid"));
C(P("Each of these actually happened, was caught, or was a near-miss on this project. They are the cheapest lessons to inherit."));
C(bulletLead("Session-order drift. ", "This is the single biggest recurring error. The theme order was confused repeatedly, in the curriculum (Contentment and Stewardship swapped more than once) and independently in the filmed videos (sessions labeled out of order). Lock the macro-sequence, propagate it to every document and asset, and re-verify it at the start of every new file. Treat order as load-bearing."));
C(bulletLead("Batching before locking the format. ", "A fuller multi-page spread was drafted before the lean format was settled, which created rework. Lock the daily format and the session template before producing volume."));
C(bulletLead("Producing volume before the first piece of each is approved. ", "Mass-producing on an unapproved template multiplies a hidden flaw across forty days. Build one of everything first."));
C(bulletLead("Triple-teaching the same content. ", "Writing the full teaching into the devotional, the curriculum, and the leader guide gives the student the same lesson three times and inflates print cost. Decide what lives where once."));
C(bulletLead("Treating children as easier teens. ", "Children think concretely and the youngest cannot read alone, which breaks the solo-daily model outright. Redesign for them; do not scale the youth book down."));
C(bulletLead("Inventing church safety policy. ", "Background checks, two-adult rules, and mandatory reporting vary by state and denomination. Use marked placeholders, never invented rules."));
C(bulletLead("Over-relying on one testimony source. ", "Concentrating stories in a single advisor or channel reads as a sales pitch and was flagged. Diversify voices and explain affiliations plainly."));
C(bulletLead("Stretch scripture. ", "Verses that are merely adjacent to the theme get flagged every time. Choose verses that are actually about the day's truth."));
C(bulletLead("Paraphrasing or miscounting framework tools. ", "Changing a tool's name or its number of parts breaks reviewer trust. Reproduce tools exactly and keep them congruent everywhere."));
C(bulletLead("Letting source language and curriculum labels drift. ", "When the video says one word and the workbook says another, the campaign stops reading as one thing. Reconcile them."));
C(bulletLead("Forgetting the parent email series. ", "It is a standard, expected component that is easy to leave off the build list. Put it on the map from day one, even though it is built last."));
C(bulletLead("Designing only for the ideal room. ", "A mechanic that needs full staffing and prepared students is unfinished. Build the floor first: empty-handed student, no-prep volunteer, too few leaders."));
C(bulletLead("Trusting partial reviewer exports. ", "A PDF export of comments missed comments that were live in the document. Work from the complete comment set."));
C(bulletLead("Style slips. ", "Em-dashes, self-answering questions, compound dash-joined questions, triplet sentence stacks, overused parallel structure, formulaic prayers, and self-help language all violate the standing rules. Check every deliverable against them."));

C(new Paragraph({ children: [new PageBreak()] }));

// ===================== 14. MASTER PROMPT =====================
C(H1("14. Master Student Edition Prompt"));
C(P("What follows is a ready-to-use prompt for starting a new Student Edition from scratch. It carries every transferable lesson above. Replace the bracketed variables with the new title's specifics. A worked example for Master Your Money is shown after the template so the prompt reads concretely for a book that is not God Owns It All."));

C(rule());
C(H2("The prompt (copy from here)"));

C(P("You are a curriculum developer and project lead building the Student Edition of [BOOK TITLE] by [AUTHOR], produced for the Ron Blue Institute. This is one track of a church-wide campaign in which adults, students, and children move through the same themes in the same weeks, so families discuss the same idea on the same week. Treat that family-level simultaneity as the point of the whole project.", { }));

C(H3("What you are building"));
C(bulletLead("Three separate student books: ", "a Student Devotional (solo and daily), a Student Curriculum (the in-room workbook for the weekly gathering), and a Leader Guide (the facilitator book). Confirm with me whether the devotional and curriculum should instead be combined into one student book before you begin."));
C(bulletLead("Parent assets: ", "a per-session parent guide and a weekly parent email series (a kickoff plus one email per week)."));
C(bulletLead("Appendix tools: ", "teen-adapted versions of [AUTHOR]'s framework tools, named exactly and kept congruent across every book."));

C(H3("Non-negotiable rules"));
C(bulletLead("No em-dashes anywhere. ", "Also no self-answering discussion questions, no compound questions joined by dashes, no triplet sentence stacks, no overused parallel structure, no formulaic prayers, no self-help language."));
C(bulletLead("Lock the theme sequence first and re-verify it at the start of every document. ", "The order is [LIST THE LOCKED SEQUENCE], one theme per week, each building on the one before. Order drift is the most common failure on these projects; treat the sequence as load-bearing."));
C(bulletLead("Name [AUTHOR]'s framework tools exactly, with exact composition. ", "Never paraphrase a tool name or miscount its parts. Build each tool once and reference that single version everywhere."));
C(bulletLead("Every verse must genuinely fit its day or session. ", "No thematically adjacent stretch references. Use one passage that states the truth and one that shows it in action, both actually about that truth."));
C(bulletLead("Keep [AUTHOR] as source, not subject. ", "Weave quotes and stories in as teaching material; do not write biography or lean on repeated the author says framing."));

C(H3("Curriculum philosophy"));
C(bulletLead("Translate, do not simplify. ", "Treat students as capable. Anchor to a fourteen-year-old: concrete enough for a twelve-year-old to enter, with enough underneath that a seventeen-year-old is not talked down to."));
C(bulletLead("Story before principle, and low-exposure entry. ", "Open on a scene a student has lived. Let them picture people their age before asking anything personal; escalate to you only after the scene works."));
C(bulletLead("Keep the truth, drop the mechanism that does not fit. ", "Teen-adapt tool inputs (replace adult-only steps with a trusted parent or mentor). Retire machinery the audience cannot yet use."));
C(bulletLead("Prefer real stories where they fit. ", "Use [AUTHOR]'s real, teen-appropriate stories first, because they land harder and reinforce the campaign; write original teen narratives only where a real one does not fit."));

C(H3("The daily devotional"));
C(bulletLead("Lean format. ", "About 500 to 650 words total, an opening story of 150 to 225 words, a four-minute read, sixth to seventh grade floor."));
C(bulletLead("A fixed daily shape: ", "Opening Story; two Scriptures (one states, one shows); Big Idea in one sentence; Picture This (one image); Real Talk (names the hard part); Try This Today (one small action); Write It Down; Talk About It (carried to group); Ask Someone; short prayer and a one-line reminder."));
C(bulletLead("Wire solo to social. ", "Every day carries one question to bring to the gathering and one to ask a friend or sibling."));
C(bulletLead("Streak, framed honestly. ", "Name that most people want to quit early and that this is when forming begins; aim for did not quit, not perfect."));

C(H3("The weekly session (one template all sessions copy)"));
C(P("Build one standard eight-segment run-of-show, near-scripted so an untrained volunteer can run any week cold:"));
C(num("Arrival and Icebreaker (5 to 10 min)."));
C(num("Stand-Up Pair-Up (3 min): rotate partners weekly; use one thing you noticed, one that felt real, one you tried; low bar of one thing you remember from last week."));
C(num("Recap (2 to 3 min): a three to four sentence summary so the session works even if a student read nothing."));
C(num("Teaching (15 to 20 min): opens with a story; carries an alternate-metaphor menu and for-younger and for-older age-flex notes along the bottom; reserves a fixed slot for the leader's own money story."));
C(num("Breakout Discussion (15 to 30 min): concentric circles (pairs, then student-led circles of three or four, then a large-group share of one good thing my partner said, with a compliment beat)."));
C(num("Try Something: a three-level action menu labeled Start it, Stretch it, Go all in."));
C(num("Bring It to Group and Take It Home (3 min): write-in lines for one question to bring back and one to ask a friend or sibling."));
C(num("Closing Prayer and Streak Reminder (3 to 5 min)."));
C(P("Provide a timing table for the same eight segments at 45, 60, and 90 minutes, with the breakout segment absorbing most of the flex."));

C(H3("The Leader Guide also contains"));
C(bulletLead("Front matter: ", "how to use, recruiting volunteers (including a finance guest for the relevant week), a Heart of the Pastors fill-in page, a group covenant, and a pre-launch checklist."));
C(bulletLead("Per-session facilitator notes: ", "the questions plus what to listen for, what to do if the room is silent, and what a breakthrough sounds like, written for a first-time volunteer."));
C(bulletLead("A zero-prep check-in card ", "and an icebreaker bank with more openers than weeks."));
C(bulletLead("Visual reinforcement guidance: ", "named teaching points appear on screen as spoken; named tools are shown and highlighted piece by piece."));
C(bulletLead("Volunteer training with marked placeholders for the church's safety policies. ", "Never invent background-check, two-adult, or mandatory-reporting rules."));

C(H3("Parent assets"));
C(bulletLead("Per-session parent guide: ", "what the student is learning, why it matters to the parent too, and one conversation for a car ride, dinner, or bedtime. Never homework. Encourage parents to be honest about their own money struggles."));
C(bulletLead("Weekly email series: ", "a kickoff a few days before launch plus one short email per week, each with what they are learning, why it matters, and one conversation. Use bracketed customizable fields. Write these last, after the tools exist, so they can reference them."));

C(H3("Audience adaptation"));
C(bulletLead("One youth edition with age-flex notes ", "rather than separate middle and high school books; the gap is narrow enough for floor-and-ceiling writing plus per-segment flex notes."));
C(bulletLead("If a children edition is in scope, ", "redesign rather than scale down: parent-led family moments instead of solo reading, one big idea per week repeated with verse, song, and motion, and a real decision about splitting early elementary from older elementary."));

C(H3("Process and the decisions I owe you"));
C(bulletLead("Build the first piece of each component before batching volume, ", "and start with front matter because it is self-contained and sets the tone."));
C(bulletLead("Audit existing work against any new authoritative spec before producing more."));
C(bulletLead("Before writing day-level content, get my decisions on: ", "the locked theme sequence; day count and branding (40, 42, or six weeks); combined versus separate student books; primary delivery setting; age band and any children split; video scope; and which framework tools translate, teen-adapt, or retire. Ask me for these as a short decision list."));
C(bulletLead("Confirm verse and title selections with the theological reviewer, ", "expecting the dominant note to be that any merely-adjacent verse must be replaced with one that is actually on point."));

C(rule());
C(H2("Worked example: filling the variables for Master Your Money"));
C(P("This shows how the bracketed variables resolve for a real, different title. It is illustrative; confirm each with the team and reviewers before building."));
C(twoColTable(["Variable", "Example value for Master Your Money"], [
  ["[BOOK TITLE]", "Master Your Money"],
  ["[AUTHOR]", "Ron Blue"],
  ["[LIST THE LOCKED SEQUENCE]", "Derive from the book's own structure and confirm with the reviewer before any content is written; re-verify the order at the top of every document."],
  ["Framework tools to teen-adapt", "The book's planning and money-management tools, named exactly and kept congruent across all three books; teen-adapt any adult-only inputs (for example, replace a spouse-agreement step with a trusted parent or mentor)."],
  ["Day count and branding", "Open decision: 40, 42, or a six-week frame, reconciled before day-level writing."],
  ["Children edition in scope?", "Open decision: confirm whether this title ships a children track and, if so, the age split."]
]));
C(spacer());
C(P("With the variables resolved, the same prompt produces the next Student Edition while inheriting the lean daily format, the eight-segment session, the concentric-circles discussion, the tiered action menu, the parent email series, the author-preservation rules, and the order-verification discipline that this project paid to learn.", { italics: true }));

// ===================== build =====================
const doc = new Document({
  creator: "Student Edition Playbook",
  title: "Student Edition Playbook",
  styles: {
    default: { document: { run: { font: "Arial", size: 21, color: INK } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: "Arial", color: TEAL },
        paragraph: { spacing: { before: 200, after: 160 }, outlineLevel: 0,
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: AMBER, space: 4 } } } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: TEALDK },
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 21, bold: true, font: "Arial", color: AMBER },
        paragraph: { spacing: { before: 140, after: 70 }, outlineLevel: 2 } },
    ]
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [
        { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 540, hanging: 280 } } } },
        { level: 1, format: LevelFormat.BULLET, text: "\u25E6", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1080, hanging: 280 } } } } ] },
      { reference: "nums", levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 540, hanging: 320 } } } } ] },
    ]
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("/home/claude/Student_Edition_Playbook.docx", buf);
  console.log("written", buf.length, "bytes");
});
