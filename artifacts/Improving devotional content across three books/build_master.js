const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageBreak
} = require('docx');
const fs = require('fs');

const GRAY = "F2F2F2";
const BLUE = "1F4E79";
const LIGHTBLUE = "D6E4F0";
const GOLD = "FFF2CC";
const GREEN = "E2EFDA";
const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 360, after: 120 },
    children: [new TextRun({ text, bold: true, size: 32, font: "Arial", color: BLUE })]
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 240, after: 80 },
    children: [new TextRun({ text, bold: true, size: 26, font: "Arial", color: "2E75B6" })]
  });
}

function h3(text) {
  return new Paragraph({
    spacing: { before: 160, after: 60 },
    children: [new TextRun({ text, bold: true, size: 24, font: "Arial", color: "404040" })]
  });
}

function body(text) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, size: 22, font: "Arial" })]
  });
}

function bodyRuns(runs) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    children: runs
  });
}

function label(text) {
  return new TextRun({ text, bold: true, size: 22, font: "Arial" });
}

function normal(text) {
  return new TextRun({ text, size: 22, font: "Arial" });
}

function italic(text) {
  return new TextRun({ text, italics: true, size: 22, font: "Arial", color: "555555" });
}

function quote(text) {
  return new Paragraph({
    spacing: { before: 80, after: 80 },
    indent: { left: 720, right: 720 },
    children: [new TextRun({ text: `"${text}"`, italics: true, size: 22, font: "Arial", color: "404040" })]
  });
}

function bullet(text) {
  return new Paragraph({
    spacing: { before: 40, after: 40 },
    numbering: { reference: "bullets", level: 0 },
    children: [new TextRun({ text, size: 22, font: "Arial" })]
  });
}

function rule() {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 1 } },
    children: []
  });
}

function shade(children, color = GOLD) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            borders,
            width: { size: 9360, type: WidthType.DXA },
            shading: { fill: color, type: ShadingType.CLEAR },
            margins: { top: 120, bottom: 120, left: 200, right: 200 },
            children
          })
        ]
      })
    ]
  });
}

function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

// ─── SECTION: TITLE PAGE ───────────────────────────────────────────────────

const titlePage = [
  new Paragraph({ spacing: { before: 1440 }, children: [] }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "40-DAY DEVOTIONAL", bold: true, size: 48, font: "Arial", color: BLUE })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text: "Master Source & Story Mapping Guide", bold: false, size: 28, font: "Arial", color: "555555" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 40, after: 400 },
    children: [new TextRun({ text: "God Owns It All · Master Your Money · Generous Living", italics: true, size: 24, font: "Arial", color: "777777" })]
  }),
  rule(),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 160 },
    children: [new TextRun({ text: "For the Writing Team — Internal Use Only", size: 20, font: "Arial", color: "999999" })]
  }),
  pageBreak()
];

// ─── SECTION: HOW TO USE THIS DOCUMENT ────────────────────────────────────

const howToUse = [
  h1("How to Use This Document"),
  body("This guide maps every Ron Blue transcript story, story bank entry, and book source to the specific devotional days they serve. It is organized in two ways:"),
  bullet("Part 1 — Source Inventory: A complete reference of every usable story and where it lives (transcript, book, story bank)"),
  bullet("Part 2 — Day-by-Day Story Map: For each of the 21 days across GOIA, MYM, and GL, the recommended primary story, supporting material, and writing notes"),
  bullet("Part 3 — Gap Analysis: What is still missing and what to ask for"),
  new Paragraph({ spacing: { before: 100 }, children: [new TextRun({ text: "The goal is not to replace the devotional content — it is to replace the abstract language with Ron\u2019s actual voice, stories, and teaching moments so the devotional feels like it was written by Ron Blue, not about him.", italics: true, size: 22, font: "Arial" })] }),
  rule(),
  pageBreak()
];

// ─── PART 1: SOURCE INVENTORY ──────────────────────────────────────────────

const part1 = [
  h1("PART 1 — Source Inventory"),
  h2("A. Ron Blue Transcripts (Video Sessions)"),

  h3("GOIA Session 1 — Worldview, Ownership, Stewardship"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "god_owns_it_all_session_1_v1.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Best for: GOIA Days 1–5, MYM Day 1", bold: true, size: 21, font: "Arial" })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Kenya Pastor  "), italic("(Session 1, ~1:14)")]),
  body('Ron is with Crew Ministries, looking down at a pastor\'s mud hut in Kenya. He asks: "What is the greatest barrier to the spread of the gospel here?" He expected transportation, money, or tribalism. The pastor said: materialism. "If a man has a mud hut, he wants a stone hut. If he has a thatch roof, he wants a metal roof. If he\'s got one cow, he wants two cows." Ron\'s realization: materialism isn\'t unique to America — it\'s unique to the heart.'),
  bodyRuns([label("Best for: "), normal("GOIA Day 3 (Your Name on the Label) — opens the teaching on 'mine' as identity drift. Also strong for MYM Day 1 as the global context for why ownership matters.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Heart Surgeon / Million-Dollar Home  "), italic("(Session 1, ~12:49)")]),
  body("A young heart surgeon in his late 30s asks Ron: 'Is it okay for a Christian to live in a million-dollar home?' Ron turns the question back: 'What do you think God wants you to do?' The surgeon admits he doesn\u2019t pray or study Scripture — he\u2019s in surgery by 6am. Ron: 'What are you doing at four in the morning? Generally sleeping. Then you don\u2019t have anything better to do.' A year and a half later the surgeon\u2019s wife tells Ron he\u2019s now spending 2–3 hours daily in prayer and Bible study. That home became a center for ministry — hundreds came to Christ there. He became a leading evangelical, chairman of several international ministries, and never asked Ron the question again."),
  bodyRuns([label("Best for: "), normal("GOIA Day 5 (The Real Test) or MYM Day 22 (Start With Reality). Illustrates that the right question isn\u2019t 'how much is enough?' but 'Lord, what would you have me do?'")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Teaching: Money as Tool, Test, Testimony  "), italic("(Session 1, ~15:14)")]),
  body("Ron distills how God uses money in three ways. As a tool — something we manage. As a test — Paul said 'I have learned to be content in whatever circumstances.' As a testimony — the world has a right to look at Christians and see they\u2019re different. Not better — different. They\u2019re content in the middle of confusion. They make principle-based decisions and communicate clearly."),
  bodyRuns([label("Best for: "), normal("GOIA Day 1 (Foundation) or Day 7 (New Default). The testimony framing is particularly strong for Day 7.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Teaching: The Three Questions  "), italic("(Session 1, ~11:51)")]),
  body("The world asks: Will I ever have enough? Will it continue to be enough? How much is enough? These are wrong questions. The biblical worldview asks three different questions: Who owns it? How much is enough (as a stewardship question)? Is the next steward chosen and prepared? Ron: 'If God owns it, that means I am a steward — and it changes everything about the way I view money and possessions.'"),
  bodyRuns([label("Best for: "), normal("GOIA Day 1 opening or MYM Day 1. This is Ron\u2019s clearest statement of the foundational shift.")]),

  rule(),

  h3("GOIA Session 2 — Principles, Pie Chart, Foundation"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "god_owns_it_all_session_2_v1.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Best for: MYM Days 8–14, GOIA Day 2", bold: true, size: 21, font: "Arial" })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Congressional Testimony  "), italic("(Session 2, ~8:06 — also in MYM transcripts)")]),
  body("Ron is asked to testify before a congressional subcommittee in the early 1990s. Senator asks: 'What would you tell the American family?' Ron gives four principles — spend less than you earn, avoid debt, build margin, set long-term goals. He expects the senator to laugh. Instead, the senator picks up his pencil and writes them down. Then: 'It seems to me those would work at any income level.' Ron: 'You\u2019re right, senator — including the United States government.' They had quite a conversation after. Ron later added a fifth: give generously."),
  bodyRuns([label("Best for: "), normal("MYM Day 8 (God\u2019s Wisdom Has a Shape). Also useful as a brief opener for any MYM day introducing a principle.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: Galveston Island / Hurricane Ike  "), italic("(Session 2, ~6:05)")]),
  body("Ron sees a photograph of Galveston Island after Hurricane Ike — everything flattened except one house. The family had survived a hurricane before and lost their home, so they built a hurricane-proof house on a solid foundation. When the storms came, it was damaged but standing. 'That\u2019s the only house on the island.' Ron\u2019s application: hurricanes will come — health, job loss, the unexpected — but if we build on God\u2019s transcendent principles, we will survive."),
  bodyRuns([label("Best for: "), normal("MYM Day 8 (foundation/principles) or GOIA Day 7 (New Default). The image is vivid and earned.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The 2008 Crash — Merrill Lynch Advisor  "), italic("(Session 2, ~16:16)")]),
  body("A friend who was a significant financial advisor at Merrill Lynch — working with clients of $50 million and up — lost half his retirement in the 2008 crash. He and his wife asked: 'What did we do wrong?' Then they realized: they lived within their income, paid off all debt, had liquidity, were saving long-term, had goals for their kids\u2019 education. They hadn\u2019t done anything wrong. 'The hurricane came and our house received some damage, but there\u2019s nothing else I could have done to avoid that.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 15 (Freedom Isn\u2019t Independence from God) or Day 17 (Power of Margin). Powerful because it shows principles working even when circumstances don\u2019t.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: Pastor Debt-Free at 41  "), italic("(Session 2, ~12:17)")]),
  body("A 41-year-old associate pastor comes to Ron. He and his wife, right out of college, made a decision to become totally debt-free as soon as possible. It took 16 years. 'Our friends thought we were crazy because we had no home mortgage, no credit card debt, no debt whatsoever.' With one less piece of the pie, he now had freedom to allocate to giving — which reduced taxes — which increased his ability to live more generously."),
  bodyRuns([label("Best for: "), normal("MYM Day 10 (Avoid Debt) or Day 12 (Plan for Margin). Clean, brief, real.")]),

  rule(),

  h3("GOIA Session 3 — Lifestyle / How Much Is Enough"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "god_owns_it_all_session_3_v1.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Best for: GOIA Days 3–4, MYM Days 17, 22–24, GOIA Day 7", bold: true, size: 21, font: "Arial" })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Green Trailer  "), italic("(Session 3, ~6:52)")]),
  body("Ron and Judy got married while he still had a year left in college and two years of graduate school. Their first home was the cheapest married housing at Indiana University: a green trailer 28 feet long, 6 feet wide, 8 feet tall. Ron: 'You could sit on the toilet, cook dinner, and do your ironing without moving.' When Judy ironed, Ron either left or went to the back bedroom — there wasn\u2019t room for the ironing board and him. They had no choices: not where to eat out (they didn\u2019t go), not what cars to buy, not what clothes. 'When you don\u2019t have any choices, life is relatively simple.' Fast forward 50 years, five children, 13 grandchildren, multiple homes, many cars, college educations — the paradox of prosperity: more options, less real freedom."),
  bodyRuns([label("Best for: "), normal("MYM Day 23 (The Paradox of Prosperity) or GOIA Day 3. Grounds the entire lifestyle section in lived experience rather than abstraction.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: Dr. Bill Bright / 'What Does a Million-Dollar Giver Look Like?'  "), italic("(Session 3, ~1:14)")]),
  body("Dr. Bill Bright, founder of Campus Crusade (now Cru), knew Ron worked with wealthy people. He asked: 'Ron, what does a million-dollar giver look like?' Ron\u2019s answer came immediately: 'Bill, if they look like they can give you a million, they probably can\u2019t.' Ron\u2019s experience: those who could give away the most had typically chosen a lifestyle less than what they could have afforded by the world\u2019s definition. Tom Stanley later proved it in The Millionaire Next Door."),
  bodyRuns([label("Best for: "), normal("GOIA Day 3 (Your Name on the Label) or MYM Day 24 (Lifestyle and the Finish Line).")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Physician with Holes in His Shoes  "), italic("(Session 3, ~3:14)")]),
  body("A physician client asked Ron to hold him accountable to maintaining his med-school lifestyle — even as he started earning significant income. He had taken a mission trip to Haiti as a teenager and was impassioned about the poor. He and his wife in med school decided to cap their lifestyle at that level and give away everything above it. One day a patient noticed holes in his shoes as his legs were crossed. The patient was a shoe salesman. 'Would you be willing to let me buy your shoes for the rest of your life?' The doctor had to learn to receive in order to give. Another time: his in-laws in Seattle invited the family to a reunion. The family in Alabama couldn\u2019t afford the plane tickets because of their giving commitments — a physician who had to accept a gift from his in-laws. His lesson to Ron: 'You have to receive in order to give. I had to learn that first.'"),
  bodyRuns([label("Best for: "), normal("GOIA Day 4 (Owned and Loved — stewardship as response, not performance) or GL Day 34 (Whole-Life Generosity). The most concrete illustration of lifestyle stewardship in the entire archive.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Teaching: Contentment — No Regrets, No Envy, No Fear  "), italic("(Session 3, ~12:39)")]),
  body("Ron quotes pastor David Jeremiah\u2019s definition of contentment: no regrets of the past (Jesus took care of the past), no envy in the present (where envy exists there is disorder and evil), and no fear of the future (because you know who is already in the future). Ron: 'If I have no envy in the present, no regrets of the past, and no fear of the future because of who the Lord Jesus Christ is — think about the freedom that comes from all of that.'"),
  bodyRuns([label("Best for: "), normal("GOIA Day 6 (Anxiety and Ownership) or Day 7 (New Default). Also MYM Day 21 (Worship, Not Achievement).")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The John Steinbeck Letter (1959)  "), italic("(Session 3, ~23:48 — also in MYM transcripts)")]),
  body("John Steinbeck wrote to Adlai Stevenson in November 1959. Ron found it in Randy Alcorn\u2019s book. Steinbeck was writing about the materialism of Christmas, but what struck Ron was one line he called prophetic: 'A strange species we are. We can stand anything that God and nature can throw at us, save plenty. If I wanted to destroy a nation, I would give it too much, and I would have it on its knees — miserable, greedy, rich, and sick.' Ron: 'That was 1959. The world has never seen a runup in wealth like what America has accomplished since, and it has not given us contentment, peace, or freedom. If anything, it has caused anxiety and confusion.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 23 (The Paradox of Prosperity) or GOIA Day 3. Works as a standalone cultural-moment illustration.")]),

  rule(),

  h3("GOIA Session 4 — Giving"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "god_owns_it_all_session_4_v1.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Best for: GL Days 29–35, 37–38", bold: true, size: 21, font: "Arial" })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The \\$10,000 Vacation Pledge  "), italic("(Session 4, ~20:25)")]),
  body("When Ron was just starting his financial planning business, he and Judy attended a conference and made a pledge to give $10,000 to a ministry — with no date attached, more a faith goal. A year later they revisited it. The only thing they had was a $10,000 vacation fund saved for a guest ranch trip in Colorado with their five children. Ron happened to be reading 2 Corinthians 8 at the time: 'Now finish the task as well... complete it out of what you have.' Ron: 'It was like, Dear Ron, this is written to you.' They wrote the check and canceled the reservation. The ranch owner called back and offered to fly the whole family out free and put them up for the week in exchange for Ron speaking to his staff. That year the family also took a Caribbean cruise and a seaside resort trip — all paid. 'We had three vacations that year that would have cost us a lot of money, and it was several years before we ever paid for a vacation again. God gave beyond what I could ask, think, or even imagine.'"),
  bodyRuns([label("Best for: "), normal("GL Day 31 (Cheerful, Not Pressured) or Day 33 (Spontaneous Generosity). The definitive Ron Blue personal giving story.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Chick-fil-A \\$100  "), italic("(Session 4, ~25:17 — also in MYM transcripts)")]),
  body("Ron and one of his sons had breakfast weekly at a Chick-fil-A. The same Hispanic woman worked the counter — she knew their order before they reached her. One day walking out, Ron thought: 'You tip waitresses in restaurants. Why don\u2019t you tip people in fast food?' He reached in his wallet — had several twenties. Pulled one out to give. Ron: 'The Lord said, You cheap skate. You\u2019ve got a lot of twenties.' He took out five, folded them over so she couldn\u2019t see the amount, and asked if she could take a tip. She said yes. A week or two later she came to his table: 'When you gave me that money, I needed a set of tires.' But that evening her daughter came home from high school — a classmate\u2019s apartment had burned, they\u2019d lost everything. She gave them the hundred dollars. 'I gave out of my abundance. She gave out of her poverty.' Ron\u2019s conclusion: giving generously has nothing to do with income. It has everything to do with a heart attitude."),
  bodyRuns([label("Best for: "), normal("GL Day 33 (Spontaneous Generosity). Best illustration in the archive of the chain of generosity — one act multiplying.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Weekly Tithe Practice  "), italic("(Session 4, ~13:51)")]),
  body("Ron and Judy\u2019s personal practice: every week they sit down and ask what income came in that week. They write a check for exactly 10% — sometimes $51.26, sometimes $600.85. Ron: 'I\u2019m sure people who count the collection think it\u2019s pretty unusual.' They don\u2019t do it legalistically but out of conviction that on the first day of the week they want to recognize what God provided. 'It is only the beginning of our giving.' They give additionally to missionaries, parachurch organizations, and the poor — including non-deductible cash gifts. 'I love giving cash spontaneously — buying groceries for somebody. Every time I give someone a $20 bill, I say: This is a gift from the Lord Jesus Christ. I\u2019m just his ambassador.'"),
  bodyRuns([label("Best for: "), normal("GL Day 32 (Proportionate Giving). Ron\u2019s own practice, not just his teaching.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: Grandchildren \\$100 Giving Assignment  "), italic("(Session 4, ~17:34)")]),
  body("Ron and Judy give each grandchild $100 at Thanksgiving — starting as young as age two. The instruction: 'Your gift to us is to give this money away, then write us a letter or make a video telling us where you gave it.' Ron: 'We want them to experience the joy of giving. And it is incredible how they grasp that idea.' One son\u2019s three boys in Austin used their Thanksgiving money at Walmart to buy sleeping bags, nutrition bars, and supplies for homeless people. They went out and handed them to people on the streets. One homeless man took his bag, walked across the street, and shared the contents with another homeless person. 'What an unbelievable lesson for those young people.'"),
  bodyRuns([label("Best for: "), normal("GL Day 34 (Whole-Life Generosity) or Day 39 (7-Day Open-Hand Challenge).")]),

  rule(),

  h3("GOIA Session 5 — Debt"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "god_owns_it_all_session_5_v1.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Best for: MYM Days 12–13, GOIA Day 6 (conviction moment)", bold: true, size: 21, font: "Arial" })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The \\$10,000 Line of Credit  "), italic("(Session 5, ~4:49)")]),
  body("When Ron started his financial planning business, he went to the bank and arranged a $10,000 line of credit — standard business practice. Then God convicted him: 'You\u2019re going to start a business giving people financial advice, and you\u2019re going to begin with debt?' Ron canceled it with no backup plan and a family to feed. Shortly after, a friend introduced him to the head of training at Coca-Cola, who asked Ron to develop and teach a retirement seminar. The man outlined the scope and asked what Ron would charge. Ron: 'Do you mean you pay for that stuff?' He had no idea. The man calculated: $6,000 to develop it, $1,000 each time to teach it four times. Total: $10,000 — exactly what the line of credit would have been. And he offered to pay immediately, in December, to get it into that year\u2019s budget. Ron: 'God gave me back exactly what I gave up, and in a way I never would have imagined.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 12 (Plan for Margin) or GOIA Day 6 (Anxiety and Ownership). The most direct personal illustration of 'don\u2019t presume on the future' and 'don\u2019t deny God an opportunity to provide.'")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The NFL Player with Three Super Bowl Rings  "), italic("(Session 5, ~23:39)")]),
  body("Ron is teaching a group of Christian professional football players about biblical financial principles. He says: 'Husbands should never take on any debt unless their wife is in perfect agreement.' At the back of the room sits a man with three Super Bowl rings — a well-known player — and his wife is weeping. After the session, she approaches Ron: 'We are getting ready to declare bankruptcy. My husband took on debt that I did not want him to take on, and the business has failed. We\u2019ve lost everything we accumulated in professional ball.' Ron: 'He was not a bad person. He tended to be optimistic — he was used to winning. He didn\u2019t listen to the gift God had given him. My mentor Howard Hendricks always said: God gave you a spouse not to frustrate you, but to complete you.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 19 (Money Talks in Marriage) or Day 13 (The Four Questions / borrowing).")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: The Seminary Student and the Mission Field  "), italic("(Session 5, ~21:46)")]),
  body("A seminary student calls Ron on a radio program. God has called him to the mission field, but he\u2019s considering student debt. Ron\u2019s counsel: 'If you\u2019ve got enough money to go for two weeks, go for two weeks. Enough for a month, go for a month. Allow God to provide — that will tell you how long it takes. When you\u2019re done, you\u2019ll have no debt and can go straight to the mission field.' Several years later, Ron receives a letter: the young man is on the mission field. He lists all the ways God provided — dorm counselor, waiting tables, scholarships, gift money, people letting him stay in their homes. 'God provided everything I needed. When I finished, I had no debt.' Ron: 'A lot of times we take the conventional way to solve a problem when God wants to show us his faithfulness.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 13 (The Four Questions) or Day 18 (Dangers of Debt).")]),

  rule(),

  h3("Bloomington Roundtable — Conversational Teaching"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "God_Owns_it_all_Bloomington.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Best for: MYM Day 3, Day 22, Day 24, GOIA Day 7", bold: true, size: 21, font: "Arial" })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Teaching: 'Enough Isn\u2019t a Number — It\u2019s a Person'  "), italic("(Bloomington, ~4:39)")]),
  body("In the roundtable, Ron says: 'Paul teaches us in Philippians that enough isn\u2019t really a number — it\u2019s a lesson, a faith issue. He says I\u2019ve learned to be content. That\u2019s pretty important. And that means contentment is taught by God and practiced by us.' A panelist adds: 'It\u2019s not a number, it\u2019s a person' — finding contentment in Christ himself. Ron: 'The finish line concept is a target, but God\u2019s target for me is contentment.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 22 (Start with Reality) or GOIA Day 7 (New Default).")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Story: Two Clients — Million-Dollar Home vs. Trailer Park  "), italic("(Bloomington, ~7:54)")]),
  body("Ron had two clients. One lived in a million-dollar home (the heart surgeon). Another was a CEO of a major grocery chain who lived in a trailer park. Both wanted to maximize their giving. Ron: 'It wasn\u2019t wrong for one to live in a million-dollar home, and it wasn\u2019t right for one to live in a trailer park. It was a lifestyle choice, driven by: I have enough.' He knew the physician had reached contentment when he sold his Porsche and bought a Honda. 'Physicians don\u2019t drive Hondas into the physician\u2019s parking lot.' He had to park down the street."),
  bodyRuns([label("Best for: "), normal("MYM Day 24 (Lifestyle and the Finish Line). Perfectly illustrates that the right lifestyle is between you and God — not a formula.")]),

  rule(),

  h3("MYM Transcripts — Interview Clips"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "Master_your_Money_Transcripts_-_All_Videos.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Best for: MYM Days 1–2, 9–12, 16", bold: true, size: 21, font: "Arial" })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Quote: Every Decision Is a Spiritual Decision  ")]),
  body("'Once you recognize God\u2019s ownership, 100% of what you have belongs to him. That means every spending decision I make is a spiritual decision — because I\u2019m a steward. It\u2019s no more spiritual to give than it is to go on vacation. If I\u2019m using what he entrusted to me, every decision financially is a decision about using his resources. It\u2019s the most fundamental decision a Christian can make, and once they make it, everything changes. They began seeing things in Scripture they didn\u2019t see before. Just like me.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 2 (Every Spending Decision Is a Spiritual Decision). This is the exact core argument of that day in Ron\u2019s own voice.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Teaching: Get Rich Slow / The \\$83/Month Illustration  ")]),
  body("'If you don\u2019t spend $83 a month that you could spend — starting when you get out of college — and you put it away for a working life, you\u2019ve saved $40–50,000. But because of the laws of compounding, that could be worth hundreds of thousands, if not a million dollars. Or on the other side: I overspend by $83 a month. It doesn\u2019t cost me $40,000 over a working life — it costs me what it could have earned: $300,000 or $400,000. A little bit, over a long timeframe, works.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 16 (Time Value of Money). Clean, concrete, memorable.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Teaching: Living Within Your Income Is Unnatural  ")]),
  body("'We live in a society where we\u2019re taught to be discontent, and this next thing will do it. Living within my income is unnatural in this culture. Those principles are transcendent — they will provide financial freedom, confidence, contentment. But we have no reinforcement of that at all. Which is why, in a church, if we can get this as part of the church culture, we can get the reinforcement we need on a day-to-day basis. We need it.'"),
  bodyRuns([label("Best for: "), normal("MYM Day 9 (Spend Less Than You Earn) — frames why the principle is hard even when it\u2019s simple.")]),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("Quote: Tithing Is Training Wheels  ")]),
  body("'Tithing is just the beginning of giving. I think New Testament giving is 1 Corinthians 16:2 — give as God has prospered you. Tithing is a beginning point. I counsel people: don\u2019t give 10% — give 10.1%. Because if you give exactly 10%, you tend to think of that as God\u2019s money and the rest is mine. No, it\u2019s all his. I do the tithe in recognition of God\u2019s ownership. But if I\u2019m prospering, I should see my percentage going up.'"),
  bodyRuns([label("Best for: "), normal("GL Day 32 (Proportionate Giving) or Day 37 (Give First).")]),

  rule(),

  h3("Generous Living Transcripts"),
  shade([
    new Paragraph({ children: [new TextRun({ text: "Source file: ", bold: true, size: 21, font: "Arial" }), new TextRun({ text: "Generous_Living_-_all_transcripts.docx", size: 21, font: "Arial", italics: true })] }),
    new Paragraph({ spacing: { before: 60 }, children: [new TextRun({ text: "Note: This transcript is primarily production setup and roundtable warmup. The substantive Ron Blue teaching is in Session 2+ video content, not captured in full here.", bold: false, size: 21, font: "Arial", italics: true })] }),
  ], LIGHTBLUE),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  body("The usable content in this transcript is real-people testimonials from the roundtable participants — not Ron\u2019s formal teaching. These can supplement GL days with peer voices. Key moments:"),
  bullet("Nicole Ford: family became debt-free using biblical principles and now passes them to their children"),
  bullet("Jill Burnett: married 43 years, three sons, six grandchildren — wants to bless them with financial wisdom while still alive"),
  bullet("Doug Harder (school administrator): 'Most people don\u2019t think the Lord has anything to say about finances. But it applies to all of us — and it\u2019s a way to reach unchurched people.'"),
  body("These could open individual GL days as brief scene-setters before Ron\u2019s teaching, showing that this material resonates across income levels."),

  rule(),
  pageBreak()
];

// ─── PART 1B: STORY BANK ───────────────────────────────────────────────────

const part1b = [
  h2("B. Story Bank (RBI Advisor / Client Stories)"),
  body("These are stories from advisors and clients in the Ron Blue Institute network. They are organized by the devotional section where they serve best. Use these to add the 'everyday person' voice to days where Ron\u2019s own stories are less available."),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  h3("GOIA Days 1–7 — Best Story Bank Matches"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [2200, 2200, 2600, 2360],
    rows: [
      new TableRow({
        tableHeader: true,
        children: [
          ...[["Person", "2200"], ["Theme", "2200"], ["Summary", "2600"], ["Best Day", "2360"]].map(([t, w]) =>
            new TableCell({
              borders, width: { size: parseInt(w), type: WidthType.DXA },
              shading: { fill: BLUE, type: ShadingType.CLEAR },
              margins: { top: 80, bottom: 80, left: 100, right: 100 },
              children: [new Paragraph({ children: [new TextRun({ text: t, bold: true, size: 20, font: "Arial", color: "FFFFFF" })] })]
            })
          )
        ]
      }),
      ...[
        ["Jim Underwood", "Fear vs. Freedom", "Fear keeps people from surrendering money to God; freedom comes from alignment with Him", "Day 1 or 5"],
        ["Brandon Stoller", "Letting Go of Control", "Starting a family + major transition; learns to surrender control", "Day 2 (Second Chair)"],
        ["Andrea Hall", "Clarity Through Ownership", "Single mom; 'God owns it all' reshapes her identity and direction", "Day 1 or 4 (Owned and Loved)"],
        ["Audra Ames", "Trust Through Loss", "Lost husband in accident; grief deepens trust and becomes ministry", "Day 4 or 6 (Anxiety)"],
        ["Emmett Mankin", "Faith Redefines Work", "Late-in-life conversion; career reframed as ministry and stewardship", "Day 7 (New Default)"],
        ["Samuel Richmond", "Money as Faith", "Financial decisions as acts of faith aligned with God\u2019s purpose", "Day 5 (Real Test)"],
        ["Generic: Business Failure \u2192 Trust", "Failure, surrender", "Business loss leads to deeper trust in God as owner", "Day 6 (Anxiety / Ownership)"],
      ].map(([name, theme, summary, day]) =>
        new TableRow({
          children: [
            ...[name, theme, summary, day].map((text, i) => {
              const ws = [2200, 2200, 2600, 2360];
              return new TableCell({
                borders, width: { size: ws[i], type: WidthType.DXA },
                margins: { top: 60, bottom: 60, left: 100, right: 100 },
                children: [new Paragraph({ children: [new TextRun({ text, size: 20, font: "Arial" })] })]
              });
            })
          ]
        })
      )
    ]
  }),
  new Paragraph({ spacing: { before: 120 }, children: [] }),

  h3("MYM Days 1–7 — Best Story Bank Matches"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [2200, 2200, 2600, 2360],
    rows: [
      new TableRow({
        tableHeader: true,
        children: [
          ...[["Person", "2200"], ["Theme", "2200"], ["Summary", "2600"], ["Best Day", "2360"]].map(([t, w]) =>
            new TableCell({
              borders, width: { size: parseInt(w), type: WidthType.DXA },
              shading: { fill: BLUE, type: ShadingType.CLEAR },
              margins: { top: 80, bottom: 80, left: 100, right: 100 },
              children: [new Paragraph({ children: [new TextRun({ text: t, bold: true, size: 20, font: "Arial", color: "FFFFFF" })] })]
            })
          )
        ]
      }),
      ...[
        ["Greg & Joanne Gunter", "Marriage & Money", "Debt vs. saver tension in marriage leads to alignment and stewardship", "MYM Day 7 (Daily Surrender) or Day 19"],
        ["Mark & Adam Wilson", "Training Next Generation", "Father-son team models stewardship via 10/10/80 family system", "MYM Day 5 (Faith Requires Action)"],
        ["Keith Moore", "Money & Discipleship", "Money is central to discipleship, not separate from it", "MYM Day 1 or 2"],
        ["Brendan Hawks", "Redefining Success", "Success is alignment with God, not returns", "MYM Day 3 (Growth Process)"],
        ["Generic: Debt to Freedom", "Discipline, freedom", "Journey from consumer debt to margin and generosity", "MYM Day 4 (Faithfulness First)"],
      ].map(([name, theme, summary, day]) =>
        new TableRow({
          children: [
            ...[name, theme, summary, day].map((text, i) => {
              const ws = [2200, 2200, 2600, 2360];
              return new TableCell({
                borders, width: { size: ws[i], type: WidthType.DXA },
                margins: { top: 60, bottom: 60, left: 100, right: 100 },
                children: [new Paragraph({ children: [new TextRun({ text, size: 20, font: "Arial" })] })]
              });
            })
          ]
        })
      )
    ]
  }),
  new Paragraph({ spacing: { before: 120 }, children: [] }),

  h3("GL Days 1–7 — Best Story Bank Matches"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [2200, 2200, 2600, 2360],
    rows: [
      new TableRow({
        tableHeader: true,
        children: [
          ...[["Person", "2200"], ["Theme", "2200"], ["Summary", "2600"], ["Best Day", "2360"]].map(([t, w]) =>
            new TableCell({
              borders, width: { size: parseInt(w), type: WidthType.DXA },
              shading: { fill: BLUE, type: ShadingType.CLEAR },
              margins: { top: 80, bottom: 80, left: 100, right: 100 },
              children: [new Paragraph({ children: [new TextRun({ text: t, bold: true, size: 20, font: "Arial", color: "FFFFFF" })] })]
            })
          )
        ]
      }),
      ...[
        ["Bob Lotich", "Radical Generosity", "Increased giving from 11% to 31%; saw unexpected provision", "GL Day 1 (God Is the First Giver) or Day 3"],
        ["Brent & Peg Dunn", "Giving in Hardship", "Continued tithing through unemployment; shaped family legacy", "GL Day 2 (Open Hands) or Day 3"],
        ["Chuck Simmons", "From Saving to Giving", "Realized he had \u2018enough\u2019 and shifted from accumulation to generosity", "GL Day 5 (Joy Returns) or Day 6"],
        ["Ken O\u2019Leary", "Redefining \u2018Enough\u2019", "Advisor stories: widow and heiress learning open-handed living", "GL Day 4 (Cheerful, Not Pressured)"],
        ["Generic: Fearful Giving \u2192 Breakthrough", "Fear, generosity", "Overcomes fear of giving less; discovers generosity multiplies", "GL Day 2 or 3"],
      ].map(([name, theme, summary, day]) =>
        new TableRow({
          children: [
            ...[name, theme, summary, day].map((text, i) => {
              const ws = [2200, 2200, 2600, 2360];
              return new TableCell({
                borders, width: { size: ws[i], type: WidthType.DXA },
                margins: { top: 60, bottom: 60, left: 100, right: 100 },
                children: [new Paragraph({ children: [new TextRun({ text, size: 20, font: "Arial" })] })]
              });
            })
          ]
        })
      )
    ]
  }),
  new Paragraph({ spacing: { before: 120 }, children: [] }),
  rule(),
  pageBreak()
];

// ─── PART 2: DAY-BY-DAY MAP ────────────────────────────────────────────────

function dayEntry(dayLabel, title, subtitle, primaryStory, supportingMaterial, writingNote, editorNote) {
  const rows = [
    shade([
      new Paragraph({ children: [new TextRun({ text: dayLabel + " — " + title, bold: true, size: 24, font: "Arial", color: BLUE })] }),
      new Paragraph({ children: [new TextRun({ text: subtitle, italics: true, size: 21, font: "Arial", color: "555555" })] }),
    ], LIGHTBLUE),
    new Paragraph({ spacing: { before: 80 }, children: [] }),
    bodyRuns([label("\uD83D\uDCCC Primary Story: "), normal(primaryStory)]),
    new Paragraph({ spacing: { before: 60 }, children: [] }),
    bodyRuns([label("\uD83D\uDCDA Supporting Material: "), normal(supportingMaterial)]),
    new Paragraph({ spacing: { before: 60 }, children: [] }),
    bodyRuns([label("\u270F\uFE0F Writing Note: "), italic(writingNote)]),
  ];
  if (editorNote) {
    rows.push(new Paragraph({ spacing: { before: 60 }, children: [] }));
    rows.push(bodyRuns([label("\uD83D\uDED1 Editor Flag to Resolve: "), italic(editorNote)]));
  }
  rows.push(rule());
  return rows;
}

const part2 = [
  h1("PART 2 — Day-by-Day Story Map (Days 1–7, All Three Books)"),

  h2("GOIA Days 1–7"),

  ...dayEntry(
    "GOIA Day 1", "The Foundation",
    "God Owns It All — And That Changes the Story",
    "Teaching: The Three Questions (GOIA Session 1, ~11:51). The world asks 'Will I ever have enough?' Scripture asks 'Who owns it?' Ron: 'If God owns it, that changes everything about the way I view money and possessions.' Use this as the opening movement of the day — the shift from the wrong question to the right one.",
    "The Kenya Pastor story (Session 1, ~1:14) can work as an optional opening vignette to show materialism isn't cultural — it's the heart. Story Bank: Jim Underwood (fear vs. freedom) adds a contemporary voice. Session 1 Tool/Test/Testimony teaching (~15:14) supports the 'why ownership matters' section.",
    "The current Day 1 opens with abstract 'many questions' language. Replace the first two paragraphs with Ron asking the three wrong questions the world asks — give the reader a mirror — then introduce the three right ones. The 'I must...' affirmations throughout need to be removed or converted to second-person invitations.",
    "Editor: 'Explain the first-person affirmations — why are we suddenly inserting an I statement?' Answer: convert them all to second-person or cut. The structure is sound; the register needs repair."
  ),

  ...dayEntry(
    "GOIA Day 2", "The Second Chair",
    "Surrendering Control",
    "The editor's dinner-party anecdote (already incorporated in the draft) is the right opening image. Strengthen what follows with: Teaching on responsibility vs. control from GOIA Session 1 — 'Responsibility says I'll do what's mine to do. Control says I need to make sure nothing goes wrong.' Story Bank: Brandon Stoller (Letting Go of Control) gives a contemporary peer-level voice for the middle section.",
    "Session 1 Tool/Test/Testimony on contentment supports the closing. The editor-supplied boss-at-dinner anecdote should stay — it was flagged positively by the editor.",
    "The paragraph 'It never belonged to your bank account' is flagged as illogical by the editor — fix to 'It never belonged to your circumstances, your plans, or your outcomes.' The second 'I must define faithful' sentence repeats from three paragraphs earlier — cut the duplicate (editor caught this). The exercises in Day 2 repeat the same grip question as Day 1 — advance the exercise to: what does control look like in your actual spending or planning decisions this week?",
    "Editor: 'Not this but that formula followed by triplet repetition — feels very AI.' Specifically the paragraph beginning 'Control rarely walks into your life wearing a villain costume.' The content is good; the formula needs to be broken."
  ),

  ...dayEntry(
    "GOIA Day 3", "Your Name on the Label",
    "Why 'Mine' Is the Most Dangerous Word",
    "The Kenya Pastor story (GOIA Session 1, ~1:14) is the natural opener: Ron sees materialism in a Kenyan mud hut and realizes it isn't American — it's the heart. Two sentences from Ron's mouth, then the transition: 'If the problem is the heart, then the word "mine" is where it lives.' The Dr. Bill Bright story (~1:14, Session 3) can close the section on identity drift: if you look like you can give a million, you probably can't.",
    "Session 3 Steinbeck letter (~23:48) supports the cultural framing of 'mine becoming me.' Story Bank: Andrea Hall (single mom, 'God owns it all' reshapes identity) is a strong second voice for the middle section.",
    "The 'Mine becomes Me' section is genuinely the strongest part of this day — the editor noted it. Don't dilute it. The exercise repeats the Day 1 and Day 2 grip question for the third time (editor caught this). Replace with: ask the reader to identify something they would lose identity over if it disappeared — their career, a savings number, a lifestyle benchmark — and trace that back to the ownership question.",
    "Editor: 'All three exercises are synonymous — the study feels like it is not covering new ground.' This is the most critical structural fix for the first week."
  ),

  ...dayEntry(
    "GOIA Day 4", "Owned and Loved",
    "God's Ownership Is Personal, Not Corporate",
    "The Physician with Holes in His Shoes (GOIA Session 3, ~3:14). This is the day's story. The physician who capped his lifestyle at med-school level and had to learn to receive in order to give — the shoe salesman, the plane tickets from his in-laws — illustrates stewardship as response to love, not performance for approval. Open with: a doctor sitting with his legs crossed, a patient notices the holes in his shoes. From there the story teaches itself.",
    "Session 3 Contentment teaching (no regrets/no envy/no fear, ~12:39) supports the closing. Story Bank: Audra Ames (trust through loss) adds a different dimension of 'owned and loved' — when the Owner takes something away, trust deepens.",
    "This is already the strongest day structurally (editor noted it). The main fix: remove the superscript '20' left visible in the NIV quotation of 1 Corinthians 6:19–20. The subheads (Rescue / Belonging / Protection) are working and should stay.",
    "Editor: 'Did you mean to leave the verse number in?' — visible superscript 20 in the 1 Cor quotation. Fix in final layout."
  ),

  ...dayEntry(
    "GOIA Day 5", "The Real Test",
    "Money Reveals Who You Trust",
    "The Heart Surgeon / Million-Dollar Home story (GOIA Session 1, ~12:49 — also MYM transcripts). The surgeon asks the wrong question ('Is it okay for a Christian to live in a million-dollar home?') and Ron turns it back: 'What do you think God wants you to do?' That question — not the answer — is the point of this day. The real test isn't your theology; it's your reflex.",
    "Session 1 'checkbook reveals your goals, values, and priorities' teaching (~8:00). Story Bank: Samuel Richmond (financial decisions as acts of faith) adds a contemporary peer voice. Story Bank: Generic 'Fearful Giving → Breakthrough' can close the day's action section.",
    "The day is well-structured. The potential borrowed phrase about money testifying (editor flagged a YouTube pastor using similar language) should either be attributed or reworded — don't use it as written. The closing 'generosity reorders the heart' section is strong and should stay.",
    "Editor: 'Money can't speak but it testifies — found a pastor who said something similar on YouTube.' Reword to something more original: 'Money has no voice but it has a record.'"
  ),

  ...dayEntry(
    "GOIA Day 6", "Anxiety and Ownership",
    "Worry Is Often a Control Issue",
    "The $10,000 Line of Credit (GOIA Session 5, ~4:49). This is a story about Ron canceling his security net — literally — and God providing not just what he gave up but in a way he couldn't have engineered. Open with: Ron at the bank arranging the line of credit. Then the conviction. Then the canceled check. Then the Coca-Cola call. The story physically enacts 'seek first' — he stopped trying to secure tomorrow and God moved.",
    "Session 3 Contentment teaching (no regrets/no envy/no fear) supports the 'seek first' closing. Story Bank: Generic 'Business Failure → Trust' adds a contemporary parallel for readers who have faced financial loss.",
    "This is the best-written of the seven GOIA days — most conversational, least cluttered with 'I must' statements. The distinction between 'rehearsing' and 'preparing' is genuinely useful and should stay. The 'background music' metaphor (editor flagged it) should be replaced — change to 'background hum' or 'default frequency.'",
    "Editor: 'Not sure this metaphor works — background music is not a reflex.' Replace."
  ),

  ...dayEntry(
    "GOIA Day 7", "A New Default",
    "Live Like a Steward",
    "Two sources work together here. (1) Bloomington roundtable: 'Enough isn't a number — it's a person. It's a lesson. Paul says I learned to be content.' (2) Session 1 Tool/Test/Testimony: the world has a right to look at Christians and see they're different. Not better — different. They're content. This is what 'new default' produces as testimony. Open with the contrast: most people don't struggle because they don't know the right truths — they struggle because their default settings are strong. Then introduce stewardship as a daily posture through Ron's language.",
    "Bloomington: Two-client illustration (million-dollar home vs. trailer park CEO) shows two different 'defaults' — both faithful, both generous, both decided on their knees. Story Bank: Emmett Mankin (late-in-life conversion reframes entire career as stewardship) shows a new default replacing an old one.",
    "The steward vs. owner question pairs (editor liked this section) are excellent — 'How do I protect what's mine?' vs. 'How do I honor God with what's entrusted?' Keep these. The 'I actually like this paragraph' note from the editor refers to the Colossians 1:16–17 section — don't touch it.",
    "Editor: 'Weird phrasing' on the steward questions section needs a second pass — but the editor also liked the Colossians paragraph. Keep the good; tighten the transitions."
  ),

  rule(),
  h2("MYM Days 1–7"),

  ...dayEntry(
    "MYM Day 1", "The Ownership Transfer",
    "Peace Begins When 'Mine' Becomes 'His'",
    "Quote from MYM transcripts: 'The most fundamental decision a Christian can make is recognizing God's ownership. Once they make that decision, everything changes — they began seeing things in Scripture they didn't see before. Just like me.' Open with this quote, attributed directly. Then the Three Questions teaching (Session 1): the wrong questions the world asks vs. the right ones. Specifically: ownership answers the 'will I be okay?' question before you even ask it.",
    "Story Bank: Keith Moore (money is central to discipleship) frames the theological stakes. Editor note on MYM Day 1: it is very similar to GOIA Day 3 — acknowledge this by entering at a different angle. GOIA Day 3 was about 'mine' as identity drift. MYM Day 1 should start with the practical pressure Ron's clients feel: 'If this is mine, then it's on me.' The distinction is between spiritual identity and practical burden.",
    "The current MYM Day 1 re-relitigates the same ownership argument from scratch. It should instead assume the reader has internalized GOIA and now enter at the application level: where does 'mine' still show up in your budget, your savings habit, your monthly decisions? The exercises should begin with a cash-flow or budget reflection rather than another abstract grip inventory.",
    "Editor: 'Very similar to Day 3 of GOIA.' The fix is to enter the material from the financial-application angle rather than re-teaching the theology."
  ),

  ...dayEntry(
    "MYM Day 2", "Every Spending Decision Is a Spiritual Decision",
    "Money Reveals What You Trust",
    "Quote from MYM transcripts: 'It's no more spiritual to give than it is to go on vacation. Every spending decision I make is a decision about using his resources.' This is the day's thesis in Ron's own voice. The day currently makes this argument abstractly — replace the opening with Ron's direct statement and build from there. Add: the checkbook illustration from Session 1 (~8:00): 'If you let me look at your checkbook and credit card statements, I could tell you your goals, values, and priorities.'",
    "Story Bank: Greg & Joanne Gunter (marriage and money) — their debt-vs.-saver tension illustrates two people making spending decisions from different default beliefs. Relevant because Day 2 is about what's under the decision.",
    "The day is solid. The main improvement is grounding the abstract argument in Ron's checkbook illustration and one of his client-level observations. Keep the 'decision behind the decision' framing — it's the clearest organizing idea in the MYM section.",
    null
  ),

  ...dayEntry(
    "MYM Day 3", "The Growth Process",
    "God Uses Money to Form You",
    "Bloomington: 'Enough isn't a number — it's a lesson. I've learned to be content. Contentment is taught by God and practiced by us.' This is the thesis of the day rephrased — God is forming you through the financial seasons you're in right now, including the stretching ones. Use this to open the day before moving into the Philippians/James teaching.",
    "Story Bank: Brendan Hawks (Redefining Success — success isn't returns but alignment with God) gives a contemporary voice for the mid-section. The Chick-fil-A $100 story (Session 4) can work here as an illustration of a formation moment — a moment where a reflex is retrained.",
    "The day needs a concrete opening story. Currently it starts abstractly. Recommend: open with the Bloomington quote, then a brief scene (one of Ron's clients who came in after a hard financial season and discovered what God was teaching them through it — the Merrill Lynch advisor who lost half his retirement but realized he hadn't done anything wrong works here).",
    null
  ),

  ...dayEntry(
    "MYM Day 4", "Faithfulness First",
    "God Measures the Heart, Not the Amount",
    "Session 4 Parable of the Talents teaching (~7:59): the master said the same thing to the one with five talents and the one with two. 'Well done, good and faithful servant. You were faithful over a few things.' Ron: 'He didn't say they gave it all away. He said they were faithful.' Use this as the opening teaching. Then add: the Weekly Tithe illustration (Session 4, ~13:51) — faithfulness looks like the exact 10%, week after week, $51.26 or $600.85. Not impressive. Just faithful.",
    "Story Bank: Generic 'Debt to Freedom' — faithfulness in small decisions over time producing the freedom to give. Story Bank: Mark & Adam Wilson (10/10/80 family system) is a practical example of systematic faithfulness.",
    "This day is currently one of the weaker ones for concrete illustration. The Talents teaching from Session 4 is the most natural fit and should anchor it.",
    null
  ),

  ...dayEntry(
    "MYM Day 5", "Faith Requires Action",
    "Obedience Is the First Financial Step",
    "The $10,000 Line of Credit story (Session 5, ~4:49) is the strongest illustration of faith requiring a specific, costly, visible action. Ron didn't just believe in principle — he canceled the check. Faith became visible in a ledger. Use this to anchor the day. The Coca-Cola punchline is the reward, but don't let it overshadow the obedience moment — that's what teaches.",
    "Story Bank: Bob Lotich (increased giving from 11% to 31% — trusting God and seeing unexpected provision) parallels the structure of Ron's line-of-credit story for the generosity angle.",
    "The day needs an anchor story at the top. The line-of-credit story is available and perfectly matched. Currently the day runs abstract for too long before the exercises.",
    null
  ),

  ...dayEntry(
    "MYM Day 6", "The 'Will I Be Okay?' Question",
    "God's Provision Answers Our Fears",
    "Session 1 (~9:00): Ron names the three questions the world is really asking — 'Will I ever have enough? And if I do, will it continue to be enough? How much is enough?' Then: 'They're really asking: What will it take for me to be successful, significant, or secure?' These are the questions under the question. Open with this, then show why God's ownership answers them — not by guaranteeing income, but by relocating the source of security.",
    "Session 3 Contentment teaching: no regrets, no envy, no fear (~12:39). Story Bank: Audra Ames (trust through loss — she had no financial security and God provided) is the human-level counterweight to Ron's financial-advisor framing.",
    "The day currently circles around the 'Will I be okay?' question without grounding it in a story. Ron's direct articulation of those three questions from Session 1 is more honest and more specific than the current abstract treatment. Start with the question, not the answer.",
    null
  ),

  ...dayEntry(
    "MYM Day 7", "A Daily Surrender",
    "Living Like a Steward Before You Feel Ready",
    "Bloomington: 'I've lived long enough that I've lived in almost every stage of life.' Ron has been in the green trailer and in the surplus; he's earned the right to say surrender works across seasons. Use the brief two-client comparison (trailer park CEO vs. million-dollar home physician) to close — not as a lifestyle lesson but as a surrender one: both of them had decided, on their knees, what enough looked like.",
    "Story Bank: Greg & Joanne Gunter (marriage and money alignment — they surrendered control of their finances together) gives a younger-generation peer voice. The Weekly Tithe illustration from Session 4 grounds 'daily surrender' in a specific, repeatable practice.",
    "The day needs a brief opening story. The green trailer (Session 3, ~6:52) — 'when you don't have choices, life is relatively simple' — is a good opening contrast before the paradox of prosperity section that currently runs too long. Keep the daily reset structure in the exercises — it's one of the more original elements in the MYM section.",
    null
  ),

  rule(),
  h2("GL Days 1–7"),

  ...dayEntry(
    "GL Day 1", "God Is the First Giver",
    "Generosity Starts in the Gospel",
    "Session 4 (~1:09): 'There is not a shortage of money for kingdom purposes. There is a shortage of obedience. When we talk about stewardship and generosity, there can be shame and guilt associated with it. I don't want this to dwell on shame — I want to focus on the positive nature of giving.' This is the tone-setter for the entire GL section. Ron's explicit rejection of shame-based giving should open Day 1.",
    "Story Bank: Bob Lotich (11% to 31% — saw unexpected provision) gives an opening story of what cheerful, obedient giving looks like in practice. The 2 Corinthians 8:9 quote Ron uses when signing books: 'Though he was rich, yet for your sake he became poor.' This is his own touchstone verse for generosity.",
    "The GL section currently lacks a strong personal opening story. Ron's own statement about shame-based giving vs. heart transformation is the right frame. Start there, then move into the gospel foundation.",
    null
  ),

  ...dayEntry(
    "GL Day 2", "Open Hands, Open Heart",
    "Why Giving Breaks Money's Power",
    "Session 4 (~5:06): 'Giving breaks the power of money. When I open my fist and give, I am breaking the power of money — and I don't want money controlling my life.' Then the Matthew 6 teaching on two masters: 'Am I a slave to money, or am I a slave to God? If I'm a slave to money, I use people. If I'm a slave to God, I use money to free up people.'",
    "Story Bank: Brent & Peg Dunn (gave through unemployment — faithfulness when giving was costly). Story Bank: Generic 'Fearful Giving → Breakthrough' gives the emotional arc of opening closed hands.",
    "The current GL Day 2 is solid theologically. The main addition is grounding the 'open fist' image in Ron's actual teaching from Session 4 — he physically demonstrated it in the video. The writing should reference this as a tangible image, not just a metaphor.",
    null
  ),

  ...dayEntry(
    "GL Day 3", "Cheerful, Not Pressured",
    "The Kind of Giving God Forms",
    "The $10,000 Vacation Pledge (Session 4, ~20:25). This is the primary story for this day — and it may be the most important story in the entire 40-day series for GL. Ron and Judy gave cheerfully (they wrote the check freely), not under compulsion (they had a choice — they could have taken the vacation), and God responded with abundance beyond imagination. The story is long enough to anchor the day on its own. Let it breathe.",
    "The 2 Corinthians 8:9 passage Ron was reading when he made the decision connects directly to the day's Scripture. Session 4 (~11:54): 'I can never outgive God.' Story Bank: Bob Lotich (radical giving) as a contemporary parallel.",
    "Don't compress this story. It is the devotional illustration that the GL section has been missing — a real, named, costly, joyful act with a specific punchline that doesn't feel transactional. The writing team should give it a full opening paragraph before the theological section.",
    null
  ),

  ...dayEntry(
    "GL Day 4", "Proportionate Giving",
    "Consistency Beats Emotion",
    "Session 4 (~13:51): Ron and Judy's weekly tithe practice. Every week, a check for exactly 10% of income received — $51.26 or $600.85. Not legalistic: 'Out of conviction that on the first day of the week we want to recognize what God provided.' Then: 'Tithing is just the training wheels. It's the beginning. If I'm prospering, my percentage should go up.' The illustration makes proportionate giving concrete and personal.",
    "MYM transcript quote: 'Give ten-point-one percent, not ten — because if you give exactly 10%, you tend to think of that as God's money and the rest is yours. No, it's all his.' Story Bank: Chuck Simmons (realized he had enough and shifted from accumulation) for the 'more than a tithe' angle.",
    "The day needs Ron's personal practice to anchor it. It currently reads abstractly. The weekly tithe illustration is available, specific, and shows proportionate giving as a habit, not a doctrine.",
    null
  ),

  ...dayEntry(
    "GL Day 5", "Spontaneous Generosity",
    "Ready to Meet Needs When God Prompts",
    "The Chick-fil-A $100 (Session 4, ~25:17 / MYM transcripts). This is the definitive spontaneous generosity story. Open with: a man walking out of a fast food restaurant, wallet in hand. The convicting nudge. The five twenties. The woman's response a week later. Her daughter giving it away the same evening. The chain of generosity. Ron's conclusion: 'I gave out of my abundance. She gave out of her poverty. And giving generously has nothing to do with income.'",
    "Session 4 (~15:41): Ron at the parking garage, handing a $20 to the attendant in the cold. 'This is a gift from the Lord Jesus Christ. I'm just his ambassador.' Then: the 7-year-old daughter who told him the money paid their water bill. Session 4 Grandchildren $100 assignment also belongs in this general zone.",
    "This is the day where the story IS the devotional. Let the Chick-fil-A story open the day with no preamble, and let the theology flow from it. Currently the day starts abstractly. Flip the order.",
    null
  ),

  ...dayEntry(
    "GL Day 6", "Whole-Life Generosity",
    "Money, Time, Talent, Influence",
    "Session 4 Grandchildren giving assignment (~17:34): the $100 each Thanksgiving, the three boys in Austin buying supplies for homeless people and watching one homeless man share his bag with another. This story is about whole-life generosity modeled across generations — time, money, presence — not just a check. It redefines 'generous' as a way of living.",
    "Story Bank: Darren Key (redirects financial systems toward ministry impact). Story Bank: Jackie Garrett & James Reed (children learn stewardship through example, not instruction) reinforces the modeling theme.",
    "The current GL Day 6 lists the categories of generosity but doesn't show them. The Austin grandsons story shows all four: money (the $100), time (going out together), talent (planning and executing), influence (modeling for the next generation). Use it to embody the entire teaching.",
    null
  ),

  ...dayEntry(
    "GL Day 7", "Joy Returns",
    "The Surprise Fruit of a Generous Life",
    "Session 4 conclusion (~25:17 and ~28:00): 'Giving is for my benefit. Not God's benefit. It's to free me up financially and break the power of money — and give me a joy I couldn't experience any other way.' Then Ron's personal statement: 'Every time I give, I experience joy. I can never outgive God.' The parking garage $20 story — the 7-year-old daughter who said the money paid their water bill — is the clearest illustration of joy returning unexpectedly.",
    "Story Bank: Chuck Simmons (joy after the shift from accumulation to generosity). Session 3 Contentment teaching as closing frame: 'No regrets, no envy, no fear — that's the end result of a generous life.'",
    "The day should feel like the completion of a week-long arc: the reader has been invited into open hands, spontaneous giving, proportionate practice. Day 7 is the payoff — joy, not as a reward mechanism, but as the natural fruit of alignment. Keep the arc moving forward rather than restating the principles.",
    null
  ),

  rule(),
  pageBreak()
];

// ─── PART 3: GAP ANALYSIS ─────────────────────────────────────────────────

const part3 = [
  h1("PART 3 — Gap Analysis: What Is Still Missing"),

  h2("Stories Not Yet Found in Any Source"),

  shade([
    new Paragraph({ children: [new TextRun({ text: "These stories appear in the books but are NOT in any transcript uploaded so far. They need to be located or recreated.", bold: true, size: 22, font: "Arial", color: "C00000" })] }),
  ], "FFE0E0"),
  new Paragraph({ spacing: { before: 80 }, children: [] }),

  bodyRuns([label("1. The Ruby Story (Generous Living book)  ")]),
  body("Ruby is a woman whose husband's business hasn't paid bills in years. Ron asks her about giving. She says something like 'Go for it.' This story illustrates giving from a position of scarcity — not abundance. It is the most emotionally powerful giving story in the GL book and does not appear in any transcript. If a recorded version exists, it belongs in GL Day 2 or Day 3."),
  new Paragraph({ spacing: { before: 60 }, children: [] }),

  bodyRuns([label("2. Frank and Shirley (Generous Living book)  ")]),
  body("A couple who went through bankruptcy. Their story appears to illustrate surrender and trust after financial failure. Not in any transcript. Best use: GOIA Day 6 (Anxiety and Ownership) or as a 'Business Failure → Trust' arc for MYM."),
  new Paragraph({ spacing: { before: 60 }, children: [] }),

  bodyRuns([label("3. Ron's Personal Generosity Journey Before Success  ")]),
  body("The transcripts show Ron's client stories extensively but contain only one personal giving story (the $10,000 pledge). Is there a recorded account of Ron and Judy's early giving habits when money was tight — pre-financial planning firm, pre-success? This would be the most powerful story for GL Day 2 (Open Hands)."),

  rule(),
  h2("Structural Issues Flagged by the Editor — Action Items"),

  new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [1800, 3600, 3960],
    rows: [
      new TableRow({
        tableHeader: true,
        children: [
          ...[["Day(s)", "1800"], ["Issue", "3600"], ["Fix", "3960"]].map(([t, w]) =>
            new TableCell({
              borders, width: { size: parseInt(w), type: WidthType.DXA },
              shading: { fill: BLUE, type: ShadingType.CLEAR },
              margins: { top: 80, bottom: 80, left: 100, right: 100 },
              children: [new Paragraph({ children: [new TextRun({ text: t, bold: true, size: 20, font: "Arial", color: "FFFFFF" })] })]
            })
          )
        ]
      }),
      ...[
        ["All 7 GOIA days", "Bold 'I must...' first-person affirmations interrupt the second-person register with no explanation", "Remove all or convert to second-person invitations. Keep the content; change the voice."],
        ["Days 1, 2, 3 (GOIA)", "Exercises repeat the same 'grip' question three times", "Day 1: Identify the area. Day 2: How does that grip show up in a spending or planning decision? Day 3: What would you lose identity over if it disappeared?"],
        ["GOIA Day 2", "'It never belonged to your bank account' — illogical (the bank account doesn't sit in the chair)", "Change to: 'It never belonged to your circumstances, your plans, or your ability to guarantee outcomes.'"],
        ["GOIA Day 2", "Duplicate 'I must define faithful' sentence appears twice", "Delete the second instance (three paragraphs after the first)."],
        ["GOIA Day 4", "Superscript verse number '20' left visible in NIV quote", "Remove in final layout pass."],
        ["GOIA Day 5", "Money 'testifies' — possible uncredited borrowing from a pastor's talk", "Rephrase: 'Money has no voice but it has a record.'"],
        ["GOIA Day 6", "'Background music' metaphor for reflexes", "Change to: 'background hum' or 'default frequency.'"],
        ["GOIA Day 7", "Odd phrasing in steward vs. owner questions section", "Light edit — the Colossians paragraph that follows it is strong; don't touch that."],
        ["MYM Day 1", "Nearly identical to GOIA Day 3 — re-teaches the same ownership theology", "Enter at the application level: where does 'mine' show up in your actual budget or savings behavior?"],
        ["GOIA + MYM", "Placeholder URLs and QR codes still showing", "All placeholder.url/goia/day-N links and '[PLACE QR CODE IMAGE HERE]' need to be replaced before delivery."],
      ].map(([day, issue, fix]) =>
        new TableRow({
          children: [
            ...[day, issue, fix].map((text, i) => {
              const ws = [1800, 3600, 3960];
              return new TableCell({
                borders, width: { size: ws[i], type: WidthType.DXA },
                margins: { top: 60, bottom: 60, left: 100, right: 100 },
                children: [new Paragraph({ children: [new TextRun({ text, size: 20, font: "Arial" })] })]
              });
            })
          ]
        })
      )
    ]
  }),
  new Paragraph({ spacing: { before: 160 }, children: [] }),

  rule(),
  h2("Sources Still Needed"),
  body("To complete the devotional at the quality level these materials deserve, the following would help:"),
  bullet("Generous Living video transcripts (Sessions 1–6 equivalent) — the uploaded GL transcript was primarily production setup, not Ron teaching"),
  bullet("Any transcript or recording of Ron telling the Ruby story or Frank and Shirley story"),
  bullet("The client interview transcripts referenced in the project files (Wilson Wealth, Randy Brunson, Jeff Chenery advisors) — if these exist as audio/text, they could feed the story bank with more depth than the one-paragraph summaries"),
  bullet("Full story bank narratives — the current story bank PDF has one-paragraph summaries; full interview transcripts for Jim Underwood, Brandon Stoller, Andrea Hall, Bob Lotich, and the Dunns would allow actual quotes and specific details to be woven in"),
  new Paragraph({ spacing: { before: 80 }, children: [] }),
  body("What you have right now is more than enough to transform Days 1–7 significantly. The Kenya pastor, the green trailer, the physician with holes in his shoes, the $10,000 pledge, and the Chick-fil-A chain are each strong enough to anchor a day on their own. The structural fixes are line-level — no day needs to be rewritten from scratch. The voice fixes are the priority."),
];

// ─── BUILD DOCUMENT ───────────────────────────────────────────────────────

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: BLUE },
        paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: "2E75B6" },
        paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 1 } },
    ]
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      ...titlePage,
      ...howToUse,
      ...part1,
      ...part1b,
      ...part2,
      ...part3
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/40Day_Devotional_Source_Map.docx', buffer);
  console.log('Done');
});
