const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageNumber, PageBreak
} = require('docx');
const fs = require('fs');

// Color palette
const DARK_BLUE = "1B3A5C";
const MID_BLUE = "2E6DA4";
const LIGHT_BLUE = "D5E8F4";
const ACCENT_GOLD = "C9A84C";
const LIGHT_GOLD = "FDF3DC";
const LIGHT_GRAY = "F5F5F5";
const MED_GRAY = "DDDDDD";
const WHITE = "FFFFFF";
const DARK_TEXT = "1A1A1A";

const cellBorder = { style: BorderStyle.SINGLE, size: 1, color: MED_GRAY };
const cellBorders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };
const noBorder = { style: BorderStyle.NONE, size: 0, color: WHITE };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

function spacer(size = 120) {
  return new Paragraph({ spacing: { before: size, after: 0 }, children: [] });
}

function sectionDivider(color = MID_BLUE) {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color, space: 1 } },
    spacing: { before: 0, after: 160 },
    children: []
  });
}

function coverTitle(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 120 },
    children: [new TextRun({ text, font: "Arial", size: 52, bold: true, color: WHITE })]
  });
}

function coverSubtitle(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 80 },
    children: [new TextRun({ text, font: "Arial", size: 26, color: "D4E8F7", italics: true })]
  });
}

function coverLabel(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 200, after: 0 },
    children: [new TextRun({ text, font: "Arial", size: 20, color: ACCENT_GOLD, bold: true })]
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 320, after: 120 },
    children: [new TextRun({ text, font: "Arial", size: 32, bold: true, color: DARK_BLUE })]
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 240, after: 80 },
    children: [new TextRun({ text, font: "Arial", size: 24, bold: true, color: MID_BLUE })]
  });
}

function bodyText(text, options = {}) {
  return new Paragraph({
    spacing: { before: 80, after: 80 },
    children: [new TextRun({
      text,
      font: "Arial",
      size: 22,
      color: DARK_TEXT,
      italics: options.italic || false,
      bold: options.bold || false
    })]
  });
}

function labeledPara(label, text) {
  return new Paragraph({
    spacing: { before: 100, after: 60 },
    children: [
      new TextRun({ text: label + " ", font: "Arial", size: 22, bold: true, color: DARK_BLUE }),
      new TextRun({ text, font: "Arial", size: 22, color: DARK_TEXT })
    ]
  });
}

function sectionHeaderBar(sessionNum, title) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders: noBorders,
            shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
            margins: { top: 140, bottom: 140, left: 200, right: 200 },
            children: [
              new Paragraph({
                children: [
                  new TextRun({ text: `SESSION ${sessionNum}  `, font: "Arial", size: 20, bold: true, color: ACCENT_GOLD }),
                  new TextRun({ text: `  ${title}`, font: "Arial", size: 24, bold: true, color: WHITE })
                ]
              })
            ]
          })
        ]
      })
    ]
  });
}

function comparisonTable(originalTitle, originalSubtitle, suggestedSubtitle, reason) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1440, 3960, 3960],
    rows: [
      // Header row
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            shading: { fill: MID_BLUE, type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "", font: "Arial", size: 20 })] })]
          }),
          new TableCell({
            borders: cellBorders,
            shading: { fill: MID_BLUE, type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "ORIGINAL SUBTITLE", font: "Arial", size: 20, bold: true, color: WHITE })] })]
          }),
          new TableCell({
            borders: cellBorders,
            shading: { fill: MID_BLUE, type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "SUGGESTED SUBTITLE", font: "Arial", size: 20, bold: true, color: WHITE })] })]
          })
        ]
      }),
      // Content row
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
            margins: { top: 100, bottom: 100, left: 120, right: 120 },
            verticalAlign: VerticalAlign.CENTER,
            children: [new Paragraph({ children: [new TextRun({ text: originalTitle, font: "Arial", size: 20, bold: true, color: DARK_BLUE })] })]
          }),
          new TableCell({
            borders: cellBorders,
            shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
            margins: { top: 100, bottom: 100, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: originalSubtitle, font: "Arial", size: 20, color: DARK_TEXT, italics: true })] })]
          }),
          new TableCell({
            borders: cellBorders,
            shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
            margins: { top: 100, bottom: 100, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: suggestedSubtitle, font: "Arial", size: 20, bold: true, color: DARK_BLUE })] })]
          })
        ]
      }),
      // Reason row
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            columnSpan: 1,
            shading: { fill: WHITE, type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: "WHY", font: "Arial", size: 18, bold: true, color: ACCENT_GOLD })] })]
          }),
          new TableCell({
            borders: cellBorders,
            columnSpan: 2,
            shading: { fill: WHITE, type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 120, right: 120 },
            children: [new Paragraph({ children: [new TextRun({ text: reason, font: "Arial", size: 20, color: DARK_TEXT })] })]
          })
        ]
      })
    ]
  });
}

function twoColumnOutlineTable(originalContent, suggestedContent) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [4680, 4680],
    rows: [
      // Header
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            shading: { fill: MED_GRAY, type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 140, right: 140 },
            children: [new Paragraph({ children: [new TextRun({ text: "ORIGINAL OUTLINE", font: "Arial", size: 20, bold: true, color: DARK_BLUE })] })]
          }),
          new TableCell({
            borders: cellBorders,
            shading: { fill: ACCENT_GOLD, type: ShadingType.CLEAR },
            margins: { top: 80, bottom: 80, left: 140, right: 140 },
            children: [new Paragraph({ children: [new TextRun({ text: "SUGGESTED SHIFT", font: "Arial", size: 20, bold: true, color: WHITE })] })]
          })
        ]
      }),
      // Content
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
            margins: { top: 120, bottom: 120, left: 140, right: 140 },
            children: originalContent.map(line => new Paragraph({
              spacing: { before: 60, after: 60 },
              children: [new TextRun({ text: line, font: "Arial", size: 20, color: DARK_TEXT })]
            }))
          }),
          new TableCell({
            borders: cellBorders,
            shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
            margins: { top: 120, bottom: 120, left: 140, right: 140 },
            children: suggestedContent.map(line => new Paragraph({
              spacing: { before: 60, after: 60 },
              children: [new TextRun({ text: line, font: "Arial", size: 20, color: DARK_TEXT })]
            }))
          })
        ]
      })
    ]
  });
}

// ─── SESSION DATA ───────────────────────────────────────────────────────────

const sessions = [
  {
    num: "1",
    title: "The Ownership Question",
    originalSubtitle: "What Does it Really Mean if God Owns it All?",
    suggestedSubtitle: "When You\u2019re Holding On for Dear Life \u2014 What Are You Actually Holding?",
    subtitleReason: "The original subtitle restates the session title rather than creating emotional entry. The suggested subtitle meets the audience where they actually are \u2014 in the grip of anxiety, control, and identity \u2014 before introducing the theological answer.",
    originalOutline: [
      "The cultural worldview: money = success,",
      "  significance, security",
      "The biblical worldview and 3 foundational questions:",
      "  Who owns it? How much is enough?",
      "  Is the next steward prepared?",
      "Key scriptures: Psalm 24:1, 1 Chronicles 29:14,",
      "  Luke 16:10\u201313",
      "Transferable concept: Behavior follows belief",
      "Ron\u2019s \u201cDad\u2019s car\u201d illustration",
      "God uses money as Tool, Test, and Testimony",
      "Application: Stewardship acknowledgment/signature"
    ],
    suggestedOutline: [
      "KEEP: The \u201cDad\u2019s car\u201d illustration \u2014 it\u2019s the perfect",
      "  emotional on-ramp",
      "EXPAND: Whole-life lordship (family, vocation,",
      "  identity, fears, relationships) not just money",
      "PLANT: The 3 biblical questions as a preview of",
      "  the full series arc \u2014 let each session answer one",
      "REFRAME: Tool/Test/Testimony as a personal",
      "  diagnostic, not just teaching content",
      "ADD: The stewardship acknowledgment as a",
      "  moment of surrender, not just an exercise",
      "TONE: Devotional, story-driven, open-handed"
    ],
    descriptionOriginal: "Focus on the fundamental theological question that God owns it all. Initially applied to money and possessions, but then including a whole-life surrender/Lordship implications. Addressing our identity, family, relationships, vocation, fears, aspirations, goals, and ultimately our trust in God.",
    descriptionSuggested: "Open with something every person in the room already feels: the white-knuckle grip of holding on \u2014 to money, security, identity, or control. The \u201cDad\u2019s car\u201d story isn\u2019t just a financial illustration; it\u2019s the picture of every human being\u2019s relationship to everything they think they own. The three biblical questions (Who owns it? How much is enough? Is the next steward prepared?) are planted here as seeds that will grow across the series. The session closes not with a workbook exercise but with a moment of genuine surrender \u2014 a signed acknowledgment that feels like a prayer, not a form."
  },
  {
    num: "2",
    title: "The Stewardship Question",
    originalSubtitle: "How Do We Learn Faithfulness Through Stewardship?",
    suggestedSubtitle: "What Would Change If You Stopped Seeing It as Yours?",
    subtitleReason: "The original subtitle sounds like a seminary course description. The suggested version creates a personal, disarming challenge that the audience feels immediately \u2014 it\u2019s the same theological question in human language.",
    originalOutline: [
      "Money as Tool, Test, and Testimony",
      "5 money management principles",
      "LGOG pie diagram introduced",
      "Debt categories and biblical principles",
      "of borrowing",
      "Four questions about borrowing",
      "Session Note: Overloaded \u2014 debt material",
      "  may need to carry into Session 3"
    ],
    suggestedOutline: [
      "LEAD: Tool/Test/Testimony as the framework",
      "  for stewardship (moved here from S1)",
      "ANCHOR: 5 principles + LGOG pie as the",
      "  practical expression of faithful stewardship",
      "REFRAME DEBT: \u201cDebt pre-commits God\u2019s resources",
      "  to someone else\u201d \u2014 a stewardship issue, not",
      "  just a financial one",
      "KEEP: Four borrowing questions, reframed as",
      "  stewardship diagnostic questions",
      "LIGHTEN: Don\u2019t force all debt content here;",
      "  let it breathe into Session 3 if needed",
      "TONE: Honest, practical, grace-filled"
    ],
    descriptionOriginal: "If God owns everything including myself (Psalm 24), what are the implications for ALL that God has given me to steward? Beginning with money and possessions and moving into whole-life stewardship. Money as tool, test, and testimony. Debt addressed here or in Session 3.",
    descriptionSuggested: "This session answers the \u201cso what?\u201d of Session 1. If God owns it all, then I am managing someone else\u2019s resources \u2014 and that changes everything about how I spend, save, borrow, and give. The LGOG pie diagram isn\u2019t just a budgeting tool; it\u2019s a picture of your priorities. Debt gets its most powerful reframe here: when you borrow, you\u2019re pre-committing resources that belong to God. The four borrowing questions become stewardship questions, not just financial ones. The tone is practical but never clinical \u2014 this is about freedom, not obligation."
  },
  {
    num: "3",
    title: "The Confidence Question",
    originalSubtitle: "Will I Be OK?",
    suggestedSubtitle: "Will I Be OK?",
    subtitleReason: "KEEP AS IS. This is the strongest subtitle in the series \u2014 it\u2019s the most human, the most universal, and the most emotionally resonant. Every person in the room is asking it. Don\u2019t touch it.",
    originalOutline: [
      "Biblical basis for contentment",
      "Five habits/principles of money management",
      "Practical financial strength for retirement",
      "Communication around money for couples",
      "Trusting God\u2019s provision + biblical principles",
      "Session Note: Mixes heart content (contentment)",
      "  with practical content (principles/retirement)",
      "\u2014 risks being the catch-all session"
    ],
    suggestedOutline: [
      "ANCHOR: 5 principles as the foundation of",
      "  financial confidence (the \u201cwhat to do\u201d)",
      "USE: Ron\u2019s congressional testimony story \u2014",
      "  timeless principles at any income level",
      "ADD: Treasure Target tool so people can see",
      "  where they stand and what the path looks like",
      "INCLUDE: Couples communication as part of",
      "  building confidence together",
      "DRAW THE LINE: Confidence = what I DO.",
      "  Contentment = what I BELIEVE (that\u2019s Session 4)",
      "TONE: Assuring, practical, forward-looking"
    ],
    descriptionOriginal: "The session can rely on the biblical basis for contentment which supports confidence that \u201cwe will be OK.\u201d Practical elements from week six can develop confidence in finances and clarity of communication around money. Giving attention to the five habits as biblical principles that when followed lead to financial strength.",
    descriptionSuggested: "This is the session where people exhale. They\u2019ve accepted God\u2019s ownership (S1), understood their role as stewards (S2), and now they need to know: does this actually work? The answer is yes \u2014 and Ron\u2019s story of testifying before Congress is the evidence. The five principles aren\u2019t financial advice; they\u2019re ancient wisdom that works at every income level. The Treasure Target gives people a map. The session closes by drawing a clear line: confidence is about what you do; the deeper question of whether you can be at peace regardless of the numbers \u2014 that\u2019s the next session."
  },
  {
    num: "4",
    title: "The Contentment Question",
    originalSubtitle: "How Much Is Enough?",
    suggestedSubtitle: "How Much Is Enough?",
    subtitleReason: "KEEP AS IS. This subtitle is culturally universal, emotionally honest, and theologically loaded all at once. It needs no improvement.",
    originalOutline: [
      "True contentment from God\u2019s ownership",
      "Eternal perspective",
      "God\u2019s provision and contentment with",
      "  little or much",
      "Contentment as learned behavior",
      "Paradox of prosperity",
      "Assessing contentment level",
      "Combating materialism",
      "Session Note: Overlaps risk with S5 (Generosity)"
    ],
    suggestedOutline: [
      "LEAD: Prosperity Paradox \u2014 name the tension",
      "  people already feel before offering the answer",
      "ANCHOR: Philippians 4:11\u201313 \u2014 contentment is",
      "  LEARNED, not earned, not a number",
      "USE: Africa/materialism story \u2014 universalizes",
      "  the struggle across every income level",
      "INTRODUCE: The lifestyle finish line as the",
      "  practical tool for answering \u201cenough\u201d",
      "DISTINGUISH: S3 = what I DO. S4 = what I BELIEVE",
      "BRIDGE: Close with \u201cContentment is what makes",
      "  an open hand possible\u201d \u2014 sets up S5 naturally",
      "TONE: Warm, honest, liberating"
    ],
    descriptionOriginal: "Highlight that true contentment comes from recognizing God\u2019s ownership and adopting an eternal perspective. Contentment is a learned behavior God helps us achieve. Also noting the paradox of prosperity. Helping people assess their contentment level and combat materialism.",
    descriptionSuggested: "Everyone walks into this session quietly convinced that if they just had a little more, they\u2019d finally feel okay. This session names that lie gently and replaces it with something better. The Prosperity Paradox does the diagnostic work \u2014 more stuff creates more complexity, not more peace. Paul\u2019s words in Philippians become the turning point: contentment isn\u2019t something you achieve; it\u2019s something you learn, in the middle of whatever circumstances you\u2019re in right now. The lifestyle finish line gives couples and individuals a practical tool to stop the comparison treadmill. The session ends with a bridge: \u201cContentment is what makes an open hand possible\u201d \u2014 which is exactly where Session 5 begins."
  },
  {
    num: "5",
    title: "The Generosity Question",
    originalSubtitle: "How Does Giving Change Everything?",
    suggestedSubtitle: "What Happens When You Finally Let Go?",
    subtitleReason: "The original subtitle is a statement dressed as a question \u2014 the audience already knows giving is supposed to change things. The suggested version creates genuine emotional stakes. \u201cFinally let go\u201d names the thing they\u2019ve been holding too tightly, which is where transformation actually begins.",
    originalOutline: [
      "Similarities to Generous Living content",
      "God\u2019s generosity to us as foundation",
      "Call to be generous and openhanded",
      "Giving breaks the power of money",
      "Joy and recognition of God\u2019s provision",
      "Privilege of participating in God\u2019s",
      "  provision for others"
    ],
    suggestedOutline: [
      "OPEN: Pick up the bridge from S4 \u2014 you can\u2019t",
      "  give freely until contentment is settled",
      "ANCHOR: Treasure Principle (Matt 6:19\u201320) as",
      "  the theological foundation",
      "EXPLORE: Motivations for giving \u2014 obligation",
      "  vs. gratitude vs. joy (let people self-identify)",
      "INTRODUCE: Three giving disciplines \u2014",
      "  proportionate, planned, precommitted",
      "CENTER: \u201cGenerosity isn\u2019t what God wants FROM",
      "  you \u2014 it\u2019s what he wants FOR you.\u201d",
      "TONE: Joyful, freeing, story-driven"
    ],
    descriptionOriginal: "This may have similarities to Generous Living, but fundamentally addresses God\u2019s generosity to us and his call for us to be generous. Being openhanded and generous breaks the power of money and fosters joy and recognition of God\u2019s provision, as well as the privilege of participating in God\u2019s provision for others.",
    descriptionSuggested: "You can\u2019t get here without going through Session 4. That\u2019s intentional. Generosity that flows from guilt or obligation never lasts. But generosity that flows from a settled heart \u2014 one that has genuinely learned contentment \u2014 that changes a person\u2019s entire relationship with money. The Treasure Principle gives the theological anchor: you can\u2019t take it with you, but you can send it ahead. The three giving disciplines (proportionate, planned, precommitted) move people from intention to action. And the emotional center of this session is a single line from the source material: \u201cGenerosity isn\u2019t what God wants from you \u2014 it\u2019s what he wants for you.\u201d That\u2019s the line that stays with people long after the session ends."
  },
  {
    num: "6",
    title: "The Impact Question",
    originalSubtitle: "Making an Impact Today, Tomorrow, and for Eternity",
    suggestedSubtitle: "What Do You Want Your Life to Have Been About?",
    subtitleReason: "The original subtitle is a description of the session, not an invitation into it. The suggested subtitle is the question every person quietly carries \u2014 about legacy, purpose, and whether their life will have mattered. It\u2019s the right question to end a series on stewardship.",
    originalOutline: [
      "Motivations and purpose for giving",
      "Treasure Principle",
      "Proportionate, planned, precommitted giving",
      "Time and Talent as well as Treasure",
      "Impact on sphere of influence,",
      "  church, community, and world",
      "Passing along GOIA wisdom to family",
      "Session Note: Least developed session \u2014",
      "  needs more curriculum architecture"
    ],
    suggestedOutline: [
      "STRUCTURE: Three concentric circles \u2014",
      "  Household \u2192 Community \u2192 World",
      "REVISIT: The 3 biblical questions from S1 \u2014",
      "  answer them now with 5 sessions of growth",
      "DEVELOP: \u201cNext steward\u201d question fully \u2014",
      "  legacy, raising financially wise children,",
      "  estate and generational stewardship",
      "INCLUDE: Time and Talent alongside Treasure \u2014",
      "  impact is not only financial",
      "CLOSE: Capstone exercise \u2014 a personal",
      "  stewardship statement covering all 6 sessions",
      "TONE: Hopeful, legacy-minded, forward and eternal"
    ],
    descriptionOriginal: "The session explores motivations and purpose for giving, the Treasure Principle, and practical ideas about proportionate, planned, and pre-committed giving. Focus on Time and Talent as well as Treasure regarding impact today, tomorrow, and for eternity. Includes passing along GOIA wisdom to family and others.",
    descriptionSuggested: "This session is the one people will remember for the rest of their lives \u2014 if the curriculum gives it what it needs. Structure it around three concentric circles: your household, your community, and the world. Then bring back the three questions planted in Session 1. What does it mean now, after five sessions, that God owns it all? How much is enough \u2014 and have you settled on a number? And the question that carries the most weight: is the next steward prepared? That\u2019s not just a financial planning question; it\u2019s a legacy question. Who are you raising, mentoring, and equipping to carry this forward? The session closes with a capstone exercise \u2014 a personal stewardship statement that covers ownership, principles, contentment, generosity, and legacy on a single page. It\u2019s the thing they take home and keep."
  }
];

// ─── BUILD DOCUMENT ──────────────────────────────────────────────────────────

const children = [];

// COVER PAGE
children.push(
  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders: noBorders,
            shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
            margins: { top: 800, bottom: 800, left: 400, right: 400 },
            children: [
              coverTitle("GOD OWNS IT ALL"),
              coverSubtitle("Series Outline: Comparison & Recommendations"),
              coverLabel("SUBTITLE REVIEW  \u2022  OUTLINE SHIFTS  \u2022  SESSION DESCRIPTIONS"),
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 400, after: 0 },
                children: [new TextRun({ text: "Prepared for Internal Review", font: "Arial", size: 18, color: "A0B8CC" })]
              })
            ]
          })
        ]
      })
    ]
  })
);

children.push(new Paragraph({ children: [new PageBreak()] }));

// INTRO
children.push(h1("Overview"));
children.push(sectionDivider());
children.push(bodyText("This document compares the current God Owns It All series outline against recommended revisions. The session titles are locked (already filmed). Recommendations address three areas for each session:"));
children.push(spacer(80));
children.push(bodyText("1.  SUBTITLE \u2014 Whether to keep or change, and why", { bold: false }));
children.push(bodyText("2.  OUTLINE CONTENT \u2014 What to keep, shift, add, or reframe inside each session", { bold: false }));
children.push(bodyText("3.  SESSION DESCRIPTION \u2014 Original intent vs. suggested approach", { bold: false }));
children.push(spacer(80));
children.push(bodyText("The primary audience lens applied throughout: everyday people wrestling with life, trust, pressure, identity, fear, purpose, generosity, and stewardship. The primary engagement driver in a church context is often women. The series must work for small groups, couples, individuals, and churchwide use."));

children.push(spacer(200));

// SUBTITLE COMPARISON CHART
children.push(h1("Subtitle Comparison at a Glance"));
children.push(sectionDivider());

// Build the at-a-glance table
const glanceRows = [
  new TableRow({
    children: [
      new TableCell({
        borders: cellBorders,
        shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: "SESSION", font: "Arial", size: 19, bold: true, color: WHITE })] })]
      }),
      new TableCell({
        borders: cellBorders,
        shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: "TITLE", font: "Arial", size: 19, bold: true, color: WHITE })] })]
      }),
      new TableCell({
        borders: cellBorders,
        shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: "ORIGINAL SUBTITLE", font: "Arial", size: 19, bold: true, color: WHITE })] })]
      }),
      new TableCell({
        borders: cellBorders,
        shading: { fill: DARK_BLUE, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({ children: [new TextRun({ text: "RECOMMENDATION", font: "Arial", size: 19, bold: true, color: WHITE })] })]
      })
    ]
  })
];

sessions.forEach(s => {
  const keep = s.originalSubtitle === s.suggestedSubtitle;
  glanceRows.push(
    new TableRow({
      children: [
        new TableCell({
          borders: cellBorders,
          shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: `S${s.num}`, font: "Arial", size: 20, bold: true, color: DARK_BLUE })] })]
        }),
        new TableCell({
          borders: cellBorders,
          shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: s.title, font: "Arial", size: 19, bold: true, color: DARK_TEXT })] })]
        }),
        new TableCell({
          borders: cellBorders,
          shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: s.originalSubtitle, font: "Arial", size: 19, color: DARK_TEXT, italics: true })] })]
        }),
        new TableCell({
          borders: cellBorders,
          shading: { fill: keep ? LIGHT_BLUE : LIGHT_GOLD, type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: keep ? "\u2713 KEEP" : s.suggestedSubtitle, font: "Arial", size: 19, bold: !keep, color: keep ? MID_BLUE : DARK_BLUE })] })]
        })
      ]
    })
  );
});

children.push(new Table({ width: { size: 9360, type: WidthType.DXA }, columnWidths: [520, 1800, 3020, 4020], rows: glanceRows }));

children.push(new Paragraph({ children: [new PageBreak()] }));

// SESSION DETAIL PAGES
sessions.forEach((s, i) => {
  children.push(sectionHeaderBar(s.num, s.title.toUpperCase()));
  children.push(spacer(160));

  // Subtitle comparison
  children.push(h2("Subtitle"));
  children.push(comparisonTable(s.title, s.originalSubtitle, s.suggestedSubtitle, s.subtitleReason));
  children.push(spacer(200));

  // Outline comparison
  children.push(h2("Outline Comparison"));
  children.push(twoColumnOutlineTable(s.originalOutline, s.suggestedOutline));
  children.push(spacer(200));

  // Description comparison
  children.push(h2("Session Description"));

  // Original description box
  children.push(new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders: noBorders,
            shading: { fill: MED_GRAY, type: ShadingType.CLEAR },
            margins: { top: 60, bottom: 60, left: 160, right: 160 },
            children: [new Paragraph({ children: [new TextRun({ text: "ORIGINAL", font: "Arial", size: 18, bold: true, color: DARK_BLUE })] })]
          })
        ]
      }),
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
            margins: { top: 120, bottom: 120, left: 200, right: 200 },
            children: [new Paragraph({ children: [new TextRun({ text: s.descriptionOriginal, font: "Arial", size: 21, color: DARK_TEXT, italics: true })] })]
          })
        ]
      })
    ]
  }));

  children.push(spacer(120));

  // Suggested description box
  children.push(new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders: noBorders,
            shading: { fill: ACCENT_GOLD, type: ShadingType.CLEAR },
            margins: { top: 60, bottom: 60, left: 160, right: 160 },
            children: [new Paragraph({ children: [new TextRun({ text: "SUGGESTED", font: "Arial", size: 18, bold: true, color: WHITE })] })]
          })
        ]
      }),
      new TableRow({
        children: [
          new TableCell({
            borders: cellBorders,
            shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
            margins: { top: 120, bottom: 120, left: 200, right: 200 },
            children: [new Paragraph({ children: [new TextRun({ text: s.descriptionSuggested, font: "Arial", size: 21, color: DARK_TEXT })] })]
          })
        ]
      })
    ]
  }));

  if (i < sessions.length - 1) {
    children.push(new Paragraph({ children: [new PageBreak()] }));
  }
});

// BUILD DOC
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: DARK_BLUE },
        paragraph: { spacing: { before: 320, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: MID_BLUE },
        paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 1 } }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 }
      }
    },
    children
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/mnt/user-data/outputs/GOIA_Outline_Comparison.docx", buffer);
  console.log("Done!");
});
