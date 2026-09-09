const docx = require('docx');
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, PageBreak, TabStopType
} = docx;
const { sessions } = require('./content.js');
const { more } = require('./sessions2to6.js');
const allSessions = sessions.concat(more);

const FIVE_FS = "FAMILY (immediate or extended) · FRIENDS · FAMILIAR (neighbors, kids' sports, school) · FIRM (work) · FUN (gym, hobbies, hangouts)";
const CONTENT_W = 9360; // letter, 1in margins

// ---------- palette ----------
const INK = "1A2A33";
const ACCENT = "1F5E5B";     // deep teal
const RULE = "9BB7B0";
const SHADE = "EAF1EF";

// ---------- helpers ----------
function spacer(size) { return new Paragraph({ spacing: { after: size || 120 }, children: [] }); }

function sectionHeading(text) {
  return new Paragraph({
    spacing: { before: 260, after: 120 },
    border: { bottom: { color: RULE, space: 4, style: BorderStyle.SINGLE, size: 6 } },
    children: [new TextRun({ text, bold: true, color: ACCENT, size: 24, allCaps: true, font: "Calibri" })]
  });
}

function bodyPara(text, opts = {}) {
  return new Paragraph({
    spacing: { after: opts.after != null ? opts.after : 140, line: 276 },
    alignment: opts.align || AlignmentType.LEFT,
    children: [new TextRun({ text, italics: !!opts.italics, bold: !!opts.bold, color: opts.color || INK, size: opts.size || 21, font: "Calibri" })]
  });
}

function leadLine(text) {
  return new Paragraph({
    spacing: { after: 100, line: 276 },
    children: [new TextRun({ text, bold: true, color: INK, size: 21, font: "Calibri" })]
  });
}

// numbered item (manual numbering for reliability across many restarting lists)
function numItem(i, text, indent) {
  return new Paragraph({
    spacing: { after: 90, line: 268 },
    indent: { left: 360, hanging: 300 },
    children: [
      new TextRun({ text: i + ". ", bold: true, color: ACCENT, size: 21, font: "Calibri" }),
      new TextRun({ text, color: INK, size: 21, font: "Calibri" })
    ]
  });
}

// named practice: bold lead + explanation, numbered
function practiceItem(i, name, expl) {
  return new Paragraph({
    spacing: { after: 100, line: 268 },
    indent: { left: 360, hanging: 300 },
    children: [
      new TextRun({ text: i + ". ", bold: true, color: ACCENT, size: 21, font: "Calibri" }),
      new TextRun({ text: name + " ", bold: true, color: INK, size: 21, font: "Calibri" }),
      new TextRun({ text: expl, color: INK, size: 21, font: "Calibri" })
    ]
  });
}

// plain line (building values)
function plainLine(text) {
  return new Paragraph({
    spacing: { after: 60, line: 268 },
    indent: { left: 240 },
    children: [new TextRun({ text, color: INK, size: 21, font: "Calibri" })]
  });
}

function blankLine(i, text) {
  return new Paragraph({
    spacing: { after: 110, line: 276 },
    indent: { left: 360, hanging: 300 },
    children: [
      new TextRun({ text: i + ". ", bold: true, color: ACCENT, size: 21, font: "Calibri" }),
      new TextRun({ text, color: INK, size: 21, font: "Calibri" })
    ]
  });
}

// table builder
function buildTable(headers, rows) {
  const nCols = headers.length;
  const colW = Math.floor(CONTENT_W / nCols);
  const widths = headers.map((_, i) => (i === nCols - 1 ? CONTENT_W - colW * (nCols - 1) : colW));
  const border = { style: BorderStyle.SINGLE, size: 4, color: RULE };
  const cellBorders = { top: border, bottom: border, left: border, right: border };
  const headerRow = new TableRow({
    tableHeader: true,
    children: headers.map((h, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: ACCENT },
      margins: { top: 60, bottom: 60, left: 90, right: 90 },
      borders: cellBorders,
      children: [new Paragraph({ children: [new TextRun({ text: h, bold: true, color: "FFFFFF", size: 19, font: "Calibri" })] })]
    }))
  });
  const bodyRows = rows.map((r, ri) => new TableRow({
    children: r.map((c, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: ri % 2 === 1 ? { type: ShadingType.CLEAR, fill: SHADE } : undefined,
      margins: { top: 70, bottom: 70, left: 90, right: 90 },
      borders: cellBorders,
      children: [new Paragraph({ children: [new TextRun({ text: c || " ", color: INK, size: 19, font: "Calibri" })] })]
    }))
  }));
  return new Table({
    columnWidths: widths,
    width: { size: CONTENT_W, type: WidthType.DXA },
    rows: [headerRow, ...bodyRows]
  });
}

function pullQuote(text) {
  return new Paragraph({
    spacing: { before: 120, after: 160, line: 288 },
    indent: { left: 360, right: 360 },
    border: { left: { color: ACCENT, space: 12, style: BorderStyle.SINGLE, size: 18 } },
    children: [new TextRun({ text: "\u201C" + text.replace(/^"|"$/g, '') + "\u201D", italics: true, color: ACCENT, size: 22, font: "Calibri" })]
  });
}

function checkboxDay(day) {
  const [title, subtitle, ref, verse, respond] = day;
  return new Paragraph({
    spacing: { after: 130, line: 272 },
    indent: { left: 360, hanging: 300 },
    children: [
      new TextRun({ text: "\u2610  ", size: 21, font: "Calibri", color: ACCENT }),
      new TextRun({ text: title + " ", bold: true, color: INK, size: 21, font: "Calibri" }),
      new TextRun({ text: subtitle + " ", italics: true, color: INK, size: 21, font: "Calibri" }),
      new TextRun({ text: ref + " ", color: INK, size: 21, font: "Calibri" }),
      new TextRun({ text: verse + " ", color: "4A5A62", size: 20, font: "Calibri" }),
      new TextRun({ text: "RESPOND: ", bold: true, color: ACCENT, size: 20, font: "Calibri" }),
      new TextRun({ text: respond, color: INK, size: 20, font: "Calibri" })
    ]
  });
}

// ---------- session renderer ----------
function renderSession(s) {
  const el = [];
  // header (3 lines)
  el.push(new Paragraph({ spacing: { before: 0, after: 40 }, pageBreakBefore: true,
    children: [new TextRun({ text: `PARTICIPANT GUIDE \u00B7 SESSION ${s.n}`, bold: true, color: ACCENT, size: 20, allCaps: true, font: "Calibri" })] }));
  el.push(new Paragraph({ spacing: { after: 20 },
    children: [new TextRun({ text: s.question, bold: true, color: INK, size: 40, font: "Calibri" })] }));
  el.push(new Paragraph({ spacing: { after: 160 },
    children: [new TextRun({ text: s.subtitle, italics: true, color: "4A5A62", size: 26, font: "Calibri" })] }));

  // memory verse
  el.push(sectionHeading("Memory Verse"));
  el.push(new Paragraph({ spacing: { after: 40, line: 288 }, indent: { left: 240, right: 240 },
    children: [new TextRun({ text: "\u201C" + s.memoryVerse + "\u201D", italics: true, color: INK, size: 22, font: "Calibri" })] }));
  el.push(new Paragraph({ spacing: { after: 80 }, indent: { left: 240 },
    children: [new TextRun({ text: s.memoryRef, bold: true, color: ACCENT, size: 20, allCaps: true, font: "Calibri" })] }));

  // introduction
  el.push(sectionHeading("Introduction"));
  el.push(bodyPara(s.intro));

  // opening story
  el.push(sectionHeading("Opening Story"));
  el.push(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: s.story.label, bold: true, color: INK, size: 22, font: "Calibri" })] }));
  el.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: s.story.subtitle, color: ACCENT, size: 18, allCaps: true, bold: true, font: "Calibri" })] }));
  s.story.paras.forEach(p => el.push(bodyPara(p)));
  el.push(pullQuote(s.story.quote));

  // come together
  el.push(sectionHeading("Come Together"));
  el.push(leadLine("Open your group with prayer."));
  el.push(bodyPara(s.comeTogether.prayerPara));
  el.push(bodyPara(s.comeTogether.tonePara));
  el.push(leadLine("Discuss"));
  s.comeTogether.discuss.forEach((q, i) => el.push(numItem(i + 1, q)));

  // building (S1 only)
  if (s.building) {
    el.push(sectionHeading("Building a Healthy Group Culture"));
    el.push(leadLine(s.building.lead));
    el.push(bodyPara(s.building.intro));
    s.building.values.forEach(v => el.push(plainLine(v)));
    el.push(spacer(60));
    el.push(bodyPara(s.building.closing));
  }

  // learn together
  el.push(sectionHeading("Learn Together"));
  el.push(leadLine(`Watch the Session ${s.n} teaching video.`));
  el.push(bodyPara(s.learn.listenPara));
  el.push(leadLine("Fill in the blanks as you watch."));
  s.learn.blanks.forEach((b, i) => el.push(blankLine(i + 1, b)));
  el.push(new Paragraph({ spacing: { before: 60, after: 140 }, children: [new TextRun({ text: "[space for notes]", italics: true, color: "4A5A62", size: 20, font: "Calibri" })] }));

  // grow together
  el.push(sectionHeading("Grow Together"));
  el.push(leadLine("As a group, talk through the following questions."));
  s.grow.questions.forEach((q, i) => el.push(numItem(i + 1, q)));
  el.push(spacer(60));
  el.push(bodyPara(s.grow.practicesLead, { bold: true, after: 100 }));
  s.grow.practices.forEach((p, i) => el.push(practiceItem(i + 1, p[0], p[1])));
  el.push(bodyPara(s.grow.mostAbsent, { after: 140 }));

  // financial wisdom exercise
  el.push(sectionHeading("Financial Wisdom Exercise"));
  el.push(new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: s.exercise.name, bold: true, color: INK, size: 22, font: "Calibri" })] }));
  el.push(bodyPara(s.exercise.quietLine, { italics: true }));
  el.push(bodyPara(s.exercise.instructions));
  el.push(buildTable(s.exercise.table.headers, s.exercise.table.rows));
  el.push(spacer(100));
  el.push(bodyPara(s.exercise.circleLine));
  el.push(new Paragraph({ spacing: { after: 140, line: 276 }, indent: { left: 240 }, children: [new TextRun({ text: s.exercise.finishSentence, italics: true, color: INK, size: 21, font: "Calibri" })] }));
  el.push(new Paragraph({ spacing: { after: 140, line: 276 },
    children: [
      new TextRun({ text: s.exercise.selfCheck.split('(private)')[0] + "(private)", bold: true, color: INK, size: 21, font: "Calibri" }),
      new TextRun({ text: s.exercise.selfCheck.split('(private)')[1], color: INK, size: 21, font: "Calibri" })
    ] }));

  // circles of life
  el.push(sectionHeading("Circles of Life"));
  el.push(bodyPara("Who else would enjoy or benefit from this group? Financial wisdom is something almost everyone wrestles with and almost no one talks about out loud, so there may be people in your life quietly hoping for a place like this. Look at the circles below and write down two or three names. Then commit to praying about inviting them over the next couple of weeks, and share your list so the group can pray too."));
  el.push(new Paragraph({ spacing: { after: 140 }, children: [new TextRun({ text: FIVE_FS, color: ACCENT, size: 19, bold: true, font: "Calibri" })] }));

  // next steps
  el.push(sectionHeading("Next Steps"));
  el.push(leadLine("Carry the session into your week."));
  s.nextSteps.forEach((n, i) => el.push(numItem(i + 1, n)));

  // family conversation
  el.push(sectionHeading("Family Conversation"));
  el.push(bodyPara(s.family.intro));
  s.family.questions.forEach((q, i) => el.push(numItem(i + 1, q)));

  // going deeper
  el.push(sectionHeading("Going Deeper"));
  el.push(bodyPara("If you have time and your group wants to go further into Scripture on this week's theme, use these. You can do them together or on your own during the week."));
  s.goingDeeper.reads.forEach(r => {
    el.push(new Paragraph({ spacing: { before: 60, after: 80 }, children: [new TextRun({ text: r.ref, bold: true, color: ACCENT, size: 21, allCaps: true, font: "Calibri" })] }));
    r.qs.forEach((q, i) => el.push(numItem(i + 1, q)));
  });

  // devotional readings
  el.push(sectionHeading("This Week's Devotional Readings"));
  el.push(new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: s.readings.weekHeader, bold: true, color: INK, size: 22, allCaps: true, font: "Calibri" })] }));
  el.push(bodyPara("From the Master Your Money devotional. Read one each day, and check them off as you go. Scan each day's code for a short video from Ron.", { after: 140 }));
  s.readings.days.forEach(d => el.push(checkboxDay(d)));

  // close in prayer
  el.push(sectionHeading("Close in Prayer"));
  el.push(bodyPara(s.close.p1));
  el.push(bodyPara(s.close.p2));

  return el;
}

module.exports = {
  renderSession, allSessions,
  helpers: { spacer, sectionHeading, bodyPara, leadLine, numItem, plainLine, buildTable, pullQuote, checkboxDay, INK, ACCENT, RULE, SHADE, CONTENT_W },
  docx
};
