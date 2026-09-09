const {
  Document, Packer, Paragraph, TextRun, PageBreak,
  AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, Table, TableRow, TableCell
} = require('docx');
const fs = require('fs');

// ── PALETTE ───────────────────────────────────────────────
const NAVY   = "1B3A5C";
const TEAL   = "2A7B8C";
const GOLD   = "C8922A";
const LB     = "E8F0F7";
const LG     = "FDF3E3";
const LT     = "E0F2F5";
const GRAY   = "F3F4F6";
const MGRAY  = "6B7280";
const WHITE  = "FFFFFF";
const DARK   = "1F2937";

const NO = { style: BorderStyle.NONE };
const thin = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };

// ── PRIMITIVES ────────────────────────────────────────────
const sp  = (b=80,a=80) => ({ before:b, after:a });
const pb  = () => new Paragraph({ children:[new PageBreak()] });
const gap = (h=120) => new Paragraph({ spacing:sp(h,0), children:[] });
const t   = (text, o={}) => new TextRun({ text, font:"Georgia", size:22, color:DARK, ...o });
const ta  = (text, o={}) => new TextRun({ text, font:"Arial", size:20, color:DARK, ...o });

// Body paragraph
const body = (text, b=60, a=60, align=AlignmentType.LEFT) =>
  new Paragraph({ spacing:sp(b,a), alignment:align,
    children:[ new TextRun({ text, font:"Georgia", size:22, color:DARK }) ] });

// All-caps label
const label = (text, color=TEAL) =>
  new Paragraph({ spacing:sp(200,60),
    children:[ new TextRun({ text:text.toUpperCase(), font:"Arial", size:17, bold:true, color }) ] });

// Script heading
const script = (text) =>
  new Paragraph({ spacing:sp(240,80),
    children:[ new TextRun({ text, font:"Georgia", size:36, italics:true, color:TEAL }) ] });

// Bold heading
const h2 = (text, color=NAVY) =>
  new Paragraph({ spacing:sp(220,80),
    children:[ new TextRun({ text, font:"Arial", size:28, bold:true, color }) ] });

const h3 = (text) =>
  new Paragraph({ spacing:sp(160,60),
    children:[ new TextRun({ text, font:"Arial", size:22, bold:true, color:NAVY }) ] });

// Bullet
const bul = (text) =>
  new Paragraph({ numbering:{reference:"bullets",level:0}, spacing:sp(40,40),
    children:[ new TextRun({ text, font:"Georgia", size:22, color:DARK }) ] });

// Numbered item
const num = (text, ref="numbers") =>
  new Paragraph({ numbering:{reference:ref,level:0}, spacing:sp(40,40),
    children:[ new TextRun({ text, font:"Georgia", size:22, color:DARK }) ] });

// Centered text
const ctr = (text, size=22, bold=false, color=DARK, font="Georgia") =>
  new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(60,60),
    children:[ new TextRun({ text, font, size, bold, color }) ] });

// Divider line
const divider = (color=TEAL) =>
  new Paragraph({ spacing:sp(120,120),
    border:{ bottom:{ style:BorderStyle.SINGLE, size:4, color } }, children:[] });

// ── BOX BUILDER ───────────────────────────────────────────
const box = (children, fill=LB, accent=TEAL, thick=true) =>
  new Table({
    width:{size:9360,type:WidthType.DXA}, columnWidths:[160,9200],
    borders:{top:NO,bottom:NO,left:NO,right:NO,insideH:NO,insideV:NO},
    rows:[new TableRow({children:[
      new TableCell({
        width:{size:160,type:WidthType.DXA},
        shading:{fill:accent,type:ShadingType.CLEAR},
        borders:{top:NO,bottom:NO,right:NO,
          left:{style:BorderStyle.SINGLE,size:thick?24:8,color:accent}},
        children:[new Paragraph({children:[]})]
      }),
      new TableCell({
        width:{size:9200,type:WidthType.DXA},
        shading:{fill,type:ShadingType.CLEAR},
        margins:{top:140,bottom:140,left:240,right:240},
        borders:{top:NO,bottom:NO,left:NO,right:NO},
        children:Array.isArray(children)?children:[children]
      })
    ]})]
  });

// Full-width shaded block
const shade = (children, fill=LB) =>
  new Table({
    width:{size:9360,type:WidthType.DXA}, columnWidths:[9360],
    borders:{top:NO,bottom:NO,left:NO,right:NO,insideH:NO,insideV:NO},
    rows:[new TableRow({children:[new TableCell({
      width:{size:9360,type:WidthType.DXA},
      shading:{fill,type:ShadingType.CLEAR},
      margins:{top:160,bottom:160,left:280,right:280},
      borders:{top:NO,bottom:NO,left:NO,right:NO},
      children:Array.isArray(children)?children:[children]
    })]})]
  });

// Full-width navy banner
const navyBanner = (children) =>
  new Table({
    width:{size:9360,type:WidthType.DXA}, columnWidths:[9360],
    borders:{top:NO,bottom:NO,left:NO,right:NO,insideH:NO,insideV:NO},
    rows:[new TableRow({children:[new TableCell({
      width:{size:9360,type:WidthType.DXA},
      shading:{fill:NAVY,type:ShadingType.CLEAR},
      margins:{top:200,bottom:200,left:320,right:320},
      borders:{top:NO,bottom:NO,left:NO,right:NO},
      children:Array.isArray(children)?children:[children]
    })]})]
  });

// Pull quote
const pq = (text) => box([
  new Paragraph({ children:[t(`\u201c${text}\u201d`,{size:24,bold:true,italics:true,color:NAVY,font:"Georgia"})],
    spacing:sp(40,40) })
], LG, GOLD);

// Memory verse box
const memVerse = (verse, ref) => shade([
  ctr("MEMORY VERSE", 15, true, TEAL, "Arial"),
  gap(60),
  new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(40,20),
    children:[t(`\u201c${verse}\u201d`,{size:23,italics:true,color:NAVY})] }),
  gap(20),
  new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,40),
    children:[ta(ref,{bold:true,size:17,color:TEAL})] })
], LB);

// Scripture block
const scripture = (verse, ref) => box([
  new Paragraph({ spacing:sp(20,12), children:[t(`\u201c${verse}\u201d`,{italics:true,size:22,color:NAVY})] }),
  new Paragraph({ spacing:sp(0,20), children:[ta(`\u2014 ${ref}`,{bold:true,size:18,color:GOLD})] })
], LB, NAVY);

// Response line
const respond = (prompt) => [
  new Paragraph({ spacing:sp(80,8),
    children:[ta("RESPOND: ",{bold:true,size:18,color:TEAL}), t(prompt,{size:21,italics:true})] }),
  new Paragraph({ spacing:sp(4,4), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] }),
  new Paragraph({ spacing:sp(4,20), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] }),
];

// Write lines block
const writeLines = (n=8) => {
  const lines = [];
  for(let i=0;i<n;i++) lines.push(
    new Paragraph({ spacing:sp(4,4), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] })
  );
  return lines;
};

// Discussion question numbered
const dq = (n, text) =>
  new Paragraph({ spacing:sp(60,60),
    children:[
      ta(`${n}.  `,{bold:true,size:22,color:TEAL}),
      t(text,{size:22})
    ]});

// ── SESSION SPLASH ────────────────────────────────────────
const sessionSplash = (num, romanNum, title, subtitle) => [
  navyBanner([
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,40),
      children:[ta(`SESSION ${num}`,{size:17,bold:true,color:GOLD})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,60),
      children:[new TextRun({text:title,font:"Georgia",size:64,bold:true,color:WHITE})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,120),
      children:[new TextRun({text:subtitle,font:"Georgia",size:28,italics:true,color:"B8D0E8"})] }),
  ]),
  pb(),
];

// ── STORY PAGE ────────────────────────────────────────────
const storyPage = (name, subheading, p1, p2, p3, quote) => [
  label("Student Story"),
  divider(),
  gap(80),
  shade([
    new Paragraph({ spacing:sp(0,40),
      children:[new TextRun({text:name,font:"Georgia",size:40,italics:true,color:NAVY})] }),
    new Paragraph({ spacing:sp(0,0),
      children:[ta(subheading.toUpperCase(),{size:17,bold:true,color:TEAL})] }),
  ], LB),
  gap(80),
  body(p1, 60, 60),
  body(p2, 60, 60),
  body(p3, 60, 60),
  gap(60),
  pq(quote),
  pb(),
];

// ── GET IN (= Come Together) ──────────────────────────────
const getIn = (q1, q2) => [
  script("Get In"),
  divider(),
  gap(80),
  box([
    new Paragraph({ spacing:sp(0,60),
      children:[ta("Open with prayer.",{bold:true,size:20,color:NAVY})] }),
    body("Ask God to search your heart honestly. Invite him to reveal where you\u2019ve been trying to carry things that belong to him. Then set the tone for your group: no performing, no shame, no comparing. You\u2019re here to learn together and take one faithful next step."),
  ], LT, TEAL),
  gap(80),
  script("Discuss"),
  dq(1, q1),
  gap(40),
  dq(2, q2),
  pb(),
];

// ── GROUP COVENANT (Session 1 only) ──────────────────────
const groupCovenant = () => [
  shade([
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,60),
      children:[ta("GROUP",{bold:true,size:40,color:WHITE,font:"Arial"})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,0),
      children:[ta("RHYTHM & AGREEMENT",{bold:true,size:17,color:WHITE,font:"Arial"})] }),
  ], NAVY),
  gap(80),
  h3("Build a healthy group culture."),
  body("A strong group isn\u2019t built on perfect answers\u2014it\u2019s built on trust, honesty, and grace. As you meet, protect a tone that helps everyone participate without fear."),
  gap(60),
  bul("We listen without judgment or interruption."),
  bul("We keep what\u2019s shared here confidential."),
  bul("We speak from our own experience (no fixing or lecturing)."),
  bul("We make room for everyone to contribute."),
  bul("We choose encouragement over comparison."),
  bul("We keep it real: small steps, actual life, honest answers."),
  pb(),
];

// ── WATCH PAGE ────────────────────────────────────────────
const watchPage = (sessionNum, instructions) => [
  script("Watch"),
  label(`Video Session ${sessionNum}`),
  divider(),
  gap(60),
  box([body(instructions)], LG, GOLD),
  gap(80),
  ...writeLines(20),
  pb(),
];

// ── TALK ABOUT IT (= Learn Together) ─────────────────────
const talkAboutIt = (qs) => [
  script("Talk About It"),
  divider(),
  body("As a group, react to the video and discuss the following questions."),
  gap(60),
  ...qs.map((q,i) => [dq(i+1, q), gap(20)]).flat(),
  pb(),
];

// ── GO DEEPER (= Grow Together) ──────────────────────────
const goDeeper = (qs) => [
  script("Go Deeper"),
  divider(),
  body("Work through these as a group. Choose the ones that hit closest to where you actually are."),
  gap(60),
  ...qs.map((q,i) => [dq(i+1, q), gap(20)]).flat(),
  pb(),
];

// ── YOUR WORLD (= Circles of Life) ───────────────────────
const yourWorld = (intro, circles) => [
  shade([
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,40),
      children:[new TextRun({text:"Your World",font:"Georgia",size:44,bold:true,italics:true,color:WHITE})] }),
  ], NAVY),
  gap(80),
  body(intro, 60, 80),
  gap(60),
  ...circles.map(c => box([
    new Paragraph({ spacing:sp(0,30), children:[ta(c.title,{bold:true,size:20,color:NAVY})] }),
    new Paragraph({ spacing:sp(0,40), children:[ta(c.sub,{size:19,color:MGRAY})] }),
    new Paragraph({ spacing:sp(0,8), children:[ta("What has God entrusted to you here?",{italics:true,size:19,color:TEAL})] }),
    new Paragraph({ spacing:sp(4,4), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] }),
  ], LB, TEAL)),
  pb(),
];

// ── THIS WEEK'S CHALLENGE (= Go Deeper This Week) ────────
const thisWeeksChallenge = (bullets, prayerText, readingChapters) => [
  script("This Week\u2019s Challenge"),
  divider(),
  gap(60),
  ...bullets.map(b => bul(b)),
  gap(80),
  box([
    new Paragraph({ spacing:sp(0,40), children:[ta("Close your group with prayer.",{bold:true,size:20,color:NAVY})] }),
    body(prayerText),
  ], LT, TEAL),
  gap(80),
  shade([
    new Paragraph({ spacing:sp(0,40), children:[new TextRun({text:"Reading Plan",font:"Georgia",size:32,italics:true,color:NAVY})] }),
    body("The God Owns It All book is a great companion to what you\u2019re learning in group. Read these chapters before your next session."),
    gap(40),
    ...readingChapters.map(c => new Paragraph({ spacing:sp(20,20),
      children:[ta("\u25a1  "+c,{size:21})] })),
  ], GRAY),
  pb(),
];

// ── DIG IN (= Additional Study) ──────────────────────────
const digIn = (passage1, passage2) => [
  shade([
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,0),
      children:[ta("DIG IN",{bold:true,size:32,color:WHITE,font:"Arial"})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(20,0),
      children:[ta("Additional Study",{size:17,color:"B8D0E8",font:"Arial"})] }),
  ], NAVY),
  gap(80),
  body("If you want to go further, work through these passages on your own or as a group."),
  gap(80),
  h3(`Read ${passage1.ref}`),
  scripture(passage1.verse, passage1.ref),
  gap(40),
  ...passage1.questions.map((q,i) => [
    new Paragraph({ spacing:sp(40,8), children:[ta("\u2022  ",{bold:true,size:22,color:TEAL}), t(q,{size:22})] }),
    new Paragraph({ spacing:sp(4,20), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] }),
  ]).flat(),
  gap(80),
  h3(`Read ${passage2.ref}`),
  scripture(passage2.verse, passage2.ref),
  gap(40),
  ...passage2.questions.map((q,i) => [
    new Paragraph({ spacing:sp(40,8), children:[ta("\u2022  ",{bold:true,size:22,color:TEAL}), t(q,{size:22})] }),
    new Paragraph({ spacing:sp(4,20), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] }),
  ]).flat(),
  pb(),
];

// ── DAILY READS ───────────────────────────────────────────
const dailyReads = (days, reflectPrompt) => [
  shade([
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,0),
      children:[new TextRun({text:"Daily Reads",font:"Georgia",size:40,italics:true,bold:true,color:WHITE})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(20,0),
      children:[ta("Five days of Scripture between sessions",{size:17,color:"B8D0E8",font:"Arial"})] }),
  ], NAVY),
  gap(80),
  ...days.map((d,i) => [
    navyBanner([
      new Paragraph({ spacing:sp(0,0),
        children:[ta(`Day ${i+1}`,{bold:true,size:17,color:GOLD})] })
    ]),
    gap(60),
    scripture(d.verse, d.ref),
    gap(40),
    ...respond(d.respond),
    gap(40),
  ]).flat(),
  gap(60),
  shade([
    new Paragraph({ spacing:sp(0,40),
      children:[ta("REFLECT",{bold:true,size:17,color:TEAL,font:"Arial"})] }),
    body("Write what God is stirring in you after this week\u2019s reading. Name one clear next step you will take."),
    gap(40),
    ...writeLines(5),
    gap(20),
    new Paragraph({ spacing:sp(40,8), children:[ta("My next step:",{bold:true,size:19,color:NAVY,font:"Arial"})] }),
    new Paragraph({ spacing:sp(4,4), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] }),
    new Paragraph({ spacing:sp(4,20), border:{bottom:{style:BorderStyle.SINGLE,size:2,color:"CCCCCC"}}, children:[t("  ")] }),
  ], LB),
  pb(),
];

// ════════════════════════════════════════════════════════
//  SESSION DATA
// ════════════════════════════════════════════════════════

// ── SESSION 1: THE OWNERSHIP QUESTION ────────────────────
function session1() {
  return [
    ...sessionSplash("1","I","The Ownership Question","What Does It Really Mean If God Owns It All?"),

    memVerse(
      "Everything comes from you, and we have given you only what comes from your hand.",
      "1 Chronicles 29:14"
    ),
    gap(80),
    body("This session starts with the one question everything else depends on: who actually owns what you have? We\u2019ll start where most of us feel it first\u2014money and stuff\u2014and widen out to the whole picture: identity, friendships, your future, your fears. The goal isn\u2019t guilt or pressure. The goal is freedom. Because when God is the actual Owner, you finally get to stop carrying what was never yours to carry.", 60, 60),
    pb(),

    ...storyPage(
      "Marcus & Leah",
      "Learning to Let Go",
      "They weren\u2019t big spenders. Marcus and Leah both worked part-time jobs, kept their spending pretty reasonable, and genuinely tried to be responsible. But money had started feeling like a low-grade anxiety that never fully went away\u2014always calculating, always comparing, always wondering if they had enough or were doing it right.",
      "Over time they started to notice the real issue. It wasn\u2019t what they had. It was what they were trying to hold together. They\u2019d both been operating like owners\u2014defending outcomes, protecting plans, managing their own futures\u2014instead of asking a simpler question: is this actually mine to carry?",
      "One evening they prayed honestly, named what they\u2019d been gripping\u2014money, plans, reputation, the future\u2014and released it. Nothing changed on the outside overnight. But something shifted on the inside. The weight started to lift.",
      "We weren\u2019t just managing money. We were trying to manage our whole lives. When we gave that to God, we finally felt like we could breathe."
    ),

    ...getIn(
      "When you hear \u2018God owns it all,\u2019 what part of you feels comfort\u2014and what part of you feels resistance?",
      "Where do you most feel the weight of ownership right now\u2014money, the future, a relationship, something else? What would it look like to release it?"
    ),

    ...groupCovenant(),

    ...watchPage(1, "As you watch Session 1, listen for the difference between ownership and stewardship. Notice how Scripture stretches \u2018all\u2019 beyond money\u2014into identity, relationships, and your future. Write down one phrase that lands for you, and one area where you sense God is asking you to let go."),

    ...talkAboutIt([
      "What\u2019s the good news in the ownership truth\u2014why is it meant to bring freedom, not fear?",
      "What\u2019s the difference between living as an owner and living as a steward? How does that show up in real daily decisions?",
      "Why does surrender have to come before budgeting, planning, or giving?",
      "What\u2019s one specific next step that could help you live this week as a steward, not an owner?",
    ]),

    ...goDeeper([
      "What tends to trigger \u2018owner thinking\u2019 in you\u2014uncertainty, comparison, pressure, fear, something else?",
      "If God\u2019s ownership includes you\u2014not just what you have\u2014how does that change the way you see your worth?",
      "Ron Blue says behavior follows belief. Looking at how you actually handle money right now, what does your behavior say you believe?",
      "How might genuinely surrendering ownership change the tone of your closest relationships?",
      "Choose one specific area to surrender this week. What would faithfulness look like over the next seven days?",
    ]),

    ...yourWorld(
      "God\u2019s ownership isn\u2019t only about your bank account. It touches every part of your life. Look at each circle below and ask: what has God entrusted to me here?",
      [
        { title: "FAMILY", sub: "Immediate or extended family" },
        { title: "FRIENDS", sub: "Your close friend group" },
        { title: "FAMILIAR", sub: "Neighbors, teammates, classmates" },
        { title: "FUTURE", sub: "Plans, goals, what comes next" },
        { title: "FINANCES", sub: "Money, possessions, what you earn" },
      ]
    ),

    ...thisWeeksChallenge([
      "Spend five quiet minutes each morning acknowledging God as Owner\u2014before you plan, decide, or react.",
      "Re-read this week\u2019s key Scriptures slowly and underline one phrase you want to remember.",
      "Take one small step of surrender that costs you something\u2014time, control, pride, comfort.",
    ],
    "Thank God for his gentle ownership, and ask for the faith to live as a steward\u2014free from fear, ready to obey in small ways.",
    ["Chapter 3", "Chapter 4"]),

    ...digIn(
      {
        ref: "Psalm 50:9\u201312",
        verse: "I have no need of a bull from your stall or of goats from your pens, for every animal of the forest is mine, and the cattle on a thousand hills. I know every bird in the mountains, and the insects in the fields are mine. If I were hungry I would not tell you, for the world is mine, and all that is in it.",
        questions: [
          "What does God specifically name as His\u2014and what does that teach you about the scope of ownership?",
          "How does this passage correct the idea that God \u2018needs\u2019 us in order to have enough?",
          "If God truly owns \u2018the world and all that is in it,\u2019 what changes about how you hold your resources and your plans?",
        ]
      },
      {
        ref: "Deuteronomy 8:10\u201318",
        verse: "When you have eaten and are satisfied, praise the Lord your God... Be careful that you do not forget the Lord your God... You may say to yourself, \u2018My power and the strength of my hands have produced this wealth for me.\u2019 But remember the Lord your God, for it is he who gives you the ability to produce wealth.",
        questions: [
          "What can happen to us after things are going well and we feel \u2018satisfied\u2019?",
          "Where do you see the progression Moses describes\u2014blessing \u2192 pride \u2192 forgetting God\u2014in everyday life?",
          "What does God claim to give in verse 18, and how does that change the way you think about your work and opportunities?",
        ]
      }
    ),

    ...dailyReads([
      { verse: "I have no need of a bull from your stall or of goats from your pens, for every animal of the forest is mine, and the cattle on a thousand hills.", ref: "Psalm 50:9\u201310",
        respond: "What is one \u2018mine\u2019 you\u2019re holding tightly today\u2014and what would it look like to hold it with open hands?" },
      { verse: "But who am I, and who are my people, that we should be able to give as generously as this? Everything comes from you, and we have given you only what comes from your hand.", ref: "1 Chronicles 29:14",
        respond: "Where do you need to replace entitlement with gratitude\u2014acknowledging, \u2018Everything comes from You\u2019?" },
      { verse: "You may say to yourself, \u2018My power and the strength of my hands have produced this wealth for me.\u2019 But remember the Lord your God, for it is he who gives you the ability to produce wealth.", ref: "Deuteronomy 8:17\u201318",
        respond: "What is one \u2018I did this\u2019 story in your life that actually belongs to God?" },
      { verse: "No one can serve two masters. Either you will hate the one and love the other, or you will be devoted to the one and despise the other. You cannot serve both God and money.", ref: "Luke 16:13",
        respond: "Where do you feel divided loyalties\u2014wanting God, but also wanting money to make you feel safe?" },
      { verse: "Whoever can be trusted with very little can also be trusted with much, and whoever is dishonest with very little will also be dishonest with much.", ref: "Luke 16:10",
        respond: "What is one small area where you can practice faithfulness today\u2014one simple act of stewardship or honesty?" },
    ], "Write what God is stirring in you after this week\u2019s reading."),
  ];
}

// ── SESSION 2: THE STEWARDSHIP QUESTION ──────────────────
function session2() {
  return [
    ...sessionSplash("2","II","The Stewardship Question","How Do We Learn Faithfulness Through Stewardship?"),

    memVerse(
      "His master replied, \u2018Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things.\u2019",
      "Matthew 25:21"
    ),
    gap(80),
    body("If Session 1 answered \u2018who owns it,\u2019 Session 2 asks the follow-up question: so what does the steward actually do? Faithfulness isn\u2019t dramatic. It\u2019s the small, ordinary, daily decisions that form the person who later makes the big ones. This session is about living the answer to the ownership question\u2014not just believing it.", 60, 60),
    pb(),

    ...storyPage(
      "Jordan",
      "The First Paycheck",
      "Jordan had been working at a burger place for three weeks when the first real paycheck hit the account. The plan was already made: some new clothes, food with friends, save a little. It was not a complicated plan. It was not a spiritual plan.",
      "That same week at church, someone talked about honoring God first with what you earn\u2014not from what\u2019s left over after everything else, but first. Jordan didn\u2019t love that idea. It felt like God was asking for a cut before the enjoyment even started. But the thought wouldn\u2019t leave.",
      "The decision to give first\u2014not perfectly, not confidently, but first\u2014changed something that had nothing to do with the amount. It changed how Jordan saw the paycheck. Not as money that was earned alone, but as something entrusted.",
      "It wasn\u2019t a huge moment. But it was the moment I stopped seeing my paycheck as mine and started seeing it as something I\u2019d been given to manage."
    ),

    ...getIn(
      "Think about the last time you did something with money you were genuinely proud of afterward. What made that decision feel right?",
      "What\u2019s the difference between being responsible for something and owning it? Can you give an example from your actual life?"
    ),

    ...watchPage(2, "As you watch Session 2, listen for the three ways money works in a steward\u2019s life: as a tool, a test, and a testimony. Notice which one feels most active in your life right now. Write down what stands out, and one area where you sense God inviting you to be more faithful."),

    ...talkAboutIt([
      "What does \u2018faithful with little\u2019 actually look like for someone your age? What\u2019s a real example?",
      "Ron says money functions as a tool, a test, and a testimony. Which one hits closest to home for you right now?",
      "What\u2019s the difference between stewardship as a discipline you perform and stewardship as a daily posture you live from?",
      "What one small, specific practice could you add this week to live more like a steward than an owner?",
    ]),

    ...goDeeper([
      "Where in your life is the gap widest between what you say you believe and how you actually handle money?",
      "Matthew 6:21 says \u2018where your treasure is, there your heart will be also.\u2019 If someone looked at where your money goes, what would they say your heart is most invested in?",
      "What would it mean, practically, for your financial life to be a testimony\u2014not just a private spiritual matter but something visibly different?",
      "The physician parked down the street because he chose not to live above a certain level. What would a similar \u2018enough is enough\u2019 decision look like for you?",
      "What\u2019s one next faithful step\u2014not the whole plan, just the next thing you know you should do?",
    ]),

    ...yourWorld(
      "Stewardship isn\u2019t only about money. It\u2019s about everything entrusted to you. Look at each circle and ask: how am I being faithful with what God has given me here?",
      [
        { title: "TIME", sub: "How you spend it, who gets it" },
        { title: "MONEY", sub: "What you do with what you earn" },
        { title: "INFLUENCE", sub: "Who looks up to you or follows your lead" },
        { title: "SKILLS", sub: "What you\u2019re naturally good at" },
        { title: "RELATIONSHIPS", sub: "The people entrusted to you" },
      ]
    ),

    ...thisWeeksChallenge([
      "Before any financial decision this week\u2014large or small\u2014pause and ask: \u2018What would a steward do here?\u2019",
      "Look at one month of your spending (bank app, Venmo, wherever your money actually went). Write one honest sentence about what it reveals.",
      "Do one act of faithful stewardship that no one else will see\u2014give, save, or sacrifice something small as practice.",
    ],
    "Thank God for the invitation to be a steward, not just an owner. Ask for wisdom for the small decisions this week that are quietly forming the person you\u2019re becoming.",
    ["Chapter 5", "Chapter 6"]),

    ...digIn(
      {
        ref: "Matthew 25:14\u201321",
        verse: "Again, it will be like a man going on a journey, who called his servants and entrusted his wealth to them\u2026 His master replied, \u2018Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things.\u2019",
        questions: [
          "What do you notice about how the master distributes responsibility\u2014and what does that say about stewardship?",
          "The commended servant is called \u2018faithful,\u2019 not \u2018successful.\u2019 What\u2019s the difference, and why does it matter?",
          "Where in your life is God currently calling you to be faithful with \u2018a few things\u2019?",
        ]
      },
      {
        ref: "Luke 16:10\u201311",
        verse: "Whoever can be trusted with very little can also be trusted with much, and whoever is dishonest with very little will also be dishonest with much. So if you have not been trustworthy in handling worldly wealth, who will trust you with true riches?",
        questions: [
          "Why do you think Jesus connects faithfulness with small amounts to faithfulness with larger ones?",
          "What does \u2018true riches\u2019 refer to\u2014and what does it reveal about what stewardship is really preparing us for?",
          "What is one small area of your current life where practicing faithfulness right now matters more than you\u2019ve been treating it?",
        ]
      }
    ),

    ...dailyReads([
      { verse: "His master replied, \u2018Well done, good and faithful servant! You have been faithful with a few things; I will put you in charge of many things. Come and share your master\u2019s happiness!\u2019", ref: "Matthew 25:21",
        respond: "What would it feel like to hear those words at the end of your life? What would need to change now for that to be true?" },
      { verse: "For where your treasure is, there your heart will be also.", ref: "Matthew 6:21",
        respond: "If someone looked at where your money went last month, what would they say your heart is most invested in?" },
      { verse: "Whoever can be trusted with very little can also be trusted with much.", ref: "Luke 16:10",
        respond: "What is one \u2018little\u2019 area in your life where you can practice faithfulness more intentionally today?" },
      { verse: "No one can serve two masters\u2026 You cannot serve both God and money.", ref: "Matthew 6:24",
        respond: "Where are your financial decisions being driven more by fear or comfort than by faithfulness?" },
      { verse: "And whatever you do, whether in word or deed, do it all in the name of the Lord Jesus, giving thanks to God the Father through him.", ref: "Colossians 3:17",
        respond: "What would it look like today to do your work\u2014including how you handle money\u2014\u2018in the name of the Lord Jesus\u2019?" },
    ], "Write what God is stirring in you after this week\u2019s reading."),
  ];
}

// ── SESSION 3: THE CONFIDENCE QUESTION ───────────────────
function session3() {
  return [
    ...sessionSplash("3","III","The Confidence Question","Will I Be Okay?"),

    memVerse(
      "But seek first his kingdom and his righteousness, and all these things will be given to you as well.",
      "Matthew 6:33"
    ),
    gap(80),
    body("The question running underneath almost every financial anxiety is the same one: will I be okay? This session addresses it directly. Not with a budget or a savings strategy\u2014with the foundational answer Scripture gives. You can stop rehearsing the worst-case scenarios. You can stop trying to secure every outcome. And you can start building the kind of steadiness that doesn\u2019t depend on your account balance.", 60, 60),
    pb(),

    ...storyPage(
      "Amara",
      "When the Plan Fell Apart",
      "Amara had worked for months saving toward a specific goal. The plan was clear. The timeline was set. Then, in the same week, two unexpected expenses hit that wiped out most of what she\u2019d saved. She remembers sitting with her phone open to her banking app, feeling a kind of panic she hadn\u2019t anticipated.",
      "What surprised her wasn\u2019t the loss. It was what the loss revealed. She\u2019d thought her peace was coming from following God. But in that moment she realized her peace had actually been coming from the savings account. The number going down had hit harder than it should have if God had really been the source.",
      "She didn\u2019t get the money back quickly. But she started praying differently\u2014not asking God to restore the number, but asking him to actually be the foundation. And gradually, something steadier than the account balance started to grow.",
      "I thought I trusted God. But I trusted the savings account. Losing it showed me the difference\u2014and that was actually the thing I needed to learn."
    ),

    ...getIn(
      "When something financial goes wrong\u2014an unexpected expense, money running out, a plan falling apart\u2014what is your first internal move? What do you reach for?",
      "What\u2019s the difference between financial anxiety and wise planning? How do you know which one you\u2019re in?"
    ),

    ...watchPage(3, "As you watch Session 3, listen for the difference between rehearsing and preparing. Notice how Jesus connects worry to ownership in Matthew 6. Write down one phrase that reframes the way you\u2019ve been thinking about your current financial situation."),

    ...talkAboutIt([
      "Jesus says \u2018do not worry\u2019 in Matthew 6, but he doesn\u2019t shame anxiety\u2014he diagnoses it. What does he say worry is actually about?",
      "What\u2019s the difference between rehearsing a problem and preparing for it? Which one are you most often doing?",
      "What does \u2018seek first his kingdom\u2019 actually look like as a daily, practical thing\u2014not as a slogan, but as a decision?",
      "What would it look like for your financial life to produce genuine peace rather than more anxiety?",
    ]),

    ...goDeeper([
      "What is the financial fear you carry most consistently? If you\u2019re honest, what are you really afraid of underneath it?",
      "Ron Blue tells the story of canceling his line of credit when starting his business\u2014and God providing the exact amount. That\u2019s not a formula. But it illustrates something. What does it illustrate to you?",
      "What\u2019s the practical difference between peace that depends on your account balance and peace that comes from the foundation described in Matthew 6?",
      "What is one area of your financial life where you\u2019ve been trying to guarantee an outcome that belongs to God?",
      "What is one next faithful step\u2014the actual next thing, not the whole plan\u2014you can take this week?",
    ]),

    ...yourWorld(
      "The \u2018confidence question\u2019 touches more than finances. Where in your world are you most tempted to secure outcomes that belong to God? Look at each circle.",
      [
        { title: "FINANCES", sub: "What you\u2019re trying to protect or guarantee" },
        { title: "THE FUTURE", sub: "Plans and outcomes you\u2019re trying to control" },
        { title: "RELATIONSHIPS", sub: "People or outcomes you\u2019re trying to manage" },
        { title: "REPUTATION", sub: "What others think of how you\u2019re doing" },
        { title: "HEALTH", sub: "What you\u2019re worried you might lose" },
      ]
    ),

    ...thisWeeksChallenge([
      "Identify your biggest financial anxiety this week. Write it down, then write a one-sentence prayer giving it to God. Pray it every morning.",
      "Practice the \u2018seek first\u2019 posture: before any significant decision, pray first\u2014before you plan, before you react, before you search for answers.",
      "Name one practical step that builds real stability (a conversation, a plan, one wise adjustment). Do it calmly\u2014without needing to solve everything past it.",
    ],
    "Father, you know what we\u2019re carrying and what we\u2019re afraid might happen. Teach us to seek your kingdom first. Turn our rehearsing into preparing, and our anxiety into steadiness.",
    ["Chapter 7", "Chapter 8"]),

    ...digIn(
      {
        ref: "Matthew 6:25\u201334",
        verse: "Therefore I tell you, do not worry about your life\u2026 But seek first his kingdom and his righteousness, and all these things will be given to you as well. Therefore do not worry about tomorrow, for tomorrow will worry about itself.",
        questions: [
          "What specific argument does Jesus build for why worry is unnecessary? How does he use birds and flowers?",
          "What does \u2018seek first\u2019 suggest about the order of our priorities\u2014and how does that apply to financial decisions?",
          "What is one thing you\u2019re currently worrying about tomorrow that Jesus\u2019 words here speak directly to?",
        ]
      },
      {
        ref: "Philippians 4:6\u20137, 11\u201313",
        verse: "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God\u2026 I have learned to be content whatever the circumstances\u2026 I can do all this through him who gives me strength.",
        questions: [
          "Paul says to bring everything to God with thanksgiving\u2014before the situation changes. What does gratitude do to anxiety?",
          "Paul \u2018learned\u2019 contentment. It wasn\u2019t natural. What does that mean for how you develop it?",
          "What\u2019s the difference between contentment that comes from having enough and contentment that comes from the God who is enough?",
        ]
      }
    ),

    ...dailyReads([
      { verse: "But seek first his kingdom and his righteousness, and all these things will be given to you as well.", ref: "Matthew 6:33",
        respond: "What would \u2018seeking first\u2019 look like today in one specific decision you\u2019re currently facing?" },
      { verse: "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God.", ref: "Philippians 4:6",
        respond: "What is the one financial anxiety you most need to actually give to God today\u2014not just acknowledge, but give?" },
      { verse: "I have learned to be content whatever the circumstances\u2026 I can do all this through him who gives me strength.", ref: "Philippians 4:11, 13",
        respond: "What \u2018season\u2019 are you in right now, and what might God be forming in you through it?" },
      { verse: "The Lord is my shepherd, I lack nothing.", ref: "Psalm 23:1",
        respond: "Is this sentence true for you today\u2014not as a feeling but as a settled reality? What\u2019s the gap between believing it and living it?" },
      { verse: "Cast all your anxiety on him because he cares for you.", ref: "1 Peter 5:7",
        respond: "What is one specific anxiety you\u2019ve been carrying that you can actually cast on God right now?" },
    ], "Write what God is stirring in you after this week\u2019s reading."),
  ];
}

// ── SESSION 4: THE CONTENTMENT QUESTION ──────────────────
function session4() {
  return [
    ...sessionSplash("4","IV","The Contentment Question","How Much Is Enough?"),

    memVerse(
      "But godliness with contentment is great gain. For we brought nothing into the world, and we can take nothing out of it.",
      "1 Timothy 6:6\u20137"
    ),
    gap(80),
    body("The culture never gives you a satisfying answer to \u2018how much is enough?\u2019 It always says: a little more than what you have. This session goes after a different kind of enough\u2014not a number that arrives from the outside, but a settled decision that gets made from the inside. Contentment isn\u2019t a personality type. It\u2019s a formation outcome. And it\u2019s available to anyone willing to learn it.", 60, 60),
    pb(),

    ...storyPage(
      "Priya",
      "The Comparison Loop",
      "Priya wasn\u2019t trying to be discontent. She was scrolling, and the scroll was doing something to her. Seeing other people\u2019s experiences, clothing, apartments, trips. Each image not particularly dramatic on its own\u2014but together they were quietly building a case that her life was slightly less-than.",
      "She decided to try an experiment: unfollow every account that consistently made her feel like she needed more. Not because those accounts were bad\u2014but because she wanted to find out if the restlessness was as tied to what she was consuming as she suspected it was.",
      "The first week was genuinely uncomfortable. The second week, something started to shift. By the third week she was noticing that gratitude\u2014actual, specific gratitude\u2014had more room to surface than it usually did. The comparison loop had been quieter than it felt. But it had been running constantly.",
      "I didn\u2019t realize how much of my discontent was chosen\u2014not because I chose to be unhappy, but because I kept choosing inputs that kept telling me I didn\u2019t have enough."
    ),

    ...getIn(
      "Think about the last time you felt genuinely content with what you had. What was different about that moment or season?",
      "Comparison doesn\u2019t just produce envy\u2014it produces a moving finish line. Where is that most active in your life right now?"
    ),

    ...watchPage(4, "As you watch Session 4, listen for the difference between contentment as a feeling and contentment as a skill\u2014something that gets learned, not just felt. Write down one thing that reframes how you\u2019ve been thinking about \u2018enough.\u2019"),

    ...talkAboutIt([
      "Paul says he \u2018learned\u2019 to be content\u2014not that he felt it naturally. What does it mean for contentment to be something you learn?",
      "What\u2019s the difference between wanting more because of genuine need and wanting more because comparison has set a moving finish line?",
      "What would it look like to actually decide what \u2018enough\u2019 means for your life\u2014before the culture decides it for you?",
      "What one habit could you build that would grow contentment rather than erode it?",
    ]),

    ...goDeeper([
      "What is the area of your life where the comparison loop is most active? What does it make you feel\u2014and what does it make you want to do?",
      "The physician capped his lifestyle at medical school levels and gave everything above that away. He ended up parking down the street from the physician\u2019s lot. What would a comparable decision look like for you in your current stage of life?",
      "Ron Blue says contentment is available to anyone at any income level. If that\u2019s true, what is actually preventing it from being more present in your life right now?",
      "What is one environment, feed, or input that consistently erodes your contentment? What would it look like to address that?",
      "If you defined \u2018enough\u2019 right now\u2014in one sentence\u2014what would you say? Write it down.",
    ]),

    ...yourWorld(
      "Contentment isn\u2019t only financial. It\u2019s a whole-life posture. Where in your world is the \u2018more\u2019 pressure strongest\u2014and where is contentment most genuinely present?",
      [
        { title: "POSSESSIONS", sub: "Stuff you have or want to have" },
        { title: "STATUS", sub: "How you\u2019re perceived or where you rank" },
        { title: "EXPERIENCES", sub: "What you\u2019re missing out on" },
        { title: "ACHIEVEMENT", sub: "Success, results, being ahead" },
        { title: "APPEARANCE", sub: "How you look or come across" },
      ]
    ),

    ...thisWeeksChallenge([
      "Identify one environment that consistently erodes your contentment. Step back from it for the full week and track what changes.",
      "Every morning this week, name three specific things you have that you didn\u2019t create. Say them out loud before you look at your phone.",
      "Write your one-sentence \u2018enough\u2019 statement. Put it somewhere you\u2019ll see it daily this week.",
    ],
    "Father, teach us the contentment that Paul described\u2014not the kind that arrives when we finally have enough, but the kind that comes from knowing you. Let this session form something in us, not just inform us.",
    ["Chapter 9", "Chapter 10"]),

    ...digIn(
      {
        ref: "Philippians 4:10\u201313",
        verse: "I have learned to be content whatever the circumstances. I know what it is to be in need, and I know what it is to have plenty. I have learned the secret of being content in any and every situation\u2026 I can do all this through him who gives me strength.",
        questions: [
          "Paul says he \u2018learned the secret.\u2019 What does that suggest about how contentment actually develops?",
          "Both need and plenty can disrupt contentment in different directions. Which one is more of a temptation for you right now?",
          "What role does \u2018him who gives me strength\u2019 play in contentment\u2014and how does that change the way you pursue it?",
        ]
      },
      {
        ref: "1 Timothy 6:6\u201310",
        verse: "But godliness with contentment is great gain. For we brought nothing into the world, and we can take nothing out of it. But if we have food and clothing, we will be content with that\u2026 For the love of money is a root of all kinds of evil.",
        questions: [
          "What does \u2018we brought nothing in and can take nothing out\u2019 do to the way you calculate what you actually need?",
          "Notice it\u2019s \u2018the love of money,\u2019 not money itself, that is \u2018a root of all kinds of evil.\u2019 What\u2019s the difference?",
          "What practical steps does this passage imply for someone who wants to grow in contentment?",
        ]
      }
    ),

    ...dailyReads([
      { verse: "But godliness with contentment is great gain. For we brought nothing into the world, and we can take nothing out of it.", ref: "1 Timothy 6:6\u20137",
        respond: "What does \u2018brought nothing in, take nothing out\u2019 do to how you hold what you currently have?" },
      { verse: "I have learned to be content whatever the circumstances.", ref: "Philippians 4:11",
        respond: "What season\u2014tight or abundant\u2014is forming contentment in you right now? What is it teaching?" },
      { verse: "When they measure themselves by themselves and compare themselves with themselves, they are not wise.", ref: "2 Corinthians 10:12",
        respond: "Where is the comparison loop most active in your life? What would it look like to get off that scale this week?" },
      { verse: "'What is that to you? You must follow me.'", ref: "John 21:22",
        respond: "Is there a comparison you\u2019re running right now that is distracting you from your own path? What would it mean to redirect?" },
      { verse: "Keep your lives free from the love of money and be content with what you have, because God has said, \u2018Never will I leave you; never will I forsake you.\u2019", ref: "Hebrews 13:5",
        respond: "The reason for contentment here is a promise about presence, not provision. How does that reframe what you actually need?" },
    ], "Write what God is stirring in you after this week\u2019s reading."),
  ];
}

// ── SESSION 5: THE GENEROSITY QUESTION ───────────────────
function session5() {
  return [
    ...sessionSplash("5","V","The Generosity Question","How Does Giving Change Everything?"),

    memVerse(
      "Each of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver.",
      "2 Corinthians 9:7"
    ),
    gap(80),
    body("Session 5 changes the direction of the conversation\u2014from holding to releasing, from receiving to giving. Generosity isn\u2019t a financial discipline you master. It\u2019s a person you become. And it starts not with how much you have but with what you\u2019ve already received: a God who gave first, at the highest possible cost, because of love. That changes everything about why and how you give.", 60, 60),
    pb(),

    ...storyPage(
      "Tyler",
      "The Shoes He Didn\u2019t Buy",
      "Tyler had been saving for three months for a specific pair of shoes. Every time he checked his balance it was like a countdown. He was close. Then a friend texted saying his family was going through something hard financially, and Tyler felt a pull he didn\u2019t expect and didn\u2019t really want.",
      "He went back and forth all day. The shoes were practically in his cart. But the pull didn\u2019t leave. Eventually he took part of what he\u2019d saved and gave it to his friend. Awkwardly, without much of an explanation. The shoes didn\u2019t happen.",
      "What he didn\u2019t expect was the shift that came a few days later. Not a feeling that he\u2019d done something impressive. More like: I wasn\u2019t giving away my money. I was using what God trusted me with to help someone else. That reframe was small. But it changed how he saw his wallet.",
      "The shoes would have been forgotten in two years. What I did instead\u2014I\u2019m still thinking about."
    ),

    ...getIn(
      "God gave first\u2014extravagantly, at the highest possible cost, before we had anything to offer. Does it feel different to give as a response rather than an obligation? What\u2019s the difference?",
      "Think about a time you gave something that genuinely cost you something. What happened\u2014and what did it do to how you saw your stuff?"
    ),

    ...watchPage(5, "As you watch Session 5, listen for the way generosity connects to identity, not just action. Notice what Jesus says about where treasure goes and where hearts follow. Write down what shifts in how you see giving\u2014not as a transaction but as a formation practice."),

    ...talkAboutIt([
      "Matthew 6:21 says treasure leads and heart follows\u2014not the other way around. What does that mean for how you start becoming more generous?",
      "What\u2019s the difference between giving because you feel guilty and giving because you\u2019ve received? What produces each, and what does each produce?",
      "What does a \u2018cheerful giver\u2019 actually look like day-to-day\u2014not as a spiritual ideal but as a real practice?",
      "If generosity is a person you become rather than a discipline you master, what does that person look like in five years?",
    ]),

    ...goDeeper([
      "Is your current experience of giving closer to obligation or response? What would need to change for it to move toward genuine cheerfulness?",
      "Acts 4:32 describes the early church: nobody claimed anything as their own. That\u2019s the natural result of a community that\u2019s genuinely answered the ownership question. What would your friend group or church look like if people actually lived that way?",
      "The widow\u2019s two coins were tiny in amount and massive in proportion. Jesus specifically noticed. What does that tell you about how God measures generosity?",
      "What is one non-financial form of generosity you could practice more\u2014time, attention, encouragement, presence?",
      "What is one specific act of generosity\u2014financial or otherwise\u2014you\u2019ve been sensing you should do but haven\u2019t yet?",
    ]),

    ...yourWorld(
      "Generosity isn\u2019t only money. It\u2019s how you move through every part of your world. Where do you have something to give\u2014and where might God be inviting you to give it?",
      [
        { title: "MONEY", sub: "What you earn and have saved" },
        { title: "TIME", sub: "What you could give that costs you" },
        { title: "ATTENTION", sub: "Genuine presence with someone who needs it" },
        { title: "SKILLS", sub: "Abilities you could use for others" },
        { title: "ENCOURAGEMENT", sub: "Words that cost nothing and mean everything" },
      ]
    ),

    ...thisWeeksChallenge([
      "Do one act of generosity this week that genuinely costs you something\u2014money, time, or comfort\u2014and do it without anyone knowing.",
      "Honor God with the first of what you earn or receive this week, not what\u2019s left over. Give before you plan everything else.",
      "Write a one-sentence \u2018generosity intention\u2019\u2014not a guilt resolution, but a genuine response to what God has given you.",
    ],
    "Father, you gave first. At the highest possible cost, because of love. Teach us to give freely\u2014not reluctantly, not under pressure\u2014as people who have genuinely received from you.",
    ["Chapter 11", "Chapter 12"]),

    ...digIn(
      {
        ref: "2 Corinthians 9:6\u20138",
        verse: "Remember this: Whoever sows sparingly will also reap sparingly, and whoever sows generously will also reap generously. Each of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver. And God is able to bless you abundantly, so that in all things at all times, having all that you need, you will abound in every good work.",
        questions: [
          "What is the agricultural image Paul is using\u2014and what does it imply about the nature of generosity?",
          "God loves a \u2018cheerful giver.\u2019 What produces cheerfulness in giving\u2014and what prevents it?",
          "What does \u2018having all that you need, you will abound in every good work\u2019 suggest about what abundance is actually for?",
        ]
      },
      {
        ref: "Luke 21:1\u20134",
        verse: "As Jesus looked up, he saw the rich putting their gifts into the temple treasury. He also saw a poor widow put in two very small copper coins. \u2018Truly I tell you,\u2019 he said, \u2018this poor widow has put in more than all the others. All these people gave their gifts out of their wealth; but she out of her poverty put in all she had to live on.\u2019",
        questions: [
          "Why does Jesus say the widow gave \u2018more\u2019\u2014what is he measuring that everyone else missed?",
          "What does this passage say about the relationship between the amount given and the significance of the giving?",
          "What does the widow\u2019s gift reveal about her theology\u2014what did she actually believe about God?",
        ]
      }
    ),

    ...dailyReads([
      { verse: "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.", ref: "John 3:16",
        respond: "God gave first, at the highest possible cost. How does that change the shape of your giving\u2014from obligation to response?" },
      { verse: "For where your treasure is, there your heart will be also.", ref: "Matthew 6:21",
        respond: "If you redirected some treasure toward something that mattered to God, where would you want your heart to end up?" },
      { verse: "One person gives freely, yet gains even more; another withholds unduly, but comes to poverty.", ref: "Proverbs 11:24",
        respond: "Have you ever experienced the paradox here\u2014that giving produced something unexpected? What happened?" },
      { verse: "Honor the Lord with your wealth, with the firstfruits of all your crops.", ref: "Proverbs 3:9",
        respond: "What would it mean to give \u2018first\u2019 rather than from what\u2019s left over\u2014what would that require, practically?" },
      { verse: "\u2018It is more blessed to give than to receive.\u2019", ref: "Acts 20:35",
        respond: "Do you actually believe this is true? What would it take for it to move from something you believe to something you live?" },
    ], "Write what God is stirring in you after this week\u2019s reading."),
  ];
}

// ── SESSION 6: THE IMPACT QUESTION ───────────────────────
function session6() {
  return [
    ...sessionSplash("6","VI","The Impact Question","How Do I Make an Impact Today, Tomorrow, and Eternally?"),

    memVerse(
      "Do not store up for yourselves treasures on earth\u2026 But store up for yourselves treasures in heaven, where moths and vermin do not destroy, and where thieves do not break in and steal.",
      "Matthew 6:19\u201320"
    ),
    gap(80),
    body("Session 6 is the capstone. It asks the biggest version of the ownership question: not just what you do with your money now, but what kind of life you\u2019re building, what legacy you\u2019re leaving, and what investments you\u2019re making that will still matter when everything temporary has proven not to be. This session doesn\u2019t end the conversation. It opens the rest of it.", 60, 60),
    pb(),

    ...storyPage(
      "Destiny",
      "Invest in What Lasts",
      "Destiny had a summer job that paid more than she\u2019d expected. She\u2019d thought she had a plan for it. But a few weeks in, she started asking a question she\u2019d never really asked before: ten years from now, which of the things I could do with this money will I actually be glad I did?",
      "Some of what she\u2019d been planning looked different through that lens. Some of it still made sense. A few things shifted entirely. She started thinking in a longer timeline than she was used to\u2014what would I want my relationship with money to look like when I\u2019m thirty? What habits am I forming right now that will either serve me or cost me?",
      "She gave more generously than she\u2019d planned, saved more deliberately than she\u2019d intended, and spent on some things she genuinely wouldn\u2019t regret. It wasn\u2019t a dramatic transformation. It was a reorientation\u2014a decision to start asking the longer-term question before the short-term impulse got to answer it first.",
      "I realized I\u2019d been making financial decisions for the version of me that exists today. I wanted to start making them for the version of me I actually want to become."
    ),

    ...getIn(
      "If someone who knew you well looked at your financial habits right now, what kind of legacy do they say you\u2019re building? What would you want them to see instead?",
      "What\u2019s one investment\u2014financial or otherwise\u2014you\u2019ve made that you\u2019re genuinely glad about? What made it worth it?"
    ),

    ...watchPage(6, "As you watch Session 6, listen for the difference between treasures that last and treasures that don\u2019t. Notice how Ron connects today\u2019s decisions to tomorrow\u2019s impact. Write down one thing that changes in how you see the relationship between what you do now and the life you\u2019re building."),

    ...talkAboutIt([
      "Matthew 6:19\u201320 doesn\u2019t say earthly treasure is evil\u2014it says it\u2019s temporary. What\u2019s the difference, and why does it matter for how you hold what you have?",
      "What does \u2018heavenly treasure\u2019 actually look like in practical terms\u2014not as an abstract spiritual concept but as real daily investment?",
      "Moses chose \u2018disgrace for the sake of Christ\u2019 over the treasures of Egypt. What made that a rational decision for him\u2014and what would a similar decision look like for you?",
      "What\u2019s the one thing from these six sessions you most want to carry forward into the rest of your life?",
    ]),

    ...goDeeper([
      "You\u2019re building a legacy right now\u2014not in the future when you have more. What does the person who sees your financial habits from the outside say you\u2019re building?",
      "What\u2019s the difference between living for an earthly finish line and living from a settled identity in God\u2019s ownership? Which one most describes how you\u2019ve been operating?",
      "Ron says the people who answer the ownership question differently show four things over time: contentment, confidence, clarity in communication, and consistency of behavior. Which of those do you most want to develop?",
      "If you wrote a one-sentence legacy statement\u2014the mark you want to leave with your life and resources\u2014what would it say?",
      "What\u2019s one specific commitment you want to make coming out of this six-week series? Name it. Write it. Tell someone.",
    ]),

    ...yourWorld(
      "Impact and legacy aren\u2019t just financial. Every circle of your life is a place where what you invest today produces something tomorrow. Where are you building something that will outlast you?",
      [
        { title: "PEOPLE", sub: "Who are you investing in that will carry it forward?" },
        { title: "FAITH", sub: "What are you doing to strengthen it for the long run?" },
        { title: "GENEROSITY", sub: "What are you giving that will ripple beyond you?" },
        { title: "WORK", sub: "What are you building that serves others?" },
        { title: "FAMILY", sub: "What are you modeling that will shape the next generation?" },
      ]
    ),

    ...thisWeeksChallenge([
      "Write your one-sentence legacy statement: \u201cThe mark I want to leave is ___.\u201d Carry it with you this week.",
      "Name one financial commitment you\u2019re making coming out of this series. Tell someone who will hold you to it.",
      "Do one thing this week that invests in something that will outlast you\u2014give, encourage, disciple, serve, or create something with staying power.",
    ],
    "Father, thank you for these six sessions. Thank you for what shifted. Thank you for what is still being formed. Teach us to invest in what lasts. Let our financial lives\u2014our actual habits, not just our stated values\u2014be a quiet testimony to a watching world that you are enough.",
    ["Chapter 13"]),

    ...digIn(
      {
        ref: "Matthew 6:19\u201321",
        verse: "Do not store up for yourselves treasures on earth, where moths and vermin destroy, and where thieves break in and steal. But store up for yourselves treasures in heaven, where moths and vermin do not destroy, and where thieves do not break in and steal. For where your treasure is, there your heart will be also.",
        questions: [
          "What are the specific vulnerabilities of earthly treasure that Jesus names? What does that say about its nature?",
          "If you take the principle seriously\u2014that treasure leads and heart follows\u2014what would you redirect to build more treasure in the lasting category?",
          "What does \u2018treasures in heaven\u2019 actually look like in practice? What kind of investments have that kind of staying power?",
        ]
      },
      {
        ref: "Hebrews 11:24\u201326",
        verse: "By faith Moses, when he had grown up, refused to be known as the son of Pharaoh\u2019s daughter. He chose to be mistreated along with the people of God rather than to enjoy the fleeting pleasures of sin. He regarded disgrace for the sake of Christ as of greater value than the treasures of Egypt, because he was looking ahead to his reward.",
        questions: [
          "Moses compared \u2018the fleeting pleasures of sin\u2019 to something better\u2014and chose the better thing. What was his basis for making that comparison?",
          "What does it mean to look \u2018ahead to your reward\u2019 in the way that shaped Moses\u2019 daily decisions?",
          "What would it look like for you to make one decision this week that prioritizes the lasting thing over the impressive thing?",
        ]
      }
    ),

    ...dailyReads([
      { verse: "Do not store up for yourselves treasures on earth\u2026 But store up for yourselves treasures in heaven.", ref: "Matthew 6:19\u201320",
        respond: "What is one earthly treasure you\u2019ve been over-investing in, and one heavenly treasure you\u2019ve been under-investing in?" },
      { verse: "By faith Moses\u2026 regarded disgrace for the sake of Christ as of greater value than the treasures of Egypt.", ref: "Hebrews 11:26",
        respond: "What is one \u2018treasure of Egypt\u2019 you\u2019re currently choosing that you sense you should trade for the lasting thing?" },
      { verse: "For we are God\u2019s handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.", ref: "Ephesians 2:10",
        respond: "The good works were prepared before you arrived at the moment. What prepared moment for impact are you walking toward this week?" },
      { verse: "The generous will themselves be blessed, for they share their food with the poor.", ref: "Proverbs 22:9",
        respond: "What would the \u2018blessed\u2019 described here look like in your actual life? What would you have to give to experience it?" },
      { verse: "Now to him who is able to do immeasurably more than all we ask or imagine, according to his power that is at work within us\u2014", ref: "Ephesians 3:20",
        respond: "Where do you want God to do \u2018immeasurably more\u2019 in your financial and generosity life? Ask him for it specifically." },
    ], "Write what God is stirring in you after all six sessions. What changed? What\u2019s your next step?"),
  ];
}

// ════════════════════════════════════════════════════════
//  COVER + INTRO PAGES
// ════════════════════════════════════════════════════════

const coverPage = [
  navyBanner([
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,60),
      children:[ta("GOD OWNS IT ALL",{size:64,bold:true,color:WHITE,font:"Arial"})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,80),
      children:[new TextRun({text:"Youth Edition",font:"Georgia",size:36,italics:true,color:GOLD})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(0,100),
      children:[new TextRun({text:"Six-Week Small Group Curriculum",font:"Georgia",size:26,italics:true,color:"B8D0E8"})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(80,0),
      children:[ta("RON BLUE  \u00b7  Ron Blue Institute",{size:20,color:"A0B8CC",font:"Arial"})] }),
  ]),
  gap(240),
  shade([
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(40,40),
      children:[t("\u201cMore than a money class, God Owns It All forms biblical stewards through honest group conversation and lasting transformation.\u201d",{size:23,italics:true,color:NAVY})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:sp(20,20),
      children:[ta("RICK WARREN",{bold:true,size:17,color:TEAL,font:"Arial"})] }),
  ], LB),
  pb(),
];

const contentsPage = [
  h2("Contents", NAVY),
  divider(),
  gap(80),
  ...[
    ["Session 1", "The Ownership Question", "What does it really mean if God owns it all?"],
    ["Session 2", "The Stewardship Question", "How do we learn faithfulness through stewardship?"],
    ["Session 3", "The Confidence Question", "Will I be okay?"],
    ["Session 4", "The Contentment Question", "How much is enough?"],
    ["Session 5", "The Generosity Question", "How does giving change everything?"],
    ["Session 6", "The Impact Question", "How do I make an impact today, tomorrow, and eternally?"],
  ].map(([s, t_, q]) =>
    new Table({
      width:{size:9360,type:WidthType.DXA}, columnWidths:[1800,7560],
      borders:{top:NO,bottom:{style:BorderStyle.SINGLE,size:2,color:"E5E7EB"},left:NO,right:NO,insideH:NO,insideV:NO},
      rows:[new TableRow({children:[
        new TableCell({width:{size:1800,type:WidthType.DXA},shading:{fill:LB,type:ShadingType.CLEAR},margins:{top:120,bottom:120,left:160,right:160},borders:{top:NO,bottom:NO,left:NO,right:NO},children:[
          new Paragraph({spacing:sp(0,20),children:[ta(s,{bold:true,size:17,color:TEAL})]}),
        ]}),
        new TableCell({width:{size:7560,type:WidthType.DXA},margins:{top:120,bottom:120,left:160,right:160},borders:{top:NO,bottom:NO,left:NO,right:NO},children:[
          new Paragraph({spacing:sp(0,20),children:[new TextRun({text:t_,font:"Georgia",size:22,bold:true,color:NAVY})]}),
          new Paragraph({spacing:sp(0,0),children:[new TextRun({text:q,font:"Georgia",size:20,italics:true,color:MGRAY})]}),
        ]}),
      ]})]
    })
  ),
  pb(),
];

const howToUsePage = [
  h2("How to Use This Guide"),
  divider(),
  gap(80),
  body("This is a six-session small group guide designed for middle school and high school students. Each session runs 60\u201375 minutes and includes every piece a leader or student needs to have a real, productive, and honest conversation about money, identity, and what it means to live like God actually owns everything.", 60, 80),
  h3("Each Session Includes:"),
  bul("A student story\u2014a real peer testimonial (or a story based on a real situation a student went through)"),
  bul("Get In\u2014a warm-up discussion and opening prayer"),
  bul("Group Rhythm & Agreement\u2014a group covenant to establish trust (Session 1 only)"),
  bul("Watch\u2014a video notes page for the teaching segment"),
  bul("Talk About It\u2014four questions to process the video as a group"),
  bul("Go Deeper\u2014five deeper questions for honest group conversation"),
  bul("Your World\u2014an application tool connecting the session to all areas of life"),
  bul("This Week\u2019s Challenge\u2014three action steps + closing prayer + reading plan"),
  bul("Dig In\u2014two passages with questions for additional study"),
  bul("Daily Reads\u2014five days of Scripture with RESPOND prompts between sessions"),
  gap(80),
  box([
    h3("A Note on Honesty"),
    body("This curriculum works when people answer honestly\u2014not when they answer impressively. No performing, no shame, no comparing. The best thing a leader can do is go first with a real answer. The best thing a student can do is trust the group with what\u2019s actually true."),
  ], LT, TEAL),
  gap(80),
  box([
    h3("A Note on the Videos"),
    body("Each session is designed to accompany a video teaching segment. The Watch page includes a prompt to focus attention before the video plays and space to write notes during it. The Talk About It questions connect directly back to the video content."),
  ], LG, GOLD),
  pb(),
];

// ════════════════════════════════════════════════════════
//  BUILD DOCUMENT
// ════════════════════════════════════════════════════════

const doc = new Document({
  numbering:{config:[
    {reference:"bullets",levels:[{level:0,format:LevelFormat.BULLET,text:"\u2022",alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:360}}}}]},
    {reference:"numbers",levels:[{level:0,format:LevelFormat.DECIMAL,text:"%1.",alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:720,hanging:360}}}}]},
  ]},
  styles:{default:{document:{run:{font:"Georgia",size:22}}}},
  sections:[{
    properties:{page:{size:{width:12240,height:15840},margin:{top:1080,right:1080,bottom:1080,left:1080}}},
    children:[
      ...coverPage,
      ...contentsPage,
      ...howToUsePage,
      ...session1(),
      ...session2(),
      ...session3(),
      ...session4(),
      ...session5(),
      ...session6(),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('/mnt/user-data/outputs/GOIA_Youth_6Session_SmallGroup_Curriculum.docx', buf);
  console.log('Done.');
});
