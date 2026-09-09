
import sys
sys.path.insert(0, '/tmp')
import catalytic_data as D
import html as hlib
def e(s): return hlib.escape(str(s))

# ── PALETTE: 20 accent colors ──
ACCS = ["#5070a0","#508060","#906060","#407070","#807040","#806080",
        "#507080","#507060","#607040","#508090","#906050","#608040",
        "#408070","#805060","#606090","#406080","#906040","#507090",
        "#705050","#508060"]
BGS  = ["#040810","#060a06","#080608","#04080a","#060608","#060408",
        "#04060a","#060a08","#060806","#04080c","#080606","#060a04",
        "#040a08","#080608","#040608","#06080a","#080604","#04060a",
        "#060806","#040a06"]

CSS = """
:root{--navy:#02040a;--gold:#c9a84c;--gold-lt:#e2c97e;--gold-dk:#8a6e30;
  --cream:#f8f5ef;--tl:#d4c9b8;--tm:#8a9ab5;--rule:rgba(201,168,76,0.10);--ink:#0e1520;}
*{margin:0;padding:0;box-sizing:border-box;}html{scroll-behavior:smooth;}
body{font-family:'Lato',sans-serif;background:#e0dbd3;color:var(--ink);}
.page{max-width:1180px;margin:0 auto;background:var(--cream);box-shadow:0 4px 80px rgba(0,0,0,.2);}
.cover{background:var(--navy);min-height:92vh;display:flex;flex-direction:column;
  justify-content:flex-end;padding:0;position:relative;overflow:hidden;}
.cover-glow{position:absolute;inset:0;background:
  radial-gradient(ellipse at 20% 70%,rgba(201,168,76,.07),transparent 50%),
  radial-gradient(ellipse at 80% 20%,rgba(80,100,160,.05),transparent 48%),
  linear-gradient(180deg,#010306,#02050c 70%,#030810);}
.cover-top{padding:48px 72px 0;position:relative;z-index:1;
  display:flex;justify-content:space-between;align-items:flex-start;}
.cover-logo{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;
  color:rgba(255,255,255,.4);letter-spacing:2px;}
.cover-tag{font-size:7.5px;letter-spacing:4px;text-transform:uppercase;font-weight:700;
  color:var(--gold-dk);border:1px solid rgba(201,168,76,.2);padding:5px 12px;}
.cover-body{padding:64px 72px 80px;position:relative;z-index:1;}
.cover-ey{font-size:8.5px;letter-spacing:5px;text-transform:uppercase;font-weight:700;
  color:rgba(90,128,112,.9);display:flex;align-items:center;gap:14px;margin-bottom:22px;}
.cover-ey::before{content:'';width:30px;height:1px;background:rgba(90,128,112,.7);}
.cover-h1{font-family:'Playfair Display',serif;font-size:clamp(44px,6.5vw,100px);
  font-weight:400;line-height:.88;color:#fff;letter-spacing:-2px;margin-bottom:22px;}
.cover-h1 em{font-style:italic;color:var(--gold);}
.cover-rule{display:flex;align-items:center;gap:14px;margin:24px 0;}
.cover-rule-line{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.cover-rule-dot{width:6px;height:6px;background:var(--gold);transform:rotate(45deg);flex-shrink:0;}
.cover-sub{font-family:'Playfair Display',serif;font-size:clamp(15px,2vw,22px);
  font-weight:300;font-style:italic;color:var(--tl);max-width:700px;line-height:1.6;margin-bottom:40px;}
.cover-stats{display:grid;grid-template-columns:repeat(5,1fr);gap:0;
  max-width:820px;border:1px solid rgba(201,168,76,.2);}
.cstat{padding:16px 18px;border-right:1px solid rgba(201,168,76,.15);text-align:center;}
.cstat:last-child{border-right:none;}
.cstat-n{font-family:'Playfair Display',serif;font-size:24px;color:var(--gold);display:block;line-height:1;}
.cstat-l{font-size:7px;letter-spacing:2.5px;text-transform:uppercase;color:rgba(255,255,255,.25);font-weight:700;display:block;margin-top:3px;}
/* TOC */
.toc{background:#04080e;padding:40px 72px;border-bottom:3px solid var(--gold);}
.toc-h2{font-family:'Playfair Display',serif;font-size:20px;font-style:italic;color:var(--gold);margin-bottom:18px;}
.toc-grid{display:grid;grid-template-columns:1fr 1fr;gap:3px 32px;}
.toc-item{display:flex;align-items:baseline;gap:7px;padding:4px 0;border-bottom:1px solid rgba(255,255,255,.04);}
.toc-num{font-family:'Playfair Display',serif;font-size:10px;color:var(--gold-dk);flex-shrink:0;min-width:20px;}
.toc-title{font-size:11.5px;color:var(--tl);}
.toc-title a{color:var(--tl);text-decoration:none;}
.toc-title a:hover{color:var(--gold);}
.toc-count{font-size:8.5px;color:rgba(255,255,255,.18);margin-left:auto;white-space:nowrap;padding-left:6px;}
/* SECTION INTRO */
.sect-intro{padding:40px 72px 16px;border-top:4px solid var(--gold);}
.si-kk{font-size:8px;letter-spacing:4px;text-transform:uppercase;font-weight:700;
  color:rgba(90,128,112,.8);display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.si-kk::before{content:'';width:18px;height:1px;background:rgba(90,128,112,.7);}
.si-h2{font-family:'Playfair Display',serif;font-size:clamp(24px,3.5vw,44px);
  font-weight:400;color:var(--ink);margin-bottom:8px;}
.si-h2 em{font-style:italic;color:var(--gold-dk);}
.si-sub{font-family:'Georgia',serif;font-size:14px;color:#555;line-height:1.75;max-width:780px;margin-bottom:8px;}
/* CAT HEADERS */
.cat-hdr{padding:28px 72px 10px;border-left:7px solid;}
.cat-ey{font-size:8px;letter-spacing:4px;text-transform:uppercase;font-weight:700;
  display:flex;align-items:center;gap:9px;margin-bottom:8px;}
.cat-nb{display:inline-flex;align-items:center;justify-content:center;
  width:24px;height:24px;border:1px solid currentColor;
  font-family:'Playfair Display',serif;font-size:10px;flex-shrink:0;}
.cat-name{font-family:'Playfair Display',serif;font-size:clamp(15px,2vw,26px);
  font-weight:400;color:var(--ink);line-height:1.0;margin-bottom:4px;}
.cat-why{font-family:'Georgia',serif;font-size:12.5px;color:#666;font-style:italic;line-height:1.5;max-width:760px;}
/* TITLE GRID */
.title-grid{padding:6px 72px 26px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px;}
.tc{padding:8px 12px;border:1px solid rgba(0,0,0,.06);background:rgba(255,255,255,.5);}
.tc.flagship{border-color:rgba(201,168,76,.5);background:linear-gradient(135deg,rgba(201,168,76,.09),rgba(201,168,76,.02));}
.tc.seasonal{border-color:rgba(80,120,170,.25);background:rgba(80,120,170,.03);}
.tc.crisis{border-color:rgba(160,80,80,.25);background:rgba(160,80,80,.02);}
.tc-top{display:flex;align-items:flex-start;gap:6px;margin-bottom:1px;}
.tc-num{font-family:'Playfair Display',serif;font-size:10px;color:rgba(138,110,48,.3);flex-shrink:0;padding-top:1px;}
.tc.flagship .tc-num{color:var(--gold-dk);font-size:12px;}
.tc-ti{font-family:'Playfair Display',serif;font-size:12px;font-style:italic;color:var(--ink);line-height:1.25;}
.tc.flagship .tc-ti{font-size:13.5px;color:#1a0e00;}
.tc-su{font-size:9px;color:#888;font-family:'Georgia',serif;font-style:italic;line-height:1.3;padding-left:18px;}
/* 7-DAY */
.seven{padding:52px 72px;background:#eee8e0;}
.sd-h2{font-family:'Playfair Display',serif;font-size:clamp(22px,3vw,40px);font-weight:400;color:var(--ink);margin-bottom:8px;}
.sd-h2 em{font-style:italic;color:var(--gold-dk);}
.sd-sub{font-family:'Georgia',serif;font-size:14.5px;color:#555;line-height:1.75;max-width:780px;margin-bottom:28px;}
.sd-days{display:flex;flex-direction:column;gap:0;}
.sd-day{display:grid;grid-template-columns:72px 1fr;gap:0;border-bottom:1px solid rgba(0,0,0,.07);}
.sd-dl{padding:18px 12px;background:var(--navy);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
.sd-dl.cel{background:rgba(201,168,76,.12);border-left:4px solid var(--gold);}
.sd-dn{font-family:'Playfair Display',serif;font-size:20px;color:var(--gold);display:block;line-height:1;}
.sd-dl.cel .sd-dn{color:var(--gold-dk);}
.sd-dname{font-size:7px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.35);font-weight:700;display:block;margin-top:3px;}
.sd-dl.cel .sd-dname{color:var(--gold-dk);}
.sd-db{padding:16px 22px;}
.sd-dt{font-family:'Playfair Display',serif;font-size:15px;font-style:italic;color:var(--ink);margin-bottom:7px;}
.sd-dt.cel{color:#5a3800;font-size:17px;}
.sd-els{display:flex;flex-direction:column;gap:6px;}
.sd-el{display:flex;gap:7px;align-items:flex-start;}
.el-lbl{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;font-weight:700;
  padding:2px 6px;flex-shrink:0;margin-top:1px;}
.el-lbl.s{background:rgba(80,120,170,.12);color:#5080b0;}
.el-lbl.q{background:rgba(201,168,76,.12);color:var(--gold-dk);}
.el-lbl.p{background:rgba(90,128,112,.1);color:#5a8060;}
.el-lbl.a{background:rgba(80,80,80,.08);color:#555;}
.el-lbl.st{background:rgba(160,80,120,.1);color:#a05070;}
.el-txt{font-family:'Georgia',serif;font-size:12.5px;color:#444;line-height:1.5;}
/* TOP 10 */
.top10{padding:52px 72px;background:var(--navy);}
.t10-h2{font-family:'Playfair Display',serif;font-size:clamp(20px,3vw,36px);font-weight:400;font-style:italic;color:#fff;margin-bottom:6px;}
.t10-sub{font-family:'Georgia',serif;font-size:13.5px;color:var(--tl);line-height:1.7;max-width:780px;margin-bottom:28px;}
.t10-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
.t10i{padding:18px 20px;border:1px solid var(--rule);background:rgba(255,255,255,.02);}
.t10i.gold{border-color:rgba(201,168,76,.3);background:rgba(201,168,76,.04);}
.t10n{font-family:'Playfair Display',serif;font-size:28px;color:rgba(201,168,76,.18);display:block;line-height:1;margin-bottom:4px;}
.t10i.gold .t10n{color:var(--gold);}
.t10title{font-family:'Playfair Display',serif;font-size:15px;font-style:italic;color:#fff;margin-bottom:4px;}
.t10why{font-family:'Georgia',serif;font-size:12px;color:var(--tl);line-height:1.5;}
.t10act{font-size:7.5px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;
  color:var(--gold-dk);display:block;margin-top:7px;padding-top:6px;border-top:1px solid var(--rule);}
/* NEXT STEPS 250 */
.nextsteps{padding:48px 72px;}
.ns-kk{font-size:8px;letter-spacing:4px;text-transform:uppercase;font-weight:700;
  color:rgba(90,128,112,.8);display:flex;align-items:center;gap:10px;margin-bottom:20px;}
.ns-kk::before{content:'';width:18px;height:1px;background:rgba(90,128,112,.7);}
.ns-h2{font-family:'Playfair Display',serif;font-size:clamp(22px,3vw,38px);
  font-weight:400;color:var(--ink);margin-bottom:8px;}
.ns-h2 em{font-style:italic;color:var(--gold-dk);}
.ns-sub{font-family:'Georgia',serif;font-size:14px;color:#555;line-height:1.7;max-width:780px;margin-bottom:36px;}
.ns-cat{margin-bottom:32px;}
.ns-cat-hdr{padding:12px 16px;margin-bottom:8px;border-left:5px solid;}
.ns-cat-title{font-family:'Playfair Display',serif;font-size:19px;font-style:italic;color:var(--ink);}
.ns-cat-why{font-family:'Georgia',serif;font-size:12px;color:#666;font-style:italic;margin-top:2px;}
.ns-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;}
.ns-item{padding:9px 12px;border:1px solid rgba(0,0,0,.07);background:rgba(255,255,255,.5);}
.ns-item.p{border-color:rgba(201,168,76,.35);background:rgba(201,168,76,.04);}
.ns-num{font-family:'Playfair Display',serif;font-size:9.5px;color:rgba(138,110,48,.3);display:block;margin-bottom:1px;}
.ns-item.p .ns-num{color:var(--gold-dk);}
.ns-title{font-family:'Playfair Display',serif;font-size:12px;font-style:italic;color:var(--ink);}
.ns-desc{font-family:'Georgia',serif;font-size:9.5px;color:#777;line-height:1.4;margin-top:2px;}
/* DIVIDERS */
.hdiv{height:3px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.25),transparent);}
.sdiv{height:1px;background:var(--rule);margin:0 72px;}
/* BACK */
.back{background:#010406;padding:52px 72px;text-align:center;}
.bq{font-family:'Playfair Display',serif;font-size:clamp(14px,2vw,20px);
  font-style:italic;color:var(--cream);max-width:780px;margin:0 auto 18px;line-height:1.55;}
.ba{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.bc{margin-top:14px;font-size:12px;color:var(--tm);}
.bc a{color:var(--gold-lt);text-decoration:none;}
.lm{font-family:'Playfair Display',serif;font-size:30px;color:#fff;font-style:italic;margin-top:24px;}
@media(max-width:960px){
  .cover-top,.cover-body,.toc,.cat-hdr,.title-grid,.seven,.top10,.nextsteps,.back,.sect-intro{padding-left:28px;padding-right:28px;}
  .title-grid{grid-template-columns:1fr 1fr;}
  .t10-grid,.ns-grid{grid-template-columns:1fr 1fr;}
  .cover-stats{grid-template-columns:repeat(3,1fr);}
  .toc-grid{grid-template-columns:1fr;}
  .sd-day{grid-template-columns:56px 1fr;}
}
@media(max-width:600px){
  .title-grid,.ns-grid{grid-template-columns:1fr;}
  .t10-grid{grid-template-columns:1fr;}
}
"""

def tc(rank, title, sub, cls_x):
    cls = f"tc {cls_x}".strip() if cls_x else "tc"
    r = "★" if rank == "★" else rank
    return f'<div class="{cls}"><div class="tc-top"><span class="tc-num">{e(r)}</span><span class="tc-ti">{e(title)}</span></div><p class="tc-su">{e(sub)}</p></div>'

def cat_section(cat_num, cat_name, cat_desc, titles, acc, bg):
    cards = "\n".join(tc(r,t,s,cls) for r,t,s,_,cls in titles)
    return f'''<section class="cat-hdr" id="cat{cat_num}" style="background:{bg};border-color:{acc};">
  <div class="cat-ey" style="color:{acc};">
    <span class="cat-nb" style="border-color:{acc};">{e(cat_num)}</span>
    {e(cat_name)}
  </div>
  <p class="cat-why">{e(cat_desc)}</p>
</section>
<section class="title-grid" style="background:{bg};">
{cards}
</section>
<div class="hdiv"></div>'''

# ── SEVEN-DAY STRUCTURE ──
SEVEN_DAYS = [
  ("1","Mon","Start Here — Sit With the Sermon",[
    ("s","The text the pastor preached",""),
    ("q","What one word, image, or moment from Sunday is still with you? Why did it stay?",""),
    ("p","God, I want to receive what Sunday offered. Slow me down enough to let it form me.",""),
    ("a","Write one sentence: the big idea of Sunday's message in your own words.",""),
    ("st","Think of one person the sermon brought to mind. What about them made that connection?",""),
  ],""),
  ("2","Tue","Go Deeper — The Text in Your Own Life",[
    ("s","Re-read the passage. Read it slowly. Read it twice.",""),
    ("q","Where does this text make you uncomfortable? Where does it feel like it was written for you specifically?",""),
    ("p","God, this part of the text is hard for me: ___. Help me not skip past it.",""),
    ("a","Write down one specific area of your life this text directly addresses.",""),
    ("st","Think of a time this truth was tested in your experience. What happened?",""),
  ],""),
  ("3","Wed","The Obstacle — What Is Keeping You From Living This",[
    ("s","Return to the big idea from Sunday.",""),
    ("q","What is the most honest reason you have not been living this truth? Fear? Habit? Doubt? Comfort?",""),
    ("p","God, I name this honestly: ___. This is what gets in the way. I need you to change this in me.",""),
    ("a","Name one specific thing that has to change for the Sunday message to become your life, not just your belief.",""),
    ("st","Think of someone who has overcome the obstacle you named. What do you know about how they did it?",""),
  ],""),
  ("4","Thu","The One Step — What Monday Looks Like",[
    ("s","Proverbs 4:18 — The path of the righteous is like the morning sun, shining ever brighter.",""),
    ("q","If you took one step toward living Sunday's message this week, what would that step look like? Be specific enough that you could explain it to a friend.",""),
    ("p","God, I am not asking for the whole arc. I am asking for the next step. Show me what it is and give me the courage to take it.",""),
    ("a","Write the step down. Name the day and time you will take it before next Sunday.",""),
    ("st","Think of the person in your life who most needs to see you take this step. Why them?",""),
  ],""),
  ("5","Fri","The Community — Who Walks This With You",[
    ("s","Ecclesiastes 4:9–10 — Two are better than one… If either of them falls down, one can help the other up.",""),
    ("q","Who in your community knows what God is forming in you through this series? Who should?",""),
    ("p","God, formation is not solo work. Show me who I am supposed to do this with. Give me the courage to tell them what is happening in me.",""),
    ("a","Send one message today — text, email, in person — to someone in your community. Tell them one thing from this week's formation.",""),
    ("st","Think of a moment when someone's honesty about their own formation journey changed yours. What did it give you?",""),
  ],""),
  ("6","Sat","The Story You Are Becoming",[
    ("s","Revelation 12:11 — They triumphed over him by the blood of the Lamb and by the word of their testimony.",""),
    ("q","What is the story this week is adding to your formation? If you wrote one paragraph about what God has been doing in you this week, what would it say?",""),
    ("p","God, I want my life to be a story worth telling — not because of my virtue but because of your faithfulness. Let this week be a chapter worth reading.",""),
    ("a","Write your formation paragraph. One hundred words. What happened this week, what you discovered, and what you are taking into next Sunday.",""),
    ("st","Prepare one story — two to three minutes — about something God did in you this week that you would be willing to share Sunday if asked.",""),
  ],""),
  ("7","Celebration Sunday","Celebration & Storytelling Sunday",[
    ("s","The same text the pastor preached seven days ago — read it again with fresh eyes.",""),
    ("q","What is different about how you read this text today versus seven days ago? What did the week add to what Sunday started?",""),
    ("p","God, thank you for what this week formed. I receive it. I offer it back to you and to the community gathered here today.",""),
    ("a","Come ready to celebrate. Come ready to hear what God did in others. Come ready to tell your story if invited.",""),
    ("st","Share one thing — one story, one discovery, one step taken — with someone in the congregation before the service ends.",""),
  ],"cel"),
]

def seven_day_section():
    days_html = []
    for num, name, title, els, cel in SEVEN_DAYS:
        cls = "cel" if cel else ""
        dt_cls = "cel" if cel else ""
        els_html = "\n".join(
            f'<div class="sd-el"><span class="el-lbl {k}">{label}</span><p class="el-txt">{e(v)}</p></div>'
            for k,v,_ in els
            for label in [{"s":"Scripture","q":"Question","p":"Prayer","a":"Action","st":"Story"}[k]]
        )
        days_html.append(f'''<div class="sd-day">
  <div class="sd-dl {cls}"><span class="sd-dn">{e(num)}</span><span class="sd-dname">{e(name)}</span></div>
  <div class="sd-db"><p class="sd-dt {dt_cls}">{e(title)}</p><div class="sd-els">{els_html}</div></div>
</div>''')
    return "\n".join(days_html)

# ── TOP 10 ──
TOP_10 = [
  ("01","The Communication Card","The physical or digital form that captures Sunday's response before the person leaves the building. Every application that is written down has a 3x higher completion rate than one that is only heard. The card must be simple: one checkbox, one line, one next step.","Give every person a card. Ask them to write one thing before they leave.","gold"),
  ("02","The 7-Day Challenge","The Mon–Sat daily devotional that extends the Sunday sermon through the week, closing with Celebration Sunday. Not a Bible study. Not homework. Five to ten minutes per day that keeps the sermon alive Monday through Saturday.","Announce the 7-day challenge from the pulpit. Distribute the guide at the door.",""),
  ("03","The Small Group Launch","Every Catalytic Sunday is an invitation to move from the crowd into the community. The group signup that opens at the end of the service captures the formation momentum before it cools.","Have signup sheets, a QR code, or a text-to-join in the bulletin. Make it one action.","gold"),
  ("04","The One Specific Action","The most common failure of American preaching is the application that is too general to act on. The Catalytic Sunday next step must be specific enough that a person can do it or not do it before Wednesday. Not 'be more generous.' Identify one person in financial difficulty and do one specific thing for them by Friday.","State the action. Name the day it should be done. Give them something to write it on.",""),
  ("05","The Public Commitment","When the congregation stands, raises a hand, comes forward, writes it on a card, or says it aloud together, they form the behavior they are committing to before they act on it. The public declaration is not manipulation — it is formation.","Design the commitment moment before you design the sermon. Know how Sunday ends before you write how it begins.","gold"),
  ("06","The Prayer Partner Pairing","Two minutes at the end of the service. Turn to the person next to you. Share one sentence about what you are taking from today. Pray for each other. The relationship formed in two minutes has a higher retention rate than any program.","Instruct the congregation specifically. 'Turn to someone near you. Not your spouse. Share one thing. Pray twenty seconds.'",""),
  ("07","The Pastoral Follow-Up","The communication card captures who responded. The Formation Tracker identifies who responded with conviction versus confusion. The pastoral follow-up that happens Tuesday reaches the people Sunday moved while the movement is still fresh.","Every card reviewed by Tuesday. Every 'I need pastoral follow-up' card contacted before Wednesday.","gold"),
  ("08","The Formation Tracker","The data layer that tells the pastor what worked, what produced conviction, what produced confusion, and who responded to what. Without the tracker, the pastor can only improve intuitively. With it, they improve systematically.","After every Catalytic Sunday, record attendance pattern, response card numbers, small group signups, and one observation about what moment produced the most visible response.",""),
  ("09","The Testimony Sunday","The most powerful next step from any Catalytic Sunday is the Sunday three to four weeks later when three people in the congregation share what happened to them. Not polished. Not produced. Honest. Three minutes each.","Schedule the testimony Sunday before the Catalytic Sunday. Ask three people in advance. Coach them on the format: what was, what happened, what is different.","gold"),
  ("10","The Formation Arc Connection","Every Catalytic Sunday is the beginning of something, not the end. The sermon that moves people and offers them nothing to do next has wasted the movement it created. The Catalytic Sunday that connects to a 7-day journey, a 6-week series, a small group study, or a 40-day campaign converts the catalytic moment into a formation arc.","Before every Catalytic Sunday, name the formation next step in the bulletin, from the pulpit, and in the communication card.",""),
]

def top10_section():
    items = []
    for n,title,why,action,cls in TOP_10:
        items.append(f'''<div class="t10i {cls}">
  <span class="t10n">{e(n)}</span>
  <p class="t10title">{e(title)}</p>
  <p class="t10why">{e(why)}</p>
  <span class="t10act">{e(action)}</span>
</div>''')
    return "\n".join(items)

# ── 250 NEXT STEPS ──
NS_ACCS = ["#5070a0","#508060","#806060","#407070","#807040","#806080","#507080","#507060","#607040","#508090"]

NS_CATS = [
  ("Personal Formation Next Steps","The individual practices that extend Sunday into the week.",
   ["Write one sentence summary of Sunday's big idea before leaving the building","Read the sermon text in three different translations this week","Complete the 7-Day Challenge — five to ten minutes per day Mon-Sat","Journal for ten minutes each morning about one aspect of Sunday's message","Memorize the key verse from Sunday's text before next week","Listen to the sermon audio on your commute this week","Share Sunday's big idea with one person before Wednesday","Identify one belief the sermon challenged — sit with the tension for three days","Write the specific action you are committing to and the day you will do it","Take a thirty-minute walk this week and pray through Sunday's message","Read one chapter of a book related to Sunday's topic this week","Complete the personal study guide that comes with the sermon","Do a personal audit: how does this topic show up in my daily choices","Write a letter to yourself about what you want to be true in this area six months from now","Fast for one meal this week in connection with Sunday's theme","Practice one spiritual discipline connected to Sunday's message for the full week","Identify the one relationship this sermon most directly affects","Tell your story — write the paragraph about your own formation journey in this area","Spend one hour in silence this week in reflection on Sunday's message","Take one action that costs you something in connection with Sunday's theme","Find one person who has lived what Sunday preached and ask them one question","Read the full chapter that Sunday's verse came from","Identify one practical change to your routine that aligns with Sunday's message","Listen to one message or read one article that goes deeper on Sunday's topic","Begin Sunday's formation practice today — not next week",""],
  ),
  ("Small Group Next Steps","Community practices that bring Sunday into Thursday.",
   ["Sign up for a small group before leaving the building today","Invite one friend to join your group this week","Use Sunday's message as the discussion guide for this Thursday's group","Text your small group leader and tell them one thing from Sunday you want to discuss","Ask your group: where in my life do you see this sermon's topic playing out","Begin a new six-week study connected to Sunday's series","Share one personal application from Sunday with your group before Thursday","Schedule a group prayer time this week focused on Sunday's theme","Have each group member complete the 7-Day Challenge and debrief together Saturday","Identify one person in your group who is living Sunday's message well — honor them","Have each group member share their formation paragraph at the next meeting","Use the communication card's group discussion question as Thursday's opening","Commit to a group fast connected to Sunday's generosity message","Study the same passage together — each member from a different commentary perspective","Have the group identify one communal action they will take before next Sunday","Invite a new attender from Sunday to join your group this week","Schedule a group celebration for what God has done in the last series","Begin the 40-day campaign that follows this Sunday's series with your group","Have each group member write their testimony on this topic — share at next meeting","Plan a group service project connected to Sunday's justice theme","Study one related passage together that Sunday's sermon did not have time to reach","Identify the group member who most needs support in this area and rally around them","Have each person bring a story next week of where they saw Sunday's message in real life","Commit to a group year of formation — define what you will study together through December","Have the group pray for one person outside the group who needs to hear Sunday's message",""],
  ),
  ("Family & Home Next Steps","Formation practices that take Sunday home.",
   ["Have a family dinner conversation about Sunday's big idea this week","Read the key verse together at dinner every night this week","Ask your children what they remember from children's church this Sunday","Do the 7-Day family devotional together — five minutes each morning","Write Sunday's application on a sticky note and put it somewhere the family sees it","Pray together as a family about one thing Sunday named","Have each family member answer: what is the one thing you are going to do differently this week","Read a picture book or chapter book connected to Sunday's theme with your children","Tell a family story that illustrates Sunday's message — something from your history","Write a family mission statement based on the value Sunday preached","Have a family meeting to discuss Sunday's topic — even if it is uncomfortable","Take a family service action this week connected to Sunday's justice or generosity theme","Put Sunday's key verse on the refrigerator for the week","Each family member writes one commitment in response to Sunday — share at dinner","Plan a family experience that embodies Sunday's message — hospitality, service, rest","Ask the grandparents what they think about Sunday's topic — start a multigenerational conversation","Share Sunday's sermon with an extended family member who was not there","Create a family gratitude ritual connected to Sunday's Thanksgiving theme","Have each family member pray for one person they know who needs to hear Sunday's message","Watch a film this week that connects to Sunday's topic — discuss it together","Spend one hour this week in a formation practice as a family — prayer, service, reading","Write a family lament connected to Sunday's grief or justice theme","Have the children create something — a drawing, a prayer — in response to Sunday's message","Establish one new family rhythm this week that embodies Sunday's formation theme","Identify the one thing in your family culture that Sunday directly challenged",""],
  ),
  ("Church Community Next Steps","Collective actions the congregation takes together.",
   ["Sign the congregation-wide covenant displayed in the lobby","Join the congregation's text-to-commit campaign before leaving the parking lot","Volunteer for one hour with the community initiative launched from today's message","Attend the follow-up event announced from the pulpit today","Register for the congregation's formation class that starts this week","Sponsor one person in the congregation who needs help with this week's application","Participate in the congregation-wide fast announced for Wednesday","Join the prayer team that is praying through Sunday's theme all week","Welcome a first-time attender and share one thing from Sunday's message with them","Attend the all-church service project announced from the pulpit","Participate in the congregation-wide reading plan that accompanies this series","Sign up to serve in the ministry that Sunday's outreach message introduced","Attend the testimony service scheduled for three Sundays from now","Participate in the offering campaign launched by Sunday's stewardship message","Invite someone to next Sunday — the specific someone Sunday's message made you think of","Sign the reconciliation covenant introduced in Sunday's justice message","Participate in the church-wide prayer vigil scheduled for this week","Join the small group that is forming around Sunday's specific topic","Bring something to next Sunday's celebration service — a testimony, an offering, a story","Participate in the community meal that follows Sunday's hospitality message","Sign up to mentor someone in the area Sunday's message addressed","Attend the Q&A session with the pastor scheduled for Wednesday evening","Submit a testimony card about how Sunday's topic has affected your life this week","Join the working group forming to address the community need Sunday named","Commit to attending every Sunday of this series — not just today",""],
  ),
  ("Generosity & Stewardship Next Steps","Financial and material formation practices.",
   ["Fill out the pledge card before leaving today","Set up automatic giving before Sunday evening","Increase your giving by one percent this week","Give your first fruits this week — give before any other expense","Identify one person in financial difficulty and do one specific thing for them by Friday","Make a legacy gift decision — complete the estate planning form the church has available","Write a check to a Kingdom organization you have been meaning to support","Complete the financial audit the stewardship message invited you to do this week","Have the financial conversation with your spouse that Sunday's message made necessary","Meet with a Christian financial advisor this week about your generosity goals","Commit to the giving campaign with a specific amount and a specific duration","Give anonymously to someone in the congregation who has a need you know about","Tithe on a bonus, inheritance, or unexpected income you have been holding","Review your budget tonight and identify what Sunday's message changes","Give sacrificially — the gift that you feel in your budget, not just the gift that does not","Write a generosity plan for the calendar year — total giving, recipients, and rationale","Fund one specific Kingdom project in full this week","Commit to teaching your children about tithing this week with a physical illustration","Begin the debt elimination plan Sunday's financial freedom message described","Give your time — volunteer ten hours this month in the area Sunday's sermon addressed","Reduce one expense this week and give the savings","Contact the estate attorney about the charitable bequest you have been considering","Start the emergency fund Sunday's financial formation message recommended","Join the financial accountability group that is forming this week","Write a letter to your future self about what generous living looks like for you in ten years",""],
  ),
  ("Mission & Outreach Next Steps","Sending practices that take Sunday into the community.",
   ["Pray for one person by name who does not yet know Jesus — do it before you leave the parking lot","Write the name of the person you are going to tell your story to this week","Walk across the room — literally — and introduce yourself to someone you do not know","Sign up for the neighborhood outreach event announced from the pulpit","Bring a friend to church next Sunday — the specific friend Sunday's message made you think of","Write your personal testimony in three hundred words — practice saying it aloud","Volunteer for one shift at the community organization Sunday's mercy message described","Begin the friendship with the neighbor you have been meaning to know","Join the team going on the international mission trip announced today","Sponsor a child through the mission organization Sunday's global message highlighted","Participate in the church's community prayer walk this week","Sign up to serve at the food bank, shelter, or school the church partners with","Send a card or text to one person this week that shares what God has been doing in you","Make a meal for someone outside the congregation who could use it","Have the gospel conversation you have been avoiding — this week, with this person","Volunteer as a mentor in the at-risk youth program Sunday's justice message described","Participate in the neighborhood clean-up event the church is organizing","Donate to the disaster relief campaign Sunday's crisis response message announced","Begin learning the language of the immigrant community in your city","Visit someone in prison, a nursing home, or a hospital this week — go as the church","Support the church plant that Sunday's planting message described — financially or prayerfully","Share Sunday's message on social media with one sentence about why it mattered to you","Write a letter to your local elected representative about the issue Sunday's civic message addressed","Partner with the adjacent congregation for one joint service project this month","Identify and pursue the specific mission field Sunday's message named as yours",""],
  ),
  ("Leadership Development Next Steps","Formation practices for leaders and future leaders.",
   ["Identify one leader in your congregation and thank them specifically before next Sunday","Sign up for the elder formation class that begins this week","Volunteer to lead a small group in the series that launches from today's message","Mentor one person this week in the area Sunday's leadership message addressed","Read one leadership book connected to Sunday's topic before the end of this series","Attend the staff formation meeting that follows this Catalytic Sunday","Identify the next leader in your organization and take one step toward investing in them","Complete the leadership assessment the church is offering following Sunday's vision message","Share Sunday's leadership message with your work team and facilitate a ten-minute discussion","Sign up for the leadership cohort that is forming out of today's message","Begin the specific leadership behavior Sunday's message named as your next growth edge","Invite a younger leader to shadow you in your work this week","Have the hard leadership conversation you have been avoiding — this week","Establish the leadership accountability relationship Sunday's governance message invited","Submit your name for consideration for the deacon election announced today","Read the board governance resource announced in connection with Sunday's leadership theme","Attend the leadership retreat being announced today and commit before you leave","Identify one way your leadership this week will look different because of Sunday's message","Begin the practice of weekly leadership reflection — fifteen minutes every Friday","Join the peer advisory group forming out of Sunday's leadership formation series","Write the leadership development plan for the person you are mentoring","Have the succession conversation with the person who needs to hear it","Attend the community leader prayer breakfast being organized from today's message","Identify the one leadership gift Sunday's message revealed in you that you have been underusing","Commit to one year of intentional leadership formation — name the specific arc",""],
  ),
  ("Healing & Recovery Next Steps","Formation practices for the congregation navigating healing.",
   ["Call or text a counselor, pastor, or trusted friend today about what Sunday named","Attend the first meeting of the recovery group that meets this Thursday","Tell one person in your life what Sunday's message surfaced in you — today","Complete the mental health resource the church has made available this week","Schedule an appointment with a Christian counselor before this week ends","Begin the recovery program the church's healing ministry offers","Sign up for the grief group that begins this week","Tell your small group leader that you are struggling in the area Sunday addressed","Reach out to the pastoral care team using the contact information in today's bulletin","Begin the healing prayer practice that Sunday's anointing message described","Attend the mental health awareness event the church is hosting this week","Make an appointment with your doctor about the physical health issue Sunday's wellness message prompted","Tell your sponsor what happened in you during Sunday's message","Complete the personal inventory Sunday's recovery message invited you to do this week","Join the support group that is forming out of Sunday's specific healing topic","Begin the daily practice that Sunday's wholeness message described — this morning","Reach out to the person in your congregation who you know is also struggling in this area","Attend the Saturday healing prayer service announced from the pulpit","Begin the addiction recovery step Sunday's message described — do not wait for Monday","Write a letter to the younger version of yourself about what Sunday's healing message offers","Tell your accountability partner what you discovered in Sunday's message","Begin the trauma-informed formation program the church is offering","Make the call you have been putting off — the one person Sunday made you think of","Attend the family counseling session the church has made available","Name the wound Sunday's message identified and tell one person its name today",""],
  ),
  ("Prayer & Spiritual Discipline Next Steps","Formation practices that build the interior life.",
   ["Begin a prayer journal today with Sunday's text as the first entry","Spend thirty minutes in silent prayer before Monday morning — no phone","Pray the Lord's Prayer slowly and completely every day this week","Begin a daily quiet time — ten minutes every morning — connected to Sunday's series","Fast from one meal or one screen practice this week in connection with Sunday's theme","Write out your prayer for the person Sunday's message brought to mind","Pray specifically for the three things Sunday's intercession message named","Begin a prayer practice from the contemplative tradition Sunday described","Join the church's intercessory prayer team that meets this week","Pray through the psalm Sunday's message was rooted in — slowly, out loud","Set a daily alarm this week that reminds you to stop and pray Sunday's theme","Begin a practice of praying for your enemies — the specific practice Sunday's forgiveness message described","Attend the church's prayer meeting this week — the one you have been meaning to attend","Practice the examen — the daily prayer of review — every evening this week","Begin praying the Bible — take Sunday's text and turn each verse into a prayer","Set up a prayer partner relationship with someone in the congregation — text your first prayer today","Complete the prayer guide that accompanies this week's 7-Day Challenge","Practice Sabbath prayer — one hour on Saturday of unhurried conversation with God","Pray for the city — specifically, geographically, by name — as Sunday's civic message invited","Begin a gratitude prayer practice — three specific thanks before sleep every night this week","Pray the congregation's covenant prayer together as a family this week","Participate in the church's forty-day prayer campaign that begins with this Sunday","Pray for the pastor — specifically, by name, for the burden Sunday's message carried","Begin a prayer rhythm that aligns with the five purposes Sunday's discipleship message described","Spend time in nature this week in prayerful attention to the Creator Sunday's creation message described",""],
  ),
  ("Justice & Cultural Engagement Next Steps","Formation practices for engaging the world the congregation inhabits.",
   ["Write a letter to your elected representative about the issue Sunday's justice message named","Volunteer this week with the organization serving the community need Sunday identified","Make a financial gift to the justice organization Sunday's mercy message highlighted","Have a conversation with someone from a different political or cultural background — listen more than talk","Register to vote if you are not registered — complete the process before this week ends","Attend a city council or school board meeting this month","Read one book by an author whose background differs from yours — on Sunday's topic","Follow three voices on social media that represent perspectives different from yours","Identify the one civic engagement step Sunday's message called you to and take it before Wednesday","Join the advocacy organization the church has partnered with for Sunday's issue","Attend the interracial dialogue group forming from Sunday's reconciliation message","Sign the community petition the church is supporting in connection with Sunday's justice theme","Sponsor one child, refugee family, or justice initiative with a recurring monthly gift","Walk through the neighborhood most affected by the issue Sunday named — go slowly","Meet the person from the different culture, class, or background Sunday's message described — this week","Begin learning about the policy issue Sunday's civic message described — read one credible source","Participate in the restorative justice program Sunday's criminal justice message highlighted","Attend the community meeting being organized around the local issue Sunday named","Write your personal statement about Sunday's justice theme — where you stand and what you will do","Begin the racial formation reading plan the church is offering following Sunday's reconciliation message","Engage the community organization Sunday described — attend one meeting or volunteer one time","Make one structural change in your life that reduces your contribution to the systemic issue Sunday named","Support the local business, school, or organization that serves the community Sunday's message cared about","Participate in the voter registration drive the church is organizing","Commit to one year of intentional justice formation — name the specific arc Sunday offered",""],
  ),
]

def nextsteps_section():
    cats_html = []
    for i,(cat_title, cat_why, items) in enumerate(NS_CATS):
        acc = NS_ACCS[i % len(NS_ACCS)]
        cards = []
        for j, item in enumerate(items):
            if not item: continue
            cls = "p" if j == 0 else ""
            cards.append(f'<div class="ns-item {cls}"><span class="ns-num">{j+1}</span><p class="ns-title">{e(item)}</p></div>')
        cats_html.append(f'''<div class="ns-cat">
  <div class="ns-cat-hdr" style="border-color:{acc};background:rgba(0,0,0,.02);">
    <p class="ns-cat-title">{e(cat_title)}</p>
    <p class="ns-cat-why">{e(cat_why)}</p>
  </div>
  <div class="ns-grid">{"".join(cards)}</div>
</div>''')
    return "\n".join(cats_html)

# ── ASSEMBLE HTML ──
total = sum(len(c[3]) for c in D.CATEGORIES)

toc_items = "".join(
  f'<div class="toc-item"><span class="toc-num">{e(c[0])}</span><span class="toc-title"><a href="#cat{c[0]}">{e(c[1])}</a></span><span class="toc-count">50 titles</span></div>'
  for c in D.CATEGORIES
)

cats_html = "\n".join(
  cat_section(c[0],c[1],c[2],c[3],ACCS[i%len(ACCS)],BGS[i%len(BGS)])
  for i,c in enumerate(D.CATEGORIES)
)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Catalytic Sundays — The Complete Library · Lifetogether</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="page">

<section class="cover">
  <div class="cover-glow"></div>
  <div class="cover-top">
    <span class="cover-logo">Lifetogether</span>
    <span class="cover-tag">Complete Library · 2026 Edition</span>
  </div>
  <div class="cover-body">
    <p class="cover-ey">The Complete Catalytic Sunday System — Titles · Next Steps · 7-Day Framework</p>
    <h1 class="cover-h1">Catalytic<br><em>Sundays.</em><br>All of Them.</h1>
    <div class="cover-rule"><div class="cover-rule-dot"></div><div class="cover-rule-line"></div></div>
    <p class="cover-sub">{total} standalone sermon titles across 20 categories — every timely, topical, transitional, and crisis Sunday a pastor will ever face — plus the 10 timeless next steps for any Catalytic Sunday, the 7-Day Sermon Devotional framework, and 250 curated formation next steps by category.</p>
    <div class="cover-stats">
      <div class="cstat"><span class="cstat-n">{total}</span><span class="cstat-l">Sermon Titles</span></div>
      <div class="cstat"><span class="cstat-n">20</span><span class="cstat-l">Categories</span></div>
      <div class="cstat"><span class="cstat-n">10</span><span class="cstat-l">Timeless Next Steps</span></div>
      <div class="cstat"><span class="cstat-n">7</span><span class="cstat-l">Day Framework</span></div>
      <div class="cstat"><span class="cstat-n">250</span><span class="cstat-l">Curated Next Steps</span></div>
    </div>
  </div>
</section>

<section class="toc">
  <h2 class="toc-h2">Table of Contents</h2>
  <div class="toc-grid">{toc_items}</div>
</section>
<div class="hdiv"></div>

<section class="sect-intro">
  <p class="si-kk">Part One · The Complete Title Library</p>
  <h2 class="si-h2"><em>1,000 Catalytic Sunday Titles</em> Across 20 Categories</h2>
  <p class="si-sub">Every Catalytic Sunday is one of six types: an Unplanned Crisis, a Planned Transition, a Personal Milestone, a Seasonal Anchor, a Cultural Response, or a Ministry Launch. Every title below is organized by occasion, not just topic — so the pastor who knows what kind of Sunday they are facing can find exactly what they need. Flagship titles (★) are the highest-priority sermon in each category. Seasonal titles reflect planned-calendar moments. Crisis titles are for the Sundays that were not on the calendar.</p>
</section>

{cats_html}

<!-- THE 7-DAY SECTION -->
<section class="seven" id="seven-day">
  <p class="si-kk" style="padding:0;border:none;">Part Two · The Formation Framework</p>
  <h2 class="sd-h2">The Classic<br><em>7-Day Sermon</em><br>Devotional</h2>
  <p class="sd-sub">This framework works with any Catalytic Sunday sermon on any topic. It takes the inspiration of Sunday and moves the congregation through six days of transformation — ending with a Celebration Sunday that closes the loop through shared story and communal testimony. Each day has a Scripture anchor, an open-ended formation question, a prayer, a specific action, and a story prompt that prepares the congregation to tell what happened to them. The questions are open-ended by design: the answers come from the person's own life, not from a study guide. The celebration on Day 7 is not a closing — it is a commissioning.</p>
  <div class="sd-days">{seven_day_section()}</div>
</section>
<div class="hdiv"></div>

<!-- TOP 10 -->
<section class="top10" id="top10">
  <p class="si-kk" style="padding:0;border:none;color:rgba(90,128,112,.7);">Part Three · The Universal System</p>
  <h2 class="t10-h2">The Top 10 Timeless Next Steps<br>for <em>Any</em> Catalytic Sunday</h2>
  <p class="t10-sub">These ten next steps work after any Catalytic Sunday regardless of topic, occasion, or crisis type. The pastor who builds these ten into their formation system has a response infrastructure for every significant Sunday — planned or unplanned — that their congregation will ever experience. The specific content changes. The system stays the same.</p>
  <div class="t10-grid">{top10_section()}</div>
</section>
<div class="hdiv"></div>

<!-- 250 NEXT STEPS -->
<section class="nextsteps" id="nextsteps">
  <p class="ns-kk">Part Four · The Complete Next Step Library</p>
  <h2 class="ns-h2">250 <em>Formation Next Steps</em><br>by Category</h2>
  <p class="ns-sub">Every Catalytic Sunday creates appetite. These 250 next steps give the congregation something specific to do with that appetite — organized by where the application lands in their life. The first item in every category is the highest-priority, most universally applicable step for that category. The rest are calibrated for different congregational contexts, seasons, and levels of formation readiness.</p>
  {nextsteps_section()}
</section>
<div class="hdiv"></div>

<section class="back">
  <p class="bq">"Every Catalytic Sunday is a formation opportunity that lasts exactly as long as the next step waiting for the person who walks out the door. The sermon that moves people and offers them nothing to do next has wasted the movement it created. This library exists so that every Sunday — planned, unplanned, crisis, or celebration — has a formation arc waiting to receive what the sermon started."</p>
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

with open('/mnt/user-data/outputs/lifetogether-catalytic-1000.html','w') as f:
    f.write(HTML)
print(f"Done — {len(HTML):,} chars · {total} titles")
