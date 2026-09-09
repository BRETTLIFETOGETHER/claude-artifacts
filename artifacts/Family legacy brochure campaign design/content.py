# -*- coding: utf-8 -*-
# Family Legacy Collection — content for top 10 titles, 40-day / 6-session campaigns.
# Content is original, shaped by the project's "Family Legacy by Design" frameworks
# (legacy by design vs. default, the Five Areas of Legacy, the F.A.M.I.L.Y. Review,
# wisdom transfer vs. wealth transfer, God's multi-generational design, family mission/values).

COLLECTION = {
    "eyebrow": "LIFETOGETHER · THE FAMILY LEGACY COLLECTION · TOP TEN CAMPAIGN TITLES",
    "title": "The Family Legacy",
    "title_accent": "Collection.",
    "lede": ("Ten complete campaign and small group series on the most enduring question a "
             "household will ever answer — not how much we will leave, but what kind of "
             "people we will send into the generations that follow. Built on the conviction "
             "that a lasting legacy is never an accident of wealth but the fruit of faith, "
             "wisdom, and love passed on by design."),
    "framework": ("\u201cFamily Legacy helps us build on purpose. Leaving a Lasting Legacy helps us "
                  "invest in what endures. Generations helps us see God\u2019s covenant across time. "
                  "Faith for Generations helps us hand on a living faith. Family by Design helps us "
                  "construct the home intentionally. Legacy Living helps us build legacy today. "
                  "Blessing the Next Generation helps us confer value and identity. The Generational "
                  "Life helps us choose interdependence. Building a Spiritual Legacy helps us lay the "
                  "only foundation that lasts. Passing Faith Forward helps us complete the handoff. "
                  "Together, they are the legacy God always intended a family to leave.\u201d"),
    "footer": ("Brett Eastman \u00b7 Founder, Lifetogether \u00b7 brett@lifetogether.com \u00b7 "
               "The Family Legacy Collection \u00b7 Ten-Title Campaign Platform \u00b7 "
               "Drawn from Family Legacy by Design"),
    "closing_kicker": "Ten titles. One calling.",
    "closing_title": "A legacy by design.",
    "closing_body": ("The Family Legacy Collection is the most complete whole-family legacy "
                     "platform available \u2014 ten 40-day journeys, sixty small group sessions, and a "
                     "two-year ministry calendar that helps every household move from a legacy left "
                     "by default to a legacy built on purpose: faith handed forward, wisdom "
                     "transferred, blessing spoken, and a name that means something for generations "
                     "to come."),
}

# Shared series-information defaults for every title (Tier 2 · Church, Company)
def info(audience, season, related):
    return [
        ("Format", "40-Day Journey + 6-Session Small Group"),
        ("Audience", audience),
        ("Best Season", season),
        ("Publisher Tier", "Tier 2 \u2014 Church & Company"),
        ("Best For", "Church \u00b7 Company \u00b7 Family"),
        ("Core Theme", "Family mission, inheritance & legacy"),
        ("Related Campaign", related),
    ]

TITLES = [
 # 1 -----------------------------------------------------------------------
 {
  "num": 1, "color": "#6b2737",
  "category": "MISSION, INHERITANCE & THE LIFE YOU LEAVE",
  "title": "Family", "accent": "Legacy",
  "subhead": ("A legacy is not what you leave behind by accident \u2014 it is what you build on "
              "purpose: the faith, wisdom, and love that outlive you when everything else is gone."),
  "pullquote": ("\u201cEvery family leaves a legacy. The only question is whether yours will be "
                "left by design \u2014 or by default.\u201d"),
  "body": ("Family Legacy addresses the most important question a household will ever face: not how "
           "much we will leave, but who we will send into the generations that follow. Scripture "
           "defines inheritance not as the wealthy person\u2019s privilege but as the good "
           "person\u2019s intention \u2014 \u201ca good person leaves an inheritance for their "
           "children\u2019s children.\u201d <b>A family that simply drifts will still pass something "
           "on; the only choice is whether what they pass on was chosen, or inherited from the "
           "culture by default.</b> This series gives every household the biblical vision, the "
           "practical framework, and the honest conversations to build a legacy on purpose."),
  "scripture": "\u201cA good person leaves an inheritance for their children\u2019s children.\u201d",
  "scripture_ref": "\u2014 Proverbs 13:22 (NIV)",
  "subtitles": ["A 40-Day Journey from Legacy by Default to Legacy by Design",
                "Discovering God\u2019s Design for the Family You Leave Behind",
                "A 40-Day Path to a Legacy Built on Purpose",
                "Building a Family Legacy That Outlasts You"],
  "bigidea": ("God designed the family to be the primary place where faith, wisdom, character, and "
              "blessing pass from one generation to the next \u2014 and the family that lives that "
              "calling on purpose leaves a legacy that outlasts every account, title, and possession."),
  "tags": ["legacy by design","inheritance","family mission","wisdom transfer","generations","stewardship"],
  "info": info("All church \u2014 parents, grandparents, couples, single adults",
               "Fall family launch \u00b7 New Year \u00b7 Father\u2019s / Mother\u2019s Day",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"Legacy by Design,","a":"Not by Default",
    "s":"\u201cBe sure you know the condition of your flocks, give careful attention to your herds.\u201d \u2014 Proverbs 27:23",
    "tags":["legacy","intention","design vs default","Proverbs 27","vision"],
    "q":["When you hear the word \u201clegacy,\u201d what comes to mind first \u2014 and how much of it is about money versus faith, character, and relationships?",
         "Every family is already passing something on, intentionally or not. What do you think your family is currently catching from you by default?",
         "What would it mean for your family\u2019s legacy to be built \u201cby design\u201d \u2014 and what is the first decision that would change?"],
    "step":"Finish this sentence in writing: \u201cThe legacy I most want to leave my family is \u2026\u201d Share it with your group partner this week."},
   {"t":"More Than","a":"Money",
    "s":"\u201cWisdom, like an inheritance, is a good thing \u2026 wisdom preserves those who have it.\u201d \u2014 Ecclesiastes 7:11\u201312",
    "tags":["inheritance","wisdom","wealth","meaning","Ecclesiastes 7"],
    "q":["\u201cWealth without wisdom is an inheritance without instruction.\u201d Where have you seen money passed down without the wisdom to handle it \u2014 and what happened?",
         "What non-financial inheritance did you receive from those before you \u2014 for better or worse \u2014 and how is it shaping you today?",
         "If you could pass on only three things that are not money, what would they be?"],
    "step":"List the five most valuable things you have to pass on that cannot be deposited in a bank. Bring it to the next session."},
   {"t":"God\u2019s","a":"Multi-Generational Design",
    "s":"\u201c\u2026that the generation to come might know \u2026 that they may arise and tell them to their children.\u201d \u2014 Psalm 78:5\u20137",
    "tags":["generations","God\u2019s design","Psalm 78","covenant","faithfulness"],
    "q":["Psalm 78 names five generations in a single breath. How far down the line are you actually thinking when you make decisions today?",
         "The modern view says \u201craise them and release them\u201d; the biblical view is multi-generational and interdependent. Which view has shaped your family more?",
         "What is one work of God in your own story that the next generation will never know unless you intentionally tell them?"],
    "step":"This week, tell one child, grandchild, or younger person a specific story of how God has been faithful in your life."},
   {"t":"The Honest","a":"Inventory",
    "s":"\u201cSearch me, God, and know my heart; test me and know my anxious thoughts.\u201d \u2014 Psalm 139:23",
    "tags":["clarity","family health","honesty","readiness","assessment"],
    "q":["Look honestly at your family\u2019s spiritual, relational, and financial health. Which of the three is strongest right now \u2014 and which most needs attention?",
         "Are the people who will receive what you pass on actually prepared to steward it well? What would \u201cprepared\u201d look like?",
         "What is one hard but necessary conversation your family has been avoiding?"],
    "step":"Privately rate your family\u2019s spiritual, relational, and financial health from 1\u201310. Name the lowest score and one step to raise it."},
   {"t":"A Family","a":"on Mission",
    "s":"\u201c\u2026as for me and my household, we will serve the Lord.\u201d \u2014 Joshua 24:15",
    "tags":["family mission","values","unity","vision","Joshua 24"],
    "q":["Joshua made a public declaration for his whole household. If your family had a one-sentence mission statement, what would you want it to say?",
         "What three or four values do you most want to define your family \u2014 and are they actually visible in how you spend time and money?",
         "Who in your family will help carry the torch of these values into the next generation?"],
    "step":"Draft a first attempt at a one-sentence family mission: \u201cOur family exists to \u2026\u201d Share it and refine it together."},
   {"t":"Building It","a":"on Purpose","commit":True,
    "s":"\u201cLet us not become weary in doing good, for at the proper time we will reap a harvest.\u201d \u2014 Galatians 6:9",
    "tags":["commitment","perseverance","rhythms","next steps","Galatians 6"],
    "q":["After these 40 days, what is the single most important shift in how you think about the legacy you are leaving?",
         "The keys to passing on a legacy begin with \u201cbe intentional\u201d and \u201cbe humble enough to ask for help.\u201d Which do you most need to grow in?",
         "What is one concrete, repeatable rhythm \u2014 a family meeting, a weekly meal, a yearly retreat \u2014 you will build to keep this legacy on purpose?"],
    "commit":("Each person names one legacy commitment for the next 12 months and one person in the "
              "group who will ask them about it. Close by praying over each family by name.")},
  ]},
 # 2 -----------------------------------------------------------------------
 {
  "num": 2, "color": "#234a3a",
  "category": "WHAT ENDURES BEYOND A LIFETIME",
  "title": "Leaving a Lasting", "accent": "Legacy",
  "subhead": ("Most of what we spend our lives accumulating will not survive a single generation \u2014 "
              "but some things echo for a thousand. Wisdom is knowing the difference, and building "
              "only what lasts."),
  "pullquote": ("\u201cYou cannot take it with you \u2014 but you can send it on ahead. The only "
                "question is what you are sending.\u201d"),
  "body": ("Leaving a Lasting Legacy confronts the quiet illusion that the things we work hardest "
           "for are the things that last. The estate is spent, the title is forgotten, the house "
           "changes hands \u2014 but faith, wisdom, character, and the relationships we invest in can "
           "outlive us by centuries. <b>A lasting legacy is not measured by the size of an estate "
           "but by the depth of what survives long after the assets are gone.</b> This series helps a "
           "congregation number their days, weigh what truly endures, and pour their lives into the "
           "few things that will still matter in a hundred years."),
  "scripture": "\u201cTeach us to number our days, that we may gain a heart of wisdom.\u201d",
  "scripture_ref": "\u2014 Psalm 90:12 (NIV)",
  "subtitles": ["A 40-Day Journey into What Truly Lasts",
                "Discovering God\u2019s Design for an Enduring Life",
                "A 40-Day Path to Finishing Well and Leaving More",
                "Investing Your One Life in What Outlives You"],
  "bigidea": ("A lasting legacy is not the size of an estate but the depth of the faith, the "
              "strength of the relationships, and the wisdom that remain long after the assets are "
              "spent \u2014 and that kind of legacy is built deliberately, one ordinary decision at a time."),
  "tags": ["endurance","wisdom","what lasts","finishing well","character","perspective"],
  "info": info("All church \u2014 second-half adults, families, leaders",
               "New Year \u00b7 Fall \u00b7 Year-end reflection",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"What Actually","a":"Lasts",
    "s":"\u201cTeach us to number our days, that we may gain a heart of wisdom.\u201d \u2014 Psalm 90:12",
    "tags":["perspective","eternity","priorities","Psalm 90","wisdom"],
    "q":["If you knew your days were numbered, what would suddenly matter more \u2014 and what would matter far less?",
         "Name something you are pouring energy into now that will not last a generation. Why does it still hold so much of your attention?",
         "What is one thing in your life you are confident will still matter in a hundred years?"],
    "step":"Write a short list this week titled \u201cWhat I want to still be true of my family in 100 years.\u201d"},
   {"t":"The Inheritance That","a":"Outlives the Estate",
    "s":"\u201cA good person leaves an inheritance for their children\u2019s children.\u201d \u2014 Proverbs 13:22",
    "tags":["inheritance","wisdom over wealth","blessing","Proverbs 13","stewardship"],
    "q":["Proverbs says a good person \u2014 not a wealthy person \u2014 leaves an inheritance. What does that distinction change for you?",
         "What would it look like to leave your children wise rather than merely wealthy?",
         "Have you ever seen an inheritance become a burden instead of a blessing? What was missing?"],
    "step":"Identify one piece of hard-won wisdom you want your heirs to receive, and write down how you will pass it on."},
   {"t":"A Thousand","a":"Generations",
    "s":"\u201cHe keeps his covenant of love to a thousand generations of those who love him.\u201d \u2014 Deuteronomy 7:9",
    "tags":["covenant","faithfulness","God\u2019s promise","long view","Deuteronomy 7"],
    "q":["God thinks in terms of a thousand generations. How does that scale reframe the decisions you make this year?",
         "What promise of God do you most want the generations after you to stake their lives on?",
         "Where are you tempted to live for the short term at the expense of the long story?"],
    "step":"Choose one promise of God to memorize and pass to someone younger this week, explaining why it has held you."},
   {"t":"Remembered","a":"Well",
    "s":"\u201cA good name is more desirable than great riches; to be esteemed is better than silver or gold.\u201d \u2014 Proverbs 22:1",
    "tags":["character","reputation","integrity","good name","Proverbs 22"],
    "q":["If your family described your character in one sentence at your funeral, what do you hope \u2014 and fear \u2014 they would say?",
         "Where is there a gap between the reputation you have and the character you actually want?",
         "Whose \u201cgood name\u201d shaped you, and what specifically did they model?"],
    "step":"Identify one area where your private character and public reputation don\u2019t yet match, and take one step to close the gap."},
   {"t":"Telling the","a":"Story",
    "s":"\u201cOne generation commends your works to another; they tell of your mighty acts.\u201d \u2014 Psalm 145:4",
    "tags":["story","remembrance","testimony","Psalm 145","legacy letter"],
    "q":["What is the family story \u2014 of faith, struggle, or provision \u2014 that the next generation must not lose?",
         "Why do family stories so easily disappear, and what would it take to capture yours?",
         "Who in your family is the keeper of the stories, and what happens when they are gone?"],
    "step":"Record one family God-story this week \u2014 written, audio, or video \u2014 and share it at the next gathering."},
   {"t":"Finishing","a":"Well","commit":True,
    "s":"\u201cI have fought the good fight, I have finished the race, I have kept the faith.\u201d \u2014 2 Timothy 4:7",
    "tags":["finishing well","perseverance","commitment","2 Timothy 4","legacy"],
    "q":["What would it mean for you, specifically, to \u201cfinish well\u201d in this season of life?",
         "What is the one thing you do not want to leave undone or unsaid with your family?",
         "Over these 40 days, what has shifted in how you weigh what lasts against what merely glitters?"],
    "commit":("Each person names one enduring investment \u2014 a relationship, a habit, a story to be "
              "told \u2014 they will give themselves to, and one person who will check in at 30 days. "
              "Close in prayer for one another to finish well.")},
  ]},
 # 3 -----------------------------------------------------------------------
 {
  "num": 3, "color": "#23314f",
  "category": "GOD\u2019S COVENANT ACROSS TIME",
  "title": "", "accent": "Generations",
  "subhead": ("God has never worked one life at a time. From Abraham forward, His promises run like a "
              "river through generations \u2014 and your family is meant to be part of that current, not "
              "a dam that stops it."),
  "pullquote": ("\u201cGod\u2019s promises are not loans for a lifetime. They are covenants that run a "
                "thousand generations deep.\u201d"),
  "body": ("Generations lifts a family\u2019s eyes from the immediate to the eternal. The God of "
           "Scripture binds Himself not to isolated individuals but to families across time, "
           "commanding each generation to make Him known to the next so that even the children yet "
           "unborn might set their hope in Him. <b>The greatest threat to a family of faith is "
           "rarely an attack from outside \u2014 it is a single generation that fails to pass it on.</b> "
           "This series helps a congregation recover God\u2019s multi-generational vision and take up "
           "their place in a story far longer than their own lives."),
  "scripture": "\u201cHe remembers his covenant forever, the promise he made, for a thousand generations.\u201d",
  "scripture_ref": "\u2014 Psalm 105:8 (NIV)",
  "subtitles": ["A 40-Day Journey into God\u2019s Generational Story",
                "Discovering God\u2019s Covenant Across the Generations",
                "A 40-Day Path from One Generation to the Next",
                "Taking Your Place in a Thousand-Generation Story"],
  "bigidea": ("God\u2019s design has always been multi-generational \u2014 He commits Himself to families "
              "across time and calls each generation to make Him known to the next, so the children "
              "yet unborn might know Him, trust Him, and keep His commandments."),
  "tags": ["covenant","generations","God\u2019s design","faithfulness","heritage","continuity"],
  "info": info("All church \u2014 grandparents, parents, young families",
               "Fall \u00b7 New Year \u00b7 Grandparents\u2019 emphasis",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"A God of","a":"Generations",
    "s":"\u201cI will establish my covenant \u2026 between me and you and your descendants after you for the generations to come.\u201d \u2014 Genesis 17:7",
    "tags":["covenant","Abraham","promise","Genesis 17","generations"],
    "q":["God made His covenant not just with Abraham but with his descendants \u201cfor generations to come.\u201d How does it feel to be downstream of a promise like that?",
         "What spiritual covenant or commitment in your family began before you were born?",
         "What promise of God do you most want to be true of your descendants after you?"],
    "step":"Trace your family\u2019s faith back as far as you can this week, and thank God for one person who carried it to you."},
   {"t":"The Generation","a":"That Forgot",
    "s":"\u201cAnother generation grew up who knew neither the Lord nor what he had done for Israel.\u201d \u2014 Judges 2:10",
    "tags":["warning","forgetting","handoff","Judges 2","urgency"],
    "q":["Judges describes faith collapsing in a single generation. How does that happen so quickly \u2014 even in good families?",
         "What is the difference between a child who knows about God and a child who knows God?",
         "Where might your family be one step away from a generation that \u201cforgets\u201d?"],
    "step":"Name one specific way you will help a younger person know God \u2014 not just know about Him \u2014 this month."},
   {"t":"From Independence","a":"to Interdependence",
    "s":"\u201cYour children will be like olive shoots around your table \u2026 may you live to see your children\u2019s children.\u201d \u2014 Psalm 128:3,6",
    "tags":["interdependence","family","multi-generational","Psalm 128","connection"],
    "q":["The culture\u2019s goal is to raise children to independence and send them off. God\u2019s vision adds interdependence. What would change if you aimed for both?",
         "What does healthy lifelong connection between generations look like \u2014 versus unhealthy dependence?",
         "How could your extended family become more of a team and less of a collection of individuals?"],
    "step":"Take one action this week to strengthen a cross-generational relationship in your family."},
   {"t":"The Voices","a":"That Shape Us",
    "s":"\u201cI am reminded of your sincere faith, which first lived in your grandmother Lois and in your mother Eunice.\u201d \u2014 2 Timothy 1:5",
    "tags":["influence","grandparents","sincere faith","2 Timothy 1","modeling"],
    "q":["Timothy\u2019s faith was traced through his grandmother and mother. Whose faith can you trace in your own story?",
         "What did the most influential believer in your life do that actually formed you?",
         "Whose faith are you currently shaping, whether you intended to or not?"],
    "step":"Write a short thank-you to someone whose faith shaped yours \u2014 or, if they\u2019re gone, write what you\u2019d say."},
   {"t":"Bridging","a":"the Gap",
    "s":"\u201cHe will turn the hearts of the parents to their children, and the hearts of the children to their parents.\u201d \u2014 Malachi 4:6",
    "tags":["reconciliation","healing","relationship","Malachi 4","restoration"],
    "q":["Is there a gap between generations in your family \u2014 of distance, hurt, or silence \u2014 that needs a heart turned back?",
         "What keeps families from repairing generational wounds, and what would a first step toward repair cost you?",
         "How does unresolved relational distance threaten everything else you hope to pass on?"],
    "step":"Identify one relationship across generations that needs a step toward repair. Pray about it daily, then take the step."},
   {"t":"The Generation","a":"to Come","commit":True,
    "s":"\u201c\u2026so the next generation would know them, even the children yet to be born.\u201d \u2014 Psalm 78:6",
    "tags":["commitment","next generation","vision","Psalm 78","continuity"],
    "q":["Picture a descendant you will never meet. What do you most want to be true of their faith because of choices you make now?",
         "What is the single most important thing this group has helped you see about generational faith?",
         "What will you do differently, starting this week, so the generation to come will know the Lord?"],
    "commit":("Each person names one commitment for the generations to come \u2014 a story to tell, a "
              "relationship to mend, a faith habit to model \u2014 and one person to ask about it in 30 days. "
              "Close by praying for children yet unborn.")},
  ]},
 # 4 -----------------------------------------------------------------------
 {
  "num": 4, "color": "#42345c",
  "category": "HANDING ON A LIVING FAITH",
  "title": "Faith for", "accent": "Generations",
  "subhead": ("You can leave your children money and they may lose it. You can leave them a name and "
              "they may forget it. But a living faith, handed on with intention, can carry a family "
              "for centuries."),
  "pullquote": ("\u201cThe most valuable thing you will ever hand your children is not in your will. "
                "It is in your walk.\u201d"),
  "body": ("Faith for Generations addresses the inheritance that matters more than any other and is "
           "passed on least automatically. Deuteronomy 6 does not describe a program; it describes a "
           "lifestyle \u2014 faith impressed on children in the ordinary moments of sitting at home, "
           "walking along the road, lying down, and getting up. <b>Faith is never transferred by "
           "accident; it is handed on deliberately, modeled before it is mentioned, and lived before "
           "it is taught.</b> This series gives parents, grandparents, and mentors the conviction and "
           "the practical rhythms to raise a generation that owns the faith for themselves."),
  "scripture": ("\u201cImpress them on your children. Talk about them when you sit at home and when "
                "you walk along the road, when you lie down and when you get up.\u201d"),
  "scripture_ref": "\u2014 Deuteronomy 6:7 (NIV)",
  "subtitles": ["A 40-Day Journey to a Faith Worth Passing On",
                "Discovering God\u2019s Design for Faith That Lasts",
                "A 40-Day Path to Discipleship in the Home",
                "Raising a Generation That Knows God for Themselves"],
  "bigidea": ("Faith is not transferred automatically \u2014 it is handed on deliberately, modeled in "
              "daily life and spoken into ordinary moments, so the generation to come knows God for "
              "themselves and not merely by reputation."),
  "tags": ["discipleship","faith at home","Deuteronomy 6","modeling","spiritual inheritance","prayer"],
  "info": info("All church \u2014 parents, grandparents, mentors, ministry leaders",
               "Fall discipleship launch \u00b7 New Year \u00b7 Back-to-school",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"Caught","a":"and Taught",
    "s":"\u201cThese commandments \u2026 are to be on your hearts. Impress them on your children.\u201d \u2014 Deuteronomy 6:6\u20137",
    "tags":["daily faith","home","rhythms","Deuteronomy 6","intentional"],
    "q":["Faith is more often caught than taught. What is your family currently catching from your everyday life with God?",
         "Deuteronomy locates faith formation in ordinary moments \u2014 meals, drives, bedtimes. Which of those moments could become spiritual ground in your home?",
         "What would have to change for faith conversations to feel natural rather than forced in your family?"],
    "step":"Pick one daily moment \u2014 a meal, a drive, bedtime \u2014 and use it for one short faith conversation every day this week."},
   {"t":"A Faith","a":"of Their Own",
    "s":"\u201cYour sincere faith \u2026 first lived in your grandmother \u2026 and \u2026 your mother, and \u2026 now lives in you also.\u201d \u2014 2 Timothy 1:5",
    "tags":["ownership","sincere faith","2 Timothy 1","generational","authenticity"],
    "q":["Inherited faith eventually has to become owned faith. When did your faith become genuinely your own \u2014 and what helped?",
         "How can you create space for a young person to question and wrestle without losing their faith?",
         "What\u2019s the difference between pressuring a child toward faith and inviting them into it?"],
    "step":"Ask a younger person an open, non-anxious question about what they actually believe \u2014 and listen without correcting."},
   {"t":"Modeled,","a":"Not Just Mentioned",
    "s":"\u201cFollow my example, as I follow the example of Christ.\u201d \u2014 1 Corinthians 11:1",
    "tags":["modeling","example","integrity","1 Corinthians 11","authenticity"],
    "q":["The next generations \u2014 G2 and G3 \u2014 are always watching. What are they learning about God from watching you, not hearing you?",
         "Where is there a gap between the faith you talk about and the faith you live? How might a child read that gap?",
         "What is one practice you\u2019d want a young person to imitate after watching your life?"],
    "step":"Let someone younger see one part of your real walk with God this week \u2014 your prayer, your repentance, your generosity."},
   {"t":"The Table","a":"and the Talk",
    "s":"\u201cWe will tell the next generation the praiseworthy deeds of the Lord \u2026 the wonders he has done.\u201d \u2014 Psalm 78:4",
    "tags":["conversation","family table","storytelling","Psalm 78","intentional"],
    "q":["Where does meaningful conversation actually happen in your family \u2014 and how could faith have a place there?",
         "What keeps the dinner table (or its equivalent) from becoming a place of real connection?",
         "What is one \u201cpraiseworthy deed of the Lord\u201d from your life the next generation has never heard?"],
    "step":"Protect one shared meal this week with no screens, and tell one story of God\u2019s faithfulness at it."},
   {"t":"Faith Under","a":"Pressure",
    "s":"\u201cAlways be prepared to give an answer to everyone who asks you to give the reason for the hope that you have.\u201d \u2014 1 Peter 3:15",
    "tags":["doubt","questions","resilience","1 Peter 3","preparation"],
    "q":["The next generation is growing up with hard questions about faith. Are you a safe place for those questions, or a place to avoid them?",
         "What is a question about faith you\u2019re afraid a younger person will ask \u2014 and what would it take to face it together?",
         "How do you pass on a faith sturdy enough to survive a secular culture?"],
    "step":"Invite a young person to bring you their hardest question about faith \u2014 and commit to seeking the answer together."},
   {"t":"Handing Off","a":"the Baton","commit":True,
    "s":"\u201c\u2026entrust to reliable people who will also be qualified to teach others.\u201d \u2014 2 Timothy 2:2",
    "tags":["commitment","multiplication","discipleship","2 Timothy 2","handoff"],
    "q":["A baton dropped in the handoff loses the race. Where is your family\u2019s faith \u201chandoff\u201d strongest \u2014 and where is it most at risk?",
         "Beyond your own children, who is one younger believer you could pour faith into?",
         "What is the most important thing you\u2019ve learned in 40 days about passing on a living faith?"],
    "commit":("Each person names one young person they will intentionally disciple over the next year "
              "and one specific first step. The group prays over each name.")},
  ]},
 # 5 -----------------------------------------------------------------------
 {
  "num": 5, "color": "#8a4128",
  "category": "BUILDING THE HOME ON PURPOSE",
  "title": "Family", "accent": "by Design",
  "subhead": ("No one builds a house by accident \u2014 yet most families are constructed by drift, "
              "reacting to schedules and screens instead of being designed around a shared purpose."),
  "pullquote": ("\u201cA family without a design will be designed by everything else competing for it.\u201d"),
  "body": ("Family by Design brings the discipline of intentional construction to the most important "
           "thing most people will ever build. Proverbs says a house is built by wisdom and "
           "established through understanding \u2014 not by good intentions and busy calendars. <b>A "
           "flourishing family is not the accidental product of love alone but the deliberate result "
           "of a clear vision, a shared mission, and stated values that turn a household from a set "
           "of individuals into a family on purpose.</b> This series walks a congregation through "
           "drafting a family vision, mission, and values, and building the rhythms that hold them."),
  "scripture": "\u201cBy wisdom a house is built, and through understanding it is established.\u201d",
  "scripture_ref": "\u2014 Proverbs 24:3 (NIV)",
  "subtitles": ["A 40-Day Journey to an Intentional Family",
                "Discovering God\u2019s Design for the Home You Build",
                "A 40-Day Path to Family Vision, Mission, and Values",
                "From Family by Default to Family by Design"],
  "bigidea": ("A flourishing family is not the product of good intentions but of intentional design "
              "\u2014 a clear vision, a shared mission, and stated values that turn a household from a "
              "collection of busy individuals into a family on purpose."),
  "tags": ["intentionality","family vision","mission statement","values","rhythms","Proverbs 24"],
  "info": info("All church \u2014 couples, parents, blended families, engaged couples",
               "New Year \u00b7 Fall \u00b7 Marriage / family emphasis",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"Built","a":"or Drifted?",
    "s":"\u201cBy wisdom a house is built \u2026 through knowledge its rooms are filled with rare and beautiful treasures.\u201d \u2014 Proverbs 24:3\u20134",
    "tags":["intentional","drift","construction","Proverbs 24","design"],
    "q":["Be honest: is your family more the result of intentional design or of drift and reaction? What\u2019s the evidence?",
         "If your family is a house, what is it currently being \u201cbuilt\u201d around \u2014 and is that what you actually want?",
         "What would it look like to build your home \u201cby wisdom\u201d rather than by whatever fits the schedule?"],
    "step":"Name the one thing your family\u2019s life is most organized around right now, and ask whether it deserves that place."},
   {"t":"A Vision Only","a":"God Could Do",
    "s":"\u201cWrite down the revelation and make it plain \u2026 so that whoever reads it may run with it.\u201d \u2014 Habakkuk 2:2",
    "tags":["vision","future","clarity","Habakkuk 2","dream"],
    "q":["A vision statement is a short, memorable picture of a future only God could bring about. What future do you long for your family?",
         "If God did something in your family in the next 20 years that only He could do, what would it be?",
         "Why does a family rarely move toward a future it has never named?"],
    "step":"Draft a one-line family vision: \u201cOur family vision is \u2026\u201d Make it short, memorable, and God-sized."},
   {"t":"Your Family","a":"Mission",
    "s":"\u201cBut as for me and my household, we will serve the Lord.\u201d \u2014 Joshua 24:15",
    "tags":["mission","purpose","Joshua 24","unity","clarity"],
    "q":["A mission says why your family exists. Complete it roughly: \u201cOur family exists to \u2026\u201d What surfaces?",
         "How would a clear mission make hard family decisions \u2014 about money, time, conflict \u2014 simpler?",
         "Whose voice in the family still needs to be heard before a mission can truly be shared?"],
    "step":"Bring a draft family mission to the people it describes and invite their words into it before the next session."},
   {"t":"The Values","a":"That Guide Us",
    "s":"\u201cWhatever is true \u2026 noble \u2026 right \u2026 pure \u2026 lovely \u2026 admirable \u2014 think about such things.\u201d \u2014 Philippians 4:8",
    "tags":["values","character","Philippians 4","identity","conviction"],
    "q":["What five or six values do you most want to define your family \u2014 and which are actually lived right now?",
         "Where is there a gap between the values you claim and the values your calendar and bank statement reveal?",
         "Which one value, if your family truly lived it, would change the most?"],
    "step":"Write your family\u2019s top five values on paper, post them where everyone sees them, and pick one to practice this week."},
   {"t":"Rhythms and","a":"the Family Table",
    "s":"\u201cThey broke bread in their homes and ate together with glad and sincere hearts.\u201d \u2014 Acts 2:46",
    "tags":["rhythms","habits","family meetings","Acts 2","tradition"],
    "q":["Values live or die in rhythms. What weekly or yearly rhythm could carry your family\u2019s mission and values?",
         "What is one tradition from your past you want to keep \u2014 and one you want to start?",
         "What would a simple, regular family meeting look like in your home?"],
    "step":"Schedule one recurring family rhythm \u2014 a weekly meal, a monthly meeting, a yearly retreat \u2014 and put it on the calendar."},
   {"t":"Living","a":"the Design","commit":True,
    "s":"\u201cEveryone who hears these words of mine and puts them into practice is like a wise man who built his house on the rock.\u201d \u2014 Matthew 7:24",
    "tags":["commitment","practice","foundation","Matthew 7","wisdom"],
    "q":["A design on paper changes nothing until it\u2019s practiced. What is the first thing you\u2019ll actually do?",
         "Who in the family will help \u201ccarry the torch\u201d to keep the vision and values alive over time?",
         "What\u2019s the most important shift these 40 days have produced in how you build your home?"],
    "commit":("Each person commits to finalizing one element \u2014 vision, mission, or values \u2014 with "
              "their family in the next 30 days, and names one person to check in. Close by praying "
              "over each household.")},
  ]},
 # 6 -----------------------------------------------------------------------
 {
  "num": 6, "color": "#1f4d4f",
  "category": "LEGACY BUILT IN THE PRESENT TENSE",
  "title": "Legacy", "accent": "Living",
  "subhead": ("Legacy is not something you arrange at the end of your life. It is something you are "
              "building today, in a thousand ordinary moments you barely notice."),
  "pullquote": ("\u201cYour legacy is not written in your will. It is written in your Tuesdays.\u201d"),
  "body": ("Legacy Living dismantles the myth that legacy is a deathbed event. The faith your family "
           "will carry, the character they will imitate, the habits they will keep \u2014 all of it is "
           "being formed right now in how you live an unremarkable day. <b>The most important legacy "
           "work does not happen in an estate attorney\u2019s office; it happens in the ordinary "
           "rhythms your family watches you live.</b> This series helps a congregation stop "
           "postponing legacy to \u2018someday\u2019 and start building it in the present \u2014 through "
           "daily faithfulness, everyday generosity, and a life worth imitating."),
  "scripture": "\u201cWhatever you do, work at it with all your heart, as working for the Lord.\u201d",
  "scripture_ref": "\u2014 Colossians 3:23 (NIV)",
  "subtitles": ["A 40-Day Journey to Living Your Legacy Now",
                "Discovering God\u2019s Design for an Everyday Legacy",
                "A 40-Day Path to a Life Worth Imitating",
                "Building Your Legacy One Ordinary Day at a Time"],
  "bigidea": ("Legacy is not a document you sign at the end \u2014 it is the cumulative weight of how "
              "you live every ordinary day, which means the most important legacy work happens now, "
              "in the habits and choices your family watches you make."),
  "tags": ["daily faithfulness","habits","everyday legacy","generosity","presence","Colossians 3"],
  "info": info("All church \u2014 every household and stage of life",
               "Any season \u00b7 New Year \u00b7 Stewardship emphasis",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"Made in","a":"the Ordinary",
    "s":"\u201cWhatever you do, work at it with all your heart, as working for the Lord, not for human masters.\u201d \u2014 Colossians 3:23",
    "tags":["ordinary","faithfulness","daily","Colossians 3","work"],
    "q":["If legacy is built in ordinary days, what is your typical Tuesday teaching your family about what matters?",
         "Where do you tend to \u201cphone it in\u201d \u2014 and what might your family be learning from that?",
         "What would change if you treated your most routine responsibilities as work done for the Lord?"],
    "step":"Choose one ordinary, repeated task this week and do it as worship \u2014 fully present, with all your heart."},
   {"t":"What They See","a":"Is What They Keep",
    "s":"\u201cLet your light shine before others, that they may see your good deeds and glorify your Father.\u201d \u2014 Matthew 5:16",
    "tags":["example","visibility","modeling","Matthew 5","influence"],
    "q":["Your family keeps what they see far longer than what they\u2019re told. What are they seeing most consistently?",
         "What is one good habit you hope a younger person imitates \u2014 and are you actually living it visibly?",
         "What private inconsistency would most undermine the legacy you want to live?"],
    "step":"Identify one good practice you do privately and let it become visible to your family this week."},
   {"t":"Habits That","a":"Outlive Us",
    "s":"\u201cThree times a day he got down on his knees and prayed \u2026 just as he had done before.\u201d \u2014 Daniel 6:10",
    "tags":["habits","prayer","consistency","Daniel 6","rhythm"],
    "q":["Daniel\u2019s legacy was built on a settled, unshakable habit. What daily habit do you most want to outlive you?",
         "Which of your current habits, if multiplied across your descendants, would you be proud of \u2014 and which would worry you?",
         "What is one small habit you could begin now that could echo for generations?"],
    "step":"Start one simple, daily faith habit this week and track it \u2014 small and consistent beats large and occasional."},
   {"t":"Generosity as","a":"a Way of Life",
    "s":"\u201cEach of you should give what you have decided in your heart to give \u2026 for God loves a cheerful giver.\u201d \u2014 2 Corinthians 9:7",
    "tags":["generosity","giving","stewardship","2 Corinthians 9","open hands"],
    "q":["Is generosity a special event in your family or a normal rhythm? What are your children catching about giving?",
         "What would it take to make generosity part of your family\u2019s identity rather than an occasional gesture?",
         "Who is the most genuinely generous person you know, and what is different about how they hold money?"],
    "step":"Make one act of generosity together as a family this week \u2014 and talk about why you did it."},
   {"t":"Margin for","a":"What Matters",
    "s":"\u201cBe very careful, then, how you live \u2026 making the most of every opportunity.\u201d \u2014 Ephesians 5:15\u201316",
    "tags":["time","presence","margin","Ephesians 5","priorities"],
    "q":["Presence is the currency of legacy. Where is your time actually going \u2014 and where do you wish it went?",
         "What good thing is crowding out the best thing in your family\u2019s schedule?",
         "What would you have to say no to in order to be more present to the people who matter most?"],
    "step":"Protect one block of unhurried, agenda-free time with your family this week, and guard it like an appointment."},
   {"t":"Start","a":"Today","commit":True,
    "s":"\u201cLet us not become weary in doing good \u2026 as we have opportunity, let us do good to all.\u201d \u2014 Galatians 6:9\u201310",
    "tags":["commitment","start now","perseverance","Galatians 6","action"],
    "q":["If legacy is built today, what is the one thing you will stop postponing to \u2018someday\u2019?",
         "Which daily rhythm from these 40 days do you most want to keep?",
         "What has shifted in how you understand when legacy actually gets built?"],
    "commit":("Each person names one everyday legacy practice \u2014 a habit, a generosity, a rhythm of "
              "presence \u2014 they will begin now and sustain, and one person to ask about it in 30 days. "
              "Close in prayer.")},
  ]},
 # 7 -----------------------------------------------------------------------
 {
  "num": 7, "color": "#7a521e",
  "category": "CONFERRING VALUE & IDENTITY",
  "title": "Blessing the", "accent": "Next Generation",
  "subhead": ("Every child is asking two silent questions: Do you see me? Am I valued? The blessing "
              "is how a parent answers \u2014 with words, with presence, and with a future spoken over "
              "a life."),
  "pullquote": ("\u201cChildren do not outgrow their need for a blessing. They simply learn to stop "
                "asking for it.\u201d"),
  "body": ("Blessing the Next Generation recovers one of Scripture\u2019s most powerful and most "
           "neglected practices. A blessing is far more than a kind word \u2014 it is the intentional "
           "act of conferring value, affirming identity, and speaking a hopeful future over a life, "
           "the way God blessed His people and fathers blessed their children. <b>An unblessed "
           "generation will spend its life trying to earn what should have been freely given \u2014 a "
           "deep sense of being seen, loved, and believed in.</b> This series equips parents, "
           "grandparents, and mentors to speak meaningful blessing and to prepare, not merely "
           "provide for, those who come after them."),
  "scripture": ("\u201cThe Lord bless you and keep you; the Lord make his face shine on you and be "
                "gracious to you.\u201d"),
  "scripture_ref": "\u2014 Numbers 6:24\u201325 (NIV)",
  "subtitles": ["A 40-Day Journey into the Power of Blessing",
                "Discovering God\u2019s Design for Blessing Your Children",
                "A 40-Day Path to Conferring Value on the Next Generation",
                "Speaking Identity and Future Over Those You Love"],
  "bigidea": ("A blessing is more than a kind word \u2014 it is the intentional act of conferring value, "
              "affirming identity, and speaking a future over the next generation, the way God "
              "blessed His people and fathers in Scripture blessed their children."),
  "tags": ["blessing","affirmation","identity","words of life","preparing heirs","presence"],
  "info": info("All church \u2014 parents, grandparents, mentors, spiritual parents",
               "Father\u2019s / Mother\u2019s Day \u00b7 Fall \u00b7 Graduation season",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"The Power","a":"of a Blessing",
    "s":"\u201cThe Lord bless you and keep you; the Lord make his face shine on you.\u201d \u2014 Numbers 6:24\u201325",
    "tags":["blessing","Numbers 6","value","affirmation","intention"],
    "q":["Did you receive a clear blessing from your parents \u2014 a sense of being seen and believed in? How has its presence or absence shaped you?",
         "What is the difference between approval of what a child does and blessing of who a child is?",
         "Who in your life still needs to hear a blessing from you?"],
    "step":"Speak one specific, unearned word of blessing over a child or younger person this week \u2014 out loud."},
   {"t":"Words That","a":"Build a Life",
    "s":"\u201cThe tongue has the power of life and death.\u201d \u2014 Proverbs 18:21",
    "tags":["words","affirmation","Proverbs 18","speech","encouragement"],
    "q":["What words \u2014 said or unsaid \u2014 from a parent still echo in you, for good or ill?",
         "What is the ratio of correction to blessing in how you speak to the next generation?",
         "What specific words of life does someone in your family most need to hear from you right now?"],
    "step":"For one week, deliberately give one specific, genuine word of affirmation each day to someone younger."},
   {"t":"Seeing Each","a":"Child Uniquely",
    "s":"\u201cStart children off on the way they should go, and even when they are old they will not turn from it.\u201d \u2014 Proverbs 22:6",
    "tags":["uniqueness","calling","Proverbs 22","attention","design"],
    "q":["Proverbs points to a child\u2019s unique bent. What is the unique design of each young person in your life?",
         "Where might you be trying to shape a child into your plan rather than blessing the person God made them to be?",
         "What gift or strength in a young person have you noticed but never named to them?"],
    "step":"Tell one young person a specific strength or calling you see in them \u2014 something only attentive love would notice."},
   {"t":"Preparing,","a":"Not Just Providing",
    "s":"\u201cWhoever can be trusted with very little can also be trusted with much.\u201d \u2014 Luke 16:10",
    "tags":["preparing heirs","stewardship","Luke 16","readiness","wisdom"],
    "q":["It\u2019s easier to provide for children than to prepare them. Where have you defaulted to providing instead of preparing?",
         "What would it look like to hand on responsibility in increasing measures rather than all at once?",
         "Are the next generation ready to steward what you hope to leave them \u2014 and if not, what is the first lesson?"],
    "step":"Give a young person one new, real responsibility this week \u2014 and coach rather than rescue them through it."},
   {"t":"The Gift","a":"of Presence",
    "s":"\u201cLet the little children come to me \u2026 And he took the children in his arms \u2026 and blessed them.\u201d \u2014 Mark 10:14,16",
    "tags":["presence","attention","Mark 10","time","blessing"],
    "q":["Jesus blessed children by stopping for them. Where do the young people in your life experience your full, unhurried attention?",
         "What competes most for the presence your family actually needs from you?",
         "When did you last give someone younger your undivided attention \u2014 and what did it do for them?"],
    "step":"Give one young person an hour of undistracted, agenda-free presence this week."},
   {"t":"Speaking the","a":"Blessing","commit":True,
    "s":"\u201cMay he give you the dew of heaven \u2026 may nations serve you \u2026 \u201d \u2014 Genesis 27:28\u201329",
    "tags":["commitment","blessing","Genesis 27","words","legacy"],
    "q":["What full, intentional blessing do you most want to speak over the next generation \u2014 and what has held you back?",
         "How could blessing become a regular practice in your family rather than a one-time event?",
         "What has changed in these 40 days about how you understand the power of a spoken blessing?"],
    "commit":("Each person commits to writing and speaking one full blessing over a specific child or "
              "young person in the next 30 days, and names someone to follow up. The group prays a "
              "blessing over one another to close.")},
  ]},
 # 8 -----------------------------------------------------------------------
 {
  "num": 8, "color": "#2e4a52",
  "category": "INTERDEPENDENCE & THE HUNDRED-YEAR FAMILY",
  "title": "The Generational", "accent": "Life",
  "subhead": ("The world tells you to raise children to independence and send them off. God designed "
              "something richer \u2014 a family woven across generations, each one needing and "
              "strengthening the others."),
  "pullquote": ("\u201cIndependence raises a child. Interdependence raises a family that lasts a "
                "hundred years.\u201d"),
  "body": ("The Generational Life challenges the modern \u201cup-and-out\u201d theory of family \u2014 raise "
           "them, release them, and let them fend for themselves. The biblical vision is "
           "multi-generational and interdependent: generations loving, serving, and strengthening "
           "one another across decades. <b>God\u2019s ideal has never been the isolated, "
           "self-sufficient individual but the covenant family, where wisdom flows down, honor flows "
           "up, and faith is reaffirmed by each succeeding generation.</b> This series helps a "
           "congregation think in centuries, build interdependence without unhealthy dependence, "
           "and become a family that endures."),
  "scripture": "\u201cOne generation commends your works to another; they tell of your mighty acts.\u201d",
  "scripture_ref": "\u2014 Psalm 145:4 (NIV)",
  "subtitles": ["A 40-Day Journey into the Multi-Generational Family",
                "Discovering God\u2019s Design for the Hundred-Year Family",
                "A 40-Day Path from Independence to Interdependence",
                "Building a Family That Lasts for Generations"],
  "bigidea": ("God\u2019s vision for the family is not isolated independence but covenant "
              "interdependence \u2014 multiple generations loving, serving, and strengthening one "
              "another, so the family becomes a living testimony that outlasts any single life."),
  "tags": ["interdependence","multi-generational","honor","covenant","hundred-year family","Psalm 145"],
  "info": info("All church \u2014 extended families, grandparents, adult children",
               "Fall \u00b7 Holidays \u00b7 Family-reunion season",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"Up-and-Out","a":"or All-In?",
    "s":"\u201cMay you live to see your children\u2019s children. Peace be on Israel.\u201d \u2014 Psalm 128:6",
    "tags":["interdependence","family vision","Psalm 128","connection","design"],
    "q":["The culture\u2019s goal is independence; God\u2019s vision adds lifelong connection. Which has shaped your family more, and with what result?",
         "What\u2019s the difference between healthy interdependence and unhealthy dependence between generations?",
         "What would a more connected, all-in family look like for you \u2014 without losing healthy maturity?"],
    "step":"Take one step this week to deepen connection with a generation above or below you \u2014 a call, a visit, a meal."},
   {"t":"The","a":"Hundred-Year Family",
    "s":"\u201cKnow therefore that the Lord your God is \u2026 the faithful God, keeping his covenant \u2026 to a thousand generations.\u201d \u2014 Deuteronomy 7:9",
    "tags":["long view","covenant","Deuteronomy 7","vision","faithfulness"],
    "q":["What would change in your decisions if you genuinely thought of your family as a hundred-year project?",
         "What do you most hope is still true of your family in three generations?",
         "What would have to be intentionally articulated and reaffirmed for that to happen?"],
    "step":"Write one paragraph describing your family three generations from now if God answers your deepest prayers."},
   {"t":"Strength in","a":"Connection",
    "s":"\u201cA cord of three strands is not quickly broken.\u201d \u2014 Ecclesiastes 4:12",
    "tags":["unity","support","Ecclesiastes 4","strength","connection"],
    "q":["Where has connection across generations made your family stronger \u2014 and where has isolation made it weaker?",
         "Who in your family is currently carrying a burden alone that the family could help bear?",
         "How could your family function more like a team and less like separate households?"],
    "step":"Identify one family member carrying something heavy, and offer specific, practical help this week."},
   {"t":"Honoring Those","a":"Before Us",
    "s":"\u201cHonor your father and your mother, so that you may live long in the land.\u201d \u2014 Exodus 20:12",
    "tags":["honor","elders","Exodus 20","gratitude","respect"],
    "q":["Honor flows up as wisdom flows down. How well does your family honor its older generations?",
         "What wisdom or story would be lost if the oldest member of your family passed tomorrow?",
         "What is one way you could honor an older family member that you\u2019ve been meaning to do?"],
    "step":"Honor one older family member this week \u2014 a visit, a recorded conversation, a written word of gratitude."},
   {"t":"Carrying","a":"the Torch",
    "s":"\u201cI think it is right \u2026 to refresh your memory \u2026 to stir you up by way of reminder.\u201d \u2014 2 Peter 1:13",
    "tags":["reminder","values","2 Peter 1","reaffirming","continuity"],
    "q":["A hundred-year family requires values reaffirmed by each generation. Who in your family \u2018carries the torch\u2019 of what matters?",
         "What values or traditions are at risk of fading if no one deliberately keeps them alive?",
         "How do you pass responsibility for the family\u2019s heart to the next generation without forcing it?"],
    "step":"Name one value or tradition worth preserving and one younger person you\u2019ll invite to help carry it."},
   {"t":"A Family","a":"That Endures","commit":True,
    "s":"\u201cOne generation commends your works to another; they tell of your mighty acts.\u201d \u2014 Psalm 145:4",
    "tags":["commitment","endurance","Psalm 145","generations","continuity"],
    "q":["What is the single most important thing this group has shown you about the generational life?",
         "What is one way you will move your family from isolated independence toward covenant interdependence?",
         "Who will you commit to staying connected with across generations \u2014 and how?"],
    "commit":("Each person names one commitment to strengthen the multi-generational life of their "
              "family \u2014 a rhythm of connection, an act of honor, a tradition to keep \u2014 and one "
              "person to ask about it in 30 days. Close in prayer for the whole family line.")},
  ]},
 # 9 -----------------------------------------------------------------------
 {
  "num": 9, "color": "#3d4327",
  "category": "THE FOUNDATION THAT LASTS",
  "title": "Building a", "accent": "Spiritual Legacy",
  "subhead": ("You can transfer wealth in an afternoon. Transferring wisdom takes a lifetime \u2014 and "
              "it is the only transfer that decides whether everything else becomes a blessing or a "
              "burden."),
  "pullquote": ("\u201cWealth transfer fills a bank account. Wisdom transfer fills a life. Only one "
                "of them lasts.\u201d"),
  "body": ("Building a Spiritual Legacy addresses the foundation beneath every other kind of "
           "inheritance. The hard work of legacy planning usually fixates on the wealth transfer \u2014 "
           "but the greater and more neglected work is the wisdom transfer: passing on the faith, "
           "convictions, and character that make wealth a blessing rather than a curse. <b>Without a "
           "spiritual foundation, wealth becomes an idol and an inheritance becomes a burden; with "
           "it, even modest means become a generational blessing.</b> This series helps a "
           "congregation build the only foundation that lasts \u2014 a deliberate transfer of faith and "
           "wisdom to those who come after."),
  "scripture": "\u201cBy the grace God has given me, I laid a foundation as a wise builder.\u201d",
  "scripture_ref": "\u2014 1 Corinthians 3:10 (NIV)",
  "subtitles": ["A 40-Day Journey to a Spiritual Foundation That Lasts",
                "Discovering God\u2019s Design for Wisdom Transfer",
                "A 40-Day Path from Wealth Transfer to Wisdom Transfer",
                "Laying the Only Foundation a Family Can Build On"],
  "bigidea": ("The foundation of every lasting legacy is spiritual \u2014 a transfer of faith and "
              "wisdom that must be built deliberately, because without it wealth becomes an idol and "
              "an inheritance becomes a burden instead of a blessing."),
  "tags": ["spiritual foundation","wisdom transfer","faith","stewardship","legacy letter","1 Corinthians 3"],
  "info": info("All church \u2014 parents, business owners, those with assets to steward",
               "Year-end \u00b7 New Year \u00b7 Stewardship season",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"The Foundation","a":"Under Everything",
    "s":"\u201cNo one can lay any foundation other than the one already laid, which is Jesus Christ.\u201d \u2014 1 Corinthians 3:11",
    "tags":["foundation","Christ","1 Corinthians 3","priority","faith"],
    "q":["Every legacy is built on some foundation. What is your family\u2019s legacy actually built on right now?",
         "What happens to a family\u2019s wealth, name, or business when the spiritual foundation is missing?",
         "Where do you most need to strengthen the foundation before building anything else?"],
    "step":"Name the foundation your family\u2019s legacy is currently built on, and one way to make Christ more central to it."},
   {"t":"Wisdom Transfer vs.","a":"Wealth Transfer",
    "s":"\u201cThe beginning of wisdom is this: Get wisdom. Though it cost all you have, get understanding.\u201d \u2014 Proverbs 4:7",
    "tags":["wisdom","wealth","Proverbs 4","transfer","priorities"],
    "q":["Most legacy energy goes into transferring wealth. What would it look like to invest equally in transferring wisdom?",
         "What is the most important piece of wisdom you\u2019ve learned \u2014 from success or from failure \u2014 that the next generation needs?",
         "Why is wisdom so much harder to pass on than money, and what does that require of you?"],
    "step":"Write down three life lessons \u2014 including from your mistakes \u2014 you most want to transfer to those after you."},
   {"t":"The Faith","a":"You Model",
    "s":"\u201cHe decreed statutes \u2026 which he commanded our ancestors to teach their children.\u201d \u2014 Psalm 78:5",
    "tags":["modeling","faith","Psalm 78","example","teaching"],
    "q":["The strongest spiritual legacy is modeled, not lectured. What is your life actually teaching about following Jesus?",
         "Are you cultivating a family culture that visibly prioritizes Christ \u2014 prayer, Scripture, service? Where is it strong, where thin?",
         "What is one spiritual practice you want to be unmistakably part of your family\u2019s identity?"],
    "step":"Invite your family into one shared spiritual practice this week \u2014 prayer, Scripture, or serving someone together."},
   {"t":"Stewards,","a":"Not Owners",
    "s":"\u201cThe earth is the Lord\u2019s, and everything in it.\u201d \u2014 Psalm 24:1",
    "tags":["stewardship","ownership","Psalm 24","trust","surrender"],
    "q":["If God owns it all and you are a steward, how does that reframe what you\u2019re really \u2018leaving\u2019 anyone?",
         "Where do you still live as an owner rather than a manager of what God has entrusted to you?",
         "What would your family learn about money if they saw you hold it with open hands?"],
    "step":"Identify one area where you\u2019ve been holding tightly as an owner, and take one step to steward it with open hands."},
   {"t":"The Legacy","a":"Letter",
    "s":"\u201cWrite them on the doorframes of your house and on your gates.\u201d \u2014 Deuteronomy 6:9",
    "tags":["legacy letter","codifying","Deuteronomy 6","convictions","values"],
    "q":["If you wrote a letter to your children and grandchildren about faith and what matters most, what would it have to say?",
         "What spiritual conviction or family value has never been written down \u2014 and is therefore at risk of being lost?",
         "Why do we so often leave the most important things unspoken until it\u2019s too late?"],
    "step":"Begin a legacy letter this week: \u201cThe most important thing I want you to know about God and life is \u2026\u201d"},
   {"t":"Laying the","a":"Cornerstone","commit":True,
    "s":"\u201c\u2026built on the foundation \u2026 with Christ Jesus himself as the chief cornerstone.\u201d \u2014 Ephesians 2:20",
    "tags":["commitment","cornerstone","Ephesians 2","foundation","faith"],
    "q":["What is the most important thing you\u2019ve learned in 40 days about building a spiritual legacy?",
         "What is the one piece of wisdom or faith you are most determined to transfer \u2014 and to whom?",
         "What concrete step will you take to make your family\u2019s foundation more clearly Christ?"],
    "commit":("Each person commits to one act of wisdom transfer in the next 30 days \u2014 finishing a "
              "legacy letter, a recorded lesson, a discipleship conversation \u2014 and names one person "
              "to ask about it. Close in prayer over each family\u2019s foundation.")},
  ]},
 # 10 ----------------------------------------------------------------------
 {
  "num": 10, "color": "#73332a",
  "category": "COMPLETING THE HANDOFF",
  "title": "Passing Faith", "accent": "Forward",
  "subhead": ("A faith that is not handed forward dies in a single generation. The great commission "
              "begins at your own kitchen table \u2014 and the first people you are sent to are the ones "
              "who share your last name."),
  "pullquote": ("\u201cFaith is always one generation away from extinction. The handoff is everything.\u201d"),
  "body": ("Passing Faith Forward focuses on the moment everything depends on \u2014 the handoff. Faith "
           "does not survive by inheritance alone; it survives by being deliberately told and "
           "retold, modeled and multiplied, until the next generation owns it and hands it on again. "
           "<b>Scripture warns that a single generation can fail to pass it on, and the faith of "
           "centuries can vanish \u2014 which makes the deliberate handoff the most urgent work a "
           "believer ever does.</b> This series helps a congregation tell the family\u2019s "
           "God-story, equip the next generation to own it, and multiply faith beyond their own "
           "bloodline."),
  "scripture": ("\u201cWe will tell the next generation the praiseworthy deeds of the Lord, his power, "
                "and the wonders he has done.\u201d"),
  "scripture_ref": "\u2014 Psalm 78:4 (NIV)",
  "subtitles": ["A 40-Day Journey to Completing the Handoff of Faith",
                "Discovering God\u2019s Design for Passing Faith On",
                "A 40-Day Path from My Faith to Their Faith",
                "Telling, Modeling, and Multiplying a Living Faith"],
  "bigidea": ("Faith does not survive by inheritance alone \u2014 it survives by being deliberately "
              "handed forward, told and retold, modeled and multiplied, until the next generation "
              "owns it and hands it on again."),
  "tags": ["handoff","storytelling","remembrance","discipleship","multiplication","Psalm 78"],
  "info": info("All church \u2014 parents, grandparents, mentors, the whole congregation",
               "Fall discipleship launch \u00b7 New Year \u00b7 Any season",
               "Feeds into Family Legacy by Design"),
  "sessions": [
   {"t":"One Generation","a":"Away",
    "s":"\u201cAfter that whole generation \u2026 another generation grew up who knew neither the Lord nor what he had done.\u201d \u2014 Judges 2:10",
    "tags":["urgency","handoff","Judges 2","faith","generation"],
    "q":["Faith collapsed in Israel in one generation. What makes the handoff so fragile \u2014 even for committed families?",
         "Where do you sense the handoff is strong in your family \u2014 and where is it most at risk?",
         "What would it cost your family\u2019s future if this generation simply assumed faith would pass on by itself?"],
    "step":"Identify the weakest link in your family\u2019s faith handoff right now, and one step to strengthen it this month."},
   {"t":"Tell","a":"the Story",
    "s":"\u201cIn the future, when your children ask \u2026 tell them \u2026 \u201d \u2014 Joshua 4:6\u20137",
    "tags":["storytelling","memorial","Joshua 4","testimony","remembrance"],
    "q":["Israel built stone memorials so children would ask, \u201cWhat do these mean?\u201d What \u2018memorials\u2019 prompt faith conversations in your family?",
         "What is the central God-story of your family that must be told and retold?",
         "How do you tell your faith story in a way that invites the next generation in rather than lecturing them?"],
    "step":"Tell one God-story from your life to a younger person this week, and end with what it taught you about God."},
   {"t":"The Power","a":"of Remembering",
    "s":"\u201cBe careful that you do not forget the Lord \u2026 \u201d \u2014 Deuteronomy 6:12",
    "tags":["remembrance","gratitude","Deuteronomy 6","faithfulness","reminder"],
    "q":["Forgetting is the enemy of faith. How does your family deliberately remember what God has done?",
         "What spiritual marker or tradition helps your family remember \u2014 and what could you add?",
         "What past faithfulness of God are you in danger of forgetting in this season?"],
    "step":"Start one simple practice of remembrance \u2014 a family journal of answered prayers, a regular testimony time."},
   {"t":"From My Faith","a":"to Their Faith",
    "s":"\u201cContinue in what you have learned \u2026 from infancy you have known the Holy Scriptures.\u201d \u2014 2 Timothy 3:14\u201315",
    "tags":["ownership","Scripture","2 Timothy 3","conviction","handoff"],
    "q":["Faith must move from your conviction to their conviction. How do you help a young person own faith rather than just inherit it?",
         "What\u2019s the difference between forcing belief and forming the conditions where belief can take root?",
         "Who in your family is on the edge of owning \u2014 or walking away from \u2014 faith, and how can you walk with them?"],
    "step":"Have one unhurried, non-defensive conversation with a younger person about where they actually are with God."},
   {"t":"Multiplying Beyond","a":"the Family",
    "s":"\u201cEntrust to reliable people who will also be qualified to teach others.\u201d \u2014 2 Timothy 2:2",
    "tags":["multiplication","mentoring","2 Timothy 2","discipleship","spiritual family"],
    "q":["Passing faith forward isn\u2019t limited to bloodline. Who outside your family could you invest in spiritually?",
         "Who poured into you who wasn\u2019t a relative \u2014 and what did that mean?",
         "What would it look like to become a spiritual parent to someone who has no one passing faith to them?"],
    "step":"Identify one person beyond your family you could begin to disciple, and take a first step toward them this week."},
   {"t":"The","a":"Handoff","commit":True,
    "s":"\u201cGo and make disciples \u2026 teaching them to obey everything I have commanded you.\u201d \u2014 Matthew 28:19\u201320",
    "tags":["commitment","commission","Matthew 28","discipleship","handoff"],
    "q":["The great commission starts at home. Who are the people you are most clearly \u2018sent\u2019 to with the gospel?",
         "What is the most important thing these 40 days have shown you about passing faith forward?",
         "What is the one handoff you will not leave to chance, starting now?"],
    "commit":("Each person names the specific people \u2014 within and beyond the family \u2014 they will "
              "intentionally pass faith to, one concrete next step, and one person to ask about it in "
              "30 days. The group prays over each name to close the journey.")},
  ]},
]
