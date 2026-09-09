# -*- coding: utf-8 -*-
import io
from build_vol4 import BASE, head, esc

V1="catalytic-sundays-easter-christmas.html"
V2="catalytic-sundays-calendar-strategic.html"
V3="catalyst-kit-vol-3.html"
V4="catalytic-sundays-vol-4.html"
V5="catalytic-sundays-vol-5.html"
O1="catalytic-sundays-outlines-vol-1.html"

# (name, anchor, count, note, explainer, experience)
VOLUMES=[
("Volume One &mdash; Easter and Christmas", V1, [
("Resurrection Sunday","c1",20,"Kit built","The one Sunday where the entire claim of Christianity is on the table, in front of the least-churched room a pastor sees all year.","Start in the dark. Open the service with the tomb, not the trumpet &mdash; three minutes of Friday before a single light comes up."),
("Good Friday","c2",20,"","The service that earns Sunday. A church that rushes to hope has nothing to be hopeful about.","End without a benediction. No closing song, no dismissal, no music. Lights down, people leave in silence. Nobody forgets it."),
("Palm Sunday","c3",20,"","Celebration with an edge, and the week that changes everything begins here.","Two processions. Stage the contrast &mdash; Rome's warhorse and a borrowed colt &mdash; and let the congregation choose which parade they are actually in."),
("Holy Week &amp; Maundy Thursday","c4",20,"","The table, the garden, and the long night. Midweek services most churches under-build.","Wash feet. Actually. Basins at the front, staff going first, elders washing the youth. It costs twenty minutes and it is remembered for twenty years."),
("Easter for the Skeptic","c5",20,"","Written for the person dragged in by family who is deciding, around the third song, whether any of this is real.","Take questions. Print index cards in the seats, collect them, and answer three from the platform unfiltered. Nothing signals confidence like that."),
("The Sunday After Easter","c6",20,"","The week attendance drops and the follow-through decides whether Easter mattered at all.","Breakfast on the beach. Serve an actual meal before or after the service and preach John 21 from a table rather than a pulpit."),
("Ash Wednesday &amp; the Road to Lent","c7",20,"","Forty days of preparation that make Resurrection Sunday land like an ending rather than an event.","Ashes and a written thing to lay down. People write one thing on paper, and it is burned to make the ashes for the following year."),
("Easter for the Grieving","c8",20,"","For the people who buried someone this year and cannot sing yet.","A candle table at the back, lit throughout the service, with names written on cards. Name it from the platform in the first two minutes."),
("Christmas Eve","c9",20,"Outlined","The highest-attendance night of the year and the most unchurched crowd a pastor will ever face.","One flame, passed. Kill every light in the building and light the room from a single candle outward. Hold the silence longer than feels comfortable."),
("Christmas Day &amp; Christmas Sunday","c10",20,"","The claim at the center of the season, stated plainly to people who have heard it every year of their lives.","Read the genealogy out loud. All of it, by different voices, before anyone preaches. The messy family tree is the sermon."),
("Advent Sunday Singles","c11",20,"","Each Advent theme built to stand alone for churches that will not run the full series.","Give every household a candle and a card on week one. The service starts at home before it starts in the building."),
("Christmas for the Skeptic","c12",20,"","Your second-biggest guest room of the year, written for the visitor who came for the music.","Say the objections out loud from the platform before they can. Naming the census, the date, and the virgin birth first removes their power."),
("The Characters of the Nativity","c13",20,"","Character-driven messages that work as a series or as standalone Sundays.","Cast it. One person in the congregation embodies each character for ninety seconds &mdash; not a pageant, a monologue, in modern clothes."),
("Blue Christmas","c14",20,"","The fastest-growing service type in American churches, and the one most pastors write from scratch every December.","A separate midweek service, dimly lit, no upbeat music, and permission stated in the first sentence. Advertise it as widely as Christmas Eve."),
("After Christmas &amp; New Year","c15",20,"","The lowest-attendance Sunday of the year, full of the people who will carry the next twelve months.","One word for the year, written on a card, taken home and taped somewhere they will see it in June."),
("The Incarnation","c16",20,"","The theology underneath the season, for churches that want depth rather than warmth.","Read John 1 in three languages, by three people from your own congregation. The Word became flesh in a specific place, to specific people."),
]),
("Volume Two &mdash; Calendar Locks and Strategic Weekends", V2, [
("Mother's Day","c1",100,"5 tracks &middot; Kit built","Third-highest attendance Sunday of the year, and the one most likely to wound the person in row nine.","Name the hard version from the platform before a single flower is handed out. Then have a room staffed and open afterward, announced by name."),
("Father's Day","c2",100,"5 tracks","Lowest-attendance major holiday, highest stakes, because the men in the room are the least likely to return.","Skip the joke. Instead, have three men of three different ages give ninety seconds each on what their father gave them or failed to."),
("Graduation","c3",100,"5 tracks","Three audiences in one service: the graduate, the extended family, and parents quietly grieving.","Commission by name. Every graduate on the platform, church surrounding them, hands on shoulders, and a physical letter from the congregation."),
("End-of-Year Giving","c4",20,"","The last four Sundays of the calendar, when the largest gifts of the year are decided and most churches say nothing.","Show the year first. Two minutes of what last year's giving actually did, with names, before a single word about this year's need."),
("Baptism Sunday","c5",20,"","The clearest evangelistic Sunday available, usually buried at the end of a service.","Baptize outdoors if you can, and make it same-day. Towels, shirts, and a signup table in the lobby with people ready to say yes at 11:40."),
("Baby Dedication &amp; Family Blessing","c6",20,"","Extended family attends who never otherwise walk in, and the congregation makes a promise most of them do not notice making.","The congregation stands and answers out loud. Give them a line to say together, and mean it. Then bless the grandparents by name too."),
("Series Launch &amp; Friends Sunday","c7",20,"Kit built","The single highest-leverage Sunday in a church's year, because everything downstream depends on who is in the room.","Cards and pens in the seats. Everyone writes one name during the service. Not after &mdash; during, while the pastor waits."),
("Group Life Launch &amp; the Call to Serve","c8",20,"Kit built","The retention Sunday. Everyone Easter and Christmas brought in either connects here or is gone by March.","Groups meet in the room. Dismiss by neighborhood, leaders stand with signs, and the first gathering happens in the lobby before anyone leaves."),
]),
("Volume Four &mdash; The Working Calendar", V4, [
("Thanksgiving","c1",20,"","The one holiday nobody argues about, and a rare open door for gratitude preached as formation rather than sentiment.","A gratitude wall in the lobby. People write one name or one thing, and it stays up through the end of the year."),
("Next Step Sundays","c2",60,"3 tracks","The Sundays that move people from attending to following. Three tracks, because a next step means something different depending on where someone is standing.","A physical pathway. Stations across the back of the room, each with a person standing at it, and dismissal routed through them rather than past them."),
("Any Given Sunday","c3",20,"","Deployable any week of the year with no seasonal anchor. The drop-in messages for a gap, a guest, or a Sunday that needs to carry itself.","Design it for the person who has never been. Assume nothing, explain the offering, name the songs, and say out loud that they are welcome to not participate."),
("Communion Sundays","c4",25,"","Twenty-five ways to stop rushing the table. Most churches spend six minutes on the most theologically dense thing they do all month.","One loaf. Families break bread for each other and serve one another rather than receiving from a tray. Take twenty minutes and do not apologize for it."),
("Prayer Sundays","c5",20,"","Services built around praying rather than talking about prayer.","Move the chairs. Circles of six, no sermon past ten minutes, and pray for the church, then each household, then each person by name in the circle."),
("Advent Kickoff","c6",20,"Launches 21-day devotional","The Sunday that decides whether December forms a family or simply exhausts one.","Every household leaves with a candle, a devotional, and a night assigned. Light the first one together in the service, then send them home to continue it."),
("Lent Kickoff","c7",20,"Launches 40-day devotional","The Sunday that gives Easter a runway.","Two cards: one thing laid down, one thing taken up. Both written, one carried home, one left at the front."),
("Vision Sunday","c8",20,"","The single most consequential message a senior pastor preaches all year, and the one most often written last.","Build the wall. A physical representation of the goal that fills in over the following weeks &mdash; visible, in the lobby, updated where everyone walks past it."),
("New Year's Sunday","c9",20,"","Low attendance, high leverage. The people who show up on the first Sunday of January carry the year.","Communion at the turn of the year, plus one written commitment sealed in an envelope the church mails back to them in June."),
("Serve Sunday","c10",20,"","A churchwide serving initiative. Not a food drive with a sermon attached.","Cancel the second service and go. Bus people to sites straight from the parking lot, in the clothes they came in, and come back to eat together."),
("Connection Sunday","c11",20,"","A service engineered to launch groups during the weekend itself rather than hoping people follow up on Tuesday.","Group leaders stand at the front holding signs with their neighborhood and their night. Dismiss the congregation into them rather than out the door."),
("Pair Up and Group Up","c12",20,"","The four-week challenge. People map their circles, then gather in twos or in a living room, starting with an open house.","Do the 5 F exercise in the seats with a worksheet, then have everyone text one person before the closing song. Phones out, on purpose."),
("Church at Home","c13",20,"","The household as the first congregation &mdash; for a snow week, a scattered season, or a deliberate strategy.","Send a table kit home. A card of questions, a passage, a candle, and a blessing to speak. Then ask families to send back one photo."),
("Ask Sundays","c14",20,"","Twenty ways to make a clear ask without apologizing for it. Most churches ask badly, late, and only for money.","Say the number out loud, in one sentence, without a preamble. Then be quiet for five seconds. The pause does more than the paragraph."),
("Ministry Launch Sundays","c15",50,"One per ministry","Fifty ministries, fifty launch messages. Every ministry a church starts lives or dies on the Sunday that introduces it.","One person tells the story of why this ministry needs to exist &mdash; from their own life, in ninety seconds &mdash; and the signup table is staffed before they finish."),
]),
("Volume Five &mdash; The Challenge Library", V5, [
("21-Day Challenges","c1",80,"4 tracks","Three weeks is long enough to change something and short enough that a congregation will finish it.","A physical tracker with twenty-one boxes, and a wall in the lobby the whole church marks together each Sunday."),
("Celebration Sundays","c2",20,"","The last weekend of any series, redesigned so people arrive with something to say rather than something to hear.","Signups three weeks out, ninety seconds each, coached beforehand. Close in the water or at the table rather than with a summary sermon."),
("Challenge Sunday","c3",20,"","A universal launch message for any challenge at seven, ten, or twenty-one days.","Sign the card in the room and walk it forward. A commitment that leaves in a pocket is abandoned by Wednesday."),
("Fasting Sundays","c4",10,"","The discipline the modern church quietly dropped. Jesus said when you fast, not if.","Break the fast together at a shared meal in the building. People remember the meal for a decade, and the meal is what makes the fast make sense."),
("The Challenge Hundred","c5",100,"5 tracks","One hundred messages engineered to become a seven or ten day challenge, each with its companion daily content named up front.","Rotate the companion type. Testimony weeks land differently than devotional weeks, and training weeks &mdash; a skill practiced daily &mdash; finish highest."),
("Impact Sundays","c6",25,"","Twenty-five messages that report rather than ask, reversing the reflex a congregation has learned to brace against.","Bring the actual person, not the video. And hand every giver a card with one name on it: this is who your giving reached."),
("Bible Reading Challenge Sundays","c7",25,"","Twenty-five ways to launch a reading plan, including the ones that address why the last four attempts failed.","Same edition for everyone, bookmarked to the first chapter. Then declare a mid-plan amnesty week where everyone behind restarts together."),
]),
]

KIT=[
("The Message","What the pastor preaches from",[
"Sermon outline &mdash; text, big idea, movements, the turn, the close",
"Landing lines written out &mdash; opening, each transition, and the final sentence",
"Full manuscript, optional tier &mdash; available but never the default",
"Three to five illustration slots, each describing the <em>kind</em> of story needed",
"Deeper study &mdash; exegetical notes, word study, and the commentary the pastor did not have time to read",
"Scripture reading and call to worship",
]),
("The Service","What the other thirty-five minutes do",[
"Run sheet &mdash; minute-by-minute order, timings, transitions, and who does what",
"Cold open or bumper video script &mdash; sixty seconds before anyone speaks",
"Worship set suggestions &mdash; six to eight songs keyed to the big idea, in singable keys",
"Prayer guide &mdash; the pastoral prayer for the service and a household prayer for the week",
"Experience design &mdash; the physical element, the staging, the thing people touch or take home",
]),
("The Response","What happens before anyone leaves",[
"Call to action, written in one sentence",
"Commitment card &mdash; print-ready, signed and collected in the room",
"Next-step mechanic &mdash; the table, the station, the line, staffed and specified",
"Follow-up sequence &mdash; four texts or emails across the week that carry the commitment",
"What to count &mdash; the two or three numbers that tell you whether it worked",
]),
("The Week","How one Sunday becomes seven days",[
"Seven-day devotional &mdash; reading, reflection question, and a daily action",
"Small group session with next steps for the person, the family, and the group",
"Kids and student versions &mdash; the same big idea at three ages, so families talk about one thing",
"Challenge track &mdash; the seven, ten, or twenty-one day extension if the church wants one",
"Family table card &mdash; one question and one passage for the dinner table",
]),
("The Invite","How the room fills",[
"Series and message title graphics &mdash; specification and source files",
"Bulletin blurb and announcement script",
"Social copy and text-message invite, written for the person doing the inviting",
"Email sequence for the week before",
"Testimony brief &mdash; who to look for, what to ask, and how to coach ninety seconds",
]),
]

CSS = BASE + """
.volhead{padding:56px 0 0;border-top:2px solid var(--gold)}
.volhead .label{display:block;margin-bottom:10px}
.volhead h2{font-size:34px}
.open{display:inline-block;margin-top:18px;font-family:'Lato',sans-serif;font-size:11px;
letter-spacing:.18em;text-transform:uppercase;color:var(--navy);background:var(--gold);
padding:11px 22px;text-decoration:none;font-weight:700}
.centry{padding:26px 0;border-bottom:1px solid rgba(184,147,78,.16)}
.chead{display:flex;gap:14px;align-items:baseline}
.chead .n{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.14em;
color:var(--gold);min-width:28px;flex-shrink:0}
.chead a{flex:1;font-family:'Playfair Display',serif;font-size:23px;color:var(--cream);
text-decoration:none}
.chead a:hover{color:var(--gold-lt)}
.chead .note{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.12em;
text-transform:uppercase;color:var(--gold-lt);flex-shrink:0}
.chead .c{font-family:'Lato',sans-serif;font-size:12px;color:#9d958a;
min-width:36px;text-align:right;flex-shrink:0}
.centry .ex{margin-top:10px;color:#c8c0b2;font-size:18px;padding-left:42px}
.centry .xp{margin-top:12px;margin-left:42px;border-left:2px solid var(--gold);
padding:4px 0 4px 16px;color:#ded6c6;font-size:18px}
.centry .xp b{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;
text-transform:uppercase;color:var(--gold);display:block;margin-bottom:5px;font-weight:700}
.tier{margin-top:30px;border:1px solid var(--rule);background:var(--navy-2)}
.tier .th{font-family:'Playfair Display',serif;font-size:22px;color:var(--gold-lt);
padding:16px 22px;border-bottom:1px solid var(--rule)}
.tier .th span{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:#9d958a;display:block;margin-top:4px;font-style:normal}
.tier ul{margin:0;padding:16px 22px 20px 40px;color:#ded6c6}
.tier li{margin-bottom:9px;font-size:18px}
.kitcard{margin-top:24px;border:1px solid var(--rule);background:var(--navy-2);padding:24px}
.kitcard h3{font-size:25px;color:var(--gold-lt)}
.kitcard p{margin-top:12px;color:#ded6c6;font-size:18px}
@media(max-width:620px){
.volhead h2{font-size:26px}.chead a{font-size:20px}.chead .note{display:none}
.centry .ex,.centry .xp{padding-left:0;margin-left:0}
.centry .xp{padding-left:14px}
}
"""

NCAT = sum(len(c[2]) for c in VOLUMES)
NTIT = sum(x[2] for c in VOLUMES for x in c[2])

o=[head('Catalytic Sundays &mdash; Master Directory | LifeTogether', CSS)]
o.append('<div class="wrap cover"><span class="label">LifeTogether &middot; The Single-Message Library</span>')
o.append('<h1>Catalytic Sundays<em>Master Directory</em></h1>')
o.append('<p class="dek">Every category explained, every count honest, and for each one the experience that turns a good message into a Sunday people talk about on Tuesday.</p>')
o.append('<div class="brandline">LifeTogether &middot; 25 Years &middot; 500+ Churches &middot; 50M+ Campaigns</div></div>')

o.append('<div class="stats">')
for b,s in [(NCAT,"Categories"),(NTIT,"Titles"),(25,"Kit Components"),(4,"Catalyst Kits")]:
    o.append('<div class="stat"><b>'+str(b)+'</b><span>'+s+'</span></div>')
o.append('</div>')

o.append('<div class="block"><div class="wrap"><span class="label">What a Sunday Can Be</span>')
o.append('<h2>Nobody remembers <em>a good point</em></h2>')
o.append('<p class="drop">Ask anyone about a church service that changed something in them and they will not quote the outline. They will describe a room going dark, a basin of water, a name written on a card and carried to the front, a meal that went long. The content mattered &mdash; a memorable experience built on a thin idea is just theater &mdash; but content alone has never been what people carry out of a building.</p>')
o.append('<p>So every category in this directory carries two things: an explainer for why that Sunday matters, and an experience &mdash; one specific, physical, stageable thing a church can do to make it land. Most of them cost nothing. All of them take planning that happens weeks earlier than most churches plan.</p>')
o.append('<p>Keep all seven files in one folder and every link on this page works offline.</p>')
o.append('</div></div>')

o.append('<div class="block alt"><div class="wrap"><span class="label">The Standard</span>')
o.append('<h2>What every sermon <em>should ship with</em></h2>')
o.append('<p>Twenty-five components in five tiers. Two of them are the ones most often missing, and both decide whether the Sunday works: the <strong>run sheet</strong>, because the message is thirty-five minutes of a seventy-minute service and most churches design one and improvise the other; and the <strong>follow-up sequence</strong>, because a card signed on Sunday is forgotten by Wednesday without it.</p>')
for tname,tsub,items in KIT:
    o.append('<div class="tier"><div class="th">'+tname+'<span>'+tsub+'</span></div><ul>')
    for it in items:
        o.append('<li>'+it+'</li>')
    o.append('</ul></div>')
o.append('<div class="kitcard"><h3>The one to argue about</h3>')
o.append('<p>The full manuscript sits in tier one as an optional layer rather than the default deliverable, and that is deliberate. A pastor preaching someone else\'s script sounds like a pastor preaching someone else\'s script, and a congregation can hear it inside two minutes. The expanded outline with landing lines written out gives a pastor the hard parts &mdash; the opening, the transitions, the turn, the last sentence &mdash; and leaves the connective tissue in his own voice. Same argument as the illustration slots. Ship the manuscript for the churches that want it, but do not make it the standard, because the standard is what shapes the product.</p></div>')
o.append('</div></div>')

for vname,vfile,cats in VOLUMES:
    n=sum(c[2] for c in cats)
    o.append('<div class="wrap volhead"><span class="label">'+str(len(cats))+' Categories &middot; '+str(n)+' Titles</span>')
    o.append('<h2>'+vname+'</h2>')
    o.append('<a class="open" href="'+vfile+'">Open the volume</a>')
    for i,(cn,anc,cc,note,expl,exper) in enumerate(cats,1):
        o.append('<div class="centry"><div class="chead"><span class="n">'+('%02d'%i)+'</span>')
        o.append('<a href="'+vfile+'#'+anc+'">'+cn+'</a>')
        if note: o.append('<span class="note">'+note+'</span>')
        o.append('<span class="c">'+str(cc)+'</span></div>')
        o.append('<p class="ex">'+expl+'</p>')
        o.append('<div class="xp"><b>Make it an experience</b>'+exper+'</div></div>')
    o.append('</div>')

o.append('<div class="block alt" style="margin-top:56px"><div class="wrap">')
o.append('<span class="label">Built Past the Title Stage</span>')
o.append('<h2>Outlines and <em>Catalyst Kits</em></h2>')
o.append('<div class="kitcard"><h3>Outline Volume One</h3><p>40 complete sermon outlines &mdash; all 20 Resurrection Sunday titles and all 20 Christmas Eve titles.</p>')
o.append('<a class="open" href="'+O1+'">Open the outlines</a></div>')
o.append('<div class="kitcard"><h3>The Catalyst Kit &mdash; Volume Three</h3><p>Four complete kits. Message, seven-day devotional, and a group session with next steps for the person, the family, and the group.</p>')
o.append('<a class="open" href="'+V3+'">Open the kits</a></div>')
o.append('</div></div>')

o.append('<div class="closing"><div class="wrap"><p class="q">A church does not launch a program on Easter morning. It releases a movement, and then spends the rest of the year proving it meant it.</p>')
o.append('<div class="attr">Brett Eastman &middot; LifeTogether</div></div></div>')
o.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; Master Directory &middot; '+str(NCAT)+' Categories &middot; '+str(NTIT)+' Titles</div></footer>')
o.append('</body></html>')

html="\n".join(o)
with io.open('/mnt/user-data/outputs/catalytic-sundays-INDEX.html','w',encoding='utf-8') as f:
    f.write(html)
print("INDEX categories:",NCAT,"titles:",NTIT,"bytes:",len(html))
