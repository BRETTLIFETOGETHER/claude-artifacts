
import html as hlib, os
def e(s): return hlib.escape(str(s))

CSS = open('/tmp/flagship_css.txt').read()

def week(label, tasks, sunday=False, color="#c9a84c"):
    cls = "cd-week sunday" if sunday else "cd-week"
    bg = "rgba(201,168,76,.06)" if sunday else "rgba(255,255,255,.4)"
    bdr = f"border-top:3px solid {color};" if sunday else ""
    rows = "".join(
        f'<p class="cd-task priority">{e(t[1:].strip())}</p>' if t.startswith("★")
        else f'<p class="cd-task">{e(t)}</p>'
        for t in tasks
    )
    return f'<div class="{cls}" style="background:{bg};{bdr}"><span class="cd-week-label">{e(label)}</span>{rows}</div>'

def rank(n, title, desc, action, roi, color, top=False):
    cls = "rank-item rank1" if top else "rank-item"
    bg = "rgba(201,168,76,.04)" if top else "rgba(255,255,255,.5)"
    fs = "44px" if top else "24px"
    nb = "rgba(201,168,76,.06)" if top else "rgba(0,0,0,.03)"
    return f'''<div class="{cls}" style="border-color:rgba(0,0,0,.07);background:{bg};">
<div class="rank-num" style="background:{nb};font-size:{fs};color:{color};">{e(str(n))}</div>
<div class="rank-body">
<h3 class="rank-title">{e(title)}</h3>
<p class="rank-desc">{e(desc)}</p>
<div class="rank-action" style="color:{color};">{e(action)}<span class="rank-roi" style="border-color:{color};color:{color};">{e(roi)}</span></div>
</div></div>'''

def dir_card(r, color, cat, title, why, metrics, mega=False):
    mcls = "dir-card mega" if mega else "dir-card"
    rs = "44px" if mega else "28px"
    met = "".join(f'<span class="dir-metric">{e(m)}</span>' for m in metrics)
    return f'''<div class="{mcls}" style="border-color:{color};{'border-left:4px solid '+color+';' if not mega else ''}">
<span class="dir-rank" style="font-size:{rs};color:{'rgba(201,168,76,.25)' if mega else 'rgba(0,0,0,.1)'};">{r}</span>
<span class="dir-type" style="border-color:{color};color:{color};">{e(cat)}</span>
<h3 class="dir-title">{e(title)}</h3>
<p class="dir-why">{e(why)}</p>
<div class="dir-metrics">{met}</div>
</div>'''

def principle(n, color, title, body):
    return f'''<div class="principle" style="border-color:{color};background:rgba(0,0,0,.01);">
<span class="pr-n">{e(n)}</span>
<h3 class="pr-title">{e(title)}</h3>
<p class="pr-body">{e(body)}</p>
</div>'''

# ── TOP 25 DIRECTORY ────────────────────────────────────────────
DIR_TIER1 = [
    (1,"var(--east)","Easter","Easter Sunday + Outreach","Highest-attended Sunday × highest theological stakes. Every unchurched person the congregation will ever bring arrives at Easter.",["Highest Attendance","Gospel Moment","Formation Launch","Baptism Opportunity","Next Step Critical"],True),
    (2,"var(--gold-dk)","Generosity","Year-End Generosity Sunday","Intersection of maximum financial generosity motivation and maximum formation opportunity. Sets the giving culture for the following year.",["Giving Peak","Legacy Decisions","Pledge Commitment","Formation Depth","Budget Impact"],True),
    (3,"var(--cap)","Capital Campaign","Capital Campaign Launch Sunday","Determines whether the campaign succeeds. The congregation that leaves the launch Sunday with conviction gives extravagantly.",["Multi-Year Impact","Vision Formation","Leadership Test","Community Witness","Building Mission"],True),
    (4,"var(--bap)","Baptism","Baptism Sunday","Publicly marks the most significant formation decision in a person's life. Baptism Sundays reproduce themselves.",["Life-Change Visible","Outreach Catalyst","Community Formation","Story Power","Reproduction"],True),
    (5,"var(--gen)","Launch","Fall Launch / Vision Sunday","Sets the formation culture for the entire year. What the congregation believes is possible here is what they pursue for 12 months.",["Year Sets Here","SG Launch","Ministry Fair","Volunteer Peak","Culture Setting"],True),
]
DIR_TIER2 = [
    (6,"var(--east)","Christmas","Christmas Eve Service","Second highest attendance. Maximum unchurched presence. The family that comes once per year comes tonight.",["Max Unchurched","Family Formation","Re-entry Point","Gospel Moment","Giving Peak"]),
    (7,"var(--gen)","Launch","New Year Launch Sunday","The congregation arrives already asking formation questions. Sets the arc for the year.",["Formation Appetite","SG Launch","New Commitments","Vision Setting","Resolution Culture"]),
    (8,"#6a7a3a","Ministry","Ministry Fair Sunday","Highest volunteer recruitment Sunday of the year when executed with intention.",["Volunteer Peak","Ministry Visibility","Leadership Pipeline","Ownership Culture","Activation"]),
    (9,"#3a6a7a","Outreach","Invite Sunday / Friend Sunday","Designed entirely around the congregation bringing one person.",["Evangelism Culture","Guest Peak","Relationship Mission","Network Effect","Outreach DNA"]),
    (10,"var(--bap)","Formation","Small Group Launch Weekend","Determines small group enrollment for the year.",["Community Formation","Leadership Dev","Retention Peak","Discipleship Arc","Connection"]),
    (11,"var(--gen)","Stewardship","Pledge / Commitment Sunday","The specific Sunday that closes the stewardship campaign.",["Giving Commitment","Formation Test","Budget Foundation","Generosity Culture","Trust"]),
    (12,"var(--east)","Seasonal","Mother's Day Sunday","Second-highest attendance. Most pastorally complex Sunday of the year.",["Attendance Peak","Pastoral Depth","Family Formation","Healing Opportunity","Return Catalyst"]),
    (13,"#6a7a3a","Leadership","Elder / Deacon Installation Sunday","Most visibly models the leadership culture the congregation will reproduce.",["Leadership Culture","Governance Formation","Commissioning Power","Community Ownership","Multiplication"]),
    (14,"var(--cap)","Campaign","Capital Campaign Close / Celebration","Closes the campaign and celebrates what God did through it.",["Generosity Testimony","Faith Building","Community Celebration","Next Gen Formation","Legacy"]),
    (15,"#3a6a7a","Mission","Mission Trip Launch / Return Sunday","Highest discipleship-density weekend in the church year.",["Disciple Formation","Mission Culture","Story Power","Leadership Pipeline","Outreach DNA"]),
    (16,"var(--gen)","Seasonal","Thanksgiving Sunday","Frames gratitude as formation rather than sentiment. The generosity setup for December.",["Gratitude Formation","Generosity Prep","Family Presence","Unchurched Moment","Year Review"]),
    (17,"var(--east)","Seasonal","Advent — First Sunday","Sets the formation culture for the entire Advent season.",["Season Setting","Formation Arc","Family Rhythm","Expectation Culture","Christmas Prep"]),
    (18,"var(--bap)","Formation","40-Day Campaign Launch Sunday","Launches the most formation-intensive experience available to a congregation.",["Formation Peak","SG Launch","Daily Engagement","Campaign Arc","Community"]),
    (19,"#6a7a3a","Pastoral","Pastoral Transition Sunday","Determines whether the transition produces growth or decline.",["Institutional Health","Leadership Transfer","Community Formation","Trust Building","Future Setting"]),
    (20,"#3a6a7a","Justice","Justice / Reconciliation Sunday","Highest formation stakes and lowest pastor comfort.",["Formation Depth","Cultural Witness","Community Integrity","Prophetic Voice","Discipleship Test"]),
    (21,"var(--gen)","Anniversary","Church Anniversary Sunday","Connects the current congregation to every congregation that came before.",["Identity Formation","Legacy Connection","Vision Renewal","Community Pride","Historical Witness"]),
    (22,"var(--bap)","Formation","Membership / Covenant Sunday","Moves attenders into belonging. High membership = high volunteer engagement and giving.",["Belonging Formation","Ownership Culture","Volunteer Pipeline","Giving Correlation","Retention"]),
    (23,"var(--cap)","Building","Groundbreaking / Dedication Sunday","Highest communal pride and physical formation intensity.",["Faith Milestone","Communal Vision","Campaign Momentum","Physical Formation","Pride"]),
    (24,"#3a6a7a","Seasonal","Father's Day Sunday","Highest male attendance percentage of the year.",["Male Attendance Peak","Family Formation","Leadership Pipeline","Generational Impact","Return Catalyst"]),
    (25,"var(--gen)","Formation","Commissioning Sunday (Year End)","Closes the formation year and commissions the congregation into the next one.",["Year Review","Formation Summary","Next Year Vision","Community Celebration","Launch Prep"]),
]

# ── UNIVERSAL TOP 10 ────────────────────────────────────────────
UNIVERSAL = [
    (1,"Prayer Cover — The Infrastructure That Goes Before Everything","Nothing multiplies a flagship Sunday more reliably than a congregation that has been praying for it for six weeks. Not the pastor praying. The congregation praying — specifically, persistently, with names of people they are believing will be there. Recruit 50 people to pray for 50 specific people for 6 weeks. The results are not explainable without it.","Six weeks out: form the prayer team. Five weeks out: distribute the prayer cards. Sunday: the prayer team prays during the service. One week after: collect testimonies.","Multiplication",True),
    (2,"Personal Invitation Culture — Activated Six Weeks Out","The single highest-impact behavior available to every congregation member is the personal invitation. Research consistently shows that 80% of people not in a church would come if personally invited. The congregation that activates personal invitation six weeks before a flagship Sunday produces 30–50% higher attendance.","Six weeks out: preach the invitation culture. Four weeks out: give invitation cards with the date. Two weeks out: accountability check from the pulpit.","Engagement",False),
    (3,"Communication Cascade — Every Channel, Every Week, Six Weeks","The congregation that hears about a significant Sunday once forgets. The congregation that hears about it six times — from six different channels, with six different angles of the same story — shows up and brings someone. Week 1: announcement. Week 2: story. Week 3: testimony. Week 4: specific invitation. Week 5: practical preparation. Week 6: final call.","Build the six-week communication calendar in one session. Execute without deviation. Each week gets a different angle on the same story.","Engagement",False),
    (4,"Response Infrastructure — Built Before the Sermon Is Written","The most common reason a significant Sunday underperforms is that the response infrastructure was not ready. The communication card designed Friday. The small group sheet that ran out. The prayer team not positioned. Every mechanism for capturing and following up on every response must be designed, tested, and staffed before the sermon is written.","Four weeks out: design every response mechanism. Three weeks out: train every volunteer who will staff it. Two weeks out: test the follow-up sequence.","Retention",False),
    (5,"Volunteer Mobilization — Recruited and Trained Four Weeks Out","Every flagship Sunday requires more people than a regular Sunday. The congregation that recruits Thursday is the congregation that gets whoever is available. Four weeks out gets the best people for the most important roles. For every 100 people expected, recruit and train one volunteer.","Four weeks out: identify every role. Three weeks out: recruit by name, not by general announcement. Two weeks out: train specifically. Sunday: brief every volunteer 30 minutes before.","Mobilization",False),
    (6,"The Follow-Up System — 48-Hour Window is Non-Negotiable","Every person who responds to a significant Sunday has a formation window of 48 hours in which follow-up reinforces the decision with 3× the impact it would have a week later. The 48-hour follow-up system is not an administrative nicety. It is the mechanism that converts Sunday moments into formation trajectories.","Build the follow-up sequence before the Sunday. Assign a person to every response card category. Guarantee every first-time guest a personal contact within 24 hours. Every commitment card followed up within 48 hours.","Retention",False),
    (7,"Testimony Integration — Three Stories That Do More Than Any Sermon","The three minutes a congregation member spends telling their own transformation story does more formation work than 30 minutes of the best sermon. Every flagship Sunday should include at least one testimony directly connected to what the Sunday is about. Recruited, coached, and positioned before the response invitation — not after it.","Six weeks out: identify the testimony. Four weeks out: coaching interview. Two weeks out: final rehearsal. Sunday: testimony positioned before the response invitation.","Multiplication",False),
    (8,"Small Group Connection — The Sunday That Fills the Groups","Every flagship Sunday is a small group recruitment opportunity. Moving people from Sunday to Thursday community multiplies formation impact by a factor of five. The connection pathway — with a specific name, leader, meeting time — must be as clear and frictionless as possible.","Design the connection pathway before the Sunday. Have group leaders present and identifiable. Use the communication card for small group signup. Follow up every group interest card within 24 hours.","Multiplication",False),
    (9,"Leadership Development — Using the Sunday to Form the Next Generation","Every flagship Sunday is a formation laboratory for the leaders who will run the next flagship Sunday. The team that debriefs every flagship Sunday produces leaders who improve every subsequent Sunday. Invite apprentices into the preparation process, not just the execution.","Six weeks out: identify leaders who will apprentice in the preparation. Each week: debrief with the apprentice team. One week after: conduct the full post-Sunday debrief with every volunteer.","Leadership Dev",False),
    (10,"The Formation Arc — Connecting the Sunday to What Comes Next","The flagship Sunday that does not connect to a formation arc — 7-day journey, 6-week series, 40-day campaign, small group study — has produced a peak experience. Peak experiences are not formation. Formation is the daily practice that follows the peak. Announce the next step from the pulpit, in the bulletin, and on the response card.","Design the formation arc before designing the Sunday service. The sermon is the entry point to the arc, not the whole arc. Announce next step from the pulpit, in the bulletin, on the response card.","Formation",False),
]

# ── GEN SUNDAY TOP 10 ────────────────────────────────────────────
GEN_TOP10 = [
    (1,"Preach Formation, Not Fundraising — The Entire Series","The congregation that arrives at Generosity Sunday having heard six weeks of formation preaching about what generosity does to the giver's soul gives from conviction. Every week: one truth about what holding tightly to money does to a person. One truth about what releasing it does. The anthropology of generosity is the campaign.","Begin the formation series six weeks before Commitment Sunday. Week 1: theology. Week 2: the giver's soul. Week 3: testimony. Week 4: specific invitation. Week 5: next generation. Week 6: harvest.","Formation",True),
    (2,"The Leaders Give First — Before the Congregation Is Asked","The single most powerful generosity statement a congregation can make is that the elders, deacons, and staff have already committed before asking anyone else. Not a matching gift strategy. A theology of leadership by example. The congregation that hears 'your leaders have already committed' responds from gratitude rather than obligation.","Four weeks out: meet with the governing board and ask for their commitment first. Three weeks out: announce the leadership commitment percentage from the pulpit without dollar amounts.","Generosity",False),
    (3,"The Testimony of the First-Time Tither — Not the Major Donor","The most formation-producing testimony is not the major donor who gives easily. It is the first-time tither who gave what they could not afford and discovered they could. This testimony is available to every person in the congregation — unlike the major donor story, which most people believe is not for them.","Recruit the first-time tither testimony four weeks out. Coach it to 3 minutes: what I believed about money, what I decided, what happened. Position directly before the commitment invitation.","Engagement",False),
    (4,"The Personal Pastor Letter — Handwritten to the Top 20%","Twenty percent of the congregation typically accounts for eighty percent of the giving. A handwritten letter from the pastor to every significant giver, received two weeks before Commitment Sunday, produces a giving response that no pulpit appeal can match. Not because of the content. Because of the relationship it demonstrates.","Three weeks out: write 20 personal letters to the top 20 giving households. Handwritten. Specific to each family — their giving history, their family. This takes 3 hours and multiplies the campaign outcome more than any other single act.","Generosity",False),
    (5,"The Generosity Devotional — 21 Days Before the Sunday","The congregation that has been reading a daily generosity devotional for three weeks before Commitment Sunday has been formed before they are asked to give. One thought per day. One Scripture. One reflection question. One practice. Not a campaign tool. A formation instrument. Distributed to every household.","Three weeks out: distribute the 21-day generosity devotional — in print, via app, via daily text. Use it to build the person who will make the ask unnecessary.","Formation",False),
    (6,"The Family Generosity Conversation — Parents and Children Together","The congregation that gives most generously across generations is the congregation whose parents talked about giving with their children. The family generosity conversation — structured, simple, age-appropriate — plants the formation that a stewardship sermon cannot reach.","Four weeks out: distribute the family generosity conversation guide. Two weeks out: preach to parents about talking to their children about money. Commitment Sunday: invite families to complete the pledge card together.","Multiplication",False),
    (7,"The Legacy Giving Conversation — A Separate Dinner for 55+ Families","The congregation's highest untapped generosity resource is the planned gift. The high-capacity family whose estate has never been asked about will not respond to a stewardship sermon. They will respond to a dinner, a conversation, an estate attorney present, and a pastor who shows up.","Five weeks out: host a dinner for families over 55 with higher capacity. Bring a Christian estate attorney. Have the pastor lead the conversation. Do not make an ask at the dinner. Schedule individual follow-up conversations.","Generosity",False),
    (8,"The Matching Gift — Announced Three Weeks Out","A matching gift secured from a high-capacity family three weeks before Commitment Sunday doubles the motivational energy of the campaign without doubling the ask. Not primarily a financial strategy. A declaration of faith by one family and an invitation to partnership for every other family.","Secure the matching commitment six weeks out. Announce it three weeks out with a story — not just a number. 'One family in this congregation believes so strongly in what God is doing here that they will match every dollar given on Commitment Sunday up to [amount].'","Generosity",False),
    (9,"The Commitment Card as Worship — Not Administration","The commitment card filled out while the congregation sings, placed in the offering plate as worship, prayed over by the elders before the service ends, is a different act than the card that is tallied and reported. The theology of the commitment card determines whether it produces formation or transaction.","Design the commitment moment as worship, not administration. Song selection, elder prayer over the cards, physical placement as offering — every element communicates this is a sacred act.","Formation",False),
    (10,"The 48-Hour Celebration — Report What God Did","The email that goes out within 48 hours reporting what the congregation gave — not in relief that the budget is covered, but in awe at what God did through his people — is the most formation-producing communication the stewardship season produces. The congregation that hears this is the congregation that gives again next year.","Draft the celebration email before Commitment Sunday. Have the template ready. Fill in the numbers Monday morning and send by Monday noon. Preach the celebration the following Sunday.","Retention",False),
]

# ── CAP CAMPAIGN TOP 10 ─────────────────────────────────────────
CAP_TOP10 = [
    (1,"The Quiet Phase — 40–60% Committed Before the Public Launch","The capital campaign that announces its goal before securing 40–60% of the goal from the top 15–20% of givers has started with a momentum deficit. The quiet phase — six to eight weeks of private, personal conversations with high-capacity families — produces the announcement that says 'before we asked everyone, this many said yes.'","Eight weeks out: identify the top 20% of givers. Six weeks out: begin quiet phase conversations. Secure 40–60% of the campaign goal before the public launch Sunday. Announce the quiet phase total at the launch.","Generosity",True),
    (2,"The Mission Case — Build the Why Before the What","The congregation that understands what the building enables — more children formed, more families served, more community reached — gives to the mission. The congregation that understands only what the building costs gives to the construction. The mission case document is the most important piece of capital campaign communication.","Six weeks out: write the mission case. One page. Why we build: the ministry the building enables. One story that illustrates it. One vision statement that names what it produces. Distribute in every format before the public launch.","Engagement",False),
    (3,"The Testimonies of the Life Changed in the Current Space","The testimony that produces the most capital campaign generosity is not the vision for the new building. It is the story of the life changed in the current building — and why the new building would have changed even more. The person baptized in the current sanctuary. The child whose parents first heard the gospel in the fellowship hall.","Five weeks out: collect five testimonies of life change in the current facility. Record on video. Release one per week in the five weeks before the launch. Use the most powerful in the launch service.","Engagement",False),
    (4,"The Three-Year Pledge Framework — Monthly, Not Total","The capital campaign that helps the congregation calculate a monthly amount produces higher completion rates than the campaign that asks for a total amount. Monthly feels manageable. The pledge card that says '$50/month for 36 months — your three-year gift is $1,800' converts more pledges than '$1,800 over three years.'","Design the commitment card around a monthly amount. Train every conversation around the monthly figure. The ask is never 'how much can you give?' The ask is 'what could you commit per month for 36 months that would stretch you without breaking you?'","Generosity",False),
    (5,"The Children and Youth Campaign — Building for the Next Generation","The capital campaign that includes the children and youth as active participants — not spectators — produces the highest family giving response. The family that watches their child contribute their own gift gives more than the family that gives alone.","Five weeks out: design a children's and youth campaign component. Children earn money by doing chores. Youth participate in a service project whose proceeds go to the campaign. Children bring their gifts on Launch Sunday.","Multiplication",False),
    (6,"The Architect's Rendering — What People Are Giving To","The congregation that can see what they are giving to gives more than the congregation that is giving to a concept. The architect's rendering placed at every entrance, printed in the bulletin, shown on every screen makes the vision tangible before it is real.","Four weeks out: display the architect's rendering in every available space. Create a scale model if budget allows. Commission a video walkthrough of the future space. Make the vision visible before the launch Sunday.","Engagement",False),
    (7,"The Town Hall — Every Question Answered Before the Ask","The congregation that has unanswered questions about the capital campaign gives less than the congregation that has had every question answered. The pre-launch town hall is not optional. It is the formation meeting that converts skeptics into champions.","Three weeks out: host an all-congregation town hall meeting. The senior pastor, executive pastor, board chair, and architect are all present. Every question is answered. No question is deflected. The meeting ends with prayer.","Engagement",False),
    (8,"The Legacy Naming Opportunity — For High-Capacity Families","The well-executed capital campaign includes a limited number of naming opportunities — the children's wing, the prayer room, the fellowship hall — reserved for families whose gifts at a specific level make a permanent statement of faith about what the building is for.","Six weeks out: design the naming opportunity tiers. Identify the families for each tier. Have the conversations in the quiet phase. Announce the named spaces on Launch Sunday as a celebration of what God has already done through those families.","Generosity",False),
    (9,"The Matching Gift — Announced at the Launch","The capital campaign matching gift announced at the Launch Sunday changes the congregation's sense of possibility. 'One family has committed to match every gift given today up to $250,000' converts the launch Sunday into the highest single-day giving event in the campaign.","Secure the matching commitment in the quiet phase. Do not announce it before the Launch Sunday. Use it as the final motivation at the commitment moment.","Generosity",False),
    (10,"The Groundbreaking as Celebration — Not Construction Notice","The groundbreaking ceremony six to nine months after the campaign launch is the most emotionally significant formation event of the campaign. The congregation that stands on the dirt, holding a shovel, singing, is the congregation that keeps its pledge because it was there when the ground was turned.","Plan the groundbreaking as a full worship service — outside, at the site, with the congregation gathered. Communion, testimony, prayer, song. The groundbreaking is not construction. It is consecration.","Retention",False),
]

# ── EASTER TOP 10 ───────────────────────────────────────────────
EAST_TOP10 = [
    (1,"The 50-for-50 Prayer Strategy — Activated Six Weeks Out","The most reproducible Easter outreach strategy in church history: recruit 50 people to pray for 50 specific people every day for 50 days before Easter Sunday. Not to invite them — to pray for them first. The congregation that prays specifically for specific people for six weeks before Easter sees attendance numbers that the best production cannot produce.","Six weeks out: recruit 50 people. Give each person a card with space for five names. Collect the cards. Pray for every name in every service for six weeks. Invite after four weeks of prayer — not before.","Multiplication",True),
    (2,"Baptism Sunday the Week After Easter — Announced from the Easter Pulpit","The single most formation-producing decision a congregation can make for Easter is to announce Baptism Sunday for the following week from the Easter pulpit. The person who comes to Easter and hears 'next Sunday, we will baptize everyone who has decided to follow Jesus — including anyone who makes that decision today' has been given a specific, accessible, immediate next step.","Announce Baptism Sunday from the Easter pulpit before the sermon. 'Next week, this time, this room, we will baptize every person who has decided to follow Jesus.' Then preach the resurrection. Watch what happens.","Multiplication",False),
    (3,"The Guest Experience — Designed as a Formation System","The Easter guest who has an extraordinary experience — parking, greeting, children's check-in, seat, service, follow-up — returns. The guest experience is not hospitality. It is formation infrastructure. Every touchpoint communicates whether this congregation is for people who are already formed or for people who are still becoming.","Four weeks out: audit every guest experience touchpoint from parking to post-service follow-up. Recruit and train a guest experience team double the normal size. Brief every regular attender on how to treat a guest.","Retention",False),
    (4,"The Personal Invitation — With a Physical Card","Research consistently shows that the most effective Easter outreach strategy is the personal invitation from one person who knows the guest. The physical card — the size of a business card, with the date, time, and address — is the instrument of the personal invitation. The congregation that has invitation cards four weeks before Easter has four weeks to invite.","Four weeks out: distribute Easter invitation cards to every family — 5 cards per family minimum. Two weeks out: accountability from the pulpit: 'How many of you have given your cards to someone? Stand.' The physical card converts intention into action.","Engagement",False),
    (5,"The Post-Easter Formation Arc — Announced Before They Leave","The most common Easter failure is producing a peak experience with no formation arc attached. The congregation that hears from the Easter pulpit what begins Monday — the 7-Day Resurrection Journey, the post-Easter series, the small group launch — has been given a reason to return. The congregation that hears only 'see you next Easter' returns at exactly that rate.","Design the post-Easter formation arc before designing the Easter service. Announce it from the Easter pulpit. Distribute the 7-Day Resurrection Journey guide at the door as guests leave. Make the next step as accessible and compelling as the service itself.","Retention",False),
    (6,"The Holy Week Formation Arc — Not Just Easter Sunday","The congregation that participates in Holy Week — Palm Sunday, Maundy Thursday, Good Friday, Easter — is the congregation most transformed by Easter. The transformation compounds across the week. The Good Friday service that sits in darkness, the Easter Sunday that greets what came before it — these are the formation experiences that make Easter the culmination of something rather than the beginning of nothing.","Build the full Holy Week calendar six weeks out. Promote every service as a formation experience, not a program addition. The congregation that experiences Maundy Thursday and Good Friday arrives at Easter Sunday with a readiness to receive that the congregation that only attends Easter cannot have.","Formation",False),
    (7,"The Children's Easter Experience — Designed for the Unchurched Child","The Easter guest brings children. The unchurched child who has an extraordinary Easter children's experience becomes the primary reason the unchurched family returns. The children's Easter experience is the formation event with the highest retention impact of any Easter element.","Four weeks out: design the children's Easter experience with the same intentionality as the adult service. Four weeks out: recruit and train children's Easter volunteers. One week out: brief every children's volunteer on the unchurched child experience.","Retention",False),
    (8,"The Overflow Plan — Faith That Expects More Than the Room Holds","The congregation that plans for overflow is the congregation that sees God fill the room. The congregation that does not plan for overflow is the congregation that turns people away and loses them. The overflow plan is not logistics. It is a declaration of faith.","Five weeks out: design the overflow plan. Four weeks out: recruit overflow volunteers. Two weeks out: communicate the overflow options to the congregation. Sunday: overflow is a celebration, not a problem.","Engagement",False),
    (9,"The 48-Hour Guest Follow-Up — Before They Forget They Were There","The Easter guest who receives a personal follow-up within 48 hours — not a generic mass email, a specific contact from a specific person — is three times more likely to return. The follow-up is not marketing. It is pastoral care for a person who just had a significant experience.","Design the follow-up sequence before Easter. Collect communication cards during the service. Assign specific follow-up to specific volunteers. Monday 8am: begin the follow-up sequence. Every first-time guest receives a personal contact by Tuesday.","Retention",False),
    (10,"The Easter Giving Moment — Not an Afterthought","Easter is the second-highest single-day giving opportunity of the year. The Easter offering moment — positioned with intention, framed as an act of gratitude for the resurrection, with a specific mission it funds — is the generosity formation moment that shapes the giving culture for the rest of the year.","Design the Easter offering moment as a worship act. Frame it as a response to the resurrection: 'Because he rose, we give.' Designate a specific mission that the Easter offering funds. Announce what the Easter offering will do.","Generosity",False),
]

# ── BAPTISM TOP 10 ──────────────────────────────────────────────
BAP_TOP10 = [
    (1,"The Story Before the Water — Always","The baptism that is preceded by the candidate's story produces more faith in the congregation and more resolve in the candidate than the baptism that goes directly to the water. Three minutes. What my life was before. What happened. What is different now. The story is not preparation for the baptism. The story is the formation event. The water is the public declaration of the story.","Four weeks out: collect the story from every candidate. Coach it to three minutes: before, what happened, after. Never more than three minutes. Never less than one minute. Position in the service so the congregation is already in tears before the candidate gets in the water.","Engagement",True),
    (2,"Announce the Next Baptism Sunday the Moment This One Ends","The single most reproducible baptism strategy is the announcement from the baptism pulpit: 'Our next Baptism Sunday is [date]. If you have been thinking about baptism, this is your invitation. See me after the service.' The congregation that hears this announcement while still moved by the baptisms they just witnessed produces the most baptism candidates for the next Sunday.","Design the announcement before the Sunday. Have the pastor deliver it immediately after the final baptism, while the congregation is still standing and celebrating. The next Baptism Sunday should be within 60–90 days.","Multiplication",False),
    (3,"The Prayer Team — One Person Assigned to Each Candidate","The candidate who is prayed over by name, personally, by a specific congregation member assigned to them for four weeks, arrives at their baptism differently than the candidate who comes alone. The prayer team is the congregation's expression that this person's decision matters to the whole body.","Four weeks out: assign one prayer team member to each candidate. The assignment includes: weekly prayer for the candidate, one personal conversation, and presence at the baptism positioned near the family.","Formation",False),
    (4,"The Family Invitation — Personal and Specific","The baptism of an adult family member is the highest-impact outreach moment available to any congregation. Every unchurched family member who comes to witness a baptism is present for the most emotionally compelling worship service the church produces. The candidate's family must be personally, specifically, individually invited.","Three weeks out: obtain the list of every family member and close friend of every candidate. Assign a specific person to personally contact each family member with a personal invitation from the pastor.","Engagement",False),
    (5,"The Congregation's Role — Taught Before the Sunday","The congregation that does not know how to celebrate a baptism watches it. The congregation that has been taught — that this is the moment to stand, to weep, to cheer, to affirm, that their response is part of the formation of the person being baptized — participates. Participation produces more baptisms. Observation does not.","The Sunday before Baptism Sunday: teach the congregation their role. 'When [name] goes under the water, I am going to invite you to stand and say their name aloud. Here is why that matters to them and to God.'","Formation",False),
    (6,"The Baptism Preparation Class — Theology Before the Water","The candidate who understands what baptism means theologically arrives at the water with conviction, not just emotion. The preparation class is not a hoop to jump through. It is the formation event that makes the baptism the public declaration of a private conviction rather than a public experience of a private sentiment.","Three weeks out: schedule the baptism preparation class. One session, 90 minutes, led by the pastor. Cover: what baptism is, what it is not, what you are declaring, what the congregation is promising. Invite the candidates' families to attend.","Formation",False),
    (7,"The Photography and Video — As Ministry, Not Production","The baptism photograph that is in the candidate's home within one week of the Sunday is the most enduring formation artifact the church produces. It is on the refrigerator for years. It is the tangible reminder of a decision that might otherwise fade.","Recruit a photographer and videographer specifically for Baptism Sunday. Budget for printing and delivering a photograph to each candidate's home within one week. The photograph costs $15 to print. It is the most formation-dense $15 the church spends.","Retention",False),
    (8,"The Post-Baptism Pathway — Announced the Same Day","The newly baptized person has the highest formation motivation of any person in the congregation — for approximately 72 hours after the baptism. The church that has a specific, accessible, compelling next step ready converts that motivation into formation. The church that has nothing loses it.","Design the post-baptism pathway before the Sunday. The pathway includes: a specific small group connected to the candidate, a meeting with the pastor or a formation coach within one week, the 7-Day post-baptism devotional distributed at the baptism.","Retention",False),
    (9,"The Baptism Testimony Shared Beyond the Sunday","The baptism story shared on video, on social media, with the congregation's network extends the formation impact beyond the room. The unchurched person who sees a 90-second baptism testimony video in their social media feed has received the most compelling outreach the church can produce.","With the candidate's permission, record the baptism story in a 90-second format. Share on all church social media channels the Monday after Baptism Sunday. Personal shares by congregation members produce more impact than institutional posts.","Multiplication",False),
    (10,"Schedule Baptism Sundays Four Times Per Year — Minimum","The church that baptizes once per year produces a trickle. The church that baptizes four times per year produces a river. The frequency of the invitation determines the frequency of the response. Every person considering baptism needs to know the next opportunity is within 90 days, not next year.","Set four Baptism Sundays on the annual calendar on January 1. Announce them in the new year vision message. Repeat the announcement from the pulpit every six to eight weeks throughout the year.","Multiplication",False),
]

# ── 7 GOVERNING PRINCIPLES ─────────────────────────────────────
PRINCIPLES = [
    ("I","var(--gold)","Prayer Is the Foundation, Not Preparation's Companion","No preparation strategy in this playbook outperforms prayer. The churches that see God move exponentially on flagship Sundays trace every movement to a prayer infrastructure built well before the production was designed. Prayer is not the spiritual wrapper around the practical work. It is the practical work."),
    ("II","var(--gen)","The Sermon Is the Tip of the Iceberg","The congregation sees the sermon. They do not see the six weeks of prayer, communication, volunteer training, follow-up infrastructure, and formation connection that make the sermon the beginning of something rather than the end of an hour. The iceberg produces the results. The tip receives the credit."),
    ("III","var(--east)","Every Significant Sunday Reproduces Itself — or Does Not","The Baptism Sunday celebrated with full formation infrastructure produces the next baptism. The Easter Sunday with a compelling post-Easter formation arc produces the congregation that brings someone next Easter. The Generosity Sunday with a 48-hour follow-up produces the congregation that gives more generously next year. Formation is reproductive or it is not formation."),
    ("IV","var(--cap)","The Response Infrastructure Is More Important Than the Sermon","The best sermon ever preached in a congregation with no response infrastructure produced less transformation than a mediocre sermon with a fully staffed response system. The communication card, the small group signup, the follow-up system — these are not administrative tools. They are formation mechanisms."),
    ("V","var(--bap)","Personal Is Always More Powerful Than Institutional","The personal invitation outperforms the church mailer by a factor of ten. The handwritten note outperforms the email blast by a factor of five. The personal follow-up phone call outperforms the automated text by a factor of three. Scale the personal. Never substitute the institutional for it."),
    ("VI","#6a7a3a","The Story Does What the Sermon Cannot","The three-minute testimony by a congregation member produces formation that the thirty-minute sermon cannot replicate. The story is not illustration. It is evidence. Evidence that the gospel does what it promises, in this congregation, to people the audience already knows."),
    ("VII","#3a6a7a","The Sunday Is the Door, Not the Room","Every flagship Sunday is the beginning of a formation arc, not the formation arc itself. The sermon is the door. The 7-day journey is the hallway. The small group is the room. The 40-day campaign is where formation happens."),
]

def make_week_rows(cols):
    return "".join(cols)

# BUILD GEN COUNTDOWN
G_CD = [
    make_week("Week 6",["★ Launch the prayer team — 50 people praying for 50 people","Begin the generosity formation devotional","Announce the series arc from the pulpit","Distribute personal invitation cards","Brief all staff on campaign vision"]),
    make_week("Week 5",["★ Preach Generosity Week 1 — Theology first","Share first testimony: why I give","Send handwritten notes from pastor to top 20 givers","Recruit small group leaders for campaign connection"]),
    make_week("Week 4",["★ Generosity Week 2 — The formation of the giver","Launch the 7-Day Generosity devotional","Conduct family generosity conversation training","Mail the stewardship letter with pledge card"]),
    make_week("Week 3",["★ Generosity Week 3 — Testimony Sunday","First-time tither testimony from pulpit","Deacon and elder give first — before congregation","Host generosity conversation dinner for key families"]),
    make_week("Week 2",["★ Generosity Week 4 — The specific invitation","Finalize Commitment Sunday response infrastructure","Train all ushers and response team","Send commitment card preview with personal pastor note","Host legacy giving conversation for 55+ families"]),
    make_week("Week 1",["★ Commitment Sunday — Harvest day preparation","Response card and pledge infrastructure operational","Testimony positioned before the invitation","Prayer team deployed during the service"]),
    make_week("SUNDAY",["★ The Harvest Sunday","Every element designed for response","Testimony before the invitation","Every response card followed up by Tuesday","Text all responders by Monday 9am","Celebrate what was planted six weeks ago"],sunday=True,color="var(--gen)"),
]

# BUILD CAPITAL COUNTDOWN
C_CD = [
    make_week("Week 6",["★ Campaign case statement complete","Quiet phase conversations begin with top 25 families","Prayer team commissioned for campaign","Architect's rendering available for display"]),
    make_week("Week 5",["★ Quiet phase — leadership commitments","Host dinner for top giving families","Share the mission case: why we build","Early commitment testimonies recorded"]),
    make_week("Week 4",["★ Quiet phase closes","Announce to congregation: quiet phase exceeded X%","Build pre-launch momentum — one story per day","Distribute campaign devotional to all households"]),
    make_week("Week 3",["★ Pre-launch momentum building","Campaign devotional in daily use","Testimony videos released — one per day","Town hall meeting: answer every question","Children's and youth campaign components launch"]),
    make_week("Week 2",["★ Final launch preparation","Response infrastructure tested and staffed","Commitment card design finalized","All volunteers briefed and positioned"]),
    make_week("Week 1",["★ Launch week","Daily prayer and fasting option offered","Final testimonies distributed","One personal pastor contact per top-50 family","Venue prepared for maximum visual impact"]),
    make_week("SUNDAY",["★ Capital Campaign Launch Sunday","Vision statement from every elder","Key testimony: 'what this building enables in my family'","Commitment card as worship moment","Quiet phase totals announced from pulpit","Matching gift announced"],sunday=True,color="var(--cap)"),
]

# BUILD EASTER COUNTDOWN
E_CD = [
    make_week("Week 6",["★ 50-for-50 prayer launch: 50 people pray for 50 specific people","Easter invitation cards distributed to every family","Holy Week schedule announced","Baptism Sunday (day after Easter) announced"]),
    make_week("Week 5",["★ Personal invitation week: every family equipped","Lenten devotional launched for congregation","Guest follow-up infrastructure design begins","Video invite distributed for sharing"]),
    make_week("Week 4 (Palm Sunday)",["★ First catalytic Sunday of Holy Week","Congregation invited to read Passion narrative daily","Baptism candidates contacted and coached","Easter service details finalized","Guest experience team training begins"]),
    make_week("Week 3 (Holy Week)",["★ Holy Week formation arc","Wednesday night Tenebrae service","Maundy Thursday footwashing and communion","Good Friday service","★ Every service communicates Easter invitation","★ Baptism Sunday preview announced"]),
    make_week("Week 2",["★ Final Easter preparation","All volunteer roles confirmed and briefed","Overflow preparation finalized","Guest follow-up sequence drafted and ready","Communication card designed and printed"]),
    make_week("Week 1",["★ Easter week","Daily prayer and fasting for specific people","Personal pastor contacts: 20 specific families","All response infrastructure tested","Text blast: bring someone Sunday"]),
    make_week("SUNDAY",["★ Easter Sunday","Maximum greeting team deployed","Multiple service options if needed","Baptism announced for following Sunday","Communication card in every seat","Post-Easter series announced from pulpit","★ 48-hour follow-up system activated Monday 8am"],sunday=True,color="var(--east)"),
]

# BUILD BAPTISM COUNTDOWN
B_CD = [
    make_week("Week 4",["★ Baptism candidates identified and contacted","Personal interview with each candidate begins","Congregation invited to prayer for candidates","Baptism Sunday announced from pulpit","Story collection from each candidate begins"]),
    make_week("Week 3",["★ Candidate stories recorded (video or written)","Prayer team assigned to each candidate","Family and friends of candidates personally invited","Baptism preparation class scheduled","Stories shared in service — building toward Sunday"]),
    make_week("Week 2",["★ Baptism preparation class — candidates + their guests","Share one story from each candidate in service","Personal invitation push: 'bring someone for their baptism'","Logistics confirmed: pool, team, photography, video","Congregation briefed: how to celebrate"]),
    make_week("Week 1",["★ Final preparation week","Personal pastor conversation with each candidate","Every candidate's family and friends directly contacted","Story preview shared on all channels","Service order finalized: stories before the water"]),
    make_week("SUNDAY",["★ Baptism Sunday","Stories told before the water","Family positioned in front row","Prayer team prays over each candidate","Congregation invited to respond after baptisms","★ Post-baptism pathway announced","★ Next Baptism Sunday announced from pulpit"],sunday=True,color="var(--bap)"),
]

# ── BUILD HTML ─────────────────────────────────────────────────────────
def top10_rows(items, color):
    return "".join(rank(i+1, title, desc, action, roi, color, i==0) for i,(n,title,desc,action,roi,top) in enumerate(items))

dir1_html = "".join(dir_card(r,c,cat,title,why,m,mega=True) for r,c,cat,title,why,m,_ in DIR_TIER1)
dir2_html = "".join(dir_card(r,c,cat,title,why,m) for r,c,cat,title,why,m in DIR_TIER2)
univ_html = "".join(rank(i+1,title,desc,action,roi,"var(--gold-dk)",i==0) for i,(n,title,desc,action,roi,top) in enumerate(UNIVERSAL))
gen_html = "".join(rank(i+1,title,desc,action,roi,"var(--gen)",i==0) for i,(n,title,desc,action,roi,top) in enumerate(GEN_TOP10))
cap_html = "".join(rank(i+1,title,desc,action,roi,"var(--cap)",i==0) for i,(n,title,desc,action,roi,top) in enumerate(CAP_TOP10))
east_html = "".join(rank(i+1,title,desc,action,roi,"var(--east)",i==0) for i,(n,title,desc,action,roi,top) in enumerate(EAST_TOP10))
bap_html = "".join(rank(i+1,title,desc,action,roi,"var(--bap)",i==0) for i,(n,title,desc,action,roi,top) in enumerate(BAP_TOP10))
prin_html = "".join(principle(n,c,t,b) for n,c,t,b in PRINCIPLES)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Top 25 Flagship Sundays — Preparation Playbook · Lifetogether</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="page">

<section class="cover">
  <div class="cover-glow"></div>
  <div class="cover-top">
    <span class="cover-logo">Lifetogether</span>
    <span class="cover-tag">The Preparation Playbook · 2026 Edition</span>
  </div>
  <div class="cover-body">
    <p class="cover-ey">Top 25 Flagship Sundays · Top 10 Ranked Strategies Each · 4–6 Week Countdown</p>
    <h1 class="cover-h1">The Sunday<br>That<br><em>Changes</em><br>Everything.</h1>
    <div class="cover-rule"><div class="cover-rule-dot"></div><div class="cover-rule-line"></div></div>
    <p class="cover-sub">The proven 4–6 week preparation system for the 25 most significant Sundays a congregation will ever experience — ranked, sequenced, and built around the single conviction that the Sunday that changes the most lives is the Sunday prepared for most intentionally.</p>
    <div class="cover-stats">
      <div class="cstat"><span class="cstat-n">25</span><span class="cstat-l">Flagship Sundays</span></div>
      <div class="cstat"><span class="cstat-n">10</span><span class="cstat-l">Ranked Strategies Each</span></div>
      <div class="cstat"><span class="cstat-n">4–6</span><span class="cstat-l">Week Countdown</span></div>
      <div class="cstat"><span class="cstat-n">4</span><span class="cstat-l">Deep Dive Playbooks</span></div>
      <div class="cstat"><span class="cstat-n">100%</span><span class="cstat-l">Proven Practice</span></div>
      <div class="cstat"><span class="cstat-n">∞</span><span class="cstat-l">Formation Impact</span></div>
    </div>
  </div>
</section>

<div class="pull" style="margin-top:48px;">
  <p>"The Sunday that changes the most lives is never the one prepared for on Thursday. It is the one the pastor began preparing for six weeks before anyone else knew it was coming — in prayer, in communication, in volunteer mobilization, in small group connection, in follow-up infrastructure. The sermon is the visible tip of an invisible iceberg. The iceberg is preparation."</p>
  <span>Brett Eastman · Founder, Lifetogether · 25 Years · 500+ Church Relationships · 50M+ Campaigns</span>
</div>
<div class="hdiv"></div>

<!-- TOP 25 DIRECTORY -->
<section class="sect-intro">
  <p class="si-kk" style="color:var(--gold-dk);">The Complete Directory</p>
  <h2 class="si-h2">The <em>Top 25 Flagship Sundays</em> — Ranked by Formation Impact</h2>
  <p class="si-sub">Ranked by their combined potential for congregational mobilization, life transformation, leadership development, volunteer deployment, generosity response, and disciple multiplication. The ranking assumes a congregation that prepares intentionally — not one that simply shows up.</p>
</section>
<section class="dir">
  <div class="dir-grid">{dir1_html}{dir2_html}</div>
</section>
<div class="hdiv"></div>

<!-- UNIVERSAL TOP 10 -->
<section class="part" style="border-color:var(--gold);">
  <p class="part-kk" style="color:var(--gold-dk);">Universal Preparation System</p>
  <h2 class="part-h2" style="color:var(--ink);">The Top 10 Things That <em>Multiply Every</em> Flagship Sunday</h2>
  <p class="part-sub">These ten preparation practices apply to every flagship Sunday on the calendar — ranked by their impact on congregational mobilization, life transformation, and disciple multiplication. A congregation that executes all ten consistently produces exponential results on every major Sunday.</p>
</section>
<section class="top10-wrap">
  <div class="top10-grid">{univ_html}</div>
</section>
<div class="hdiv"></div>

<!-- DEEP DIVE 1: GENEROSITY -->
<section class="part" style="border-color:var(--gen);">
  <p class="part-kk" style="color:var(--gen);">Deep Dive · Playbook One</p>
  <h2 class="part-h2" style="color:var(--ink);">Generosity Sunday <em>Harvest</em> — The Top 10</h2>
  <div class="part-sub"><p>The Generosity Sunday Harvest is the weekend that closes the stewardship season and invites the congregation's first-fruits response. It is also the most psychologically complex Sunday a pastor preaches — because the congregation arrives suspicious of the motive and the pastor arrives afraid of the ask.</p>
  <p><strong>The fundamental principle:</strong> The congregation that gives most generously on Generosity Sunday has been formed around generosity for six weeks before they arrive. The Sunday is the harvest of six weeks of seed. You cannot harvest what you have not planted.</p></div>
</section>
<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(74,122,80,.08);border-bottom:1px solid rgba(74,122,80,.15);">
    <span style="font-size:20px;">◇</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 6-Week Generosity Sunday Countdown</h3>
  </div>
  <div class="cd-weeks">{"".join(G_CD)}</div>
</div>
<section class="top10-wrap"><div class="top10-grid">{gen_html}</div></section>
<div class="hdiv"></div>

<!-- DEEP DIVE 2: CAPITAL CAMPAIGN -->
<section class="part" style="border-color:var(--cap);">
  <p class="part-kk" style="color:var(--cap);">Deep Dive · Playbook Two</p>
  <h2 class="part-h2" style="color:var(--ink);">Capital Campaign <em>Launch Sunday</em> — The Top 10</h2>
  <div class="part-sub"><p>The Capital Campaign Launch Sunday is the Sunday that determines whether the campaign produces the building or only a portion of it. The congregation that leaves the launch Sunday with conviction about why they are building — not what they are building — is the congregation that gives sacrificially over three years.</p>
  <p><strong>The fundamental principle:</strong> Capital campaigns are not building programs. They are formation programs that produce a building as a byproduct. The congregation formed around the mission the building enables gives to the building. The congregation asked to fund the building gives less generously and stops sooner.</p></div>
</section>
<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(74,90,138,.08);border-bottom:1px solid rgba(74,90,138,.15);">
    <span style="font-size:20px;">🏛</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 6-Week Capital Campaign Launch Countdown</h3>
  </div>
  <div class="cd-weeks">{"".join(C_CD)}</div>
</div>
<section class="top10-wrap"><div class="top10-grid">{cap_html}</div></section>
<div class="hdiv"></div>

<!-- DEEP DIVE 3: EASTER -->
<section class="part" style="border-color:var(--east);">
  <p class="part-kk" style="color:var(--east);">Deep Dive · Playbook Three</p>
  <h2 class="part-h2" style="color:var(--ink);"><em>Easter Outreach</em> Sunday — The Top 10</h2>
  <div class="part-sub"><p>Easter Sunday is the highest-attended Sunday of the year — and the Sunday with the highest percentage of people who will not return the following week unless something specific happens to bring them back. The congregation that treats Easter as its best production Sunday produces an experience. The congregation that treats Easter as its most intentional formation and outreach Sunday produces disciples.</p>
  <p><strong>The fundamental principle:</strong> Easter is not the destination. It is the door. The formation arc that begins the Monday after Easter determines whether the guests who came become the disciples who stay.</p></div>
</section>
<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(138,74,48,.08);border-bottom:1px solid rgba(138,74,48,.15);">
    <span style="font-size:20px;">✝</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 6-Week Easter Outreach Countdown</h3>
  </div>
  <div class="cd-weeks">{"".join(E_CD)}</div>
</div>
<section class="top10-wrap"><div class="top10-grid">{east_html}</div></section>
<div class="hdiv"></div>

<!-- DEEP DIVE 4: BAPTISM -->
<section class="part" style="border-color:var(--bap);">
  <p class="part-kk" style="color:var(--bap);">Deep Dive · Playbook Four</p>
  <h2 class="part-h2" style="color:var(--ink);"><em>Baptism Sunday</em> — The Top 10</h2>
  <div class="part-sub"><p>Baptism Sunday is the most emotionally powerful and formation-dense Sunday in the church year — when it is prepared for. It is also the Sunday most frequently under-prepared for, treated as a logistical event rather than a formation catalyst.</p>
  <p><strong>The fundamental principle:</strong> Baptism Sundays reproduce themselves. The congregation that celebrates one baptism with full formation infrastructure produces the next baptism within 60 days. The congregation that processes baptism as a program item produces baptisms at the rate of program items — rarely and without momentum.</p></div>
</section>
<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(90,74,138,.08);border-bottom:1px solid rgba(90,74,138,.15);">
    <span style="font-size:20px;">💧</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 4-Week Baptism Sunday Countdown</h3>
  </div>
  <div class="cd-weeks">{"".join(B_CD)}</div>
</div>
<section class="top10-wrap"><div class="top10-grid">{bap_html}</div></section>
<div class="hdiv"></div>

<!-- 7 GOVERNING PRINCIPLES -->
<section class="sect-intro">
  <p class="si-kk" style="color:var(--gold-dk);">The Foundation</p>
  <h2 class="si-h2">The 7 <em>Governing Principles</em> Behind Every Flagship Sunday</h2>
  <p class="si-sub">Every preparation strategy in this playbook emerges from seven convictions about how God works through intentional preparation. These are not best practices. They are theological commitments that produce the best practices.</p>
</section>
<section class="principle-wrap">
  <div class="principle-grid">{prin_html}</div>
</section>
<div class="hdiv"></div>

<section class="back">
  <p class="bq">"The Sunday that changes the most lives is the one prepared for with the most prayer, the most intentional communication, the most carefully staffed response infrastructure, and the most compelling formation arc for the Monday that follows. This playbook exists so that every pastor who picks it up walks into their most significant Sundays not hoping for something to happen — but having built the conditions in which God moves."</p>
  <p class="ba">Brett Eastman · Founder, Lifetogether</p>
  <p class="bc"><a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &nbsp;·&nbsp; <a href="https://lifetogether.com">lifetogether.com</a> &nbsp;·&nbsp; 25 Years · 500+ Church Relationships · 50M+ Campaigns</p>
  <div class="lm">Lifetogether</div>
</section>

</div>
</body>
</html>"""

with open('/mnt/user-data/outputs/lifetogether-flagship-sunday-playbook.html','w') as f:
    f.write(HTML)
print(f"Done — {len(HTML):,} chars")
