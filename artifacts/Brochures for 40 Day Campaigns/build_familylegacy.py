# -*- coding: utf-8 -*-
import pathlib
from brochure_template import FONTS, CSS, campaign_page

campaigns = [
{
 "num":"01","accent":"#7a5a2e","accent_soft":"#ecddc6",
 "title_a":"Family","title_b":"Legacy",
 "subtitle":"The inheritance that matters more than anything in your will",
 "problem":"When most of us think about what we\u2019ll leave our children, we think about money, property, the contents of a will. But the inheritance that shapes a family for generations isn\u2019t financial at all \u2014 it\u2019s the faith, the stories, the character, and the values we pass down. And unlike money, that legacy is built on purpose, or not at all.",
 "promise":"Family Legacy helps your people leave what lasts. Over forty days they\u2019ll get intentional about the spiritual inheritance they\u2019re passing to their children and grandchildren \u2014 telling the next generation the goodness of God \u2014 so that long after the estate is settled, the truest part of their legacy lives on.",
 "verse":"We will tell the next generation the praiseworthy deeds of the Lord.",
 "ref":"Psalm 78:4 (NIV)",
 "bigidea":"The most valuable thing you\u2019ll ever pass down won\u2019t appear in your will. It\u2019s the faith, character, and stories you hand your children \u2014 the inheritance that actually shapes a life.",
 "tags":["Inheritance","Faith","Family","Values","Legacy"],
 "best_for":"Church &amp; Company","backbone":"Psalm 78:1\u20137; Proverbs 13:22","metaphor":"Telling the Next Generation","felt":"Spiritual legacy, what you leave your family",
 "sessions":[
   ("1","More Than a Will","The inheritance that money could never cover."),
   ("2","What You\u2019re Really Leaving","Taking honest stock of your spiritual legacy."),
   ("3","Telling the Story","Passing on the goodness of God to your children."),
   ("4","Character Over Cash","Why who you are outlasts what you leave."),
   ("5","Intentional, Not Accidental","Building a legacy on purpose."),
   ("6","A Legacy of Faith","Leaving what will still matter in a hundred years."),
 ],
 "journey":"Each of the 40 days captures one piece of your spiritual legacy \u2014 a story, a value, a lesson of faith \u2014 to pass on intentionally, with a partner check-in and a prayer.",
 "why":"Estates get spent and forgotten. But the faith and character you pass down can shape your family for generations. That legacy is built now, on purpose.",
 "cta":"Launch Family Legacy and help your people leave the inheritance that lasts.",
 "note":None,
},
{
 "num":"02","accent":"#34507e","accent_soft":"#d8e0ee",
 "title_a":"Leaving a","title_b":"Lasting Legacy",
 "subtitle":"Building a life whose impact endures long after you\u2019re gone",
 "problem":"Most legacies fade faster than we\u2019d like to admit \u2014 a name half-remembered, accomplishments forgotten within a generation or two. We pour our lives into things that don\u2019t outlast us, and quietly fear that when we\u2019re gone, little will remain. But a life anchored in the right things leaves a mark that genuinely endures.",
 "promise":"Leaving a Lasting Legacy lifts your people\u2019s eyes to the long view. Over forty days they\u2019ll learn to build a life and a family legacy that doesn\u2019t fade \u2014 the kind that blesses children\u2019s children, finishes well, and is remembered for what truly matters long after they\u2019re gone.",
 "verse":"Surely the righteous will never be shaken; they will be remembered forever.",
 "ref":"Psalm 112:6 (NIV)",
 "bigidea":"Almost everything you build will be forgotten. But a life rooted in righteousness leaves a legacy that endures \u2014 remembered, fruitful, and blessing generations you\u2019ll never meet.",
 "tags":["The Long View","Endurance","Finishing Well","Remembered","Legacy"],
 "best_for":"Church &amp; Company","backbone":"Psalm 112; 2 Timothy 4:7","metaphor":"Remembered Forever","felt":"Lasting legacy, endurance, finishing well",
 "sessions":[
   ("1","The Legacies That Fade","Why most of what we build doesn\u2019t last."),
   ("2","Remembered Forever","The kind of life Scripture says endures."),
   ("3","Rooted in the Right Things","Building on a foundation that holds."),
   ("4","Blessing Generations","A legacy that reaches children\u2019s children."),
   ("5","Finishing Well","Ending the story the way it should be told."),
   ("6","A Lasting Mark","Living now for what will still stand later."),
 ],
 "journey":"Each of the 40 days connects one present choice to its long-term legacy and takes one step toward building what lasts, with a partner check-in and a prayer.",
 "why":"The question isn\u2019t whether you\u2019ll leave a legacy \u2014 you will. It\u2019s whether you\u2019re building one that fades or one that lasts. The difference is decided now.",
 "cta":"Launch Leaving a Lasting Legacy and help your people build what endures.",
 "note":None,
},
{
 "num":"03","accent":"#b8902f","accent_soft":"#f1e8cd",
 "title_a":"","title_b":"Generations",
 "subtitle":"Receiving the faith handed to you, and passing it on",
 "problem":"Faith was always meant to travel through families \u2014 handed from one generation to the next like a lit candle. But somewhere the chain often breaks: a generation that received much passes on little, and the faith that was alive in grandparents grows faint by the time it reaches the grandchildren. We rarely see ourselves as a crucial link in that chain.",
 "promise":"Generations helps your people take their place in the line. Over forty days they\u2019ll honor the faith handed to them, recognize their role as a vital link between past and future, and learn to pass on \u2014 strengthened, not weakened \u2014 the living faith that once lived in a Lois and a Eunice and now lives in them.",
 "verse":"\u2026your sincere faith, which first lived in your grandmother Lois and in your mother Eunice.",
 "ref":"2 Timothy 1:5 (NIV)",
 "bigidea":"You are a link in a chain of faith that stretches back generations and reaches forward into ones you\u2019ll never see. The chain is only as strong as the link you choose to be.",
 "tags":["Generations","The Chain of Faith","Heritage","Honoring the Past","Legacy"],
 "best_for":"Church &amp; Company","backbone":"2 Timothy 1:5; Psalm 145:4","metaphor":"Lois, Eunice, and Timothy","felt":"Generational faith, the chain of generations",
 "sessions":[
   ("1","A Chain of Faith","How faith was designed to move through families."),
   ("2","Lois, Eunice, and Timothy","Three generations and a faith handed down."),
   ("3","Honoring What You Received","Giving thanks for the faith passed to you."),
   ("4","The Link You\u2019ll Be","Recognizing your place between past and future."),
   ("5","Breaking and Building","Ending unhealthy patterns, starting godly ones."),
   ("6","Passing It On","Handing the faith forward, stronger than you found it."),
 ],
 "journey":"Each of the 40 days honors one part of the faith handed to you and takes one step to pass it forward, with a partner check-in and a prayer.",
 "why":"Every family\u2019s faith is one generation from fading. Help your people become the strong link that keeps the candle lit for those who come after.",
 "cta":"Launch Generations and help your people strengthen the chain of faith.",
 "note":None,
},
{
 "num":"04","accent":"#2f6b4f","accent_soft":"#d8e8df",
 "title_a":"Faith for","title_b":"Generations",
 "subtitle":"Passing living faith to your children, woven into everyday life",
 "problem":"Many parents and grandparents deeply want their children to know God \u2014 and quietly assume it will simply happen, that faith will rub off through church attendance and good intentions. But faith is rarely caught by accident. Without intentional, everyday transmission, the most precious thing we have to give can fail to reach the very people we love most.",
 "promise":"Faith for Generations equips your people to pass faith on with intention. Over forty days they\u2019ll learn the ancient pattern of weaving faith into the ordinary fabric of family life \u2014 impressing it on their children as they sit at home and walk along the road \u2014 so that living faith actually reaches the next generation.",
 "verse":"Impress them on your children. Talk about them when you sit at home and when you walk along the road.",
 "ref":"Deuteronomy 6:7 (NIV)",
 "bigidea":"Faith is rarely caught by accident. It\u2019s passed on by parents and grandparents intentional enough to weave it into the ordinary moments of everyday family life.",
 "tags":["Spiritual Parenting","Discipleship","Children","Everyday Faith","Transmission"],
 "best_for":"Church &amp; Company","backbone":"Deuteronomy 6:4\u20139; Psalm 78:5\u20136","metaphor":"Impress Them on Your Children","felt":"Passing faith to kids, spiritual parenting",
 "sessions":[
   ("1","Caught, Not Assumed","Why faith rarely transmits by accident."),
   ("2","Impress Them","The intentional work of passing faith on."),
   ("3","As You Walk Along the Road","Weaving faith into ordinary moments."),
   ("4","The Family Altar","Simple rhythms that pass faith down."),
   ("5","When Faith Gets Hard","Staying faithful through doubt and distance."),
   ("6","Faith That Reaches Them","Making sure the next generation knows God."),
 ],
 "journey":"Each of the 40 days offers one simple, everyday way to pass faith to a child or grandchild \u2014 a conversation, a habit, a prayer \u2014 with a partner check-in and a prayer.",
 "why":"The faith we assume will pass on its own often doesn\u2019t. Give your people the tools to transmit it intentionally, and watch it reach the children they love.",
 "cta":"Launch Faith for Generations and help your people pass faith to their children.",
 "note":None,
},
{
 "num":"05","accent":"#2d6a7a","accent_soft":"#d6e7ec",
 "title_a":"Family by","title_b":"Design",
 "subtitle":"Building your family on purpose instead of by default",
 "problem":"Most families don\u2019t choose their culture \u2014 they drift into it. Without a clear sense of mission or shared values, family life gets shaped by busyness, screens, and whatever the calendar demands, and we wake up years later wondering how we got here. A family left to default rarely becomes the family we hoped for.",
 "promise":"Family by Design hands your people the blueprint. Over forty days they\u2019ll move from a family shaped by accident to one built on purpose \u2014 clarifying their family\u2019s mission, values, and rhythms, and making the decisive declaration that, whatever others do, this household will follow the Lord.",
 "verse":"\u2026as for me and my household, we will serve the Lord.",
 "ref":"Joshua 24:15 (NIV)",
 "bigidea":"A family is either built on purpose or shaped by default \u2014 and default rarely drifts anywhere good. The strongest families are the ones designed on purpose.",
 "tags":["Family Mission","Intentionality","Values","Vision","On Purpose"],
 "best_for":"Church &amp; Company","backbone":"Joshua 24:14\u201315; Proverbs 24:3\u20134","metaphor":"As for Me and My House","felt":"Family mission, intentionality, on purpose",
 "sessions":[
   ("1","Drift or Design","How most families are shaped by default."),
   ("2","As for Me and My House","The decisive declaration that sets direction."),
   ("3","Your Family\u2019s Mission","Clarifying what your family is for."),
   ("4","Shared Values","Naming the things your family stands on."),
   ("5","Rhythms That Shape Us","Building habits that form your family\u2019s culture."),
   ("6","A Family on Purpose","Becoming the household you\u2019ve chosen to be."),
 ],
 "journey":"Each of the 40 days clarifies one piece of your family\u2019s design \u2014 a value, a mission, a rhythm \u2014 and puts it into practice, with a partner check-in and a prayer.",
 "why":"No family drifts into health, mission, or deep faith by accident. The families that thrive are built on purpose \u2014 and it\u2019s never too late to start designing.",
 "cta":"Launch Family by Design and help your people build their family on purpose.",
 "note":None,
},
]

for _c in campaigns:
    _c["category"] = "Family Legacy"
    _c["tier"] = "Tier 2"
    _c["audience"] = "Church + Company"

cover = """
<div class="page cover">
  <div class="frame gold"></div>
  <div class="cover-inner">
    <div class="brandmark">Lifetogether</div>
    <div class="kicker">The Campaign Library &nbsp;&middot;&nbsp; Family Legacy Collection</div>
    <div class="cover-rule"></div>
    <h1>The <em>Family Legacy</em><br>Collection</h1>
    <div class="sub">Five forty-day campaigns to help your people build families on purpose and pass down a legacy of faith that lasts for generations.</div>
    <div class="cover-foot">
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">Campaigns</div></div>
        <div class="stat"><div class="n">40</div><div class="l">Day Journey</div></div>
        <div class="stat"><div class="n">6</div><div class="l">Sessions Each</div></div>
        <div class="stat"><div class="n">NIV</div><div class="l">Scripture</div></div>
      </div>
      <div class="tier">Tier 2 &nbsp;&middot;&nbsp; Family, Inheritance &amp; Legacy &nbsp;&middot;&nbsp; For Churches &amp; Companies</div>
    </div>
  </div>
</div>"""

intro = """
<div class="page intro">
  <div class="frame"></div>
  <div class="intro-inner">
    <div class="kicker">Before You Begin</div>
    <h2>The most important thing you\u2019ll<br>ever leave isn\u2019t in your <em>will</em>.</h2>
    <p class="lead">Long after the estate is settled, what truly shapes a family is the faith, character, and mission passed from one generation to the next. Yet that kind of legacy never happens by accident \u2014 it\u2019s received, built, and handed forward on purpose. <strong>The Family Legacy Collection helps your people do exactly that.</strong> Five distinct, forty-day journeys move them from drifting to designing \u2014 building families on purpose and passing down a faith that lasts for generations.</p>
    <div class="howrow">
      <div class="howcard"><div class="hn">40</div><h4>A Daily Rhythm</h4><p>Every day offers a short reading, one practical step, a spiritual-partner check-in, and a written prayer &mdash; small, repeatable, and easy to keep.</p></div>
      <div class="howcard"><div class="hn">6</div><h4>A Weekly Gathering</h4><p>Six group sessions give the journey its backbone, turning private intention into shared momentum across your church or team.</p></div>
      <div class="howcard"><div class="hn">1</div><h4>A Clear Outcome</h4><p>Each campaign is built around one transformation &mdash; so your people don\u2019t just hope for a legacy, they begin to build one.</p></div>
    </div>
    <div class="contents">
      <div class="ct">Inside This Collection</div>
      <div class="clist">
        <div class="cli"><span class="cnum">01</span><span><span class="cnm">Family Legacy</span><br><span class="cds">Leave the inheritance that truly lasts</span></span></div>
        <div class="cli"><span class="cnum">02</span><span><span class="cnm">Leaving a Lasting Legacy</span><br><span class="cds">Build a life whose impact endures</span></span></div>
        <div class="cli"><span class="cnum">03</span><span><span class="cnm">Generations</span><br><span class="cds">Receive the faith and pass it on</span></span></div>
        <div class="cli"><span class="cnum">04</span><span><span class="cnm">Faith for Generations</span><br><span class="cds">Pass living faith to your children</span></span></div>
        <div class="cli"><span class="cnum">05</span><span><span class="cnm">Family by Design</span><br><span class="cds">Build your family on purpose</span></span></div>
      </div>
    </div>
  </div>
</div>"""

closing = """
<div class="page close">
  <div class="frame"></div>
  <div class="close-inner">
    <div class="kicker">Ready When You Are</div>
    <h2>Help your people leave<br>a legacy that <em>lasts</em>.</h2>
    <p class="cp">From the inheritance that outlasts any will to a family built on purpose, these five campaigns help your people receive, build, and hand down a faith that endures for generations. Choose where your church or team is ready to grow, or journey through all five across a season.</p>
    <div class="close-list">
      <div class="cl-row"><span class="cln">01</span><span class="clt">Family Legacy</span><span class="cld">The real inheritance</span></div>
      <div class="cl-row"><span class="cln">02</span><span class="clt">Leaving a Lasting Legacy</span><span class="cld">Remembered forever</span></div>
      <div class="cl-row"><span class="cln">03</span><span class="clt">Generations</span><span class="cld">The chain of faith</span></div>
      <div class="cl-row"><span class="cln">04</span><span class="clt">Faith for Generations</span><span class="cld">Impress them on your children</span></div>
      <div class="cl-row"><span class="cln">05</span><span class="clt">Family by Design</span><span class="cld">As for me and my house</span></div>
    </div>
    <div class="close-cta"><span class="btn">Start Your Campaign</span></div>
    <div class="close-foot">
      <div class="niv">All Scripture taken from the New International Version (NIV)</div>
      <div class="brandmark">Lifetogether</div>
    </div>
  </div>
</div>"""

pages = cover + intro + "".join(campaign_page(c) for c in campaigns) + closing
doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>The Family Legacy Collection \u2014 Lifetogether</title>
<style>{FONTS}</style>
<style>{CSS}</style>
</head><body>{pages}</body></html>"""

pathlib.Path("/tmp/family_legacy.html").write_text(doc, encoding="utf-8")
print("HTML written:", len(doc), "chars")
