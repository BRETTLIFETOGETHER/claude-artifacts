const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageBreak
} = require('docx');
const fs = require('fs');

// ── COLORS ──────────────────────────────────────────────────
const NAVY   = "1F3864";
const GOLD   = "C9A84C";
const WHITE  = "FFFFFF";
const DGRAY  = "333333";
const MGRAY  = "666666";
const LGRAY  = "F4F4F4";

// Per-book accent colors
const GOIA_DARK  = "1F3864"; const GOIA_MED = "2E5DA6"; const GOIA_LIGHT = "D6E4F7";
const MYM_DARK   = "1A4731"; const MYM_MED  = "2E7D52"; const MYM_LIGHT  = "D8F0E3";
const GL_DARK    = "6B3A00"; const GL_MED   = "A05C0C"; const GL_LIGHT   = "FFF0D6";

// ── HELPERS ──────────────────────────────────────────────────
const sp = (b=80,a=80) => new Paragraph({ spacing:{before:b,after:a}, children:[new TextRun("")] });

function rule(color=GOLD) {
  return new Paragraph({
    border: { bottom:{style:BorderStyle.SINGLE,size:10,color,space:1} },
    spacing:{before:80,after:80}
  });
}

function coverTitle(line1, line2, line3, accentColor) {
  return [
    sp(480,0),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing:{before:0,after:120},
      children:[new TextRun({text:line1, bold:true, size:56, font:"Arial", color:accentColor})]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing:{before:0,after:80},
      children:[new TextRun({text:line2, bold:false, size:28, font:"Arial", color:MGRAY, italics:true})]
    }),
    rule(accentColor),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing:{before:120,after:480},
      children:[new TextRun({text:line3, size:22, font:"Arial", color:MGRAY})]
    }),
    sp(120,120)
  ];
}

function sectionBanner(text, darkColor, lightColor) {
  const brd = { style:BorderStyle.SINGLE, size:4, color:darkColor };
  const borders = {top:brd,bottom:brd,left:brd,right:brd};
  return new Table({
    width:{size:9360,type:WidthType.DXA},
    columnWidths:[9360],
    rows:[new TableRow({children:[
      new TableCell({
        borders, shading:{fill:lightColor,type:ShadingType.CLEAR},
        margins:{top:140,bottom:140,left:240,right:240},
        children:[new Paragraph({
          alignment:AlignmentType.CENTER,
          children:[new TextRun({text,bold:true,size:28,font:"Arial",color:darkColor})]
        })]
      })
    ]})]
  });
}

function tableHeader(darkColor) {
  const brd = {style:BorderStyle.SINGLE,size:2,color:darkColor};
  const borders={top:brd,bottom:brd,left:brd,right:brd};
  const cell = (txt,w) => new TableCell({
    borders, width:{size:w,type:WidthType.DXA},
    shading:{fill:darkColor,type:ShadingType.CLEAR},
    margins:{top:100,bottom:100,left:120,right:120},
    children:[new Paragraph({alignment:AlignmentType.CENTER,
      children:[new TextRun({text:txt,bold:true,size:20,font:"Arial",color:WHITE})]})]
  });
  return new TableRow({children:[cell("Day",560),cell("Theme / Focus",2400),cell("Reading",2600),cell("Application & Reflection",3800)]});
}

function dayRow(day,theme,reading,application,lightColor,medColor) {
  const brd={style:BorderStyle.SINGLE,size:1,color:"CCCCCC"};
  const borders={top:brd,bottom:brd,left:brd,right:brd};
  const isWeek = day.startsWith("—") || day === "";
  return new TableRow({children:[
    new TableCell({borders,width:{size:560,type:WidthType.DXA},
      shading:{fill:lightColor,type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:80,right:80},
      children:[new Paragraph({alignment:AlignmentType.CENTER,
        children:[new TextRun({text:day,bold:true,size:20,font:"Arial",color:medColor})]})]
    }),
    new TableCell({borders,width:{size:2400,type:WidthType.DXA},
      shading:{fill:lightColor,type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:120,right:120},
      children:[new Paragraph({children:[new TextRun({text:theme,bold:true,size:19,font:"Arial",color:DGRAY})]})]
    }),
    new TableCell({borders,width:{size:2600,type:WidthType.DXA},
      shading:{fill:WHITE,type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:120,right:120},
      children:[new Paragraph({children:[new TextRun({text:reading,size:19,font:"Arial",color:DGRAY})]})]
    }),
    new TableCell({borders,width:{size:3800,type:WidthType.DXA},
      shading:{fill:WHITE,type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:120,right:120},
      children:[new Paragraph({children:[new TextRun({text:application,size:19,font:"Arial",color:DGRAY})]})]
    }),
  ]});
}

function buildTable(rows, dark) {
  return new Table({
    width:{size:9360,type:WidthType.DXA},
    columnWidths:[560,2400,2600,3800],
    rows:[tableHeader(dark),...rows]
  });
}

// ════════════════════════════════════════════════════════════════════
// BOOK 1 — GOD OWNS IT ALL  (40 days across 6 sessions)
// 6 sessions × ~6–7 days each = 40 days
// Structure per session: Intro → Study → Deepen → Scripture → Apply → Reflect → (Integration)
// ════════════════════════════════════════════════════════════════════
const goiaWeeks = [
  {
    label: "SESSION 1 — PERSPECTIVE  (Days 1–7)",
    subtitle: "Who Really Owns It? Establishing a Biblical Financial Worldview",
    desc: "The foundation of all financial wisdom: shifting from ownership to stewardship. Every financial decision is a spiritual decision.",
    days: [
      ["Day 1",  "Introduction: Ownership vs. Stewardship",        "Read the Introduction & Session 1 overview",                     "Write your honest answer to: 'Who owns the money in your bank account?' Don't use 'church' language — be real."],
      ["Day 2",  "What the Bible Says About Ownership",             "Study 1 Chr. 29:14; Ps. 24:1; Ps. 50:9–12",                    "Underline every phrase that indicates God's ownership. List three implications for your life today."],
      ["Day 3",  "The Steward vs. The Owner",                       "Study the 'Dad's Car' illustration (Session 1)",                 "In what area of your finances are you acting as the owner rather than the manager? Name it specifically."],
      ["Day 4",  "Behavior Follows Belief",                         "Study the Neil Anderson quote; re-read Luke 16:10–13",          "Identify one financial behavior that is out of sync with what you say you believe. What belief is driving it?"],
      ["Day 5",  "The 5 Money-Management Principles — Overview",    "Study the five principles: earn, debt, margin, goals, give",    "Rate yourself 1–5 on each principle. Which one, if improved, would most change your financial life?"],
      ["Day 6",  "Contentment & Perspective",                       "Study Philippians 4:11–13; Hebrews 13:5",                       "Journal: Do you believe God will never leave or forsake you — financially? Where does anxiety still live?"],
      ["Day 7",  "Session 1 Reflection & Application",              "Review all Session 1 notes and scriptures",                     "Write a one-paragraph 'stewardship declaration' — your personal statement of belief about who owns your resources."],
    ]
  },
  {
    label: "SESSION 2 — PRINCIPLES  (Days 8–14)",
    subtitle: "Five Biblical Principles & Five Uses of Money",
    desc: "All financial priorities are simultaneous, not sequential. Understanding the interconnected 5-use pie diagram changes every decision.",
    days: [
      ["Day 8",  "Principle 1: Spend Less Than You Earn",           "Study Session 2; Matthew 7:24–27 (build on rock)",              "Calculate your current monthly surplus or deficit. What specific change would create a margin this month?"],
      ["Day 9",  "Principle 2: Avoid Debt",                         "Study Session 2 debt section; Prov. 22:7",                      "List every debt you carry. For each, ask: Is this debt serving God's purposes or limiting them?"],
      ["Day 10", "Principle 3: Save — Build Margin",                "Study the margin/emergency fund concept",                       "Do you have 1–3 months of living expenses saved? Write your plan to get there within 12 months."],
      ["Day 11", "Principle 4: Set Long-Term Goals",                "Study goal-setting from Session 2",                             "Write one long-term financial goal that reflects your faith, not just your comfort. Make it measurable."],
      ["Day 12", "Principle 5: Give Generously",                    "Study the giving principle; 2 Cor. 9:6–8",                      "What percentage of income are you currently giving? What would it take to increase it by 1–2%?"],
      ["Day 13", "The 5 Uses of Money — The Pie Diagram",          "Study the Live/Give/Owe/Grow/Tax pie diagram",                  "Draw your actual pie. Estimate your current percentages. Which wedge is dominating in an unhealthy way?"],
      ["Day 14", "Session 2 Reflection & Application",              "Review all Session 2 principles and the pie diagram",           "Write the single biggest shift in how you think about financial decisions after studying these five principles."],
    ]
  },
  {
    label: "SESSION 3 — LIVE  (Days 15–21)",
    subtitle: "How Much Is Enough? Lifestyle, Contentment & the Prosperity Paradox",
    desc: "Lifestyle is the largest and most consequential financial decision you will make. This session confronts the paradox that more does not equal more freedom.",
    days: [
      ["Day 15", "The Prosperity Paradox",                          "Read Session 3; 1 Tim. 6:6–10, 17",                            "In your own words, explain the Prosperity Paradox. Where have you experienced it personally?"],
      ["Day 16", "What People Really Look For",                     "Study: Success, Significance, Security (Session 3 video notes)","Which of the three — success, significance, or security — most drives your financial decisions? Be honest."],
      ["Day 17", "The Right Lifestyle for a Christian",             "Study 1 Tim. 5:8; 1 Tim. 6:8; 1 Tim. 6:17",                   "Describe in one sentence what 'the lifestyle God has provided for me' means in your specific context."],
      ["Day 18", "How Much Is Enough? — Part 1",                   "Study the 'enough' framework: lifestyle + accumulation",        "Define your current lifestyle. Write the monthly cost of maintaining it. Does it align with your values?"],
      ["Day 19", "How Much Is Enough? — Part 2",                   "Study Philippians 4:11–13 in context; the 5 possessions lists", "Complete the two lists: 5 things you value most, 5 things most burdensome. What patterns do you see?"],
      ["Day 20", "Delayed Gratification & the Lifestyle Wedge",     "Study the transferable concept of delayed gratification",       "Identify one lifestyle expense you could reduce or delay that would increase giving or margin. Commit to it."],
      ["Day 21", "Session 3 Reflection & Application",              "Review all Session 3 content and scriptures",                  "Answer in writing: 'How much is enough for my household?' Set a lifestyle number and explain why."],
    ]
  },
  {
    label: "SESSION 4 — GIVE  (Days 22–27)",
    subtitle: "The Treasure Principle — Motivations, Methods & a Giving Plan",
    desc: "Generosity is not a budget line — it is the overflow of a heart that believes God owns it all. This session moves from obligation to joyful, intentional giving.",
    days: [
      ["Day 22", "Why We Give — Motivations",                       "Read Session 4; study the motivations for giving",              "Which best describes your current giving motivation: duty, habit, guilt, joy, or faith? What would shift it?"],
      ["Day 23", "The Treasure Principle",                          "Study Matt. 6:19–21 and the Treasure Principle concept",        "Where are you currently storing treasure? Write one way to send more of it ahead."],
      ["Day 24", "Proportionate Giving",                            "Study proportionate giving framework and tithe discussion",     "Calculate 10%, 15%, and 20% of your gross income. Which level feels like a stretch of faith right now?"],
      ["Day 25", "Planned Giving",                                  "Study the planned giving section of Session 4",                 "Do you have a written giving plan? Draft one: amount, recipients, frequency. Put it in your budget today."],
      ["Day 26", "Precommitted Giving",                             "Study precommitted giving and the faith dynamic it creates",    "Identify one giving commitment you could precommit to for the next 12 months. Write the amount and recipient."],
      ["Day 27", "Session 4 Reflection & Application",              "Review all Session 4 content",                                  "Write your complete giving plan: current %, 1-year target %, two recipients, and one giving stretch goal."],
    ]
  },
  {
    label: "SESSION 5 — OWE  (Days 28–33)",
    subtitle: "Biblical Borrowing — Debt Categories, Dangers & the Path to Freedom",
    desc: "Debt is not a sin, but it is dangerous. This session brings biblical wisdom to bear on one of the greatest financial burdens Christians carry.",
    days: [
      ["Day 28", "The Three Debt Categories",                       "Read Session 5; study the three biblical debt categories",      "List every debt you carry. Categorize each as: wise/productive, neutral/manageable, or dangerous/bondage."],
      ["Day 29", "The 5 Dangers of Debt",                           "Study: compounding, trap, mortgages future, presumes, denies",  "Which of the 5 dangers is most present in your current debt load? What is it costing you beyond dollars?"],
      ["Day 30", "Biblical Principles of Borrowing",                "Study Prov. 22:7; Rom. 13:8; the borrowing principles",         "Review your debt list against the biblical principles. Which debts should you begin eliminating first and why?"],
      ["Day 31", "The 4 Borrowing Questions",                       "Study the 4 questions framework from Session 5",                "Apply all 4 questions to one debt decision you are currently facing or recently made. What do they reveal?"],
      ["Day 32", "A Debt Elimination Plan",                         "Study the debt elimination strategy options",                   "Build a simple debt elimination timeline: list each debt, balance, minimum payment, and target payoff date."],
      ["Day 33", "Session 5 Reflection & Application",              "Review all Session 5 content and debt notes",                   "Write a 'freedom declaration': the date you intend to be consumer-debt free and the plan to get there."],
    ]
  },
  {
    label: "SESSION 6 — GROW  (Days 34–40)",
    subtitle: "Growing Wealth with Kingdom Purpose — Confidence, Clarity & Consistency",
    desc: "The final session brings the entire study to completion: wealth built on God's principles, deployed for kingdom purposes, held with an open hand.",
    days: [
      ["Day 34", "Growing with Kingdom Purpose",                    "Read Session 6; study the kingdom investment concept",          "Write your answer to: 'If God truly owns it all, what is the purpose of the wealth He has placed in my hands?'"],
      ["Day 35", "Confidence Through Biblical Principles",          "Study the transferable concept: principles → confidence",       "Review all 5 principles from Session 2. Which one, applied consistently, would most change your financial future?"],
      ["Day 36", "Clarity in Communication & Goals",                "Study the clarity/communication section of Session 6",          "Are your financial goals written down? Are they clear enough to explain to a spouse or accountability partner?"],
      ["Day 37", "Consistency of Behavior",                         "Study the consistency theme from Session 6",                   "Identify one area where your financial behavior is inconsistent with your stated beliefs. Write one change to make."],
      ["Day 38", "The Sequential Investing Strategy",               "Study the 5-step sequential investing framework",               "Plot where you are in the sequence: debt elimination, emergency fund, savings, diversify, long-term goals."],
      ["Day 39", "Eternal Perspective & Kingdom ROI",               "Study Matt. 6:19–20; the eternal investment concept",          "Define 'kingdom ROI' for your household. Write one investment of time, talent, or treasure with kingdom impact."],
      ["Day 40", "40-Day Capstone — Full Review",                   "Re-read all six Learning Objectives sections",                  "Write your personal 'God Owns It All' covenant: who owns it, how you'll manage it, and what you'll do with it."],
    ]
  }
];

// ════════════════════════════════════════════════════════════════════
// BOOK 2 — MASTER YOUR MONEY  (40 days, 14 chapters expanded)
// Ch 1–2: 4 days | Ch 3–4: 4 days | Ch 5: 3 days | Ch 6: 3 days
// Ch 7: 3 days | Ch 8: 3 days | Ch 9: 3 days | Ch 10: 4 days
// Ch 11: 3 days | Ch 12: 4 days | Ch 13: 3 days | Ch 14: 3 days
// ════════════════════════════════════════════════════════════════════
const mymGroups = [
  {
    label: "CHAPTERS 1–2 — FOUNDATIONS  (Days 1–4)",
    subtitle: "Will I Ever Have Enough? + Four Biblical Principles of Money Management",
    desc: "The anchor of the entire book: the economy is unreliable but God is not. Every financial decision is a spiritual decision built on four unchanging biblical principles.",
    days: [
      ["Day 1",  "The Question Every Person Asks",                  "Read Ch. 1: Will I Ever Have Enough?",                          "Journal: What are your top three financial fears right now? Is your confidence in the economy or in God?"],
      ["Day 2",  "Three Financial Questions",                        "Re-read Ch. 1; study the three key questions",                  "Answer in writing: Will I ever have enough? Will it continue to be enough? How much is enough?"],
      ["Day 3",  "The 4 Biblical Principles — Part 1",              "Read Ch. 2; study principles 1–2 (God owns it; growth process)","In your own words explain: 'Every spending decision is a spiritual decision.' Give one example from your week."],
      ["Day 4",  "The 4 Biblical Principles — Part 2",              "Study Ch. 2 principles 3–4 (amount doesn't matter; faith acts)", "Which of the 4 principles is hardest for you to live out? Write one step to begin applying it this week."],
    ]
  },
  {
    label: "CHAPTERS 3–4 — PLANNING & MARGIN  (Days 5–8)",
    subtitle: "Financial Planning Overview + Guaranteed Financial Success",
    desc: "The objectives of money are to achieve goals and reflect values — not just accumulate more. Margin is the engine of every financial breakthrough.",
    days: [
      ["Day 5",  "Financial Planning Overview",                      "Read Ch. 3; study the 4-step planning process",                 "Map your current cash flow across the 5 uses of money. Which use is disproportionately large?"],
      ["Day 6",  "The 5 Uses of Money & Their Interconnection",     "Re-read Ch. 3; study 'no independent financial decisions'",     "Draw your personal pie chart by estimated percentage. Write what surprises you about what you see."],
      ["Day 7",  "Guaranteed Financial Success — Compounding",      "Read Ch. 4; study time value of money and compounding",         "Find one recurring expense (coffee, subscriptions, dining). Calculate its 10-year compounding opportunity cost."],
      ["Day 8",  "Building Margin Over Time",                        "Re-read Ch. 4; study the margin concept and delayed gratification","Write your current monthly margin (income minus all outgo). What one change would increase it by $100/month?"],
    ]
  },
  {
    label: "CHAPTER 5 — DEBT  (Days 9–11)",
    subtitle: "The Dangers of Debt — Five Dangers, Four Questions, One Path Forward",
    desc: "Debt is not a sin, but it is dangerous in ways most people underestimate. Biblical principles of borrowing bring both hope and a clear path to freedom.",
    days: [
      ["Day 9",  "The Five Dangers of Debt",                         "Read Ch. 5; study all five dangers carefully",                  "Which danger is most present in your life right now? Write one sentence about what it is costing you beyond money."],
      ["Day 10", "The Four Borrowing Questions",                     "Study the four criteria for responsible borrowing (Ch. 5)",     "Apply all four questions to your largest current debt. What do they reveal about whether the debt was wise?"],
      ["Day 11", "Hope, Not Shame — Debt Reflection",                "Re-read Ron & Michael's '40 Years of Reflection' sidebar",      "Write a personal debt inventory: every debt, balance, and interest rate. Then write one step toward freedom."],
    ]
  },
  {
    label: "CHAPTER 6 — WHERE AM I?  (Days 12–14)",
    subtitle: "Understanding Your Present Situation — Net Worth, Cash Flow & Insurance",
    desc: "You cannot plan where you are going until you honestly know where you are. This chapter provides the diagnostic tools every financial plan requires.",
    days: [
      ["Day 12", "Your Statement of Net Worth",                       "Read Ch. 6; complete the net worth statement worksheet",        "List all assets and all liabilities. Calculate your actual net worth. Does the number surprise you?"],
      ["Day 13", "Your Summary of Cash Flow",                         "Complete the cash flow summary from Ch. 6",                     "Track every dollar in and every dollar out for one week. Compare to your estimates. Where is the leakage?"],
      ["Day 14", "Insurance Coverage Analysis",                       "Study the insurance coverage section of Ch. 6",                 "Review your current life, disability, and property insurance. Identify one gap that needs immediate attention."],
    ]
  },
  {
    label: "CHAPTER 7 — FAITH GOALS  (Days 15–17)",
    subtitle: "Setting Faith Financial Goals — Purpose, Direction & Measurable Action",
    desc: "Goals are stewardship in sentences. Without them, money drifts toward what is urgent. Faith goals align resources with God's purposes for your life.",
    days: [
      ["Day 15", "Why Financial Goals Matter",                        "Read Ch. 7; study the four reasons for goals",                  "Which of the four barriers to goal-setting has stopped you in the past? Write how you will overcome it this time."],
      ["Day 16", "Writing Your Purpose Statement",                    "Study the purpose statement concept (Ch. 7)",                   "Draft a one-paragraph financial life purpose statement. What is money for in your life, specifically?"],
      ["Day 17", "Setting Measurable Faith Goals",                    "Study the four-step goal-setting process (Ch. 7)",              "Set three measurable financial goals: one short-term (90 days), one mid-term (1 year), one long-term (5+ years)."],
    ]
  },
  {
    label: "CHAPTER 8 — COMMON MISTAKES  (Days 18–20)",
    subtitle: "Avoiding the Most Common Financial Mistakes",
    desc: "A consumptive lifestyle, no budget, and poor vehicle decisions silently derail more financial plans than any external crisis. Awareness is the first step.",
    days: [
      ["Day 18", "The Consumptive Lifestyle",                         "Read Ch. 8; study the consumptive lifestyle mistake",           "Honestly audit your lifestyle. Name one area where consumption is outpacing your values and income."],
      ["Day 19", "No Budget — The Silent Killer",                     "Study the 'no budget' mistake and its consequences",            "If you have no current budget, write a draft budget today. If you have one, identify the category most off-track."],
      ["Day 20", "The Vehicle Trap & Other Mistakes",                 "Study the 'driving to the poorhouse' car decision section",     "Review your last vehicle decision. What did it cost over 5 years (payments + depreciation)? What would you do differently?"],
    ]
  },
  {
    label: "CHAPTER 9 — PERSONAL FINANCIAL PLAN  (Days 21–23)",
    subtitle: "Designing Your Personal Financial Plan — The Blueprint",
    desc: "This is the integration chapter: a financial plan is not a document, it is a set of decisions that align your cash flow with your goals and values.",
    days: [
      ["Day 21", "The Financial Planning Diagram",                    "Read Ch. 9; study the Financial Planning Diagram",              "Identify where you currently are in the planning process. Which of the 4 steps has never been completed?"],
      ["Day 22", "Analyzing Bob & Laura's Plan",                      "Study the Bob & Laura case study and charts (Ch. 9)",           "Use Bob & Laura's framework to identify 3 specific changes in your own cash flow that would increase your margin."],
      ["Day 23", "Writing Your Personal Financial Plan",              "Complete Ch. 9 action steps — your full plan draft",            "Write your personal financial plan: present situation, goals, margin-increase steps, and budget control method."],
    ]
  },
  {
    label: "CHAPTER 10 — CONTROL THE FLOW  (Days 24–27)",
    subtitle: "Budgeting — Estimate, Record, Build, Control",
    desc: "A budget is not a restriction — it is permission to spend intentionally. Four steps turn financial intentions into lived reality.",
    days: [
      ["Day 24", "Estimate Your Living Expenses",                     "Read Ch. 10; study the estimate step",                          "Build a complete monthly expense estimate from scratch. Include every category, even the irregular ones."],
      ["Day 25", "Record What Actually Happens",                      "Study the recording/tracking step (Ch. 10)",                   "Track every purchase today and tomorrow. Compare to your estimates from Day 24. What categories are off?"],
      ["Day 26", "Build Your Budget",                                 "Study the budget-building process (Ch. 10)",                   "Finalize your monthly budget with all categories. Make sure giving is a line item — not a leftover."],
      ["Day 27", "Control the Budget",                                "Study the budget control system (Ch. 10)",                     "Choose your budget control method (envelope, app, spreadsheet). Set it up today. Identify your accountability partner."],
    ]
  },
  {
    label: "CHAPTER 11 — TAX PLANNING  (Days 28–30)",
    subtitle: "Tax Planning — Biblical Perspective, Types of Taxes & Legal Strategies",
    desc: "Scripture speaks clearly about taxes. Understanding your tax obligations — and legal ways to reduce them — is faithful stewardship, not avoidance.",
    days: [
      ["Day 28", "What Scripture Says About Taxes",                   "Read Ch. 11; study the biblical tax principles",                "Read Rom. 13:1–7; Matt. 22:21. What is your attitude toward taxes? Is it shaped more by culture or Scripture?"],
      ["Day 29", "Types of Taxes and Their Implications",             "Study the types of taxes covered in Ch. 11",                   "List the taxes you currently pay (income, payroll, property, sales, capital gains). Which do you least understand?"],
      ["Day 30", "Avoiding (Not Evading) Taxes Legally",             "Study legal tax reduction strategies from Ch. 11",              "Identify two legal tax strategies you are not using (HSA, retirement contributions, charitable deductions, etc.). Plan to act."],
    ]
  },
  {
    label: "CHAPTER 12 — INVESTMENT PLANNING  (Days 31–34)",
    subtitle: "Sequential Investing — Accumulation, Preservation & Kingdom Strategy",
    desc: "Investing is stewardship with a strategy. The Sequential Investing Strategy eliminates guesswork and connects every investment decision to your long-term goals.",
    days: [
      ["Day 31", "Accumulation vs. Preservation Phases",             "Read Ch. 12; study the two phases of an investor's life",       "Which phase are you in — accumulation or preservation? Write what that means for your investment strategy today."],
      ["Day 32", "The Sequential Investing Strategy — Steps 1–3",   "Study steps 1–3: eliminate debt, emergency fund, savings",      "Which step are you on? What would it take to complete your current step within the next 12 months?"],
      ["Day 33", "The Sequential Investing Strategy — Steps 4–5",   "Study steps 4–5: diversify and complete long-term goals",       "What are your long-term investment goals? Write them down with target amounts and timelines."],
      ["Day 34", "Three Key Investing Questions",                     "Study the three questions (why, purpose, God's will) in Ch. 12","Answer all three investing questions for your current or next investment decision. Does your strategy reflect them?"],
    ]
  },
  {
    label: "CHAPTER 13 — STEWARDSHIP AFTER DEATH  (Days 35–37)",
    subtitle: "Estate Planning — Life Insurance, Wills & Legacy Stewardship",
    desc: "Stewardship does not end at death. A will, adequate insurance, and a clear estate plan are acts of love and faithful management of what God has entrusted to you.",
    days: [
      ["Day 35", "The Role of Life Insurance",                        "Read Ch. 13; study the life insurance section",                 "Do you have adequate life insurance? Calculate the income replacement your family would need for 10–15 years."],
      ["Day 36", "Estate Planning Fundamentals",                      "Study the estate planning section of Ch. 13",                   "Do you have a current will? If yes, review it. If no, write the name of the attorney you will call this week."],
      ["Day 37", "Stewardship After Death — Legacy",                  "Study the legacy and stewardship framing of Ch. 13",            "Write a one-paragraph statement of what you want your estate to communicate about your values and faith."],
    ]
  },
  {
    label: "CHAPTER 14 — GIVING LIVING  (Days 38–40)",
    subtitle: "Giving Living — When, Where & How Much: The Capstone of Mastered Money",
    desc: "The capstone of mastering your money is an open hand. Giving is not the last thing you do after everything else is handled — it is the point of everything else.",
    days: [
      ["Day 38", "Discerning When to Give",                           "Read Ch. 14; study the 'when to give' section",                 "Is your giving reactive (responding to requests) or proactive (planned and intentional)? Write what change you need to make."],
      ["Day 39", "Where and How Much to Give",                        "Study the 'where' and 'how much' sections of Ch. 14",           "List the organizations or causes you currently give to. Are they aligned with your values and calling? Adjust if needed."],
      ["Day 40", "40-Day Capstone — Master Your Money",               "Review your notes from all 14 chapters",                        "Write your Master Your Money personal covenant: your budget, debt plan, giving percentage, and investment strategy — in one page."],
    ]
  }
];

// ════════════════════════════════════════════════════════════════════
// BOOK 3 — GENEROUS LIVING  (40 days, 13 chapters expanded)
// Ch 1–3 given ~4 days each; Ch 4–9 ~3 days; Ch 10–13 ~3 days
// ════════════════════════════════════════════════════════════════════
const glGroups = [
  {
    label: "CHAPTER 1 — GENEROSITY & CONTENTMENT  (Days 1–4)",
    subtitle: "Generosity: The Secret to True Contentment",
    desc: "The amount of money you have has nothing to do with financial security or contentment. The secret to freedom and joy is directly linked to the willingness to be generous.",
    days: [
      ["Day 1",  "The Discontent Around Us",                          "Read Ch. 1; study the airplane opening illustration",           "Describe a time when having more did not bring the contentment you expected. What did you learn?"],
      ["Day 2",  "Generosity and Financial Freedom Are Linked",       "Study the core thesis of Ch. 1",                               "On a scale of 1–10, how would you rate your contentment right now? What role does generosity play in that number?"],
      ["Day 3",  "The Secret Revealed",                               "Study Luke 12:15–21 in connection with Ch. 1",                 "What would your life look like if generosity — not accumulation — were your primary financial orientation? Write it out."],
      ["Day 4",  "Chapter 1 Reflection",                              "Review Ch. 1 and your notes",                                  "Write your one-sentence answer to: 'What is the connection between generosity and contentment in my life right now?'"],
    ]
  },
  {
    label: "CHAPTER 2 — TREASURE HUNTING  (Days 5–7)",
    subtitle: "Where Is Your Heart? Following the Money to Find Your True Priorities",
    desc: "Your checkbook and calendar are the most honest autobiography you will ever write. This chapter uses your spending to reveal your actual — not stated — priorities.",
    days: [
      ["Day 5",  "The Heart and the Treasure",                        "Read Ch. 2; study Matthew 6:19–21",                            "Pull up last month's bank/credit card statement. What does it reveal about what you actually treasure?"],
      ["Day 6",  "Reading Your Financial Autobiography",              "Study the checkbook-as-autobiography concept (Ch. 2)",          "Identify the top three categories where your money goes. Do they reflect your stated values? Where is the gap?"],
      ["Day 7",  "Chapter 2 Reflection",                              "Review Ch. 2",                                                  "Write a one-paragraph 'financial autobiography': what story is your money telling about you right now?"],
    ]
  },
  {
    label: "CHAPTER 3 — OBSTACLES TO GENEROSITY  (Days 8–11)",
    subtitle: "Why Christians Don't Give — Seven Things That Hold Us Back",
    desc: "Seven barriers block generous living, moving from deeply spiritual obstacles to practical ones. Naming them is the first step to dismantling them.",
    days: [
      ["Day 8",  "Spiritual Obstacles (1–3)",                         "Read Ch. 3; study the first three obstacles to generosity",     "Which of the first three obstacles is most alive in your life? Write one honest sentence about how it operates."],
      ["Day 9",  "Practical Obstacles (4–7)",                         "Study obstacles 4–7, ending with 'failing to plan to give'",    "Which practical obstacle most limits your generosity? Design one specific step to remove it this month."],
      ["Day 10", "The Pyramid of Problems",                           "Study the 'Pyramid of Problems' diagram in Ch. 3",              "Identify where on the pyramid you currently sit. What is the foundational issue that must be resolved first?"],
      ["Day 11", "Chapter 3 Reflection & Action",                     "Review Ch. 3 and your two key obstacles",                      "Write a personal 'obstacle elimination plan': name your top two barriers and one action step for each."],
    ]
  },
  {
    label: "CHAPTER 4 — GENEROSITY AS LIFESTYLE  (Days 12–14)",
    subtitle: "Giving Time, Talents & Possessions — Generosity Beyond the Checkbook",
    desc: "Generosity is not a transaction — it is a way of life. This chapter expands the vision of giving from money to the full scope of what God has entrusted to you.",
    days: [
      ["Day 12", "Generosity Beyond Money",                           "Read Ch. 4; study the time/talent/possessions framework",       "List one way you could give each: time, a talent, and a possession. Which is hardest for you and why?"],
      ["Day 13", "A Generous Lifestyle in Practice",                  "Study the lifestyle generosity examples from Ch. 4",            "This week, practice one non-financial act of generosity each day. Journal briefly about what happened."],
      ["Day 14", "Chapter 4 Reflection",                              "Review Ch. 4 and your generosity journal",                     "Write: 'Being generous with my ________ is the area where God is most calling me to grow right now.'"],
    ]
  },
  {
    label: "CHAPTER 5 — PREPARATION  (Days 15–17)",
    subtitle: "Hearing God's Word — Letting Scripture Shape Your Generosity",
    desc: "Generosity that is not rooted in Scripture becomes either performance or self-congratulation. This chapter prepares your heart before the practical steps begin.",
    days: [
      ["Day 15", "Hearing God on Money",                              "Read Ch. 5; study the scriptural preparation framework",        "Identify five passages about generosity or money you have never studied deeply. Choose one to memorize this month."],
      ["Day 16", "Aligning Heart, Head & Habits",                    "Study the head/heart/habits framing from Ch. 5",                "In which area are you weakest: your beliefs about giving (head), your motivations (heart), or your habits (action)?"],
      ["Day 17", "Chapter 5 Reflection",                              "Review Ch. 5; journal your preparation",                       "Write a prayer about your generosity: where you are, where you want to be, and what you need from God to get there."],
    ]
  },
  {
    label: "CHAPTER 6 — PROBLEM SOLVING  (Days 18–20)",
    subtitle: "Getting a Fix on Your Finances — Removing the Barriers That Block Generosity",
    desc: "You cannot give away what you do not have. Practical financial health is not the enemy of generosity — it is its prerequisite.",
    days: [
      ["Day 18", "Diagnosing Your Financial Barriers",               "Read Ch. 6; study the financial problem-solving framework",     "What is the number one financial problem currently limiting your ability to give? Be specific and honest."],
      ["Day 19", "The Fivefold Increase in Giving",                  "Study the statistic: planning increases giving fivefold (Ch. 6)","Do you currently have a written financial plan? If not, what is stopping you? If yes, how has it affected your giving?"],
      ["Day 20", "Chapter 6 Reflection",                              "Review Ch. 6",                                                  "Write a one-page 'financial problem diagnosis': identify your top two financial barriers and a solution path for each."],
    ]
  },
  {
    label: "CHAPTER 7 — THE RIGHT PERSPECTIVE  (Days 21–23)",
    subtitle: "Seeing Things As God Sees Them — A God-Sized View of Your Life and Resources",
    desc: "The most important financial tool is not a budget — it is a perspective. Seeing your resources as God sees them changes every decision you make with them.",
    days: [
      ["Day 21", "A God-Sized View of Life",                          "Read Ch. 7; study the perspective-shifting framework",          "If God held your checkbook today, what story would it tell about His priorities vs. your own?"],
      ["Day 22", "Time, Eternity & Money",                            "Study the eternal framing of Ch. 7; reread Matt. 6:19–21",      "Name one financial decision you need to make this year. How does an eternal perspective change your answer?"],
      ["Day 23", "Chapter 7 Reflection",                              "Review Ch. 7 and Chs. 4–7 together",                           "Write: 'The way I most need to shift my perspective on money to see it as God sees it is ____________________.'"],
    ]
  },
  {
    label: "CHAPTER 8 — THE PLAN  (Days 24–26)",
    subtitle: "How Generous Do You Want to Be? Building a Strategic Giving Plan",
    desc: "Without a plan, giving is always whatever is left over. This chapter moves you from reactive to strategic, from occasional to intentional.",
    days: [
      ["Day 24", "How Generous Do You Want to Be?",                  "Read Ch. 8; study the giving plan framework",                   "Answer the chapter's core question: How generous do you want to be? Write a specific percentage target and why."],
      ["Day 25", "Building Your Formal Giving Plan",                  "Study the giving plan steps from Ch. 8",                       "Draft your formal giving plan: percentage of income, two recipient organizations, and one stretch giving goal for the year."],
      ["Day 26", "Chapter 8 Reflection",                              "Review Ch. 8 and your giving plan draft",                      "Share your giving plan with your spouse or a trusted friend. Ask for accountability to reach your percentage target."],
    ]
  },
  {
    label: "CHAPTER 9 — STRATEGIC GIVING  (Days 27–29)",
    subtitle: "Making Your Charitable Contributions Count — Tools, Vehicles & Impact",
    desc: "Not all giving is equally strategic. This chapter provides the tools to evaluate charities, maximize tax efficiency, and direct resources where they have the greatest kingdom impact.",
    days: [
      ["Day 27", "Evaluating Charities and Ministries",              "Read Ch. 9; study the charity evaluation framework",            "Research two organizations you currently support. What percentage of funds goes to the stated mission?"],
      ["Day 28", "Donor-Advised Funds and Giving Vehicles",          "Study the strategic giving vehicles covered in Ch. 9",          "Identify one giving vehicle you have never used (DAF, appreciated stock, planned gift). Research it this week."],
      ["Day 29", "Chapter 9 Reflection",                              "Review Ch. 9 and your current giving recipients",              "Audit your giving list: Does each recipient reflect your values and calling? Add one; remove one if needed."],
    ]
  },
  {
    label: "CHAPTER 10 — GIVING TO YOUR CHILDREN  (Days 30–32)",
    subtitle: "Passing Down More Than Money — Wisdom, Work Ethic & Inheritance",
    desc: "Financial assets should not be passed on without first handing down wisdom. The prodigal son story frames the danger of giving wealth without values.",
    days: [
      ["Day 30", "Passing Down Wisdom Before Wealth",                "Read Ch. 10; study the prodigal son and inheritance framing",   "What financial values are you intentionally transferring to your children (or the next generation) right now?"],
      ["Day 31", "How Much to Give Your Children?",                   "Study the 'how much' framework and observations from Ch. 10",   "Reflect: Could a large inheritance harm your children's work ethic, marriage, or self-reliance? What is your plan?"],
      ["Day 32", "Chapter 10 Reflection",                             "Review Ch. 10",                                                 "Write a 'generational giving statement': what you intend to give your children (wisdom, assets, timing) and why."],
    ]
  },
  {
    label: "CHAPTER 11 — GIVING THROUGH YOUR WILL  (Days 33–35)",
    subtitle: "Six Critical Estate Decisions You Need to Make",
    desc: "Your will is your final financial statement — a declaration of what you valued and who you trusted. Making these six decisions is an act of love and stewardship.",
    days: [
      ["Day 33", "Why Most People Don't Have a Will",                "Read Ch. 11; study the opening 'will paralysis' section",       "Do you have a current will? If not, write the name and number of an estate attorney you will call this week."],
      ["Day 34", "The Six Critical Estate Decisions",                "Study all six decisions in the estate planning process (Ch. 11)","Work through each of the six decisions for your own situation. Write a one-line answer to each decision."],
      ["Day 35", "Chapter 11 Reflection",                             "Review Ch. 11; draw your own estate decision map",             "Does your current will (or planned will) reflect your stated values about faith, family, and charity?"],
    ]
  },
  {
    label: "CHAPTER 12 — A FORMAL TALK  (Days 36–37)",
    subtitle: "Holding a Family Conference — Communicating Your Estate Plan to Your Heirs",
    desc: "Every family has a conference eventually. The only question is whether you control it or circumstances do. A planned family conference is a gift to your heirs.",
    days: [
      ["Day 36", "Why Hold a Family Conference?",                    "Read Ch. 12; study the family conference concept",              "What would be the greatest benefit of holding a family conference in your family? What is the biggest obstacle?"],
      ["Day 37", "Planning and Holding Your Conference",             "Study the transgenerational planning chart and agenda (Ch. 12)", "Draft a one-page agenda for your family conference. Include: estate overview, giving plan, and values statement."],
    ]
  },
  {
    label: "CHAPTER 13 — THE WEALTH PARADOX  (Days 38–40)",
    subtitle: "Opportunity Knocks — Solving the Wealth Paradox & Launching a Generous Legacy",
    desc: "The final challenge: faithful stewardship builds wealth, and wealth can undermine the very generosity that made it possible. The solution is a proactive, intentional commitment to generosity as a way of life.",
    days: [
      ["Day 38", "The Wealth Paradox Defined",                        "Read Ch. 13; study the wealth paradox concept",                 "Have you experienced the wealth paradox — where more financial security has made you less generous? Describe it."],
      ["Day 39", "Seizing the Opportunity",                           "Study the 'seizing the opportunity' section of Ch. 13",         "Identify one specific kingdom opportunity in front of you right now that would require generosity to pursue."],
      ["Day 40", "40-Day Capstone — Generous Living Covenant",       "Review all three parts of the book and your notes",             "Write your Generous Living covenant: your giving plan, your family legacy statement, and your lifestyle commitment — one page."],
    ]
  }
];

// ════════════════════════════════════════════════════════════════════
// DOCUMENT BUILDER
// ════════════════════════════════════════════════════════════════════
function buildBookSection(titleLine1, titleLine2, titleLine3, weekData, darkColor, medColor, lightColor) {
  const nodes = [];
  // Cover
  coverTitle(titleLine1, titleLine2, titleLine3, darkColor).forEach(n => nodes.push(n));

  for (const week of weekData) {
    nodes.push(sectionBanner(week.label, darkColor, lightColor));
    nodes.push(sp(60,40));
    nodes.push(new Paragraph({
      spacing:{before:0,after:100},
      children:[new TextRun({text:week.subtitle,bold:true,size:22,font:"Arial",color:medColor})]
    }));
    nodes.push(new Paragraph({
      spacing:{before:0,after:120},
      children:[new TextRun({text:week.desc,size:20,font:"Arial",color:MGRAY,italics:true})]
    }));
    nodes.push(buildTable(
      week.days.map(([d,t,r,a]) => dayRow(d,t,r,a,lightColor,medColor)),
      darkColor
    ));
    nodes.push(sp(120,80));
  }
  return nodes;
}

const allChildren = [];

// ── BOOK 1: GOIA ──
buildBookSection(
  "God Owns It All", "Ron Blue with Michael Blue  ·  40-Day Reading Plan",
  "Six Sessions  ·  Perspective · Principles · Live · Give · Owe · Grow",
  goiaWeeks, GOIA_DARK, GOIA_MED, GOIA_LIGHT
).forEach(n => allChildren.push(n));

allChildren.push(new Paragraph({children:[new PageBreak()]}));

// ── BOOK 2: MYM ──
buildBookSection(
  "Master Your Money", "Ron Blue with Michael Blue  ·  40-Day Reading Plan",
  "Fourteen Chapters  ·  From Biblical Foundations to Giving Living",
  mymGroups, MYM_DARK, MYM_MED, MYM_LIGHT
).forEach(n => allChildren.push(n));

allChildren.push(new Paragraph({children:[new PageBreak()]}));

// ── BOOK 3: GL ──
buildBookSection(
  "Generous Living", "Ron Blue  ·  40-Day Reading Plan",
  "Thirteen Chapters  ·  Living & Giving with Joy · Process · Practical Applications",
  glGroups, GL_DARK, GL_MED, GL_LIGHT
).forEach(n => allChildren.push(n));

// ── ASSEMBLE ──
const doc = new Document({
  styles: {
    default: { document: { run: { font:"Arial", size:20 } } },
    paragraphStyles: [
      { id:"Heading1", name:"Heading 1", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{size:36,bold:true,font:"Arial",color:NAVY},
        paragraph:{spacing:{before:360,after:200},outlineLevel:0} },
      { id:"Heading2", name:"Heading 2", basedOn:"Normal", next:"Normal", quickFormat:true,
        run:{size:26,bold:true,font:"Arial",color:NAVY},
        paragraph:{spacing:{before:240,after:120},outlineLevel:1} },
    ]
  },
  sections:[{
    properties:{
      page:{
        size:{width:12240,height:15840},
        margin:{top:900,right:900,bottom:900,left:900}
      }
    },
    children: allChildren
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/mnt/user-data/outputs/Three_40Day_Reading_Plans_GOIA_MYM_GL.docx', buf);
  console.log('Done!');
});
