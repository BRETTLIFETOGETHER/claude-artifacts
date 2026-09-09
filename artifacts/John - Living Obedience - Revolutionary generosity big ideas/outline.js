const fs = require('fs');
const d = require('docx');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, PageBreak, PageOrientation
} = d;

const C = JSON.parse(fs.readFileSync('/home/claude/rg/content.json', 'utf8'));

const NAVY = "1B2A4A";
const GOLD = "8A6D2F";
const GREY = "555555";

const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE };

function p(text, opts = {}) {
  return new Paragraph({
    alignment: opts.align,
    spacing: { before: opts.before ?? 0, after: opts.after ?? 140, line: opts.line ?? 280 },
    indent: opts.indent,
    border: opts.border,
    children: [new TextRun({
      text: text,
      font: opts.font || "Calibri",
      size: opts.size || 21,
      bold: opts.bold || false,
      italics: opts.italics || false,
      color: opts.color || "222222",
      allCaps: opts.caps || false,
      characterSpacing: opts.track || 0
    })]
  });
}

function runsPara(runs, opts = {}) {
  return new Paragraph({
    alignment: opts.align,
    spacing: { before: opts.before ?? 0, after: opts.after ?? 100, line: opts.line ?? 280 },
    children: runs
  });
}

function label(text) {
  return p(text, { caps: true, size: 15, bold: true, color: GOLD, track: 24, after: 40, before: 160 });
}

function h(text, level, opts = {}) {
  return new Paragraph({
    heading: level,
    spacing: { before: opts.before ?? 320, after: opts.after ?? 120 },
    children: [new TextRun({
      text: text,
      font: "Cambria",
      size: opts.size || 30,
      bold: true,
      color: opts.color || NAVY
    })]
  });
}

function rule(before = 60, after = 160) {
  return new Paragraph({
    spacing: { before: before, after: after },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "C9C9C9" } },
    children: [new TextRun({ text: "", size: 2 })]
  });
}

function field(name, value) {
  return runsPara([
    new TextRun({ text: name + "  ", font: "Calibri", size: 18, bold: true, color: NAVY, allCaps: true, characterSpacing: 16 }),
    new TextRun({ text: value, font: "Calibri", size: 21, color: "222222" })
  ], { after: 90, line: 280 });
}

const children = [];

/* ---------- Title page ---------- */
children.push(new Paragraph({ spacing: { before: 2200, after: 0 }, children: [new TextRun({ text: "", size: 2 })] }));
children.push(p("A Book Concept", { align: AlignmentType.CENTER, caps: true, size: 17, bold: true, color: GOLD, track: 44, after: 200 }));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 160 },
  children: [new TextRun({ text: C.title, font: "Cambria", size: 62, bold: true, color: NAVY })]
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 420, line: 340 },
  children: [new TextRun({ text: C.subtitle, font: "Cambria", size: 26, italics: true, color: GREY })]
}));
children.push(p(C.authors, { align: AlignmentType.CENTER, size: 24, bold: true, color: "222222", after: 120 }));
children.push(p("The Signatry", { align: AlignmentType.CENTER, size: 20, color: GREY, after: 900 }));
children.push(rule(0, 120));
children.push(p(C.status, { align: AlignmentType.CENTER, size: 18, italics: true, color: GREY, after: 60 }));
children.push(p("Outline prepared by Brett Eastman, LifeTogether Ministries \u00b7 August 2026", { align: AlignmentType.CENTER, size: 18, color: GREY }));
children.push(new Paragraph({ children: [new PageBreak()] }));

/* ---------- The premise ---------- */
children.push(h("The Premise", HeadingLevel.HEADING_1, { before: 0 }));
children.push(p("The generosity movement has spent twenty-five years winning the argument about the heart. Generous Giving proved that a room without an ask produces honesty. National Christian Foundation proved that the asset, not the paycheck, is where the real giving lives. The Gathering proved that generous families do better work in each other's company. Ron Blue taught a generation that ownership is the root question. Randy Alcorn taught them that the treasure moves before the heart does. What the movement has never had is one book a family can hand to their adult children, or an advisor can hand to a client, that carries the conviction and the mechanics in the same hundred pages."));
children.push(p("That is the gap this book fills. It argues that revolutionary generosity is not a temperament or a tax strategy but three specific breaks with normal Christian giving: giving while you are alive to see it, giving from what you actually own rather than what happens to be liquid, and leaving your children a practice instead of a balance. Each of those is teachable. None of them requires more income. All three are ordinary decisions that most families never got around to making because nobody put them in one place."));
children.push(p("The authors are the two people in the movement positioned to write it without flinching. Steve French built and sold a company before he ever advised anyone on selling one, and now spends his days on the least understood corner of the field \u2014 stock, real estate, closely held business interests. Dale Armstrong has spent nearly three decades on the other side of the table, in the conversations where a family finally says out loud what it wants its money to do. One brings the mechanics, the other brings the thousand conversations. Neither has to speculate about what stops people."));

/* ---------- The reader ---------- */
children.push(h("The Reader", HeadingLevel.HEADING_1));
children.push(p("Four readers, in priority order. The manuscript should be able to name which one every chapter is serving.", { after: 160 }));

const readers = [
  ["The owner with an event coming", "A business owner, farmer, or executive within five years of a liquidity event who has never been told that sequence determines the size of the gift. He is the reader whose life the book can most concretely change, and the one who most often finds out too late."],
  ["The family with capacity and no practice", "A couple who give faithfully, hold more than they need, and have four adult children who have never once decided where real money went. They do not need to be convinced to be generous. They need a way to make it a household practice rather than a personal habit."],
  ["The advisor who has never asked", "The professional standing at the gate. He is not the buyer of the book, but he is the fastest channel to the first two readers, and he will only hand it on if it never sells anything."],
  ["The pastor with high-capacity families he is afraid to disciple", "He has families in the third row he has never discipled about money because every conversation he could imagine having sounds like an ask. This book is his permission and his script."]
];
readers.forEach(([t, b]) => {
  children.push(p(t, { bold: true, size: 22, color: NAVY, after: 50, before: 140 }));
  children.push(p(b, { after: 100 }));
});

/* ---------- Editorial rules ---------- */
children.push(h("The No-Ask Rule", HeadingLevel.HEADING_1));
children.push(p("A book by the CEO and Chief Revenue Officer of a donor advised fund sponsor carries an inherent credibility tax. Read uncharitably, it is a brochure. The defense is not a disclaimer; it is a set of editorial constraints borrowed from the movement's own best practice, and they should be treated as non-negotiable through the whole manuscript."));
const rules = [
  "No vehicle is sold in the body of the book. Donor advised funds, foundations, charitable trusts and the rest are described where the idea requires them and explained in the appendix, never recommended.",
  "No Signatry client is used as a case study without at least an equal number of stories sourced from outside the organization. The reader should not be able to guess the authors' employer from the stories alone.",
  "Every mechanism chapter ends on the reader's decision, not on a service that could make the decision easier.",
  "No superlatives about the authors' own institution. The one claim it may make about itself \u2014 that a fund should be measured by how fast money leaves \u2014 is made as a standard the whole industry should adopt, and the authors' own numbers are published alongside it.",
  "Endorsements are sought from peers who compete with The Signatry for the same families. If they will not endorse it, the book is not yet a movement book."
];
rules.forEach((r, i) => {
  children.push(runsPara([
    new TextRun({ text: String(i + 1) + ".  ", font: "Cambria", size: 21, bold: true, color: GOLD }),
    new TextRun({ text: r, font: "Calibri", size: 21, color: "222222" })
  ], { after: 110, line: 280 }));
});

children.push(new Paragraph({ children: [new PageBreak()] }));

/* ---------- Structure at a glance ---------- */
children.push(h("The Structure at a Glance", HeadingLevel.HEADING_1, { before: 0 }));
children.push(p("Five parts, four chapters each. The arc runs from conviction to capacity to household to community to purpose, and closes on joy. Twenty chapters, roughly 65,000 words.", { after: 200 }));

const TW = 9360;
const COLS = [860, 5100, 3400];

function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.w, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: "DDDDDD" },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: "DDDDDD" },
      left: NONE, right: NONE
    },
    shading: opts.shade ? { type: ShadingType.CLEAR, fill: opts.shade, color: "auto" } : undefined,
    margins: { top: 90, bottom: 90, left: 90, right: 90 },
    children: [new Paragraph({
      spacing: { after: 0, line: 260 },
      children: [new TextRun({
        text: text,
        font: opts.head ? "Calibri" : "Calibri",
        size: opts.head ? 17 : 20,
        bold: opts.bold || opts.head || false,
        italics: opts.italics || false,
        color: opts.color || (opts.head ? "FFFFFF" : "222222"),
        allCaps: opts.head || false,
        characterSpacing: opts.head ? 20 : 0
      })]
    })]
  });
}

const rows = [new TableRow({
  tableHeader: true,
  children: [
    cell("Ch.", { w: COLS[0], head: true, shade: NAVY }),
    cell("Chapter", { w: COLS[1], head: true, shade: NAVY }),
    cell("Anchor voice", { w: COLS[2], head: true, shade: NAVY })
  ]
})];

const anchorShort = {
  1: "Ron Blue", 2: "Randy Alcorn", 3: "Ron Blue \u00b7 April Chapman", 4: "April Chapman \u00b7 Ron Blue",
  5: "NCF \u00b7 The Signatry", 6: "Steve French", 7: "David Green", 8: "Rick Warren",
  9: "Bill High \u00b7 The Signatry", 10: "Ron Blue", 11: "The Signatry \u00b7 Bill High", 12: "The Signatry",
  13: "Generous Giving \u00b7 Todd Harper", 14: "The Gathering \u00b7 Josh Kwan", 15: "Kingdom Advisors \u00b7 Dale Armstrong", 16: "Rick Warren",
  17: "The Signatry", 18: "The Signatry", 19: "Daryl Heald", 20: "Todd Harper \u00b7 April Chapman"
};

C.parts.forEach((part, pi) => {
  rows.push(new TableRow({
    children: [
      new TableCell({
        width: { size: TW, type: WidthType.DXA },
        columnSpan: 3,
        borders: { top: NONE, bottom: NONE, left: NONE, right: NONE },
        shading: { type: ShadingType.CLEAR, fill: "F2EFE7", color: "auto" },
        margins: { top: 110, bottom: 110, left: 90, right: 90 },
        children: [new Paragraph({
          spacing: { after: 0 },
          children: [
            new TextRun({ text: "PART " + part.num.toUpperCase() + "   ", font: "Calibri", size: 17, bold: true, color: GOLD, characterSpacing: 24 }),
            new TextRun({ text: part.name, font: "Cambria", size: 22, bold: true, color: NAVY })
          ]
        })]
      })
    ]
  }));
  C.chapters.filter(c => c.part === pi + 1).forEach(c => {
    rows.push(new TableRow({
      children: [
        cell(String(c.n), { w: COLS[0], bold: true, color: GOLD }),
        cell(c.title, { w: COLS[1] }),
        cell(anchorShort[c.n], { w: COLS[2], italics: true, color: GREY })
      ]
    }));
  });
});

children.push(new Table({ columnWidths: COLS, width: { size: TW, type: WidthType.DXA }, rows: rows }));

children.push(new Paragraph({ children: [new PageBreak()] }));

/* ---------- Chapter by chapter ---------- */
children.push(h("Chapter by Chapter", HeadingLevel.HEADING_1, { before: 0 }));
children.push(p("Each entry gives the premise, the voice the chapter draws on, the story the authors need to go find, the turn where the reader's assumption breaks, and what the reader does before the chapter ends. Every chapter closes with its own action; the reflection questions belong in the back matter and the companion guide.", { after: 200 }));

C.parts.forEach((part, pi) => {
  children.push(new Paragraph({
    spacing: { before: 400, after: 60 },
    children: [new TextRun({ text: "PART " + part.num.toUpperCase(), font: "Calibri", size: 17, bold: true, color: GOLD, characterSpacing: 40 })]
  }));
  children.push(h(part.name, HeadingLevel.HEADING_2, { before: 0, after: 90, size: 34 }));
  children.push(p(part.premise, { italics: true, color: GREY, size: 21, after: 60 }));
  children.push(rule(20, 220));

  C.chapters.filter(c => c.part === pi + 1).forEach(c => {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_3,
      spacing: { before: 300, after: 100 },
      children: [
        new TextRun({ text: String(c.n) + ".  ", font: "Cambria", size: 26, bold: true, color: GOLD }),
        new TextRun({ text: c.title, font: "Cambria", size: 26, bold: true, color: NAVY })
      ]
    }));
    children.push(p(c.premise, { after: 130 }));
    children.push(field("Anchor", c.anchor));
    children.push(field("Story to source", c.story));
    children.push(field("The turn", c.turn));
    children.push(field("Reader's action", c.action));
    children.push(field("Target length", c.words.toLocaleString() + " words"));
  });
});

children.push(new Paragraph({ children: [new PageBreak()] }));

/* ---------- Front and back matter ---------- */
children.push(h("Front and Back Matter", HeadingLevel.HEADING_1, { before: 0 }));
const matter = [
  ["Foreword", "One voice from outside The Signatry. The natural ask is a founder of the movement rather than a peer institution \u2014 someone whose endorsement reads as blessing rather than trade. Roughly 900 words."],
  ["Introduction: The Word We Have to Earn", "The authors take the title apart before the reader can. Revolutionary is The Signatry's own mission language, and the introduction says plainly what would have to be true for it not to be a slogan. Ends by naming the three breaks the subtitle promises. 2,200 words."],
  ["Appendix A: How the Vehicles Actually Work", "Donor advised funds, private foundations, charitable remainder trusts, gifts of closely held stock and real estate \u2014 described neutrally, with the trade-offs of each and no recommendation. This is where every mechanism deferred from the body finally gets explained."],
  ["Appendix B: The Revolutionary Generosity Benchmark", "The twenty diagnostic questions, one per chapter, formatted so a family or an advisor can work through them in an evening. This is the artifact that travels furthest and should be designed accordingly."],
  ["Appendix C: A Six-Session Guide", "The book divided for small groups, family meetings, and advisor study groups. Five parts plus a closing session. Written so a layperson can lead it without training."],
  ["Acknowledgements", "Named credit to the organizations whose work the book synthesizes. Generosity about generosity is the least the book can do, and it is also the thing that makes it a movement book rather than a company book."]
];
matter.forEach(([t, b]) => {
  children.push(p(t, { bold: true, size: 22, color: NAVY, after: 50, before: 160 }));
  children.push(p(b, { after: 80 }));
});

/* ---------- Production ---------- */
children.push(h("Production Plan", HeadingLevel.HEADING_1));
const prod = [
  ["Manuscript", "65,000 words across twenty chapters plus front and back matter. Delivered in five parts so each can be reviewed and corrected before the next is drafted."],
  ["Interviews", "Twenty to thirty recorded conversations \u2014 the contributing voices, plus givers whose stories carry the chapters. The stories are the scarce resource in this book, not the ideas. Budget the interview calendar first."],
  ["Voice", "First person plural, with named single-author passages where one of them is telling his own story. Coaching tone, narrative paragraphs, minimal lists. The reader should feel advised by two people who have watched this go wrong."],
  ["Sequence", "Part Two is drafted first. It contains the most specific and least contested material, it proves the authors can write, and it is the part a publisher will read to decide."],
  ["Companion products", "The benchmark, the six-session guide, an advisor edition of Part Four, and a family edition of Part Three. Named here so the manuscript is written with them in view rather than retrofitted afterward."]
];
prod.forEach(([t, b]) => {
  children.push(p(t, { bold: true, size: 22, color: NAVY, after: 50, before: 160 }));
  children.push(p(b, { after: 80 }));
});

/* ---------- Decisions ---------- */
children.push(h("Decisions Required Before Drafting", HeadingLevel.HEADING_1));
children.push(p("Six open questions. None of them are editorial; all of them change the book.", { after: 160 }));
const decisions = [
  "Authorship. Have Steve French and Dale Armstrong agreed to write this, and is it a Signatry project or a personal one? Everything downstream \u2014 the no-ask rule, the endorsements, the publisher conversation \u2014 depends on the answer, and the answer is currently assumed rather than confirmed.",
  "The contributing voices. Are the named thinkers contributors, interview subjects, or simply lineage the book acknowledges? Three very different books, three very different permission conversations.",
  "Publisher or independent. A traditional house buys distribution and credibility and costs eighteen months. Independent publishing keeps derivative rights, which matter more than usual here because the companion products are where the real leverage sits.",
  "How much of The Signatry appears by name. The current outline keeps the organization almost entirely out of the body. If that is not acceptable internally, the no-ask rule needs to be renegotiated openly rather than eroded chapter by chapter.",
  "Who owns the benchmark. If the diagnostic becomes the movement's shared instrument it needs a neutral home; if it stays proprietary it will be read as lead generation, which will cost the book more than the instrument is worth.",
  "The story pipeline. Twenty chapters need roughly forty usable stories, and half of them have to come from outside The Signatry's own client base. Nobody has begun collecting them."
];
decisions.forEach((r, i) => {
  children.push(runsPara([
    new TextRun({ text: String(i + 1) + ".  ", font: "Cambria", size: 21, bold: true, color: GOLD }),
    new TextRun({ text: r, font: "Calibri", size: 21, color: "222222" })
  ], { after: 120, line: 280 }));
});

const doc = new Document({
  creator: "LifeTogether Ministries",
  title: C.title + " \u2014 Book Outline",
  description: "Concept outline",
  styles: {
    default: {
      document: { run: { font: "Calibri", size: 21, color: "222222" } }
    }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1300, bottom: 1300, left: 1440, right: 1440 }
      }
    },
    children: children
  }]
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('/home/claude/rg/Revolutionary-Generosity-Book-Outline.docx', b);
  console.log('outline written', b.length);
});
