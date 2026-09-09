# -*- coding: utf-8 -*-
"""All copy for the Family Legacy Intelligence suite."""

TM = "\u2122"
BRAND = "Family Legacy Intelligence" + TM
PROMISE = ("Discover what your family has received, what it must strengthen, "
           "and what it is called to pass forward.")
AUDIENCE = "For Christian Financial Advisors Serving High-Capacity Families"

NAVY = "#16233A"
INK = "#2B3440"
GOLD = "#A67C3D"

# ---------------------------------------------------------------- assessment
DIMENSIONS = [
    dict(n=1, color="#2B5C9B", title="Faith and Spiritual Heritage",
         wheel=("Faith &", "Spiritual Heritage"),
         q="What have we received spiritually, and what are we intentionally passing forward?",
         items=[
             "Our children and grandchildren understand the faith convictions that guide our family.",
             "We regularly tell stories about God\u2019s faithfulness throughout our family\u2019s history.",
             "Prayer, Scripture, worship, and spiritual conversations are natural parts of our family life.",
             "We have intentionally discussed what we hope future generations will believe about God.",
         ]),
    dict(n=2, color="#0F7A6C", title="Family Story, Identity, and Values",
         wheel=("Family Story,", "Identity & Values"),
         q="Does our family know who we are and what we stand for?",
         items=[
             "Our family knows the important people, sacrifices, challenges, and turning points that shaped us.",
             "We can clearly name the values we want our family to represent.",
             "Our financial and lifestyle decisions generally reflect those values.",
             "Our children and grandchildren experience a meaningful sense of family identity and belonging.",
         ]),
    dict(n=3, color="#B85C3B", title="Relationships and Family Unity",
         wheel=("Relationships &", "Family Unity"),
         q="Are our relationships strong enough to carry the legacy we hope to leave?",
         items=[
             "Family members can discuss difficult subjects without withdrawing, attacking, or dividing.",
             "We have addressed \u2014 or are actively addressing \u2014 significant hurts, conflicts, and misunderstandings.",
             "Family members feel heard, respected, loved, and valued across generations.",
             "Our family knows how to disagree while protecting relationships and honoring one another.",
         ]),
    dict(n=4, color="#6B4E9E", title="Wisdom and Next-Generation Preparation",
         wheel=("Wisdom & Next-", "Generation Preparation"),
         q="Are we preparing our heirs for responsibility, not merely inheritance?",
         items=[
             "We intentionally share the lessons we have learned through faith, work, success, failure, and adversity.",
             "Our children and grandchildren are developing the character and competence needed to steward responsibility.",
             "We have meaningful conversations about work, calling, money, generosity, leadership, and purpose.",
             "Younger family members are gradually being invited into age-appropriate family decisions and responsibilities.",
         ]),
    dict(n=5, color="#A8811C", title="Stewardship, Wealth, and Generosity",
         wheel=("Stewardship, Wealth", "& Generosity"),
         q="Do our resources serve our faith, values, family, and Kingdom purpose?",
         items=[
             "Our family has a shared understanding that everything ultimately belongs to God.",
             "We have explained the purpose behind our wealth, property, business interests, opportunities, and influence.",
             "Our children and grandchildren are being prepared to receive resources without developing entitlement.",
             "Giving, serving, and generosity are shared family practices rather than private financial transactions.",
         ]),
    dict(n=6, color="#2F6B45", title="Succession, Communication, and Enduring Legacy",
         wheel=("Succession &", "Enduring Legacy"),
         q="Have we prepared the people as carefully as we have prepared the documents?",
         items=[
             "Our estate, succession, business, and charitable plans reflect our deeper values and intentions.",
             "Appropriate family members understand the general direction of our plans and the reasons behind them.",
             "We have identified the stories, beliefs, blessings, wisdom, and instructions we want preserved.",
             "We have a practical process for continuing legacy conversations across generations.",
         ]),
]

SCALE = [("1", "Not true of our family"), ("2", "Rarely true"), ("3", "Somewhat true"),
         ("4", "Mostly true"), ("5", "Clearly and consistently true")]

INSTRUCTIONS = ("Rate each statement from 1 to 5. Answer honestly based on what is happening now "
                "\u2014 not what you hope will happen someday.")

PREAMBLE = ("This experience helps a family move beyond financial planning into a deeper "
            "conversation about faith, relationships, wisdom, stewardship, generosity, and "
            "multigenerational legacy. It is not intended to measure whether a family is "
            "\u201cgood\u201d or \u201cbad.\u201d It helps identify the first area of "
            "Family Legacy Intelligence" + TM + " your family may want to explore.")

DISCERN_INTRO = ("Your lowest-scoring section may reveal the first layer of Family Legacy "
                 "Intelligence your family should explore. However, the lowest score is not "
                 "automatically the first priority. Consider three questions:")

QUESTIONS3 = [
    "Where would growth create the greatest positive impact?",
    "Which issue becomes more difficult if we continue postponing it?",
    "Where do we currently sense God inviting us to act?",
]

BANDS = [
    ("96\u2013120", "Intentional Legacy Formation", "#2F6B45",
     "Your family has established many strong legacy practices. Your next opportunity is to document, deepen, and multiply them."),
    ("72\u201395", "Emerging Legacy Alignment", "#A8811C",
     "Important pieces are present, but greater clarity, communication, and intentionality are needed."),
    ("48\u201371", "Legacy Conversations Needed", "#B85C3B",
     "Your family has valuable stories, faith, wisdom, and resources, but much of the legacy remains undocumented or undiscussed."),
    ("24\u201347", "Begin with Trust and Discovery", "#6B4E9E",
     "Start slowly. Prioritize relationships, listening, family stories, and shared values before addressing complex financial or succession decisions."),
]

# ---------------------------------------------------------------- interviews
PERMISSION = ("This conversation may be recorded \u2014 with your permission \u2014 and "
              "transcribed, so that your words, stories, and convictions are preserved "
              "accurately. With your permission, the material can then be used to create "
              "private, personalized devotionals and family legacy experiences for you, "
              "your children, and your grandchildren.")

LISTENING_FOR = ["Stories", "Scripture", "Convictions", "Family language", "Defining moments",
                 "Wounds and turning points", "Lessons learned", "Hopes and fears",
                 "Blessings", "Unfinished conversations"]

INTERVIEWS = [
    dict(
        slug="couple",
        color="#2B5C9B",
        kicker="Instrument Two",
        title="The Couple Legacy Interview",
        subtitle="Ten Questions for the Matriarch and Patriarch to Answer Together",
        deck="A guided conversation about the faithfulness of God, the values that formed you, and what you most want to place into the hands of the next generation.",
        why=[("Why this conversation matters",
              "You have spent years preparing your assets for your family. This conversation begins preparing your family for the assets \u2014 and preserving the faith, values, wisdom, and stories that matter even more."),
             ("What it produces",
              "Answered together and preserved in your own words, this conversation becomes the primary source material for every personalized devotional, family meeting, and legacy experience built for your children and grandchildren.")],
        how=["Answer together, out loud, with both of you present.",
             "There are no wrong answers and nothing to score.",
             "Take the questions in order, but follow the stories wherever they lead.",
             "Ninety minutes is typical. Two conversations is common."],
        questions=[
            ("When you look back over your marriage and family life, where do you most clearly see the faithfulness of God?",
             "Consider spiritual turning points, answered prayer, provision, protection, redirection, healing, and unexpected grace."),
            ("What people, experiences, hardships, and opportunities most shaped the family you have become?",
             "Think about parents, grandparents, mentors, churches, businesses, financial seasons, losses, failures, and major decisions."),
            ("What three to five values do you most want your family name to represent?",
             "Describe what each value looks like in actual behavior \u2014 not merely as an attractive word."),
            ("What have you learned about marriage, love, forgiveness, commitment, and staying united?",
             "Share honest lessons about both strength and struggle."),
            ("What have you learned about work, success, money, wealth, responsibility, and contentment?",
             "Consider how your understanding has changed over time."),
            ("What do you hope your children and grandchildren will understand about why God has entrusted resources and influence to your family?",
             "Speak to stewardship, opportunity, ownership, generosity, responsibility, and purpose."),
            ("What concerns do you have about the impact that success, wealth, comfort, or inheritance could have on future generations?",
             "Consider entitlement, dependency, conflict, loss of motivation, spiritual drift, secrecy, and family fragmentation."),
            ("What wisdom do you wish you had received when you were younger \u2014 and what wisdom do you now feel responsible to pass forward?",
             "Include what you would say about faith, marriage, parenting, vocation, money, leadership, adversity, and finishing well."),
            ("What conversations have you delayed because they feel difficult, emotional, complicated, or potentially divisive?",
             "Nothing needs to be resolved here. Simply name the conversations that still need to happen."),
            ("When your children and grandchildren describe your legacy decades from now, what do you hope they will say you gave them?",
             "Think beyond assets \u2014 name the faith, love, memories, wisdom, opportunities, blessings, and examples you hope will live on."),
        ],
        closing_title="Our Shared Legacy Statement",
        closing=[
            "The five stories our family should never forget:",
            "The values our family name should represent:",
            "The Scripture or biblical theme that guides our family:",
            "The one conversation we are ready to begin:",
        ],
    ),
    dict(
        slug="patriarch",
        color="#1E5F5A",
        kicker="Instrument Three",
        title="The Patriarch Legacy Interview",
        subtitle="A Private Conversation About Faith, Responsibility, Wisdom, and Blessing",
        deck="A place to reflect personally on what you have carried, what you have learned, what you would do differently, and what you most want to pass forward.",
        why=[("Why this conversation matters",
              "These questions are not intended to reinforce stereotypes about men or family leadership. They create space for the father, grandfather, founder, or senior family leader to speak plainly about the weight he has carried and the blessing he wants to leave."),
             ("What it produces",
              "Your answers become a preserved record in your own voice \u2014 and the foundation of a written blessing your children and grandchildren can hold long after the conversation ends.")],
        how=["This is private. Nothing is shared without your permission.",
             "Write, dictate, or speak your answers aloud to be recorded.",
             "Where a question is difficult, say so and keep going.",
             "Complete the Legacy Statement at the end in your own words."],
        questions=[
            ("What did you learn from your father, grandfather, or the men who shaped you?",
             "What did you receive from them that you want to preserve? What do you want to do differently?"),
            ("When have you felt the greatest weight of responsibility for your family?",
             "Describe a season when leadership, provision, protection, faith, or decision-making felt especially costly."),
            ("What experiences most shaped your understanding of manhood, leadership, and faithfulness?",
             "Who modeled these qualities well? Which experiences corrected or refined your understanding?"),
            ("What have success and failure taught you about your true identity?",
             "How have achievement, disappointment, recognition, loss, or regret affected your relationship with God and your family?"),
            ("What sacrifices have you made that your family may not fully know or understand?",
             "Share these without seeking recognition or creating obligation. What motivated those sacrifices?"),
            ("What mistakes do you hope the next generation will learn from without having to repeat?",
             "What would you tell your younger self about faith, marriage, parenting, work, money, or priorities?"),
            ("What do you most want your sons, daughters, and grandchildren to understand about work and responsibility?",
             "What does meaningful work look like? How should they think about ambition, excellence, rest, provision, and service?"),
            ("What does it mean to you to bless your children and grandchildren?",
             "What words of affirmation, identity, permission, challenge, prayer, or encouragement do you want each person to receive?"),
            ("Is there anything you still need to say, repair, confess, forgive, or make clear?",
             "This may include a relationship, decision, misunderstanding, expectation, or family transition."),
            ("What do you want to place into the hands of the next generation before your life is complete?",
             "Consider faith, wisdom, responsibility, opportunity, relationships, leadership, generosity, and blessing \u2014 not only financial assets."),
        ],
        closing_title="Patriarch Legacy Statement",
        closing=[
            "The most important thing I want my family to know is:",
            "The blessing I want to speak over the next generation is:",
            "The responsibility I hope they will carry is:",
        ],
    ),
    dict(
        slug="matriarch",
        color="#6B4E9E",
        kicker="Instrument Four",
        title="The Matriarch Legacy Interview",
        subtitle="A Private Conversation About Faith, Relationships, Strength, Wisdom, and Family Culture",
        deck="A place to describe the relational, spiritual, cultural, and practical legacy you have carried \u2014 and the qualities you pray will mark your family for generations.",
        why=[("Why this conversation matters",
              "Much of what holds a family together is built quietly and rarely recorded. These questions create space for the mother, grandmother, founder, or senior family leader to name the culture she created and the convictions behind it."),
             ("What it produces",
              "Your answers preserve the traditions, prayers, and practices that would otherwise be lost \u2014 and become the foundation of a written blessing for the generations that follow.")],
        how=["This is private. Nothing is shared without your permission.",
             "Write, dictate, or speak your answers aloud to be recorded.",
             "Small details matter here \u2014 a recipe, a prayer, a phrase you always said.",
             "Complete the Legacy Statement at the end in your own words."],
        questions=[
            ("What did you learn from your mother, grandmother, or the women who shaped you?",
             "What qualities, practices, stories, and convictions did they give you? What patterns did you choose to change?"),
            ("What experiences most shaped the woman, wife, mother, grandmother, or leader you became?",
             "Consider joys, sacrifices, disappointments, transitions, mentors, losses, and encounters with God."),
            ("What have you done to create belonging, connection, and emotional safety within the family?",
             "Which traditions, conversations, celebrations, meals, prayers, or acts of care have mattered most?"),
            ("What strengths have helped you carry the family through difficult seasons?",
             "How did faith, courage, perseverance, discernment, hospitality, forgiveness, or advocacy shape those seasons?"),
            ("What sacrifices or unseen contributions might your family not fully recognize?",
             "What would you want them to understand about the heart behind those choices?"),
            ("What have marriage and family relationships taught you about love, grace, boundaries, and forgiveness?",
             "What do you hope future generations practice differently because of what you learned?"),
            ("What do you most want your daughters, sons, and grandchildren to understand about identity and worth?",
             "How can they resist defining themselves only through achievement, appearance, wealth, approval, or family expectations?"),
            ("What family stories, traditions, recipes, practices, prayers, or celebrations should never be lost?",
             "Why do they matter, and what do they reveal about the family\u2019s values?"),
            ("Is there a relationship, hurt, misunderstanding, or unspoken hope that you would like to see addressed?",
             "What would healing, clarity, or reconciliation look like?"),
            ("What qualities do you pray will characterize your family for generations?",
             "Consider faith, kindness, courage, hospitality, unity, generosity, resilience, service, and love."),
        ],
        closing_title="Matriarch Legacy Statement",
        closing=[
            "The heart of our family that I most want preserved is:",
            "The wisdom I most want to pass forward is:",
            "My prayer for future generations is:",
        ],
    ),
    dict(
        slug="next-generation",
        color="#2F6B45",
        kicker="Instrument Five",
        title="The Next-Generation Legacy Interview",
        subtitle="Ten Questions Children and Grandchildren Can Ask Parents and Grandparents",
        deck="The next generation is not a passive recipient of wealth or family history. These questions make them listeners, storytellers, learners, and future stewards.",
        why=[("Why this conversation matters",
              "Most families assume the stories will simply be there when someone finally asks. They rarely are. This conversation gives a son, daughter, or grandchild a meaningful role \u2014 and a reason to ask now."),
             ("What it produces",
              "A recorded family archive in the elder\u2019s own voice, plus the next generation\u2019s own written reflection on what they will carry forward and what responsibility they are willing to accept.")],
        how=["Ask permission to record before you begin.",
             "Ask one question and then stop talking. The pauses do the work.",
             "Ask for the story, not the summary.",
             "Complete your own reflection page afterward, while it is fresh."],
        questions=[
            ("What was life like in your family when you were growing up?",
             "Ask about home, church, school, community, celebrations, responsibilities, and relationships."),
            ("Who influenced your faith most deeply, and what did that person give you?",
             "Ask for a story that shows the influence, not just a name."),
            ("What were some of the hardest seasons of your life, and how did those experiences change you?",
             "What helped you persevere? Where did you see God?"),
            ("What decisions most changed the direction of your life, marriage, family, career, or faith?",
             "Looking back, how did you make those decisions?"),
            ("What are you most grateful for when you think about our family?",
             "Which people, memories, opportunities, traditions, or examples mean the most?"),
            ("What mistakes or regrets have taught you the most?",
             "What would you want our generation to learn from them?"),
            ("How did you learn to think about work, money, saving, investing, giving, and contentment?",
             "How has your perspective changed as you have grown older?"),
            ("What do you believe God has uniquely entrusted to our family?",
             "This could include relationships, faith, influence, knowledge, a business, resources, a place, a story, or an opportunity to serve."),
            ("What do you hope our generation preserves \u2014 and what do you hope we have the courage to change?",
             "Invite both affirmation and freedom. Legacy should guide the next generation without controlling it."),
            ("What blessing, prayer, or message would you like to speak personally over me and my generation?",
             "Record the response in the family member\u2019s own voice whenever possible."),
        ],
        closing_title="Next-Generation Reflection",
        closing=[
            "The story I most want to remember is:",
            "The value I want to carry forward is:",
            "The question I still want to ask is:",
            "The responsibility I am willing to accept is:",
        ],
    ),
]

# ---------------------------------------------------------------- brochure
PROBLEMS = [
    ("Wealth transfers. Values do not.",
     "Shared mission, spiritual clarity, and generational alignment do not travel automatically with a balance sheet. They require intentional conversation and leadership."),
    ("Legacy does not happen by accident.",
     "We are living through the largest wealth transfer in history, yet wealth alone has never created unity or wisdom in a family."),
    ("The documents are prepared. The people are not.",
     "Estate, succession, and charitable plans are complete and current while the family that will receive them has never discussed what any of it is for."),
    ("Drift eventually divides.",
     "Without preparation and clarity, what was meant to bless a family can quietly divide it \u2014 not through malice, but through silence."),
    ("Distribution is not preparation.",
     "The question is not simply what will be passed down. It is who the next generation is becoming before they receive it."),
]

BEFORE_PAIRS = [
    ("Faith", "fortune"), ("Wisdom", "wealth"), ("Character", "capital"),
    ("Responsibility", "inheritance"), ("Relationships", "structures"),
    ("Purpose", "possessions"), ("Generosity", "accumulation"), ("Blessing", "transition"),
]

INSTRUMENTS = [
    dict(no="01", name="Family Legacy Intelligence Assessment", color="#16233A",
         time="10 minutes \u00b7 completed together",
         purpose="Establishes a shared starting point without requiring anyone to be vulnerable first.",
         surfaces=["Six dimensions of family legacy", "Twenty-four honest self-ratings",
                   "The lowest-scoring dimension", "The first layer worth exploring"],
         produces="A scored legacy profile and one clear answer to the question every family asks first: where do we begin?"),
    dict(no="02", name="The Couple Legacy Interview", color="#2B5C9B",
         time="90 minutes \u00b7 both spouses present \u00b7 recorded",
         purpose="Captures the family\u2019s founding story, convictions, and language in the founders\u2019 own words.",
         surfaces=["Stories, Scripture, and convictions", "Defining moments and turning points",
                   "Lessons learned and hopes and fears", "Unfinished conversations"],
         produces="The primary source transcript from which every personalized devotional and family experience is built."),
    dict(no="03", name="The Patriarch Legacy Interview", color="#1E5F5A",
         time="60 minutes \u00b7 private",
         purpose="Gives the senior male family leader room to speak about what he has carried and what he wants to bless.",
         surfaces=["What he received from the men before him", "The true cost of responsibility",
                   "Sacrifices the family never saw", "What still needs to be said or repaired"],
         produces="A written patriarch legacy statement and a blessing addressed to the next generation."),
    dict(no="04", name="The Matriarch Legacy Interview", color="#6B4E9E",
         time="60 minutes \u00b7 private",
         purpose="Preserves the relational, spiritual, and cultural legacy that holds a family together.",
         surfaces=["Traditions, prayers, and practices", "The strengths that carried hard seasons",
                   "Unseen contributions", "Hopes for healing and reconciliation"],
         produces="A written matriarch legacy statement and a prayer for the generations that follow."),
    dict(no="05", name="The Next-Generation Legacy Interview", color="#2F6B45",
         time="60 minutes \u00b7 led by a child or grandchild \u00b7 recorded",
         purpose="Turns the next generation from recipients into listeners, learners, and future stewards.",
         surfaces=["The family story in the elder\u2019s own voice", "What the elders hope is preserved",
                   "What they give permission to change", "A spoken blessing over the next generation"],
         produces="A family archive recording and the next generation\u2019s written statement of the responsibility they accept."),
]

JOURNEYS = [
    ("Couple\u2019s Marriage Journey", "The Story God Has Written Through Us", "#2B5C9B",
     "A private devotional journey for the matriarch and patriarch",
     ["Courtship and marriage story", "Defining decisions", "Seasons of sacrifice",
      "Lessons from conflict", "Moments of God\u2019s faithfulness", "Shared values",
      "Unfinished conversations", "Prayers for the remaining years", "A vision for finishing well"]),
    ("Children\u2019s Legacy Journey", "What We Want You to Know", "#1E5F5A",
     "A personalized devotional for adult children",
     ["The family\u2019s spiritual story", "Lessons about identity", "Lessons about marriage",
      "Lessons about work", "Lessons about money", "Family values",
      "Stories of failure and resilience", "The purpose behind the family\u2019s resources",
      "Words of blessing and invitations to responsibility"]),
    ("Grandchildren\u2019s Legacy Journey", "The Story You Are Part Of", "#A8811C",
     "An age-appropriate experience for grandchildren",
     ["Family origin stories", "Photographs and milestones", "Stories of courage and faith",
      "Simple family values", "Grandparent prayers", "Questions for conversation",
      "Generosity activities and service projects", "A personal blessing for each grandchild",
      "Space to add to the family story"]),
    ("Whole-Family Legacy Campaign", "What Will Live On?", "#2F6B45",
     "A six-session experience for the entire family",
     ["Remember the Story", "Recognize God\u2019s Faithfulness", "Clarify What Matters Most",
      "Strengthen the Relationships", "Prepare the Generations",
      "Choose What We Will Pass Forward"]),
]

SESSIONS = [
    ("Remember the Story", "What has shaped our family?"),
    ("Recognize God\u2019s Faithfulness", "Where has God led, provided, protected, and redeemed?"),
    ("Clarify What Matters Most", "What values and convictions should define us?"),
    ("Strengthen the Relationships", "What must be celebrated, protected, repaired, or discussed?"),
    ("Prepare the Generations", "What wisdom, character, and responsibility must be developed?"),
    ("Choose What We Will Pass Forward",
     "How will our faith, wisdom, generosity, influence, and resources serve future generations?"),
]

STEPS = [
    ("Invitation", "Positioned as a value-added family service, never a sales presentation."),
    ("Family Assessment", "The couple completes the ten-minute Family Legacy Intelligence Assessment."),
    ("Recorded Couple Interview", "The advisor facilitates the ten joint questions with both spouses present."),
    ("Individual Interviews", "The patriarch and matriarch complete their private legacy interviews."),
    ("Next-Generation Conversation", "Selected children or grandchildren ask the next-generation questions."),
    ("Intelligence Summary", "A private summary of strengths, unspoken priorities, legacy risks, core values, next-generation needs, and planning implications."),
    ("Personalized Legacy Experience", "The Journey Builder produces the first devotional, conversation guide, family meeting, or six-session campaign."),
    ("Professional Planning Alignment", "With permission, insights inform the attorney, CPA, business advisor, generosity advisor, family coach, pastor, and trustee."),
]

INVITATION_QUOTE = ("We have spent considerable time helping you prepare your assets for your "
                    "family. We would also like to help prepare your family for the assets \u2014 "
                    "and preserve the faith, values, wisdom, and stories that matter even more.")

CONFIDENTIALITY = ("Private spiritual and relational disclosures are never treated as sales "
                   "intelligence. All material remains confidential, permission-based, securely "
                   "stored, and used only for the purposes the family has stated.")

CAPTURE = ["Five defining family stories", "Five core family values",
           "Three significant faith experiences", "Three major lessons from hardship",
           "Three lessons about marriage and relationships", "Three lessons about work and calling",
           "Three lessons about money and stewardship", "Three hopes for the next generation",
           "Three concerns for the next generation", "One family legacy statement",
           "One guiding Scripture or biblical theme", "One immediate family action step"]

CLOSING_LINE = ("The goal is not a successful estate transfer. It is a prepared family, a "
                "preserved story, a strengthened marriage, an equipped next generation, and a "
                "legacy that continues to bear fruit.")
