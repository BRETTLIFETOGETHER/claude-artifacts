/* ════════════════════════════════════════════════════════════════
   FAMILY LEGACY CAMPAIGN INTELLIGENCE™ · source: Tom & Brett's
   intelligence document. Loads after data.js; extends FLC.
   ════════════════════════════════════════════════════════════════ */
(function(){
'use strict';
var FLI = window.FLI = {};

/* ---------- core purpose ---------- */
FLI.purpose = {
  q: "What do we want our family to know, believe, practice, preserve, and pass forward?",
  topics: ["Faith","Family identity","Shared values","Relationships","Stories","Wisdom","Wealth","Responsibility","Generosity","Leadership","Succession","Eternal legacy"],
  components: ["Weekend messages","Six-session curriculum","Daily readings","Family conversations","Couple exercises","Children and student editions","Grandparent resources","Advisor or facilitator guides","Legacy projects","Family meeting tools","Assessments","Commitment experiences"]
};

/* ---------- the 100 campaigns · 10 domains ---------- */
FLI.domains = [
{id:"d1", n:"Family Identity and Story", c:[
 ["The Story We Carry","Discovering the people, places, sacrifices, and moments that shaped our family."],
 ["Remember Who You Are","Building a family identity rooted in faith, values, and belonging."],
 ["Our Family Story","Preserving the stories future generations should never forget."],
 ["The Roots Beneath Us","Understanding how family history continues to shape present relationships."],
 ["Nothing Is Wasted","Redeeming family pain, setbacks, and disappointments through faith."],
 ["The People Who Made Us","Honoring the mentors, relatives, and spiritual influences behind our lives."],
 ["Milestones That Matter","Remembering the defining moments that changed the direction of our family."],
 ["The Family Name","Living in a way that gives integrity and meaning to what our name represents."],
 ["Our Shared Inheritance","Recognizing the spiritual, relational, cultural, and practical gifts we received."],
 ["Tell It to the Next Generation","Creating a deliberate plan to preserve and share the family story."]]},
{id:"d2", n:"Faith and Spiritual Heritage", c:[
 ["Faith Worth Passing On","Building a spiritual inheritance that can outlast financial wealth."],
 ["As for Me and My House","Clarifying the spiritual commitments that will guide our family."],
 ["Generations of Faith","Strengthening belief and discipleship across children, parents, and grandparents."],
 ["The God Who Has Led Us","Remembering God\u2019s faithfulness throughout the family journey."],
 ["Sacred Stories","Sharing the moments when God met, guided, protected, or redirected our family."],
 ["A Faith of Their Own","Helping the next generation move from inherited belief to personal conviction."],
 ["Blessing the Generations","Using words, prayers, and presence to affirm the people coming behind us."],
 ["The Family Altar","Restoring simple rhythms of prayer, Scripture, worship, and spiritual conversation."],
 ["Spiritual Grandparenting","Helping grandparents become intentional mentors and faith-builders."],
 ["An Eternal Family Legacy","Defining success in light of faithfulness, discipleship, and eternity."]]},
{id:"d3", n:"Family Values and Vision", c:[
 ["What Matters Most","Naming the values our family wants to live and be remembered by."],
 ["The Family Mission","Creating a shared statement of purpose for the generations."],
 ["Our Nonnegotiables","Clarifying the convictions that should guide family decisions."],
 ["The Life We Want to Build","Aligning relationships, resources, priorities, and practices with a shared vision."],
 ["Living What We Believe","Turning family values from attractive words into observable behaviors."],
 ["The Family Compass","Using shared principles to navigate difficult choices and changing seasons."],
 ["A Culture of Honor","Building a family known for respect, gratitude, responsibility, and love."],
 ["More Than Success","Redefining achievement around character, contribution, and faithfulness."],
 ["Our Family Constitution","Developing shared commitments for relationships, leadership, wealth, and service."],
 ["The Legacy We Choose","Moving from an accidental inheritance to an intentional family legacy."]]},
{id:"d4", n:"Relationships and Reconciliation", c:[
 ["Stronger Together","Building the trust and relational strength required for a lasting legacy."],
 ["The Conversations We Avoid","Learning to address difficult family issues with courage and grace."],
 ["Repairing the Family Story","Confronting wounds without allowing them to define future generations."],
 ["The Freedom of Forgiveness","Releasing resentment and creating room for relational healing."],
 ["Building Bridges Across Generations","Strengthening relationships between grandparents, parents, and adult children."],
 ["When Families Disagree","Navigating conflict without dividing the family."],
 ["Listening Before Leading","Creating a family culture in which every generation feels heard and valued."],
 ["Grace for Imperfect Families","Replacing unrealistic expectations with humility, honesty, and growth."],
 ["Love That Tells the Truth","Combining compassion with healthy boundaries and responsible confrontation."],
 ["Reconciliation as Legacy","Giving future generations a healthier relational inheritance."]]},
{id:"d5", n:"Marriage and Family Leadership", c:[
 ["The Marriage Beneath the Legacy","Strengthening the relationship that often carries the family\u2019s long-term vision."],
 ["Leading the Family Together","Helping couples align around values, decisions, and generational influence."],
 ["A United Front","Addressing differences before they become divisions in family leadership."],
 ["Marriage, Money, and Mission","Aligning financial decisions with shared purpose and relational unity."],
 ["The Legacy of a Healthy Marriage","Showing future generations what commitment, grace, and covenant look like."],
 ["Preparing for the Empty Nest","Redefining marriage, purpose, and family influence in a new season."],
 ["Blended Family Legacy","Building trust, belonging, and shared identity across complex family systems."],
 ["Single-Parent Legacy","Building a strong spiritual and relational inheritance with courage and support."],
 ["The Family Leadership Team","Clarifying how parents, grandparents, and adult children can lead together."],
 ["Love That Outlives Us","Creating patterns of commitment future generations can carry forward."]]},
{id:"d6", n:"Parenting and Preparing the Next Generation", c:[
 ["Raising Legacy-Minded Children","Helping children understand identity, responsibility, gratitude, and contribution."],
 ["Preparing Them, Not Protecting Them","Developing resilience and wisdom rather than removing every difficulty."],
 ["Raising Faithful Stewards","Teaching children to manage time, talent, money, opportunity, and influence."],
 ["More Than an Inheritance","Preparing children to receive responsibility before receiving assets."],
 ["The Character Before the Capital","Building maturity before transferring significant wealth or leadership."],
 ["Launching with Purpose","Helping young adults develop calling, competence, and responsible independence."],
 ["Teaching Children to Give","Developing gratitude, compassion, and generosity from an early age."],
 ["Raising Contributors","Moving children from entitlement toward responsibility and service."],
 ["The Questions Every Parent Must Ask","Evaluating what children are learning from the family\u2019s daily example."],
 ["Passing the Baton Well","Preparing the next generation to carry family values without controlling them."]]},
{id:"d7", n:"Wisdom, Mentoring, and Life Experience", c:[
 ["What I Wish I Had Known","Turning life lessons into practical wisdom for the next generation."],
 ["Lessons from the Journey","Capturing the insights gained through work, family, faith, and adversity."],
 ["The Wisdom Transfer","Creating intentional conversations between generations."],
 ["Mentoring Your Own Family","Becoming a trusted guide without becoming controlling or intrusive."],
 ["The Stories Behind the Lessons","Using personal experience to make family wisdom memorable."],
 ["Questions Worth Asking","Creating deeper conversations about purpose, relationships, money, and faith."],
 ["The Family Council of Wisdom","Giving mature voices a constructive role in family decision-making."],
 ["Learning from Failure","Transferring honest lessons without hiding mistakes or creating shame."],
 ["The Advice I Want to Leave You","Creating a personal wisdom letter for children and grandchildren."],
 ["A Lifetime of Lessons","Building a permanent archive of family insight, conviction, and guidance."]]},
{id:"d8", n:"Wealth, Stewardship, and Responsibility", c:[
 ["Wealth with Purpose","Aligning financial resources with family values and meaningful impact."],
 ["God Owns It All","Building a family philosophy of ownership, stewardship, and accountability."],
 ["The Stewardship of Affluence","Understanding the opportunities and dangers that accompany financial abundance."],
 ["Money Without Entitlement","Preparing heirs to receive wealth with humility and responsibility."],
 ["The Family Wealth Conversation","Creating honest, age-appropriate dialogue about money and inheritance."],
 ["Beyond the Financial Plan","Connecting wealth transfer with faith, character, relationships, and purpose."],
 ["Preparing Responsible Heirs","Developing financial competence, emotional maturity, and shared responsibility."],
 ["Assets, Values, and Intentions","Ensuring financial documents reflect the deeper purpose behind the plan."],
 ["The Stewardship of Opportunity","Helping family members use education, access, relationships, and influence wisely."],
 ["Enough Is a Decision","Defining contentment, lifestyle, generosity, and the purpose of excess."]]},
{id:"d9", n:"Generosity and Family Impact", c:[
 ["The Generous Family","Creating shared practices of giving, serving, and compassion."],
 ["Giving Together","Using family generosity to deepen relationships and shared purpose."],
 ["The Family Generosity Plan","Developing a practical strategy for annual and long-term giving."],
 ["From Success to Significance","Redirecting achievement and abundance toward meaningful contribution."],
 ["A Legacy of Open Hands","Teaching future generations that generosity is a way of life."],
 ["The Family Giving Fund","Engaging children and grandchildren in thoughtful grant-making decisions."],
 ["Generosity Conversations","Helping family members discern where, why, and how they should give."],
 ["Serving Side by Side","Building unity through shared ministry and community service."],
 ["Impact Beyond Our Family","Using resources and influence to strengthen churches, communities, and causes."],
 ["The Gift That Keeps Giving","Designing generosity practices that can continue across generations."]]},
{id:"d10", n:"Succession, Governance, and Enduring Legacy", c:[
 ["The Succession Conversation","Preparing for the transfer of leadership, responsibility, ownership, and influence."],
 ["When the Founder Steps Back","Navigating identity, authority, and transition without destabilizing the family."],
 ["The Family Meeting","Building a healthy rhythm for communication, learning, and shared decisions."],
 ["The Family Council","Creating appropriate structures for multigenerational leadership and collaboration."],
 ["Estate Planning with Purpose","Connecting legal documents to values, relationships, and long-term intentions."],
 ["The Ethical Will","Passing on beliefs, blessings, stories, wisdom, and hopes \u2014 not only property."],
 ["The Next Generation at the Table","Preparing younger family members to participate in meaningful decisions."],
 ["Finishing Well Together","Planning for aging, caregiving, transition, and the final chapters of life."],
 ["The Legacy Master Plan","Integrating faith, family, wealth, generosity, governance, and succession."],
 ["What Will Live On?","Creating a legacy that continues to shape people long after we are gone."]]}
];

/* ---------- the recommended flagship collection ---------- */
FLI.flags = [
 {id:"faith-worth-passing-on", n:"Faith Worth Passing On", sub:"Building a Spiritual Inheritance That Can Outlast Financial Wealth", dom:2, hue:["#1E5C44","#0C2A1E"], areas:["personal","family"], built:true},
 {id:"what-matters-most", n:"What Matters Most", sub:"Clarifying the Values, Convictions, and Priorities That Define Your Family", dom:3, hue:["#B08A3E","#6E541F"], areas:["personal","family"]},
 {id:"the-story-we-carry", n:"The Story We Carry", sub:"Preserving the People, Experiences, and Lessons That Shaped Your Family", dom:1, hue:["#8E3A2C","#5A2318"], areas:["family"]},
 {id:"more-than-an-inheritance", n:"More Than an Inheritance", sub:"Preparing the Next Generation for Responsibility, Stewardship, and Purpose", dom:6, hue:["#3E6B8C","#1F3A50"], areas:["family","financial"]},
 {id:"the-generous-family", n:"The Generous Family", sub:"Creating a Multigenerational Culture of Giving, Serving, and Kingdom Impact", dom:9, hue:["#C58166","#7E4A36"], areas:["charitable","family"]},
 {id:"the-wisdom-transfer", n:"The Wisdom Transfer", sub:"Turning a Lifetime of Experience into Guidance for Future Generations", dom:7, hue:["#4E5D2E","#2B3418"], areas:["personal","family"]},
 {id:"wealth-with-purpose", n:"Wealth with Purpose", sub:"Aligning Family Resources with Faith, Values, Relationships, and Impact", dom:8, hue:["#2E8B6A","#154334"], areas:["financial","charitable"]},
 {id:"the-conversations-we-avoid", n:"The Conversations We Avoid", sub:"Addressing Money, Conflict, Succession, Aging, and Legacy Before a Crisis", dom:4, hue:["#7A4E68","#46293C"], areas:["family"]},
 {id:"the-legacy-we-choose", n:"The Legacy We Choose", sub:"Moving from an Accidental Inheritance to an Intentional Family Legacy", dom:3, hue:["#5A6B8C","#2F3A50"], areas:["personal","family"]},
 {id:"what-will-live-on", n:"What Will Live On?", sub:"Building a Legacy of Faith, Love, Wisdom, Generosity, and Service", dom:10, hue:["#8C6A3E","#4E3A1F"], areas:["personal","charitable"]}
];
FLI.flagIds = FLI.flags.map(function(f){return f.id;});

/* ---------- standard six-session campaign frame ---------- */
FLI.frame6 = [
 {t:"Remember Your Story", q:"What has shaped our family?", d:"Families identify defining people, experiences, blessings, struggles, and turning points."},
 {t:"Clarify What Matters", q:"What do we want our family to stand for?", d:"Families name shared beliefs, values, convictions, and priorities."},
 {t:"Strengthen the Relationships", q:"What must be healed, protected, or strengthened?", d:"Families address trust, communication, forgiveness, boundaries, and belonging."},
 {t:"Prepare the Generations", q:"What do our children and grandchildren need before receiving responsibility?", d:"Families explore character, competence, stewardship, work, and leadership development."},
 {t:"Align the Resources", q:"How should our time, wealth, influence, and opportunities serve our values?", d:"Families connect financial planning, generosity, succession, and impact."},
 {t:"Choose the Legacy", q:"What will we intentionally pass forward?", d:"Families develop a family legacy plan, commitment, and next-step calendar."}
];
FLI.pathway = ["Remember the story","Clarify the values","Strengthen the relationships","Prepare the generations","Align the resources","Multiply the impact","Pass the legacy forward"];

/* ---------- campaign resource suite ---------- */
FLI.suite = {
 family:["Family Legacy Assessment","Six-session participant guide","30- or 40-day reading journey","Family conversation cards","Couple discussion guide","Parent-child activities","Grandparent-grandchild guide","Family story workbook","Family values exercise","Family mission statement builder","Ethical will template","Legacy letter template","Family meeting agenda","Family generosity plan","Annual legacy review"],
 leader:["Facilitator guide","Small group leader guide","Pastor teaching guide","Advisor conversation guide","Estate-planning attorney guide","Family coach guide","Family office implementation guide","Pre-campaign assessment","Post-campaign evaluation","Referral and escalation guidelines"],
 media:["Six teaching videos","Family testimony films","Pastor sermon series","Podcast conversations","Short-form social videos","Children\u2019s teaching videos","Student edition","Audio edition","Presentation slides","Promotional trailer"]
};

/* ---------- product positioning ---------- */
FLI.brands = [
 {t:"Family Legacy Campaigns\u2122", tag:"Guided multigenerational journeys that help families preserve faith, strengthen relationships, transfer wisdom, prepare heirs, and multiply impact."},
 {t:"Family Legacy Campaign Builder\u2122", tag:"Turn a family\u2019s story, values, faith, wisdom, wealth, and generosity into a personalized legacy journey."},
 {t:"Family Legacy Campaign Library\u2122", tag:"A complete collection of biblical, relational, financial, and multigenerational experiences for every family season."},
 {t:"Family Legacy Intelligence\u2122", tag:"Discover what your family has received, what it must strengthen, and what it is called to pass forward."}
];

/* ---------- the 10-minute assessment ---------- */
FLI.assess = {
 scale:["Not true of our family","Rarely true","Somewhat true","Mostly true","Clearly and consistently true"],
 note:"Answer honestly based on what is happening now \u2014 not what you hope will happen someday.",
 sections:[
  {n:"Faith and Spiritual Heritage", q:"What have we received spiritually, and what are we intentionally passing forward?", items:[
   "Our children and grandchildren understand the faith convictions that guide our family.",
   "We regularly tell stories about God\u2019s faithfulness throughout our family\u2019s history.",
   "Prayer, Scripture, worship, and spiritual conversations are natural parts of our family life.",
   "We have intentionally discussed what we hope future generations will believe about God."]},
  {n:"Family Story, Identity, and Values", q:"Does our family know who we are and what we stand for?", items:[
   "Our family knows the important people, sacrifices, challenges, and turning points that shaped us.",
   "We can clearly name the values we want our family to represent.",
   "Our financial and lifestyle decisions generally reflect those values.",
   "Our children and grandchildren experience a meaningful sense of family identity and belonging."]},
  {n:"Relationships and Family Unity", q:"Are our relationships strong enough to carry the legacy we hope to leave?", items:[
   "Family members can discuss difficult subjects without withdrawing, attacking, or dividing.",
   "We have addressed \u2014 or are actively addressing \u2014 significant hurts, conflicts, and misunderstandings.",
   "Family members feel heard, respected, loved, and valued across generations.",
   "Our family knows how to disagree while protecting relationships and honoring one another."]},
  {n:"Wisdom and Next-Generation Preparation", q:"Are we preparing our heirs for responsibility, not merely inheritance?", items:[
   "We intentionally share the lessons we have learned through faith, work, success, failure, and adversity.",
   "Our children and grandchildren are developing the character and competence needed to steward responsibility.",
   "We have meaningful conversations about work, calling, money, generosity, leadership, and purpose.",
   "Younger family members are gradually being invited into age-appropriate family decisions and responsibilities."]},
  {n:"Stewardship, Wealth, and Generosity", q:"Do our resources serve our faith, values, family, and Kingdom purpose?", items:[
   "Our family has a shared understanding that everything ultimately belongs to God.",
   "We have explained the purpose behind our wealth, property, business interests, opportunities, and influence.",
   "Our children and grandchildren are being prepared to receive resources without developing entitlement.",
   "Giving, serving, and generosity are shared family practices rather than private financial transactions."]},
  {n:"Succession, Communication, and Enduring Legacy", q:"Have we prepared the people as carefully as we have prepared the documents?", items:[
   "Our estate, succession, business, and charitable plans reflect our deeper values and intentions.",
   "Appropriate family members understand the general direction of our plans and the reasons behind them.",
   "We have identified the stories, beliefs, blessings, wisdom, and instructions we want preserved.",
   "We have a practical process for continuing legacy conversations across generations."]}],
 bands:[
  {min:96, t:"Intentional Legacy Formation", d:"Your family has established many strong legacy practices. Your next opportunity is to document, deepen, and multiply them."},
  {min:72, t:"Emerging Legacy Alignment", d:"Important pieces are present, but greater clarity, communication, and intentionality are needed."},
  {min:48, t:"Legacy Conversations Needed", d:"Your family has valuable stories, faith, wisdom, and resources, but much of the legacy remains undocumented or undiscussed."},
  {min:24, t:"Begin with Trust and Discovery", d:"Start slowly. Prioritize relationships, listening, family stories, and shared values before addressing complex financial or succession decisions."}],
 discern:[
  "Where would growth create the greatest positive impact?",
  "Which issue becomes more difficult if we continue postponing it?",
  "Where do we currently sense God inviting us to act?"],
 fills:["The area we most need to explore is:","The first conversation we are willing to have is:","The person who should help initiate it is:"],
 rec:[
  {id:"faith-worth-passing-on", alt:null},
  {id:"the-story-we-carry", alt:"what-matters-most"},
  {id:"the-conversations-we-avoid", alt:null},
  {id:"more-than-an-inheritance", alt:"the-wisdom-transfer"},
  {id:"wealth-with-purpose", alt:"the-generous-family"},
  {id:"what-will-live-on", alt:"the-legacy-we-choose"}]
};

/* ---------- the four interviews ---------- */
FLI.iv = {
 listen:["Stories","Scripture","Convictions","Family language","Defining moments","Wounds and turning points","Lessons learned","Hopes and fears","Blessings","Unfinished conversations"],
 permission:"Would you be comfortable if I recorded our conversation? The recording will allow us to preserve your words, stories, and convictions accurately. With your permission, the material can then be used to create private, personalized devotionals and family legacy experiences for you, your children, and your grandchildren.",
 capture:["Five defining family stories","Five core family values","Three significant faith experiences","Three major lessons from hardship","Three lessons about marriage and relationships","Three lessons about work and calling","Three lessons about money and stewardship","Three hopes for the next generation","Three concerns for the next generation","One family legacy statement","One guiding Scripture or biblical theme","One immediate family conversation or action step"],
 couple:{
  intro:"The advisor should conduct this conversation with both spouses or founding family leaders present whenever possible. The conversation should be recorded \u2014 with permission \u2014 and transcribed. The transcript becomes the primary source material for the Family Legacy Campaign or Journey Builder. The advisor is not merely collecting facts.",
  qs:[
   ["When you look back over your marriage and family life, where do you most clearly see the faithfulness of God?","Listen for spiritual turning points, answered prayer, provision, protection, redirection, healing, and unexpected grace."],
   ["What people, experiences, hardships, and opportunities most shaped the family you have become?","Explore parents, grandparents, mentors, churches, businesses, financial seasons, losses, failures, and major decisions."],
   ["What three to five values do you most want your family name to represent?","Ask them to describe what each value looks like in actual behavior, not merely as an attractive word."],
   ["What have you learned about marriage, love, forgiveness, commitment, and staying united?","Invite honest lessons about both strength and struggle."],
   ["What have you learned about work, success, money, wealth, responsibility, and contentment?","Ask how their understanding has changed over time."],
   ["What do you hope your children and grandchildren will understand about why God has entrusted resources and influence to your family?","Listen for their theology of stewardship, opportunity, ownership, generosity, responsibility, and purpose."],
   ["What concerns do you have about the impact that success, wealth, comfort, or inheritance could have on future generations?","Explore entitlement, dependency, conflict, loss of motivation, spiritual drift, secrecy, and family fragmentation."],
   ["What wisdom do you wish you had received when you were younger \u2014 and what wisdom do you now feel responsible to pass forward?","Ask for advice related to faith, marriage, parenting, vocation, money, leadership, adversity, and finishing well."],
   ["What conversations have you delayed because they feel difficult, emotional, complicated, or potentially divisive?","Do not force resolution. Identify the conversations that may require facilitation, pastoral care, legal counsel, or family coaching."],
   ["When your children and grandchildren describe your legacy decades from now, what do you hope they will say you gave them?","Encourage them to think beyond assets and name the faith, love, memories, wisdom, opportunities, blessings, and examples they hope will live on."]]},
 patriarch:{
  intro:"A private conversation about faith, responsibility, wisdom, and blessing. These questions are not intended to reinforce stereotypes about men or family leadership. They create space for the patriarch, father, grandfather, founder, or senior male family leader to reflect personally on what he has carried, learned, regretted, and hopes to pass forward.",
  qs:[
   ["What did you learn from your father, grandfather, or the men who shaped you?","What did you receive from them that you want to preserve? What do you want to do differently?"],
   ["When have you felt the greatest weight of responsibility for your family?","Describe a season when leadership, provision, protection, faith, or decision-making felt especially costly."],
   ["What experiences most shaped your understanding of manhood, leadership, and faithfulness?","Who modeled these qualities well? Which experiences corrected or refined your understanding?"],
   ["What have success and failure taught you about your true identity?","How have achievement, disappointment, recognition, loss, or regret affected your relationship with God and your family?"],
   ["What sacrifices have you made that your family may not fully know or understand?","Share these without seeking recognition or creating obligation. What motivated those sacrifices?"],
   ["What mistakes do you hope the next generation will learn from without having to repeat?","What would you tell your younger self about faith, marriage, parenting, work, money, or priorities?"],
   ["What do you most want your sons, daughters, and grandchildren to understand about work and responsibility?","What does meaningful work look like? How should they think about ambition, excellence, rest, provision, and service?"],
   ["What does it mean to you to bless your children and grandchildren?","What words of affirmation, identity, permission, challenge, prayer, or encouragement do you want each person to receive?"],
   ["Is there anything you still need to say, repair, confess, forgive, or make clear?","This may include a relationship, decision, misunderstanding, expectation, or family transition."],
   ["What do you want to place into the hands of the next generation before your life is complete?","Consider faith, wisdom, responsibility, opportunity, relationships, leadership, generosity, and blessing \u2014 not only financial assets."]],
  fills:["The most important thing I want my family to know is:","The blessing I want to speak over the next generation is:","The responsibility I hope they will carry is:"]},
 matriarch:{
  intro:"A private conversation about faith, relationships, strength, wisdom, and family culture. These questions create space for the matriarch, mother, grandmother, founder, or senior female family leader to describe the relational, spiritual, cultural, and practical legacy she has carried and hopes to pass forward.",
  qs:[
   ["What did you learn from your mother, grandmother, or the women who shaped you?","What qualities, practices, stories, and convictions did they give you? What patterns did you choose to change?"],
   ["What experiences most shaped the woman, wife, mother, grandmother, or leader you became?","Consider joys, sacrifices, disappointments, transitions, mentors, losses, and encounters with God."],
   ["What have you done to create belonging, connection, and emotional safety within the family?","Which traditions, conversations, celebrations, meals, prayers, or acts of care have mattered most?"],
   ["What strengths have helped you carry the family through difficult seasons?","How did faith, courage, perseverance, discernment, hospitality, forgiveness, or advocacy shape those seasons?"],
   ["What sacrifices or unseen contributions might your family not fully recognize?","What would you want them to understand about the heart behind those choices?"],
   ["What have marriage and family relationships taught you about love, grace, boundaries, and forgiveness?","What do you hope future generations practice differently because of what you learned?"],
   ["What do you most want your daughters, sons, and grandchildren to understand about identity and worth?","How can they resist defining themselves only through achievement, appearance, wealth, approval, or family expectations?"],
   ["What family stories, traditions, recipes, practices, prayers, or celebrations should never be lost?","Why do they matter, and what do they reveal about the family\u2019s values?"],
   ["Is there a relationship, hurt, misunderstanding, or unspoken hope that you would like to see addressed?","What would healing, clarity, or reconciliation look like?"],
   ["What qualities do you pray will characterize your family for generations?","Consider faith, kindness, courage, hospitality, unity, generosity, resilience, service, and love."]],
  fills:["The heart of our family that I most want preserved is:","The wisdom I most want to pass forward is:","My prayer for future generations is:"]},
 nextgen:{
  intro:"Ten questions children and grandchildren can ask parents and grandparents. These questions give the next generation a meaningful role. They are not passive recipients of wealth or family history. They become listeners, storytellers, learners, and future stewards. The conversation may be recorded \u2014 with permission \u2014 and preserved in the family archive.",
  qs:[
   ["What was life like in your family when you were growing up?","What were your home, church, school, community, celebrations, responsibilities, and relationships like?"],
   ["Who influenced your faith most deeply, and what did that person give you?","Ask for a story that demonstrates the influence."],
   ["What were some of the hardest seasons of your life, and how did those experiences change you?","What helped you persevere? Where did you see God?"],
   ["What decisions most changed the direction of your life, marriage, family, career, or faith?","Looking back, how did you make those decisions?"],
   ["What are you most grateful for when you think about our family?","Which people, memories, opportunities, traditions, or examples mean the most?"],
   ["What mistakes or regrets have taught you the most?","What would you want our generation to learn from them?"],
   ["How did you learn to think about work, money, saving, investing, giving, and contentment?","How has your perspective changed as you have grown older?"],
   ["What do you believe God has uniquely entrusted to our family?","This could include relationships, faith, influence, knowledge, a business, resources, a place, a story, or an opportunity to serve."],
   ["What do you hope our generation preserves \u2014 and what do you hope we have the courage to change?","Invite both affirmation and freedom. Legacy should guide the next generation without controlling it."],
   ["What blessing, prayer, or message would you like to speak personally over me and my generation?","Record the response in the family member\u2019s own voice whenever possible."]],
  fills:["The story I most want to remember is:","The value I want to carry forward is:","The question I still want to ask is:","The responsibility I am willing to accept is:"]}
};

/* ---------- the journey builder ---------- */
FLI.builder = [
 {k:"The Couple\u2019s Marriage Journey", t:"The Story God Has Written Through Us", d:"A private devotional journey for the matriarch and patriarch.", inc:["Their courtship and marriage story","Defining decisions","Seasons of sacrifice","Lessons from conflict","Moments of God\u2019s faithfulness","Shared values","Unfinished conversations","Prayers for their remaining years","Their vision for finishing well together"]},
 {k:"The Children\u2019s Legacy Journey", t:"What We Want You to Know", d:"A personalized devotional for adult children.", inc:["The family\u2019s spiritual story","Lessons about identity","Lessons about marriage","Lessons about work","Lessons about money","Family values","Stories of failure and resilience","The purpose behind the family\u2019s resources","Words of blessing","Invitations to responsibility"]},
 {k:"The Grandchildren\u2019s Legacy Journey", t:"The Story You Are Part Of", d:"An age-appropriate experience.", inc:["Family origin stories","Photographs and milestones","Stories of courage and faith","Simple family values","Grandparent prayers","Questions for conversation","Generosity activities","Service projects","A personal blessing for each grandchild","Space for the grandchild to add to the family story"]},
 {k:"The Whole-Family Legacy Campaign", t:"What Will Live On?", d:"A six-session family experience.", sessions:[
  ["Remember the Story","What has shaped our family?"],
  ["Recognize God\u2019s Faithfulness","Where has God led, provided, protected, and redeemed?"],
  ["Clarify What Matters Most","What values and convictions should define us?"],
  ["Strengthen the Relationships","What must be celebrated, protected, repaired, or discussed?"],
  ["Prepare the Generations","What wisdom, character, and responsibility must be developed?"],
  ["Choose What We Will Pass Forward","How will our faith, wisdom, generosity, influence, and resources serve future generations?"]]}
];

/* ---------- advisor implementation model ---------- */
FLI.model = {
 invite:"We have spent considerable time helping you prepare your assets for your family. We would also like to help prepare your family for the assets \u2014 and preserve the faith, values, wisdom, and stories that matter even more.",
 steps:[
  ["Invitation","Position it as a value-added family service, not a sales presentation."],
  ["Family Assessment","The couple completes the 10-minute Family Legacy Intelligence Assessment."],
  ["Recorded Couple Interview","The advisor facilitates the ten joint questions with the matriarch and patriarch."],
  ["Individual Interviews","The patriarch and matriarch complete their individual legacy interviews."],
  ["Next-Generation Conversation","Selected children or grandchildren ask the next-generation questions."],
  ["Intelligence Summary","The advisor prepares a private summary of strengths, priorities, risks, stories, values, needs, and implications."],
  ["Personalized Legacy Experience","The Journey Builder produces the first customized devotional, conversation guide, family meeting, or six-session campaign."],
  ["Professional Planning Alignment","With the family\u2019s permission, appropriate insights can inform the family\u2019s professional team."]],
 summary:["Family strengths","Unspoken priorities","Legacy risks","Important stories","Core values","Next-generation needs","Planning implications","Recommended first journey"],
 pros:["The financial advisor","Estate-planning attorney","CPA or tax advisor","Family business advisor","Generosity advisor","Family coach","Pastor or spiritual mentor","Trustee or family office"],
 confid:"The advisor should never treat private spiritual or relational disclosures as sales intelligence. The information must remain confidential, permission-based, securely stored, and used only for the family\u2019s stated legacy purposes.",
 delivery:{
  before:["Invites the couple or family","Administers the Family Legacy Intelligence Assessment","Conducts the recorded matriarch-and-patriarch interview","Identifies the family\u2019s strongest themes and most important gaps","Personalizes the 21-day experience with family stories, Scriptures, photographs, and quotations"],
  during:["Hosts the four sessions","Facilitates sensitive conversations","Provides reflective rather than prescriptive guidance","Invites appropriate legal, tax, generosity, ministry, or family specialists","Protects confidentiality and family ownership of the material"],
  after:["A Family Spiritual Legacy Statement","A family meeting rhythm","A next-generation preparation plan","A generosity experience","A legacy letter or ethical will","A personalized children\u2019s devotional","A personalized grandchildren\u2019s devotional","A couple\u2019s marriage and legacy journey","A planning follow-up with the family\u2019s professional team"]}
};

/* ---------- the central promise ---------- */
FLI.promise = {
 pairs:[["Faith","fortune"],["Wisdom","wealth"],["Character","capital"],["Responsibility","inheritance"],["Relationships","structures"],["Purpose","possessions"],["Generosity","accumulation"],["Blessing","transition"]],
 close:"The ultimate goal is not merely a successful estate transfer. It is a prepared family, a preserved story, a strengthened marriage, an equipped next generation, and a legacy that continues to bear fruit."
};

/* ════════════════════════════════════════════════════════════════
   FAITH WORTH PASSING ON · the fully written 21-day flagship
   ════════════════════════════════════════════════════════════════ */
var D = function(t,v,vl,body,q,pr,pray){ return {title:t, verse:v, verseLabel:vl, body:body, table:q, step:pr, pray:pray}; };
var FWPO_READS = {
 1: D("Every Family Leaves a Legacy","Tell it to your children, and let your children tell it to their children, and their children to the next generation.","Joel 1:3",
  ["A legacy is not limited to what is distributed after someone dies. Legacy is being formed every day through what a family talks about, celebrates, practices, tolerates, and prioritizes.",
   "Your family is already passing something forward.",
   "The first step is not to create a perfect family story. It is to recognize the story that is already being written and decide what should continue into the next generation."],
  "What do you believe your family is currently passing on \u2014 intentionally or unintentionally?",
  "Write down five things your family is already transferring to the next generation.",
  "God, help us recognize the legacy we are forming and give us wisdom to pass forward what honors You."),
 2: D("The People Who Shaped Your Faith","I am reminded of your sincere faith, which first lived in your grandmother Lois and in your mother Eunice.","2 Timothy 1:5",
  ["Faith often reaches us through people before it becomes deeply personal.",
   "A parent may have prayed for us. A grandparent may have modeled generosity. A pastor, teacher, coach, neighbor, or friend may have helped us understand the character of God.",
   "Recognizing these people reminds us that spiritual influence is rarely wasted. The faithfulness of one generation can shape people they may never live long enough to meet."],
  "Who most influenced your faith, and what did that person give you?",
  "Write a short note of gratitude to someone who shaped your faith. If that person is no longer living, write the note as part of your family archive.",
  "Thank You, God, for the people who faithfully helped us know and trust You."),
 3: D("The Stories We Must Not Lose","We will tell the next generation the praiseworthy deeds of the Lord, his power, and the wonders he has done.","Psalm 78:4",
  ["Families easily preserve photographs, legal records, and financial documents while losing their most important spiritual stories.",
   "Future generations need to know more than where the family lived or what the family owned. They need to know when God provided, redirected, protected, healed, or sustained the family.",
   "A spiritual story tells the next generation, \u201CThe God who met us can also meet you.\u201D"],
  "What story of God\u2019s faithfulness should every member of your family know?",
  "Record or write one story of God\u2019s faithfulness in your family.",
  "Lord, help us remember and preserve the stories that reveal Your faithfulness."),
 4: D("Faith Through Hard Seasons","We also glory in our sufferings, because we know that suffering produces perseverance; perseverance, character; and character, hope.","Romans 5:3\u20134",
  ["Some of the most important parts of a family\u2019s spiritual legacy come through difficulty.",
   "Loss, disappointment, illness, financial pressure, failure, conflict, and uncertainty can deepen faith or expose where faith needs to grow.",
   "The next generation does not need a polished version of the family story. It needs an honest account of how God remained present in imperfect circumstances."],
  "What hardship most shaped your faith, character, or family?",
  "Complete this sentence: \u201COne difficult season that taught our family to trust God was\u2026\u201D",
  "God, redeem the difficult parts of our story and use them to give hope to future generations."),
 5: D("The Faith of Your Fathers and Mothers","Stand at the crossroads and look; ask for the ancient paths, ask where the good way is, and walk in it.","Jeremiah 6:16",
  ["Every family inherits strengths and weaknesses.",
   "Some spiritual practices should be preserved. Other patterns may need to be changed. Honoring previous generations does not mean pretending they were perfect. It means receiving what was good, learning from what was painful, and choosing a more faithful path forward.",
   "Legacy requires both gratitude and courage."],
  "What spiritual strength did you receive from previous generations? What unhealthy pattern should end with your generation?",
  "Create two columns: what we want to preserve, and what we want to change.",
  "Give us gratitude for what was faithful and courage to change what should not continue."),
 6: D("The Convictions That Guide Us","As for me and my household, we will serve the Lord.","Joshua 24:15",
  ["A family\u2019s convictions become a compass when decisions become difficult.",
   "Convictions are deeper than preferences. They clarify who the family wants to be, how it will respond under pressure, and what it will prioritize when competing values collide.",
   "Children and grandchildren cannot carry convictions they have never heard explained."],
  "What are the three spiritual convictions you most want your family to understand?",
  "Write three statements beginning with: \u201CIn our family, we believe\u2026\u201D",
  "Lord, help our family live from clear biblical convictions rather than changing cultural pressure."),
 7: D("Remembering God\u2019s Faithfulness","Praise the Lord, my soul, and forget not all his benefits.","Psalm 103:2",
  ["Remembering is a spiritual discipline.",
   "When families remember together, gratitude grows, faith is strengthened, and current challenges are placed within the larger story of God\u2019s faithfulness.",
   "Before deciding what you want to pass forward, pause to recognize what God has already given you."],
  "Where have you most clearly seen God\u2019s provision, protection, guidance, or grace?",
  "Create a family faithfulness timeline with at least seven significant moments.",
  "God, keep us from forgetting Your goodness and help us tell the next generation what You have done."),
 8: D("Faith Is More Caught Than Taught","Follow my example, as I follow the example of Christ.","1 Corinthians 11:1",
  ["The next generation will remember more than the lessons we taught. They will remember the life they observed.",
   "They notice how we respond to pressure, treat people, use money, handle disappointment, apologize, forgive, pray, work, rest, and make decisions.",
   "A spiritual legacy becomes credible when our practices support our words."],
  "What is the next generation learning about faith by watching how you live?",
  "Identify one area where your example needs to become more consistent with your beliefs.",
  "Jesus, make our daily lives a faithful example worth following."),
 9: D("Creating a Home Where Faith Can Be Discussed","Talk about them when you sit at home and when you walk along the road.","Deuteronomy 6:7",
  ["Spiritual formation does not require every family conversation to become a formal Bible study.",
   "Faith is passed through ordinary moments: meals, travel, celebrations, disappointment, financial decisions, caregiving, work, and family transitions.",
   "The goal is not to force spiritual conversation. It is to make it normal."],
  "How natural is it for members of your family to talk about God, faith, doubt, prayer, and spiritual decisions?",
  "Ask one family member: \u201CWhere have you seen God at work in your life recently?\u201D",
  "God, make spiritual conversation natural, honest, and life-giving in our family."),
 10: D("The Legacy of a Healthy Marriage","Be completely humble and gentle; be patient, bearing with one another in love.","Ephesians 4:2",
  ["For married parents and grandparents, the quality of the marriage becomes part of the family\u2019s inheritance.",
   "A healthy marriage does not require the absence of disagreement. It demonstrates commitment, humility, affection, forgiveness, truth, and grace through changing seasons.",
   "One of the greatest gifts a couple can offer future generations is an honest example of love that continued to grow."],
  "What has your marriage taught your children and grandchildren about love and commitment?",
  "Couples complete this statement together: \u201COne lesson our marriage has taught us that we want to pass forward is\u2026\u201D",
  "Strengthen our marriage and use it to model faithful, enduring love."),
 11: D("Grace for Imperfect Families","Bear with each other and forgive one another\u2026 Forgive as the Lord forgave you.","Colossians 3:13",
  ["Every family contains disappointment, misunderstanding, weakness, and unresolved pain.",
   "A family legacy does not become strong by hiding imperfection. It becomes strong when people learn to acknowledge failure, extend grace, speak truth, establish healthy boundaries, and seek reconciliation.",
   "Sometimes the most important inheritance a generation can leave is a healthier way of handling conflict."],
  "What relationship needs greater grace, truth, forgiveness, or healing?",
  "Identify one safe and appropriate step toward relational healing.",
  "God, give us humility to admit our failures and courage to pursue peace."),
 12: D("Work as Calling and Stewardship","Whatever you do, work at it with all your heart, as working for the Lord.","Colossians 3:23",
  ["Families pass down powerful messages about work.",
   "Work may be treated as an identity, a burden, a pathway to status, a means of provision, or an opportunity to serve God and others.",
   "A healthy legacy teaches the next generation to pursue excellence without worshiping achievement and to see vocation as an arena of stewardship."],
  "What do you want future generations to believe about work, success, ambition, and calling?",
  "Write a one-paragraph family philosophy of work.",
  "Teach us to work faithfully, rest wisely, and use our abilities to serve others."),
 13: D("Money Reveals What We Trust","For where your treasure is, there your heart will be also.","Matthew 6:21",
  ["Money is never merely financial.",
   "It reveals fears, desires, priorities, loyalties, and expectations. The next generation learns about money not only through instruction but through what a family worries about, celebrates, accumulates, withholds, and gives.",
   "Financial wealth becomes a blessing when it is governed by wisdom, contentment, responsibility, and trust in God."],
  "What has your family\u2019s use of money taught the next generation about security and trust?",
  "Discuss one financial decision that reflects \u2014 or should better reflect \u2014 your family\u2019s faith.",
  "God, help us use money as faithful stewards rather than allowing money to master us."),
 14: D("The Generous Family","Command them to do good, to be rich in good deeds, and to be generous and willing to share.","1 Timothy 6:18",
  ["Generosity is more likely to continue when the next generation participates in it.",
   "Private giving can accomplish good, but shared generosity also forms the family. It teaches gratitude, compassion, responsibility, and the joy of contributing to something beyond oneself.",
   "Generosity is not simply a financial transaction. It is a family practice."],
  "How are children and grandchildren currently participating in your family\u2019s generosity?",
  "Choose one giving or service opportunity your family can participate in together.",
  "Make our family rich in good deeds, generous in spirit, and willing to share."),
 15: D("Preparing the People, Not Only the Plan","From everyone who has been given much, much will be demanded.","Luke 12:48",
  ["Families often spend years preparing financial documents while spending very little time preparing the people who will eventually carry responsibility.",
   "The purpose of next-generation preparation is not to control children or grandchildren. It is to help them develop character, competence, wisdom, humility, and a sense of calling.",
   "The central question is not only, \u201CWhat will they receive?\u201D It is also, \u201CWho are they becoming?\u201D"],
  "How prepared is the next generation to carry responsibility, opportunity, leadership, and wealth?",
  "Identify one area of character and one area of competence that should be strengthened.",
  "God, prepare the hearts and hands of those who will carry responsibility after us."),
 16: D("The Wisdom Transfer","Teach us to number our days, that we may gain a heart of wisdom.","Psalm 90:12",
  ["Experience does not automatically become legacy.",
   "Wisdom must be reflected upon, expressed, recorded, and shared. Lessons hidden in one generation may need to be learned again through painful experience in the next.",
   "Your family does not need only your conclusions. It also needs the stories behind them."],
  "What do you know now that you wish you had understood at age 20, 30, or 40?",
  "Write down three lessons you want the next generation to receive.",
  "Help us turn a lifetime of experience into wisdom that serves others."),
 17: D("Speaking Blessing","The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you.","Numbers 6:24\u201325",
  ["Many people know what their parents expected from them but are unsure what their parents saw in them.",
   "A blessing communicates identity, love, affirmation, prayer, and hope. It does not deny areas of growth. It reminds a person that they are more than their achievements, mistakes, or financial role in the family.",
   "A spoken or written blessing can become one of the most treasured parts of a legacy."],
  "What does each child or grandchild need to hear from you?",
  "Begin writing a personal blessing for one family member.",
  "Give us words that affirm identity, communicate love, and call forth faithful purpose."),
 18: D("The Conversations We Avoid","Speaking the truth in love, we will grow to become\u2026 mature.","Ephesians 4:15",
  ["Silence does not protect a family from difficult issues. It frequently leaves the next generation unprepared.",
   "Families may postpone conversations about faith, money, inheritance, aging, caregiving, business succession, conflict, addiction, or unmet expectations.",
   "Wisdom includes knowing when a conversation is necessary, how much should be shared, and who can help facilitate it."],
  "What important family conversation have you been postponing?",
  "Write down the conversation, the people who should participate, and a healthy first step.",
  "Give us courage, humility, wisdom, and love for the conversations we need to have."),
 19: D("Wealth with Purpose","Remember the Lord your God, for it is he who gives you the ability to produce wealth.","Deuteronomy 8:18",
  ["Wealth can expand a family\u2019s opportunity to provide, invest, create, employ, give, and serve. It can also increase entitlement, conflict, dependency, fear, and spiritual drift.",
   "The difference is often purpose.",
   "Future generations need to understand not only what the family owns, but why the resources exist and what responsibilities accompany them."],
  "What do you believe is the God-given purpose of your family\u2019s resources and influence?",
  "Complete this statement: \u201CWe believe God has entrusted resources to our family so that we can\u2026\u201D",
  "God, help us understand the purpose behind what You have entrusted to us."),
 20: D("Write What Matters Most","Write down the revelation and make it plain.","Habakkuk 2:2",
  ["Spoken memories fade. Written convictions can travel across generations.",
   "A family legacy letter, ethical will, recorded interview, or devotional can preserve what legal documents cannot: faith, affection, stories, blessings, lessons, hopes, and spiritual direction.",
   "You do not need to say everything. Begin with what matters most."],
  "What would you most regret leaving unsaid?",
  "Write the opening paragraph of a legacy letter to your family. Begin with: \u201CMore than anything else, we want you to know\u2026\u201D",
  "Give us clarity and courage to preserve the words our family most needs to receive."),
 21: D("Faith Worth Passing On","One generation commends your works to another; they tell of your mighty acts.","Psalm 145:4",
  ["A spiritual legacy is not created through one conversation, document, or devotional.",
   "It is built through a lifetime of faithful practices and strengthened through intentional moments of remembrance, conversation, blessing, preparation, and generosity.",
   "The goal is not to create a family that depends on the previous generation forever. The goal is to help each generation know God personally, live faithfully, and take responsibility for passing faith forward.",
   "Your family\u2019s legacy remains unfinished. The next generation is not merely receiving the story. It is being invited to continue it."],
  "What do you now feel called to pass forward more intentionally?",
  "Choose the first three actions for your Family Spiritual Legacy Plan.",
  "God, help us pass forward a faith that is sincere, lived, tested, generous, and deeply rooted in You.")
};

var FWPO = {
 id:"faith-worth-passing-on", docFlagship:true, built:true,
 title:"Faith Worth Passing On",
 sub:"Building a Spiritual Inheritance That Can Outlast Financial Wealth",
 kicker:"A 21-Day Family Legacy Journey",
 quote:"The question is not whether your family will leave a legacy. The question is what kind of legacy you will intentionally pass forward.",
 desc:"Every family transfers something. Some families transfer financial assets, property, businesses, opportunities, or influence. Every family also transfers beliefs, habits, stories, wounds, values, expectations, and ways of relating to God and one another. Faith Worth Passing On is a 21-day guided experience designed to help parents, grandparents, children, and grandchildren identify the spiritual inheritance they have received, strengthen what matters most, and intentionally pass faith to the next generation.",
 big:"This journey helps families move beyond estate planning to legacy formation.",
 scrRef:"Psalm 145:4", kjv:false,
 scrKJV:"One generation commends your works to another; they tell of your mighty acts.",
 areas:["personal","family"], hue:["#1E5C44","#0C2A1E"],
 audience:"Individuals, couples, adult children, grandchildren, family meetings, small groups of families \u2014 with or without a Christian financial advisor",
 season:"Any season \u2014 and as part of an estate, generosity, or succession-planning process",
 days:21, open:21,
 elements:[
  ["Scripture","A biblical foundation for the day"],
  ["Devotional Thought","A short reflection"],
  ["Legacy Question","A question for personal or family conversation"],
  ["Legacy Practice","A simple action step"],
  ["Prayer","A brief prayer of response"]],
 labels:{table:"The Legacy Question", step:"The Legacy Practice", pray:"Prayer"},
 slabels:{qs:"Discussion Questions", step:"Between-Session Practice", open:"Opening Question"},
 rhythm:"Session 1 before Days 1\u20137 \u00B7 Session 2 after Days 1\u20137 \u00B7 Session 3 after Days 8\u201314 \u00B7 Session 4 after Days 15\u201321 \u00B7 Each session runs approximately 75\u201390 minutes.",
 uses:["A single family","Several couples","A family legacy group","A Christian advisor and selected client families","A church-based family legacy ministry","A group of parents and grandparents"],
 weeks:[
  {t:"Remember the Faith You Received", d:"Recognize the people, stories, experiences, and encounters with God that shaped your spiritual life.", days:[
   ["Every Family Leaves a Legacy","Joel 1:3",""],["The People Who Shaped Your Faith","2 Timothy 1:5",""],["The Stories We Must Not Lose","Psalm 78:4",""],["Faith Through Hard Seasons","Romans 5:3\u20134",""],["The Faith of Your Fathers and Mothers","Jeremiah 6:16",""],["The Convictions That Guide Us","Joshua 24:15",""],["Remembering God\u2019s Faithfulness","Psalm 103:2",""]]},
  {t:"Practice the Faith You Want to Pass On", d:"Examine how faith is being demonstrated through everyday relationships, decisions, stewardship, generosity, and family life.", days:[
   ["Faith Is More Caught Than Taught","1 Corinthians 11:1",""],["Creating a Home Where Faith Can Be Discussed","Deuteronomy 6:7",""],["The Legacy of a Healthy Marriage","Ephesians 4:2",""],["Grace for Imperfect Families","Colossians 3:13",""],["Work as Calling and Stewardship","Colossians 3:23",""],["Money Reveals What We Trust","Matthew 6:21",""],["The Generous Family","1 Timothy 6:18",""]]},
  {t:"Intentionally Pass Faith Forward", d:"Capture your family\u2019s wisdom, speak blessing, prepare the next generation, and create a practical spiritual legacy plan.", days:[
   ["Preparing the People, Not Only the Plan","Luke 12:48",""],["The Wisdom Transfer","Psalm 90:12",""],["Speaking Blessing","Numbers 6:24\u201325",""],["The Conversations We Avoid","Ephesians 4:15",""],["Wealth with Purpose","Deuteronomy 8:18",""],["Write What Matters Most","Habakkuk 2:2",""],["Faith Worth Passing On","Psalm 145:4",""]]}],
 sessions:[
  {t:"The Faith We Received", scr:"2 Timothy 1:5",
   sq:"Before we can intentionally pass faith forward, we must recognize the people, stories, and experiences through which faith reached us.",
   outcomes:["Identify the people who shaped their faith","Recognize defining spiritual moments","Name strengths and gaps in their family\u2019s spiritual inheritance","Begin preserving a family faith story"],
   opening:"Who is one person whose faith influenced your life, and what did you observe in that person?",
   moves:[
    {t:"Faith Travels Through People", p:"God frequently uses ordinary people to influence future generations. Faith is passed through:", list:["Example","Prayer","Scripture","Encouragement","Correction","Hospitality","Generosity","Perseverance","Stories of God\u2019s faithfulness"]},
    {t:"Every Family Has a Spiritual Story", p:"A family\u2019s spiritual story may include both faithfulness and failure. Healthy legacy formation asks:", list:["What did we receive?","What should we preserve?","What should we strengthen?","What should end with us?","What new pattern should begin with us?"]},
    {t:"Remembering Strengthens Faith", p:"When families remember God\u2019s faithfulness, they build confidence for the future. The goal is not to glorify the family. It is to recognize the grace of God throughout the family\u2019s story."}],
   qs:["Who most shaped your understanding of God?","What spiritual strength did you inherit?","What family faith story should never be lost?","What pattern do you hope will change with your generation?","Where have you most clearly seen God\u2019s faithfulness?"],
   exercise:{t:"The Faith Timeline", p:"Create a simple timeline including:", list:["Significant births and marriages","Conversions or spiritual turning points","Churches and ministries that influenced the family","Major decisions","Seasons of hardship","Answered prayers","Significant acts of generosity","Moments of provision or protection"]},
   step:"Complete Days 1\u20137 of the 21-day journey. Record one story of God\u2019s faithfulness."},
  {t:"The Faith We Practice", scr:"1 Corinthians 11:1",
   sq:"The faith most likely to be passed forward is the faith the next generation sees practiced consistently.",
   outcomes:["Examine what their daily example communicates","Identify visible and invisible family values","Discuss marriage, relationships, work, money, and generosity","Choose one family practice to strengthen"],
   opening:"What did your family teach you through example that it may never have taught you with words?",
   moves:[
    {t:"The Next Generation Is Watching", p:"Children and grandchildren notice:", list:["How we speak to one another","How we handle pressure","Whether we apologize","What we prioritize","How we make decisions","What we fear","How we use money","Whether faith influences everyday life"]},
    {t:"Values Become Legacy Through Practice", p:"A family may say it values faith, relationships, generosity, or service. The next generation learns the actual values by observing where the family invests:", list:["Time","Attention","Money","Energy","Celebration","Sacrifice"]},
    {t:"Ordinary Practices Become Spiritual Formation", p:"Faith can be woven into:", list:["Family meals","Celebrations","Travel","Giving decisions","Business conversations","Caregiving","Conflict","Family traditions","Major transitions"]}],
   qs:["What does the next generation currently see us prioritize?","Where is our example consistent with our beliefs?","Where is there a gap between what we say and what we practice?","What has our family modeled about work and success?","What has our family modeled about money and generosity?","What spiritual practice could become more natural in our family?"],
   exercise:{t:"Our Visible Values", p:"Choose five values important to your family. For each value, answer:", list:["What does this value mean?","How do we currently practice it?","What behavior would make it more visible?","What could undermine it?"]},
   step:"Complete Days 8\u201314 of the 21-day journey. Choose one shared practice involving prayer, conversation, service, or generosity."},
  {t:"The Faith We Prepare Others to Carry", scr:"Luke 12:48",
   sq:"Passing faith forward requires preparing people, not merely preparing documents or transferring resources.",
   outcomes:["Evaluate next-generation readiness","Identify wisdom that must be transferred","Discuss the opportunities and risks associated with wealth","Recognize conversations that should no longer be postponed","Begin planning a personal blessing"],
   opening:"What responsibility were you given that helped you grow into maturity?",
   moves:[
    {t:"Responsibility Must Be Developed", p:"The next generation needs more than opportunity. It needs:", list:["Character","Wisdom","Competence","Spiritual maturity","Relational health","Financial understanding","A sense of calling","Experience making decisions"]},
    {t:"Wealth Requires Purpose", p:"Resources without purpose can create confusion, entitlement, conflict, and dependency. Families should explain:", list:["Where the resources came from","What sacrifices helped create them","What the family believes about ownership","What responsibilities accompany wealth","How generosity fits into the family\u2019s purpose","What the family hopes the resources will accomplish"]},
    {t:"Silence Is Also a Message", p:"When families avoid difficult subjects, the next generation may create its own assumptions. Healthy conversations should be:", list:["Age-appropriate","Gradual","Honest","Respectful","Facilitated when necessary","Focused on preparation rather than control"]}],
   qs:["In what ways is the next generation well prepared?","Where does it need greater character, competence, or experience?","What wisdom do we wish we had received earlier?","What do we want our family to understand about wealth?","What conversation have we postponed?","What blessing does each child or grandchild need to hear?"],
   exercise:{t:"Readiness Before Inheritance", p:"For each next-generation family member, prayerfully consider strengths, spiritual maturity, financial competence, relational readiness, leadership potential, current needs, the appropriate next responsibility, and support or mentoring needed. This is not a judgment exercise. It is a preparation exercise."},
   step:"Complete Days 15\u201318 of the 21-day journey. Write one personal blessing or wisdom letter."},
  {t:"The Faith We Intentionally Pass Forward", scr:"Psalm 145:4",
   sq:"A spiritual legacy becomes more powerful when faith, stories, wisdom, generosity, relationships, and resources are aligned around a clear family purpose.",
   outcomes:["Clarify the purpose of their family\u2019s resources","Develop a family spiritual legacy statement","Identify stories and wisdom to preserve","Select three practical next steps","Commit to an ongoing legacy rhythm"],
   opening:"If future generations remember only three things about your faith and family, what do you hope they remember?",
   moves:[
    {t:"Legacy Is More Than an Estate", p:"A complete family legacy includes faith, relationships, character, stories, wisdom, work, generosity, resources, influence, and blessing. Financial assets are only one part of what is entrusted."},
    {t:"What Is Unwritten May Be Lost", p:"Families should consider preserving:", list:["Recorded interviews","Legacy letters","Ethical wills","Family devotionals","Photographs with stories","Family values","Faith timelines","Personal blessings","Giving histories","Lessons from failure and success"]},
    {t:"Legacy Requires an Ongoing Rhythm", p:"Legacy is not a one-time event. Families can establish:", list:["An annual family meeting","A yearly generosity conversation","Recorded grandparent interviews","A family service project","A shared devotional journey","A next-generation mentoring plan","An annual review of the family mission and values"]}],
   qs:["What do we believe God has entrusted to our family?","Why do we believe these resources and opportunities exist?","What stories and wisdom must be preserved?","What do we want our family name to represent?","What should future generations be free to change?","What are our three most important next steps?"],
   exercise:{t:"Our Spiritual Legacy Statement", p:"Complete the following:", list:["We believe God has entrusted our family with \u2026","We are most grateful for \u2026","We want our family to be known for \u2026","We will seek to use our time, abilities, relationships, resources, and influence to \u2026","We pray that future generations will \u2026"]},
   step:"Choose the first three actions for your Family Spiritual Legacy Plan, and set the date of your next family legacy meeting."}],
 plan:{t:"The Family Spiritual Legacy Plan", d:"At the end of the 21 days, complete the following:", items:[
  ["The Faith We Have Received","The people and experiences that most shaped our faith are:"],
  ["The Stories We Will Preserve","The three stories our family must not lose are:"],
  ["The Convictions We Will Carry","Our family believes:"],
  ["The Practices We Will Strengthen","The spiritual practices we want to make more visible are:"],
  ["The Relationships We Will Protect","The relationships or conversations needing attention are:"],
  ["The Wisdom We Will Transfer","The lessons we most want future generations to receive are:"],
  ["The Resources We Will Steward","We believe God has entrusted resources and influence to us for:"],
  ["The Blessing We Will Speak","The blessing we want every child and grandchild to hear is:"],
  ["The First Three Actions We Will Take",""]]},
 commit:{t:"Final Commitment", items:["One story I will preserve","One relationship I will strengthen","One piece of wisdom I will pass forward","One blessing I will speak","One responsibility I will help the next generation develop","One generosity practice our family will begin","Our next family legacy meeting will take place on"]}
};

/* ---------- register the flagship collection into FLC ---------- */
if(window.FLC){
  FLC.campaigns.push(FWPO);
  FLC.readings = FLC.readings || {};
  FLC.readings["faith-worth-passing-on"] = FWPO_READS;
  FLI.flags.forEach(function(f){
    if(f.built) return;
    var dom = FLI.domains[f.dom-1];
    var cat = dom.c.filter(function(x){return x[0]===f.n || x[0]===f.n.replace("?","");})[0] || dom.c.filter(function(x){return x[0].indexOf(f.n.slice(0,12))===0;})[0];
    FLC.campaigns.push({
      id:f.id, docFlagship:true, status:"architected",
      title:f.n, sub:f.sub,
      kicker:"A Flagship Family Legacy Campaign",
      quote:f.sub+".",
      desc:(cat?cat[1]+" ":"")+"A complete campaign built on the standard six-session frame \u2014 daily readings, table questions, weekly steps, and the full resource suite \u2014 composed in the Family Legacy by Design framework upon the shepherd\u2019s blessing.",
      big:cat?cat[1]:f.sub+".",
      scrRef:"", scrKJV:"", kjv:false,
      areas:f.areas, hue:f.hue,
      audience:"", season:"",
      days:40, domName:dom.n, domNo:f.dom
    });
  });
  var fw=FLC.campaigns.filter(function(c){return c.id==="faith-worth-passing-on";})[0];
  fw.domName=FLI.domains[1].n; fw.domNo=2;
}
})();
