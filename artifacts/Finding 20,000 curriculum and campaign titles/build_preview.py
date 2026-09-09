# -*- coding: utf-8 -*-
import io, json
from preview_data import SERMONS, JUMPSTART, JOHN10, FRIENDS_DAY, FRIENDS_MOTIVATE

DATA = {"sermons":SERMONS, "jump":JUMPSTART, "john":JOHN10,
        "fday":FRIENDS_DAY, "fmot":FRIENDS_MOTIVATE}

CSS = """
:root{--navy:#101a33;--navy-2:#16213d;--navy-3:#1c2a4a;--gold:#b8934e;
--gold-lt:#d9bc82;--cream:#f7f3ea;--rule:rgba(184,147,78,.28)}
*{box-sizing:border-box}
body{margin:0;background:var(--navy);color:var(--cream);
font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;line-height:1.65;
-webkit-text-size-adjust:100%}
.wrap{max-width:860px;margin:0 auto;padding:0 22px}
h1,h2,h3,h4{font-family:'Playfair Display',Georgia,serif;font-weight:600;line-height:1.15;margin:0}
.label{font-family:'Lato',system-ui,sans-serif;font-size:11px;letter-spacing:.22em;
text-transform:uppercase;color:var(--gold);font-weight:700}
.cover{padding:58px 0 42px;text-align:center;border-bottom:1px solid var(--rule)}
.cover .label{display:block;margin-bottom:18px}
.cover h1{font-size:44px}
.cover h1 em{display:block;font-style:italic;font-size:23px;color:var(--gold-lt);margin-top:10px;font-weight:400}
.cover .dek{font-size:19px;color:#e6dfd0;margin:18px auto 0;max-width:600px}
.tabs{position:sticky;top:0;z-index:30;background:var(--navy-3);
border-bottom:1px solid var(--rule);overflow-x:auto;-webkit-overflow-scrolling:touch}
.tabs .inner{display:flex;max-width:860px;margin:0 auto;padding:0 12px}
.tab{flex:0 0 auto;background:none;border:0;color:#b9b0a0;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.15em;text-transform:uppercase;padding:16px 14px;cursor:pointer;
border-bottom:2px solid transparent;white-space:nowrap;font-weight:700}
.tab.on{color:var(--gold-lt);border-bottom-color:var(--gold)}
#view{padding:32px 0 70px}
.lead{color:#e6dfd0;margin:0 0 22px;font-size:19px}
.grid{border-top:1px solid var(--rule)}
.item{display:flex;gap:14px;align-items:baseline;padding:16px 2px;
border-bottom:1px solid rgba(184,147,78,.14);cursor:pointer}
.item:hover .iname{color:var(--gold-lt)}
.item .icat{font-family:'Lato',sans-serif;font-size:9px;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);min-width:96px;flex-shrink:0;padding-top:6px}
.item .ibody{flex:1}
.item .iname{font-family:'Playfair Display',serif;font-size:22px;line-height:1.25}
.item .isub{color:#a9a094;font-size:17px;margin-top:3px;line-height:1.4}
.item .arrow{color:var(--gold);font-size:20px;flex-shrink:0}
.back{background:none;border:1px solid var(--rule);color:var(--gold-lt);
font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;text-transform:uppercase;
padding:9px 16px;cursor:pointer;margin-bottom:22px;font-weight:700}
.dh .dc{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--gold);margin-bottom:6px}
.dh h2{font-size:33px}
.dh .df{font-style:italic;color:#c8c0b2;font-size:19px;margin-top:7px}
.meta{margin-top:20px;border-top:1px solid rgba(184,147,78,.18);
border-bottom:1px solid rgba(184,147,78,.18);padding:14px 0}
.row{display:flex;gap:14px;padding:6px 0;align-items:baseline}
.row .k{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.16em;
text-transform:uppercase;color:var(--gold);min-width:78px;flex-shrink:0}
.row .v{flex:1;color:#efe9dc}
.row .v.idea{font-family:'Playfair Display',serif;font-size:20px;line-height:1.35;
color:var(--gold-lt);font-style:italic}
.sec{margin-top:30px}
.sec .sh{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.22em;
text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--rule);
padding-bottom:9px;margin-bottom:6px;font-weight:700}
.mov{display:flex;gap:13px;padding:10px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.mov .mn{font-family:'Playfair Display',serif;font-size:18px;color:var(--gold);min-width:22px;flex-shrink:0}
.mov .mt{flex:1;color:#e6dfd0;font-size:18px}
.day{display:flex;gap:13px;padding:12px 0;border-bottom:1px solid rgba(184,147,78,.12)}
.day .dn{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.14em;color:var(--gold);
min-width:52px;flex-shrink:0;padding-top:5px}
.day .dt{font-family:'Playfair Display',serif;font-size:19px}
.day .ds{color:#b6ac9d;font-size:17px;margin-top:2px;line-height:1.4}
.xp{padding:12px 0;border-bottom:1px solid rgba(184,147,78,.12);color:#ded6c6;font-size:18px}
.xp b{color:var(--gold-lt);font-weight:600}
.ships{margin-top:32px;border:2px solid var(--gold);background:var(--navy-2)}
.ships .sht{font-family:'Playfair Display',serif;font-size:24px;color:var(--gold-lt);
padding:20px 22px 6px}
.ships .shs{padding:0 22px 16px;color:#c3bbad;font-size:17px}
.ships .tier{border-top:1px solid var(--rule);padding:16px 22px}
.ships .tn{font-family:'Lato',sans-serif;font-size:10px;letter-spacing:.18em;
text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:8px}
.ships ul{margin:0;padding-left:18px;color:#ded6c6}
.ships li{margin-bottom:6px;font-size:17px}
.card{border:1px solid var(--rule);background:var(--navy-2);padding:22px;margin-top:22px}
.card h3{font-size:23px;color:var(--gold-lt)}
.card p{margin-top:10px;color:#ded6c6;font-size:18px}
.card ul,.card ol{margin:14px 0 0;padding-left:20px;color:#ded6c6}
.card li{margin-bottom:8px;font-size:18px}
.tbl{margin-top:16px;border-top:1px solid var(--rule)}
.trow{display:flex;gap:14px;padding:12px 0;border-bottom:1px solid rgba(184,147,78,.13)}
.trow .tk{font-family:'Lato',sans-serif;font-size:11px;letter-spacing:.1em;
color:var(--gold-lt);min-width:132px;flex-shrink:0;padding-top:3px}
.trow .tv{flex:1;color:#ded6c6;font-size:17px}
.quote{border-left:2px solid var(--gold);padding:10px 0 10px 18px;margin-top:16px;
color:#e9e2d4;font-style:italic;font-size:18px}
.flag{margin-top:20px;background:var(--navy-3);border-left:2px solid var(--gold);padding:14px 18px;
color:#c3bbad;font-size:17px}
footer{padding:34px 0 56px;text-align:center;font-family:'Lato',sans-serif;
font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8d8579;border-top:1px solid var(--rule)}
@media(max-width:620px){
body{font-size:18px}.cover h1{font-size:30px}.cover h1 em{font-size:19px}
.dh h2{font-size:26px}.item .iname{font-size:20px}
.item{flex-wrap:wrap}.item .icat{min-width:0;width:100%;padding-top:0;margin-bottom:3px}
.row{flex-direction:column;gap:2px}.row .k{min-width:0}
.trow{flex-direction:column;gap:3px}.trow .tk{min-width:0}
.day{flex-direction:column;gap:2px}.day .dn{min-width:0}
}
"""

JS = """
var D = window.__PV__;
var state = {tab:'browse', item:null};

function listSermons(){
  var h = '<p class="lead">Six messages, fully built. Tap any one to see the outline, the seven devotional day titles underneath it, and exactly what ships in the kit.</p><div class="grid">';
  for (var i = 0; i < D.sermons.length; i++){
    var s = D.sermons[i];
    h += '<div class="item" data-i="' + i + '"><span class="icat">' + s.cat + '</span>';
    h += '<span class="ibody"><span class="iname">' + s.t + '</span>';
    h += '<span class="isub">' + s.s + '</span></span><span class="arrow">&rsaquo;</span></div>';
  }
  return h + '</div>';
}

function shipsBlock(exp){
  var h = '<div class="ships"><div class="sht">What ships with this message</div>';
  h += '<div class="shs">Twenty-five components in five tiers, plus the experiential ideas written for this message specifically.</div>';
  h += '<div class="tier"><div class="tn">The message</div><ul><li>Full outline &mdash; text, big idea, movements, the turn, the close</li>';
  h += '<li>Landing lines written out: opening, transitions, and the last sentence</li>';
  h += '<li>Three to five illustration slots, plus the excavation prompts that surface your own</li>';
  h += '<li>Cross-purpose Scripture &mdash; four passages that illustrate the same idea</li>';
  h += '<li>Deeper study: exegetical notes and the commentary you did not have time for</li></ul></div>';
  h += '<div class="tier"><div class="tn">The experience &mdash; written for this message</div><ul>';
  for (var i = 0; i < exp.length; i++){ h += '<li>' + exp[i] + '</li>'; }
  h += '</ul></div>';
  h += '<div class="tier"><div class="tn">The service</div><ul><li>Run sheet &mdash; minute by minute, with timings and handoffs</li>';
  h += '<li>PowerPoint and Keynote decks, plus title and lower-third graphics</li>';
  h += '<li>Cold open script, sixty seconds</li>';
  h += '<li>Worship set suggestions keyed to the big idea, in singable keys</li>';
  h += '<li>Prayer guide for the service and for the household</li></ul></div>';
  h += '<div class="tier"><div class="tn">The response</div><ul><li>Bulletin insert, print-ready</li>';
  h += '<li>Commitment card, signed and collected in the room</li>';
  h += '<li>Invitation card and the three invite scripts &mdash; text, in person, and social</li>';
  h += '<li>Follow-up sequence: four texts or emails across the week</li>';
  h += '<li>What to count &mdash; the two or three numbers that tell you it worked</li></ul></div>';
  h += '<div class="tier"><div class="tn">The week</div><ul><li>Seven-day devotional, print and digital</li>';
  h += '<li>Seven iPhone video scripts &mdash; the same content, shot in under an hour</li>';
  h += '<li>Printable participant journal, ready for a local printer</li>';
  h += '<li>Small group session with next steps for the person, the family, and the group</li>';
  h += '<li>Kids and student versions of the same big idea</li></ul></div>';
  return h + '</div>';
}

function sermonDetail(i){
  var s = D.sermons[i];
  var h = '<button class="back" id="bk">&larr; All messages</button>';
  h += '<div class="dh"><div class="dc">' + s.cat + '</div><h2>' + s.t + '</h2>';
  h += '<p class="df">' + s.s + '</p></div>';
  h += '<div class="meta"><div class="row"><div class="k">Text</div><div class="v">' + s.x + ' (NIV)</div></div>';
  h += '<div class="row"><div class="k">Big idea</div><div class="v idea">' + s.b + '</div></div></div>';
  h += '<div class="sec"><div class="sh">The outline</div>';
  for (var m = 0; m < s.m.length; m++){
    h += '<div class="mov"><div class="mn">' + (m + 1) + '</div><div class="mt">' + s.m[m] + '</div></div>';
  }
  h += '</div>';
  h += '<div class="sec"><div class="sh">Where the week goes &mdash; the seven daily devotions</div>';
  for (var d = 0; d < s.dev.length; d++){
    h += '<div class="day"><div class="dn">Day ' + (d + 1) + '</div><div>';
    h += '<div class="dt">' + s.dev[d][0] + '</div><div class="ds">' + s.dev[d][1] + '</div></div></div>';
  }
  h += '</div>';
  h += shipsBlock(s.exp);
  return h;
}

function jumpView(){
  var h = '<p class="lead">Ten weekdays. Monday through Friday, twice, with the weekends left alone &mdash; because Sunday is the gathering and Saturday belongs to the family. A person who has never finished a devotional finishes this one.</p>';
  h += '<div class="card"><h3>Why ten weekdays beats fourteen days</h3><p>Every daily plan dies on the weekend. Saturday scatters people and Sunday already has a spiritual obligation attached to it, so a plan that requires seven consecutive days is really asking for two acts of obedience it never named. Ten weekdays asks for the commute, the lunch break, or the ten minutes before the house wakes up &mdash; the slots that already exist.</p>';
  h += '<p>The format also gives a church a clean two-week runway between a launch Sunday and a Celebration Sunday, which is exactly the interval where momentum is still live.</p></div>';
  h += '<div class="card"><h3>The flagship: Ten Days Through John</h3><p>The Gospel of John in ten weekday readings, built around the I Am statements and the two bookend invitations. Written so a person who has never opened a Bible can start on a Monday and finish knowing why the book was written.</p></div>';
  h += '<div class="tbl">';
  for (var i = 0; i < D.john.length; i++){
    var j = D.john[i];
    h += '<div class="trow"><div class="tk">Day ' + j[0] + ' &middot; ' + j[2] + '</div>';
    h += '<div class="tv"><strong>' + j[1] + '</strong><br>' + j[3] + '</div></div>';
  }
  h += '</div>';
  h += '<div class="sec"><div class="sh">Twenty jumpstart editions</div>';
  for (var k = 0; k < D.jump.length; k++){
    h += '<div class="day"><div class="dn">' + (k < 9 ? '0' : '') + (k + 1) + '</div><div>';
    h += '<div class="dt">' + D.jump[k][0] + '</div><div class="ds">' + D.jump[k][1] + '</div></div></div>';
  }
  return h + '</div>';
}

function friendsView(){
  var h = '<p class="lead">Friends Day is two categories, not one. There are the messages you preach <em>on</em> the day, written for the guest &mdash; and the messages you preach in the three weeks before it, written to move a congregation to actually ask someone. Most churches build the first and skip the second, then wonder why the room looks the same.</p>';
  h += '<div class="card"><h3>The three-week runway</h3><ol>';
  h += '<li><strong>Three weeks out.</strong> Map the circles. The 5F insert goes in every bulletin and people write names during the service, not after.</li>';
  h += '<li><strong>Two weeks out.</strong> Pray for the name. One person, every morning, and say so from the platform each week.</li>';
  h += '<li><strong>One week out.</strong> Make the ask. Invite cards handed out, texts sent during the service, phones out on purpose.</li>';
  h += '<li><strong>Friends Day.</strong> The guest-facing message. Nothing assumed, nothing insider, and a next step that is coffee rather than an aisle.</li>';
  h += '</ol></div>';
  h += '<div class="card"><h3>The 5F bulletin insert</h3><p>A half-sheet with five boxes, one per circle, and room for two names in each. People fill it in during the service while the pastor waits. Ten names on paper beats a sincere intention every time.</p>';
  h += '<div class="tbl">';
  var circles = [["Circle one","The household &mdash; who lives under your roof or shares your table"],
    ["Circle two","Friends &mdash; the people you would call on a Saturday"],
    ["Circle three","Work &mdash; the person two desks over you have never invited to anything"],
    ["Circle four","Recreation &mdash; the gym, the team, the hobby, the group chat"],
    ["Circle five","Where you live &mdash; the neighbors whose names you do or do not know"]];
  for (var c = 0; c < circles.length; c++){
    h += '<div class="trow"><div class="tk">' + circles[c][0] + '</div><div class="tv">' + circles[c][1] + '</div></div>';
  }
  h += '</div>';
  h += '<div class="flag">The five headings above are functional placeholders. Drop your own five F words in over them &mdash; I have not been given your master version and would rather leave the slot labelled than guess at it.</div></div>';
  h += '<div class="sec"><div class="sh">On the day &mdash; twenty guest-facing messages</div>';
  for (var i = 0; i < D.fday.length; i++){
    h += '<div class="day"><div class="dn">' + (i < 9 ? '0' : '') + (i + 1) + '</div><div>';
    h += '<div class="dt">' + D.fday[i][0] + '</div><div class="ds">' + D.fday[i][1] + '</div></div></div>';
  }
  h += '</div><div class="sec"><div class="sh">Before the day &mdash; twenty messages that motivate the ask</div>';
  for (var m = 0; m < D.fmot.length; m++){
    h += '<div class="day"><div class="dn">' + (m < 9 ? '0' : '') + (m + 1) + '</div><div>';
    h += '<div class="dt">' + D.fmot[m][0] + '</div><div class="ds">' + D.fmot[m][1] + '</div></div></div>';
  }
  return h + '</div>';
}

function homeView(){
  var h = '<p class="lead">Not a livestream. A Sunday where the building stays closed on purpose, every household hosts, and the people who would never walk into a sanctuary walk into a living room instead.</p>';
  h += '<div class="card"><h3>Why the building closes</h3><p>A streamed service asks a family to sit in rows on a couch. Church at Home asks them to do something a sanctuary cannot: eat together, talk, pray for each other by name, and invite two people who were never going to come to a building. The strategic point is the guest list, not the convenience.</p>';
  h += '<p>Run it once a year. Announce it six weeks out, because the invitations are the whole work.</p></div>';
  h += '<div class="card"><h3>The home service order &mdash; about seventy minutes</h3><div class="tbl">';
  var order = [
   ["Before, all week","Deliver the invitations by hand. Set the table the night before so Sunday morning is not a scramble."],
   ["Gather &mdash; 10 min","Everyone arrives, nobody sits in rows. Host says one sentence about why they wanted these particular people here."],
   ["Sing &mdash; 5 min","One song, played from a phone or sung badly by everyone. Badly is fine. Badly is better."],
   ["Read &mdash; 3 min","The youngest person who can read reads the passage aloud. Then someone reads it again."],
   ["Teach &mdash; 12 min","The pastor's video message, or the read-aloud script for households that would rather not use a screen."],
   ["Talk &mdash; 20 min","Three questions, supplied. The host asks and then does not answer first."],
   ["Eat &mdash; 20 min","The meal is not after the service. It is the service. Do not rush this part."],
   ["Pray &mdash; 8 min","Around the table, each person by name, out loud. Guests are prayed for too, and told in advance so nobody is ambushed."],
   ["Bless &mdash; 2 min","The host speaks a supplied blessing over the room and over the guests specifically."],
   ["After","One photo sent back to the church. The wall of photos the following Sunday is the whole payoff."]];
  for (var i = 0; i < order.length; i++){
    h += '<div class="trow"><div class="tk">' + order[i][0] + '</div><div class="tv">' + order[i][1] + '</div></div>';
  }
  h += '</div></div>';
  h += '<div class="card"><h3>What the church supplies</h3><ul>';
  h += '<li>Printed invitations, four per household, delivered two Sundays before</li>';
  h += '<li>The host guide &mdash; the order above, on one folded card</li>';
  h += '<li>The teaching video, twelve minutes, plus a read-aloud script</li>';
  h += '<li>Three discussion questions and one blessing, printed large enough to read across a table</li>';
  h += '<li>A table card with the passage and one question for the meal itself</li>';
  h += '<li>A song list with a QR code, three songs, nothing that needs a band</li>';
  h += '<li>A follow-up text to every host the next morning asking one question: who came?</li></ul></div>';
  return h;
}

function journalView(){
  var h = '<p class="lead">Every challenge should end with something a person can hold. A journal turns seven days of reading into an object that sits on a nightstand and gets finished, and it is the cheapest print piece a church will ever produce.</p>';
  h += '<div class="card"><h3>The page math</h3><p>Saddle-stitch booklets print in multiples of four. Design to the multiple or pay for blank pages.</p><div class="tbl">';
  var math = [["7-day journal","20 pages &mdash; 4 front matter, 14 daily (two per day), 2 back"],
   ["10-day jumpstart","28 pages &mdash; 4 front matter, 20 daily, 4 notes, plus back cover"],
   ["21-day challenge","52 pages &mdash; 6 front matter, 42 daily, 4 notes or tracker"],
   ["Trim size","5.5 x 8.5 inches, half of a letter sheet. Fits a bag, a glovebox, and a Bible."],
   ["Pocket alternative","4 x 6 inches for the 7-day. Cheaper, and people actually carry it."],
   ["Paper","70lb uncoated text. People are writing in it, so coated stock is a mistake."]];
  for (var i = 0; i < math.length; i++){
    h += '<div class="trow"><div class="tk">' + math[i][0] + '</div><div class="tv">' + math[i][1] + '</div></div>';
  }
  h += '</div></div>';
  h += '<div class="card"><h3>What goes on a daily spread</h3><ol>';
  h += '<li><strong>Left page.</strong> Day number, title, the passage printed in full, and the reading. Roughly a hundred and fifty words &mdash; short enough to finish standing up.</li>';
  h += '<li><strong>Right page.</strong> One reflection question with six ruled lines under it, then the day\\'s action in a box, then a checkbox. The checkbox matters more than it looks like it should.</li>';
  h += '<li><strong>Never</strong> put two days on one spread. The finish line has to be visible from the start of each day.</li></ol></div>';
  h += '<div class="card"><h3>Front and back matter</h3><ul>';
  h += '<li><strong>Page 1.</strong> How to use this, in under a hundred words.</li>';
  h += '<li><strong>Page 2.</strong> The commitment page &mdash; name, date, and the name of one person who will ask about it. Signed in the service.</li>';
  h += '<li><strong>Page 3.</strong> A calendar grid with the days to check off, so progress is visible without flipping.</li>';
  h += '<li><strong>Back, minus two.</strong> Two blank notes pages. People use them and it makes the book feel like theirs.</li>';
  h += '<li><strong>Back page.</strong> The next step. Group signup, the QR code, the date of the Celebration Sunday. Never leave this blank.</li></ul></div>';
  h += '<div class="card"><h3>How to actually print it</h3><ul>';
  h += '<li><strong>In house.</strong> Under two hundred copies, print double-sided on a decent copier, fold and staple with a long-reach stapler. It looks homemade because it is, and nobody minds.</li>';
  h += '<li><strong>Local printer.</strong> Two hundred to two thousand. Ask for saddle-stitch, 70lb text, 100lb cover. Get quotes at 250, 500 and 1000 &mdash; the per-unit price falls off a cliff somewhere in there and it is different at every shop.</li>';
  h += '<li><strong>Print on demand.</strong> Above two thousand, or when other churches want to buy it from you. This is also the point at which the journal stops being a cost and starts being a product.</li>';
  h += '<li><strong>Digital.</strong> Always ship a fillable PDF alongside the print run. It costs nothing and it catches the people who lost the physical one by Wednesday.</li></ul></div>';
  h += '<div class="quote">The journal is the artifact that outlives the series. Six months later nobody remembers the sermon title, and the booklet is still in the drawer with handwriting in it.</div>';
  return h;
}

function inviteView(){
  var h = '<p class="lead">Every next-step Sunday needs an invitation, and most churches supply a graphic and hope. An invitation is three things: a physical card, a script for the person doing the asking, and a specific thing to invite someone to.</p>';
  h += '<div class="card"><h3>The one rule</h3><p>Do not invite someone to church. Invite them to <em>this</em> &mdash; a named message, on a named date, about a named thing they are actually dealing with. "Come to my church sometime" is not an invitation. "There is a message on anxiety on the fifteenth and I thought of you" is.</p></div>';
  h += '<div class="card"><h3>The card</h3><ul>';
  h += '<li>Business-card size or half-sheet. Anything larger gets folded, forgotten, and left in a car.</li>';
  h += '<li>Front: the message title, the date, the time. Nothing else. No mission statement.</li>';
  h += '<li>Back: address, what to expect in one line, and where to park. Parking is the single most common reason a first-time guest turns around.</li>';
  h += '<li>A blank line for a handwritten name. Handwriting is what converts a flyer into an invitation.</li>';
  h += '<li>Printed in the hundreds and handed out during the service, not stacked on a table in the lobby.</li></ul></div>';
  h += '<div class="card"><h3>Three scripts</h3><div class="tbl">';
  var scripts = [
   ["The text","Hey &mdash; there is a message at my church on the fifteenth about [the thing]. I thought of you when I heard about it. Want to come with me? I will save you a seat and we can get coffee after."],
   ["In person","Can I ask you something? There is a thing at my church on the fifteenth and it is about [the thing]. No pressure at all, and I am not going to be weird about it. Would you come with me?"],
   ["The follow-up","No worries at all &mdash; the offer stands whenever. And if you ever want to talk about [the thing] without any of the church attached, I am around."]];
  for (var i = 0; i < scripts.length; i++){
    h += '<div class="trow"><div class="tk">' + scripts[i][0] + '</div><div class="tv">' + scripts[i][1] + '</div></div>';
  }
  h += '</div>';
  h += '<div class="flag">Every script names a specific topic, offers to go together, and gives an exit. The offer to attend together is the variable that moves acceptance most, and it is the one most churches leave off the card.</div></div>';
  h += '<div class="card"><h3>Which Sundays get invitations</h3><ul>';
  h += '<li><strong>Friends Day and every series launch.</strong> The whole point.</li>';
  h += '<li><strong>Church at Home.</strong> Four per household, delivered by hand two Sundays out.</li>';
  h += '<li><strong>Baptism Sunday.</strong> The person being baptized invites &mdash; it is the highest-converting invitation a church has, and nobody has to be trained to make it.</li>';
  h += '<li><strong>Baby dedication and graduation.</strong> The family is already inviting. Give them cards so they invite well.</li>';
  h += '<li><strong>Easter, Christmas Eve, Mother\\'s Day.</strong> Obvious, and still frequently missed.</li>';
  h += '<li><strong>Every ministry launch.</strong> The invitation is to the ministry, not the service, and it goes to the person who needs it rather than the whole room.</li></ul></div>';
  return h;
}

function render(){
  var v = document.getElementById('view'), h = '';
  if (state.tab === 'browse'){
    h = (state.item === null) ? listSermons() : sermonDetail(state.item);
  } else if (state.tab === 'jump'){ h = jumpView(); }
  else if (state.tab === 'friends'){ h = friendsView(); }
  else if (state.tab === 'home'){ h = homeView(); }
  else if (state.tab === 'journal'){ h = journalView(); }
  else { h = inviteView(); }
  v.innerHTML = '<div class="wrap">' + h + '</div>';
  window.scrollTo(0, 0);
  var items = v.querySelectorAll('.item');
  for (var i = 0; i < items.length; i++){
    items[i].onclick = function(){ state.item = parseInt(this.getAttribute('data-i'), 10); render(); };
  }
  var bk = document.getElementById('bk');
  if (bk){ bk.onclick = function(){ state.item = null; render(); }; }
}

var tabs = document.querySelectorAll('.tab');
for (var t = 0; t < tabs.length; t++){
  tabs[t].onclick = function(){
    for (var k = 0; k < tabs.length; k++){ tabs[k].classList.remove('on'); }
    this.classList.add('on');
    state.tab = this.getAttribute('data-t');
    state.item = null;
    render();
  };
}
render();
"""

o = []
o.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">')
o.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
o.append('<title>Catalytic Sundays &mdash; The Clickable Preview | LifeTogether</title>')
o.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
o.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
o.append('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">')
o.append('<style>' + CSS + '</style></head><body>')
o.append('<div class="wrap cover"><span class="label">LifeTogether &middot; Clickable Preview</span>')
o.append('<h1>See Where It Goes<em>One Sunday, opened all the way up</em></h1>')
o.append('<p class="dek">Tap a message. See the outline, the seven daily devotions underneath it, and exactly what arrives when a church orders one.</p></div>')
o.append('<div class="tabs"><div class="inner">')
for key, lbl, on in [("browse","Browse Messages",True),("jump","10-Day Jumpstart",False),
                     ("friends","Friends Day",False),("home","Church at Home",False),
                     ("journal","The Journal",False),("invite","Invitations",False)]:
    o.append('<button class="tab' + (' on' if on else '') + '" data-t="' + key + '">' + lbl + '</button>')
o.append('</div></div><div id="view"></div>')
o.append('<footer><div class="wrap">LifeTogether Ministries &middot; Catalytic Sundays &middot; The Clickable Preview</div></footer>')
o.append('<script>window.__PV__ = ' + json.dumps(DATA) + ';</script>')
o.append('<script>' + JS + '</script></body></html>')

html = "\n".join(o)
with io.open('/mnt/user-data/outputs/catalytic-sundays-preview.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("sermons:", len(SERMONS), "jumpstart:", len(JUMPSTART), "john days:", len(JOHN10))
print("friends day:", len(FRIENDS_DAY), "friends motivate:", len(FRIENDS_MOTIVATE))
print("bytes:", len(html))
