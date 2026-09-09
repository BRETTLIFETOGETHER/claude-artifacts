const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, PageBreak
} = require('docx');
const fs = require('fs');

const C = {
  white:"FFFFFF", dgray:"222222", mgray:"555555", lgray:"F5F5F5",
  g1:"1F3864", g2:"2E5DA6", g3:"D6E4F7",
  m1:"1A4731", m2:"276B4A", m3:"C8EDD8",
  l1:"7B3F00", l2:"B35A00", l3:"FFE0B2",
};

const sp = (b=80,a=80)=>new Paragraph({spacing:{before:b,after:a},children:[new TextRun("")]});
const pb = ()=>new Paragraph({children:[new PageBreak()]});

function rule(color){
  return new Paragraph({border:{bottom:{style:BorderStyle.SINGLE,size:12,color,space:1}},spacing:{before:60,after:60}});
}

function bookCover(title,sub,versionLabel,dark,med,light){
  const brd={style:BorderStyle.SINGLE,size:4,color:dark};
  return [
    sp(240,0),
    new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[9360],rows:[
      new TableRow({children:[new TableCell({
        borders:{top:brd,bottom:brd,left:brd,right:brd},
        shading:{fill:light,type:ShadingType.CLEAR},
        margins:{top:240,bottom:240,left:360,right:360},
        children:[
          new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:60},
            children:[new TextRun({text:title,bold:true,size:64,font:"Arial",color:dark})]}),
          new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:60},
            children:[new TextRun({text:sub,size:26,font:"Arial",color:med,italics:true})]}),
          rule(med),
          new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:60,after:0},
            children:[new TextRun({text:versionLabel,bold:true,size:30,font:"Arial",color:dark})]})
        ]
      })]})
    ]}),
    sp(120,120)
  ];
}

function sessionBanner(num,title,dark){
  const brd={style:BorderStyle.SINGLE,size:6,color:dark};
  return new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[9360],rows:[
    new TableRow({children:[new TableCell({
      borders:{top:brd,bottom:brd,left:brd,right:brd},
      shading:{fill:dark,type:ShadingType.CLEAR},
      margins:{top:120,bottom:120,left:240,right:240},
      children:[new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:0},
        children:[new TextRun({text:`SESSION ${num}  ·  ${title}`,bold:true,size:28,font:"Arial",color:C.white})]})]
    })]})
  ]});
}

function sessionMeta(subtitle,desc,verses,med,light){
  const brd={style:BorderStyle.SINGLE,size:2,color:med};
  return new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[9360],rows:[
    new TableRow({children:[new TableCell({
      borders:{top:brd,bottom:brd,left:brd,right:brd},
      shading:{fill:light,type:ShadingType.CLEAR},
      margins:{top:120,bottom:120,left:240,right:240},
      children:[
        new Paragraph({spacing:{before:0,after:60},children:[new TextRun({text:subtitle,bold:true,size:24,font:"Arial",color:med})]}),
        new Paragraph({spacing:{before:0,after:80},children:[new TextRun({text:desc,size:20,font:"Arial",color:C.dgray,italics:true})]}),
        new Paragraph({spacing:{before:0,after:0},children:[
          new TextRun({text:"Key Verses:  ",bold:true,size:20,font:"Arial",color:med}),
          new TextRun({text:verses,size:20,font:"Arial",color:C.mgray})
        ]})
      ]
    })]})
  ]});
}

function dayTable(days,dark,med,light){
  const hbrd={style:BorderStyle.SINGLE,size:2,color:dark};
  const hb={top:hbrd,bottom:hbrd,left:hbrd,right:hbrd};
  const cbrd={style:BorderStyle.SINGLE,size:1,color:"CCCCCC"};
  const cb={top:cbrd,bottom:cbrd,left:cbrd,right:cbrd};
  function hCell(t,w){return new TableCell({borders:hb,width:{size:w,type:WidthType.DXA},shading:{fill:dark,type:ShadingType.CLEAR},margins:{top:80,bottom:80,left:100,right:100},children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:t,bold:true,size:18,font:"Arial",color:C.white})]})]})}
  function dCell(t,w,sh,bold,col){return new TableCell({borders:cb,width:{size:w,type:WidthType.DXA},shading:{fill:sh||C.white,type:ShadingType.CLEAR},margins:{top:70,bottom:70,left:100,right:100},children:[new Paragraph({children:[new TextRun({text:t,bold:bold,size:18,font:"Arial",color:col||C.dgray})]})]})}
  const rows=[new TableRow({children:[hCell("Day",480),hCell("Day Title",1840),hCell("Subtitle",1840),hCell("Description & Activity",2980),hCell("Key Verses",1220)]})];
  for(const [d,ti,su,de,ve] of days){
    rows.push(new TableRow({children:[
      dCell(d,480,light,true,med),
      dCell(ti,1840,C.lgray,true,dark),
      dCell(su,1840,C.white,false,C.mgray),
      dCell(de,2980,C.white,false,C.dgray),
      dCell(ve,1220,light,false,med),
    ]}));
  }
  return new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[480,1840,1840,2980,1220],rows});
}

function descBox(text,med,light){
  const brd={style:BorderStyle.SINGLE,size:2,color:med};
  return new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[9360],rows:[
    new TableRow({children:[new TableCell({
      borders:{top:brd,bottom:brd,left:brd,right:brd},
      shading:{fill:light,type:ShadingType.CLEAR},
      margins:{top:100,bottom:100,left:200,right:200},
      children:[
        new Paragraph({spacing:{before:0,after:40},children:[new TextRun({text:"Outline Overview",bold:true,size:21,font:"Arial",color:med})]}),
        new Paragraph({spacing:{before:0,after:0},children:[new TextRun({text,size:19,font:"Arial",color:C.dgray,italics:true})]})
      ]
    })]})
  ]});
}

// ════════════════════════════════════════════════════════════════
// GOD OWNS IT ALL — 3 OUTLINES
// ════════════════════════════════════════════════════════════════
const GOIA = [
{
  label:"OUTLINE A",
  name:"Who Owns It? — A Classic Stewardship Journey",
  desc:"A thorough, session-by-session walk through the full sweep of biblical money management. Best for first-time groups who want a comprehensive exploration of all six sessions in sequence.",
  sessions:[
    {num:1,title:"PERSPECTIVE",sub:"Everything You Own Belongs to Someone Else",desc:"The entire financial life shifts when one question is answered correctly: who owns it? This session establishes God's ownership as the non-negotiable foundation of every financial decision.",verses:"1 Chr. 29:14 · Ps. 24:1 · Luke 16:10–13",days:[
      ["Day 1","The Most Important Money Question","Who Owns What You Have?","Is your money yours, or are you managing it for God? Examine how you truly answer this in daily spending decisions. Write your honest answer before reading any further.","1 Chr. 29:14"],
      ["Day 2","What the Bible Says About Ownership","God's Claim on All Creation","Survey the key ownership scriptures. Underline everything God claims. Explore the implications of those claims for your bank account, your home, and your investments.","Ps. 24:1; Ps. 50:9–12"],
      ["Day 3","The Steward vs. The Owner","Dad's Car and God's Resources","Study the 'Dad's Car' illustration. Examine the practical difference between believing you own something vs. holding it in trust for God. Where are you acting as owner today?","Matt. 25:14–21"],
      ["Day 4","Behavior Follows Belief","Your Worldview Drives Your Wallet","Explore the principle: lasting change requires belief change. Identify one financial behavior rooted in a worldly belief about money. What would the behavior look like if the belief changed?","Luke 16:13; Prov. 23:7"],
      ["Day 5","Three Ways God Uses Money","Tool, Test, and Testimony","Discover the three purposes God has for money in your life. Which one is most active in your current financial situation? What is He developing in you through it?","Phil. 4:12; Jas. 1:5–6"],
      ["Day 6","An Eternal Perspective","Holding Lightly What You Cannot Keep","Study Matthew 6:19–21 as a meditation. What would it look like to hold your possessions this week with genuine openness and lightness? Practice it today.","Matt. 6:19–21; Heb. 11:26"],
      ["Day 7","Perspective Capstone","Writing Your Stewardship Declaration","Review the session. Write your personal stewardship declaration — a signed, dated statement of who owns your resources and what that means for how you will manage them tomorrow.","Ps. 24:1; Luke 16:13"],
    ]},
    {num:2,title:"PRINCIPLES",sub:"Five Timeless Rules That Never Change",desc:"Biblical principles are always right, always relevant, and never going to change. This session grounds every financial decision in an unshakeable framework that produces confidence regardless of economic conditions.",verses:"2 Tim. 3:16–17 · Matt. 7:24–27 · Prov. 3:9–10",days:[
      ["Day 8","Why Biblical Finance Never Goes Out of Date","Principles Built to Last","Contrast the constantly-changing financial landscape with the never-changing wisdom of Scripture. Why is something that is 'always right' so rare — and so valuable?","2 Tim. 3:16–17; Matt. 7:24–27"],
      ["Day 9","Principle 1: Spend Less Than You Earn","The Non-Negotiable Foundation","Study the first and most critical principle. Calculate your actual monthly margin. What single change would most increase it? Every other financial success depends on this one habit.","Prov. 21:20; Luke 14:28"],
      ["Day 10","Principle 2: Avoid Debt","The Danger of Financial Bondage","Examine what Scripture says about borrowing. Classify your current debts: wise, neutral, or dangerous. Assess which ones are limiting your obedience and generosity today.","Prov. 22:7; Rom. 13:8"],
      ["Day 11","Principles 3 & 4: Save and Set Goals","Margin and Direction for the Future","Study the principles of building margin and setting long-term goals. Identify your current margin and write one goal that would require genuine faith to achieve.","Prov. 13:11; Hab. 2:2"],
      ["Day 12","Principle 5: Give Generously","The Principle That Changes Everything","Explore why generosity is foundational, not optional. Move from duty-driven to faith-driven giving. Draft a giving percentage that requires trust rather than comfort.","2 Cor. 9:6–8; Mal. 3:10"],
      ["Day 13","The Five Uses of Money","No Independent Financial Decisions","Map your spending against the pie diagram: Live, Give, Owe, Grow, Tax. Examine why every category affects every other and identify the one that is most out of alignment.","Eccl. 5:10; 1 Tim. 6:17–19"],
      ["Day 14","Principles Capstone","Building on Rock, Not Sand","Review all five principles. Identify which one is most out of alignment in your life right now. Write one concrete, dated change you will make this week to realign it.","Matt. 7:24–27"],
    ]},
    {num:3,title:"LIVE",sub:"How Much Is Enough? The Freedom Question",desc:"Lifestyle is the largest financial decision most people never consciously make. This session confronts the Prosperity Paradox and invites every participant to define 'enough' before their circumstances define it for them.",verses:"1 Tim. 6:6–10 · Phil. 4:11–13 · Heb. 13:5",days:[
      ["Day 15","The Prosperity Paradox","Why More Often Means Less Freedom","Accumulating more can produce less freedom, not more. Explore why the American Dream often creates financial captivity rather than financial peace. Where have you experienced this?","1 Tim. 6:6–10; Eccl. 5:10–12"],
      ["Day 16","What People Really Want","Success, Significance, and Security","Examine the three things people pursue through money — and why money cannot deliver any of them. Which one most drives your financial decisions? Name it specifically.","Matt. 6:31–33; Ps. 62:10"],
      ["Day 17","The Right Lifestyle for a Christian","Provision, Contentment, and Enjoyment","Study the three biblical lifestyle categories. What does 'the lifestyle God has provided for me' mean in your specific, practical context? Write your honest current answer.","1 Tim. 5:8; 1 Tim. 6:8,17"],
      ["Day 18","How Much Is Enough? Part 1","Defining Your Lifestyle Number","Identify your actual monthly lifestyle cost. Is that number chosen intentionally or have circumstances chosen it for you? What would intentional look like?","Phil. 4:11–13; Prov. 30:8–9"],
      ["Day 19","How Much Is Enough? Part 2","The Accumulation Question","What do you need to accumulate to sustain your defined lifestyle indefinitely? How does an eternal perspective change what that 'enough' number should actually be?","Heb. 13:5; 1 Tim. 6:17"],
      ["Day 20","Delayed Gratification","The Habit That Unlocks Every Other Goal","Delayed gratification is the mechanism behind margin, saving, and generosity. Identify one area where immediate consumption is blocking a greater goal. Name the trade-off explicitly.","Prov. 21:5; Eccl. 5:12"],
      ["Day 21","Live Capstone","Setting Your Lifestyle Ceiling","Write your 'how much is enough' number and a one-sentence explanation of why. This is one of the most defining financial decisions you will ever make. Sign and date it.","Phil. 4:11–13"],
    ]},
    {num:4,title:"GIVE",sub:"From Obligation to Overflow — The Joy of Generosity",desc:"Giving is the overflow of a heart that has genuinely surrendered ownership to God. This session moves participants from duty-based tithing to joyful, strategic, Spirit-led generosity.",verses:"Matt. 6:19–21 · 2 Cor. 9:6–8 · Luke 12:34",days:[
      ["Day 22","Why We Give — The Motivation Matters","Obligation, Fear, Love, or Faith?","Examine the four main motivations for giving. Which motivation is currently driving your giving? What would faith-driven generosity actually look like in your budget?","2 Cor. 9:7; 1 John 3:17"],
      ["Day 23","The Treasure Principle","Store Up Treasure in Heaven","Study Jesus' teaching on treasure and the heart. Where are you storing your treasure currently? Identify one practical way to begin sending more of it ahead today.","Matt. 6:19–21; Luke 12:33–34"],
      ["Day 24","Proportionate Giving","Percentage vs. Amount","Explore the biblical case for proportionate giving. Calculate what 10%, 15%, and 20% of your gross income looks like as a monthly number. Which percentage would require genuine faith?","Deut. 16:17; Prov. 3:9–10"],
      ["Day 25","Planned Giving","Generosity Requires a Plan","Planned giving is premeditated generosity. Write a giving plan today: amount, recipient, and frequency. If giving is reactive, it will always be what is left over.","1 Cor. 16:2; 2 Cor. 9:5"],
      ["Day 26","Precommitted Giving","Faith Obligations That Fuel Obedience","Precommitting to giving creates a framework of faith that shapes all other spending. Make one precommitted giving pledge today — one you must trust God to fulfill.","Eccl. 5:4–5; Neh. 10:32"],
      ["Day 27","The Cheerful Giver","The Portrait of Generous Faith","Study the portrait of the giver God loves — not reluctant, not under compulsion. What would it take for your giving to become genuinely joyful rather than obedient?","2 Cor. 9:7–8; Prov. 11:24–25"],
      ["Day 28","Give Capstone","Your Complete Giving Plan","Finalize your giving plan: current percentage, one-year target, two recipients, one stretch goal, and a commitment to precommitted giving. Sign it as an act of faith.","2 Cor. 9:6–8"],
    ]},
    {num:5,title:"OWE",sub:"Debt, Borrowing & the Path to Freedom",desc:"Debt is not a sin, but it is dangerous in ways most people underestimate. This session brings biblical clarity to borrowing, classifies current debt, and charts a practical path toward the freedom God intends.",verses:"Prov. 22:7 · Rom. 13:8 · Ps. 37:21",days:[
      ["Day 29","What Scripture Actually Says About Debt","Biblical Clarity on Borrowing","Survey every major biblical text on debt. Distinguish between warnings, permissions, and wisdom. What does the Bible actually command vs. caution vs. forbid about borrowing?","Prov. 22:7; Rom. 13:8; Ps. 37:21"],
      ["Day 30","The Three Debt Categories","Wise, Neutral, or Dangerous?","Classify every debt you carry: wise (asset-building), neutral (manageable consumer), dangerous (bondage debt). This single exercise can change how urgently you approach your debt.","Prov. 22:26–27; Hab. 2:6–7"],
      ["Day 31","The Five Dangers of Debt","Why Debt Is Riskier Than You Know","Study the five dangers: compounding, trap, mortgaging the future, presuming on tomorrow, denying God a chance to work. Which danger is most actively present in your life?","Prov. 22:7; Luke 14:28–30"],
      ["Day 32","The Four Borrowing Questions","A Framework for Every Debt Decision","Apply the four questions to any debt you currently carry or are considering: Does it make economic sense? Are both spouses at peace? Can it be undertaken with spiritual confidence? What goal does it serve?","Prov. 3:5–6; 1 Cor. 7:23"],
      ["Day 33","The Road to Debt Freedom","A Plan, Not Just a Prayer","List your debts in order. Identify the first one to eliminate. Write the behavioral change required to eliminate it within 12 months. Commit to it publicly with an accountability partner.","Ps. 37:21; Prov. 13:7"],
      ["Day 34","Hope, Not Shame","God's Grace in Financial Failure","Explore the message of hope for those overwhelmed by debt. Debt does not define identity. Assess where you are, make a plan, and trust God's grace for both the journey and the destination.","Isa. 43:18–19; Rom. 8:1"],
      ["Day 35","Owe Capstone","Your Debt Freedom Declaration","Write a debt freedom declaration: your complete debt list, elimination timeline, behavioral commitment, and the date you are trusting God to make you debt-free.","Rom. 13:8; Gal. 5:1"],
    ]},
    {num:6,title:"GROW",sub:"Kingdom Wealth — Building with an Open Hand and an Eternal Eye",desc:"The final session completes the study: wealth built on God's principles is deployed for God's purposes. Grow is not about accumulation — it is about faithfulness, clarity, consistency, and a legacy that outlasts your life.",verses:"Matt. 25:14–21 · 1 Tim. 6:17–19 · Prov. 13:22",days:[
      ["Day 36","Grow with Kingdom Purpose","What Is Wealth Actually For?","Write your answer to this question before reading any commentary: If God owns it all, what is the purpose of the wealth He has entrusted to you? Let that answer shape the rest of the session.","Matt. 25:14–21; 1 Tim. 6:17–19"],
      ["Day 37","Sequential Investing","First Things First — Always","Study the five-step sequential strategy. Plot where you are in the sequence: consumer debt, emergency fund, savings, diversified investing, long-term goals. What does your next step require?","Prov. 21:5; Luke 16:10"],
      ["Day 38","Confidence Through Principles","Why Biblical Investors Sleep at Night","Review all five principles and assess how consistently you are living each one. Which principle, applied more faithfully, would produce the most confidence in your financial life?","Jas. 1:5; Prov. 3:5–6"],
      ["Day 39","Clarity and Consistency","The Two Habits That Compound Over Decades","Are your financial goals written and shared? Identify one area of financial inconsistency. Write a specific 30-day commitment to make it consistent. Small faithfulness compounds enormously.","Luke 16:10; 1 Cor. 4:2"],
      ["Day 40","Full-Study Capstone","Your Complete Stewardship Covenant","Review all six sessions. Write your stewardship covenant: who owns it, how you manage it, what you give, what you owe, and what kingdom purpose you are growing toward. Sign it.","Matt. 25:21; 1 Tim. 6:17–19"],
    ]},
  ]
},
{
  label:"OUTLINE B",
  name:"Stewardship as Discipleship — A Spiritual Formation Approach",
  desc:"Frames each session around spiritual formation rather than financial mechanics. Each day engages the heart before addressing the habit. Ideal for groups that want to go deep on the spiritual and devotional dimensions of money.",
  sessions:[
    {num:1,title:"PERSPECTIVE",sub:"The Surrender That Changes Everything",desc:"Before any financial tool matters, a theological question must be settled: have you genuinely surrendered ownership? This session approaches financial perspective as an act of worship, not a financial strategy.",verses:"Ps. 24:1 · Deut. 8:17–18 · Luke 12:15–21",days:[
      ["Day 1","A Confession Before a Plan","Admitting You Don't Own What You Think You Do","Begin not with a budget but with a confession. What would it mean to genuinely believe that everything you call yours is actually God's? Write what tomorrow would look like if you lived that belief.","Ps. 24:1; Job 1:21"],
      ["Day 2","The Danger of Forgetting","When Prosperity Produces Amnesia","Deuteronomy warns: prosperity causes people to forget God's provision and claim credit for their own success. Where has this happened in your financial story? Name it specifically.","Deut. 8:11–18; Hos. 13:6"],
      ["Day 3","Rich Toward God","The Parable That Should Unsettle You","Examine the Rich Fool parable. What does it mean to be 'rich toward God' rather than rich in possessions? Write what that difference would look like in your budget this month.","Luke 12:15–21; 1 Tim. 6:17–19"],
      ["Day 4","Stewardship Cannot Be Faked","Your Checkbook as Your Spiritual Autobiography","Engage with Ron Blue's insight that the checkbook reveals actual spiritual priorities. Review last month's spending as a spiritual document. What does it say about who you actually serve?","Matt. 6:21; Luke 16:11"],
      ["Day 5","Three Ways God Uses Money","Tool, Test, and Testimony","Which of the three purposes is God primarily using money for in your life right now — to accomplish something, to test your faith, or to display His faithfulness to others?","Phil. 4:12; Jas. 1:2–4"],
      ["Day 6","Holding What You Cannot Keep","An Eternal Perspective on Temporary Wealth","What would it look like to hold your possessions this week with genuine openness? Not with denial but with the lightness of someone who knows they are managing what belongs to Another.","Matt. 6:19–21; Heb. 11:26"],
      ["Day 7","Perspective Capstone","The Act of Surrender","Write a prayer of surrender over your finances. Name every specific financial asset and obligation. Place each one before God. Sign and date it as a declaration of stewardship over ownership.","1 Chr. 29:14; Luke 16:13"],
    ]},
    {num:2,title:"PRINCIPLES",sub:"Wisdom That Is Always True — Even When Culture Lies",desc:"The spiritual discipline of financial wisdom: applying biblical principles is not about intelligence or income — it is about obedience to a wisdom that transcends every economic cycle.",verses:"Prov. 3:5–6 · 2 Tim. 3:16–17 · Jas. 1:5",days:[
      ["Day 8","Why Human Wisdom Fails","The Shifting Sands of Financial Advice","Contrast the constantly-changing financial landscape with the never-changing wisdom of Scripture. Review the five principles. Why is 'always right' so rare — and so spiritually significant?","2 Tim. 3:16–17; Isa. 55:8–9"],
      ["Day 9","Earning More Than Spending as Spiritual Discipline","Faithfulness in the Smallest Things","Approach spending less than you earn as a spiritual discipline, not an accounting exercise. What does faithfulness with small amounts reveal about your readiness for greater responsibility?","Luke 16:10–11; Prov. 21:20"],
      ["Day 10","The Spiritual Weight of Debt","Bondage, Trust, and Freedom","Explore debt as a spiritual condition — not just a financial one. How does debt affect your sense of freedom to obey, to give, and to respond to God's unexpected direction in your life?","Prov. 22:7; 1 Cor. 7:23"],
      ["Day 11","Margin as a Form of Faith","The Space Where God Can Move","Margin is not just a financial buffer — it is spiritual breathing room. Is your financial life so tight that there is no room for God to interrupt, redirect, or call you to something new?","Prov. 13:11; Phil. 4:19"],
      ["Day 12","Goals as Declarations of Trust","Faith Written Down and Dated","Approach financial goal-setting as a spiritual act of trust. What goals would you set if you genuinely believed God was your provider? Write three of them with dates and specific amounts.","Hab. 2:2; Jer. 29:11"],
      ["Day 13","Generosity as Spiritual Warfare","Giving Breaks the Power of Money","Jesus talks more about money than almost any other topic. Generosity is not just obedience — it is a declaration that money does not have power over you. What would that declaration look like?","Matt. 6:24; Luke 16:13; Mal. 3:10"],
      ["Day 14","Principles Capstone","Living the Upside-Down Kingdom Economics","Where does following these principles most sharply contradict the financial values of the culture around you? Write your commitment to maintain that tension as a form of witness.","Matt. 7:24–27"],
    ]},
    {num:3,title:"LIVE",sub:"Contentment — The Learned Art That Breaks Every Financial Chain",desc:"Contentment is not a personality trait — it is a learned discipline. Paul says he learned it. This session approaches lifestyle choices as a spiritual formation issue, not merely a budgeting exercise.",verses:"Phil. 4:11–13 · 1 Tim. 6:6 · Heb. 13:5",days:[
      ["Day 15","The Secret Paul Discovered","What Contentment Actually Is — and Isn't","Study Philippians 4:11–13 slowly and carefully. Contentment is not apathy — it is a learned peace in all circumstances. What circumstances are most challenging your contentment right now?","Phil. 4:11–13; Heb. 13:5"],
      ["Day 16","Godliness with Contentment","The Real Return on Investment","Explore 1 Timothy 6:6 as a financial statement: godliness with contentment is great gain. What would it look like to evaluate your financial life with this as the primary return metric?","1 Tim. 6:6–8; Luke 12:15"],
      ["Day 17","The Idol of More","When Enough Is Never Enough","Examine how consumer culture and comparison fuel financial discontent. Identify the specific 'more' that most drives your spending. What spiritual hunger is it trying — and failing — to feed?","Eccl. 5:10; Prov. 30:15–16"],
      ["Day 18","What God Actually Promises","Provision, Not Luxury","Study what God actually promises regarding provision. He promises daily bread, not abundance. How does this reshape what you define as need vs. want in your household?","Matt. 6:11,31–33; Phil. 4:19"],
      ["Day 19","The Freedom of Simplicity","Less Is Often Spiritually More","Choosing a simpler lifestyle creates financial freedom — and freedom creates more room for generosity, obedience, and joy. What would one act of simplification look like in your home this week?","1 Tim. 6:8; Matt. 5:3"],
      ["Day 20","Gratitude as a Financial Strategy","The Practice That Rewires Discontent","List ten specific financial blessings you have been taking for granted. Sit with the list for ten minutes. How does this inventory change your desires and your spending behavior?","1 Thess. 5:18; Ps. 103:2"],
      ["Day 21","Live Capstone","Settling the Enough Question Once and for All","Write your answer to 'How much is enough?' — not as a math problem but as a spiritual declaration. Name the lifestyle God has provided for you and commit to living within it.","Phil. 4:11–13"],
    ]},
    {num:4,title:"GIVE",sub:"Generosity as a Spiritual Discipline — The Practice of Open Hands",desc:"Giving is not primarily a financial decision — it is a spiritual one. This session approaches generosity as a discipline that must be practiced, planned, and protected from the tyranny of the urgent.",verses:"2 Cor. 9:7 · Luke 21:1–4 · Acts 2:44–45",days:[
      ["Day 22","The Theology of Open Hands","Giving as a Response to Grace","Ground all giving in theology, not obligation. We give because we were given to (2 Cor. 8:9). How does the gift of the gospel change the category of giving from duty to delight?","2 Cor. 8:9; 9:15; Luke 7:47"],
      ["Day 23","The Widow's Offering","Percentage Over Amount","Meditate on Luke 21:1–4. God evaluates giving by what it costs you as a percentage of all you have — not by the amount. How does this reframe evaluate your current giving?","Luke 21:1–4; 2 Cor. 8:12"],
      ["Day 24","Storing Treasure — The Eternal ROI","Investing in What Lasts Forever","Study heavenly treasure not as metaphor but as economic reality. What return does Jesus promise for generous givers? Is this a promise you are actually acting on in your financial plan?","Matt. 6:19–21; Luke 12:33–34"],
      ["Day 25","Giving and the Heart","Generosity Flows From What You Believe","Study 2 Corinthians 9:6–8 as a window into the cheerful giver's heart. What would you need to believe differently about God for your giving to become genuinely joyful? Write it.","2 Cor. 9:6–8; Prov. 11:24–25"],
      ["Day 26","The Discipline of Planned Giving","Generosity Is Rarely an Accident","If you wait to give what is left over, it will never come. Build giving into the first line of your budget as an act of first-fruits trust. Write the plan today.","1 Cor. 16:2; Prov. 3:9–10"],
      ["Day 27","Generosity in the Household","When a Family Becomes a Giving Culture","How can your household become a giving culture where generosity is taught, modeled, and celebrated? What is one way you will teach generosity to the next generation this month?","Acts 2:44–45; Acts 4:32–35"],
      ["Day 28","Give Capstone","Your Giving Covenant","Write your personal giving covenant: the percentage you will give, the recipients you will support, and the spiritual motivation behind it. Sign it as a declaration of surrender.","2 Cor. 9:7"],
    ]},
    {num:5,title:"OWE",sub:"Debt as a Spiritual Condition — Finding Freedom Through Biblical Truth",desc:"Debt is rarely just a financial problem. It is often a symptom of deeper issues: fear, impatience, comparison, or lack of trust. This session approaches debt freedom as a spiritual journey.",verses:"Rom. 13:8 · Prov. 22:7 · Gal. 5:1",days:[
      ["Day 29","The Spiritual Weight of What We Owe","Debt as Bondage, Not Just a Balance","Explore debt as a condition, not just a number. How does financial debt affect your sense of spiritual freedom — your ability to respond to God, to give spontaneously, or to change direction?","Prov. 22:7; Gal. 5:1"],
      ["Day 30","How Debt Happens to Good People","The Path From Wisdom to Bondage","Study the patterns that lead believers into debt bondage: lifestyle inflation, comparison, impatience, emergencies. Which pattern most accurately describes how you arrived at your current debt?","Prov. 22:26–27; Eccl. 5:5"],
      ["Day 31","Presuming on the Future","Why Debt Is a Theological Problem","Explore the spiritual presumption embedded in most consumer debt: assuming tomorrow will look like today. How does this contradict a life of trust and daily dependence on God?","Jas. 4:13–15; Luke 14:28–30"],
      ["Day 32","God's Grace in Financial Failure","There Is No Condemnation in the Gospel","Study how the gospel speaks to financial failure and debt bondage — with hope, not condemnation. If debt has you paralyzed by shame, write a prayer of repentance and receive grace today.","Isa. 43:18–19; Rom. 8:1"],
      ["Day 33","The Long Obedience of Debt Elimination","Small Steps, Sustained Over Time","Explore debt elimination as a long obedience in the same direction, not a sprint. List your debts. Choose the first to eliminate. Commit to it regardless of how many months it takes.","Prov. 6:1–5; Ps. 37:21"],
      ["Day 34","What Debt-Free Living Actually Creates","Room to Obey, Room to Give","What would financial freedom allow you to do — give, serve, obey — that debt is currently preventing? Let that vision fuel your commitment to the elimination plan from yesterday.","Gal. 5:1; 1 Cor. 7:23"],
      ["Day 35","Owe Capstone","Writing Your Freedom Story in Advance","Write the story of your debt-free life as if it has already happened — what changed, how long it took, what obedience it required, and what freedom followed. Then go live it.","Rom. 13:8"],
    ]},
    {num:6,title:"GROW",sub:"Faithfulness, Not Abundance — The Spiritual Measure of Financial Growth",desc:"The final session reframes financial growth entirely. The goal is not a larger portfolio — it is faithfulness, clarity, consistency, and a legacy that outlasts your life and outlasts your name.",verses:"Matt. 25:21 · 1 Tim. 6:17–19 · Luke 16:10",days:[
      ["Day 36","The Measure God Uses","Faithful, Not Wealthy","The master's praise is 'well done, faithful servant' — not 'well done, wealthy servant.' Study the parable of the talents as a faithfulness framework. What does this reframe for your financial goals?","Matt. 25:14–21; Luke 16:10"],
      ["Day 37","Sequential Investing as Spiritual Wisdom","Do First Things First","Study the Sequential Investing Strategy as an exercise in biblical wisdom: do first things first, eliminate what limits obedience, build what creates freedom to serve. Where are you in the sequence?","Prov. 21:5; Luke 14:28"],
      ["Day 38","When Saving Becomes Hoarding","The Idol of Security","Examine the thin line between wise saving and trusting in accumulated wealth. When does a safety net become a substitute for trusting God? How much is enough to accumulate?","Luke 12:19–21; 1 Tim. 6:17"],
      ["Day 39","Legacy — More Than Money","What You Leave Behind","What does a kingdom legacy look like: wisdom transferred to children, resources directed to kingdom work, habits modeled for generations. What do you want your estate to say about your life?","Prov. 13:22; Ps. 112:1–3"],
      ["Day 40","Full-Study Capstone: Stewardship Covenant","40 Days Later — Who Are You Now?","Review all six sessions. Write your full stewardship covenant: what you believe about ownership, how you manage, what you give, what you owe, and what you are growing toward — as an act of worship.","Matt. 25:21; 1 Tim. 6:17–19"],
    ]},
  ]
},
{
  label:"OUTLINE C",
  name:"From Financial Anxiety to Financial Contentment — A Healing Journey",
  desc:"Designed for groups carrying financial fear, shame, or stress. Each session addresses the emotional and spiritual obstacle before the practical principle. Ideal for groups in financial difficulty or significant life transition.",
  sessions:[
    {num:1,title:"PERSPECTIVE",sub:"You Are Not Your Net Worth — Finding Identity Before Finances",desc:"Financial anxiety is often rooted in a false identity: I am what I own, earn, or owe. Before the numbers can change, the story must change. This session begins with grace, not goals.",verses:"Luke 12:15 · Heb. 13:5 · Rom. 8:38–39",days:[
      ["Day 1","Naming the Anxiety","What Money Is Doing to Your Peace","Give honest voice to your financial fears. This is not the time for answers — only for naming the anxiety before God without editing it. Write your three biggest money fears as they actually are.","Phil. 4:6–7; Ps. 55:22"],
      ["Day 2","You Are Not What You Own","Confronting the Lie at the Root","Confront the cultural lie that net worth equals self-worth. Study what Scripture says about identity in Christ vs. identity in possessions. Where have you confused the two? Name it.","Luke 12:15; Gal. 2:20"],
      ["Day 3","The Ownership Question as Liberation","Releasing What Was Never Yours","Reframe the ownership question not as a theological demand but as an invitation to freedom. If God owns it, you are no longer responsible for outcomes — only for faithfulness. Does this bring relief?","1 Chr. 29:14; Ps. 24:1"],
      ["Day 4","God's Track Record","Building Faith on a Provision Audit","Conduct a personal provision audit. List ten specific ways God has provided for you financially — large and small. Let the record speak against your anxiety.","Matt. 6:25–32; Ps. 23:1"],
      ["Day 5","Money as Tool, Test, and Testimony","Reframing Your Financial Difficulty","What if your current financial struggle is not a punishment but a test or a testimony in progress? Study all three purposes. How does that reframe change your posture toward your situation?","Jas. 1:2–4; Phil. 4:12"],
      ["Day 6","Temporal Problems, Eternal Perspective","Seeing With Heaven's Eyes","What does it look like to hold your financial situation in light of eternity — not with denial but with genuine hope? Explore the difference between ignoring a problem and trusting God through it.","2 Cor. 4:17–18; Matt. 6:19–21"],
      ["Day 7","Perspective Capstone","From Fear to Trust — One Step at a Time","Write a prayer of surrender: name every financial fear, place each one before God, and declare His ownership. You are a steward. The outcomes belong to Him. Sign and date the prayer.","Heb. 13:5; Ps. 46:1"],
    ]},
    {num:2,title:"PRINCIPLES",sub:"Simple Rules for a Complex World — Starting Where You Are",desc:"Financial principles are not just for people who have their finances together — they are the path out for those who do not. This session applies the five principles with compassion for those in difficult circumstances.",verses:"Prov. 3:5–6 · Matt. 7:24–27 · 2 Tim. 3:16–17",days:[
      ["Day 8","Principles Are Lifelines, Not Grades","The Rock Is Available Today","Reframe the five principles not as a report card but as a lifeline. You may be building on sand right now — but the rock is available today. Identify where you will begin rebuilding.","Matt. 7:24–27; Jas. 1:5"],
      ["Day 9","The Smallest Possible Step","Starting With One Dollar Less","For those in financial difficulty, creating any margin at all is the first victory. Identify the smallest immediate step toward spending less than you earn. Start there. Only there.","Prov. 21:20; Luke 16:10"],
      ["Day 10","Debt Honestly Named","The First Step Is Seeing Clearly","Create a complete, honest list of every debt you carry. This is not a moment of shame — it is a moment of clarity. You cannot make a plan for what you refuse to look at.","Prov. 27:23; Luke 14:28"],
      ["Day 11","The $1,000 Emergency Fund","The Discipline That Changes Everything","For many in financial stress, saving $1,000 changes the entire trajectory. It ends the cycle of debt-for-emergencies. Write a 90-day plan to reach this one goal. Make it specific.","Prov. 21:5; Jas. 4:13–15"],
      ["Day 12","Faith Goals for Anxious Times","Hope Written Down and Dated","Setting financial goals when your situation feels unstable is not denial — it is faith. Write one financial goal you would set if you genuinely believed God would provide. Make it measurable.","Jer. 29:11; Hab. 2:2"],
      ["Day 13","Giving When You Have Almost Nothing","Why Generosity Is Especially Critical in Need","Study the widow of Zarephath. Even in lack, a posture of generosity signals trust and breaks the grip of scarcity fear. Even $5 given intentionally is an act of faith worth making.","1 Kgs. 17:10–16; Mark 12:41–44"],
      ["Day 14","Principles Capstone","Your One-Page Starting Point","Write your financial starting point: your current margin, your debt list, your first goal, and your giving commitment — however small. This is your foundation. Sign it.","Matt. 7:24–27"],
    ]},
    {num:3,title:"LIVE",sub:"The Courage to Say Enough — Contentment as an Act of Defiance",desc:"In a culture that never stops selling more, choosing contentment is an act of spiritual courage. This session addresses lifestyle anxiety directly and gives participants permission to stop the comparison game.",verses:"Phil. 4:11–13 · Heb. 13:5 · 1 Tim. 6:6–8",days:[
      ["Day 15","The Comparison Trap","Why You Are Always Behind","Name the specific comparisons — neighbors, social media, family — that most fuel your financial restlessness. What would you need to stop looking at to break the comparison cycle?","Prov. 14:30; Gal. 6:4"],
      ["Day 16","What Contentment Is Not","Three Misunderstandings to Clear Up","Address the three most common misunderstandings: contentment is not passivity, not poverty, not settling for less. It is a learned trust that does not require changed circumstances before bringing peace.","Phil. 4:11–13; 1 Tim. 6:6"],
      ["Day 17","The Lifestyle Gap","What You Have vs. What You Are Trying to Have","Name your current lifestyle honestly — income, housing, spending. Then name the lifestyle you are trying to maintain. How large is the gap, and what anxiety is it producing every month?","1 Tim. 6:8; Luke 12:15"],
      ["Day 18","Choosing Your Lifestyle Instead of Inheriting One","The Most Important Financial Decision You Never Made","Most people never consciously choose a lifestyle — it simply happens. This day invites a deliberate choice. What lifestyle will you choose, based on God's provision rather than cultural pressure?","Prov. 30:8–9; Phil. 4:11"],
      ["Day 19","How Complexity Makes Things Worse","The Prosperity Paradox in Your Life","Lifestyle simplification is not deprivation — it is freedom. Identify one area where simplifying would reduce your monthly anxiety. Write what the simplified version would look like.","Eccl. 5:10–12; 1 Tim. 6:9–10"],
      ["Day 20","'He Will Never Leave You'","The Promise That Holds When Nothing Else Does","Study Hebrews 13:5 as a financial promise. God's presence is the ultimate financial security. Sit with this promise for ten minutes before answering: Is this enough for you today?","Heb. 13:5; Ps. 23:1–3"],
      ["Day 21","Live Capstone","Your Declaration of Freedom","Write and sign a Declaration of Enough: your chosen lifestyle, your monthly budget ceiling, and the reason why. This is a courageous act of counter-cultural obedience.","Phil. 4:11–13"],
    ]},
    {num:4,title:"GIVE",sub:"Giving Through Fear — Breaking Free from Scarcity Thinking",desc:"For those in financial stress, generosity can feel impossible. But scarcity thinking is often what keeps people stuck. This session addresses the fear behind withholding and invites a courageous first step toward freedom.",verses:"2 Cor. 9:6–8 · Mark 12:41–44 · Prov. 11:24–25",days:[
      ["Day 22","The Scarcity Mindset","Why Fear Makes You Hold On Tighter","Where does the scarcity belief come from in your story? Examine the conviction that if you give, there will not be enough. When did you first learn to fear that money would run out?","Prov. 11:24–25; Matt. 25:24–25"],
      ["Day 23","The Faith of the Widow","When Giving Everything Is Not Reckless","Meditate on both widows — Zarephath and the temple. Both gave from emptiness. Both were sustained. What is God asking you to trust Him with financially right now?","1 Kgs. 17:10–16; Mark 12:41–44"],
      ["Day 24","The Sowing-Reaping Principle","Why Generosity Is the Most Reliable Financial Strategy","Study 2 Corinthians 9:6. This is not a prosperity formula — it is a spiritual reality. Generous people generally experience God's provision more directly. What does your sowing history show?","2 Cor. 9:6–8; Prov. 11:24"],
      ["Day 25","Your First Step Back to Generosity","Starting Exactly Where You Are","For those who have stopped giving due to financial stress, design a restart. Even $10/month given intentionally is a declaration that scarcity thinking no longer has the final word. Write your restart plan.","2 Cor. 8:12; Luke 21:3–4"],
      ["Day 26","Planning Protects Generosity","If You Don't Plan It, It Won't Happen","Unplanned giving is almost always crowded out by urgent expenses. Write a giving plan — however small — that is the first line of your budget. Make it non-negotiable before any other spending.","1 Cor. 16:2; Prov. 3:9–10"],
      ["Day 27","Cheerfulness Is Coming","Giving as a Journey, Not a Destination","Cheerful giving is not always where you start — it is where the discipline takes you. Commit to the practice even before the emotion follows. Joy will catch up with obedience.","2 Cor. 9:7; Gal. 6:9"],
      ["Day 28","Give Capstone","Your Courageous Giving Commitment","Write your giving commitment for the next 90 days: a percentage, a recipient, and a declaration that scarcity thinking no longer controls your giving. Sign it.","2 Cor. 9:6–8"],
    ]},
    {num:5,title:"OWE",sub:"From Shame to Freedom — The Gospel and Your Debt",desc:"For many participants, debt carries significant shame. This session addresses the emotional and spiritual weight of debt before the practical plan — because shame must be confronted and released before a plan can be sustained.",verses:"Isa. 43:18–19 · Rom. 8:1 · Prov. 22:7",days:[
      ["Day 29","Naming the Shame","The Weight You Are Carrying","Give language for the emotional weight of debt: the anxiety, the hiding, the exhaustion of carrying a secret. This is not the time to fix it — it is the time to name it before God and receive grace.","Ps. 55:22; Isa. 43:18–19"],
      ["Day 30","Debt Does Not Define You","The Gospel and Your Balance Sheet","Your debt does not determine your identity, your value, or your future. Study how the gospel speaks to financial failure — not with condemnation but with a new beginning.","Rom. 8:1; 2 Cor. 5:17"],
      ["Day 31","Understanding How Debt Got Its Power","Not Condemnation — Explanation","Study the five dangers of debt as an explanation, not a condemnation. Understanding how debt works breaks the shame of not knowing why it feels so inescapable.","Prov. 22:7; Jas. 4:13–15"],
      ["Day 32","The Honest List","Clarity Is the Beginning of Freedom","Create a complete, unflinching debt inventory. This is a courageous act of love toward yourself. You cannot make a plan for what you continue to hide. List every debt, balance, and rate.","Luke 14:28–30; Prov. 27:23"],
      ["Day 33","A Plan Is More Powerful Than Shame","One Clear Next Step","Once you see the complete picture, map a path forward. The goal is not perfection — it is one clear next step. Identify the first debt to eliminate and the one behavioral change it requires.","Ps. 40:1–3; Prov. 13:7"],
      ["Day 34","You Were Not Meant to Do This Alone","Support on the Road to Freedom","Who do you need to tell? Who can walk with you? Explore the role of community, accountability, and counsel in debt freedom. Identify one person to invite into your journey.","Prov. 15:22; Gal. 6:2"],
      ["Day 35","Owe Capstone","Your Freedom Declaration","Write a freedom declaration: name every debt, commit to the plan, and declare the date you are trusting God to reach zero consumer debt. Give it to your accountability partner.","Rom. 13:8; Gal. 5:1"],
    ]},
    {num:6,title:"GROW",sub:"Rebuilding With Purpose — From Survival to Kingdom Legacy",desc:"The final session is for those beginning to come out of financial survival mode and needing a vision for what comes next — not just financial recovery, but financial purpose and a story worth telling.",verses:"Joel 2:25 · Luke 16:10 · Prov. 13:22",days:[
      ["Day 36","God Restores What the Locusts Ate","A Vision for Financial Rebuilding","Study Joel 2:25 as a financial promise. God can restore years of financial loss. Write your story of what was lost — and then write the story of what you believe God will restore.","Joel 2:25; Ps. 126:4–6"],
      ["Day 37","First Things First","The Sequential Strategy for Those Starting Over","Study the Sequential Investing Strategy as the road map for rebuilding: eliminate debt first, emergency fund, savings, then investing. Write your current step and specific next step.","Prov. 21:5; Luke 16:10"],
      ["Day 38","Small Faithfulness Compounded","The Habit That Rewrites Your Financial Story","Identify one small, daily financial habit that, sustained for five years, would transform your financial position. It does not have to be large. It has to be consistent.","Luke 16:10; Matt. 25:21"],
      ["Day 39","Your Story Can Help Someone","A Kingdom Purpose for Your Recovery","Your financial story — including its difficulty — is being redeemed for kingdom purposes. Who could your story help? How could your recovery become a testimony that changes another family?","Rom. 8:28; 2 Cor. 1:3–4"],
      ["Day 40","Full-Study Capstone: Your New Story","40 Days Later — Who Are You Now?","Review all six sessions. Write your new financial story: what you believe about ownership, how you are managing it, what you are giving, and where you are going. This is the beginning.","Luke 16:10; Matt. 25:21"],
    ]},
  ]
},
];

// ════════════════════════════════════════════════════════════════
// MASTER YOUR MONEY — 3 OUTLINES
// ════════════════════════════════════════════════════════════════
const MYM = [
{
  label:"OUTLINE A",
  name:"The Financial Contentment Journey — A Step-by-Step Plan",
  desc:"Follows the natural progression of the book: Why / What the Bible Says / Where You Are / What to Avoid / How to Plan / How to Give. Best for those new to biblical financial planning who want a sequential, comprehensive guide.",
  sessions:[
    {num:1,title:"WILL I EVER HAVE ENOUGH?",sub:"Ch. 1–2: Confronting Financial Anxiety with Biblical Truth",desc:"The first session names the anxiety most people carry and replaces it with four unchanging biblical principles. The economy is uncertain; God is not. Every spending decision is a spiritual decision.",verses:"Phil. 4:11–13 · Matt. 6:25–33 · 1 Tim. 6:6–10",days:[
      ["Day 1","The Question Everyone Is Asking","Will I Ever Have Enough?","Introduce the three financial questions: Will I ever have enough? Will it continue to be enough? How much is enough? Write your honest current answers to all three without filtering them.","Phil. 4:11–13; Matt. 6:25–33"],
      ["Day 2","Why the Economy Cannot Be Your Anchor","God Is More Reliable Than the Market","Review the preface: five editions, five different economic crises, same principles. The economy is never reliable but God always is. Where is your financial confidence actually anchored?","Ps. 62:5–8; Prov. 3:5–6"],
      ["Day 3","Principle 1: God Owns It All","Every Spending Decision Is a Spiritual Decision","Study the most foundational principle. What changes when you genuinely believe every purchase you make is a stewardship decision rather than a personal one? Name one purchase from this week.","Ps. 24:1; 1 Chr. 29:14"],
      ["Day 4","Principle 2: Money Is a Growth Tool","Tool, Test, and Testimony","God uses money in your life as a tool, test, or testimony. Which is He primarily using it for in your current financial situation? What is He developing in you through it?","Phil. 4:12; Jas. 1:2–4"],
      ["Day 5","Principles 3 & 4: Amount and Action","Faithfulness Is the Measure — Faith Must Move","The amount does not matter; faithfulness does. And faith that does not act is not real faith. What faithful action is your current financial situation requiring of you right now?","Luke 16:10; Jas. 2:14–17"],
      ["Day 6","Biblical vs. Worldly Financial Worldview","Which Foundation Are You Building On?","Contrast the worldly view (money = security, significance, success) with the biblical view (money = stewardship opportunity). Which worldview is actually driving your financial decisions today?","Matt. 6:24; Luke 16:13"],
      ["Day 7","Session 1 Capstone","Your Financial Foundation Statement","Write your financial foundation statement: what you believe about money, ownership, and God's role in your finances. This is your anchor for the entire 40-day journey.","Phil. 4:11–13"],
    ]},
    {num:2,title:"WHERE AM I?",sub:"Ch. 3, 6: Financial Planning Overview and Your Current Reality",desc:"You cannot plan where you are going until you honestly know where you are. This session provides both the conceptual framework for financial planning and the practical tools to assess your present situation honestly.",verses:"Prov. 27:23 · Luke 14:28–30 · Prov. 21:5",days:[
      ["Day 8","The Purpose of Financial Planning","Goals and Values — Not Just Growth","The objective of money is not more money — it is achieving goals and reflecting values. Write your financial life purpose statement: what is money for in your specific life?","Prov. 21:5; Hab. 2:2"],
      ["Day 9","The Five Uses of Money","No Independent Financial Decisions","Map your current spending against the five uses: Live, Give, Owe (debt), Owe (taxes), Grow. Estimate your actual percentages. Which use is disproportionate and why?","Eccl. 5:10; 1 Tim. 6:17–19"],
      ["Day 10","The 4-Step Planning Process","Summarize, Set Goals, Increase Margin, Control Flow","Study the four planning steps. Which step have you never actually completed? Commit to completing it during this 40-day plan. Write what completing it would require.","Prov. 3:5–6; Luke 14:28–30"],
      ["Day 11","Your Net Worth Statement","Knowing What You Actually Have","Complete your personal net worth statement: assets minus liabilities. Does the number surprise you? Where is the majority of your wealth? Where is your greatest liability?","Prov. 27:23; Luke 14:31–32"],
      ["Day 12","Your Cash Flow Summary","The Story Your Money Tells Every Month","Complete your monthly cash flow summary. What does it reveal that your intentions have not? Where is the leak you have been ignoring? Name it specifically.","Luke 16:10–11; Prov. 27:23"],
      ["Day 13","Your Insurance Gap","Protecting What Is Entrusted to You","Review your current life, disability, and property insurance. Identify the single most important coverage gap. Write the name of the person you will call this week to address it.","Prov. 22:3; 1 Tim. 5:8"],
      ["Day 14","Session 2 Capstone","Your Complete Financial Snapshot","Combine your net worth statement, cash flow summary, and insurance review into one page. Write an honest one-paragraph assessment of where you stand financially today.","Luke 14:28–30"],
    ]},
    {num:3,title:"WHAT SHOULD I AVOID?",sub:"Ch. 5, 8: Dangers of Debt and the Most Common Financial Mistakes",desc:"Most financial plans fail not from lack of information but from predictable, avoidable mistakes and the silent weight of debt. This session names the two greatest enemies of financial faithfulness.",verses:"Prov. 22:7 · Rom. 13:8 · Prov. 22:3",days:[
      ["Day 15","The Five Dangers of Debt","Why Debt Is Riskier Than You Think","Study all five dangers: compounding works against you, debt is a trap, it mortgages your future, presumes on tomorrow, and can deny God a chance to work. Which danger is most present for you?","Prov. 22:7; Jas. 4:13–15"],
      ["Day 16","Biblical Questions for Every Borrowing Decision","Four Tests That Protect You","Apply the four borrowing questions to your largest current debt. Then apply them to any debt you are currently considering. What do they reveal about your financial decision-making?","Prov. 3:5–6; 1 Cor. 7:23"],
      ["Day 17","Debt Is Not the End","Hope and a Path Forward","Study Ron and Michael Blue's reflections on debt and shame. Your debt does not define you. Write a personal response to any shame you carry: receive grace, make a plan, take one step today.","Isa. 43:18–19; Rom. 8:1"],
      ["Day 18","The Consumptive Lifestyle","The Mistake That Blocks Every Other Goal","Examine your lifestyle honestly. Where is consumption outpacing your values and income? Identify one specific area of lifestyle inflation to address in the next 30 days.","1 Tim. 6:8–10; Luke 12:15"],
      ["Day 19","The Budget-less Life","Why Failing to Plan Is Planning to Fail","If you do not have a budget, commit to building one this week. If you do, identify the category most off-track and write one change you will make to bring it back into alignment.","Prov. 21:5; Luke 14:28"],
      ["Day 20","The Vehicle Trap","Decisions That Follow You for Years","Calculate the true 5-year cost of your most recent vehicle purchase (payments + depreciation + insurance). What would you do differently with what you now know?","Prov. 22:3; Luke 14:28"],
      ["Day 21","Session 3 Capstone","Your Danger and Mistake Audit","Write your personal danger audit: your top two debt dangers, your most significant financial mistake, and one behavioral change for each that begins today.","Prov. 22:7; Rom. 13:8"],
    ]},
    {num:4,title:"HOW CAN I SUCCEED?",sub:"Ch. 4, 7: Guaranteed Financial Success and Setting Faith Goals",desc:"Financial success is guaranteed for those who apply biblical principles consistently and set goals anchored in God's purposes. This session makes both the math and the faith concrete.",verses:"Hab. 2:2 · Prov. 21:5 · Jer. 29:11",days:[
      ["Day 22","The Guarantee","Guaranteed Financial Success Is Available to Everyone","Study Ron Blue's bold claim. What conditions are attached to the guarantee? Are you currently meeting them? Where is the gap between the conditions and your present behavior?","Prov. 21:5; Matt. 7:24–27"],
      ["Day 23","The Power of Compounding","Small Faithfulness, Enormous Results","Study time value of money and compounding. Run the opportunity cost calculation for one recurring expense in your life. What is its 10-year compounding cost?","Prov. 13:11; Luke 16:10"],
      ["Day 24","Opportunity Cost","Every Dollar Has an Alternate Destiny","Identify two monthly expenses that, redirected toward savings or giving, would build significant margin within five years. Write the numbers. Write the redirection plan.","Prov. 21:20; Eccl. 5:12"],
      ["Day 25","Why Goals Matter","Direction, Motivation, and the Will of God","Study the four reasons for financial goals. Which reason is most compelling for you personally? Write your financial life purpose statement in one clear, specific sentence.","Hab. 2:2; Jer. 29:11"],
      ["Day 26","Setting Faith Goals","Goals That Require God to Show Up","Work through the four-step goal process. Write three goals: one 90-day, one 1-year, one 5-year. Each must be specific, measurable, and faith-requiring — meaning it depends on God's provision.","Hab. 2:2; Phil. 4:13"],
      ["Day 27","Overcoming Goal-Setting Barriers","Why Most People Never Write Their Goals","Study the four barriers: fear of failure, time assumption, uncertainty, and absence of process. Which one has stopped you before? Write specifically how you will defeat it today.","Jas. 4:13; Prov. 3:5–6"],
      ["Day 28","Session 4 Capstone","Your Faith Financial Goals Document","Finalize three written, dated, measurable faith goals. Share them with one accountability partner this week. Pray over them together before submitting them to God.","Hab. 2:2; Phil. 4:13"],
    ]},
    {num:5,title:"HOW DO I PLAN?",sub:"Ch. 9–11: Your Personal Financial Plan, Budget, and Tax Strategy",desc:"This session moves from vision to execution: designing the actual integrated plan, building and controlling the budget, and understanding taxes as a stewardship responsibility before God.",verses:"Prov. 3:9–10 · Luke 14:28 · Rom. 13:6–7",days:[
      ["Day 29","The Financial Planning Blueprint","Connecting Goals to Behavior","Study the Financial Planning Diagram and the Bob and Laura case study. Use their framework to identify three specific action steps that would increase your monthly margin.","Prov. 21:5; Luke 14:28–30"],
      ["Day 30","Building Your Budget","Estimate, Record, Build, Control","Follow the four-step budget-building process. Build your complete monthly budget today — no categories skipped. Giving goes on the first line. This is your financial operating plan.","Prov. 3:9–10; 1 Cor. 16:2"],
      ["Day 31","Controlling the Flow","Your Budget Only Works If You Use It","Set up your tracking system today. Choose the simplest tool you will actually use consistently. Name your accountability partner and share your budget with them this week.","Luke 16:10–11; Prov. 27:23"],
      ["Day 32","Scripture and Taxes","What the Bible Says About Your Obligation","Study all relevant tax passages. What is your current attitude toward taxes — biblical or cultural? Write one sentence that aligns your perspective on taxes with Romans 13.","Rom. 13:6–7; Matt. 22:21"],
      ["Day 33","Legal Tax Reduction","The Stewardship of Not Paying More Than You Owe","Identify two legal tax reduction strategies you are not currently using. Write a specific plan to implement both within the next 90 days.","Prov. 22:3; 1 Tim. 6:17"],
      ["Day 34","The Integrated Plan","Connecting Budget, Debt, Goals, and Taxes","Review your budget, debt plan, tax strategy, and faith goals together. Do they tell a coherent story? Write the one integration step that would most improve the alignment.","Prov. 21:5; Luke 14:28"],
      ["Day 35","Session 5 Capstone","Your Complete Living Financial Plan","Compile your full plan: net worth, cash flow, budget, debt elimination timeline, tax plan, and faith goals. Commit to reviewing it every quarter.","Prov. 27:23; Luke 14:28"],
    ]},
    {num:6,title:"HOW CAN I GIVE?",sub:"Ch. 12–14: Investing, Estate Planning, and the Life of Generous Giving",desc:"The capstone session brings the entire book to its purpose: money mastered is money available for generosity. Investment strategy, estate planning, and giving are presented as integrated acts of stewardship.",verses:"Matt. 25:14–21 · Prov. 13:22 · 2 Cor. 9:6–8",days:[
      ["Day 36","Accumulation vs. Preservation","Knowing Which Phase You Are In","Study the two investment phases. Which are you in — accumulation or preservation? How does that phase change your investment strategy, your risk tolerance, and your giving capacity?","Luke 16:10; Prov. 21:5"],
      ["Day 37","The Sequential Investing Strategy","First Things First — Always","Study all five sequential steps. Plot your current position in the sequence. Write your next step and the specific behavioral action required to complete it.","Prov. 21:5; Luke 14:28"],
      ["Day 38","Stewardship After Death","Your Will Is Your Final Financial Statement","Do you have a current will? Does it reflect your stated values? Review it today. If changes are needed, write the name of the attorney you will contact this week.","Prov. 13:22; 1 Tim. 5:8"],
      ["Day 39","Giving Living — When, Where, How Much","The Capstone of Mastered Money","Work through all three giving questions. Write your complete giving plan: timing, allocation to recipients, percentage commitment, and a 5-year giving growth vision.","2 Cor. 9:6–8; Mal. 3:10"],
      ["Day 40","40-Day Capstone: Master Your Money Covenant","Mastered Money Is Generous Money","Review all six sessions. Write your Master Your Money covenant: foundation, financial plan, giving commitment, and investment strategy — one page, signed and dated.","Matt. 25:21; 2 Cor. 9:6–8"],
    ]},
  ]
},
{
  label:"OUTLINE B",
  name:"The Master Money Questions — A Question-Driven Discovery Journey",
  desc:"Organizes the entire book around six driving questions rather than chapter sequence. Each session answers one fundamental question every person asks about money. Best for self-directed learners and those who respond to inquiry-based approaches.",
  sessions:[
    {num:1,title:"GOD AND MONEY",sub:"Ch. 1–2: What Does God Actually Have to Do With My Finances?",desc:"Before financial mechanics, a more fundamental question: Is there a connection between faith and finances? This session establishes the theological case that every financial decision is a spiritual one — not metaphorically, but actually.",verses:"Luke 16:11 · Ps. 24:1 · Phil. 4:6–7",days:[
      ["Day 1","The God and Money Connection","Why Faith and Finance Cannot Be Separated","Examine the claim: every spending decision is a spiritual decision. Do you actually believe this? Where have you been keeping God out of your financial life? Name the specific area.","Luke 16:11; Matt. 6:24"],
      ["Day 2","Four Principles You Can Trust","The Unchanging Foundation in a Changing World","Study the four principles. How do they hold up against the most recent economic crisis you experienced personally? What would have been different if you had applied them then?","2 Tim. 3:16–17; Matt. 7:24–27"],
      ["Day 3","Tool, Test, or Testimony","Which Is God Doing in Your Life Right Now?","Apply all three categories to your current financial situation. Write a paragraph on what you believe God is doing with your money right now — and how you should respond.","Phil. 4:12; Jas. 1:2–4"],
      ["Day 4","Two Worldviews, One Wallet","Which Story Is Your Money Telling?","Contrast the two worldviews explicitly. Then review last month's spending. Which worldview does it reflect? Where is the gap between your stated beliefs and your financial behavior?","Matt. 6:24; Luke 16:13"],
      ["Day 5","Will I Ever Have Enough?","Naming the Anxiety, Finding the Answer","Journal your three financial fears honestly. Then study the biblical answer. Does the answer satisfy you? What would it take to actually live from that answer, not just know it?","Phil. 4:11–13; Heb. 13:5"],
      ["Day 6","A Faith Financial Goal","Declaring What You Believe About God's Provision","Study the faith goal framework. Write one financial goal that you could only achieve if God shows up. This is not wishful thinking — it is an act of declared trust.","Hab. 2:2; Jer. 29:11"],
      ["Day 7","Session 1 Capstone","Your Financial Creed","Write a personal financial creed: five sentences about what you believe about God and money. This is the foundation everything else will be built on for the rest of this 40-day journey.","Ps. 24:1; Phil. 4:11–13"],
    ]},
    {num:2,title:"WHERE AM I?",sub:"Ch. 3, 6: Your Money Map — Understanding Your Present Reality",desc:"You cannot navigate toward financial health without an honest assessment of where you are. This session provides the diagnostic tools and the spiritual courage to look at the complete picture.",verses:"Prov. 27:23 · Luke 14:28 · Lam. 3:40",days:[
      ["Day 8","The Cost of Financial Avoidance","What Happens When We Stop Looking","Explore why financial avoidance is so common and so costly. What are you currently not looking at? What would happen if you looked at your complete financial picture today?","Luke 14:28–30; Prov. 27:23"],
      ["Day 9","The Five Uses of Money","Mapping Where Every Dollar Goes","Learn the five-use framework and map your current spending percentages. Which category is most surprising? Which is most out of alignment with your stated values?","1 Tim. 6:17–19; Eccl. 5:10"],
      ["Day 10","Your Net Worth Statement","Assets, Liabilities, and the Real Picture","Complete your full net worth statement. Sit with the number honestly. What does it reveal? What does it conceal? What trajectory are you on if nothing changes in the next five years?","Prov. 27:23; Luke 14:31–32"],
      ["Day 11","Your Cash Flow Summary","The Monthly Story of Your Financial Life","Complete your monthly cash flow summary. Where is the margin? Where is the leak? Is your monthly cash flow moving you toward your goals or consistently away from them?","Luke 16:10–11; Prov. 27:23"],
      ["Day 12","Your Insurance Picture","Protecting What Is Entrusted to You","Review all insurance coverage. Is what God has placed in your care adequately protected? Identify the most critical gap and a realistic timeline to address it this month.","Prov. 22:3; 1 Tim. 5:8"],
      ["Day 13","The 4-Step Planning Process","From Snapshot to Strategy","Study the four steps: summarize present, set goals, increase margin, control cash flow. Which step is the most underdeveloped in your financial life right now?","Prov. 21:5; Luke 14:28"],
      ["Day 14","Session 2 Capstone","Your Honest One-Page Financial Map","Compile your net worth, cash flow, insurance summary, and planning gaps into one page. Share it with your spouse or accountability partner. Honesty is the beginning of health.","Prov. 27:23"],
    ]},
    {num:3,title:"WHAT SHOULD I AVOID?",sub:"Ch. 5, 8: The Dangers and Mistakes That Derail Financial Plans",desc:"Most financial plans fail not from bad information but from predictable, avoidable mistakes and the silent accumulation of debt. This session names the enemies of financial health before they can do more damage.",verses:"Prov. 22:7 · Prov. 22:3 · Eccl. 5:10",days:[
      ["Day 15","The Five Dangers of Debt","From Trap to Bondage — Understanding the Full Picture","Study all five dangers carefully. Which one do you feel most acutely right now? Write a paragraph on what debt is currently costing you beyond the monthly payment amount.","Prov. 22:7; Hab. 2:6–7"],
      ["Day 16","Is Debt Ever Acceptable?","Applying the Four Borrowing Questions","Apply the four questions to every current debt and to any debt you are considering. Create a simple matrix categorizing each debt: wise, neutral, or dangerous.","Prov. 3:5–6; Jas. 4:13–15"],
      ["Day 17","Your Debt Plan","From Awareness to Action in 24 Hours","Write a complete debt list: name, balance, rate, minimum payment. Choose your elimination method. Identify the first debt to eliminate and the change required to do it in 12 months or less.","Ps. 37:21; Prov. 22:26–27"],
      ["Day 18","The Lifestyle Trap","How Consumption Quietly Steals Your Future","Study the consumptive lifestyle mistake. Identify the three spending categories where your lifestyle is most inconsistent with your stated values. Name one you will change this month.","1 Tim. 6:8–10; Luke 12:15"],
      ["Day 19","Why Your Budget Keeps Failing","The No-Budget Mistake and How to Finally Fix It","Study the budget failure patterns. Diagnose why past budget attempts have failed in your life. Choose the simplest possible system and commit to just 30 days with it.","Prov. 21:5; Luke 14:28"],
      ["Day 20","Decisions That Follow You for Years","Cars, Houses, and Long-Tail Consequences","Study the vehicle decision mistake in detail. Examine your most recent major purchase. What long-tail financial consequences is it currently producing? What will you do differently next time?","Prov. 22:3; Luke 14:28–30"],
      ["Day 21","Session 3 Capstone","Your Mistake and Danger Elimination Plan","Write your danger and mistake report: your two most dangerous financial patterns, your complete debt list, and one change for each that begins today — not tomorrow.","Prov. 22:7; Prov. 22:3"],
    ]},
    {num:4,title:"HOW CAN I SUCCEED?",sub:"Ch. 4, 7: The Power of Compounding and Faith-Driven Financial Goals",desc:"Financial success is not luck, income level, or intelligence. It is the compounding result of consistent, principle-based decisions made over time — guided by goals that are anchored in God's purposes.",verses:"Prov. 21:5 · Hab. 2:2 · Prov. 13:11",days:[
      ["Day 22","The Guarantee Explained","Why Success Is Available to Anyone Who Applies the Principles","What conditions are required for guaranteed financial success? Are you currently meeting them? Where is the gap between the conditions and your present daily behavior?","Prov. 21:5; Matt. 7:24–27"],
      ["Day 23","The Power of Compounding","The Math That Makes Patience Profitable","Study the compounding principle with real numbers from your own life. Calculate the compounding value of one behavioral change — saving, giving, debt reduction — sustained for 10 years.","Prov. 13:11; Eccl. 11:4"],
      ["Day 24","Opportunity Cost","Every Dollar Has a Competing Destiny","Run the opportunity cost exercise for three current regular expenses. Which one, redirected, would most change your financial trajectory? Write the specific redirection plan.","Prov. 21:20; Luke 16:10"],
      ["Day 25","Why You Need Written Goals","The Purpose of Financial Direction in a Life of Faith","Study all four reasons for financial goals. Do you have written financial goals right now? If not, identify the single biggest barrier and address it specifically today.","Hab. 2:2; Prov. 3:5–6"],
      ["Day 26","The Four-Step Goal Process","From Prayer to Plan to Action","Work through the goal-setting process. Write three faith goals: a 90-day goal, a 1-year goal, and a 5-year goal. Each one must be specific, measurable, and faith-requiring.","Jer. 29:11; Hab. 2:2"],
      ["Day 27","Goals That Include Giving","Your Giving Goal Is the Most Important One","Build giving into your goal structure from the start. What is your current giving percentage? What is your one-year giving goal? What is your five-year giving vision?","2 Cor. 9:7; Prov. 3:9–10"],
      ["Day 28","Session 4 Capstone","Your Financial Goals Document","Write your complete financial goals document: purpose statement, three goals with dates, and giving vision. Share it with an accountability partner and pray over it together.","Hab. 2:2; Phil. 4:13"],
    ]},
    {num:5,title:"HOW DO I PLAN?",sub:"Ch. 9–11: Building the Integrated Plan That Makes Goals Real",desc:"Vision without a plan is a wish. This session builds the actual financial plan — budget, cash flow control, and tax strategy — that turns goals into lived, daily reality.",verses:"Luke 14:28 · Prov. 3:9–10 · Rom. 13:6–7",days:[
      ["Day 29","From Goals to Action Steps","The Financial Planning Diagram Made Personal","Study the financial planning diagram and the Bob and Laura case study. What action steps would increase your monthly cash flow margin by 10%? Write three specific ones.","Prov. 21:5; Luke 14:28–30"],
      ["Day 30","Build Your Budget Today","The One Financial Tool You Cannot Function Without","Build your complete monthly budget from scratch — no categories skipped. Giving is the first line. This is the one financial tool that makes every other tool work.","Prov. 3:9–10; 1 Cor. 16:2"],
      ["Day 31","Controlling the Flow","Your Budget Only Works If You Engage It","Set up your budget tracking system today. Choose the simplest one you will actually use. Name your accountability partner and share your budget with them.","Luke 16:10–11; Prov. 27:23"],
      ["Day 32","Scripture and Taxes","What the Bible Says About Your Obligation to Caesar","What is your current attitude toward taxes — biblically shaped or culturally shaped? Write one sentence that aligns your tax perspective with Romans 13:6–7.","Rom. 13:6–7; Matt. 22:21"],
      ["Day 33","Legal Tax Reduction","The Stewardship of Keeping What You Are Not Required to Give","Identify two legal tax reduction strategies you are not using. Write a plan to implement both within the next 90 days. Consult a professional if needed.","Prov. 22:3; 1 Tim. 6:17"],
      ["Day 34","The Integrated Plan","Where Budget, Debt, Goals, and Taxes Become One Story","Review your budget, debt plan, tax strategy, and faith goals together. Do they tell one coherent story? Write the one integration step that would most improve alignment.","Prov. 21:5; Luke 14:28"],
      ["Day 35","Session 5 Capstone","Your Complete Living Financial Plan","Compile your complete financial plan: net worth, cash flow, budget, debt elimination timeline, tax plan, and faith goals. Review it every quarter without exception.","Prov. 27:23; Luke 14:28"],
    ]},
    {num:6,title:"HOW CAN I GIVE?",sub:"Ch. 12–14: Investing, Legacy, and the Life of Generous Living",desc:"The final and most important question: What is all this money management for? The answer is generosity — today, tomorrow, and for eternity. Every financial discipline culminates in an open hand.",verses:"2 Cor. 9:6–8 · Prov. 13:22 · Matt. 25:21",days:[
      ["Day 36","The Purpose of Investing","Why You Accumulate — and When to Stop","What are your long-term goals? When will you have 'enough' accumulated? Answer honestly: why are you continuing to accumulate beyond what your defined goals require?","Prov. 21:5; Luke 12:19–21"],
      ["Day 37","The Sequential Strategy for Kingdom Investors","First Things First — Then Kingdom Things","Study the five sequential investing steps through a kingdom lens. How does knowing your wealth will eventually serve kingdom purposes change how aggressively you accumulate?","Prov. 21:5; Matt. 25:14–21"],
      ["Day 38","Stewardship Doesn't End at Death","Your Will, Your Estate, Your Final Financial Statement","Study the estate planning section. Does your will reflect your kingdom values? Review it today. If you lack one, commit to creating it within 30 days.","Prov. 13:22; Ps. 112:1–3"],
      ["Day 39","Giving Living — Today, Tomorrow, Eternity","When, Where, and How Much Is Enough to Give?","Work through all three giving questions from Chapter 14. Write a complete giving plan: your current percentage, one-year target, recipients, and legacy giving vision.","2 Cor. 9:6–8; Mal. 3:10"],
      ["Day 40","40-Day Capstone: Mastered Money","The Covenant That Ties It All Together","Review all six sessions. Write your Master Your Money covenant: foundation, plan, goals, giving, and investment strategy — one page, signed and dated as a declaration of stewardship.","Matt. 25:21; 2 Cor. 9:6–8"],
    ]},
  ]
},
{
  label:"OUTLINE C",
  name:"Financial Contentment for Couples and Families — A Shared Journey",
  desc:"Designed for couples and families engaging with the material together. Each session includes specific relational application prompts and addresses the interpersonal dynamics of money. Best for marriage small groups and family financial discipleship.",
  sessions:[
    {num:1,title:"GOD, MONEY, AND US",sub:"Ch. 1–2: Building a Shared Biblical Foundation for Your Marriage Finances",desc:"Before a couple can manage money together effectively, they need a shared foundation of belief. This session helps partners identify where their financial worldviews are aligned — and where they diverge.",verses:"Gen. 2:24 · Amos 3:3 · Phil. 4:11–13",days:[
      ["Day 1","Your Financial Story","How Your Upbringing Shaped Your Money Beliefs","Each partner writes independently: your top three beliefs about money from your family of origin. Share and compare. Where do your financial stories most significantly differ?","Prov. 23:7; Luke 16:13"],
      ["Day 2","Do You Share a Financial Worldview?","Identifying Where You Agree — and Where You Don't","Study the biblical vs. worldly worldview side by side. As a couple, discuss: which view is actually driving your household financial decisions? Where are you in conflict right now?","Matt. 6:24; Amos 3:3"],
      ["Day 3","The Four Principles as a Couple","A Shared Foundation You Can Both Stand On","Study each of the four principles together. Which principle is the weakest in your household? What would strengthening it together over the next 40 days require of both of you?","2 Tim. 3:16–17; Matt. 7:24–27"],
      ["Day 4","The Three Financial Questions, Answered Together","Will We Ever Have Enough?","Each partner answers the three questions independently, then compare answers. Where do your financial fears and hopes differ most? What does this reveal about areas needing shared prayer?","Phil. 4:11–13; Heb. 13:5"],
      ["Day 5","Money as Tool, Test, and Testimony in Your Marriage","What Is God Doing Through Your Household Finances?","As a couple, identify which of the three — tool, test, or testimony — best describes what God is doing through your finances right now. What is He developing in you together?","Phil. 4:12; Jas. 1:2–4"],
      ["Day 6","Setting a Shared Faith Goal","What Are We Trusting God for Together?","Write one faith financial goal as a couple — one that requires both of you to trust God together for the outcome. Make it specific, dated, and something neither of you can achieve alone.","Hab. 2:2; Jer. 29:11"],
      ["Day 7","Session 1 Capstone","Your Shared Financial Foundation Statement","Write a joint foundation statement — two or three sentences capturing what you both believe about God, money, and your household. Discuss, agree, and both sign it.","Phil. 4:11–13"],
    ]},
    {num:2,title:"WHERE ARE WE?",sub:"Ch. 3, 6: Your Shared Financial Snapshot",desc:"Many couples avoid an honest financial assessment because it feels threatening. This session creates a safe, grace-filled framework for both partners to see the complete household picture — together.",verses:"Prov. 27:23 · Amos 3:3 · Eph. 4:25",days:[
      ["Day 8","The Cost of Financial Avoidance in Marriage","What Hiding Does to Trust","How does financial avoidance and secrecy damage marital trust? Is there anything about your household finances that only one of you knows fully? This session is about complete transparency.","Eph. 4:25; Prov. 27:23"],
      ["Day 9","The Five Uses in Your Household","Where Does Our Money Actually Go?","Map your household spending across the five uses together. Do both partners know the actual percentages? Complete this exercise together — and discuss honestly what surprises each of you.","Eccl. 5:10; 1 Tim. 6:17–19"],
      ["Day 10","Your Shared Net Worth","Assets, Liabilities, and the Real Number","Complete your household net worth statement together. If one partner has been unaware of the full picture, receive it with grace — not blame. Clarity is a gift to both of you.","Prov. 27:23; Luke 14:31–32"],
      ["Day 11","Your Household Cash Flow","The Monthly Story of Your Marriage Finances","Complete your household cash flow together. Where is the disagreement about spending? Which categories is each partner most sensitive about? Discuss with curiosity, not judgment.","Luke 16:10–11; Prov. 27:23"],
      ["Day 12","Insurance and Protection — Both Partners Informed","Caring for Each Other and What God Has Given You","Review all insurance coverage as a couple. Is the other partner fully informed? If one of you died tomorrow, would the other know exactly what to do? Identify one gap to address this week.","1 Tim. 5:8; Prov. 22:3"],
      ["Day 13","The Planning Process for Two","Whose Job Is Financial Planning?","Study the four-step planning process. Discuss: who is responsible for each step in your marriage? Is responsibility shared fairly? Write one change to make the process more collaborative.","Prov. 21:5; Luke 14:28"],
      ["Day 14","Session 2 Capstone","Your Complete Shared Financial Snapshot","Review your complete picture together — net worth, cash flow, insurance. Agree on one financial health goal you will pursue together as a team in the next 90 days.","Prov. 27:23; Amos 3:3"],
    ]},
    {num:3,title:"WHAT SHOULD WE AVOID?",sub:"Ch. 5, 8: Protecting Your Marriage From Common Financial Destroyers",desc:"Financial conflict is one of the most common sources of marital stress. This session names the financial dangers and mistakes that most threaten marriages — and helps couples build a shared defense.",verses:"Prov. 22:7 · Prov. 22:3 · Eph. 5:25–33",days:[
      ["Day 15","When Debt Becomes a Marriage Problem","The Weight You Are Both Carrying","Study the five dangers of debt through the lens of your marriage. How has debt affected your relationship — your options, your stress level, your freedom to obey God together?","Prov. 22:7; Hab. 2:6–7"],
      ["Day 16","The Four Borrowing Questions as a Couple","Both Spouses Must Be at Peace","Study the four questions with special attention to Question 2: Is your spouse free from anxiety about this debt? Have you ever taken on debt your partner was not at peace with? Discuss it.","Prov. 3:5–6; 1 Cor. 7:23"],
      ["Day 17","Your Shared Debt Plan","From Conflict to Collaboration","Create your shared debt list together. If this is the first time both of you have seen the complete picture, receive it with grace. Write your shared elimination plan — both partners fully owning it.","Ps. 37:21; Prov. 22:26–27"],
      ["Day 18","The Lifestyle Conversation","His Version, Her Version, God's Version","Discuss honestly: what is each partner's vision of the ideal lifestyle? Where do those visions differ? How does God's standard of provision reshape the conversation between you?","1 Tim. 6:8; Phil. 4:11"],
      ["Day 19","Budgeting Together","Why Couple Budgets Fail and How Yours Won't","What has made past budgeting attempts fail in your marriage? Write a fresh approach both partners can genuinely commit to — one that represents both voices, not just the financial manager's.","Prov. 21:5; Luke 14:28"],
      ["Day 20","Major Purchase Decisions","A Shared Framework for Decisions That Affect You Both","Develop a shared major-purchase decision framework: what dollar threshold triggers a joint discussion? What criteria does each partner most care about? Write the framework together.","Prov. 22:3; Luke 14:28–30"],
      ["Day 21","Session 3 