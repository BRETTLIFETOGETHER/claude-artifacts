const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageNumber, PageBreak, UnderlineType
} = require('docx');
const fs = require('fs');

// Color palette
const NAVY = "1B3A5C";
const GOLD = "C8922A";
const LIGHT_BLUE = "E8F0F7";
const LIGHT_GOLD = "FDF3E3";
const MID_GRAY = "6B7280";
const LIGHT_GRAY = "F3F4F6";
const WHITE = "FFFFFF";
const DARK = "1F2937";

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorders = {
  top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
  left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE }
};

function para(text, opts = {}) {
  const { bold, italic, size = 22, color = DARK, spacing, align, indent, font = "Arial" } = opts;
  return new Paragraph({
    alignment: align || AlignmentType.LEFT,
    spacing: spacing || { before: 80, after: 80 },
    indent: indent,
    children: [new TextRun({ text, bold: bold || false, italics: italic || false, size, color, font })]
  });
}

function heading1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 120 },
    children: [new TextRun({ text, bold: true, size: 40, color: NAVY, font: "Arial" })]
  });
}

function heading2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 100 },
    children: [new TextRun({ text, bold: true, size: 30, color: NAVY, font: "Arial" })]
  });
}

function heading3(text) {
  return new Paragraph({
    spacing: { before: 200, after: 80 },
    children: [new TextRun({ text, bold: true, size: 24, color: GOLD, font: "Arial" })]
  });
}

function subheading(text) {
  return new Paragraph({
    spacing: { before: 160, after: 60 },
    children: [new TextRun({ text, bold: true, size: 22, color: NAVY, font: "Arial" })]
  });
}

function bodyText(text, opts = {}) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, size: 22, color: DARK, font: "Arial", ...opts })]
  });
}

function italicText(text) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, size: 22, color: MID_GRAY, font: "Arial", italics: true })]
  });
}

function bullet(text, bold_prefix = "") {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { before: 40, after: 40 },
    children: bold_prefix
      ? [new TextRun({ text: bold_prefix, bold: true, size: 22, color: DARK, font: "Arial" }),
         new TextRun({ text, size: 22, color: DARK, font: "Arial" })]
      : [new TextRun({ text, size: 22, color: DARK, font: "Arial" })]
  });
}

function colorBox(children, fillColor = LIGHT_BLUE, leftBorderColor = NAVY) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [200, 9160],
    borders: { ...Object.fromEntries(["top","bottom","left","right","insideH","insideV"].map(k => [k, { style: BorderStyle.NONE }])) },
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: 200, type: WidthType.DXA },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
            left: { style: BorderStyle.SINGLE, size: 24, color: leftBorderColor },
            right: { style: BorderStyle.NONE } },
          shading: { fill: leftBorderColor, type: ShadingType.CLEAR },
          children: [new Paragraph({ children: [] })]
        }),
        new TableCell({
          width: { size: 9160, type: WidthType.DXA },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
            left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
          shading: { fill: fillColor, type: ShadingType.CLEAR },
          margins: { top: 120, bottom: 120, left: 200, right: 200 },
          children
        })
      ]
    })]
  });
}

function divider() {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD } },
    children: []
  });
}

function spacer(before = 120) {
  return new Paragraph({ spacing: { before, after: 0 }, children: [] });
}

function sessionHeader(number, title, subtitle, theme, scripture) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE }, insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE } },
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: NAVY, type: ShadingType.CLEAR },
        margins: { top: 240, bottom: 240, left: 360, right: 360 },
        borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
          left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
        children: [
          new Paragraph({ spacing: { before: 0, after: 60 }, children: [
            new TextRun({ text: `SESSION ${number}`, size: 18, color: GOLD, bold: true, font: "Arial" })
          ]}),
          new Paragraph({ spacing: { before: 0, after: 80 }, children: [
            new TextRun({ text: title, size: 40, color: WHITE, bold: true, font: "Arial" })
          ]}),
          new Paragraph({ spacing: { before: 0, after: 80 }, children: [
            new TextRun({ text: subtitle, size: 24, color: "C8D8E8", font: "Arial", italics: true })
          ]}),
          new Paragraph({ spacing: { before: 60, after: 0 }, children: [
            new TextRun({ text: `Theme: `, size: 20, color: GOLD, bold: true, font: "Arial" }),
            new TextRun({ text: theme, size: 20, color: "E8F0F7", font: "Arial" }),
          ]}),
          new Paragraph({ spacing: { before: 20, after: 0 }, children: [
            new TextRun({ text: `Key Scripture: `, size: 20, color: GOLD, bold: true, font: "Arial" }),
            new TextRun({ text: scripture, size: 20, color: "E8F0F7", font: "Arial" }),
          ]}),
        ]
      })]
    })]
  });
}

function twoColTable(col1Header, col1Items, col2Header, col2Items) {
  const makeCell = (header, items, fill) => new TableCell({
    width: { size: 4680, type: WidthType.DXA },
    shading: { fill, type: ShadingType.CLEAR },
    borders,
    margins: { top: 120, bottom: 120, left: 160, right: 160 },
    children: [
      new Paragraph({ spacing: { before: 0, after: 80 }, children: [new TextRun({ text: header, bold: true, size: 22, color: NAVY, font: "Arial" })] }),
      ...items.map(i => new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { before: 30, after: 30 }, children: [new TextRun({ text: i, size: 20, color: DARK, font: "Arial" })] }))
    ]
  });
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [4680, 4680],
    borders: { insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE },
      top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
    rows: [new TableRow({ children: [makeCell(col1Header, col1Items, LIGHT_BLUE), makeCell(col2Header, col2Items, LIGHT_GOLD)] })]
  });
}

function flowTable(steps) {
  // steps: [{time, label, detail}]
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1400, 2200, 5760],
    borders: { insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE },
      top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
    rows: steps.map((s, i) => new TableRow({
      children: [
        new TableCell({
          width: { size: 1400, type: WidthType.DXA },
          shading: { fill: i % 2 === 0 ? NAVY : "2A4F78", type: ShadingType.CLEAR },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
          margins: { top: 100, bottom: 100, left: 120, right: 120 },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: s.time, size: 18, color: GOLD, bold: true, font: "Arial" })] })]
        }),
        new TableCell({
          width: { size: 2200, type: WidthType.DXA },
          shading: { fill: i % 2 === 0 ? LIGHT_BLUE : "EEF4FA", type: ShadingType.CLEAR },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
          margins: { top: 100, bottom: 100, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: s.label, size: 20, bold: true, color: NAVY, font: "Arial" })] })]
        }),
        new TableCell({
          width: { size: 5760, type: WidthType.DXA },
          shading: { fill: i % 2 === 0 ? LIGHT_GRAY : WHITE, type: ShadingType.CLEAR },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
          margins: { top: 100, bottom: 100, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: s.detail, size: 20, color: DARK, font: "Arial" })] })]
        }),
      ]
    }))
  });
}

// ============ DOCUMENT CONTENT ============

const doc = new Document({
  numbering: {
    config: [
      { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 40, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 280, after: 100 }, outlineLevel: 1 } },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 }
      }
    },
    children: [

      // ===== COVER PAGE =====
      spacer(1440),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [9360],
        borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE }, insideH: { style: BorderStyle.NONE }, insideV: { style: BorderStyle.NONE } },
        rows: [new TableRow({ children: [new TableCell({
          width: { size: 9360, type: WidthType.DXA },
          shading: { fill: NAVY, type: ShadingType.CLEAR },
          margins: { top: 600, bottom: 600, left: 720, right: 720 },
          borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
          children: [
            new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 80 }, children: [new TextRun({ text: "GOD OWNS IT ALL", size: 56, bold: true, color: WHITE, font: "Arial" })] }),
            new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 160 }, children: [new TextRun({ text: "Youth Edition", size: 36, color: GOLD, font: "Arial", italics: true })] }),
            new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 120 }, children: [new TextRun({ text: "6-Session Curriculum", size: 26, color: "C8D8E8", font: "Arial" })] }),
            new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 80, after: 0 }, children: [new TextRun({ text: "Based on the Teaching of Ron Blue", size: 22, color: "A8C0D8", font: "Arial" })] }),
          ]
        })]})],
      }),
      spacer(240),
      colorBox([
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 40, after: 40 }, children: [
          new TextRun({ text: '"The earth is the Lord\'s, and everything in it." — Psalm 24:1', size: 24, italics: true, color: NAVY, font: "Arial" })
        ]})
      ], LIGHT_GOLD, GOLD),
      spacer(360),
      new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Ron Blue Institute", size: 22, bold: true, color: MID_GRAY, font: "Arial" })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Designed for Middle School & High School Students", size: 20, color: MID_GRAY, font: "Arial" })] }),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== OVERVIEW SECTION =====
      heading1("Overview & Vision"),
      divider(),
      spacer(80),

      bodyText("This six-session curriculum translates the core teaching of God Owns It All into the language and world of teenagers. The theology is unchanged — who owns it, what that means for daily decisions, how identity gets formed around money — but the delivery is designed for where students actually live: first jobs, spending choices, social pressure, and a culture that tells them the opposite of everything on these pages."),
      spacer(80),
      bodyText("The adult devotional asks Ron's foundational question across forty days. This curriculum asks the same question across six sessions — and builds a formation arc that can hold a small group, a Sunday school class, or a midweek youth night."),
      spacer(120),

      heading2("The Core Question"),
      colorBox([
        new Paragraph({ spacing: { before: 40, after: 20 }, children: [new TextRun({ text: "Who owns it?", size: 30, bold: true, color: NAVY, font: "Arial" })] }),
        new Paragraph({ spacing: { before: 0, after: 40 }, children: [new TextRun({ text: "That single question, answered honestly, changes everything downstream — how students handle their first paycheck, how they respond to comparison, how they think about their future, and what kind of person they're becoming one small decision at a time.", size: 22, color: DARK, font: "Arial" })] }),
      ], LIGHT_BLUE, NAVY),
      spacer(120),

      heading2("Why This Curriculum Is Different"),
      bodyText("Most youth financial tools start with behavior — budget, save, give — and gesture toward theology. This curriculum inverts that sequence. It starts with the ownership question and lets practical formation flow from the answer. That's not just pedagogically different: for teenagers forming their identity in real time, starting with 'you belong to God' rather than 'here's how to handle money better' is a genuinely different kind of formation."),
      spacer(80),

      heading2("The 3-Layer Delivery System"),
      bodyText("Following the proven model from The Great Life Youth Edition framework, each session operates across three environments:"),
      spacer(60),
      twoColTable(
        "Daily (Personal)", ["2–4 min student devotional", "Story-driven, first-person voice", "1 reflection question + 1 action step", "Short prayer", "Builds daily habit between sessions"],
        "Weekly (Group Experience)", ["60–75 min youth night OR 45 min Sunday format", "Student story video (2–3 min) — cold open", "Youth pastor teaching (8–10 min)", "Small group discussion", "Live-It-Out Challenge + closing prayer"]
      ),
      spacer(80),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "Home Layer: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Weekly parent guide (1 page) + 60–90 sec parent video. One question, one action, one prayer. Simple enough for dinner conversation.", size: 22, color: DARK, font: "Arial" })] })
      ], LIGHT_GOLD, GOLD),
      spacer(120),

      heading2("The 40-Day to 6-Session Bridge"),
      bodyText("Days 1–7 of the adult devotional (Section I: The Ownership Question) map directly to Sessions 1–3 of this curriculum. Sessions 4–6 draw from Sections II–V of the adult 40-day outline, translating the stewardship, contentment, and generosity threads into student-accessible format. As more days of the adult devotional are developed, this curriculum can expand to a full 9-session or 12-session arc."),
      spacer(60),

      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2200, 2800, 4360],
        borders: { insideH: border, insideV: { style: BorderStyle.NONE }, top: border, bottom: border, left: border, right: border },
        rows: [
          new TableRow({ children: [
            new TableCell({ width: { size: 2200, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders, children: [new Paragraph({ children: [new TextRun({ text: "Session", bold: true, size: 20, color: WHITE, font: "Arial" })] })] }),
            new TableCell({ width: { size: 2800, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders, children: [new Paragraph({ children: [new TextRun({ text: "Adult Devotional Source", bold: true, size: 20, color: WHITE, font: "Arial" })] })] }),
            new TableCell({ width: { size: 4360, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders, children: [new Paragraph({ children: [new TextRun({ text: "Youth Theme", bold: true, size: 20, color: WHITE, font: "Arial" })] })] }),
          ]}),
          ...[ 
            ["Session 1", "Days 1–2", "Who's Really in Charge? The Ownership Question"],
            ["Session 2", "Days 3–4", "Mine Is Not a Safe Word — Identity & Belonging"],
            ["Session 3", "Days 5–6", "Your Money Has a Record — Tool, Test, Testimony"],
            ["Session 4", "Days 7 + Section II", "What Faithful Looks Like — Stewardship in Real Life"],
            ["Session 5", "Sections III–IV", "Enough Is a Spiritual Word — Contentment vs. Culture"],
            ["Session 6", "Sections V–VI", "Open Hands — Generosity & Who You're Becoming"],
          ].map((row, i) => new TableRow({ children: row.map((cell, j) => new TableCell({
            width: { size: [2200, 2800, 4360][j], type: WidthType.DXA },
            shading: { fill: i % 2 === 0 ? WHITE : LIGHT_GRAY, type: ShadingType.CLEAR },
            margins: { top: 60, bottom: 60, left: 120, right: 120 },
            borders,
            children: [new Paragraph({ children: [new TextRun({ text: cell, size: 20, color: DARK, font: "Arial", bold: j === 0 })] })]
          })) }))
        ]
      }),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== RON BLUE INTEGRATION =====
      heading1("Ron Blue Integration Strategy"),
      divider(),
      spacer(80),
      bodyText("Ron Blue is an authority and credibility asset — not a youth communication asset. The goal is not 'how do we use Ron in youth content?' but 'how do we use Ron to elevate the credibility and depth of the whole system?' Used strategically, his voice becomes what distinguishes this curriculum from every other teen financial resource on the market."),
      spacer(100),

      heading2("Where Ron Shows Up"),
      spacer(60),

      subheading("1. Opening Campaign Cameo (One Time — 60–90 seconds)"),
      bodyText("Plays at the launch event or beginning of Session 1. Ron speaks directly to students — brief, warm, and clear:"),
      spacer(40),
      colorBox([
        new Paragraph({ spacing: { before: 30, after: 30 }, children: [new TextRun({ text: "Suggested framing: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: '"For decades I\'ve sat across the table from people — young and old, wealthy and struggling — and underneath every financial conversation was the same question. The same fear. I want you to hear something that took me years and thousands of conversations to really believe: you are not the owner. And that is not bad news."', size: 22, italics: true, color: DARK, font: "Arial" })] })
      ], LIGHT_GOLD, GOLD),
      spacer(80),

      subheading("2. Leader Training Series (5–7 Videos, 5–8 Minutes Each)"),
      bodyText("This is the highest-value use of Ron's content. Youth pastors, volunteer leaders, and parents receive a short video track that grounds them in the theology before they ever run a session. Suggested topics:"),
      spacer(40),
      bullet("Why financial discipleship must start in adolescence — not adulthood"),
      bullet("God Owns It All: the foundational shift from owner to steward"),
      bullet("How to talk to students about money without shame or pressure"),
      bullet("From allowance to stewardship mindset — what formation actually looks like"),
      bullet("What most churches miss about money and identity formation"),
      bullet("Helping families align, not just students"),
      spacer(80),

      subheading("3. Parent Insight Clips (2–3 Minutes Each, One Per Session)"),
      bodyText("Ron speaks directly to parents — not as the youth communicator but as the trusted authority who has spent forty years watching what happens when families do and don't have these conversations. These are optional viewing, included in the weekly parent guide."),
      spacer(80),

      subheading("4. Strategic Session Insert (One Per Series)"),
      bodyText("Around Session 3 or 4, a short 90-second clip from Ron serves as a 'weight moment' — the curriculum pauses, the youth pastor says 'Before we go further, I want you to hear from someone who has spent his life on this,' and Ron adds depth that the student communicators can't carry alone."),
      spacer(80),

      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "Positioning line: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: '"Built on the lifelong teaching of Ron Blue — designed for the next generation."', size: 22, italics: true, color: DARK, font: "Arial" })] }),
        new Paragraph({ spacing: { before: 10, after: 10 }, children: [new TextRun({ text: "This gives the curriculum theological depth (Ron) + relational connection (students) + practical delivery (youth pastors).", size: 22, color: DARK, font: "Arial" })] }),
      ], LIGHT_BLUE, NAVY),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== YOUTH TESTIMONIALS =====
      heading1("Youth Testimonial Framework"),
      divider(),
      spacer(80),
      bodyText("Each session opens with a student story — the emotional hook that pulls students in before the teaching segment explains the meaning. These are not fabricated. They are either real testimonials captured in interview format, or stories based on real situations framed honestly as such. Below are the three primary testimonial profiles recommended for this series, plus guidance on sourcing and filming them."),
      spacer(100),

      heading2("Testimonial 1: The Second-Generation Steward"),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 10 }, children: [new TextRun({ text: "Source: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Based on Adam Wilson's story from Master Your Money (Wilson Wealth Stewardship, Macon, GA)", size: 22, color: DARK, font: "Arial" })] }),
        new Paragraph({ spacing: { before: 10, after: 10 }, children: [new TextRun({ text: "Best for: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Session 1 or Session 4 — Ownership Foundation / Stewardship in Real Life", size: 22, color: DARK, font: "Arial" })] }),
      ], LIGHT_BLUE, NAVY),
      spacer(60),
      bodyText("Adam Wilson grew up in a home where 'God owns it all' wasn't a slogan — it was a household rule. 'We weren't given allowance. We earned. We saved 10 percent, gave 10 percent, and lived on the rest. It wasn't optional. It was obedience.' Today Adam works alongside his father as a financial advisor, helping families live the same principles he grew up with."),
      spacer(60),
      bodyText("For the video, find a high school senior or college freshman — ideally someone with a similar background — who can speak to what it felt like to grow up with these habits. The interview question isn't 'tell me about your finances.' It's: 'Was there a moment when you realized your parents' approach to money was actually different from everyone around you — and did that feel weird or freeing?'"),
      spacer(60),
      italicText("Adam's line is the one to chase: \"Letting go isn't a burden. It's a joy. It's not my money anyway.\" That's the testimonial destination for this story thread."),
      spacer(100),

      heading2("Testimonial 2: The First Paycheck Moment"),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 10 }, children: [new TextRun({ text: "Source: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Original — recruit from partnering churches or RBI network", size: 22, color: DARK, font: "Arial" })] }),
        new Paragraph({ spacing: { before: 10, after: 10 }, children: [new TextRun({ text: "Best for: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Session 3 — Tool, Test, Testimony", size: 22, color: DARK, font: "Arial" })] }),
      ], LIGHT_GOLD, GOLD),
      spacer(60),
      bodyText("The story arc: A student gets their first paycheck from a part-time job. They had plans — clothes, food with friends, maybe some savings. That week at church they hear about honoring God first with what you earn. They do the math. Giving 10 percent feels like a lot when the number is small. But they give first — not confidently, not perfectly, but first. What changes isn't the bank account. It's how they see the paycheck."),
      spacer(60),
      bodyText("Interview prompt for filming: 'Do you remember your first real paycheck? What was going through your head? Was there a moment where someone or something made you think differently about what to do with it?' Let the student tell it in their own words. Edit for the turn — the moment the ownership question landed."),
      spacer(60),
      italicText("The line to find in editing: the moment they say something like 'I stopped seeing it as money I earned alone and started seeing it as something entrusted to me.' That's the clip."),
      spacer(100),

      heading2("Testimonial 3: The Small Thing That Was Actually Big"),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 10 }, children: [new TextRun({ text: "Source: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Original — ideal for a junior high student or young high schooler", size: 22, color: DARK, font: "Arial" })] }),
        new Paragraph({ spacing: { before: 10, after: 10 }, children: [new TextRun({ text: "Best for: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Session 2 or Session 6 — Identity / Generosity", size: 22, color: DARK, font: "Arial" })] }),
      ], LIGHT_BLUE, NAVY),
      spacer(60),
      bodyText("The story arc: A student has a small amount of money — birthday money, a gift, saved-up allowance. They had a plan for it. Then they encounter a moment where someone else needs it more. The internal fight is real. They give — not everything, but something. It doesn't feel dramatic. But later, something shifted. They realized stewardship isn't about big dramatic decisions. It's about what you do with what's right in front of you."),
      spacer(60),
      bodyText("This story is most powerful when told by a younger student (8th or 9th grade) because it removes the 'paycheck' context and makes the principle accessible to students who don't have jobs yet. The $20 bill, the birthday money, the Venmo gift — these are the financial stakes of middle school, and they matter just as much spiritually."),
      spacer(60),
      italicText("Interview prompt: 'Have you ever had money and felt pulled between spending it on yourself and doing something else with it? What happened? What did you learn?' The goal is the internal shift, not the amount."),
      spacer(100),

      heading2("How to Film These Stories"),
      bodyText("Following the Great Life Youth framework, the winning format is guided authentic — not fully scripted, not fully improvised."),
      spacer(60),
      bullet("Give the student the written story beforehand. Let them read it. Have them re-tell it in their own words."),
      bullet("Film in interview format — seated, relaxed, simple background (couch or chair, not a podium)."),
      bullet("Ask the question, capture the answer, edit to the turn. You are looking for one genuine moment of insight."),
      bullet("Open with: 'This is based on a real situation a student went through…' OR let the student speak naturally if it IS their story."),
      bullet("2–3 minutes maximum. Leave space for the teaching to explain the meaning."),
      spacer(80),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 10 }, children: [new TextRun({ text: "Production tip: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "Film 15–20 students at a Saturday morning capture session using 2–3 interview stations simultaneously. Build a story library of 30–40 clips, then assign them to sessions in editing. Do not try to match stories 1:1 to sessions during filming — you will lose flexibility.", size: 22, color: DARK, font: "Arial" })] })
      ], LIGHT_BLUE, NAVY),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== SESSION 1 =====
      sessionHeader("1", "Who's Really in Charge?", "The Ownership Question — The Foundation Everything Else Rests On", "God's ownership is the place your heart can finally rest.", "Psalm 24:1; Romans 11:36"),
      spacer(120),

      heading2("Adult Devotional Connection"),
      bodyText("Drawn from Days 1–2 of the God Owns It All devotional — 'The Question Underneath the Question' and 'Rights Belong to the Owner.' The three wrong questions (Will I have enough? Will it last? How much is enough?) and the second-chair illustration are the theological core. Youth translation: rename the questions in teen language, replace the boss's dinner table with a team captain's locker room or a starting lineup, and surface the same ownership drift in their world."),
      spacer(100),

      heading2("Session Flow (60–75 Minutes)"),
      flowTable([
        { time: "10 min", label: "Icebreaker", detail: "The Ownership Game: Give two students identical items. One 'owns' it, one is 'borrowing' it for the hour. At the end, the owner asks for it back. Debrief: What's the difference between how you treated it when you thought it was yours vs. borrowed? This is the entire session in one object lesson." },
        { time: "3 min", label: "Student Story Video", detail: "Cold open. Student story: The Second-Generation Steward (Adam Wilson arc). 'We saved 10 percent, gave 10 percent, lived on the rest. It wasn't optional. It was obedience.' Plays without introduction — drop straight into it." },
        { time: "2 min", label: "Leader Bridge", detail: "Youth pastor: 'That tension you just heard — being raised differently than everyone around you — that's actually what we're talking about. Not weird. Different. Let me tell you why that difference matters so much…'" },
        { time: "10 min", label: "Teaching", detail: "The Three Wrong Questions: Will I be successful? Will I be significant? Will I be secure? The culture's answer is always 'more.' Ron's forty years of client work showed that more doesn't answer these questions — it moves them. The Three Right Questions: Who owns it? How much is enough (as stewardship, not scarcity)? Is the next steward prepared? The first question changes everything downstream." },
        { time: "15 min", label: "Small Groups", detail: "Discussion Questions (choose 2): (1) When something financial goes wrong — parent loses a job, your savings disappear — what's your first internal move? (2) What does your spending say about what you actually value? (3) If God owns it all, what changes about how you feel about not having something?" },
        { time: "8 min", label: "Live-It-Out Challenge", detail: "Before your next purchase this week — anything — pause for 10 seconds and ask: 'God, you're the owner. What does faithful look like here?' Don't change what you do. Just ask the question. Report back next week." },
        { time: "5 min", label: "Closing Prayer", detail: "Youth pastor prays the student declaration aloud: 'God, you are the Owner. Everything I have belongs to you. I am not the source. Teach me to steward what you've entrusted to me with open hands and a steady heart.'" },
      ]),
      spacer(100),

      heading2("Key Teaching Moment"),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "The reframe: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "If God owns it, you are not alone in carrying it. The question changes from 'Will I be okay?' to 'What does faithful look like today?' That's not just a spiritual idea — it's a lighter load. And a lighter load changes everything about how you make decisions.", size: 22, italics: true, color: DARK, font: "Arial" })] })
      ], LIGHT_BLUE, NAVY),
      spacer(80),

      heading2("Ron Blue Connection"),
      bodyText("Play the Opening Campaign Cameo here if launching the series for the first time. Ron's line to find: 'You stop being the owner responsible for guaranteeing outcomes, and you become a steward responsible for faithfulness. Those are very different jobs.'"),
      spacer(80),

      heading2("Parent Guide — Session 1"),
      bodyText("What your student is learning: That everything they have belongs to God — and that changes how they feel about money, stuff, and the future."),
      bodyText("One question for dinner: 'What's something you've been stressing about lately — and what would change if you knew God was in charge of how it turned out?'"),
      bodyText("One action: Before any purchase this week, say together: 'God, you're the Owner. Is this how you'd want this used?'"),
      bodyText("Prayer: Father, you are the source of every good gift. Help our family hold what we have with open hands. Amen."),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== SESSION 2 =====
      sessionHeader("2", "Mine Is Not a Safe Word", "Identity & Belonging — Why What You Own Doesn't Define You", "God's ownership is personal. You're not a property — you're a person.", "Deuteronomy 8:17–18; Isaiah 43:1; 1 Corinthians 6:19–20"),
      spacer(120),

      heading2("Adult Devotional Connection"),
      bodyText("Drawn from Days 3–4 — 'Mine Is Not a Word, It's an Identity' and 'Owned and Loved.' The Kenya pastor story (materialism isn't uniquely American — it's uniquely human), the identity-attachment warning ('the test isn't what you have — it's what you would lose yourself over if it disappeared'), and the Isaiah 43:1 reframe ('I have called you by name, you are mine') are the theological spine. For teenagers, identity formation is happening right now — this session lands at the center of that."),
      spacer(100),

      heading2("Session Flow (60–75 Minutes)"),
      flowTable([
        { time: "10 min", label: "Icebreaker", detail: "The Status Symbol Game: Each student writes down one thing they own (or want) that would feel embarrassing to lose in front of their friends. Collect anonymously, read them out. Debrief: Why does losing it feel embarrassing? What does that reveal about why you wanted it?" },
        { time: "3 min", label: "Student Story Video", detail: "The Small Thing That Was Actually Big (birthday money / $20 story). The internal fight between 'mine' and 'something better.' Plays cold — no introduction." },
        { time: "2 min", label: "Leader Bridge", detail: "'That feeling — that grip — that's what today is about. Not what you spend. What you grip. Let me tell you about a pastor in Kenya who taught me something I didn't expect…' (Tell the Kenya mud hut story briefly — Ron's Africa trip.)" },
        { time: "10 min", label: "Teaching", detail: "How 'Mine' Becomes 'Me': Deuteronomy 8 identifies the drift — we start crediting ourselves as the source. 'Mine' stops being a description and becomes a claim. The identity attachment: when something is 'mine,' any threat to it feels like a threat to me. Financial pressure becomes a verdict on my worth. Then Isaiah 43:1 — the counter-claim. God doesn't claim you like an asset. He calls you like a Father. 'I have called you by name, you are mine' — that's not a legal document. That's a shelter." },
        { time: "15 min", label: "Small Groups", detail: "Discussion Questions: (1) Is there something you own or want that you'd feel embarrassed or anxious to lose — not because it's necessary, but because of what it says about you? (2) What's the difference between 'mine' as a description (I'm responsible for this) and 'mine' as an identity (this is proof I'm okay)? (3) If God says 'You are mine' — does that feel like a restriction or a relief? Why?" },
        { time: "8 min", label: "Live-It-Out Challenge", detail: "Write five things you have that you didn't create: an ability, a relationship, an opportunity, your health, a door God opened. Spend two minutes this week saying one out loud before you go to bed: 'God, thank you for ___. I didn't make that. You did.'" },
        { time: "5 min", label: "Closing Prayer", detail: "Declaration: 'Lord, you are the Owner. My life is not defined by what I have. I remember that my strength comes from you, and I choose to hold what you've entrusted to me with gratitude and open hands.'" },
      ]),
      spacer(100),

      heading2("Key Teaching Moment"),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "The test: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "It's not what you have. It's what you would lose yourself over if it disappeared. Where your identity is attached, your anxiety will follow. And God's answer isn't 'own less.' It's 'belong to me.' That relocation is everything.", size: 22, italics: true, color: DARK, font: "Arial" })] })
      ], LIGHT_BLUE, NAVY),
      spacer(80),

      heading2("Parent Guide — Session 2"),
      bodyText("What your student is learning: That 'mine' is more than a description — it can quietly become the place we go to feel safe or prove our worth. And that belonging to God is a better anchor than anything they own."),
      bodyText("One question for dinner: 'Is there something you really want right now — and if you're honest, why do you want it? What would it give you?'"),
      bodyText("One action: As a family, name one thing you have that none of you created. Thank God for it together."),
      bodyText("Prayer: God, thank you that we belong to you. Help us hold what we have with open hands. Amen."),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== SESSION 3 =====
      sessionHeader("3", "Your Money Has a Record", "Tool. Test. Testimony. — What God Is Already Doing With Your Finances", "Your trust shows up in your choices, not your intentions.", "Matthew 6:21; Philippians 4:11–12"),
      spacer(120),

      heading2("Adult Devotional Connection"),
      bodyText("Drawn from Days 5–6 — 'Tool. Test. Testimony.' and 'Anxiety and Ownership.' The three-function framework (money as tool, test, and testimony) and the rehearsing-vs.-preparing distinction are the core. The line from Day 5 — 'Money has no voice, but it has a record' — is the session anchor. For students: look at your last month of purchases (or your Venmo/Cash App history). What does it say about what you actually trust?"),
      spacer(100),

      heading2("Session Flow (60–75 Minutes)"),
      flowTable([
        { time: "10 min", label: "Icebreaker", detail: "The Spending Reveal: Ask students to think about what they spent money on in the last two weeks — don't share details, just the categories (food, clothes, entertainment, games, giving, etc). Ask: If a stranger looked at this list and had to guess what you value most, what would they say? Let three or four students share (voluntarily)." },
        { time: "3 min", label: "Student Story Video", detail: "The First Paycheck (Session 3 version — the tool/test thread). Student describes realizing their paycheck revealed something about themselves, not just their bank account." },
        { time: "2 min", label: "Leader Bridge", detail: "'What you just heard isn't a money story. It's a heart story. And Ron Blue has a phrase I want you to think about for the next thirty minutes: Money has no voice, but it has a record. Let's talk about what that means.'" },
        { time: "10 min", label: "Teaching", detail: "Money as Tool: It funds things. But also, it's a tool in God's hands to do something in you. The habit of giving is a practice of trust. The discipline of not spending everything you earn is a practice of believing you have enough. Money as Test: Paul says he 'learned' contentment — it was formed, not felt. Tight seasons reveal what you actually trust. Abundant seasons reveal what you actually love. Both directions reveal the heart. Money as Testimony: The world is watching whether Christians are actually different. Not wealthier — different. The teenager who doesn't spiral when their savings disappear. The one who gives when it doesn't make mathematical sense. That's a testimony. Not a sales pitch. A life." },
        { time: "15 min", label: "Small Groups", detail: "Discussion Questions: (1) If someone looked at where you've spent money in the last month, what would they say you value? Is that accurate? (2) Paul said he 'learned' contentment — it was formed through seasons of need and plenty. What season are you in right now, and what might God be teaching you through it? (3) What would it look like for your financial life to be a testimony — not perfect, but different?" },
        { time: "8 min", label: "Live-It-Out Challenge", detail: "Pull up one month of spending — bank app, Venmo, whatever you use. Don't judge it. Just look at it and finish this sentence: 'If God looked at this record, the one thing I'd want to change is ___.' Write it down. Bring it back next week." },
        { time: "5 min", label: "Closing Prayer", detail: "Declaration: 'Jesus, you are my Master. My treasure will follow you. Teach me to choose faithfulness over fear, and to use what you've entrusted to me as a tool for your purposes, an open field for your formation, and a testimony to your faithfulness.'" },
      ]),
      spacer(100),

      heading2("Key Teaching Moment"),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "Matthew 6:21: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "'Where your treasure is, there your heart will be also.' Treasure leads and the heart follows. Which means how you handle money is shaping your heart right now — in ordinary weeks, in unremarkable decisions. That's not meant to make you paranoid. It's meant to make you intentional.", size: 22, italics: true, color: DARK, font: "Arial" })] })
      ], LIGHT_BLUE, NAVY),
      spacer(80),

      heading2("Parent Guide — Session 3"),
      bodyText("What your student is learning: That money is more than a practical tool — it's doing something spiritual. It reveals what they trust, it forms contentment through seasons, and it can be a visible testimony to something different."),
      bodyText("One question for dinner: 'What's one thing you spent money on recently that you're glad you did — and one thing you kind of regret? What does each one say about what you value?'"),
      bodyText("One action: Share one category from your family's spending this month — together, honestly. Ask: does this reflect what we say we value? No judgment. Just curiosity."),
      bodyText("Prayer: Father, let our financial lives — as a family — be a quiet testimony to the world that you are enough. Amen."),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== SESSION 4 =====
      sessionHeader("4", "What Faithful Looks Like", "Stewardship in Real Life — The Daily Return", "Stewardship is not a one-time decision. It is a daily return.", "Colossians 1:16–17; 1 Corinthians 4:2; Luke 16:10"),
      spacer(120),

      heading2("Adult Devotional Connection"),
      bodyText("Drawn from Day 7 (the daily reset / you're different not better) and Section II of the adult outline (The Stewardship Question — Days 8–14). The physician-and-CEO pair from Day 7 is the anchor story. The steward-vs.-owner question set is the formation framework. For students: stewardship isn't dramatic. It's the small daily choices — what you buy, what you don't, what you give before you plan the rest."),
      spacer(100),

      heading2("Session Flow (60–75 Minutes)"),
      flowTable([
        { time: "10 min", label: "Icebreaker", detail: "The Enough Game: Write down a number — the amount of money per month that would feel like 'enough.' Don't share the number. Then ask: where did that number come from? What would change above it? What would change below it? Debrief: Is 'enough' a number or something else?" },
        { time: "3 min", label: "Student Story Video", detail: "The Second-Generation Steward, continued — or a new student who can speak to the daily rhythm: what does it look like to actually live like a steward when no one is watching?" },
        { time: "2 min", label: "Leader Bridge", detail: "'Ron Blue had two clients — a physician who drove a Honda and parked down the street from the physician's lot. And a CEO who chose to live in a trailer park. They made completely different choices — but they got there the same way. On their knees, asking God what enough looks like for them.'" },
        { time: "10 min", label: "Teaching", detail: "A steward asks different questions than an owner. Owner: How do I protect what's mine? Steward: How do I honor God with what's entrusted to me? Owner: How do I stay in control? Steward: What is the next faithful step? Small things count (Luke 16:10): The person who can't be trusted with small amounts won't suddenly become trustworthy with large ones. Faithfulness isn't a special occasion. It's built one ordinary decision at a time. The Daily Return: You will drift. Everyone does. The goal isn't to eliminate drift — it's to return faster. One sentence before the day starts. One pause before a decision. One prayer when the grip tightens." },
        { time: "15 min", label: "Small Groups", detail: "Discussion Questions: (1) What's the difference between faithful and perfect? Can you think of a moment when you were faithful but it didn't work out perfectly? (2) The physician traded his Porsche for a Honda and parked down the street. That was a public, visible choice that cost him status. What would a similar choice look like in your world? (3) What's one 'next faithful step' in your financial life right now — not the whole plan, just the next thing?" },
        { time: "8 min", label: "Live-It-Out Challenge", detail: "The Morning Return practice: For the next seven days, before you check your phone, pray one sentence: 'God, you own it all. Lead me today.' Then take one small faithful step — not a perfect plan, just the next thing. Write down what happens." },
        { time: "5 min", label: "Closing Prayer", detail: "Declaration: 'God, you are the Owner. I am your steward. Today I will practice open hands, take the next faithful step, and trust you to hold what I cannot.'" },
      ]),
      spacer(80),

      heading2("Parent Guide — Session 4"),
      bodyText("What your student is learning: What faithful actually looks like day-to-day — the small decisions, the daily return, the choice to ask 'what would a steward do?' before every financial move."),
      bodyText("One question for dinner: 'What would it look like for us — as a family — to make one decision this week that reflects 'enough is enough' rather than always wanting the next thing?'"),
      bodyText("One action: Together, name one area of your family's finances where you're practicing faithfulness — not perfection, but faithfulness. Celebrate it briefly."),
      bodyText("Prayer: Father, teach us what faithful looks like in the ordinary day. Amen."),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== SESSION 5 =====
      sessionHeader("5", "Enough Is a Spiritual Word", "Contentment vs. Culture — How to Break the Comparison Loop", "Contentment is not a personality type. It is a formation outcome.", "Philippians 4:11–13; 1 Timothy 6:6; Hebrews 13:5"),
      spacer(120),

      heading2("Adult Devotional Connection"),
      bodyText("Drawn from Sections III–IV of the adult outline (The Confidence Question and The Contentment Question — Days 15–28). The 'learning' language from Philippians 4:11 ('I have learned to be content') is central — contentment is practiced and formed, not felt naturally. The prosperity paradox (more options, more restlessness) and comparison as a thief are the cultural pressure points for students."),
      spacer(100),

      heading2("Session Flow (60–75 Minutes)"),
      flowTable([
        { time: "10 min", label: "Icebreaker", detail: "The Comparison Spiral: Show students two identical pairs of shoes — one is $40, one is $200. Ask: Would you rather have the $40 pair or the $200 pair? Now: Would your answer change if nobody knew which one you had? What does that tell you? (This is not about shoes. It's about why you want what you want.)" },
        { time: "3 min", label: "Student Story Video", detail: "A new story: a student who unfollowed certain accounts for one month and noticed something shift. The comparison loop — once you see it, you can't unsee it." },
        { time: "2 min", label: "Leader Bridge", detail: "'Paul says in Philippians that he learned to be content. Not that he felt it. Not that his circumstances got easier. He learned it. That means it's a skill. And that means you can actually get better at it.'" },
        { time: "10 min", label: "Teaching", detail: "Contentment is not a mood — it's a formation outcome. Paul learned it through seasons of need and plenty. The comparison trap: Comparison 2:10 — 'When they measure themselves by themselves and compare themselves with themselves, they are not wise.' Comparison doesn't just produce envy. It produces a moving finish line. The prosperity paradox: more options, more restlessness. The person with the most choices often has the least peace. 'Enough' is a spiritual decision, not a financial number. You don't find it — you decide it. And you have to decide it before the culture decides it for you." },
        { time: "15 min", label: "Small Groups", detail: "Discussion Questions: (1) What's the most recent thing you saw someone else have that made you feel like you had less? What did that feeling tell you? (2) If contentment is learned, not felt — where are you in the learning curve? What season of life or situation is teaching you right now? (3) What would it look like to decide what 'enough' means for you — before the culture decides it for you?" },
        { time: "8 min", label: "Live-It-Out Challenge", detail: "The Gratitude Warfare practice: Every morning this week, before you open any social media, name three things you have that you didn't create. Say them out loud. Then open your phone. Track whether it changes how you feel looking at it." },
        { time: "5 min", label: "Closing Prayer", detail: "Declaration: 'Father, teach me what enough looks like for me. Free me from the comparison spiral. I choose contentment — not because I have everything I want, but because you are enough and I belong to you.'" },
      ]),
      spacer(80),

      heading2("Parent Guide — Session 5"),
      bodyText("What your student is learning: That contentment is a skill that gets practiced and formed — not a feeling that arrives when you finally have enough. And that comparison is one of the most powerful forces eroding it."),
      bodyText("One question for dinner: 'Is there something you've wanted lately mostly because someone else has it — or mostly because it would genuinely make your life better? How can you tell the difference?'"),
      bodyText("One action: As a family, go through one month of purchases and name one thing you're glad you bought and one thing that was mostly comparison-driven. No shame — just honesty."),
      bodyText("Prayer: God, teach our family to define enough by what you've given us — not by what everyone around us has. Amen."),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== SESSION 6 =====
      sessionHeader("6", "Open Hands", "Generosity & Who You're Becoming — The Finish Line of the Series", "Generosity is not a discipline you master. It is a person you become.", "2 Corinthians 9:6–8; Matthew 6:21; Luke 12:34"),
      spacer(120),

      heading2("Adult Devotional Connection"),
      bodyText("Drawn from Sections V–VI of the adult outline (The Generosity Question and The Impact Question — Days 29–42). The God-is-the-first-giver framing, the treasure-leads-the-heart principle, and the whole-life generosity arc are the theological core. For students: the session closes the six-week arc by asking the identity question from the other direction — not 'what do you have?' but 'who are you becoming?' Open hands is the posture that produces all of it."),
      spacer(100),

      heading2("Session Flow (60–75 Minutes)"),
      flowTable([
        { time: "10 min", label: "Icebreaker", detail: "The Open / Closed Hand Demo: Have every student make a fist. Then open their hand flat. Ask: What can you hold in a closed fist? What can you receive with an open hand? What can you give with an open hand? The open-vs.-closed hand is the physical picture of this entire series." },
        { time: "3 min", label: "Student Story Video", detail: "The Shoes I Didn't Buy — the full arc. Saved for three months. Felt the nudge. Gave part of it. Shoes didn't happen. Something shifted. 'I realized I wasn't giving away my money — I was just using what God trusted me with to help someone else.' This is the testimony close." },
        { time: "2 min", label: "Leader Bridge", detail: "'That line — I was just using what God trusted me with — that's what six weeks of this has been building toward. Not a rule about giving. Not guilt. A different kind of person. Let me show you where this ends up.'" },
        { time: "10 min", label: "Teaching", detail: "God is the first giver: The entire generosity conversation starts at the gospel — John 3:16 and Romans 8:32. God gave first. Generosity is a response, not a discipline. Open hands produce open hearts: Matthew 6:21 says where your treasure goes, your heart follows. Which means giving isn't just about the money. It changes you. Whole-life generosity: It's not just money. It's time, attention, influence, kindness — the posture of a person whose hands are open because they trust the Owner. Who are you becoming? The physician who parked down the street. The CEO in the trailer park. Two completely different lives. Same posture: on their knees, asking God what enough looks like for them. Both were free." },
        { time: "15 min", label: "Small Groups", detail: "Discussion Questions: (1) Think about someone you know who gives generously — not just money, but time, attention, energy. What is it about them that makes it obvious? (2) If treasure leads and heart follows — where do you want your heart to end up? What would it mean to redirect some of your treasure there? (3) Looking at the last six sessions: what's the one thing that changed most about how you think about money, stuff, or your identity?" },
        { time: "8 min", label: "Live-It-Out Challenge", detail: "The Open Hand Decision: This week, do one thing with your money that you'd normally keep for yourself — and give it away without anyone knowing. It doesn't have to be large. It just has to be intentional. Then reflect: What did it feel like?" },
        { time: "5 min", label: "Closing Prayer / Series Close", detail: "Leader reads the full series declaration aloud, students repeat phrase by phrase: 'God, you are the Owner. I am your steward. I am different because of whose I am — not better, different. Teach me open hands, a steady heart, and faithful obedience. I belong to you. Amen.'" },
      ]),
      spacer(100),

      heading2("Series Closing: The Invitation"),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "Invite students to write one sentence on a card: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "'Because God owns it all, one thing I'm going to do differently is ___.' Collect the cards. Consider sharing them anonymously at a parent gathering or follow-up event. These sentences are the fruit of the series.", size: 22, color: DARK, font: "Arial" })] })
      ], LIGHT_GOLD, GOLD),
      spacer(80),

      heading2("Parent Guide — Session 6"),
      bodyText("What your student is learning: That generosity is the natural overflow of a life with open hands — and that the posture of a steward produces a kind of freedom that hoarding never can."),
      bodyText("One question for dinner: 'What's one thing our family could do together in the next month that reflects open hands — giving something away (money, time, attention) that costs us something?'"),
      bodyText("One action: As a family, choose one act of generosity to do together before the end of the month. Plan it at dinner tonight."),
      bodyText("Prayer: Father, make our family known for open hands. Not perfectly — but consistently. Let generosity be the word people use to describe us. Amen."),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== PRODUCTION STRATEGY =====
      heading1("Production & Deployment Strategy"),
      divider(),
      spacer(80),

      heading2("Video Architecture"),
      bodyText("Each session requires two video assets: a student story (2–3 min) and a teaching segment (8–10 min). These are designed to be filmed in a concentrated production block and deployed across multiple settings."),
      spacer(80),

      twoColTable(
        "Student Story Videos", [
          "Interview format — seated, relaxed, simple background",
          "Guided authentic: student reads story, retells in own words",
          "Open with: 'This is based on a real situation…' OR natural first-person",
          "2–3 minutes maximum — leave room for teaching",
          "Film 15–20 students at one Saturday session, 2–3 stations simultaneously",
          "Build a 30–40 clip story library — assign in editing, not during filming"
        ],
        "Teaching Segments", [
          "Young youth pastor, 28–40, direct to camera, conversational",
          "8–10 minutes maximum — not a sermon, a guide",
          "Simple background, minimal cuts, slightly imperfect is fine",
          "One teacher per series (3 teachers total for 3 series)",
          "Batch all teaching on Day 1–2 of shoot before student filming",
          "Script outline + key points provided — not word-for-word script"
        ]
      ),
      spacer(100),

      heading2("Session Format Options"),
      bodyText("The curriculum is designed to run in three deployment environments. Youth leaders choose the format that fits their setting — the content is identical, only the timing and energy level adjust."),
      spacer(60),

      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2000, 2480, 2440, 2440],
        borders: { insideH: border, insideV: { style: BorderStyle.NONE }, top: border, bottom: border, left: border, right: border },
        rows: [
          new TableRow({ children: [
            new TableCell({ width: { size: 2000, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders, children: [new Paragraph({ children: [new TextRun({ text: "Element", bold: true, size: 20, color: WHITE, font: "Arial" })] })] }),
            new TableCell({ width: { size: 2480, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders, children: [new Paragraph({ children: [new TextRun({ text: "Midweek Youth Night (75 min)", bold: true, size: 20, color: GOLD, font: "Arial" })] })] }),
            new TableCell({ width: { size: 2440, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders, children: [new Paragraph({ children: [new TextRun({ text: "Sunday Morning (45 min)", bold: true, size: 20, color: GOLD, font: "Arial" })] })] }),
            new TableCell({ width: { size: 2440, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, borders, children: [new Paragraph({ children: [new TextRun({ text: "Small Group (60 min)", bold: true, size: 20, color: GOLD, font: "Arial" })] })] }),
          ]}),
          ...[
            ["Energy", "High — game, video, full flow", "Moderate — discussion-heavy", "Conversational — peer-led"],
            ["Icebreaker", "10 min", "Optional / 5 min", "5 min"],
            ["Story Video", "3 min", "3 min", "3 min"],
            ["Teaching", "10 min video", "10 min video", "8 min video or live"],
            ["Discussion", "15 min small groups", "20 min full group", "25 min"],
            ["Challenge + Prayer", "8 min", "5 min", "5 min"],
          ].map((row, i) => new TableRow({ children: row.map((cell, j) => new TableCell({
            width: { size: [2000, 2480, 2440, 2440][j], type: WidthType.DXA },
            shading: { fill: i % 2 === 0 ? WHITE : LIGHT_GRAY, type: ShadingType.CLEAR },
            margins: { top: 60, bottom: 60, left: 120, right: 120 },
            borders,
            children: [new Paragraph({ children: [new TextRun({ text: cell, size: 20, color: DARK, font: "Arial", bold: j === 0 })] })]
          })) }))
        ]
      }),
      spacer(100),

      heading2("Storytelling Integrity Guide for Youth Pastors"),
      bodyText("Youth leaders who want to tell student stories with integrity — without claiming a story as their own — have three clean options:"),
      spacer(60),
      bullet("\"A student I know recently…\" — specific enough to feel real, protects identity, doesn't feel scripted"),
      bullet("\"This is the kind of situation a lot of students face…\" — universal story, every student sees themselves in it"),
      bullet("\"As leaders, we see this all the time…\" — pastoral perspective, builds credibility"),
      spacer(60),
      bodyText("When a student reads a story that isn't theirs on video, the gold standard opening is: 'This is based on a real situation a student went through…' Then tell it naturally. The honesty builds trust rather than eroding it."),
      spacer(100),

      heading2("The Whole-Church Alignment Model"),
      bodyText("This curriculum is designed to run in parallel with the adult 40-day devotional. When all three tracks run simultaneously — adults in the devotional, students in this 6-session curriculum, children in the simplified age-based version — the church family is processing the same question at the same depth across every generation. Parents who are doing the adult devotional are already living inside the same theology their students are discussing on Wednesday night. That alignment doesn't require anyone to do more work. It just requires the tracks to run at the same time."),
      spacer(60),
      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "Positioning statement: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: '"We help your entire church — from kids to students to adults — grow through the same message, at the same time, in a way each age can understand and live out."', size: 22, italics: true, color: DARK, font: "Arial" })] })
      ], LIGHT_BLUE, NAVY),

      new Paragraph({ children: [new PageBreak()] }),

      // ===== NEXT STEPS =====
      heading1("Next Steps"),
      divider(),
      spacer(80),
      bodyText("This document provides the 6-session curriculum framework, production strategy, testimonial profiles, and Ron Blue integration map. The following steps move it from framework to finished product:"),
      spacer(80),

      subheading("Immediate (Curriculum Development)"),
      bullet("Write the weekly student devotionals for Sessions 1–6 (7 days each = 42 devotionals total), following the voice and format of the existing GOIA Days 1–7 adult draft"),
      bullet("Develop the leader guide for each session (full word-for-word teaching script + transition lines)"),
      bullet("Write the parent guide for each session (1-page format + parent video script)"),
      bullet("Finalize the student story scripts for the three testimonial profiles identified above"),
      spacer(60),

      subheading("Production"),
      bullet("Recruit 3 youth pastor communicators (one per series if expanding to 3 series)"),
      bullet("Identify 15–20 student participants for the story capture session"),
      bullet("Schedule a 2–3 day shoot: Day 1–2 teaching, Day 2–3 student stories"),
      bullet("Film Ron Blue's opening cameo and leader training series (separate shorter shoot)"),
      spacer(60),

      subheading("When Additional Adult Devotional Days Are Available"),
      bullet("Days 8–14 (Section II: Stewardship) will expand and deepen Session 4"),
      bullet("Days 15–28 (Sections III–IV) provide additional teaching content for Sessions 5 and a potential Session 7"),
      bullet("Days 29–42 (Sections V–VI) complete the generosity and impact arc for Session 6 and beyond"),
      spacer(80),

      colorBox([
        new Paragraph({ spacing: { before: 20, after: 20 }, children: [new TextRun({ text: "Note: ", bold: true, size: 22, color: NAVY, font: "Arial" }), new TextRun({ text: "The framework presented here is built from the existing Days 1–7 adult draft plus the adult 40-day outline. As additional days of the devotional are completed, the session content, discussion questions, and teaching points in Sessions 4–6 should be revisited and deepened to reflect the full manuscript.", size: 22, color: DARK, font: "Arial" })] })
      ], LIGHT_GOLD, GOLD),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/GOIA_Youth_Edition_6Session_Curriculum.docx', buffer);
  console.log('Done');
});
