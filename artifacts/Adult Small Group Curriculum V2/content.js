// Master Your Money — Participant Guide content, built to the locked spec.
// Every session: header(3), memoryVerse+ref, intro(1 para), openingStory(label,subtitle,3 paras,quote),
// comeTogether(prayerLine,2 paras,2 discuss), building(S1 only), learn(watchLine,listenPara,6 blanks),
// grow(7 questions, practices[], mostAbsentLine), exercise(name,quietLine,table,circleLine,selfCheck),
// circles, nextSteps(3), family(intro,3), goingDeeper(intro,2 reads x3), readings(weekHeader,intro,7 days), close(2 paras)

const FIVE_FS = "FAMILY (immediate or extended) · FRIENDS · FAMILIAR (neighbors, kids' sports, school) · FIRM (work) · FUN (gym, hobbies, hangouts)";

const buildingBlock = {
  lead: "Build a healthy group culture.",
  intro: "Money is a subject most people carry quietly and rarely discuss openly. That makes trust especially important for the next six weeks. Agree together on how you will treat each other.",
  values: [
    "What is shared here stays here.",
    "We listen without fixing or advising.",
    "We speak from our own experience, never about someone else's choices.",
    "We never ask each other for numbers.",
    "We make room for the quiet voices, and anyone can pass on any question.",
    "We are open to learn. Nobody here has arrived, and that is exactly the point."
  ],
  closing: "Before you go further. Whether your group is brand new or has been together for years, take a few minutes to get on the same page. Turn to the Small Group Agreement in the back and read through it together. You do not have to adopt every value formally, just review it and make sure everyone's expectations match. While you are there, fill in the Group Calendar so you know who is hosting each week."
};

const sessions = [
  {
    n: 1,
    question: "THE OWNERSHIP QUESTION",
    subtitle: "Who really owns it all?",
    memoryVerse: "Yours, Lord, is the greatness and the power and the glory and the majesty and the splendor, for everything in heaven and earth is yours.",
    memoryRef: "1 CHRONICLES 29:11",
    intro: "Most of us treat a money problem as a math problem. If I earned a little more, or budgeted a little better, or finally showed some discipline, then I would feel settled. But underneath the math is a question the math never answers: who really owns it all? Until that question is settled, money stays heavier than it needs to be, because every outcome seems to rest on you. This session starts where the real issue starts, not with a spreadsheet, but with ownership. We begin with money and possessions, where ownership gets tested most plainly, and then widen into the rest of life. The aim is not guilt. The aim is freedom, because the weight most of us carry is the weight of ownership, and it was never ours to carry.",
    story: {
      label: "A Story from the Interviews",
      subtitle: "LEARNING TO HOLD WHAT WAS NEVER OURS",
      paras: [
        "A man interviewed for this study described how settling the ownership question reshaped the way he sees everything he has. His parents had passed, and he and his siblings inherited the family farm. That was not something he built, he said. It was something he was given, and that recognition changed how he held it. The home he lives in, the margin in his retirement, all of it traced back to something received rather than earned.",
        "He had learned the posture years earlier from a pastor he once worked with, who taught a three-part way of living: grace, gratefulness, and generosity. We receive grace, which is God giving us what we do not deserve. Gratefulness grows out of that. And gratefulness, held honestly, turns outward into generosity, because if you have been blessed with something, you carry a responsibility to steward it well and share it.",
        "Nothing about his circumstances changed when he grasped this. Everything about his grip did."
      ],
      quote: "It's not mine to do with as I please. I'm managing what I've been blessed with."
    },
    comeTogether: {
      prayerPara: "Ask God to quiet the part of each of you that wants to perform or hide. Invite him to show you where you have been living like an owner and carrying a weight he never asked you to carry.",
      tonePara: "Then set the tone for the six weeks ahead. This is not a class where anyone gets graded. No one here will be asked how much they make, owe, give, or save. Money can feel very personal, and dignity matters more than disclosure. You and God know your numbers, and that is enough. What we are after is honesty about the heart, not numbers on a page.",
      discuss: [
        "When you hear the phrase \"God owns it all,\" what is your first reaction? Comfort, resistance, confusion, something else?",
        "What is the first thing you remember saving up to buy as a kid, and how did it feel when you finally got it?"
      ]
    },
    building: buildingBlock,
    learn: {
      listenPara: "As you watch, listen for the distinction Ron draws between owning something and stewarding it, and the reason he says security never comes from accumulation. Notice the practices he names for living as a steward, and the question he says almost everyone carries their whole life.",
      blanks: [
        "The most important financial question is not how much I make or owe. It is, who really ________ it all?",
        "If God owns it all, then I am a ________, managing what belongs to ________.",
        "Security does not come from ________. It comes from trusting the owner and provider.",
        "Every financial decision is a ________ decision.",
        "If I do not ________ it, I cannot ________ it.",
        "When God is the owner, money becomes a ________, and it loses its ________ over me."
      ]
    },
    grow: {
      questions: [
        "Ron says every money decision is a spiritual decision, no more and no less spiritual than prayer or worship. What is the practical difference between believing that and living it on an ordinary Tuesday?",
        "Your memory verse says everything in heaven and earth belongs to God. What would change if you took the word \"everything\" at face value with your own money and possessions?",
        "The teaching described the weight of ownership, the sense that every outcome rests on you. Where do you feel that weight most in this season?",
        "Ron offered a line worth sitting with: if I do not own it, I cannot lose it. Does that feel freeing, unsettling, or both, and why?",
        "This week's devotional begins with naming what came from God's hand rather than your own. What makes it hard to hold what you have as a manager rather than an owner, especially with money?",
        "Money carries an unspoken meaning we absorb growing up. Without sharing any numbers, what is one belief about money you think you inherited from your family?",
        "Name one specific thing, not a category, that you have been holding as an owner. What would open hands look like with that one thing this week?"
      ],
      practicesLead: "The practices for living as a steward. Ron names several everyday practices for living this out.",
      practices: [
        ["Make the ownership transfer.", "Name one financial stress and say plainly, \"Lord, this belongs to you. Show me how to steward it.\" You are not giving God something he lacked. You are recognizing what was already true."],
        ["Pause before you purchase.", "Before you spend, sign, or swipe, ask one question: is this faithful stewardship of what God has entrusted to me? That single question brings clarity faster than most people expect."],
        ["Have the owner-versus-steward conversation.", "With a spouse, a friend, or the group, ask honestly: where are we acting like owners instead of stewards?"]
      ],
      mostAbsent: "Now discuss: which of these practices is most absent from how you handle money right now? Share only what you feel comfortable sharing openly."
    },
    exercise: {
      name: "The Steward's First Look",
      quietLine: "Do this quietly on your own. You will not be asked to read it aloud.",
      instructions: "Ownership is tested first with money, so start there. For each area below, name what you are holding, then note whether you have been carrying it as an owner or managing it as a steward. There are no numbers to write and nothing to share.",
      table: {
        headers: ["The area", "What I am holding here", "Owner or steward right now?"],
        rows: [
          ["A bill or expense", "", ""],
          ["A financial decision I am facing", "", ""],
          ["A fear about the future", "", ""],
          ["Something I have been given", "", ""]
        ]
      },
      circleLine: "Circle the row with the tightest grip, and finish this sentence:",
      finishSentence: "\"If this really belongs to God and not to me, then one thing that would change is ________.\"",
      selfCheck: "Where am I with ownership? (private) On a scale of 1 to 5, how closely do your day-to-day money habits match what you say you believe about who owns it all? ___ Where is the widest gap? ___"
    },
    nextSteps: [
      "Each morning, before you look at your phone, say out loud: \"Lord, all I have is yours. Show me how to manage it today.\"",
      "Before one purchase this week, pause and ask: am I acting like an owner or a steward right now?",
      "Finish the Steward's First Look if you did not complete it together."
    ],
    family: {
      intro: "Take this week's theme home. Ask one of these to a spouse, a child, a parent, or a friend. If your family is going through the Master Your Money devotional together, these bring everyone's week to the same table.",
      questions: [
        "If everything we have is really on loan from God, what is one thing we might do differently as a family?",
        "What is something we are grateful for right now that we did not earn or create?",
        "Is there anything we have been holding too tightly that we could practice holding with open hands together?"
      ]
    },
    goingDeeper: {
      reads: [
        { ref: "READ 1 CHRONICLES 29:11-16", qs: [
          "What does David say is the source of the wealth and honor the people are giving?",
          "In verse 14 David asks, \"who am I, and who are my people, that we should be able to give as generously as this?\" How does that question reframe your sense of your own ability to give?",
          "David says the wealth came from God's hand and they are only giving back what was already his. Where would that posture change how you hold your finances?"
        ]},
        { ref: "READ LUKE 12:13-21", qs: [
          "What precisely does Jesus identify as the man's mistake? Notice it is not that he saved.",
          "The farmer worked hard and had a genuinely good year. What went wrong anyway?",
          "Jesus calls him a fool, not a criminal. What is the difference, and which one is easier to become?"
        ]}
      ]
    },
    readings: {
      weekHeader: "WEEK ONE · THE OWNERSHIP QUESTION",
      days: [
        ["Day 1 — The Ownership Transfer", "Peace Begins When \"Mine\" Becomes \"His\"", "Haggai 2:8.", "\"'The silver is mine and the gold is mine,' declares the Lord Almighty.\"", "Name the one thing you are gripping hardest, and hand it back to God as its manager, not its owner."],
        ["Day 2 — Every Spending Decision Is a Spiritual Decision", "Money Reveals What You Trust", "Matthew 6:21.", "\"For where your treasure is, there your heart will be also.\"", "Look at where your money actually went last month, and ask what it says about where your heart has been."],
        ["Day 3 — God Uses Money to Form You", "The Growth Process", "Philippians 4:11-12.", "\"I have learned to be content whatever the circumstances.\"", "Name one place God may be forming you through money, not just funding you."],
        ["Day 4 — Faithfulness First", "God Measures What's In Your Heart, Not Your Hands", "Luke 16:10.", "\"Whoever can be trusted with very little can also be trusted with much.\"", "Choose one small place to be faithful this week, and do it."],
        ["Day 5 — Faith Requires Action", "Obedience Is the First Financial Step", "James 2:17.", "\"Faith by itself, if it is not accompanied by action, is dead.\"", "Name one obedient money step you have been postponing, and take it."],
        ["Day 6 — The \"Will I Be Okay?\" Question", "God's Provision Answers Our Fears", "Matthew 6:31-33.", "\"But seek first his kingdom and his righteousness, and all these things will be given to you as well.\"", "Where does the \"will I be okay?\" question live loudest in you? Bring it to God by name."],
        ["Day 7 — A Daily Surrender", "Living Like a Steward Before You Feel Ready", "Romans 11:36.", "\"For from him and through him and for him are all things.\"", "Practice handing something back to God before you feel ready."]
      ]
    },
    close: {
      p1: "Before you leave, ask one another: how can we pray for you this week? Write the requests on the Prayer and Praise Report so you can pray between meetings.",
      p2: "Then close together. Thank God that everything comes from his hand and that we give him only what was already his, and ask him to replace the weight of ownership with the freedom of trusting him."
    }
  }
];

module.exports = { sessions, FIVE_FS, buildingBlock };
