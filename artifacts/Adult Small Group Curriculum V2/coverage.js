const docx = require('docx');
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, ShadingType, Footer
} = docx;

const INK = "1A2A33", ACCENT = "1F5E5B", RULE = "9BB7B0", SHADE = "EAF1EF", MUTE = "4A5A62";
const CW = 9360;

function P(text, o = {}) {
  return new Paragraph({ spacing: { after: o.after != null ? o.after : 100, line: 260 }, alignment: o.align || AlignmentType.LEFT,
    children: [new TextRun({ text, bold: !!o.bold, italics: !!o.italics, color: o.color || INK, size: o.size || 19, font: "Calibri" })] });
}
function H(text) {
  return new Paragraph({ spacing: { before: 160, after: 80 }, border: { bottom: { color: RULE, space: 3, style: BorderStyle.SINGLE, size: 6 } },
    children: [new TextRun({ text, bold: true, color: ACCENT, size: 20, allCaps: true, font: "Calibri" })] });
}
function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.w, type: WidthType.DXA },
    shading: opts.fill ? { type: ShadingType.CLEAR, fill: opts.fill } : undefined,
    margins: { top: 50, bottom: 50, left: 80, right: 80 },
    borders: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE }, left: { style: BorderStyle.SINGLE, size: 4, color: RULE }, right: { style: BorderStyle.SINGLE, size: 4, color: RULE } },
    children: [new Paragraph({ children: [new TextRun({ text, bold: !!opts.bold, color: opts.color || INK, size: opts.size || 17, font: "Calibri" })] })]
  });
}
function tbl(headers, rows, widths) {
  const hr = new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, { w: widths[i], fill: ACCENT, color: "FFFFFF", bold: true })) });
  const br = rows.map((r, ri) => new TableRow({ children: r.map((c, i) => cell(c, { w: widths[i], fill: ri % 2 ? SHADE : undefined, bold: i === 0, color: i === 0 ? INK : (typeof c === 'string' && /omitted|light/i.test(c) ? MUTE : INK) })) }));
  return new Table({ columnWidths: widths, width: { size: CW, type: WidthType.DXA }, rows: [hr, ...br] });
}

const kids = [];

// Title
kids.push(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: "MASTER YOUR MONEY", bold: true, color: ACCENT, size: 30, font: "Calibri" })] }));
kids.push(new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: "Book-to-Curriculum Coverage Map", color: INK, size: 24, font: "Calibri" })] }));
kids.push(new Paragraph({ spacing: { after: 120 }, border: { bottom: { color: ACCENT, space: 2, style: BorderStyle.SINGLE, size: 10 } },
  children: [new TextRun({ text: "How the six-session adult curriculum traces to Ron Blue's Master Your Money and the 42-day devotional", italics: true, color: MUTE, size: 18, font: "Calibri" })] }));

// Principles
kids.push(H("The two principles lists — both fully covered"));
kids.push(P("The book's chapter 2 names four theological principles. Ron's teaching also names five practical principles. The curriculum carries both, in full.", { size: 18, after: 80 }));
kids.push(tbl(
  ["Principles list (source)", "The principles", "In the curriculum"],
  [
    ["Four Biblical Principles (book, ch. 2)", "God owns it all · a growth process · faithfulness over amount · faith requires action", "4 of 4 — Session 1 and devotional Week 1 (Days 1, 3, 4, 5)"],
    ["Five Practical Principles (Ron's teaching)", "Spend less than you earn · avoid debt · give generously · plan for margin · set long-term goals", "5 of 5 — Session 2 practices block"]
  ],
  [2900, 3760, 2700]
));

// Chapter coverage
kids.push(H("The book's 14 chapters — eleven represented"));
kids.push(tbl(
  ["Book chapter", "Where it appears in the curriculum", "Coverage"],
  [
    ["1. Will I Ever Have Enough?", "Session 1 (the \"will I be okay\" question); Session 5 (enough, finish line)", "Full"],
    ["2. Four Biblical Principles", "Session 1; devotional Week 1", "Full"],
    ["3. A Financial Planning Overview", "Session 4", "Full"],
    ["4. Guaranteed Financial Success", "Session 4 (as \"true financial success\" per editorial rule)", "Full"],
    ["5. The Dangers of Debt", "Session 2 (avoid debt); Session 3, Day 18", "Full"],
    ["6. Where Am I?", "Session 4 (Where Am I Map)", "Full"],
    ["7. Setting Faith Financial Goals", "Session 4 (Faith Financial Goals)", "Full"],
    ["8. Avoiding Common Mistakes", "Session 3, Day 19", "Full"],
    ["9. Designing a Personal Financial Plan", "Session 4", "Full"],
    ["10. Control the Flow", "Session 4; devotional Day 28", "Full"],
    ["11. Tax Planning", "Not covered", "Omitted"],
    ["12. Investment Planning", "Session 5 (wise growth, high level only; no sequential-investing mechanics)", "Light"],
    ["13. Stewardship After Death", "Session 6, Day 40 (estate/insurance mechanics not taught)", "Partial"],
    ["14. Giving Living", "Session 6 (generosity)", "Full"]
  ],
  [3000, 4360, 2000]
));

// Exercises
kids.push(H("The exercises — where each one comes from"));
kids.push(P("In every case the worksheet layout is an original, no-numbers construction. What varies is the source of the underlying framework: some are RBI-published, one is decades-established RBI teaching, and one first appears in the MYM videos. Session 4 is the only place an official RBI worksheet maps directly.", { size: 18, after: 80 }));
kids.push(tbl(
  ["Session exercise", "Framework source", "Worksheet layout", "Official RBI worksheet to swap in?"],
  [
    ["S1 · The Steward's First Look", "RBI-published — \"God owns it all,\" book ch. 2", "Original (mine)", "No direct equivalent"],
    ["S2 · The One-Principle Step", "RBI-established — the five principles (Ron's testimony & sermon, decades old)", "Original (mine)", "No direct equivalent"],
    ["S3 · Name Your Rung", "Video-originated — the Freedom Ladder first appears in the MYM videos", "Original (mine)", "No — new to this study"],
    ["S4 · Live / Give / Owe / Grow", "RBI-published — L/G/O/G, Where Am I Map, spending plan, faith goals (book chs. 6, 7, 9, 10)", "Original (mine) — a no-numbers simplification of RBI tools", "Yes — official net-worth and spending-plan tools could be swapped in"],
    ["S5 · Finish Line & Purpose Sentence", "Mixed — \"enough/contentment\" is book ch. 1; the \"finish line\" framing is video-originated", "Original (mine)", "No direct equivalent"],
    ["S6 · Decide in Your Heart", "RBI-published — discerning giving, book ch. 14 \"Giving Living\" (open-hand challenge is a curriculum touch)", "Original (mine)", "No direct equivalent"]
  ],
  [2200, 3560, 1700, 1900]
));

// Notes
kids.push(H("Notes for the client"));
kids.push(new Paragraph({ spacing: { after: 60, line: 258 }, indent: { left: 260, hanging: 200 }, children: [new TextRun({ text: "\u2022  ", color: ACCENT, size: 18 }), new TextRun({ text: "The technical chapters (tax planning, investment mechanics, estate and insurance detail) are intentionally left out. They belong to book-and-advisor territory, not a heart-level small-group format with a no-numbers promise.", color: INK, size: 18, font: "Calibri" })] }));
kids.push(new Paragraph({ spacing: { after: 60, line: 258 }, indent: { left: 260, hanging: 200 }, children: [new TextRun({ text: "\u2022  ", color: ACCENT, size: 18 }), new TextRun({ text: "\"Go deeper\" always routes to the 42-day devotional, not the book, matching the God Owns It All approach.", color: INK, size: 18, font: "Calibri" })] }));
kids.push(new Paragraph({ spacing: { after: 60, line: 258 }, indent: { left: 260, hanging: 200 }, children: [new TextRun({ text: "\u2022  ", color: ACCENT, size: 18 }), new TextRun({ text: "If RBI prefers its official net-worth and spending-plan worksheets in Session 4, they can be swapped in directly.", color: INK, size: 18, font: "Calibri" })] }));

const doc = new Document({
  creator: "Ron Blue Institute",
  title: "Master Your Money — Book-to-Curriculum Coverage Map",
  styles: { default: { document: { run: { font: "Calibri", size: 19, color: INK } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Master Your Money  \u00B7  Book-to-Curriculum Coverage Map  \u00B7  for client review", color: "8A8A8A", size: 15, font: "Calibri" })] })] }) },
    children: kids
  }]
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync('/home/claude/MYM_CoverageMap.docx', buf); console.log('wrote', buf.length); });
