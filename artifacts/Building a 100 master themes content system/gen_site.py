import json, re, shutil, zipfile, os
from data_a import THEMES_A
from data_b import THEMES_B

THEMES = THEMES_A + THEMES_B
CATS = {1:'Identity & Purpose',2:'Peace & Emotional Health',3:'Marriage & Relationships',4:'Family & Parenting',
5:'Money & Stewardship',6:'Generosity & Kingdom Impact',7:'Faith & Discipleship',8:'Community & Belonging',
9:'Hope & Trials',10:'Mission & Legacy'}

AUD = {1:['Young adults','College students','Midlife adults','Adults in their 30s-40s','New graduates','Those in career transition'],
2:['Those battling anxiety','Caregivers','Parents of teens','Church staff','Healthcare workers','The lonely'],
3:['Engaged couples','Newlyweds','Married couples','Couples in crisis','Empty nesters','Blended families'],
4:['Parents of school-age kids','Parents of teens','Grandparents','Multi-generational families','Parents of adult children','Legacy families'],
5:['Young professionals','Married couples','Business owners','The financially stressed','Pre-retirees','New homeowners'],
6:['Major donors','Kingdom investors','Philanthropic couples','Family foundations','Donor-advised fund holders','Giving circles'],
7:['New believers','Small group members','Small group leaders','Sunday-only attenders','Volunteers','Church staff'],
8:['The lonely','New members','The recently relocated','Singles','Young adults','Seniors'],
9:['The grieving','Those facing illness','Those in recovery','The unemployed','Widows and widowers','Caregivers'],
10:['Retirees','Empty nesters','Legacy families','Seniors','Business sellers','Succession-stage owners']}

EVT = {1:['College Graduation','First Career','Leaving Home','Coming to Faith in Christ','Baptism','Retirement'],
2:['Serious Health Diagnosis','Becoming a Caregiver','Business Crisis','Significant Financial Loss','Retirement Planning','Long-Term Care Decision'],
3:['Engagement','Wedding','Honeymoon / First Year of Marriage','Anniversary Milestones','Blended Family Formation','Purchasing First Home'],
4:['Birth of First Child','Child Dedication','High School Graduation','Becoming Grandparents','Annual Family Meeting','Creating Family Mission Statement'],
5:['First Bank Account','Purchasing First Home','Paying Off Debt','Significant Salary Increase','Retirement Planning','Bonus or Windfall'],
6:['First Major Gift','Creating a Giving Plan','Opening a Donor-Advised Fund','Starting a Family Foundation','Legacy Giving Decision','Funding a Ministry Project'],
7:['Coming to Faith in Christ','Baptism','Joining a Church','Becoming a Small Group Leader','Beginning Family Devotions','Sabbatical or Spiritual Retreat'],
8:['Joining a Church','Becoming a Small Group Leader','Family Reunion','Leaving Home','Retirement','Launching a Family Ministry'],
9:['Death of a Parent','Death of a Spouse','Serious Health Diagnosis','Significant Financial Loss','Business Crisis','Hospice Care'],
10:['Retirement','Commissioning the Next Generation','Writing Legacy Letters','Succession Planning','Celebrating a Family Legacy','End-of-Life Blessing & Celebration']}

GUIDE = {1:['Senior pastor','Life coach','Mentor'],2:['Christian counselor','Senior pastor','Small group leader'],
3:['Marriage and family therapist','Senior pastor','Christian counselor'],4:['Parent','Grandparent','Family meeting facilitator'],
5:['Financial advisor','CPA','Senior pastor'],6:['Wealth manager','Planned giving officer','Foundation officer'],
7:['Discipleship pastor','Small group leader','Mentor'],8:['Small groups pastor','Small group leader','Senior pastor'],
9:['Christian counselor','Senior pastor','Military or hospital chaplain'],10:['Missions pastor','Legacy coach','Senior pastor']}

SEAS = {1:[['fall'],['any']],2:[['new'],['any']],3:[['any'],['new']],4:[['fall'],['any']],5:[['new'],['yearend']],
6:[['yearend'],['any']],7:[['fall'],['lent']],8:[['fall'],['any']],9:[['lent'],['any']],10:[['any'],['yearend']]}
OUT = {1:['discipleship'],2:['emotional'],3:['discipleship'],4:['discipleship'],5:['generosity'],
6:['generosity'],7:['discipleship'],8:['groups'],9:['emotional'],10:['outreach']}
FMT_ROT = ['40-Day','40-Day','21-Day','40-Day','30-Day','40-Day','6-Week','40-Day','21-Day','30-Day',
'40-Day','7-Day','40-Day','6-Week','21-Day','40-Day','30-Day','40-Day','21-Day','40-Day']

rows, wb_rows = [], []
cid = 0
for theme, cat, scr, need, camps in THEMES:
    assert len(camps) == 20, (theme, len(camps))
    for i, (t, s) in enumerate(camps):
        cid += 1
        id_ = f"C{cid:04d}"
        aud = AUD[cat][i % 6]; evt = EVT[cat][i % 6]; g = GUIDE[cat][i % 3]
        fmt = FMT_ROT[i]; seas = SEAS[cat][i % 2]; out = OUT[cat]
        pop = 99 - (i * 3) % 60 - (cid % 7)
        nw = (cid * 37) % 100
        flag = 1 if i == 0 or t.startswith('40 Days') else 0
        rows.append([t, s, cat, fmt, seas, out, pop, nw, flag, id_, theme, aud, evt, scr])
        wb_rows.append((id_, theme, t, s, aud, evt, g, fmt + (' Campaign' if fmt=='40-Day' else ''),
                        'The 40-Day Campaign Arc', need, scr, 'Flagship' if flag else 'Core', 'Ready', ''))

# duplicate title check
titles = [r[0] for r in rows]
dups = sorted({t for t in titles if titles.count(t) > 1})
print('campaigns:', len(rows), '| duplicate titles:', dups if dups else 'none')

os.makedirs('/home/claude/site/out', exist_ok=True)
with open('/home/claude/site/out/data.js', 'w') as f:
    f.write('window.CATS=' + json.dumps(CATS) + ';\n')
    f.write('window.CAMPAIGNS=' + json.dumps(rows, ensure_ascii=False) + ';\n')

# ---------- patch browse.html ----------
b = open('/mnt/user-data/uploads/browse.html').read()
b = b.replace('<script>\nconst HUE=', '<script src="data.js"></script>\n<script>\nconst HUE=')
b = re.sub(r"const CHNAME=\{[^}]*\};",
  "const CHNAME=window.CATS;", b)
counts = {c: sum(1 for r in rows if r[2] == c) for c in CATS}
b = re.sub(r"const CHCOUNT=\{[^}]*\};", "const CHCOUNT=" + json.dumps({str(k): v for k, v in counts.items()}) + ";", b)
b = re.sub(r"// \[title, sub.*?\nconst DATA=\[.*?\n\];", "const DATA=window.CAMPAIGNS;", b, flags=re.S)
# wire search
b = b.replace('<input type="text" placeholder="Search', '<input type="text" id="q" placeholder="Search')
b = b.replace("const active={channel:new Set(),format:new Set(),season:new Set(),outcome:new Set()};",
  "const active={channel:new Set(),format:new Set(),season:new Set(),outcome:new Set()};\nlet QUERY='';\ndocument.getElementById('q').addEventListener('input',e=>{QUERY=e.target.value.toLowerCase();render();});")
b = b.replace("""function matches(row){
  const [t,s,ch,fmt,seas,out]=row;""",
  """function matches(row){
  const [t,s,ch,fmt,seas,out,pop,nw,flag,id,theme,aud]=row;
  if(QUERY && !(t+' '+s+' '+theme+' '+aud+' '+CHNAME[ch]).toLowerCase().includes(QUERY))return false;""")
# card render: link to campaign page, show subtitle + theme, format-aware tab
old_card = """  rows.forEach(row=>{const [t,s,ch,fmt,seas,out,pop,nw,flag]=row;const [a,b]=HUE[ch];
    const d=document.createElement('div');d.className='cov';
    d.innerHTML=`<div class="canvas" style="--ca:${a};--cb:${b}">
      <div class="tab"><b>40 DAY</b></div><div class="nm">${t}</div>
      ${flag?'<span class="flag">Flagship</span>':''}<span class="fmt">${fmt}</span></div>
      <div class="meta"><div class="t">${t}</div><div class="s">${CHNAME[ch].replace(' & ',' & ')}</div></div>`;
    grid.appendChild(d);});"""
new_card = """  rows.forEach(row=>{const [t,s,ch,fmt,seas,out,pop,nw,flag,id,theme]=row;const [a,b]=HUE[ch];
    const d=document.createElement('a');d.className='cov';d.href='campaign.html?id='+id;
    d.innerHTML=`<div class="canvas" style="--ca:${a};--cb:${b}">
      <div class="tab"><b>${fmt.replace('-',' ').toUpperCase()}</b></div><div class="nm">${t}</div>
      ${flag?'<span class="flag">Flagship</span>':''}<span class="fmt">${fmt}</span></div>
      <div class="meta"><div class="t">${t}</div><div class="s">${s} · ${theme}</div></div>`;
    grid.appendChild(d);});"""
assert old_card in b, 'card block not found'
b = b.replace(old_card, new_card)
b = b.replace('Explore by category, then narrow with filters.',
  'One thousand campaigns across fifty themes and ten categories.')
open('/home/claude/site/out/browse.html', 'w').write(b)

# ---------- patch campaign.html ----------
c = open('/mnt/user-data/uploads/campaign.html').read()
HUEHEX = {1:['#16A88F','#0C5A4E'],2:['#C8484C','#7E2326'],3:['#4F86E0','#26417F'],4:['#E0703F','#8A3A1E'],
5:['#E8A52E','#9A6810'],6:['#36A85E','#176233'],7:['#7B5FE0','#3F2E86'],8:['#E2542F','#8A2A14'],
9:['#5A6B8C','#2E3A52'],10:['#C99A3C','#7E601C']}
c = c.replace('<title>God Owns It All — 40 Day Campaigns</title>', '<title id="ptitle">40 Day Campaigns</title>')
c = c.replace('<a href="browse.html">Browse</a> <span>/</span> <a href="browse.html">Money &amp; Generosity</a> <span>/</span> <span style="color:var(--ink)">God Owns It All</span>',
  '<a href="browse.html">Browse</a> <span>/</span> <a href="browse.html" id="crumbcat">Category</a> <span>/</span> <span style="color:var(--ink)" id="crumbtitle"></span>')
c = c.replace('<div class="cov"><div class="canvas"><div class="tab"><b>40 DAY</b>',
  '<div class="cov"><div class="canvas" id="cvs"><div class="tab" ><b id="tabfmt">40 DAY</b>')
c = c.replace('<div class="nm">God Owns It All</div>', '<div class="nm" id="covnm"></div>')
c = c.replace('<span class="eb">Money &amp; Generosity · Flagship</span>', '<span class="eb" id="heb"></span>')
c = c.replace('<h1>God Owns It All</h1>', '<h1 id="h1t"></h1>')
c = re.sub(r'<p class="blurb">.*?</p>', '<p class="blurb" id="hblurb"></p>', c, flags=re.S)
c = c.replace('<span class="fmt on">40-Day Campaign</span><span class="fmt">30-Day</span><span class="fmt">21-Day</span><span class="fmt">7-Day</span><span class="fmt">6-Week Group</span>',
  '')
c = c.replace('<div class="fmts" id="fmts">', '<div class="fmts" id="fmts">')
c = c.replace('<script>\nconst DEVO=', '<script src="data.js"></script>\n<script>\nconst GOIA_DEVO=')
# append the data-driven controller before closing of that script: replace show(0); block ending
driver = """
const HUEHEX=%s;
const ALLFMTS=['40-Day Campaign','30-Day','21-Day','7-Day','6-Week Group'];
const P=new URLSearchParams(location.search);
const C=window.CAMPAIGNS.find(r=>r[9]===P.get('id'))||window.CAMPAIGNS[0];
const [T,S,CH,FMT,SEAS,OUTC,POP,NW,FLAG,ID,THEME,AUD,EVT,SCR]=C;
document.getElementById('ptitle').textContent=T+' — 40 Day Campaigns';
document.getElementById('crumbcat').textContent=window.CATS[CH];
document.getElementById('crumbtitle').textContent=T;
document.getElementById('covnm').textContent=T;
document.getElementById('tabfmt').textContent=FMT.replace('-',' ').toUpperCase();
document.getElementById('cvs').style.background=`linear-gradient(160deg,${HUEHEX[CH][0]},${HUEHEX[CH][1]})`;
document.getElementById('heb').textContent=window.CATS[CH]+' · '+THEME+(FLAG?' · Flagship':'');
document.getElementById('h1t').textContent=T;
document.getElementById('hblurb').innerHTML=`<b>${S}.</b> A ${FMT.toLowerCase()} journey through <em>${THEME}</em> — written for ${AUD.toLowerCase()}, and recommended around the season of <em>${EVT}</em>. Anchored in ${SCR} (NIV), with a daily Scripture, reflection, prayer, and one next step.`;
const fw=document.getElementById('fmts');fw.innerHTML='';
ALLFMTS.forEach(f=>{const s=document.createElement('span');s.className='fmt'+(f.startsWith(FMT)?' on':'');s.textContent=f;
 s.addEventListener('click',()=>{document.querySelectorAll('#fmts .fmt').forEach(x=>x.classList.remove('on'));s.classList.add('on');});fw.appendChild(s);});
function genDevo(){
 const wk=THEME+' · Week One';
 return [
 {dn:'Day 01',dl:wk,theme:'Where This Journey Begins',v:'Begin by reading today\\u2019s passage slowly, twice.',r:SCR+' (NIV)',
  body:`Every campaign in this library starts with a felt need — and this one begins with a sentence many of us have thought but rarely said out loud: <em>\\u201C${window.NEEDS[THEME]}\\u201D</em> If that\\u2019s you, you\\u2019re in the right place.<br><br>Over the coming days, <em>${T}</em> walks through what Scripture actually says to that need — not with clichés, but with daily time in God\\u2019s Word, honest reflection, and one small step at a time. Today, simply begin. Read the passage. Underline one phrase. Ask God to meet you in these forty days.`,
  pray:`Father, You know exactly where this finds me. Meet me in these days. Open Your Word, open my heart, and lead me one step at a time. In Jesus\\u2019 name, amen.`,
  q:`What made you pick up this campaign — and what do you hope is different at the end of it?`,
  step:`Tell one person you\\u2019re starting this journey, and invite them to do it with you.`},
 {dn:'Day 02',dl:wk,theme:'The Truth Underneath',v:'Return to the anchor passage and read it in context.',r:SCR+' (NIV)',
  body:`Yesterday you began. Today we slow down inside the anchor passage for this whole journey — ${SCR}. Read the verses around it. Notice who it was written to, and what was happening when it was written.<br><br>Scripture speaks to <em>${S.toLowerCase()}</em> not as an idea but as a promise with God\\u2019s character behind it. Write the anchor verse somewhere you\\u2019ll see it every day for the rest of this campaign.`,
  pray:`Lord, plant this truth deeper than my circumstances. Let it become the sentence my heart says back when the old sentence starts again. Amen.`,
  q:`Which word or phrase in the anchor passage speaks most directly to your situation right now?`,
  step:`Write the anchor verse on a card and put it where you\\u2019ll see it tomorrow morning.`},
 {dn:'Day 03',dl:wk,theme:'One Small Obedience',v:'Ask: what is one thing this passage invites me to do?',r:SCR+' (NIV)',
  body:`Forty days doesn\\u2019t change a life. Forty small obediences do. Today the journey turns practical: not what you feel about <em>${THEME.toLowerCase()}</em>, but what you\\u2019ll do about it before the sun goes down.<br><br>Your spiritual partner matters here. Every Lifetogether campaign is designed to be walked with someone — a friend, a spouse, a small group. Today\\u2019s step is the first conversation. It will feel small. It is how everything starts.`,
  pray:`God, save me from a faith of good intentions. Show me today\\u2019s one small obedience, and give me the courage to take it before tonight. Amen.`,
  q:`What is the smallest concrete step you could take today in the direction this campaign is pointing?`,
  step:`Take it — then text your spiritual partner one sentence about what you did.`}];
}
window.NEEDS=%s;
const DEVO=(ID==='C0361')?GOIA_DEVO:genDevo();
""" % (json.dumps(HUEHEX), json.dumps({t[0]: t[3] for t in THEMES}, ensure_ascii=False))
c = c.replace("const tabs=document.getElementById('daytabs');", driver + "\nconst tabs=document.getElementById('daytabs');")
# remove the old fmt click handler (now handled in driver)
c = c.replace("""document.querySelectorAll('#fmts .fmt').forEach(f=>f.addEventListener('click',()=>{
  document.querySelectorAll('#fmts .fmt').forEach(x=>x.classList.remove('on'));f.classList.add('on');}));""", "")
open('/home/claude/site/out/campaign.html', 'w').write(c)

# God Owns It All actual id
goia = [r for r in rows if r[0] == 'God Owns It All'][0]
print('GOIA id:', goia[9])

# ---------- index & others ----------
shutil.copy('/mnt/user-data/uploads/index.html', '/home/claude/site/out/index.html')
shutil.copy('/mnt/user-data/uploads/finder.html', '/home/claude/site/out/finder.html')
shutil.copy('/mnt/user-data/uploads/nav.html', '/home/claude/site/out/nav.html')
print('done phase 1')
