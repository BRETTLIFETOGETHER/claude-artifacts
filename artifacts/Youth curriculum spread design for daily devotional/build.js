const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, BorderStyle, WidthType,
  ShadingType, VerticalAlign, PageNumber, PageBreak, HeadingLevel
} = require("docx");

/* ---------- palette ---------- */
const INK        = "20312F";  // body text
const PRIMARY    = "0E5A63";  // deep teal
const ACCENT     = "D9722E";  // warm amber
const ACCENT_DK  = "B45A1F";
const TINT_TEAL  = "E6F0F0";
const TINT_AMBER = "FAEEE2";
const TINT_SOFT  = "F4F8F8";
const RULE_GRAY  = "AFC0C0";
const PH_GRAY    = "8EA1A1";
const BOX_BORDER = "CBDDDD";

const CONTENT_W = 7920; // 7in - 2*0.75in margins, in DXA

/* ---------- helpers ---------- */
const SERIF = "Georgia";
const SANS  = "Arial";

function eyebrow(text, color = ACCENT) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text: text.toUpperCase(), font: SANS, bold: true, size: 18, color, characterSpacing: 30 })],
  });
}

function sectionHeader(text) {
  return new Paragraph({
    spacing: { before: 260, after: 140 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 4 } },
    children: [new TextRun({ text, font: SANS, bold: true, size: 27, color: PRIMARY })],
  });
}

function body(text, opts = {}) {
  return new Paragraph({
    spacing: { after: opts.after ?? 120, line: 264 },
    alignment: opts.align,
    children: [new TextRun({ text, font: SERIF, size: 22, color: INK, italics: opts.italics })],
  });
}

// single-cell callout box
function box({ fill, leftBar, children }) {
  const thin = { style: BorderStyle.SINGLE, size: 4, color: BOX_BORDER };
  const borders = {
    top: thin, right: thin, bottom: thin,
    left: leftBar ? { style: BorderStyle.SINGLE, size: 26, color: leftBar } : thin,
  };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        borders,
        shading: { fill, type: ShadingType.CLEAR },
        margins: { top: 150, bottom: 150, left: 220, right: 220 },
        children,
      })],
    })],
  });
}

// photo placeholder box
function photoBox(label, blankLines = 4) {
  const b = { style: BorderStyle.DASHED, size: 8, color: PH_GRAY };
  const inner = [
    new Paragraph({
      spacing: { before: 40, after: 40 },
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: label, font: SANS, italics: true, size: 19, color: PH_GRAY })],
    }),
  ];
  for (let i = 0; i < blankLines; i++) inner.push(new Paragraph({ spacing: { after: 0, line: 240 }, children: [new TextRun("")] }));
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        borders: { top: b, bottom: b, left: b, right: b },
        shading: { fill: TINT_SOFT, type: ShadingType.CLEAR },
        verticalAlign: VerticalAlign.CENTER,
        margins: { top: 120, bottom: 120, left: 160, right: 160 },
        children: inner,
      })],
    })],
  });
}

// ruled writing line
function ruled() {
  return new Paragraph({
    spacing: { before: 180, after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE_GRAY, space: 2 } },
    children: [new TextRun("")],
  });
}

function spacer(h = 80) {
  return new Paragraph({ spacing: { after: h }, children: [new TextRun("")] });
}

function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

/* ---------- scripture verse line ---------- */
function verse(text, ref) {
  return new Paragraph({
    spacing: { after: 100, line: 252 },
    children: [
      new TextRun({ text: `\u201C${text}\u201D`, font: SERIF, size: 22, italics: true, color: INK }),
      new TextRun({ text: `  \u2014 ${ref}`, font: SANS, size: 18, bold: true, color: PRIMARY }),
    ],
  });
}

/* ============================================================= */
/*  PAGE 1                                                        */
/* ============================================================= */
const page1 = [
  new Paragraph({
    spacing: { before: 40, after: 20 },
    children: [new TextRun({ text: "DAY 1", font: SANS, bold: true, size: 22, color: ACCENT, characterSpacing: 40 })],
  }),
  new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: "It Was Never Mine First", font: SANS, bold: true, size: 44, color: PRIMARY })],
  }),
  new Paragraph({
    spacing: { after: 220 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 14, color: ACCENT, space: 2 } },
    children: [new TextRun("")],
  }),

  eyebrow("Opening Story"),
  body("Have you ever had someone borrow something and then act like it belonged to them?"),
  body("Maybe it was your hoodie. Your charger. Your basketball. Your favorite pen. Your seat at lunch. They used it for a while, got comfortable with it, and somehow forgot it was yours."),
  body("That can be annoying \u2014 because ownership matters. When something belongs to you, people should treat it differently."),
  body("Now here is the bigger question: What if everything we have is borrowed?"),
  body("Your room. Your phone. Your body. Your abilities. Your money. Your time. Your friendships. Your future. Even the breath in your lungs."),
  body("That does not mean those things do not matter. It means they matter more. They are gifts from God, and gifts are meant to be cared for."),
  body("Most of the world says, \u201CThis is mine. I earned it. I deserve it. I can do whatever I want with it.\u201D"),
  body("Jesus teaches us to say, \u201CGod, this came from You. Help me use it well.\u201D That is a completely different way to see life.", { after: 60 }),

  sectionHeader("Today\u2019s Scripture"),
  box({
    fill: TINT_TEAL, leftBar: PRIMARY,
    children: [
      verse("The earth is the LORD\u2019s, and everything in it, the world, and all who live in it.", "Psalm 24:1, NIV"),
      new Paragraph({
        spacing: { after: 0, line: 252 },
        children: [
          new TextRun({ text: "\u201CEverything comes from you, and we have given you only what comes from your hand.\u201D", font: SERIF, size: 22, italics: true, color: INK }),
          new TextRun({ text: "  \u2014 1 Chronicles 29:14, NIV", font: SANS, size: 18, bold: true, color: PRIMARY }),
        ],
      }),
    ],
  }),
  spacer(120),

  eyebrow("Big Idea"),
  box({
    fill: TINT_AMBER, leftBar: ACCENT,
    children: [new Paragraph({
      spacing: { after: 0, line: 264 },
      children: [new TextRun({ text: "God owns everything, so I can live with gratitude instead of grabbing for more.", font: SANS, bold: true, size: 26, color: ACCENT_DK })],
    })],
  }),
];

/* ============================================================= */
/*  PAGE 2                                                        */
/* ============================================================= */
const page2 = [
  pageBreak(),
  sectionHeader("Picture This"),
  body("Hold one hand in a tight fist."),
  body("That is what life feels like when we think everything is ours. We grip. We worry. We compare. We protect. We get mad when someone else has more."),
  body("Now open your hand."),
  body("That is what trust looks like. An open hand can receive. An open hand can give. An open hand remembers, \u201CGod gave this to me, and God can be trusted.\u201D", { after: 100 }),
  photoBox("Photo space  \u00B7  a closed fist and an open hand", 3),

  sectionHeader("3 Things to Remember"),
  new Paragraph({
    numbering: { reference: "remember", level: 0 }, spacing: { after: 90, line: 258 },
    children: [
      new TextRun({ text: "Everything starts with God. ", font: SERIF, bold: true, size: 22, color: PRIMARY }),
      new TextRun({ text: "Before something was yours, it was His.", font: SERIF, size: 22, color: INK }),
    ],
  }),
  new Paragraph({
    numbering: { reference: "remember", level: 0 }, spacing: { after: 90, line: 258 },
    children: [
      new TextRun({ text: "Gratitude changes how you see your life. ", font: SERIF, bold: true, size: 22, color: PRIMARY }),
      new TextRun({ text: "Instead of asking, \u201CWhy don\u2019t I have more?\u201D you start asking, \u201CGod, how can I use what You\u2019ve given me?\u201D", font: SERIF, size: 22, color: INK }),
    ],
  }),
  new Paragraph({
    numbering: { reference: "remember", level: 0 }, spacing: { after: 60, line: 258 },
    children: [
      new TextRun({ text: "Open hands are freer than closed fists. ", font: SERIF, bold: true, size: 22, color: PRIMARY }),
      new TextRun({ text: "When you trust God, you do not have to hold everything so tightly.", font: SERIF, size: 22, color: INK }),
    ],
  }),

  sectionHeader("Real Talk"),
  body("This is hard because comparison is everywhere. Someone has better shoes. A newer phone. A bigger house. A nicer car. A better vacation. More freedom. More money. More likes."),
  body("But comparison usually makes us forget what God has already given. Gratitude helps us wake up.", { after: 60 }),

  sectionHeader("Try This Today"),
  box({
    fill: TINT_AMBER, leftBar: ACCENT,
    children: [
      new Paragraph({
        spacing: { after: 80, line: 260 },
        children: [new TextRun({ text: "Look around your room and name five things that belong to God but have been entrusted to you.", font: SERIF, size: 22, color: INK })],
      }),
      new Paragraph({
        spacing: { after: 0, line: 260 },
        children: [
          new TextRun({ text: "Then say out loud:  ", font: SERIF, size: 22, color: INK }),
          new TextRun({ text: "\u201CGod, this all belongs to You. Help me use it well.\u201D", font: SERIF, size: 22, bold: true, italics: true, color: ACCENT_DK }),
        ],
      }),
    ],
  }),
];

/* ============================================================= */
/*  PAGE 3                                                        */
/* ============================================================= */
const page3 = [
  pageBreak(),
  sectionHeader("Write It Down"),
  body("What is one thing God has given you that you sometimes forget to thank Him for?", { after: 60 }),
  ruled(), ruled(), ruled(), ruled(),
  spacer(120),

  sectionHeader("Talk About It"),
  body("What do you think students your age are most tempted to compare?", { after: 40 }),

  sectionHeader("Ask Someone"),
  body("Ask a parent, friend, sibling, or youth leader:", { after: 40 }),
  new Paragraph({
    spacing: { after: 60, line: 260 },
    children: [new TextRun({ text: "\u201CWhat is one thing God has given you that you are learning not to take for granted?\u201D", font: SERIF, size: 22, italics: true, color: INK })],
  }),

  sectionHeader("Prayer"),
  box({
    fill: TINT_TEAL, leftBar: PRIMARY,
    children: [new Paragraph({
      spacing: { after: 0, line: 280 },
      children: [new TextRun({ text: "God, everything I have comes from You. Help me stop grabbing for more and start noticing Your gifts. Teach me to live with open hands. Show me how to use what You have given me for good. Amen.", font: SERIF, size: 22, italics: true, color: INK })],
    })],
  }),
  spacer(180),

  // one-line reminder bar
  new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        borders: {
          top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
          left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
        },
        shading: { fill: PRIMARY, type: ShadingType.CLEAR },
        verticalAlign: VerticalAlign.CENTER,
        margins: { top: 200, bottom: 200, left: 220, right: 220 },
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { after: 40 },
            children: [new TextRun({ text: "ONE-LINE REMINDER", font: SANS, bold: true, size: 16, color: "BFE0E2", characterSpacing: 40 })],
          }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { after: 0, line: 264 },
            children: [new TextRun({ text: "Everything I have is a gift before it is mine.", font: SANS, bold: true, size: 28, color: "FFFFFF" })],
          }),
        ],
      })],
    })],
  }),
];

/* ---------- document ---------- */
const doc = new Document({
  styles: { default: { document: { run: { font: SERIF, size: 22, color: INK } } } },
  numbering: {
    config: [{
      reference: "remember",
      levels: [{
        level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
        style: { run: { bold: true, color: ACCENT, font: SANS },
                 paragraph: { indent: { left: 460, hanging: 320 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 10080, height: 14400 }, // 7 x 10 in
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 }, // 0.75in
      },
    },
    headers: {
      default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 0 },
        children: [new TextRun({ text: "GOD OWNS IT ALL  \u00B7  STUDENT EDITION", font: SANS, size: 14, color: PH_GRAY, characterSpacing: 30 })],
      })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT], font: SANS, size: 16, color: PH_GRAY })],
      })] }),
    },
    children: [...page1, ...page2, ...page3],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("/home/claude/goia/GOIA_Student_Day1_Spread.docx", buf);
  console.log("written");
});
