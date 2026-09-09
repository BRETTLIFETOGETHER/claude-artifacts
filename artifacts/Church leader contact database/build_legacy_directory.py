#!/usr/bin/env python3
# Legacy Library Directory — Vol. II generator (zero-JS static HTML, navy/gold system)
import html as H

# (first, last, church, attendance, city, state, tag) — transcribed from Brett's paste, file order
R = [
("David","Platt","McLean Bible Church",11867,"Vienna","VA","C"),
("Solomon","Kinloch","Triumph Church",11600,"Detroit","MI","C"),
("Steve","Stroope","Lake Pointe Church",11225,"Rockwall","TX","C"),
("Keith","Butler","Word of Faith International Christian Center",11000,"Southfield","MI","C"),
("Wayne","Cordeiro","New Hope Christian Fellowship",11000,"Honolulu","HI","C"),
("Daniel","De Leon","Templo Calvario Assembly of God",11000,"Santa Ana","CA","C"),
("Willie","George","Church on the Move",11000,"Tulsa","OK","C"),
("Stephen","Hayes","Covenant Church",11000,"Carrollton","TX","C"),
("Ron","Vietti","Valley Bible Fellowship",11000,"Bakersfield","CA","C"),
("Kevin","Cosby","Saint Stephen Church",10714,"Louisville","KY","C"),
("Byron","Brazier","Apostolic Church of God",10500,"Chicago","IL","C"),
("Chris","Brown","North Coast Church",10500,"Vista","CA","C"),
("Chris","Hodges","Church of the Highlands",10301,"Birmingham","AL","C"),
("Matt","Chandler","The Village Church",10200,"Flower Mound","TX","C"),
("Cal","Jernigan","Central Christian Church",10200,"Mesa","AZ","C"),
("Adam","Hamilton","Church of the Resurrection",10137,"Leawood","KS","C"),
("Mike","Housholder","Lutheran Church of Hope",10100,"West Des Moines","IA","C"),
("Steve","Smothermon","Legacy Church",10100,"Albuquerque","NM","C"),
("Josh","Surratt","Seacoast Church",10050,"Mount Pleasant","SC","C"),
("Claude","Alexander","University Park Baptist Church",10000,"Charlotte","NC","C"),
("Mark","Balmer","Calvary Chapel of Melbourne",10000,"West Melbourne","FL","C"),
("Luke","Barnett","Dream City Church",10000,"Phoenix","AZ","C"),
("Jim","Cymbala","Brooklyn Tabernacle",10000,"Brooklyn","NY","C"),
("Joe","Focht","Calvary Chapel of Philadelphia",10000,"Philadelphia","PA","C"),
("Milton","Hawkins","Temple of Deliverance",10000,"Memphis","TN","C"),
("Jeffrey","Johnson","Eastern Star Church",10000,"Indianapolis","IN","C"),
("Noel","Jones","City of Refuge Church",10000,"Gardena","CA","C"),
("Aubrey","Malphurs","Lake Pointe Church",10000,"","","J"),
("James","Meeks","Salem Baptist Church of Chicago",10000,"Chicago","IL","C"),
("Debra","Morton","Greater Saint Stephen Full Gospel Baptist",10000,"New Orleans","LA","C"),
("Dan","Reeve","Faith Community Church",10000,"West Covina","CA","C"),
("Raul","Ries","Calvary Chapel Golden Springs",10000,"","CA","C"),
("Raul","Ries","Calvary Chapel Golden Springs",10000,"Diamond Bar","CA","C"),
("Dan","Roth","The Rock Church and World Outreach Center",10000,"","CA","C"),
("Steve","Stroope","Lake Pointe Church",10000,"Rockwall","TX","C"),
("Karl","Stuckenberg","Shepherd of the Hills",10000,"Mission Viejo","CA","C"),
("Andy","Thompson","World Overcomers Christian Church",10000,"Durham","NC","C"),
("Joseph","Walker","Mount Zion Baptist Church",10000,"Nashville","TN","C"),
("Lance D.","Watson","The Saint Paul's Baptist Church",10000,"Richmond","VA","C"),
("Bruce","","Shepherd of the Hills",10000,"","","J"),
("Matthew","Barnett","The Dream Center",9500,"Los Angeles","CA","C"),
("Paul","Daugherty","Victory Christian Center",9500,"Tulsa","OK","C"),
("Nick","Floyd","Cross Church",9223,"Rogers","AR","C"),
("Tim","Clark","The Church on the Way",9032,"Van Nuys","CA","C"),
("Todd","Cook","Sagebrush Community Church",9000,"Albuquerque","NM","C"),
("Victor","Curry","New Birth Baptist Church",9000,"Miami","FL","C"),
("Raymond","Gordon","Saint Matthew's Baptist Church",9000,"Williamstown","NJ","C"),
("Mac","Hammond","Living Word Christian Center",9000,"Brooklyn Park","MN","C"),
("Frederick","Haynes","Friendship West Baptist Church",9000,"Dallas","TX","C"),
("Jeff","Johnson","Calvary Chapel Downey",9000,"Downey","CA","C"),
("Steve","Mays","Calvary Chapel of South Bay",9000,"Torrance","CA","C"),
("David","Thompson","The Summit Church",9000,"Durham","NC","C"),
("Remus","Wright","The Fountain of Praise",9000,"Houston","TX","C"),
("Todd","Wagner","Watermark Community Church",8876,"Dallas","TX","C"),
("Denny","Davis","Saint John Baptist Church",8800,"Grand Prairie","TX","C"),
("Chip","Henderson","Pinelake Church",8791,"Oxford","MS","C"),
("Randy","Frazee","Oak Hills Church",8663,"San Antonio","TX","C"),
("Dary","Northrop","Timberline Church",8616,"Fort Collins","CO","C"),
("Greg","Barr","Saint Matthews Baptist Church",8300,"Louisville","KY","C"),
("Dale","Bronner","Word of Faith Family Worship Cathedral",8300,"Austell","GA","C"),
("David","Rosales","Calvary Chapel Chino Valley",8300,"Chino","CA","C"),
("Omar","Giritli","Christ Fellowship",8098,"Palmetto Bay","FL","C"),
("Mike","Lee","Hope Community Church",8085,"Raleigh","NC","C"),
("David","Hughes","Church by the Glades",8079,"Coral Springs","FL","C"),
("Charles","Jackson","Brookland Baptist Church",8075,"West Columbia","SC","C"),
("Gregg","Matte","Houston's First Baptist Church",8019,"Houston","TX","C"),
("Carter","Conlon","Times Square Church",8000,"New York","NY","C"),
("David","Crank","Faith Church",8000,"St. Louis","MO","C"),
("Charles","Ellis","Greater Grace Temple",8000,"Detroit","MI","C"),
("Henry","Fernandez","The Faith Center Ministries",8000,"Sunrise","FL","C"),
("Eric","Geiger","Mariners Church",8000,"Irvine","CA","C"),
("Allen","Jackson","World Outreach Church",8000,"Murfreesboro","TN","C"),
("Clifford","Johnson","Mount Pleasant Church and Ministries",8000,"Baltimore","MD","C"),
("Daniel","Kim","Sarang Community Church",8000,"Anaheim","CA","C"),
("John","MacArthur","Grace Community Church",8000,"Sun Valley","CA","C"),
("Courtney","McBath","Calvary Revival Church",8000,"Norfolk","VA","C"),
("Tom","Politz","Hillside Christian Church",8000,"Amarillo","TX","C"),
("Lee","Powell","CedarCreek Church",8000,"Perrysburg","OH","C"),
("Dennis","Rouse","Victory World Church",8000,"Norcross","GA","C"),
("Rickie","Rush","Inspiring Body of Christ Church",8000,"Dallas","TX","C"),
("K B","Shore","Mariners Church",8000,"","CA","J"),
("Jonathan","Stockstill","Bethany World Prayer Center",8000,"Baker","LA","C"),
("Casey","Treat","Christian Faith Center",8000,"Seattle","WA","C"),
("Kenneth","Ulmer","Faithful Central Bible Church",8000,"Inglewood","CA","C"),
("Kenny","Foreman","Cathedral of Faith",7800,"San Jose","CA","C"),
("Toure","Roberts","Potter's House Church of Denver",7800,"Denver","CO","C"),
("Jeff","Manion","Ada Bible Church",7700,"Ada","MI","C"),
("David","Jeremiah","Shadow Mountain Community Church",7513,"El Cajon","CA","C"),
("Dan","Betzer","First Assembly of God",7500,"Ft. Myers","FL","C"),
("Leon","Fontaine","Springs Church",7500,"Winnipeg","MB","C"),
("Phillip","Macintosh","Horizon Christian Fellowship",7500,"San Diego","CA","C"),
("Mike","Macintosh","Horizon Christian Fellowship",7500,"","CA","J"),
("Otis","Moss","Trinity United Church of Christ",7500,"Chicago","IL","C"),
("Mark","Whitlock","Reid Temple AME Church",7465,"Glenn Dale","MD","C"),
("Kevin","Peck","The Austin Stone Community Church",7428,"Austin","TX","C"),
("Cam","Huxford","Savannah Christian Church",7331,"Savannah","GA","C"),
("David","Crank","Faith Church",7300,"St. Louis","MO","C"),
("Doug","Thiesen","Heartland Community Church",7274,"Rockford","IL","C"),
("Randal","Ross","Calvary Church of Naperville",7200,"Naperville","IL","C"),
("Robby","Gallaty","Long Hollow Baptist Church",7154,"Hendersonville","TN","C"),
("Robert","Cupp","Fellowship Northwest Arkansas",7100,"Rogers","AR","C"),
]

# ---- dedupe to distinct churches (normalized name), collecting all contacts ----
def norm(c): return c.lower().replace("the ","").replace("'","").strip()
churches = {}
order = []
for (f,l,c,att,city,st,tag) in R:
    k = norm(c)
    if k not in churches:
        churches[k] = {"name":c,"att":att,"city":city,"st":st,"contacts":[],"tags":set(),"records":0}
        order.append(k)
    e = churches[k]
    e["records"] += 1
    e["tags"].add(tag)
    nm = (f+" "+l).strip()
    if nm not in e["contacts"]: e["contacts"].append(nm)
    if city and not e["city"]: e["city"], e["st"] = city, st
    e["att"] = max(e["att"], att)

n_records = len(R)
n_church  = len(order)
n_copper  = sum(1 for r in R if r[6]=="C")
n_jacobs  = sum(1 for r in R if r[6]=="J")
print("records", n_records, "distinct", n_church, "copper", n_copper, "jacobs", n_jacobs)

# ---- the proof shelf: 9 fully-linked productized libraries + 2 bench ----
SHELF = [
 dict(no="01", lib="Grace to You", pastor="John MacArthur", church="Grace Community Church", city="Sun Valley, CA", att="filed 8,000",
  body="The largest single-pastor legacy library in American evangelicalism, and the clearest proof that an archive becomes an asset. MacArthur died in July 2025 having completed a 42-year verse-by-verse cycle through the entire New Testament; Grace to You keeps the full archive of 55+ years free to stream and download, runs a 24/7 Grace Stream, and sells the same corpus as products — topical series, flash drives, and a 3,127-sermon digital archive that Logos retails at $399.99. The library outlived the pulpit and now runs as a publishing operation.",
  rank="SermonAudio publishes per-sermon play counts for his feed (individual messages showing 11,000 to 57,000+ plays) — the most legible ranking surface on this entire list. The GTY store's featured and bestselling series are the ministry's own curation.",
  links=[("Full free archive","https://www.gty.org/"),
         ("Series archive","https://www.gty.org/sermons/series/archive/topical-series"),
         ("Store (series, drives, bundles)","https://shop.gty.org/library/resources/sermons-library"),
         ("Play-count ranking (SermonAudio)","https://www.sermonaudio.com/broadcasters/johnmacarthur/sermons"),
         ("The productized archive (Logos, $399.99)","https://www.logos.com/johnmacarthursermonarchivelist")]),
 dict(no="02", lib="ShareChurch", pastor="Adam Hamilton", church="Church of the Resurrection", city="Leawood, KS", att="filed 10,137 · now ~25,000 across nine campuses",
  body="The closest existing thing to the campaign-library model, run as a gift: Resurrection packages entire sermon series — the sermons plus every produced resource, small-group curriculum, children's material, and administrative kit — and gives them to other churches under a Creative Commons license. Hamilton calls the church a &ldquo;living laboratory,&rdquo; and his books ship through Abingdon as full churchwide campaigns with video and leader guides. ShareChurch also runs the Leadership Institute conference.",
  rank="ShareChurch's own resource library is the curation — series are packaged, titled, and categorized by the source church itself, which is stronger than any view-count proxy.",
  links=[("ShareChurch series kits","https://sharechurch.com/the-promise-of-christmas/"),
         ("Resource library — sermon series","https://www.sharechurch.com/Resource-Library.aspx?category=Sermon+Series"),
         ("Latest packaged series (Why Church?, 2025)","https://sharechurch.com/why-church/"),
         ("Sermons at Resurrection","https://resurrection.church/enote/weekly-update-from-pastor-adam-august-9-2024/"),
         ("Leadership Institute","https://leadership.sharechurch.com/speakers/adam-hamilton/")]),
 dict(no="03", lib="Sermon-Based Small Groups", pastor="Chris Brown &middot; Larry Osborne", church="North Coast Church", city="Vista, CA", att="filed 10,500",
  body="The one church in America that has run the week-after-Sunday architecture at scale for forty years: every weekend message ships with Sermon Notes and Homework in PDF and DOC, the homework feeds that week's groups, and adult small-group participation has held at 80% of weekend attendance since 1985. Osborne wrote the model up as Sticky Church (Zondervan) and North Coast Training sells a Starter Kit — site license, covenants, forms, and his training videos. They productized the methodology; the weekly content library itself was never packaged for other churches.",
  rank="Their message archive is organized by series with the notes attached — the curation is structural, not statistical. Osborne was still teaching live in July 2026; the current series is The Art of Surrender through Matthew.",
  links=[("Message archive w/ notes + homework","https://northcoastchurch.com/messages/1-bitter-or-better-the-choice-is-ours/"),
         ("Osborne's message feed (live 2026)","https://northcoastchurch.com/pastor-larrys-messages/"),
         ("Starter Kit product","https://northcoasttraining.org/product/sermon-based-small-groups-starter-kit/"),
         ("The model, explained","https://churchexecutive.com/archives/sermon-based-small-groups-keep-people-from-exiting-the-back-door")]),
 dict(no="04", lib="Secret Church &middot; Radical", pastor="David Platt", church="McLean Bible Church", city="Vienna, VA", att="filed 11,867",
  body="A sermon format turned annual product: one six-hour night of intensive teaching, streamed to tens of thousands, with twenty-six past events archived free — stream, Guided Scripture Journal, and discussion questions for each. Study guides sell separately through the Radical bookstore. It is the cleanest demonstration on this list that a teaching event plus a printed journal plus group questions equals a durable, repeatable SKU.",
  rank="Radical's own event archive is the shelf — 26 numbered events, each a self-contained kit. The bookstore's study-guide sales are the revealed preference.",
  links=[("26 past events — media, journals, questions","https://radical.net/secret-church-events/"),
         ("Resource library","http://www.radical.net/resources/secret_church/"),
         ("Study guides (bookstore)","https://bookstore.radical.net/series/secret-church-study-guides"),
         ("Latest: Secret Church — Elijah","https://radical.net/secret_church/elijah/")]),
 dict(no="05", lib="TVC Resources", pastor="Matt Chandler", church="The Village Church", city="Flower Mound, TX", att="filed 10,200",
  body="The church's resource arm carries its own brand name — a donation-supported library of sermons, series pages, articles, and study content, with Chandler still preaching weekly (messages posted through August 2026). Every named series has a permanent index page, and the whole operation sits adjacent to the Acts 29 planting network, which is the distribution channel most churches on this list never built.",
  rank="The series index is the curation; the long-running Apple Podcasts feed carries two decades of episodes where chart placement and reviews are the visible proxy.",
  links=[("Resource library","https://www.tvcresources.net/resource-library/"),
         ("Sermon archive (live)","https://www.tvcresources.net/resource-library/sermons/"),
         ("Example series page","https://www.tvcresources.net/resource-library/series-index/grace-made-visible/"),
         ("Apple Podcasts feed","https://podcasts.apple.com/us/podcast/the-village-church-sermons/id82014403")]),
 dict(no="06", lib="21 Days of Prayer", pastor="Chris Hodges", church="Church of the Highlands", city="Birmingham, AL", att="filed 10,301 · now ~60,000, the largest church in Alabama",
  body="A congregational rhythm turned national franchise: twice a year since 2001, and the resources are published for any church to run — with the ARC church-planting network (which Hodges co-founded) carrying it to hundreds of congregations. It is the purest example on this list of campaign plus network distribution: the content is simple, the calendar is fixed, and the channel was built before the product needed one.",
  rank="Highlands' own media channel archives every 21 Days message; the ARC network's adoption is the ranking — a campaign other churches choose to run is the strongest vote available.",
  links=[("21 Days hub","https://21days.churchofthehighlands.com/"),
         ("Prayer strategy + resources","https://www.churchofthehighlands.com/prayer"),
         ("21 Days message archive","https://www.churchofthehighlands.com/media/channel/21-days-of-prayer?page=2"),
         ("ARC network distribution","https://www.arcchurches.com/21-days-of-prayer-resources/")]),
 dict(no="07", lib="Replicate", pastor="Robby Gallaty", church="Long Hollow Baptist Church", city="Hendersonville, TN", att="filed 7,154",
  body="A complete IP-multiplication ladder built off one pulpit: the F260 Foundations reading plan (with separate adult, teen, and kids workbooks), the H.E.A.R. journaling method, a Disciple's Study Bible built around the system with Lifeway, an 18-video Discipleship Blueprint course with church assessments, twenty-plus books (Growing Up past 100,000 copies), and a coaching and consulting arm. Reading plan to journal to Bible to course to coaching — every rung monetized, every rung feeding the next.",
  rank="Replicate's own product line is the ranking — the F260 family and Growing Up are what the market kept buying. The YouVersion editions of the plans carry public completion numbers.",
  links=[("Replicate home","https://replicate.org/"),
         ("Foundations / F260 plans (adult-teen-kids)","https://replicate.org/foundations"),
         ("Discipleship Blueprint course","https://replicate.org/resources/discipleship-blueprint"),
         ("Books + journals","https://replicate.org/books"),
         ("The Disciple's Study Bible","https://disciplesbible.csbible.com/")]),
 dict(no="08", lib="Turning Point", pastor="David Jeremiah", church="Shadow Mountain Community Church", city="El Cajon, CA", att="filed 7,513",
  body="The broadcast-era legacy library at full maturity: radio, television, live events, fifty-plus books, and TurningPoint+ — a streaming platform of complete teaching series and Bible studies. Jeremiah, in his eighties, is still preaching weekly at Shadow Mountain while the ministry runs the archive as a media company. Every sermon series becomes a broadcast season, a book, and a study resource on a fixed conveyor.",
  rank="TurningPoint+ and the series index are the ministry's own curation; the radio archive on OnePlace and the television schedule show which series they keep putting in front of the audience — rebroadcast frequency is their revealed ranking.",
  links=[("Television + TurningPoint+","https://www.davidjeremiah.org/television"),
         ("Full series index","https://www.lightsource.com/ministry/turning-point/series/"),
         ("Daily radio archive","https://www.oneplace.com/ministries/turning-point/")]),
 dict(no="09", lib="The Life Journal", pastor="Wayne Cordeiro", church="New Hope Christian Fellowship", city="Honolulu, HI", att="filed 11,000",
  body="A devotional method that outgrew its church: the Life Journal and the SOAP reading method (Scripture, Observation, Application, Prayer) are used by thousands of congregations, and Cordeiro is general editor of the LifeConnect Study Bible built on the same system. He handed off New Hope Oahu in 2017 — 153 churches planted, 110,000+ first-time decisions — and still publishes the Life Journal Daily from his Oregon lab church. The product survived two church transitions because it was never really a church program; it was a portable practice.",
  rank="Adoption is the ranking — thousands of churches running the journal independent of New Hope. The daily blog shows the format still producing twenty years on.",
  links=[("Life Journal Daily (live)","https://newhopewest.com/life-journal-daily-with-pastor-wayne/"),
         ("Cordeiro profile + the method's reach","https://theascentleader.org/cohorts/wayne-cordeiro/")]),
]

BENCH = [
 ("Randy Frazee &middot; Oak Hills Church","The Story and Believe — the Zondervan churchwide campaign systems of the 2010s, multi-week alignment of sermons, all-age curriculum, and reading. The nearest structural cousin the 40-day model has ever had in the trade market. Current home of the church kits: locate in the full sweep."),
 ("Jim Cymbala &middot; Brooklyn Tabernacle","Fresh Wind, Fresh Fire and its successors — the Tuesday prayer meeting turned into one of the bestselling pastoral libraries of the era, curated as books rather than an archive. Digital library status: confirm in the full sweep."),
]

css = """
:root{--ink:#080e16;--navy:#0b1726;--panel:#132439;--gold:#c9a35c;--goldb:#e3c186;--cream:#ece7d8;--muted:#8b94a5;}
*{margin:0;padding:0;box-sizing:border-box;}html{scroll-behavior:smooth;}
body{background:var(--navy);color:var(--cream);font-family:'Cormorant Garamond',Georgia,serif;font-size:19px;line-height:1.55;}
.wrap{max-width:840px;margin:0 auto;padding:0 22px;}
a{color:var(--goldb);text-decoration:none;border-bottom:1px solid rgba(201,163,92,.35);}
a:hover{border-bottom-color:var(--goldb);} a:focus-visible{outline:2px solid var(--goldb);outline-offset:2px;}
.eyebrow{font-family:'Playfair Display',serif;font-size:12px;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);}
header.m{padding:62px 0 42px;border-bottom:1px solid rgba(201,163,92,.4);}
h1{font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(33px,6vw,52px);line-height:1.08;margin:16px 0 14px;}
h1 em{font-style:italic;font-weight:400;color:var(--goldb);}
.stand{font-size:21px;max-width:660px;}
.date{margin-top:16px;font-size:15px;color:var(--muted);letter-spacing:.06em;}
.census{display:flex;flex-wrap:wrap;border-bottom:1px solid rgba(201,163,92,.4);}
.census div{flex:1 1 140px;padding:20px 14px 22px;border-right:1px solid rgba(201,163,92,.18);}
.census div:last-child{border-right:none;}
.census .n{font-family:'Playfair Display',serif;font-size:30px;color:var(--goldb);display:block;line-height:1;}
.census .l{font-size:13px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin-top:8px;display:block;}
.sechead{font-family:'Playfair Display',serif;font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);padding:44px 0 12px;border-bottom:1px solid rgba(201,163,92,.4);}
.secintro{padding:16px 0 4px;font-size:19px;max-width:700px;}
article.e{padding:40px 0 36px;border-bottom:1px solid rgba(139,148,165,.25);}
.etop{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;}
.num{font-family:'Playfair Display',serif;font-size:14px;color:var(--gold);letter-spacing:.1em;}
h2{font-family:'Playfair Display',serif;font-weight:600;font-size:clamp(24px,4.2vw,32px);margin:8px 0 3px;}
.who{font-size:16.5px;letter-spacing:.02em;color:var(--cream);margin-bottom:4px;}
.who b{color:var(--goldb);font-weight:600;}
.place{font-size:14px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:16px;}
.body{font-size:18.5px;margin-bottom:14px;}
.lbl{font-family:'Playfair Display',serif;font-size:11.5px;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);margin:16px 0 8px;}
.rank{font-size:17.5px;font-style:italic;color:var(--cream);padding-left:14px;border-left:2px solid rgba(201,163,92,.5);margin-bottom:6px;}
table.lk{width:100%;border-collapse:collapse;margin-top:6px;}
table.lk td{padding:7px 2px;border-bottom:1px solid rgba(139,148,165,.16);font-size:16.5px;vertical-align:baseline;}
table.lk td.k{width:44%;font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);padding-right:12px;}
table.lk tr:last-child td{border-bottom:none;}
.bench{padding:26px 0 8px;}
.bench h3{font-family:'Playfair Display',serif;font-size:20px;font-weight:600;margin:14px 0 4px;color:var(--cream);}
.bench p{font-size:17.5px;color:var(--cream);max-width:720px;}
.meth p{margin:14px 0;font-size:19px;max-width:720px;}
.meth p b{font-family:'Playfair Display',serif;font-size:17px;color:var(--goldb);font-weight:600;}
table.roster{width:100%;border-collapse:collapse;margin:14px 0 8px;}
table.roster th{font-family:'Playfair Display',serif;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);text-align:left;padding:8px 6px;border-bottom:1px solid rgba(201,163,92,.4);}
table.roster td{padding:8px 6px;border-bottom:1px solid rgba(139,148,165,.14);font-size:16.5px;vertical-align:baseline;}
td.att{font-family:'Playfair Display',serif;font-size:14px;color:var(--goldb);white-space:nowrap;}
td.st{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);white-space:nowrap;}
td.st.p{color:var(--goldb);}
.contact{color:var(--muted);font-size:15px;font-style:italic;}
footer{padding:34px 0 64px;color:var(--muted);font-size:15px;border-top:1px solid rgba(201,163,92,.4);margin-top:30px;}
.up{font-size:12px;letter-spacing:.18em;text-transform:uppercase;}
@media(max-width:600px){.census div{flex:1 1 45%;border-right:none;border-bottom:1px solid rgba(201,163,92,.18);}
 table.roster td:nth-child(2),table.roster th:nth-child(2){display:none;}}
"""

def links_table(links):
    rows = "".join('<tr><td class="k">%s</td><td><a href="%s">%s</a></td></tr>' % (k, u, u.replace("https://","").replace("http://","").rstrip("/")) for k,u in links)
    return '<table class="lk">%s</table>' % rows

shelf_html = ""
profiled = set()
for e in SHELF:
    profiled.add(norm(e["church"]))
    shelf_html += ('<article class="e" id="s%s"><div class="etop"><span class="num">No. %s</span></div>'
        '<h2>%s</h2><div class="who">%s &mdash; <b>%s</b></div><div class="place">%s &middot; %s</div>'
        '<p class="body">%s</p><div class="lbl">Where the ranking lives</div><p class="rank">%s</p>'
        '<div class="lbl">Indexed links</div>%s'
        '<p style="margin-top:14px"><a class="up" href="#idx">&uarr; Index</a></p></article>') % (
        e["no"], e["no"], e["lib"], e["pastor"], e["church"], e["city"], e["att"], e["body"], e["rank"], links_table(e["links"]))

bench_html = "".join('<h3>%s</h3><p>%s</p>' % (t, b) for t,b in BENCH)
for t,_ in BENCH:
    if "Oak Hills" in t: profiled.add(norm("Oak Hills Church"))
    if "Brooklyn Tabernacle" in t: profiled.add(norm("Brooklyn Tabernacle"))

# roster
bands = [(11000,99999,"11,000 and above"),(10000,10999,"The 10,000 band"),(9000,9999,"The 9,000 band"),(8000,8999,"The 8,000 band"),(7000,7999,"The 7,000 band")]
roster_html = ""
count_profiled = 0
for lo,hi,label in bands:
    rows = ""
    for k in order:
        e = churches[k]
        if not (lo <= e["att"] <= hi): continue
        loc = (e["city"]+", "+e["st"]).strip(", ") if e["city"] or e["st"] else "&mdash;"
        contacts = " &middot; ".join(e["contacts"])
        note = ""
        if e["records"] > 1: note = ' <span class="contact">(%d file records merged)</span>' % e["records"]
        if k in profiled:
            st = '<td class="st p">On the shelf</td>'; count_profiled += 1
        else:
            st = '<td class="st">Sweep pending</td>'
        tag = "/".join(sorted("Copper 6300" if t=="C" else "Jacobs Ladder" for t in e["tags"]))
        rows += '<tr><td>%s%s<br><span class="contact">%s &middot; %s</span></td><td>%s</td><td class="att">%s</td>%s</tr>' % (
            H.escape(e["name"]), note, H.escape(contacts), H.escape(tag), H.escape(loc), format(e["att"], ","), st)
    roster_html += '<div class="lbl" style="margin-top:26px">%s</div><table class="roster"><tr><th>Church &middot; filed contact &middot; tag</th><th>Location</th><th>Filed size</th><th>Status</th></tr>%s</table>' % (label, rows)

n_shelf = len(SHELF) + len(BENCH)
n_pending = n_church - count_profiled

page = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Legacy Library Directory &mdash; Vol. II &middot; The Megachurch File</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>%s</style></head><body><div class="wrap" id="idx">

<header class="m">
<span class="eyebrow">LifeTogether &middot; Ministry Intelligence &middot; Field Research &middot; Volume II</span>
<h1>The Legacy Library <em>Directory</em></h1>
<p class="stand">The megachurch cut of the master file &mdash; %d records, %d distinct churches, filed at 7,100 to 11,867 in attendance. Pastor names are treated as archive identifiers, not current staff: the question asked of every record is whether the preaching library was ever stewarded into a product, and where its ranking surface lives.</p>
<p class="date">Compiled August 26, 2026 &middot; dedupe and counts computed from the source records &middot; shelf entries verified against live sources this date</p>
</header>

<div class="census">
<div><span class="n">%d</span><span class="l">File records</span></div>
<div><span class="n">%d</span><span class="l">Distinct churches</span></div>
<div><span class="n">%d</span><span class="l">Productized libraries identified</span></div>
<div><span class="n">%d</span><span class="l">Archives pending the sweep</span></div>
</div>

<div class="sechead">Part One &middot; The Proof Shelf</div>
<p class="secintro">Nine libraries from this file that already run as products &mdash; each one a working demonstration of a different rung on the ladder: free archive, packaged series, group system, annual event, resource brand, campaign franchise, discipleship line, broadcast platform, portable practice. These are comps and potential partners, not prospects.</p>
%s

<div class="bench"><div class="lbl">Also belongs on this shelf &mdash; links pending the sweep</div>%s</div>

<div class="sechead">Part Two &middot; How &ldquo;Highest Ranked&rdquo; Actually Gets Determined</div>
<div class="meth">
<p><b>No church ranks its own sermons.</b> Every &ldquo;best of&rdquo; is a proxy, and the five that exist are: the ministry's own curation shelf (featured series, start-here pages, store bestsellers &mdash; the strongest signal, because it is the owner's judgment); SermonAudio play counts where a church broadcasts there (public, per-sermon, sortable); the YouTube Popular tab on each channel (one tap in a browser, but rendered client-side &mdash; a crawler cannot read it, an API key or a thumb can); Spotify's per-episode popularity bars on podcast feeds; and the pastor's books, which are his own ranking of his own material &mdash; nobody writes the book of the sermons that didn't work.</p>
<p><b>And one caution worth pricing in:</b> popularity measures reference, not result. The most-viewed video on a channel is often a clip, a controversy, or a funeral &mdash; not the series that filled the groups. For acquisition purposes the better axis is productization evidence: did the sermon become a series, the series a study, the study a campaign? Part One is ranked on that axis. The sweep can carry both columns &mdash; the popular one and the proven one &mdash; and the gap between them is itself intelligence.</p>
</div>

<div class="sechead">Part Three &middot; The Full Roster &mdash; Every Church Accounted For</div>
<p class="secintro">All %d distinct churches from the file, in attendance order as filed, with the original contact name and program tag preserved as archive identifiers. &ldquo;Sweep pending&rdquo; means the archive exists in some form &mdash; nearly every church this size publishes sermons &mdash; but its library, series structure, and ranking surface have not yet been indexed.</p>
%s

<footer>
<span class="eyebrow" style="font-size:11px">LifeTogether Ministries &middot; The Pastor's Library &middot; Field Research Vol. II</span><br><br>
Source: the master-file megachurch cut, %d records. Duplicates merged by church: Lake Pointe (3 records incl. the Malphurs lay-leader row), Calvary Chapel Golden Springs (2), Faith Church St. Louis (2), Mariners (2), Horizon Christian Fellowship (2), Shepherd of the Hills (2 &mdash; the two records may describe different churches of the same name; flagged, not resolved). Tags as filed: Copper 6300 &times;%d, Jacobs Ladder &times;%d. Shelf claims verified against live public sources on August 26, 2026; descriptions written in original language, no source text reproduced. Attendance figures are the file's own numbers &mdash; several are a generation old (the largest drift found: one church filed at 10,301 now runs ~60,000).
</footer>
</div></body></html>""" % (css, n_records, n_church, n_records, n_church, n_shelf, n_pending, shelf_html, bench_html, n_church, roster_html, n_records, n_copper, n_jacobs)

open("/mnt/user-data/outputs/legacy-library-directory.html","w").write(page)
print("written", len(page), "bytes; shelf", len(SHELF), "+ bench", len(BENCH), "; profiled-flagged", count_profiled, "; pending", n_pending)
