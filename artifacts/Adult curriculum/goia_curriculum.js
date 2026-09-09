const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageBreak, LevelFormat
} = require('docx');
const fs = require('fs');

// Color palette
const NAVY = "1B3A5C";
const TEAL = "0D7680";
const GOLD = "C8973A";
const LIGHT_BLUE = "D5E8F0";
const LIGHT_GOLD = "FFF3DC";
const LIGHT_GRAY = "F2F2F2";
const WHITE = "FFFFFF";
const DARK_GRAY = "333333";
const MED_GRAY = "555555";

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text, font: "Arial", size: 36, bold: true, color: NAVY })],
    spacing: { before: 400, after: 200 },
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun({ text, font: "Arial", size: 26, bold: true, color: TEAL })],
    spacing: { before: 300, after: 120 },
  });
}

function h3(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 22, bold: true, color: NAVY })],
    spacing: { before: 200, after: 80 },
  });
}

function body(text, italic=false, color=DARK_GRAY) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 22, italic, color })],
    spacing: { before: 60, after: 60 },
  });
}

function bodyBold(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 22, bold: true, color: DARK_GRAY })],
    spacing: { before: 60, after: 60 },
  });
}

function scriptureBox(verse, ref) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [new TableRow({
      children: [new TableCell({
        borders,
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
        margins: { top: 160, bottom: 160, left: 240, right: 240 },
        children: [
          new Paragraph({
            children: [new TextRun({ text: `"${verse}"`, font: "Georgia", size: 22, italic: true, color: NAVY })],
            alignment: AlignmentType.CENTER,
          }),
          new Paragraph({
            children: [new TextRun({ text: `— ${ref}`, font: "Arial", size: 20, bold: true, color: TEAL })],
            alignment: AlignmentType.CENTER,
            spacing: { before: 80 },
          }),
        ]
      })]
    })]
  });
}

function colorBox(label, items, fillColor=LIGHT_GOLD) {
  const children = [
    new Paragraph({
      children: [new TextRun({ text: label, font: "Arial", size: 22, bold: true, color: NAVY })],
      spacing: { before: 0, after: 80 },
    }),
    ...items.map(item => new Paragraph({
      numbering: { reference: "bullets", level: 0 },
      children: [new TextRun({ text: item, font: "Arial", size: 21, color: DARK_GRAY })],
      spacing: { before: 40, after: 40 },
    }))
  ];
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [new TableRow({
      children: [new TableCell({
        borders,
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: fillColor, type: ShadingType.CLEAR },
        margins: { top: 140, bottom: 140, left: 240, right: 240 },
        children,
      })]
    })]
  });
}

function qrBox(label, url) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1440, 7920],
    rows: [new TableRow({
      children: [
        new TableCell({
          borders,
          width: { size: 1440, type: WidthType.DXA },
          shading: { fill: NAVY, type: ShadingType.CLEAR },
          margins: { top: 120, bottom: 120, left: 120, right: 120 },
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: "▶ QR", font: "Arial", size: 20, bold: true, color: WHITE })],
          })]
        }),
        new TableCell({
          borders,
          width: { size: 7920, type: WidthType.DXA },
          shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
          margins: { top: 120, bottom: 120, left: 240, right: 240 },
          children: [
            new Paragraph({ children: [new TextRun({ text: label, font: "Arial", size: 22, bold: true, color: NAVY })] }),
            new Paragraph({ children: [new TextRun({ text: `Scan QR code or visit: ${url}`, font: "Arial", size: 20, italic: true, color: TEAL })] }),
          ]
        }),
      ]
    })]
  });
}

function sectionDivider(title, session, theme) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [new TableRow({
      children: [new TableCell({
        borders: { top: border, bottom: border, left: { style: BorderStyle.SINGLE, size: 16, color: GOLD }, right: border },
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: NAVY, type: ShadingType.CLEAR },
        margins: { top: 200, bottom: 200, left: 300, right: 240 },
        children: [
          new Paragraph({ children: [new TextRun({ text: session, font: "Arial", size: 20, color: GOLD })] }),
          new Paragraph({ children: [new TextRun({ text: title, font: "Arial", size: 32, bold: true, color: WHITE })], spacing: { before: 60 } }),
          new Paragraph({ children: [new TextRun({ text: theme, font: "Arial", size: 20, italic: true, color: LIGHT_BLUE })], spacing: { before: 60 } }),
        ]
      })]
    })]
  });
}

function threeColumnTable(label, col1Title, col1Items, col2Title, col2Items, col3Title, col3Items) {
  const colW = 3120;
  function colCell(title, items) {
    return new TableCell({
      borders,
      width: { size: colW, type: WidthType.DXA },
      shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
      margins: { top: 120, bottom: 120, left: 160, right: 160 },
      children: [
        new Paragraph({ children: [new TextRun({ text: title, font: "Arial", size: 21, bold: true, color: TEAL })], spacing: { after: 80 } }),
        ...items.map((item, i) => new Paragraph({
          children: [new TextRun({ text: `${i+1}. ${item}`, font: "Arial", size: 20, color: DARK_GRAY })],
          spacing: { before: 40, after: 40 },
        }))
      ]
    });
  }
  return [
    new Paragraph({ children: [new TextRun({ text: label, font: "Arial", size: 22, bold: true, color: NAVY })], spacing: { before: 200, after: 80 } }),
    new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [colW, colW, colW],
      rows: [new TableRow({ children: [colCell(col1Title, col1Items), colCell(col2Title, col2Items), colCell(col3Title, col3Items)] })]
    })
  ];
}

function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

function spacer() {
  return new Paragraph({ children: [new TextRun("")], spacing: { before: 120, after: 120 } });
}

function timingRow(time, activity) {
  return new TableRow({
    children: [
      new TableCell({
        borders, width: { size: 1440, type: WidthType.DXA },
        shading: { fill: TEAL, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: time, font: "Arial", size: 20, bold: true, color: WHITE })], alignment: AlignmentType.CENTER })]
      }),
      new TableCell({
        borders, width: { size: 7920, type: WidthType.DXA },
        shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 160, right: 160 },
        children: [new Paragraph({ children: [new TextRun({ text: activity, font: "Arial", size: 21, color: DARK_GRAY })] })]
      }),
    ]
  });
}

function timingTable(rows) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1440, 7920],
    rows: rows.map(([t, a]) => timingRow(t, a))
  });
}

// ─── SESSIONS ──────────────────────────────────────────────────────────────

function hostNote(text) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [new TableRow({
      children: [new TableCell({
        borders: { top: border, bottom: border, left: { style: BorderStyle.SINGLE, size: 16, color: GOLD }, right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } },
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
        margins: { top: 120, bottom: 120, left: 240, right: 240 },
        children: [new Paragraph({ children: [
          new TextRun({ text: "HOST NOTE  ", font: "Arial", size: 20, bold: true, color: GOLD }),
          new TextRun({ text, font: "Arial", size: 20, italic: true, color: MED_GRAY }),
        ]})]
      })]
    })]
  });
}

// ─── BUILD DOCUMENT ──────────────────────────────────────────────────────────

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
        run: { size: 36, bold: true, font: "Arial", color: NAVY }, paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: TEAL }, paragraph: { spacing: { before: 300, after: 120 }, outlineLevel: 1 } },
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

      // ─── COVER ───────────────────────────────────────────────────────
      new Paragraph({
        children: [new TextRun({ text: "GOD OWNS IT ALL", font: "Arial", size: 64, bold: true, color: NAVY })],
        alignment: AlignmentType.CENTER,
        spacing: { before: 1440, after: 200 },
      }),
      new Paragraph({
        children: [new TextRun({ text: "6-Session Adult Small Group Curriculum", font: "Arial", size: 32, color: TEAL })],
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 200 },
      }),
      new Paragraph({
        children: [new TextRun({ text: "Based on the Book & Devotional by Ron Blue", font: "Arial", size: 24, italic: true, color: MED_GRAY })],
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 600 },
      }),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [9360],
        rows: [new TableRow({ children: [new TableCell({
          borders: { top: { style: BorderStyle.SINGLE, size: 4, color: GOLD }, bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD }, left: noBorder, right: noBorder },
          width: { size: 9360, type: WidthType.DXA },
          shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
          margins: { top: 200, bottom: 200, left: 360, right: 360 },
          children: [
            new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "\"The earth is the Lord's, and everything in it.\"", font: "Georgia", size: 28, italic: true, color: NAVY })] }),
            new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "— Psalm 24:1", font: "Arial", size: 22, bold: true, color: TEAL })], spacing: { before: 120 } }),
          ]
        })] })]
      }),

      spacer(),
      new Paragraph({
        children: [new TextRun({ text: "SESSION OVERVIEW", font: "Arial", size: 22, bold: true, color: NAVY })],
        spacing: { before: 400, after: 120 },
        alignment: AlignmentType.CENTER,
      }),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [1440, 4000, 3920],
        rows: [
          new TableRow({ children: [
            new TableCell({ borders, width: { size: 1440, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Session", font: "Arial", size: 20, bold: true, color: WHITE })] })] }),
            new TableCell({ borders, width: { size: 4000, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Title", font: "Arial", size: 20, bold: true, color: WHITE })] })] }),
            new TableCell({ borders, width: { size: 3920, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Book Chapters / Devotional Days", font: "Arial", size: 20, bold: true, color: WHITE })] })] }),
          ]}),
          ...[
            ["1", "Perspective — Who Owns It?", "Ch. 1 | Devotional Days 1–7"],
            ["2", "Principles — Five Ways to Use Money", "Ch. 2 | Devotional Days 8–14"],
            ["3", "Live — Spend Less Than You Earn", "Ch. 3 | Devotional Days 15–21"],
            ["4", "Give — Generosity That Transforms", "Ch. 4 | Devotional Days 22–28"],
            ["5", "Owe — Freedom from Debt", "Ch. 5 | Devotional Days 29–35"],
            ["6", "Grow — Building with Kingdom Purpose", "Ch. 6 | Devotional Days 36–40"],
          ].map(([num, title, reading], idx) => new TableRow({ children: [
            new TableCell({ borders, width: { size: 1440, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: num, font: "Arial", size: 20, bold: true, color: NAVY })] })] }),
            new TableCell({ borders, width: { size: 4000, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: title, font: "Arial", size: 20, color: DARK_GRAY })] })] }),
            new TableCell({ borders, width: { size: 3920, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: reading, font: "Arial", size: 20, italic: true, color: MED_GRAY })] })] }),
          ]}))
        ]
      }),

      pageBreak(),

      // ─── HOW TO USE ───────────────────────────────────────────────────
      h1("HOW TO USE THIS CURRICULUM"),
      body("This guide is designed to be plug-and-play. You do not need to be a financial expert, a theologian, or a seasoned small group leader to host these sessions. If you love people and you're willing to show up, you can lead this group."),
      spacer(),
      h3("WHAT PARTICIPANTS SHOULD DO BETWEEN SESSIONS"),
      colorBox("Each week, participants should complete the following before meeting:", [
        "Read the assigned chapters in the God Owns It All book",
        "Complete the corresponding daily devotional entries (listed in each session)",
        "Bring their book, devotional, and any notes or questions to the group",
        "Come ready to share — no pressure, but openness makes the group richer",
      ]),
      spacer(),
      h3("WHAT THE HOST DOES"),
      colorBox("Your role is to facilitate, not lecture. That means:", [
        "Arrive 10 minutes early to set up and pray",
        "Choose your icebreaker, discussion questions, and group activity before the meeting",
        "Keep an eye on the clock using the suggested timing guide in each session",
        "Encourage everyone to share — gently redirect if one person dominates",
        "Read the Host Notes (highlighted in gold) for extra guidance",
        "End on time and with prayer",
      ], LIGHT_GOLD),
      spacer(),
      h3("FORMAT AT A GLANCE"),
      timingTable([
        ["0–10 min", "Welcome & Icebreaker (choose one of three options)"],
        ["10–20 min", "Key Concept Review (brief teaching from the book/devotional)"],
        ["20–45 min", "Group Discussion Questions"],
        ["45–60 min", "Group Activity (choose one of three options)"],
        ["60–70 min", "Closing Reflection, Prayer, and Weekly Challenge"],
      ]),
      spacer(),
      body("Sessions are designed for 60–75 minutes. You can shorten or extend based on your group's energy and needs.", true),

      pageBreak(),

      // ─────────────────────────── SESSION 1 ───────────────────────────
      sectionDivider("SESSION 1", "WEEK ONE", "PERSPECTIVE — WHO OWNS IT?"),
      spacer(),
      h3("THIS WEEK'S READING"),
      body("Book: Chapter 1 (Perspective)   |   Devotional: Days 1–7"),
      spacer(),
      scriptureBox("The earth is the Lord's, and everything in it, the world, and all who live in it.", "Psalm 24:1 (NIV)"),
      spacer(),
      h3("BIG IDEA"),
      body("The most foundational question every Christian must answer about money is not 'How much do I have?' but 'Who does it belong to?' When God's ownership becomes our foundation, it changes not just our finances but our contentment, our confidence, and our communication."),
      spacer(),
      hostNote("Ron Blue says: 'Every financial decision is a spiritual decision.' This session sets the theological foundation for everything that follows. Don't rush it. Let people sit with the ownership question."),
      spacer(),
      h3("KEY CONCEPTS FROM THE BOOK & DEVOTIONAL"),
      colorBox("This week participants encountered:", [
        "God owns everything — Psalm 24:1, 1 Chronicles 29:14, Psalm 50:9-12",
        "The three wrong questions: Will I have enough? Will it last? How much is enough?",
        "The three right questions: Who owns it? How much is enough (as stewardship)? Is the next steward chosen?",
        "Behavior always follows belief — our financial habits reveal our theology",
        "Stewardship vs. ownership: owners have rights; stewards have responsibilities",
        "Ron's 5 money management principles: Spend less than you earn, Give generously, Avoid debt, Build margin, Set long-term goals",
      ]),
      spacer(),
      ...threeColumnTable("ICEBREAKER — Choose One (5–7 minutes)",
        "Option A — Light & Fun",
        ["If your wallet could talk, what's the most embarrassing thing it would say about you?", "What's the best money-related advice you ever received — and did you follow it?"],
        "Option B — Reflective",
        ["What's your earliest money memory — something that shaped how you think about it today?", "Growing up, was money in your home a source of stress, security, or something else?"],
        "Option C — Direct",
        ["What's one financial fear you've carried for a long time?", "On a scale of 1-10, how much would you say money affects your daily peace? Why?"]
      ),
      spacer(),
      h3("DISCUSSION QUESTIONS"),
      hostNote("You won't get through all of these. Choose 3–4 that feel right for your group. Start with easier ones and move toward deeper ones as trust builds."),
      colorBox("Work through these together:", [
        "Ron Blue spent his career helping people manage money, yet he says the real issue isn't financial — it's a 'Who owns it?' question. Why do you think that question matters so much?",
        "Read Psalm 24:1 aloud. What does it feel like, emotionally, to really believe that statement about your home, your paycheck, your savings?",
        "What's the difference between acting like an owner versus acting like a steward? Can you think of a recent financial decision where the distinction would have mattered?",
        "The devotional talks about 'ownership drift' — the slow, invisible shift from 'I'm managing this for God' to 'this is mine.' Where do you notice that drift most in your own life?",
        "Ron says contentment, confidence, and communication with a spouse all change when we settle the ownership question. Which of those three do you most need to see change?",
        "Day 1 of the devotional says: 'Behavior follows belief.' What does your financial behavior right now reveal about what you actually believe?",
      ]),
      spacer(),
      ...threeColumnTable("GROUP ACTIVITY — Choose One (10–15 minutes)",
        "Option A — The Ownership Inventory",
        ["Give everyone a piece of paper. Write at the top: 'Things I call mine.'", "List possessions, income, savings, relationships, talents — anything you consider 'yours.'", "Then silently circle what you'd have the hardest time releasing. Discuss: What does that tell you?"],
        "Option B — The 3 Questions Audit",
        ["Write the 3 wrong questions and 3 right ones on a whiteboard or paper.", "As a group, discuss: Which of the 'wrong' questions drives most financial decisions in our culture?", "Which of the 'right' questions is hardest to keep in view? Why?"],
        "Option C — Sign the Stewardship Statement",
        ["Read this from the book: 'I acknowledge God's ownership of my time, talents, treasure, relationships, influence, and all other resources...'", "Invite anyone willing to sign it — in their own book or on paper.", "Share briefly: What feels different about signing this vs. just knowing it?"]
      ),
      spacer(),
      qrBox("Watch: Ron Blue — Session 1 Video Teaching (Perspective)", "ronblueinstitute.com/goia"),
      spacer(),
      h3("WEEKLY CHALLENGE"),
      colorBox("Before next week's session, choose one of these:", [
        "OPTION A: Each morning this week, before any financial decision, pause and say: 'God, you're the Owner. Lead me.' Write down what shifts.",
        "OPTION B: Pick one area of your finances and actually pray over it — don't just think about it. Ask God what faithfulness looks like in that specific area.",
        "OPTION C: Have a 'stewardship conversation' with your spouse or a trusted friend. Ask: 'Where are we living like owners? Where are we living like stewards?'",
      ]),
      spacer(),
      h3("CLOSING PRAYER"),
      body("Close your time with this prayer (read aloud together or have the host pray):"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [9360],
        rows: [new TableRow({ children: [new TableCell({
          borders,
          width: { size: 9360, type: WidthType.DXA },
          shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
          margins: { top: 160, bottom: 160, left: 240, right: 240 },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Father, you are the source of every good gift. Forgive us for the ways we've lived like everything depends on us. Today we return to the foundation: everything is from you, through you, and for you. Teach us to live with open hands — not passive, but trusting. You are the Owner, and we are yours. Amen.", font: "Georgia", size: 22, italic: true, color: NAVY })] })]
        })]})
      }),

      pageBreak(),

      // ─────────────────────────── SESSION 2 ───────────────────────────
      sectionDivider("SESSION 2", "WEEK TWO", "PRINCIPLES — FIVE WAYS TO USE MONEY"),
      spacer(),
      h3("THIS WEEK'S READING"),
      body("Book: Chapter 2 (Principles)   |   Devotional: Days 8–14"),
      spacer(),
      scriptureBox("Moreover, it is required of stewards that they be found faithful.", "1 Corinthians 4:2 (ESV)"),
      spacer(),
      h3("BIG IDEA"),
      body("If God owns it all, then how we use money is a matter of faithfulness. This week introduces a simple framework: every dollar goes somewhere in four categories — Live, Give, Owe, Grow. Understanding your current pie — and asking whether it reflects your values — is the beginning of financial discipleship."),
      spacer(),
      hostNote("The Pie Chart exercise tends to be the most eye-opening activity in this entire curriculum. Be prepared for some quiet moments. Let people process. This isn't about shame — it's about clarity."),
      spacer(),
      h3("KEY CONCEPTS FROM THE BOOK & DEVOTIONAL"),
      colorBox("This week participants encountered:", [
        "The Five Money Management Principles: (1) Spend less than you earn, (2) Avoid debt, (3) Build margin, (4) Set long-term goals, (5) Give generously",
        "The Four Uses of Money: Live (lifestyle), Give (generosity), Owe (debt + taxes), Grow (saving + investing)",
        "The Treasure Target tool — four quadrants, three levels each — showing the path to financial freedom",
        "Behavior always follows belief — principles must be rooted in conviction, not willpower",
        "Biblical wisdom about money is transcendent and works at every income level",
      ]),
      spacer(),
      ...threeColumnTable("ICEBREAKER — Choose One (5–7 minutes)",
        "Option A — Light & Fun",
        ["Would you rather have a 20% pay raise or a 20% reduction in your monthly expenses? Why?", "What's the most creative way you've ever saved money?"],
        "Option B — Reflective",
        ["What financial principle did you grow up with — spoken or unspoken?", "If you had to guess what percentage of your income goes to 'Live' vs. 'Give,' what would you say?"],
        "Option C — Direct",
        ["Is there one area of your finances you tend to avoid looking at? What keeps you from looking?", "On the Treasure Target, where do you instinctively feel you are right now?"]
      ),
      spacer(),
      h3("DISCUSSION QUESTIONS"),
      colorBox("Work through these together:", [
        "Ron testified before Congress and gave four principles. The senator said they'd work at any income level. What makes these principles so durable across very different financial situations?",
        "Look at the four categories: Live, Give, Owe, Grow. Without getting into exact numbers, which category do you feel is out of balance in your life right now?",
        "1 Corinthians 4:2 says stewards are required to be 'found faithful.' What does faithfulness look like when your income is limited or your debt feels overwhelming?",
        "Ron says these principles only work if they're built on the right foundation. What does that mean practically? How does motivation change the same behavior?",
        "The Treasure Target moves from the outer rings (struggling) toward the center (financial freedom). Where do you currently see yourself? What's the next level?",
        "The devotional this week explored the idea that financial principles are a form of worship. Does that reframe them for you? How so?",
      ]),
      spacer(),
      ...threeColumnTable("GROUP ACTIVITY — Choose One (10–15 minutes)",
        "Option A — The Pie Diagram",
        ["Using the Live/Give/Owe/Grow Worksheet, estimate your current percentages.", "Draw your personal pie on paper.", "Share: Does your pie reflect your actual values? What would your 'ideal' pie look like?"],
        "Option B — The Treasure Target Check-in",
        ["Look at the Treasure Target diagram together.", "Individually, mark where you currently are in each quadrant (Live, Give, Owe, Grow).", "Share one quadrant where you'd like to move one level deeper in the next year."],
        "Option C — The 5 Principles Quiz",
        ["Host reads each principle. Group votes: 'We're doing well,' 'This is a struggle,' or 'We've never tried this.'", "Discuss: Which principle would make the biggest difference if your whole group committed to it?", "Pray specifically over that one principle together."]
      ),
      spacer(),
      qrBox("Watch: Ron Blue — Session 2 Video Teaching (Principles)", "ronblueinstitute.com/goia"),
      spacer(),
      h3("WEEKLY CHALLENGE"),
      colorBox("Before next week's session, choose one:", [
        "OPTION A: Complete the Live/Give/Owe/Grow worksheet with your actual numbers. Bring it next week — you don't have to share specifics, but come ready to discuss what you noticed.",
        "OPTION B: Identify which of the five principles feels most countercultural to you. Write down why — and what it would cost you to practice it more consistently.",
        "OPTION C: Have one 'money values' conversation with your spouse or an accountability partner. Ask: 'Does how we spend money reflect what we say matters most to us?'",
      ]),
      spacer(),
      h3("CLOSING PRAYER"),
      new Table({
        width: { size: 9360, type: WidthType.DXA }, columnWidths: [9360],
        rows: [new TableRow({ children: [new TableCell({
          borders, width: { size: 9360, type: WidthType.DXA },
          shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
          margins: { top: 160, bottom: 160, left: 240, right: 240 },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Lord, you have given us everything we need. Help us to be faithful with what you've entrusted to us — not out of obligation, but out of love. Give us clarity about how we're using your resources, and courage to align our spending with our convictions. You are the Owner; teach us to be trustworthy stewards. Amen.", font: "Georgia", size: 22, italic: true, color: NAVY })] })]
        })]})
      }),

      pageBreak(),

      // ─────────────────────────── SESSION 3 ───────────────────────────
      sectionDivider("SESSION 3", "WEEK THREE", "LIVE — SPENDING LESS THAN YOU EARN"),
      spacer(),
      h3("THIS WEEK'S READING"),
      body("Book: Chapter 3 (Live)   |   Devotional: Days 15–21"),
      spacer(),
      scriptureBox("But godliness with contentment is great gain. For we brought nothing into the world, and we can take nothing out of it.", "1 Timothy 6:6–7 (NIV)"),
      spacer(),
      h3("BIG IDEA"),
      body("Spending less than you earn sounds simple. It isn't. Culture's relentless pressure to consume more, upgrade more, and keep up with more makes lifestyle the hardest quadrant to control. This week explores the Prosperity Paradox — the counterintuitive truth that more doesn't produce contentment — and asks the honest question: How much is enough?"),
      spacer(),
      hostNote("This session often surfaces strong emotions — guilt, comparison, even grief over past decisions. Create a safe environment. Remind the group that the goal is not judgment but awareness and freedom."),
      spacer(),
      h3("KEY CONCEPTS FROM THE BOOK & DEVOTIONAL"),
      colorBox("This week participants encountered:", [
        "The Prosperity Paradox: increasing wealth often produces more fear, not more peace — because the stakes feel higher",
        "'How much is enough?' as a stewardship question, not a scarcity question",
        "Setting a 'Lifestyle Finish Line' — a conscious decision about how much is enough to live on",
        "The Treasure Target: Level 1 (track spending) → Level 2 (create a plan) → Level 3 (set a lifestyle finish line)",
        "Provision vs. protection: God provides; our job is to steward faithfully, not hoard fearfully",
        "Contentment is not the same as complacency — it's freedom from the tyranny of 'more'",
      ]),
      spacer(),
      ...threeColumnTable("ICEBREAKER — Choose One (5–7 minutes)",
        "Option A — Light & Fun",
        ["What's something you bought that you were totally convinced you needed — and never used?", "What's the most satisfying 'I didn't buy that' decision you've ever made?"],
        "Option B — Reflective",
        ["What does 'enough' look like to you right now? Could you define it in one sentence?", "Have you ever experienced a season of less that surprisingly brought more peace? What was that like?"],
        "Option C — Direct",
        ["What's the biggest lifestyle pressure you feel — from culture, social media, or people around you?", "If you were completely honest, is your lifestyle driven more by your values or by what those around you expect?"]
      ),
      spacer(),
      h3("DISCUSSION QUESTIONS"),
      colorBox("Work through these together:", [
        "Ron calls it the 'Prosperity Paradox' — the richer people get, the more financial anxiety they often experience. Have you seen this in your own life or in others? Why do you think more doesn't equal more peace?",
        "The book asks: 'How much is enough?' Not as a rhetorical question — as a real one you're supposed to answer. How would you answer it right now? What makes the question hard?",
        "Setting a 'Lifestyle Finish Line' is a radical idea. What would it mean for you to consciously decide that your lifestyle is 'enough' — and to stop expanding it as income grows?",
        "1 Timothy 6:6 says godliness with contentment is 'great gain.' In a culture that defines gain as accumulation, how does that verse land for you?",
        "The devotional this week drew a distinction between trusting God's provision and trusting your own protective measures. Where is the line? How do you personally find that balance?",
        "What would change in your life — practically and emotionally — if you truly had a settled answer to 'How much is enough?'",
      ]),
      spacer(),
      ...threeColumnTable("GROUP ACTIVITY — Choose One (10–15 minutes)",
        "Option A — Define Your Enough",
        ["On paper, each person writes their current monthly lifestyle expenses.", "Then write what 'enough' would look like for your season of life.", "Discuss: Is there a gap? What's filling it — genuine needs, or lifestyle inflation?"],
        "Option B — The Contentment Timeline",
        ["On a single sheet, draw a timeline of your adult life. Mark financial highs and lows.", "Then mark your contentment level at each point. Is there a correlation?", "Share what you noticed. Did money = contentment? What else mattered?"],
        "Option C — The Finish Line Conversation",
        ["Discuss as a group: What would it take for you to say, 'Our lifestyle is enough — any extra goes elsewhere'?", "What are the obstacles to setting that finish line?", "Pray for one another specifically around the area of contentment."]
      ),
      spacer(),
      qrBox("Watch: Ron Blue — Session 3 Video Teaching (Live)", "ronblueinstitute.com/goia"),
      spacer(),
      h3("WEEKLY CHALLENGE"),
      colorBox("Before next week's session, choose one:", [
        "OPTION A: Track every dollar you spend this week. Don't change anything yet — just look. Bring your observations to the next session.",
        "OPTION B: Write your 'Lifestyle Finish Line' — a sentence or number that defines 'enough' for your current season. Post it somewhere visible.",
        "OPTION C: Identify one discretionary expense this week that you can redirect. Give it away, save it, or use it to pay down debt.",
      ]),
      spacer(),
      h3("CLOSING PRAYER"),
      new Table({
        width: { size: 9360, type: WidthType.DXA }, columnWidths: [9360],
        rows: [new TableRow({ children: [new TableCell({
          borders, width: { size: 9360, type: WidthType.DXA },
          shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
          margins: { top: 160, bottom: 160, left: 240, right: 240 },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Father, you are our provider. Forgive us for the ways we've confused accumulation with security. Teach us to define enough by your generosity, not by our fear. Give us contentment that isn't passive — but free. Help us spend your resources in ways that reflect what we actually believe. Amen.", font: "Georgia", size: 22, italic: true, color: NAVY })] })]
        })]})
      }),

      pageBreak(),

      // ─────────────────────────── SESSION 4 ───────────────────────────
      sectionDivider("SESSION 4", "WEEK FOUR", "GIVE — GENEROSITY THAT TRANSFORMS"),
      spacer(),
      h3("THIS WEEK'S READING"),
      body("Book: Chapter 4 (Give)   |   Devotional: Days 22–28"),
      spacer(),
      scriptureBox("Do not store up for yourselves treasures on earth... But store up for yourselves treasures in heaven.", "Matthew 6:19–20 (NIV)"),
      spacer(),
      h3("BIG IDEA"),
      body("There are over 2,300 verses in the Bible about money — more than any other topic. And the reason, Ron Blue says, is that money is a reflection of the heart, and giving is a reflection of who you believe the Owner is. This week explores giving not as obligation but as the one financial behavior that is purely an act of worship."),
      spacer(),
      hostNote("Ron explicitly says this session should NOT be about shame or guilt. Keep the tone positive and wonder-filled. The goal is to help people discover joy in generosity — not feel bad about where they are."),
      spacer(),
      h3("KEY CONCEPTS FROM THE BOOK & DEVOTIONAL"),
      colorBox("This week participants encountered:", [
        "Three motivations for giving: out of obedience (1 Cor. 16:2), to break the power of money (Matt. 6:19-20), and because it reflects God's character",
        "The Treasure Principle: You can't take it with you — but you can send it ahead",
        "Three giving frameworks: Proportionate giving, Planned giving, Precommitted giving",
        "Giving is the only financial decision where you don't 'buy' anything — it's a pure expression of faith",
        "Ron's conviction: There is no shortage of kingdom money. There is a shortage of obedience.",
        "Treasure Target — Give quadrant: Level 1 (Start giving) → Level 2 (Percentage giving) → Level 3 (Sacrificial giving)",
      ]),
      spacer(),
      ...threeColumnTable("ICEBREAKER — Choose One (5–7 minutes)",
        "Option A — Light & Fun",
        ["What's the most creative or surprising gift you've ever given — or received?", "Tell us about a time generosity cost you something — and how you felt afterward."],
        "Option B — Reflective",
        ["Was generosity modeled for you growing up? How has that shaped you?", "When have you given something and felt lighter rather than poorer?"],
        "Option C — Direct",
        ["Be honest: Is giving something you genuinely look forward to, or does it mostly feel like obligation?", "Have you ever experienced what Ron calls 'joyful giving'? What was the context?"]
      ),
      spacer(),
      h3("DISCUSSION QUESTIONS"),
      colorBox("Work through these together:", [
        "Ron says, 'Giving is a reflection of my recognition of God's ownership.' What's the connection? How does believing God owns it change how you feel about giving it away?",
        "He identifies three motives for giving — obedience, breaking money's power, and reflecting God's character. Which of those three is most meaningful to you right now? Which feels most foreign?",
        "Matthew 6:19–20 introduces the Treasure Principle. What does it look like, practically, to 'store up treasures in heaven'? What forms does that take?",
        "Ron says there is no shortage of kingdom money — only a shortage of obedience. That's a bold claim. Do you agree? What does it stir in you?",
        "What's the difference between giving out of guilt and giving out of gratitude? Have you experienced both? What changed between them?",
        "Proportionate, planned, and precommitted giving — which of those three practices is least present in your current approach to generosity? What would it look like to start there?",
      ]),
      spacer(),
      ...threeColumnTable("GROUP ACTIVITY — Choose One (10–15 minutes)",
        "Option A — The Generosity Story",
        ["Everyone shares briefly: What's one act of generosity (given or received) that changed something for you?", "After each story, the group asks: What does that reveal about God's character?", "Close by identifying: What's one way God is inviting us to grow in generosity this year?"],
        "Option B — The Giving Audit",
        ["On paper, each person writes their current giving percentage or amount.", "Then write what 'next level' generosity would look like for your season.", "Share: What's holding you back from moving there? Is it financial, emotional, or spiritual?"],
        "Option C — Precommit Together",
        ["Each person writes down one specific giving commitment for the next 30 days — a dollar amount or percentage.", "Seal it in an envelope with your name on it. Host holds them.", "At the final session (Week 6), open them and celebrate faithfulness."]
      ),
      spacer(),
      qrBox("Watch: Ron Blue — Session 4 Video Teaching (Give)", "ronblueinstitute.com/goia"),
      spacer(),
      h3("WEEKLY CHALLENGE"),
      colorBox("Before next week's session, choose one:", [
        "OPTION A: Give something this week — money, time, or possessions — that costs you enough to feel it. Write down how it felt before, during, and after.",
        "OPTION B: Research one organization or cause you've been curious about supporting. Take a first step toward intentional generosity.",
        "OPTION C: Have the 'giving conversation' with your spouse or household. Ask: 'What percentage of our income do we want to give? What would make that joyful rather than reluctant?'",
      ]),
      spacer(),
      h3("CLOSING PRAYER"),
      new Table({
        width: { size: 9360, type: WidthType.DXA }, columnWidths: [9360],
        rows: [new TableRow({ children: [new TableCell({
          borders, width: { size: 9360, type: WidthType.DXA },
          shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
          margins: { top: 160, bottom: 160, left: 240, right: 240 },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Lord, you gave everything. Teach us to hold what we have with open hands. Release us from the grip of money — not by taking it away, but by making us generous. Let our giving be worship, not transaction. Let it reflect your character in us. Make us joyful givers. Amen.", font: "Georgia", size: 22, italic: true, color: NAVY })] })]
        })]})
      }),

      pageBreak(),

      // ─────────────────────────── SESSION 5 ───────────────────────────
      sectionDivider("SESSION 5", "WEEK FIVE", "OWE — FREEDOM FROM DEBT"),
      spacer(),
      h3("THIS WEEK'S READING"),
      body("Book: Chapter 5 (Owe)   |   Devotional: Days 29–35"),
      spacer(),
      scriptureBox("The rich rule over the poor, and the borrower is slave to the lender.", "Proverbs 22:7 (NIV)"),
      spacer(),
      h3("BIG IDEA"),
      body("Debt always mortgages the future. This week, the group examines the biblical perspective on borrowing — not as a blanket prohibition, but as a call to wisdom, clarity, and freedom. The four key questions about debt help participants evaluate every borrowing decision through a stewardship lens."),
      spacer(),
      hostNote("Some people in your group may be carrying significant debt — and significant shame. Remind the group early that this is not a shame session. The goal is wisdom and a path forward, not judgment about the past."),
      spacer(),
      h3("KEY CONCEPTS FROM THE BOOK & DEVOTIONAL"),
      colorBox("This week participants encountered:", [
        "The biblical perspective: debt is not explicitly forbidden, but it is always a risk and a burden",
        "Proverbs 22:7 — the borrower is slave to the lender; debt limits future options and giving",
        "Four questions before borrowing: (1) Does it make economic sense? (2) What is my lender's perspective? (3) Is there a guaranteed way to repay? (4) Does my spouse agree?",
        "Three debt categories: consumer debt (avoid), mortgage debt (use carefully), investment debt (use wisely)",
        "Treasure Target — Owe quadrant: Level 1 (repay credit card debt) → Level 2 (repay all debt except mortgage) → Level 3 (repay mortgage)",
        "Debt freedom isn't just financial — it expands margin for generosity, contentment, and kingdom impact",
      ]),
      spacer(),
      ...threeColumnTable("ICEBREAKER — Choose One (5–7 minutes)",
        "Option A — Light & Fun",
        ["What's the most random thing you ever bought on credit — and regretted?", "What would you do first if all your debt disappeared tomorrow?"],
        "Option B — Reflective",
        ["When you hear the word 'debt,' what's the first emotion that comes up? Why?", "Have you ever experienced the feeling of being debt-free? What was that like?"],
        "Option C — Direct",
        ["Is debt a source of stress for you right now? You don't need to share amounts — just yes or no and how it feels.", "What's one debt decision you wish you'd made differently? What would you tell your younger self?"]
      ),
      spacer(),
      h3("DISCUSSION QUESTIONS"),
      colorBox("Work through these together:", [
        "Proverbs 22:7 is blunt: the borrower is slave to the lender. How does that metaphor hit you? In what ways have you felt 'enslaved' by a financial obligation?",
        "The book doesn't say debt is always sin — but it does say debt always mortgages the future. What future options have you seen debt foreclose on — for you or others?",
        "The four questions before borrowing are practical guardrails. Which of those four do people most often skip? Which is hardest to answer honestly?",
        "Consumer debt, mortgage debt, investment debt — these are different in character. How does recognizing those distinctions change how we think about borrowing?",
        "Ron argues that debt freedom expands generosity. Have you seen that connection? What becomes possible when debt is removed?",
        "What would it look like to take one concrete step toward your next level on the Treasure Target's 'Owe' quadrant?",
      ]),
      spacer(),
      ...threeColumnTable("GROUP ACTIVITY — Choose One (10–15 minutes)",
        "Option A — The Debt Categories Exercise",
        ["Individually, list your current debts by category: consumer, mortgage, investment.", "For each, ask: Does this align with the four borrowing questions?", "Share: Which debt on your list do you most want to be free of — and what's one step toward that?"],
        "Option B — The Four Questions Discussion",
        ["Host reads each of Ron's four questions about borrowing out loud.", "As a group, discuss: Which question is most countercultural? Which would most change decision-making if people actually asked it?", "Role play: Apply all four questions to a common scenario (e.g., new car, home renovation, credit card)."],
        "Option C — Accountability Pairs",
        ["Pair up within the group. Share one debt-related goal for the next 90 days.", "Exchange contact info and agree to check in on each other mid-week.", "Close by praying specifically for each other's financial freedom."]
      ),
      spacer(),
      qrBox("Watch: Ron Blue — Session 5 Video Teaching (Owe)", "ronblueinstitute.com/goia"),
      spacer(),
      h3("WEEKLY CHALLENGE"),
      colorBox("Before next week's session, choose one:", [
        "OPTION A: Make a list of all current debts — type, balance, interest rate. Pray over the list and ask God for a clear path forward.",
        "OPTION B: Apply the four borrowing questions to one financial decision you're currently considering. Write down your honest answers.",
        "OPTION C: Identify your 'next level' on the Owe quadrant of the Treasure Target. Write down one specific action that moves you toward it.",
      ]),
      spacer(),
      h3("CLOSING PRAYER"),
      new Table({
        width: { size: 9360, type: WidthType.DXA }, columnWidths: [9360],
        rows: [new TableRow({ children: [new TableCell({
          borders, width: { size: 9360, type: WidthType.DXA },
          shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
          margins: { top: 160, bottom: 160, left: 240, right: 240 },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Lord, you came to set the captives free. For those in this room carrying financial burdens — bring clarity, courage, and a clear path forward. Where there is shame, replace it with wisdom. Where there is debt, give a strategy and the perseverance to follow it. Free us to give generously and live faithfully. Amen.", font: "Georgia", size: 22, italic: true, color: NAVY })] })]
        })]})
      }),

      pageBreak(),

      // ─────────────────────────── SESSION 6 ───────────────────────────
      sectionDivider("SESSION 6", "WEEK SIX", "GROW — BUILDING WITH KINGDOM PURPOSE"),
      spacer(),
      h3("THIS WEEK'S READING"),
      body("Book: Chapter 6 (Grow)   |   Devotional: Days 36–40"),
      spacer(),
      scriptureBox("Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things.", "Matthew 25:23 (NIV)"),
      spacer(),
      h3("BIG IDEA"),
      body("Growing margin is the only way to meet long-term goals. But what are your long-term goals? This final session connects financial growth to kingdom purpose — asking not just 'Am I growing?' but 'Am I growing toward something that matters eternally?' The group ends by looking back at six weeks of transformation and forward at what comes next."),
      spacer(),
      hostNote("This is the final session — make it celebratory. Acknowledge growth. If you did the 'Precommit Together' activity in Session 4, open those envelopes today. Close with a longer prayer time. Let people share what changed."),
      spacer(),
      h3("KEY CONCEPTS FROM THE BOOK & DEVOTIONAL"),
      colorBox("This week participants encountered:", [
        "Growing margin is the path to long-term financial freedom and kingdom impact",
        "Three goals of financial growth: contentment, confidence, and consistency of behavior",
        "The question of the 'next steward' — who will inherit what you're building, and are they prepared?",
        "Eternal ROI: measuring financial success by kingdom impact, not net worth alone",
        "Treasure Target — Grow quadrant: Level 1 (save $1,500 while paying down debt) → Level 2 (save 3-6 months living expenses) → Level 3 (save for God-given goals)",
        "The study closes with a call to confidence — not in our financial plans, but in the God who owns it all",
      ]),
      spacer(),
      ...threeColumnTable("ICEBREAKER — Choose One (5–7 minutes)",
        "Option A — Light & Fun",
        ["If someone gave you $10,000 right now with no strings attached, what would you do with it?", "What's one financial goal you have for the next 5 years that excites you?"],
        "Option B — Reflective",
        ["What's changed in how you think about money over the past six weeks?", "What's one thing someone said in this group that has stayed with you?"],
        "Option C — Direct",
        ["What does 'financial freedom' mean to you now compared to when we started?", "Where do you feel most confident? Where do you still feel the most stuck?"]
      ),
      spacer(),
      h3("DISCUSSION QUESTIONS"),
      colorBox("Work through these together:", [
        "Ron says the goal of financial growth isn't accumulation — it's contentment, confidence, and consistency. How has your understanding of 'growth' changed through this study?",
        "The third right question from Session 1 was: 'Is the next steward chosen and prepared?' How are you thinking about that question now? What does it mean for your family or legacy?",
        "Matthew 25:23 pictures God saying 'well done, good and faithful servant.' What does it look like to hear those words specifically about your finances? What would have to be true?",
        "Growing margin is described as the only path to long-term goals. What are your long-term goals — not just financially, but in terms of kingdom impact?",
        "Look back at the six sessions. Where did you experience the most conviction? Where did you experience the most freedom?",
        "As a group: What is one thing you want to commit to carrying forward from this study — individually and together?",
      ]),
      spacer(),
      ...threeColumnTable("GROUP ACTIVITY — Choose One (10–15 minutes)",
        "Option A — The Treasure Target Review",
        ["Revisit the Treasure Target as a group. Each person marks where they are in all four quadrants today.", "Compare to where you started in Session 2.", "Celebrate any movement — including a changed mindset. Share one goal for the next 6 months."],
        "Option B — Write Your 'Why'",
        ["From the Week 1 book content: 'Take a minute to think about why you want a better handle on your money. Record your why.'", "Share your 'why' with the group today.", "Then discuss: Has your 'why' deepened or changed over 6 weeks? How?"],
        "Option C — The Stewardship Statement & Commitment",
        ["Read the Stewardship Statement from Session 1 aloud together.", "Each person writes one specific commitment they're making as a steward going forward.", "Share briefly. Pray over one another's commitments specifically."]
      ),
      spacer(),
      qrBox("Watch: Ron Blue — Session 6 Video Teaching (Grow) + Closing Message", "ronblueinstitute.com/goia"),
      spacer(),
      h3("LOOKING FORWARD — WHAT NOW?"),
      colorBox("Encourage your group to:", [
        "Continue the devotional if they haven't completed all 40 days",
        "Share the God Owns It All book with one person in their life who needs it",
        "Revisit the Treasure Target every 6 months as a personal 'stewardship check-up'",
        "Consider joining or starting a financial accountability pairing or couple's financial check-in",
        "Explore additional resources from the Ron Blue Institute at ronblueinstitute.com",
      ]),
      spacer(),
      h3("FINAL CLOSING — CELEBRATION & PRAYER"),
      body("Take 5 minutes to let anyone share a word of gratitude or a specific way God moved during this study. Then close with the following prayer:"),
      spacer(),
      new Table({
        width: { size: 9360, type: WidthType.DXA }, columnWidths: [9360],
        rows: [new TableRow({ children: [new TableCell({
          borders: { top: { style: BorderStyle.SINGLE, size: 4, color: GOLD }, bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD }, left: { style: BorderStyle.SINGLE, size: 16, color: GOLD }, right: noBorder },
          width: { size: 9360, type: WidthType.DXA },
          shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
          margins: { top: 200, bottom: 200, left: 300, right: 240 },
          children: [
            new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "CLOSING PRAYER", font: "Arial", size: 22, bold: true, color: GOLD })], spacing: { after: 120 } }),
            new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Father, you are the Owner of everything. Over these six weeks, you have been our Teacher. You have shown us that the way we handle money is not separate from the way we follow you — it is part of it. Thank you for the freedom that comes from releasing what was never ours in the first place. Help us to carry these truths forward — not just in how we budget or save or give — but in who we are becoming. May we be found faithful. Not perfect. Faithful. And when we see you face to face, may we hear those words: 'Well done.' In Jesus' name, Amen.", font: "Georgia", size: 22, italic: true, color: NAVY })] }),
          ]
        })]})
      }),

      pageBreak(),

      // ─── APPENDIX ──────────────────────────────────────────────────────
      h1("APPENDIX & HOST RESOURCES"),
      spacer(),
      h2("A. QUICK-REFERENCE: SESSION AT A GLANCE"),
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [900, 2200, 2360, 2300, 1600],
        rows: [
          new TableRow({ children: [
            ...[["#", 900], ["Title", 2200], ["Key Scripture", 2360], ["Big Question", 2300], ["Devotional Days", 1600]].map(([h, w]) =>
              new TableCell({ borders, width: { size: w, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 100 },
                children: [new Paragraph({ children: [new TextRun({ text: String(h), font: "Arial", size: 19, bold: true, color: WHITE })] })] })
            )
          ]}),
          ...[
            ["1", "Perspective", "Psalm 24:1", "Who owns it?", "Days 1–7"],
            ["2", "Principles", "1 Cor. 4:2", "How should I use it?", "Days 8–14"],
            ["3", "Live", "1 Tim. 6:6–7", "How much is enough?", "Days 15–21"],
            ["4", "Give", "Matt. 6:19–20", "What does faithful giving look like?", "Days 22–28"],
            ["5", "Owe", "Prov. 22:7", "How do I find freedom?", "Days 29–35"],
            ["6", "Grow", "Matt. 25:23", "Am I building toward eternity?", "Days 36–40"],
          ].map(([num, title, ref, q, days], idx) =>
            new TableRow({ children: [
              new TableCell({ borders, width: { size: 900, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 100 }, children: [new Paragraph({ children: [new TextRun({ text: num, font: "Arial", size: 19, bold: true, color: NAVY })] })] }),
              new TableCell({ borders, width: { size: 2200, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 100 }, children: [new Paragraph({ children: [new TextRun({ text: title, font: "Arial", size: 19, bold: true, color: TEAL })] })] }),
              new TableCell({ borders, width: { size: 2360, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 100 }, children: [new Paragraph({ children: [new TextRun({ text: ref, font: "Arial", size: 19, italic: true, color: DARK_GRAY })] })] }),
              new TableCell({ borders, width: { size: 2300, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 100 }, children: [new Paragraph({ children: [new TextRun({ text: q, font: "Arial", size: 19, color: DARK_GRAY })] })] }),
              new TableCell({ borders, width: { size: 1600, type: WidthType.DXA }, shading: { fill: idx%2===0 ? LIGHT_BLUE : WHITE, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 100 }, children: [new Paragraph({ children: [new TextRun({ text: days, font: "Arial", size: 19, color: DARK_GRAY })] })] }),
            ]})
          )
        ]
      }),
      spacer(),
      h2("B. HOST TIPS FOR GREAT SMALL GROUP DISCUSSION"),
      colorBox("Before you meet:", [
        "Pray specifically for each group member by name",
        "Read the session yourself — all of it — and note what personally resonates",
        "Choose your icebreaker, activity, and 3–4 discussion questions in advance",
        "Prepare the room: comfortable seating, good lighting, something to drink",
        "Have Bibles or a Bible app available",
      ]),
      spacer(),
      colorBox("During the discussion:", [
        "Use silence. A few seconds of quiet usually means someone is about to say something important",
        "Affirm sharing without over-praising: 'Thank you for that' is enough",
        "If one person dominates, redirect warmly: 'That's great — does anyone else want to respond?'",
        "Keep God's Word central — opinions are welcome, but Scripture is the authority",
        "It's okay to say 'I don't know.' You're a facilitator, not a financial advisor",
        "Watch for emotion — if someone tears up or goes quiet, slow down and stay there",
      ], LIGHT_GOLD),
      spacer(),
      h2("C. THE FIVE MONEY MANAGEMENT PRINCIPLES — REFERENCE CARD"),
      colorBox("Ron Blue's Five Principles (share these freely):", [
        "SPEND LESS THAN YOU EARN — The foundation. Margin is only created here.",
        "GIVE GENEROUSLY — Not the last thing, the first. Reflects who the Owner is.",
        "AVOID THE USE OF DEBT — The borrower is slave to the lender. Debt always mortgages the future.",
        "BUILD CASH FLOW MARGIN — Save for the unexpected. Margin creates options.",
        "SET LONG-TERM GOALS — Prioritize short-term vs. long-term. Eternity clarifies everything.",
      ]),
      spacer(),
      h2("D. KEY RESOURCES"),
      colorBox("Recommended tools and resources for participants:", [
        "God Owns It All book — Ron Blue with Michael Blue (LifeWay, 2016)",
        "God Owns It All Devotional — 40 days of personal application",
        "Live/Give/Owe/Grow Worksheet — calculate your personal financial pie",
        "Treasure Target Tool — four quadrants, three levels each: ronblueinstitute.com/FourHTool",
        "Ron Blue Institute: ronblueinstitute.com — additional courses, articles, and financial discipleship resources",
        "Master Your Money — Ron Blue's foundational personal finance book (30th anniversary edition)",
      ]),
      spacer(),
      new Paragraph({
        children: [new TextRun({ text: "God Owns It All 6-Session Curriculum  |  Based on the book by Ron Blue with Michael Blue  |  For group use", font: "Arial", size: 18, italic: true, color: "999999" })],
        alignment: AlignmentType.CENTER,
        spacing: { before: 400, after: 0 },
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/GOIA_6Session_Curriculum.docx', buffer);
  console.log('Done!');
}).catch(err => { console.error(err); process.exit(1); });
