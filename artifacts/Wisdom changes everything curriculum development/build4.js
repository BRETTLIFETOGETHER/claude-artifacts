const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, LevelFormat, TabStopType, HeadingLevel, BorderStyle,
  WidthType, ShadingType, VerticalAlign, PageNumber, Header, Footer,
  HeightRule, PageBreak
} = require("docx");
const { sessions, weeks, devSamples } = require("./content3.js");

// ---- brand tokens (matched to the uploaded deck) ----
const DISPLAY = "Anton";          // heavy condensed display
const COND = "Oswald";            // condensed bold for labels/subheads/table heads
const BODY = "Calibri";           // clean body
const INK = "16242E";             // near-black navy (big headings, body-dark)
const NAVY = "1A5384";            // medium corporate blue (fills)
const NAVY_DK = "123A5C";
const YELLOW = "F4C20D";
const GREYRULE = "D8D8D8";
const TXT = "3A3A3A";
const PANEL = "EEF2F6";
const WHITE = "FFFFFF";

const CW = 10080; // content width with 0.75" L/R margins
const NB = { style: BorderStyle.NONE };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB, insideHorizontal: NB, insideVertical: NB };
const gline = { style: BorderStyle.SINGLE, size: 2, color: GREYRULE };

const run = (t, o = {}) => new TextRun({ text: t, font: o.font || BODY, size: o.size || 21, color: o.color || TXT, bold: o.bold, italics: o.italics, characterSpacing: o.cs });
const para = (kids, o = {}) => new Paragraph({ spacing: { before: o.before || 0, after: o.after != null ? o.after : 120, line: o.line || 280 }, alignment: o.align, indent: o.indent, children: Array.isArray(kids) ? kids : [kids] });
const body = (t, o = {}) => para([run(t, { size: o.size || 21, color: o.color || TXT })], o);
const sp = (h) => new Paragraph({ spacing: { after: h }, children: [run("")] });
const pb = () => new Paragraph({ pageBreakBefore: true, spacing: { after: 0 }, children: [run("")] });

// navy + yellow rule motif (thin two-segment bar)
function ruleMotif() {
  return new Table({
    width: { size: 3400, type: WidthType.DXA }, columnWidths: [950, 2450], borders: noBorders,
    rows: [new TableRow({ cantSplit: true, height: { value: 70, rule: HeightRule.EXACT }, children: [
      new TableCell({ width: { size: 950, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, borders: noBorders, margins: { top: 0, bottom: 0, left: 0, right: 0 }, children: [new Paragraph({ spacing: { after: 0 }, children: [run("", { size: 2 })] })] }),
      new TableCell({ width: { size: 2450, type: WidthType.DXA }, shading: { fill: YELLOW, type: ShadingType.CLEAR }, borders: noBorders, margins: { top: 0, bottom: 0, left: 0, right: 0 }, children: [new Paragraph({ spacing: { after: 0 }, children: [run("", { size: 2 })] })] })
    ]})]
  });
}

const sectionLabel = (t) => new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: t.toUpperCase(), font: COND, bold: true, color: NAVY, size: 22, characterSpacing: 50 })] });
const bigHeading = (lines, o = {}) => { const size = o.size || 58; const lh = Math.round(size * 10.6); return lines.map((ln, i) => new Paragraph({ spacing: { before: i === 0 ? (o.before || 40) : 0, after: i === lines.length - 1 ? 150 : 0, line: lh, lineRule: "exact" }, children: [new TextRun({ text: ln.toUpperCase(), font: DISPLAY, color: o.color || INK, size })] })); };

// keep a block from splitting across pages: wrap in 1x1 cantSplit table
function keepTogether(kids) {
  return new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [CW], borders: noBorders,
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({ width: { size: CW, type: WidthType.DXA }, borders: noBorders, margins: { top: 0, bottom: 0, left: 0, right: 0 }, children: kids })] })] });
}

// full-width color band with optional yellow left accent
function bandFill(kids, o = {}) {
  return new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [CW], borders: noBorders,
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: CW, type: WidthType.DXA }, shading: { fill: o.fill || NAVY, type: ShadingType.CLEAR },
      borders: o.accent ? { left: { style: BorderStyle.SINGLE, size: 26, color: o.accent }, top: NB, bottom: NB, right: NB } : noBorders,
      margins: { top: o.pad || 150, bottom: o.pad || 160, left: 240, right: 200 }, children: kids })] })] });
}

// micro label with grey underline
const micro = (t) => new Paragraph({ spacing: { before: 150, after: 70 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GREYRULE, space: 2 } }, children: [new TextRun({ text: t.toUpperCase(), font: COND, bold: true, color: NAVY, size: 19, characterSpacing: 40 })] });
const leadIn = (label, text, o = {}) => para([new TextRun({ text: label + "  ", font: COND, bold: true, color: INK, size: o.size || 21 }), run(text, { size: o.size || 21 })], { after: o.after != null ? o.after : 100 });

// table cells
const hCell = (t, w, al) => new TableCell({ width: { size: w, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 70, bottom: 70, left: 120, right: 120 }, verticalAlign: VerticalAlign.CENTER, children: [new Paragraph({ alignment: al || AlignmentType.LEFT, spacing: { after: 0 }, children: [new TextRun({ text: t, font: COND, bold: true, color: WHITE, size: 18 })] })] });
const dCell = (kids, w, fill, m) => new TableCell({ width: { size: w, type: WidthType.DXA }, shading: fill ? { fill, type: ShadingType.CLEAR } : undefined, margins: { top: m != null ? m : 60, bottom: m != null ? m : 60, left: 120, right: 120 }, verticalAlign: VerticalAlign.CENTER, children: Array.isArray(kids) ? kids : [kids] });
const cbd = { style: BorderStyle.SINGLE, size: 1, color: "C7CDD6" };
const tBorders = { top: cbd, bottom: cbd, left: cbd, right: cbd, insideHorizontal: cbd, insideVertical: cbd };

// two-column borderless (kept together)
function twoCol(leftKids, rightKids) {
  return new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [4900, 5180], borders: noBorders,
    rows: [new TableRow({ cantSplit: true, children: [
      new TableCell({ width: { size: 4900, type: WidthType.DXA }, borders: noBorders, margins: { top: 0, bottom: 0, left: 0, right: 260 }, children: leftKids }),
      new TableCell({ width: { size: 5180, type: WidthType.DXA }, borders: noBorders, margins: { top: 0, bottom: 0, left: 260, right: 0 }, children: rightKids })
    ]})] });
}
const numLi = (i, text, color) => new Paragraph({ spacing: { after: 80, line: 274 }, indent: { left: 340, hanging: 340 }, children: [new TextRun({ text: i + ".  ", font: COND, bold: true, color: color || NAVY, size: 20 }), run(text, { size: 20 })] });

const children = [];

// =================== COVER ===================
children.push(sp(80));
children.push(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: "RON BLUE INSTITUTE", font: COND, color: NAVY, size: 22, characterSpacing: 40 })] }));
children.push(new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: "FINANCIAL WISDOM ", font: COND, bold: true, color: INK, size: 26 }), new TextRun({ text: "MINISTRY", font: COND, bold: true, color: NAVY, size: 26, characterSpacing: 60 })] }));
children.push(new Paragraph({ spacing: { before: 60, after: 0 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GREYRULE, space: 6 } }, children: [run("", { size: 8 })] }));
children.push(sp(420));
children.push(...bigHeading(["Wisdom", "Changes", "Everything"], { size: 96 }));
children.push(new Paragraph({ spacing: { before: 60, after: 80 }, children: [new TextRun({ text: "40 DAYS OF FINANCIAL WISDOM  \u00B7  CURRICULUM & OUTLINE", font: COND, bold: true, color: NAVY, size: 26, characterSpacing: 30 })] }));
children.push(ruleMotif());
children.push(sp(520));
// navy bottom band
children.push(bandFill([
  new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: "A CURRICULUM FOR THE LOCAL CHURCH", font: COND, bold: true, color: YELLOW, size: 22, characterSpacing: 30 })] }),
  new Paragraph({ spacing: { before: 50, after: 140 }, children: [run("Equipping pastors, families, and small groups to live wisely, give generously, and honor God with all He has entrusted to them.", { color: "DCE6F0", size: 20 })] }),
  // six-H strip inside band
  new Paragraph({ spacing: { after: 0 }, children: [
    new TextRun({ text: "HONOR", font: COND, bold: true, color: WHITE, size: 20 }), new TextRun({ text: "   \u2192   ", color: YELLOW, size: 18 }),
    new TextRun({ text: "HEART", font: COND, bold: true, color: WHITE, size: 20 }), new TextRun({ text: "   \u2192   ", color: YELLOW, size: 18 }),
    new TextRun({ text: "HABITS", font: COND, bold: true, color: WHITE, size: 20 }), new TextRun({ text: "   \u2192   ", color: YELLOW, size: 18 }),
    new TextRun({ text: "HEALTH", font: COND, bold: true, color: WHITE, size: 20 }), new TextRun({ text: "   \u2192   ", color: YELLOW, size: 18 }),
    new TextRun({ text: "HOPE", font: COND, bold: true, color: WHITE, size: 20 }), new TextRun({ text: "   \u2192   ", color: YELLOW, size: 18 }),
    new TextRun({ text: "HARVEST", font: COND, bold: true, color: WHITE, size: 20 })
  ]}),
  new Paragraph({ spacing: { before: 160, after: 0 }, children: [new TextRun({ text: "www.financialwisdomministry.com   \u00B7   (949) 842-4752", color: "DCE6F0", size: 18 })] })
], { pad: 220 }));

// =================== OVERVIEW ===================
children.push(pb());
children.push(sectionLabel("The Curriculum"));
children.push(...bigHeading(["Overview"]));
children.push(ruleMotif());
children.push(sp(120));
children.push(body("Most of us were never discipled about money. We were taught to pray, to read Scripture, to serve \u2014 but when it came to the one subject Jesus spoke about more than heaven and hell combined, the church often went quiet."));
children.push(body("Wisdom Changes Everything is a different invitation. Not a budgeting class and not a giving campaign, but six weeks of letting God\u2019s wisdom reshape how we hold money, possessions, and ultimately our whole lives \u2014 heart, habits, home, hope, and harvest. It is built for the family that is struggling and the family that is doing well, because both need wisdom and both can drift."));
children.push(body("The conviction underneath it is the one Ron Blue has spent a lifetime teaching \u2014 God owns it all. When that single question is settled, everything downstream reorganizes around a different center. One promise shapes the whole journey: no one is ever asked how much they make, owe, give, or have saved. Dignity matters more than disclosure.", { after: 200 }));
children.push(keepTogether([bandFill([
  new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: "\u201CTHIS is God\u2019s wisdom. CHANGES is what happens when we trust and obey. EVERYTHING is the whole life He has entrusted to us \u2014 heart, habits, household, finances, generosity, and legacy.\u201D", font: COND, color: WHITE, size: 24, characterSpacing: 10 })] })
], { fill: NAVY, accent: YELLOW, pad: 200 })]));

// =================== SIX MOVEMENTS ===================
children.push(pb());
children.push(sectionLabel("The Journey"));
children.push(...bigHeading(["The Six", "Movements"]));
children.push(ruleMotif());
children.push(sp(140));
const goals = ["Move from control to trust.", "Break the comparison trap.", "Replace confusion with clarity.", "Build margin and reduce anxiety.", "Define enough; trust God\u2019s future.", "Move from maintenance to multiplication."];
sessions.forEach((s, i) => {
  children.push(keepTogether([new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [1150, 8930], borders: noBorders,
    rows: [new TableRow({ cantSplit: true, children: [
      new TableCell({ width: { size: 1150, type: WidthType.DXA }, borders: noBorders, verticalAlign: VerticalAlign.CENTER, margins: { top: 0, bottom: 0, left: 0, right: 0 }, children: [new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: "0" + (i + 1), font: DISPLAY, color: YELLOW, size: 52 })] })] }),
      new TableCell({ width: { size: 8930, type: WidthType.DXA }, borders: noBorders, verticalAlign: VerticalAlign.CENTER, margins: { top: 60, bottom: 60, left: 0, right: 0 }, children: [
        new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: s.h + "  \u00B7  ", font: COND, bold: true, color: NAVY, size: 24 }), new TextRun({ text: s.title, font: COND, bold: true, color: INK, size: 24 }), new TextRun({ text: "   " + s.sub, font: BODY, italics: true, color: "777777", size: 18 })] }),
        new Paragraph({ spacing: { after: 0 }, children: [run(goals[i] + "   Key verse: " + s.verse + ".", { size: 19 })] })
      ]})
    ]})] })]));
  children.push(new Paragraph({ spacing: { after: 60 }, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: GREYRULE, space: 4 } }, children: [run("", { size: 4 })] }));
});

// =================== 40-DAY OUTLINE ===================
function weekBlock(w, wi) {
  const kids = [];
  kids.push(new Paragraph({ spacing: { before: 0, after: 50 }, children: [
    new TextRun({ text: "WEEK " + (wi + 1) + "  \u00B7  " + w.h, font: COND, bold: true, color: NAVY, size: 23 }),
    new TextRun({ text: "   " + w.title, font: COND, bold: true, color: INK, size: 23 }),
    new TextRun({ text: "   \u2014 " + w.focus, font: BODY, italics: true, color: "777777", size: 16 })
  ]}));
  const head = new TableRow({ tableHeader: true, cantSplit: true, children: [hCell("Day", 720, AlignmentType.CENTER), hCell("Title & Subtitle", 6480), hCell("Key Verse", 2880)] });
  const rows = w.days.map((d, i) => new TableRow({ cantSplit: true, children: [
    dCell(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: d[0], font: COND, bold: true, color: NAVY, size: 20 })] }), 720, i % 2 ? "F3F6F9" : WHITE, 44),
    dCell([new Paragraph({ spacing: { after: 2 }, children: [new TextRun({ text: d[1], font: COND, bold: true, color: INK, size: 19 })] }), new Paragraph({ spacing: { after: 0 }, children: [run(d[2], { italics: true, color: "666666", size: 16 })] })], 6480, i % 2 ? "F3F6F9" : WHITE, 44),
    dCell(new Paragraph({ spacing: { after: 0 }, children: [run(d[3], { color: INK, size: 18 })] }), 2880, i % 2 ? "F3F6F9" : WHITE, 44)
  ]}));
  kids.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [720, 6480, 2880], borders: tBorders, rows: [head, ...rows] }));
  return keepTogether(kids);
}
children.push(pb());
children.push(sectionLabel("The Campaign"));
children.push(...bigHeading(["The 40-Day Outline"], { size: 48 }));
children.push(ruleMotif());
children.push(sp(70));
children.push(body("Forty daily readings carry the six movements \u2014 each day mapped to that week\u2019s small-group session.", { after: 120 }));
children.push(weekBlock(weeks[0], 0));
children.push(sp(110));
children.push(weekBlock(weeks[1], 1));
children.push(pb());
children.push(weekBlock(weeks[2], 2));
children.push(sp(110));
children.push(weekBlock(weeks[3], 3));
children.push(pb());
children.push(weekBlock(weeks[4], 4));
children.push(sp(110));
children.push(weekBlock(weeks[5], 5));
children.push(sp(120));
children.push(keepTogether([bandFill([new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: "CELEBRATION SUNDAY  \u2014  ", font: COND, bold: true, color: YELLOW, size: 20 }), run("Testimonies, generosity commitments, and Legacy Letters as the church celebrates stories of transformation.", { color: "DCE6F0", size: 19 })] })], { fill: NAVY, pad: 130 })]));

// =================== CURRICULUM DRAFT DIVIDER ===================
children.push(pb());
children.push(sectionLabel("Most Important"));
children.push(...bigHeading(["The", "Curriculum", "Draft"]));
children.push(ruleMotif());
children.push(sp(140));
children.push(body("Below is the curriculum written, not just outlined \u2014 first a sample of the daily devotional, then a complete small-group session. Each of the forty days and all six sessions follow these same templates.", { after: 200 }));
children.push(keepTogether([new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [4900, 5180], borders: noBorders,
  rows: [new TableRow({ cantSplit: true, children: [
    new TableCell({ width: { size: 4900, type: WidthType.DXA }, shading: { fill: PANEL, type: ShadingType.CLEAR }, borders: { left: { style: BorderStyle.SINGLE, size: 22, color: YELLOW }, top: NB, bottom: NB, right: NB }, margins: { top: 160, bottom: 160, left: 200, right: 200 }, children: [
      new Paragraph({ spacing: { after: 30 }, children: [new TextRun({ text: "01  \u00B7  DAILY DEVOTIONAL", font: COND, bold: true, color: NAVY, size: 22 })] }),
      new Paragraph({ spacing: { after: 0 }, children: [run("A two-to-three-minute reading for each of the 40 days \u2014 title, verse, reflection, and prayer.", { size: 19 })] })
    ]}),
    new TableCell({ width: { size: 280, type: WidthType.DXA }, borders: noBorders, children: [new Paragraph({ children: [run("", { size: 2 })] })] }),
    new TableCell({ width: { size: 5000, type: WidthType.DXA }, shading: { fill: PANEL, type: ShadingType.CLEAR }, borders: { left: { style: BorderStyle.SINGLE, size: 22, color: NAVY }, top: NB, bottom: NB, right: NB }, margins: { top: 160, bottom: 160, left: 200, right: 200 }, children: [
      new Paragraph({ spacing: { after: 30 }, children: [new TextRun({ text: "02  \u00B7  SMALL-GROUP SESSIONS", font: COND, bold: true, color: NAVY, size: 22 })] }),
      new Paragraph({ spacing: { after: 0 }, children: [run("Six 90-minute sessions \u2014 story, teaching, discussion, a hands-on tool, and a weekly practice.", { size: 19 })] })
    ]})
  ]})] })]));

// =================== SAMPLE DEVOTIONAL DAYS ===================
devSamples.forEach(d => {
  children.push(pb());
  children.push(sectionLabel("Sample Daily Devotional"));
  children.push(...bigHeading(["Day " + (d.num.length < 2 ? "0" + d.num : d.num)], { size: 60 }));
  children.push(new Paragraph({ spacing: { after: 8 }, children: [new TextRun({ text: d.title, font: COND, bold: true, color: NAVY, size: 30 })] }));
  children.push(new Paragraph({ spacing: { after: 60 }, children: [run(d.subtitle, { italics: true, color: "666666", size: 21 })] }));
  children.push(ruleMotif());
  children.push(sp(120));
  children.push(keepTogether([bandFill([
    new Paragraph({ spacing: { after: 30 }, children: [new TextRun({ text: "KEY VERSE  \u00B7  " + d.verse, font: COND, bold: true, color: YELLOW, size: 19 })] }),
    new Paragraph({ spacing: { after: 0 }, children: [run("\u201C" + d.verseText + "\u201D", { color: WHITE, italics: true, size: 22 })] })
  ], { fill: NAVY, accent: YELLOW, pad: 170 })]));
  children.push(sp(120));
  children.push(body(d.reading, { size: 22, after: 140 }));
  children.push(leadIn("Reflect.", d.reflect, { size: 22, after: 90 }));
  children.push(para([new TextRun({ text: "Pray.  ", font: COND, bold: true, color: INK, size: 22 }), run("\u201C" + d.pray + "\u201D", { italics: true, color: "444444", size: 22 })]));
});

// =================== FULL SESSIONS ===================
function renderTool(t) {
  const kids = [];
  kids.push(body(t.intro, { after: 110 }));
  if (t.cols) {
    const head = new TableRow({ tableHeader: true, cantSplit: true, children: t.cols.map(c => hCell(c, Math.floor(CW / t.cols.length))) });
    const rows = t.rows.map(r => new TableRow({ cantSplit: true, children: t.cols.map((c, ci) => dCell(new Paragraph({ spacing: { before: 50, after: 50 }, children: [new TextRun({ text: (ci === 0 && typeof r === "string") ? r : "", font: COND, bold: ci === 0, color: INK, size: 18 })] }), Math.floor(CW / t.cols.length))) }));
    kids.push(new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: t.cols.map(() => Math.floor(CW / t.cols.length)), borders: tBorders, rows: [head, ...rows] }));
  }
  if (t.prompts) t.prompts.forEach(p => kids.push(para([new TextRun({ text: "\u25B8  ", color: NAVY, bold: true, size: 21 }), run(p, { size: 21 })], { before: 50, after: 50 })));
  if (t.close) kids.push(para([new TextRun({ text: "Then: ", font: COND, bold: true, color: INK, size: 21 }), run(t.close, { italics: true, color: "444444", size: 21 })], { before: 100 }));
  return keepTogether(kids);
}

sessions.forEach((s, si) => {
  children.push(pb());
  // session band
  children.push(bandFill([
    new Paragraph({ spacing: { after: 22 }, children: [new TextRun({ text: "SESSION " + s.n + "   \u00B7   " + s.h, font: COND, bold: true, color: YELLOW, size: 20, characterSpacing: 30 })] }),
    new Paragraph({ spacing: { after: 14 }, children: [new TextRun({ text: s.title, font: DISPLAY, color: WHITE, size: 46 })] }),
    new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: s.sub, font: COND, color: "CFE0EE", size: 22 })] })
  ], { pad: 190 }));
  children.push(sp(70));
  // verse panel (light) + big idea (navy)
  children.push(keepTogether([new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [CW], borders: noBorders,
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({ width: { size: CW, type: WidthType.DXA }, shading: { fill: PANEL, type: ShadingType.CLEAR }, borders: { left: { style: BorderStyle.SINGLE, size: 22, color: NAVY }, top: NB, bottom: NB, right: NB }, margins: { top: 120, bottom: 120, left: 200, right: 180 }, children: [
      new Paragraph({ spacing: { after: 24 }, children: [new TextRun({ text: "THEME VERSE  \u00B7  " + s.verse, font: COND, bold: true, color: NAVY, size: 18 })] }),
      new Paragraph({ spacing: { after: 0 }, children: [run("\u201C" + s.verseText + "\u201D", { italics: true, color: INK, size: 22 })] })
    ]})]})] })]));
  children.push(sp(70));
  children.push(keepTogether([bandFill([
    new Paragraph({ spacing: { after: 24 }, children: [new TextRun({ text: "BIG IDEA", font: COND, bold: true, color: YELLOW, size: 18 })] }),
    new Paragraph({ spacing: { after: 0 }, children: [run(s.big, { color: WHITE, size: 22 })] })
  ], { fill: NAVY, accent: YELLOW, pad: 150 })]));

  // WELCOME
  children.push(micro("Welcome"));
  children.push(body(s.welcome));
  children.push(leadIn("Opening Prayer.", "\u201C" + s.prayer0 + "\u201D"));
  children.push(leadIn("Icebreaker.", s.icebreaker, { after: 40 }));
  // STORY
  children.push(micro("Opening Story \u2014 " + s.story.title));
  children.push(body(s.story.text, { after: 40 }));
  // WATCH
  children.push(micro("Watch \u2014 Teaching & Fill-in Notes"));
  children.push(body("As you watch, listen for how this week\u2019s truth reshapes the way you hold money. Fill in the blanks.", { after: 80 }));
  s.fillins.forEach(f => children.push(new Paragraph({ spacing: { after: 76 }, children: [new TextRun({ text: "\u2022  ", color: YELLOW, bold: true, size: 22 }), run(f, { size: 21 })] })));
  // DISCUSSION
  children.push(micro("Table Discussion"));
  const half = Math.ceil(s.discuss.length / 2);
  children.push(twoCol(s.discuss.slice(0, half).map((q, i) => numLi(i + 1, q)), s.discuss.slice(half).map((q, i) => numLi(i + 1 + half, q))));
  // REFLECTION
  children.push(micro("Scripture Reflection"));
  s.reflect.forEach(r => children.push(leadIn(r[0] + ".", r[1], { after: 90 })));
  // TOOL
  children.push(micro("Financial Wisdom Tool \u2014 " + s.tool.name));
  children.push(renderTool(s.tool));
  // ASSESSMENT
  children.push(micro("Personal Assessment \u00B7 Private"));
  children.push(body("Not shared. Rate each statement 1 (not true of me) to 5 (very true of me).", { after: 64 }));
  children.push(keepTogether(s.assess.map((a, i) => new Paragraph({ spacing: { after: 60 }, indent: { left: 340, hanging: 340 }, children: [new TextRun({ text: (i + 1) + ".  ", font: COND, bold: true, color: NAVY, size: 20 }), run(a + "   ", { size: 20 }), new TextRun({ text: "_____", bold: true, color: YELLOW, size: 20 })] }))));
  // PRACTICE
  children.push(sp(40));
  children.push(keepTogether([bandFill([
    new Paragraph({ spacing: { after: 22 }, children: [new TextRun({ text: "THIS WEEK\u2019S PRACTICE", font: COND, bold: true, color: NAVY, size: 18 })] }),
    new Paragraph({ spacing: { after: 0 }, children: [run(s.practice, { color: INK, size: 21 })] })
  ], { fill: PANEL, accent: YELLOW, pad: 140 })]));
  // PRAYER + MEMORY
  children.push(micro("Close in Prayer"));
  children.push(para([new TextRun({ text: "Memory Verse \u2014 " + s.verse + ".  ", font: COND, bold: true, color: INK, size: 21 }), run("\u201C" + s.verseText + "\u201D", { italics: true, color: "444444", size: 21 })], { after: 80 }));
  children.push(para([new TextRun({ text: "Together:  ", font: COND, bold: true, color: INK, size: 21 }), run("\u201C" + s.prayer + "\u201D", { italics: true, color: "444444", size: 21 })], { after: 40 }));
  // DEVOTIONAL
  children.push(micro("Seven-Day Devotional"));
  const wk = weeks[si].days;
  const dHalf = Math.ceil(wk.length / 2);
  const devPara = (d) => new Paragraph({ spacing: { after: 86, line: 272 }, children: [new TextRun({ text: "Day " + d[0] + " \u2014 " + d[1] + ".  ", font: COND, bold: true, color: INK, size: 18 }), new TextRun({ text: d[3] + "  ", italics: true, color: NAVY, size: 17 }), run(d[4], { size: 18 })] });
  children.push(twoCol(wk.slice(0, dHalf).map(devPara), wk.slice(dHalf).map(devPara)));
});

// =================== CONCLUSION ===================
children.push(pb());
children.push(sectionLabel("Conclusion"));
children.push(...bigHeading(["Wisdom", "That Changes", "Everything"]));
children.push(ruleMotif());
children.push(sp(140));
children.push(body("When pastors are equipped, families are discipled, and small groups gather around God\u2019s wisdom, generosity flows and the church becomes a center of financial wisdom. This is the heart of Wisdom Changes Everything \u2014 a durable discipleship pathway, not a one-time campaign.", { after: 200 }));
children.push(keepTogether([bandFill([
  new Paragraph({ spacing: { after: 0 }, children: [new TextRun({ text: "\u201CIf the Church truly lived as though God owns it all \u2014 what could happen next?\u201D", font: COND, color: WHITE, size: 26 })] })
], { fill: NAVY, accent: YELLOW, pad: 220 })]));

// =================== ASSEMBLE ===================
const doc = new Document({
  styles: { default: { document: { run: { font: BODY, size: 21, color: TXT } } } },
  sections: [{
    properties: { titlePage: true, page: { size: { width: 12240, height: 15840 }, margin: { top: 1040, right: 1080, bottom: 980, left: 1080 } } },
    headers: {
      first: new Header({ children: [new Paragraph({ children: [] })] }),
      default: new Header({ children: [new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: CW }],
        spacing: { after: 0 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: GREYRULE, space: 6 } },
        children: [
          new TextRun({ text: "RON BLUE INSTITUTE", font: COND, color: NAVY, size: 15, characterSpacing: 30 }),
          new TextRun({ text: "  \u00B7  FINANCIAL WISDOM MINISTRY", font: COND, bold: true, color: INK, size: 15 }),
          new TextRun({ text: "\tWisdom Changes Everything", font: BODY, italics: true, color: "888888", size: 15 })
        ]
      })] })
    },
    footers: {
      first: new Footer({ children: [new Paragraph({ children: [] })] }),
      default: new Footer({ children: [new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: CW }],
        spacing: { before: 40 },
        children: [
          new TextRun({ children: [PageNumber.CURRENT], font: DISPLAY, color: INK, size: 22 }),
          new TextRun({ text: "\tFINANCIAL WISDOM MINISTRY", font: COND, color: "9AA3AD", size: 14, characterSpacing: 20 })
        ]
      })] })
    },
    children
  }]
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync("/home/claude/WCE_Curriculum_Deck.docx", buf); console.log("WROTE. blocks:", children.length); });
