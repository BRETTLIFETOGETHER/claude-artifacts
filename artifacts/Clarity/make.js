const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, PageBreak, AlignmentType,
        HeadingLevel, PageOrientation, BorderStyle } = d;

const NAVY = "1F3B57";
const GOLD = "8A6D2F";
const GREY = "5A6570";

function build(mdPath, outPath) {
  const lines = fs.readFileSync(mdPath, 'utf8').split('\n');
  const kids = [];

  for (let raw of lines) {
    const line = raw.trim();
    if (!line) continue;

    if (line === '[PAGEBREAK]') {
      kids.push(new Paragraph({ children: [new PageBreak()] }));
      continue;
    }

    // Session number heading
    if (line.startsWith('# ')) {
      const t = line.slice(2);
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        alignment: AlignmentType.CENTER,
        spacing: { before: 240, after: 160 },
        children: [new TextRun({ text: t.toUpperCase(), bold: true, size: 40,
                                 color: NAVY, font: "Georgia", characterSpacing: 40 })]
      }));
      continue;
    }

    // Session title
    if (line.startsWith('## ')) {
      const t = line.slice(3);
      kids.push(new Paragraph({
        heading: HeadingLevel.HEADING_2,
        alignment: AlignmentType.CENTER,
        spacing: { before: 80, after: 80 },
        children: [new TextRun({ text: t, bold: true, size: 52, color: NAVY, font: "Georgia" })]
      }));
      continue;
    }

    // Subtitle
    if (line.startsWith('### ')) {
      const t = line.slice(4);
      kids.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 40, after: 400 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 12 } },
        children: [new TextRun({ text: t, italics: true, size: 30, color: GREY, font: "Georgia" })]
      }));
      continue;
    }

    // Stage cue
    if (line.startsWith('[CUE] ')) {
      const t = line.slice(6);
      kids.push(new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 460, after: 160 },
        children: [new TextRun({ text: t.toUpperCase(), bold: true, size: 22,
                                 color: GOLD, font: "Arial", characterSpacing: 60 })]
      }));
      continue;
    }

    // Speaker line
    const sp = line.match(/^\*\*(Brett|Tom):\*\*\s*(.*)$/);
    if (sp) {
      kids.push(new Paragraph({
        spacing: { before: 320, after: 140, line: 360 },
        children: [
          new TextRun({ text: sp[1].toUpperCase() + "   ", bold: true, size: 26,
                        color: NAVY, font: "Arial" }),
          new TextRun({ text: sp[2], size: 28, font: "Georgia" })
        ]
      }));
      continue;
    }

    // Plain body paragraph
    kids.push(new Paragraph({
      spacing: { before: 120, after: 140, line: 360 },
      indent: { left: 720 },
      children: [new TextRun({ text: line, size: 28, font: "Georgia" })]
    }));
  }

  const doc = new Document({
    styles: { default: { document: { run: { font: "Georgia", size: 28 } } } },
    sections: [{
      properties: {
        page: {
          size: { width: 12240, height: 15840, orientation: PageOrientation.PORTRAIT },
          margin: { top: 1080, bottom: 1080, left: 1440, right: 1440 }
        }
      },
      children: kids
    }]
  });

  return Packer.toBuffer(doc).then(b => {
    fs.writeFileSync(outPath, b);
    console.log("wrote " + outPath);
  });
}

build('book1.md', '/mnt/user-data/outputs/Book1_Family_Legacy_Coaching_by_Design_Scripts.docx')
  .then(() => build('book4.md', '/mnt/user-data/outputs/Book4_Communication_Scripts.docx'))
  .catch(e => { console.error(e); process.exit(1); });
