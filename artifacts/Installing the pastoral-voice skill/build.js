const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType,
} = require("docx");

const NAVY = "1F2A44";
const GOLD = "9A7B2F";
const GRAY = "555555";

const pillar = (letter, title, body) =>
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1400, 7960],
    borders: {
      top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
    },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: 1400, type: WidthType.DXA },
            shading: { type: ShadingType.CLEAR, fill: "F2EEE3" },
            margins: { top: 160, bottom: 160, left: 120, right: 120 },
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text: letter, bold: true, size: 40, color: GOLD, font: "Georgia" })],
              }),
            ],
          }),
          new TableCell({
            width: { size: 7960, type: WidthType.DXA },
            margins: { top: 160, bottom: 160, left: 220, right: 120 },
            children: [
              new Paragraph({
                spacing: { after: 60 },
                children: [new TextRun({ text: title, bold: true, size: 24, color: NAVY, font: "Georgia" })],
              }),
              new Paragraph({
                children: [new TextRun({ text: body, size: 21, color: GRAY, font: "Calibri" })],
              }),
            ],
          }),
        ],
      }),
    ],
  });

const spacer = (h = 160) => new Paragraph({ spacing: { after: h }, children: [] });

const doc = new Document({
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 },
        },
      },
      children: [
        new Paragraph({
          spacing: { after: 40 },
          children: [new TextRun({ text: "LIFETOGETHER", bold: true, size: 20, color: GOLD, font: "Calibri", characterSpacing: 20 })],
        }),
        new Paragraph({
          spacing: { after: 60 },
          children: [new TextRun({ text: "Authentic Intelligence", bold: true, size: 64, color: NAVY, font: "Georgia" })],
        }),
        new Paragraph({
          spacing: { after: 40 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 8 } },
          children: [new TextRun({ text: "The Accelerator for Your Sermon Impact", italics: true, size: 28, color: NAVY, font: "Georgia" })],
        }),
        spacer(260),

        new Paragraph({
          spacing: { after: 160 },
          children: [new TextRun({
            text: "For years, \u201CAI\u201D has meant Artificial Intelligence \u2014 something manufactured, something apart from you.",
            size: 23, color: GRAY, font: "Calibri",
          })],
        }),
        new Paragraph({
          spacing: { after: 160 },
          children: [new TextRun({
            text: "We think your church deserves something different.",
            size: 23, color: GRAY, font: "Calibri",
          })],
        }),
        new Paragraph({
          spacing: { after: 260 },
          children: [new TextRun({
            text: "Authentic Intelligence isn\u2019t a replacement for your voice \u2014 it\u2019s an accelerator for your sermon impact. It takes the message God gave you this Sunday and helps it become everything your church needs to live it out all year long.",
            size: 23, color: GRAY, font: "Calibri",
          })],
        }),

        new Paragraph({
          spacing: { before: 120, after: 40 },
          children: [new TextRun({ text: "THE SEVEN A\u2019S OF AUTHENTIC INTELLIGENCE", bold: true, size: 22, color: GOLD, font: "Calibri", characterSpacing: 15 })],
        }),
        spacer(120),

        pillar("A", "Aligned",
          "Every resource stays aligned with your theology \u2014 for every age and stage of your church: adults, students, kids, even preschool."),
        spacer(140),
        pillar("A", "Aggregated",
          "Built on best practices gathered from thought-leading pastors, churches, and ministries around the world."),
        spacer(140),
        pillar("A", "Authored",
          "Every resource is authored in your voice, for your vision, for the congregation only you know."),
        spacer(140),
        pillar("A", "Affinity",
          "Custom affinity editions, shaped for the specific ministries and groups already inside your church."),
        spacer(140),
        pillar("A", "Applied",
          "Your sermon series, applied and extended into a full library of resources that serve your church for years to come: small group curriculum, devotions, classes, and more."),
        spacer(140),
        pillar("A", "Assessed",
          "Built-in assessments help you understand where each person is right now \u2014 and what they need next."),
        spacer(140),
        pillar("A", "Approved",
          "Nothing reaches your people until you\u2019ve reviewed and approved it. You stay the shepherd. Authentic Intelligence just carries the load."),

        spacer(320),
        new Paragraph({
          border: { top: { style: BorderStyle.SINGLE, size: 4, color: "D9D2BF", space: 12 } },
          spacing: { before: 80, after: 140 },
          children: [new TextRun({ text: "EVERY AGE. EVERY STAGE.", bold: true, size: 20, color: GOLD, font: "Calibri", characterSpacing: 15 })],
        }),
        new Paragraph({
          spacing: { after: 260 },
          children: [new TextRun({
            text: "Adult \u00B7 Student \u00B7 Kids \u00B7 Preschool \u2014 one sermon, translated faithfully for every room in your building.",
            size: 23, color: GRAY, font: "Calibri",
          })],
        }),

        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 200 },
          children: [new TextRun({
            text: "One sermon. A thousand ways to live it.",
            italics: true, bold: true, size: 26, color: NAVY, font: "Georgia",
          })],
        }),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buf) => require("fs").writeFileSync("Authentic_Intelligence_Brochure.docx", buf));
