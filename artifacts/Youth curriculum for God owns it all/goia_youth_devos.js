const {
  Document, Packer, Paragraph, TextRun, PageBreak,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, Table, TableRow, TableCell, UnderlineType
} = require('docx');
const fs = require('fs');

// ---- COLORS ----
const NAVY = "1B3A5C";
const GOLD = "C8922A";
const TEAL = "2A7B8C";
const LIGHT_BLUE = "E8F0F7";
const LIGHT_GOLD = "FDF3E3";
const LIGHT_TEAL = "E0F2F5";
const MID_GRAY = "6B7280";
const LIGHT_GRAY = "F3F4F6";
const WHITE = "FFFFFF";
const DARK = "1F2937";
const RED_SOFT = "FFF0F0";
const RED_BORDER = "C0392B";

// ---- HELPERS ----
const noBorder = { style: BorderStyle.NONE };
const thinBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };

function sp(before = 80, after = 80) { return { before, after }; }
function indent(left = 720) { return { left }; }

function body(text, opts = {}) {
  const { bold = false, italic = false, size = 22, color = DARK, before = 60, after = 60 } = opts;
  return new Paragraph({
    spacing: sp(before, after),
    children: [new TextRun({ text, bold, italics: italic, size, color, font: "Arial" })]
  });
}

function mixedBody(runs) {
  return new Paragraph({
    spacing: sp(60, 60),
    children: runs.map(r => new TextRun({ font: "Arial", size: 22, color: DARK, ...r }))
  });
}

function h1(text, color = NAVY) {
  return new Paragraph({
    spacing: sp(400, 80),
    children: [new TextRun({ text, bold: true, size: 52, color, font: "Arial" })]
  });
}

function h2(text) {
  return new Paragraph({
    spacing: sp(280, 80),
    children: [new TextRun({ text, bold: true, size: 32, color: NAVY, font: "Arial" })]
  });
}

function sectionLabel(text) {
  return new Paragraph({
    spacing: sp(240, 60),
    children: [new TextRun({ text: text.toUpperCase(), bold: true, size: 18, color: GOLD, font: "Arial" })]
  });
}

function italic(text) {
  return new Paragraph({
    spacing: sp(60, 60),
    children: [new TextRun({ text, italics: true, size: 22, color: MID_GRAY, font: "Arial" })]
  });
}

function pullQuote(text) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [160, 9200],
    borders: {
      top: noBorder, bottom: noBorder, left: noBorder, right: noBorder,
      insideH: noBorder, insideV: noBorder
    },
    rows: [new TableRow({ children: [
      new TableCell({
        width: { size: 160, type: WidthType.DXA },
        borders: { top: noBorder, bottom: noBorder, right: noBorder,
          left: { style: BorderStyle.SINGLE, size: 20, color: GOLD } },
        shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
        children: [new Paragraph({ children: [] })]
      }),
      new TableCell({
        width: { size: 9200, type: WidthType.DXA },
        borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
        shading: { fill: LIGHT_GOLD, type: ShadingType.CLEAR },
        margins: { top: 140, bottom: 140, left: 240, right: 240 },
        children: [new Paragraph({
          children: [new TextRun({ text, bold: true, italics: true, size: 24, color: NAVY, font: "Arial" })]
        })]
      })
    ]})]
  });
}

function callout(children, fill = LIGHT_BLUE, borderColor = NAVY) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [160, 9200],
    borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder, insideH: noBorder, insideV: noBorder },
    rows: [new TableRow({ children: [
      new TableCell({
        width: { size: 160, type: WidthType.DXA },
        borders: { top: noBorder, bottom: noBorder, right: noBorder,
          left: { style: BorderStyle.SINGLE, size: 20, color: borderColor } },
        shading: { fill: borderColor, type: ShadingType.CLEAR },
        children: [new Paragraph({ children: [] })]
      }),
      new TableCell({
        width: { size: 9200, type: WidthType.DXA },
        borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
        shading: { fill, type: ShadingType.CLEAR },
        margins: { top: 120, bottom: 120, left: 240, right: 240 },
        children
      })
    ]})]
  });
}

function scriptureBox(verse, ref) {
  return callout([
    new Paragraph({ spacing: sp(40, 20), children: [new TextRun({ text: `"${verse}"`, italics: true, size: 22, color: NAVY, font: "Arial" })] }),
    new Paragraph({ spacing: sp(0, 40), children: [new TextRun({ text: `— ${ref}`, bold: true, size: 20, color: GOLD, font: "Arial" })] })
  ], LIGHT_BLUE, NAVY);
}

function bul(text, boldPrefix = "") {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: sp(40, 40),
    children: boldPrefix
      ? [new TextRun({ text: boldPrefix, bold: true, size: 22, color: DARK, font: "Arial" }),
         new TextRun({ text, size: 22, color: DARK, font: "Arial" })]
      : [new TextRun({ text, size: 22, color: DARK, font: "Arial" })]
  });
}

function num(text, ref) {
  return new Paragraph({
    numbering: { reference: ref || "numbers", level: 0 },
    spacing: sp(40, 40),
    children: [new TextRun({ text, size: 22, color: DARK, font: "Arial" })]
  });
}

function spacer(h = 120) {
  return new Paragraph({ spacing: sp(h, 0), children: [] });
}

function divider() {
  return new Paragraph({
    spacing: sp(160, 160),
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD } },
    children: []
  });
}

function pb() { return new Paragraph({ children: [new PageBreak()] }); }

// Day header block
function dayHeader(num, title, subtitle, tagline, scriptures) {
  return [
    new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [9360],
      borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder, insideH: noBorder, insideV: noBorder },
      rows: [new TableRow({ children: [new TableCell({
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: NAVY, type: ShadingType.CLEAR },
        margins: { top: 280, bottom: 280, left: 400, right: 400 },
        borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
        children: [
          new Paragraph({ spacing: sp(0, 60), children: [new TextRun({ text: `DAY ${num}`, size: 18, color: GOLD, bold: true, font: "Arial" })] }),
          new Paragraph({ spacing: sp(0, 80), children: [new TextRun({ text: title, size: 44, bold: true, color: WHITE, font: "Arial" })] }),
          new Paragraph({ spacing: sp(0, 80), children: [new TextRun({ text: subtitle, size: 24, italics: true, color: "C8D8E8", font: "Arial" })] }),
          new Paragraph({ spacing: sp(60, 0), children: [new TextRun({ text: tagline.toUpperCase(), size: 18, bold: true, color: GOLD, font: "Arial" })] }),
        ]
      })]})],
    }),
    spacer(100),
    sectionLabel("Today's Verses"),
    ...scriptures.map(s => scriptureBox(s.verse, s.ref)),
    spacer(80),
  ];
}

// Exercise fill-in box
function fillIn(number, prompt, options = null) {
  const children = [
    new Paragraph({ spacing: sp(40, 20), children: [
      new TextRun({ text: `${number}.  `, bold: true, size: 22, color: NAVY, font: "Arial" }),
      new TextRun({ text: prompt, size: 22, color: DARK, font: "Arial" }),
    ]}),
  ];
  if (options) {
    children.push(new Paragraph({ spacing: sp(10, 10), children: [
      new TextRun({ text: `     ${options}`, size: 20, italics: true, color: MID_GRAY, font: "Arial" })
    ]}));
  }
  children.push(new Paragraph({ spacing: sp(4, 4), border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: "CCCCCC" } }, children: [new TextRun({ text: "     ", size: 22, font: "Arial" })] }));
  children.push(new Paragraph({ spacing: sp(4, 24), border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: "CCCCCC" } }, children: [new TextRun({ text: "     ", size: 22, font: "Arial" })] }));
  return callout(children, LIGHT_GRAY, TEAL);
}

function completeSentence(prompt) {
  return new Paragraph({
    spacing: sp(60, 4),
    children: [
      new TextRun({ text: `"${prompt}`, italics: true, size: 22, color: DARK, font: "Arial" }),
      new TextRun({ text: ' _____________________\u201d', size: 22, color: TEAL, font: "Arial" })
    ]
  });
}

function declarationBox(text) {
  return callout([
    new Paragraph({ spacing: sp(20, 20), children: [new TextRun({ text: "WRITE THIS DECLARATION", bold: true, size: 18, color: GOLD, font: "Arial" })] }),
    new Paragraph({ spacing: sp(20, 20), children: [new TextRun({ text: `"${text}"`, italics: true, bold: true, size: 22, color: NAVY, font: "Arial" })] })
  ], LIGHT_BLUE, GOLD);
}

function nextSteps(a, b, c) {
  return [
    sectionLabel("Next Steps — Pick one. Do it today."),
    callout([
      new Paragraph({ spacing: sp(0, 60), children: [new TextRun({ text: "Option A", bold: true, size: 22, color: NAVY, font: "Arial" })] }),
      body(a),
      spacer(40),
      new Paragraph({ spacing: sp(0, 60), children: [new TextRun({ text: "Option B", bold: true, size: 22, color: NAVY, font: "Arial" })] }),
      body(b),
      spacer(40),
      new Paragraph({ spacing: sp(0, 60), children: [new TextRun({ text: "Option C", bold: true, size: 22, color: NAVY, font: "Arial" })] }),
      body(c),
    ], LIGHT_GRAY, TEAL)
  ];
}

function closingPrayer(text) {
  return [
    sectionLabel("Closing Prayer"),
    callout([
      new Paragraph({ spacing: sp(20, 20), children: [new TextRun({ text, italics: true, size: 22, color: DARK, font: "Arial" })] })
    ], LIGHT_TEAL, TEAL)
  ];
}

// Session cover page
function sessionCover(num, title, subtitle, bigIdea, days) {
  return [
    new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [9360],
      borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder, insideH: noBorder, insideV: noBorder },
      rows: [new TableRow({ children: [new TableCell({
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: NAVY, type: ShadingType.CLEAR },
        margins: { top: 480, bottom: 480, left: 560, right: 560 },
        borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
        children: [
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: sp(0, 60), children: [new TextRun({ text: `SESSION ${num}`, size: 22, color: GOLD, bold: true, font: "Arial" })] }),
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: sp(0, 80), children: [new TextRun({ text: title, size: 56, bold: true, color: WHITE, font: "Arial" })] }),
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: sp(0, 120), children: [new TextRun({ text: subtitle, size: 28, italics: true, color: "C8D8E8", font: "Arial" })] }),
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: sp(120, 40), children: [new TextRun({ text: "BIG IDEA", size: 18, color: GOLD, bold: true, font: "Arial" })] }),
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: sp(0, 120), children: [new TextRun({ text: bigIdea, size: 26, bold: true, color: WHITE, font: "Arial" })] }),
          new Paragraph({ alignment: AlignmentType.CENTER, spacing: sp(80, 0), children: [new TextRun({ text: days, size: 20, color: "A8C0D8", font: "Arial" })] }),
        ]
      })]})],
    }),
    pb(),
  ];
}

// ============================================================
// THE DEVOTIONALS
// ============================================================

// ---- SESSION 1: WHO'S REALLY IN CHARGE? (Days 1–7) ----

function s1d1() {
  return [
    ...dayHeader(1, "Who's Running This?", "The Question Underneath the Question", "God's ownership is where your heart can finally stop running.", [
      { verse: "The earth is the Lord's, and everything in it, the world, and all who live in it.", ref: "Psalm 24:1 (NIV)" },
      { verse: "For from him and through him and for him are all things. To him be the glory forever! Amen.", ref: "Romans 11:36 (NIV)" },
    ]),

    body("There's a game I used to play with myself at the mall. I'd walk past a store window and mentally tally what the stuff inside was worth. The shoes. The headphones. The jacket. And then — without really meaning to — I'd start doing the math on whether I could ever afford it. Whether I was keeping up. Whether I was behind.", { before: 80 }),
    body("Most of us do this constantly, in ways more subtle than mall windows. We check other people's feeds. We calculate what they seem to have. We wonder where we rank. And running underneath all of it is a question we don't usually say out loud:"),
    spacer(40),
    pullQuote("Am I going to be okay? Will I ever have enough? And if I get enough — will it last?"),
    spacer(40),
    body("Those questions are real. But I want to suggest something: you've been asking the right question in the wrong direction."),

    h2("The Questions We're Actually Asking"),
    body("Ron Blue spent forty years as a financial advisor — sitting with thousands of families, from people who had almost nothing to people who had more than they could spend. And he said the same three questions showed up every single time, regardless of income:"),
    spacer(40),
    bul("Will I ever have enough?"),
    bul("Will it keep being enough?"),
    bul("How much is enough, anyway?"),
    spacer(60),
    body("Underneath those three, he almost always found the same deeper fear: What will it take to feel successful? Significant? Secure? And the culture has one answer to all three: more. More money. More options. More status. More cushion."),
    spacer(60),
    body("Here's what forty years taught Ron: more doesn't answer those questions. It just moves them. Every time you hit the number you thought would be enough, the number changes. The finish line runs away from you."),

    h2("The Questions That Actually Lead Somewhere"),
    body("Scripture offers three different questions — ones that don't move on you:"),
    spacer(40),
    bul("Who owns it?"),
    bul("How much is enough — as a stewardship question, not a scarcity question?"),
    bul("Is the next steward ready?"),
    spacer(60),
    body("That first question — who owns it — is the one everything else depends on. Answer it honestly, and the weight shifts. Not because your bank account changes. Because your role changes. You stop being the owner responsible for guaranteeing your future, and you become a steward responsible for faithfulness. Those are very different jobs."),
    spacer(60),
    body("Psalm 24:1 doesn't leave room for debate: \"The earth is the Lord's, and everything in it.\" Romans 11:36 takes it further — everything is from him, through him, and for him. Your ability to earn. Your health that lets you show up. The opportunity that opened when it did. None of it is self-originated. It was entrusted to you."),

    spacer(80),
    pullQuote("If God owns it, you are not alone in carrying it. The question changes from \"Will I be okay?\" to \"What does faithful look like today?\""),
    spacer(80),

    body("That's not just a spiritual idea. That's a lighter load. And a lighter load changes how you make every decision — from the big ones to the ones nobody else ever sees."),

    spacer(100),
    sectionLabel("Think About It"),
    body("When something financial goes wrong — unexpected expense, money runs out before the month does, you see someone else get something you wanted — what's your first internal move? What do you reach for?", { italic: false }),
    spacer(40),
    body("The three questions (Will I have enough? Will it last? How much is enough?) assume you're the one responsible for the answers. What would change in your day-to-day life if you genuinely believed you weren't?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Three Questions Inventory (10 minutes)"),
    body("Write short, honest answers."),
    spacer(40),
    fillIn(1, "The money question I carry most often is:", "(one sentence)"),
    fillIn(2, "Underneath it, what I'm really asking is:", "(circle one: Will I be successful? / Will I be significant? / Will I be secure?)"),
    fillIn(3, "The way I try to answer that right now is:", "(more money / more control / more options / something else)"),
    fillIn(4, "If God is the actual Owner, what changes about who has to answer my question?"),
    spacer(60),

    h2("The 'From Him' Reset (2 minutes)"),
    body("Read Romans 11:36 slowly: \"For from him and through him and for him are all things.\" Then finish these:"),
    spacer(40),
    completeSentence("An area where I'm acting like I'm the source is"),
    completeSentence("One thing I can return to God today is"),
    spacer(80),

    declarationBox("God, you are the Owner. Everything I have and everything I am belongs to you. I am not the source. Teach me to steward what you've entrusted to me with open hands and a steady heart."),
    spacer(80),

    ...nextSteps(
      "Choose one area of your life you've been carrying like you own it. Say one sentence out loud: \"God, this belongs to you.\" Don't just think it. Say it.",
      "Before the next time you spend money today — anything — pause ten seconds and ask: \"God, you're the Owner. What does faithful look like here?\" Then proceed.",
      "Text or tell one person: \"I'm thinking about what it would actually mean to live like God owns what I have. Ask me next week what changed.\""
    ),
    spacer(80),
    ...closingPrayer("Father, you are the source of every good thing, and you don't change. Forgive me for living like everything depends on me. Today I come back to the foundation: everything is from you, through you, and for you. Teach me to hold what I have with open hands — not passive, but trusting. You are the Owner. I am yours. Amen."),
    pb(),
  ];
}

function s1d2() {
  return [
    ...dayHeader(2, "Borrowed, Not Owned", "Surrendering Control Is Not Losing — It's Coming Home", "God doesn't ask you to carry everything. He asks you to trust him first.", [
      { verse: "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.", ref: "Proverbs 3:5–6 (NIV)" },
      { verse: "Casting all your cares on him, because he cares about you.", ref: "1 Peter 5:7 (CSB)" },
    ]),

    body("Picture this: Your coach invites the whole team over for dinner after the championship. Tables are set, food is ready, and everyone's standing around waiting. Coach walks toward the head of the table — and before he can sit down, you walk past him and drop into his chair.", { before: 80 }),
    body("Nobody does that. Not because there's a rule. Because the situation is obvious. It's his house, his table, his chair. You wait because he's the host."),
    body("That's what Ron Blue calls the second chair. In every life there's a first chair — the seat of ultimate authority. The question isn't whether a first chair exists. It's who's sitting in it."),
    spacer(60),
    body("If God's in the first chair, you can live with steadiness. If you're in the first chair, you might look totally fine on the outside while something inside quietly wears out from trying to hold everything together."),

    h2("Responsibility vs. Control"),
    body("Here's where most people get confused, because responsibility and control look almost identical from the outside. Both involve working hard. Both involve caring about outcomes. The difference is what's driving you."),
    spacer(40),
    bul("Responsibility says: I'll do what's mine to do.", ""),
    bul("Control says: I need to make sure nothing goes wrong.", ""),
    spacer(60),
    body("Responsibility works within the limits of being human. Control tries to go past those limits. And the difference between them, over time, is everything. Responsibility produces diligence and a clear conscience. Control produces anxiety and this quiet background belief that if you ever stop holding things together, everything will fall apart."),
    spacer(60),
    body("Here's the honest thing: the grip often isn't selfish. It's protective. You want to provide. You want to be reliable. You don't want to let people down. But even good desires become crushing when they turn into demands. When \"I want to take care of my family\" becomes \"I am the reason my family is okay,\" the weight of that will slowly flatten you. Not because you don't care — but because you've taken on a role that belongs to God."),

    h2("What Stewardship Actually Is"),
    body("Imagine you're managing someone else's investment account. The money isn't yours. You have no right to it. Your only job is to find out what the owner wants — their goals, their values, their priorities — and manage toward those ends. At some point, the owner will ask for it back. Your stewardship will be over."),
    spacer(60),
    body("That's the role. You hold much. You own nothing. God gives you access to his resources. Your job is to use them in a way that honors him. And at some point, he may take back whatever he chooses, whenever he chooses. That's not a threat — it's the nature of stewardship. Owners have rights. Stewards have responsibilities."),
    spacer(60),
    body("When this lands — not just as a concept but as something you actually live from — something surprising happens: it's a relief. Because stewards are responsible for faithfulness, not for omniscience. For obedience, not outcomes. For taking the next wise step, not for guaranteeing where every step leads."),

    spacer(80),
    pullQuote("Surrender isn't stepping into emptiness. It's stepping into the care of a steady Father. The seat you've been trying to sit in was never designed to hold you."),
    spacer(80),

    body("Proverbs 3:5–6 isn't asking for partial trust. It's asking for all of it — \"with all your heart.\" Partial trust produces divided living. Part of you trusts God, part of you is quietly managing your own backup plan. That split is exhausting. And the promise on the other side of full trust is a straight path — not an easy path, but one you don't have to navigate alone."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Where in your life right now are you most trying to make sure nothing goes wrong? What would it look like to bring responsibility to that situation — without needing to control every outcome?"),
    spacer(40),
    body("When you imagine releasing one specific area to God, what comes first — relief, fear, or something else? What does that reaction tell you about what you actually believe?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Second Chair Inventory (10 minutes)"),
    fillIn(1, "The area where I'm most likely sitting in the first chair right now is:", "(finances / future / family outcomes / my reputation / a relationship)"),
    fillIn(2, "The reason it's hard to give that up is:", "(fear of failure / don't trust the outcome / I feel responsible / something else)"),
    fillIn(3, "One step that would look like stewardship instead of control in that area:"),
    spacer(60),

    h2("The Surrender Sentence (2 minutes)"),
    completeSentence("God, you can have the first chair in"),
    completeSentence("My next faithful step as a steward is"),
    spacer(80),

    declarationBox("God, you are first. I release the need to control outcomes. Teach me to be faithful with what you've entrusted to me, and to trust you with what I can't control. I take the second chair. Lead me from there."),
    spacer(80),

    ...nextSteps(
      "Before your next decision today — money or otherwise — pause and say: \"God, you're first. Lead me.\" Then choose with steadiness, not urgency.",
      "Write down one outcome you've been trying to control. Pray one sentence: \"Father, this belongs to you.\" Identify one step that's actually yours to take. Take it. Stop there.",
      "Tell one trusted person one area where you've been sitting in the first chair. Ask them to ask you next week: \"Are you letting God lead that, or are you still running it yourself?\""
    ),
    spacer(80),
    ...closingPrayer("Father, you are steady and you do not change. Forgive me for the ways I've tried to sit in the first chair — not out of rebellion but out of fear that if I stop holding things together, nothing will hold. Today I take the second chair. Give me wisdom for what's mine to do, and peace to trust you with what's not. Amen."),
    pb(),
  ];
}

function s1d3() {
  return [
    ...dayHeader(3, "The 'Mine' Trap", "Why Ownership Drift Is So Hard to Catch", "Identity drifts when you forget where your strength came from.", [
      { verse: "You may say to yourself, 'My power and the strength of my hands have produced this wealth for me.' But remember the Lord your God, for it is he who gives you the ability to produce wealth.", ref: "Deuteronomy 8:17–18 (NIV)" },
      { verse: "Take care, and be on your guard against all covetousness, for one's life does not consist in the abundance of his possessions.", ref: "Luke 12:15 (ESV)" },
    ]),

    body("Ron Blue tells a story about a trip to Kenya in the mid-1970s. He'd spent years on Wall Street and building a CPA practice, and he assumed materialism was basically an American problem — something born of too many options and too many ads. Then he found himself standing with a Kenyan pastor, looking at a mud hut.", { before: 80 }),
    body("Ron asked what the biggest barrier to the gospel was in that part of the world. He expected the answer to be poverty, or roads, or language."),
    body("The pastor said: materialism."),
    body("Ron said: what do you mean?"),
    body("The pastor said: if a man has a mud hut, he wants a stone one. If he has a thatch roof, he wants metal. If he has one acre, he wants two. If he has one cow, he wants two."),
    spacer(60),
    body("Ron said he never forgot that. Materialism isn't a wealth problem. It isn't an American problem. It's a human heart problem. And the word at the center of it is tiny. Just four letters. Mine."),

    h2("How 'Mine' Becomes 'Me'"),
    body("The word starts out neutral. My locker. My lunch. My phone. My savings. Used that way, it just means what I'm responsible for managing. But Deuteronomy 8 identifies a slow shift that happens when things go well: we start believing we're the source."),
    spacer(60),
    body("Not dramatically. Not all at once. Just gradually. We start thinking our stability is the product of our own hustle, our own grades, our own good decisions. And when that happens, \"mine\" stops being a description and starts being a claim. It becomes the thing we protect when threatened. The proof that we're okay."),
    spacer(60),
    body("Deuteronomy calls this forgetting. And it's worth sitting with the fact that the Bible treats forgetting as a spiritual danger at the same level as outright rebellion — because forgetting doesn't look like sin. It looks like confidence. Like \"I've got this.\""),
    spacer(60),
    body("The most dangerous moment isn't when you consciously decide to take ownership from God. It's when you stop noticing you have."),

    h2("When Things Feel Personal"),
    body("Here's where the \"mine\" trap gets really costly: when something is \"mine,\" any threat to it starts to feel like a threat to me. The money stress isn't just a money stress — it becomes a verdict on my worth. The setback isn't just a setback — it feels like evidence that I'm failing. Someone else's success doesn't just make me happy for them — it quietly destabilizes me, because their \"more\" implies my \"less.\""),
    spacer(60),
    body("You can feel when this is happening in yourself. You get more defensive than the situation calls for. Someone else having something good bothers you more than it should. You feel a low-grade panic at the thought of losing what you have. These aren't character flaws. They're signals. They're signs that \"mine\" has quietly become \"me.\""),
    spacer(60),
    body("Jesus gets at this directly in Luke 12:15. He doesn't say possessions are evil. He says life doesn't consist in them. He's protecting you from letting things define you. Because once what you have becomes part of who you are, you can't hold it freely. You grip it. And a gripping hand is not a giving hand, a planning hand, or a peaceful hand."),

    spacer(80),
    pullQuote("The test isn't what you have. It's what you would lose yourself over if it disappeared. Where your identity is attached, your anxiety will follow."),
    spacer(80),

    h2("The Way Back"),
    body("Deuteronomy 8 doesn't just warn — it offers a path: \"But remember the Lord your God.\" Remembering is a practice. Not nostalgia. Re-centering. Telling yourself the truth again before your heart tells you a different story. Remembering is how you get your footing back when your identity starts leaning on the wrong thing."),
    spacer(60),
    body("When you remember God, your resources stop being proof of your worth. Your outcomes stop being your identity. Your savings account stops being the place you go to feel safe. Not because you become careless — but because you return to what's actually true: your value is anchored in God, not in what you've accumulated."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Is there something in your life — a status, a possession, a level of having — that you'd feel genuinely destabilized to lose? Not just inconvenienced. Actually shaken. What does that tell you?"),
    spacer(40),
    body("What's one specific thing you need to remember about God's faithfulness today that would loosen your grip on something you've been holding too tightly?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The 'Mine to Me' Map (10 minutes)"),
    fillIn(1, "Something I'd lose a piece of my identity over if it disappeared tomorrow:"),
    fillIn(2, "What that thing represents to me is:", "(circle one: security / proof I'm doing okay / freedom / status / something else)"),
    fillIn(3, "If it disappeared and God said 'I took it because it's mine,' my honest reaction would be:"),
    fillIn(4, "One thing I have that I didn't create — that God provided — that I can thank him for today:"),
    spacer(60),

    h2("The Remembering Practice (2 minutes)"),
    completeSentence("God, thank you for the strength you gave me to"),
    completeSentence("Today I will remember you by"),
    spacer(80),

    declarationBox("Lord, you are the Owner. My life is not defined by what I have. I remember that my strength comes from you, and I choose to hold what you've entrusted to me with gratitude and open hands."),
    spacer(80),

    ...nextSteps(
      "Write five things you have that you didn't create — a skill, a relationship, an opportunity, your health, a season God brought you through. Thank God for each one by name.",
      "The next time you feel defensive, anxious, or competitive about something you have, pause and say: \"My life does not consist in what I possess. God is my source.\" Then continue.",
      "Make one small decision today that reflects a lighter grip — don't buy something you were going to, simplify a choice you've been overthinking, or do something quietly generous."
    ),
    spacer(80),
    ...closingPrayer("Father, forgive me for quietly believing my planning and hustle are the source of my security. Thank you for every good thing you've given me — including the ability to work and decide and provide. Help me remember you today. Free me from letting what I own define who I am. Teach me to hold what I have with gratitude and open hands. Amen."),
    pb(),
  ];
}

function s1d4() {
  return [
    ...dayHeader(4, "You're Not Just Managed — You're Loved", "God's Ownership Is Personal, Not Corporate", "God's ownership isn't a claim. It's a rescue.", [
      { verse: "Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; you were bought at a price. Therefore honor God with your bodies.", ref: "1 Corinthians 6:19–20 (NIV)" },
      { verse: "Fear not, for I have redeemed you; I have called you by name, you are mine.", ref: "Isaiah 43:1 (ESV)" },
    ]),

    body("There's a version of \"God owns it all\" that sounds cold when you first hear it. Like a legal statement. Like God filing a claim on your stuff.", { before: 80 }),
    body("If that's how it lands, something important got lost in translation."),
    body("Ron Blue tells a story about an early client — a physician, one of the first generation of heart surgeons, who had built significant wealth and built a beautiful home with his wife. He came to Ron with a question he was clearly uncomfortable asking: \"Is it okay for a Christian to live in a million-dollar home?\""),
    spacer(60),
    body("Ron turned it back to him: \"What do you think God wants you to do?\" The physician said he didn't know. Ron asked if he spent time in prayer and Scripture. He didn't — he was in surgery by 6 a.m., on call at night. Ron said: \"What are you doing at four in the morning? Generally sleeping? Then you've got nothing better to do. Get up and spend ten minutes asking God that question.\""),
    spacer(60),
    body("He did. A year and a half later, Ron ran into his wife. She said: \"I don't know what you did to him, but he now spends two or three hours every morning in prayer and Bible study.\""),
    spacer(60),
    body("He never asked Ron about the house again. That house became a center of ministry — hundreds of people came to faith there. He became a significant leader in the church. And the question he started with — \"is this allowed?\" — was replaced by the only question that ever really mattered: \"Lord, what would you have me do?\""),
    spacer(60),
    body("That shift — from \"is this allowed?\" to \"what does faithfulness look like?\" — is only possible when you understand something about the nature of God's ownership. It isn't distant. It isn't impersonal. It isn't a property claim. It's a relationship with someone who knows your name."),

    h2("Ownership as Rescue"),
    body("1 Corinthians 6:19–20 reframes the word \"owns\" entirely. \"You are not your own; you were bought at a price.\" That's not God taking something from you. That's God giving something for you. The price wasn't paid by you — it was paid for you. God's ownership isn't a power move. It's a rescue story."),
    spacer(60),
    body("He didn't purchase you to use you. He redeemed you to love you. He didn't claim you like a possession. He claimed you like a person. That kind of ownership doesn't shrink you. It dignifies you. It says your life is valuable enough to be fought for."),

    h2("Ownership as Belonging"),
    body("Then Isaiah gets even more personal: \"I have called you by name, you are mine.\""),
    spacer(60),
    body("God doesn't claim you like an asset. He calls you like a Father. He knows your name. He knows your story. He knows what you're carrying right now, today, that nobody else fully sees. And he says: you belong to me. That's not corporate language. That's family language. It's the kind of thing you say to someone who's scared or exhausted or trying too hard to be okay. \"You are mine\" is not a threat. It's a shelter."),

    spacer(80),
    pullQuote("When God says 'you are mine,' he's relocating your worth from what you have to who holds you. That relocation changes everything about how you handle money — not because you now have rules, but because you now have a resting place."),
    spacer(80),

    body("A lot of people try to use money to answer questions that only love can answer. We use money to feel safe. To feel like we matter. To feel like we belong. But money can never give you what identity gives you. It can never say \"I have called you by name.\" And if you treat money as the place where you find safety and belonging, you'll always need more of it — more margin, more options, more \"just in case.\" The issue is never the amount. It's the foundation."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Where does the idea of God owning your life feel more like a restriction than a rescue? What belief about God is underneath that feeling?"),
    spacer(40),
    body("The physician stopped asking \"is this allowed?\" and started asking \"Lord, what would you have me do?\" What would that same shift look like in one area of your life right now?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("Ownership as Love (10 minutes)"),
    fillIn(1, "The area where God's ownership feels most like a restriction rather than a rescue:"),
    fillIn(2, "The fear underneath that feeling is:", "(circle one: loss / uncertainty / being forgotten / not being enough / being controlled)"),
    fillIn(3, "The truth I want to actually receive today:", "(circle one: I belong to God / I am not alone / God is steady / God fought for me)"),
    fillIn(4, "One step that would look like 'I belong to a loving Father' instead of 'I must secure myself':"),
    spacer(60),

    h2("Name and Belonging (2 minutes)"),
    completeSentence("God, you have called me by name. Today I belong to you in"),
    completeSentence("Because I belong to you, the next thing I'll do is"),
    spacer(80),

    declarationBox("Father, I belong to you. I am not my own, and I am not alone. Teach me to steward my life and my resources as a loved person — not from fear, but from trust in the One who called me by name."),
    spacer(80),

    ...nextSteps(
      "Before your next decision today, pause and say: \"I belong to God.\" Then choose — not from what protects you, but from what honors him.",
      "Write three things you've been gripping. Pray over each one: \"Father, I'm yours. This is yours too.\" Then don't immediately pick them back up.",
      "Do one small act of generosity today that no one will see. Let it be a response to belonging, not a performance of it."
    ),
    spacer(80),
    ...closingPrayer("Father, thank you that your ownership is personal. You redeemed me, called me by name, and made me yours. Forgive me for trying to find safety and identity in what I can hold or control. Today I receive your love. Teach me to steward my life with a steady heart — faithful in what you've entrusted to me, surrendered in what I can't control. I belong to you. Amen."),
    pb(),
  ];
}

function s1d5() {
  return [
    ...dayHeader(5, "Your Money Has a Record", "What God Is Already Doing With Your Finances", "Your trust shows up in your choices, not your intentions.", [
      { verse: "For where your treasure is, there your heart will be also.", ref: "Matthew 6:21 (NIV)" },
      { verse: "I have learned to be content whatever the circumstances.", ref: "Philippians 4:11 (NIV)" },
    ]),

    body("Ron Blue once told a mega-church pastor that after forty years in financial services, he believed God's Word speaks to every financial decision — gives wisdom for the process and principles for the decisions, at all times, in all circumstances. He said it works as well in Africa as on Wall Street. It works for a single mom and for a billionaire.", { before: 80 }),
    body("The pastor said: \"If that's the case, why is it that the church is not seen as the center of financial wisdom?\""),
    spacer(60),
    body("Ron's been sitting with that question ever since. Part of the answer is shame — money conversations in church often become guilt-based rather than grace-based. But there's something else. Most people don't understand what God is actually doing with their money. They treat it as a practical problem to solve. They don't see it as a spiritual formation process that's already in motion."),
    spacer(60),
    body("But it is. And once you understand how it works, your finances stop feeling like random noise and start feeling like something with a shape."),

    h2("Money as a Tool"),
    body("The most obvious way God uses money is as a tool — a resource that enables things to happen. It funds families, builds organizations, serves people, creates margin for generosity. At that level, money just does things."),
    spacer(60),
    body("But it's also a tool in God's hands to do something in you. The discipline of not spending everything you earn isn't just about numbers — it's a practice of trust. The habit of giving first isn't just about your budget — it's a practice of believing you have enough. What you do with money is forming you, even when you're not paying attention."),

    h2("Money as a Test"),
    body("Paul says in Philippians 4 that he \"learned\" to be content. Not that he felt it naturally. Not that his circumstances got easier. He learned it — through seasons of need and seasons of plenty — until contentment became a strength rather than a mood."),
    spacer(60),
    body("That word \"learned\" is the key: contentment is not a personality type. It's a formation outcome. Tight seasons reveal what you actually trust. Abundant seasons reveal what you actually love. Both directions expose the heart. The test isn't pass or fail — it's diagnostic. God isn't testing you to catch you out. He's testing you the way a good coach does — to show you where you've grown and where you still need work."),

    h2("Money as a Testimony"),
    body("The third way God uses money is the one most people never think about: as a testimony. The world is living in confusion, asking the same three wrong questions on repeat. And the world has a right to look at people who follow Jesus and see something different."),
    spacer(60),
    body("Not better. Different. Less anxious than the circumstances justify. The person whose friendship doesn't crack under financial pressure the way every other relationship does. The one who gives generously when it doesn't make mathematical sense. The one who is genuinely okay with enough in a culture screaming for more. That's a testimony. Not a speech. A life."),

    spacer(80),
    pullQuote("Money has no voice, but it has a record. If someone followed you for thirty days and looked at where your money went, what would they conclude about what you actually trust?"),
    spacer(80),

    body("Matthew 6:21 says treasure leads and heart follows. Which means how you handle money is shaping your heart right now — in ordinary weeks, in unremarkable decisions. That's not meant to make you paranoid about every purchase. It's meant to make you intentional. Because your financial habits are forming you whether you're paying attention to them or not."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Looking at the three uses of money — tool, test, testimony — which one feels most active in your life right now? What do you think God is doing in that dimension?"),
    spacer(40),
    body("Paul said he \"learned\" contentment. What season in your life has taught you the most about what you actually trust? What did it teach you?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Tool / Test / Testimony Inventory (10 minutes)"),
    fillIn(1, "One way money is acting as a tool in my life right now — something God is doing through it:"),
    fillIn(2, "One way my current financial situation is revealing something about what I trust:"),
    fillIn(3, "One thing about how I handle money that could be a testimony to something different — if I changed it:"),
    fillIn(4, "The area where 'treasure leads and heart follows' is most obviously true for me right now:"),
    spacer(60),

    h2("The Trust Mirror (2 minutes)"),
    completeSentence("One habit that most reveals what I actually prioritize is"),
    completeSentence("One choice I could make this week that would redirect my treasure is"),
    spacer(80),

    declarationBox("Jesus, you are my Master. My treasure will follow you. Teach me to choose faithfulness over fear, and to use what you've entrusted to me as a tool for your purposes, an open field for your formation, and a testimony to your faithfulness."),
    spacer(80),

    ...nextSteps(
      "Before any non-essential purchase today, pause and ask: \"What is this revealing about what I trust?\" Then choose with clarity.",
      "Give a small amount today in a way no one will see. Let it be a private act of redirecting your treasure — training your heart to follow.",
      "Look at one month of spending — your bank app or whatever you use. Don't judge it. Just look. Write one sentence: \"If a stranger saw this, they'd conclude I value ___.\""
    ),
    spacer(80),
    ...closingPrayer("Father, thank you for using my finances to form me. Teach me to handle what you've entrusted to me with the awareness that it's doing something in me, not just for me. Give me a contented heart that keeps learning what you taught Paul. And let my financial life be a quiet testimony to the world that you are enough. Amen."),
    pb(),
  ];
}

function s1d6() {
  return [
    ...dayHeader(6, "Stop Rehearsing It", "Worry Is Often a Control Issue", "God doesn't ask you to carry tomorrow. He asks you to trust him today.", [
      { verse: "But seek first his kingdom and his righteousness, and all these things will be given to you as well.", ref: "Matthew 6:33 (NIV)" },
      { verse: "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.", ref: "Philippians 4:6–7 (ESV)" },
    ]),

    body("When Ron Blue started his financial planning practice, he did what any sensible business owner does: arranged a $10,000 line of credit at the bank. That's how you start a business. You establish liquidity. You protect yourself.", { before: 80 }),
    body("Then a conviction hit him that he couldn't shake: you're going to give people financial advice, and you're starting with debt?"),
    body("He canceled it. No backup plan. A family to feed. A business to launch. No idea what was going to happen."),
    body("Not long after, a contact introduced him to the head of training at Coca-Cola — who hired him to develop and teach retirement seminars for their employees. Ron worked out the numbers: six thousand to develop it, one thousand each time he taught it, four sessions. Total: ten thousand dollars. The exact amount he'd given up. Paid that December."),
    spacer(60),
    body("He tells that story not as a formula — obey and get back the exact amount. He tells it because of what it taught him about worry: almost all of it is about control. And surrendering control is almost always what makes room for God to move."),

    h2("What Worry Is Actually Doing"),
    body("Nobody chooses to worry because they enjoy it. We choose it because it feels responsible. Staying alert. Staying prepared. For a lot of people, worry is how they prove to themselves they're not being careless."),
    spacer(60),
    body("But Jesus, in Matthew 6, treats worry differently. He doesn't shame it. He diagnoses it. He shows that worry is fundamentally connected to ownership — to the assumption that the future belongs to you and you have to secure it. When you live like the future is yours to manage, your mind will work overtime trying to manage it."),
    spacer(60),
    body("There's a critical difference between rehearsing and preparing:"),
    spacer(40),
    bul("Preparing asks: what's mine to do today? It produces action."),
    bul("Rehearsing asks: what if this goes wrong, what if that changes, what if I can't handle it? It produces fatigue."),
    spacer(60),
    body("Preparing keeps you present. Rehearsing keeps you living in a future that doesn't exist yet, carrying weight for scenarios that may never arrive. Worry is rehearsal. And rehearsal is a way of trying to stay in the first chair."),

    h2("What Jesus Actually Offers"),
    body("Matthew 6:33 might be the most practically useful sentence in the Sermon on the Mount: \"Seek first his kingdom and his righteousness, and all these things will be given to you as well.\" That's a daily re-ordering with concrete application. God's agenda shapes your decisions before your fear does. You don't wait until you feel safe to obey. You obey as a way of learning safety."),
    spacer(60),
    body("Seeking first might look like praying before planning instead of after. Slowing down a decision fear is rushing. Having an honest conversation you've been avoiding. The shape varies. The direction is always the same: God's priorities before your anxiety's demands."),

    spacer(80),
    pullQuote("Worry doesn't carry what you're carrying. It just keeps you busy while you carry it alone. Prayer is the exchange: bring it into the light, and the peace of God stands guard over what you brought."),
    spacer(80),

    body("Philippians 4:6–7 gives you a practice, not just a principle. In everything — by prayer and thanksgiving — bring your requests to God. That's not telling you to deny what's hard. It's telling you to bring what's hard into God's presence instead of running it in loops inside your own head. The promise isn't that the problem disappears. It's that the peace of God will guard your heart and mind. Peace as a guard. A stabilizing presence in the middle of real, unresolved circumstances."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Think about your biggest anxiety right now — financial or otherwise. Are you rehearsing it or preparing for it? What's the practical difference in this specific situation?"),
    spacer(40),
    body("\"Seek first his kingdom\" is a daily re-ordering. What would it look like, in one decision you're currently facing, to let God's priorities shape your choice before your anxiety does?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Worry-to-Prayer Inventory (10 minutes)"),
    fillIn(1, "The thing I'm rehearsing most often right now is:"),
    fillIn(2, "What I'm trying to protect underneath it:", "(circle one: security / stability / a relationship / my reputation / my options)"),
    fillIn(3, "What is actually mine to do about it — the one responsible step:"),
    fillIn(4, "What is God's to carry — the part I need to stop managing:"),
    spacer(60),

    h2("The 'Seek First' Practice (2 minutes)"),
    completeSentence("God, today I'm seeking your kingdom first in"),
    completeSentence("My next faithful step — not the whole plan, just the next step — is"),
    spacer(80),

    declarationBox("Father, you are the Owner. I release tomorrow into your care. Teach me to seek you first today and take the next faithful step with a steady heart — preparing, not rehearsing; trusting, not controlling."),
    spacer(80),

    ...nextSteps(
      "Write your most persistent worry in one sentence. Under it, write a one-sentence prayer giving it to God. Thank him for his care before anything has changed. Pray it twice today.",
      "Set a limit on how long you let your mind run through worst-case scenarios today. When you hit the limit, read Philippians 4:6–7 out loud instead.",
      "Identify one practical step that builds stability — a conversation you've been avoiding, a plan you haven't started. Do it calmly today, without needing to solve everything past it."
    ),
    spacer(80),
    ...closingPrayer("Father, you know what I'm carrying and what I'm afraid could happen. Thank you that you care for me personally and completely. Teach me to seek your kingdom first and trust you with outcomes I can't control. Turn my rehearsing into preparing, and my pressure into wisdom. Guard my heart and my mind with your peace as I take the next faithful step. In Jesus' name, amen."),
    pb(),
  ];
}

function s1d7() {
  return [
    ...dayHeader(7, "Different, Not Better", "What a Surrendered Life Actually Looks Like", "Stewardship is not a one-time decision. It is a daily return.", [
      { verse: "For in him all things were created... all things have been created through him and for him. He is before all things, and in him all things hold together.", ref: "Colossians 1:16–17 (NIV)" },
      { verse: "But godliness with contentment is great gain.", ref: "1 Timothy 6:6 (NIV)" },
    ]),

    body("Two of Ron Blue's clients had about as different lives as you could imagine.", { before: 80 }),
    body("One was a physician who had built significant wealth and, at some point, made a decision: he would cap his lifestyle at the level he'd been living when he finished medical school. Everything above that, he gave away. He went to Haiti. He funded hospitals. He invested in people he'd never meet. At some point Ron noticed he'd traded his Porsche for a Honda. Physicians don't drive Hondas into the physician's parking lot. He parked down the street."),
    body("The other was the CEO of a major grocery chain who lived in a trailer park. Not because he had to. Because he chose to. Same logic: capped lifestyle, everything above it given away."),
    spacer(60),
    body("Two men. One in a million-dollar home, one in a trailer park. They couldn't have looked more different from the outside. But they had arrived at the same place by the same path: on their knees, asking God what enough looked like for them. And both of them were genuinely, visibly, surprisingly free."),
    spacer(60),
    body("That's what this week has been building toward. Not a financial plan. A different kind of person."),

    h2("The World Is Watching"),
    body("One of the most powerful things a person can have in a culture this restless, this status-obsessed, this anxious about money — is simply being different. Not better. Different. Not wealthier — more content. Not without pressure — but handling pressure from a foundation that produces steadiness instead of panic."),
    spacer(60),
    body("The people around you — friends, classmates, people who barely know you — have a right to look at you and wonder: why are they different? Why does that person not spiral when money gets tight? Why are they generous when it doesn't make sense? Why do they seem genuinely okay with enough?"),
    spacer(60),
    body("Those questions, when they get asked, are an open door. But they only get asked when the life behind them is actually different. Beliefs that produce the same restlessness as everyone else's don't open any doors."),

    h2("What Stewardship Builds Over Time"),
    body("Colossians 1:16–17 is one of the most stabilizing things in Scripture: in him all things hold together. Your life is not held together by your vigilance or your perfect decisions or your ability to see around every corner. It is held together by someone stronger, steadier, and wiser than you. That doesn't cancel your responsibility. It relocates your confidence."),
    spacer(60),
    body("A steward asks different questions than an owner:"),
    spacer(40),
    bul("Owner: How do I protect what's mine?  →  Steward: How do I honor God with what's entrusted to me?"),
    bul("Owner: How do I stay in control?  →  Steward: What is the next faithful step?"),
    bul("Owner: What if it goes wrong?  →  Steward: Who is holding this with me?"),
    spacer(60),
    body("Those questions, asked daily, form a person over time. Not dramatically. Quietly. The way any habit forms — through repetition, one ordinary decision at a time, until the new way of thinking starts to feel like the default."),

    spacer(80),
    pullQuote("Your old default was: I have to hold this together. Your new default is: God holds all things together, and I am faithful with what's in my hands today. That shift doesn't happen once. It happens every morning."),
    spacer(80),

    h2("The Daily Return"),
    body("You will drift. Everyone does. The goal of this week hasn't been to eliminate drift — it's been to introduce a new default. A place to return to when you notice you've wandered. The difference between a mature steward and an immature one isn't that the mature one never drifts. It's that they return faster."),
    spacer(60),
    body("A daily reset is how that return gets quick. It doesn't have to be complicated. One sentence before the day starts: God, you own it all. Lead me today. Then the next faithful step. Not the whole plan. Just the next thing."),
    spacer(60),
    body("Ron has watched people live this way for decades. The ones who do it consistently — who keep returning to the foundation — show four things: contentment, confidence, clarity of communication, and consistency of behavior. Not as achievements they worked toward. As fruit that grew naturally when the foundation was right."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Think of someone you know who handles what they have with genuine peace. What is it about the way they live? What would you need to believe to live that way?"),
    spacer(40),
    body("The physician and the CEO both arrived at freedom the same way — on their knees, asking God what enough looked like for them. Have you spent time asking that question? What came up?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Daily Reset Plan (10 minutes)"),
    fillIn(1, "The moment in my day when I most often drift back into thinking like an owner:", "(morning / before a purchase / in a hard conversation / when something unexpected happens)"),
    fillIn(2, "My old default in that moment:", "(circle one: tighten / avoid / overthink / react / try harder)"),
    fillIn(3, "My new steward response could be:", "(one sentence)"),
    fillIn(4, "One simple practice I can repeat this week to build the new default:"),
    spacer(60),

    h2("The Steward Questions (2 minutes)"),
    completeSentence("If God owns it all, what is mine to do today?"),
    completeSentence("If Christ holds all things together, I can release"),
    spacer(80),

    declarationBox("God, you are the Owner. I am your steward. Today I will practice open hands, take the next faithful step, and trust you to hold what I cannot. I am different because of whose I am — not better, different."),
    spacer(80),

    ...nextSteps(
      "Before you check your phone in the morning, say one sentence: \"God, you own it all. Lead me today.\" Then take one small faithful step — not a perfect plan, just the next thing.",
      "Before your next money decision, pause ten seconds and ask: what would a steward do here? Then choose calmly.",
      "Tonight: where did you live like a steward today? Where did you drift back into ownership? Thank God for one win. Surrender one drift. Then rest."
    ),
    spacer(80),
    ...closingPrayer("Father, thank you that I am not the owner of my life. Thank you that in Christ, all things hold together — not by my vigilance but by your power. Forgive me for living like everything depends on me. Teach me a new default: open hands, steady trust, faithful obedience. Help me remember your ownership throughout the ordinary day — in the unremarkable decisions, the unexpected pressures, the daily chances to be genuinely different. Give me wisdom for what is mine to do, peace for what is not, and the courage to take the next faithful step. Amen."),
    pb(),
  ];
}

// ============================================================
// SESSION 2 — MINE IS NOT A SAFE WORD (Days 8–14)
// ============================================================

function s2d1() {
  return [
    ...dayHeader(8, "The Grip", "Why 'Mine' Is the Most Dangerous Word You Own", "Materialism isn't a wealth problem. It's a human heart problem.", [
      { verse: "Watch out! Be on your guard against all kinds of greed; life does not consist in an abundance of possessions.", ref: "Luke 12:15 (NIV)" },
      { verse: "Keep your lives free from the love of money and be content with what you have, because God has said, 'Never will I leave you; never will I forsake you.'", ref: "Hebrews 13:5 (NIV)" },
    ]),

    body("There's a word that feels completely harmless until you look at it closely.", { before: 80 }),
    body("Mine."),
    body("My phone. My money. My stuff. My future. Used casually, it's just shorthand for what we're responsible for. But Ron Blue discovered something working with thousands of families over forty years: the word \"mine\" has a second gear. And when it kicks in, it changes everything."),
    spacer(60),
    body("The shift is subtle. It starts with the neutral version — I'm managing this thing. Then gradually, almost invisibly, it becomes something else: this thing is part of who I am. I'm not just responsible for it. I need it. And if it threatens to go away, something in me threatens to go away with it."),

    h2("It's Not Just an American Problem"),
    body("Ron tells a story about standing with a pastor in Kenya, looking at a mud hut. Ron assumed materialism was a product of wealth — something that grew in places like America where there was too much of everything. He asked the pastor what the biggest barrier to the gospel was in that region. He expected an answer about roads or resources."),
    spacer(60),
    body("The pastor said: materialism."),
    body("Ron pushed: what do you mean?"),
    body("\"If a man has a mud hut, he wants a stone one. If he has a thatch roof, he wants metal. If he has one acre, he wants two. If he has one cow, he wants two.\""),
    spacer(60),
    body("Ron said he never forgot that. The grip isn't a feature of abundance. It's a feature of the human heart. It shows up at every income level, in every culture, in every generation. The word \"mine\" — in its dangerous form — is not a first-world problem. It's a soul problem."),

    h2("What the Grip Actually Costs"),
    body("When something is \"mine\" in the deep sense — when it's attached to your identity — any threat to it stops being just a threat to a thing. It becomes a threat to you. The financial stress isn't just a financial stress — it's a verdict on whether you're doing okay. The comparison with someone who has more isn't just uncomfortable — it's destabilizing, because their \"more\" implies your \"less.\""),
    spacer(60),
    body("You can feel this in yourself if you pay attention. You get more defensive than the situation calls for. You feel a low-grade panic when something feels uncertain. You notice a quiet irritation when someone else gets something good. These aren't character flaws. They're signals. Signs that \"mine\" has moved from a description to an identity."),

    spacer(80),
    pullQuote("Jesus doesn't say possessions are evil. He says life doesn't consist in them. He's protecting you from letting things define you — because once possessions become your identity, you can't hold them freely."),
    spacer(80),

    body("And a gripping hand is not a giving hand, a planning hand, or a peaceful hand. The grip produces the opposite of what you wanted the thing to produce in the first place."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Is there something you have — or want — that feels like part of who you are? Not just something you own, but something that would shake your sense of self if it disappeared?"),
    spacer(40),
    body("Think about the last time you felt genuinely envious of something someone else had. What was underneath it — what were you really afraid you were missing?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Grip Inventory (10 minutes)"),
    fillIn(1, "Something I'd feel genuinely shaken to lose — not just inconvenienced, but destabilized:"),
    fillIn(2, "What that thing says about me to others — or to myself — is:"),
    fillIn(3, "The last time I felt envious of someone else, the thing underneath it was:"),
    fillIn(4, "One thing I can hold with a lighter grip this week:"),
    spacer(60),

    h2("The Hebrews 13 Anchor (2 minutes)"),
    body("Read Hebrews 13:5 slowly: \"Be content with what you have, because God has said, 'Never will I leave you; never will I forsake you.'\""),
    spacer(40),
    body("The promise isn't more stuff. It's presence. Write one sentence about what it means to have a God who never leaves:"),
    completeSentence("Because God never leaves me, I don't need"),
    spacer(80),

    declarationBox("Lord, you are the Owner. I refuse to let what I have — or don't have — define who I am. You are my security. Teach me to hold everything else with open hands."),
    spacer(80),

    ...nextSteps(
      "Spend five minutes today noticing when you feel the grip tighten — when something feels threatened or someone has more. Don't shame yourself. Just notice.",
      "Identify one thing you've been holding tightly. Do one small act that reflects a lighter grip — delay a purchase, give something away, or simply thank God for it.",
      "Memorize Hebrews 13:5 today. Write it on something you'll see. Let the promise \"never will I leave you\" be the thing you reach for instead of more."
    ),
    spacer(80),
    ...closingPrayer("Father, forgive me for letting things define me. Forgive me for gripping when I should be giving. Teach me to find my security not in what I accumulate but in the unshakeable fact that you will never leave me. Loosen my grip today. Amen."),
    pb(),
  ];
}

function s2d2() {
  return [
    ...dayHeader(9, "The Identity Reset", "When 'Mine' Becomes 'Me'", "Deuteronomy's warning isn't about success. It's about what success can quietly do to you.", [
      { verse: "You may say to yourself, 'My power and the strength of my hands have produced this wealth for me.' But remember the Lord your God, for it is he who gives you the ability to produce wealth.", ref: "Deuteronomy 8:17–18 (NIV)" },
      { verse: "For it is by grace you have been saved, through faith — and this is not from yourselves, it is the gift of God — not by works, so that no one can boast.", ref: "Ephesians 2:8–9 (NIV)" },
    ]),

    body("Deuteronomy 8 is one of the strangest warnings in the Bible. It's not a warning for people who are struggling. It's a warning for people who are doing well.", { before: 80 }),
    body("God is speaking to Israel right before they enter the promised land — a place with cities they didn't build, houses full of things they didn't fill, wells they didn't dig. The warning: when all this good comes to you, be careful. Because the story you'll be tempted to tell yourself is wrong."),
    spacer(60),
    body("The story is: I did this. My hustle. My decisions. My work ethic. The good things in my life are evidence of my strength."),
    spacer(60),
    body("The Bible calls that forgetting. And it treats forgetting as spiritually dangerous — not because success is bad, but because success is exactly the kind of thing that quietly reorders your story so that you become the hero."),

    h2("The Slow Slide"),
    body("The shift Deuteronomy warns about doesn't happen in a dramatic moment. It happens in a series of small, unremarkable moments where you simply stop giving credit where it belongs."),
    spacer(60),
    body("You work hard — which is right and good — and the work pays off. You don't stop to ask whether the ability to work came from God. You make a smart decision and it works out. You don't pause to acknowledge that the clarity came from somewhere. Over time, the narrative solidifies: I did this. My strength. My hands. My hustle."),
    spacer(60),
    body("And at some point, \"I did this\" becomes the foundation your identity sits on. Which means anything that threatens what you've built threatens you. And anything that contradicts the narrative — failure, loss, someone doing better — feels like an attack on who you are."),

    h2("Grace as the Corrective"),
    body("Ephesians 2 cuts to the root of it: by grace you have been saved — not from yourselves, not from your works, so that no one can boast. The gospel is the ultimate story about a gift you didn't earn. If the most important thing about you is something you received, not something you achieved — if your very standing before God is grace rather than hustle — then the narrative changes."),
    spacer(60),
    body("You stop taking credit for what was given. You stop measuring yourself against what others have produced, because production was never the point. You hold your accomplishments more lightly, because they were always a stewardship, not a proof."),

    spacer(80),
    pullQuote("The most dangerous moment isn't when you consciously decide to take ownership from God. It's when you stop noticing you have."),
    spacer(80),

    body("The antidote Deuteronomy offers is simple and ancient: remember. Not nostalgia — re-centering. Tell yourself the true story before your heart tells you the alternative. What did God give you that you didn't create? What door opened that you didn't open? What ability do you have that you didn't build from scratch?"),
    body("Remembering is the practice that keeps the slide from happening."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Where in your life are you most tempted to think: I did this? What would change if you re-told that story as a gift received rather than an achievement earned?"),
    spacer(40),
    body("The gospel says the most important thing about you is something you received, not something you produced. How does that change the way you think about what you have?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The 'I Did This' Audit (10 minutes)"),
    fillIn(1, "One area where I'm most tempted to take full credit for my success:"),
    fillIn(2, "If I told the honest version of that story — what God gave me that I didn't create — it would include:"),
    fillIn(3, "One way the 'I did this' narrative has made me defensive or anxious:"),
    fillIn(4, "One thing about who I am that is entirely grace — not performance:"),
    spacer(60),

    h2("The Remembering Practice (2 minutes)"),
    completeSentence("God, the ability you gave me that I most often forget to credit you for is"),
    completeSentence("Today I'll remember you by"),
    spacer(80),

    declarationBox("Father, I remember that everything I have and every ability I carry came from you. My success is not my proof — your grace is my foundation. I hold what I've built with open hands. It was never mine to begin with."),
    spacer(80),

    ...nextSteps(
      "Write out three things you've accomplished recently. For each one, write one thing God gave you that made it possible — an ability, an open door, health, a person, timing.",
      "The next time you catch yourself taking full credit for something good in your life, pause and say: \"Thank you, God. You gave me that.\" Say it out loud.",
      "Read Deuteronomy 8:11–18 slowly today. Write one sentence about what it says to you personally."
    ),
    spacer(80),
    ...closingPrayer("Father, forgive me for telling myself the wrong story — the one where I'm the source and the hero. The truth is simpler and better: every good thing I have is a gift. I didn't build my own ability. I didn't open my own doors. You did. Teach me to remember that today in the moments when I'm most tempted to forget. Amen."),
    pb(),
  ];
}

function s2d3() {
  return [
    ...dayHeader(10, "You Are Not What You Own", "Your Worth Was Settled Before You Had Anything", "The thing you're trying to earn with your stuff — you already have it.", [
      { verse: "Fear not, for I have redeemed you; I have called you by name, you are mine.", ref: "Isaiah 43:1 (ESV)" },
      { verse: "See what great love the Father has lavished on us, that we should be called children of God! And that is what we are!", ref: "1 John 3:1 (NIV)" },
    ]),

    body("Here's something worth sitting with: almost every reason people want more stuff is actually about something else entirely.", { before: 80 }),
    body("We want the car because of what the car says about us. We want the brand because of what the brand communicates to people watching. We want the apartment, the experience, the item — and underneath the wanting is a question we don't usually acknowledge: Does this make me worth something?"),
    spacer(60),
    body("That question is ancient. It's also exactly the wrong place to go looking."),

    h2("The Identity That Doesn't Move"),
    body("Isaiah 43:1 is one of the most personal sentences in the entire Bible. God says to his people — who are, at this exact moment, in exile, stripped of everything, without country or temple or stability — \"I have called you by name, you are mine.\""),
    spacer(60),
    body("Not: I have recognized your achievements. Not: I have evaluated your performance and found it acceptable. Not: I have seen your balance sheet and determined your value."),
    spacer(60),
    body("Called by name. That's intimate. That's specific. That's not the language of a distant administrator — it's the language of a Father who knows you individually, not collectively. And the claim — \"you are mine\" — is not a legal document. It's a shelter. It's the thing you say to someone who needs to know they are not alone and not forgotten."),
    spacer(60),
    body("1 John 3:1 adds the staggering layer: \"See what great love the Father has lavished on us, that we should be called children of God. And that is what we are.\" Not \"what we're working toward.\" Not \"what we could become if we're faithful enough.\" That is what we are, right now, today, regardless of what's in the account or on the shelf."),

    h2("What Money Can't Give You"),
    body("A lot of us try to use money to answer questions that only love can answer. We use what we have to feel significant, to feel like we belong, to prove we're doing okay. But money can never give you what identity gives you."),
    spacer(60),
    body("Money can't tell you \"I have called you by name.\" It can't hold you when things fall apart. It can't forgive you when you fail. And if you try to use it as the place where your worth lives, you'll discover something unpleasant: the more you accumulate, the more anxious you become about losing it. Because if your worth is stored there, losing it means losing you."),
    spacer(60),
    body("The person who knows who they are — whose identity is anchored in belonging to God rather than in what they have — can hold everything else with an open hand. Because none of it is the point. The point was already settled on a cross before you had anything."),

    spacer(80),
    pullQuote("When God says 'you are mine,' he's relocating your worth from what you have to who holds you. That is the only relocation that actually works."),
    spacer(80),

    spacer(100),
    sectionLabel("Think About It"),
    body("What is one thing you own (or want) that is, honestly, partly about what it says about you? What story does it tell — and is that story worth carrying?"),
    spacer(40),
    body("\"I have called you by name, you are mine\" — does that feel like an anchor to you, or does it feel abstract? What would it take for it to feel real?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Worth Audit (10 minutes)"),
    fillIn(1, "Something I want (or have) that is partly about what it says about me:"),
    fillIn(2, "The story it's supposed to tell is:"),
    fillIn(3, "If God's love is my identity and this thing disappeared, what would actually be lost?"),
    fillIn(4, "One way I can act today from my God-given identity instead of from what I own:"),
    spacer(60),

    h2("The Belonging Practice (2 minutes)"),
    completeSentence("Because God has called me by name, I don't need to prove myself by"),
    completeSentence("Today I will live from my identity by"),
    spacer(80),

    declarationBox("Father, you called me by name. You lavished love on me and called me your child. My worth is not in my wallet or my wardrobe or my achievements. It was settled before I had anything. Teach me to live like that's true."),
    spacer(80),

    ...nextSteps(
      "Read 1 John 3:1–3 slowly today. Write one sentence about what it means for your worth to be settled by love rather than by what you produce or possess.",
      "Choose one thing you own that you've been using (consciously or not) to signal your worth. Hold it differently today. Thank God for it as a gift, not as proof.",
      "Tell someone today one thing you appreciate about them that has nothing to do with what they own or accomplish — something about who they are."
    ),
    spacer(80),
    ...closingPrayer("Father, thank you that you called me by name before I had anything to show for myself. Thank you that my identity is your child — not my performance, not my possessions, not my achievements. Teach me to live from that foundation today — to hold everything else lightly because the only thing that really matters is already settled. Amen."),
    pb(),
  ];
}

function s2d4() {
  return [
    ...dayHeader(11, "The Comparison Trap", "Why Somebody Else's More Makes You Feel Like Less", "Comparison is a thief. And it's remarkably good at its job.", [
      { verse: "We do not dare to classify or compare ourselves with some who commend themselves. When they measure themselves by themselves and compare themselves with themselves, they are not wise.", ref: "2 Corinthians 10:12 (NIV)" },
      { verse: "When Peter saw him, he asked, 'Lord, what about him?' Jesus answered, 'What is that to you? You must follow me.'", ref: "John 21:21–22 (NIV)" },
    ]),

    body("There's a loop that social media is extremely good at triggering, and it goes like this:", { before: 80 }),
    spacer(40),
    bul("You see someone else's life, stuff, experience, or success."),
    bul("You compare it to yours."),
    bul("Yours feels smaller."),
    bul("You feel the urge to do something about it — buy something, post something, achieve something."),
    bul("You do the thing. Briefly feel okay. Repeat."),
    spacer(60),
    body("The problem with comparison isn't just that it's unpleasant. The problem is that it's built on a lie: that there is a ranking, and your wellbeing depends on where you land."),
    body("2 Corinthians 10:12 says something remarkably blunt about this: people who measure themselves by other people are not wise. Not sinful — unwise. The comparison game is a foolish game, because the scale was never real."),

    h2("The Moving Finish Line"),
    body("Here's what comparison actually does: it installs a finish line that runs away from you. You hit one level and immediately compare yourself to the next level up. Which means you can never actually arrive. The moment you achieve the thing that was supposed to make you feel okay, you find yourself looking at someone who has more, and the cycle restarts."),
    spacer(60),
    body("This is why contentment can never be found by comparison. Contentment is not the feeling you get when you finally outcompete everyone. Contentment is what you discover when you stop playing the comparison game entirely. It requires getting off the scale — deciding that someone else's more doesn't say anything about your enough."),

    h2("What Jesus Said to Peter"),
    body("After his resurrection, Jesus was restoring Peter by the water. He gave Peter a calling, told him something hard was coming, and said: \"Follow me.\""),
    spacer(60),
    body("Peter looked over at the disciple Jesus loved and said: \"Lord, what about him?\""),
    spacer(60),
    body("Jesus said: \"What is that to you? You must follow me.\""),
    spacer(60),
    body("That exchange contains one of the most practical things Jesus ever said about comparison. The question \"what about him?\" is the comparison question. It's the question that takes your eyes off your own path and locks them onto someone else's. And Jesus' answer isn't a long explanation. It's a redirect: that's not your concern. Follow me."),
    spacer(60),
    body("Your call. Your path. Your enough. Not theirs."),

    spacer(80),
    pullQuote("Comparison installs a moving finish line. The only way to stop chasing it is to get off the scale entirely — to decide that someone else's more doesn't say anything about your enough."),
    spacer(80),

    spacer(100),
    sectionLabel("Think About It"),
    body("What is one account, person, or environment that consistently triggers the comparison loop for you? What does it make you feel — and what does it make you want to do?"),
    spacer(40),
    body("Jesus said to Peter: \"What is that to you? Follow me.\" Is there a comparison you're currently running that is distracting you from your own path? What would it look like to redirect?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Comparison Audit (10 minutes)"),
    fillIn(1, "The place I'm most likely to compare myself to others right now is:", "(school / social media / a specific person / a group I want to be part of / something else)"),
    fillIn(2, "When the comparison loop runs, the feeling underneath it is:", "(not enough / behind / overlooked / unfair / something else)"),
    fillIn(3, "The thing I'm most tempted to do to fix that feeling is:"),
    fillIn(4, "What would it look like to simply redirect — to ask 'what is that to me, and what is mine to follow?'"),
    spacer(60),

    h2("The Redirect Practice (2 minutes)"),
    completeSentence("God, the comparison I most need to release right now is"),
    completeSentence("What's mine to follow is"),
    spacer(80),

    declarationBox("Father, free me from measuring myself against anyone but you. What someone else has says nothing about what I lack. Teach me to follow my own path with contentment, and to celebrate others' good without it meaning my own less."),
    spacer(80),

    ...nextSteps(
      "Choose one feed, account, or environment that consistently triggers the comparison loop. Step back from it for one day. Notice what changes.",
      "The next time you feel the comparison loop start, say Jesus' line out loud: \"What is that to me? I must follow.\" Then redirect.",
      "Write a genuine encouragement to someone whose success you've been comparing yourself against. Send it. See how it changes the feeling."
    ),
    spacer(80),
    ...closingPrayer("Father, the comparison trap is subtle and I fall into it easily. Teach me to measure myself only by your call and your grace — not by what others have or where others are. Free me from the moving finish line. Teach me to celebrate others' good without diminishing my own path. And help me follow you — just follow you. Amen."),
    pb(),
  ];
}

function s2d5() {
  return [
    ...dayHeader(12, "The Status Game", "Why We Want What We Want", "Most of what we call wanting stuff is actually wanting belonging.", [
      { verse: "Do nothing out of selfish ambition or vain conceit. Rather, in humility value others above yourselves, not looking to your own interests but each of you to the interests of the others.", ref: "Philippians 2:3–4 (NIV)" },
      { verse: "But whatever were gains to me I now consider loss for the sake of Christ.", ref: "Philippians 3:7 (NIV)" },
    ]),

    body("Here's an experiment worth trying: the next time you really want something, ask yourself this question honestly:", { before: 80 }),
    spacer(40),
    pullQuote("Would I still want this if nobody knew I had it?"),
    spacer(40),
    body("For a lot of things, the honest answer is: not really. Or at least — not as much. Because a lot of what we call wanting stuff is actually wanting what the stuff signals. The right brand communicates a certain kind of person. The right activity signals a certain kind of life. The right look places you in the right group."),
    spacer(60),
    body("That's not a moral failure. It's human nature. We are social creatures, and we use what we have to communicate who we are. The problem isn't that we care about belonging — belonging is a real and legitimate need. The problem is when we try to purchase belonging instead of build it."),

    h2("The Status Ladder Goes Nowhere"),
    body("The status game has a built-in problem: the ladder never ends. Every level up reveals another level above it. Every group you successfully signal your way into has an inner ring that requires more to access. The people who seem to have \"arrived\" are often the most anxious, because they know exactly how thin the social ice they're standing on actually is."),
    spacer(60),
    body("Paul had every reason to play the status game. In Philippians 3 he lists his credentials — legitimate, impressive, hard-won. And then he says something radical: all of that, he considers loss. Not neutral. Loss. Because everything that used to be in the gain column — status, achievement, credentials, belonging to the right group — had to be subtracted from his life to make room for something better."),
    spacer(60),
    body("The something better wasn't another, higher-status group. It was a relationship that didn't require performing. A belonging that couldn't be revoked. An identity that didn't need props."),

    h2("Humility as the Escape"),
    body("Philippians 2:3–4 offers what sounds like a difficult command — value others above yourself, look to others' interests. But there's a hidden gift in it: when you genuinely shift your attention from what you look like to what others need, the status game loses its grip. You can't be anxious about where you rank and genuinely focused on someone else at the same time. They're mutually exclusive."),
    spacer(60),
    body("Humility isn't self-deprecation. It's freedom from the exhausting work of performance. It's the posture of someone who already knows who they are, so they have nothing to prove."),

    spacer(80),
    pullQuote("Belonging built on what you own is rented. Belonging built on who you are is owned. And the belonging that matters most came free — at a price paid by someone else."),
    spacer(80),

    spacer(100),
    sectionLabel("Think About It"),
    body("Is there something you own (or want) that is mostly about what it signals to others? What would it feel like to have it with no audience?"),
    spacer(40),
    body("Paul called his status and credentials \"loss\" compared to knowing Christ. Is there anything in your life you've been treating as gain that might actually be costing you something?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Status Audit (10 minutes)"),
    fillIn(1, "Something I own or want that is mostly about what it signals:"),
    fillIn(2, "The group or level I'm trying to signal my way into:"),
    fillIn(3, "If that status disappeared tomorrow, what would I actually lose?"),
    fillIn(4, "One way I can invest in belonging that doesn't require props or performance:"),
    spacer(60),

    h2("The Philippians 3 Recalculation (2 minutes)"),
    completeSentence("Something I've been treating as 'gain' that might actually be holding me back is"),
    completeSentence("What I'd rather invest in instead is"),
    spacer(80),

    declarationBox("Father, free me from the exhausting work of performing for approval. I already belong to you. I have nothing to prove and nothing to lose. Teach me to invest in what lasts — in people, not props; in relationship, not status."),
    spacer(80),

    ...nextSteps(
      "Before you buy or post or do something today, ask the honest question: \"Would I still want this if nobody knew I had it?\" Let the answer inform what you do.",
      "Do one thing for someone else today that they'll never know about. Let it be a practice of acting from identity rather than performing for audience.",
      "Write a list of five things that make you valuable that have nothing to do with what you own. Read it when the status loop starts."
    ),
    spacer(80),
    ...closingPrayer("Father, I'm tired of trying to earn my place with what I own or what I look like. Thank you that my belonging to you came free — paid for by someone else. Teach me to live from that security, not perform for a different one. And free me to invest my energy in people rather than props. Amen."),
    pb(),
  ];
}

function s2d6() {
  return [
    ...dayHeader(13, "Contentment Is a Skill", "Paul Didn't Feel It — He Learned It", "Contentment is not a personality type. It is a formation outcome.", [
      { verse: "I have learned to be content whatever the circumstances. I know what it is to be in need, and I know what it is to have plenty. I have learned the secret of being content in any and every situation, whether well fed or hungry, whether living in plenty or in want.", ref: "Philippians 4:11–12 (NIV)" },
      { verse: "But godliness with contentment is great gain. For we brought nothing into the world, and we can take nothing out of it.", ref: "1 Timothy 6:6–7 (NIV)" },
    ]),

    body("Contentment sounds like the kind of thing some people have and others don't. Like it's a temperament — you're either naturally laid-back about what you have, or you're not. Some people are just wired for gratitude, and the rest of us are stuck wanting more.", { before: 80 }),
    body("Paul dismantles that idea in one sentence."),
    body("\"I have learned to be content.\""),
    body("Not: I was born content. Not: I finally got enough to feel content. Not: I had a moment of spiritual breakthrough and contentment just arrived."),
    body("Learned. Practiced. Trained. Through seasons of not having much, and seasons of having plenty — and discovering that both directions can trip you up, and both directions can teach you something."),

    h2("What Tight Seasons Teach"),
    body("When Paul says he knows what it is to be in need, he's not romanticizing poverty. He's reporting a classroom. Tight seasons reveal what you actually trust. When the comfortable margin disappears — when you can't buy what you normally buy, when the plan doesn't work out, when the number is lower than expected — what you reach for is what you've been quietly building your security on."),
    spacer(60),
    body("For some people, a tight season reveals that they've been trusting God — and peace holds, unexpectedly. For others, it reveals that they've been trusting their own ability to produce, and when production slows, anxiety floods in. Both responses are diagnostic. Neither is permanent. Both are formation material."),

    h2("What Abundant Seasons Teach"),
    body("Comfortable seasons are just as revealing. When money is good and options are open, what you naturally drift toward is what you actually love. Does abundance make you generous or acquisitive? Grateful or just wanting more? Settled or restless?"),
    spacer(60),
    body("Paul says he has \"learned the secret of being content in any and every situation.\" The word secret is fascinating. It implies something hidden, something that has to be discovered — not something you can just decide. And the secret is this: contentment doesn't come from the amount. It comes from the anchor. If your identity is in God's ownership and God's love rather than in the amount you have, then the amount stops running your emotional life."),

    spacer(80),
    pullQuote("You don't find contentment when you finally have enough. You discover it when you stop making enough the point."),
    spacer(80),

    body("1 Timothy 6:7 adds the most clarifying frame: \"We brought nothing into the world, and we can take nothing out of it.\" Everything in between is stewardship. The sooner you're at peace with that, the more freely you can manage what you've been given — generously, wisely, without the low-grade anxiety that comes from treating it like it's yours to keep."),

    spacer(100),
    sectionLabel("Think About It"),
    body("What season of life — tight or abundant — has taught you the most about what you actually trust? What did you discover?"),
    spacer(40),
    body("Contentment is learned through practice, not achieved once. Where are you in the learning curve? What is the current season teaching you?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Contentment Journal (10 minutes)"),
    fillIn(1, "A season that revealed what I was actually trusting (tight or abundant):"),
    fillIn(2, "What it taught me about myself:"),
    fillIn(3, "The area where I'm most obviously still learning contentment right now:"),
    fillIn(4, "One practice I could add this week that would build contentment as a skill:"),
    spacer(60),

    h2("The Abundance Inventory (2 minutes)"),
    completeSentence("When I have extra money or resources, I naturally drift toward"),
    completeSentence("What I'd like that pattern to be instead is"),
    spacer(80),

    declarationBox("Father, teach me the contentment that Paul learned — not the kind that comes from enough, but the kind that comes from knowing you. Whatever the season I'm in right now, let it form me rather than just pass over me."),
    spacer(80),

    ...nextSteps(
      "Identify the season you're currently in — tight or abundant or somewhere in between. Write one thing this season might be trying to form in you.",
      "Fast from one thing you usually reach for when you're restless — scrolling, spending, comparing. Replace it with one act of gratitude for what you already have.",
      "Memorize Philippians 4:11–12 this week. Read it when the restlessness starts."
    ),
    spacer(80),
    ...closingPrayer("Father, I want the contentment that Paul described — the kind that holds regardless of the amount. Teach me through this season, whatever it is. Form me. Don't let me just move through it unchanged. I want to learn the secret. Amen."),
    pb(),
  ];
}

function s2d7() {
  return [
    ...dayHeader(14, "The Open Hand", "What Happens When You Stop Gripping", "You can't receive with a closed fist. You can't give with one either.", [
      { verse: "One person gives freely, yet gains even more; another withholds unduly, but comes to poverty.", ref: "Proverbs 11:24 (NIV)" },
      { verse: "Now he who supplies seed to the sower and bread for food will also supply and increase your store of seed and will enlarge the harvest of your righteousness.", ref: "2 Corinthians 9:10 (NIV)" },
    ]),

    body("There's a physical picture that captures everything this week has been building toward:", { before: 80 }),
    body("Close your fist as tight as you can. Now try to receive something. Try to give something. Try to hold something precious and fragile with care."),
    body("You can't. Not with a closed fist. The grip that feels protective is actually the thing preventing all the transactions that matter."),
    body("The open hand isn't weakness. It's the posture that makes everything else possible."),

    h2("The Paradox of Proverbs"),
    body("Proverbs 11:24 sounds backwards at first read: \"One person gives freely, yet gains even more; another withholds unduly, but comes to poverty.\" This isn't a financial strategy — it's a description of how the universe works under God's ownership."),
    spacer(60),
    body("The person who grips tightly ends up losing the very thing they were trying to protect. Not always financially — sometimes in ways harder to measure but more important: peace, generosity, the ability to enjoy what they have, the freedom to give without it feeling like loss."),
    spacer(60),
    body("The person who holds loosely — who gives freely, who doesn't treat what they have as the source of their security — discovers that there's more. Not necessarily more money, though often that too. More freedom. More peace. More capacity to be present rather than anxious."),

    h2("What God Does With Open Hands"),
    body("2 Corinthians 9:10 carries an agricultural image: God supplies seed to the sower. The sower, by definition, is the person who doesn't hoard the seed — who takes what they have and puts it in the ground, trusting it will come back multiplied. The hoarder protects the seed but gets no harvest. The sower risks the seed and receives the harvest."),
    spacer(60),
    body("The open hand doesn't mean careless. It doesn't mean irresponsible. It means trusting that you can afford to be generous because your security isn't stored in what you're holding. Your security is in the One who owns it all."),

    spacer(80),
    pullQuote("The open hand is the posture of a person who knows whose they are. It doesn't grip because it doesn't have to. The source isn't what's in the hand. The source is who's holding the hand."),
    spacer(80),

    body("This is the destination of everything this session has been pointing toward. Not a financial strategy. Not a discipline to master. A posture — the posture of a person whose identity is anchored in belonging to God rather than in what they accumulate."),
    spacer(60),
    body("Open hands don't just give more freely. They live more freely. They rest more. They compare less. They plan without panic. They hold what they have with gratitude rather than anxiety. Because the point was never the thing in the hand."),

    spacer(100),
    sectionLabel("Think About It"),
    body("Where is your hand most closed right now — where are you holding something too tightly to give freely or receive well? What are you afraid will happen if you open it?"),
    spacer(40),
    body("Think about someone you know who lives with genuinely open hands — who gives freely, who holds what they have lightly. What is it about the way they carry themselves? What do they seem to know that makes it possible?"),
    spacer(40),

    sectionLabel("Exercises"),
    h2("The Open Hand Inventory (10 minutes)"),
    fillIn(1, "One area where my hand is most closed right now:"),
    fillIn(2, "What I'm afraid will happen if I open it:"),
    fillIn(3, "One small act of open-handed generosity I could practice this week:"),
    fillIn(4, "What would change about my daily life if I carried everything with an open hand?"),
    spacer(60),

    h2("The Sower's Decision (2 minutes)"),
    completeSentence("One thing I've been holding onto that might be meant to be given away or released is"),
    completeSentence("If I opened my hand there, what I'd hope to receive is"),
    spacer(80),

    declarationBox("Father, teach me the open hand. Teach me to hold what you've given me with gratitude and with looseness — knowing that my security isn't in what I'm holding, but in who's holding me. I release the grip. Amen."),
    spacer(80),

    ...nextSteps(
      "Do one act of generosity today that requires genuinely open hands — give something that costs you something, without expecting anything back.",
      "Identify one thing you've been gripping out of fear. Hold it open before God in prayer: \"This is yours. I trust you with it.\"",
      "Review the week: where did you live with more of an open hand than before? Where is the grip still tight? Thank God for the progress. Bring the rest back to him."
    ),
    spacer(80),
    ...closingPrayer("Father, I want to be the person described in Proverbs — the one who gives freely and gains more, not more stuff, but more of what actually matters. Teach me the open hand. Loosen my grip on what I've been clutching. And let me find that you are the source I needed all along. Amen."),
    pb(),
  ];
}

// I'll continue with Sessions 3-6 in condensed but complete form
// Sessions 3-6 follow identical structure — 7 days each

function generateSession3() {
  const days = [
    { n:15, t:"It's Already Doing Something", st:"Money as a Tool — What God Uses It to Accomplish", tl:"Every dollar is a decision. Every decision is a formation.", scriptures:[{verse:"For where your treasure is, there your heart will be also.",ref:"Matthew 6:21 (NIV)"},{verse:"No one can serve two masters. Either you will hate the one and love the other, or you will be devoted to the one and despise the other. You cannot serve both God and money.",ref:"Matthew 6:24 (NIV)"}], content:[
      body("Think about the last time you spent money on something and felt good about it afterward — not just satisfied, but genuinely good. Now think about a purchase you regret.", {before:80}),
      body("There's a difference between those two experiences, and it's not primarily about the amount. The difference is about alignment. One purchase lined up with something real in you. The other didn't. And you knew the difference, even if you couldn't explain why."),
      body("That instinct is telling you something important: money isn't neutral. It moves in a direction. And the direction it's moving is forming you."),
      h2("A Tool in Your Hands"),
      body("The most straightforward way money functions is as a tool — it makes things happen. It funds what matters to you. It enables experiences, relationships, and work. At that level, money just does things."),
      body("But it's also a tool in God's hands to do something in you. Matthew 6:21 is the operating principle: where your treasure goes, your heart follows. Not the other way around. The heart doesn't lead and the money follows. The money leads, and the heart follows after it."),
      body("Which means: every financial habit is a formation habit. What you give first shapes what you trust. What you save for shapes what you're hoping for. What you spend consistently on shapes what you love. Your budget — if you made it brutally honest — is less a financial document and more a spiritual autobiography."),
      h2("Two Masters"),
      body("Matthew 6:24 is blunt in a way that makes people uncomfortable: you cannot serve both God and money. Most of us read that and immediately want to defend ourselves — I'm not worshipping money. I'm just using it."),
      body("But Jesus isn't describing dramatic idol worship. He's describing divided loyalty. When money becomes the thing your decisions are organized around — when the question \"can I afford it?\" shapes more of your life than \"what does God want here?\" — then money has effectively taken the first chair. Not by a dramatic act of rebellion. Just by accumulation of small defaults."),
      body("The question isn't: do you love money? The question is: what runs your decisions? If it's the account balance more than the Owner of the account — then something has taken a seat it wasn't designed to fill."),
      spacer(80),
      pullQuote("If you let me look at where your money goes for thirty days, I can tell you your goals, your values, and your priorities. Not because money is the most important thing — but because how you handle it tells the truth about what is."),
      spacer(80),
    ]},
    { n:16, t:"What Your Money Says About You", st:"Money as a Test — What Tight Seasons Reveal", tl:"The test isn't pass or fail. It's diagnostic.", scriptures:[{verse:"Whoever can be trusted with very little can also be trusted with much, and whoever is dishonest with very little will also be dishonest with much.",ref:"Luke 16:10 (NIV)"},{verse:"The Lord is my shepherd, I lack nothing.",ref:"Psalm 23:1 (NIV)"}], content:[
      body("There's a moment that happens in a tight season that doesn't happen anywhere else. Your normal margin disappears. The comfortable buffer is gone. And suddenly you find out what's underneath all the good intentions.", {before:80}),
      body("You find out what you actually trust."),
      body("Not what you say you trust. Not what you believe intellectually. What you functionally trust — the thing you actually reach for when the ground gets unsteady. For some people it's God, and a genuine peace surfaces that surprises even them. For most people it's something else: a frantic need to solve it, a quiet panic, a grip that tightens around whatever is left."),
      body("Neither response is a verdict. Both are data. The tight season is diagnostic, not punitive."),
      h2("Small Things Aren't Small"),
      body("Luke 16:10 says something that sounds simple but runs deep: the person who can be trusted with little can be trusted with much, and vice versa. The implication is that the small, daily, unremarkable financial decisions are actually the primary classroom. Not the big moments. The small ones."),
      body("How you handle $20 when no one's watching. Whether you give when the amount feels too small to matter. Whether you tell the truth on a form when it would be easier not to. Whether you say no to something when the right answer is no. Those tiny decisions are building something. They're forming a person. And the person they form is the one who will make the big decisions later."),
      h2("Psalm 23 as Financial Theology"),
      body("\"The Lord is my shepherd, I lack nothing.\" That sentence is either true or it isn't. And the way you respond to a tight season is a pretty good indicator of which one you actually believe."),
      body("If you lack nothing — if the Shepherd's provision is genuinely your foundation — then a tight season is uncomfortable but not destabilizing. It's not a verdict on your worth. It's not evidence that God has forgotten you. It's a season. And seasons form things."),
      body("If you lack nothing, then the small decision to give when you don't have much isn't reckless. It's testimony. It's saying with your checkbook what you've been saying with your mouth: I trust the Shepherd."),
      spacer(80),
      pullQuote("The test isn't pass or fail. God isn't testing you to catch you — he's testing you the way a good coach does: to show you where you've grown and where you still need work."),
      spacer(80),
    ]},
    { n:17, t:"Your Life as Evidence", st:"Money as a Testimony — What the World Sees", tl:"The most powerful witness is not what you say. It's how you live when the pressure is on.", scriptures:[{verse:"In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.",ref:"Matthew 5:16 (NIV)"},{verse:"Do not conform to the pattern of this world, but be transformed by the renewing of your mind.",ref:"Romans 12:2 (NIV)"}], content:[
      body("One of the most underrated forms of witness isn't a conversation about faith. It's a life that doesn't make sense to the people watching.", {before:80}),
      body("The student who doesn't spiral when money gets tight. The friend who gives generously when they don't have much. The person who seems genuinely okay with what they have in a culture that is screaming \"you need more.\" That's not a sermon. That's a life. And it raises questions that sermons often don't."),
      h2("What 'Different' Looks Like"),
      body("Romans 12:2 calls you to be transformed — not conformed to the pattern of the world. The world's pattern around money is: get more, spend more, compare more, worry more. The transformed pattern is: steward faithfully, give generously, be content, trust the Owner."),
      body("Those two patterns produce visibly different people. The world's pattern produces anxiety dressed up as ambition. The transformed pattern produces peace that doesn't make sense given the circumstances. And peace that doesn't make sense given the circumstances is one of the most powerful testimonies a person can have."),
      h2("What People Are Actually Watching"),
      body("Matthew 5:16 says let your light shine so that people see your good deeds and glorify God. Financial behavior is one of the most visible forms of good deeds — because money is the thing everyone is anxious about, which means your lack of anxiety about it is immediately noticeable."),
      body("You don't have to say anything. The way you respond when something financial goes wrong. The ease with which you give. The absence of the low-grade panic that everyone else is carrying. The genuinely contented way you talk about what you have. Those things get noticed. And they open conversations that nothing else opens."),
      spacer(80),
      pullQuote("Your life doesn't have to be perfect to be a testimony. It just has to be different. And the difference isn't about how much you have — it's about who you trust with it."),
      spacer(80),
    ]},
    { n:18, t:"First Things First", st:"Seek First — A Daily Practice", tl:"You don't wait until you feel safe to seek God. You seek God as a way of learning what safe actually is.", scriptures:[{verse:"But seek first his kingdom and his righteousness, and all these things will be given to you as well. Therefore do not worry about tomorrow.",ref:"Matthew 6:33–34 (NIV)"},{verse:"Commit to the Lord whatever you do, and he will establish your plans.",ref:"Proverbs 16:3 (NIV)"}], content:[
      body("Most people's prayer and financial life are on parallel tracks that rarely intersect.", {before:80}),
      body("They pray about spiritual things — relationships, faith, character — and they handle money with their own wisdom, their own plan, their own backup strategies. God gets the spiritual realm. They get the practical realm. And the problem is that Jesus never made that distinction."),
      body("Matthew 6:33 is one of the most comprehensive verses in the Sermon on the Mount: seek first his kingdom and his righteousness, and all these things will be given to you as well. \"All these things\" includes the practical things — food, clothing, the basic needs Jesus has been talking about. Seeking first isn't a spiritual discipline separate from practical life. It's the integration of the two."),
      h2("What 'Seek First' Actually Means"),
      body("Seeking first means God's agenda shapes your financial decisions before your fear does. It means you pray before you plan, not after. It means you ask what faithfulness looks like before you ask what protection looks like. It means the first question you bring to a money decision isn't \"can I afford it?\" but \"what does God want here?\""),
      body("This sounds impractical until you try it. And then it becomes the most practical thing you do. Because a decision made from clarity — from a settled sense of who you are and who owns what — is almost always better than a decision made from anxiety."),
      h2("Proverbs 16:3 as a Practice"),
      body("\"Commit to the Lord whatever you do, and he will establish your plans.\" Commit means to roll something off your shoulders and onto his. Not to stop working or stop planning — but to acknowledge before you start that the outcome isn't yours to guarantee. You bring your best faithful effort. He establishes the result."),
      body("This is the posture that makes work sustainable long-term. The person who works for God's purposes and trusts the outcomes to God has a different energy than the person carrying the full weight of guaranteeing results. One produces faithful effort. The other produces burnout."),
      spacer(80),
      pullQuote("Seeking first is a daily act of re-ordering. Before the anxiety runs your decisions, bring God into the first moment. Then proceed — with steadiness instead of urgency."),
      spacer(80),
    ]},
    { n:19, t:"The Gratitude Weapon", st:"How Thankfulness Breaks the Comparison Cycle", tl:"Gratitude isn't a mood. It's a weapon against the thing that would otherwise consume you.", scriptures:[{verse:"Give thanks in all circumstances; for this is God's will for you in Christ Jesus.",ref:"1 Thessalonians 5:18 (NIV)"},{verse:"Praise the Lord, my soul, and forget not all his benefits.",ref:"Psalm 103:2 (NIV)"}], content:[
      body("The comparison loop — that cycle of seeing what others have, feeling like you have less, wanting to fix it — has an enemy. Not a complicated one. Not an expensive one.", {before:80}),
      body("Specific, named gratitude."),
      body("Not general gratitude — \"I'm thankful for my family and my health.\" That kind of gratitude is real but it doesn't cut through the comparison spiral because it's too abstract. What cuts through it is the specific, named, out-loud kind: \"God, thank you for this exact thing. Today. Right now.\""),
      h2("Why Specificity Matters"),
      body("Psalm 103:2 says \"forget not all his benefits.\" The failure mode it's warning against is not dramatic ingratitude — it's forgetting. The slow slide where the good things stop registering because they've become background noise."),
      body("The practice of specific gratitude is the cure for forgetting. It forces you to actually see what you have instead of automatically filtering toward what you lack. And every time you name something specifically — this conversation, this meal, this moment, this provision at this exact time — you are re-training your attention away from the comparison spiral and back toward what's actually true."),
      h2("Thankfulness in All Circumstances"),
      body("1 Thessalonians 5:18 says give thanks in all circumstances — not for all circumstances, but in them. There's an important distinction. You don't have to be grateful that hard things are hard. You can be grateful in the middle of a hard thing — grateful for what God is doing, for his presence in the season, for what you still have while other things are difficult."),
      body("This kind of gratitude doesn't deny reality. It widens the frame. It refuses to let the hard thing be the only thing in view. And a widened frame changes decisions. The person who can see what they have — even in a tight season — makes better decisions than the person whose vision has narrowed to only the problem."),
      spacer(80),
      pullQuote("Gratitude doesn't deny what's hard. It refuses to let what's hard be the only thing in view. It widens the frame — and a wider frame changes everything about how you see your options."),
      spacer(80),
    ]},
    { n:20, t:"What Faithful Means Right Now", st:"Small Decisions, Big Formation", tl:"Faithfulness isn't an event. It's a thousand small decisions that build a person.", scriptures:[{verse:"His master replied, 'Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things. Come and share your master's happiness!'",ref:"Matthew 25:21 (NIV)"},{verse:"The one who is faithful in a very little is also faithful in much.",ref:"Luke 16:10 (ESV)"}], content:[
      body("One of the questions teenagers get asked more than almost any other is: what do you want to do with your life?", {before:80}),
      body("It's not a bad question. But it sometimes creates the impression that life is organized around a few big moments — the big decision, the big achievement, the big turning point. And that the space between those moments is just... waiting."),
      body("The Bible tells a very different story. In Matthew 25, the master doesn't praise the servant for the big dramatic thing. He praises the servant for being faithful with \"a few things.\" The promotion came from how the small things were handled. Not the impressive things. The ordinary ones."),
      h2("The Things Nobody Sees"),
      body("There's a version of faithfulness that happens in front of audiences — generous donations at church, public commitments, visible acts of service. That kind of faithfulness is good. But it's not the primary classroom."),
      body("The primary classroom is the thing nobody sees. Whether you tell the truth on the form when it would be easier not to. Whether you give when the amount feels too small to bother. Whether you spend the birthday money in a way that reflects who you say you are. Whether you return the extra change when the cashier made an error in your favor."),
      body("Those tiny moments are building the person who will make the big decisions. Every small act of faithfulness is a rep — a practice that strengthens the muscle. And every small act of unfaithfulness is a rep in the opposite direction."),
      h2("Right Now Counts"),
      body("You might be thinking: I don't have much money yet. I'll be faithful with finances when there's more to be faithful with."),
      body("Luke 16:10 corrects that assumption directly. The person faithful with little is the same person who'll be faithful with much — because faithfulness is a character trait, not a threshold. The person who waits for the larger amounts to start practicing stewardship will find that the larger amounts come with the same temptations at a bigger scale."),
      body("Right now — with whatever you have — is the classroom. And what you practice right now is what you'll default to later."),
      spacer(80),
      pullQuote("You're not in a waiting room until your life gets big enough to matter. You're in the classroom. And what you're doing with the little right now is exactly who you'll be with the much later."),
      spacer(80),
    ]},
    { n:21, t:"The Record of a Life", st:"Seven Days Later — What Changed?", tl:"Stewardship isn't a weekend retreat. It's a daily return to the same foundation.", scriptures:[{verse:"Therefore, since we are surrounded by such a great cloud of witnesses, let us throw off everything that hinders and the sin that so easily entangles. And let us run with perseverance the race marked out for us.",ref:"Hebrews 12:1 (NIV)"},{verse:"Not that I have already obtained all this, or have already arrived at my goal, but I press on to take hold of that which Christ Jesus took hold of me for.",ref:"Philippians 3:12 (NIV)"}], content:[
      body("At the end of two weeks — fourteen days of asking the question \"who owns this?\" in fourteen different directions — it's worth pausing to ask a different question:", {before:80}),
      body("What actually changed?"),
      body("Not what changed in your bank account. Not what changed in your circumstances. What changed in how you're carrying things? What shifted in the grip? What looks different about the way you're holding what you have?"),
      h2("Progress, Not Arrival"),
      body("Paul says in Philippians 3 that he hasn't arrived — he's pressing on. Even after years of practicing what he preaches, he's still in formation. Still running the race. Still taking hold of the thing Christ took hold of him for."),
      body("That's not discouraging. It's the most honest description of the Christian life there is. Formation doesn't end. The race is run until it's finished. And the goal isn't to cross a finish line where you're no longer tempted to grip, no longer tempted to compare, no longer tempted to sit in the first chair."),
      body("The goal is to keep returning. To notice when you've drifted and come back faster than last time. To let the accumulation of small faithful decisions form a person who looks, over time, genuinely different from the culture around them."),
      h2("Throw Off What Hinders"),
      body("Hebrews 12:1 says throw off everything that hinders and the sin that so easily entangles — and run. The throwing off is active. It's intentional. It's the daily choice to release what you've been carrying that wasn't yours to carry."),
      body("After two weeks of this, you probably have a clearer picture of what your particular \"everything that hinders\" looks like. The grip that's tightest. The comparison that runs longest. The area where you're still sitting in the first chair. That specificity is a gift — because you can't throw off what you haven't named."),
      body("Name it. Then run."),
      spacer(80),
      pullQuote("The difference between a mature steward and an immature one isn't that the mature one never drifts. It's that they return faster. That's the goal — not perfection. Faster return."),
      spacer(80),
    ]},
  ];
  return days;
}

function generateSession4() {
  const days = [
    { n:22, t:"The Daily Return", st:"Stewardship as a Practice, Not a Position", tl:"You don't achieve stewardship. You practice it. Every morning.", scriptures:[{verse:"Because of the Lord's great love we are not consumed, for his compassions never fail. They are new every morning; great is your faithfulness.",ref:"Lamentations 3:22–23 (NIV)"},{verse:"So whether you eat or drink or whatever you do, do it all for the glory of God.",ref:"1 Corinthians 10:31 (NIV)"}], content:[
      body("Two of Ron Blue's clients ended up in the same place from completely different starting points.", {before:80}),
      body("One was a physician who built significant wealth and capped his lifestyle at medical school levels — giving everything above that away. He traded his Porsche for a Honda and parked down the street from the physician's lot."),
      body("The other was a CEO of a major grocery chain who chose to live in a trailer park. Different houses, different tax brackets, different visible lives. But they had arrived at the same posture by the same path: on their knees, asking God what enough looked like for them. And both of them were genuinely, visibly free."),
      body("That freedom wasn't a one-time decision. It was a daily return to the same foundation: God owns it, I manage it, and the question isn't how much I accumulate — it's how faithfully I steward what I'm given today."),
      h2("New Every Morning"),
      body("Lamentations 3:22–23 says God's compassions are new every morning. That newness is the structure of grace — not a lump sum delivered once, but a fresh supply every morning you wake up. And stewardship works the same way."),
      body("You don't become a faithful steward in a dramatic transformation moment. You become one by returning to the foundation every morning. By making the small decision to acknowledge ownership before you start spending. By asking what faithful looks like today, not just in general."),
      h2("Whatever You Do"),
      body("1 Corinthians 10:31 is almost too simple: \"Whatever you do, do it all for the glory of God.\" Whatever includes financial decisions. It includes small purchases. It includes what you do with your paycheck on the day it hits your account. It includes how you negotiate, how you negotiate, how you give, how you save."),
      body("The comprehensiveness of \"whatever\" is the point. Stewardship isn't a category of life separate from the rest. It's the posture underneath everything — the orientation of a person who has settled the ownership question and is living from that settled place."),
      spacer(80),
      pullQuote("The question isn't whether you had a dramatic conversion moment about money. The question is whether you come back to the foundation today. That's the only day that counts right now."),
      spacer(80),
    ]},
    { n:23, t:"What Does 'Enough' Look Like?", st:"Defining the Finish Line Before You Get There", tl:"If you don't decide what enough looks like, the culture will decide for you — and it will never be enough.", scriptures:[{verse:"But if we have food and clothing, we will be content with that.", ref:"1 Timothy 6:8 (NIV)"},{verse:"Keep falsehood and lies far from me; give me neither poverty nor riches, but give me only my daily bread. Otherwise, I may have too much and disown you and say, 'Who is the Lord?' Or I may become poor and steal, and so dishonor the name of my God.", ref:"Proverbs 30:8–9 (NIV)"}], content:[
      body("At some point — ideally before you have the amount, not after — you need to ask a question that surprisingly few people ever ask:", {before:80}),
      body("What does enough look like for me?"),
      body("Not as an abstract philosophical question. As a practical one with an actual answer. A lifestyle level. A giving target. A savings goal. A specific picture of what \"I have enough\" looks like — so that when you get there, you recognize it instead of moving the finish line."),
      h2("The Proverbs Prayer"),
      body("Proverbs 30:8–9 contains one of the most honest prayers in the Bible: \"Give me neither poverty nor riches, but give me only my daily bread.\" The pray-er is asking for enough — not excess, not scarcity. And he gives the reason: too much and I might forget God; too little and I might dishonor him."),
      body("That's a remarkable level of self-awareness. It takes knowing yourself — your particular weaknesses, your particular temptations — and making that knowledge a prayer. I know what excess does to me. I know what scarcity does to me. God, lead me to the middle where I'm most faithful."),
      h2("Deciding Before the Pressure"),
      body("Ron Blue watched clients set lifestyle finish lines — caps on what they would spend on themselves — and give everything above those caps away. The physician parked down the street. The CEO lived in a trailer park. Neither decision was easy. Both decisions were made before the pressure to decide hit — before the income grew to the level that made the upgrade seem reasonable."),
      body("The principle: decisions made in advance, from a place of clarity and prayer, are almost always better than decisions made in the moment when desire, peer pressure, and cultural expectation are all running simultaneously. Decide what enough looks like now, when the decision is cheaper to make."),
      spacer(80),
      pullQuote("'Enough' is not a number that arrives from outside you. It's a decision you make. And the person who decides it deliberately lives differently from the person who never does."),
      spacer(80),
    ]},
    { n:24, t:"The Danger of Drift", st:"How Good Things Quietly Become the Wrong Thing", tl:"The biggest financial danger for most people isn't a catastrophic loss. It's a slow, comfortable drift.", scriptures:[{verse:"The ground of a certain rich man yielded an abundant harvest. He thought to himself, 'What shall I do? I have no room to store my crops...' But God said to him, 'You fool! This very night your life will be demanded from you. Then who will get what you have prepared for yourself?'", ref:"Luke 12:16–20 (NIV)"},{verse:"For the love of money is a root of all kinds of evil.", ref:"1 Timothy 6:10 (NIV)"}], content:[
      body("The parable in Luke 12 is about a man who had a good harvest. Not a man who cheated anyone. Not a man who was obviously evil. A man who had a lot, and whose primary response to having a lot was to figure out how to keep it.", {before:80}),
      body("He didn't ask what the harvest was for. He didn't ask who might need what he had. He asked: how do I secure this for myself? And the answer he landed on — build bigger barns — was completely logical from a purely practical standpoint. You have more. You need more storage. Makes sense."),
      body("Except that the same night, his life was demanded of him. And suddenly the bigger barns were irrelevant."),
      h2("The Drift Is Gradual"),
      body("1 Timothy 6:10 says the love of money is a root of all kinds of evil. It doesn't say money. It says the love of it. The unhealthy attachment. The way it starts to function as the organizing principle rather than a tool."),
      body("That drift is almost never dramatic. It's gradual. You get a little more, and the response is to protect a little more. Then a little more after that. Bigger barns is just the natural conclusion of a logic that started much earlier and much smaller."),
      body("The safeguard isn't poverty. The safeguard is a question asked regularly: what is this for? If the answer keeps coming back to \"more for me,\" that's the drift. If the answer includes others, includes kingdom purposes, includes the next steward — that's the path."),
      h2("What a Good Harvest Is Actually For"),
      body("An abundant harvest, in biblical logic, is not primarily a personal windfall. It's an increase in stewardship responsibility. More to manage, yes — but more to deploy wisely, more to give, more to invest in things that outlast you."),
      body("The rich man's failure wasn't having a good harvest. It was the question he asked in response. The right question to ask when abundance comes isn't: how do I secure this? It's: what does God want done with this? And the answer almost always includes someone else."),
      spacer(80),
      pullQuote("When abundance comes, the first question isn't 'how do I keep this?' The first question is: 'what is this for?' That question keeps you from building bigger barns."),
      spacer(80),
    ]},
    { n:25, t:"Margin Means Peace", st:"The Practical Gift of Spending Less Than You Earn", tl:"Margin is not about having extra. It's about having space to be faithful.", scriptures:[{verse:"Dishonest money dwindles away, but whoever gathers money little by little makes it grow.", ref:"Proverbs 13:11 (NIV)"},{verse:"The wise store up choice food and olive oil, but fools gulp theirs down.", ref:"Proverbs 21:20 (NIV)"}], content:[
      body("There's a simple financial principle that sounds obvious and is rarely practiced:", {before:80}),
      body("Spend less than you earn. Consistently. Over time."),
      body("That's it. That's the foundation. And the gap between what you earn and what you spend — the margin — is what makes everything else possible."),
      h2("Why Margin Is a Spiritual Issue"),
      body("Margin is not just a financial concept. It's a posture. The person with margin has options the person without margin doesn't have. Margin is what lets you be generous when an opportunity comes unexpectedly. It's what prevents a crisis from becoming a catastrophe. It's what creates the space to make a wise decision rather than a desperate one."),
      body("Proverbs 21:20 contrasts the wise who store up and the fools who gulp everything down immediately. The word \"store\" isn't about greed — it's about stewarding the resource in a way that preserves options for the future. Building margin isn't hoarding. It's preparation."),
      h2("Building It Slowly"),
      body("Proverbs 13:11 says money gathered little by little grows. There's no shortcut here. The margin you build in the small, ordinary, unremarkable financial decisions of daily life is exactly the margin that's there when you need it. Every small act of spending less than you earn is a brick. Every brick is tiny. Over time, they become something."),
      body("For students: this isn't about having a perfect budget or making a certain amount. It's about the habit. Every time you leave something in the account rather than spending it, you're practicing. And the practice forms the person who will have real options later — including the option to be radically generous when the time comes."),
      spacer(80),
      pullQuote("Margin isn't about having extra. It's about having space — space to be faithful, space to be generous, space to make wise decisions when the pressure is on instead of desperate ones."),
      spacer(80),
    ]},
    { n:26, t:"Debt and Tomorrow", st:"When You Pre-Spend the Future", tl:"Debt isn't just a financial issue. It's a question about who controls your future.", scriptures:[{verse:"The rich rule over the poor, and the borrower is slave to the lender.", ref:"Proverbs 22:7 (NIV)"},{verse:"Let no debt remain outstanding, except the continuing debt to love one another.", ref:"Romans 13:8 (NIV)"}], content:[
      body("Proverbs 22:7 is one of those verses that's easy to nod at and hard to sit with: \"the borrower is slave to the lender.\"", {before:80}),
      body("Slave is a strong word. But it describes a real dynamic. When you borrow, you commit tomorrow's income to pay for today's decision. Which means tomorrow, when you get paid, someone else gets the first claim on what you earned. And the day after that. And the month after that."),
      body("The freedom debt is supposed to give you — access to something now rather than later — costs you a portion of your freedom going forward. Sometimes that's worth it. Often it isn't."),
      h2("The Student Debt Question"),
      body("Student loans are often framed as an investment — you're borrowing to build earning potential. That can be true. But it's worth asking the question Ron Blue used to ask clients about any borrowing: does taking on this debt make economic sense? Is the thing I'm borrowing for going to produce something that justifies the cost?"),
      body("Not every degree does. Not every car loan does. Not every buy-now-pay-later purchase does. The question isn't \"can I afford the monthly payment?\" The question is: \"does this decision make economic sense, and does it honor God with the stewardship he's entrusted to me?\""),
      h2("The Freedom of Owing Nothing"),
      body("Romans 13:8 says let no debt remain outstanding — except the debt to love one another. There's a vision here of financial freedom that isn't primarily about wealth. It's about owing nothing to anyone except the ongoing obligation to love. That freedom is worth working toward. Not as legalism, but as aspiration — as a picture of what faithful stewardship can look like over time."),
      body("The person who owes nothing has options that the person with debt doesn't. They can give more freely. They can make decisions based on calling rather than cash flow. They can respond when God opens a door without first asking whether the payment fits the budget."),
      spacer(80),
      pullQuote("Debt isn't a tool. It's a claim on your future. And every claim on your future is a reduction in your freedom to be faithful in that future when it arrives."),
      spacer(80),
    ]},
    { n:27, t:"Work as Worship", st:"What You Do Monday Through Friday Matters Eternally", tl:"The way you work is a statement about what you believe. Make it a true one.", scriptures:[{verse:"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters.", ref:"Colossians 3:23 (NIV)"},{verse:"For we are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.", ref:"Ephesians 2:10 (NIV)"}], content:[
      body("There's a trap a lot of students fall into around the idea of calling. They're waiting to find the thing — the career or vocation that feels meaningful enough to engage fully. And until they find it, work is something they do minimally, for money, until the real thing comes along.", {before:80}),
      body("Colossians 3:23 interrupts that waiting game directly. Whatever you do — not just the meaningful thing, not just the calling you're waiting for — do it with all your heart, as working for the Lord."),
      body("That means the part-time job that funds your education is not just a job. The chores nobody sees are not just chores. The homework nobody grades your character on is not just homework. All of it is worship, when it's done with the right orientation."),
      h2("Prepared in Advance"),
      body("Ephesians 2:10 says you were created to do good works which God prepared in advance for you. The work ahead of you — the ordinary, daily, sometimes-boring work — is not accidental. It was prepared. Which means it matters. Which means how you do it matters."),
      body("The student who works their current job with integrity, diligence, and genuine care for the people around them — who shows up on time, does more than required, treats their employer's resources like they're on loan from God — is not waiting for their real life to start. Their real life is already happening."),
      h2("The Witness of Work"),
      body("The way you work is one of the most visible forms of testimony you have. In most contexts, people will never ask you about your faith. But they will notice whether you work hard when no one's watching, whether you're trustworthy with small things, whether you bring genuine care to what you do."),
      body("That noticeability is an opportunity. Not to perform, but to be genuinely different — to work from a place of purpose rather than just paycheck."),
      spacer(80),
      pullQuote("The person who works hard and honestly at whatever they have right now is practicing the exact same faithfulness they'll need for the big decisions later. The classroom is open. You're already in it."),
      spacer(80),
    ]},
    { n:28, t:"The Steward's Questions", st:"A Week of Living Differently", tl:"You're not just managing money. You're managing a life. And the questions you ask determine what kind of life it becomes.", scriptures:[{verse:"His master replied, 'Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things.'", ref:"Matthew 25:21 (NIV)"},{verse:"Now it is required that those who have been given a trust must prove faithful.", ref:"1 Corinthians 4:2 (NIV)"}], content:[
      body("Three weeks in. Twenty-one days of returning to the same foundation from different directions.", {before:80}),
      body("Here's what a steward actually does with what they've learned — they take the questions into the ordinary day and let those questions do their slow, quiet work of formation."),
      body("Ron Blue watched thousands of people go through this kind of material. Some came back the next week changed — genuinely, visibly different in how they carried themselves around money. Others nodded at all the right moments and went home unchanged."),
      body("The difference between those two groups wasn't intelligence or spiritual maturity. It was whether they let the questions follow them into Tuesday."),
      h2("The Three Steward Questions"),
      body("For this week — and ideally for the rest of your financial life — here are the three questions worth asking before any significant financial decision:"),
      spacer(40),
      bul("Does this make economic sense? (Is this a wise use of what I've been given?)"),
      bul("Does this honor God? (Does this reflect who the Owner is and what he values?)"),
      bul("Does this serve others? (Does this decision account for people beyond just me?)"),
      spacer(60),
      body("Those three questions won't answer themselves. You have to bring the actual decision to them and sit there long enough to get an honest answer. But they're the questions that form a steward rather than just a financially literate person."),
      h2("Well Done"),
      body("Matthew 25:21 — \"well done, good and faithful servant\" — is one of the most motivating sentences in the Bible when you understand what it's not saying. It's not \"well done, successful servant.\" Not \"well done, wealthy servant.\" Not \"well done, servant who made excellent returns.\" It's faithful."),
      body("Faithful is available to anyone, at any income level, at any stage of life. It's available to the student with $40 in their account and to the executive with four million. The only question is whether you're doing what's yours to do, with what you've been given, in a way that honors the Owner."),
      body("That's the goal. And it starts again tomorrow morning."),
      spacer(80),
      pullQuote("Faithful is available to anyone at any income level. The only question is whether you're doing what's yours to do, with what you've been given, in a way that honors the Owner."),
      spacer(80),
    ]},
  ];
  return days;
}

function generateSession5() {
  const days = [
    { n:29, t:"God Gave First", st:"The Gospel Changes Everything About Generosity", tl:"Generosity doesn't start with what you have. It starts with what you've received.", scriptures:[{verse:"For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.", ref:"John 3:16 (NIV)"},{verse:"He who did not spare his own Son, but gave him up for us all — how will he not also, along with him, graciously give us all things?", ref:"Romans 8:32 (NIV)"}], content:[
      body("Every discussion of money and generosity in the Bible flows downstream from one fact: God gave first.", {before:80}),
      body("John 3:16 is often quoted as an evangelism verse — which it is. But it's also the foundation of the entire biblical vision for generosity. God loved. God gave. The giving came from the love. Not from surplus. Not from strategy. From love."),
      body("Romans 8:32 takes it further: if God didn't spare his own Son — the most precious thing imaginable — but gave him up for us, then how will he not also give us everything we need? The logic is astonishing: if the biggest gift has already been given, then everything else is downstream of that generosity."),
      h2("Generosity as Response"),
      body("This changes the shape of generosity entirely. Generosity that starts with obligation — \"I have to give because it's required\" — produces a specific kind of life. It produces the feeling of loss. Every dollar given is a dollar taken away from what could have been kept."),
      body("Generosity that starts with the gospel — \"I give because God gave first, because I've already received the greatest gift imaginable\" — produces a completely different kind of life. Giving becomes response. Not sacrifice. Response. You give because you've been given to in a way that changes everything else."),
      h2("Open Hands Follow an Open Heaven"),
      body("When you understand that the Owner of everything gave his most precious thing freely for you, holding your stuff tightly starts to seem not just unwise but almost absurd. If God can give that, you can give this."),
      body("This is the foundation underneath every conversation about generosity. Not guilt. Not duty. Not social pressure. The gospel — the fact that God gave first, extravagantly, personally, at the highest possible cost — is the engine that powers genuine generosity."),
      spacer(80),
      pullQuote("You don't give generously because you have extra. You give generously because you've received extravagantly. The gospel creates givers."),
      spacer(80),
    ]},
    { n:30, t:"Treasure and Heart", st:"Where Your Money Goes, Your Heart Goes Too", tl:"Giving isn't just about the money. It changes you.", scriptures:[{verse:"For where your treasure is, there your heart will be also.", ref:"Matthew 6:21 (NIV)"},{verse:"Sell your possessions and give to the poor. Provide purses for yourselves that will not wear out, a treasure in heaven that will never fail, where no thief comes near and no moth destroys. For where your treasure is, there your heart will be also.", ref:"Luke 12:33–34 (NIV)"}], content:[
      body("Matthew 6:21 has an order that matters. Not: where your heart is, there your treasure will follow. But: where your treasure is, your heart will follow.", {before:80}),
      body("Treasure leads. Heart follows."),
      body("This means you don't have to wait until you feel generous to give generously. You start giving, and over time, the giving trains the heart to be genuinely generous. You don't have to wait until you care about the poor to invest in the poor. You start investing, and the investment creates the care."),
      h2("The Redirecting Power of Giving"),
      body("Luke 12:33–34 tells you to give in order to build treasure in heaven — and then tells you that's where your heart will follow. This is Jesus giving you a practical tool for redirecting your deepest affections. You can't directly control what you love. But you can redirect your treasure, and the love follows."),
      body("This is why giving is not just a financial discipline. It's a heart formation discipline. Every time you give, you are training your heart to love something beyond yourself, beyond your immediate wants, beyond what you can see and hold. Over time, that training produces a person with a genuinely enlarged heart."),
      h2("The Smallest Gift That Costs Something"),
      body("The size of the gift isn't the primary variable. Whether it costs you something is. The widow's mite was tiny in absolute terms and significant in proportional terms — and Jesus specifically noticed it. The two coins that came from her poverty were doing more formation work than the large amounts that came from others' abundance."),
      body("The principle isn't give as much as possible. It's give in a way that requires trust. Give before you've guaranteed you'll be fine without it. Give in a way that actually moves your treasure in a direction — and trust your heart to follow."),
      spacer(80),
      pullQuote("You don't wait until you feel generous to start giving. You give first, and the giving trains the heart. Treasure leads; heart follows. That's not a warning — it's an invitation."),
      spacer(80),
    ]},
    { n:31, t:"Cheerful, Not Pressured", st:"The Kind of Giving That Actually Means Something", tl:"God doesn't need your money. He wants your heart. The giving is evidence.", scriptures:[{verse:"Each of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver.", ref:"2 Corinthians 9:7 (NIV)"},{verse:"All the believers were one in heart and mind. No one claimed that any of their possessions was their own, but they shared everything they had.", ref:"Acts 4:32 (NIV)"}], content:[
      body("One of the things Ron Blue noticed after decades in Christian financial practice was this: almost every conversation about giving was guilt-based.", {before:80}),
      body("The pitch was usually some version of: you should be giving more, here's why you're not, here's what you're missing out on if you don't. And some people responded to that pressure by giving more. But they were still giving reluctantly. Still giving under compulsion. Still experiencing giving as loss rather than response."),
      body("2 Corinthians 9:7 names exactly what God is actually after: a cheerful giver. Not a guilted giver. Not a socially pressured giver. Not someone who gives because they're afraid of what happens if they don't. Someone who gives because they genuinely want to. Because it flows from gratitude and delight rather than obligation."),
      h2("Decided in the Heart"),
      body("\"What you have decided in your heart to give.\" That phrase is doing a lot of work. The giving starts in the heart — in a genuine decision about what the Owner would want done with what he's entrusted to you — not in a sermon that made you feel bad."),
      body("Pre-commitment is the practical version of this: decide in advance, in a moment of clarity and prayer, what you're going to give. Then give it faithfully, regardless of how you feel in the moment. This protects you from both extremes — from never giving because the impulse never comes, and from giving chaotically based on emotional highs that you can't sustain."),
      h2("Acts 4 — A Different Economy"),
      body("Acts 4:32 describes the early church in a way that stopped everyone around them cold: nobody claimed that any possession was their own, but they shared everything. That's not communism or coercion. It's the natural result of a community of people who have genuinely settled the ownership question."),
      body("If everything belongs to God, and you belong to the same community as others who also live under God's ownership, then the line between \"mine\" and \"theirs\" becomes permeable in a way the culture around you cannot explain. That kind of generosity is not a financial product. It's a witness."),
      spacer(80),
      pullQuote("God doesn't need your money. He wants your heart. And the way you give is one of the clearest windows into where your heart actually is."),
      spacer(80),
    ]},
    { n:32, t:"First, Not Last", st:"Why Firstfruits Matters", tl:"Giving first is not a financial strategy. It is a declaration of trust.", scriptures:[{verse:"Honor the Lord with your wealth, with the firstfruits of all your crops.", ref:"Proverbs 3:9 (NIV)"},{verse:"On the first day of every week, each one of you should set aside a sum of money in keeping with your income.", ref:"1 Corinthians 16:2 (NIV)"}], content:[
      body("There's a reason the Bible is specific about when to give, not just how much.", {before:80}),
      body("Proverbs 3:9 says honor the Lord with the firstfruits — the first of the harvest, before you know how much will be left over. 1 Corinthians 16:2 says on the first day of every week, set aside what you're going to give. Not: give whatever is left at the end. First."),
      body("The order is the statement. Giving first says: God's priorities come before mine. Giving first says: I trust that what's left will be enough. Giving first says: I'm not a steward who gives God the leftovers after I've satisfied my own needs. Giving first is a declaration of trust in the Owner before you know exactly how the numbers will work out."),
      h2("The Student Version"),
      body("The firstfruits principle applies whether you have a full-time salary or a fifteen-dollar shift. When the paycheck comes in — or the birthday money, or the occasional gig payment — the first decision about what to do with it is: what does God want from this first? What goes to the kingdom before anything else gets allocated?"),
      body("Some traditions call this the tithe — ten percent. That's a useful starting point, not a ceiling. The question isn't what the minimum is. The question is what the Spirit is prompting, what the pattern of Scripture indicates, and what reflects genuine trust in the Owner."),
      h2("The Trust That First-Giving Builds"),
      body("There's a formation effect to first-giving that you can't get by giving last. Giving first forces you to trust before you see the result. It's the financial equivalent of seeking God's kingdom first — acting on faith before you know how it will work out."),
      body("The person who consistently gives first develops a different relationship with money than the person who gives whatever is left. They live with a different kind of freedom — the freedom of someone who has already made the most important decision and is now managing from a place of trust rather than anxiety."),
      spacer(80),
      pullQuote("Giving first is the financial version of Matthew 6:33. Before you know how it will work out, you put God's priorities first. And then you trust him with the rest."),
      spacer(80),
    ]},
    { n:33, t:"The Generous Life", st:"What Full-Surrender Generosity Actually Looks Like", tl:"Generosity isn't a financial category. It's a posture. A way of moving through the world.", scriptures:[{verse:"Whoever sows sparingly will also reap sparingly, and whoever sows generously will also reap generously.", ref:"2 Corinthians 9:6 (NIV)"},{verse:"The generous will themselves be blessed, for they share their food with the poor.", ref:"Proverbs 22:9 (NIV)"}], content:[
      body("There's a version of generosity that's calculated. You give a fixed percentage, on time, consistently. You hit the target. You move on.", {before:80}),
      body("That's good. It's genuinely better than not giving at all. But it's not the fullest version of the generous life."),
      body("The fullest version is the one where generosity has become a reflex rather than a discipline. Where the question \"should I give?\" has been replaced by \"what does God want me to do with this right now?\" Where giving feels less like releasing something and more like participating in something."),
      h2("Sowing and Reaping"),
      body("2 Corinthians 9:6 uses agricultural language: you reap what you sow. The sower who sows sparingly gets a sparse harvest. The sower who sows generously gets an abundant harvest. But the abundance isn't only financial — it's relational, spiritual, and often deeply practical in ways you couldn't have predicted."),
      body("The generous life produces something in the giver that the non-generous life can't produce. A different quality of relationship with money — lighter, freer, more open. A different quality of relationship with God — more intimate, more trusting. A different quality of life altogether."),
      h2("Whole-Life Generosity"),
      body("Money is the most obvious vehicle for generosity, but it's not the only one. Generosity shows up in how you spend your time, your attention, your encouragement, your skills, your presence. The generous person is the one who moves through the world looking for opportunities to give rather than to get — in every form that giving can take."),
      body("And the beautiful paradox of Proverbs 22:9 is that the generous are themselves blessed. Not as a transaction — give and receive. But as a reality: the open-handed life is a blessed life. Not always wealthier. Almost always richer in the things that matter most."),
      spacer(80),
      pullQuote("When generosity becomes a reflex rather than a discipline, something shifts. You stop asking 'should I give?' and start asking 'what does God want done with this?' That's the generous life."),
      spacer(80),
    ]},
    { n:34, t:"The Joy That Returns", st:"What Happens to a Giver Over Time", tl:"Joy is one of the most underrated fruits of a generous life.", scriptures:[{verse:"A generous person will prosper; whoever refreshes others will be refreshed.", ref:"Proverbs 11:25 (NIV)"},{verse:"And if you spend yourselves in behalf of the hungry and satisfy the needs of the oppressed, then your light will rise in the darkness, and your night will become like the noonday.", ref:"Isaiah 58:10 (NIV)"}], content:[
      body("Ron Blue has spent a lifetime watching what generosity does to people over time. And he says the same thing consistently: the most contented, most joyful people he has ever known were also the most generous.", {before:80}),
      body("Not always the wealthiest. The most generous."),
      body("This shouldn't be surprising, given what Scripture says about it. But it is surprising, because it runs counter to the financial anxiety that grips most people — the feeling that giving is loss, that the generous person is the one who ends up with less."),
      h2("Refreshed by Refreshing"),
      body("Proverbs 11:25 says whoever refreshes others will be refreshed. It's a law built into the way things work. The person who gives themselves to others — who spends energy on behalf of people who need it — doesn't end up depleted. They end up replenished. Not always immediately. Not always in the way expected. But the rhythm of giving out and being replenished is real."),
      body("This is one of those things that sounds impractical until you've experienced it. Then it becomes the most obvious thing in the world. Generosity creates capacity. Hoarding doesn't. The open-handed person is, over time, more energized by their life than the closed-fisted one."),
      h2("Light in the Darkness"),
      body("Isaiah 58:10 is a picture of what a generous life looks like from the outside: your light rises in the darkness. Your night becomes like noonday. This isn't primarily an individual benefit — it's a communal one. The generous life becomes a source of light for the people around it. A source of warmth. A source of hope."),
      body("In a culture this anxious about money, this status-obsessed, this comparison-driven — a genuinely generous person is conspicuous. Not because they make a show of it, but because what they're living by is different. And different is visible. And visible opens conversations."),
      spacer(80),
      pullQuote("The most contented people are almost always the most generous. Not because generosity produces wealth. But because generosity produces the kind of life that wealth was supposed to provide and almost never does."),
      spacer(80),
    ]},
    { n:35, t:"More Than Money", st:"Whole-Life Generosity and What It Builds", tl:"The generous life isn't just about what you give. It's about who you become.", scriptures:[{verse:"For we are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.", ref:"Ephesians 2:10 (NIV)"},{verse:"'It is more blessed to give than to receive.'", ref:"Acts 20:35 (NIV)"}], content:[
      body("There's a final picture worth sitting with as this session comes to a close.", {before:80}),
      body("Generosity — in its fullest expression — is not a financial category. It's a way of moving through the world. It includes money, yes. But it also includes time, energy, attention, presence, encouragement, skill, and love."),
      body("The generous person isn't just the one who writes the check. It's the one who gives their real attention to a friend who's struggling. Who shows up when nobody else does. Who uses their abilities to serve people who can't pay for it. Who shares their life, not just their resources."),
      h2("Prepared in Advance"),
      body("Ephesians 2:10 says you were created to do good works that God prepared in advance for you. The works were prepared before you arrived at the moment. Which means when the opportunity for generosity shows up — the friend who needs money, the stranger who needs encouragement, the community that needs your skill — it's not an interruption. It's the thing you were made for."),
      body("Living from that perspective changes how you experience your life. Every day becomes a landscape full of prepared moments. The question stops being \"what are my financial goals?\" and becomes \"what good works am I walking into today?\""),
      h2("The Blessed Life"),
      body("Acts 20:35 — \"it is more blessed to give than to receive\" — is one of the most counter-cultural statements in the Bible. It's also one of the most verifiable. You can test it. You can give generously for a month — your time, your money, your attention — and see what happens to your experience of your own life."),
      body("Almost universally, the people who try this discover that Jesus was right. The blessed life — the full, rich, genuinely good life — runs in the direction of generosity. The more you live open-handed, the more you find yourself in possession of exactly what you were looking for when you were living closed-fisted."),
      spacer(80),
      pullQuote("The generous life isn't just about what you give away. It's about who you become in the giving. And the person you become is, slowly, the person Jesus described: someone who is more blessed in the giving than they ever were in the receiving."),
      spacer(80),
    ]},
  ];
  return days;
}

function generateSession6() {
  const days = [
    { n:36, t:"Invest in What Lasts", st:"Treasure Has a Direction — Choose Wisely", tl:"You are investing in something right now. The only question is whether it's what you intend.", scriptures:[{verse:"Do not store up for yourselves treasures on earth, where moths and vermin destroy, and where thieves break in and steal. But store up for yourselves treasures in heaven.", ref:"Matthew 6:19–20 (NIV)"},{verse:"Set your minds on things above, not on earthly things.", ref:"Colossians 3:1–2 (NIV)"}], content:[
      body("Everything you own right now has a shelf life.", {before:80}),
      body("The phone will be obsolete in two years. The clothes will be out of style in less. The car will rust. The balance in the account is vulnerable to a thousand different contingencies. Everything in the \"earthly treasures\" category is temporary — not as a moral judgment, just as a fact about the nature of material things."),
      body("Matthew 6:19–20 isn't telling you to feel guilty about owning things. It's giving you accurate information about which categories of investment have staying power and which ones don't. Moths, rust, thieves — these are the vulnerabilities of earthly treasure. The heavenly category doesn't have those vulnerabilities."),
      h2("What 'Heavenly Treasure' Actually Means"),
      body("Heavenly treasure isn't a vague spiritual concept. It's a category of investment with specific content: people brought to faith, the poor cared for, the kingdom advanced, the next generation equipped, the truth passed on, love expressed in ways that outlast the moment."),
      body("Every dollar invested in a person's growth lasts longer than the dollar itself. Every hour given to a relationship that matters outlasts the convenience you gave up. Every act of generosity that costs you something sends a ripple further than you can see."),
      h2("Setting Your Mind"),
      body("Colossians 3:1–2 says set your mind on things above. This isn't a command to be impractical or to ignore the real world. It's a command about orientation — about which direction you're fundamentally pointed when you make decisions."),
      body("The person oriented toward earthly treasures makes decisions based on: what will this do for my comfort, my status, my security right now? The person oriented toward heavenly treasure asks: what will this look like in eternity? Which investment has staying power? Which use of this resource will I be glad I made?"),
      spacer(80),
      pullQuote("You are investing in something right now. Every day. The only question is whether what you're investing in will still be worth something when the things that seem permanent have turned out not to be."),
      spacer(80),
    ]},
    { n:37, t:"Decided Before the Pressure", st:"Pre-Commitment as a Spiritual Discipline", tl:"The best decisions are made before the pressure to decide arrives.", scriptures:[{verse:"But Daniel resolved not to defile himself with the royal food and wine, and he asked the chief official for permission not to defile himself this way.", ref:"Daniel 1:8 (NIV)"},{verse:"I have hidden your word in my heart that I might not sin against you.", ref:"Psalm 119:11 (NIV)"}], content:[
      body("Daniel's story in the first chapter of his book is easy to overlook, but it contains one of the most practically useful things the Bible says about decision-making:", {before:80}),
      body("He resolved before the pressure arrived."),
      body("He didn't wait until the king's food was in front of him and then try to summon the willpower to say no in the moment. He made the decision in advance — when the stakes were lower, the pressure was less, and his mind was clear. By the time the food arrived, the decision was already made."),
      h2("Pre-Commitment in Financial Life"),
      body("Pre-commitment is one of the most powerful tools in financial stewardship. You decide — before the impulse, before the sale, before the social pressure, before the rationalization — what you're going to give, save, and spend. And then you let the decision you made in your clearest moment run your behavior rather than the feeling you have in the moment."),
      body("This is how consistent givers stay consistent — they committed before the month got complicated. This is how people stay out of debt — they decided what they'd borrow before they wanted something they couldn't afford. This is how people build margin — they decided to save first before they planned what to spend."),
      h2("The Word Hidden in the Heart"),
      body("Psalm 119:11 says \"I have hidden your word in my heart that I might not sin against you.\" The hiding happens in advance — in the quiet moments, in the discipline of memorization and meditation. And then, in the moment of pressure, what's been hidden surfaces as a resource."),
      body("The principle transfers directly: the convictions you form in the clear, quiet moments — about what you will and won't do with what God entrusts to you — are the convictions that will run your decisions in the pressured moments. Put them in place now."),
      spacer(80),
      pullQuote("The best version of you shows up in the hard moment if the best version of you made the decision before the hard moment arrived. Pre-commitment is how you ensure your clearest self runs your life."),
      spacer(80),
    ]},
    { n:38, t:"Your Sphere of Influence", st:"Impact Starts Closer Than You Think", tl:"You don't have to change the world to be faithful. You have to be faithful in your world.", scriptures:[{verse:"Anyone who does not provide for their relatives, and especially for their own household, has denied the faith and is worse than an unbeliever.", ref:"1 Timothy 5:8 (NIV)"},{verse:"Therefore, as we have opportunity, let us do good to all people, especially to those who belong to the family of believers.", ref:"Galatians 6:10 (NIV)"}], content:[
      body("There's a certain kind of generosity daydream that students fall into. It goes like this: someday, when I have real money, I'm going to do something significant. Fund a nonprofit. Support a missionary. Change something large.", {before:80}),
      body("That's a good dream. But it can become an excuse — a way of delaying faithfulness in the current sphere until you have the resources to be faithful in a bigger one."),
      body("1 Timothy 5:8 doesn't start with the large sphere. It starts at home — with the people closest to you. Those you are actually responsible for. Your family. Your household. Your immediate circle. The generosity that proves itself on a large scale is almost always the generosity that started with genuine faithfulness in the small, near, ordinary sphere."),
      h2("Your Current Sphere"),
      body("Galatians 6:10 says: as we have opportunity, do good to all — especially to those in the family of believers. \"As we have opportunity\" is the operative phrase. You don't have to manufacture opportunities. You have them right now. In your current school, neighborhood, friend group, family. People who need encouragement. People who are struggling financially. People who would be significantly helped by what you could give right now."),
      body("The person faithful in their current sphere is building the person who will be faithful in a larger one. The student who gives what they have now to the people in their actual life is practicing exactly the kind of generosity they'll need later. The practice is what matters — not the amount."),
      h2("Impact in the Ordinary"),
      body("Impact doesn't require a platform. It requires presence. The friend who shows up consistently, who gives their real attention, who uses what they have to serve the people actually around them — that person is having impact. Not visible impact, perhaps. Not quantifiable impact. But the kind that changes lives in ways you'll never fully know."),
      body("Start there. Be faithful there. Let that faithfulness be the foundation of everything larger that comes later."),
      spacer(80),
      pullQuote("The question isn't whether you're doing something significant enough. The question is whether you're faithful in your actual sphere — the people in front of you, with what you have, right now."),
      spacer(80),
    ]},
    { n:39, t:"The Mark You Leave", st:"Legacy Is Not About What You Accumulate — It's About What You Pass On", tl:"The most important inheritance isn't financial. It's the values and faith that live in the people who came after you.", scriptures:[{verse:"By faith Moses, when he had grown up, refused to be known as the son of Pharaoh's daughter. He chose to be mistreated along with the people of God rather than to enjoy the fleeting pleasures of sin. He regarded disgrace for the sake of Christ as of greater value than the treasures of Egypt.", ref:"Hebrews 11:24–26 (NIV)"},{verse:"Command those who are rich in this present world not to be arrogant nor to put their hope in wealth, which is so uncertain, but to put their hope in God, who richly provides us with everything for our enjoyment.", ref:"1 Timothy 6:17 (NIV)"}], content:[
      body("Moses gave up something that most people spend their whole lives chasing. He had the identity of Pharaoh's daughter's son — access, security, status at the highest level of the most powerful civilization on earth. And he walked away from it.", {before:80}),
      body("Hebrews 11 says he regarded the disgrace of being identified with God's people as more valuable than the treasures of Egypt. That's an extraordinary valuation. Not because Egypt's treasures weren't real. But because he had a different frame for what real wealth looks like."),
      body("He saw further than the present. He weighed what was lasting against what was temporary. And the lasting thing won."),
      h2("What You're Building Right Now"),
      body("You are building a legacy right now. Not in the future when you have significant wealth. Right now — in the choices you make about how to use what you have, in the values you're forming, in the posture you're developing toward money and possessions and generosity."),
      body("The legacy isn't primarily financial. The most valuable legacies are always the values, the faith, the patterns of living that outlast the money — that get passed to the people who come after you. The parent who models faithful stewardship gives their children something more valuable than any inheritance. The friend who models genuine contentment gives the people watching them a picture of something that can't be bought."),
      h2("Hope in God, Not Wealth"),
      body("1 Timothy 6:17 says don't put your hope in wealth — which is uncertain — but in God, who richly provides everything for enjoyment. The uncertainty of wealth isn't pessimism. It's realism. Markets change. Economies shift. The things that seem permanent turn out not to be. But God doesn't change. And a life built on hope in him rather than hope in accumulated assets is a life that holds when the uncertain things move."),
      body("That's the legacy worth leaving. And it starts right now — in the decisions you're making about what to trust, what to hold, and what to release."),
      spacer(80),
      pullQuote("Moses chose the lasting thing over the impressive thing. That decision defined everything that came after. You're making the same kind of decision — one ordinary choice at a time."),
      spacer(80),
    ]},
    { n:40, t:"Different, Not Better", st:"The Life the World Is Watching", tl:"Your most powerful financial witness is not what you say. It is the life you actually live.", scriptures:[{verse:"You are the light of the world. A town built on a hill cannot be hidden. Neither do people light a lamp and put it under a bowl. Instead they put it on its stand, and it gives light to everyone in the house.", ref:"Matthew 5:14–15 (NIV)"},{verse:"So in everything, do to others what you would have them do to you.", ref:"Matthew 7:12 (NIV)"}], content:[
      body("Forty days of the same foundation, from forty different directions.", {before:80}),
      body("Here's what Ron Blue has consistently observed in the people who actually live this — who come back to the ownership question every day, who hold what they have with open hands, who practice contentment and give generously and seek God's kingdom first:"),
      body("They are genuinely, visibly, surprisingly different."),
      body("Not better. Not wealthier. Not more disciplined, necessarily. But different in a way that the culture around them notices and cannot fully explain."),
      h2("What Different Looks Like"),
      body("The student whose sense of self doesn't rise and fall with their account balance. The young person who gives generously when it doesn't make mathematical sense. The one who is genuinely okay with what they have while everyone around them is restless for more. The friend who doesn't spiral when something financial goes wrong — who is steady in a way that requires explanation."),
      body("Matthew 5:14 calls you the light of the world. A town on a hill can't be hidden. The life you live — the actual, daily, financial decisions you make and the posture you carry them with — is visible. And visible lives open conversations that nothing else opens."),
      h2("The Practice Continues"),
      body("These forty days are not a graduation. They're an introduction to a practice that continues for the rest of your life. You will drift. You will grip things you should hold loosely. You will sit in the first chair sometimes. You will compare and worry and reach for the wrong things."),
      body("The goal was never perfection. The goal was a new default — a foundation to return to, a question to keep asking, a posture to keep practicing. And the practice of returning, day after day, is what builds the person who is genuinely, visibly, surprisingly different."),
      body("Different, not better. But unmistakably, inexplicably, beautifully different."),
      spacer(80),
      pullQuote("The ownership question — who really owns this? — is not a question you answer once. It's the question that shapes every day. And the person who keeps answering it honestly, day after day, becomes someone the world around them cannot quite explain."),
      spacer(80),
    ]},
    { n:41, t:"The Church as a Generous Body", st:"What Happens When a Whole Community Lives This Way", tl:"Individual stewardship is powerful. Collective stewardship is transformational.", scriptures:[{verse:"All the believers were together and had everything in common. They sold property and possessions to give to anyone who had need.", ref:"Acts 2:44–45 (NIV)"},{verse:"And God is able to bless you abundantly, so that in all things at all times, having all that you need, you will abound in every good work.", ref:"2 Corinthians 9:8 (NIV)"}], content:[
      body("The early church in Acts 2 was not a collection of individuals who happened to share a belief system. It was a community whose shared conviction — everything belongs to God — had changed the way they related to everything they owned.", {before:80}),
      body("They were together. They had things in common. They sold property to give to those with need. None of them claimed exclusive rights to what they had — because they had genuinely, collectively, answered the ownership question and let the answer run their common life."),
      body("The result was a community that the world around it could not explain — and could not ignore."),
      h2("What You're Part Of"),
      body("You are not practicing stewardship in isolation. You are part of a body — a community of people who are all, in theory, answering the same ownership question. And when that community actually lives from a shared foundation of God's ownership, the collective impact is staggering."),
      body("Mark Wilson put it this way: \"If you get 'God owns it all' in your heart, it changes your family. It ripples into your community, your church, and beyond. If the church truly believed God owns it all, we could do far more than any government program ever could.\""),
      h2("Your Contribution to the Collective"),
      body("The community's collective faithfulness is made up of individual faithfulness — yours included. Your decision to live differently, to give generously, to hold things with open hands, contributes to the culture of the whole body. You are either contributing to a community of open hands or a community of closed fists, by how you live."),
      body("2 Corinthians 9:8 says God is able to make all grace abound toward you — so that, having all that you need, you will abound in every good work. The abundance isn't for accumulation. It's to enable good work. For you. Through you. To the world around you and beyond."),
      spacer(80),
      pullQuote("Your individual faithfulness isn't just about you. It ripples. Into your family, your community, your church. And the church that genuinely believes God owns it all can do things the world will not be able to explain."),
      spacer(80),
    ]},
    { n:42, t:"Start Again Tomorrow", st:"The Devotional Ends. The Practice Doesn't.", tl:"Stewardship isn't a 42-day course. It's a lifelong posture. Today is a good day to begin again.", scriptures:[{verse:"Now to him who is able to do immeasurably more than all we ask or imagine, according to his power that is at work within us, to him be glory in the church and in Christ Jesus throughout all generations, for ever and ever! Amen.", ref:"Ephesians 3:20–21 (NIV)"},{verse:"The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you; the Lord turn his face toward you and give you peace.", ref:"Numbers 6:24–26 (NIV)"}], content:[
      body("Forty-two days. And tomorrow you wake up and start again.", {before:80}),
      body("Not because you failed. Not because the forty-two days weren't enough. But because stewardship is not a course with a graduation. It's a posture you carry every day — a way of answering the ownership question in the morning, before the day runs off in a dozen different directions."),
      body("The foundation you've been building over these six weeks doesn't complete itself on day forty-two. It becomes the floor of the rest of your life. Every decision you make for the rest of your life will be made either from this foundation — or from the alternative one the culture will constantly offer you."),
      h2("More Than You Can Ask or Imagine"),
      body("Ephesians 3:20–21 closes with one of the great benedictions: God is able to do immeasurably more than all we ask or imagine, according to his power at work within us."),
      body("That phrase — within us — is the key. The power isn't external. It's not a lucky windfall or a market moving favorably. It's the transformative work of God in a person who has genuinely submitted their financial life to his ownership. The immeasurably-more is what happens in the long run to a person who keeps returning to the foundation, keeps holding things with open hands, keeps being faithful in the small things."),
      body("You don't know what your life will look like from this foundation in ten, twenty, forty years. But you can look at the people who've lived it — people like the physician who parked down the street, or the CEO who chose the trailer park, or Adam Wilson who grew up earning and saving and giving — and you can see: it produces something. Something genuine. Something free. Something the world around it cannot explain."),
      h2("The Blessing"),
      body("The oldest blessing in Scripture — Numbers 6:24–26 — is worth receiving as you close:"),
      body("The Lord bless you and keep you. May his face shine on you. May he be gracious to you. May he turn his face toward you and give you peace."),
      body("Not wealth. Not status. Not financial security as the world measures it. Peace. The peace of a person who knows who holds them, who knows who owns what they're managing, who knows that faithful is enough — because faithful is exactly what the Master called good."),
      body("Go be faithful. Be different. Be genuinely, quietly, unexplainably free."),
      spacer(80),
      pullQuote("Day 43 is just day 1 again — the same question, the same foundation, the same return. God owns it. You steward it. Faithful is enough. Start again tomorrow."),
      spacer(80),
    ]},
  ];
  return days;
}

// Build day content from template
function buildDay(dayData) {
  const { n, t, st, tl, scriptures, content } = dayData;
  return [
    ...dayHeader(n, t, st, tl, scriptures),
    ...content,
    spacer(100),
    sectionLabel("Think About It"),
    // Generic think-about-its based on session content
    body("Looking at today's passage — what's the most uncomfortable part? What does that discomfort reveal about where you are right now?"),
    spacer(40),
    body("If someone who knew you well read today's devotional, what specific area of your life would they say it speaks to most directly? Are they right?"),
    spacer(40),
    sectionLabel("Exercises"),
    fillIn(1, "The part of today that hits closest to home is:"),
    fillIn(2, "One thing I want to do differently this week because of what I read:"),
    fillIn(3, "A question I want to bring to God in prayer today:"),
    spacer(80),
    declarationBox("Father, you are the Owner. I am your steward. Teach me today. Form me through this. I want to be genuinely different — not better, different — because of whose I am. Amen."),
    spacer(80),
    ...nextSteps(
      "Take five minutes today to sit with the key question from this devotional. Write one honest sentence in response.",
      "Choose one small financial decision today and bring the ownership question to it before you decide.",
      "Share one thing from today's reading with someone who would understand it. Ask them: 'Is this true of me? Am I living this?'"
    ),
    spacer(80),
    ...closingPrayer("Father, you are steady and you do not change. Thank you for this day, for this Word, for the slow, patient work of forming me into someone who holds what they have with open hands and trusts you with what they can't control. Give me wisdom for what is mine to do, and peace for what is not. Amen."),
    pb(),
  ];
}

// ============================================================
// SMALL GROUP CURRICULUM (6 sessions)
// ============================================================

function smallGroupSession(num, title, subtitle, bigIdea, scripture, devoDays, icebreaker, videoNote, discussionQ, challenge, parentNote) {
  return [
    new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [9360],
      borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder, insideH: noBorder, insideV: noBorder },
      rows: [new TableRow({ children: [new TableCell({
        width: { size: 9360, type: WidthType.DXA },
        shading: { fill: NAVY, type: ShadingType.CLEAR },
        margins: { top: 320, bottom: 320, left: 480, right: 480 },
        borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
        children: [
          new Paragraph({ spacing: sp(0, 60), children: [new TextRun({ text: `SESSION ${num}  ·  SMALL GROUP GUIDE`, size: 18, color: GOLD, bold: true, font: "Arial" })] }),
          new Paragraph({ spacing: sp(0, 60), children: [new TextRun({ text: title, size: 44, bold: true, color: WHITE, font: "Arial" })] }),
          new Paragraph({ spacing: sp(0, 80), children: [new TextRun({ text: subtitle, size: 24, italics: true, color: "C8D8E8", font: "Arial" })] }),
          new Paragraph({ spacing: sp(60, 20), children: [new TextRun({ text: "BIG IDEA: ", size: 18, bold: true, color: GOLD, font: "Arial" }), new TextRun({ text: bigIdea, size: 18, color: WHITE, font: "Arial" })] }),
          new Paragraph({ spacing: sp(10, 0), children: [new TextRun({ text: "DEVOTIONALS: ", size: 18, bold: true, color: GOLD, font: "Arial" }), new TextRun({ text: devoDays, size: 18, color: "A8C0D8", font: "Arial" })] }),
        ]
      })]})],
    }),
    spacer(120),

    callout([
      new Paragraph({ spacing: sp(0,60), children: [new TextRun({ text: "KEY SCRIPTURE", bold: true, size: 18, color: NAVY, font: "Arial" })] }),
      new Paragraph({ spacing: sp(0,20), children: [new TextRun({ text: `"${scripture.verse}"`, italics: true, size: 22, color: DARK, font: "Arial" })] }),
      new Paragraph({ spacing: sp(0,0), children: [new TextRun({ text: `— ${scripture.ref}`, bold: true, size: 20, color: GOLD, font: "Arial" })] }),
    ], LIGHT_BLUE, NAVY),
    spacer(80),

    sectionLabel("Session Flow (60–75 minutes)"),
    new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [1440, 2200, 5720],
      borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder, insideH: noBorder, insideV: noBorder },
      rows: [
        ["10 min", "Icebreaker", icebreaker],
        ["3 min", "Story Video", videoNote],
        ["10 min", "Teaching", `Teaching content drawn from Days ${devoDays} of the student devotional. Youth pastor delivers 8–10 minutes building from the student story to the week's theological core.`],
        ["20 min", "Discussion", "See discussion questions below."],
        ["8 min", "Challenge + Prayer", `Live-It-Out Challenge (below) + closing declaration together.`],
      ].map(([time, label, detail], i) => new TableRow({ children: [
        new TableCell({ width:{size:1440,type:WidthType.DXA}, shading:{fill:i%2===0?NAVY:"2A4F78",type:ShadingType.CLEAR}, borders:{top:noBorder,bottom:noBorder,left:noBorder,right:noBorder}, margins:{top:100,bottom:100,left:120,right:120}, children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:time,size:18,color:GOLD,bold:true,font:"Arial"})]})] }),
        new TableCell({ width:{size:2200,type:WidthType.DXA}, shading:{fill:i%2===0?LIGHT_BLUE:"EEF4FA",type:ShadingType.CLEAR}, borders:{top:noBorder,bottom:noBorder,left:noBorder,right:noBorder}, margins:{top:100,bottom:100,left:120,right:120}, children:[new Paragraph({children:[new TextRun({text:label,size:20,bold:true,color:NAVY,font:"Arial"})]})] }),
        new TableCell({ width:{size:5720,type:WidthType.DXA}, shading:{fill:i%2===0?LIGHT_GRAY:WHITE,type:ShadingType.CLEAR}, borders:{top:noBorder,bottom:noBorder,left:noBorder,right:noBorder}, margins:{top:100,bottom:100,left:120,right:120}, children:[new Paragraph({children:[new TextRun({text:detail,size:20,color:DARK,font:"Arial"})]})] }),
      ]}))
    }),
    spacer(100),

    sectionLabel("Discussion Questions"),
    body("Choose 3–4. Let the conversation breathe. Don't rush to the next question."),
    spacer(40),
    ...discussionQ.map((q, i) => callout([new Paragraph({spacing:sp(20,20),children:[new TextRun({text:`${i+1}.  ${q}`,size:22,color:DARK,font:"Arial"})]})], i%2===0?LIGHT_BLUE:LIGHT_GOLD, i%2===0?NAVY:GOLD)),
    spacer(100),

    sectionLabel("Live-It-Out Challenge"),
    callout([body(challenge)], LIGHT_TEAL, TEAL),
    spacer(80),

    sectionLabel("Parent Guide — This Week"),
    callout([
      new Paragraph({spacing:sp(0,40),children:[new TextRun({text:"What your student is learning:",bold:true,size:22,color:NAVY,font:"Arial"})]}),
      new Paragraph({spacing:sp(0,60),children:[new TextRun({text:parentNote.summary,size:22,color:DARK,font:"Arial"})]}),
      new Paragraph({spacing:sp(0,40),children:[new TextRun({text:"One question for dinner:",bold:true,size:22,color:NAVY,font:"Arial"})]}),
      new Paragraph({spacing:sp(0,60),children:[new TextRun({text:`"${parentNote.question}"`,italics:true,size:22,color:DARK,font:"Arial"})]}),
      new Paragraph({spacing:sp(0,40),children:[new TextRun({text:"One family action:",bold:true,size:22,color:NAVY,font:"Arial"})]}),
      new Paragraph({spacing:sp(0,60),children:[new TextRun({text:parentNote.action,size:22,color:DARK,font:"Arial"})]}),
      new Paragraph({spacing:sp(0,40),children:[new TextRun({text:"Prayer:",bold:true,size:22,color:NAVY,font:"Arial"})]}),
      new Paragraph({spacing:sp(0,20),children:[new TextRun({text:parentNote.prayer,italics:true,size:22,color:DARK,font:"Arial"})]}),
    ], LIGHT_GOLD, GOLD),
    pb(),
  ];
}

// ============================================================
// ASSEMBLE THE DOCUMENT
// ============================================================

// Cover
const coverPage = [
  spacer(1440),
  new Table({
    width:{size:9360,type:WidthType.DXA},columnWidths:[9360],
    borders:{top:noBorder,bottom:noBorder,left:noBorder,right:noBorder,insideH:noBorder,insideV:noBorder},
    rows:[new TableRow({children:[new TableCell({
      width:{size:9360,type:WidthType.DXA},shading:{fill:NAVY,type:ShadingType.CLEAR},
      margins:{top:720,bottom:720,left:720,right:720},
      borders:{top:noBorder,bottom:noBorder,left:noBorder,right:noBorder},
      children:[
        new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(0,80),children:[new TextRun({text:"GOD OWNS IT ALL",size:72,bold:true,color:WHITE,font:"Arial"})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(0,120),children:[new TextRun({text:"Youth Edition",size:40,color:GOLD,italics:true,font:"Arial"})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(0,80),children:[new TextRun({text:"42 Daily Devotionals + 6-Session Small Group Guide",size:26,color:"C8D8E8",font:"Arial"})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(120,0),children:[new TextRun({text:"Based on the Teaching of Ron Blue  ·  Ron Blue Institute",size:22,color:"A8C0D8",font:"Arial"})]}),
      ]
    })]})],
  }),
  spacer(240),
  callout([new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(40,40),children:[new TextRun({text:'"The earth is the Lord\'s, and everything in it." — Psalm 24:1',size:24,italics:true,color:NAVY,font:"Arial"})]})], LIGHT_GOLD, GOLD),
  spacer(360),
  new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(0,40),children:[new TextRun({text:"For Middle School & High School Students",size:22,color:MID_GRAY,font:"Arial"})]}),
  new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(0,0),children:[new TextRun({text:"Designed to run alongside the God Owns It All 40-Day Adult Devotional",size:20,color:MID_GRAY,font:"Arial"})]}),
  pb(),
];

// How to Use This Book
const howToUse = [
  h1("How to Use This Book"),
  divider(),
  spacer(80),
  body("This book contains two things: 42 daily devotionals and a 6-session small group guide. They're designed to work together — the daily reading builds the foundation, and the weekly group experience makes it communal."),
  spacer(60),

  h2("The Daily Devotionals"),
  body("Each devotional is built for 10–15 minutes of daily reading. It follows the same structure every day:"),
  spacer(40),
  bul("Today's Verses — the Scripture anchor for the day"),
  bul("A story or real-life scenario that opens the concept"),
  bul("2–3 teaching sections that develop the idea"),
  bul("A pull quote — the core idea in one sentence"),
  bul("Think About It — 2 questions to sit with"),
  bul("Exercises — short, honest written responses"),
  bul("A declaration to write and mean"),
  bul("Next Steps — three options, pick one"),
  bul("A closing prayer"),
  spacer(60),
  body("The exercises have fill-in lines. Use them. Write short, honest answers — not what sounds right, what's actually true. The formation happens in the honest answer, not the impressive one."),
  spacer(80),

  h2("The Small Group Guide"),
  body("The 6-session guide is designed for a weekly group experience — midweek youth group, Sunday morning class, or small group setting. Each session runs 60–75 minutes and includes a flow guide, discussion questions, a Live-It-Out challenge, and a parent guide."),
  spacer(40),
  body("Sessions align with the devotional sessions:"),
  spacer(40),
  bul("Session 1 = Days 1–7"),
  bul("Session 2 = Days 8–14"),
  bul("Session 3 = Days 15–21"),
  bul("Session 4 = Days 22–28"),
  bul("Session 5 = Days 29–35"),
  bul("Session 6 = Days 36–42"),
  spacer(80),

  h2("The Big Question"),
  callout([
    new Paragraph({spacing:sp(20,20),children:[new TextRun({text:"Every day asks the same question from a different angle:", size:22, color:DARK, font:"Arial"})]}),
    new Paragraph({spacing:sp(20,20),children:[new TextRun({text:"Who owns this?", bold:true, size:32, color:NAVY, font:"Arial"})]}),
    new Paragraph({spacing:sp(20,20),children:[new TextRun({text:"Answer it honestly, and everything else follows. The goal isn't financial expertise. It's a different kind of person — one who holds what they have with open hands, trusts the Owner with what they can't control, and is genuinely, visibly different because of whose they are.", size:22, color:DARK, font:"Arial"})]}),
  ], LIGHT_BLUE, NAVY),
  pb(),
];

// Session covers and content
const allSessions = [
  // Session 1
  ...sessionCover("1", "Who's Really in Charge?", "The Ownership Question", "God's ownership is the place your heart can finally stop running.", "Days 1–7"),
  ...s1d1(), ...s1d2(), ...s1d3(), ...s1d4(), ...s1d5(), ...s1d6(), ...s1d7(),

  // Session 2
  ...sessionCover("2", "Mine Is Not a Safe Word", "Identity & Belonging", "The thing you're trying to earn with what you own — you already have it.", "Days 8–14"),
  ...s2d1(), ...s2d2(), ...s2d3(), ...s2d4(), ...s2d5(), ...s2d6(), ...s2d7(),

  // Sessions 3-6: use template days
  ...sessionCover("3", "Your Money Has a Record", "Tool. Test. Testimony.", "Your trust shows up in your choices, not your intentions.", "Days 15–21"),
  ...generateSession3().map(buildDay).flat(),

  ...sessionCover("4", "What Faithful Looks Like", "Stewardship in Real Life", "You don't achieve stewardship. You practice it. Every single day.", "Days 22–28"),
  ...generateSession4().map(buildDay).flat(),

  ...sessionCover("5", "Enough Is a Spiritual Word", "Contentment vs. Culture", "You don't find contentment when you finally have enough. You discover it when you stop making enough the point.", "Days 29–35"),
  ...generateSession5().map(buildDay).flat(),

  ...sessionCover("6", "Open Hands", "Generosity & Who You're Becoming", "The generous life isn't just about what you give away. It's about who you become in the giving.", "Days 36–42"),
  ...generateSession6().map(buildDay).flat(),
];

// Small group sessions
const smallGroupGuide = [
  new Table({
    width:{size:9360,type:WidthType.DXA},columnWidths:[9360],
    borders:{top:noBorder,bottom:noBorder,left:noBorder,right:noBorder,insideH:noBorder,insideV:noBorder},
    rows:[new TableRow({children:[new TableCell({
      width:{size:9360,type:WidthType.DXA},shading:{fill:NAVY,type:ShadingType.CLEAR},
      margins:{top:480,bottom:480,left:560,right:560},
      borders:{top:noBorder,bottom:noBorder,left:noBorder,right:noBorder},
      children:[
        new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(0,80),children:[new TextRun({text:"SMALL GROUP GUIDE",size:52,bold:true,color:WHITE,font:"Arial"})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(0,80),children:[new TextRun({text:"6 Sessions for Weekly Group Use",size:28,italics:true,color:GOLD,font:"Arial"})]}),
        new Paragraph({alignment:AlignmentType.CENTER,spacing:sp(80,0),children:[new TextRun({text:"For Midweek Youth Night · Sunday Morning · Small Group",size:22,color:"A8C0D8",font:"Arial"})]}),
      ]
    })]})],
  }),
  pb(),

  ...smallGroupSession(1, "Who's Really in Charge?", "The Ownership Question",
    "God's ownership is where your heart can finally stop running.",
    {verse:"The earth is the Lord's, and everything in it, the world, and all who live in it.", ref:"Psalm 24:1 (NIV)"},
    "Days 1–7",
    "The Ownership Game: Give two students identical objects. One 'owns' it, one is 'borrowing' it for the night. At the end, the owner asks for it back. What's the difference between how you treated it? Debrief together: what changes when something is borrowed vs. owned? That's the entire session in one object lesson.",
    "Student Story: The Second-Generation Steward. 'We weren't given allowance. We earned. We saved 10 percent, gave 10 percent, lived on the rest. It wasn't optional. It was obedience.' Plays cold — no introduction from the leader.",
    [
      "When something financial goes wrong in your family — or your own money runs out — what's your first internal move? What do you reach for?",
      "The three wrong questions (Will I be successful? Significant? Secure?) assume you're the one responsible for the answers. What would actually change in your daily life if you genuinely believed you weren't?",
      "What's the difference between responsibility and control? Can you give an example of each from your own life?",
      "If God is the actual Owner, what changes about your role? Does that feel like relief or restriction — and why?",
      "Think of someone you know who handles what they have with genuine peace. What is it about the way they carry themselves? What do you think they believe that you don't yet?",
    ],
    "Before every purchase this week — anything — pause ten seconds and ask: 'God, you're the Owner. What does faithful look like here?' Don't change what you do. Just ask the question. Come back next week with a report.",
    {
      summary: "This week your student is asking the foundational question underneath all of Ron Blue's financial teaching: who actually owns what we have? The answer — that God owns everything and we are stewards, not owners — changes how we carry money, stuff, and the future.",
      question: "When something goes wrong financially in our family — an unexpected bill, a tight month — what do you think our first reaction says about what we actually trust?",
      action: "Before any purchase this week, pause together and ask: 'Is this how the Owner would want this used?' Try it once. Report back.",
      prayer: "Father, you are the Owner of everything we have. Teach our family to hold it with open hands. Amen.",
    }
  ),

  ...smallGroupSession(2, "Mine Is Not a Safe Word", "Identity & Belonging",
    "The thing you're trying to earn with what you own — you already have it.",
    {verse:"Fear not, for I have redeemed you; I have called you by name, you are mine.", ref:"Isaiah 43:1 (ESV)"},
    "Days 8–14",
    "The Status Reveal: Each person writes anonymously on a card: one thing you own (or want) that you'd be embarrassed to lose in front of your friends. Collect all cards, shuffle, read them aloud. Don't reveal who wrote what. Debrief: why would losing it be embarrassing? What is it actually standing for?",
    "Student Story: The Small Thing That Was Actually Big. A student with birthday money, a friend who needed it, an internal fight that lasted all day. The moment they gave some of it — and what shifted afterward.",
    [
      "Is there something you own — or want to own — that is partly about what it signals to other people? What story is it supposed to tell?",
      "The 'mine' trap: when does 'mine' go from being a description (I'm responsible for this) to being an identity (this is part of who I am)? Can you give an example?",
      "When you think about losing something you currently have — possessions, status, a social position — what's the first emotion? What does that reaction reveal?",
      "Isaiah 43:1 says God has called you by name and you belong to him. Does that feel like a shelter to you, or does it feel abstract? What would it take for it to feel real?",
      "Paul called his status credentials 'loss' compared to knowing Christ. Is there anything in your life you've been treating as gain that might actually be costing you something?",
    ],
    "This week: write five things you have that you didn't create — an ability, a relationship, an open door, your health, a season God brought you through. Say one of them out loud before you go to sleep every night. Report back on what changed.",
    {
      summary: "This week your student is exploring how what we own can quietly become what defines us — and why that's a trap. They're also hearing about God's ownership as personal and loving: 'I have called you by name, you are mine.'",
      question: "Is there something our family treats as part of our identity — our neighborhood, our stuff, our standard of living — that we'd feel more than just inconvenienced to lose?",
      action: "Name one thing together that you have but didn't create. Thank God for it specifically.",
      prayer: "God, we belong to you. Help us find our security in that, not in what we own. Amen.",
    }
  ),

  ...smallGroupSession(3, "Your Money Has a Record", "Tool. Test. Testimony.",
    "Your trust shows up in your choices, not your intentions.",
    {verse:"For where your treasure is, there your heart will be also.", ref:"Matthew 6:21 (NIV)"},
    "Days 15–21",
    "The Spending Reveal: Without sharing specific numbers, each person thinks about what they spent money on in the past two weeks. Write the categories only: food, clothes, entertainment, gaming, giving, savings, etc. Share your list with a partner. If a stranger saw your list, what would they say you value most?",
    "Student Story: The First Paycheck. A student who planned what to do with their first real paycheck — and then had a conversation at church that changed the question from 'what do I want?' to 'what does God want with this?'",
    [
      "Money as a Tool: if someone looked at where your money goes, what would they conclude your priorities are? Is that conclusion accurate?",
      "Money as a Test: Paul said he 'learned' contentment through tight seasons and abundant ones. What financial season are you in right now — and what might it be trying to teach you?",
      "Money as Testimony: what would it look like for your financial life to be a witness to something different? Not perfect — just different from what everyone else around you is doing?",
      "Matthew 6:21 says treasure leads and heart follows. Where do you want your heart to end up in five years? What would it mean to redirect your treasure there now?",
      "If someone followed you for thirty days and looked at your bank statements, what would they say you trust? What would you want them to say instead?",
    ],
    "Pull up one month of spending — your bank app, Venmo history, wherever your money actually went. Don't judge it. Just look. Write one sentence: 'If God looked at this record, the one thing I'd most want to change is ___.' Bring it back next week.",
    {
      summary: "This week your student is learning that money is more than a practical tool — it's doing something spiritually. It reveals what you trust (in tight seasons), forms your heart through habits, and can be a visible testimony to a different foundation.",
      question: "What's one thing our family spent money on this month that we're glad we did — and one thing that, honestly, was mostly comparison or impulse?",
      action: "Look at one month of family spending together. No shame — just curiosity. Ask: does this reflect what we say we value?",
      prayer: "Father, let our family's financial life be a quiet testimony to the world that you are enough. Amen.",
    }
  ),

  ...smallGroupSession(4, "What Faithful Looks Like", "Stewardship in Real Life",
    "You don't achieve stewardship. You practice it. Every single day.",
    {verse:"His master replied, 'Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things.'", ref:"Matthew 25:21 (NIV)"},
    "Days 22–28",
    "The 'Enough' Game: Everyone writes a number — the amount of money per month that would feel like 'enough' for their life. Don't share the number. Then ask: where did that number come from? What changes above it? What changes below it? Is 'enough' a number or something else?",
    "Student Story: A student who capped their spending on something — chose a ceiling — and then watched what happened to their sense of what they needed as a result.",
    [
      "A steward asks different questions than an owner. Which set of questions — owner questions or steward questions — more accurately describes how you currently think about your finances?",
      "The physician drove a Honda and parked down the street. The CEO chose a trailer park. Both decisions cost them social status. What would a similar 'enough is enough' decision look like in your world?",
      "Proverbs 22:7 says the borrower is slave to the lender. Have you ever experienced debt — or seen someone you know experience it — in a way that felt like that? What did it limit?",
      "What's one 'next faithful step' in your financial life right now — not the whole plan, just the next thing you know you should do?",
      "The morning return: 'God, you own it all. Lead me today.' What would it change about your mornings to actually say that — and mean it — before you check your phone?",
    ],
    "The Morning Return practice: For the next seven days, before you check your phone, say one sentence: 'God, you own it all. Lead me today.' Then take one small faithful step. Write down what happens. Bring your report next week.",
    {
      summary: "This week your student is thinking about what faithful stewardship actually looks like day-to-day — the daily reset, the question of 'enough,' the difference between responsible spending and pre-spending tomorrow.",
      question: "What would it look like for our family to make one decision this week that reflects 'enough is enough' rather than always wanting the next thing?",
      action: "As a family, practice the morning return together for three days: 'God, you own it all. Lead us today.'",
      prayer: "Father, teach our family what faithful looks like in the ordinary day. Amen.",
    }
  ),

  ...smallGroupSession(5, "Enough Is a Spiritual Word", "Contentment vs. Culture",
    "You don't find contentment when you finally have enough. You discover it when you stop making enough the point.",
    {verse:"I have learned to be content whatever the circumstances.", ref:"Philippians 4:11 (NIV)"},
    "Days 29–35",
    "The Comparison Demo: Show two identical items — one costs $40, one costs $200 (or describe them that way). Ask: which would you rather have? Now: would your answer change if nobody knew which one you had? What does your honest answer reveal about what you're actually buying?",
    "Student Story: A student who unfollowed several accounts for one month and tracked what changed in how they felt about what they had. What the experiment revealed.",
    [
      "Paul said he 'learned' contentment through need and plenty. What season are you in right now — and what might it be teaching you about what you actually trust?",
      "Comparison doesn't just produce envy — it produces a moving finish line. Is there a finish line in your life that keeps moving? What is it?",
      "2 Corinthians 10:12 says people who measure themselves by others are 'not wise.' What's the wisest thing you could do with the energy you currently spend comparing?",
      "God gave first — extravagantly, at the highest possible cost. How does the gospel change the shape of generosity? Does it feel different to give as a response rather than as an obligation?",
      "When generosity becomes a reflex rather than a discipline, something shifts. What would it take for generosity to feel less like loss and more like participation in something bigger?",
    ],
    "The Gratitude Practice: Every morning this week, before you open social media, name three things you have that you didn't create. Say them out loud. Track whether it changes how you feel looking at your feed afterward. Report back.",
    {
      summary: "This week your student is exploring contentment as a skill that gets practiced — not a feeling that arrives when you finally have enough. And the beginning of generosity — that God gave first, and our giving is a response to that.",
      question: "Is there something our family wants because someone around us has it — or because it would genuinely make our life better? How can we tell the difference?",
      action: "As a family, fast from one place where comparison most often happens — one feed, one environment — for three days. Notice what changes.",
      prayer: "God, teach our family to define enough by what you've given us — not by what everyone around us has. Amen.",
    }
  ),

  ...smallGroupSession(6, "Open Hands", "Generosity & Who You're Becoming",
    "The generous life isn't just about what you give away. It's about who you become in the giving.",
    {verse:"One person gives freely, yet gains even more; another withholds unduly, but comes to poverty.", ref:"Proverbs 11:24 (NIV)"},
    "Days 36–42",
    "The Open / Closed Hand Demo: Every person makes a tight fist. Now: what can you hold with a closed fist? What can you receive? What can you give? Now open your hand flat. What changes? The closed vs. open hand is the physical picture of this entire series. Debrief: where is your hand right now — in which area of your life is your hand most closed?",
    "Student Story: The Shoes I Didn't Buy. Saved for three months. Felt the nudge. Gave part of it. Shoes didn't happen. Something shifted. 'I realized I wasn't giving away my money — I was just using what God trusted me with to help someone else.' This is the testimony close.",
    [
      "Looking back over six sessions: what's the one thing that changed most about how you think about money, stuff, or your identity? What shifted?",
      "Moses chose 'disgrace for the sake of Christ' over the treasures of Egypt. What's one thing in your life that you've been choosing over the things that last?",
      "You are building a legacy right now — in the habits you're forming, the values you're developing. What kind of person do the decisions you've been making this month say you're becoming?",
      "Proverbs 11:24 says the person who gives freely gains more. Have you ever experienced this? What did you give, and what came back?",
      "If your financial life — your actual daily habits — could be a testimony to one truth about God, what would you want it to say? What would you need to change for that to be true?",
    ],
    "The Open Hand Decision: This week, do one thing with your money that you'd normally keep for yourself — and give it away without anyone knowing. It doesn't have to be large. It just has to cost you something. Then reflect: what did it feel like? Bring your honest answer.",
    {
      summary: "This week closes the six-session arc by asking who your student is becoming — not just what they know. The generous life is not just about financial decisions. It's a posture. Open hands. A way of moving through the world.",
      question: "What's one way our family could do something together this month that reflects open hands — giving something away that costs us something?",
      action: "Choose one family act of generosity to do together before the month ends. Plan it tonight.",
      prayer: "Father, make our family known for open hands. Not perfectly — but consistently. Let generosity be what people see. Amen.",
    }
  ),
];

// Build the final document
const doc = new Document({
  numbering: {
    config: [
      { reference:"bullets", levels:[{level:0, format:LevelFormat.BULLET, text:"•", alignment:AlignmentType.LEFT, style:{paragraph:{indent:{left:720,hanging:360}}}}] },
      { reference:"numbers", levels:[{level:0, format:LevelFormat.DECIMAL, text:"%1.", alignment:AlignmentType.LEFT, style:{paragraph:{indent:{left:720,hanging:360}}}}] },
    ]
  },
  styles: {
    default: { document: { run: { font:"Arial", size:22 } } },
    paragraphStyles: [
      { id:"Heading1", name:"Heading 1", basedOn:"Normal", next:"Normal", quickFormat:true, run:{size:52,bold:true,font:"Arial",color:NAVY}, paragraph:{spacing:{before:400,after:120},outlineLevel:0} },
      { id:"Heading2", name:"Heading 2", basedOn:"Normal", next:"Normal", quickFormat:true, run:{size:32,bold:true,font:"Arial",color:NAVY}, paragraph:{spacing:{before:280,after:100},outlineLevel:1} },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width:12240, height:15840 },
        margin: { top:1080, right:1080, bottom:1080, left:1080 }
      }
    },
    children: [
      ...coverPage,
      ...howToUse,
      ...allSessions,
      ...smallGroupGuide,
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/GOIA_Youth_42_Devotionals_SmallGroup.docx', buffer);
  console.log('Complete. File written.');
});
