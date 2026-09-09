
CSS = """
:root{
  --navy:#02040a;--gold:#c9a84c;--gold-lt:#e2c97e;--gold-dk:#8a6e30;
  --cream:#f8f5ef;--tl:#d4c9b8;--tm:#8a9ab5;--rule:rgba(201,168,76,0.10);
  --ink:#0e1218;--paper:#f3efe7;--paper-alt:#ebe6dd;
  --gen:#4a7a50;   /* generosity green */
  --cap:#4a5a8a;   /* capital campaign blue */
  --east:#8a4a30;  /* easter copper */
  --bap:#5a4a8a;   /* baptism purple */
  --lead:#6a7a3a;  /* leadership / general olive */
  --miss:#3a6a7a;  /* mission teal */
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Lato',sans-serif;background:#d8d4cc;color:var(--ink);}
.page{max-width:1180px;margin:0 auto;background:var(--cream);box-shadow:0 4px 80px rgba(0,0,0,.22);}

/* ── COVER ── */
.cover{background:var(--navy);min-height:96vh;display:flex;flex-direction:column;
  justify-content:flex-end;padding:0;position:relative;overflow:hidden;}
.cover-glow{position:absolute;inset:0;background:
  radial-gradient(ellipse at 18% 70%,rgba(201,168,76,.07),transparent 48%),
  radial-gradient(ellipse at 82% 22%,rgba(74,122,80,.05),transparent 48%),
  radial-gradient(ellipse at 50% 50%,rgba(74,90,138,.04),transparent 55%),
  linear-gradient(180deg,#010306,#020408 60%,#030810);}
.cover-top{padding:52px 80px 0;position:relative;z-index:2;
  display:flex;justify-content:space-between;align-items:flex-start;}
.cover-logo{font-family:'Playfair Display',serif;font-size:15px;font-style:italic;
  color:rgba(255,255,255,.38);letter-spacing:2px;}
.cover-tag{font-size:7.5px;letter-spacing:4px;text-transform:uppercase;font-weight:700;
  color:var(--gold-dk);border:1px solid rgba(201,168,76,.2);padding:5px 12px;}
.cover-body{padding:68px 80px 84px;position:relative;z-index:2;}
.cover-ey{font-size:8.5px;letter-spacing:5px;text-transform:uppercase;font-weight:700;
  color:rgba(74,122,80,.9);display:flex;align-items:center;gap:14px;margin-bottom:22px;}
.cover-ey::before{content:'';width:30px;height:1px;background:rgba(74,122,80,.65);}
.cover-h1{font-family:'Playfair Display',serif;
  font-size:clamp(44px,6.5vw,100px);font-weight:400;line-height:.88;
  color:#fff;letter-spacing:-2px;margin-bottom:22px;}
.cover-h1 em{font-style:italic;color:var(--gold);}
.cover-rule{display:flex;align-items:center;gap:14px;margin:26px 0;}
.cover-rule-line{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.cover-rule-dot{width:6px;height:6px;background:var(--gold);transform:rotate(45deg);flex-shrink:0;}
.cover-sub{font-family:'Playfair Display',serif;font-size:clamp(15px,2vw,22px);
  font-weight:300;font-style:italic;color:var(--tl);max-width:720px;line-height:1.62;margin-bottom:48px;}
.cover-stats{display:grid;grid-template-columns:repeat(6,1fr);
  max-width:900px;border:1px solid rgba(201,168,76,.2);}
.cstat{padding:15px 16px;border-right:1px solid rgba(201,168,76,.14);text-align:center;}
.cstat:last-child{border-right:none;}
.cstat-n{font-family:'Playfair Display',serif;font-size:24px;color:var(--gold);display:block;line-height:1;}
.cstat-l{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;
  color:rgba(255,255,255,.22);font-weight:700;display:block;margin-top:3px;}

/* ── PART HEADERS ── */
.part{padding:52px 80px 24px;border-top:5px solid;}
.part-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;
  display:flex;align-items:center;gap:12px;margin-bottom:16px;}
.part-kk::before{content:'';width:20px;height:1px;background:currentColor;}
.part-h2{font-family:'Playfair Display',serif;font-size:clamp(28px,4vw,56px);
  font-weight:400;line-height:.9;margin-bottom:12px;}
.part-h2 em{font-style:italic;}
.part-sub{font-family:'Georgia',serif;font-size:14.5px;color:#555;
  line-height:1.78;max-width:820px;margin-bottom:8px;}
.part-sub p{margin-bottom:12px;}
.part-sub strong{color:var(--ink);}

/* ── TOP 10 RANKED LISTS ── */
.top10-wrap{padding:0 80px 52px;}
.top10-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;}
.rank-item{display:grid;grid-template-columns:44px 1fr;gap:0;border:1px solid;}
.rank-item.rank1{grid-column:1/-1;} /* rank 1 spans full width */
.rank-num{display:flex;align-items:center;justify-content:center;
  font-family:'Playfair Display',serif;font-weight:400;flex-shrink:0;}
.rank-body{padding:14px 18px;}
.rank-title{font-family:'Playfair Display',serif;font-size:15px;font-style:italic;
  color:var(--ink);margin-bottom:4px;}
.rank-title strong{font-style:normal;color:inherit;}
.rank-desc{font-family:'Georgia',serif;font-size:12.5px;color:#555;line-height:1.6;margin-bottom:6px;}
.rank-action{font-size:8px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;
  display:flex;align-items:center;gap:5px;padding-top:6px;border-top:1px solid rgba(0,0,0,.06);}
.rank-action::before{content:'→';}
.rank-roi{font-size:7.5px;padding:2px 7px;border:1px solid;font-weight:700;
  letter-spacing:1px;text-transform:uppercase;margin-left:auto;white-space:nowrap;}
.rank-item.rank1 .rank-num{font-size:44px;}
.rank-item:not(.rank1) .rank-num{font-size:26px;}
/* week tag */
.week-tag{font-size:7px;padding:2px 6px;border:1px solid rgba(0,0,0,.12);
  color:#888;letter-spacing:1px;font-weight:700;text-transform:uppercase;margin-right:5px;}

/* ── COUNTDOWN TIMELINE ── */
.countdown{margin:0 80px 52px;border:1px solid rgba(0,0,0,.08);overflow:hidden;}
.cd-header{padding:14px 20px;display:flex;align-items:center;gap:10px;}
.cd-header-title{font-family:'Playfair Display',serif;font-size:15px;font-style:italic;}
.cd-weeks{display:grid;grid-template-columns:repeat(6,1fr) 1fr;gap:0;}
.cd-week{padding:14px 14px 16px;border-right:1px solid rgba(0,0,0,.06);border-top:1px solid rgba(0,0,0,.06);}
.cd-week:last-child{border-right:none;}
.cd-week-label{font-size:7.5px;letter-spacing:2px;text-transform:uppercase;font-weight:700;
  color:#aaa;margin-bottom:8px;display:block;}
.cd-week.sunday .cd-week-label{font-weight:900;}
.cd-task{font-size:10.5px;font-family:'Georgia',serif;color:#444;
  padding:4px 0;border-bottom:1px solid rgba(0,0,0,.05);line-height:1.35;}
.cd-task:last-child{border-bottom:none;}
.cd-task.priority{color:var(--ink);font-weight:700;}

/* ── THE 25 SUNDAYS DIRECTORY ── */
.dir{padding:0 80px 52px;}
.dir-intro{margin-bottom:28px;}
.dir-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;}
.dir-card{padding:14px 16px;border:1px solid rgba(0,0,0,.07);background:rgba(255,255,255,.5);}
.dir-card.mega{border-width:2px;}
.dir-rank{font-family:'Playfair Display',serif;font-size:32px;
  color:rgba(0,0,0,.08);display:block;line-height:1;float:right;margin-left:8px;}
.dir-card.mega .dir-rank{color:rgba(201,168,76,.25);font-size:44px;}
.dir-type{font-size:7px;padding:2px 6px;border:1px solid;
  font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
  display:inline-block;margin-bottom:7px;}
.dir-title{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;
  color:var(--ink);margin-bottom:4px;}
.dir-card.mega .dir-title{font-size:17px;}
.dir-why{font-family:'Georgia',serif;font-size:10.5px;color:#666;line-height:1.45;margin-bottom:5px;}
.dir-metrics{display:flex;gap:5px;flex-wrap:wrap;margin-top:4px;}
.dir-metric{font-size:7px;padding:1px 5px;border:1px solid rgba(0,0,0,.1);
  color:#888;letter-spacing:.7px;text-transform:uppercase;font-weight:700;}

/* ── PRINCIPLE BOXES ── */
.principle-wrap{padding:0 80px 52px;}
.principle-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;}
.principle{padding:20px 22px;border-left:5px solid;}
.pr-n{font-family:'Playfair Display',serif;font-size:40px;
  color:rgba(0,0,0,.06);display:block;line-height:1;float:right;margin-left:10px;}
.pr-title{font-family:'Playfair Display',serif;font-size:16px;font-style:italic;
  color:var(--ink);margin-bottom:6px;}
.pr-body{font-family:'Georgia',serif;font-size:12px;color:#555;line-height:1.6;}

/* ── PULL QUOTES ── */
.pull{margin:0 80px 32px;padding:20px 26px;border-left:4px solid var(--gold);
  background:rgba(201,168,76,.04);}
.pull p{font-family:'Playfair Display',serif;font-size:clamp(15px,1.8vw,20px);
  font-style:italic;color:var(--ink);line-height:1.55;}
.pull span{font-size:8.5px;letter-spacing:2px;text-transform:uppercase;
  font-weight:700;color:var(--gold-dk);display:block;margin-top:8px;}

/* ── SECTION INTRO ── */
.sect-intro{padding:36px 80px 16px;}
.si-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;
  display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.si-kk::before{content:'';width:16px;height:1px;background:currentColor;}
.si-h2{font-family:'Playfair Display',serif;font-size:clamp(22px,3vw,40px);
  font-weight:400;margin-bottom:8px;}
.si-h2 em{font-style:italic;}
.si-sub{font-family:'Georgia',serif;font-size:14px;color:#555;line-height:1.75;max-width:800px;}

/* ── SPECIAL CALL-OUT ── */
.callout{margin:0 80px 28px;padding:18px 22px;border:1px solid;display:grid;
  grid-template-columns:44px 1fr;gap:0;}
.callout-icon{display:flex;align-items:flex-start;justify-content:center;
  padding-top:2px;font-size:22px;}
.callout-body{padding:0 0 0 4px;}
.callout-label{font-size:7.5px;letter-spacing:3px;text-transform:uppercase;
  font-weight:700;display:block;margin-bottom:4px;}
.callout-text{font-family:'Georgia',serif;font-size:13px;color:var(--ink);line-height:1.6;}

.hdiv{height:3px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.22),transparent);}
.sdiv{height:1px;background:var(--rule);margin:0 80px;}

/* BACK */
.back{background:#010406;padding:56px 80px;text-align:center;}
.bq{font-family:'Playfair Display',serif;font-size:clamp(14px,2vw,20px);
  font-style:italic;color:var(--cream);max-width:780px;margin:0 auto 20px;line-height:1.55;}
.ba{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.bc{margin-top:14px;font-size:12px;color:var(--tm);}
.bc a{color:var(--gold-lt);text-decoration:none;}
.lm{font-family:'Playfair Display',serif;font-size:30px;color:#fff;font-style:italic;margin-top:26px;}

@media(max-width:960px){
  .cover-top,.cover-body,.part,.top10-wrap,.dir,.principle-wrap,.pull,.callout,.countdown,.sect-intro,.back{
    padding-left:28px;padding-right:28px;}
  .countdown{margin-left:28px;margin-right:28px;}
  .pull{margin-left:28px;margin-right:28px;}
  .callout{margin-left:28px;margin-right:28px;}
  .sdiv{margin:0 28px;}
  .top10-grid,.dir-grid,.principle-grid{grid-template-columns:1fr;}
  .rank-item.rank1{grid-column:auto;}
  .cd-weeks{grid-template-columns:repeat(3,1fr);}
  .cover-stats{grid-template-columns:repeat(3,1fr);}
  .cd-week:nth-child(3){border-right:none;}
}
@media(max-width:600px){
  .top10-grid,.dir-grid,.principle-grid{grid-template-columns:1fr;}
  .cover-stats{grid-template-columns:repeat(2,1fr);}
}
"""

def ri(rank, title, desc, action, roi_label, color, roi_color, week="", is_top=False):
    """Render a ranked item card."""
    cls = "rank-item rank1" if is_top else "rank-item"
    num_size = "44px" if is_top else "24px"
    week_html = f'<span class="week-tag">{week}</span>' if week else ""
    return f'''<div class="{cls}" style="border-color:rgba(0,0,0,.07);background:{'rgba(201,168,76,.04)' if is_top else 'rgba(255,255,255,.5)'};">
  <div class="rank-num" style="background:{'rgba(201,168,76,.06)' if is_top else 'rgba(0,0,0,.03)'};font-size:{num_size};color:{color};">{rank}</div>
  <div class="rank-body">
    <h3 class="rank-title">{title}</h3>
    <p class="rank-desc">{desc}</p>
    <div class="rank-action" style="color:{color};">{week_html}{action}<span class="rank-roi" style="border-color:{roi_color};color:{roi_color};">{roi_label}</span></div>
  </div>
</div>'''

def cd_week(label, tasks, is_sunday=False, color="#c9a84c"):
    """Render a countdown week column."""
    cls = "cd-week sunday" if is_sunday else "cd-week"
    bg = f"rgba(201,168,76,.06)" if is_sunday else "rgba(255,255,255,.4)"
    tasks_html = "".join(f'<p class="cd-task{" priority" if t.startswith("★") else ""}">{t.lstrip("★").strip()}</p>' for t in tasks)
    return f'''<div class="{cls}" style="background:{bg};{'border-top:3px solid '+color+';' if is_sunday else ''}">
  <span class="cd-week-label">{label}</span>
  {tasks_html}
</div>'''

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

<!-- ══ COVER ══ -->
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
    <p class="cover-sub">The proven 4–6 week preparation system for the 25 most significant Sundays and weekend initiatives a congregation will ever experience — ranked, sequenced, and built around the single conviction that the Sunday that changes the most lives is the Sunday prepared for most intentionally.</p>
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

<!-- ══ THE MASTER PRINCIPLE ══ -->
<div class="pull" style="margin-top:48px;">
  <p>"The Sunday that changes the most lives is never the one that was prepared for on Thursday. It is the one the pastor began preparing for six weeks before anyone else knew it was coming — in prayer, in communication, in volunteer mobilization, in small group connection, in follow-up infrastructure. The sermon is the visible tip of an invisible iceberg. The iceberg is preparation."</p>
  <span>Brett Eastman · Founder, Lifetogether · 25 Years · 500+ Church Relationships</span>
</div>
<div class="hdiv"></div>

<!-- ══ THE 25 FLAGSHIP SUNDAYS DIRECTORY ══ -->
<section class="sect-intro">
  <p class="si-kk" style="color:var(--gold-dk);">The Complete Directory</p>
  <h2 class="si-h2">The <em>Top 25 Flagship Sundays</em> — Ranked by Formation Impact</h2>
  <p class="si-sub">Ranked by their combined potential for congregational mobilization, life transformation, leadership development, volunteer deployment, generosity response, and disciple multiplication. The ranking assumes a congregation that prepares intentionally — not one that simply shows up.</p>
</section>
<section class="dir">
  <div class="dir-grid">

    <!-- TIER 1: THE BIG FIVE -->
    {"".join([
    f'''<div class="dir-card mega" style="border-color:{c};">
      <span class="dir-rank">{r}</span>
      <span class="dir-type" style="border-color:{c};color:{c};">{cat}</span>
      <h3 class="dir-title">{title}</h3>
      <p class="dir-why">{why}</p>
      <div class="dir-metrics">{"".join(f'<span class="dir-metric">{m}</span>' for m in metrics)}</div>
    </div>'''
    for r,c,cat,title,why,metrics in [
      ("1","var(--east)","Easter","Easter Sunday + Outreach","The highest-attended Sunday of the year combined with the highest theological stakes. Every unchurched person the congregation will ever bring arrives at Easter. It is simultaneously the most important evangelistic Sunday and the most important formation Sunday.",["Highest Attendance","Gospel Moment","Formation Launch","Baptism Opportunity","Next Step Critical"]),
      ("2","var(--gold-dk)","Generosity","Year-End Generosity Sunday","The intersection of maximum financial generosity motivation (December tax deadline) and maximum formation opportunity (the congregation is primed by the year's preaching). The Sunday that determines the giving culture for the following year.",["Giving Peak","Legacy Decisions","Pledge Commitment","Formation Depth","Budget Impact"]),
      ("3","var(--cap)","Capital Campaign","Capital Campaign Launch Sunday","The Sunday that determines whether the campaign succeeds. Not the campaign close — the launch. The congregation that leaves the launch Sunday with conviction gives extravagantly. The congregation that leaves confused gives adequately.",["Multi-Year Impact","Vision Formation","Leadership Test","Community Witness","Building Mission"]),
      ("4","var(--bap)","Baptism","Baptism Sunday","The Sunday that publicly marks the most significant formation decision in a person's life. The congregation that celebrates baptism with tears and testimonies is the congregation that produces more baptisms. Baptism Sundays reproduce themselves.",["Life-Change Visible","Outreach Catalyst","Community Formation","Story Power","Reproduction"]),
      ("5","var(--gen)","Launch","Fall Launch / Vision Sunday","The Sunday that sets the formation culture for the entire year. What the congregation believes is possible on Fall Launch Sunday is what they pursue for the next twelve months. It is the most leveraged Sunday on the calendar for congregational mobilization.",["Year Sets Here","SG Launch","Ministry Fair","Volunteer Peak","Culture Setting"]),
    ]])}

    <!-- TIER 2: THE MAJOR CATALYTIC SUNDAYS -->
    {"".join([
    f'''<div class="dir-card" style="border-color:{c};border-left:4px solid {c};">
      <span class="dir-rank" style="font-size:28px;color:rgba(0,0,0,.1);">{r}</span>
      <span class="dir-type" style="border-color:{c};color:{c};">{cat}</span>
      <h3 class="dir-title">{title}</h3>
      <p class="dir-why">{why}</p>
      <div class="dir-metrics">{"".join(f'<span class="dir-metric">{m}</span>' for m in metrics)}</div>
    </div>'''
    for r,c,cat,title,why,metrics in [
      ("6","var(--east)","Christmas","Christmas Eve Service","Second highest attendance. Maximum unchurched presence. The family that comes once per year comes tonight. Every element of the service is formation architecture for the person who has not been in months.",["Max Unchurched","Family Formation","Re-entry Point","Gospel Moment","Giving Peak"]),
      ("7","var(--gen)","Launch","New Year Launch Sunday","The congregation arrives already asking formation questions. The New Year series that launches with maximum intention converts January attenders into year-long formation participants.",["Formation Appetite","SG Launch","New Commitments","Vision Setting","Resolution Culture"]),
      ("8","var(--lead)","Ministry","Ministry Fair Sunday","The single highest volunteer recruitment Sunday of the year when executed with intention. Every ministry of the church visible, staffed, and inviting in a single weekend.",["Volunteer Peak","Ministry Visibility","Leadership Pipeline","Ownership Culture","Activation"]),
      ("9","var(--miss)","Outreach","Invite Sunday / Friend Sunday","The one Sunday per year designed entirely around the congregation bringing one person. The formation that produces an invitation culture is the most effective outreach infrastructure available.",["Evangelism Culture","Guest Peak","Relationship Mission","Network Effect","Outreach DNA"]),
      ("10","var(--bap)","Formation","Small Group Launch Weekend","The weekend that determines small group enrollment for the year. The congregation that launches with maximum commitment infrastructure on this Sunday doubles its group participation.",["Community Formation","Leadership Dev","Retention Peak","Discipleship Arc","Connection"]),
      ("11","var(--gen)","Stewardship","Pledge / Commitment Sunday","The specific Sunday that closes the stewardship campaign. Not the generosity sermon — the commitment moment. The infrastructure for capturing commitment determines the percentage who follow through.",["Giving Commitment","Formation Test","Budget Foundation","Generosity Culture","Trust"]),
      ("12","var(--east)","Seasonal","Mother's Day Sunday","Second-highest attendance after Easter. The pastoral complexity of this Sunday — 20% of the room is grieving — makes it the Sunday that most reveals the pastor's formation intelligence. Done well, it is the most pastorally transformative Sunday of the year.",["Attendance Peak","Pastoral Depth","Family Formation","Healing Opportunity","Return Catalyst"]),
      ("13","var(--lead)","Leadership","Elder / Deacon Installation Sunday","The Sunday that most visibly models the leadership culture the congregation will reproduce. The installation that includes the congregation's commissioning produces the leadership culture; the ceremony that excludes it produces an institutional culture.",["Leadership Culture","Governance Formation","Commissioning Power","Community Ownership","Multiplication"]),
      ("14","var(--cap)","Campaign","Capital Campaign Close / Celebration Sunday","The Sunday that closes the campaign and celebrates what God did through it. The close that tells the story before the story is fully written builds faith for the next campaign and the next generation of givers.",["Generosity Testimony","Faith Building","Community Celebration","Next Gen Formation","Legacy"]),
      ("15","var(--miss)","Mission","Mission Trip Launch / Return Sunday","The highest discipleship-density weekend in the church year. The congregation that sends and debriefs well produces the most formed disciples and the highest volunteer retention.",["Disciple Formation","Mission Culture","Story Power","Leadership Pipeline","Outreach DNA"]),
      ("16","var(--gen)","Seasonal","Thanksgiving Sunday","The Sunday that frames gratitude as formation rather than sentiment is the Sunday that produces a generous congregation in January. Thanksgiving is the formation setup for December giving.",["Gratitude Formation","Generosity Prep","Family Presence","Unchurched Moment","Year Review"]),
      ("17","var(--east)","Seasonal","Advent — First Sunday","The Sunday that sets the formation culture for the entire Advent season. The congregation that begins Advent with maximum intention arrives at Christmas Eve ready to receive rather than depleted by performing.",["Season Setting","Formation Arc","Family Rhythm","Expectation Culture","Christmas Prep"]),
      ("18","var(--bap)","Formation","40-Day Campaign Launch Sunday","The Sunday that launches the most formation-intensive experience available to a congregation. The 40-Day Campaign Launch that includes maximum communication, small group signup, and devotional distribution converts Sunday attenders into daily formation participants.",["Formation Peak","SG Launch","Daily Engagement","Campaign Arc","Community"]),
      ("19","var(--lead)","Pastoral","Pastoral Transition Sunday","The Sunday that determines whether the transition produces growth or decline. The congregation that receives the transition with theological depth and communal solidarity is the congregation that emerges stronger.",["Institutional Health","Leadership Transfer","Community Formation","Trust Building","Future Setting"]),
      ("20","var(--miss)","Justice","Justice / Reconciliation Sunday","The Sunday with the highest formation stakes and the lowest pastor comfort. The congregation that learns to navigate this Sunday with honesty and grace is the congregation that is becoming the church Jesus described.",["Formation Depth","Cultural Witness","Community Integrity","Prophetic Voice","Discipleship Test"]),
      ("21","var(--gen)","Anniversary","Church Anniversary Sunday","The Sunday that connects the current congregation to every congregation that came before it. Done with stories, witnesses, and vision — not just nostalgia — it produces the identity formation that sustains a congregation through every challenge.",["Identity Formation","Legacy Connection","Vision Renewal","Community Pride","Historical Witness"]),
      ("22","var(--bap)","Formation","Membership / Covenant Sunday","The Sunday that moves attenders into belonging. The congregation with a high membership percentage has the highest volunteer engagement, the highest giving percentage, and the highest retention. Membership is not bureaucracy — it is formation.",["Belonging Formation","Ownership Culture","Volunteer Pipeline","Giving Correlation","Retention"]),
      ("23","var(--cap)","Building","Groundbreaking / Dedication Sunday","The Sunday with the highest communal pride and the highest physical formation intensity. The congregation that stands on the dirt it is about to build on is the congregation that gives generously because the sacrifice is visible.",["Faith Milestone","Communal Vision","Campaign Momentum","Physical Formation","Pride"]),
      ("24","var(--miss)","Seasonal","Father's Day Sunday","The Sunday with the highest male attendance percentage of the year — and therefore the highest opportunity to form the men who form families who form congregations.",["Male Attendance Peak","Family Formation","Leadership Pipeline","Generational Impact","Return Catalyst"]),
      ("25","var(--gen)","Formation","Commissioning Sunday (End of Year)","The Sunday that closes the formation year and commissions the congregation into the next one. The congregation that ends intentionally begins intentionally.",["Year Review","Formation Summary","Next Year Vision","Community Celebration","Launch Prep"]),
    ]])}
  </div>
</section>
<div class="hdiv"></div>

<!-- ══ UNIVERSAL TOP 10 — APPLIES TO ALL 25 ══ -->
<section class="part" style="border-color:var(--gold);">
  <p class="part-kk" style="color:var(--gold-dk);">Universal Preparation System</p>
  <h2 class="part-h2" style="color:var(--ink);">The Top 10 Things That <em>Multiply Every</em> Flagship Sunday</h2>
  <p class="part-sub">Before the deep dives by Sunday type, these ten preparation practices apply to every flagship Sunday on the calendar — ranked by their impact on congregational mobilization, life transformation, and disciple multiplication. A congregation that executes all ten consistently produces exponential results on every major Sunday.</p>
</section>
<div class="callout" style="margin:0 80px 28px;border-color:rgba(201,168,76,.3);background:rgba(201,168,76,.03);">
  <div class="callout-icon">📐</div>
  <div class="callout-body">
    <span class="callout-label" style="color:var(--gold-dk);">How to Read the Rankings</span>
    <p class="callout-text">Each item is ranked by its return on preparation investment — the ratio of impact produced to effort required in the 4–6 weeks before the Sunday. Rank 1 is not the most dramatic. It is the highest-leverage. The ROI label indicates the primary multiplication area: <strong>Engagement</strong> (more people more deeply connected), <strong>Retention</strong> (people who come back), <strong>Mobilization</strong> (volunteers and leaders activated), <strong>Generosity</strong> (giving response), <strong>Multiplication</strong> (disciples who make disciples).</p>
  </div>
</div>
<section class="top10-wrap">
  <div class="top10-grid">
    {ri("1","Prayer Cover — The Infrastructure That Goes Before Everything","Nothing multiplies a flagship Sunday more reliably than a congregation that has been praying for it for six weeks. Not the pastor praying. The congregation praying — specifically, persistently, with names of people they are believing will be there. The churches that see God move exponentially on significant Sundays almost always trace the movement to a prayer infrastructure that was built well before the Sunday arrived. Recruit 50 people to pray for 50 specific people for 6 weeks before the Sunday. The results are not explainable without it.","Six weeks out: form the prayer team. Five weeks out: distribute the prayer cards. Sunday: the prayer team prays during the service. One week after: collect testimonies.","Multiplication","var(--gold)","var(--gold-dk)","Weeks 6–1",True)}
    {ri("2","Personal Invitation Culture — Activated Six Weeks Out","The single highest-impact behavior available to every congregation member is the personal invitation. Not the social media post. Not the church mailer. The specific, personal, face-to-face invitation from one person who knows you to one person who needs what the Sunday offers. Research consistently shows that 80% of people who are not in a church would come if personally invited. The congregation that activates personal invitation six weeks before a flagship Sunday produces 30–50% higher attendance than the congregation that announces the Sunday from the pulpit.","Six weeks out: preach the invitation culture. Four weeks out: give invitation cards with the date. Two weeks out: accountability check. Sunday: count the guests and honor the inviters.","Engagement","var(--gold)","var(--gold-dk)","Weeks 6–2")}
    {ri("3","Communication Cascade — Every Channel, Every Week, Six Weeks","The congregation that hears about a significant Sunday once is the congregation that forgets. The congregation that hears about it six times — from six different channels, with six different angles of the same story — is the congregation that shows up and brings someone. The communication cascade is not repetition. It is narrative escalation. Week 1: the announcement. Week 2: a story. Week 3: a testimony. Week 4: a specific invitation. Week 5: a practical preparation step. Week 6: the final call.","Build the six-week communication calendar in one session. Assign each channel (email, text, social, bulletin, pulpit, video) a specific week and angle. Execute without deviation.","Engagement","var(--cap)","var(--cap)","Weeks 6–1")}
    {ri("4","Response Infrastructure — Built Before the Sermon Is Written","The most common reason a significant Sunday produces less transformation than it could is that the response infrastructure was not ready. The communication card designed on Friday. The small group signup sheet that ran out. The prayer team that was not positioned. The follow-up email that went out eleven days later. The response infrastructure — every mechanism for capturing and following up on every response — must be designed, tested, and staffed before the sermon is written.","Four weeks out: design every response mechanism. Three weeks out: train every volunteer who will staff it. Two weeks out: test the follow-up sequence. Sunday: infrastructure is operational before the first person arrives.","Retention","var(--east)","var(--east)","Weeks 4–1")}
    {ri("5","Volunteer Mobilization — Recruited and Trained Four Weeks Out","Every flagship Sunday requires more people than a regular Sunday. The congregation that recruits volunteers for the Sunday on Thursday is the congregation that gets whoever is available. The congregation that recruits four weeks out gets the best people for the most important roles. For every 100 people expected to attend, recruit and train one volunteer. For every response the Sunday is designed to produce, staff a specific volunteer.","Four weeks out: identify every volunteer role. Three weeks out: recruit by name, not by general announcement. Two weeks out: train specifically. Sunday: brief every volunteer thirty minutes before the service.","Mobilization","var(--gen)","var(--gen)","Weeks 4–1")}
    {ri("6","The Follow-Up System — 48-Hour Window is Not Negotiable","Every person who responds to a significant Sunday — fills out a card, signs up for a group, makes a commitment, raises a hand, gets baptized, makes a giving decision — has a formation window of 48 hours in which the follow-up, if it arrives, reinforces the decision with 3x the impact it would have a week later. The 48-hour follow-up system is not an administrative nicety. It is the mechanism that converts Sunday moments into formation trajectories.","Build the follow-up sequence before the Sunday. Assign a person to every category of response card. Guarantee that every first-time guest receives a personal contact within 24 hours. Every commitment card followed up within 48 hours.","Retention","var(--east)","var(--east)","Weeks 3–1")}
    {ri("7","Testimony Integration — Three Stories That Do More Than Any Sermon","The three minutes a congregation member spends telling their own story of transformation — specifically, in their own words, without polish — does more formation work than thirty minutes of the best sermon. Every flagship Sunday should include at least one testimony that is directly connected to what the Sunday is about. Recruited, coached, and positioned in the service architecture at the moment of maximum formation impact — not after the offering.","Six weeks out: identify the testimony. Four weeks out: conduct the coaching interview. Two weeks out: final rehearsal. Sunday: testimony positioned before the response invitation, not after it.","Multiplication","var(--bap)","var(--bap)","Weeks 6–1")}
    {ri("8","Small Group Connection — The Sunday That Fills the Groups","Every flagship Sunday is a small group recruitment opportunity. The congregation that moves people from Sunday attendance to Thursday community multiplies its formation impact by a factor of five. The connection pathway from the flagship Sunday to a specific small group — with a specific name, a specific leader, a specific meeting time — must be as clear and frictionless as possible. Eliminate every step between 'I want to be in a group' and 'here is your group.'","Design the connection pathway before the Sunday. Have group leaders present and identifiable. Use the communication card for small group signup. Follow up every group interest card within 24 hours with a specific group assignment.","Multiplication","var(--gen)","var(--gen)","Weeks 5–1")}
    {ri("9","Leadership Development — Using the Sunday to Form the Next Generation","Every flagship Sunday is a formation laboratory for the leaders in the congregation who will run the next flagship Sunday. The associate pastor who watches the senior pastor prepare for a capital campaign launch is receiving the most valuable leadership training available. The team that debrief every flagship Sunday produces leaders who improve every subsequent Sunday. Invite apprentices into the preparation process, not just the execution.","Six weeks out: identify the leaders who will apprentice in the preparation. Each week: debrief with the apprentice team. One week after: conduct the full post-Sunday debrief with every volunteer.","Leadership Dev","var(--lead)","var(--lead)","Weeks 6+1")}
    {ri("10","The Formation Arc — Connecting the Sunday to What Comes Next","The flagship Sunday that does not connect to a formation arc — a 7-day journey, a 6-week series, a 40-day campaign, a small group study — has produced a peak experience. Peak experiences are not formation. Formation is the daily practice that follows the peak experience. Every flagship Sunday should close with a specific, accessible, compelling invitation to the formation arc that begins Monday morning.","Design the formation arc before designing the Sunday service. The sermon is the entry point to the arc, not the whole arc. Communicate the next step from the pulpit, in the bulletin, and on the response card.","Formation","var(--bap)","var(--bap)","Weeks 6–1")}
  </div>
</section>
<div class="hdiv"></div>

<!-- ══ DEEP DIVE 1: GENEROSITY SUNDAY / HARVEST ══ -->
<section class="part" style="border-color:var(--gen);">
  <p class="part-kk" style="color:var(--gen);">Deep Dive · Playbook One</p>
  <h2 class="part-h2" style="color:var(--ink);">Generosity Sunday <em>Harvest</em><br>— The Top 10</h2>
  <p class="part-sub"><p>The Generosity Sunday Harvest is the weekend that closes the stewardship season and invites the congregation's first-fruits response. It is also the most psychologically complex Sunday a pastor preaches — because the congregation arrives suspicious of the motive and the pastor arrives afraid of the ask. The congregation that executes the ten strategies below in the six weeks before Generosity Sunday does not produce a campaign. It produces a formation movement that expresses itself financially.</p>
  <p><strong>The fundamental principle:</strong> The congregation that gives most generously on Generosity Sunday has been formed around generosity for six weeks before they arrive. The Sunday is the harvest of six weeks of seed. You cannot harvest what you have not planted.</p></p>
</section>

<!-- Countdown Timeline: Generosity -->
<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(74,122,80,.08);border-bottom:1px solid rgba(74,122,80,.15);">
    <span style="font-size:20px;">◇</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 6-Week Generosity Sunday Countdown</h3>
  </div>
  <div class="cd-weeks">
    {cd_week("Week 6","★ Launch the prayer team — 50 people praying for 50 people","Begin the generosity formation devotional","Announce the series arc from the pulpit","Distribute personal invitation cards","Brief all staff on campaign vision")}
    {cd_week("Week 5","★ Preach Generosity Week 1 — Theology first","Share first testimony: why I give","Send handwritten notes from pastor to top 20 givers","Recruit small group leaders for campaign connection","Post week's giving theme on all channels")}
    {cd_week("Week 4","★ Generosity Week 2 — The formation of the giver","Launch the 7-Day Generosity devotional","Conduct family generosity conversation training","Volunteer debrief and preparation","Mail the stewardship letter with pledge card")}
    {cd_week("Week 3","★ Generosity Week 3 — Testimony Sunday","Invite second testimony: a first-time tither","Deacon and elder give first — before the congregation","Host a generosity conversation dinner for key families","Send text message campaign: Day 21 of formation")}
    {cd_week("Week 2","★ Generosity Week 4 — The specific invitation","Finalize Commitment Sunday response infrastructure","Train all ushers and response team","Send commitment card preview with personal pastor note","Social media: 48-hour countdown begins","Host legacy giving conversation for 55+ families")}
    {cd_week("Week 1","★ Commitment Sunday — Harvest day","Response card, pledge, and commitment infrastructure operational","Testimony positioned before the invitation","Prayer team deployed during the service","Elder reads the commitment prayer together","Three-point follow-up plan begins Monday")}
    {cd_week("SUNDAY","★ The Harvest Sunday","Every element designed for response","Testimony before the invitation","Every response card followed up by Tuesday","Text all responders by Monday 9am","Celebrate what was planted six weeks ago","","True","var(--gen)")}
  </div>
</div>

<section class="top10-wrap">
  <div class="top10-grid">
    {ri("1","Preach Formation, Not Fundraising — The Entire Series","The congregation that arrives at Generosity Sunday having heard six weeks of formation preaching about what generosity does to the giver's soul gives from conviction. The congregation that has heard one stewardship sermon per year for ten years gives from guilt or obligation — if they give. The most important preparation for Generosity Sunday is the formation series that precedes it. Every week: one truth about what holding tightly to money does to a person. One truth about what releasing it does. The anthropology of generosity.","Begin the generosity formation series six weeks before Commitment Sunday. Week 1: theology of stewardship. Week 2: the giver's soul. Week 3: testimony. Week 4: the specific invitation. Week 5: the next generation. Week 6: the harvest.","Formation","var(--gen)","var(--gen)","Weeks 6–1",True)}
    {ri("2","The Leaders Give First — Before the Congregation is Asked","The single most powerful generosity statement a congregation can make is the announcement that the elders, deacons, and staff have already committed before asking anyone else. This is not a matching gift strategy. It is a theology of leadership by example. The congregation that hears 'your leaders have already committed' is the congregation that responds from gratitude rather than obligation.","Four weeks out: meet with the governing board and ask for their commitment first. Three weeks out: announce the leadership commitment percentage from the pulpit without dollar amounts. This alone increases campaign response by 15–25%.","Generosity","var(--gen)","var(--gen)","Weeks 4–3")}
    {ri("3","The Testimony of the First-Time Tither — Not the Major Donor","The most formation-producing testimony in any stewardship campaign is not the major donor who gives easily. It is the first-time tither who gave what they could not afford and discovered they could. This testimony is more powerful than any sermon because it is available to every person in the congregation — unlike the major donor testimony, which most people believe is not for them.","Recruit the first-time tither testimony four weeks out. Coach it to 3 minutes: what I believed about money, what I decided, what happened. Position it directly before the commitment invitation.","Engagement","var(--gen)","var(--gen)","Weeks 4–1")}
    {ri("4","The Personal Pastor Letter — Handwritten to the Top 20%","Twenty percent of the congregation typically accounts for eighty percent of the giving. A handwritten letter from the pastor to every significant giver, received two weeks before Commitment Sunday, produces a giving response that no pulpit appeal can match. Not because of the content. Because of the relationship it demonstrates.","Three weeks out: write 20 personal letters to the top 20 giving households. Not typed. Handwritten. Specific to each family — what you know about their giving history and their family. This takes three hours and multiplies the campaign outcome by more than any other single act.","Generosity","var(--gen)","var(--gen)","Week 3")}
    {ri("5","The Generosity Devotional — 21 Days Before the Sunday","The congregation that has been reading a daily generosity devotional for three weeks before Commitment Sunday has been formed around generosity before they are asked to give. The devotional is not a campaign tool. It is a formation instrument. One thought per day. One Scripture. One reflection question. One practice. Distributed to every household.","Three weeks out: distribute the 21-day generosity devotional — in print, via app, via daily text. One message per day. Do not use the devotional to build toward the ask. Use it to build the person who will make the ask unnecessary.","Formation","var(--gen)","var(--gen)","Weeks 3–1")}
    {ri("6","The Family Generosity Conversation — Parents and Children Together","The congregation that gives most generously from one generation to the next is the congregation whose parents talked about giving with their children. The family generosity conversation — structured, simple, age-appropriate — plants the formation that a stewardship sermon cannot reach.","Four weeks out: distribute the family generosity conversation guide. Two weeks out: preach to parents about talking to their children about money. Commitment Sunday: invite families to complete the pledge card together.","Multiplication","var(--gen)","var(--gen)","Weeks 4–2")}
    {ri("7","The Legacy Giving Conversation — Hosted Separately for 55+ Families","The congregation's highest untapped generosity resource is the planned gift. The high-capacity family whose estate has never been asked about will not respond to a stewardship sermon. They will respond to a dinner, a conversation, an estate attorney present, and a pastor who shows up and asks.","Five weeks out: host a dinner for families over 55 with higher capacity. Bring a Christian estate attorney. Have the pastor lead the conversation. Do not make an ask at the dinner. Schedule individual follow-up conversations.","Generosity","var(--gen)","var(--gen)","Week 5")}
    {ri("8","The Matching Gift — Announced Three Weeks Out","A matching gift — secured from a high-capacity family three weeks before Commitment Sunday — doubles the motivational energy of the campaign without doubling the ask. The matching gift is not primarily a financial strategy. It is a declaration of faith by one family and an invitation to partnership for every other family.","Secure the matching commitment six weeks out. Announce it three weeks out with a story — not just a number. 'One family in this congregation believes so strongly in what God is doing here that they will match every dollar given on Commitment Sunday up to [amount].'","Generosity","var(--gen)","var(--gen)","Week 3")}
    {ri("9","The Commitment Card as Worship — Not Administration","The commitment card that is filled out while the congregation sings a worship song, placed in the offering plate as an act of worship, and prayed over by the elders before the service ends is a different act than the commitment card that is tallied and reported. The theology of the commitment card determines whether it produces formation or transaction.","Design the commitment moment as worship, not administration. Song selection, elder prayer over the cards, physical placement as offering — every element communicates that this is a sacred act, not a pledge drive.","Formation","var(--gen)","var(--gen)","Weeks 2–1")}
    {ri("10","The 48-Hour Celebration — Report What God Did","The email that goes out within 48 hours of Commitment Sunday reporting what the congregation gave — not in a tone of relief that the budget is covered, but in a tone of awe at what God did through his people — is the most formation-producing communication the stewardship season produces. The congregation that hears 'here is what God did through you' is the congregation that gives again next year.","Draft the celebration email before Commitment Sunday. Have the template ready. Fill in the numbers Monday morning and send by Monday noon. Preach the celebration the following Sunday.","Retention","var(--gen)","var(--gen)","Day +1")}
  </div>
</section>
<div class="hdiv"></div>

<!-- ══ DEEP DIVE 2: CAPITAL CAMPAIGN ══ -->
<section class="part" style="border-color:var(--cap);">
  <p class="part-kk" style="color:var(--cap);">Deep Dive · Playbook Two</p>
  <h2 class="part-h2" style="color:var(--ink);">Capital Campaign <em>Launch Sunday</em><br>— The Top 10</h2>
  <p class="part-sub"><p>The Capital Campaign Launch Sunday is the Sunday that determines whether the campaign produces the building or only a portion of it. The congregation that leaves the launch Sunday with conviction about why they are building — not what they are building — is the congregation that gives sacrificially over three years. The congregation that leaves with questions about the vision gives adequately when it is convenient.</p>
  <p><strong>The fundamental principle:</strong> Capital campaigns are not building programs. They are formation programs that produce a building as a byproduct. The congregation that is formed around the mission the building enables gives to the building. The congregation that is asked to fund the building gives to the building less generously and stops giving sooner.</p></p>
</section>

<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(74,90,138,.08);border-bottom:1px solid rgba(74,90,138,.15);">
    <span style="font-size:20px;">🏛</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 6-Week Capital Campaign Launch Countdown</h3>
  </div>
  <div class="cd-weeks">
    {cd_week("Week 6","★ Campaign case statement complete","Quiet phase conversations begin with top 25 families","Prayer team commissioned for campaign","Architect's rendering available for display","Campaign narrative rehearsed by all leaders")}
    {cd_week("Week 5","★ Quiet phase — leadership commitments","Host dinner for top giving families","Share the mission case: why we build","Early commitment testimonies recorded","Every elder and deacon commits in quiet phase")}
    {cd_week("Week 4","★ Quiet phase closes","Announce to congregation: quiet phase exceeded [X]%","Build pre-launch momentum — one story per day","Train all small group leaders on campaign narrative","Distribute campaign devotional to all households")}
    {cd_week("Week 3","★ Pre-launch momentum building","Campaign devotional in daily use","Testimony videos released — one per day","Town hall meeting: answer every question","Children's and youth campaign components launch","Social media campaign: why we build")}
    {cd_week("Week 2","★ Final launch preparation","Response infrastructure tested and staffed","Commitment card design finalized","All volunteers briefed and positioned","Campaign Sunday order of service finalized","Matching gift announcement prepared")}
    {cd_week("Week 1","★ Launch week","Daily prayer and fasting option offered","Final testimonies distributed","One personal pastor contact per top-50 family","Venue prepared for maximum visual impact","Launch Sunday: every element aligned to mission narrative")}
    {cd_week("SUNDAY","★ Capital Campaign Launch Sunday","Vision statement from every elder","Key testimony: 'what this building enables in my family'","Commitment card as worship moment","Quiet phase totals announced from pulpit","Matching gift announced","48-hour follow-up sequence begins","","True","var(--cap)")}
  </div>
</div>

<section class="top10-wrap">
  <div class="top10-grid">
    {ri("1","The Quiet Phase — 40–60% Committed Before the Public Launch","The capital campaign that announces its goal to the full congregation before securing 40–60% of the goal in commitments from the top 15–20% of givers has started with a momentum deficit. The quiet phase — six to eight weeks of private, personal conversations with high-capacity families — produces the announcement that says 'before we asked everyone, this many said yes.' That announcement changes the congregation's faith response.","Eight weeks out: identify the top 20% of givers. Six weeks out: begin quiet phase conversations — pastor to family, personally, with the mission narrative. Secure 40–60% of the campaign goal before the public launch Sunday. Announce the quiet phase total at the launch.","Generosity","var(--cap)","var(--cap)","Weeks 8–2",True)}
    {ri("2","The Mission Case — Build the Why Before the What","The congregation that understands what the building enables — more children formed, more families served, more community reached — gives to the mission. The congregation that understands only what the building costs gives to the construction. The mission case document is the most important piece of capital campaign communication — one page, one story, one vision for what the building makes possible.","Six weeks out: write the mission case. One page. Why we build: the ministry the building enables. One story that illustrates it. One vision statement that names what it produces. Distribute it in every format before the public launch.","Engagement","var(--cap)","var(--cap)","Weeks 6–1")}
    {ri("3","The Testimonies of the Life Changed in the Current Space","The testimony that produces the most capital campaign generosity is not the vision for the new building. It is the story of the life that was changed in the current building — and why the new building would have changed even more. The person who was baptized in the current sanctuary. The child whose parents first heard the gospel in the current fellowship hall. The recovery group that meets in the current basement.","Five weeks out: collect five testimonies of life change in the current facility. Record them on video. Release one per week in the five weeks before the launch. Use the most powerful one in the launch service.","Engagement","var(--cap)","var(--cap)","Weeks 5–1")}
    {ri("4","The Three-Year Pledge Framework — Month, Not Year","The capital campaign that asks for a three-year pledge and helps the congregation calculate a monthly amount produces higher completion rates than the campaign that asks for a total amount. Monthly feels manageable. The total is overwhelming. The pledge card that says '$50/month for 36 months — your three-year gift is $1,800' converts more pledges than '$1,800 over three years.'","Design the commitment card around a monthly amount. Train every conversation around the monthly figure. The ask is never 'how much can you give?' The ask is 'what could you commit per month for 36 months that would stretch you without breaking you?'","Generosity","var(--cap)","var(--cap)","Weeks 4–1")}
    {ri("5","The Children and Youth Campaign — Building for the Next Generation","The capital campaign that includes the children and youth of the congregation as active participants — not spectators — produces the highest family giving response. The family that watches their child contribute their own gift to the building campaign gives more than the family that gives alone.","Five weeks out: design a children's and youth campaign component. Children earn money by doing chores. Youth participate in a service project whose proceeds go to the campaign. Children bring their gifts on Launch Sunday. This single element increases family giving by 15–30%.","Multiplication","var(--cap)","var(--cap)","Weeks 5–1")}
    {ri("6","The Architect's Rendering — What People Are Giving To","The congregation that can see what they are giving to gives more than the congregation that is giving to a concept. The architect's rendering — placed at every entrance, printed in the bulletin, shown on every screen — makes the vision tangible before it is real.","Four weeks out: display the architect's rendering in every available space. Create a scale model if budget allows. Commission a video walkthrough of the future space. Make the vision visible before the launch Sunday.","Engagement","var(--cap)","var(--cap)","Weeks 4–1")}
    {ri("7","The Town Hall — Every Question Answered Before the Ask","The congregation that has unanswered questions about the capital campaign — the financial need, the construction plan, the debt strategy, the operational impact — gives less than the congregation that has had every question answered. The pre-launch town hall is not optional. It is the formation meeting that converts skeptics into champions.","Three weeks out: host an all-congregation town hall meeting. The senior pastor, the executive pastor, the board chair, and the architect are all present. Every question is answered. No question is deflected. The meeting ends with prayer.","Engagement","var(--cap)","var(--cap)","Week 3")}
    {ri("8","The Legacy Naming Opportunity — For High-Capacity Families","The well-executed capital campaign includes a limited number of naming opportunities — the children's wing, the prayer room, the fellowship hall — reserved for families whose gifts at a specific level make a permanent statement of faith about what the building is for.","Six weeks out: design the naming opportunity tiers. Identify the families for each tier. Have the conversations in the quiet phase. Announce the named spaces on Launch Sunday as a celebration of what God has already done through those families.","Generosity","var(--cap)","var(--cap)","Weeks 6–1")}
    {ri("9","The Matching Gift — Announced at the Launch","The capital campaign matching gift announced at the launch Sunday changes the congregation's sense of possibility. 'One family has committed to match every gift given today up to $250,000' converts the launch Sunday into the highest single-day giving event in the campaign.","Secure the matching commitment in the quiet phase. Do not announce it before the launch Sunday. Use it as the final motivation at the commitment moment.","Generosity","var(--cap)","var(--cap)","Weeks 2–Launch")}
    {ri("10","The Groundbreaking as Celebration — Not Construction Notice","The groundbreaking ceremony six to nine months after the campaign launch is the most emotionally significant formation event of the campaign. The congregation that stands on the dirt, holding a shovel, singing, is the congregation that keeps its pledge because it was there when the ground was turned.","Plan the groundbreaking as a full worship service — outside, at the site, with the congregation gathered. Communion, testimony, prayer, song. The groundbreaking is not construction. It is consecration.","Retention","var(--cap)","var(--cap)","Month 6")}
  </div>
</section>
<div class="hdiv"></div>

<!-- ══ DEEP DIVE 3: EASTER OUTREACH ══ -->
<section class="part" style="border-color:var(--east);">
  <p class="part-kk" style="color:var(--east);">Deep Dive · Playbook Three</p>
  <h2 class="part-h2" style="color:var(--ink);"><em>Easter Outreach</em> Sunday<br>— The Top 10</h2>
  <p class="part-sub"><p>Easter Sunday is the highest-attended Sunday of the year — and the Sunday with the highest percentage of people present who will not return the following week unless something specific happens to bring them back. The congregation that treats Easter as its best production Sunday produces an experience. The congregation that treats Easter as its most intentional formation and outreach Sunday produces disciples.</p>
  <p><strong>The fundamental principle:</strong> Easter is not the destination. It is the door. The formation arc that begins the Monday after Easter is what determines whether the guests who came for Easter become the disciples who stay for the formation.</p></p>
</section>

<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(138,74,48,.08);border-bottom:1px solid rgba(138,74,48,.15);">
    <span style="font-size:20px;">✝</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 6-Week Easter Outreach Countdown</h3>
  </div>
  <div class="cd-weeks">
    {cd_week("Week 6","★ 50-for-50 prayer launch: 50 people pray for 50 specific people","Easter invitation cards distributed to every family","Holy Week schedule announced","Sermon series arc finalized","Baptism Sunday (day after Easter) announced")}
    {cd_week("Week 5","★ Personal invitation week: every family equipped","Lenten devotional launched for congregation","Guest follow-up infrastructure design begins","Video invite distributed for sharing","Volunteer roles for Easter Sunday recruitment begins")}
    {cd_week("Week 4 (Palm Sunday)","★ First catalytic Sunday of Holy Week","Congregation invited to read Passion narrative daily","Baptism candidates contacted and coached","Easter service details finalized","Guest experience team training begins")}
    {cd_week("Week 3","★ Holy Week formation arc","Wednesday night Tenebrae service","Maundy Thursday footwashing and communion","Good Friday service — highest attendance besides Easter","★ Every service communicates Easter invitation","★ Baptism Sunday preview announced")}
    {cd_week("Week 2","★ Final Easter preparation","All volunteer roles confirmed and briefed","Overflow preparation finalized","Guest follow-up sequence drafted and ready","Communication card designed and printed","Every greeter briefed on guest experience protocol")}
    {cd_week("Week 1","★ Easter week","Daily prayer and fasting for specific people","Personal pastor contacts: 20 specific families","All response infrastructure tested","Text blast to entire congregation list: bring someone Sunday","Children's Easter experience preparation complete")}
    {cd_week("SUNDAY","★ Easter Sunday","Maximum greeting team deployed","Multiple service options if needed","Baptism announced for following Sunday","Communication card in every seat","Post-Easter series announced from pulpit","★ 48-hour follow-up system activated Monday 8am","","True","var(--east)")}
  </div>
</div>

<section class="top10-wrap">
  <div class="top10-grid">
    {ri("1","The 50-for-50 Prayer Strategy — Activated Six Weeks Out","The most reproducible Easter outreach strategy in church history is the simplest: recruit 50 people to pray for 50 specific people every day for 50 days before Easter Sunday. Not to invite them — to pray for them first. The congregation that prays specifically for specific people for six weeks before Easter sees attendance numbers that the best production cannot produce.","Six weeks out: recruit 50 people (or 100, or 200). Give each person a card with space for five names. Collect the cards. Pray for every name on the list as a congregation in every service for six weeks. Invite after four weeks of prayer — not before.","Multiplication","var(--east)","var(--east)","Weeks 6–1",True)}
    {ri("2","Baptism Sunday the Week After Easter — Announced from the Easter Pulpit","The single most formation-producing decision a congregation can make for Easter is to announce Baptism Sunday for the following week from the Easter pulpit. The person who comes to Easter and hears 'next Sunday, we will baptize everyone who has decided to follow Jesus — including anyone who makes that decision today' has been given a specific, accessible, immediate next step.","Announce Baptism Sunday from the Easter pulpit before the sermon. 'Next week, this time, this room, we will baptize every person who has decided to follow Jesus.' Then preach the resurrection. Watch what happens.","Multiplication","var(--east)","var(--east)","Weeks 4–Launch")}
    {ri("3","The Guest Experience — Designed as a Formation System","The Easter guest who has an extraordinary experience — parking, greeting, children's check-in, seat, bulletin, service, follow-up — returns. The Easter guest who has a confusing experience does not. The guest experience is not hospitality. It is formation infrastructure. Every touchpoint communicates whether this congregation is for people who are already formed or for people who are still becoming.","Four weeks out: audit every guest experience touchpoint from parking to post-service follow-up. Recruit and train a guest experience team that is double the normal size. Brief every regular attender on how to treat a guest.","Retention","var(--east)","var(--east)","Weeks 4–1")}
    {ri("4","The Personal Invitation — With a Physical Card","Research consistently shows that the most effective Easter outreach strategy is the personal invitation from one person who knows the guest. The physical card — the size of a business card, with the date, time, and address — is the instrument of the personal invitation. The congregation that has invitation cards four weeks before Easter has four weeks to invite.","Four weeks out: distribute Easter invitation cards to every family — 5 cards per family minimum. Two weeks out: accountability from the pulpit: 'How many of you have given your cards to someone? Stand.' The physical card converts intention into action.","Engagement","var(--east)","var(--east)","Weeks 4–1")}
    {ri("5","The Post-Easter Formation Arc — Announced Before They Leave","The most common Easter failure is producing a peak experience with no formation arc attached. The congregation that hears from the Easter pulpit what begins Monday — the 7-Day Resurrection Journey, the post-Easter series, the small group launch — has been given a reason to return. The congregation that hears only 'see you next Easter' returns at exactly that rate.","Design the post-Easter formation arc before designing the Easter service. Announce it from the Easter pulpit. Distribute the 7-Day Resurrection Journey guide at the door as guests leave. Make the next step as accessible and compelling as the service itself.","Retention","var(--east)","var(--east)","Weeks 6–Launch")}
    {ri("6","The Holy Week Formation Arc — Not Just Easter Sunday","The congregation that participates in Holy Week — Palm Sunday, Maundy Thursday, Good Friday, Easter — is the congregation most transformed by Easter. The transformation compounds across the week. The Maundy Thursday service that practices foot washing, the Good Friday service that sits in darkness, the Easter sunrise service that greets the dawn — these are the formation experiences that make Easter Sunday the culmination of something rather than the beginning of nothing.","Build the full Holy Week calendar six weeks out. Promote every service as a formation experience, not a program addition. The congregation that experiences Maundy Thursday and Good Friday arrives at Easter Sunday with a readiness to receive that the congregation that only attends Easter cannot have.","Formation","var(--east)","var(--east)","Weeks 6–1")}
    {ri("7","The Children's Easter Experience — Designed for the Unchurched Child","The Easter guest brings children. The unchurched child who has an extraordinary Easter children's experience becomes the primary reason the unchurched family returns. The children's Easter experience is not a junior version of the adult service. It is the formation event that has the highest retention impact of any Easter element.","Four weeks out: design the children's Easter experience with the same intentionality as the adult service. Four weeks out: recruit and train children's Easter volunteers. One week out: brief every children's volunteer on the unchurched child experience.","Retention","var(--east)","var(--east)","Weeks 4–1")}
    {ri("8","The Overflow Plan — Faith That Expects More Than the Room Holds","The congregation that plans for overflow is the congregation that sees God fill the room. The congregation that does not plan for overflow is the congregation that turns people away and loses them. The overflow plan — a second service, a simulcast room, a parking plan — is not logistics. It is a declaration of faith that God will bring more than the room can hold.","Five weeks out: design the overflow plan. Four weeks out: recruit overflow volunteers. Two weeks out: communicate the overflow options to the congregation. Sunday: overflow is a celebration, not a problem.","Engagement","var(--east)","var(--east)","Weeks 5–1")}
    {ri("9","The 48-Hour Guest Follow-Up — Before They Forget They Were There","The Easter guest who receives a personal follow-up within 48 hours — not a generic mass email, a specific contact from a specific person — is three times more likely to return than the guest who does not. The follow-up is not marketing. It is pastoral care for a person who just had a significant experience.","Design the follow-up sequence before Easter. Collect communication cards during the service. Assign specific follow-up to specific volunteers. Monday 8am: begin the follow-up sequence. Every first-time guest receives a personal contact by Tuesday.","Retention","var(--east)","var(--east)","Day +1")}
    {ri("10","The Easter Giving Moment — Not an Afterthought","Easter is the second-highest single-day giving opportunity of the year. The congregation that treats the Easter offering as an afterthought after a long service misses the formation opportunity. The Easter offering moment — positioned with intention, framed as an act of gratitude for the resurrection, with a specific mission it funds — is the generosity formation moment that shapes the giving culture for the rest of the year.","Design the Easter offering moment as a worship act, not an administrative pause. Frame it as a response to the resurrection: 'Because he rose, we give.' Designate a specific mission that the Easter offering funds. Announce what the Easter offering will do.","Generosity","var(--east)","var(--east)","Weeks 2–1")}
  </div>
</section>
<div class="hdiv"></div>

<!-- ══ DEEP DIVE 4: BAPTISM SUNDAY ══ -->
<section class="part" style="border-color:var(--bap);">
  <p class="part-kk" style="color:var(--bap);">Deep Dive · Playbook Four</p>
  <h2 class="part-h2" style="color:var(--ink);"><em>Baptism Sunday</em><br>— The Top 10</h2>
  <p class="part-sub"><p>Baptism Sunday is the most emotionally powerful and formation-dense Sunday in the church year — when it is prepared for. It is also the Sunday most frequently under-prepared for, treated as a logistical event rather than a formation catalyst. The congregation that has been praying for the people being baptized for four weeks, that knows their stories, that is positioned to celebrate with tears, is the congregation that produces more baptisms every subsequent year.</p>
  <p><strong>The fundamental principle:</strong> Baptism Sundays reproduce themselves. The congregation that celebrates one baptism with full formation infrastructure produces the next baptism within 60 days. The congregation that processes baptism as a program item produces baptisms at the rate of program items — which is to say, rarely and without momentum.</p></p>
</section>

<div class="countdown" style="margin:0 80px 24px;">
  <div class="cd-header" style="background:rgba(90,74,138,.08);border-bottom:1px solid rgba(90,74,138,.15);">
    <span style="font-size:20px;">💧</span>
    <h3 class="cd-header-title" style="color:var(--ink);">The 4-Week Baptism Sunday Countdown</h3>
  </div>
  <div class="cd-weeks">
    {cd_week("Week 4","★ Baptism candidates identified and contacted","Personal interview with each candidate begins","Congregation invited to prayer for candidates","Baptism Sunday announced from pulpit","Story collection from each candidate begins")}
    {cd_week("Week 3","★ Candidate stories recorded (video or written)","Prayer team assigned to each candidate","Family and friends of candidates personally invited","Baptism preparation class scheduled","Stories shared in service — building toward Sunday")}
    {cd_week("Week 2","★ Baptism preparation class — candidates + their guests","Share one story from each candidate in service","Personal invitation push: 'bring someone for their baptism'","Logistics confirmed: pool, team, photography, video","Congregation briefed: how to celebrate with tears")}
    {cd_week("Week 1","★ Final preparation week","Personal pastor conversation with each candidate","Every candidate's family and friends directly contacted","Story preview shared on all channels","Service order finalized: stories before the water","Prayer team briefed and positioned")}
    {cd_week("SUNDAY","★ Baptism Sunday","Stories told before the water","Family positioned in front row","Prayer team prays over each candidate before they go in","Congregation invited to respond after baptisms","★ Post-baptism pathway announced","★ Next Baptism Sunday announced from pulpit","","True","var(--bap)")}
  </div>
</div>

<section class="top10-wrap">
  <div class="top10-grid">
    {ri("1","The Story Before the Water — Always","The baptism that is preceded by the candidate's story produces more faith in the congregation and more resolve in the candidate than the baptism that goes directly to the water. Three minutes. What my life was before. What happened. What is different now. The story is not preparation for the baptism. The story is the formation event. The water is the public declaration of the story.","Four weeks out: collect the story from every candidate. Coach it to three minutes: before, what happened, after. Never more than three minutes. Never less than one minute. Position the story in the service so the congregation is already in tears before the candidate gets in the water.","Engagement","var(--bap)","var(--bap)","Weeks 4–1",True)}
    {ri("2","Announce the Next Baptism Sunday the Moment This One Ends","The single most reproducible baptism strategy is the announcement from the baptism pulpit: 'Our next Baptism Sunday is [date]. If you have been thinking about baptism, this is your invitation. See me after the service.' The congregation that hears this announcement while still moved by the baptisms they just witnessed produces the most baptism candidates for the next Sunday.","Design the announcement before the Sunday. Have the pastor deliver it immediately after the final baptism, while the congregation is still standing and celebrating. The next Baptism Sunday should be within 60–90 days.","Multiplication","var(--bap)","var(--bap)","Launch Day")}
    {ri("3","The Prayer Team — One Person Assigned to Each Candidate","The candidate who is prayed over by name, personally, by a specific congregation member who has been assigned to them for four weeks, arrives at their baptism differently than the candidate who comes alone. The prayer team is not a pastoral support. It is the congregation's expression that this person's decision matters to the whole body.","Four weeks out: assign one prayer team member to each candidate. The assignment includes: weekly prayer for the candidate, one personal conversation, and presence at the baptism positioned near the family.","Formation","var(--bap)","var(--bap)","Weeks 4–1")}
    {ri("4","The Family Invitation — Personal and Specific","The baptism of an adult family member is the highest-impact outreach moment available to any congregation. Every unchurched family member who comes to witness a baptism is present for the most emotionally compelling worship service the church produces. The candidate's family must be personally, specifically, individually invited — not by announcement but by the pastor or a team member.","Three weeks out: obtain the list of every family member and close friend of every candidate. Assign a specific person to personally contact each family member with a personal invitation from the pastor.","Engagement","var(--bap)","var(--bap)","Weeks 3–1")}
    {ri("5","The Congregation's Role — Taught Before the Sunday","The congregation that does not know how to celebrate a baptism watches it. The congregation that has been taught — that this is the moment to stand, to weep, to cheer, to affirm, that their response is part of the formation of the person being baptized — participates. Participation produces more baptisms. Observation does not.","The Sunday before Baptism Sunday: teach the congregation their role. 'When [name] goes under the water, I am going to invite you to stand and say their name aloud. Here is why that matters to them and to God.'","Formation","var(--bap)","var(--bap)","Week 1")}
    {ri("6","The Baptism Preparation Class — Theology Before the Water","The candidate who understands what baptism means theologically arrives at the water with conviction, not just emotion. The preparation class is not a hoop to jump through. It is the formation event that makes the baptism the public declaration of a private conviction rather than a public experience of a private sentiment.","Three weeks out: schedule the baptism preparation class. One session, 90 minutes, led by the pastor. Cover: what baptism is, what it is not, what you are declaring, what the congregation is promising. Invite the candidates' families to attend.","Formation","var(--bap)","var(--bap)","Week 3")}
    {ri("7","The Photography and Video — As Ministry, Not Production","The baptism photograph that is in the candidate's home within one week of the Sunday is the most enduring formation artifact the church produces. It is on the refrigerator for years. It is the tangible reminder of a decision that might otherwise fade.","Recruit a photographer and videographer specifically for Baptism Sunday. Budget for printing and delivering a photograph to each candidate's home within one week. The photograph costs $15 to print and produce. It is the most formation-dense $15 the church spends.","Retention","var(--bap)","var(--bap)","Day +7")}
    {ri("8","The Post-Baptism Pathway — Announced the Same Day","The newly baptized person has the highest formation motivation of any person in the congregation — for approximately 72 hours after the baptism. The church that has a specific, accessible, compelling next step ready for the newly baptized person converts that motivation into formation. The church that has nothing loses it.","Design the post-baptism pathway before the Sunday. The pathway includes: a specific small group connected to the candidate, a meeting with the pastor or a formation coach within one week, the 7-Day post-baptism devotional distributed at the baptism.","Retention","var(--bap)","var(--bap)","Launch Day")}
    {ri("9","The Baptism Testimony Shared Beyond the Sunday","The baptism story that is shared on video, on social media, with the congregation's network, extends the formation impact of the baptism Sunday beyond the room. The unchurched person who sees a 90-second baptism testimony video in their social media feed has received the most compelling outreach the church can produce.","With the candidate's permission, record the baptism story in a 90-second format. Share it on all church social media channels the Monday after Baptism Sunday. Personal shares by congregation members produce more impact than institutional posts.","Multiplication","var(--bap)","var(--bap)","Day +1")}
    {ri("10","Schedule Baptism Sundays Four Times Per Year — Minimum","The church that baptizes once per year produces a trickle. The church that baptizes four times per year produces a river. The frequency of the invitation determines the frequency of the response. Every person in the congregation who is considering baptism needs to know that the next opportunity is within 90 days, not next year.","Set four Baptism Sundays on the annual calendar on January 1. Announce them in the new year vision message. Repeat the announcement from the pulpit every six to eight weeks.","Multiplication","var(--bap)","var(--bap)","Annual")}
  </div>
</section>
<div class="hdiv"></div>

<!-- ══ THE 7 PRINCIPLES THAT GOVERN ALL 25 ══ -->
<section class="sect-intro">
  <p class="si-kk" style="color:var(--gold-dk);">The Foundation</p>
  <h2 class="si-h2">The 7 <em>Governing Principles</em> Behind Every Flagship Sunday</h2>
  <p class="si-sub">Every preparation strategy in this playbook emerges from seven convictions about how God works through intentional preparation. These are not best practices. They are theological commitments that produce the best practices.</p>
</section>
<section class="principle-wrap">
  <div class="principle-grid">
    {"".join([
    f'''<div class="principle" style="border-color:{c};background:rgba(0,0,0,.01);">
      <span class="pr-n">{n}</span>
      <h3 class="pr-title">{title}</h3>
      <p class="pr-body">{body}</p>
    </div>'''
    for n,c,title,body in [
      ("I","var(--gold)","Prayer Is Not Preparation's Companion — It Is Its Foundation","No preparation strategy in this playbook outperforms prayer. The churches that see God move exponentially on flagship Sundays trace every movement to a prayer infrastructure that was built before the production was designed. Prayer is not the spiritual wrapper around the practical work. It is the practical work."),
      ("II","var(--gen)","The Sermon Is the Tip of the Iceberg","The congregation sees the sermon. They do not see the six weeks of prayer, communication, volunteer training, follow-up infrastructure, and formation connection that make the sermon the beginning of something rather than the end of an hour. The iceberg produces the results. The tip receives the credit."),
      ("III","var(--east)","Every Significant Sunday Reproduces Itself — or Does Not","The Baptism Sunday that is celebrated with full formation infrastructure produces the next baptism. The Easter Sunday with a compelling post-Easter formation arc produces the congregation that brings someone next Easter. The Generosity Sunday with a 48-hour follow-up produces the congregation that gives more generously next year. Formation is reproductive or it is not formation."),
      ("IV","var(--cap)","The Response Infrastructure Is More Important Than the Sermon","The best sermon ever preached in a congregation that had no mechanism for capturing the response produced less transformation than a mediocre sermon in a congregation with a fully staffed response infrastructure. The communication card, the small group signup, the follow-up system — these are not administrative tools. They are formation mechanisms."),
      ("V","var(--bap)","Personal Is Always More Powerful Than Institutional","The personal invitation outperforms the church mailer by a factor of ten. The handwritten note outperforms the email blast by a factor of five. The personal follow-up phone call outperforms the automated text by a factor of three. Scale the personal. Never substitute the institutional for it."),
      ("VI","var(--lead)","The Story Does What the Sermon Cannot","The three-minute testimony by a congregation member produces formation that the thirty-minute sermon cannot replicate. The story is not illustration. It is evidence. Evidence that the gospel does what it promises, in this congregation, to people the audience already knows. The pastor who replaces one sermon with three stories has not reduced their formation impact. They have multiplied it."),
      ("VII","var(--miss)","The Sunday Is the Door, Not the Room","Every flagship Sunday is the beginning of a formation arc, not the formation arc itself. The sermon is the door. The 7-day journey is the hallway. The small group is the room. The 40-day campaign is where formation happens. The congregation that invests all its preparation energy in the Sunday and none in what comes after has built a beautiful door to an empty building."),
    ]])}
  </div>
</section>

<div class="hdiv"></div>

<section class="back">
  <p class="bq">"The Sunday that changes the most lives is the one prepared for with the most prayer, the most intentional communication, the most carefully staffed response infrastructure, and the most compelling formation arc for the Monday that follows. This playbook exists so that every pastor who picks it up walks into their most significant Sundays not hoping for something to happen — but having built the conditions in which God moves."</p>
  <p class="ba">Brett Eastman · Founder, Lifetogether</p>
  <p class="bc">
    <a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &nbsp;·&nbsp;
    <a href="https://lifetogether.com">lifetogether.com</a> &nbsp;·&nbsp;
    25 Years · 500+ Church Relationships · 50M+ Campaigns Distributed
  </p>
  <div class="lm">Lifetogether</div>
</section>

</div>
</body>
</html>"""

with open('/mnt/user-data/outputs/lifetogether-flagship-sunday-playbook.html','w') as f:
    f.write(HTML)
print(f"Done — {len(HTML):,} chars")
