const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, LevelFormat, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageBreak, TableOfContents
} = require("docx");

const NAVY = "1B2A4A";
const GOLD = "C8941A";
const GREEN = "2D5A3D";

// ---------- helpers ----------
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const H3 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun(t)] });
const P = (t, opts = {}) => new Paragraph({
  spacing: { after: 140, line: 276 },
  children: [new TextRun({ text: t, italics: !!opts.italics, bold: !!opts.bold })]
});
const LABEL = (label, text) => new Paragraph({
  spacing: { after: 120, line: 276 },
  children: [
    new TextRun({ text: label + "  ", bold: true, color: NAVY }),
    new TextRun({ text: text })
  ]
});
const QUOTE = (t) => new Paragraph({
  spacing: { after: 140, line: 276 },
  indent: { left: 480 },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 12 } },
  children: [new TextRun({ text: t, italics: true })]
});
const bullet = (t) => new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  spacing: { after: 60, line: 276 },
  children: [new TextRun(t)]
});
const spacer = () => new Paragraph({ spacing: { after: 80 }, children: [new TextRun("")] });

// ---------- daily format ----------
function day(num, title, conviction, story, teaching, principle, reflection, team, wisdom, carry) {
  const out = [];
  out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(`Day ${num} — ${title}`)] }));
  out.push(LABEL("Today\u2019s Conviction.", conviction));
  out.push(new Paragraph({ spacing: { before: 80, after: 60 }, children: [new TextRun({ text: "A Story", bold: true, color: GREEN })] }));
  story.forEach(s => out.push(P(s)));
  out.push(new Paragraph({ spacing: { before: 80, after: 60 }, children: [new TextRun({ text: "The Why", bold: true, color: GREEN })] }));
  teaching.forEach(s => out.push(P(s)));
  out.push(QUOTE("Ron\u2019s principle: " + principle));
  out.push(LABEL("Leadership Reflection.", reflection));
  out.push(LABEL("Team Conversation.", team));
  out.push(LABEL("The Wisdom Question.", wisdom));
  out.push(new Paragraph({ spacing: { after: 220 }, children: [new TextRun({ text: "Carry It Forward:  ", bold: true, color: GOLD }), new TextRun({ text: carry, italics: true })] }));
  return out;
}

// ---------- outline rows ----------
function outlineDay(num, title, idea) {
  return new Paragraph({
    spacing: { after: 90, line: 264 },
    children: [
      new TextRun({ text: `Day ${num} — ${title}. `, bold: true }),
      new TextRun({ text: idea })
    ]
  });
}

const children = [];

// ===== TITLE PAGE =====
children.push(new Paragraph({ spacing: { before: 1600, after: 80 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "THIS CHANGES EVERYTHING", bold: true, size: 56, color: NAVY })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
  children: [new TextRun({ text: "30 Days of Financial Wisdom for Church Leaders", size: 32, color: GOLD })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 600 },
  children: [new TextRun({ text: "The Vision and the Why \u2014 First Base in the Financial Wisdom Pathway", size: 24, italics: true })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
  children: [new TextRun({ text: "A leadership journey for senior pastors, executive pastors, elders,", size: 22 })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 600 },
  children: [new TextRun({ text: "staff, and ministry leaders", size: 22 })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
  children: [new TextRun({ text: "Built on Ron Blue\u2019s philosophy and the 5 H\u2019s \u2014 Ron\u2019s Five Purposes", size: 20, italics: true, color: GREEN })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
  children: [new TextRun({ text: "FIRST DRAFT FOR REVIEW \u2014 not a final manuscript", size: 18, italics: true, color: "888888" })] }));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ===== 1. POSITIONING =====
children.push(H1("1. Product Positioning Statement"));
children.push(P("This Changes Everything: 30 Days of Financial Wisdom for Church Leaders is the vision-and-conviction resource \u2014 First Base \u2014 in the Ron Blue Institute church engagement pathway. Before a church can build a financial wisdom culture or launch a campaign, its leadership must first be gripped by why biblical financial wisdom belongs at the very center of discipleship."));
children.push(P("This 30-day leadership journey equips senior pastors, executive pastors, elders, staff, and ministry leaders with the theological vision, the Kingdom mission, and the shared conviction to lead their church into financial discipleship \u2014 not as a fundraising strategy, but as one of the most neglected and most transformational frontiers of whole-life discipleship."));
children.push(P("It is deliberately not a personal-finance course, not a marriage resource, not an implementation plan, and not a congregational campaign. It is the Why that makes all of those worth doing."));
children.push(spacer());
children.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "Where it sits in the pathway:", bold: true, color: NAVY })] }));
children.push(bullet("First Base \u2014 Wisdom (this resource): the WHY \u2014 vision and mission."));
children.push(bullet("Second Base \u2014 Culture: the HOW \u2014 leadership alignment and implementation."));
children.push(bullet("Third Base \u2014 Campaign (This Changes Everything: 40 Days): the CATALYST \u2014 the whole congregation."));
children.push(bullet("Home Plate \u2014 Financial Wisdom Ministry: the DESTINATION \u2014 the ongoing ministry."));
children.push(P("Pastor Advisor stands off the base path as a separate, personal resource and is not part of this sequence.", { italics: true }));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ===== 2. CORE PROMISE =====
children.push(H1("2. Core Promise"));
children.push(P("In 30 days, your leadership team will move from seeing money as a practical problem to seeing financial wisdom as a discipleship mission \u2014 and will share the conviction, vision, and language to lead your church toward a culture of stewardship, generosity, and Kingdom impact."));
children.push(new Paragraph({ spacing: { before: 80, after: 60 }, children: [new TextRun({ text: "By the end of the journey, your leaders will:", bold: true, color: NAVY })] }));
children.push(bullet("Understand why God owns it all \u2014 and why that single truth reshapes how we lead."));
children.push(bullet("See financial discipleship as whole-life discipleship, not a money program."));
children.push(bullet("Share a common biblical vocabulary rooted in Ron\u2019s 5 H\u2019s."));
children.push(bullet("Be convinced that discipling people financially is a pastoral mandate, not a fundraising tactic."));
children.push(bullet("Be ready \u2014 and eager \u2014 to step to Second Base and build the culture."));
children.push(spacer());
children.push(QUOTE("The deeper promise: a church whose leaders are gripped by this vision becomes a church marked by trust, wisdom, generosity, family legacy, and Kingdom impact."));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ===== 3. TABLE OF CONTENTS =====
children.push(H1("3. Table of Contents"));
children.push(P("Welcome: Why We Start at First Base"));
children.push(P("How to Use This Resource (a leadership-team journey)"));
children.push(P("The Four Bases: Where This Fits"));
children.push(P("The 5 H\u2019s: Ron\u2019s Five Purposes"));
children.push(spacer());
children.push(P("Week 1 \u2014 HONOR: God Owns It All (Days 1\u20136)", { bold: true }));
children.push(P("Week 2 \u2014 HEART: Money Reveals What We Trust (Days 7\u201312)", { bold: true }));
children.push(P("Week 3 \u2014 HABITS: Wisdom Becomes a Way of Life (Days 13\u201318)", { bold: true }));
children.push(P("Week 4 \u2014 HEALTH: Wisdom Brings Peace, Margin, and Freedom (Days 19\u201324)", { bold: true }));
children.push(P("Week 5 \u2014 HOPE: Living for What Lasts (Days 25\u201330)", { bold: true }));
children.push(spacer());
children.push(P("The Harvest: What This Will Produce"));
children.push(P("Where You Go Next: Stepping to Second Base (Culture)"));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ===== 4. 5 H MAPPING =====
children.push(H1("4. Ron\u2019s 5 H Framework Mapping"));
children.push(P("The 5 H\u2019s are Ron\u2019s Five Purposes \u2014 the backbone of financial wisdom. Five form the journey; Harvest is the outcome the journey produces, not a formation week."));

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const cell = (text, opts = {}) => new TableCell({
  borders,
  width: { size: opts.w, type: WidthType.DXA },
  shading: opts.head ? { fill: NAVY, type: ShadingType.CLEAR } : { fill: opts.fill || "FFFFFF", type: ShadingType.CLEAR },
  margins: { top: 80, bottom: 80, left: 120, right: 120 },
  children: [new Paragraph({ children: [new TextRun({ text, bold: !!opts.head || !!opts.bold, color: opts.head ? "FFFFFF" : (opts.color || "000000") })] })]
});
const cols = [1100, 1900, 3360, 3000];
const row = (a, b, c, d, opts = {}) => new TableRow({ children: [
  cell(a, { w: cols[0], head: opts.head, bold: opts.head ? false : true, color: opts.head ? null : NAVY }),
  cell(b, { w: cols[1], head: opts.head }),
  cell(c, { w: cols[2], head: opts.head }),
  cell(d, { w: cols[3], head: opts.head })
]});

children.push(new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: cols,
  rows: [
    row("H", "Ron\u2019s Purpose", "The Leadership Question", "What Changes", { head: true }),
    row("Honor", "God owns it all", "Do we lead as owners or as stewards?", "Our posture"),
    row("Heart", "Money reveals what we trust", "What is money forming in our people?", "Our discernment"),
    row("Habits", "Wisdom becomes practice", "Are we giving people a way to live wisely?", "Our discipleship"),
    row("Health", "Wisdom brings peace and margin", "Are our people free, or pressured?", "Our care"),
    row("Hope", "Eternal perspective on enough and legacy", "What future are we discipling people toward?", "Our vision"),
  ]
}));
children.push(spacer());
children.push(new Paragraph({ spacing: { after: 60 }, children: [
  new TextRun({ text: "Harvest (the outcome).  ", bold: true, color: GOLD }),
  new TextRun({ text: "Generosity, legacy, and Kingdom impact \u2014 the fruit the whole journey produces. It is named throughout and arrived at on Day 30, but it is the result of the five purposes rather than a sixth week of formation." })
]}));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ===== 5. COMPLETE 30-DAY OUTLINE =====
children.push(H1("5. Complete 30-Day Outline"));

children.push(H2("Week 1 \u2014 HONOR: God Owns It All"));
children.push(P("The foundation of all financial discipleship. Before leaders can build anything, they must settle the ownership question for themselves and for the church.", { italics: true }));
children.push(outlineDay(1, "The Owner of Everything", "Financial discipleship begins the moment leaders remember God owns it all \u2014 the church, the calling, the resources, the future."));
children.push(outlineDay(2, "Stewards, Not Owners", "The difference between owning ministry and stewarding it changes everything about how we lead."));
children.push(outlineDay(3, "Why the Church Has Been Silent", "Naming the fear that has kept leaders from discipling people financially is the first step to freedom."));
children.push(outlineDay(4, "Money Is a Discipleship Issue", "Jesus addressed money more than almost any subject; our discipleship cannot skip what He emphasized."));
children.push(outlineDay(5, "From Fundraising to Faith-Building", "The shift that frees leaders to teach about money without flinching."));
children.push(outlineDay(6, "The Vision of a Steward Church", "What a church looks like when honor \u2014 not institutional need \u2014 shapes its whole culture."));

children.push(H2("Week 2 \u2014 HEART: Money Reveals What We Trust"));
children.push(P("Money as a spiritual diagnostic. Why leaders must shepherd the heart, not merely manage behavior.", { italics: true }));
children.push(outlineDay(7, "The Heart Beneath the Budget", "Every financial decision is, at root, a spiritual decision."));
children.push(outlineDay(8, "What Money Competes With", "Jesus named money as a rival god; leaders must understand the contest for the heart."));
children.push(outlineDay(9, "Fear, Comparison, and Contentment", "The heart conditions money quietly exposes in our people \u2014 and in us."));
children.push(outlineDay(10, "Discipling Desire", "Forming what people love is more powerful than managing what people do."));
children.push(outlineDay(11, "The Generous Heart", "Generosity is the evidence of a transformed heart, not a fundraising goal."));
children.push(outlineDay(12, "Shepherding the Heart Around Money", "Leaders as physicians of the heart, not financial planners."));

children.push(H2("Week 3 \u2014 HABITS: Wisdom Becomes a Way of Life"));
children.push(P("The practical wisdom the church can actually give people \u2014 Ron\u2019s enduring principles, framed as discipleship for leaders to champion.", { italics: true }));
children.push(outlineDay(13, "Wisdom You Can Practice", "Biblical financial wisdom is livable and teachable, not abstract."));
children.push(outlineDay(14, "The Five Uses of Money", "Live, give, owe, grow \u2014 a simple framework every leader can teach and every person can use."));
children.push(outlineDay(15, "Ron\u2019s Enduring Principles", "Spend less than you earn, avoid debt, build margin, set long-term goals, give generously."));
children.push(outlineDay(16, "A Shared Language for the Whole Church", "Common vocabulary multiplies discipleship across every ministry and stage."));
children.push(outlineDay(17, "Wisdom for Every Decision", "\u201CWhat would wisdom do here?\u201D becomes a discipleship habit, not just a financial one."));
children.push(outlineDay(18, "Habits That Outlast a Sermon", "Formation requires rhythm, not just inspiration \u2014 which is why culture must follow conviction."));

children.push(H2("Week 4 \u2014 HEALTH: Wisdom Brings Peace, Margin, and Freedom"));
children.push(P("The fruit of wisdom in people\u2019s lives. Why a church that disciples financially produces healthier, freer, more available people.", { italics: true }));
children.push(outlineDay(19, "From Pressure to Peace", "Financial wisdom is whole-life health, not just better money management."));
children.push(outlineDay(20, "The People in Our Pews Are Struggling", "The hidden financial pain present in every congregation \u2014 and the silence around it."));
children.push(outlineDay(21, "Margin Makes Ministry Possible", "Free people serve more, give more, and follow more fully."));
children.push(outlineDay(22, "Serving Every Financial Stage", "From struggling to surplus, every person in the church needs discipleship, not just the giver."));
children.push(outlineDay(23, "Wisdom Before Wealth", "People need wisdom far more than they need more money; the church uniquely offers it."));
children.push(outlineDay(24, "A Healthier Church", "What changes across a whole body when financial health begins to spread."));

children.push(H2("Week 5 \u2014 HOPE: Living for What Lasts"));
children.push(P("Eternal perspective, contentment, and legacy \u2014 the vision that pulls everything forward into Kingdom impact.", { italics: true }));
children.push(outlineDay(25, "Redefining Success", "Wisdom reframes what we are actually aiming at as leaders and as a church."));
children.push(outlineDay(26, "How Much Is Enough?", "Contentment and finish lines are discipleship, not just financial planning."));
children.push(outlineDay(27, "Discipling for Legacy", "Multi-generational stewardship and the church\u2019s irreplaceable role in it."));
children.push(outlineDay(28, "The Kingdom Vision of Generosity", "Generosity as mission and overflow, not maintenance and obligation."));
children.push(outlineDay(29, "A Church That Changes Everything", "The vision of financial wisdom as a movement, not a program or a season."));
children.push(outlineDay(30, "From Why to How", "Commissioning leaders to carry the vision and step to Second Base \u2014 building the culture."));

children.push(spacer());
children.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "The Harvest \u2014 the outcome arrived at on Day 30 and beyond:", bold: true, color: GOLD })] }));
children.push(P("Generosity, legacy, and Kingdom impact \u2014 the fruit of a leadership team that now shares one vision, one language, and one conviction, ready to lead their church from Why to How."));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ===== 6. SAMPLE DAYS 1-5 =====
children.push(H1("6. Fully Written Sample \u2014 Days 1\u20135"));
children.push(P("These five days show the intended voice, depth, and daily format. The format repeats for all 30 days. Note: every day stays at the level of leadership vision and conviction \u2014 it does not drift into personal budgets, marriage, implementation, or congregational campaign material, which live in other resources.", { italics: true }));
children.push(spacer());

day(1, "The Owner of Everything",
  "Financial discipleship begins the moment a leader remembers that God owns it all \u2014 the church, the calling, the resources, and the future.",
  ["A pastor sits in his office on a Monday morning, looking at a giving report that is behind budget. His mind runs the familiar loop: the building, the staff, the programs, the shortfall. And somewhere in that loop a quiet lie takes root \u2014 that all of this depends on him. He has begun to carry what he was only ever asked to steward."],
  ["Ron Blue spent his life teaching one foundational truth: God owns it all. Not most of it. Not the religious portion of it. All of it. \u201CThe earth is the Lord\u2019s, and everything in it\u201D (Psalm 24:1). For a church leader, this is not an abstract doctrine. It is the ground on which all ministry stands.",
   "If God owns it all, then the church is not ours to fund, fix, or carry. It is His to build. Our role is not ownership but stewardship \u2014 and that single shift changes the emotional posture of leadership from pressure to peace, from anxiety to faithfulness.",
   "This is also why financial discipleship cannot be an afterthought in the church. If everything belongs to God, then how His people handle money becomes one of the clearest pictures of whether they actually trust Him. We cannot disciple people in everything except the one area Jesus addressed most."],
  "God owns it all. We are stewards, not owners. Stewardship is using God-given resources to accomplish God-given goals.",
  "Where am I carrying ownership pressure in ministry that God never asked me to carry?",
  "When our church talks about money, does it sound like we believe God owns it all \u2014 or like we are managing an institution\u2019s needs?",
  "If we truly led as stewards rather than owners, what would change first about how we lead?",
  "Honor begins not with a budget, but with surrender."
).forEach(p => children.push(p));

day(2, "Stewards, Not Owners",
  "The difference between owning ministry and stewarding it changes everything about how we lead.",
  ["Two pastors face the same budget gap. One asks, \u201CHow do I make this work?\u201D The other asks, \u201CLord, what have You entrusted to us, and how do we manage it faithfully?\u201D Same numbers. Two entirely different postures of the heart \u2014 and two entirely different kinds of leadership."],
  ["Ownership and stewardship ask different questions. Ownership asks: How do I protect, grow, and control what is mine? Stewardship asks: How do I faithfully manage what belongs to Another? The owner is driven by outcomes. The steward is freed by faithfulness.",
   "Ron often said the steward\u2019s only job is faithfulness \u2014 the results belong to God. For church leaders, this is liberating. A steward-leader does not have to manufacture generosity, manipulate giving, or carry the weight of every shortfall. A steward-leader teaches people to honor God and trusts God with the harvest.",
   "This is also why financial discipleship is so freeing to lead. We are not asking people to fund our vision; we are inviting them to steward God\u2019s resources for God\u2019s purposes. The pressure lifts, and the mission clarifies."],
  "Faithfulness, not success, is the measure of a steward.",
  "In my leadership, where do I act more like an owner than a steward?",
  "If we measured our financial leadership by faithfulness instead of by results, what would we do differently?",
  "What is one decision we are facing where the steward\u2019s question \u2014 \u201CWhat has God entrusted to us?\u201D \u2014 would lead us somewhere different than the owner\u2019s question?",
  "Owners carry pressure. Stewards carry assignments."
).forEach(p => children.push(p));

day(3, "Why the Church Has Been Silent",
  "Naming the fear that has kept leaders from discipling people financially is the first step to freedom.",
  ["At a pastors\u2019 gathering, the speaker asks, \u201CHow many of you have preached a full series on money in the last three years?\u201D A handful of hands go up. Then he asks, \u201CHow many of you felt fully equipped and unafraid to do it?\u201D Almost none."],
  ["There is a reason the church has often gone quiet about money. Pastors fear sounding transactional. They fear the prosperity-gospel association. They fear appearing self-serving when the offering is tied to the budget. So an entire domain of life \u2014 the one Jesus addressed more than heaven, hell, or prayer \u2014 quietly gets left out of discipleship.",
   "But silence has a cost. When the church says nothing, the culture says everything. Our people are being discipled about money every single day \u2014 by advertising, by anxiety, by comparison \u2014 just not by the church.",
   "Ron understood that the answer to the fear is not avoidance but wisdom. When we reframe money as a matter of biblical wisdom rather than fundraising, the fear loses its grip. We are not asking for money. We are forming disciples. That reframe is the doorway out of the silence."],
  "Money is not a taboo subject; it is a discipleship subject. Jesus made it one.",
  "What fear has most kept me from leading boldly in this area?",
  "What has our church\u2019s silence \u2014 or hesitation \u2014 about money taught our people by default?",
  "If fear were not a factor, how would we want to disciple our people about money?",
  "The opposite of fundraising is not silence. It is discipleship."
).forEach(p => children.push(p));

day(4, "Money Is a Discipleship Issue",
  "Jesus talked about money more than almost any other subject \u2014 our discipleship cannot skip what He emphasized.",
  ["A seminary graduate realizes he was trained to exegete every kind of parable except the ones about money \u2014 those he had always treated as illustrations about something else. Then he counts them. Nearly half of Jesus\u2019 parables touch money or possessions. He had been taught to preach around the very thing Jesus was aiming at."],
  ["Jesus spoke about money and possessions more than He spoke about prayer or faith. Sixteen of His thirty-eight parables deal with how we handle resources. This was not because money mattered to Jesus for its own sake \u2014 it was because money reveals and forms the heart. \u201CWhere your treasure is, there your heart will be also.\u201D",
   "Ron built his entire ministry on a simple conviction: you cannot disciple a whole person while ignoring the area Jesus addressed most. For leaders, this reframes everything. Financial discipleship is not a niche ministry or a stewardship season. It is whole-life discipleship.",
   "A church that disciples people in marriage, parenting, purity, and purpose \u2014 but not in money \u2014 has skipped the very arena Jesus used to test the heart. To leave it out is to leave a hole in the center of our people\u2019s formation."],
  "How we handle money is the truest external indicator of our internal spiritual condition.",
  "In my own teaching and leadership, have I treated money as a discipleship issue or merely as a practical one?",
  "What does it say about our discipleship that money is often the last thing we are willing to address directly?",
  "If we believed money discipleship was as essential as marriage or parenting discipleship, what would we start doing?",
  "You cannot disciple a heart while avoiding its treasure."
).forEach(p => children.push(p));

day(5, "From Fundraising to Faith-Building",
  "The shift from fundraising to faith-building frees leaders to teach about money without flinching.",
  ["A pastor dreads the annual stewardship sermon \u2014 the one everyone knows is really about the budget. Then a mentor asks him a question that changes everything: \u201CWhat if you never had to talk about the church\u2019s need again \u2014 and instead only ever talked about your people\u2019s growth?\u201D"],
  ["The deepest reframe in this entire journey is this: we are not raising money; we are building faith. A fundraising posture starts with the institution\u2019s need and asks people to meet it. A faith-building posture starts with the person\u2019s discipleship and trusts God to provide for the church as a byproduct.",
   "Ron taught that generosity is not the goal \u2014 it is the evidence. When people grow in trust, surrender, and wisdom, generosity follows naturally, the way fruit follows health. This is profoundly freeing for leaders. You are no longer the institution\u2019s collector. You are the people\u2019s shepherd.",
   "And here is the paradox Ron observed again and again: churches that stop fundraising and start discipling almost always become more generous, not less. When you aim at the heart, the harvest takes care of itself."],
  "Giving is a result, not a goal. Disciple the heart, and generosity follows.",
  "Do I think of myself more as a steward of the budget or a shepherd of people\u2019s hearts around money?",
  "How would our language change if we never spoke of money as a need to be met, only as a discipleship to be pursued?",
  "What is one place our church currently \u201Cfundraises\u201D that we could reframe as \u201Cfaith-building\u201D?",
  "Stop raising money. Start raising disciples. The generosity will come."
).forEach(p => children.push(p));

// closing reviewer note
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H1("Reviewer Notes \u2014 Open Questions for Brett"));
children.push(bullet("Daily format: 7 light elements (Conviction, Story, The Why, Ron\u2019s Principle, Leadership Reflection, Team Conversation, Wisdom Question) + a one-line Carry It Forward. Too heavy, too light, or right for leaders?"));
children.push(bullet("Structure: 5 H\u2019s \u00D7 6 days = 30, with Harvest as the outcome (not a sixth week). Confirm this is the intended math."));
children.push(bullet("\u201CTeam Conversation\u201D replaces the couple/spouse prompt so any role \u2014 single youth pastor, married elder, senior pastor \u2014 can engage. Confirm this is the right move per your note in the strategy session."));
children.push(bullet("Ron\u2019s voice: principles are paraphrased in his spirit. Final manuscript should pull verified Ron Blue quotes/citations where you want his exact words."));
children.push(bullet("Day 30 hands off to Second Base (Culture) but contains no implementation steps \u2014 confirm that boundary holds where you want it."));

// ===== DOCUMENT =====
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: GREEN },
        paragraph: { spacing: { before: 220, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 23, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 2 } },
    ]
  },
  numbering: { config: [
    { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 540, hanging: 280 } } } }] }
  ]},
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/home/claude/FirstBase_Draft.docx", buffer);
  console.log("written");
});
