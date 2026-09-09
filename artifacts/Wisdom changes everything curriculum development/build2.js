const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, LevelFormat, TabStopType, HeadingLevel, BorderStyle,
  WidthType, ShadingType, VerticalAlign, PageNumber, Header, Footer
} = require("docx");
const { sessions, weeks } = require("./content2.js");

// palette
const NAVY = "1B2A4A", NAVY2 = "2C4A7A", GOLD = "A8842C", GOLD2 = "C9A227";
const GOLD_LIGHT = "F5EFDD", NAVY_LIGHT = "E9EEF6", GREY = "555555", RULE = "D9CBA3";
const CW = 9360;
const NONE = { style: BorderStyle.NONE };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE };
const cb = { style: BorderStyle.SINGLE, size: 1, color: "C9CFDA" };
const tB = { top: cb, bottom: cb, left: cb, right: cb, insideHorizontal: cb, insideVertical: cb };

const T = (t, o = {}) => new TextRun({ text: t, size: o.size || 22, color: o.color || "242424", bold: o.bold, italics: o.italics, characterSpacing: o.cs });
const P = (children, o = {}) => new Paragraph({ spacing: { after: o.after != null ? o.after : 130, before: o.before || 0, line: o.line || 286 }, alignment: o.align, indent: o.indent, children: Array.isArray(children) ? children : (typeof children === "string" ? [T(children, { size: o.size || 22 })] : [children]) });
const blank = (h = 0) => new Paragraph({ spacing: { after: h }, children: [new TextRun("")] });

// micro section label (compact, designed)
function micro(text) {
  return new Paragraph({
    spacing: { before: 170, after: 70 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 5, color: RULE, space: 2 } },
    children: [new TextRun({ text: text.toUpperCase(), bold: true, color: GOLD, size: 18, characterSpacing: 70 })]
  });
}

// full-width navy band (section or session header) — placed at top of a new page
function band(parts, opts = {}) {
  const cellKids = parts;
  const tbl = new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: [CW], borders: noBorders,
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: CW, type: WidthType.DXA },
      shading: { fill: opts.fill || NAVY, type: ShadingType.CLEAR },
      borders: { left: { style: BorderStyle.SINGLE, size: 30, color: GOLD }, top: NONE, bottom: NONE, right: NONE },
      margins: { top: 150, bottom: 160, left: 240, right: 200 },
      children: cellKids
    })]})]
  });
  return tbl;
}
const pageStart = () => new Paragraph({ pageBreakBefore: true, spacing: { after: 60 }, children: [new TextRun("")] });

// gold idea box / navy practice box
function tintBox(label, runs, fill, accent) {
  return new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: [CW], borders: noBorders,
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CW, type: WidthType.DXA },
      shading: { fill, type: ShadingType.CLEAR },
      borders: { left: { style: BorderStyle.SINGLE, size: 22, color: accent }, top: NONE, bottom: NONE, right: NONE },
      margins: { top: 120, bottom: 120, left: 200, right: 180 },
      children: [
        new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: label.toUpperCase(), bold: true, color: accent, size: 17, characterSpacing: 60 })] }),
        new Paragraph({ spacing: { after: 0, line: 284 }, children: runs })
      ]
    })]})]
  });
}
const ideaBox = (label, text) => tintBox(label, [T(text, { size: 22 })], GOLD_LIGHT, GOLD);
const verseBox = (verse, text) => tintBox(verse, [T(text, { italics: true, size: 22, color: "333333" })], GOLD_LIGHT, GOLD);
const practiceBox = (text) => tintBox("This Week\u2019s Practice", [T(text, { size: 22 })], NAVY_LIGHT, NAVY2);

// two-column borderless table
function twoCol(leftKids, rightKids) {
  return new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: [4560, 4800], borders: noBorders,
    rows: [new TableRow({ children: [
      new TableCell({ width: { size: 4560, type: WidthType.DXA }, borders: noBorders, margins: { top: 0, bottom: 0, left: 0, right: 240 }, children: leftKids }),
      new TableCell({ width: { size: 4800, type: WidthType.DXA }, borders: noBorders, margins: { top: 0, bottom: 0, left: 240, right: 0 }, children: rightKids })
    ]})]
  });
}
// numbered paragraph (manual)
const numP = (i, text, color) => new Paragraph({ spacing: { after: 90, line: 280 }, indent: { left: 360, hanging: 360 },
  children: [new TextRun({ text: i + ".  ", bold: true, color: color || GOLD, size: 21 }), new TextRun({ text, size: 21 })] });

function leadIn(label, text, o = {}) {
  return P([new TextRun({ text: label + "  ", bold: true, color: NAVY, size: o.size || 22 }), T(text, { size: o.size || 22 })], { after: o.after != null ? o.after : 110 });
}

// generic header/body cells
const hCell = (t, w, al) => new TableCell({ width: { size: w, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, verticalAlign: VerticalAlign.CENTER, children: [new Paragraph({ alignment: al || AlignmentType.LEFT, children: [new TextRun({ text: t, bold: true, color: "FFFFFF", size: 18 })] })] });
const dCell = (kids, w, fill) => new TableCell({ width: { size: w, type: WidthType.DXA }, shading: fill ? { fill, type: ShadingType.CLEAR } : undefined, margins: { top: 70, bottom: 70, left: 120, right: 120 }, verticalAlign: VerticalAlign.CENTER, children: Array.isArray(kids) ? kids : [kids] });

const children = [];

// ============ COVER ============
children.push(
  blank(1500),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 30 }, children: [new TextRun({ text: "A CURRICULUM PROPOSAL", bold: true, color: GOLD, size: 22, characterSpacing: 140 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } }, children: [new TextRun({ text: "", size: 8 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 340, after: 70 }, children: [new TextRun({ text: "WISDOM CHANGES", bold: true, color: NAVY, size: 62 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 180 }, children: [new TextRun({ text: "EVERYTHING", bold: true, color: NAVY, size: 62 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: "This Changes Everything   \u00B7   40 Days of Financial Wisdom", color: NAVY2, size: 25, italics: true })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 240 }, children: [new TextRun({ text: "\u201CWhat has God entrusted to me \u2014 and what does His wisdom require?\u201D", color: GREY, size: 23 })] })
);
// six-H strip
const hWords = ["Honor", "Heart", "Habits", "Health", "Hope", "Harvest"];
children.push(blank(420));
children.push(new Table({
  width: { size: CW, type: WidthType.DXA }, columnWidths: [1560, 1560, 1560, 1560, 1560, 1560],
  borders: { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: { style: BorderStyle.SINGLE, size: 4, color: "33507F" } },
  rows: [new TableRow({ children: hWords.map((w, i) => new TableCell({
    width: { size: 1560, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR },
    margins: { top: 130, bottom: 130, left: 40, right: 40 }, verticalAlign: VerticalAlign.CENTER,
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [new TextRun({ text: String(i + 1), bold: true, color: GOLD2, size: 18 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: w, bold: true, color: "FFFFFF", size: 19 })] })
    ]
  })) })]
}));
children.push(blank(360));
children.push(
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 30 }, children: [new TextRun({ text: "Adult Small Group Curriculum", bold: true, color: NAVY, size: 23 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: [new TextRun({ text: "Overview   \u00B7   40-Day Outline   \u00B7   Six Full Sessions", color: GREY, size: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Ron Blue Institute   \u00B7   Financial Wisdom Ministry", bold: true, color: NAVY2, size: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 30 }, children: [new TextRun({ text: "June 2026", color: GREY, size: 18 })] })
);

// ============ 01 OVERVIEW ============
children.push(pageStart());
children.push(band([
  new Paragraph({ children: [new TextRun({ text: "01   ", bold: true, color: GOLD2, size: 24 }), new TextRun({ text: "Overview", bold: true, color: "FFFFFF", size: 32 })] }),
  new Paragraph({ spacing: { before: 20 }, children: [new TextRun({ text: "The vision, the promise, and how the journey works", italics: true, color: "D7DEEA", size: 20 })] })
]));
children.push(blank(40));

children.push(micro("A word before you begin"));
children.push(P("Most of us were never discipled about money. We were taught to pray, to read Scripture, to serve \u2014 but when it came to the one subject Jesus spoke about more than heaven and hell combined, the church often went quiet. So we picked up our financial beliefs the way most people do: from our families, our fears, and whatever we happened to absorb along the way."));
children.push(P("This journey is a different invitation. It is not a budgeting class and it is not a giving campaign. It is six weeks of letting God\u2019s wisdom reshape the way you hold money, possessions, and ultimately your whole life \u2014 your heart, your habits, your home, your hope, and your harvest. We start with money honestly, because money is where trust gets tested most. Then we follow the thread outward into everything else."));
children.push(P([T("Here is the promise that shapes this entire guide: "), new TextRun({ text: "no one will ever be asked how much you make, owe, give, or have saved.", bold: true, color: NAVY, size: 22 }), T(" Dignity matters more than disclosure.")]));

children.push(micro("Why this, why now"));
children.push(P("Many financial programs are built to help people get out of trouble \u2014 eliminate debt, fix the budget, regain control. That work is good and necessary. But it usually speaks to one kind of family, in one kind of season, and it ends when the crisis ends."));
children.push(P([new TextRun({ text: "Wisdom Changes Everything", italics: true, size: 22, color: "242424" }), T(" is built differently. It is for the family that is struggling "), new TextRun({ text: "and", italics: true, size: 22 }), T(" the family that is doing well, because both need wisdom and both can drift. The conviction underneath all of it is one Ron Blue has spent a lifetime teaching: "), new TextRun({ text: "God owns it all.", bold: true, color: NAVY, size: 22 }), T(" When you truly settle that one question, everything downstream reorganizes around a different center.")]));

children.push(micro("How to use this guide"));
children.push(P([T("Every week follows the same rhythm. You "), new TextRun({ text: "gather", bold: true, color: NAVY, size: 22 }), T(" with a welcome and a story, "), new TextRun({ text: "watch", bold: true, color: NAVY, size: 22 }), T(" a short teaching, "), new TextRun({ text: "talk it through", bold: true, color: NAVY, size: 22 }), T(", put your hands on a practical "), new TextRun({ text: "tool", bold: true, color: NAVY, size: 22 }), T(", take a private "), new TextRun({ text: "self-assessment", bold: true, color: NAVY, size: 22 }), T(", and leave with "), new TextRun({ text: "one doable step", bold: true, color: NAVY, size: 22 }), T(". You close in "), new TextRun({ text: "prayer", bold: true, color: NAVY, size: 22 }), T(" and carry the theme through the week with seven "), new TextRun({ text: "devotional", bold: true, color: NAVY, size: 22 }), T(" readings.")]));
children.push(P([new TextRun({ text: "Three asks: ", bold: true, color: NAVY, size: 22 }), new TextRun({ text: "show up, stay honest, and try the weekly step.", bold: true, color: NAVY, size: 22 }), T(" You don\u2019t need to read ahead or have your finances figured out. You only need to be willing. And a note for leaders: you are not the expert in the room. Your job is to create a safe table \u2014 no shame, no pressure, no public numbers \u2014 and keep the conversation moving. The video carries the teaching; you carry the room.")]));

children.push(micro("The six movements at a glance"));
children.push(P("The arc moves from who owns it all, inward to the heart, into daily practice, toward wholeness and peace, outward to an eternal perspective, and finally to a life that multiplies.", { after: 110 }));
const gHead = new TableRow({ tableHeader: true, children: [hCell("Wk", 720, AlignmentType.CENTER), hCell("Movement & Session", 4040), hCell("Key Verse", 2080), hCell("Group Goal", 2520)] });
const goals = ["Move from control to trust", "Break the comparison trap", "Replace confusion with clarity", "Build margin, reduce anxiety", "Live with vision beyond self", "Move from maintenance to multiplication"];
const gRows = sessions.map((s, i) => new TableRow({ children: [
  dCell(new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: String(s.n), bold: true, color: NAVY, size: 22 })] }), 720, i % 2 ? "F4F6FA" : "FFFFFF"),
  dCell([new Paragraph({ spacing: { after: 8 }, children: [new TextRun({ text: s.h + " \u00B7 ", bold: true, color: GOLD, size: 18 }), new TextRun({ text: s.title, bold: true, color: NAVY, size: 20 })] }), new Paragraph({ children: [new TextRun({ text: s.sub, italics: true, color: GREY, size: 17 })] })], 4040, i % 2 ? "F4F6FA" : "FFFFFF"),
  dCell(new Paragraph({ children: [new TextRun({ text: s.verse, color: "333333", size: 19 })] }), 2080, i % 2 ? "F4F6FA" : "FFFFFF"),
  dCell(new Paragraph({ children: [new TextRun({ text: goals[i], color: "333333", size: 19 })] }), 2520, i % 2 ? "F4F6FA" : "FFFFFF")
]}));
children.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [720, 4040, 2080, 2520], borders: tB, rows: [gHead, ...gRows] }));

children.push(micro("Scale it to your church"));
children.push(P([
  new TextRun({ text: "6 Sessions ", bold: true, color: NAVY, size: 22 }), T("the small-group core  \u00B7  "),
  new TextRun({ text: "40 Days ", bold: true, color: NAVY, size: 22 }), T("the full churchwide campaign  \u00B7  "),
  new TextRun({ text: "30 Days ", bold: true, color: NAVY, size: 22 }), T("a personal follow-up  \u00B7  "),
  new TextRun({ text: "21 Days ", bold: true, color: NAVY, size: 22 }), T("a focused reset  \u00B7  "),
  new TextRun({ text: "7 Days ", bold: true, color: NAVY, size: 22 }), T("a weekend jumpstart.")
]));
children.push(P("The shorter formats are on-ramps; the longer formats are transformation. They flow into one another \u2014 and into an ongoing Financial Wisdom Ministry once the campaign ends. The campaign is the catalyst; the ministry is the container.", { after: 150 }));
children.push(ideaBox("What \u201CThis Changes Everything\u201D means", "This is God\u2019s wisdom. Changes is what happens when we trust and obey. Everything is the whole life He has entrusted to us \u2014 our heart, habits, household, finances, generosity, and legacy."));

// ============ 02 40-DAY OUTLINE ============
children.push(pageStart());
children.push(band([
  new Paragraph({ children: [new TextRun({ text: "02   ", bold: true, color: GOLD2, size: 24 }), new TextRun({ text: "The 40-Day Outline", bold: true, color: "FFFFFF", size: 32 })] }),
  new Paragraph({ spacing: { before: 20 }, children: [new TextRun({ text: "Daily readings across the six movements", italics: true, color: "D7DEEA", size: 20 })] })
]));
children.push(blank(40));
children.push(P([T("The full churchwide campaign carries the same six movements across forty daily readings (two to three minutes each), bookended by an Intro Sunday and a Celebration Sunday. Each day maps to that week\u2019s session, so Sunday teaching, groups, and daily devotions all move together.")], { after: 120 }));
children.push(P([new TextRun({ text: "Intro \u00B7 Wisdom Changes Everything.  ", bold: true, color: NAVY, size: 21 }), new TextRun({ text: "The Ownership Question \u00B7 The Freedom Ladder \u00B7 When Belief Meets Behavior.", size: 21 })], { after: 140 }));

weeks.forEach((w, wi) => {
  children.push(new Paragraph({ spacing: { before: wi === 0 ? 20 : 200, after: 70 }, keepNext: true,
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 2 } },
    children: [new TextRun({ text: `WEEK ${wi + 1}  \u00B7  ${w.h}`, bold: true, color: GOLD, size: 21 }), new TextRun({ text: `   ${w.title}`, bold: true, color: NAVY, size: 21 }), new TextRun({ text: `   \u2014 ${w.focus}`, italics: true, color: GREY, size: 17 })] }));
  const head = new TableRow({ tableHeader: true, children: [hCell("Day", 700, AlignmentType.CENTER), hCell("Reading", 3160), hCell("Verse", 2100), hCell("Daily Prompt", 3400)] });
  const rows = w.days.map((d, i) => new TableRow({ children: [
    dCell(new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: d[0], bold: true, color: NAVY, size: 20 })] }), 700, i % 2 ? "F4F6FA" : "FFFFFF"),
    dCell(new Paragraph({ children: [new TextRun({ text: d[1], bold: true, color: NAVY, size: 19 })] }), 3160, i % 2 ? "F4F6FA" : "FFFFFF"),
    dCell(new Paragraph({ children: [new TextRun({ text: d[2], color: "333333", size: 18 })] }), 2100, i % 2 ? "F4F6FA" : "FFFFFF"),
    dCell(new Paragraph({ children: [new TextRun({ text: d[3], italics: true, color: "444444", size: 17 })] }), 3400, i % 2 ? "F4F6FA" : "FFFFFF")
  ]}));
  children.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [700, 3160, 2100, 3400], borders: tB, rows: [head, ...rows] }));
});
children.push(P([new TextRun({ text: "Celebration Sunday.  ", bold: true, color: GOLD, size: 21 }), new TextRun({ text: "Testimonies, generosity commitments, and Legacy Letters \u2014 the congregation celebrates stories of transformation from the journey.", size: 21 })], { before: 160 }));

// ============ 03 THE SIX SESSIONS ============
children.push(pageStart());
children.push(band([
  new Paragraph({ children: [new TextRun({ text: "03   ", bold: true, color: GOLD2, size: 24 }), new TextRun({ text: "The Six Sessions", bold: true, color: "FFFFFF", size: 32 })] }),
  new Paragraph({ spacing: { before: 20 }, children: [new TextRun({ text: "Complete participant-guide spreads, ready to facilitate", italics: true, color: "D7DEEA", size: 20 })] })
]));
children.push(blank(20));
children.push(P("Each session below runs the full small-group rhythm. They share one proven structure; every story, tool, and assessment is specific to its movement.", { after: 40 }));

function renderTool(t) {
  const out = [];
  out.push(P(t.intro, { after: 110 }));
  if (t.cols) {
    const head = new TableRow({ tableHeader: true, children: t.cols.map((c, i) => hCell(c, Math.floor(CW / t.cols.length))) });
    const rows = t.rows.map(r => new TableRow({ children: t.cols.map((c, ci) => dCell(
      new Paragraph({ spacing: { before: 50, after: 50 }, children: [new TextRun({ text: (ci === 0 && typeof r === "string") ? r : "", bold: ci === 0, color: NAVY, size: 19 })] }),
      Math.floor(CW / t.cols.length)))
    }));
    out.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: t.cols.map(() => Math.floor(CW / t.cols.length)), borders: tB, rows: [head, ...rows] }));
  }
  if (t.prompts) t.prompts.forEach(p => out.push(P([new TextRun({ text: "\u25B8  ", color: GOLD, bold: true, size: 21 }), T(p, { size: 21 })], { before: 60, after: 60 })));
  if (t.close) out.push(P([new TextRun({ text: "Then: ", bold: true, color: NAVY, size: 21 }), new TextRun({ text: t.close, italics: true, color: "333333", size: 21 })], { before: 110 }));
  return out;
}

sessions.forEach((s, si) => {
  // session band (flows continuously to avoid trailing white space)
  children.push(blank(si === 0 ? 60 : 200));
  children.push(band([
    new Paragraph({ spacing: { after: 24 }, children: [new TextRun({ text: `SESSION ${s.n}   \u00B7   ${s.h}`, bold: true, color: GOLD2, size: 19, characterSpacing: 40 })] }),
    new Paragraph({ spacing: { after: 18 }, children: [new TextRun({ text: s.title, bold: true, color: "FFFFFF", size: 34 })] }),
    new Paragraph({ children: [new TextRun({ text: s.sub, italics: true, color: "D7DEEA", size: 21 })] })
  ]));
  children.push(blank(60));
  children.push(verseBox("Theme Verse \u00B7 " + s.verse, s.verseText));
  children.push(blank(70));
  children.push(ideaBox("Big Idea", s.big));

  // WELCOME
  children.push(micro("Welcome"));
  children.push(P(s.welcome));
  children.push(leadIn("Opening Prayer.", "\u201C" + s.prayer0 + "\u201D"));
  children.push(leadIn("Icebreaker.", s.icebreaker, { after: 40 }));

  // OPENING STORY
  children.push(micro("Opening Story \u2014 " + s.story.title));
  children.push(P(s.story.text, { after: 40 }));

  // WATCH
  children.push(micro("Watch \u2014 Teaching & Fill-in Notes"));
  children.push(P("As you watch, listen for how this week\u2019s truth reshapes the way you hold money. Fill in the blanks as you go.", { after: 90 }));
  s.fillins.forEach(f => children.push(new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: "\u2022  ", color: GOLD, bold: true, size: 22 }), T(f, { size: 22 })] })));

  // DISCUSSION (two columns)
  children.push(micro("Table Discussion"));
  const half = Math.ceil(s.discuss.length / 2);
  const left = s.discuss.slice(0, half).map((q, i) => numP(i + 1, q));
  const right = s.discuss.slice(half).map((q, i) => numP(i + 1 + half, q));
  children.push(twoCol(left, right));

  // SCRIPTURE REFLECTION
  children.push(micro("Scripture Reflection"));
  s.reflect.forEach(r => children.push(leadIn(r[0] + ".", r[1], { after: 90 })));

  // TOOL
  children.push(micro("Financial Wisdom Tool \u2014 " + s.tool.name));
  renderTool(s.tool).forEach(x => children.push(x));

  // ASSESSMENT
  children.push(micro("Personal Assessment \u2014 Private"));
  children.push(P("Not shared. Rate each statement from 1 (not true of me) to 5 (very true of me).", { after: 70 }));
  s.assess.forEach((a, i) => children.push(new Paragraph({ spacing: { after: 64 }, indent: { left: 360, hanging: 360 }, children: [
    new TextRun({ text: (i + 1) + ".  ", bold: true, color: NAVY, size: 21 }), new TextRun({ text: a + "   ", size: 21 }), new TextRun({ text: "_____", bold: true, color: GOLD, size: 21 })
  ]})));

  // PRACTICE
  children.push(blank(40));
  children.push(practiceBox(s.practice));

  // PRAYER + MEMORY
  children.push(micro("Close in Prayer"));
  children.push(P([new TextRun({ text: "Memory Verse \u2014 " + s.verse + ".  ", bold: true, color: NAVY, size: 21 }), new TextRun({ text: "\u201C" + s.verseText + "\u201D", italics: true, color: "333333", size: 21 })], { after: 80 }));
  children.push(P([new TextRun({ text: "Together:  ", bold: true, color: NAVY, size: 21 }), new TextRun({ text: "\u201C" + s.prayer + "\u201D", italics: true, color: "333333", size: 21 })], { after: 40 }));

  // DEVOTIONAL (two columns)
  children.push(micro("Seven-Day Devotional"));
  children.push(P("A companion to this session \u2014 one short reading each day this week.", { after: 80 }));
  const wk = weeks[si].days;
  const dHalf = Math.ceil(wk.length / 2);
  const devPara = (d) => new Paragraph({ spacing: { after: 90, line: 274 }, children: [
    new TextRun({ text: "Day " + d[0] + " \u2014 " + d[1] + ".  ", bold: true, color: NAVY, size: 19 }),
    new TextRun({ text: d[2] + "  ", italics: true, color: GOLD, size: 18 }),
    new TextRun({ text: d[3], size: 19 })
  ]});
  children.push(twoCol(wk.slice(0, dHalf).map(devPara), wk.slice(dHalf).map(devPara)));
});

// ============ ASSEMBLE ============
const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  sections: [{
    properties: { titlePage: true, page: { size: { width: 12240, height: 15840 }, margin: { top: 1300, right: 1320, bottom: 1180, left: 1320 } } },
    headers: {
      first: new Header({ children: [new Paragraph({ children: [] })] }),
      default: new Header({ children: [new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
        children: [new TextRun({ text: "WISDOM CHANGES EVERYTHING", color: NAVY2, size: 15, characterSpacing: 30 }), new TextRun({ text: "\tCurriculum Proposal", color: GREY, size: 15 })]
      })] })
    },
    footers: {
      first: new Footer({ children: [new Paragraph({ children: [] })] }),
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 30 },
        children: [new TextRun({ text: "Ron Blue Institute  \u00B7  Financial Wisdom Ministry  \u00B7  ", color: GREY, size: 15 }), new TextRun({ children: [PageNumber.CURRENT], color: GREY, size: 15 })] })] })
    },
    children
  }]
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync("/home/claude/Wisdom_Changes_Everything_Proposal.docx", buf); console.log("WROTE. blocks:", children.length); });
