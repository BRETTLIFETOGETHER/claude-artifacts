# -*- coding: utf-8 -*-
import re
O='/home/claude/site/out/'

# ---------- index.html ----------
p=O+'index.html'; s=open(p).read()
s=s.replace('''      <a href="browse.html">Campaigns</a>
      <a href="browse.html">Channels</a>
      <a href="#features">Resources</a>
      <a href="#faq">Pricing</a>''',
'''      <a href="browse.html">Campaigns</a>
      <a href="finder.html">Finder</a>
      <a href="how-it-works.html">How It Works</a>
      <a href="pricing.html">Pricing</a>''')
s=s.replace('<a class="btn btn-white" href="#">Sign in</a>','<a class="btn btn-white" href="signin.html">Sign in</a>')
s=s.replace('<a class="btn btn-orange" href="#">Get access','<a class="btn btn-orange" href="get-access.html">Get access')
s=s.replace('<a class="btn btn-white" href="#features">See how it works</a>','<a class="btn btn-white" href="how-it-works.html">See how it works</a>')
s=s.replace('<a class="btn btn-dark" href="#">See everything that\'s included','<a class="btn btn-dark" href="how-it-works.html#included">See everything that\'s included')
s=s.replace('<a class="btn btn-dark" href="#">Explore customer stories','<a class="btn btn-dark" href="churches.html#stories">Explore customer stories')
s=s.replace('<a class="btn btn-dark" href="#">Browse all FAQ','<a class="btn btn-dark" href="faq.html">Browse all FAQ')
s=s.replace('<a class="btn btn-orange" href="#">Request a walkthrough','<a class="btn btn-orange" href="contact.html">Request a walkthrough')
s=s.replace('<a href="#" class="on">Churches</a><a href="#">Families</a><a href="#">Advisors</a><a href="#">Networks</a>',
 '<a href="churches.html#churches" class="on">Churches</a><a href="churches.html#families">Families</a><a href="churches.html#advisors">Advisors</a><a href="churches.html#networks">Networks</a>')
for lab in ['Instagram','Facebook','X','YouTube']:
    s=s.replace(f'<a href="#" aria-label="{lab}">', f'<a href="contact.html" aria-label="{lab}" title="Social channels launch soon — say hello">')
s=s.replace('NIV throughout · Privacy · Terms','NIV throughout · <a href="faq.html" style="color:rgba(255,255,255,.7)">FAQ</a> · <a href="about.html" style="color:rgba(255,255,255,.7)">About</a>')
# channels->categories language sweep
s=s.replace('>Channels<','>Categories<').replace('10 channels','10 categories').replace('ten channels','ten categories')
open(p,'w').write(s); print('index patched')

# ---------- browse.html ----------
p=O+'browse.html'; s=open(p).read()
s=s.replace('<div class="nlinks"><a href="#" class="on">Campaigns</a><a href="index.html#ministry">Audiences</a><a href="index.html#features">How It Works</a><a href="index.html#faq">Pricing</a></div>',
 '<div class="nlinks"><a href="browse.html" class="on">Campaigns</a><a href="finder.html">Finder</a><a href="how-it-works.html">How It Works</a><a href="pricing.html">Pricing</a></div>')
s=s.replace('<a class="btn btn-white" href="#">Sign in</a><a class="btn btn-orange" href="#">Get access</a>',
 '<a class="btn btn-white" href="signin.html">Sign in</a><a class="btn btn-orange" href="get-access.html">Get access</a>')
s=s.replace('<a class="btn btn-white" href="#">Search</a>','<button class="btn btn-white" id="qgo" type="button">Search</button>')
s=s.replace('Ten channels, every topic a pastor plans around.','Ten categories, every topic a pastor plans around.')
# URL params + search button wiring
s=s.replace("render();\n</script>", """
document.getElementById('qgo').addEventListener('click',()=>{render();scrollToGrid();});
/* deep links: ?cat= ?season= ?outcome= ?fmt= ?q= ?sort=new */
(function(){const P=new URLSearchParams(location.search);
 if(P.get('cat'))toggleFilter('channel',P.get('cat'),true);
 if(P.get('season'))toggleFilter('season',P.get('season'),true);
 if(P.get('outcome'))toggleFilter('outcome',P.get('outcome'),true);
 if(P.get('fmt'))toggleFilter('format',P.get('fmt'),true);
 if(P.get('q')){QUERY=P.get('q').toLowerCase();document.getElementById('q').value=P.get('q');}
 if(P.get('sort')){document.getElementById('sort').value=P.get('sort');}
 if([...P.keys()].length)render();
})();
render();
</script>""")
open(p,'w').write(s); print('browse patched')

# ---------- campaign.html ----------
p=O+'campaign.html'; s=open(p).read()
s=s.replace('<a class="btn btn-orange" href="#">Start this campaign','<a class="btn btn-orange" href="pricing.html">Start this campaign')
s=s.replace('<a class="btn btn-white" href="#">Add to my plan</a>','<a class="btn btn-white" href="get-access.html">Add to my plan</a>')
s=s.replace('href="god-owns-it-all-devotional-sample.pdf"','href="sample-devotional.pdf"')
s=s.replace('<a class="btn btn-white" href="#" style="font-size:13px;padding:9px 15px;">Open in Canva','<a class="btn btn-white" href="how-it-works.html#exports" style="font-size:13px;padding:9px 15px;">Open in Canva')
s=s.replace('<a class="btn btn-white" href="#" style="font-size:13px;padding:9px 15px;">Export editable copy</a>','<a class="btn btn-white" href="how-it-works.html#exports" style="font-size:13px;padding:9px 15px;">Export editable copy</a>')
s=s.replace('<a class="btn btn-white" href="#" style="font-size:13px;padding:9px 15px;">Brand it for our church</a>','<a class="btn btn-white" href="pricing.html#premium" style="font-size:13px;padding:9px 15px;">Brand it for our church</a>')
s=s.replace('Uses a shared Canva brand template · or import the PDF above','Import the PDF into Canva today · one-click integration in development')
open(p,'w').write(s); print('campaign patched')

# ---------- nav.html ----------
p=O+'nav.html'; s=open(p).read()
s=s.replace("const CH=[['Spiritual Formation',1],['The Bible',2],['Emotional &amp; Mental Health',3],['Relationships &amp; Family',4],",
 "const CH=[['Identity &amp; Purpose',1],['Peace &amp; Emotional Health',2],['Marriage &amp; Relationships',3],['Family &amp; Parenting',4],")
# find the rest of CH array
m=re.search(r"const CH=\[.*?\];", s, re.S)
newch=("const CH=[['Identity &amp; Purpose',1],['Peace &amp; Emotional Health',2],['Marriage &amp; Relationships',3],"
 "['Family &amp; Parenting',4],['Money &amp; Stewardship',5],['Generosity &amp; Kingdom Impact',6],"
 "['Faith &amp; Discipleship',7],['Community &amp; Belonging',8],['Hope &amp; Trials',9],['Mission &amp; Legacy',10]];")
s=s[:m.start()]+newch+s[m.end():]
s=s.replace('href="browse.html"><span class="dot" style="background:var(--c${c[1]})"></span>',
 'href="browse.html?cat=${c[1]}"><span class="dot" style="background:var(--c${c[1]})"></span>')
seas_map={'New Year &amp; Prayer':'browse.html?season=new','Lent &amp; Easter':'browse.html?season=lent',
 'Fall Kickoff':'browse.html?season=fall','Advent &amp; Christmas':'browse.html?season=advent','Year-End Giving':'browse.html?season=yearend'}
for lab,href in seas_map.items():
    s=s.replace(f'<a class="lk" href="#">{lab}</a>', f'<a class="lk" href="{href}">{lab}</a>')
out_map={'Small Group Launch':'browse.html?outcome=groups','Build a Generosity Culture':'browse.html?outcome=generosity','Emotional Health':'browse.html?outcome=emotional'}
for lab,href in out_map.items():
    s=s.replace(f'<a class="lk" href="#">{lab}</a>', f'<a class="lk" href="{href}">{lab}</a>')
res_map={'What is a campaign?':'how-it-works.html#what','Choosing a format':'how-it-works.html#formats',
 "What's included":'how-it-works.html#included','The campaign process':'how-it-works.html#process',
 'Case studies':'churches.html#stories','FAQ':'faq.html'}
for lab,href in res_map.items():
    s=s.replace(f'<a class="lk" href="#">{lab}</a>', f'<a class="lk" href="{href}">{lab}</a>')
s=s.replace('<a class="viewall" href="#" style="margin-top:12px;">New this month','<a class="viewall" href="browse.html?sort=new" style="margin-top:12px;">New this month')
# remaining generic placeholders in nav (sign in / get access / any menu links)
s=s.replace('href="#">Sign in','href="signin.html">Sign in').replace('href="#">Get access','href="get-access.html">Get access')
open(p,'w').write(s); print('nav patched')
