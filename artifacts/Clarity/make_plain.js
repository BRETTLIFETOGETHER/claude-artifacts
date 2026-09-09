const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, PageBreak, AlignmentType,
        HeadingLevel, PageOrientation, BorderStyle, Table, TableRow, TableCell,
        WidthType } = d;

const lines = fs.readFileSync('clarity30.md', 'utf8').split('\n');
const kids = [];

function blankLines(n) {
  for (let i = 0; i < n; i++) {
    kids.push(new Paragraph({
      spacing: { before: 160, after: 160 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 4 } },
      children: [new TextRun({ text: "" })]
    }));
  }
}

function fillLine(label) {
  kids.push(new Paragraph({
    spacing: { before: 180, after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 6 } },
    children: [new TextRun({ text: label, italics: true })]
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
      margins: { top: 100, bottom: 100, left: 120, right: 120 },
      children: [new Paragraph({ children: [new TextRun({ text: h, bold: true })] })]
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
      spacing: { before: 100, after: 140, line: 300 },
      children: [new TextRun({ text: line })]
    }));
    continue;
  }

  const tag = m[1], val = m[2];

  switch (tag) {
    case 'TITLE':
      kids.push(new Paragraph({
        heading: HeadingLevel.TITLE,
        alignment: AlignmentType.CENTER,
        spacing: { before: 2400, after: 120 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'SUB':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 60 },
        children: [new TextRun({ text: val, size: 32 })]
      }));
      break;
    case 'SUB2':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 1600 },
        children: [new TextRun({ text: val, italics: true })]
      }));
      break;
    case 'AUTH':
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: val, bold: true })]
      }));
      break;
    case 'H1':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 240, after: 200 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'WEEK':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        alignment: AlignmentType.CENTER,
        spacing: { before: 3000, after: 100 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'WEEKSUB':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_2,
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'WEEKC':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 320, after: 120 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'TOC': {
      const p = val.split('|');
      kids.push(new Paragraph({
        spacing: { before: 100, after: 20 },
        children: [
          new TextRun({ text: p[0], bold: true }),
          new TextRun({ text: "     " + (p[2] || ""), size: 18 })
        ]
      }));
      kids.push(new Paragraph({
        spacing: { after: 60 }, indent: { left: 240 },
        children: [new TextRun({ text: p[1] || "", italics: true })]
      }));
      break;
    }
    case 'DAY':
      kids.push(new Paragraph({
        spacing: { before: 120, after: 60 },
        children: [new TextRun({ text: val.toUpperCase(), bold: true, size: 20 })]
      }));
      break;
    case 'TITLE2':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { after: 40 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'SUBT':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { after: 220 },
        children: [new TextRun({ text: val, italics: true })]
      }));
      break;
    case 'VIDEO':
      kids.push(new Paragraph({
        spacing: { before: 120, after: 40 },
        border: {
          top:    { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 8 },
          bottom: { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 6 },
          left:   { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 8 },
          right:  { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 8 }
        },
        children: [
          new TextRun({ text: "TODAY'S VIDEO", bold: true, size: 20 }),
          new TextRun({ text: "     (" + val + ")", size: 18 })
        ]
      }));
      kids.push(new Paragraph({
        spacing: { before: 0, after: 260 },
        border: {
          bottom: { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 8 },
          left:   { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 8 },
          right:  { style: BorderStyle.SINGLE, size: 4, color: "999999", space: 8 }
        },
        children: [new TextRun({ text: "Link:  ______________________________________________", size: 20 })]
      }));
      break;
    case 'VERSE':
      kids.push(new Paragraph({
        spacing: { before: 60, after: 40, line: 320 },
        indent: { left: 360 },
        children: [new TextRun({ text: val, bold: true })]
      }));
      break;
    case 'REF':
      kids.push(new Paragraph({
        spacing: { after: 300 }, indent: { left: 360 },
        children: [new TextRun({ text: val, size: 20 })]
      }));
      break;
    case 'H2':
      numCounter = 0;
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 400, after: 80 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'NUM':
      numCounter++;
      kids.push(new Paragraph({
        spacing: { before: 100, after: 100, line: 300 },
        indent: { left: 360, hanging: 300 },
        children: [
          new TextRun({ text: numCounter + ".   ", bold: true }),
          new TextRun({ text: val })
        ]
      }));
      if (!val) blankLines(1);
      break;
    case 'Q':
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_4,
        spacing: { before: 120, after: 140, line: 300 },
        children: [new TextRun({ text: val })]
      }));
      break;
    case 'FILL':
    case 'FILLB':
      fillLine(val);
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
        spacing: { before: 120, after: 200, line: 300 },
        indent: { left: 360 },
        children: [new TextRun({ text: val, italics: true })]
      }));
      break;
    default:
      kids.push(new Paragraph({ children: [new TextRun({ text: val })] }));
  }
}

const doc = new Document({
  styles: {
    default: {
      document:  { run: { font: "Calibri", size: 22 } },
      title:     { run: { font: "Calibri Light", size: 56, bold: true, color: "000000" },
                   paragraph: { spacing: { after: 120 } } },
      heading1:  { run: { font: "Calibri Light", size: 36, bold: true, color: "000000" },
                   paragraph: { spacing: { before: 280, after: 120 } } },
      heading2:  { run: { font: "Calibri Light", size: 28, bold: false, color: "000000" },
                   paragraph: { spacing: { before: 160, after: 120 } } },
      heading3:  { run: { font: "Calibri", size: 24, bold: true, color: "000000" },
                   paragraph: { spacing: { before: 320, after: 80 } } },
      heading4:  { run: { font: "Calibri", size: 22, bold: true, italics: false, color: "000000" },
                   paragraph: { spacing: { before: 120, after: 100 } } }
    }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840, orientation: PageOrientation.PORTRAIT },
        margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 }
      }
    },
    children: kids
  }]
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('/mnt/user-data/outputs/Clarity_Thirty_Days_of_Reading.docx', b);
  console.log('done');
});
