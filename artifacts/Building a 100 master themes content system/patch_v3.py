# -*- coding: utf-8 -*-
import re, glob
O='/home/claude/site/out/'

# ============ 1. curriculum.html: new formats + rich sermon appendix ============
h=open(O+'curriculum.html').read()
h=h.replace("const FMTS=['7-Day','21-Day','30-Day','40-Day','6-Week'];",
            "const FMTS=['7-Day','21-Day','30-Day','40-Day','6-Week','Youth','Kids','Leader Kit'];")

# replace the entire render branch (from `if(FMT==='6-Week'){` through the final `}` before footer append)
start=h.index("if(FMT==='6-Week'){")
end=h.index("h+=`<div style=\"text-align:center;margin-top:28px;")
new_branch='''if(FMT==='Leader Kit'){
 const lk=Engine.leaderKit(C);
 h+=`<p style="font-size:14px;"><b>How to use this kit:</b> the training half equips every host in one 45-minute session; the recruitment half fills the living rooms three weeks before launch. Print one per host.</p>`;
 h+=`<div class="dhead"><span class="dn">Part 1</span><span class="dl">Host training</span></div><div class="dth">You Can Do This: Host Training</div>
  <div class="dlbl">The role</div><p>${lk.training.role}</p>`;
 lk.training.points.forEach(p=>{h+=`<div class="dlbl">${p.h}</div><p>${p.p}</p>`;});
 h+=`<div class="dlbl">First-night checklist</div><ol style="padding-left:20px;">${lk.training.firstNight.map(x=>'<li style="font-size:13.5px;margin-bottom:4px;">'+x+'</li>').join('')}</ol>
  <div class="dlbl">Shepherd care notes</div><ol style="padding-left:20px;">${lk.training.care.map(x=>'<li style="font-size:13.5px;margin-bottom:4px;">'+x+'</li>').join('')}</ol>`;
 h+=`<div class="dhead" style="margin-top:34px;"><span class="dn">Part 2</span><span class="dl">Host recruitment</span></div><div class="dth">Filling the Living Rooms</div>
  <div class="dlbl">Pulpit ask (read as written)</div><p class="dpray">${lk.recruit.pulpit}</p>
  <div class="dlbl">Personal ask script</div><p class="dpray">${lk.recruit.personal}</p>
  <div class="dlbl">Three-week recruitment timeline</div><ol style="padding-left:20px;">${lk.recruit.timeline.map(x=>'<li style="font-size:13.5px;margin-bottom:4px;">'+x+'</li>').join('')}</ol>
  <div class="dlbl">When they hesitate</div>${lk.recruit.faq.map(f=>`<p><b>${f.q}</b><br>${f.a}</p>`).join('')}`;
}else if(FMT==='Youth'){
 const y=Engine.youth(C);
 h+=`<p style="font-size:14px;"><b>How to use this edition:</b> six student sessions aligned to the adult journey — same weekly themes, student voice. Works for youth group, campus clubs, or family use alongside the adult devotional.</p>`;
 y.sessions.forEach(s=>{
  h+=`<div class="sess day"><h3>${s.title}</h3><div class="focus">${s.sub}</div>
   <div class="dlbl">Hook (5 min)</div><p>${s.hook}</p>
   <div class="dlbl">Real talk</div><p>${s.talk}</p>
   <div class="dlbl">Look it up</div><p>${s.refs.join(' · ')}</p>
   <div class="dlbl">Talk it out</div><ol>${s.qs.map(q=>'<li>'+q+'</li>').join('')}</ol>
   <div class="dlbl">This week's challenge</div><p class="dq">${s.challenge}</p>
   <p style="font-size:12px;color:#5A6B7B;margin-top:10px;">${s.leader}</p></div>`;});
}else if(FMT==='Kids'){
 const k=Engine.children(C);
 h+=`<p style="font-size:14px;"><b>How to use this edition:</b> six children's lessons matched to the adult weeks — a Bible story, a Big Truth, the family memory verse, an activity, and a takeaway for parents. Ideal for Sunday kids' ministry or the family table.</p>`;
 k.lessons.forEach(L=>{
  h+=`<div class="sess day"><h3>${L.title}</h3><div class="focus">${L.big}</div>
   <div class="dscr" style="background:#F2F6FB;border-left-color:#4F86E0;color:#26417F;text-transform:none;letter-spacing:0;font-weight:400;font-family:Georgia,serif;font-size:14.5px;font-style:italic;">\u201C${L.mem.t}\u201D<div style="font-family:'Hanken Grotesk';font-style:normal;font-weight:800;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;margin-top:6px;">Family memory verse · ${L.mem.v} (KJV)</div></div>
   <div class="dlbl">Tell the story</div><p>${L.story}</p>
   <div class="dlbl">Activity</div><p>${L.activity}</p>
   <div class="dlbl">Talk about it</div><ol>${L.qs.map(q=>'<li>'+q+'</li>').join('')}</ol>
   <div class="dlbl">Send-home</div><p class="dq">${L.family}</p></div>`;});
}else if(FMT==='6-Week'){
 const g=Engine.groupStudy(C);
 h+=`<p style="font-size:14px;"><b>How to use this series:</b> six leader-led sessions, 60–75 minutes each. No seminary required — the leader\u2019s only job is to keep the circle honest and keep it moving. Pair it with any daily format of <em>${C[0]}</em> for churchwide alignment.</p>`;
 g.sessions.forEach(s=>{
  h+=`<div class="sess day"><h3>${s.title}</h3><div class="focus">${s.focus}</div>
   <div class="dscr" style="background:#F2F6FB;border-left-color:#4F86E0;color:#26417F;text-transform:none;letter-spacing:0;font-weight:400;font-family:Georgia,serif;font-size:14.5px;font-style:italic;">\u201C${s.mem.t}\u201D<div style="font-family:'Hanken Grotesk';font-style:normal;font-weight:800;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;margin-top:6px;">This week\u2019s memory verse · ${s.mem.v} (KJV)</div></div>
   <div class="dlbl">Open (10 min)</div><p>${s.opener}</p>
   <div class="dlbl">Read together</div><p>${s.refs.join(' · ')}</p>
   <div class="dlbl">Discuss (35 min)</div><ol>${s.qs.map(q=>'<li>'+q+'</li>').join('')}</ol>
   <div class="dlbl">Pray</div><p class="dpray">${s.pray}</p>
   <div class="dlbl">This week\u2019s practice</div><p class="dq">${s.practice}</p>
   <p style="font-size:12px;color:#5A6B7B;margin-top:10px;">${s.leader}</p></div>`;});
 const ser=Engine.sermons(C);
 h+=`<div class="dhead"><span class="dn">Appendix</span><span class="dl">Weekend alignment</span></div>
 <div class="dth">Six Full Message Builds</div>
 <p style="font-size:13.5px;">Each week: sermon title & subtitle, three texts, five preaching ideas with supporting references, and a complete message outline.</p>`;
 ser.forEach(s=>{h+=`<div class="sess day"><div style="font-family:'Hanken Grotesk';font-weight:800;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-d);margin-bottom:4px;">${s.wk}</div>
  <h3>${s.title}</h3><div class="focus">${s.subtitle}</div>
  <div class="dlbl">Texts</div><p>${s.texts.join(' · ')}</p>
  <div class="dlbl">Five preaching ideas</div>
  ${s.ideas.map(i=>`<p style="margin-bottom:10px;"><b>${i.h}</b><br>${i.p}<br><span style="font-size:12px;color:#5A6B7B;">Supporting texts: ${i.refs.join(' · ')}</span></p>`).join('')}
  <div class="dlbl">Message outline</div><ol style="padding-left:20px;">${s.outline.map(o=>'<li style="font-size:13.5px;margin-bottom:4px;">'+o+'</li>').join('')}</ol></div>`;});
}else{
 const dev=Engine.devotional(C,FMT);
 h+=`<p style="font-size:14px;"><b>How to use this journey:</b> one reading a day — Scripture, a short reflection, a prayer, one question, one small step. Missed a day? Grace covers it; just pick up where you are. Better with a partner or a group: the 6-Week study is included with your license.</p>`;
 dev.days.forEach(d=>{
  h+=`<div class="day"><div class="dhead"><span class="dn">${d.dn}</span><span class="dl">${C[0]} · ${d.wk}</span></div>
  <div class="dth">${d.title}</div>
  <div class="dscr" style="background:#F2F6FB;border-left-color:#4F86E0;color:#26417F;text-transform:none;letter-spacing:0;font-weight:400;font-family:Georgia,serif;font-size:14.5px;font-style:italic;">\u201C${d.mem.t}\u201D<div style="font-family:'Hanken Grotesk';font-style:normal;font-weight:800;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;margin-top:6px;">This week\u2019s memory verse · ${d.mem.v} (KJV)</div></div>
  <div class="dscr">Today\u2019s reading: ${d.scr}</div>
  <div class="dlbl">Reflect</div>${d.body}
  <div class="dlbl">Pray</div><p class="dpray">${d.pray}</p>
  <div class="dlbl">Reflect &amp; Respond</div><p class="dq">${d.q}</p>
  <div class="dlbl">One Step Today</div><p class="dstep">${d.step}</p></div>`;});
 const k=Engine.launchKit(C);
 h+=`<div class="dhead"><span class="dn">Launch kit</span><span class="dl">For your team</span></div>
 <div class="dth">Launching ${C[0]}</div>
 <div class="dlbl">Pulpit announcement</div><p class="dpray">${k.announce}</p>
 <div class="dlbl">Communication sequence</div><ol style="padding-left:20px;">${k.emails.map(e=>'<li style="font-size:13.5px;margin-bottom:4px;">'+e+'</li>').join('')}</ol>
 <div class="dlbl">Celebration Sunday</div><p>${k.celebration}</p>`;
}
'''
h=h[:start]+new_branch+h[end:]
# header cover tab label for new fmts
h=h.replace("${FMT.replace('-',' ').toUpperCase()} ${FMT==='6-Week'?'GROUP SERIES':'CAMPAIGN'}",
            "${FMT.replace('-',' ').toUpperCase()} ${FMT==='6-Week'?'GROUP SERIES':(FMT==='Youth'?'EDITION':(FMT==='Kids'?\"CHILDREN'S EDITION\":(FMT==='Leader Kit'?'':'CAMPAIGN')))}")
open(O+'curriculum.html','w').write(h)

# ============ 2. confirmation + account pills ============
for f in ('confirmation.html','account.html'):
    h=open(O+f).read()
    h=h.replace("const FMTS=['40-Day','30-Day','21-Day','7-Day','6-Week'];",
                "const FMTS=['40-Day','30-Day','21-Day','7-Day','6-Week','Youth','Kids','Leader Kit'];")
    open(O+f,'w').write(h)

# ============ 3. campaign.html kit tiles + sermon copy ============
h=open(O+'campaign.html').read()
h=h.replace('<div class="it">Sermon Series</div><div class="id">6 message outlines that align the weekend</div>',
            '<div class="it">Sermon Series</div><div class="id">6 full builds — title, texts, five ideas &amp; complete outline</div>')
h=h.replace('<div class="it">Launch Kit</div><div class="id">Graphics, leader training &amp; Celebration Sunday</div></div>',
'''<div class="it">Launch Kit</div><div class="id">Announcements, comms sequence &amp; Celebration Sunday</div></div>
    <div class="inc"><div class="ii"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l7 4v5c0 4-3 6.5-7 8-4-1.5-7-4-7-8V7zM9 12h6M12 9v6"/></svg></div><div class="it">Youth &amp; Kids Editions</div><div class="id">Student sessions + children\u2019s lessons, same weekly journey</div></div>
    <div class="inc"><div class="ii"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 11l-3 3-2-2"/></svg></div><div class="it">Leader Training &amp; Recruitment</div><div class="id">Host training, ask scripts &amp; a 3-week recruiting plan</div></div>''')
h=h.replace('.incl{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;}','.incl{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}')
h=h.replace('One campaign, every asset your church needs to launch — across five formats and four audience editions.',
            'One campaign, every asset your church needs — adult, youth, and children\u2019s editions, leader training, and a full launch system.')
open(O+'campaign.html','w').write(h)

# ============ 4. About: rewrite page, add to nav everywhere, index band ============
h=open(O+'about.html').read()
m=re.search(r'<header class="head">.*?(?=<footer|<script src="cart)', h, re.S)
about_body='''<header class="head"><span class="eb">About Lifetogether</span><h1>Twenty-five years of one conviction: nobody does this alone</h1>
<p>40 Day Campaigns is the platform expression of Lifetogether — built on a quarter century of churchwide campaigns with the largest and fastest-growing churches in America.</p></header>

<section class="section" style="max-width:820px;">
<h2 style="font-weight:900;font-size:22px;margin-bottom:10px;">The story</h2>
<p style="font-size:15px;line-height:1.75;color:var(--ink-2);margin-bottom:14px;">Lifetogether was founded by Brett Eastman, who helped launch the Apple Macintosh before answering Bob Buford\u2019s call from success to significance. He earned his M.Div., served alongside Bill Hybels at Willow Creek and Rick Warren at Saddleback, and sat in the rooms where the Purpose Driven Life campaign was designed — then spent twenty-five years running churchwide campaigns with more than 500 of the largest and fastest-growing churches in America, reaching tens of millions of campaign participants.</p>
<p style="font-size:15px;line-height:1.75;color:var(--ink-2);margin-bottom:14px;">Across those years, one pattern held every single time: when an entire congregation reads the same Scripture, prays about the same theme, and walks the same journey in the same season — Sunday teaching, daily devotional, small groups, students, kids, everyone — the message stops being a sermon and becomes a shared life. That is what a campaign is. It is the most reliable spiritual-formation engine the local church has ever had.</p>
<p style="font-size:15px;line-height:1.75;color:var(--ink-2);">For most of those twenty-five years, that experience belonged mostly to churches with big teams and bigger budgets. Technology has now changed the economics of producing complete campaigns — which means the model that served the megachurch can finally serve every church. That is what this platform exists to do.</p>
</section>

<section class="section" style="max-width:820px;">
<h2 style="font-weight:900;font-size:22px;margin-bottom:10px;">What we believe about campaigns</h2>
<p style="font-size:15px;line-height:1.75;color:var(--ink-2);margin-bottom:14px;">Don\u2019t let Sunday end on Sunday. A weekend message, however good, evaporates by Tuesday unless it has somewhere to live during the week — a devotional in every hand, a circle of people walking it out together, a next step small enough to take today. Every campaign in this library is built on that architecture: one theme, one anchor passage, six weekly movements, and daily obedience in community.</p>
<p style="font-size:15px;line-height:1.75;color:var(--ink-2);">And every campaign is written in plain, pastoral language — felt needs first, no seminary jargon, grace before pressure — because the people who most need these journeys are rarely the ones who feel spiritually impressive.</p>
</section>

<section class="section" style="max-width:820px;">
<h2 style="font-weight:900;font-size:22px;margin-bottom:12px;">The heritage</h2>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;">
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;text-align:center;"><div style="font-family:'Hanken Grotesk';font-weight:900;font-size:26px;color:var(--orange);">25</div><div style="font-size:12.5px;color:var(--dim);">years of churchwide campaigns</div></div>
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;text-align:center;"><div style="font-family:'Hanken Grotesk';font-weight:900;font-size:26px;color:var(--orange);">500+</div><div style="font-size:12.5px;color:var(--dim);">church partnerships</div></div>
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;text-align:center;"><div style="font-family:'Hanken Grotesk';font-weight:900;font-size:26px;color:var(--orange);">10M+</div><div style="font-size:12.5px;color:var(--dim);">campaign participants — tens of millions served</div></div>
<div class="card" style="background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;text-align:center;"><div style="font-family:'Hanken Grotesk';font-weight:900;font-size:26px;color:var(--orange);">10,000</div><div style="font-size:12.5px;color:var(--dim);">campaigns in this library today</div></div>
</div>
<p style="font-size:13px;color:var(--faint);margin-top:12px;">Trusted through the years by Rick Warren, Ron Blue, Saddleback, Willow Creek, The Signatry, and hundreds of senior pastors.</p>
</section>

<section class="section" style="max-width:820px;">
<h2 style="font-weight:900;font-size:22px;margin-bottom:10px;">Where this is going</h2>
<p style="font-size:15px;line-height:1.75;color:var(--ink-2);margin-bottom:18px;">The mission is simple to say and enormous to build: the world\u2019s largest Christian campaign library — every theme a pastor plans around, every audience, every life event, every format — organized so that any church of any size can launch a professionally built, personally fitted campaign in days, not months. Every campaign. Every church. Every day.</p>
<div style="display:flex;gap:10px;flex-wrap:wrap;">
<a class="btn btn-orange" href="browse.html">Browse the library</a>
<a class="btn btn-white" href="churches.html">For churches</a>
<a class="btn btn-white" href="contact.html">Talk to us</a>
</div>
</section>
'''
h=h[:m.start()]+about_body+h[m.end():]
open(O+'about.html','w').write(h)

# nav: add About after How It Works on every page that has an .nlinks nav
added=[]
for p in glob.glob(O+'*.html'):
    x=open(p).read(); o=x
    for pat in ('<a href="how-it-works.html">How It Works</a>','<a href="how-it-works.html">How it works</a>'):
        if pat in x and 'about.html">About' not in x.split('</nav>')[0]:
            x=x.replace(pat, pat+'<a href="about.html"'+(' class="on"' if p.endswith('about.html') else '')+'>About</a>',1)
    if x!=o: open(p,'w').write(x); added.append(p.split('/')[-1])
print('nav About added:',len(added),'pages')

# index About band before testimonials
h=open(O+'index.html').read()
band='''<section class="wash" id="aboutband"><div class="wrap center">
  <span class="sec-eyebrow">About Lifetogether</span>
  <h2 class="big">Built on 25 years of churchwide campaigns</h2>
  <p class="lead" style="max-width:720px;margin:0 auto 18px;">From the rooms where the Purpose Driven Life campaign was designed to 500+ church partnerships and tens of millions of participants — this platform puts that entire methodology within reach of every church.</p>
  <a class="btn btn-white" href="about.html">Read our story <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6"><path d="M7 17 17 7M8 7h9v9"/></svg></a>
</div></section>
'''
# insert before testimonials section (find a stable marker)
for marker in ('<!-- TESTIMONIALS','<section id="stories"','Running campaigns since'):
    if marker in h:
        idx=h.index(marker)
        # back up to nearest <section
        sidx=h.rfind('<section',0,idx+40)
        h=h[:sidx]+band+h[sidx:]
        break
open(O+'index.html','w').write(h)
print('done')
