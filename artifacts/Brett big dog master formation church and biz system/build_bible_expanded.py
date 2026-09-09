
CSS = open('/tmp/flagship_css.txt').read() if __import__('os').path.exists('/tmp/flagship_css.txt') else ""

# We'll write a self-contained HTML — no dependency on CSS file
STYLES = """
:root{
  --navy:#02040a;--gold:#c9a84c;--gold-lt:#e2c97e;--gold-dk:#8a6e30;
  --cream:#f8f5ef;--ink:#0e1218;--paper:#f3efe7;
  --c1:#4a5a8a;  /* deep blue — Bible campaigns */
  --c2:#4a7a50;  /* forest — characters */
  --c3:#8a4a30;  /* copper — stories/themes */
  --muted:#8a9ab5;--rule:rgba(201,168,76,0.10);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Lato',sans-serif;background:#ccc8c0;color:var(--ink);}
.page{max-width:1200px;margin:0 auto;background:var(--cream);box-shadow:0 4px 80px rgba(0,0,0,.22);}

/* COVER */
.cover{background:var(--navy);min-height:94vh;display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden;}
.cover-glow{position:absolute;inset:0;background:radial-gradient(ellipse at 20% 70%,rgba(74,90,138,.08),transparent 50%),radial-gradient(ellipse at 80% 20%,rgba(74,122,80,.05),transparent 50%),linear-gradient(180deg,#010306,#020510);}
.cover-top{padding:48px 80px 0;position:relative;z-index:2;display:flex;justify-content:space-between;align-items:flex-start;}
.cover-logo{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;color:rgba(255,255,255,.35);letter-spacing:2px;}
.cover-tag{font-size:7px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:var(--gold-dk);border:1px solid rgba(201,168,76,.18);padding:4px 11px;}
.cover-body{padding:56px 80px 72px;position:relative;z-index:2;}
.cover-ey{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;color:rgba(201,168,76,.8);display:flex;align-items:center;gap:12px;margin-bottom:18px;}
.cover-ey::before{content:'';width:28px;height:1px;background:rgba(201,168,76,.5);}
.cover-h1{font-family:'Playfair Display',serif;font-size:clamp(36px,5.5vw,80px);font-weight:400;line-height:.9;color:#fff;letter-spacing:-2px;margin-bottom:18px;}
.cover-h1 em{font-style:italic;color:var(--gold);}
.cover-rule{display:flex;align-items:center;gap:12px;margin:22px 0;}
.cover-rule-line{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.cover-rule-dot{width:5px;height:5px;background:var(--gold);transform:rotate(45deg);flex-shrink:0;}
.cover-sub{font-family:'Playfair Display',serif;font-size:clamp(14px,1.8vw,20px);font-weight:300;font-style:italic;color:rgba(212,196,168,.85);max-width:700px;line-height:1.6;margin-bottom:40px;}
.cover-stats{display:grid;grid-template-columns:repeat(6,1fr);max-width:840px;border:1px solid rgba(201,168,76,.18);}
.cstat{padding:14px 15px;border-right:1px solid rgba(201,168,76,.12);text-align:center;}
.cstat:last-child{border-right:none;}
.cstat-n{font-family:'Playfair Display',serif;font-size:22px;color:var(--gold);display:block;line-height:1;}
.cstat-l{font-size:6px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.2);font-weight:700;display:block;margin-top:3px;}

/* COLLECTION HEADER */
.coll-header{padding:48px 80px 20px;border-top:6px solid;}
.coll-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.coll-kk::before{content:'';width:18px;height:1px;background:currentColor;}
.coll-h2{font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,52px);font-weight:400;line-height:.92;margin-bottom:10px;}
.coll-h2 em{font-style:italic;}
.coll-sub{font-family:'Georgia',serif;font-size:14px;color:#555;line-height:1.75;max-width:800px;margin-bottom:8px;}
.coll-count{font-size:8px;letter-spacing:3px;text-transform:uppercase;font-weight:700;border:1px solid;display:inline-block;padding:4px 12px;margin-top:6px;}

/* CATEGORY BLOCK */
.cat-block{padding:0 80px 10px;}
.cat-hdr{display:flex;align-items:center;gap:14px;padding:20px 0 12px;border-bottom:2px solid;margin-bottom:10px;}
.cat-num{font-family:'Playfair Display',serif;font-size:28px;color:rgba(255,255,255,.12);flex-shrink:0;line-height:1;}
.cat-name{font-family:'Playfair Display',serif;font-size:clamp(16px,2vw,24px);font-weight:400;font-style:italic;}
.cat-desc{font-size:11px;color:#666;margin-top:2px;line-height:1.4;}
.cat-books{font-size:9px;letter-spacing:1px;color:#888;margin-top:3px;}

/* SERIES GRID */
.series-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;padding-bottom:20px;}
.s-card{padding:12px 14px;border:1px solid rgba(0,0,0,.06);background:rgba(255,255,255,.55);}
.s-card:nth-child(1){grid-column:1/-1;border-width:2px;background:rgba(255,255,255,.75);}
.s-card:nth-child(2),.s-card:nth-child(3){grid-column:span 2;}
.s-num{font-size:8px;letter-spacing:2px;color:#bbb;font-weight:700;display:block;margin-bottom:4px;}
.s-title{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;color:var(--ink);line-height:1.25;margin-bottom:3px;}
.s-card:nth-child(1) .s-title{font-size:16px;}
.s-sub{font-size:10px;color:#7a6a5a;line-height:1.35;}
.s-card:nth-child(1) .s-sub{font-size:11.5px;}
.s-ref{font-size:8px;color:#aaa;margin-top:4px;letter-spacing:.5px;}
.s-badge{display:inline-block;font-size:7px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;padding:2px 6px;border:1px solid;margin-top:4px;}

/* HDIV */
.hdiv{height:3px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.2),transparent);}
.sdiv{height:1px;background:var(--rule);margin:0 80px;}

/* PULL QUOTE */
.pull{margin:0 80px 28px;padding:18px 24px;border-left:4px solid var(--gold);background:rgba(201,168,76,.04);}
.pull p{font-family:'Playfair Display',serif;font-size:clamp(14px,1.7vw,19px);font-style:italic;color:var(--ink);line-height:1.5;}

/* BACK */
.back{background:#010406;padding:48px 80px;text-align:center;}
.back-q{font-family:'Playfair Display',serif;font-size:clamp(13px,1.8vw,18px);font-style:italic;color:var(--cream);max-width:740px;margin:0 auto 16px;line-height:1.5;}
.back-a{font-size:8.5px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.back-c{margin-top:12px;font-size:11.5px;color:#5a6a7a;}
.back-c a{color:var(--gold-lt);text-decoration:none;}
.lm{font-family:'Playfair Display',serif;font-size:28px;color:#fff;font-style:italic;margin-top:22px;}

@media(max-width:960px){
  .cover-top,.cover-body,.coll-header,.cat-block,.pull,.back{padding-left:28px;padding-right:28px;}
  .pull{margin-left:28px;margin-right:28px;}
  .sdiv{margin:0 28px;}
  .series-grid{grid-template-columns:1fr 1fr;}
  .s-card:nth-child(1),.s-card:nth-child(2),.s-card:nth-child(3){grid-column:auto;}
  .cover-stats{grid-template-columns:repeat(3,1fr);}
}
"""

def e(s):
    import html
    return html.escape(str(s))

def card(n, title, sub, ref, badge=None, color="#4a5a8a"):
    badge_html = f'<span class="s-badge" style="border-color:{color};color:{color};">{e(badge)}</span>' if badge else ""
    return f"""<div class="s-card">
  <span class="s-num">{n:02d}</span>
  <p class="s-title">{e(title)}</p>
  <p class="s-sub">{e(sub)}</p>
  <p class="s-ref">{e(ref)}</p>
  {badge_html}
</div>"""

def cat_section(num, name, desc, books, color, entries):
    cards_html = "".join(card(i+1, t, s, r, b, color) for i,(t,s,r,b) in enumerate(entries))
    return f"""<div class="cat-block">
  <div class="cat-hdr" style="border-color:{color};">
    <span class="cat-num">{num:02d}</span>
    <div>
      <h3 class="cat-name" style="color:{color};">{e(name)}</h3>
      <p class="cat-desc">{e(desc)}</p>
      {f'<p class="cat-books">{e(books)}</p>' if books else ""}
    </div>
  </div>
  <div class="series-grid">
    {cards_html}
  </div>
</div>"""

def coll_header(color, kk, h2, sub, count):
    return f"""<div class="hdiv"></div>
<section class="coll-header" style="border-color:{color};">
  <p class="coll-kk" style="color:{color};">{e(kk)}</p>
  <h2 class="coll-h2">{h2}</h2>
  <p class="coll-sub">{e(sub)}</p>
  <span class="coll-count" style="border-color:{color};color:{color};">{e(count)}</span>
</section>"""

# ══════════════════════════════════════════════════════════════════════════════
# COLLECTION 1: 250 BIBLE CAMPAIGNS — 10 CATEGORIES × 25 EACH
# ══════════════════════════════════════════════════════════════════════════════

BIBLE_CAMPAIGNS = [

  # CAT 1: FRESH ANGLES ON THE PENTATEUCH
  ("Fresh Angles on the Pentateuch", "25 alternative campaign approaches to the first five books — same texts, new formation angles", "Genesis · Exodus · Leviticus · Numbers · Deuteronomy", "#4a5a8a", [
    ("The Image Bearers","What it means to carry the image of God into every Monday morning","Genesis 1–2","40-Day"),
    ("The God Who Starts Over","Seven stories in Genesis of beginnings after collapse","Genesis 1–11","21-Day"),
    ("The Ancestors of Faith","The formation of Abraham, Isaac, Jacob, and Joseph as a single arc","Genesis 12–50","6-Week"),
    ("Chosen for This","The theology of election from Abraham to Joseph — why God picks the unexpected","Genesis","40-Day"),
    ("The Burning Ordinary","Moses and the presence of God in the unremarkable places","Exodus 1–4","7-Day"),
    ("Plagues and Promises","Ten signs, one God, and the congregation that has been waiting for deliverance","Exodus 7–15","3-Week"),
    ("The Tabernacle and You","What the detailed instructions for God's dwelling place say about the nature of holy presence","Exodus 25–40","4-Week"),
    ("The Holiness Code for the Unholy","Leviticus as the formation manual for ordinary people who want to live near God","Leviticus","40-Day"),
    ("The Sacred Calendar","The seven feasts of Israel as a formation arc for the full year","Leviticus 23","7-Week"),
    ("Every Sacrifice Tells a Story","The five offerings of Leviticus and what they say about how we approach a holy God","Leviticus 1–7","5-Week"),
    ("The Grumbling Congregation","Numbers as the anatomy of a complaining church — and the God who stays with it anyway","Numbers","40-Day"),
    ("Water from the Rock Twice","The formation cost of the leader who gets it right, then fails — Moses' complete arc","Numbers 11–27","3-Week"),
    ("The Spy Report","Caleb and Joshua vs. the ten — faith when the majority vote against","Numbers 13–14","3-Week"),
    ("Remember and Obey","Deuteronomy's formation architecture for the second generation","Deuteronomy","40-Day"),
    ("The Shema Every Morning","Hear, O Israel — the formation practice of the greatest commandment","Deuteronomy 6","7-Day"),
    ("A Land You Did Not Cultivate","The theology of unearned blessing and the formation of gratitude","Deuteronomy 6–8","3-Week"),
    ("Choices Set Before You","Life and death, blessing and curse — the architecture of covenant obedience","Deuteronomy 30","21-Day"),
    ("The Song of Moses","Deuteronomy 32 as a formation text for the congregation living between promise and possession","Deuteronomy 32","3-Week"),
    ("Blessings Before the End","Jacob's blessing of his twelve sons as a formation text for legacy","Genesis 49","2-Week"),
    ("The Coat of Many Colors","Joseph's story as the theology of providence — what God was doing all along","Genesis 37–50","6-Week"),
    ("Midwives and Mothers","The women of Exodus as the hidden formation infrastructure of the exodus","Exodus 1–2","3-Week"),
    ("The Golden Calf and After","The formation crisis of Exodus 32 — idolatry, intercession, restoration","Exodus 32–34","3-Week"),
    ("Tent of Meeting","Exodus 33 as the most intimate portrait of prayer in the Torah","Exodus 33","7-Day"),
    ("The Forty Years","Wilderness theology — what God was forming in the years that felt like waste","Numbers–Deuteronomy","40-Day"),
    ("Balaam's Donkey","Five stories from Numbers of God using the unexpected to communicate the urgent","Numbers 22–25","2-Week"),
  ]),

  # CAT 2: HISTORICAL BOOKS — NEW ANGLES
  ("Historical Books — New Angles", "25 fresh campaign approaches to Israel's story in the land — conquest, kings, exile, return", "Joshua · Judges · Ruth · 1–2 Samuel · 1–2 Kings · 1–2 Chronicles · Ezra · Nehemiah · Esther", "#3a6a7a", [
    ("Be Strong and Very Courageous","The four commands to Joshua as a formation architecture for leaders in transition","Joshua 1","4-Week"),
    ("Stones of Remembrance","The twelve stones of Joshua 4 and the formation of communal memory","Joshua 4","3-Week"),
    ("A Long Obedience in the Same Direction","Joshua as the theology of faithful completion","Joshua","6-Week"),
    ("The Walls That Fell","Jericho and the formation of trust — marching when marching looks like foolishness","Joshua 6","2-Week"),
    ("There Is No King","Judges and the formation crisis of doing what is right in your own eyes","Judges","40-Day"),
    ("The Reluctant Judge","Gideon's formation from hiding in a winepress to leading an army","Judges 6–8","4-Week"),
    ("Samson Unsanctified","Strength without character — the most relevant story in Judges for the current moment","Judges 13–16","3-Week"),
    ("The Story at Harvest","Ruth as a theology of faithfulness, belonging, and the God who redeems","Ruth","3-Week"),
    ("Where You Go I Will Go","Ruth and Naomi and the formation of loyalty — the rarest virtue","Ruth 1","2-Week"),
    ("The God Who Hears","Hannah and the formation of prayer in the season of unanswered longing","1 Samuel 1–2","3-Week"),
    ("Not as Man Sees","The anointing of David and the formation of a theology of hiddenness","1 Samuel 16","3-Week"),
    ("Friendship as Formation","Jonathan and David as the model of covenant friendship","1 Samuel 18–20","3-Week"),
    ("The Man After God's Own Heart","The full arc of David — chosen, anointed, failing, repenting, restored","1–2 Samuel","40-Day"),
    ("Psalm 51 and After","The formation that follows failure — David's repentance as a complete theology","2 Samuel 11–12","4-Week"),
    ("Elijah Under the Juniper Tree","The prophet who ran after the fire — burnout and restoration","1 Kings 19","3-Week"),
    ("Still Small Voice","The formation of listening — what came after the wind, earthquake, and fire","1 Kings 19","2-Week"),
    ("The Divided Kingdom","Why Israel split — and what it says about the formation cost of pride","1 Kings 12","2-Week"),
    ("Mantle to Mantle","Elijah and Elisha and the formation of succession — how you pass something on","1–2 Kings","4-Week"),
    ("Rebuilding the Altar","Ezra's return and the first thing the community did — not the walls, the altar","Ezra 3","3-Week"),
    ("The Prayer of Nehemiah","Nehemiah 1 as the most compressed model of prayer and action in Scripture","Nehemiah 1","2-Week"),
    ("Builders with Swords","Nehemiah's formation approach to doing hard things in a hostile environment","Nehemiah 4–6","4-Week"),
    ("Such a Time as This","Esther and the formation of courage for the person who has access","Esther","3-Week"),
    ("The God Who Is Not Mentioned","Esther's formation theology — providence in the book where God is hidden","Esther","40-Day"),
    ("The Prayer of Jabez Recovered","1 Chronicles 4:10 and the formation of audacious asking — what the prayer actually says","1 Chronicles 4","2-Week"),
    ("Temple Theology","Solomon's dedication of the temple and what it says about the place where God dwells","1 Kings 8","3-Week"),
  ]),

  # CAT 3: WISDOM LITERATURE — NEW ANGLES
  ("Wisdom Literature — New Angles", "25 alternative formation approaches to Job, Psalms, Proverbs, Ecclesiastes, Song of Songs", "Job · Psalms · Proverbs · Ecclesiastes · Song of Solomon", "#6a4a8a", [
    ("The Silence of God","Job 1–2 and the formation of trust before the theological arguments begin","Job 1–2","4-Week"),
    ("Where Were You","God's answer from the whirlwind as a formation text on the limits of human wisdom","Job 38–41","3-Week"),
    ("The Friends We Don't Need","Job's three friends and the formation of pastoral wisdom — what not to say","Job 3–37","4-Week"),
    ("The Psalms of Ascent","Psalms 120–134 as a complete formation pilgrimage in fifteen songs","Psalms 120–134","15-Day"),
    ("The Lament Psalms","Seven psalms of lament as a formation theology for the season of loss","Various Psalms","7-Week"),
    ("When the Heavens Are Silent","Psalms of divine hiddenness — formation for the person whose prayers seem unanswered","Psalms 22, 44, 88","3-Week"),
    ("Blessed Is the One","The beatitude structure of Psalm 1 as a formation gateway to the Psalter","Psalm 1","7-Day"),
    ("O Lord You Have Searched Me","Psalm 139 as the most intimate portrait of divine knowledge in Scripture","Psalm 139","2-Week"),
    ("A Thousand Years","Psalm 90 — Moses' prayer and the formation of a theology of time","Psalm 90","2-Week"),
    ("The Lord Is My Shepherd for Life","Psalm 23 at every stage — child, adult, elder, dying — what the shepherd means in each season","Psalm 23","4-Week"),
    ("Wisdom's Seven Pillars","Proverbs 9 and the structure of wisdom — what the house is and how to enter it","Proverbs 9","7-Day"),
    ("The Fear of the Lord","Proverbs' foundational conviction — what it means and what it produces","Proverbs","40-Day"),
    ("Two Women in Proverbs","Lady Wisdom and the Woman of Folly as a formation theology of competing voices","Proverbs 1–9","4-Week"),
    ("The Capable Wife Revisited","Proverbs 31 as a formation text about character rather than productivity","Proverbs 31","3-Week"),
    ("For Everything a Season","Ecclesiastes 3 as a formation theology of time, loss, and the gift of the present","Ecclesiastes 3","4-Week"),
    ("Vanity and Grace","Ecclesiastes and the gospel — what meaninglessness reveals that abundance conceals","Ecclesiastes","40-Day"),
    ("Two Are Better Than One","Ecclesiastes 4 on the formation of community — the cord that is not quickly broken","Ecclesiastes 4","3-Week"),
    ("Remember Your Creator","Ecclesiastes 12 and the formation of a life that ends well","Ecclesiastes 12","3-Week"),
    ("Arise My Love","Song of Songs and the formation of eros as gift — desire as theology","Song of Songs","6-Week"),
    ("I Am My Beloved's","The Song of Songs as a formation text on belonging — the deepest human need","Song of Songs","4-Week"),
    ("Do Not Awaken Love","The formation restraint at the center of Song of Songs — the time for everything","Song of Songs 2,3,8","3-Week"),
    ("The Wounded Heart","Job and Psalms together — the formation library for congregations in pain","Job 1–2 · Psalms 22, 42","6-Week"),
    ("Wisdom for the Wandering","Proverbs and Ecclesiastes together — what to seek and why the seeking is not enough","Proverbs · Ecclesiastes","6-Week"),
    ("The Honest Prayer","Lament Psalms and Job together — a formation theology of bringing everything to God","Job · Psalms","40-Day"),
    ("Ancient Wisdom for the Digital Age","Proverbs on speech, attention, friendship, and money — the most current book in the Bible","Proverbs","21-Day"),
  ]),

  # CAT 4: MAJOR PROPHETS — NEW ANGLES
  ("Major Prophets — New Angles", "25 alternative campaign approaches to Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel", "Isaiah · Jeremiah · Lamentations · Ezekiel · Daniel", "#8a4a30", [
    ("The Year the King Died","Isaiah 6 and the formation that happens in the season of collapse","Isaiah 6","4-Week"),
    ("The Servant Songs","Isaiah's four servant songs as a formation Christology before Christ","Isaiah 42, 49, 50, 52–53","4-Week"),
    ("A New Thing","Second Isaiah and the formation of a congregation that can't see the new thing God is doing","Isaiah 40–55","40-Day"),
    ("Beautiful Feet","Isaiah 52:7 and the formation of a congregation sent to announce good news","Isaiah 52","3-Week"),
    ("The Messianic Highway","Isaiah's prophecies of the coming king — a pre-Christmas formation arc","Isaiah 7, 9, 11, 40, 52–53","Advent"),
    ("Comfort My People Deeply","Isaiah 40 and the formation theology of comfort — not sentiment, but strength","Isaiah 40","4-Week"),
    ("Before I Formed You","Jeremiah 1 and the formation of a theology of calling before you felt called","Jeremiah 1","3-Week"),
    ("The Linen Belt","Jeremiah's acted parables — what it means to be ruined by proximity to God","Jeremiah 13, 18, 19, 27","4-Week"),
    ("New Covenant","Jeremiah 31 and the promise of a law written on the heart rather than in stone","Jeremiah 31","4-Week"),
    ("Seek the Peace of the City","Jeremiah 29 and the formation of a congregation that flourishes in exile","Jeremiah 29","40-Day"),
    ("The Letter to the Exiles","Jeremiah 29 as a formation text for the congregation that has not arrived where it was headed","Jeremiah 29","21-Day"),
    ("How Long","Lamentations and the formation of grief — what it means to mourn without losing faith","Lamentations","3-Week"),
    ("His Mercies Are New Every Morning","Lamentations 3 inside the darkest book — the formation of hope inside despair","Lamentations 3","7-Day"),
    ("Four Living Creatures","Ezekiel's vision and the formation of a theology of God's mobility — he is not confined","Ezekiel 1","3-Week"),
    ("The Watchman","Ezekiel as a formation text for preachers and leaders — the weight of the word you carry","Ezekiel 3, 33","4-Week"),
    ("Dry Bones Can Live","Ezekiel 37 and the formation of a theology of resurrection — in the church, not just at the end","Ezekiel 37","4-Week"),
    ("The River from the Temple","Ezekiel 47 and the formation of a congregation that is the source of flourishing","Ezekiel 47","3-Week"),
    ("The Shepherd and the Flock","Ezekiel 34 and the formation of pastoral accountability — the most honest text on leadership","Ezekiel 34","4-Week"),
    ("Faithful in Babylon Deep","Daniel 1–6 and the formation of a theology of integrity in a hostile culture","Daniel 1–6","6-Week"),
    ("Even If He Does Not","Daniel 3 and the formation of faith that does not require rescue to remain faith","Daniel 3","3-Week"),
    ("The Writing on the Wall","Daniel 5 and the formation of a theology of warning — reading the signs before it is too late","Daniel 5","2-Week"),
    ("The Seventy Weeks","Daniel 9 and the formation of intercession for a city and a generation","Daniel 9","4-Week"),
    ("Son of Man","Daniel 7's vision and the formation of a Christology built on the Ancient of Days","Daniel 7","3-Week"),
    ("Where Is Your God","Isaiah 36–39 and Hezekiah — the formation of a leader who prays when threatened","Isaiah 36–39","4-Week"),
    ("Streams in the Desert","Isaiah 43–44 and the formation of trust when the route seems impassable","Isaiah 43–44","3-Week"),
  ]),

  # CAT 5: MINOR PROPHETS — NEW ANGLES
  ("Minor Prophets — New Angles", "25 fresh formation approaches to the twelve short prophets with enormous formation weight", "Hosea · Joel · Amos · Obadiah · Jonah · Micah · Nahum · Habakkuk · Zephaniah · Haggai · Zechariah · Malachi", "#5a7a3a", [
    ("God's Broken Heart","Hosea 11 — the most tender portrait of God's love in the Old Testament","Hosea 11","3-Week"),
    ("The Unfaithful Spouse","Hosea's marriage as a formation text for understanding covenant — God's side of the relationship","Hosea 1–3","4-Week"),
    ("Rend Your Hearts Not Your Garments","Joel 2 and the formation theology of genuine repentance","Joel 2","3-Week"),
    ("Pour Out My Spirit","Joel 2:28-29 and the formation of a congregation that expects the Spirit to show up","Joel 2:28–29","3-Week"),
    ("Let Justice Roll Down","Amos and the formation of a congregation that does not separate worship from ethics","Amos","40-Day"),
    ("The Plumb Line","Amos 7 and the formation of a theology of measurement — what God uses to evaluate","Amos 7","3-Week"),
    ("Though the Vision Tarry","Habakkuk's prayer and the formation of waiting — when the answer does not come on schedule","Habakkuk","4-Week"),
    ("The Just Shall Live by Faith","Habakkuk 2:4 and the formation of the convictions that hold you when the circumstances don't","Habakkuk 2","3-Week"),
    ("Running from the Right Thing","Jonah and the formation cost of refusing the call you actually received","Jonah","21-Day"),
    ("What the Lord Requires of You","Micah 6:8 and the formation of a congregation built around justice, mercy, and humility","Micah 6:8","40-Day"),
    ("The Remnant Shall Return","Micah 4–5 and the formation of hope — what the end of the story changes about the middle","Micah 4–5","3-Week"),
    ("The Great Day of the Lord","Zephaniah and the formation of a congregation that lives in light of what is coming","Zephaniah","3-Week"),
    ("He Will Rejoice Over You","Zephaniah 3:17 and the formation of a theology of divine delight","Zephaniah 3:17","2-Week"),
    ("Consider Your Ways","Haggai and the formation of a congregation that has been building everything except the right thing","Haggai","3-Week"),
    ("Not by Might","Zechariah 4:6 and the formation of a theology of Spirit-dependence in leadership","Zechariah 4","3-Week"),
    ("I Have Loved You","Malachi 1 and the formation of a theology of love that the congregation doubts","Malachi 1","4-Week"),
    ("Return to Me","Malachi 3 and the formation of a congregation that has drifted from its first love","Malachi 3","4-Week"),
    ("Will a Man Rob God","Malachi 3:10 and the formation of a generosity theology — the tithe as formation, not program","Malachi 3","4-Week"),
    ("The Vineyard","Amos · Isaiah 5 · Hosea together — three prophets, one image, one formation question","Various Prophets","4-Week"),
    ("The Valley of Dry Bones and Joel's Army","Ezekiel 37 and Joel 2 together — the formation theology of spiritual awakening","Ezekiel 37 · Joel 2","3-Week"),
    ("The Reluctant and the Willing","Jonah and Isaiah 6 together — the prophet who ran and the prophet who said 'send me'","Jonah · Isaiah 6","3-Week"),
    ("Prepare the Way","Malachi 4 · Isaiah 40 · Mark 1 together — the formation arc of expectancy","Malachi 4 · Isaiah 40","Advent"),
    ("The Righteous Remnant","Micah, Zephaniah, and Zechariah on the small faithful community that God preserves","Micah · Zeph · Zech","4-Week"),
    ("Anger, Grief, and Love","Hosea, Amos, and Lamentations together — the emotional range of God toward his people","Hosea · Amos · Lam","40-Day"),
    ("The Promise of the Spirit","Joel 2 · Zechariah 12 · Ezekiel 36 together — a pneumatology built from the prophets","Joel · Zech · Ezek","3-Week"),
  ]),

  # CAT 6: GOSPELS — NEW ANGLES
  ("The Gospels — New Angles", "25 fresh formation approaches to Matthew, Mark, Luke, and John", "Matthew · Mark · Luke · John", "#4a5a8a", [
    ("The Sermon That Changed Everything","The Beatitudes as a complete formation theology of who is blessed and why","Matthew 5–7","40-Day"),
    ("The Kingdom Is Like","Twelve parables of the kingdom as a formation catechism for what Jesus came to build","Matthew 13","6-Week"),
    ("Two Builders","Matthew 7's closing parable as a formation text for the gap between hearing and doing","Matthew 7","3-Week"),
    ("The Upside Down Kingdom","The Beatitudes as a systematic theology of reversal — what the world values vs. what God values","Matthew 5","21-Day"),
    ("The Lord's Prayer Deeply","Matthew 6:9-13 as a complete formation arc — one phrase per week","Matthew 6:9–13","7-Week"),
    ("Immediately","Mark's formation theology — the 41 uses of 'immediately' in the most urgent Gospel","Mark","3-Week"),
    ("The Servant King","Mark as a complete theology of Christus Victor — who Jesus is by what he does","Mark","40-Day"),
    ("Twelve Hours of the Passion","Mark 14–16 and the formation of a complete passion theology","Mark 14–16","Holy Week"),
    ("The Year of the Lord's Favor","Luke 4 and the formation of a congregation that announces the same thing Jesus announced","Luke 4","4-Week"),
    ("The Lost Are Found","Luke 15's three parables together — a formation theology of recovery","Luke 15","4-Week"),
    ("The Magnificat","Mary's song as a formation text for the congregation living in the upside-down kingdom","Luke 1:46–55","Advent"),
    ("Table Fellowship","Luke's twelve meal scenes and the formation theology of who Jesus eats with","Luke","6-Week"),
    ("The Prodigal and the Elder","Luke 15 as a complete formation text for the person who ran and the person who stayed","Luke 15","4-Week"),
    ("Zacchaeus Come Down","Five outsider encounter stories in Luke — the formation of a congregation that welcomes the excluded","Luke","5-Week"),
    ("In the Beginning Was the Word","John 1's prologue as a complete Christology in eighteen verses","John 1:1–18","4-Week"),
    ("The Seven I Am's","John's formation catechism — who Jesus says he is and what each claim demands of the believer","John 6–15","7-Week"),
    ("The Seven Signs","John's seven miracles as a formation theology of belief — what each sign is designed to produce","John 2–11","7-Week"),
    ("Living Water","John 4 and the formation theology of what the soul is actually thirsting for","John 4","3-Week"),
    ("The Upper Room","John 13–17 and the formation theology of the night before — what Jesus said when time was short","John 13–17","5-Week"),
    ("Abide in Me","John 15 and the formation theology of union — the branch and the vine as spiritual formation","John 15","4-Week"),
    ("Unless I Go","John 16 and the formation theology of the Holy Spirit — better that Jesus leaves","John 16","3-Week"),
    ("High Priestly Prayer","John 17 and the formation of a congregation praying what Jesus prayed","John 17","4-Week"),
    ("Thomas and the Wounds","John 20 and the formation of a theology of doubt — what Jesus does with the person who needs to see","John 20","3-Week"),
    ("Do You Love Me","John 21 and the formation of Peter — the threefold restoration after the threefold denial","John 21","3-Week"),
    ("The Women at the Tomb","The four Gospel resurrection accounts and the formation theology of being the first witness","Matt 28 · Mark 16 · Luke 24 · John 20","Easter"),
  ]),

  # CAT 7: ACTS AND EARLY CHURCH — NEW ANGLES
  ("Acts and the Early Church — New Angles", "25 fresh formation approaches to the book of Acts", "Acts · Paul's Missionary Journeys · The Birth of the Church", "#3a6a7a", [
    ("The Promise of the Father","Acts 1 and the formation of a congregation learning to wait before it launches","Acts 1","3-Week"),
    ("Rushing Wind","Pentecost and the formation of a theology of the Spirit that is not reducible to emotion","Acts 2","4-Week"),
    ("They Devoted Themselves","Acts 2:42-47 as the DNA of the church — the formation practices that produce everything else","Acts 2:42–47","40-Day"),
    ("Silver and Gold I Have None","Peter's Acts 3 healing and the formation of a congregation that gives what it actually has","Acts 3","3-Week"),
    ("The First Martyr","Stephen's sermon and death — the formation of a theology of dying well","Acts 6–7","4-Week"),
    ("The Road to Damascus","Paul's conversion and the formation of a theology of the sudden turnaround","Acts 9","3-Week"),
    ("A Man Called Barnabas","The formation theology of encouragement — the people who show up when nobody else does","Acts 4, 9, 11","3-Week"),
    ("Cornelius and the Outsider","Acts 10 and the formation of a congregation that does not decide who God can reach","Acts 10","4-Week"),
    ("Prison and Praise","Acts 16 and the formation of a theology of worship in confinement","Acts 16","3-Week"),
    ("Mars Hill","Paul's Athens sermon and the formation of cultural engagement without cultural capitulation","Acts 17","3-Week"),
    ("The Ephesian Riot","Acts 19 and the formation of a congregation whose impact changes the economy","Acts 19","3-Week"),
    ("All Night Long","Eutychus and the formation theology of the congregation that stays to hear the whole thing","Acts 20","2-Week"),
    ("The Shipwreck","Acts 27 and the formation of a theology of storms — Paul's calm in the catastrophic","Acts 27","3-Week"),
    ("Unhindered","Acts 28's final word and the formation theology of a gospel that cannot be stopped","Acts 28","3-Week"),
    ("Lydia's Household","Acts 16 and the formation theology of the first European convert — faith and household","Acts 16","3-Week"),
    ("The Antioch Church","Acts 11–13 and the formation of the sending church — the church that produced Paul","Acts 11–13","4-Week"),
    ("Priscilla and Aquila","Acts 18 and the formation of a theology of lay leadership — the tent-makers who discipled Apollos","Acts 18","3-Week"),
    ("The Jerusalem Council","Acts 15 and the formation of a theology of disagreement — how the church makes hard decisions","Acts 15","3-Week"),
    ("Philip and the Ethiopian","Acts 8 and the formation of a theology of one-on-one — the extraordinary ordinary encounter","Acts 8","3-Week"),
    ("The Church That Prayed for Peter","Acts 12 and the formation of a congregation that prays when it can do nothing else","Acts 12","3-Week"),
    ("Apollos and the More Perfect Way","Acts 18 and the formation of a theology of incomplete but sincere faith — and who completes it","Acts 18","3-Week"),
    ("The Widows and the Word","Acts 6 and the formation of a congregation that structures itself so the word is not neglected","Acts 6","3-Week"),
    ("Ananias and Sapphira","Acts 5 and the formation of a congregation that takes the community of goods with complete seriousness","Acts 5","3-Week"),
    ("When Paul Passed Through","The three missionary journeys as a formation arc for a congregation that understands itself as sent","Acts 13–21","6-Week"),
    ("From Jerusalem to Rome","Acts as a complete formation theology of how the gospel travels — step by step, person by person","Acts 1–28","40-Day"),
  ]),

  # CAT 8: PAUL'S LETTERS — NEW ANGLES
  ("Paul's Letters — New Angles", "25 fresh formation approaches to the Pauline epistles", "Romans · 1–2 Corinthians · Galatians · Ephesians · Philippians · Colossians · Thessalonians · Pastorals", "#7a4a8a", [
    ("The Righteousness of God","Romans 1–5 as a systematic formation theology of what God does when people can't","Romans 1–5","5-Week"),
    ("Dead to Sin Alive to God","Romans 6 and the formation of a theology of identity — what baptism says about who you are","Romans 6","4-Week"),
    ("The Good I Want to Do","Romans 7 and the formation of a congregation that is honest about the struggle","Romans 7","3-Week"),
    ("No Condemnation","Romans 8:1-17 and the formation of a congregation living from the verdict not toward it","Romans 8:1–17","4-Week"),
    ("The Spirit Prays for Us","Romans 8:26-27 and the formation of a theology of intercession that is not dependent on our adequacy","Romans 8:26–27","3-Week"),
    ("Nothing Can Separate","Romans 8:31-39 and the formation theology of unconditional security — building the unshakeable","Romans 8:31–39","40-Day"),
    ("Living Sacrifice","Romans 12 and the formation of a congregation that offers itself daily, not just Sunday","Romans 12","6-Week"),
    ("The Cross Is Foolishness","1 Corinthians 1–2 and the formation of a congregation that is not ashamed of an offensive gospel","1 Corinthians 1–2","3-Week"),
    ("The Body Has Many Parts","1 Corinthians 12 and the formation of a congregation where every gift is necessary","1 Corinthians 12","4-Week"),
    ("The Most Excellent Way","1 Corinthians 13 in its context — the formation of love as the grammar all gifts must speak","1 Corinthians 13","4-Week"),
    ("Resurrection Reality","1 Corinthians 15 and the formation of a theology of bodily resurrection — not just life after death","1 Corinthians 15","4-Week"),
    ("Afflicted but Not Crushed","2 Corinthians 4 and the formation of a congregation that carries treasure in clay jars","2 Corinthians 4","4-Week"),
    ("Generosity as Grace","2 Corinthians 8–9 and the formation theology of giving as participation in something larger","2 Corinthians 8–9","4-Week"),
    ("The Thorn in the Flesh","2 Corinthians 12 and the formation of a theology of weakness as the site of strength","2 Corinthians 12","3-Week"),
    ("Crucified with Christ","Galatians 2:20 and the formation of a complete theology of union with Christ","Galatians 2","4-Week"),
    ("Heirs with Abraham","Galatians 3 and the formation of a theology of belonging — who is in the family of God","Galatians 3","3-Week"),
    ("The Fruit of the Spirit","Galatians 5:22-23 and the formation of the character that walking in the Spirit produces","Galatians 5","7-Week"),
    ("Seated in Heavenly Places","Ephesians 2 and the formation of a theology of position — where you already are before you do anything","Ephesians 2","3-Week"),
    ("The Fullness of God","Ephesians 3:14-21 — Paul's prayer for formation — and what it means to be filled to all the fullness","Ephesians 3","4-Week"),
    ("Put On the New Self","Ephesians 4 and the formation of a complete theology of transformation — off and on","Ephesians 4","4-Week"),
    ("The Armor of God","Ephesians 6 not as metaphor but as formation practice — what each piece actually trains","Ephesians 6","6-Week"),
    ("I Have Learned","Philippians 4:11 and the formation of contentment as a learned skill, not a natural temperament","Philippians 4","4-Week"),
    ("The Mind of Christ","Philippians 2 and the formation of a congregation that has the pattern of the incarnation inside it","Philippians 2","4-Week"),
    ("Christ Is All","Colossians 1–2 and the formation of a Christology so complete it leaves no room for addition","Colossians 1–2","4-Week"),
    ("Set Your Minds","Colossians 3 and the formation of a congregation that thinks differently — the cognitive dimension of sanctification","Colossians 3","4-Week"),
  ]),

  # CAT 9: GENERAL EPISTLES — NEW ANGLES
  ("General Epistles — New Angles", "25 fresh formation approaches to Hebrews, James, Peter, John, and Jude", "Hebrews · James · 1–2 Peter · 1–3 John · Jude", "#8a5a3a", [
    ("The Hall of Faith Revisited","Hebrews 11 and the formation of a congregation that understands the cloud of witnesses","Hebrews 11","6-Week"),
    ("Therefore Run","Hebrews 12:1-2 and the formation theology of the 'therefore' — what the cloud of witnesses demands","Hebrews 12","3-Week"),
    ("Greater Than","Hebrews' systematic comparison of Jesus to everything Israel held — and the formation of worship","Hebrews","40-Day"),
    ("The Melchizedek Priesthood","Hebrews 7 and the formation of a complete theology of Jesus as our high priest","Hebrews 7","4-Week"),
    ("Confident Access","Hebrews 4:14-16 and the formation of a congregation that approaches God without shame","Hebrews 4","3-Week"),
    ("Holding Fast","Hebrews' five warning passages and the formation of perseverance in a congregation that wants to quit","Hebrews","5-Week"),
    ("Faith Without Works Is Dead","James as the most practical formation text in the New Testament — what belief looks like on Tuesday","James","40-Day"),
    ("The Wisdom That Comes from Above","James 3 and the formation of a congregation that controls its tongue because it has the right wisdom","James 3","3-Week"),
    ("Trials and Maturity","James 1 and the formation of a congregation that receives difficulty as formation rather than rejection","James 1","3-Week"),
    ("Chosen and Exiles","1 Peter 1–2 and the formation of a congregation that understands its dual citizenship","1 Peter 1–2","4-Week"),
    ("The Living Stone","1 Peter 2:4-10 and the formation of a theology of who the church is — a holy nation","1 Peter 2","4-Week"),
    ("Suffering According to God's Will","1 Peter 3–4 and the formation of a congregation that does not interpret suffering as evidence against God","1 Peter 3–4","4-Week"),
    ("Grace in the Fiery Trial","1 Peter 4:12-19 and the formation theology of the surprising furnace of formation","1 Peter 4","3-Week"),
    ("Humble Yourselves","1 Peter 5 and the formation of a congregation that practices the most countercultural virtue","1 Peter 5","3-Week"),
    ("The Divine Nature","2 Peter 1 and the formation of a congregation participating in something beyond itself","2 Peter 1","4-Week"),
    ("The Day of the Lord","2 Peter 3 and the formation of a congregation that lives in light of the certain end","2 Peter 3","3-Week"),
    ("God Is Light","1 John 1 and the formation of a theology of honesty — walking in the light as a community practice","1 John 1","4-Week"),
    ("Love One Another","1 John 4 and the formation of a congregation where the evidence of God's presence is love","1 John 4","40-Day"),
    ("We Love Because He First","1 John 4:19 and the formation of a complete theology of motivation — love as response not program","1 John 4","3-Week"),
    ("Perfect Love Casts Out Fear","1 John 4:18 and the formation of a congregation where people are not afraid of God","1 John 4","3-Week"),
    ("The New Commandment","John 13 and 1 John together — the formation of a community built on the commandment to love","John 13 · 1 John","4-Week"),
    ("Contend for the Faith","Jude and the formation of a congregation that knows what it believes and why","Jude","3-Week"),
    ("The Beloved Disciple","1 John and the formation of a theology of belovedness — what it means to be loved by God","1 John","40-Day"),
    ("Walk in the Truth","2–3 John and the formation of a congregation where truth and love are both non-negotiable","2–3 John","2-Week"),
    ("The Full Armor","Hebrews · James · 1 Peter together — faith, works, and suffering as a complete formation trinity","Hebrews · James · 1 Peter","6-Week"),
  ]),

  # CAT 10: REVELATION — NEW ANGLES
  ("Revelation and Eschatology — New Angles", "25 fresh formation approaches to Revelation, apocalyptic hope, and the end of the story", "Revelation · Apocalyptic Passages · The New Creation", "#8a3a4a", [
    ("Letters to Seven Real Churches","Revelation 2–3 not as prophecy but as pastoral evaluation — what Jesus says to the church that looks like yours","Revelation 2–3","7-Week"),
    ("Worthy Is the Lamb","Revelation 4–5 and the formation of a worship theology built on the throne room","Revelation 4–5","4-Week"),
    ("The Sealed and the Sealed","Revelation 7 and the formation of a congregation that knows it belongs to God before the storm","Revelation 7","3-Week"),
    ("Babylon and the New Jerusalem","Revelation 17–21 as a formation theology of two cities — and which one you are building","Revelation 17–21","5-Week"),
    ("He Who Has an Ear","Revelation's seven repeated calls to hear — the formation of a congregation that listens","Revelation 2–3","7-Day"),
    ("Come Lord Jesus","Revelation 22 and the formation of a congregation shaped by maranatha — the prayer that changes how you live","Revelation 22","3-Week"),
    ("The Four Horsemen Reimagined","Revelation 6 and the formation of a theology of history — what God is doing in the chaos","Revelation 6","4-Week"),
    ("The Great Multitude","Revelation 7:9-17 and the formation of a congregation that sees itself as part of something global","Revelation 7","3-Week"),
    ("New Heaven New Earth","Revelation 21–22 and the formation of a theology of hope that is embodied, not merely spiritual","Revelation 21–22","4-Week"),
    ("The Mark and the Seal","Revelation 13–14 and the formation of a congregation that has made the foundational choice","Revelation 13–14","3-Week"),
    ("The Millennium","Revelation 20 and the formation of a congregation that holds its eschatology with faith and humility","Revelation 20","3-Week"),
    ("Overcomers","Revelation's seven promises to the one who overcomes — a formation arc across the letters","Revelation 2–3","7-Week"),
    ("Alpha and Omega","Revelation's five 'I am' statements of Jesus — a formation Christology for the last book","Revelation 1, 21–22","5-Week"),
    ("The Lamb Who Was Slain","Revelation's lamb imagery — a formation theology of power through sacrifice","Revelation 5–14","4-Week"),
    ("The Bowls of Wrath","Revelation 15–16 and the formation of a congregation that understands divine justice","Revelation 15–16","3-Week"),
    ("The Victorious Church","Revelation's vision of the church triumphant — a formation theology of certain outcome","Revelation 7, 11, 14","4-Week"),
    ("Marriage Supper of the Lamb","Revelation 19 and the formation of a congregation that lives as the bride, not the guest","Revelation 19","3-Week"),
    ("The Book of Life","Revelation's formation theology of name and identity — whose book you are written in","Revelation 3, 20–21","3-Week"),
    ("The Tree of Life Returns","Revelation 22 and Genesis 3 together — the formation arc of Scripture from exile to return","Genesis 3 · Revelation 22","4-Week"),
    ("The Woman Clothed with the Sun","Revelation 12 and the formation of a theology of the church in spiritual warfare","Revelation 12","3-Week"),
    ("Fear God Alone","Revelation and Daniel together — the formation of a congregation that has the right fear","Daniel · Revelation","40-Day"),
    ("The End of Tears","Revelation 21:4 and the formation of a theology of comfort for the congregation in grief","Revelation 21","3-Week"),
    ("Behold I Am Coming","Revelation's three 'I am coming soon' announcements and the formation of readiness","Revelation 22","Advent"),
    ("The Throne Room Always","Revelation 4–5 as a daily formation practice — the throne room that is always accessible","Revelation 4–5","40-Day"),
    ("The Whole Story","Genesis to Revelation — the formation of a congregation that knows the arc and lives inside it","Genesis–Revelation","40-Day"),
  ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# COLLECTION 2: 200 BIBLICAL CHARACTER SERIES — 20 CATEGORIES × 10
# ══════════════════════════════════════════════════════════════════════════════

CHAR_SERIES = [
  ("The Patriarchs", "Founding fathers of faith — men who encountered God before there was a written word", "", "#4a5a8a", [
    ("Adam: The Weight of the Image","The first man and the formation cost of being made in the image of a God you then tried to replace","Genesis 1–3 · Romans 5","40-Day"),
    ("Noah: The Last One Standing","The formation of a man who built for a flood he had never seen in a world that mocked him","Genesis 6–9","3-Week"),
    ("Abraham: Called into the Unknown","The formation of the father of faith — leaving without knowing where you are going","Genesis 12–25","6-Week"),
    ("Isaac: The Quiet Patriarch","The most overlooked of the patriarchs — and the formation of a life that holds the promise without spectacle","Genesis 21–28","4-Week"),
    ("Jacob: The Wrestler","The formation of the man who fought with God and got a limp instead of a victory","Genesis 25–35","6-Week"),
    ("Joseph: From Pit to Palace","Providence in the most brutal classroom — the formation of a man who forgave the people who tried to destroy him","Genesis 37–50","40-Day"),
    ("Enoch: The One Who Walked With God","Genesis 5:24 and the formation theology of a man whose greatest achievement was a relationship","Genesis 5 · Hebrews 11","2-Week"),
    ("Melchizedek: The Mysterious Priest","The priest who appeared before the priesthood existed — and what he says about the formation of Jesus as high priest","Genesis 14 · Hebrews 7","3-Week"),
    ("Lot: The Man Who Chose the Well-Watered Plain","The formation cost of choosing proximity to Sodom — and the mercy that followed anyway","Genesis 13–19","3-Week"),
    ("Terah: The Man Who Almost Made It","The father of Abraham who left Ur and stopped at Haran — and the formation question of the incomplete journey","Genesis 11:31","2-Week"),
  ]),

  ("The Matriarchs and Women of the Old Testament", "Women whose formation stories are among the most honest and formation-rich in Scripture", "", "#6a4a8a", [
    ("Sarah: The Laughter of the Impossible","The formation of a woman who laughed at the promise and received it anyway","Genesis 12–23","4-Week"),
    ("Hagar: The God Who Sees","El Roi — the formation of a woman who met God in the wilderness when no one else was looking","Genesis 16, 21","3-Week"),
    ("Rebekah: The Woman Who Ran","The formation of decisive faith — and the formation cost of manipulation for a good outcome","Genesis 24, 27","4-Week"),
    ("Miriam: The Prophetess and the Leprosy","The formation of a leader who celebrated the exodus and paid for the pride","Exodus 15 · Numbers 12","3-Week"),
    ("Deborah: The Mother of Israel","The formation of a woman who led when the men would not — and what that says about calling","Judges 4–5","3-Week"),
    ("Ruth: Loyal When Loyalty Cost Something","The formation of faithfulness in the foreign woman who chose a people not her own","Ruth","4-Week"),
    ("Hannah: The Vow of Desperation","The formation of a woman who prayed a prayer so intense the priest thought she was drunk","1 Samuel 1–2","3-Week"),
    ("Abigail: Wisdom in a Difficult Marriage","The formation of courage and discernment in the woman who stood between David's anger and disaster","1 Samuel 25","3-Week"),
    ("Esther: The Beauty and the Burden","The formation of a woman who used her access for the people who had none","Esther","40-Day"),
    ("The Proverbs 31 Woman Re-Examined","Not a checklist — a formation portrait of the woman whose character outlasts her productivity","Proverbs 31","4-Week"),
  ]),

  ("The Kings", "Rulers of Israel and Judah whose formation stories trace the line between faithfulness and collapse", "", "#8a4a30", [
    ("Saul: The King Who Had Everything","The formation cost of a man who had the gifts and lost the character","1 Samuel 9–31","6-Week"),
    ("David: Shepherd, King, Psalmist, Sinner","The most complete formation portrait in the Old Testament — the full arc","1 Samuel 16 – 1 Kings 2","40-Day"),
    ("Solomon: Wisdom and the Wives","The man who asked for wisdom and lost it — and the formation theology of the divided heart","1 Kings 1–11","6-Week"),
    ("Josiah: The Young King Who Found the Book","The formation of a king who heard the law read and tore his robes — and changed a nation","2 Kings 22–23","3-Week"),
    ("Hezekiah: Spreads the Letter Before the Lord","The formation of a king under siege who took the threat to God instead of to an alliance","2 Kings 18–20","4-Week"),
    ("Asa: Good and Then Not","The formation cost of starting well and finishing poorly — the most common failure pattern in the kings","2 Chronicles 14–16","3-Week"),
    ("Jehoshaphat: The Alliance Trap","The good king who kept marrying into trouble — and the formation of the boundaries a good leader needs","2 Chronicles 17–20","3-Week"),
    ("Manasseh: The Worst King Who Repented","The formation theology of late-in-life repentance — the man who undid everything and then came back","2 Kings 21 · 2 Chron 33","4-Week"),
    ("Uzziah: Pride in the Sanctuary","The king who was strong until he wasn't — and the formation moment of overreach","2 Chronicles 26","3-Week"),
    ("Cyrus: The Pagan Who Served God's Purpose","The formation theology of how God uses those outside the community to accomplish the community's purpose","Isaiah 44–45 · Ezra 1","3-Week"),
  ]),

  ("The Queens and Women of Power", "Women in positions of influence whose formation stories challenge every assumption about power", "", "#6a3a7a", [
    ("The Queen of Sheba: Wisdom Sought","The formation of a powerful woman who traveled far to sit at the feet of a wiser king","1 Kings 10","2-Week"),
    ("Jezebel: The Architecture of Corruption","The formation cost of a leader who used religious power for political ends","1 Kings 18–21","3-Week"),
    ("Athaliah: The Mother Who Consumed","The formation theology of a woman whose ambition destroyed what she was supposed to protect","2 Kings 11","2-Week"),
    ("Bathsheba: From Object to Counselor","The formation arc from the most passive role to the most active — the woman who secured Solomon's throne","2 Samuel 11–12 · 1 Kings 1","4-Week"),
    ("The Widow of Zarephath: The Last Handful","The formation of a woman whose last act of generosity became her provision","1 Kings 17","2-Week"),
    ("Rahab: The Scarlet Thread","The formation of a woman whose profession did not define her destiny — the outsider who became an insider","Joshua 2, 6 · Hebrews 11","3-Week"),
    ("Jael: The Tent Peg and the Victory","The formation theology of the unlikely instrument — the woman who finished what the general was afraid to start","Judges 4–5","2-Week"),
    ("Vashti: The Queen Who Said No","The formation of integrity when compliance was expected — the refusal that made Esther's story possible","Esther 1","2-Week"),
    ("Peninnah and Hannah: Two Wives","The formation theology of provocation and pain — what God was doing in the cruelty Hannah endured","1 Samuel 1","3-Week"),
    ("The Daughters of Zelophehad: The Women Who Asked","Numbers 27 and the formation of women who petitioned God for what was right — and won","Numbers 27","2-Week"),
  ]),

  ("The Prophets", "Men and women who spoke God's word when the word was unwelcome", "", "#4a7a50", [
    ("Moses: The Most Reluctant Prophet","The formation of a man who argued with God at a burning bush and ended up writing five books","Exodus 3–4 · Deuteronomy 34","40-Day"),
    ("Elijah: Fire and Exhaustion","The formation of the prophet who called down fire and then asked to die under a bush","1 Kings 17–19","4-Week"),
    ("Elisha: The Double Portion","The formation of the successor — the man who asked for what no human could grant","1–2 Kings","5-Week"),
    ("Isaiah: Called in the Year of Collapse","The formation of a prophet who saw the throne when the earthly throne was empty","Isaiah 6–55","40-Day"),
    ("Jeremiah: The Weeping Prophet","The formation of the man who preached for forty years with no visible result","Jeremiah","40-Day"),
    ("Ezekiel: The Strange Commands","The formation of the prophet told to do things he did not understand — and the formation theology of obedient strangeness","Ezekiel","40-Day"),
    ("Daniel: Excellence Without Compromise","The formation of a man who reached the highest levels of a pagan government without becoming pagan","Daniel 1–12","40-Day"),
    ("Amos: The Shepherd Prophet","The formation of a man who was not trained for what God called him to do — and did it anyway","Amos","3-Week"),
    ("Jonah: The Prophet Who Ran","The formation of a man whose obedience was reluctant, whose anger was real, and whose story ends unresolved","Jonah","21-Day"),
    ("Anna: The Eighty-Four Year Wait","Luke 2 and the formation of a prophet who prayed in the temple for decades until the answer arrived","Luke 2","2-Week"),
  ]),

  ("The Warriors and Judges", "Men and women who led Israel when it had no king and the land needed defending", "", "#7a5a3a", [
    ("Joshua: Be Strong and Very Courageous","The formation of a leader who followed a legend and finished the mission","Joshua","40-Day"),
    ("Caleb: Still Strong at Eighty-Five","The formation of the man who waited forty-five years for the mountain God promised and climbed it when he got there","Numbers 13–14 · Joshua 14","3-Week"),
    ("Gideon: From Hiding to Leading","The formation of a man who threshed wheat in a winepress and ended up leading three hundred against thousands","Judges 6–8","4-Week"),
    ("Deborah: Under the Palm Tree","The formation of the judge who led Israel in battle because the general wouldn't go without her","Judges 4–5","3-Week"),
    ("Jephthah: The Vow That Cost Everything","The formation tragedy of the warrior whose father rejected him and whose vow destroyed him","Judges 11","3-Week"),
    ("Samson: Strength Without Submission","The formation cost of a man with a gift but without the character to steward it","Judges 13–16","4-Week"),
    ("Barak: The Leader Who Needed a Companion","The formation of a man who would not go without Deborah — and the formation theology of leaders who need community","Judges 4","3-Week"),
    ("Othniel: The First Judge","The formation of the pattern — what judges were supposed to be before they became what they became","Judges 3","2-Week"),
    ("Ehud: The Left-Handed Deliverer","The formation theology of God using the non-dominant hand — the unexpected instrument","Judges 3","2-Week"),
    ("Jonathan: The Armor-Bearer's Faith","The formation of a man who attacked an entire garrison with one companion and a theological conviction","1 Samuel 14","3-Week"),
  ]),

  ("The Twelve Disciples", "The original formation community — twelve men whose stories are among the most honest in the New Testament", "", "#3a6a7a", [
    ("Peter: Sinking and Rising","The formation of the fisherman who became the rock and the man who denied Christ and led the church","Matthew 4 · 16 · 26 · John 21","40-Day"),
    ("John: The Beloved Who Learned to Love","The formation of the Son of Thunder who ended up writing the most tender documents in the New Testament","Mark 3 · John 13 · 1 John","40-Day"),
    ("James: The First Martyr Among the Twelve","The formation of the man who asked for the best seat and received the earliest death","Mark 3 · 10 · Acts 12","3-Week"),
    ("Andrew: Always Bringing Someone","The formation of the disciple who is always introducing someone else to Jesus","John 1 · 6 · 12","3-Week"),
    ("Thomas: Honest Doubt","The formation of the disciple who would not believe until he saw — and Jesus who came back for him","John 11 · 14 · 20","3-Week"),
    ("Matthew: The Tax Collector Who Left Everything","The formation of a man who left a profitable career immediately and then wrote the most Jewish Gospel","Matthew 9 · Matthew 1–28","3-Week"),
    ("Nathanael: Can Anything Good Come","The formation of the skeptic who became a follower before he had seen anything — just from a conversation","John 1","2-Week"),
    ("Philip: Show Us the Father","The formation of the disciple who asked the most theologically loaded question at the worst possible time","John 1 · 6 · 12 · 14","3-Week"),
    ("Simon the Zealot and Judas Iscariot","The two disciples at opposite ends — the nationalist and the betrayer — and what Jesus was forming in a community that included both","Luke 6 · Matthew 26","3-Week"),
    ("Judas: The Treasurer Who Kept Stealing","The formation tragedy of the man closest to Jesus who never let Jesus form him","John 6 · 12 · 13","4-Week"),
  ]),

  ("Women of the Gospels", "Women who encountered Jesus and were formed by the encounter — and who formed the community around them", "", "#8a4a6a", [
    ("Mary of Nazareth: The Pondering Heart","The formation of the mother of Jesus — from 'let it be' to 'they have no wine' to the cross","Luke 1–2 · John 2 · 19","40-Day"),
    ("Mary Magdalene: First Witness","The formation of the woman who was the first to see the risen Christ — and why she was chosen","Luke 8 · John 20","3-Week"),
    ("Martha and Mary: Two Ways of Being Present","The formation of the two sisters — and the formation question of the one thing necessary","Luke 10 · John 11–12","4-Week"),
    ("The Woman at the Well: Five Husbands and Living Water","The formation of a woman whose shame became her testimony — 'come see a man who told me everything'","John 4","3-Week"),
    ("The Woman Who Washed His Feet","The formation of extravagant gratitude — the woman who gave what she had in the way she could","Luke 7","3-Week"),
    ("The Hemorrhaging Woman: Twelve Years","The formation of the woman who spent everything and received one touch that changed everything","Mark 5","3-Week"),
    ("The Syrophoenician Mother: Even the Dogs","The formation of persistent faith in the woman who would not be dismissed — and what Jesus found in her","Matthew 15 · Mark 7","3-Week"),
    ("The Widow's Two Mites","The formation of generosity — the woman who gave all she had while the rich gave from their surplus","Mark 12","2-Week"),
    ("Salome: The Request for the Best Seats","The formation of the mother whose ambition for her sons became a theology of servant greatness","Matthew 20","2-Week"),
    ("The Women at the Cross and Tomb","The formation of the community that stayed when the twelve fled — and received the first resurrection news","Luke 23–24 · John 19–20","4-Week"),
  ]),

  ("The Unlikely Heroes", "Men and women whose formation stories are built precisely on their unsuitability for the task", "", "#5a7a3a", [
    ("Rahab: The Harlot in the Genealogy","The formation of a woman whose past was her qualification — the outsider through whom the line continued","Joshua 2 · Matthew 1","3-Week"),
    ("Jael: The Tent Peg as Formation","The woman who won the battle the general was too afraid to finish — and the theology of unexpected instruments","Judges 4–5","2-Week"),
    ("Naaman's Servant Girl: The Unnamed Witness","2 Kings 5 and the formation theology of the person nobody thought was important who changed everything","2 Kings 5","2-Week"),
    ("The Widow Who Fed the Prophet","1 Kings 17 and the formation of the last handful — the woman who had nothing to give and gave it","1 Kings 17","2-Week"),
    ("Zacchaeus: The Short Man and the Long Transformation","The formation of the man who climbed a tree to see Jesus and came down a different person","Luke 19","2-Week"),
    ("Bartimaeus: The Blind Beggar Who Shouted","The formation of persistence — the man who was told to be quiet and shouted louder","Mark 10","2-Week"),
    ("The Gerasene Demoniac: From Tombs to the Town","The formation of the man who lived among tombs and became the first Gentile missionary","Mark 5","2-Week"),
    ("Onesimus: The Runaway Who Came Back","The formation of the slave whose flight became a return — and the formation theology of Philemon","Philemon","2-Week"),
    ("Ananias: The Unknown Disciple Who Changed History","Acts 9 and the formation of the man God sent to the most dangerous person in Damascus","Acts 9","2-Week"),
    ("Lydia: The Purple Seller Who Opened a Continent","Acts 16 and the formation of the first European convert — the businesswoman whose home became the first European church","Acts 16","2-Week"),
  ]),

  ("The Villains and Foils", "The men and women whose formation stories are cautionary — the ones the text holds up not as models but as mirrors", "", "#8a3a3a", [
    ("Pharaoh: When the Heart Hardens","The formation theology of the man God used to display his power — and the question of where the hardening began","Exodus 4–14","4-Week"),
    ("Saul: The Rejected King","The formation cost of a man who chose his own wisdom over God's command — the anatomy of spiritual decline","1 Samuel 13–31","6-Week"),
    ("Ahab: The Spineless King","The formation cost of a leader who knew what was right and chose Jezebel's way instead","1 Kings 16–22","4-Week"),
    ("Absalom: The Beautiful Rebel","The formation tragedy of the most gifted man in David's kingdom who used beauty and access to take a throne","2 Samuel 13–18","4-Week"),
    ("Balaam: The Prophet for Hire","The formation tragedy of the man with genuine prophetic gifting who sold it — and what God did anyway","Numbers 22–24","3-Week"),
    ("Nabal: The Fool Who Almost Died","The formation of the man whose name meant 'fool' — and the wife who saved him from the consequences","1 Samuel 25","2-Week"),
    ("Achan: The Hidden Thing","The formation theology of the small hidden sin that stopped an entire army — what is buried under your tent","Joshua 7","3-Week"),
    ("Diotrephes: The Church Member Who Refused John","3 John and the formation theology of the person who loves to be first — in every congregation","3 John","2-Week"),
    ("The Rich Young Ruler: Almost","Mark 10 and the formation tragedy of the man who asked the right question, got the right answer, and walked away","Mark 10","3-Week"),
    ("Ananias and Sapphira: The Half Gift","Acts 5 and the formation theology of the gift given to impress — and what God's response says about the community","Acts 5","3-Week"),
  ]),

  ("The Exiles", "Men and women whose formation happened far from home — in the places of displacement and loss", "", "#4a6a9a", [
    ("Daniel in Babylon","The formation of a man who would not eat the king's food — integrity as the first formation decision","Daniel 1","40-Day"),
    ("Shadrach Meshach and Abednego","The formation of three men who said 'even if he does not' — and the formation theology of deliverance you are not guaranteed","Daniel 3","3-Week"),
    ("Ezekiel Among the Exiles","The formation of the prophet who was himself an exile — and the visions that came in Babylon","Ezekiel 1–3","4-Week"),
    ("Nehemiah in the Persian Court","The formation of the cupbearer who became the builder — faith and strategy in exile","Nehemiah 1–2","4-Week"),
    ("Ezra the Scribe","The formation of the man who rebuilt the community around the word — not the walls first, the word","Ezra 7–10","3-Week"),
    ("Esther in the Palace","The formation of a woman who hid her identity and then had to reveal it — the theology of hidden witness","Esther","40-Day"),
    ("Joseph in Egypt","The formation of the exile whose suffering was the preparation for the rescue — the long game of providence","Genesis 37–50","40-Day"),
    ("Ruth in Bethlehem","The formation of the refugee who said 'your people shall be my people' — exile as the beginning of belonging","Ruth","3-Week"),
    ("Paul in Prison","The formation letters written in chains — Ephesians, Philippians, Colossians, Philemon","Ephesians · Phil · Col","40-Day"),
    ("John on Patmos","The formation of the exile who received the most comprehensive vision in Scripture — and the theology of seeing from the margins","Revelation 1","4-Week"),
  ]),

  ("The Reformers and Rebuilders", "Men and women who rebuilt what had collapsed — whose formation was the restoration of something lost", "", "#5a6a3a", [
    ("Josiah: The Boy King Who Found the Law","The formation of a king who heard the word and changed everything — the reformation in two chapters","2 Kings 22–23","3-Week"),
    ("Hezekiah: The King Who Opened the Temple","The formation of a king who inherited a closed temple and opened it in the first week of his reign","2 Chronicles 29–31","3-Week"),
    ("Nehemiah: Building the Wall in 52 Days","The formation of the rebuilder — prayer, planning, persistence, and opposition","Nehemiah","40-Day"),
    ("Ezra: Rebuilding Around the Word","The formation of the scribe-reformer — the man who brought the Book back to the center","Ezra","4-Week"),
    ("Zerubbabel: Finishing What Others Started","The formation of the governor who led the first wave of return and built the second temple","Ezra 1–6 · Haggai · Zechariah","4-Week"),
    ("Haggai: Stirring Up the Builders","The formation of the prophet whose two-chapter book woke up a stalled congregation","Haggai","3-Week"),
    ("Paul to the Corinthians","The formation of the church-planter who returned to the most difficult church he founded — twice","1–2 Corinthians","40-Day"),
    ("Apollos: The One Who Was Corrected","The formation of the eloquent preacher who received correction with grace — and grew","Acts 18","2-Week"),
    ("Priscilla and Aquila: The Tent-Making Reformers","The formation of the lay couple who discipled Apollos and built the church in three cities","Acts 18 · Romans 16","3-Week"),
    ("Timothy: The Young Pastor Paul Left Behind","The formation of the next generation — what Paul gave Timothy and what Timothy gave the church","1–2 Timothy","40-Day"),
  ]),

  ("The Wisdom Figures", "Men and women whose formation stories are about the acquisition of wisdom — through obedience, suffering, and proximity to God", "", "#4a5a8a", [
    ("Solomon in His Prime","The formation of wisdom as gift and practice — before the decline","1 Kings 3–10","4-Week"),
    ("Job's Friends: What Not to Wisdom","The formation theology of the wrong kind of wisdom — confident, systematic, and wrong","Job 3–37","4-Week"),
    ("Job After the Whirlwind","The formation of wisdom that comes from encounter rather than explanation","Job 38–42","3-Week"),
    ("Bezalel: The Artisan Filled with the Spirit","Exodus 35 and the formation of a wisdom that is craftsmanship — the Spirit given for making things","Exodus 31, 35","2-Week"),
    ("Jethro: The Father-in-Law Who Saw Clearly","Exodus 18 and the formation of a leader who received wisdom from an outsider — and changed","Exodus 18","2-Week"),
    ("The Wise Men: Wisdom That Traveled","The formation of the Magi — men who followed wisdom wherever it led, even to a manger","Matthew 2","Advent"),
    ("Gamaliel: The Wisdom of Restraint","Acts 5 and the formation of the Pharisee whose advice protected the early church from the Sanhedrin","Acts 5","2-Week"),
    ("Priscilla: The Woman Who Taught Apollos","The formation of a woman who corrected the most eloquent preacher in the early church","Acts 18","2-Week"),
    ("Mary of Bethany: The Better Part","Luke 10 and the formation of wisdom as presence rather than productivity","Luke 10","2-Week"),
    ("The Mephibosheth Surprise","2 Samuel 9 and the formation theology of unexpected grace — the man brought to the king's table not for merit but for covenant","2 Samuel 9","2-Week"),
  ]),

  ("The Lament Figures", "Men and women whose formation stories are shaped by loss, grief, and the experience of God's apparent silence", "", "#6a4a6a", [
    ("Job: The Man Who Lost Everything","The formation of a man in the crucible — what he held onto when everything else was taken","Job","40-Day"),
    ("Jeremiah: The Confessions","The prophet's private prayers — six laments that reveal the formation cost of long obedience","Jeremiah 11–20","6-Week"),
    ("Naomi: Call Me Bitter","Ruth 1 and the formation of a woman who told God exactly how she felt — and then walked home","Ruth 1","3-Week"),
    ("The Psalmist of Psalm 88","The only psalm with no resolution — and the formation theology of the lament that does not turn","Psalm 88","2-Week"),
    ("Mary at the Cross","The formation of the mother who watched — and the formation theology of the loss that has no explanation","John 19","Good Friday"),
    ("Thomas in the Week Before Easter","John 20 and the formation of the doubter between the death and the resurrection — eight days of uncertainty","John 20","Holy Week"),
    ("The Disciples on the Road to Emmaus","Luke 24 and the formation of two people walking away from Jerusalem with shattered hopes","Luke 24","3-Week"),
    ("Paul's Thorn","2 Corinthians 12 and the formation of the man who prayed three times and received 'my grace is sufficient'","2 Corinthians 12","3-Week"),
    ("John the Baptist in Prison","Matthew 11 and the formation of the forerunner who sent a message from prison: 'Are you the one?'","Matthew 11","3-Week"),
    ("Hezekiah's Illness","Isaiah 38 and the formation of a man who wept bitterly when told he was dying — and the prayer God heard","Isaiah 38","2-Week"),
  ]),

  ("The Builders", "Men and women whose formation was shaped by the act of building something for God", "", "#3a5a7a", [
    ("Noah: Building What No One Believed In","The formation of a builder who worked for one hundred years on a project the culture mocked","Genesis 6–9","3-Week"),
    ("Bezalel: Filled with the Spirit to Build","The formation of the artisan God specifically gifted for the tabernacle — craft as calling","Exodus 31, 35","2-Week"),
    ("Solomon: Building the Temple He Was Not Allowed to Build Himself","The formation of David's son carrying the father's dream — legacy and succession","1 Kings 5–8","4-Week"),
    ("Ezra: Rebuilding Around the Word Not the Wall","The formation of the scribe who prioritized the book before the building","Ezra","4-Week"),
    ("Nehemiah: The Midnight Ride and the 52-Day Wall","The formation of the builder under opposition — how he prayed, planned, and built simultaneously","Nehemiah","40-Day"),
    ("Paul the Church Planter","The formation of the builder who planted and watered but knew God gives the growth","1 Corinthians 3 · Acts 13–21","40-Day"),
    ("Zerubbabel: The Plumb Line","The governor who laid the cornerstone of the second temple when those who remembered the first one wept","Ezra 3 · Zechariah 4","3-Week"),
    ("Mary and Martha: The Builders of Community","The formation of two women who built around a common table — and received the Lord at it","Luke 10 · John 11–12","3-Week"),
    ("The Two House Builders","Matthew 7's parable and the formation theology of building on what cannot be moved","Matthew 7","3-Week"),
    ("John the Revelator: Building the Vision","The formation of the seer who built the church's hope in the darkest period of persecution","Revelation","4-Week"),
  ]),

  ("The Covenant Keepers", "Men and women who held the covenant when everyone else around them abandoned it", "", "#5a3a7a", [
    ("Abraham's Binding of Isaac","Genesis 22 and the formation of the covenant that holds even when obedience makes no sense","Genesis 22","4-Week"),
    ("Phinehas: The Zeal That Stopped a Plague","Numbers 25 and the formation theology of the person whose intervention changed the outcome","Numbers 25","2-Week"),
    ("Jonathan's Covenant with David","1 Samuel 18–20 and the formation of a friendship built on covenant not convenience","1 Samuel 18–20","3-Week"),
    ("Ruth: I Will Not Leave You","Ruth 1 and the formation of covenant loyalty in the person who had no legal obligation to stay","Ruth 1","3-Week"),
    ("Jeremiah: Preaching a Covenant Nobody Kept","The formation of the prophet who proclaimed the new covenant while the old one collapsed around him","Jeremiah 31","3-Week"),
    ("The Levitical Priests: Faithful in the Detail","The formation of a community whose covenant faithfulness was built into the daily rhythm of sacrifice","Leviticus · Numbers","4-Week"),
    ("Anna: Eighty-Four Years of Waiting on the Covenant","Luke 2 and the formation of the prophet who served in the temple until the covenant arrived in a manger","Luke 2","2-Week"),
    ("Simeon: The One Who Was Told He Would Not Die","Luke 2 and the formation of the old man who held on until he could hold the promise","Luke 2","2-Week"),
    ("Paul: Finishing the Race","2 Timothy 4 and the formation of the man who kept the faith in his last letter","2 Timothy 4","4-Week"),
    ("The Faithful Remnant in Sardis","Revelation 3 and the few names in Sardis who had not soiled their garments — and what God said to them","Revelation 3","3-Week"),
  ]),

  ("The Prodigals", "Men and women who ran from God — and the formation that happened in the running and in the return", "", "#8a5a3a", [
    ("The Prodigal Son: Far Country","Luke 15 and the formation of the son who came to himself in a pigpen — when the bottom is the beginning","Luke 15","40-Day"),
    ("Jonah: Running in the Wrong Direction","The formation of the prophet who sailed away from the word — and the great fish that turned him around","Jonah","21-Day"),
    ("Peter's Denial: The Courtyard","Luke 22 and the formation of the man who said he would never and did — and what Jesus did next","Luke 22 · John 21","4-Week"),
    ("Samson: The Repeated Return","The formation of the man who kept returning to Delilah — and the theology of repeated failure","Judges 13–16","3-Week"),
    ("King Manasseh: The Worst Who Repented","2 Chronicles 33 and the formation theology of the man who was carried in chains to Babylon and humbled himself","2 Chronicles 33","3-Week"),
    ("Mark: The Deserter Who Came Back","The formation of John Mark — the one who abandoned the first missionary journey and was rehabilitated","Acts 13, 15 · 2 Timothy 4","3-Week"),
    ("David After Bathsheba","The formation of the man who fell furthest and repented most deeply — Psalm 51 as a complete theology of return","2 Samuel 11–12 · Psalm 51","4-Week"),
    ("Solomon in His Decline","The formation cost of the man who started with the prayer for wisdom and ended with a thousand wives","1 Kings 11","3-Week"),
    ("The Elder Brother: The Prodigal Who Never Left","Luke 15 and the formation of the son who was home all along and couldn't find his way to the celebration","Luke 15","3-Week"),
    ("Elijah Under the Juniper Tree","1 Kings 19 and the formation of the prophet who ran after his greatest victory — the burnout that followed the fire","1 Kings 19","3-Week"),
  ]),

  ("The Foreign Witnesses", "Men and women outside the covenant community who saw what the insiders missed", "", "#3a7a5a", [
    ("Ruth: The Moabite Who Said Yes","The formation of the outsider who became a grandmother of the Messiah","Ruth","4-Week"),
    ("Rahab: The Canaanite Who Hid the Spies","The formation of the woman from the wrong city who recognized God's people and protected them","Joshua 2","3-Week"),
    ("Naaman's Servant Girl: The Unnamed Witness","The formation of the foreign slave whose words sent the Syrian general to the prophet","2 Kings 5","2-Week"),
    ("Naaman: Dipping Seven Times","The formation of the powerful man who almost missed his healing because the method was too simple","2 Kings 5","3-Week"),
    ("The Queen of Sheba: Wisdom Traveled Far","The formation of the foreign queen who came to verify and stayed to worship","1 Kings 10","2-Week"),
    ("The Magi: Following the Star","The formation of the wise men who traveled from outside the covenant and arrived at the center of it","Matthew 2","Advent"),
    ("The Roman Centurion: Such Faith","The formation of the military man whose faith exceeded everything Jesus had seen in Israel","Matthew 8","2-Week"),
    ("The Syrophoenician Woman: Even the Dogs","The formation of the Gentile woman whose argument convinced Jesus — and the formation theology of persistent outsider faith","Matthew 15","3-Week"),
    ("Cornelius: The First Gentile","Acts 10 and the formation of the Roman who prayed to a God he did not yet fully know — and was heard","Acts 10","3-Week"),
    ("The Ethiopian Eunuch: The Distant Worshipper","Acts 8 and the formation of the man reading Isaiah in a chariot — who received the word and was baptized in a desert","Acts 8","2-Week"),
  ]),

  ("The New Testament Women", "Women of the early church whose formation stories are among the most strategically important in the New Testament", "", "#8a4a5a", [
    ("Mary Magdalene: The One He Came Back For","John 20 and the formation of the woman who was the first witness — and the theology of being chosen for the announcement","John 20","3-Week"),
    ("Priscilla: The Teacher of Apollos","Acts 18 and the formation of the woman who corrected the most eloquent preacher of the early church","Acts 18","2-Week"),
    ("Phoebe: The Deaconess Who Carried Romans","Romans 16 and the formation of the woman trusted to carry Paul's most important letter","Romans 16","2-Week"),
    ("Junia: The Apostle","Romans 16:7 and the formation theology of the woman named among the apostles — and what that means","Romans 16","2-Week"),
    ("Mary of Bethany: The Better Part","Luke 10 and the formation of the woman who chose presence over productivity when the choice was forced","Luke 10","2-Week"),
    ("Martha: Lord If You Had Been Here","John 11 and the formation of the woman whose grief became a theology — 'I am the resurrection and the life'","John 11","3-Week"),
    ("Dorcas / Tabitha: Full of Good Works","Acts 9 and the formation of the woman whose ministry was so essential that the church asked for her back","Acts 9","2-Week"),
    ("Lois and Eunice: The Generational Formation","2 Timothy 1 and the formation of the grandmother and mother whose faith transferred to a generation","2 Timothy 1","3-Week"),
    ("Lydia: The Purple Seller","Acts 16 and the formation of the businesswoman whose home became the first church in Europe","Acts 16","3-Week"),
    ("Mary the Mother in Acts","Acts 1 and 12 and the formation of the woman who was in the upper room for Pentecost and whose house the church fled to","Acts 1, 12","2-Week"),
  ]),

  ("The Flawed Leaders", "Men and women whose leadership was real but marked by significant failures — and what the text says about both", "", "#6a3a4a", [
    ("Moses: He Struck the Rock","The formation cost of the leader who disobeyed once and lost his entrance — the high stakes of public leadership","Numbers 20","3-Week"),
    ("Gideon: The Ephod","The judge who delivered Israel and then created an idolatry with the spoils of the victory","Judges 8","2-Week"),
    ("Eli: The High Priest Who Would Not Restrain His Sons","The formation cost of the spiritual leader who prioritized family peace over household holiness","1 Samuel 2–3","3-Week"),
    ("David: The Census","2 Samuel 24 and the formation of a leader whose pride in what he had built cost seventy thousand lives","2 Samuel 24","2-Week"),
    ("Solomon: A Thousand Wives","The formation cost of the wisest man in history — wisdom without the formation to apply it to his own life","1 Kings 11","3-Week"),
    ("Hezekiah: The Visitors from Babylon","Isaiah 39 and the formation cost of a good leader who showed off everything he had to the wrong audience","2 Kings 20 · Isaiah 39","2-Week"),
    ("Jonah: The Angry Prophet","Jonah 4 and the formation of the leader who was glad when God judged his enemies and furious when God showed mercy","Jonah 4","2-Week"),
    ("Peter: The Vision He Wouldn't Believe","Galatians 2 and the formation cost of Peter's hypocrisy in Antioch — the leader whose behavior denied his theology","Galatians 2","3-Week"),
    ("Barnabas: The Dispute with Paul","Acts 15 and the formation cost of a sharp disagreement between two excellent men over a person who failed once","Acts 15","2-Week"),
    ("The Seven Sons of Sceva","Acts 19 and the formation of leaders who used the right words with no authority behind them","Acts 19","2-Week"),
  ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# COLLECTION 3: 100 BIBLE STORIES / THEMES / PASSAGES — 10 CATEGORIES × 10
# ══════════════════════════════════════════════════════════════════════════════

STORIES = [
  ("Creation and Beginnings", "The foundational narratives of Scripture — what God made, why it was good, and what the first rupture cost", "", "#4a5a8a", [
    ("In the Beginning God","Genesis 1 and the formation of a congregation's theology of creation — not science vs. faith but who and why","Genesis 1","40-Day"),
    ("And It Was Good","The formation of a theology of goodness — the world as gift before it was broken","Genesis 1–2","3-Week"),
    ("Image and Likeness","The formation theology of imago Dei — what carrying God's image means for every Monday morning","Genesis 1:26–27","4-Week"),
    ("The Seventh Day","Sabbath in creation — the formation of a congregation that rests before it works","Genesis 2:1–3","4-Week"),
    ("The Garden","Eden as a formation text — what was there before the fall and what the new creation restores","Genesis 2","3-Week"),
    ("The Fall","Genesis 3 and the formation of a complete theology of sin — not as rule-breaking but as relationship-fracturing","Genesis 3","4-Week"),
    ("The First Gospel","Genesis 3:15 and the formation of a congregation that reads all of Scripture as the story of the seed","Genesis 3:15","3-Week"),
    ("The Mark of Cain","Genesis 4 and the formation of a theology of protection — God's mercy to the one who least deserves it","Genesis 4","3-Week"),
    ("The Flood as Re-Creation","Genesis 6–9 and the formation of a theology of judgment that is inseparable from preservation","Genesis 6–9","4-Week"),
    ("The Tower of Babel","Genesis 11 and the formation of a theology of human ambition — and the God who confuses what he could simply destroy","Genesis 11","3-Week"),
  ]),

  ("Covenant Moments", "The specific moments in Scripture when God drew a line with a person, a people, or the whole world", "", "#3a6a4a", [
    ("The Rainbow Covenant","Genesis 9 and the formation of a theology of covenant faithfulness — God's commitment made before any human response","Genesis 9","3-Week"),
    ("The Abrahamic Covenant","Genesis 15 and the covenant God made alone — passing between the pieces when Abraham was asleep","Genesis 15","4-Week"),
    ("The Covenant of Circumcision","Genesis 17 and the formation of a theology of the body as the site of covenant — what gets marked and why","Genesis 17","3-Week"),
    ("The Mosaic Covenant at Sinai","Exodus 19–20 and the formation of the covenant community — the people who said 'we will do' before they heard the rest","Exodus 19–20","4-Week"),
    ("The Renewed Covenant After the Golden Calf","Exodus 34 and the formation of a theology of renewed covenant — when Israel failed at Sinai and God started over","Exodus 34","3-Week"),
    ("The Davidic Covenant","2 Samuel 7 and the formation of a theology of the eternal house — the promise that runs to Jesus","2 Samuel 7","4-Week"),
    ("The New Covenant","Jeremiah 31:31-34 and the formation of a congregation living in the already-not-yet of the new covenant","Jeremiah 31","40-Day"),
    ("The Last Supper as New Covenant","Luke 22 and the formation of the covenant ceremony at the last meal — this cup is the new covenant in my blood","Luke 22","Holy Week"),
    ("The Cross as Covenant","Hebrews 9 and the formation of a theology of the blood of the covenant — what the cross ratified","Hebrews 9","4-Week"),
    ("The Everlasting Covenant","Revelation 21–22 and the formation of a theology of covenant consummation — God with his people forever","Revelation 21–22","4-Week"),
  ]),

  ("Wilderness and Wandering", "The formation theology of the in-between — the time between promise and possession", "", "#7a6a3a", [
    ("Manna Every Morning","Exodus 16 and the formation of a congregation that lives on daily provision rather than stored security","Exodus 16","4-Week"),
    ("Water from the Rock","Exodus 17 and the formation theology of provision from the most unlikely source","Exodus 17","3-Week"),
    ("The Cloud and the Fire","The pillar that led Israel — and the formation theology of following presence, not a plan","Exodus 13 · Numbers 9","3-Week"),
    ("The Spies' Report","Numbers 13–14 and the formation of a congregation that is learning to believe the minority report","Numbers 13–14","4-Week"),
    ("The Bronze Serpent","Numbers 21 and the formation theology of looking up — the text Jesus applied to himself in John 3","Numbers 21 · John 3","3-Week"),
    ("Forty Years of Formation","Deuteronomy 8 and the formation theology of the wasted years that were not wasted","Deuteronomy 8","4-Week"),
    ("Jesus in the Wilderness","Matthew 4 and the formation of a Christology built on the second Israel passing the test the first one failed","Matthew 4","Lent"),
    ("The Prodigal's Far Country","Luke 15 and the formation of a theology of the wilderness season — when you come to yourself","Luke 15","3-Week"),
    ("Paul in Arabia","Galatians 1 and the formation of the apostle in the hidden years before the ministry began","Galatians 1","3-Week"),
    ("The Seven Churches in the Wilderness","Revelation 2–3 as the formation letters to congregations in their own wilderness seasons","Revelation 2–3","7-Week"),
  ]),

  ("Exile and Return", "The formation theology of displacement — what happens to faith when everything familiar is taken", "", "#6a4a8a", [
    ("By the Waters of Babylon","Psalm 137 and the formation theology of lament in a foreign land — how do you sing the Lord's song here","Psalm 137","3-Week"),
    ("Seek the Peace of the City","Jeremiah 29 and the formation of a congregation that flourishes in the place it did not choose","Jeremiah 29","40-Day"),
    ("Daniel's Three-Times-a-Day Prayer","Daniel 6 and the formation of a prayer practice so established that no prohibition can interrupt it","Daniel 6","4-Week"),
    ("Return to Me","Malachi 3 and the formation of a congregation that is aware it has drifted and hears the call to return","Malachi 3","4-Week"),
    ("When the Lord Restored","Psalm 126 and the formation of a theology of restoration — dreaming dreams, laughing again","Psalm 126","3-Week"),
    ("The Valley of Dry Bones","Ezekiel 37 and the formation theology of the community that looks dead — and what God asks the prophet to do","Ezekiel 37","4-Week"),
    ("The Highway Through the Desert","Isaiah 40 and the formation theology of return — the voice crying in the wilderness","Isaiah 40","Advent"),
    ("Restore Our Fortunes","The return under Zerubbabel and Ezra — the formation of the community that goes home to rebuild","Ezra 1–6","4-Week"),
    ("The First and the Second Return","Zerubbabel's group and Ezra's group — the formation of two distinct waves of rebuilding","Ezra 1–6 · 7–10","4-Week"),
    ("Nehemiah's Return","The third wave of return — the man whose prayer became a building project became a community renewal","Nehemiah","40-Day"),
  ]),

  ("Birth, Death, and Resurrection", "The hinge moments of Scripture — arrival, departure, and the disruption of both", "", "#8a3a4a", [
    ("The Birth Announcements","Gabriel to Mary, angels to shepherds, and the star to the Magi — the formation theology of annunciation","Luke 1–2 · Matthew 2","Advent"),
    ("Simeon's Nunc Dimittis","Luke 2 and the formation of the old man who could die now — what it means to see the salvation of God","Luke 2","3-Week"),
    ("Lazarus: Four Days Dead","John 11 and the formation theology of delayed response — why Jesus waited and what it produced","John 11","4-Week"),
    ("The Widow's Son at Nain","Luke 7 and the formation of a theology of interruption — Jesus interrupted a funeral and changed the outcome","Luke 7","2-Week"),
    ("Jairus's Daughter: She Is Not Dead","Mark 5 and the formation of a theology of two levels of death — and which one Jesus addresses first","Mark 5","3-Week"),
    ("The Transfiguration","Matthew 17 and the formation of a theology of the unveiled Christ — what Moses and Elijah confirm","Matthew 17","3-Week"),
    ("The Passion Week","Palm Sunday to Easter — the formation arc of the week that changed everything","Matthew 21–28","Holy Week"),
    ("The Empty Tomb","John 20 and the formation of a theology of absence that is also presence — what the empty tomb means before the appearances","John 20","Easter"),
    ("Ascension and Sending","Acts 1 and the formation of a congregation shaped by the departure of Jesus — and the promise of his return","Acts 1","3-Week"),
    ("The Resurrection Body","1 Corinthians 15 and the formation of a congregation whose hope is bodily and specific","1 Corinthians 15","4-Week"),
  ]),

  ("Prayer and Divine Encounter", "The moments in Scripture when a human being came close to God — and what the encounter produced", "", "#3a5a7a", [
    ("Jacob Wrestles at Jabbok","Genesis 32 and the formation of a theology of wrestling prayer — the limp that proves the encounter was real","Genesis 32","4-Week"),
    ("The Burning Bush","Exodus 3 and the formation theology of the holy ground that is everywhere once you have eyes to see it","Exodus 3","3-Week"),
    ("Moses Face to Face","Exodus 33 and the most intimate portrait of prayer in the Torah — what it means to know God as a friend","Exodus 33","4-Week"),
    ("Hannah's Silent Prayer","1 Samuel 1 and the formation of the prayer so intense the priest thought she was drunk","1 Samuel 1","3-Week"),
    ("Elijah on the Mountain","1 Kings 19 and the formation theology of the still small voice — what God says to the exhausted prophet","1 Kings 19","4-Week"),
    ("Isaiah's Throne Room","Isaiah 6 and the formation of the prophet who saw God — and the formation cost of what he was sent to say","Isaiah 6","4-Week"),
    ("Daniel's Three Weeks of Fasting","Daniel 10 and the formation theology of persistent intercession — the prayer that was heard on day one","Daniel 10","3-Week"),
    ("The Lord's Prayer as Curriculum","Matthew 6 and the formation of a congregation that prays what Jesus prayed — not how the hypocrites pray","Matthew 6","7-Week"),
    ("Gethsemane","Matthew 26 and the formation of a theology of 'not my will but yours' — the hardest prayer in Scripture","Matthew 26","Holy Week"),
    ("Stephen's Vision While Being Stoned","Acts 7 and the formation of a man who saw the Son of Man standing at the right hand of God while dying","Acts 7","3-Week"),
  ]),

  ("Miracles and Signs", "The moments of intervention — and the formation theology of what they were designed to produce", "", "#4a7a5a", [
    ("The Parting of the Red Sea","Exodus 14 and the formation of a theology of divine intervention — the army behind, the water ahead, and the command: be still","Exodus 14","4-Week"),
    ("The Sun Stands Still","Joshua 10 and the formation theology of the request that should not be made — and the God who granted it","Joshua 10","2-Week"),
    ("The Widow's Oil That Multiplied","2 Kings 4 and the formation theology of the small thing that became enough — Elisha and the vessels","2 Kings 4","2-Week"),
    ("Isaiah's Shadow Sign","Isaiah 38 and the formation of a theology of signs — what God does when asked to confirm a promise","Isaiah 38","2-Week"),
    ("Jesus' First Miracle: The Best Wine Last","John 2 and the formation of a theology of glory revealed in the ordinary — a wedding, six stone jars, a need","John 2","3-Week"),
    ("The Feeding of Five Thousand","John 6 and the formation theology of the Eucharistic text — taking, blessing, breaking, giving","John 6","4-Week"),
    ("Jesus Walking on Water","Matthew 14 and the formation of a theology of presence in the storm — and the invitation to come","Matthew 14","3-Week"),
    ("The Healing of the Ten Lepers","Luke 17 and the formation of a theology of gratitude — why one returned and nine did not","Luke 17","2-Week"),
    ("Pentecost as Sign","Acts 2 and the formation theology of the first great sign of the new age — tongues, fire, and the filling","Acts 2","4-Week"),
    ("Paul's Thorn as Anti-Sign","2 Corinthians 12 and the formation theology of the miracle that did not come — and what God gave instead","2 Corinthians 12","3-Week"),
  ]),

  ("Kingdom Parables", "The most formation-dense teachings of Jesus — stories that carry the logic of the kingdom inside them", "", "#6a5a3a", [
    ("The Mustard Seed","Matthew 13 and the formation theology of the small thing that becomes something nobody could have predicted","Matthew 13","3-Week"),
    ("The Hidden Treasure and the Pearl","Matthew 13 and the formation of a theology of singular pursuit — when you find the thing you sell everything else","Matthew 13","2-Week"),
    ("The Sower and the Soils","Matthew 13 and the formation theology of receptivity — which soil the word finds in you","Matthew 13","4-Week"),
    ("The Wheat and the Tares","Matthew 13 and the formation of a theology of patience — the kingdom that does not sort itself out until the harvest","Matthew 13","3-Week"),
    ("The Good Samaritan","Luke 10 and the formation of the question that changes everything: who is my neighbor","Luke 10","40-Day"),
    ("The Prodigal Son in Full","Luke 15 — the father, the younger son, and the elder brother as a complete formation theology","Luke 15","40-Day"),
    ("The Workers in the Vineyard","Matthew 20 and the formation of a theology of grace that is not fair — and why that is good news","Matthew 20","3-Week"),
    ("The Ten Virgins","Matthew 25 and the formation of the readiness that cannot be borrowed — what the oil actually is","Matthew 25","4-Week"),
    ("The Talents","Matthew 25 and the formation of a theology of stewardship — what we do with what we have been given while we wait","Matthew 25","4-Week"),
    ("The Rich Man and Lazarus","Luke 16 and the formation of a theology of reversal — the chasm that is fixed and the opportunity that passes","Luke 16","3-Week"),
  ]),

  ("Crucifixion Theology", "The center of Scripture — the cross and what it accomplished, reveals, and demands of those who follow", "", "#8a3a3a", [
    ("The Seven Last Words","The formation of a complete theology from the seven sayings of Jesus on the cross","Luke 23 · John 19","Holy Week"),
    ("My God My God Why","Mark 15 and the formation of a theology of divine abandonment — and why Psalm 22 ends the way it does","Mark 15 · Psalm 22","Holy Week"),
    ("It Is Finished","John 19:30 and the formation theology of tetelestai — the accounting term that means the debt is paid","John 19:30","Holy Week"),
    ("The Curtain Was Torn","Matthew 27 and the formation theology of access — what the tearing of the veil from top to bottom means","Matthew 27","Holy Week"),
    ("Crucified with Christ","Galatians 2:20 and the formation of union with Christ — not just forgiveness but co-crucifixion","Galatians 2","4-Week"),
    ("The Word of the Cross","1 Corinthians 1 and the formation theology of the offensive gospel — why the cross is foolishness and why that is its power","1 Corinthians 1","4-Week"),
    ("Christ Crucified Among You","1 Corinthians 2:2 and the formation of a congregation that is not ashamed of the centerpiece","1 Corinthians 2","3-Week"),
    ("He Himself Bore Our Sins","1 Peter 2:24 and the formation of a substitutionary theology that is also a formation text — by his wounds you have been healed","1 Peter 2","4-Week"),
    ("The Lamb Who Was Slain","Revelation 5 and the formation of a throne-room theology where the power looks like a slaughtered lamb","Revelation 5","4-Week"),
    ("Christ Our Passover","1 Corinthians 5:7 and the formation of a congregation that reads the Exodus through the cross","1 Corinthians 5 · Exodus 12","3-Week"),
  ]),

  ("New Creation", "The formation theology of what is coming — and how that changes everything now", "", "#3a6a7a", [
    ("Already and Not Yet","The formation theology of the kingdom that has come and is still coming — how to live in the overlap","Various NT Texts","40-Day"),
    ("A New Heaven and a New Earth","Revelation 21 and the formation of a complete theology of what the end actually is — embodied, restored, renewed","Revelation 21","4-Week"),
    ("The New Jerusalem","Revelation 21–22 and the formation of a congregation shaped by its destination — the city that descends","Revelation 21–22","4-Week"),
    ("No More Sea","Revelation 21:1 and the formation theology of what is absent in the new creation — and why it matters","Revelation 21","3-Week"),
    ("God Will Wipe Every Tear","Revelation 21:4 and the formation of a congregation that lives now in light of what will be done then","Revelation 21","3-Week"),
    ("The River and the Tree","Revelation 22 and Genesis 2 together — the formation arc from the first garden to the last city","Genesis 2 · Revelation 22","4-Week"),
    ("Behold I Am Making All Things New","Revelation 21:5 and the formation of a theology of restoration that is also a theology of present-day renewal","Revelation 21","40-Day"),
    ("The Resurrection as New Creation","1 Corinthians 15 and the formation of a congregation that understands the resurrection as the first installment of the new creation","1 Corinthians 15","4-Week"),
    ("If Anyone Is in Christ","2 Corinthians 5:17 and the formation of a congregation that understands new creation as present experience, not future event","2 Corinthians 5","3-Week"),
    ("The Creation Waits","Romans 8:19-25 and the formation of a theology of groaning — the whole creation in labor for what is coming","Romans 8","4-Week"),
  ]),
]

import html as hlib
def e(s): return hlib.escape(str(s))

def s_card(n, title, sub, ref, badge=None, is_hero=False, color="#4a5a8a"):
    badge_html = f'<span class="s-badge" style="border-color:{color};color:{color};">{e(badge)}</span>' if badge else ""
    return f"""<div class="s-card">
  <span class="s-num">{n:02d}</span>
  <p class="s-title">{e(title)}</p>
  <p class="s-sub">{e(sub)}</p>
  <p class="s-ref">{e(ref)}</p>
  {badge_html}
</div>"""

def cat_sec(num, name, desc, books, color, entries):
    cards = "".join(s_card(i+1, t, s, r, b, i==0, color) for i,(t,s,r,b) in enumerate(entries))
    bk = f'<p class="cat-books">{e(books)}</p>' if books else ""
    return f"""<div class="cat-block">
  <div class="cat-hdr" style="border-color:{color};">
    <span class="cat-num" style="color:{color};">{num:02d}</span>
    <div>
      <h3 class="cat-name" style="color:{color};">{e(name)}</h3>
      <p class="cat-desc">{e(desc)}</p>
      {bk}
    </div>
  </div>
  <div class="series-grid">{cards}</div>
</div>"""

def coll_hdr(color, kk, h2_html, sub, count):
    return f"""<div class="hdiv"></div>
<section class="coll-header" style="border-color:{color};">
  <p class="coll-kk" style="color:{color};">{e(kk)}</p>
  <h2 class="coll-h2">{h2_html}</h2>
  <p class="coll-sub">{e(sub)}</p>
  <span class="coll-count" style="border-color:{color};color:{color};">{e(count)}</span>
</section>"""

# Build sections
bible_sections = "".join(
    cat_sec(i+1, name, desc, books, color, entries)
    for i,(name,desc,books,color,entries) in enumerate(BIBLE_CAMPAIGNS)
)
char_sections = "".join(
    cat_sec(i+1, name, desc, books, color, entries)
    for i,(name,desc,books,color,entries) in enumerate(CHAR_SERIES)
)
story_sections = "".join(
    cat_sec(i+1, name, desc, books, color, entries)
    for i,(name,desc,books,color,entries) in enumerate(STORIES)
)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lifetogether Bible Campaign Expansion · 550 New Series</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;900&family=Georgia&display=swap" rel="stylesheet">
<style>{STYLES}</style>
</head>
<body>
<div class="page">

<!-- COVER -->
<section class="cover">
  <div class="cover-glow"></div>
  <div class="cover-top">
    <span class="cover-logo">Lifetogether</span>
    <span class="cover-tag">Campaign Library Expansion · Vol. II</span>
  </div>
  <div class="cover-body">
    <p class="cover-ey">Bible Campaigns · Biblical Characters · Bible Stories &amp; Themes</p>
    <h1 class="cover-h1">550 New<br>Series.<br><em>One Library.</em></h1>
    <div class="cover-rule"><div class="cover-rule-dot"></div><div class="cover-rule-line"></div></div>
    <p class="cover-sub">250 fresh-angle Bible campaigns across the full canon, 200 biblical character series across 20 categories, and 100 series built on the greatest Bible stories, themes, and passages — every one designed for the congregation that has already done the obvious series and is ready for the formation underneath it.</p>
    <div class="cover-stats">
      <div class="cstat"><span class="cstat-n">550</span><span class="cstat-l">New Series Titles</span></div>
      <div class="cstat"><span class="cstat-n">250</span><span class="cstat-l">Bible Campaigns</span></div>
      <div class="cstat"><span class="cstat-n">200</span><span class="cstat-l">Character Series</span></div>
      <div class="cstat"><span class="cstat-n">100</span><span class="cstat-l">Stories &amp; Themes</span></div>
      <div class="cstat"><span class="cstat-n">30</span><span class="cstat-l">Categories</span></div>
      <div class="cstat"><span class="cstat-n">66</span><span class="cstat-l">Books Covered</span></div>
    </div>
  </div>
</section>

<!-- COLLECTION 1: BIBLE CAMPAIGNS -->
{coll_hdr("var(--c1)","Collection One · 250 Series · 10 Categories","<em>Fresh Angles</em> on the<br>Bible Campaigns","250 alternative campaign approaches to the full canon — same texts, entirely different formation angles. For the congregation that has done the obvious series and is ready for the formation underneath the surface.","250 Series · 10 Categories · 25 per Category")}
{bible_sections}

<!-- COLLECTION 2: BIBLICAL CHARACTER SERIES -->
{coll_hdr("var(--c2)","Collection Two · 200 Series · 20 Categories","The <em>Biblical Characters</em><br>Library","200 character-based series across 20 categories — from the patriarchs to the flawed leaders, from the matriarchs to the women who carried the early church. Every series title designed to do the formation work the character's story is equipped to do.","200 Series · 20 Categories · 10 per Category")}
{char_sections}

<!-- COLLECTION 3: BIBLE STORIES / THEMES / PASSAGES -->
{coll_hdr("var(--c3)","Collection Three · 100 Series · 10 Categories","The Greatest <em>Bible Stories,</em><br>Themes &amp; Passages","100 series built on the most formation-dense texts in Scripture — organized not by book but by the formation question each text is equipped to answer. Creation. Covenant. Exile. Resurrection. Kingdom. Cross. New Creation.","100 Series · 10 Categories · 10 per Category")}
{story_sections}

<!-- BACK -->
<div class="hdiv"></div>
<section class="back">
  <p class="back-q">"The congregation that runs the same series every three years is not growing. The congregation that discovers the formation wealth inside the texts they have never preached from is the congregation that is always becoming something it was not last year."</p>
  <p class="back-a">Brett Eastman · Founder, Lifetogether</p>
  <p class="back-c"><a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &nbsp;·&nbsp; <a href="https://lifetogether.com">lifetogether.com</a> &nbsp;·&nbsp; 25 Years · 500+ Church Relationships · 50M+ Campaigns</p>
  <div class="lm">Lifetogether</div>
</section>

</div>
</body>
</html>"""

with open('/mnt/user-data/outputs/lifetogether-bible-campaigns-expanded.html','w') as f:
    f.write(HTML)

print(f"Done — {len(HTML):,} chars, {HTML.count('<div class=\"s-card\">')} series cards")
