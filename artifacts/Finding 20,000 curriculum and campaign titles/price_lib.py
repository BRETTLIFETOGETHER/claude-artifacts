# -*- coding: utf-8 -*-

PRINCIPLE = "Price by attendance. Never by seat."

PRINCIPLE_WHY = ("This is the single most important pricing decision on the page and it is the one most platforms "
 "get wrong. A church&rsquo;s volunteers rotate every term. The person leading a small group this autumn is not "
 "leading one next spring. Per-seat pricing turns every new volunteer into a purchase order, and the result is "
 "that a church buys ten seats, guards them, and the platform never reaches the eighty people who would actually "
 "have used it. One price by attendance, unlimited seats, and the ministry director stops rationing access.")

PRINCIPLE_RULES = [
 ["Unlimited seats, always","Pastor, staff, volunteer ministry leaders, group hosts, members, the whole congregation. Nobody is counted and nobody is rationed."],
 ["Attendance is the only variable","Average weekend attendance, self-reported, checked once a year. Simple to quote, simple to renew, and it scales with the church&rsquo;s actual capacity to pay."],
 ["No per-user analytics gating","Do not sell a cheaper tier that hides the diagnostics. The diagnostics are the front door and gating them kills the funnel."],
 ["One renewal date","Everything on one invoice, one date. A church finance committee will cancel four small subscriptions and keep one large one."],
]

FREE = {
 "n":"The Front Door",
 "price":"Free, unlimited seats",
 "line":"Free is not a trial. It is a permanent tier with a real product in it.",
 "items":[
  ["The Sermon Library","Browse and search all 21,534 titles. Full outline and text on 500 of them, refreshed quarterly."],
  ["All 22 diagnostics","Every intelligence, scored, banded, with the prescribed first move. This is the best sales instrument here and it should never be behind a wall."],
  ["One complete Sunday","An overview sermon, six daily devotionals, a group guide, a kids version and a print-ready file. One finished thing, not a sample of a sample."],
  ["Christian Life Intelligence","Any member, any time, private to them. The only instrument a congregant takes without a staff member involved."],
  ["The finder","Search every catalogue. See what exists. Build nothing."]],
 "gate":"The builder, the generation engine, the full text on 21,034 titles, print files and everything downstream of the profile.",
}

LANES = [
 ["The Weekend","Sermons, series, service design, illustrations, weddings and funerals"],
 ["The Week","The six-day devotional engine and the story capture system"],
 ["The Circle","1,000 small group studies across 20 affinity editions"],
 ["The Classroom","ABF, Sunday School, electives and the seminary spine"],
 ["The Team","Staff formation, meetings, leadership pipeline and volunteer development"],
 ["The Household","Family, kids, students and household rhythms"],
]

SIZES = ["Under 250","250 to 1,000","1,000 to 2,500","Over 2,500"]

PRICING = [
 ["One lane","Any single spoke, unlimited seats",[290,490,690,890],
  "For the church that wants groups and nothing else, or the weekend and nothing else. Most churches that start here move to all-access inside two years."],
 ["Church All-Access","All six spokes, unlimited seats, every campaign",[990,1990,3490,4990],
  "The Netflix pass. Everything on the platform, every campaign included, the whole congregation, one invoice, one renewal date."],
 ["All-Access plus Ministry","All-access plus Financial Wisdom and Family Legacy Ministry",[1690,3290,5490,7990],
  "Adds the two named ministry platforms as full church programmes rather than campaigns. For churches building a department rather than running a season."],
]

ALACARTE = [
 ["One campaign","349 / 549 / 749 / 949","Everything a six-week churchwide season needs: six messages, six weeks of devotionals, the group study, kids and student editions and the print files.",
  "Three campaigns costs more than all-access at every size. That is deliberate."],
 ["One small group study","39 digital / 89 with 12 print copies","A single six-session study for one group. Any of the 1,000, any of the 20 affinity editions.",
  "The impulse purchase. Priced so a host can put it on a personal card without asking anybody."],
 ["Financial Wisdom Ministry","1,490 campaign / 3,900 full ministry","The 40-day campaign, or the whole ministry build with the diagnostic, tracks, coaching and the senior pastor edition.",
  "Included in All-Access plus Ministry. Standalone for churches not subscribed."],
 ["Custom build","See the custom tiers","Configured, adapted or fully custom against this church&rsquo;s profile.",
  "Configured is included at All-Access. Adapted and fully custom are always priced separately."],
]

SEATS = [
 ["Senior pastor","Everything","The full library, the builder, the archive tools, every diagnostic, and the Pastor Intelligence profile."],
 ["Church staff","Everything in their lane, plus the team spoke","Their ministry&rsquo;s library, the staff formation tracks, meeting builder, and the diagnostics they own."],
 ["Volunteer ministry leaders","Their lane, plus training","The library for the ministry they lead and the training tracks that go with it. No admin, no billing, no seat request."],
 ["Small group hosts","Curriculum, leader intelligence, host training","All 1,000 studies, Small Group Leader Intelligence for their own room, and the Host track of Small Group University."],
 ["Members","Devotionals, their study, their own diagnostic","The daily devotional, whatever their group is doing, and Christian Life Intelligence, private to them."],
 ["The whole congregation","Daily devotional delivery","Email included at every tier. Anyone with an address, no login required to receive it."],
]

DELIVERY = {
 "line":"Email is a rounding error. SMS is not, and pricing must reflect that.",
 "why":("Six sends a week times fifty-two weeks is three hundred and twelve messages per subscriber per year. "
  "At email rates that is pennies. At SMS rates it becomes a real cost that at large-church scale exceeds the "
  "entire subscription, so email is included everywhere and SMS is metered."),
 "rows":[
  ["Email delivery","Included at every tier, unlimited","Under 250: about $11 a year in cost. Over 2,500: about $275. Absorb it and never mention it."],
  ["SMS, up to 250 subscribers","+$290 per year","Roughly $620 in cost at full uptake. Priced to be worth offering and not to lose money."],
  ["SMS, up to 1,000 subscribers","+$890 per year","Roughly $2,465 in cost at full uptake, and real uptake runs nearer forty percent."],
  ["SMS, unlimited","+$1,890 per year","Only sensible above 2,500 attendance, and only for churches that have asked for it twice."],
  ["Push, in their existing app","Included where integration exists","Cheapest channel of all, because somebody else already built and maintains the app."]],
 "note":("Set SMS uptake expectations honestly. A church of a thousand will not get a thousand SMS subscribers. "
  "Thirty to forty percent is a strong result and the pricing above assumes it."),
}

CUSTOM = [
 ["Configured","Included at All-Access","Church name, pastor&rsquo;s voice and phrasing, their translation, their service times, their examples and their next steps, generated from the profile with one human review pass."],
 ["Adapted","$1,200 per study or campaign","An existing study or campaign reworked for this church. New examples, changed emphasis, local material added. Most requests for custom actually want this."],
 ["Fully custom","$2,500 per study &middot; $6,500 per campaign","Written from scratch on a topic nobody has covered, in this pastor&rsquo;s voice, using this church&rsquo;s stories."],
]

PRINT = [
 ["5.5 x 8.5 saddle-stitch, 48pp","$9 / $7 / $5.50 / $4.50","12 / 50 / 100 / 500 copies. The default six-session guide."],
 ["6 x 9 perfect bound, 96pp","$16 / $12 / $9 / $7","Reads like a book. Devotionals and narrative studies."],
 ["8.5 x 11 spiral, 64pp","$18 / $14 / $10.50 / $8.50","Lies flat, room to write. Workbooks and anything with exercises."],
 ["Church bulk, top ten titles","100 copies from $450","Pre-printed, warehoused, shipped on a schedule. The line that makes campaigns land."],
]

BIGTICKET = [
 ["The Pastor&rsquo;s Library Project","$8,500 &middot; $28,000 &middot; $65,000+",
  "Foundation, Legacy and Full. Thirty years of archive uploaded, transcribed, indexed, coverage-reported and converted into usable resources. Rights stay with the pastor.",
  "The most defensible line here. Nobody else asks for the archive, which is why nobody else can do this."],
 ["Family Legacy Ministry &mdash; church door","$4,900 to $12,500 per year by size",
  "Run as a church ministry to the highest-capacity households in the congregation. Assessment, four interviews, Journey Builder and the whole-family experience.",
  "The first ministry of its kind to ultra-high-net-worth families. Churches have raised money from them for decades and almost nobody has served them."],
 ["Family Legacy Ministry &mdash; advisor door","$4,800 per advisor per year, plus $1,500 to $4,000 per family engagement",
  "The same system run as a practice by a Christian financial advisor, RIA, family office or estate attorney.",
  "Different buyer, different sales motion, different price. Never put this on the church price list."],
 ["Network or denominational licence","Quoted. Indicative: $180 to $420 per church per year at volume",
  "One agreement, many churches, a floor and a cap. Includes onboarding and a named contact.",
  "One denomination is worth two hundred individual sales and takes eighteen months to close."],
]

FOUNDING = {
 "n":"The Founding 100",
 "line":"One hundred churches. Fifty percent off year one, and the price locked for three.",
 "why":("The offer has to be worth more than the discount, because a discount alone attracts churches that leave "
  "when it ends. What holds a founding church is being heard &mdash; and what LifeTogether needs from the first "
  "hundred is not revenue, it is the thing no amount of building produces on its own: knowing which of "
  "twenty-five thousand assets a real church actually opens."),
 "gets":[
  ["Fifty percent off year one","All-Access at $495, $995, $1,745 or $2,495 depending on size."],
  ["Price locked three years","Whatever the platform costs in year three, a founding church pays year-one rates."],
  ["A Pastor&rsquo;s Library discovery session","Free. Upload the archive, get the Coverage Report, decide afterwards whether to go further."],
  ["Content requests prioritised","The category they need built next goes to the top of the queue. This is the one they will actually use."],
  ["Named as a founding church","On the site, in the materials, permanently. It costs nothing and it matters more than the discount."],
  ["A direct line","Not a support queue. An actual person, and for the first hundred it is Brett."]],
 "asks":[
  ["Use it","Three ministries live within ninety days. Not a licence sitting unopened."],
  ["Tell the truth","A twenty-minute call each quarter about what is not working. This is the whole point of the programme."],
  ["Let us name you","One case study, reviewed and approved by them before publication."],
  ["Introduce two churches","Only if it is working. Never as a condition of the discount."]],
 "math":("A hundred founding churches at an average of $1,200 in year one is $120,000 &mdash; which does not fund "
  "the business. It funds the answer to what to build, and that is worth considerably more than the revenue "
  "forgone."),
}

APP_ANSWER = "Yes, we can. No, we should not &mdash; not first, and possibly not at all."

APP_WHY = ("This is a recommendation against something that sounds obviously right, so here is the arithmetic. A "
 "native app built properly is roughly $285,000 to build and $96,000 a year to maintain. At the entry "
 "all-access price that is two hundred and eighty-seven churches before a single line of content is written. "
 "Email and SMS is $12,000 to build and thirteen churches. And the daily devotional &mdash; the thing an app "
 "would supposedly deliver &mdash; performs better over SMS than it does over push notification for this "
 "congregation.")

APP_OPTS = [
 ["Email and SMS only","$12,000","$6,000/yr","4 to 6 weeks","Do this first",
  "Highest open rate of any channel for this audience, no store, no thirty percent cut, and it works on every phone including the ones church members over sixty actually carry."],
 ["Integrate into their existing church app","$28,000","$12,000/yr","2 to 3 months","Do this second",
  "Most churches over five hundred already have an app they pay for. Being inside it beats competing with it, and the congregation does not have to be persuaded to install anything."],
 ["Progressive web app","$45,000","$18,000/yr","3 to 4 months","Do this third",
  "Installs to a home screen, looks like an app, no store approval, no revenue share, one codebase. Ninety percent of what a native app delivers here."],
 ["React Native cross-platform","$165,000","$60,000/yr","8 to 12 months","Only if the data demands it",
  "One codebase, both stores. Consider only when retention data shows the PWA is genuinely losing people."],
 ["Native iOS and Android","$285,000","$96,000/yr","12 to 18 months","Not yet, and possibly never",
  "Nothing on this platform requires a native capability. Not the devotional, not the library, not the builder, not the diagnostics."],
]

APP_RULES = [
 ["Church app fatigue is real","Most churches over five hundred already run Church Center, Subsplash or Tithely. Asking a congregation to install a second church app is asking them to choose, and the answer is usually the one their pastor already announced."],
 ["The store takes fifteen to thirty percent","Every in-app purchase. On a $4,990 subscription that is up to $1,497 a year to a company that contributed nothing."],
 ["Push is not better than SMS here","For a daily devotional to a mixed-age congregation, SMS open rates beat push notification, and email beats both for anything longer than a sentence."],
 ["A PWA is the honest middle","Home screen icon, offline reading, notifications on both platforms now, no store relationship at all."],
 ["Build the app when retention says so","Not when a pastor asks for one. Pastors ask for apps because apps signal seriousness, and there are cheaper ways to signal seriousness."],
]

HONEST = ("Every number on this page is reasoned rather than validated. No church has been quoted any of it. "
 "Before it goes on a website, take the all-access price and the founding offer to ten pastors across the four "
 "size bands and ask them the only question that matters, which is not whether it is worth it but what they "
 "would have to stop paying for in order to say yes.")
