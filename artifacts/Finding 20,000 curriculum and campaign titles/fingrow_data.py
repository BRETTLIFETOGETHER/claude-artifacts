# -*- coding: utf-8 -*-

# ============ FINANCIAL HEALTH ============

FIN_SPLIT = [
 ["The church's money","Institutional",
  "Budget, reserves, controls, compensation, facilities, audit and the capital campaign. This is stewardship of an organization, and it is a competency problem.",
  ["Budget and forecast","Reserves and cash","Internal controls","Staff compensation and HR","Facilities and capital","Audit and compliance"]],
 ["The congregation's money","Discipleship",
  "Debt, margin, giving, contentment, legacy. This is formation of people, and it is a heart problem before it is a competency problem.",
  ["Financial discipleship","Generosity formation","Debt and margin","Legacy and estate","Business owners","Next generation"]],
]

FIN_DOMAINS = [
 {"id":"budget","n":"Budgeting & Operations","one":"Can this church say where every dollar went and where the next one goes?",
  "why":"Most church budgets are last year plus three percent, built by two people, understood by nobody. A budget is a moral document — it says what the church actually believes, regardless of what it preaches.",
  "sub":["Zero-based ministry budgeting","Rolling twelve-month forecast","Fund accounting and restrictions",
         "Internal controls and two-person counting","Monthly reporting a board can read","Cash reserves policy",
         "Designated gifts handled legally","Debt policy and thresholds"],
  "tools":["Budget build template","Reserve policy generator","Controls self-audit","Board reporting pack"],
  "band":"Six months of clean monthly reporting and three months of operating reserve is the floor."},
 {"id":"gen","n":"Generosity Culture","one":"Are people becoming generous, or is the church just funded?",
  "why":"A funded church and a generous church are not the same thing, and confusing them is how a budget gets met while a congregation stays unchanged. Generosity is a discipleship outcome that happens to produce revenue.",
  "sub":["Teaching money from the platform","The five T's — Truth, Time, Talent, Treasure, Testimony",
         "First-time giver pathway","Lapsed giver recovery","Recurring giving and friction",
         "Testimony and story","Thanking and reporting impact","The no-ask season"],
  "tools":["40 Days of Generosity campaign","Giving analysis by household","First-gift follow-up sequence","Impact report template"],
  "band":"Percentage of households giving matters more than total dollars. Under thirty percent is a formation problem, not a funding one."},
 {"id":"disciple","n":"Financial Discipleship","one":"Is anyone helping the household with its own money?",
  "why":"Sixty to seventy percent of households in a typical congregation are under real financial strain, and most churches address it once a year from the platform and never in a room. This is where trust is either built or lost.",
  "sub":["The six H's — Honor, Heart, Health, Habits, Hope, Harvest",
         "Struggling to stability to surplus to stewardship to significance",
         "Budgeting and debt classes","Marriage and money","Teaching children and teenagers",
         "Business owners and marketplace","Retirement and the second half","Crisis and benevolence"],
  "tools":["40 Days of Financial Wisdom","Master Your Money curriculum","God Owns It All","Household assessment"],
  "band":"A church of any size should be running at least one financial discipleship track twice a year."},
 {"id":"capital","n":"Capital Campaigns","one":"Can this church fund a building without spending its soul?",
  "why":"Most capital campaigns ask for three-year cash pledges and nothing else, which leaves the largest gifts in the room untouched. The asset conversation is the highest-leverage addition available to any church campaign.",
  "sub":["Feasibility and readiness","The case for support","The quiet phase and lead gifts",
         "The asset track — give before you sell","Advisor liaison and the pre-exit question",
         "Congregational phase and commitment Sunday","Pledge fulfilment and reporting","Debt versus pay-as-you-go"],
  "tools":["Readiness assessment","Case for support template","Asset track seminar","18-month campaign calendar"],
  "band":"Never run formation and an ask in the same six weeks. Ninety days minimum between them."},
 {"id":"legacy","n":"Legacy & Endowment","one":"Is anyone stewarding what leaves this congregation at death?",
  "why":"The largest transfer of wealth in history is moving through congregations that have never had a single conversation about it. Most churches will receive nothing from it, not because families were unwilling but because nobody asked or taught.",
  "sub":["Wills and estate basics taught from the church","Legacy giving conversations",
         "Endowment policy and governance","Donor advised funds explained plainly",
         "Appreciated assets and business interests","The family conversation across generations",
         "Advisor partnerships","Gift acceptance policy"],
  "tools":["Legacy conversation guide","Endowment policy template","Gift acceptance policy","Advisor partnership brief"],
  "band":"A written gift acceptance policy and one legacy teaching moment a year is the minimum credible position."},
 {"id":"hr","n":"Compensation & Staff HR","one":"Is the staff paid fairly, legally and defensibly?",
  "why":"Church compensation is where good intentions produce real harm — underpaid staff, undocumented decisions, and clergy tax handled by guesswork. Most of it is fixable in one quarter and almost none of it is discussed.",
  "sub":["Compensation philosophy in writing","Benchmarking by role and region",
         "Clergy housing allowance done correctly","Payroll, benefits and retirement",
         "Employment classification and volunteers","Reviews, raises and the pay conversation",
         "Handbook, policies and safeguarding","Termination and severance"],
  "tools":["Compensation philosophy template","Role benchmark worksheet","Housing allowance resolution","Review structure"],
  "band":"Every role has a written description, a band, and a documented annual review. Anything less is a liability."},
]

FIN_QS = [
 ["Can you produce accurate monthly financials within ten days of month end?",["Always","Usually","Rarely","No"]],
 ["How many months of operating reserve do you hold?",["Six or more","Three to six","One to three","Under one"]],
 ["Does more than one unrelated person handle every count and deposit?",["Always","Usually","Sometimes","No"]],
 ["What percentage of households give in a given year?",["Over 50%","30 to 50%","15 to 30%","We do not track it"]],
 ["How often do you teach on money from the platform?",["A series a year plus","Two or three times","Once","We avoid it"]],
 ["Is there a financial discipleship class running this year?",["Twice a year","Once a year","Occasionally","Never"]],
 ["Does every staff role have a written description and pay band?",["All of them","Most","A few","No"]],
 ["Is the clergy housing allowance formally board-resolved each year?",["Yes, annually","Sometimes","Not sure","No"]],
 ["Do you have a written gift acceptance policy?",["Yes","In draft","No","What is that"]],
 ["Has anyone taught on wills or estates in the last two years?",["Yes, more than once","Once","No","Never"]],
 ["If you ran a capital campaign, would you ask for assets as well as cash?",["Yes, with an advisor track","We would mention it","Cash only","Not planning one"]],
 ["Does the congregation know where the money goes?",["Published and explained","Available on request","Only the board knows","Not really"]],
]

FIN_BANDS = [
 ["12 to 22","Exposed","Controls, reserves and documentation are the first work. Nothing else holds until they do. Start with the budget and controls domain and do not launch a campaign this year."],
 ["23 to 32","Functional but fragile","The church runs, and one departure or one audit would hurt. Document what is in people's heads, then start one financial discipleship track."],
 ["33 to 40","Healthy institution, quiet congregation","The organization is well run and the households are not being discipled. This is the most common band and the biggest missed opportunity."],
 ["41 to 48","Integrated","Both sides are working. The next frontier is legacy and the asset conversation, which almost nobody has started."],
]

FIN_SERMONS = [
 ["End-of-Year Giving","170","Six tracks — the year behind you, why we give, the practical ask, the heart behind it, giving past this year, the last Sunday"],
 ["Faith and Finances","25","Money as a discipleship issue, taught as a series or a standalone"],
 ["40-Day Campaigns · Generosity & Stewardship","20","A full track inside the campaign library — flagship giving through to God Owns It All"],
 ["Impact Sundays","125","Reporting well, local impact, global impact, and the congregation's part"],
 ["Thanksgiving","145","Harvest and provision, gratitude that moves outward, first fruits"],
 ["Vision Sunday","170","Includes the ask and the response track — count the cost, faith requires a number, commit today"],
]

FIN_CURRIC = [
 ["40 Days of Financial Wisdom","Churchwide, 6 weeks","The six H's — Honor, Heart, Health, Habits, Hope, Harvest. Whole-life financial discipleship across every income level, not a budgeting class.","Ron Blue line · active"],
 ["40 Days of Generosity","Churchwide, 6 weeks","The five T's — Truth, Time, Talent, Treasure, Testimony. Runs under a no-ask covenant: nobody is asked for anything for six weeks.","active"],
 ["God Owns It All","6 sessions","Ron Blue's published work. The single strongest standalone message in the catalogue and a whole stewardship framework underneath.","Ron Blue line · active"],
 ["Master Your Money","5 sessions","Practical enough that week one holds attention on its own.","Ron Blue line · active"],
 ["How Much Is Enough?","5 sessions","The question is the sermon. Works in any congregation and as a framework for families with more than they need.","Ron Blue line · active"],
 ["Financial Wisdom for Business Owners","4 sessions","Profit and faithfulness together, plus the pre-exit conversation most owners never have.","developing"],
 ["Teaching Children About Money","4 weeks, household","The three-jar spine, with the give jar's destination chosen by the child.","active"],
 ["The Legacy Conversation","3 sessions","For families across generations. Values before assets.","developing"],
]

FIN_COACH = [
 ["Senior Pastor","Teaching money without flinching","Four sessions on preaching generosity, the theology of ownership, handling the wealthy and the struggling in one room, and what to do when giving drops."],
 ["Executive Pastor","Building the financial year","Six sessions on budget construction, reserve policy, board reporting, and the compensation conversation."],
 ["Finance & Administration","Controls, audit and clean books","Eight sessions covering fund accounting, internal controls, audit readiness and clergy payroll."],
 ["Stewardship Pastor","Generosity as formation","Six sessions on annual strategy, donor care, the capital campaign and the legacy conversation."],
 ["Elder / Finance Committee","Fiduciary duty, plainly","Four sessions on reading statements, oversight without micromanagement, and where boards are actually liable."],
 ["The whole team","One shared language","A single half-day so the staff stops having six different conversations about the same money."],
]

# ============ CHURCH GROWTH ============

GROW_MATH = [
 ["Reach","People who visit for the first time","A church that reaches nobody new is one generation from closing, regardless of how healthy it feels."],
 ["Retain","People who come back and stay","Almost every church has a retention problem it has misdiagnosed as a reach problem. The second visit decides more than the first."],
 ["Reproduce","People who bring, lead and send","Growth that depends on the staff plateaus at the staff's capacity. Growth that depends on members does not."],
]

GROW_TRUTH = "Most churches try to fix growth with more reach when the leak is retention. If a hundred guests visit and eighty never return, another hundred guests changes nothing. Fix the leak before opening the tap."

GROW_BARRIERS = [
 ["Under 65","The single-cell church","Everyone knows everyone, and the pastor is the shepherd of every person. Growth stops because there is no room in the relational circle.",
  ["The pastor must stop being everyone's pastor","One additional group is the whole strategy","Delegate care to two or three people","Guests are absorbed or they are not — there is no system yet"]],
 ["65 to 125","The pastoral barrier","One person can pastor about seventy-five people well. Past that, care fails quietly and people leave without saying why.",
  ["Build a care team before you need one","First staff or lay leader hire","A real group structure, not a small church pretending","Someone owns follow-up by name"]],
 ["125 to 250","The program barrier","The church needs actual ministries, not just a service, and the volunteer base has to double.",
  ["Volunteer systems and placement","Children's ministry that parents trust","A second service or a bigger room","The pastor moves from doing to developing"]],
 ["250 to 500","The staff barrier","Volunteer leadership alone cannot carry it, and the first real staff team has to be built and led.",
  ["Hire for the gaps, not the fires","Executive leadership becomes a role","Systems replace heroics","Assimilation must be measurable"]],
 ["500 to 1,000","The systems barrier","Everything that worked by relationship now has to work by process, and it feels like a loss.",
  ["Every ministry documented and two deep","Data and dashboards","Leadership pipeline, not recruitment","Culture has to be taught, not caught"]],
 ["Over 1,000","The leadership barrier","Growth is limited by how many leaders the church can produce, not by how many people it can attract.",
  ["A residency or development pipeline","Multisite or planting decision","The senior pastor gives away the thing he is best at","Multiplication becomes the metric"]],
]

GROW_ENGINES = [
 ["Invite","Turning members into inviters",
  "Advertising fills a room once. Members fill it repeatedly. The most reliable growth engine in every study is an ordinary person inviting somebody they already know.",
  ["Friends Day and the 5F exercise","One name, prayed for and asked","Invite cards with three scripts",
   "Bring-someone Sundays on the calendar","The ask made from the platform, specifically"],
  "Friends Day · 140 messages"],
 ["Welcome","The first ninety seconds",
  "Most churches are judged before anyone hears a word. Parking, signage, the children's check-in and one human being who learns a name decide whether there is a second visit.",
  ["Guest experience audit with fresh eyes","Parking and wayfinding","Children's check-in a parent trusts",
   "Trained greeters, not enthusiastic ones","Follow-up inside forty-eight hours"],
  "Any Given Sunday · 120 messages"],
 ["Connect","Rows into circles",
  "The single strongest predictor of whether someone is still attending in two years is whether they have friends there. Groups are not a program, they are the retention system.",
  ["Group launch twice a year","Placement inside three weeks","Host, do not teach",
   "Sermon-aligned group material","Coaching layer above the leaders"],
  "Small Group Launch · 200 messages"],
 ["Serve","Belonging through doing",
  "Serving is the fastest front door a church has and the strongest glue it owns. People who serve stay, give and invite at multiples of those who only attend.",
  ["Ministry fair and serving Sundays","One slot, one season, signed up before leaving",
   "Onboarding inside three weeks","Team leaders developed, not just recruited","Honour publicly and often"],
  "Volunteer Sunday · 100 messages"],
 ["Send","Growth that multiplies rather than adds",
  "A church that only adds eventually stops. A church that sends people, leaders, groups and campuses compounds — and gives away its best as a strategy rather than a loss.",
  ["Leadership pipeline with named seats","Church planting or campus decision",
   "Sending your best staff on purpose","Groups that multiply from week one","Missions that deploys members"],
  "Sending and Multiplication · 20 messages"],
]

GROW_QS = [
 ["Roughly how many first-time guests visit each month?",["Twenty plus","Ten to twenty","Under ten","Almost none"]],
 ["What share of guests return for a second visit?",["Over half","A third","Under a fifth","We do not know"]],
 ["Is anyone following up with guests inside forty-eight hours?",["Every guest","Most","Occasionally","No"]],
 ["What percentage of adults are in a group?",["Over half","A third","Under a quarter","We do not track it"]],
 ["What percentage of adults serve somewhere?",["Over half","A third","Under a quarter","Not tracked"]],
 ["When did you last launch a wave of new groups?",["Within six months","Within a year","Over a year ago","We have never done a launch"]],
 ["Where does most of your growth come from?",["New believers","Invitations from members","Other churches","We are not growing"]],
 ["How many leaders have you developed and released in two years?",["Five or more","Two to four","One","None"]],
 ["Does every ministry have someone ready to take it over?",["Nearly all","Some","Few","No"]],
 ["Has anyone been sent out — planter, campus, missionary — in three years?",["Yes, more than one","One","No","Never"]],
]

GROW_BANDS = [
 ["10 to 18","Leaking","Guests arrive and disappear. Work retention before reach: follow-up, groups and serving, in that order. Advertising now would waste money."],
 ["19 to 26","Adding slowly","The basics work but nothing compounds. Build the group launch rhythm and the serving pathway, and the same reach will produce more."],
 ["27 to 34","Growing","Reach and retention both function. The constraint is leadership production — you will hit the ceiling of who you have developed."],
 ["35 to 40","Multiplying","The systems work and people are being sent. The question now is whether it survives the current leader."],
]

GROW_STAGES = [
 ["Plant","0 to 3 years","Everything is reach. Retention systems barely exist and should be built before they are needed, not after."],
 ["Growing","Adding steadily","The risk is that systems lag behind size. Build the next stage's structure while you are still in this one."],
 ["Plateaued","Flat two years or more","Almost always a retention or leadership problem misread as a reach problem. Diagnose before you spend."],
 ["Declining","Shrinking","Stop adding programmes. Name the honest reason, address care and community first, and expect eighteen months."],
 ["Replant","Starting again","A small congregation with a building and a history. Trust before change, and the timeline is measured in years."],
 ["Multisite","Multiple locations","Growth by replication. Everything that is not written down breaks at the second location."],
]
