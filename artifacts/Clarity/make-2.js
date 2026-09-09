const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, PageBreak, AlignmentType,
        HeadingLevel, PageOrientation, BorderStyle, Table, TableRow, TableCell,
        WidthType, ShadingType } = d;

const TEAL = "128085";
const SAGE = "4A9459";
const INK  = "002124";
const GREY = "5A6570";
const GOLD = "8A6D2F";

const lines = fs.readFileSync('clarity30.md', 'utf8').split('\n');
const kids = [];

function rule(color, size) {
  return new Paragraph({
    spacing: { before: 60, after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: size || 6, color: color, space: 8 } },
    children: [new TextRun({ text: "" })]
  });
}

function blankLines(n) {
  for (let i = 0; i < n; i++) {
    kids.push(new Paragraph({
      spacing: { before: 160, after: 160 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "C9CFD4", space: 4 } },
      children: [new TextRun({ text: "" })]
    }));
  }
}

function fillLine(label, indent) {
  kids.push(new Paragraph({
    spacing: { before: 180, after: 60 },
    indent: indent ? { left: 360 } : undefined,
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "C9CFD4", space: 6 } },
    children: [new TextRun({ text: label, italics: true, size: 24, color: GREY, font: "Inter" })]
  }));
}

function makeTable(headers, rows) {
  const n = headers.length;
  const total = 9000;
  const w = Math.floor(total / n);
  const widths = new Array(n).fill(w);

  const headRow = new TableRow({
    children: headers.map(h => new TableCell({
      width: { size: w, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: "E7F2F3" },
      margins: { top: 100, bottom: 100, left: 120, right: 120 },
      children: [new Paragraph({ children: [new TextRun({ text: h, bold: true, size: 20, color: INK, font: "Inter" })] })]
    }))
  });

  const bodyRows = [];
  for (let r = 0; r < rows; r++) {
    bodyRows.push(new TableRow({
      children: new Array(n).fill(0).map(() => new TableCell({
        width: { size: w, type: WidthType.DXA },
        margins: { top: 180, bottom: 180, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: "" })] })]
      }))
    }));
  }

  kids.push(new Table({
    columnWidths: widths,
    width: { size: total, type: WidthType.DXA },
    rows: [headRow, ...bodyRows]
  }));
  kids.push(new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: "" })] }));
}

let numCounter = 0;
let pendingTable = null;

for (const raw of lines) {
  const line = raw.trim();
  if (!line) continue;

  if (line === '[PAGEBREAK]') {
    kids.push(new Paragraph({ children: [new PageBreak()] }));
    numCounter = 0;
    continue;
  }

  const m = line.match(/^%%([A-Z0-9]+)%%(.*)$/);
  if (!m) {
    numCounter = 0;
    kids.push(new Paragraph({
      spacing: { before: 100, after: 160, line: 320 },
      children: [new TextRun({ text: line, size: 23, font: "Georgia", color: INK })]
    }));
    continue;
  }

  const tag = m[1], val = m[2];

  switch (tag) {
    case 'TITLE':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { before: 2400, after: 120 },
        children: [new TextRun({ text: val, bold: true, size: 96, color: TEAL, font: "Comfortaa", characterSpacing: 60 })]
      }));
      break;
    case 'SUB':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 60 },
        children: [new TextRun({ text: val, size: 40, color: INK, font: "Comfortaa" })]
      }));
      break;
    case 'SUB2':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 1600 },
        children: [new TextRun({ text: val, italics: true, size: 24, color: GREY, font: "Georgia" })]
      }));
      break;
    case 'AUTH':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: val, size: 26, color: INK, font: "Inter", characterSpacing: 80 })]
      }));
      break;
    case 'H1':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_1, spacing: { before: 240, after: 200 },
        children: [new TextRun({ text: val, bold: true, size: 44, color: TEAL, font: "Comfortaa" })]
      }));
      break;
    case 'WEEK':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { before: 3000, after: 100 },
        children: [new TextRun({ text: val, bold: true, size: 36, color: SAGE, font: "Inter", characterSpacing: 120 })]
      }));
      break;
    case 'WEEKSUB':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 200 },
        children: [new TextRun({ text: val, bold: true, size: 60, color: TEAL, font: "Comfortaa" })]
      }));
      break;
    case 'WEEKC':
      kids.push(new Paragraph({
        spacing: { before: 320, after: 120 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: SAGE, space: 6 } },
        children: [new TextRun({ text: val, bold: true, size: 24, color: SAGE, font: "Inter", characterSpacing: 40 })]
      }));
      break;
    case 'TOC': {
      const p = val.split('|');
      kids.push(new Paragraph({
        spacing: { before: 100, after: 20 },
        children: [
          new TextRun({ text: p[0], bold: true, size: 23, color: INK, font: "Inter" }),
          new TextRun({ text: "     " + (p[2] || ""), size: 18, color: GREY, font: "Inter" })
        ]
      }));
      kids.push(new Paragraph({
        spacing: { after: 60 }, indent: { left: 240 },
        children: [new TextRun({ text: p[1] || "", italics: true, size: 21, color: GREY, font: "Georgia" })]
      }));
      break;
    }
    case 'DAY':
      kids.push(new Paragraph({
        spacing: { before: 120, after: 60 },
        children: [new TextRun({ text: val.toUpperCase(), bold: true, size: 24, color: SAGE, font: "Inter", characterSpacing: 100 })]
      }));
      break;
    case 'TITLE2':
      kids.push(new Paragraph({
        spacing: { after: 40 },
        children: [new TextRun({ text: val, bold: true, size: 52, color: TEAL, font: "Comfortaa" })]
      }));
      break;
    case 'SUBT':
      kids.push(new Paragraph({
        spacing: { after: 220 },
        children: [new TextRun({ text: val, italics: true, size: 26, color: GREY, font: "Georgia" })]
      }));
      break;
    case 'VIDEO':
      kids.push(new Paragraph({
        spacing: { before: 120, after: 40 },
        shading: { type: ShadingType.CLEAR, fill: "E7F2F3" },
        border: {
          top:    { style: BorderStyle.SINGLE, size: 2, color: "B9D6D8", space: 10 },
          bottom: { style: BorderStyle.SINGLE, size: 2, color: "B9D6D8", space: 6 },
          left:   { style: BorderStyle.SINGLE, size: 2, color: "B9D6D8", space: 10 },
          right:  { style: BorderStyle.SINGLE, size: 2, color: "B9D6D8", space: 10 }
        },
        children: [
          new TextRun({ text: "TODAY'S VIDEO", bold: true, size: 20, color: TEAL, font: "Inter", characterSpacing: 60 }),
          new TextRun({ text: "     (" + val + ")", size: 18, color: GREY, font: "Inter" })
        ]
      }));
      kids.push(new Paragraph({
        spacing: { before: 0, after: 260 },
        shading: { type: ShadingType.CLEAR, fill: "E7F2F3" },
        border: {
          bottom: { style: BorderStyle.SINGLE, size: 2, color: "B9D6D8", space: 10 },
          left:   { style: BorderStyle.SINGLE, size: 2, color: "B9D6D8", space: 10 },
          right:  { style: BorderStyle.SINGLE, size: 2, color: "B9D6D8", space: 10 }
        },
        children: [new TextRun({ text: "Link:  ______________________________________________", size: 20, color: GREY, font: "Inter" })]
      }));
      break;
    case 'VERSE':
      kids.push(new Paragraph({
        spacing: { before: 60, after: 40, line: 340 },
        indent: { left: 360 },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 14 } },
        children: [new TextRun({ text: val, bold: true, size: 24, color: INK, font: "Georgia" })]
      }));
      break;
    case 'REF':
      kids.push(new Paragraph({
        spacing: { after: 300 }, indent: { left: 360 },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 14 } },
        children: [new TextRun({ text: val.toUpperCase(), size: 19, color: GOLD, font: "Inter", characterSpacing: 40 })]
      }));
      break;
    case 'H2':
      numCounter = 0;
      kids.push(new Paragraph({
        spacing: { before: 400, after: 40 },
        children: [new TextRun({ text: val, bold: true, size: 28, color: TEAL, font: "Comfortaa" })]
      }));
      kids.push(rule(SAGE, 4));
      break;
    case 'NUM':
      numCounter++;
      kids.push(new Paragraph({
        spacing: { before: 100, after: 100, line: 300 },
        indent: { left: 360, hanging: 300 },
        children: [
          new TextRun({ text: numCounter + ".   ", bold: true, size: 23, color: SAGE, font: "Inter" }),
          new TextRun({ text: val, size: 23, font: "Georgia", color: INK })
        ]
      }));
      if (!val) blankLines(1);
      break;
    case 'Q':
      kids.push(new Paragraph({
        spacing: { before: 120, after: 160, line: 320 },
        indent: { left: 300 },
        shading: { type: ShadingType.CLEAR, fill: "EFF6F1" },
        children: [new TextRun({ text: val, bold: true, size: 25, color: INK, font: "Georgia" })]
      }));
      break;
    case 'FILL':
      fillLine(val, false);
      break;
    case 'FILLB':
      fillLine(val, false);
      break;
    case 'LINES':
      blankLines(parseInt(val, 10) || 2);
      break;
    case 'TABLE':
      pendingTable = val.split('|');
      break;
    case 'ROWS':
      if (pendingTable) { makeTable(pendingTable, parseInt(val, 10) || 3); pendingTable = null; }
      break;
    case 'PRAYER':
      kids.push(new Paragraph({
        spacing: { before: 120, after: 200, line: 320 },
        indent: { left: 360 },
        border: { left: { style: BorderStyle.SINGLE, size: 8, color: SAGE, space: 12 } },
        children: [new TextRun({ text: val, italics: true, size: 23, color: GREY, font: "Georgia" })]
      }));
      break;
    default:
      kids.push(new Paragraph({ children: [new TextRun({ text: val, size: 23, font: "Georgia" })] }));
  }
}

const doc = new Document({
  styles: { default: { document: { run: { font: "Georgia", size: 23, color: INK } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840, orientation: PageOrientation.PORTRAIT },
        margin: { top: 1260, bottom: 1260, left: 1440, right: 1440 }
      }
    },
    children: kids
  }]
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('/mnt/user-data/outputs/Clarity_Thirty_Days_of_Reading.docx', b);
  console.log('done');
});
