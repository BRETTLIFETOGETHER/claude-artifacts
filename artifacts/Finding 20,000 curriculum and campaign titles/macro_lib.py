# -*- coding: utf-8 -*-

PROBLEM = ("There are now more than twenty-five thousand assets across a dozen platforms, and a pastor looking at "
 "them sees a warehouse rather than a product. The organising principle is not a menu or a taxonomy. It is a wheel "
 "&mdash; one hub that knows the church, six spokes that deliver formation into the six environments a church "
 "actually has, and a rim that turns them all at once.")

WHY_ORG = [
 ["A catalogue is not a product","Twenty-five thousand assets with no organising principle is a liability. The pastor cannot hold it, cannot describe it to his board, and cannot choose."],
 ["The environments are fixed, the content is not","Every church on earth has the same six environments. Organise around those and the content becomes obvious rather than overwhelming."],
 ["The hub is the only real moat","Anyone can build a library. Almost nobody will build the profile that makes a library usable, because it requires asking questions nobody asks."],
 ["The rim is what makes it a wheel","Without something that turns all six spokes at once, this is six products in a bag. The campaign is the rim."],
]

HUB = {
 "n":"The Church Intelligence Profile",
 "line":"One profile. Written once. Read by everything.",
 "body":("The hub is not content. It is what the platform knows about this church &mdash; assembled from the "
  "intelligences, deepened by the pastor&rsquo;s own archive, and read by every spoke before it produces anything. "
  "It is the difference between a library and a system, and it is currently the largest gap between what has been "
  "built and what could be sold."),
 "knows":[
  ["The Pastor","Voice, convictions, preaching archive, coverage gaps, what he returns to and what he has never addressed."],
  ["The Church","Size, stage, denomination, theology, season, history, and what the congregation actually needs."],
  ["The Team","Every seat, capacity, competency, bench depth and who is closest to empty."],
  ["The Ministries","What exists, what it is for, where the pathway breaks, who is missing."],
  ["The People","Household shapes, life stages, who is known, who has never been asked."],
  ["The Gaps","The one thing this church should do next, named rather than guessed."]],
 "sources":["The nine church intelligences","The Pastor&rsquo;s Library upload and coverage report",
  "The staff and congregational surveys","Giving, attendance and serving data the church already has",
  "The stated profile: denomination, size, stage, theology"],
}

SPOKES = [
 ["The Weekend","What happens when the church gathers",
  "The largest spoke and the one everybody starts with. Everything a Sunday needs, from the message to the moment somebody responds.",
  ["5,155 sermon messages across 73 categories","17,319 campaigns across 23 channels","Service design: 14 elements, 8 flows, 12 service types",
   "The illustration engine: 4 methods, 20 sources, 240 examples","200 wedding and funeral services, 51 graveside outlines",
   "Catalytic sermons: 21,534 that stand alone"],
  "Sermon &middot; Service &middot; Campaign &middot; Milestone"],
 ["The Week","What happens between Sundays",
  "The spoke almost nobody builds, and the one that turns a message into formation. Six days from the pastor, and a question at the bottom that builds a story library.",
  ["Six-day devotional engine, 129,204 slots","Two script types: sliced and summary","The story capture system and permission protocol",
   "Daily readings for every study and campaign","The forward-looking question that gathers illustrations before the sermon"],
  "Devotional &middot; Daily reading &middot; Story capture"],
 ["The Circle","What happens in a living room",
  "Where people are actually known. One thousand studies, twenty affinity editions, six sessions every time.",
  ["50 categories, 1,000 studies, 909 unique titles","20 affinity editions = 20,000 combinations","100 starter studies built to launch a new group",
   "Six sessions, always. One format, one training, one template","Leader notes written for the facilitator, not the pastor"],
  "Study &middot; Host &middot; Launch &middot; Multiply"],
 ["The Classroom","What happens when someone wants to go deep",
  "The rung above the circle. Taught rather than facilitated, in terms rather than six-week blocks.",
  ["12 ABF categories, 240 courses, 8 to 13 weeks","Small Group Seminary: 20 disciplines &times; 20 courses","Church-Based Seminary as a church-branded edition",
   "Teacher manuals, not just discussion questions","The ladder from new believer to serious study"],
  "Class &middot; Course &middot; Seminary &middot; Credential"],
 ["The Team","What happens to the people who run it",
  "The staff meeting is the church&rsquo;s most important small group and almost nobody designs it.",
  ["20 roles &times; 4 levels = 440 training modules","25 categories &times; 10 = 250 staff meeting sessions","24-month journey, quarterly planner, certification",
   "The leadership pipeline and bench depth","Volunteer formation across every ministry"],
  "Formation &middot; Meeting &middot; Pipeline &middot; Certification"],
 ["The Household","What happens where the other 167 hours are",
  "A church gets a person for one hour. The household gets them for the rest. The spoke with the most leverage and the least product.",
  ["Family editions of every campaign and study","Kids, student and parent versions","Milestone pathway from birth to launch",
   "Household rhythms, one rather than five","Family Legacy Ministry for the highest-capacity households"],
  "Family &middot; Kids &middot; Students &middot; Legacy"],
]

RIM = {
 "n":"The Campaign",
 "line":"The rim is what turns all six spokes at once.",
 "body":("A churchwide campaign is the only thing that touches the weekend, the week, the circle, the classroom, "
  "the team and the household in the same six weeks. Without it these are six products in a bag. With it they are "
  "a wheel, and the campaign is why LifeTogether has a right to build the other five."),
 "turns":[
  ["The Weekend","Six messages and a service design for each"],
  ["The Week","Six days of devotional for every week of it"],
  ["The Circle","An aligned study, hosts recruited, groups launched"],
  ["The Classroom","A term-length version for the class that wants depth"],
  ["The Team","The staff studies it first, six weeks ahead"],
  ["The Household","Family, kids and student editions of the same idea"]],
}

LAYERS = [
 ["01","Intelligence","Diagnose","Twenty-two instruments that measure what is actually happening before anything is prescribed. This is the entry point and it should be free."],
 ["02","Library","Supply","Twenty-five thousand assets across every environment. This is the inventory, and inventory alone is not a business."],
 ["03","Engine","Generate","Profile &times; library = the deliverable. The engine is what makes 25,000 assets feel like one recommendation, and it is the hardest thing here to copy."],
 ["04","Delivery","Reach","Six spokes into six environments, in the format each one actually uses. A study is not a sermon is not a devotional."],
 ["05","Artifact","Land","A hundred print templates that turn a described resource into something a church hands somebody on Sunday. Digital is the sample; print is the product."],
]

SCALE = [
 ["Sermon messages","5,155","73 categories"],
 ["Campaigns","17,319","23 channels, 1,742 themes"],
 ["Standalone sermons available","21,534","Every campaign compresses to one"],
 ["Small group studies","1,000","50 categories, 909 unique titles"],
 ["Affinity combinations","20,000","1,000 studies &times; 20 editions"],
 ["ABF and seminary courses","640","240 ABF + 400 seminary"],
 ["Staff training modules","440","20 roles &times; 4 levels"],
 ["Staff meeting sessions","250","25 categories &times; 10"],
 ["Wedding and funeral services","200","Plus 51 graveside outlines"],
 ["Intelligence instruments","22","147 dimensions, 176 questions"],
 ["Print templates","100","9 groups, every trim size specified"],
 ["Daily devotional slots","129,204","21,534 sermons &times; 6 days"],
]

MODELS = [
 ["Church subscription","Recurring","Strong",
  "Annual, per library or all-access, priced by attendance. The spine of the business and the only line that compounds.",
  "$290 to $890 per library &middot; $990 to $4,990 all-access",
  "Proven category. Every competitor sells this and none of them sell the hub."],
 ["Print and fulfilment","Recurring, per copy","Strong",
  "Journals, readers and guides. The only per-copy line in the catalogue and the one that makes campaigns profitable rather than free.",
  "Per copy, with bulk breaks at 100",
  "A church that orders ninety journals uses the campaign. A church that downloads a PDF does not."],
 ["Custom build service","Project","Strong",
  "A campaign, curriculum or resource built against one church&rsquo;s profile. Expensive from scratch, profitable against a hundred templates.",
  "$500 to $2,500 by church size",
  "The templates turn this from design into population, which is where the margin is."],
 ["The Pastor&rsquo;s Library Project","High-ticket project","Strongest",
  "Thirty years of archive uploaded, transcribed, indexed, coverage-reported and converted. Nobody else asks for the archive, which is why nobody else can do this.",
  "$8&ndash;15K foundation &middot; $25&ndash;45K legacy &middot; $50&ndash;100K+ full",
  "The most defensible line here and the one that produces the hub."],
 ["Advisor and practice licence","Recurring per seat","Strong",
  "Family Legacy Ministry run as a practice by an advisor, RIA, family office or estate attorney. Different buyer, different price, same system.",
  "Per advisor per year, plus per-family engagement",
  "A separate business with a separate sales motion. Do not put it on the church price list."],
 ["Network and denominational licence","Recurring, many churches","Promising",
  "One agreement, many churches. The fastest path to scale and the slowest sales cycle.",
  "Per-church rate at volume, floor and cap",
  "One denomination is worth two hundred individual sales and takes eighteen months."],
 ["Certification","Recurring per person","Promising",
  "Staff formation credentials at four levels, with the multiplication requirement that makes them mean something.",
  "Per person per level",
  "Only works if the credential is respected, which requires the oral exam and the multiplication proof."],
 ["White label and engine licence","Recurring, enterprise","Speculative",
  "Another organisation runs its own branded library on this engine. High leverage, high complexity, and it competes with the direct business.",
  "Platform fee plus revenue share",
  "Do not pursue until the direct business is proven. It is a distraction with a large number attached."],
 ["Benchmark and research data","Recurring, aggregate","Handle carefully",
  "Anonymised diagnostic data across hundreds of churches becomes the only benchmark dataset in the category.",
  "Report sales, or included at the top tier",
  "Ethically fine only with explicit consent and genuine anonymisation. Get it wrong once and the diagnostics stop being trusted."],
]

PLATFORMS = [
 ["LifeTogether","The church platform","Pastors and church staff",
  "The nine intelligences, six spokes and everything under them. The main business and the one everything else was learned from.",
  ["Weekend","Week","Circle","Classroom","Team","Household"],
  "Subscription plus print plus custom build"],
 ["Family Legacy Ministry","The first ministry to ultra-high-net-worth families","Churches, and advisors as a practice",
  "Churches have raised money from wealthy families for decades. Almost nobody has built a ministry that serves them. Two doors, same system, different pricing at each.",
  ["Assessment","Four interviews","Journey Builder","Whole-family experience"],
  "Church ministry licence, or advisor practice licence"],
 ["The Pastor&rsquo;s Library","The archive business","Individual pastors, high-ticket",
  "Aggregate, transcribe, index, report coverage, convert and approve. A service business that produces the hub for everything else.",
  ["Upload","Transcribe","Index","Coverage Report","Convert","Approve"],
  "Project fee, three tiers"],
 ["Marketplace Intelligence","The business edition","Companies and marketplace leaders",
  "165 categories of business and HR training, converted from the church catalogue. The same engine pointed at a different room, and a market with far more money in it.",
  ["Leadership","Team","Culture","Formation"],
  "Corporate licence, per seat or per company"],
 ["The Engine","What all of them run on","Licensed, eventually",
  "Profile times library equals deliverable. It is the actual intellectual property, and it is the last thing to sell rather than the first.",
  ["Profile","Generate","Personalise","Print"],
  "Not yet. Prove it in the direct business first"],
]

SEQUENCE = [
 ["Now","Wire the hub","One profile, written once, read by every spoke. Nothing else on this list matters as much and nothing else is as unglamorous."],
 ["Now","Make something print","A hundred templates exist as specifications and nothing produces a file. This is the gap between prototype and product."],
 ["Next 90 days","Build 120 flagship kits","Top five per category, built end to end. Eight of 21,534 is the number every founder conversation stalls on."],
 ["Next 90 days","Free diagnostic as the front door","Christian Life Intelligence for members, the church diagnostics for staff. Diagnose before selling and the sale changes shape."],
 ["Next 6 months","One complete free Sunday","The overview sermon, six days, group guide and kids version. Not a sample of a sample &mdash; one finished thing."],
 ["Next 6 months","Kids, student and family editions","Named the most defensible asset three times and still at zero."],
 ["Year one","One denomination or network","Worth two hundred individual sales and the only way this scales past word of mouth."],
 ["Year one","Prove the Pastor&rsquo;s Library with ten pastors","The coverage report is the best sales instrument in the archive and it has never been run on a real library."],
]

HONEST = ("None of the pricing here is validated and none of the revenue models have been tested with a real "
 "church. The structure will survive contact with the market. The dollars probably will not. Test the subscription "
 "price and the all-access price on ten pastors before either appears on a page, and treat every number here as a "
 "recommendation to argue with rather than a plan to execute.")
