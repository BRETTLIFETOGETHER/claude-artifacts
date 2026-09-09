import { useState, useMemo, useCallback } from "react";

// ─── 400 CAMPAIGNS ────────────────────────────────────────────────────────────
// arc: "into" | "out"   felt: true = new contemporary/felt-need titles

const CATEGORIES = [
  // ════════════════════════════════════════════════════════════
  // COMING INTO CHRISTMAS — 10 categories × 20 campaigns each
  // ════════════════════════════════════════════════════════════
  {
    id:"heart", arc:"into", num:1,
    name:"Preparing the Heart",
    desc:"Interior readiness — forming the congregation's soul before Christmas arrives",
    color:"#3a5888",
    campaigns:[
      // ORIGINAL 10
      {t:"Prepare Him Room",s:"A 4-Week Advent Series on Making Interior Space for the Incarnation"},
      {t:"Waiting Well",s:"21 Days of Formation in the Spiritual Discipline of Anticipation"},
      {t:"The Longest Advent",s:"40 Days Connecting Israel's Four-Century Wait to Your Four Weeks"},
      {t:"One Week Before",s:"A 7-Day Formation Sprint for the Final Week of Advent"},
      {t:"The Four Candles",s:"A 4-Week Series on Hope, Peace, Joy, and Love — In That Order"},
      {t:"Darkness Before Dawn",s:"21 Days of Honest Advent for the Congregation Not Feeling Festive"},
      {t:"The Posture of Advent",s:"7 Days on the Physical and Spiritual Posture of Expectant Waiting"},
      {t:"Come Lord Jesus",s:"A 4-Week Series on Maranatha — The Church's Oldest Prayer"},
      {t:"From Malachi to Matthew",s:"A 6-Week Series on the 400 Years of Silence Before Bethlehem"},
      {t:"The Advent of the Afflicted",s:"3 Weeks on the People Advent Belongs To — The Broken, the Mourning, the Displaced"},
      // CONTEMPORARY 10
      {t:"Tired Before Christmas Even Starts",s:"A 4-Week Advent Series for the Congregation That Is Already Running on Empty — and What Rest Actually Looks Like",felt:true},
      {t:"The Doomscroll Advent",s:"21 Days of Formation for the Congregation That Checks Its Phone More Than It Prays — and What Advent Looks Like Without the Feed",felt:true},
      {t:"Permission to Be Not Okay",s:"A 3-Week Advent Series on Emotional Honesty — What the Church Offers That the Holiday Season Cannot",felt:true},
      {t:"The Anxiety Epidemic at Christmas",s:"4 Weeks on Why December Is the Hardest Month for Mental Health — and What the Incarnation Says Into That",felt:true},
      {t:"Quiet in a Loud December",s:"21 Days of Formation in the Practice of Silence and Slowness When the Culture Is at Maximum Noise",felt:true},
      {t:"I Just Want This Year to Be Over",s:"A 7-Day Advent Formation for the Person Who Is Dragging Themselves to Christmas and Does Not Know Why",felt:true},
      {t:"The Gift Nobody Bought Me",s:"4 Weeks on What You Are Actually Looking for in December — and Why the Manger Is the Only Place That Has It",felt:true},
      {t:"Burnt Out Before Christmas",s:"A 3-Week Advent Series on the Formation That Only Rest Produces — for the Leader, Parent, and Caregiver Who Cannot Find Any",felt:true},
      {t:"When the Magic Doesn't Come",s:"21 Days of Honest Formation for the Person for Whom Christmas Has Lost Its Feeling — and What to Do With That",felt:true},
      {t:"Slower",s:"A 40-Day Advent Counterformation Campaign — One Countercultural Discipline Per Week Against the December Acceleration",felt:true},
    ]
  },
  {
    id:"prophetic", arc:"into", num:2,
    name:"The Prophetic Preparation",
    desc:"The Old Testament prophecies that make Christmas inevitable — traced in formation depth",
    color:"#4a6040",
    campaigns:[
      {t:"The Long Foretold",s:"A 6-Week Pre-Christmas Series Through the Messianic Prophecies from Genesis to Malachi"},
      {t:"Seven Prophets, One Promise",s:"7 Days Walking Through the Prophets Who Pointed to Bethlehem"},
      {t:"Comfort My People",s:"A 4-Week Series on Isaiah 40-55 and the Comfort That Christmas Delivers"},
      {t:"The Names He Was Given",s:"5 Weeks on the Five Names Prophesied Before the Birth — Isaiah 9:6"},
      {t:"From Exile to Bethlehem",s:"40 Days Tracing How God Brought His People Back to Prepare the World for the Manger"},
      {t:"The Royal Line",s:"21 Days in the Genealogy of Matthew 1 — Every Name a Story, Every Story Pointing Forward"},
      {t:"Micah's Christmas",s:"3 Weeks on the Minor Prophets and the Town They Named Seven Centuries Early"},
      {t:"Daniel's Calendar",s:"4 Weeks on Daniel 9 and the Chronology That Points Precisely to Bethlehem"},
      {t:"The First Christmas Prophecy",s:"7 Days on Genesis 3:15 — The Announcement Made in a Garden That Ended in a Stable"},
      {t:"The Jesse Tree Preached",s:"3 Weeks of Sermons Built on the Jesse Tree Formation Practice"},
      // CONTEMPORARY 10
      {t:"The Bible Predicted This",s:"A 4-Week Advent Series on the Prophecies That Make the Christmas Story Impossible to Dismiss — for the Skeptic in Your Congregation",felt:true},
      {t:"History's Most Specific Prediction",s:"21 Days on Micah 5:2 — What It Means That a Town Was Named 700 Years Before the Birth",felt:true},
      {t:"The OT the Magi Were Reading",s:"3 Weeks on Daniel, Balaam, and Isaiah — the Texts That Sent Astronomers From Persia to Bethlehem",felt:true},
      {t:"Christmas Is Jewish",s:"4 Weeks on the Formation the Congregation Needs — Understanding That the Nativity Is a Fulfillment, Not an Innovation",felt:true},
      {t:"Why the Angels Knew the Song",s:"21 Days on the Prophecies the Angels Were Announcing When They Appeared to the Shepherds — They Had Read Isaiah",felt:true},
      {t:"The Longest Story Ever Told",s:"40 Days Tracing the Promise From Eden to Bethlehem — The Formation of the Congregation That Reads the OT as Christmas",felt:true},
      {t:"Six Hundred Years in the Making",s:"A 3-Week Advent Series on Daniel's Seventy Weeks and What It Means That Christmas Happened Exactly on Schedule",felt:true},
      {t:"Mary's Old Testament",s:"7 Days on the Scriptures Mary Knew That Shaped Her Yes — The Formation of a Woman Who Had Memorized the Promise",felt:true},
      {t:"The Genealogy Is the Gospel",s:"21 Days in Matthew 1 — Why Four Women, Why These Names, Why This Order in the Family Tree of Jesus",felt:true},
      {t:"God Did Not Improvise",s:"A 4-Week Advent Series on the Plan That Was in Place Before Creation — Christmas as the Central Act of a Pre-Planned Story",felt:true},
    ]
  },
  {
    id:"incarnation", arc:"into", num:3,
    name:"The Incarnation Ahead",
    desc:"Preparing the congregation theologically before Christmas arrives",
    color:"#285060",
    campaigns:[
      {t:"The Scandal Coming",s:"A 4-Week Pre-Christmas Series on the Most Offensive Claim Christianity Makes"},
      {t:"In the Fullness of Time",s:"40 Days on What the World Looked Like When God Decided It Was Time"},
      {t:"Fully God, Fully Human",s:"3 Weeks on the Doctrine of the Hypostatic Union and Why It Matters"},
      {t:"The Condescension",s:"21 Days on Philippians 2 — What It Cost the Son to Become a Servant"},
      {t:"Emmanuel — God Is Actually Here",s:"4 Weeks Building the Immanuel Theology Before Christmas Eve Arrives"},
      {t:"The Word Before the Flesh",s:"7 Days on John 1:1-3 — Who the Word Was Before Bethlehem Existed"},
      {t:"He Became What He Was Not",s:"5 Weeks on the Exchange at the Heart of the Incarnation — 2 Corinthians 8:9"},
      {t:"The Heresies That Help",s:"21 Days Using Ancient Christmas Heresies as Formation Tools — What the Church Got Wrong Clarifies What Is Right"},
      {t:"Born of a Woman",s:"4 Weeks on What It Means That the Son of God Was Actually Born"},
      {t:"Before the Manger",s:"3 Weeks on the Pre-Existence of Christ — Christmas Does Not Begin in Bethlehem"},
      // CONTEMPORARY
      {t:"God Had a Body",s:"A 4-Week Advent Series on the Physical Reality of the Incarnation — for the Congregation That Has Spiritualized Christmas Into a Metaphor",felt:true},
      {t:"The Creator Became a Creature",s:"21 Days on the Most Mind-Bending Claim in Human History — and Why It Changes Everything About How You See Ordinary Things",felt:true},
      {t:"Not a Symbol",s:"3 Weeks on Why the Incarnation Is a Biological Fact, Not a Spiritual Metaphor — and What Happens When You Take It Seriously",felt:true},
      {t:"God Got Tired",s:"A 4-Week Advent Series on the Physical Humanity of Jesus — Hunger, Thirst, Exhaustion, Grief — and What That Means for Yours",felt:true},
      {t:"The Teenager Who Changed Everything",s:"21 Days on Mary's Formation — A Young Woman Who Said Yes to What She Did Not Fully Understand",felt:true},
      {t:"Upgrade or Rebirth",s:"3 Weeks on the Difference Between What Self-Help Promises and What the Incarnation Offers — They Are Not the Same Product",felt:true},
      {t:"God Moved Into the Neighborhood",s:"40 Days on John 1:14 in Eugene Peterson's Translation — The Formation of the Congregation That Understands Where God Lives",felt:true},
      {t:"Why God Did Not Just Send a Text",s:"7 Days on the Theological Necessity of the Incarnation — Why a Message Was Never Going to Be Enough",felt:true},
      {t:"The Most Vulnerable Thing God Ever Did",s:"4 Weeks on the Risk of the Incarnation — What It Cost the Omnipotent to Become an Infant",felt:true},
      {t:"The Body God Chose",s:"21 Days on the Specific Social Location of the Incarnation — Why Galilee, Why Nazareth, Why a Carpenter's Family",felt:true},
    ]
  },
  {
    id:"practices", arc:"into", num:4,
    name:"The Formation Practices",
    desc:"Campaigns built around specific Advent spiritual disciplines",
    color:"#504028",
    campaigns:[
      {t:"Silent and Holy",s:"A 4-Week Advent Counterformation Campaign — Silence Against the Noise, Stillness Against the Rush"},
      {t:"The Advent Office",s:"40 Days of Morning Prayer, Evening Prayer, and Night Prayer — The Divine Office for Advent"},
      {t:"The Advent Fast",s:"4 Weeks on What Advent Fasting Does That Advent Feasting Cannot"},
      {t:"The Advent Home",s:"7 Days of Household Formation Practices Through the Week Before Christmas"},
      {t:"Advent Reads",s:"21 Days — One Passage, One Reflection, One Practice, One Prayer"},
      {t:"The Generous Advent",s:"4 Weeks of Formation Practices That Counterform the Consumerism of December"},
      {t:"Advent Prays",s:"3 Weeks of Corporate Prayer Practices — Lament, Intercession, Praise"},
      {t:"The Advent Body",s:"7 Days of Physical Formation Practices — Kneeling, Fasting, Rising Early, Serving"},
      {t:"The Longest Night Campaign",s:"6 Weeks of Formation for the Congregation That Is in the Dark This Advent"},
      {t:"Advent in the Family",s:"21 Days of Family Formation Practices Around the Table"},
      // CONTEMPORARY
      {t:"Phone Down, Soul Open",s:"21 Days of Advent Formation Built Around the Practice of Digital Fasting — What You Find When You Put the Screen Down",felt:true},
      {t:"One Thing",s:"A 4-Week Advent Series on the Formation of Simplicity — Doing One Formation Practice Well Instead of Ten Adequately",felt:true},
      {t:"The Five-Minute Advent",s:"7 Days of Formation Practices for the Person Who Has No Time — One Formation Practice Under Five Minutes Per Day",felt:true},
      {t:"Your Body in Advent",s:"21 Days of Embodied Formation Practices — Kneeling, Walking, Fasting, Serving — the Body as the Site of Christmas Formation",felt:true},
      {t:"The Grief Practice",s:"3 Weeks of Formation Practices for the Congregation Member for Whom December Surfaces Loss — What You Do With the Pain",felt:true},
      {t:"Morning and Evening",s:"40 Days of Advent Formation at the Hinges of the Day — Five Minutes in the Morning, Five Minutes Before Sleep",felt:true},
      {t:"The Declutter Advent",s:"A 4-Week Formation Campaign Built on Subtraction — What You Stop Doing in December Creates Space for What Matters",felt:true},
      {t:"Advent Without Alcohol",s:"21 Days of Sober Formation in the Season That Pushes the Hardest — for the Congregation Member Navigating Recovery at Christmas",felt:true},
      {t:"The Reading Advent",s:"6 Weeks of Formation Through the Great Books of the Season — One Chapter Per Day, One Conversation Per Week",felt:true},
      {t:"The Advent Gratitude Practice",s:"7 Days of Formation in the Practice of Radical Gratitude — What Naming What You Have Does to What You Want",felt:true},
    ]
  },
  {
    id:"outreach", arc:"into", num:5,
    name:"The Outreach Window",
    desc:"Campaigns that use Advent and Christmas as the congregation's primary outreach formation season",
    color:"#3a6848",
    campaigns:[
      {t:"Come and See",s:"A 4-Week Advent Outreach Campaign — Forming the Congregation to Invite Before Christmas Eve"},
      {t:"Invite One",s:"A 4-Week Series Built Around the Discipline of the Christmas Eve Invitation"},
      {t:"Good News for All People",s:"21 Days Forming the Congregation to Announce What the Angels Announced"},
      {t:"The Most Unchurched Sunday",s:"3 Weeks of Formation for the Congregation That Understands Christmas Eve Is Its Highest-Stakes Sunday"},
      {t:"The Gift That Keeps",s:"4 Weeks of Outreach Formation — What to Give the Person Who Has Everything Except What Matters Most"},
      {t:"Seven Days of Invitation",s:"7 Days of Formation Practices That Build the Congregation's Invitational Posture Before Christmas"},
      {t:"The Advent Witness",s:"40 Days of Formation in Personal Testimony — How to Tell Your Christmas Story"},
      {t:"50 for Christmas",s:"3 Weeks Building the Congregation's Culture of Inviting 50 Specific People to Christmas Eve"},
      {t:"Advent for the Skeptic",s:"21 Days of Formation for the Congregation Member Who Has Skeptical Friends and Does Not Know What to Say"},
      {t:"Table for More",s:"4 Weeks Building the Culture of Hospitality That Makes Christmas Eve Invitations Natural"},
      // CONTEMPORARY
      {t:"Who Do You Know Who Needs This",s:"A 4-Week Advent Campaign Built Entirely Around One Question — and the Formation of a Congregation That Has a Specific Answer",felt:true},
      {t:"Your De-Churched Friend",s:"21 Days of Formation for the Congregation Member Who Has a Friend Who Used to Go to Church — and Knows Why They Left",felt:true},
      {t:"The Text You Have Not Sent Yet",s:"7 Days of Formation in the Specific, Personal, Non-Generic Invitation — What Inviting Someone Actually Looks Like in Your Life",felt:true},
      {t:"The Coworker at Christmas",s:"3 Weeks of Formation for the Congregation's Witness in the Workplace During December — When the Cultural Christmas Opens the Door",felt:true},
      {t:"Your Neighbor Has Never Been to Church",s:"4 Weeks on the Formation of the Congregation That Knows Its Neighbors — and Has Earned the Right to Invite Them",felt:true},
      {t:"The Christmas Eve Conversation",s:"21 Days of Preparation for the Conversations That Happen After the Service — What You Say When Someone Says It Was Beautiful",felt:true},
      {t:"Bring Someone Who Needs It",s:"A 6-Week Advent Campaign Built Around the Congregation's Personal Invitational Commitment — With Accountability and Prayer",felt:true},
      {t:"The Prodigal in Your Family",s:"3 Weeks of Formation for the Congregation Member Who Has a Prodigal Relative — and Does Not Know How to Invite Them",felt:true},
      {t:"Your Unchurched Kids",s:"4 Weeks of Formation for the Parent Whose Adult Children Have Walked Away — What to Say, What Not to Say, What to Pray",felt:true},
      {t:"The Secular Friend's Christmas",s:"21 Days of Formation in Understanding the Non-Christian Experience of Christmas — and What That Opens",felt:true},
    ]
  },
  {
    id:"justice", arc:"into", num:6,
    name:"The Justice Advent",
    desc:"Campaigns that connect the incarnation to justice, mercy, and care for the vulnerable",
    color:"#5a3a70",
    campaigns:[
      {t:"The King Who Came for the Poor",s:"A 4-Week Advent Justice Series on the Political and Economic Announcement of the Manger"},
      {t:"The Magnificat Formation",s:"40 Days on Mary's Song — The Most Radical Formation Text of the Christmas Season"},
      {t:"Advent for the Homeless",s:"3 Weeks on the Incarnation as Formation for the Congregation's Homeless Ministry"},
      {t:"The Lonely Advent",s:"21 Days of Formation for the Congregation That Wants to Reach Those Who Are Alone at Christmas"},
      {t:"A Different Kind of Christmas",s:"4 Weeks of Advent Formation Around Spending Less and Giving More"},
      {t:"Seven Acts of Advent Mercy",s:"7 Days of Embodied Advent Formation — One Act of Mercy Per Day"},
      {t:"Advent and the Refugee",s:"3 Weeks on the Flight to Egypt — Formation for the Congregation's Refugee Ministry"},
      {t:"What Would Jesus Give",s:"21 Days of Advent Formation on Christlike Generosity Toward the Vulnerable"},
      {t:"Advent and the Prisoner",s:"4 Weeks on Luke 4:18 — The Incarnation Campaign Built on Jesus' Mission Statement"},
      {t:"The Upside-Down Kingdom",s:"6 Weeks on the Beatitudes as the Advent Formation Series"},
      // CONTEMPORARY
      {t:"The Stable Was Not Picturesque",s:"A 4-Week Advent Justice Series on the Economic and Social Reality of the Nativity — God Was Born Into Poverty on Purpose",felt:true},
      {t:"Who Was Not Welcome at the Inn",s:"21 Days of Formation in the Congregation's Relationship to the Unhoused, the Immigrant, the Unseen — the People Who Were at the Manger",felt:true},
      {t:"The Asylum Seeker's Christmas",s:"3 Weeks on Matthew 2:13-15 — The Holy Family as Refugees — and What That Claims About the Congregation's Response",felt:true},
      {t:"While We Were Shopping",s:"4 Weeks of Formation in the Contrast Between the Cultural Christmas Economy and the Economic Announcement of the Incarnation",felt:true},
      {t:"The Loneliest Month",s:"21 Days of Formation for the Congregation That Takes Seriously the Epidemic of Loneliness That December Intensifies",felt:true},
      {t:"The Christmas They Will Not Have",s:"7 Days of Formation Built Around Specific Acts of Justice and Mercy for People in the Congregation's City",felt:true},
      {t:"Mary's Song Is Still Dangerous",s:"3 Weeks on the Magnificat as the Formation Text for the Congregation That Wants to Take Justice Seriously",felt:true},
      {t:"God Was Not Color-Blind",s:"4 Weeks on the Ethnic, Cultural, and Political Specificity of the Incarnation — and What That Says About Who the Manger Is For",felt:true},
      {t:"The Least of These at Christmas",s:"21 Days of Formation in Matthew 25:31-46 as an Advent Text — What Serving the Vulnerable Has to Do With the Manger",felt:true},
      {t:"The Birth Announcement Nobody Received",s:"A 40-Day Formation Campaign on Who Got the Christmas Announcement First — and What That Reveals About the Kingdom's Values",felt:true},
    ]
  },
  {
    id:"family", arc:"into", num:7,
    name:"Family Formation",
    desc:"Campaigns that form the household around the incarnation in the Advent season",
    color:"#703828",
    campaigns:[
      {t:"The Family That First Received",s:"A 4-Week Advent Family Formation Series on the Holy Family's Formation"},
      {t:"The Advent Table",s:"21 Days of Table Formation Practices for Households in Advent"},
      {t:"Joseph and Fatherhood",s:"3 Weeks on Joseph — The Father Who Obeyed Before He Understood"},
      {t:"Mary and Motherhood",s:"4 Weeks on Mary — The Formation of the Woman Who Said Yes"},
      {t:"Advent With Your Children",s:"7 Days of Family Formation Practices for Parents and Children"},
      {t:"The Formation Household",s:"40 Days of Advent and Christmas Formation Practices for the Home"},
      {t:"Grandparents and Christmas",s:"3 Weeks on the Formation Gift That Grandparents Give at Christmas"},
      {t:"The Single Parent's Advent",s:"21 Days of Formation for the Congregation's Single Parents"},
      {t:"Traditions That Form",s:"4 Weeks on the Difference Between Christmas Traditions That Form and Those That Are Merely Habit"},
      {t:"The Advent of the Prodigal",s:"6 Weeks of Formation for the Family With a Missing Member at Christmas"},
      // CONTEMPORARY
      {t:"When Your Family Does Not Celebrate the Same Christmas",s:"4 Weeks of Formation for the Blended Family, the Estranged Family, and the Family That Dreads December Together",felt:true},
      {t:"The Chair That Is Empty This Year",s:"21 Days of Formation for the Family Facing Its First Christmas After a Death, a Divorce, or a Child Who Left",felt:true},
      {t:"What You Are Teaching Your Kids About Christmas",s:"A 3-Week Advent Series on the Formation That Happens in the Household — Not in the Sanctuary",felt:true},
      {t:"The Prodigal Who Is Not Coming Home",s:"4 Weeks of Formation for the Parent Whose Adult Child Will Not Be at the Table — What You Do With That",felt:true},
      {t:"Grandparenting in a Post-Christian Family",s:"21 Days of Formation for the Grandparent Whose Children Have Left the Faith — and What Christmas Still Offers",felt:true},
      {t:"The Phone at the Table",s:"7 Days of Formation in What Advent Presence Looks Like in the Family That Is Physically Together and Emotionally Absent",felt:true},
      {t:"The Divorced Christmas",s:"3 Weeks of Formation for the Congregation Member Navigating Two Households, Two Christmas Mornings, and One Faith",felt:true},
      {t:"Your Kids Are Watching",s:"4 Weeks on the Formation Your Children Are Receiving From What You Do — Not What You Say — This December",felt:true},
      {t:"The Christmas You Cannot Afford",s:"21 Days of Formation for the Family Under Financial Pressure — What Christmas Looks Like When You Cannot Give What the Culture Expects",felt:true},
      {t:"When the Family Table Is Not Safe",s:"A 3-Week Advent Formation for the Person Who Cannot Go Home — and What the Incarnation Offers to Those Without a Safe Place",felt:true},
    ]
  },
  {
    id:"worship", arc:"into", num:8,
    name:"Worship and Music",
    desc:"Campaigns that form the congregation's worship life around the incarnation",
    color:"#2a4878",
    campaigns:[
      {t:"The Songs They Sang",s:"A 4-Week Advent Worship Formation Series — The Magnificat, Benedictus, Nunc Dimittis, Gloria"},
      {t:"Advent Hymns Deeply",s:"21 Days of Formation Through the Great Advent Hymns"},
      {t:"Sing a New Song",s:"4 Weeks on What It Means to Worship the God Who Entered Creation"},
      {t:"The Gloria",s:"3 Weeks on the Angels' Christmas Song — Glory to God in the Highest"},
      {t:"Seven Songs of Advent",s:"7 Days in the Great Songs of the Season — From the Psalms to the Magnificat"},
      {t:"The Music of the Incarnation",s:"40 Days on What the Church Has Sung About Christmas for Two Thousand Years"},
      {t:"O Come O Come Emmanuel",s:"3 Weeks on the Most Theologically Dense Advent Hymn"},
      {t:"When Heaven Sang",s:"21 Days on What the Angels Were Announcing When They Appeared to the Shepherds"},
      {t:"The Silent Night Campaign",s:"4 Weeks on Why the Most Famous Christmas Song Is Also the Most Formation-Rich"},
      {t:"Worship Before the Manger",s:"6 Weeks Forming the Congregation's Posture of Worship Before Christmas Eve Arrives"},
      // CONTEMPORARY
      {t:"Why Do We Keep Singing This",s:"4 Weeks of Formation in the Theology Behind the Christmas Songs the Congregation Sings Every Year Without Knowing What They Mean",felt:true},
      {t:"The Song Before the Stable",s:"21 Days on the Magnificat as the First Christmas Sermon — Preached in a Song by a Teenager",felt:true},
      {t:"When the Music Hits",s:"3 Weeks on the Theology of Why Christmas Music Produces Emotion — and What to Do With the Feeling",felt:true},
      {t:"Secular Carols Are Theology",s:"4 Weeks of Formation in Reading the Culture's Christmas Music — What White Christmas, O Holy Night, and Hallelujah Are Actually Saying",felt:true},
      {t:"The Loudest Week of the Year",s:"21 Days of Formation in What It Means to Worship When the Culture Has Taken Worship and Turned It Into Entertainment",felt:true},
      {t:"What the Angels Could Not Stop Saying",s:"7 Days on Luke 2:14 — The Formation of the Congregation That Actually Understands the Gloria",felt:true},
      {t:"Playlist for Advent",s:"A 3-Week Formation Campaign Built Around a Curated Daily Listening Practice — Music as a Formation Practice",felt:true},
      {t:"The Song You Cannot Unhear",s:"4 Weeks on the Formation That Music Produces — and Why the Church's Songs Are More Theologically Dense Than Its Sermons",felt:true},
      {t:"Singing What You Do Not Yet Believe",s:"21 Days on the Formation Practice of Singing the Truth Before You Feel It — the Liturgical Theology of Advent Music",felt:true},
      {t:"The Christmas Concert Formation Plan",s:"6 Weeks of Formation for the Congregation That Performs Christmas Music — Connecting the Performance to the Proclamation",felt:true},
    ]
  },
  {
    id:"preaching", arc:"into", num:9,
    name:"Preaching Formation",
    desc:"Campaigns that help pastors and preaching teams prepare to preach Christmas with fresh power",
    color:"#483060",
    campaigns:[
      {t:"The Fresh Angle",s:"A 4-Week Pre-Christmas Series for the Pastor Who Has Preached Christmas Twenty Times"},
      {t:"Seven Angles on the Nativity",s:"7 Days of Preaching Preparation — One Fresh Angle Per Day on the Christmas Text"},
      {t:"The Formation Sermon",s:"3 Weeks of Sermon Development — How to Preach Christmas as Formation"},
      {t:"The Congregation You Are Preaching To",s:"4 Weeks of Congregational Analysis Before Christmas Eve"},
      {t:"The Preaching Community",s:"21 Days of Shared Preaching Preparation — Staff, Elders, Teaching Team"},
      {t:"Christmas Preaching History",s:"6 Weeks of Formation Through the Greatest Christmas Sermons Ever Preached"},
      {t:"Preach the Incarnation",s:"40 Days of Theological Formation for the Pastor Who Wants to Preach Christmas With Depth"},
      {t:"The Unpreached Text",s:"3 Weeks on the Christmas Texts Nobody Preaches — And Why They Should"},
      {t:"The Outreach Christmas Eve Sermon",s:"21 Days of Preparation for the Most Important Sermon of the Year"},
      {t:"The Formation Christmas Series",s:"4 Weeks of Curriculum Development — Building the Formation Series Before Christmas"},
      // CONTEMPORARY
      {t:"Stop Preaching the Same Christmas Sermon",s:"A 4-Week Formation Campaign for the Pastor Who Wants to Surprise a Congregation That Knows How the Story Ends",felt:true},
      {t:"The Christmas Sermon Nobody Preaches",s:"21 Days on the Overlooked Texts of the Nativity — Massacre of the Innocents, the Presentation, the Hidden Years",felt:true},
      {t:"Preaching to the Room You Have Not the Room You Want",s:"3 Weeks on the Pastoral Reality of Christmas Eve — 80% of Whom You Have Never Met",felt:true},
      {t:"The Apologetics Christmas",s:"4 Weeks of Formation for the Pastor Who Wants to Preach Christmas as Historical Claim Not Sentiment",felt:true},
      {t:"When Your Congregation Has Heard It All",s:"21 Days of Formation in the Art of Preaching the Familiar Unfamiliar — the Craft of Surprise in a Known Story",felt:true},
      {t:"The Story Nobody Tells at Christmas",s:"7 Days of Preparation for the Preacher Who Is Willing to Go to the Darkness Before the Light",felt:true},
      {t:"The Christmas Eve First-Timer Sermon",s:"3 Weeks of Specific Preparation for the Congregation That Is 40% People You Have Never Seen Before",felt:true},
      {t:"John 1 on Christmas Eve",s:"4 Weeks of Formation for the Preaching Team That Wants to Preach the Most Theologically Dense Christmas Text — Not Luke 2",felt:true},
      {t:"The Sermon That Does Not Sentimentalize",s:"21 Days of Formation in Preaching Christmas Without Making It Smaller Than It Is",felt:true},
      {t:"Preaching to Grief at Christmas",s:"A 40-Day Formation Campaign for the Pastor Whose Congregation Has Had a Hard Year — How to Hold the Announcement and the Pain",felt:true},
    ]
  },
  {
    id:"community", arc:"into", num:10,
    name:"Community Engagement",
    desc:"Campaigns that carry the congregation into their community during Advent and Christmas",
    color:"#3a5840",
    campaigns:[
      {t:"Light in the Neighborhood",s:"A 4-Week Advent Community Engagement Campaign — Forming the Congregation to Be the Light It Celebrates"},
      {t:"Advent Serves",s:"40 Days of Advent Service Formation — One Act of Service Per Day"},
      {t:"The City at Christmas",s:"3 Weeks on What the Incarnation Demands of the Congregation's Relationship to Its City"},
      {t:"Table for the Stranger",s:"21 Days of Hospitality Formation — What the Incarnation Demands of the Welcome of Outsiders"},
      {t:"Advent Partnership",s:"4 Weeks of Community Partnership Formation — Connecting to Organizations Serving the City"},
      {t:"Seven Days of Community Formation",s:"7 Days of Advent Engagement Practices — The Congregation in Its Community the Week Before Christmas"},
      {t:"The Advent Witness in the Workplace",s:"6 Weeks of Formation for the Congregation's Witness at Work in December"},
      {t:"Advent Generosity in the Community",s:"21 Days of Community Generosity Formation"},
      {t:"The Most Wonderful Time for Mission",s:"3 Weeks on Why December Is the Church's Highest-Leverage Outreach Month"},
      {t:"From Sanctuary to Street",s:"40 Days of Formation in the Movement From Inside the Building to Outside It"},
      // CONTEMPORARY
      {t:"Your City Needs What You Have",s:"A 4-Week Advent Campaign on the Specific Needs of the Congregation's Specific City — and What the Incarnation Sends the Church Into Them With",felt:true},
      {t:"The Neighbor You Have Not Met",s:"21 Days of Formation in the Practice of Knowing the People Who Live Next to You — the Formation That Makes Christmas Invitations Natural",felt:true},
      {t:"Amazon Cannot Do What You Can Do",s:"3 Weeks on the Formation of Personal Presence — What the Congregation Offers Its Community That No Platform, App, or Service Can Replicate",felt:true},
      {t:"The December Open Door",s:"4 Weeks of Formation in the Specific Hospitality Practices That Make the Congregation's Building a Formation Location for the Community in December",felt:true},
      {t:"Your Business at Christmas",s:"21 Days of Formation for the Business Owner in the Congregation — How the Incarnation Shapes What You Do With Your Workplace in December",felt:true},
      {t:"The School, the Shelter, the Street",s:"7 Days of Community Engagement Formation — Three Specific Relationships the Congregation Can Build in December",felt:true},
      {t:"What Your Neighborhood Needs From Your Church",s:"A 3-Week Advent Series on Local Discernment — The Formation of the Congregation That Listens Before It Serves",felt:true},
      {t:"The Advent of the Unexpected Neighbor",s:"4 Weeks on Luke 10 and Good Samaritanism as an Advent Practice — Who Is Your Neighbor at Christmas",felt:true},
      {t:"First Responders at Christmas",s:"21 Days of Formation in Prayer and Care for the People Who Work on Christmas — Police, Nurses, Firefighters, EMTs",felt:true},
      {t:"The Church That the City Knows",s:"40 Days of Formation in the Reputation the Congregation Is Building — What the Community Knows About Who You Are by What You Do in December",felt:true},
    ]
  },

  // ════════════════════════════════════════════════════════════
  // COMING OUT OF CHRISTMAS — 10 categories × 20 campaigns each
  // ════════════════════════════════════════════════════════════
  {
    id:"living", arc:"out", num:1,
    name:"Living the Incarnation",
    desc:"Campaigns that translate the Christmas announcement into daily formation in the new year",
    color:"#5a3820",
    campaigns:[
      {t:"The Incarnation Every Monday",s:"A 6-Week Post-Christmas Series on Living From the Incarnation Rather Than Just Receiving It"},
      {t:"God With Us — Still",s:"40 Days Forming the Congregation to Practice the Presence of God in the Ordinary Year"},
      {t:"The Flesh of It",s:"21 Days on What It Means to Live an Embodied Spiritual Life After Christmas"},
      {t:"Incarnational Living",s:"4 Weeks on What It Means to Be Sent Into the World the Way the Son Was Sent"},
      {t:"Seven Ways Christmas Changes Monday",s:"7 Days of Specific Application — How the Incarnation Changes Work, Money, Relationships"},
      {t:"The Light After Christmas",s:"3 Weeks on What It Means to Carry the Light When the Cultural Christmas Is Over"},
      {t:"Emmanuel — Now What",s:"6 Weeks of Formation on the Specific Implications of God Being With Us"},
      {t:"January Formation",s:"21 Days of Post-Christmas Formation Practices That Carry the Incarnation Into the New Year"},
      {t:"The Permanent Incarnation",s:"40 Days on the Ascension — Why Jesus Did Not Stop Being Human"},
      {t:"The Body He Still Has",s:"4 Weeks on the Bodily Resurrection and Ascension and What That Means for Your Body"},
      // CONTEMPORARY
      {t:"Christmas Is Over and Nothing Changed",s:"A 4-Week Post-Christmas Series for the Congregation That Received the Announcement but Is Still Waiting for the Transformation",felt:true},
      {t:"The Monday After Christmas",s:"21 Days of Formation in What the Incarnation Actually Changes About the Most Ordinary Day of the Week",felt:true},
      {t:"The January Slump Is a Formation Opportunity",s:"3 Weeks on What the Emotional Deflation After Christmas Is Trying to Tell You — and What Formation Looks Like Inside It",felt:true},
      {t:"Your Ordinary Life Is the Point",s:"4 Weeks on the Theology of the Hidden Years of Jesus — What Thirty Years of Obscurity Says About the Formation of the Ordinary",felt:true},
      {t:"Still Immanuel",s:"21 Days of Post-Christmas Formation in the Practice of Divine Presence — God Did Not Leave When the Decorations Came Down",felt:true},
      {t:"The Resolution Nobody Keeps",s:"7 Days on Why January Formation Fails — and What the Incarnation Offers Instead of a Better Plan",felt:true},
      {t:"What Christmas Did to You",s:"A 3-Week Post-Christmas Formation Series on What Receiving the Incarnation Actually Produces — Specific, Named, Honest",felt:true},
      {t:"The Holiness of the Ordinary",s:"40 Days on What God Joining the Ordinary Says About What He Thinks of Your Ordinary — Work, Commute, Grocery Store, Tuesday",felt:true},
      {t:"He Did Not Come to Take You Out of Your Life",s:"4 Weeks of Formation in the Incarnational Theology That Sanctifies the Ordinary Rather Than Escapeing From It",felt:true},
      {t:"God Is Still in the Neighborhood",s:"21 Days on John 1:14 in January — the Formation of the Congregation That Does Not Let the Presence Leave With the Christmas Tree",felt:true},
    ]
  },
  {
    id:"epiphany", arc:"out", num:2,
    name:"The Epiphany Season",
    desc:"Campaigns that carry the congregation from Christmas to Epiphany and beyond",
    color:"#6a4818",
    campaigns:[
      {t:"The Light to the Nations",s:"A 6-Week Post-Christmas Epiphany Series on the Global Reach of the Incarnation"},
      {t:"What the Magi Knew",s:"4 Weeks on the Formation of the Wise Men — What They Followed, Found, and Gave"},
      {t:"The Twelve Days",s:"7 Days of Post-Christmas Formation Through the Twelve Days of Christmas"},
      {t:"Star Followers",s:"3 Weeks on What It Means to Follow the Evidence Wherever It Leads"},
      {t:"Epiphany Formation",s:"21 Days of Formation in the Season the Church Has Almost Forgotten"},
      {t:"Beyond the Manger",s:"4 Weeks Carrying the Congregation From the Manger to the Mission"},
      {t:"The Presentation",s:"6 Weeks on Luke 2:22-52 — What Happened After the Manger"},
      {t:"Gifts Worth Giving",s:"3 Weeks on What the Magi Gave and What the Congregation Is Invited to Give in Response"},
      {t:"The Year of the Lord",s:"21 Days on Isaiah 61 and Luke 4 — Launching the Year With Jesus' Mission Statement"},
      {t:"Before He Was Preaching",s:"7 Days on the Thirty Hidden Years — What Jesus Was Doing Before His Ministry"},
      // CONTEMPORARY
      {t:"The Church That Celebrates Longer Than the Culture Does",s:"4 Weeks of Post-Christmas Formation in the Practice of Continuing to Celebrate What the Culture Has Already Moved Past",felt:true},
      {t:"Chasing the Light",s:"21 Days of Epiphany Formation on What It Looks Like to Follow Evidence Rather Than Feeling — the Magi's Method in Your Life",felt:true},
      {t:"The Star Is Still Visible",s:"3 Weeks on the Epiphany Claim That the Revelation Has Not Stopped — What God Is Still Revealing in January",felt:true},
      {t:"Outsiders at the Manger",s:"4 Weeks on the Magi as the Formation Text for the Congregation's Engagement With Non-Christians — Who Got There and How",felt:true},
      {t:"January 6 Is Not Ordinary",s:"21 Days on Epiphany as the Formation Season the Congregation Has Been Skipping — and What It Has Been Missing",felt:true},
      {t:"What the Magi Left Behind",s:"7 Days on What It Cost the Magi to Seek, Find, Give, and Return by Another Route — the Formation of the One-Way Journey",felt:true},
      {t:"The Long Way Home",s:"A 3-Week Post-Christmas Formation Series on Matthew 2:12 — They Went Home by a Different Route — What Encountering Jesus Changes About Your Return",felt:true},
      {t:"The Year the Wise Men Set the Agenda",s:"4 Weeks on the Magi's Method as the Formation Plan for the New Year — Seek, Follow, Give, Worship, Depart Changed",felt:true},
      {t:"Finding God Outside the Building",s:"21 Days of Epiphany Formation in the Theology That God Revealed Himself to People Who Were Not in the Temple — and What That Still Means",felt:true},
      {t:"Gold, Frankincense, and What You Actually Brought",s:"40 Days of Post-Christmas Formation on Giving What Is Costly — What the Magi's Gifts Say About the Formation of Generosity",felt:true},
    ]
  },
  {
    id:"newyear", arc:"out", num:3,
    name:"The New Year Bridge",
    desc:"Campaigns that carry the congregation from Christmas directly into New Year formation",
    color:"#40285a",
    campaigns:[
      {t:"New Year, New Creation",s:"A 6-Week Bridge Campaign From Christmas Eve to Mid-January"},
      {t:"Christmas to January 1",s:"7 Days of Formation Between Christmas Day and New Year's Day"},
      {t:"The Resolution the Gospel Offers",s:"21 Days on What the Incarnation Offers That Self-Help Cannot"},
      {t:"Fresh Start, Full Gospel",s:"4 Weeks Connecting the New Year to the Incarnation — Not a Resolution but a Resurrection"},
      {t:"January Formation",s:"3 Weeks of Formation for the Congregation That Wants to Make the New Year Different"},
      {t:"From Bethlehem to Jordan",s:"40 Days From Christmas to the Baptism of Jesus — The Formation Arc That Launches the Year"},
      {t:"The Small Group That Christmas Started",s:"A 6-Week Post-Christmas Small Group Launch Campaign"},
      {t:"The Year He Has Prepared",s:"21 Days on Psalm 90 and the Theology of Time — Surrendering the Year Before You Know What It Is"},
      {t:"Word for the Year",s:"4 Weeks of Formation Around Choosing One Word to Carry Through the Year"},
      {t:"Seven Days That Shape the Year",s:"7 Days of Formation Between Christmas and New Year That Determine What the Year Becomes"},
      // CONTEMPORARY
      {t:"Your Resolutions Will Not Work This Time Either",s:"A 4-Week Post-Christmas Series on Why Self-Improvement Fails Where Formation Succeeds — and What the Difference Looks Like in January",felt:true},
      {t:"The Year You Stop Performing",s:"21 Days of New Year Formation in the Theology of Identity Over Achievement — Who You Are Before What You Do",felt:true},
      {t:"New Year, Same You — and That Is the Good News",s:"3 Weeks on the Formation of the Person the Incarnation Has Already Changed — Not Who You Plan to Become but Who You Already Are",felt:true},
      {t:"The Five-Year Formation Plan Nobody Is Selling",s:"4 Weeks of Post-Christmas Formation in the Long Arc — What Five Years of Consistent Formation Produces",felt:true},
      {t:"January Is Not the Enemy",s:"21 Days of Formation in the Theology of the Ordinary Month — What God Does in January When Nobody Is Watching",felt:true},
      {t:"The Year You Surrender Instead of Resolve",s:"7 Days on the Single Formation Posture That Changes the New Year More Than Ten Resolutions",felt:true},
      {t:"Your 2027 Self",s:"A 3-Week Post-Christmas Formation Campaign Built Around the Question Who Do You Want to Be in Three Years — and What Formation Gets You There",felt:true},
      {t:"Stop Waiting for January to Feel Different",s:"4 Weeks of Honest Formation for the Person Who Has Been Making the Same New Year Turn for Five Years",felt:true},
      {t:"One Thing in January",s:"21 Days of Post-Christmas Formation Built Around One Single Formation Commitment — Not Ten",felt:true},
      {t:"The Year God Already Knows",s:"40 Days of Post-Christmas Formation in the Theology of Sovereignty and Trust — Giving to God a Year He Already Holds",felt:true},
    ]
  },
  {
    id:"smallgroup", arc:"out", num:4,
    name:"The Small Group Season",
    desc:"Campaigns designed to launch small groups in the post-Christmas formation window",
    color:"#285848",
    campaigns:[
      {t:"Gather After the Gift",s:"A 4-Week Post-Christmas Campaign Built to Launch Small Groups in January"},
      {t:"The Incarnation Community",s:"6 Weeks on Acts 2 — What the Community Looks Like That the Incarnation Produced"},
      {t:"God With Us Together",s:"4 Weeks of Post-Christmas Community Formation — What Immanuel Means in a Small Group"},
      {t:"The Table After Christmas",s:"7 Days of Formation Around the Table — What the Christmas Table Started"},
      {t:"Devoted",s:"3 Weeks on Acts 2:42 — Four Practices That Build the Post-Christmas Community"},
      {t:"One Another",s:"6 Weeks on the One Another Commands — Building the Relational Infrastructure of Community"},
      {t:"The Winter Small Group",s:"21 Days of Formation Content Designed for Post-Christmas Small Group Launch"},
      {t:"From House to House",s:"4 Weeks on the Early Church's Practice of House-to-House Formation"},
      {t:"The Post-Christmas Congregation",s:"3 Weeks of Vision Casting for the Community the Incarnation Is Building"},
      {t:"The Formation Year",s:"40 Days Launching the Annual Formation Arc From Christmas Into the Year"},
      // CONTEMPORARY
      {t:"Nobody Wants to Be Alone in January",s:"A 4-Week Post-Christmas Small Group Campaign Built Around the Epidemic of Loneliness — and What the Community of the Incarnation Offers",felt:true},
      {t:"The Group That Stays",s:"21 Days of Formation for the Small Group That Launched in September and Is Still Together — What Keeps a Group From Dissolving in January",felt:true},
      {t:"Community Is the Formation",s:"3 Weeks on the Formation That Only Happens in Proximity — What You Cannot Download, Podcast, or Solo-Study Your Way Into",felt:true},
      {t:"The Table Nobody Reserved",s:"4 Weeks of Post-Christmas Formation in the Practice of Showing Up — the Simple Act of Being Present in Community as a Formation Practice",felt:true},
      {t:"What If Your Small Group Was a Formation Community",s:"21 Days of Formation in the Difference Between a Small Group That Studies Together and a Small Group That Forms Together",felt:true},
      {t:"The Friend You Need in January",s:"7 Days of Post-Christmas Formation in the Theology of Friendship — What the Incarnation Says About the Necessity of Human Community",felt:true},
      {t:"The Courage to Be Known",s:"A 3-Week Post-Christmas Formation Series on Vulnerability in Community — Why the Congregation That Risks Being Known Is the One That Grows",felt:true},
      {t:"Your People Are Not Optional",s:"4 Weeks of Formation in the Non-Negotiability of Community — The Lone-Ranger Christian Is a Pre-Resurrection Posture",felt:true},
      {t:"The Group of Two or Three",s:"21 Days of Formation in the Theology of Small — Jesus' Promise Was Not About the Large Gathering",felt:true},
      {t:"January Is the Best Month to Start",s:"40 Days of Post-Christmas Formation Built Around the Evidence That January Is the Highest Formation-Readiness Month of the Year",felt:true},
    ]
  },
  {
    id:"generosity", arc:"out", num:5,
    name:"Generosity Season",
    desc:"Campaigns that carry the generosity formed at Christmas into the new year",
    color:"#3a5828",
    campaigns:[
      {t:"The First Gift of the Year",s:"A 4-Week Post-Christmas Generosity Campaign on What You Do With Resources in January"},
      {t:"God So Loved He Gave",s:"21 Days on John 3:16 — The Formation of Generosity From the Theology of the Incarnation"},
      {t:"The Steward in January",s:"3 Weeks of Stewardship Formation for the New Year"},
      {t:"First Fruits of the Year",s:"4 Weeks on the Formation Practice of Giving the First and Best of the Year"},
      {t:"Seven Ways to Give in January",s:"7 Days of Post-Christmas Generosity Practices — Money, Time, Skill, Presence, Prayer, Hospitality, Testimony"},
      {t:"The Year of Generous Living",s:"6 Weeks Launching the Annual Generosity Formation Arc"},
      {t:"What Gold Frankincense and Myrrh Actually Cost",s:"21 Days on the Formation Theology of the Magi's Gifts"},
      {t:"The Generous Community",s:"3 Weeks Building the Culture of Communal Generosity"},
      {t:"Legacy in January",s:"4 Weeks of Post-Christmas Legacy Formation — What You Leave and Who You Leave It For"},
      {t:"The Generous Year",s:"40 Days of Formation in the Posture, Practice, and Theology of Generosity"},
      // CONTEMPORARY
      {t:"You Already Spent Too Much at Christmas",s:"A 4-Week Post-Christmas Formation Series on What Financial Generosity Looks Like After the Debt of December — the Formation of Giving From Nothing",felt:true},
      {t:"The Debt Is Not Who You Are",s:"21 Days of Post-Christmas Formation in Financial Identity — What the Incarnation Says About Your Relationship With Money in January",felt:true},
      {t:"Give Before You Feel Generous",s:"3 Weeks on the Formation of Generosity as Practice Rather Than Emotion — What Giving Does to the Giver Before the Giver Wants to Give",felt:true},
      {t:"What the Magi Did Not Take Back",s:"4 Weeks of Formation on the Theology of the Non-Returnable Gift — What It Means to Give What Cannot Be Undone",felt:true},
      {t:"The Amazon January",s:"21 Days of Post-Christmas Formation in the Counterformation Against Consumption — What Giving Looks Like When the Shopping Does Not Stop After December 25",felt:true},
      {t:"Your Money in the New Year",s:"7 Days of Post-Christmas Formation in the First Financial Practices of January — What You Do With Your Money in Week One Determines the Year",felt:true},
      {t:"The Congregation That Could Not Out-Give God",s:"A 3-Week Post-Christmas Formation Series on the Testimony of Generosity — What Happens to the Congregation That Gives Extravagantly",felt:true},
      {t:"One Percent More",s:"4 Weeks of Post-Christmas Formation in the Formation of Incremental Generosity — What Giving One Percent More This Year Produces Over Ten Years",felt:true},
      {t:"The Time You Are Not Spending",s:"21 Days of Formation in the Generosity of Time — What January Looks Like When Time Is the Primary Gift the Congregation Offers",felt:true},
      {t:"Legacy Is Not About the Money",s:"40 Days of Post-Christmas Formation in the Theology of Leaving Something Behind — What Formation Is, What Legacy Is, and Why They Are Connected",felt:true},
    ]
  },
  {
    id:"mission", arc:"out", num:6,
    name:"Mission and Witness",
    desc:"Campaigns that carry the outreach energy of Christmas into the new year",
    color:"#3a5040",
    campaigns:[
      {t:"As the Father Sent Me",s:"A 6-Week Post-Christmas Mission Formation Campaign Built on John 20:21"},
      {t:"The Witness of January",s:"4 Weeks on What to Do With the People Who Came to Christmas Eve But Have Not Been Back"},
      {t:"Witnesses",s:"40 Days Forming the Congregation in Personal Testimony — How to Tell Your Story"},
      {t:"The Magi's Method",s:"3 Weeks on the Outreach Formation of the Magi — Seeking, Finding, Worshipping, Going"},
      {t:"Good News for All People — Still",s:"21 Days Carrying the Christmas Announcement Into the New Year"},
      {t:"The Post-Christmas Invitation",s:"6 Weeks of Formation for the Congregation That Invited People and Wants to See Them Stay"},
      {t:"The Sent Life",s:"4 Weeks on What It Means to Live as Someone Who Has Been Sent"},
      {t:"Epiphany Outreach",s:"21 Days of Post-Christmas Outreach Formation — From the Magi to Your Neighborhood"},
      {t:"A Light to the Nations",s:"3 Weeks on Isaiah 60 and the Epiphany Commission"},
      {t:"The Year of Witness",s:"40 Days Launching the Annual Evangelism Formation Arc"},
      // CONTEMPORARY
      {t:"They Came to Christmas and Left",s:"A 4-Week Post-Christmas Formation Series on the Most Important Follow-Up Window of the Year — What the Congregation Does With the People Who Came Once",felt:true},
      {t:"The Text You Send in January",s:"21 Days of Formation in the Post-Christmas Invitation — What You Say to the Person Who Came to Christmas Eve When You See Them in January",felt:true},
      {t:"Your Story Is the Strategy",s:"3 Weeks of Post-Christmas Formation in Personal Testimony — The Most Underused Evangelism Tool the Congregation Has",felt:true},
      {t:"The Secular Friend in January",s:"4 Weeks of Formation for the Congregation That Wants to Keep the Conversation Going After Christmas",felt:true},
      {t:"The Neighborhood Church",s:"21 Days of Post-Christmas Formation in Local Mission — What the Congregation Becomes When It Decides to Be Known in Its Neighborhood",felt:true},
      {t:"What If They Actually Came Back",s:"7 Days of Formation for the Congregation That Is Praying for the Person Who Came to Christmas Eve — What Does It Look Like If the Prayer Is Answered",felt:true},
      {t:"The Year of One Story",s:"A 3-Week Post-Christmas Mission Formation Series Built Around Each Congregation Member Sharing One Story With One Person",felt:true},
      {t:"The Follow-Up Nobody Makes",s:"4 Weeks of Post-Christmas Formation in the Pastoral Art of Following Up — What the Congregation Does Between Christmas and Easter With the People It Met",felt:true},
      {t:"Not a Program — A People",s:"21 Days of Post-Christmas Formation in the Witness That Is Not a Strategy or a Campaign but a Congregation Whose Life Is Worth Seeing",felt:true},
      {t:"Go Home by a Different Route",s:"40 Days of Formation in the Matthew 2:12 Principle — What It Means to Carry Christmas Back Into Your Life on a Different Path",felt:true},
    ]
  },
  {
    id:"discipleship", arc:"out", num:7,
    name:"Discipleship Launch",
    desc:"Campaigns that use the post-Christmas window to launch the year's discipleship arc",
    color:"#3a3858",
    campaigns:[
      {t:"Follow Me — Again",s:"A 6-Week Post-Christmas Discipleship Series on What Following Jesus Looks Like in the New Year"},
      {t:"The Formation Year",s:"40 Days Launching the Congregation's Annual Formation Arc"},
      {t:"Abide",s:"4 Weeks on John 15 — The Formation Practice the Post-Christmas Season Is Designed to Build"},
      {t:"Daily Formation",s:"21 Days of Building the Daily Practices That Carry Through the Year"},
      {t:"The Disciple's New Year",s:"3 Weeks on What Discipleship Looks Like Differently This Year"},
      {t:"The Sermon on the Mount",s:"6 Weeks Launching the Year's Discipleship With the Greatest Teaching in the Gospels"},
      {t:"Mentored by Jesus",s:"21 Days of Formation in the Practices of Jesus — How He Prayed, Ate, Rested, Worked, Related"},
      {t:"Identity Before Activity",s:"4 Weeks on Who You Are Before What You Do — Formation of Identity From the Incarnation"},
      {t:"Spiritual Disciplines for the Year",s:"40 Days Launching the Congregation Into the Classic Spiritual Disciplines"},
      {t:"The Kingdom Life",s:"6 Weeks on What It Means to Live Under the Rule of Jesus in the Ordinary Year"},
      // CONTEMPORARY
      {t:"You Are Not as Far Along as You Think",s:"A 4-Week Post-Christmas Formation Series on the Honest Assessment of Where You Actually Are — and the Formation That Begins From That Honesty",felt:true},
      {t:"The Discipleship You Have Been Avoiding",s:"21 Days of Formation in the Specific Practice the Congregation Member Has Known They Need and Has Not Started",felt:true},
      {t:"Stop Consuming, Start Being Formed",s:"3 Weeks on the Formation of the Person Who Has Attended Church for Ten Years and Is Not Noticeably Different — What Formation Looks Like That Actually Produces Change",felt:true},
      {t:"The Formation Habit Stack",s:"4 Weeks of Post-Christmas Formation in the Architecture of Sustainable Practice — How Formation Habits Build on Each Other",felt:true},
      {t:"You Are Being Formed by Something",s:"21 Days of Post-Christmas Formation in the Awareness That Formation Is Continuous — the Question Is What Is Doing It",felt:true},
      {t:"The One Thing Your Faith Is Missing",s:"7 Days of Honest Self-Assessment and Formation Planning — the Specific Practice That Would Change Everything",felt:true},
      {t:"Discipleship Is Not a Course",s:"A 3-Week Post-Christmas Formation Series on the Difference Between Information and Transformation — Why You Keep Learning Without Changing",felt:true},
      {t:"The Person You Were Before You Were a Christian",s:"4 Weeks of Formation in the Specific Areas Where the Congregation Member Has Not Let the Gospel Penetrate — the Audit of What Formation Has and Has Not Reached",felt:true},
      {t:"Follow Through",s:"21 Days of Post-Christmas Formation in the One Formation Commitment the Congregation Member Will Actually Keep — Building the System That Makes Keeping It Possible",felt:true},
      {t:"The Formation of the Next Five Years",s:"40 Days of Post-Christmas Formation in the Long Arc — What Consistent Formation Looks Like, Produces, and Requires Across Five Years",felt:true},
    ]
  },
  {
    id:"healing", arc:"out", num:8,
    name:"Healing and Restoration",
    desc:"Campaigns that carry Christmas hope into the congregation's healing ministry in the new year",
    color:"#583038",
    campaigns:[
      {t:"He Healed Them All",s:"A 6-Week Post-Christmas Healing Formation Campaign — What the Incarnation Says to Every Broken Thing"},
      {t:"Recovery After Christmas",s:"21 Days of Post-Christmas Healing Formation for the Congregation That Is Exhausted or Depleted"},
      {t:"The God Who Heals",s:"4 Weeks on Healing Theology — Physical, Emotional, and Relational Healing"},
      {t:"The Year of Restoration",s:"3 Weeks Launching the New Year With Isaiah 61"},
      {t:"Wholeness",s:"40 Days of Formation in the Biblical Vision of Shalom — The Wholeness the Incarnation Came to Restore"},
      {t:"Renewing Your Mind",s:"21 Days on Romans 12:2 — The Post-Christmas Cognitive Renewal Campaign"},
      {t:"Carrying One Another",s:"4 Weeks on Galatians 6:2 — The Formation of the Healing Community"},
      {t:"The Broken Welcome",s:"3 Weeks on the Incarnation as the Theology of Welcome for the Broken"},
      {t:"The January Restoration",s:"6 Weeks of Formation for the Congregation Navigating Difficulty at the Start of the Year"},
      {t:"The God Who Sees",s:"21 Days on the Formation of Being Known and Seen — What the Incarnation Says to the Invisible"},
      // CONTEMPORARY
      {t:"Christmas Made It Worse",s:"A 4-Week Post-Christmas Healing Formation for the Congregation Member for Whom the Season Intensified Pain — Grief, Addiction, Family Conflict, Depression",felt:true},
      {t:"The Hangover After the Holiday",s:"21 Days of Post-Christmas Healing Formation in the Emotional and Physical Reality of the Season — What Healing Looks Like in January",felt:true},
      {t:"The Relationship That Did Not Survive Christmas",s:"3 Weeks of Formation for the Congregation Member Navigating a Family Rupture, an Estrangement, or a Conflict That Christmas Surfaced",felt:true},
      {t:"You Are Not Fine",s:"4 Weeks of Post-Christmas Formation in the Permission to Be Honest — What the Incarnation Offers to the Person Who Has Been Performing Okay",felt:true},
      {t:"The Grief That December Did Not Fix",s:"21 Days of Formation for the Person Who Arrived at January Still Carrying What They Hoped Christmas Would Lift",felt:true},
      {t:"Healing Is Not Linear",s:"7 Days of Post-Christmas Formation in the Theology of the Long Recovery — What the Incarnation Says to the Person Who Expected to Be Better by Now",felt:true},
      {t:"The Body After December",s:"A 3-Week Post-Christmas Healing Formation in the Physical Reality of Rest, Nutrition, and Recovery — the Theology of Bodily Care in January",felt:true},
      {t:"The Wound the Holidays Opened",s:"4 Weeks of Post-Christmas Formation for the Congregation Member Whose Specific Wound Was Activated in December — and What Formation Offers for January",felt:true},
      {t:"What Therapy and Church Do Together",s:"21 Days of Post-Christmas Formation in the Integration of Professional Care and Spiritual Formation — for the Congregation Member Navigating Both",felt:true},
      {t:"The Long Healing",s:"40 Days of Post-Christmas Formation in the Theology of the Slow Recovery — What the Incarnation Offers the Person for Whom Healing Is Taking Longer Than Expected",felt:true},
    ]
  },
  {
    id:"time", arc:"out", num:9,
    name:"Stewardship of Time",
    desc:"Campaigns that use the new year to form the congregation's relationship with time",
    color:"#384858",
    campaigns:[
      {t:"Teach Us to Number Our Days",s:"A 4-Week Post-Christmas Series on Psalm 90 — The Formation of a Congregation That Uses Time Well"},
      {t:"The Redeemed Calendar",s:"21 Days of Formation in What It Means to Bring Your Year to God Before You Know What It Holds"},
      {t:"Sabbath in the New Year",s:"4 Weeks of Formation in the Practice of Sabbath as the Foundation of the Year's Rhythm"},
      {t:"The First Week of the Year",s:"7 Days of Formation Practices That Order the Year From the Beginning"},
      {t:"Seasons of Formation",s:"3 Weeks on the Formation That Belongs to Each Season — What January Is For"},
      {t:"The Formation Rhythm",s:"40 Days of Building the Daily, Weekly, Monthly, and Annual Practices"},
      {t:"Morning by Morning",s:"21 Days of Formation in the Practice of Morning Prayer — How the First Hour Determines the Rest"},
      {t:"Ordering Your Life",s:"6 Weeks on the Formation of a Rule of Life"},
      {t:"The Examined Year",s:"4 Weeks of Post-Christmas Reflection on the Year Just Completed and the Year Beginning"},
      {t:"The Formation Inventory",s:"21 Days of Post-Christmas Reflection — A Complete Formation Inventory"},
      // CONTEMPORARY
      {t:"You Are Busier Than You Were Last Year",s:"A 4-Week Post-Christmas Formation Series on the Acceleration of Life — and What Formation Requires in a Season That Keeps Getting Faster",felt:true},
      {t:"The Calendar Is Not Your Boss",s:"21 Days of Post-Christmas Formation in the Theology of Time — Whose Calendar You Are Living, Whose Agenda Is Setting It",felt:true},
      {t:"Stop Saying You Do Not Have Time",s:"3 Weeks of Honest Formation in the Difference Between Not Having Time and Not Prioritizing Formation — and What Changes When You Decide It Is Non-Negotiable",felt:true},
      {t:"The Sabbath You Have Not Taken",s:"4 Weeks of Post-Christmas Formation in the Recovery of Rest as a Non-Negotiable Formation Practice — for the Congregation That Has Not Sabbathed in Years",felt:true},
      {t:"Your Phone Knows Where Your Time Goes",s:"21 Days of Formation in Screen Time as Formation Data — What Your Screen Time Report Reveals About Your Actual Priorities",felt:true},
      {t:"The Year Without Hurry",s:"7 Days of Post-Christmas Formation in the Counterformation Practice of Unhurried Living — What Formation Requires That Hurry Destroys",felt:true},
      {t:"January Is Not a Reset",s:"A 3-Week Post-Christmas Formation Series on Why the New Year Does Not Automatically Change Anything — and What Actually Does",felt:true},
      {t:"The 168 Hours You Have This Week",s:"4 Weeks of Post-Christmas Formation in Time Stewardship — Every Week Has the Same Hours, What Changes Is Who Decides What Happens In Them",felt:true},
      {t:"The Morning Matters Most",s:"21 Days of Post-Christmas Formation in the First Hour of the Day — the Practice That Shapes Every Other Practice",felt:true},
      {t:"Slow Down to Speed Up",s:"40 Days of Post-Christmas Formation in the Paradox That Formation Requires Deceleration — the Congregation That Slows in January Moves Further in December",felt:true},
    ]
  },
  {
    id:"vision", arc:"out", num:10,
    name:"Vision and Leadership",
    desc:"Campaigns that use the post-Christmas window to form the congregation's vision and leadership for the year",
    color:"#2a3a58",
    campaigns:[
      {t:"The Year He Has Given",s:"A 6-Week Post-Christmas Vision Campaign — Forming the Congregation Around the Year's Formation Direction"},
      {t:"The Vision Fast",s:"40 Days of Post-Christmas Vision Formation — Prayer, Fasting, and Seeking for the Year Ahead"},
      {t:"The Nehemiah Year",s:"4 Weeks on Nehemiah 1-2 — Building Vision From Prayer, Grief, Assessment, and Action"},
      {t:"The Pastoral Vision",s:"3 Weeks of Formation for the Senior Leadership Team"},
      {t:"The Formation Vision",s:"21 Days of Post-Christmas Formation for the Congregation's Leaders"},
      {t:"The Mission Alignment",s:"6 Weeks of Post-Christmas Mission Alignment — Forming Every Ministry Around One Formation Direction"},
      {t:"The Elders in January",s:"4 Weeks of Post-Christmas Elder Formation"},
      {t:"The Staff Formation Retreat",s:"21 Days of Post-Christmas Staff Formation — Building the Team That Will Form the Congregation"},
      {t:"The Year in One Direction",s:"3 Weeks of Post-Christmas Vision Clarity — One Priority, One Year, One Direction"},
      {t:"From Christmas to the Vision Sunday",s:"40 Days of Post-Christmas Formation Leading to the Annual Vision Sunday"},
      // CONTEMPORARY
      {t:"The Leader Who Did Not Rest at Christmas",s:"A 4-Week Post-Christmas Formation Series for the Senior Pastor or Ministry Leader Who Ran Through December and Arrived in January Empty",felt:true},
      {t:"Your Team Is Watching You",s:"21 Days of Formation for the Leader Whose Team Is Observing What January Looks Like for Them — the Formation of Leadership By Example",felt:true},
      {t:"The Vision You Are Afraid to Name",s:"3 Weeks of Post-Christmas Leadership Formation in the Courage to Say Specifically What God Has Shown You — Not the Generic Vision Statement, the Specific One",felt:true},
      {t:"When the Board Disagrees With the Vision",s:"4 Weeks of Post-Christmas Formation in the Pastoral Art of Leading Through Disagreement — What the Nehemiah Model Offers the Leader Facing Resistance",felt:true},
      {t:"The Leader Nobody Is Forming",s:"21 Days of Formation for the Senior Leader Whose Formation Has Been Sacrificed to the Formation of Everyone Else — the Soul Care of the One Doing the Caring",felt:true},
      {t:"The Strategic Planning Retreat Is Not the Answer",s:"7 Days of Post-Christmas Formation in the Difference Between Strategic Planning and Formation Vision — and Why Congregations That Plan Well Without Praying Well Produce the Wrong Results",felt:true},
      {t:"What the Staff Needs in January",s:"A 3-Week Post-Christmas Formation Campaign for Ministry Leaders — How to Invest in the Team That Is About to Carry the Year",felt:true},
      {t:"The One Thing That Would Change Everything",s:"4 Weeks of Post-Christmas Formation in the Discipline of Discernment — What the Congregation's One Formation Priority Should Be This Year and Why",felt:true},
      {t:"Burnout Is a Formation Problem",s:"21 Days of Post-Christmas Formation for the Leader Who Is Running Out of Everything — What Formation Looks Like From the Bottom of the Tank",felt:true},
      {t:"The Year You Stop Scaling and Start Forming",s:"40 Days of Post-Christmas Vision Formation in the Distinction Between Growth and Formation — What the Congregation Needs That Attendance Metrics Do Not Capture",felt:true},
    ]
  },
];

// ─── TYPE CONFIG ──────────────────────────────────────────────────────────────
const ARC_CONFIG = {
  into: { label:"Coming Into Christmas", color:"#3a5888", bg:"#eef2f8", dot:"#5a78a8" },
  out:  { label:"Coming Out of Christmas", color:"#703828", bg:"#f8f0ec", dot:"#a06040" },
};

// ─── STYLES ───────────────────────────────────────────────────────────────────
const S = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Lato:wght@300;400;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Lato',sans-serif;background:#1a1620;color:#0d1018;}
.app{min-height:100vh;display:flex;flex-direction:column;}

/* HEADER */
.hdr{background:#0a0810;border-bottom:1px solid rgba(201,168,76,.12);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0;}
.hdr-brand{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;color:rgba(255,255,255,.45);letter-spacing:1px;}
.hdr-right{display:flex;align-items:center;gap:14px;}
.hdr-stat{text-align:center;}
.hdr-stat-n{font-family:'Playfair Display',serif;font-size:17px;color:#c9a84c;display:block;line-height:1;}
.hdr-stat-l{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.18);font-weight:700;}
.hdr-tag{font-size:7px;letter-spacing:3px;text-transform:uppercase;font-weight:700;color:#8a6e30;border:1px solid rgba(201,168,76,.2);padding:3px 9px;}

/* TABS */
.tabs{background:#0c0a14;border-bottom:1px solid rgba(255,255,255,.06);display:flex;overflow-x:auto;padding:0 12px;flex-shrink:0;}
.tabs::-webkit-scrollbar{height:2px;background:transparent;}
.tabs::-webkit-scrollbar-thumb{background:rgba(201,168,76,.2);}
.arc-tab{display:flex;align-items:center;gap:7px;padding:10px 14px;font-size:11.5px;font-weight:700;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:all .12s;color:rgba(255,255,255,.3);flex-shrink:0;}
.arc-tab:hover{color:rgba(255,255,255,.6);}
.arc-tab.on{color:var(--ac);border-bottom-color:var(--ac);}
.arc-tab-dot{width:6px;height:6px;border-radius:50%;}
.arc-tab-count{font-size:9px;padding:1px 5px;background:rgba(255,255,255,.06);border-radius:8px;}

/* BODY */
.body{display:flex;flex:1;overflow:hidden;height:calc(100vh - 95px);}

/* SIDEBAR */
.sidebar{width:230px;background:#0c0a14;border-right:1px solid rgba(255,255,255,.06);flex-shrink:0;overflow-y:auto;display:flex;flex-direction:column;}
.sb-sec{padding:12px 14px;border-bottom:1px solid rgba(255,255,255,.05);}
.sb-lbl{font-size:7px;letter-spacing:3px;text-transform:uppercase;font-weight:700;color:rgba(255,255,255,.2);display:block;margin-bottom:9px;}
.search-wrap{position:relative;}
.search-icon{position:absolute;left:9px;top:50%;transform:translateY(-50%);font-size:11px;color:rgba(255,255,255,.25);}
.search-input{width:100%;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:#f4f0e8;padding:7px 10px 7px 28px;font-size:11.5px;font-family:'Lato',sans-serif;outline:none;}
.search-input::placeholder{color:rgba(255,255,255,.22);}
.search-input:focus{border-color:rgba(201,168,76,.35);}

/* FILTER PILLS */
.filter-row{display:flex;gap:4px;flex-wrap:wrap;margin-top:2px;}
.fpill{font-size:8px;padding:3px 8px;border:1px solid rgba(255,255,255,.12);color:rgba(255,255,255,.35);cursor:pointer;transition:all .1s;background:transparent;font-family:'Lato',sans-serif;border-radius:0;}
.fpill:hover{border-color:rgba(201,168,76,.4);color:#c9a84c;}
.fpill.on{border-color:rgba(201,168,76,.5);color:#c9a84c;background:rgba(201,168,76,.08);}

/* CAT FILTERS */
.cat-btn{width:100%;padding:6px 10px;text-align:left;background:transparent;border:none;border-left:2px solid transparent;cursor:pointer;transition:all .1s;display:flex;align-items:center;justify-content:space-between;}
.cat-btn:hover{background:rgba(255,255,255,.03);}
.cat-btn.on{border-left-color:var(--cc);background:rgba(255,255,255,.05);}
.cat-btn-name{font-family:'Playfair Display',serif;font-size:11px;font-style:italic;color:rgba(255,255,255,.4);}
.cat-btn.on .cat-btn-name{color:var(--cc);}
.cat-btn-count{font-size:8px;color:rgba(255,255,255,.2);}
.clear-lnk{font-size:8.5px;color:#c9a84c;cursor:pointer;display:block;padding:7px 10px;letter-spacing:1px;text-transform:uppercase;font-weight:700;}
.clear-lnk:hover{color:#e2c97e;}

/* MAIN */
.main{flex:1;overflow-y:auto;background:#f6f2ea;}

/* ARC BANNER */
.arc-banner{padding:22px 22px 16px;border-bottom:3px solid var(--ac);}
.arc-banner.into-banner{background:linear-gradient(135deg,#020508,#050a12);}
.arc-banner.out-banner{background:linear-gradient(135deg,#060302,#0d0504);}
.ab-kk{font-size:7.5px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:var(--ac);opacity:.8;display:flex;align-items:center;gap:8px;margin-bottom:8px;}
.ab-kk::before{content:'';width:12px;height:1px;background:currentColor;}
.ab-title{font-family:'Playfair Display',serif;font-size:22px;font-weight:400;color:#fff;margin-bottom:6px;}
.ab-title em{font-style:italic;}
.ab-sub{font-size:11px;color:rgba(255,255,255,.4);max-width:700px;line-height:1.6;}
.ab-stats{display:flex;gap:18px;margin-top:12px;}
.ab-stat{text-align:center;}
.ab-stat-n{font-family:'Playfair Display',serif;font-size:18px;color:var(--ac);display:block;line-height:1;}
.ab-stat-l{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.22);font-weight:700;}

/* CATEGORY SECTION */
.cat-section{margin-bottom:2px;}
.cat-hdr-row{display:flex;align-items:flex-start;gap:16px;padding:18px 22px 12px;background:rgba(255,255,255,.6);border-bottom:1px solid rgba(0,0,0,.06);}
.cat-num-big{font-family:'Playfair Display',serif;font-size:42px;font-weight:400;line-height:1;flex-shrink:0;margin-top:-6px;opacity:.12;}
.cat-hdr-text{flex:1;}
.cat-name{font-family:'Playfair Display',serif;font-size:18px;font-style:italic;margin-bottom:3px;}
.cat-desc{font-size:10.5px;color:#888;line-height:1.45;margin-bottom:5px;}
.cat-arc-badge{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:2px 7px;border:1px solid;display:inline-block;}
.cat-hdr-count{font-size:8.5px;color:#bbb;font-weight:600;margin-top:2px;white-space:nowrap;}

/* CAMPAIGN GRID */
.camp-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:4px;padding:4px 6px 8px;}

/* CAMPAIGN CARD */
.cc{padding:12px 13px;background:#fff;border:1px solid rgba(0,0,0,.06);cursor:pointer;transition:all .1s;border-top:2px solid transparent;position:relative;}
.cc:hover{background:#fdfaf4;box-shadow:0 2px 10px rgba(0,0,0,.09);transform:translateY(-1px);}
.cc.felt{background:#fefbf5;border-left:3px solid rgba(201,168,76,.35);}
.cc.selected{box-shadow:0 0 0 2px var(--ac);background:#fffef8;}
.cc-num{font-size:7px;letter-spacing:2px;color:#d0c8b8;font-weight:700;display:block;margin-bottom:4px;}
.cc-felt-tag{font-size:6.5px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;color:#8a6e30;background:rgba(201,168,76,.1);padding:1px 5px;display:inline-block;margin-bottom:4px;}
.cc-title{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;line-height:1.22;color:#0d1018;margin-bottom:4px;}
.cc-sub{font-size:9.5px;color:#888;font-family:'Georgia',serif;font-style:italic;line-height:1.38;}
.cc.selected .cc-sub{display:block;}

/* RESULT HEADER */
.results-hdr{padding:12px 22px 8px;display:flex;align-items:center;justify-content:space-between;background:rgba(255,255,255,.4);border-bottom:1px solid rgba(0,0,0,.06);}
.results-count{font-size:11px;color:#888;}
.results-count strong{color:#333;}

/* DETAIL PANEL */
.detail{background:#fff;border-top:3px solid var(--ac,#c9a84c);padding:18px 22px;position:relative;}
.detail-close{position:absolute;top:12px;right:14px;font-size:15px;cursor:pointer;color:#ccc;}
.detail-felt{font-size:7px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:#8a6e30;background:rgba(201,168,76,.1);padding:2px 8px;display:inline-block;margin-bottom:6px;}
.detail-title{font-family:'Playfair Display',serif;font-size:20px;font-style:italic;color:#0d1018;margin-bottom:5px;line-height:1.2;}
.detail-sub{font-family:'Georgia',serif;font-size:13px;color:#666;font-style:italic;line-height:1.55;margin-bottom:12px;}
.detail-actions{display:flex;gap:8px;}
.detail-btn{font-size:8.5px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;padding:7px 14px;border:1px solid;cursor:pointer;background:transparent;font-family:'Lato',sans-serif;transition:all .1s;}

/* EMPTY */
.empty{text-align:center;padding:60px 20px;}
.empty-icon{font-size:32px;display:block;margin-bottom:10px;}
.empty-text{font-family:'Playfair Display',serif;font-size:17px;font-style:italic;color:#bbb;}

/* AI PANEL */
.ai-panel{background:#080610;border-top:1px solid rgba(255,255,255,.06);flex-shrink:0;}
.ai-toggle{display:flex;align-items:center;gap:10px;padding:9px 20px;cursor:pointer;user-select:none;}
.ai-toggle-lbl{font-size:11px;font-weight:600;color:rgba(255,255,255,.45);}
.ai-badge{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:#c9a84c;border:1px solid rgba(201,168,76,.22);padding:2px 7px;}
.ai-body{padding:14px 20px;border-top:1px solid rgba(255,255,255,.05);}
.ai-row{display:flex;gap:8px;margin-bottom:8px;}
.ai-input{flex:1;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);color:#f4f0e8;padding:8px 11px;font-size:11.5px;font-family:'Lato',sans-serif;outline:none;}
.ai-input::placeholder{color:rgba(255,255,255,.22);}
.ai-input:focus{border-color:rgba(201,168,76,.4);}
.ai-btn{background:#c9a84c;color:#000;border:none;padding:8px 16px;font-size:9.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;white-space:nowrap;transition:background .12s;}
.ai-btn:hover{background:#e2c97e;}
.ai-btn:disabled{opacity:.4;cursor:not-allowed;}
.ai-opts{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:8px;}
.ai-opt{font-size:9px;padding:3px 9px;border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.3);cursor:pointer;background:transparent;font-family:'Lato',sans-serif;transition:all .1s;}
.ai-opt:hover,.ai-opt.on{border-color:rgba(201,168,76,.45);color:#c9a84c;background:rgba(201,168,76,.07);}
.ai-hint{font-size:9.5px;color:rgba(255,255,255,.22);font-style:italic;margin-bottom:8px;}
.ai-thinking{display:flex;align-items:center;gap:10px;padding:10px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.05);margin-bottom:8px;}
.ai-pulse{width:7px;height:7px;border-radius:50%;background:#c9a84c;animation:pulse 1.2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.2;}}
.ai-pulse-txt{font-size:11px;color:rgba(255,255,255,.4);}
.ai-results-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;}
.ai-card{background:rgba(255,255,255,.06);border:1px solid rgba(201,168,76,.18);padding:11px 13px;}
.ai-card-lbl{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:#c9a84c;display:block;margin-bottom:4px;}
.ai-card-title{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;color:#f4f0e8;line-height:1.25;margin-bottom:3px;}
.ai-card-sub{font-size:9px;color:rgba(255,255,255,.4);font-family:'Georgia',serif;font-style:italic;line-height:1.35;}
.ai-error{font-size:11px;color:#e08080;padding:9px;background:rgba(180,50,50,.1);border:1px solid rgba(180,50,50,.2);}

@media(max-width:860px){
  .camp-grid{grid-template-columns:1fr 1fr;}
  .sidebar{width:180px;}
  .ai-results-grid{grid-template-columns:1fr 1fr;}
}
@media(max-width:560px){
  .camp-grid,.ai-results-grid{grid-template-columns:1fr;}
  .sidebar{display:none;}
}
`;

// ─── MAIN APP ─────────────────────────────────────────────────────────────────
export default function ChristmasCampaigns() {
  const [arc, setArc] = useState("into");
  const [search, setSearch] = useState("");
  const [selCat, setSelCat] = useState(null);
  const [feltOnly, setFeltOnly] = useState(false);
  const [selectedCard, setSelectedCard] = useState(null);
  const [aiOpen, setAiOpen] = useState(false);
  const [aiPrompt, setAiPrompt] = useState("");
  const [aiArc, setAiArc] = useState("");
  const [aiResults, setAiResults] = useState([]);
  const [generating, setGenerating] = useState(false);
  const [aiError, setAiError] = useState("");

  const arcCats = useMemo(() => CATEGORIES.filter(c => c.arc === arc), [arc]);
  const ac = arc === "into" ? ARC_CONFIG.into.color : ARC_CONFIG.out.color;

  const filteredCats = useMemo(() => {
    return arcCats.map(cat => {
      let camps = cat.campaigns;
      if (selCat && cat.id !== selCat) return null;
      if (feltOnly) camps = camps.filter(c => c.felt);
      if (search) {
        const q = search.toLowerCase();
        camps = camps.filter(c =>
          c.t.toLowerCase().includes(q) || c.s.toLowerCase().includes(q)
        );
      }
      if (!camps.length) return null;
      return { ...cat, campaigns: camps };
    }).filter(Boolean);
  }, [arcCats, selCat, feltOnly, search]);

  const totalFiltered = filteredCats.reduce((a, c) => a + c.campaigns.length, 0);
  const totalArc = arcCats.reduce((a, c) => a + c.campaigns.length, 0);

  const toggleCat = useCallback(id => {
    setSelCat(p => p === id ? null : id);
    setSelectedCard(null);
  }, []);

  async function generate() {
    if (!aiPrompt.trim() && !aiArc) return;
    setGenerating(true); setAiError(""); setAiResults([]);
    const arcName = aiArc || (arc === "into" ? "Coming Into Christmas" : "Coming Out of Christmas");
    const prompt = `You are a master church curriculum strategist for Lifetogether Ministries. Generate 6 compelling Christmas/Advent campaign titles for SENIOR PASTORS.

Arc: ${arcName}
Pastor's specific need: ${aiPrompt || "Contemporary, felt-need campaign titles that would resonate with today's congregation"}

Rules:
- Each title must feel URGENT and CONTEMPORARY — pastors should feel "my congregation needs this"
- Not generic Sunday school titles — these should stop a tired pastor mid-scroll
- Subtitles should be specific formation arcs (duration + what it produces)
- Mix felt-need language (What your congregation is actually feeling) with theological depth
- The best titles name a pain the congregation has before naming the solution

Respond ONLY with valid JSON, no other text:
[{"title":"...","subtitle":"..."},{"title":"...","subtitle":"..."},{"title":"...","subtitle":"..."},{"title":"...","subtitle":"..."},{"title":"...","subtitle":"..."},{"title":"...","subtitle":"..."}]`;

    try {
      const r = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-6",
          max_tokens: 1000,
          messages: [{ role: "user", content: prompt }]
        })
      });
      const d = await r.json();
      const txt = d.content?.find(b => b.type === "text")?.text || "";
      const clean = txt.replace(/```json|```/g, "").trim();
      setAiResults(JSON.parse(clean));
    } catch {
      setAiError("Generation failed — try a more specific prompt.");
    } finally { setGenerating(false); }
  }

  return (
    <>
      <style>{S}</style>
      <div className="app" style={{ "--ac": ac }}>

        {/* HEADER */}
        <div className="hdr">
          <div className="hdr-brand">Lifetogether · Christmas Campaign System™</div>
          <div className="hdr-right">
            <div className="hdr-stat"><span className="hdr-stat-n">400</span><span className="hdr-stat-l">Campaigns</span></div>
            <div className="hdr-stat"><span className="hdr-stat-n">20</span><span className="hdr-stat-l">Categories</span></div>
            <div className="hdr-stat"><span className="hdr-stat-n">AI</span><span className="hdr-stat-l">Generator</span></div>
            <span className="hdr-tag">2026 Edition</span>
          </div>
        </div>

        {/* ARC TABS */}
        <div className="tabs">
          {[
            { id:"into", label:"Coming Into Christmas", dot:ARC_CONFIG.into.dot, n:200 },
            { id:"out",  label:"Coming Out of Christmas", dot:ARC_CONFIG.out.dot, n:200 },
          ].map(a => (
            <div key={a.id} className={`arc-tab ${arc===a.id?"on":""}`}
              style={{ "--ac": a.id==="into" ? ARC_CONFIG.into.color : ARC_CONFIG.out.color }}
              onClick={() => { setArc(a.id); setSelCat(null); setSelectedCard(null); setSearch(""); }}>
              <div className="arc-tab-dot" style={{ background: a.dot }} />
              {a.label}
              <span className="arc-tab-count">{a.n}</span>
            </div>
          ))}
        </div>

        {/* BODY */}
        <div className="body">

          {/* SIDEBAR */}
          <div className="sidebar">
            <div className="sb-sec">
              <span className="sb-lbl">Search</span>
              <div className="search-wrap">
                <span className="search-icon">🔍</span>
                <input className="search-input" value={search}
                  onChange={e => setSearch(e.target.value)}
                  placeholder="Title or subtitle…" />
              </div>
            </div>
            <div className="sb-sec">
              <span className="sb-lbl">Type</span>
              <div className="filter-row">
                <button className={`fpill ${!feltOnly ? "on" : ""}`} onClick={() => setFeltOnly(false)}>All 200</button>
                <button className={`fpill ${feltOnly ? "on" : ""}`} onClick={() => setFeltOnly(true)}>Felt Need ✦</button>
              </div>
            </div>
            <div className="sb-sec" style={{ flex:1, overflow:"auto" }}>
              <span className="sb-lbl">Category</span>
              {arcCats.map(c => (
                <button key={c.id} className={`cat-btn ${selCat===c.id?"on":""}`}
                  style={{ "--cc": c.color }}
                  onClick={() => toggleCat(c.id)}>
                  <span className="cat-btn-name">{c.name}</span>
                  <span className="cat-btn-count">{c.campaigns.length}</span>
                </button>
              ))}
              {(selCat||feltOnly||search) &&
                <span className="clear-lnk" onClick={() => {setSelCat(null);setFeltOnly(false);setSearch("");}}>✕ Clear all</span>}
            </div>
          </div>

          {/* MAIN */}
          <div className="main">
            {/* ARC BANNER */}
            <div className={`arc-banner ${arc}-banner`} style={{ "--ac": ac }}>
              <p className="ab-kk">{ARC_CONFIG[arc].label}</p>
              <h2 className="ab-title">
                {arc==="into" ? <><em>Preparing</em> the Congregation for Christmas</> : <><em>Carrying</em> the Congregation After Christmas</>}
              </h2>
              <p className="ab-sub">
                {arc==="into"
                  ? "10 categories · 20 campaigns each · Original formation titles + contemporary felt-need campaigns that meet your congregation where they actually are in December."
                  : "10 categories · 20 campaigns each · Original formation titles + contemporary felt-need campaigns that carry the incarnation into January and beyond."}
              </p>
              <div className="ab-stats">
                <div className="ab-stat"><span className="ab-stat-n">200</span><span className="ab-stat-l">Total Campaigns</span></div>
                <div className="ab-stat"><span className="ab-stat-n">100</span><span className="ab-stat-l">Formation Classics</span></div>
                <div className="ab-stat"><span className="ab-stat-n">100</span><span className="ab-stat-l">Felt-Need Contemporary</span></div>
                <div className="ab-stat"><span className="ab-stat-n">10</span><span className="ab-stat-l">Categories</span></div>
              </div>
            </div>

            {/* RESULTS HEADER */}
            <div className="results-hdr">
              <span className="results-count">
                Showing <strong>{totalFiltered}</strong> of <strong>{totalArc}</strong> campaigns
                {selCat && ` in ${arcCats.find(c=>c.id===selCat)?.name}`}
                {feltOnly && " · Felt-Need Only"}
                {search && ` · "${search}"`}
              </span>
            </div>

            {/* SELECTED DETAIL */}
            {selectedCard && (() => {
              const cfg = arc === "into" ? ARC_CONFIG.into : ARC_CONFIG.out;
              return (
                <div className="detail" style={{ "--ac": ac }}>
                  <span className="detail-close" onClick={() => setSelectedCard(null)}>✕</span>
                  {selectedCard.felt && <div className="detail-felt">✦ Contemporary · Felt-Need</div>}
                  <h2 className="detail-title">{selectedCard.t}</h2>
                  <p className="detail-sub">{selectedCard.s}</p>
                  <div className="detail-actions">
                    <button className="detail-btn" style={{ borderColor: ac, color: ac }}
                      onClick={() => { setAiPrompt(`Generate more campaigns like: "${selectedCard.t}"`); setAiOpen(true); }}>
                      → Generate Similar with AI
                    </button>
                    <button className="detail-btn" style={{ borderColor:"#bbb", color:"#999" }}
                      onClick={() => setSelectedCard(null)}>Close</button>
                  </div>
                </div>
              );
            })()}

            {/* CATEGORIES + CARDS */}
            {filteredCats.length === 0 ? (
              <div className="empty">
                <span className="empty-icon">🔍</span>
                <p className="empty-text">No campaigns match — try different search terms</p>
              </div>
            ) : filteredCats.map(cat => (
              <div key={cat.id} className="cat-section">
                <div className="cat-hdr-row">
                  <div className="cat-num-big" style={{ color: cat.color }}>{cat.num < 10 ? `0${cat.num}` : cat.num}</div>
                  <div className="cat-hdr-text">
                    <div className="cat-name" style={{ color: cat.color }}>{cat.name}</div>
                    <div className="cat-desc">{cat.desc}</div>
                    <span className="cat-arc-badge" style={{ color: cat.color, borderColor:`${cat.color}40` }}>
                      {ARC_CONFIG[arc].label}
                    </span>
                  </div>
                  <div className="cat-hdr-count">{cat.campaigns.length} campaigns</div>
                </div>
                <div className="camp-grid">
                  {cat.campaigns.map((camp, i) => {
                    const isSel = selectedCard === camp;
                    return (
                      <div key={i}
                        className={`cc ${camp.felt?"felt":""} ${isSel?"selected":""}`}
                        style={{ borderTopColor: cat.color, "--ac": cat.color }}
                        onClick={() => setSelectedCard(isSel ? null : camp)}>
                        <span className="cc-num">{String((arcCats.indexOf(cat))*20+i+1+(arc==="out"?0:0)).padStart(3,"0")}</span>
                        {camp.felt && <span className="cc-felt-tag">✦ Felt Need</span>}
                        <h3 className="cc-title">{camp.t}</h3>
                        <p className="cc-sub">{camp.s}</p>
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}

            {/* AI PANEL */}
            <div className="ai-panel">
              <div className="ai-toggle" onClick={() => setAiOpen(o => !o)}>
                <span style={{ fontSize:15, color:"#c9a84c" }}>✦</span>
                <span className="ai-toggle-lbl">AI Campaign Title Generator</span>
                <span className="ai-badge">Claude Sonnet · Live</span>
                <span style={{ marginLeft:"auto", color:"rgba(255,255,255,.25)", fontSize:11 }}>{aiOpen?"▲":"▼"}</span>
              </div>

              {aiOpen && (
                <div className="ai-body">
                  <p className="ai-hint">Describe your congregation's felt need, season, or theme — Claude will generate 6 original campaign titles not in the library above.</p>
                  <div className="ai-row">
                    <input className="ai-input" value={aiPrompt}
                      onChange={e => setAiPrompt(e.target.value)}
                      placeholder="e.g. families with prodigal adult children, grief in December, burned-out pastors…"
                      onKeyDown={e => e.key === "Enter" && generate()} />
                    <button className="ai-btn" disabled={generating || (!aiPrompt.trim() && !aiArc)} onClick={generate}>
                      {generating ? "Generating…" : "Generate →"}
                    </button>
                  </div>
                  <div className="ai-opts">
                    <span className="ai-hint" style={{ marginRight:4, alignSelf:"center" }}>Focus:</span>
                    {["Coming Into Christmas","Coming Out of Christmas","Felt-Need & Contemporary","Theological Depth","Pastoral Care","Outreach & Evangelism","Family Formation","Justice & Community"].map(opt => (
                      <button key={opt} className={`ai-opt ${aiArc===opt?"on":""}`}
                        onClick={() => setAiArc(aiArc===opt?"":opt)}>
                        {opt}
                      </button>
                    ))}
                  </div>
                  {generating && (
                    <div className="ai-thinking">
                      <div className="ai-pulse" />
                      <span className="ai-pulse-txt">Generating 6 original campaign titles…</span>
                    </div>
                  )}
                  {aiError && <div className="ai-error">{aiError}</div>}
                  {aiResults.length > 0 && (
                    <div className="ai-results-grid">
                      {aiResults.map((r, i) => (
                        <div key={i} className="ai-card">
                          <span className="ai-card-lbl">AI · {arc === "into" ? "Coming In" : "Coming Out"}</span>
                          <p className="ai-card-title">{r.title}</p>
                          <p className="ai-card-sub">{r.subtitle}</p>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              )}
            </div>

          </div>
        </div>
      </div>
    </>
  );
}
