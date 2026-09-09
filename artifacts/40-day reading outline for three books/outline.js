const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageBreak, TabStopType, TabStopPosition
} = require('docx');
const fs = require('fs');

// Color palette
const NAVY = "1F3864";
const GOLD = "C9A84C";
const LIGHT_BLUE = "D9E8F5";
const LIGHT_GREEN = "E2F0D9";
const LIGHT_GOLD = "FFF2CC";
const WHITE = "FFFFFF";
const DARK_GRAY = "404040";
const MID_GRAY = "666666";

function hRule() {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: GOLD, space: 1 } },
    spacing: { before: 120, after: 120 }
  });
}

function spacer() {
  return new Paragraph({ spacing: { before: 60, after: 60 }, children: [new TextRun("")] });
}

function bookBanner(title, subtitle, fillColor) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            shading: { fill: fillColor, type: ShadingType.CLEAR },
            margins: { top: 160, bottom: 160, left: 240, right: 240 },
            borders: {
              top: { style: BorderStyle.SINGLE, size: 4, color: GOLD },
              bottom: { style: BorderStyle.SINGLE, size: 4, color: GOLD },
              left: { style: BorderStyle.SINGLE, size: 4, color: GOLD },
              right: { style: BorderStyle.SINGLE, size: 4, color: GOLD },
            },
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text: title, bold: true, size: 32, font: "Arial", color: NAVY })]
              }),
              new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text: subtitle, size: 22, font: "Arial", color: MID_GRAY, italics: true })]
              })
            ]
          })
        ]
      })
    ]
  });
}

function sectionHeader(text, color) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 240, after: 80 },
    children: [new TextRun({ text, bold: true, size: 26, font: "Arial", color: color || NAVY })]
  });
}

function dayRow(day, focus, content, shading) {
  const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
  const borders = { top: border, bottom: border, left: border, right: border };
  return new TableRow({
    children: [
      new TableCell({
        borders,
        width: { size: 900, type: WidthType.DXA },
        shading: { fill: shading || LIGHT_BLUE, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        verticalAlign: "center",
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ text: day, bold: true, size: 22, font: "Arial", color: NAVY })]
        })]
      }),
      new TableCell({
        borders,
        width: { size: 2200, type: WidthType.DXA },
        shading: { fill: shading || LIGHT_BLUE, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({
          children: [new TextRun({ text: focus, bold: true, size: 20, font: "Arial", color: NAVY })]
        })]
      }),
      new TableCell({
        borders,
        width: { size: 6260, type: WidthType.DXA },
        shading: { fill: WHITE, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({
          children: [new TextRun({ text: content, size: 20, font: "Arial", color: DARK_GRAY })]
        })]
      })
    ]
  });
}

function tableHeader(c1, c2, c3) {
  const border = { style: BorderStyle.SINGLE, size: 2, color: NAVY };
  const borders = { top: border, bottom: border, left: border, right: border };
  return new TableRow({
    tableHeader: true,
    children: [
      new TableCell({ borders, width: { size: 900, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: c1, bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
      new TableCell({ borders, width: { size: 2200, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: c2, bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
      new TableCell({ borders, width: { size: 6260, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: c3, bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
    ]
  });
}

function buildTable(rows) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [900, 2200, 6260],
    rows
  });
}

// ===================== DATA =====================

// BOOK 1: God Owns It All (6 weeks = 18 days, 3 days per topic)
const goiaData = [
  // Week 1 - Perspective
  ["Day 1", "Perspective\n(Ch. 1 intro)", "Read Week 1: Perspective. Examine your personal worldview about money. Who do you believe owns what you have? Journal your answer honestly."],
  ["Day 2", "Perspective\n(Study)", "Work through the Week 1 Study section. Explore key scriptures (1 Chr. 29:14; Ps. 24:1; Ps. 50:9–12). Underline everything God owns. Discuss the 'Dad's car' story and its implications."],
  ["Day 3", "Perspective\n(Apply)", "Identify one financial decision you are facing. Reframe it through the lens of stewardship vs. ownership. Write out how your answer changes."],
  // Week 2 - Principles
  ["Day 4", "Principles\n(5 Uses)", "Read Week 2: Principles. Learn the 5 uses of money: Live, Give, Owe, Grow, Tax. Draw the pie chart and estimate your current percentages."],
  ["Day 5", "Principles\n(Biblical vs. Worldly)", "Study the differences between a biblical and worldly financial worldview. Which principles have you been applying? Which have you been ignoring?"],
  ["Day 6", "Principles\n(Apply)", "Using the 5 Steps framework (Struggling → Surviving → Stable → Secure → Surplus), honestly assess where you are today. What would move you one step forward?"],
  // Week 3 - Live
  ["Day 7", "Live\n(Contentment)", "Read Week 3: Live. Study the Prosperity Paradox. What is the relationship between wealth and contentment in your own experience?"],
  ["Day 8", "Live\n(Enough)", "Work through the 'How Much Is Enough?' exercise. Identify the lifestyle you want to sustain and the margin needed to give generously."],
  ["Day 9", "Live\n(Apply)", "Review your monthly spending. Where are you living beyond your means? Where is there opportunity to create margin? Write one concrete step toward simpler living."],
  // Week 4 - Give
  ["Day 10", "Give\n(Motivations)", "Read Week 4: Give. Explore the motivations for giving. Are you giving out of obligation, love, or faith? Reflect on what the Treasure Principle means for your giving."],
  ["Day 11", "Give\n(Proportionate)", "Study proportionate, planned, and precommitted giving. Calculate what 10%, 15%, and 20% giving would look like in your current budget."],
  ["Day 12", "Give\n(Apply)", "Make a specific giving plan: amount, frequency, and recipient. Commit to it for 90 days as a 'faith experiment' in giving."],
  // Week 5 - Owe
  ["Day 13", "Owe\n(Categories)", "Read Week 5: Owe. Classify your current debts into the three biblical categories. Which debts are urgent vs. acceptable?"],
  ["Day 14", "Owe\n(4 Questions)", "Apply the four borrowing questions to any future debt decision: Does it make sense? Can I repay it? Does my spouse agree? Does it reflect godly priorities?"],
  ["Day 15", "Owe\n(Apply)", "Create a debt elimination timeline. List every debt, minimum payment, and target payoff date. Identify the first debt to eliminate and celebrate when it's gone."],
  // Week 6 - Grow
  ["Day 16", "Grow\n(Kingdom Purpose)", "Read Week 6: Grow. How does building wealth look different when the end goal is God's kingdom rather than personal security?"],
  ["Day 17", "Grow\n(Confidence & Clarity)", "Review the themes of confidence, clarity, and consistency in the Grow session. What does faithful investment stewardship look like in your life?"],
  ["Day 18", "Grow\n(Apply)", "Write a one-paragraph 'kingdom investment thesis' — what you want your money to do for God's purposes in your lifetime and beyond."],
];

// BOOK 2: Master Your Money (14 chapters, 14–16 days)
const mymData = [
  ["Day 1", "Will I Ever\nHave Enough?", "Read Ch. 1. Confront the anxiety behind your financial life. Journal: Is your confidence in the economy or in God? Name three specific financial fears."],
  ["Day 2", "4 Biblical\nPrinciples", "Read Ch. 2. Study: God owns it all; We're in a growth process; The amount doesn't matter; Faith requires action. Which principle is hardest for you? Why?"],
  ["Day 3", "Planning\nOverview", "Read Ch. 3. Learn the 5 uses of money and 4-step planning process. Map your current cash flow across the 5 uses. Where are you out of balance?"],
  ["Day 4", "Guaranteed\nSuccess", "Read Ch. 4. Study time value of money and compounding. Run the Starbucks opportunity-cost exercise for one recurring expense in your life."],
  ["Day 5", "Dangers\nof Debt", "Read Ch. 5. Learn biblical borrowing principles. List every debt you carry and rate each as 'wise,' 'neutral,' or 'dangerous' based on the book's framework."],
  ["Day 6", "Where\nAm I?", "Read Ch. 6 (application). Complete your personal net worth statement and cash flow summary. This is your financial snapshot. Face it honestly."],
  ["Day 7", "Faith\nFinancial Goals", "Read Ch. 7. Write a purpose statement for your financial life, then turn it into 3 specific, measurable, faith-driven goals with target dates."],
  ["Day 8", "Avoiding\nMistakes", "Read Ch. 8. Review the most common financial mistakes (consumptive lifestyle, no budget, mismanaged debt). Identify which ones you are currently making."],
  ["Day 9", "Your Personal\nFinancial Plan", "Read Ch. 9 (application). Follow the instructions to design your integrated personal financial plan. This is the blueprint for everything that follows."],
  ["Day 10", "Control\nthe Flow", "Read Ch. 10. Estimate your living expenses, record actual spending for one week, and build your first working budget. Commit to tracking for 30 days."],
  ["Day 11", "Tax\nPlanning", "Read Ch. 11. Study what Scripture says about taxes. Identify 2–3 legal tax strategies you are not currently using and consult a professional if needed."],
  ["Day 12", "Investment\nPlanning", "Read Ch. 12. Learn the Sequential Investing Strategy: eliminate debt → emergency fund → savings → diversify → long-term goals. Plot where you are in the sequence."],
  ["Day 13", "Stewardship\nAfter Death", "Read Ch. 13. Review the role of life insurance and estate planning. Do you have a will? Is it current? Identify your next estate planning action step."],
  ["Day 14", "Giving\nLiving", "Read Ch. 14. Discern when, where, and how much to give. As the capstone of MYM, write out your complete giving plan as the final act of a well-mastered financial life."],
];

// BOOK 3: Generous Living (13 chapters, 13 days — can do 2x for 26 days)
const glData = [
  ["Day 1", "Generosity &\nContentment", "Read Ch. 1. Explore why the secret to financial freedom is generosity, not accumulation. Where in your life do you equate contentment with having more?"],
  ["Day 2", "Treasure\nHunting", "Read Ch. 2. Study Jesus' teaching on treasure and the heart. Complete the self-audit: Where does your financial behavior reveal your actual priorities?"],
  ["Day 3", "Obstacles\nto Giving", "Read Ch. 3. Work through all seven obstacles to generosity (spiritual through practical). Which two obstacles hit closest to home? Write out your plan to overcome them."],
  ["Day 4", "Generosity\nas Lifestyle", "Read Ch. 4. Expand your view of generosity beyond money — time, talent, and possessions. Identify one non-financial way to practice generosity this week."],
  ["Day 5", "Preparation:\nHearing God's Word", "Read Ch. 5. How does your engagement with Scripture shape your giving? Identify one passage about generosity to memorize and meditate on this month."],
  ["Day 6", "Problem Solving:\nFix Your Finances", "Read Ch. 6. Use the Pyramid of Problems to diagnose where financial barriers are blocking your generosity. What is the bottom-most unresolved problem?"],
  ["Day 7", "The Right\nPerspective", "Read Ch. 7. Practice seeing your life and resources the way God sees them. Journal: If God held your checkbook, what story would it tell about your values?"],
  ["Day 8", "The Plan:\nHow Generous?", "Read Ch. 8. Build a formal giving plan: percentage target, recipient organizations, timeline. Move from reactive to strategic in your giving."],
  ["Day 9", "Strategic\nGiving", "Read Ch. 9. Learn how to evaluate charities, use donor-advised funds, and make your giving count. Research one new giving vehicle you have not used before."],
  ["Day 10", "Giving to\nYour Children", "Read Ch. 10. Study how to pass down wisdom alongside wealth. What financial values and habits are you intentionally transferring to the next generation?"],
  ["Day 11", "Giving Through\nYour Will", "Read Ch. 11. Work through the six critical estate decisions. Does your current will reflect your kingdom values? Identify the one decision you need to update."],
  ["Day 12", "A Formal\nTalk", "Read Ch. 12. Plan and schedule a family conference. Prepare a one-page summary of your estate plan and charitable vision to share with your heirs."],
  ["Day 13", "Solving the\nWealth Paradox", "Read Ch. 13. Confront the paradox: faithful stewardship builds wealth, which can undermine generosity. Commit to one boundary — a lifestyle cap or giving floor — to guard against it."],
];

// ===================== BUILD DOCUMENT =====================

const children = [];

// TITLE PAGE
children.push(spacer());
children.push(spacer());
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 480, after: 120 },
  children: [new TextRun({ text: "40-Day Reading Plan", bold: true, size: 52, font: "Arial", color: NAVY })]
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 120 },
  children: [new TextRun({ text: "God Owns It All  ·  Master Your Money  ·  Generous Living", size: 28, font: "Arial", color: MID_GRAY, italics: true })]
}));
children.push(hRule());
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 120, after: 480 },
  children: [new TextRun({ text: "Ron Blue | A Curriculum Sequencing Guide", size: 22, font: "Arial", color: MID_GRAY })]
}));
children.push(spacer());

// OVERVIEW TABLE
children.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 240, after: 120 },
  children: [new TextRun({ text: "Overview: Three Books, Three Arcs", bold: true, size: 32, font: "Arial", color: NAVY })]
}));

const overviewBorder = { style: BorderStyle.SINGLE, size: 1, color: "AAAAAA" };
const overviewBorders = { top: overviewBorder, bottom: overviewBorder, left: overviewBorder, right: overviewBorder };

children.push(new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [2000, 1400, 1400, 4560],
  rows: [
    new TableRow({
      children: [
        new TableCell({ borders: overviewBorders, width: { size: 2000, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Book", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
        new TableCell({ borders: overviewBorders, width: { size: 1400, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Days", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
        new TableCell({ borders: overviewBorders, width: { size: 1400, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Sessions", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
        new TableCell({ borders: overviewBorders, width: { size: 4560, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Core Arc", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
      ]
    }),
    ...[
      ["God Owns It All", "18", "6 (3 days each)", "Perspective → Principles → Live → Give → Owe → Grow", LIGHT_BLUE],
      ["Master Your Money", "14", "14 (1 day each)", "Foundation → Planning → Execution → Legacy", LIGHT_GREEN],
      ["Generous Living", "13", "13 (1 day each)", "Joy → Process → Practical Applications", LIGHT_GOLD],
      ["TOTAL", "45", "", "Full biblical stewardship journey — use any 40", "F2F2F2"],
    ].map(([b, d, s, a, fill]) => new TableRow({
      children: [
        new TableCell({ borders: overviewBorders, width: { size: 2000, type: WidthType.DXA }, shading: { fill, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: b, bold: b === "TOTAL", size: 20, font: "Arial", color: DARK_GRAY })] })] }),
        new TableCell({ borders: overviewBorders, width: { size: 1400, type: WidthType.DXA }, shading: { fill, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: d, bold: b === "TOTAL", size: 20, font: "Arial", color: DARK_GRAY })] })] }),
        new TableCell({ borders: overviewBorders, width: { size: 1400, type: WidthType.DXA }, shading: { fill, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: s, size: 20, font: "Arial", color: DARK_GRAY })] })] }),
        new TableCell({ borders: overviewBorders, width: { size: 4560, type: WidthType.DXA }, shading: { fill, type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: a, size: 20, font: "Arial", color: DARK_GRAY })] })] }),
      ]
    }))
  ]
}));

children.push(spacer());

// NOTE
children.push(new Paragraph({
  spacing: { before: 120, after: 240 },
  children: [
    new TextRun({ text: "Note: ", bold: true, size: 20, font: "Arial", color: NAVY }),
    new TextRun({ text: "These three books together produce 45 total days of content. For a strict 40-day plan, the recommended approach is to use all 14 days of MYM, all 13 days of GL, and 13 of the 18 GOIA days (one day per session week rather than three). Alternatively, use all 45 days for a 6-week journey, running two books concurrently in weeks 2–5.", size: 20, font: "Arial", color: DARK_GRAY })]
}));

children.push(new Paragraph({
  children: [new PageBreak()]
}));

// ========= BOOK 1: GOIA =========
children.push(bookBanner("BOOK 1: GOD OWNS IT ALL", "Ron Blue with Michael Blue  ·  18 Days  ·  6 Weeks (3 Days Per Session)", LIGHT_BLUE));
children.push(spacer());
children.push(new Paragraph({
  spacing: { before: 0, after: 120 },
  children: [new TextRun({ text: "Structure: Six weekly sessions — Perspective, Principles, Live, Give, Owe, Grow — each explored over three days: Read/Study → Deep Study → Application.", size: 20, font: "Arial", color: MID_GRAY, italics: true })]
}));
children.push(spacer());

const goiaWeeks = [
  { label: "Week 1 — Perspective", days: goiaData.slice(0, 3), shade: LIGHT_BLUE },
  { label: "Week 2 — Principles", days: goiaData.slice(3, 6), shade: LIGHT_BLUE },
  { label: "Week 3 — Live", days: goiaData.slice(6, 9), shade: LIGHT_GREEN },
  { label: "Week 4 — Give", days: goiaData.slice(9, 12), shade: LIGHT_GREEN },
  { label: "Week 5 — Owe", days: goiaData.slice(12, 15), shade: LIGHT_GOLD },
  { label: "Week 6 — Grow", days: goiaData.slice(15, 18), shade: LIGHT_GOLD },
];

for (const week of goiaWeeks) {
  children.push(sectionHeader(week.label));
  children.push(buildTable([
    tableHeader("Day", "Focus", "Reading & Activity"),
    ...week.days.map(([d, f, c]) => dayRow(d, f, c, week.shade))
  ]));
  children.push(spacer());
}

children.push(new Paragraph({ children: [new PageBreak()] }));

// ========= BOOK 2: MYM =========
children.push(bookBanner("BOOK 2: MASTER YOUR MONEY", "Ron Blue with Michael Blue  ·  14 Days  ·  1 Day Per Chapter", LIGHT_GREEN));
children.push(spacer());
children.push(new Paragraph({
  spacing: { before: 0, after: 120 },
  children: [new TextRun({ text: "Structure: One chapter per day, moving from biblical foundations through practical financial planning to legacy and giving. Each day includes a reading and a focused action step.", size: 20, font: "Arial", color: MID_GRAY, italics: true })]
}));
children.push(spacer());

const mymGroups = [
  { label: "Days 1–4: Foundations", days: mymData.slice(0, 4) },
  { label: "Days 5–9: Planning & Tools", days: mymData.slice(4, 9) },
  { label: "Days 10–14: Execution & Legacy", days: mymData.slice(9, 14) },
];

for (const group of mymGroups) {
  children.push(sectionHeader(group.label));
  children.push(buildTable([
    tableHeader("Day", "Chapter Focus", "Reading & Activity"),
    ...group.days.map(([d, f, c]) => dayRow(d, f, c, LIGHT_GREEN))
  ]));
  children.push(spacer());
}

children.push(new Paragraph({ children: [new PageBreak()] }));

// ========= BOOK 3: GL =========
children.push(bookBanner("BOOK 3: GENEROUS LIVING", "Ron Blue  ·  13 Days  ·  1 Day Per Chapter", LIGHT_GOLD));
children.push(spacer());
children.push(new Paragraph({
  spacing: { before: 0, after: 120 },
  children: [new TextRun({ text: "Structure: Three parts — Living and Giving with Joy (Ch. 1–4), The Process of Giving (Ch. 5–8), Practical Applications (Ch. 9–13). Each day reads one chapter and takes one concrete action.", size: 20, font: "Arial", color: MID_GRAY, italics: true })]
}));
children.push(spacer());

const glGroups = [
  { label: "Part 1 — Living and Giving with Joy (Ch. 1–4)", days: glData.slice(0, 4) },
  { label: "Part 2 — The Process of Giving (Ch. 5–8)", days: glData.slice(4, 8) },
  { label: "Part 3 — Practical Applications (Ch. 9–13)", days: glData.slice(8, 13) },
];

for (const group of glGroups) {
  children.push(sectionHeader(group.label));
  children.push(buildTable([
    tableHeader("Day", "Chapter Focus", "Reading & Activity"),
    ...group.days.map(([d, f, c]) => dayRow(d, f, c, LIGHT_GOLD))
  ]));
  children.push(spacer());
}

children.push(new Paragraph({ children: [new PageBreak()] }));

// ========= COMBINED 40-DAY PLAN =========
children.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 120, after: 120 },
  children: [new TextRun({ text: "Recommended 40-Day Sequence", bold: true, size: 32, font: "Arial", color: NAVY })]
}));
children.push(hRule());
children.push(new Paragraph({
  spacing: { before: 120, after: 120 },
  children: [new TextRun({ text: "The following sequence interweaves all three books into a single 40-day journey. GOIA is compressed to one day per session (6 days), MYM runs its full 14 chapters, and GL runs its full 13 chapters, with 7 integration/reflection days added.", size: 20, font: "Arial", color: DARK_GRAY })]
}));

const seq40 = [
  ["1", "GOIA", "Perspective", "God owns it all. Reframe every financial decision as a spiritual decision."],
  ["2", "GOIA", "Principles", "Map your 5 uses of money. Assess your current position on the 5-step scale."],
  ["3", "MYM", "Ch. 1–2", "Confront 'Will I Ever Have Enough?' + study the 4 biblical money principles."],
  ["4", "MYM", "Ch. 3", "Build your financial planning overview. Identify goals and the 4-step process."],
  ["5", "MYM", "Ch. 4", "Understand guaranteed financial success: compounding, margin, and opportunity cost."],
  ["6", "MYM", "Ch. 5", "Study the dangers of debt. Classify every debt you carry."],
  ["7", "REFLECT", "Foundations Review", "Review Days 1–6. What is your biggest mindset shift so far? Write a one-paragraph stewardship confession."],
  ["8", "GOIA", "Live", "How much is enough? Define your lifestyle ceiling."],
  ["9", "GL", "Ch. 1", "Generosity is the secret to contentment. Where is your heart right now?"],
  ["10", "GL", "Ch. 2", "Treasure hunting: let your calendar and checkbook reveal your real priorities."],
  ["11", "GL", "Ch. 3", "Identify and dismantle the obstacles holding you back from generous living."],
  ["12", "MYM", "Ch. 6", "Complete your net worth statement and cash flow summary."],
  ["13", "MYM", "Ch. 7", "Set your faith financial goals. Write a purpose statement for your money."],
  ["14", "REFLECT", "Generosity Check", "Are your goals generous or just self-sufficient? Revise Day 13 goals to include a giving component."],
  ["15", "GOIA", "Give", "Study the Treasure Principle. Create a proportionate giving plan."],
  ["16", "GL", "Ch. 4", "Generosity as lifestyle: time, talents, and possessions — not just money."],
  ["17", "GL", "Ch. 5", "Preparation: let God's Word calibrate your heart for giving."],
  ["18", "MYM", "Ch. 8", "Avoid the most common financial mistakes. Conduct a personal mistake audit."],
  ["19", "MYM", "Ch. 9", "Design your personal financial plan — this is your blueprint."],
  ["20", "MYM", "Ch. 10", "Control the flow: estimate, record, build, and commit to your budget."],
  ["21", "REFLECT", "Mid-Point Review", "You are halfway. Review your giving plan, budget, and goals. What needs to change?"],
  ["22", "GOIA", "Owe", "Apply the 4 biblical borrowing questions. Build a debt elimination timeline."],
  ["23", "GL", "Ch. 6", "Problem Solving: identify and remove the financial barriers blocking generosity."],
  ["24", "GL", "Ch. 7", "The right perspective: see your life as God sees it."],
  ["25", "MYM", "Ch. 11", "Tax planning: understand your obligations and find legal strategies to save."],
  ["26", "MYM", "Ch. 12", "Investment planning: learn the Sequential Investing Strategy."],
  ["27", "GL", "Ch. 8", "Build your formal giving plan — set a percentage target and recipient list."],
  ["28", "REFLECT", "Wealth & Generosity", "How does growing wealth affect your generosity? Write your personal answer to the Wealth Paradox."],
  ["29", "GOIA", "Grow", "Invest with kingdom purpose. Write your kingdom investment thesis."],
  ["30", "GL", "Ch. 9", "Strategic giving: evaluate charities and explore donor-advised funds."],
  ["31", "MYM", "Ch. 13", "Stewardship after death: update or create your will and estate plan."],
  ["32", "GL", "Ch. 10", "Give to your children: pass down wisdom before — or alongside — wealth."],
  ["33", "GL", "Ch. 11", "Giving through your will: make the six critical estate decisions."],
  ["34", "GL", "Ch. 12", "A formal talk: plan your family conference."],
  ["35", "GL", "Ch. 13", "Solve the Wealth Paradox: set a lifestyle cap or giving floor."],
  ["36", "MYM", "Ch. 14", "Giving Living: the capstone of mastering your money is an open hand."],
  ["37", "REFLECT", "Integration", "Compare your Day 1 stewardship mindset to today. What has changed? What hasn't?"],
  ["38", "ALL", "Legacy Review", "Revisit your will, giving plan, and kingdom investment thesis. Are they aligned?"],
  ["39", "ALL", "Family Action", "Share your giving and estate plan with your spouse or a trusted friend. Invite accountability."],
  ["40", "ALL", "Commit & Launch", "Write your personal stewardship covenant. Sign it. Share it. Live it."],
];

const seqBorderC = { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" };
const seqBorders = { top: seqBorderC, bottom: seqBorderC, left: seqBorderC, right: seqBorderC };

const bookColors = { "GOIA": LIGHT_BLUE, "MYM": LIGHT_GREEN, "GL": LIGHT_GOLD, "REFLECT": "F2F2F2", "ALL": "EDE7F6" };
const bookTextColors = { "GOIA": NAVY, "MYM": "1A5C2B", "GL": "7B4F00", "REFLECT": "555555", "ALL": "4A235A" };

children.push(new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [600, 1000, 1600, 6160],
  rows: [
    new TableRow({
      children: [
        new TableCell({ borders: seqBorders, width: { size: 600, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Day", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
        new TableCell({ borders: seqBorders, width: { size: 1000, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Book", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
        new TableCell({ borders: seqBorders, width: { size: 1600, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Source", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
        new TableCell({ borders: seqBorders, width: { size: 6160, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Focus & Activity", bold: true, size: 20, font: "Arial", color: WHITE })] })] }),
      ]
    }),
    ...seq40.map(([day, book, source, focus]) => new TableRow({
      children: [
        new TableCell({ borders: seqBorders, width: { size: 600, type: WidthType.DXA }, shading: { fill: bookColors[book] || "FFFFFF", type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 80, right: 80 }, children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: day, bold: true, size: 20, font: "Arial", color: bookTextColors[book] || DARK_GRAY })] })] }),
        new TableCell({ borders: seqBorders, width: { size: 1000, type: WidthType.DXA }, shading: { fill: bookColors[book] || "FFFFFF", type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 80 }, children: [new Paragraph({ children: [new TextRun({ text: book, bold: true, size: 18, font: "Arial", color: bookTextColors[book] || DARK_GRAY })] })] }),
        new TableCell({ borders: seqBorders, width: { size: 1600, type: WidthType.DXA }, shading: { fill: "FAFAFA", type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 80 }, children: [new Paragraph({ children: [new TextRun({ text: source, size: 18, font: "Arial", color: MID_GRAY })] })] }),
        new TableCell({ borders: seqBorders, width: { size: 6160, type: WidthType.DXA }, shading: { fill: "FAFAFA", type: ShadingType.CLEAR }, margins: { top: 80, bottom: 80, left: 100, right: 80 }, children: [new Paragraph({ children: [new TextRun({ text: focus, size: 20, font: "Arial", color: DARK_GRAY })] })] }),
      ]
    }))
  ]
}));

// ===================== ASSEMBLE =====================
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: "Arial", size: 22 } }
    },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
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

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/mnt/user-data/outputs/40_Day_Reading_Plan_GOIA_MYM_GL.docx', buf);
  console.log('Done!');
});
