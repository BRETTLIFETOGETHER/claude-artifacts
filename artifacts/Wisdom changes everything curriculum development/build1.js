const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, LevelFormat, TabStopType, TabStopPosition,
  HeadingLevel, BorderStyle, WidthType, ShadingType, VerticalAlign,
  PageNumber, PageBreak, Header, Footer
} = require("docx");
const { sessions, weeks } = require("./content.js");

// ---------- Brand palette ----------
const NAVY = "1B2A4A";
const NAVY2 = "2C4A7A";
const GOLD = "A8842C";
const GOLD_LIGHT = "F4EEDC";
const NAVY_LIGHT = "E7ECF4";
const GREY = "555555";
const RULE = "D9CBA3";

const CW = 9360; // content width

// ---------- helpers ----------
const goldRule = (after = 200) => new Paragraph({
  spacing: { before: 40, after },
  border: { bottom: { style: BorderStyle.SINGLE, size: 14, color: GOLD, space: 2 } },
  children: [new TextRun({ text: "" })]
});

function kicker(text) {
  return new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: text.toUpperCase(), bold: true, color: GOLD, size: 18, characterSpacing: 60 })]
  });
}

function sectionTitle(num, text, opts = {}) {
  return [
    new Paragraph({
      pageBreakBefore: opts.break !== false,
      spacing: { before: opts.break === false ? 120 : 0, after: 30 },
      children: [
        new TextRun({ text: `${num}  `, bold: true, color: GOLD, size: 34 }),
        new TextRun({ text: text, bold: true, color: NAVY, size: 34 })
      ]
    }),
    goldRule(220)
  ];
}

function h2(text, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before || 240, after: 90 },
    children: [new TextRun({ text, bold: true, color: NAVY, size: 26 })]
  });
}

function h3(text, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before || 180, after: 60 },
    children: [new TextRun({ text, bold: true, color: NAVY2, size: 22 })]
  });
}

function body(text, opts = {}) {
  const runs = Array.isArray(text) ? text : [new TextRun({ text, size: 22, color: "222222" })];
  return new Paragraph({
    spacing: { after: opts.after != null ? opts.after : 140, line: 288 },
    alignment: opts.align || AlignmentType.LEFT,
    children: runs
  });
}

function bullet(text, ref = "bullets") {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 70, line: 276 },
    children: [new TextRun({ text, size: 22, color: "222222" })]
  });
}

function numbered(text, ref) {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 70, line: 276 },
    children: [new TextRun({ text, size: 22, color: "222222" })]
  });
}

// label: bold inline lead-in then text
function leadIn(label, text) {
  return new Paragraph({
    spacing: { after: 110, line: 288 },
    children: [
      new TextRun({ text: label + "  ", bold: true, color: NAVY, size: 22 }),
      new TextRun({ text, size: 22, color: "222222" })
    ]
  });
}

function verseCallout(verse, text) {
  return new Table({
    width: { size: CW, type: WidthType.DXA },
    columnWidths: [CW],
    borders: {
      top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.SINGLE, size: 24, color: GOLD }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE }
    },
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CW, type: WidthType.DXA },
      shading: { fill: GOLD_LIGHT, type: ShadingType.CLEAR },
      margins: { top: 120, bottom: 120, left: 200, right: 160 },
      children: [
        new Paragraph({ spacing: { after: 30 }, children: [new TextRun({ text, italics: true, size: 22, color: "333333" })] }),
        new Paragraph({ children: [new TextRun({ text: "\u2014 " + verse, bold: true, size: 20, color: NAVY })] })
      ]
    })]})]
  });
}

function spacer(h = 80) { return new Paragraph({ spacing: { after: h }, children: [new TextRun("")] }); }

// generic header cell
function hCell(text, w, align = AlignmentType.LEFT) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: { fill: NAVY, type: ShadingType.CLEAR },
    margins: { top: 90, bottom: 90, left: 130, right: 130 },
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({ alignment: align, children: [new TextRun({ text, bold: true, color: "FFFFFF", size: 19 })] })]
  });
}

function tCell(children, w, opts = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR } : undefined,
    margins: { top: 80, bottom: 80, left: 130, right: 130 },
    verticalAlign: VerticalAlign.CENTER,
    children: Array.isArray(children) ? children : [children]
  });
}

const cellBorder = { style: BorderStyle.SINGLE, size: 1, color: "C9CFDA" };
const tableBorders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder, insideHorizontal: cellBorder, insideVertical: cellBorder };

// ============================================================
// BUILD CONTENT
// ============================================================
const children = [];

// ---------- COVER ----------
children.push(
  new Paragraph({ spacing: { before: 1600, after: 0 }, children: [] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
    children: [new TextRun({ text: "A CURRICULUM PROPOSAL", bold: true, color: GOLD, size: 22, characterSpacing: 120 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } },
    children: [new TextRun({ text: "", size: 8 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 360, after: 80 },
    children: [new TextRun({ text: "WISDOM CHANGES", bold: true, color: NAVY, size: 64 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
    children: [new TextRun({ text: "EVERYTHING", bold: true, color: NAVY, size: 64 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
    children: [new TextRun({ text: "This Changes Everything  \u00B7  40 Days of Financial Wisdom", color: NAVY2, size: 26, italics: true })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 280, after: 0 },
    children: [new TextRun({ text: "\u201CWhat has God entrusted to me \u2014", color: GREY, size: 24 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
    children: [new TextRun({ text: "and what does His wisdom require?\u201D", color: GREY, size: 24 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 1400, after: 0 },
    border: { top: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 6 } },
    children: [new TextRun({ text: "", size: 8 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 40 },
    children: [new TextRun({ text: "Adult Small Group Curriculum", bold: true, color: NAVY, size: 24 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
    children: [new TextRun({ text: "Overview  \u00B7  Six-Session Outline  \u00B7  40-Day Outline  \u00B7  Sample Session", color: GREY, size: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 },
    children: [new TextRun({ text: "Ron Blue Institute  \u00B7  Financial Wisdom Ministry", bold: true, color: NAVY2, size: 20 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 40 },
    children: [new TextRun({ text: "June 2026", color: GREY, size: 18 })] })
);

// ---------- CONTENTS ----------
children.push(new Paragraph({ pageBreakBefore: true, spacing: { after: 30 },
  children: [new TextRun({ text: "Contents", bold: true, color: NAVY, size: 34 })] }));
children.push(goldRule(220));
const toc = [
  ["01", "Overview", "The vision, the promise, and how the journey works"],
  ["02", "The Six-Session Outline", "The full arc, session by session"],
  ["03", "The 40-Day Outline", "Daily readings across the six movements"],
  ["04", "Sample Curriculum \u2014 Session 1", "A complete participant-guide spread"]
];
toc.forEach(([n, t, d]) => {
  children.push(new Paragraph({ spacing: { after: 40 }, children: [
    new TextRun({ text: n + "   ", bold: true, color: GOLD, size: 24 }),
    new TextRun({ text: t, bold: true, color: NAVY, size: 24 })
  ]}));
  children.push(new Paragraph({ spacing: { after: 160 }, indent: { left: 560 }, children: [
    new TextRun({ text: d, italics: true, color: GREY, size: 20 })
  ]}));
});

// ============================================================
// SECTION 01 — OVERVIEW
// ============================================================
children.push(...sectionTitle("01", "Overview"));
children.push(kicker("A word before you begin"));
children.push(body("Most of us were never discipled about money. We were taught to pray, to read Scripture, to serve \u2014 but when it came to the one subject Jesus spoke about more than heaven and hell combined, the church often went quiet. So we picked up our financial beliefs the way most people do: from our families, our fears, and whatever we happened to absorb along the way."));
children.push(body("This journey is a different invitation. It is not a budgeting class and it is not a giving campaign. It is six weeks of letting God\u2019s wisdom reshape the way you hold money, possessions, and ultimately your whole life \u2014 your heart, your habits, your home, your hope, and your harvest. We start with money honestly, because money is where trust gets tested most. Then we follow the thread outward into everything else."));
children.push(body([
  new TextRun({ text: "Here is the promise that shapes this entire guide: ", size: 22, color: "222222" }),
  new TextRun({ text: "no one will ever be asked how much you make, owe, give, or have saved.", bold: true, size: 22, color: NAVY }),
  new TextRun({ text: " Dignity matters more than disclosure. You can be completely honest here without ever putting a number on the table.", size: 22, color: "222222" })
]));

children.push(h2("Why this, why now"));
children.push(body("Many financial programs are built to help people get out of trouble \u2014 eliminate debt, fix the budget, regain control. That work is good and necessary. But it usually speaks to one kind of family, in one kind of season, and it usually ends when the crisis ends."));
children.push(body([
  new TextRun({ text: "Wisdom Changes Everything", italics: true, size: 22, color: "222222" }),
  new TextRun({ text: " is built differently. It is for the family that is struggling ", size: 22, color: "222222" }),
  new TextRun({ text: "and", italics: true, size: 22, color: "222222" }),
  new TextRun({ text: " the family that is doing well, because both need wisdom and both can drift. It moves through six movements that apply at every income level and every life stage \u2014 from the person living paycheck to paycheck to the person wondering what \u201Cenough\u201D even means. The goal is not merely financial peace. The goal is a heart that trusts God, a household that\u2019s aligned, and a life that overflows into the next generation.", size: 22, color: "222222" })
]));
children.push(body([
  new TextRun({ text: "The conviction underneath all of it is one Ron Blue has spent a lifetime teaching: ", size: 22, color: "222222" }),
  new TextRun({ text: "God owns it all.", bold: true, size: 22, color: NAVY }),
  new TextRun({ text: " When you truly settle that one question, everything downstream begins to reorganize around a different center. That is what \u201Cthis changes everything\u201D actually means.", size: 22, color: "222222" })
]));

children.push(h2("How to use this guide"));
children.push(body([
  new TextRun({ text: "Every week follows the same simple rhythm, so the group always knows what comes next. You ", size: 22, color: "222222" }),
  new TextRun({ text: "gather", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: " with a welcome and an opening story on the week\u2019s theme. You ", size: 22, color: "222222" }),
  new TextRun({ text: "watch", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: " a short teaching video and take a few fill-in notes. You ", size: 22, color: "222222" }),
  new TextRun({ text: "talk it through", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: " as a group. You put your hands on a practical ", size: 22, color: "222222" }),
  new TextRun({ text: "financial wisdom tool", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: ", take a brief ", size: 22, color: "222222" }),
  new TextRun({ text: "private self-assessment", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: " that no one else sees, and leave with ", size: 22, color: "222222" }),
  new TextRun({ text: "one doable step", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: " to practice before you meet again. You close in ", size: 22, color: "222222" }),
  new TextRun({ text: "prayer", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: ", and carry the theme through the week using the seven companion ", size: 22, color: "222222" }),
  new TextRun({ text: "devotional", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: " readings.", size: 22, color: "222222" })
]));
children.push(body([
  new TextRun({ text: "You will get the most out of this if you do three things: ", size: 22, color: "222222" }),
  new TextRun({ text: "show up, stay honest, and try the weekly step.", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: " You don\u2019t need to read ahead, prepare anything, or have your finances figured out. You only need to be willing.", size: 22, color: "222222" })
]));
children.push(body([
  new TextRun({ text: "A note for leaders: ", bold: true, color: NAVY, size: 22 }),
  new TextRun({ text: "you are not the expert in the room, and you are not expected to be. Your job is to create a safe table \u2014 no shame, no pressure, no unsolicited advice, no public numbers \u2014 and to keep the conversation moving. The video carries the teaching. You carry the room.", size: 22, color: "222222" })
]));

children.push(h2("The six movements at a glance"));
children.push(body("The arc is intentional. It moves from who owns it all, inward to the heart, into daily practice, toward wholeness and peace, outward to an eternal perspective, and finally to a life that multiplies.", { after: 120 }));

// at-a-glance table
const glanceHeader = new TableRow({ tableHeader: true, children: [
  hCell("Wk", 760, AlignmentType.CENTER),
  hCell("Movement & Session", 4000),
  hCell("Key Verse", 2200),
  hCell("Group Goal", 2400)
]});
const glanceRows = sessions.map((s, i) => new TableRow({ children: [
  tCell(new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: String(s.n), bold: true, color: NAVY, size: 22 })] }), 760, { fill: i % 2 ? "F4F6FA" : "FFFFFF" }),
  tCell([
    new Paragraph({ spacing: { after: 10 }, children: [new TextRun({ text: s.h + " \u00B7 ", bold: true, color: GOLD, size: 19 }), new TextRun({ text: s.title, bold: true, color: NAVY, size: 21 })] }),
    new Paragraph({ children: [new TextRun({ text: s.sub, italics: true, color: GREY, size: 18 })] })
  ], 4000, { fill: i % 2 ? "F4F6FA" : "FFFFFF" }),
  tCell(new Paragraph({ children: [new TextRun({ text: s.verse, color: "333333", size: 20 })] }), 2200, { fill: i % 2 ? "F4F6FA" : "FFFFFF" }),
  tCell(new Paragraph({ children: [new TextRun({ text: s.goal, color: "333333", size: 20 })] }), 2400, { fill: i % 2 ? "F4F6FA" : "FFFFFF" })
]}));
children.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [760, 4000, 2200, 2400], borders: tableBorders, rows: [glanceHeader, ...glanceRows] }));

children.push(h2("Scale it to your church"));
children.push(body("The same content flexes to whatever commitment your people can make. Many churches run several of these at once or in sequence:"));
children.push(bullet("6 Sessions \u2014 the small-group core (this guide)."));
children.push(bullet("40 Days \u2014 the full churchwide campaign with weekend messages, groups, and a daily devotional."));
children.push(bullet("30 Days \u2014 a personal follow-up to sustain the momentum."));
children.push(bullet("21 Days \u2014 a focused reset to rebuild habits and restore peace."));
children.push(bullet("7 Days \u2014 a weekend jumpstart to spark awareness and a first \u201Cyes.\u201D"));
children.push(body("The shorter formats are on-ramps; the longer formats are transformation. They flow into one another \u2014 and into an ongoing Financial Wisdom Ministry once the campaign ends. The campaign is the catalyst; the ministry is the container.", { after: 160 }));

children.push(h2("What \u201CThis Changes Everything\u201D means"));
children.push(verseCallout("Use this everywhere", "This is God\u2019s wisdom. Changes is what happens when we trust and obey. Everything is the whole life He has entrusted to us \u2014 our heart, habits, household, finances, generosity, and legacy."));
children.push(spacer(120));
children.push(body("You were not created to own everything, control everything, or carry everything. You were created to steward what God has entrusted to you with wisdom, faith, and generosity. That\u2019s the journey."));

// ============================================================
// SECTION 02 — SIX-SESSION OUTLINE
// ============================================================
children.push(...sectionTitle("02", "The Six-Session Outline"));
children.push(body([
  new TextRun({ text: "The journey moves inward, then outward: from settling who owns it all, to the heart beneath our money, to the daily practices of a steward, to wholeness and margin, to an eternal perspective, and finally to a life that multiplies. Each session runs the same proven rhythm \u2014 welcome and opening story, teaching video, fill-in notes, table discussion, a hands-on tool, a private assessment, a weekly practice, prayer, and a seven-day devotional tie-in.", italics: true, size: 21, color: GREY })
], { after: 200 }));

sessions.forEach((s, idx) => {
  children.push(new Paragraph({
    spacing: { before: idx === 0 ? 60 : 320, after: 30 },
    keepNext: true,
    children: [
      new TextRun({ text: `SESSION ${s.n}  \u00B7  `, bold: true, color: GOLD, size: 20 }),
      new TextRun({ text: s.title, bold: true, color: NAVY, size: 28 })
    ]
  }));
  children.push(new Paragraph({ spacing: { after: 40 }, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: RULE, space: 2 } },
    children: [new TextRun({ text: `${s.h} \u00B7 ${s.sub}`, bold: true, color: NAVY2, size: 21 }), new TextRun({ text: `   \u2014 ${s.line}`, italics: true, color: GREY, size: 19 })] }));
  children.push(spacer(60));
  children.push(verseCallout(s.verse, s.verseText));
  children.push(spacer(80));
  children.push(leadIn("Big Idea.", s.big));
  children.push(new Paragraph({ spacing: { before: 40, after: 50 }, children: [new TextRun({ text: "Core Movements", bold: true, color: NAVY, size: 21 })] }));
  s.moves.forEach(m => children.push(bullet(m)));
  children.push(leadIn("Pastoral Outcome.", s.outcome));
  children.push(leadIn("Hands-on Tool.", s.tool));
  children.push(leadIn("Private Assessment.", s.assess));
  children.push(leadIn("This Week\u2019s Practice.", s.practice));
});

// ============================================================
// SECTION 03 — 40-DAY OUTLINE
// ============================================================
children.push(...sectionTitle("03", "The 40-Day Outline"));
children.push(body([
  new TextRun({ text: "The full churchwide campaign carries the same six movements across forty daily readings (about two to three minutes each), bookended by an Intro Sunday and a Celebration Sunday. Each day maps to the small-group session for that week, so Sunday teaching, groups, and daily devotions all move together.", italics: true, size: 21, color: GREY })
], { after: 180 }));

children.push(new Paragraph({ spacing: { after: 140 }, children: [
  new TextRun({ text: "Intro \u00B7 Wisdom Changes Everything.  ", bold: true, color: NAVY, size: 21 }),
  new TextRun({ text: "Why wisdom \u2014 not wealth \u2014 changes lives. The Ownership Question \u00B7 The Freedom Ladder \u00B7 When Belief Meets Behavior.", size: 21, color: "222222" })
]}));

weeks.forEach((w, wi) => {
  children.push(new Paragraph({
    spacing: { before: wi === 0 ? 40 : 240, after: 30 }, keepNext: true,
    children: [
      new TextRun({ text: `WEEK ${wi + 1}  \u00B7  ${w.h}`, bold: true, color: GOLD, size: 22 }),
      new TextRun({ text: `   ${w.title}`, bold: true, color: NAVY, size: 22 })
    ]
  }));
  children.push(new Paragraph({ spacing: { after: 90 }, keepNext: true, children: [new TextRun({ text: w.focus, italics: true, color: GREY, size: 19 })] }));

  const header = new TableRow({ tableHeader: true, children: [
    hCell("Day", 760, AlignmentType.CENTER),
    hCell("Reading", 5600),
    hCell("Key Verse", 3000)
  ]});
  const rows = w.days.map((d, i) => new TableRow({ children: [
    tCell(new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: d[0], bold: true, color: NAVY, size: 21 })] }), 760, { fill: i % 2 ? "F4F6FA" : "FFFFFF" }),
    tCell([
      new Paragraph({ spacing: { after: 8 }, children: [new TextRun({ text: d[1], bold: true, color: NAVY, size: 20 })] }),
      new Paragraph({ children: [new TextRun({ text: d[2], italics: true, color: GREY, size: 18 })] })
    ], 5600, { fill: i % 2 ? "F4F6FA" : "FFFFFF" }),
    tCell(new Paragraph({ children: [new TextRun({ text: d[3], color: "333333", size: 19 })] }), 3000, { fill: i % 2 ? "F4F6FA" : "FFFFFF" })
  ]}));
  children.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [760, 5600, 3000], borders: tableBorders, rows: [header, ...rows] }));
});

children.push(new Paragraph({ spacing: { before: 200 }, children: [
  new TextRun({ text: "Celebration Sunday.  ", bold: true, color: GOLD, size: 21 }),
  new TextRun({ text: "Testimonies, generosity commitments, and Legacy Letters \u2014 the congregation celebrates stories of transformation from the journey.", size: 21, color: "222222" })
]}));

// ============================================================
// SECTION 04 — SAMPLE CURRICULUM: SESSION 1 (Participant Guide)
// ============================================================
children.push(...sectionTitle("04", "Sample Curriculum \u2014 Session 1"));
children.push(body([
  new TextRun({ text: "What follows is a complete participant-guide spread for Session 1, built in the proven small-group format. Sessions 2\u20136 drop into the same shell with theme-specific stories, tools, and assessments.", italics: true, size: 21, color: GREY })
], { after: 200 }));

// Session header block
children.push(new Paragraph({ spacing: { after: 20 }, children: [
  new TextRun({ text: "PARTICIPANT GUIDE \u00B7 SESSION 1", bold: true, color: GOLD, size: 20, characterSpacing: 40 })
]}));
children.push(new Paragraph({ spacing: { after: 10 }, children: [new TextRun({ text: "When God Owns It All", bold: true, color: NAVY, size: 40 })] }));
children.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "Honor \u00B7 The Freedom of Surrender", bold: true, color: NAVY2, size: 24 })] }));
children.push(goldRule(160));
children.push(verseCallout("Theme Verse \u00B7 Job 1:21", "The Lord gave and the Lord has taken away; may the name of the Lord be praised."));
children.push(spacer(100));
children.push(leadIn("Big Idea.", "When ownership transfers to God, anxiety transfers off of you. Financial wisdom doesn\u2019t begin with behavior \u2014 it begins with belief. Everything changes when you stop carrying what God never asked you to own."));

// WELCOME
children.push(h3("Welcome"));
children.push(body("Over the next six weeks we will talk about something most of us carry quietly and rarely say out loud: money, and what it does to our hearts. This is not a class where anyone gets graded, and no one will ever be asked how much you make, owe, give, or have saved. What we are really after is deeper than numbers \u2014 we are asking who owns our lives, and what changes when we answer that honestly. Wherever you are, whether money feels under control or like a weight you carry, you are in the right room."));
children.push(leadIn("Opening Prayer.", "\u201CFather, thank You for everyone who chose to be here. Some of us come carrying stress about money, and some of us come curious \u2014 and You welcome all of it. Quiet the part of us that wants to perform or hide. Teach us something real about who You are and who we are. We\u2019re listening. Amen.\u201D"));
children.push(leadIn("Icebreaker.", "What is the first thing you remember saving up to buy as a kid \u2014 and how did it feel when you finally got it?"));

// OPENING STORY
children.push(h3("Opening Story"));
children.push(body("Three stories, all on this week\u2019s theme of ownership. Your host will read one aloud; the other two are here to read on your own this week."));
children.push(new Paragraph({ spacing: { before: 60, after: 40 }, children: [new TextRun({ text: "Option 1 \u2014 The Open Hand", bold: true, color: NAVY, size: 21 })] }));
children.push(body("A retired tradesman who had never earned a large salary surprised his family late in life: there was far more set aside than anyone expected. Asked how, he shrugged and said two things. \u201CI never spent everything I had \u2014 and God always came through.\u201D He told of a winter early in his marriage when rent was due and the cupboard was thin, and a job he\u2019d written off as lost came through the very week he needed it. He spent the next forty years the same way \u2014 holding what he had loosely, managing it carefully, and trusting God with the rest. He had settled the ownership question early, and returned to that same answer every time a decision came up."));
children.push(new Paragraph({ spacing: { before: 60, after: 40 }, children: [new TextRun({ text: "Option 2 \u2014 The Church That Hit Pause", bold: true, color: NAVY, size: 21 })] }));
children.push(body("A pastor watched a hard season blindside families in his church \u2014 not careless people, just people who had never been discipled around money. He realized the church owed them two things at once: real help and real discipleship. So they slowed down, paused much of the calendar, and walked the whole congregation through a focused journey on a biblical view of money and how to steward it. What began as a response to a crisis became a rhythm they returned to every year \u2014 because it taught people to hold everything as God\u2019s before they ever tried to manage anything as their own."));
children.push(new Paragraph({ spacing: { before: 60, after: 40 }, children: [new TextRun({ text: "Option 3 \u2014 A Different Kind of Prayer (case study)", bold: true, color: NAVY, size: 21 })] }));
children.push(body("A couple weighing a stressful decision \u2014 a job offer that meant uprooting their family \u2014 had been praying about it for weeks, mostly asking God to protect what they\u2019d built. One night they prayed differently. Instead of asking God to guard what was theirs, they thanked Him that it was already His, and asked what He wanted them to do with it. Nothing in their bank account changed that night. Everything else did. The decision they\u2019d been wrestling with suddenly had an obvious answer, once they stopped asking how to protect what was theirs and started asking what the Owner wanted done with it."));

// WATCH
children.push(h3("Watch \u2014 The Owner Shift", { before: 220 }));
children.push(body("As you watch, listen for the difference between owning and stewarding, and for the practices that make surrender a daily posture rather than a one-time decision. Fill in the blanks as you go."));
const blanks = [
  "Financial wisdom begins with ____________, not behavior.",
  "God is the ____________; I am the ____________.",
  "I don\u2019t give God ownership \u2014 He already owns it all. What changes is my ____________.",
  "An owner manages money out of ____________. A steward manages it out of ____________.",
  "The first act of financial health is not a budget \u2014 it is ____________."
];
blanks.forEach(b => children.push(new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: b, size: 22, color: "222222" })] })));
children.push(new Paragraph({ spacing: { before: 60, after: 50 }, children: [new TextRun({ text: "Four Practices of a Steward", bold: true, color: NAVY, size: 21 })] }));
children.push(numbered("Acknowledge God\u2019s ownership daily. Begin each morning: \u201CLord, all I have is Yours. Show me how to manage it today.\u201D", "practices"));
children.push(numbered("Hold your plans with open hands. When something changes, don\u2019t only ask \u201Cwhy, God?\u201D \u2014 ask \u201Cwhat are You teaching me?\u201D", "practices"));
children.push(numbered("Give God the first and the best. Returning the first portion isn\u2019t obligation \u2014 it\u2019s a declaration that He is Owner and you are manager.", "practices"));
children.push(numbered("See your records as worship, not worry. A spending plan isn\u2019t a control document \u2014 it\u2019s a way to see whether your money is following your faith.", "practices"));

// TABLE DISCUSSION
children.push(h3("Table Discussion", { before: 220 }));
const disc = [
  "When you hear the phrase \u201CGod owns it all,\u201D what is your honest first reaction \u2014 comfort, resistance, confusion, something else?",
  "What is the practical difference between God fixing our numbers and God forming our hearts?",
  "Read Job 1:21 slowly. What would it look like to borrow Job\u2019s posture \u2014 blessing God\u2019s name \u2014 with something you\u2019re holding tightly right now?",
  "Where do you most feel the \u201Cweight of ownership\u201D \u2014 the sense that every outcome rests on you \u2014 in this season?",
  "Think about how differently you treat something you own versus something you\u2019ve borrowed. Where might that same difference show up in how you handle money?",
  "Without sharing any numbers, what is one belief about money you think you inherited from your family?",
  "What is one specific thing \u2014 not a category \u2014 that you tend to hold tightly as \u201Cmine\u201D? What might open hands look like with that one thing this week?"
];
disc.forEach(q => children.push(numbered(q, "discuss")));

// SCRIPTURE REFLECTION
children.push(h3("Scripture Reflection", { before: 220 }));
children.push(leadIn("Psalm 24:1.", "\u201CThe earth is the Lord\u2019s, and everything in it.\u201D If you took the word everything at face value with your own finances, what would change first?"));
children.push(leadIn("Deuteronomy 8:17\u201318.", "Scripture warns against \u201Cmy power and the strength of my hands.\u201D Where are you most tempted to say I built this?"));
children.push(leadIn("Luke 16:11.", "Why do you think Jesus treats how we handle money as a test of trust, rather than just a practical matter?"));

// FINANCIAL WISDOM TOOL
children.push(h3("Financial Wisdom Tool \u2014 The Owner-to-Steward Audit", { before: 220 }));
children.push(body("Do this quietly on your own (about 10 minutes). You will not be asked to read it aloud. In the first column, list four or five things you most often think of as \u201Cmine.\u201D In the second, name the pressure or worry that comes when you carry it as the owner. In the third, write what would change if you managed it for God instead."));
const auditHeader = new TableRow({ tableHeader: true, children: [
  hCell("What I treat as \u201Cmine\u201D", 3120),
  hCell("The pressure I feel as owner", 3120),
  hCell("What changes if I steward it for God", 3120)
]});
const auditRows = ["", "", "", ""].map(() => new TableRow({ children: [
  tCell(new Paragraph({ spacing: { before: 60, after: 60 }, children: [new TextRun("")] }), 3120),
  tCell(new Paragraph({ children: [new TextRun("")] }), 3120),
  tCell(new Paragraph({ children: [new TextRun("")] }), 3120)
]}));
children.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [3120, 3120, 3120], borders: tableBorders, rows: [auditHeader, ...auditRows] }));
children.push(new Paragraph({ spacing: { before: 120, after: 140 }, children: [
  new TextRun({ text: "Then circle the one with the tightest grip and finish this sentence: ", size: 22, color: "222222" }),
  new TextRun({ text: "\u201CIf this really belongs to God and not to me, then one thing that would change is \u2026\u201D", italics: true, size: 22, color: NAVY })
]}));

// PERSONAL ASSESSMENT
children.push(h3("Personal Assessment \u2014 Where Am I With Ownership?", { before: 200 }));
children.push(body("Private; not shared. Rate each statement from 1 (not true of me) to 5 (very true of me)."));
const assessItems = [
  "I genuinely believe everything I have belongs to God, and it shows in how I handle money.",
  "When an unexpected expense or a market drop hits, I can stay at peace.",
  "I make financial decisions by asking what the Owner wants, not only what protects me.",
  "I hold my plans for the future with open hands.",
  "My everyday money habits match what I say I believe about God\u2019s ownership."
];
assessItems.forEach(a => children.push(new Paragraph({
  numbering: { reference: "assess", level: 0 }, spacing: { after: 70 },
  children: [new TextRun({ text: a + "   ", size: 22, color: "222222" }), new TextRun({ text: "_____", color: GOLD, size: 22, bold: true })]
})));
children.push(body("Wherever you land, this is an invitation, not a verdict. Notice the one statement with your lowest number \u2014 that is a good place to let God work this week.", { after: 140 }));

// THIS WEEK'S PRACTICE
children.push(h3("This Week\u2019s Practice", { before: 200 }));
children.push(body("Each morning this week, before you look at your phone, say out loud: \u201CLord, all I have is Yours. Show me how to manage it today.\u201D Then pick one specific thing you\u2019ve been gripping, and tell one person you\u2019re choosing to hold it more loosely because it belongs to God. Small, daily, and honest."));
children.push(leadIn("Memory Verse.", "Job 1:21 \u2014 \u201CThe Lord gave and the Lord has taken away; may the name of the Lord be praised.\u201D"));

// PRAYER
children.push(h3("Prayer"));
children.push(body("Share one thing you\u2019d like the group to pray about this week \u2014 it doesn\u2019t have to relate to money. Write the requests down so you can pray for one another between meetings."));
children.push(body([new TextRun({ text: "Close together: ", bold: true, color: NAVY, size: 22 }), new TextRun({ text: "\u201CFather, You own it all \u2014 the income, the savings, the home, the plans, even the parts of our lives we forget to mention. We confess we often hold these things as if everything depends on us. Teach us to be faithful managers instead of anxious owners, and replace the weight we\u2019ve carried with the freedom of trusting You. Start that work in each of us this week. Amen.\u201D", italics: true, size: 22, color: "333333" })]));

// SEVEN-DAY DEVOTIONAL
children.push(h3("Seven-Day Devotional", { before: 200 }));
children.push(body("A companion to this session \u2014 one short reading each day this week, drawn from the Honor week of the 40-day journey."));
const dev = [
  ["Day 1 \u2014 The Owner of Everything", "Psalm 24:1", "Name three things today that came from God\u2019s hand. What changes if you hold them as a manager?"],
  ["Day 2 \u2014 The Illusion of Ownership", "Deuteronomy 8:17\u201318", "Where are you most tempted to say \u201CI built this\u201D? What would gratitude say instead?"],
  ["Day 3 \u2014 The Transfer of Ownership", "Luke 16:11", "What financial decision are you gripping? What would it look like to hold it with open hands?"],
  ["Day 4 \u2014 The Stewardship Mandate", "1 Corinthians 4:2", "The standard for a steward is faithfulness, not results. How does that reframe the pressure you feel?"],
  ["Day 5 \u2014 Every Decision Is Spiritual", "Luke 16:10", "Where is one small place you can be faithful this week, trusting small faithfulness forms the larger pattern?"],
  ["Day 6 \u2014 God as Provider", "Matthew 6:31\u201333", "When anxiety about provision shows up, what is your first instinct \u2014 and what does it reveal about where you look for security?"],
  ["Day 7 \u2014 The Surrendered Life", "Proverbs 3:5\u20136", "Surrender is a daily posture, not a one-time event. What is one thing you can re-surrender today?"]
];
dev.forEach(d => children.push(new Paragraph({ spacing: { after: 100, line: 276 }, children: [
  new TextRun({ text: d[0] + ".  ", bold: true, color: NAVY, size: 21 }),
  new TextRun({ text: d[1] + " \u2014 ", italics: true, color: GOLD, size: 20 }),
  new TextRun({ text: d[2], size: 21, color: "222222" })
]})));

// FAMILY CONVERSATION
children.push(h3("Family Conversation", { before: 200 }));
children.push(bullet("If everything we have is really on loan from God, what is one thing we might do differently as a family?", "family"));
children.push(bullet("What is something we\u2019re grateful for right now that we didn\u2019t earn or create?", "family"));
children.push(bullet("Is there anything we\u2019ve been holding too tightly that we could practice holding with open hands together?", "family"));

// ============================================================
// DOCUMENT ASSEMBLY
// ============================================================
const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  numbering: { config: [
    { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT, style: { run: { color: GOLD }, paragraph: { indent: { left: 460, hanging: 260 } } } }] },
    { reference: "practices", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { run: { color: NAVY, bold: true }, paragraph: { indent: { left: 460, hanging: 300 } } } }] },
    { reference: "discuss", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { run: { color: GOLD, bold: true }, paragraph: { indent: { left: 460, hanging: 300 } } } }] },
    { reference: "assess", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { run: { color: NAVY, bold: true }, paragraph: { indent: { left: 460, hanging: 300 } } } }] },
    { reference: "family", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT, style: { run: { color: GOLD }, paragraph: { indent: { left: 460, hanging: 260 } } } }] }
  ]},
  sections: [{
    properties: { titlePage: true, page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    headers: {
      first: new Header({ children: [new Paragraph({ children: [] })] }),
      default: new Header({ children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
      spacing: { after: 0 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
      children: [
        new TextRun({ text: "WISDOM CHANGES EVERYTHING", color: NAVY2, size: 15, characterSpacing: 30 }),
        new TextRun({ text: "\tCurriculum Proposal", color: GREY, size: 15 })
      ]
    })] }) },
    footers: {
      first: new Footer({ children: [new Paragraph({ children: [] })] }),
      default: new Footer({ children: [new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 40 },
      children: [
        new TextRun({ text: "Ron Blue Institute  \u00B7  Financial Wisdom Ministry  \u00B7  ", color: GREY, size: 15 }),
        new TextRun({ children: [PageNumber.CURRENT], color: GREY, size: 15 })
      ]
    })] }) },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("/home/claude/Wisdom_Changes_Everything_Proposal.docx", buf);
  console.log("WROTE docx. total blocks:", children.length);
});

