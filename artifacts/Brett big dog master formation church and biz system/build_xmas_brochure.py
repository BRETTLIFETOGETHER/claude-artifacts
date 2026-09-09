#!/usr/bin/env python3
"""
Lifetogether Christmas Campaign System — Professional Brochure
200 campaigns across 20 categories (10 INTO + 10 OUT)
Designed for pastor/church presentation
"""

import html as hlib
def e(s): return hlib.escape(str(s))

# ─── ALL 200 CAMPAIGN TITLES ──────────────────────────────────────────────────

INTO_CATS = [
  {
    "num": 1, "name": "Preparing the Heart",
    "desc": "Interior readiness — forming the congregation's soul before Christmas arrives",
    "arc": "Coming In",
    "campaigns": [
      ("Prepare Him Room",         "A 4-Week Advent Series on Making Interior Space for the Incarnation"),
      ("Waiting Well",             "21 Days of Formation in the Spiritual Discipline of Anticipation"),
      ("The Longest Advent",       "40 Days Connecting Israel's Four-Century Wait to Your Four Weeks"),
      ("One Week Before",          "A 7-Day Formation Sprint for the Final Week of Advent"),
      ("The Four Candles",         "A 4-Week Series on Hope, Peace, Joy, and Love — In That Order"),
      ("Darkness Before Dawn",     "21 Days of Honest Advent for the Congregation That Is Not Feeling Festive"),
      ("The Posture of Advent",    "7 Days on the Physical and Spiritual Posture of Expectant Waiting"),
      ("Come Lord Jesus",          "A 4-Week Series on Maranatha — The Church's Oldest Prayer"),
      ("From Malachi to Matthew",  "A 6-Week Series Covering the 400 Years of Silence Before Bethlehem"),
      ("The Advent of the Afflicted","3 Weeks on the People Advent Belongs To — The Broken, the Mourning, the Displaced"),
    ]
  },
  {
    "num": 2, "name": "The Prophetic Preparation",
    "desc": "The Old Testament prophecies that make Christmas inevitable — traced in formation depth",
    "arc": "Coming In",
    "campaigns": [
      ("The Long Foretold",         "A 6-Week Pre-Christmas Series Through the Messianic Prophecies"),
      ("Seven Prophets, One Promise","7 Days Walking Through the Prophets Who Pointed to Bethlehem"),
      ("Comfort My People",         "A 4-Week Series on Isaiah 40-55 and the Comfort Christmas Delivers"),
      ("The Names He Was Given",    "5 Weeks on the Five Names Prophesied Before the Birth"),
      ("From Exile to Bethlehem",   "40 Days Tracing How God Brought His People Back to Prepare the World"),
      ("The Royal Line",            "21 Days in the Genealogy of Matthew 1 — Every Name a Story"),
      ("Micah's Christmas",         "3 Weeks on the Minor Prophets and the Major Announcement"),
      ("Daniel's Calendar",         "4 Weeks on Daniel 9 and the Chronology That Points to Bethlehem"),
      ("The First Christmas Prophecy","7 Days on Genesis 3:15 — The Announcement Made in a Garden"),
      ("The Jesse Tree Preached",   "3 Weeks of Sermons Built on the Jesse Tree"),
    ]
  },
  {
    "num": 3, "name": "The Incarnation Ahead",
    "desc": "Preparing the congregation theologically before Christmas arrives — going deeper than the manger",
    "arc": "Coming In",
    "campaigns": [
      ("The Scandal Coming",        "A 4-Week Pre-Christmas Series on the Most Offensive Claim Christianity Makes"),
      ("In the Fullness of Time",   "40 Days on What the World Looked Like When God Decided It Was Time"),
      ("Fully God, Fully Human",    "3 Weeks on the Doctrine of the Hypostatic Union"),
      ("The Condescension",         "21 Days on What It Cost the Son to Become a Servant — Philippians 2"),
      ("Emmanuel — God Is Actually Here","4 Weeks Building the Immanuel Theology Before Christmas Eve"),
      ("The Word Before the Flesh", "7 Days on John 1:1-3 — Who the Word Was Before Bethlehem"),
      ("He Became What He Was Not", "5 Weeks on the Exchange at the Heart of the Incarnation"),
      ("The Heresies That Help",    "21 Days Using Ancient Christmas Heresies as Formation Tools"),
      ("Born of a Woman",           "4 Weeks on What It Means That the Son of God Was Born"),
      ("Before the Manger",         "3 Weeks on the Pre-Existence of Christ"),
    ]
  },
  {
    "num": 4, "name": "The Formation Practices",
    "desc": "Campaigns built around specific Advent spiritual disciplines — embodied formation before Christmas",
    "arc": "Coming In",
    "campaigns": [
      ("Silent and Holy",           "A 4-Week Advent Counterformation Campaign — Silence Against the Noise"),
      ("The Advent Office",         "40 Days of Morning Prayer, Evening Prayer, and Night Prayer"),
      ("The Advent Fast",           "4 Weeks on What Advent Fasting Does That Advent Feasting Cannot"),
      ("The Advent Home",           "7 Days of Household Formation Practices Through the Week Before Christmas"),
      ("Advent Reads",              "21 Days — One Passage, One Reflection, One Practice, One Prayer"),
      ("The Generous Advent",       "4 Weeks of Formation Practices That Counterform the Consumerism of December"),
      ("Advent Prays",              "3 Weeks of Corporate Prayer Practices — Lament, Intercession, Praise"),
      ("The Advent Body",           "7 Days of Physical Formation Practices — Kneeling, Fasting, Serving"),
      ("The Longest Night Campaign","6 Weeks of Formation for the Congregation That Is in the Dark This Advent"),
      ("Advent in the Family",      "21 Days of Family Formation Practices Around the Table"),
    ]
  },
  {
    "num": 5, "name": "The Outreach Window",
    "desc": "Campaigns that use Advent and Christmas as the congregation's primary outreach formation season",
    "arc": "Coming In",
    "campaigns": [
      ("Come and See",              "A 4-Week Advent Outreach Campaign — Forming the Congregation to Invite Before Christmas Eve"),
      ("Invite One",                "A 4-Week Series Built Around the Discipline of the Christmas Eve Invitation"),
      ("Good News for All People",  "21 Days Forming the Congregation to Announce What the Angels Announced"),
      ("The Most Unchurched Sunday","3 Weeks of Formation for the Congregation That Understands Christmas Eve Is Its Highest-Stakes Sunday"),
      ("The Gift That Keeps",       "4 Weeks of Outreach Formation — What to Give the Person Who Has Everything Except What Matters"),
      ("Seven Days of Invitation",  "7 Days of Formation Practices That Build the Congregation's Invitational Posture"),
      ("The Advent Witness",        "40 Days of Formation in Personal Testimony — How to Tell Your Christmas Story"),
      ("50 for Christmas",          "3 Weeks Building the Congregation's Culture of Inviting 50 Specific People"),
      ("Advent for the Skeptic",    "21 Days of Formation for the Congregation Member Who Has Skeptical Friends"),
      ("Table for More",            "4 Weeks Building the Culture of Hospitality That Makes Invitations Natural"),
    ]
  },
  {
    "num": 6, "name": "The Justice Advent",
    "desc": "Campaigns that connect the incarnation to justice, mercy, and care for the vulnerable",
    "arc": "Coming In",
    "campaigns": [
      ("The King Who Came for the Poor","A 4-Week Advent Justice Series on the Political and Economic Announcement of the Manger"),
      ("The Magnificat Formation",  "40 Days on Mary's Song — The Most Radical Formation Text of the Christmas Season"),
      ("Advent for the Homeless",   "3 Weeks on the Incarnation as Formation for the Congregation's Homeless Ministry"),
      ("The Lonely Advent",         "21 Days of Formation for the Congregation That Wants to Reach Those Who Are Alone"),
      ("A Different Kind of Christmas","4 Weeks of Advent Formation Around Spending Less and Giving More"),
      ("Seven Acts of Advent Mercy","7 Days of Embodied Advent Formation — One Act of Mercy Per Day"),
      ("Advent and the Refugee",    "3 Weeks on the Flight to Egypt — Formation for the Congregation's Refugee Ministry"),
      ("What Would Jesus Give",     "21 Days of Advent Formation on Christlike Generosity"),
      ("Advent and the Prisoner",   "4 Weeks on Luke 4:18 — The Incarnation Campaign Built on Jesus' Mission Statement"),
      ("The Upside-Down Kingdom",   "6 Weeks on the Beatitudes as the Advent Formation Series"),
    ]
  },
  {
    "num": 7, "name": "Family Formation",
    "desc": "Campaigns that form the household around the incarnation in the Advent season",
    "arc": "Coming In",
    "campaigns": [
      ("The Family That First Received","A 4-Week Advent Family Formation Series — What the Holy Family's Formation Looks Like in Yours"),
      ("The Advent Table",          "21 Days of Table Formation Practices for Households in Advent"),
      ("Joseph and Fatherhood",     "3 Weeks on Joseph — The Father Who Obeyed Before He Understood"),
      ("Mary and Motherhood",       "4 Weeks on Mary — The Formation of the Woman Who Said Yes"),
      ("Advent With Your Children", "7 Days of Family Formation Practices for Parents and Children"),
      ("The Formation Household",   "40 Days of Advent and Christmas Formation Practices for the Home"),
      ("Grandparents and Christmas","3 Weeks on the Formation Gift That Grandparents Give at Christmas"),
      ("The Single Parent's Advent","21 Days of Formation for the Congregation's Single Parents"),
      ("Traditions That Form",      "4 Weeks on the Difference Between Christmas Traditions That Form and Those That Are Merely Habit"),
      ("The Advent of the Prodigal","6 Weeks of Formation for the Family With a Missing Member at Christmas"),
    ]
  },
  {
    "num": 8, "name": "Worship and Music",
    "desc": "Campaigns that form the congregation's worship life around the incarnation",
    "arc": "Coming In",
    "campaigns": [
      ("The Songs They Sang",       "A 4-Week Advent Worship Formation Series — The Magnificat, Benedictus, Nunc Dimittis, Gloria"),
      ("Advent Hymns Deeply",       "21 Days of Formation Through the Great Advent Hymns"),
      ("Sing a New Song",           "4 Weeks on What It Means to Worship the God Who Entered Creation"),
      ("The Gloria",                "3 Weeks on the Angels' Christmas Song — Glory to God in the Highest, Peace on Earth"),
      ("Seven Songs of Advent",     "7 Days in the Great Songs of the Season — From the Psalms to the Magnificat"),
      ("The Music of the Incarnation","40 Days on What the Church Has Sung About Christmas for Two Thousand Years"),
      ("O Come O Come Emmanuel",    "3 Weeks on the Most Theologically Dense Advent Hymn"),
      ("When Heaven Sang",          "21 Days on What the Angels Were Announcing When They Appeared to the Shepherds"),
      ("The Silent Night Campaign", "4 Weeks on Why the Most Famous Christmas Song Is the Most Formation-Rich"),
      ("Worship Before the Manger", "6 Weeks Forming the Congregation's Posture of Worship Before Christmas Eve"),
    ]
  },
  {
    "num": 9, "name": "Preaching Formation",
    "desc": "Campaigns that help pastors and preaching teams prepare to preach Christmas with fresh power",
    "arc": "Coming In",
    "campaigns": [
      ("The Fresh Angle",           "A 4-Week Pre-Christmas Preaching Formation Series for the Pastor Who Has Preached It Twenty Times"),
      ("Seven Angles on the Nativity","7 Days of Preaching Preparation — One Fresh Angle Per Day on the Christmas Text"),
      ("The Formation Sermon",      "3 Weeks of Pre-Christmas Sermon Development — How to Preach Christmas as Formation"),
      ("The Congregation You Are Preaching To","4 Weeks of Congregational Analysis Before Christmas Eve"),
      ("The Preaching Community",   "21 Days of Shared Preaching Preparation — Staff, Elders, Teaching Team Through Advent"),
      ("Christmas Preaching History","6 Weeks of Formation Through the Greatest Christmas Sermons Ever Preached"),
      ("Preach the Incarnation",    "40 Days of Theological Formation for the Pastor Who Wants to Preach Christmas With Depth"),
      ("The Unpreached Text",       "3 Weeks on the Christmas Texts Nobody Preaches — And Why They Should"),
      ("The Outreach Christmas Eve Sermon","21 Days of Preparation for the Most Important Sermon of the Year"),
      ("The Formation Christmas Series","4 Weeks of Curriculum Development — Building the Formation Series Before Christmas"),
    ]
  },
  {
    "num": 10, "name": "Community Engagement",
    "desc": "Campaigns that carry the congregation into their community during Advent and Christmas",
    "arc": "Coming In",
    "campaigns": [
      ("Light in the Neighborhood", "A 4-Week Advent Community Engagement Campaign — Forming the Congregation to Be the Light It Celebrates"),
      ("Advent Serves",             "40 Days of Advent Service Formation — One Act of Service Per Day"),
      ("The City at Christmas",     "3 Weeks on What the Incarnation Demands of the Congregation's Relationship to Its City"),
      ("Table for the Stranger",    "21 Days of Hospitality Formation — What the Incarnation Demands of the Welcome of Outsiders"),
      ("Advent Partnership",        "4 Weeks of Community Partnership Formation — Connecting to Organizations Serving the City"),
      ("Seven Days of Community Formation","7 Days of Advent Engagement Practices — The Congregation in Its Community"),
      ("The Advent Witness in the Workplace","6 Weeks of Formation for the Congregation's Witness at Work in December"),
      ("Advent Generosity in the Community","21 Days of Community Generosity Formation"),
      ("The Most Wonderful Time for Mission","3 Weeks on Why December Is the Church's Highest-Leverage Outreach Month"),
      ("From Sanctuary to Street",  "40 Days of Formation in the Movement From Inside the Building to Outside It"),
    ]
  },
]

OUT_CATS = [
  {
    "num": 1, "name": "Living the Incarnation",
    "desc": "Campaigns that translate the Christmas announcement into daily formation in the new year",
    "arc": "Coming Out",
    "campaigns": [
      ("The Incarnation Every Monday","A 6-Week Post-Christmas Series on Living From the Incarnation Rather Than Just Receiving It"),
      ("God With Us — Still",       "40 Days Forming the Congregation to Practice the Presence of God in the Ordinary Year"),
      ("The Flesh of It",           "21 Days on What It Means to Live an Embodied Spiritual Life After Christmas"),
      ("Incarnational Living",      "4 Weeks on What It Means to Be Sent Into the World the Way the Son Was Sent"),
      ("Seven Ways Christmas Changes Monday","7 Days of Specific Application — How the Incarnation Changes Your Work, Money, Relationships"),
      ("The Light After Christmas", "3 Weeks on What It Means to Carry the Light When the Cultural Christmas Is Over"),
      ("Emmanuel — Now What",       "6 Weeks of Formation on the Specific Implications of God Being With Us"),
      ("January Formation",         "21 Days of Post-Christmas Formation Practices That Carry the Incarnation Into the New Year"),
      ("The Permanent Incarnation", "40 Days on the Ascension — Why Jesus Did Not Stop Being Human"),
      ("The Body He Still Has",     "4 Weeks on the Bodily Resurrection and Ascension and What That Means for Your Body"),
    ]
  },
  {
    "num": 2, "name": "The Epiphany Season",
    "desc": "Campaigns that carry the congregation from Christmas to Epiphany and the revelation to the nations",
    "arc": "Coming Out",
    "campaigns": [
      ("The Light to the Nations",  "A 6-Week Post-Christmas Epiphany Series on the Global Reach of the Incarnation"),
      ("What the Magi Knew",        "4 Weeks on the Formation of the Wise Men — What They Followed, Found, and Gave"),
      ("The Twelve Days",           "7 Days of Post-Christmas Formation — One Practice Per Day Through Epiphany"),
      ("Star Followers",            "3 Weeks on What It Means to Follow the Evidence Wherever It Leads"),
      ("Epiphany Formation",        "21 Days of Formation in the Season the Church Has Almost Forgotten"),
      ("Beyond the Manger",         "4 Weeks Carrying the Congregation From the Manger to the Mission"),
      ("The Presentation",          "6 Weeks on Luke 2:22-52 — What Happened After the Manger"),
      ("Gifts Worth Giving",        "3 Weeks on What the Magi Gave and What the Congregation Is Invited to Give in Response"),
      ("The Year of the Lord",      "21 Days on Isaiah 61 and Luke 4 — Launching the Year with Jesus' Mission Statement"),
      ("Before He Was Preaching",   "7 Days on the Thirty Hidden Years — What Jesus Was Doing Before His Ministry"),
    ]
  },
  {
    "num": 3, "name": "The New Year Bridge",
    "desc": "Campaigns that carry the congregation from Christmas directly into New Year formation",
    "arc": "Coming Out",
    "campaigns": [
      ("New Year, New Creation",    "A 6-Week Bridge Campaign From Christmas Eve to Mid-January"),
      ("Christmas to January 1",    "7 Days of Formation Between Christmas Day and New Year's Day"),
      ("The Resolution the Gospel Offers","21 Days on What the Incarnation Offers That Self-Help Cannot"),
      ("Fresh Start, Full Gospel",  "4 Weeks Connecting the New Year to the Incarnation — Not a Resolution, a Resurrection"),
      ("January Formation",         "3 Weeks of Formation for the Congregation That Wants to Make the New Year Different"),
      ("From Bethlehem to Jordan",  "40 Days From Christmas to the Baptism of Jesus — The Formation Arc"),
      ("The Small Group That Christmas Started","A 6-Week Post-Christmas Small Group Launch Campaign"),
      ("The Year He Has Prepared",  "21 Days on Psalm 90 and the Theology of Time"),
      ("Word for the Year",         "4 Weeks of Formation Around Choosing One Word to Carry Through the Year"),
      ("Seven Days That Shape the Year","7 Days of Formation Between Christmas and New Year That Determine What the Year Becomes"),
    ]
  },
  {
    "num": 4, "name": "The Small Group Season",
    "desc": "Campaigns designed to launch small groups in the post-Christmas formation window",
    "arc": "Coming Out",
    "campaigns": [
      ("Gather After the Gift",     "A 4-Week Post-Christmas Campaign Built to Launch Small Groups in January"),
      ("The Incarnation Community", "6 Weeks on Acts 2 — What the Community Looks Like That the Incarnation Produced"),
      ("God With Us Together",      "4 Weeks of Post-Christmas Community Formation — What Immanuel Means in a Small Group"),
      ("The Table After Christmas", "7 Days of Formation Around the Table — What the Christmas Table Started"),
      ("Devoted",                   "3 Weeks on Acts 2:42 — Four Practices That Build the Post-Christmas Community"),
      ("One Another",               "6 Weeks on the One Another Commands — Building the Relational Infrastructure"),
      ("The Winter Small Group",    "21 Days of Formation Content Designed for Post-Christmas Small Group Launch"),
      ("From House to House",       "4 Weeks on the Early Church's Practice of House-to-House Formation"),
      ("The Post-Christmas Congregation","3 Weeks of Vision Casting for the Community the Incarnation Is Building"),
      ("The Formation Year",        "40 Days Launching the Annual Formation Arc — From Christmas Into the Year"),
    ]
  },
  {
    "num": 5, "name": "Generosity Season",
    "desc": "Campaigns that carry the generosity formed at Christmas into the new year",
    "arc": "Coming Out",
    "campaigns": [
      ("The First Gift of the Year","A 4-Week Post-Christmas Generosity Campaign — What You Do With Resources in January"),
      ("God So Loved He Gave",      "21 Days on John 3:16 — The Formation of Generosity From the Theology of the Incarnation"),
      ("The Steward in January",    "3 Weeks of Stewardship Formation for the New Year"),
      ("First Fruits of the Year",  "4 Weeks on the Formation Practice of Giving the First and Best of the Year"),
      ("Seven Ways to Give in January","7 Days of Post-Christmas Generosity Practices — Money, Time, Skill, Presence, Prayer"),
      ("The Year of Generous Living","6 Weeks Launching the Annual Generosity Formation Arc"),
      ("What Gold Frankincense and Myrrh Actually Cost","21 Days on the Formation Theology of the Magi's Gifts"),
      ("The Generous Community",    "3 Weeks Building the Culture of Communal Generosity"),
      ("Legacy in January",         "4 Weeks of Post-Christmas Legacy Formation — What You Leave and Who You Leave It For"),
      ("The Generous Year",         "40 Days of Formation in the Posture, Practice, and Theology of Generosity"),
    ]
  },
  {
    "num": 6, "name": "Mission and Witness",
    "desc": "Campaigns that carry the outreach energy of Christmas into the new year",
    "arc": "Coming Out",
    "campaigns": [
      ("As the Father Sent Me",     "A 6-Week Post-Christmas Mission Formation Campaign Built on John 20:21"),
      ("The Witness of January",    "4 Weeks on What to Do With the People Who Came to Christmas Eve But Have Not Been Back"),
      ("Witnesses",                 "40 Days Forming the Congregation in Personal Testimony — How to Tell Your Story"),
      ("The Magi's Method",         "3 Weeks on the Outreach Formation of the Magi — Seeking, Finding, Worshipping, Going"),
      ("Good News for All People — Still","21 Days Carrying the Christmas Announcement Into the New Year"),
      ("The Post-Christmas Invitation","6 Weeks of Formation for the Congregation That Invited People and Wants to See Them Stay"),
      ("The Sent Life",             "4 Weeks on What It Means to Live as Someone Who Has Been Sent"),
      ("Epiphany Outreach",         "21 Days of Post-Christmas Outreach Formation — From the Magi to Your Neighborhood"),
      ("A Light to the Nations",    "3 Weeks on Isaiah 60 and the Epiphany Commission"),
      ("The Year of Witness",       "40 Days Launching the Annual Evangelism Formation Arc"),
    ]
  },
  {
    "num": 7, "name": "Discipleship Launch",
    "desc": "Campaigns that use the post-Christmas window to launch the year's discipleship arc",
    "arc": "Coming Out",
    "campaigns": [
      ("Follow Me — Again",         "A 6-Week Post-Christmas Discipleship Series on What Following Jesus Looks Like in the New Year"),
      ("The Formation Year",        "40 Days Launching the Congregation's Annual Formation Arc"),
      ("Abide",                     "4 Weeks on John 15 — The Formation Practice the Post-Christmas Season Is Designed to Build"),
      ("Daily Formation",           "21 Days of Building the Daily Practices That Carry Through the Year"),
      ("The Disciple's New Year",   "3 Weeks on What Discipleship Looks Like Differently This Year"),
      ("The Sermon on the Mount",   "6 Weeks Launching the Year's Discipleship With the Greatest Teaching in the Gospels"),
      ("Mentored by Jesus",         "21 Days of Formation in the Practices of Jesus — How He Prayed, Ate, Rested, Worked"),
      ("Identity Before Activity",  "4 Weeks on Who You Are Before What You Do — Formation of Identity From the Incarnation"),
      ("Spiritual Disciplines for the Year","40 Days Launching the Congregation Into the Classic Spiritual Disciplines"),
      ("The Kingdom Life",          "6 Weeks on What It Means to Live Under the Rule of Jesus in the Ordinary Year"),
    ]
  },
  {
    "num": 8, "name": "Healing and Restoration",
    "desc": "Campaigns that carry Christmas hope into the congregation's healing ministry in the new year",
    "arc": "Coming Out",
    "campaigns": [
      ("He Healed Them All",        "A 6-Week Post-Christmas Healing Formation Campaign on What the Incarnation Says to Broken Things"),
      ("Recovery After Christmas",  "21 Days of Post-Christmas Healing Formation for the Congregation That Is Exhausted or Depleted"),
      ("The God Who Heals",         "4 Weeks on Healing Theology — What the Incarnation Claims About Physical, Emotional, Relational Healing"),
      ("The Year of Restoration",   "3 Weeks Launching the New Year With Isaiah 61"),
      ("Wholeness",                 "40 Days of Formation in the Biblical Vision of Shalom — The Wholeness the Incarnation Came to Restore"),
      ("Renewing Your Mind",        "21 Days on Romans 12:2 — The Post-Christmas Formation Campaign on Cognitive Renewal"),
      ("Carrying One Another",      "4 Weeks on Galatians 6:2 — The Formation of the Healing Community"),
      ("The Broken Welcome",        "3 Weeks on the Incarnation as the Theology of Welcome"),
      ("The January Restoration",   "6 Weeks of Formation for the Congregation Navigating Difficulty at the Start of the Year"),
      ("The God Who Sees",          "21 Days on the Formation of Being Known and Seen — What the Incarnation Says to the Invisible"),
    ]
  },
  {
    "num": 9, "name": "Stewardship of Time",
    "desc": "Campaigns that use the new year to form the congregation's relationship with time",
    "arc": "Coming Out",
    "campaigns": [
      ("Teach Us to Number Our Days","A 4-Week Post-Christmas Series on Psalm 90 — The Formation of a Congregation That Uses Time Well"),
      ("The Redeemed Calendar",     "21 Days of Formation in What It Means to Bring Your Year to God Before You Know What It Holds"),
      ("Sabbath in the New Year",   "4 Weeks of Formation in the Practice of Sabbath as the Foundation of the Year's Rhythm"),
      ("The First Week of the Year","7 Days of Formation Practices That Order the Year From the Beginning"),
      ("Seasons of Formation",      "3 Weeks on the Formation That Belongs to Each Season — What January Is For"),
      ("The Formation Rhythm",      "40 Days of Building the Daily, Weekly, Monthly, and Annual Practices"),
      ("Morning by Morning",        "21 Days of Formation in the Practice of Morning Prayer — How the First Hour Determines the Rest"),
      ("Ordering Your Life",        "6 Weeks on the Formation of a Rule of Life"),
      ("The Examined Year",         "4 Weeks of Post-Christmas Reflection on the Year Just Completed and the Year Beginning"),
      ("The Formation Inventory",   "21 Days of Post-Christmas Reflection — A Complete Formation Inventory"),
    ]
  },
  {
    "num": 10, "name": "Vision and Leadership",
    "desc": "Campaigns that use the post-Christmas window to form the congregation's vision and leadership for the year",
    "arc": "Coming Out",
    "campaigns": [
      ("The Year He Has Given",     "A 6-Week Post-Christmas Vision Campaign — Forming the Congregation Around the Year's Formation Direction"),
      ("The Vision Fast",           "40 Days of Post-Christmas Vision Formation — Prayer, Fasting, and Seeking for the Year Ahead"),
      ("The Nehemiah Year",         "4 Weeks on Nehemiah 1-2 — Building Vision From Prayer, Grief, Assessment, and Action"),
      ("The Pastoral Vision",       "3 Weeks of Formation for the Senior Leadership Team"),
      ("The Formation Vision",      "21 Days of Post-Christmas Formation for the Congregation's Leaders"),
      ("The Mission Alignment",     "6 Weeks of Post-Christmas Mission Alignment — Forming Every Ministry Around One Formation Direction"),
      ("The Elders in January",     "4 Weeks of Post-Christmas Elder Formation"),
      ("The Staff Formation Retreat","21 Days of Post-Christmas Staff Formation — Building the Team That Will Form the Congregation"),
      ("The Year in One Direction", "3 Weeks of Post-Christmas Vision Clarity — One Priority, One Year, One Direction"),
      ("From Christmas to the Vision Sunday","40 Days of Post-Christmas Formation Leading to the Annual Vision Sunday"),
    ]
  },
]

# ─── STYLES ───────────────────────────────────────────────────────────────────

CSS = """
:root{
  --navy:#02040a;--gold:#c9a84c;--gold-lt:#e2c97e;--gold-dk:#8a6e30;
  --cream:#f7f4ed;--ink:#0d1018;--muted:#7a7a8a;
  --into:#2a4568;--out:#6a3020;
  --into-lt:#e8edf4;--out-lt:#f5ede8;
  --into-border:#c0cedf;--out-border:#dfc5b8;
  --rule:rgba(201,168,76,.09);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Lato',sans-serif;background:#bebab2;color:var(--ink);}
.page{max-width:1200px;margin:0 auto;background:var(--cream);box-shadow:0 6px 80px rgba(0,0,0,.28);}

/* ── COVER ─────────────────────────────────────────────────── */
.cover{background:var(--navy);min-height:100vh;display:flex;flex-direction:column;position:relative;overflow:hidden;}
.cover-glow{position:absolute;inset:0;background:
  radial-gradient(ellipse at 20% 75%,rgba(42,69,104,.18),transparent 52%),
  radial-gradient(ellipse at 78% 22%,rgba(106,48,32,.12),transparent 52%),
  radial-gradient(ellipse at 50% 50%,rgba(30,30,50,.06),transparent 70%),
  linear-gradient(180deg,#010205,#020408);}
.cover-header{padding:48px 72px 0;position:relative;z-index:2;display:flex;justify-content:space-between;align-items:flex-start;}
.cover-logo{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;color:rgba(255,255,255,.3);letter-spacing:2px;}
.cover-tag{font-size:7px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:var(--gold-dk);border:1px solid rgba(201,168,76,.2);padding:5px 13px;}

/* hero area */
.cover-hero{flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding:0 72px 64px;position:relative;z-index:2;}
.cover-eyebrow{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;color:rgba(201,168,76,.75);display:flex;align-items:center;gap:14px;margin-bottom:20px;}
.cover-eyebrow::before{content:'';width:32px;height:1px;background:rgba(201,168,76,.45);}
.cover-h1{font-family:'Playfair Display',serif;font-size:clamp(52px,7vw,110px);font-weight:400;line-height:.84;color:#fff;letter-spacing:-3px;margin-bottom:24px;}
.cover-h1 em{font-style:italic;color:var(--gold);}
.cover-divider{display:flex;align-items:center;gap:14px;margin-bottom:24px;}
.cover-divider-line{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.cover-divider-dot{width:6px;height:6px;background:var(--gold);transform:rotate(45deg);flex-shrink:0;}
.cover-subtitle{font-family:'Playfair Display',serif;font-size:clamp(16px,2.2vw,24px);font-weight:300;font-style:italic;color:rgba(205,188,158,.82);max-width:680px;line-height:1.55;margin-bottom:48px;}

/* stats row */
.cover-stats{display:grid;grid-template-columns:repeat(6,1fr);border:1px solid rgba(201,168,76,.18);max-width:840px;}
.cstat{padding:16px 14px;border-right:1px solid rgba(201,168,76,.12);text-align:center;}
.cstat:last-child{border-right:none;}
.cstat-n{font-family:'Playfair Display',serif;font-size:24px;color:var(--gold);display:block;line-height:1;}
.cstat-l{font-size:6px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.2);font-weight:700;display:block;margin-top:4px;}

/* ── INTRO SPREAD ──────────────────────────────────────────── */
.intro{background:var(--navy);padding:52px 72px 56px;border-bottom:3px solid rgba(201,168,76,.12);}
.intro-grid{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start;}
.intro-left{}
.intro-kk{font-size:8px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:rgba(201,168,76,.6);display:flex;align-items:center;gap:10px;margin-bottom:16px;}
.intro-kk::before{content:'';width:16px;height:1px;background:rgba(201,168,76,.4);}
.intro-h2{font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,44px);font-weight:400;color:#fff;line-height:.92;margin-bottom:16px;}
.intro-h2 em{font-style:italic;color:var(--gold);}
.intro-body{font-family:'Georgia',serif;font-size:14.5px;color:rgba(192,178,156,.75);line-height:1.78;}
.intro-body p{margin-bottom:14px;}
.intro-body strong{color:rgba(220,205,175,.9);font-weight:400;}
.into-pill,.out-pill{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;margin-bottom:12px;font-size:11px;font-weight:700;letter-spacing:.5px;}
.into-pill{background:rgba(42,69,104,.25);border:1px solid rgba(42,69,104,.4);color:#8aabd4;}
.out-pill{background:rgba(106,48,32,.25);border:1px solid rgba(106,48,32,.4);color:#d4987a;}
.pill-dot{width:7px;height:7px;border-radius:50%;}
.into-pill .pill-dot{background:#6a8aba;}
.out-pill .pill-dot{background:#c07858;}
.intro-cats{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:20px;}
.intro-cat{padding:10px 12px;border-left:3px solid;font-size:11px;}
.intro-cat.into{border-color:var(--into);background:rgba(42,69,104,.15);}
.intro-cat.out{border-color:#6a3020;background:rgba(106,48,32,.15);}
.intro-cat-name{font-family:'Playfair Display',serif;font-style:italic;font-size:12px;color:#fff;display:block;margin-bottom:2px;}
.intro-cat.into .intro-cat-name{color:#a0c0e0;}
.intro-cat.out .intro-cat-name{color:#e0b89a;}
.intro-cat-n{font-size:8.5px;color:rgba(255,255,255,.3);}

/* ── SECTION DIVIDERS ──────────────────────────────────────── */
.sec-div{padding:40px 72px 24px;position:relative;}
.sec-div.into-sec{background:linear-gradient(135deg,#020608,#040b12);border-top:5px solid var(--into);}
.sec-div.out-sec{background:linear-gradient(135deg,#060402,#0d0604);border-top:5px solid var(--out);}
.sec-div-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;display:flex;align-items:center;gap:10px;margin-bottom:16px;}
.sec-div.into-sec .sec-div-kk{color:#6a8aba;}
.sec-div.out-sec .sec-div-kk{color:#c07858;}
.sec-div-kk::before{content:'';width:16px;height:1px;background:currentColor;}
.sec-div-h{font-family:'Playfair Display',serif;font-size:clamp(28px,4vw,58px);font-weight:400;line-height:.9;color:#fff;margin-bottom:12px;}
.sec-div-h em{font-style:italic;}
.sec-div.into-sec .sec-div-h em{color:rgba(100,170,255,.8);}
.sec-div.out-sec .sec-div-h em{color:rgba(255,160,100,.8);}
.sec-div-sub{font-family:'Georgia',serif;font-size:14px;max-width:780px;line-height:1.72;margin-bottom:10px;}
.sec-div.into-sec .sec-div-sub{color:rgba(160,190,220,.65);}
.sec-div.out-sec .sec-div-sub{color:rgba(220,175,145,.65);}
.sec-div-count{font-size:8px;letter-spacing:3px;text-transform:uppercase;font-weight:700;border:1px solid;display:inline-block;padding:4px 14px;margin-top:6px;}
.sec-div.into-sec .sec-div-count{border-color:rgba(80,130,190,.3);color:#6a8aba;}
.sec-div.out-sec .sec-div-count{border-color:rgba(190,110,70,.3);color:#c07858;}

/* ── CATEGORY BLOCK ────────────────────────────────────────── */
.cat-block{margin:0;}
.cat-hdr{display:flex;align-items:flex-start;gap:20px;padding:28px 72px 14px;}
.cat-n{font-family:'Playfair Display',serif;font-size:60px;font-weight:400;line-height:1;flex-shrink:0;margin-top:-12px;}
.into-cat .cat-n{color:rgba(42,69,104,.1);}
.out-cat .cat-n{color:rgba(106,48,32,.1);}
.cat-hdr-text{}
.cat-title{font-family:'Playfair Display',serif;font-size:clamp(22px,3vw,38px);font-weight:400;font-style:italic;line-height:1.1;margin-bottom:5px;}
.into-cat .cat-title{color:var(--into);}
.out-cat .cat-title{color:var(--out);}
.cat-desc{font-size:12px;color:var(--muted);line-height:1.5;max-width:820px;}
.cat-arc{font-size:7px;letter-spacing:2.5px;text-transform:uppercase;font-weight:700;padding:2px 9px;border:1px solid;display:inline-block;margin-top:6px;}
.into-cat .cat-arc{color:var(--into);border-color:rgba(42,69,104,.3);background:rgba(42,69,104,.04);}
.out-cat .cat-arc{color:var(--out);border-color:rgba(106,48,32,.3);background:rgba(106,48,32,.04);}

/* ── CAMPAIGN CARDS ────────────────────────────────────────── */
.campaigns{display:grid;grid-template-columns:repeat(5,1fr);gap:0;padding:0 72px 4px;}

/* border structure */
.camp{padding:14px 15px;border:1px solid rgba(0,0,0,.065);border-top:none;border-left:none;background:rgba(255,255,255,.48);position:relative;transition:background .12s;}
.camp:nth-child(5n+1){border-left:1px solid rgba(0,0,0,.065);}
.camp:nth-child(-n+5){border-top:1px solid rgba(0,0,0,.065);}
.camp:hover{background:rgba(255,255,255,.85);}

/* hero — first card: full width */
.camp-hero{grid-column:1/-1;border-left:1px solid rgba(0,0,0,.065)!important;border-top:1px solid rgba(0,0,0,.065)!important;padding:18px 22px;background:rgba(255,255,255,.75);}
.camp-hero:hover{background:rgba(255,255,255,.95);}

/* size accents */
.into-cat .camp-hero{border-top:3px solid var(--into)!important;}
.out-cat .camp-hero{border-top:3px solid var(--out)!important;}
.into-cat .camp{border-top-color:rgba(42,69,104,.1);}
.out-cat .camp{border-top-color:rgba(106,48,32,.1);}

/* card internals */
.camp-num{font-size:7.5px;letter-spacing:2px;color:#ccc;font-weight:700;display:block;margin-bottom:5px;}
.camp-arc-tag{font-size:6px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:1px 6px;border:1px solid;display:inline-block;margin-bottom:5px;}
.into-cat .camp-arc-tag{color:var(--into);border-color:rgba(42,69,104,.22);}
.out-cat .camp-arc-tag{color:var(--out);border-color:rgba(106,48,32,.22);}
.camp-title{font-family:'Playfair Display',serif;font-style:italic;color:var(--ink);line-height:1.2;margin-bottom:3px;font-size:13px;}
.camp-hero .camp-title{font-size:18px;margin-bottom:6px;}
.camp-sub{font-size:9px;color:#7a6a58;font-family:'Georgia',serif;font-style:italic;line-height:1.35;font-size:9.5px;}
.camp-hero .camp-sub{font-size:12px;line-height:1.5;}

/* highlight border on hover */
.into-cat .camp:hover{border-color:rgba(42,69,104,.18);}
.out-cat .camp:hover{border-color:rgba(106,48,32,.18);}

/* ── BRIDGE ────────────────────────────────────────────────── */
.bridge{padding:36px 72px;text-align:center;background:linear-gradient(90deg,#020408,#06090e,#020408);}
.bridge-rule{display:flex;align-items:center;gap:16px;margin:0 auto;max-width:700px;}
.bridge-rl{flex:1;height:1px;background:rgba(201,168,76,.16);}
.bridge-sym{color:rgba(201,168,76,.35);font-size:20px;}
.bridge-text{font-family:'Playfair Display',serif;font-size:clamp(15px,2.2vw,22px);font-style:italic;color:rgba(201,168,76,.55);max-width:700px;margin:14px auto;line-height:1.5;}

/* ── BACK COVER ────────────────────────────────────────────── */
.hdiv{height:3px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.22),transparent);}
.cat-sdiv{height:1px;background:var(--rule);}
.back{background:#010305;padding:56px 72px;text-align:center;}
.back-quote{font-family:'Playfair Display',serif;font-size:clamp(15px,2.2vw,22px);font-style:italic;color:var(--cream);max-width:780px;margin:0 auto 18px;line-height:1.55;}
.back-attr{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.back-contact{margin-top:14px;font-size:12px;color:#4a5a6a;}
.back-contact a{color:var(--gold-lt);text-decoration:none;}
.back-logo{font-family:'Playfair Display',serif;font-size:32px;color:#fff;font-style:italic;margin-top:26px;}

@media(max-width:1000px){
  .cover-header,.cover-hero,.intro,.sec-div,.cat-hdr,.campaigns,.bridge,.back{padding-left:28px;padding-right:28px;}
  .campaigns{grid-template-columns:1fr 1fr;}
  .camp-hero{grid-column:1/-1;}
  .camp:nth-child(5n+1){border-left:1px solid rgba(0,0,0,.065);}
  .camp:nth-child(-n+5){border-top:1px solid rgba(0,0,0,.065);}
  .camp:nth-child(2n+1){border-left:1px solid rgba(0,0,0,.065)!important;}
  .camp:nth-child(-n+3){border-top:1px solid rgba(0,0,0,.065)!important;}
  .cover-stats{grid-template-columns:repeat(3,1fr);}
  .intro-grid{grid-template-columns:1fr;}
  .intro-cats{grid-template-columns:1fr 1fr;}
}
"""

def build_cat(cat_data, side, start_n):
    cls = "into-cat" if side == "into" else "out-cat"
    arc_label = "Coming Into Christmas" if side == "into" else "Coming Out of Christmas"
    
    cards_html = ""
    for i, (title, subtitle) in enumerate(cat_data["campaigns"]):
        n = start_n + i
        is_hero = (i == 0)
        card_cls = "camp camp-hero" if is_hero else "camp"
        cards_html += f"""<div class="{card_cls}">
  <span class="camp-num">{n:03d}</span>
  <span class="camp-arc-tag">{e(arc_label)}</span>
  <h3 class="camp-title">{e(title)}</h3>
  <p class="camp-sub">{e(subtitle)}</p>
</div>"""
    
    return f"""<div class="cat-block {cls}">
<div class="cat-hdr">
  <div class="cat-n">{cat_data["num"]:02d}</div>
  <div class="cat-hdr-text">
    <h2 class="cat-title">{e(cat_data["name"])}</h2>
    <p class="cat-desc">{e(cat_data["desc"])}</p>
    <span class="cat-arc">{e(arc_label)}</span>
  </div>
</div>
<div class="campaigns">{cards_html}</div>
</div><div class="cat-sdiv"></div>"""

# ─── BUILD HTML ───────────────────────────────────────────────────────────────

INTO_CATS_LIST = [
  (INTO_CATS[0], "into", 1),
  (INTO_CATS[1], "into", 11),
  (INTO_CATS[2], "into", 21),
  (INTO_CATS[3], "into", 31),
  (INTO_CATS[4], "into", 41),
  (INTO_CATS[5], "into", 51),
  (INTO_CATS[6], "into", 61),
  (INTO_CATS[7], "into", 71),
  (INTO_CATS[8], "into", 81),
  (INTO_CATS[9], "into", 91),
]

OUT_CATS_LIST = [
  (OUT_CATS[0], "out", 101),
  (OUT_CATS[1], "out", 111),
  (OUT_CATS[2], "out", 121),
  (OUT_CATS[3], "out", 131),
  (OUT_CATS[4], "out", 141),
  (OUT_CATS[5], "out", 151),
  (OUT_CATS[6], "out", 161),
  (OUT_CATS[7], "out", 171),
  (OUT_CATS[8], "out", 181),
  (OUT_CATS[9], "out", 191),
]

into_html = "\n".join(build_cat(c, s, n) for c,s,n in INTO_CATS_LIST)
out_html  = "\n".join(build_cat(c, s, n) for c,s,n in OUT_CATS_LIST)

# Intro cat list
into_cats_intro = "".join(
  f'<div class="intro-cat into"><span class="intro-cat-name">{e(c["name"])}</span><span class="intro-cat-n">{len(c["campaigns"])} campaigns</span></div>'
  for c in INTO_CATS
)
out_cats_intro = "".join(
  f'<div class="intro-cat out"><span class="intro-cat-name">{e(c["name"])}</span><span class="intro-cat-n">{len(c["campaigns"])} campaigns</span></div>'
  for c in OUT_CATS
)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Lifetogether · Christmas Campaign System · 200 Campaigns</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="page">

<!-- ══ COVER ══════════════════════════════════════════════════ -->
<section class="cover">
  <div class="cover-glow"></div>
  <div class="cover-header">
    <span class="cover-logo">Lifetogether</span>
    <span class="cover-tag">Christmas Campaign System · 2026</span>
  </div>
  <div class="cover-hero">
    <p class="cover-eyebrow">The Complete Engagement System for the Church's Most Important Season</p>
    <h1 class="cover-h1">200<br>Christmas<br><em>Campaigns.</em></h1>
    <div class="cover-divider"><div class="cover-divider-dot"></div><div class="cover-divider-line"></div></div>
    <p class="cover-subtitle">One hundred campaigns that engage your congregation before Christmas arrives. One hundred that carry them after it ends. Twenty categories. Every congregation size. Every ministry context. The complete system for forming the people who inhabit the incarnation year-round.</p>
    <div class="cover-stats">
      <div class="cstat"><span class="cstat-n">200</span><span class="cstat-l">Total Campaigns</span></div>
      <div class="cstat"><span class="cstat-n">100</span><span class="cstat-l">Coming In</span></div>
      <div class="cstat"><span class="cstat-n">100</span><span class="cstat-l">Coming Out</span></div>
      <div class="cstat"><span class="cstat-n">20</span><span class="cstat-l">Categories</span></div>
      <div class="cstat"><span class="cstat-n">7–40</span><span class="cstat-l">Days Each</span></div>
      <div class="cstat"><span class="cstat-n">25<small style="font-size:14px">yrs</small></span><span class="cstat-l">Field-Tested</span></div>
    </div>
  </div>
</section>

<!-- ══ INTRO SPREAD ═══════════════════════════════════════════ -->
<section class="intro">
  <div class="intro-grid">
    <div class="intro-left">
      <p class="intro-kk">The Problem · The System · The Solution</p>
      <h2 class="intro-h2">The congregation that only experiences Christmas<br>on December 24 has been offered<br>an <em>announcement.</em></h2>
      <div class="intro-body">
        <p>The congregation that has been formed through Advent and carried through Epiphany has received the <strong>person.</strong> These 200 campaigns are the difference between the two.</p>
        <p>Most churches engage Christmas as an event — the highest-attendance Sunday of the year with the least formation infrastructure behind it. The people who come on Christmas Eve leave before the formation has had time to do its work. The people who stayed through Advent leave on December 25 before the formation has been extended into the year.</p>
        <p>This system addresses both problems. <strong>100 campaigns coming in</strong> form the congregation before Christmas arrives. <strong>100 campaigns coming out</strong> carry the congregation after it ends. Each campaign is a complete formation arc: a title, a subtitle, a formation goal, and a duration.</p>
      </div>
    </div>
    <div class="intro-right">
      <div class="into-pill"><span class="pill-dot"></span> 100 Campaigns Coming Into Christmas</div>
      <div class="intro-cats">{into_cats_intro}</div>
      <div style="height:18px;"></div>
      <div class="out-pill"><span class="pill-dot"></span> 100 Campaigns Coming Out of Christmas</div>
      <div class="intro-cats">{out_cats_intro}</div>
    </div>
  </div>
</section>

<!-- ══ INTO CHRISTMAS ══════════════════════════════════════════ -->
<div class="hdiv"></div>
<div class="sec-div into-sec">
  <p class="sec-div-kk">Section One · 100 Campaigns</p>
  <h2 class="sec-div-h"><em>Coming Into</em><br>Christmas</h2>
  <p class="sec-div-sub">Ten formation pathways that engage your congregation before Christmas arrives — building interior readiness, theological depth, family formation, outreach posture, justice formation, worship preparation, and preaching depth for December 24.</p>
  <span class="sec-div-count">100 Campaigns · 10 Categories · 10 Campaigns Each</span>
</div>

{into_html}

<!-- ══ BRIDGE ═══════════════════════════════════════════════════ -->
<div class="bridge">
  <div class="bridge-rule"><div class="bridge-rl"></div><div class="bridge-sym">✦</div><div class="bridge-rl"></div></div>
  <p class="bridge-text">The congregation formed in Advent receives Christmas differently. The congregation carried after Christmas lives the incarnation rather than only celebrating it.</p>
  <div class="bridge-rule"><div class="bridge-rl"></div><div class="bridge-sym">✦</div><div class="bridge-rl"></div></div>
</div>

<!-- ══ OUT OF CHRISTMAS ════════════════════════════════════════ -->
<div class="sec-div out-sec">
  <p class="sec-div-kk">Section Two · 100 Campaigns</p>
  <h2 class="sec-div-h"><em>Coming Out of</em><br>Christmas</h2>
  <p class="sec-div-sub">Ten formation pathways that keep the congregation in the formation of Christmas after December 25 — through Epiphany, into the New Year, launching small groups, generosity, mission, discipleship, healing, time stewardship, and leadership formation.</p>
  <span class="sec-div-count">100 Campaigns · 10 Categories · 10 Campaigns Each</span>
</div>

{out_html}

<!-- ══ BACK COVER ══════════════════════════════════════════════ -->
<div class="hdiv"></div>
<section class="back">
  <p class="back-quote">"The congregation that experiences Christmas once a year has received an announcement. The congregation formed through Advent and carried through Epiphany has received the person. These 200 campaigns are the difference between the two."</p>
  <p class="back-attr">Brett Eastman · Founder, Lifetogether</p>
  <p class="back-contact">
    <a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &nbsp;·&nbsp;
    <a href="https://lifetogether.com">lifetogether.com</a> &nbsp;·&nbsp;
    25 Years · 500+ Church Relationships · 50M+ Campaigns Distributed
  </p>
  <div class="back-logo">Lifetogether</div>
</section>

</div>
</body>
</html>"""

out_path = "/mnt/user-data/outputs/lifetogether-christmas-campaigns.html"
with open(out_path, "w") as f:
    f.write(HTML)

import re
total_camps = len(re.findall(r'class="camp', HTML))
print(f"Done — {total_camps} campaign cards — {len(HTML):,} chars")
