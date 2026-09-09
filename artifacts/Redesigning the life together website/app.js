/* ============================================================
   LIFETOGETHER PLATFORM — shared data + behavior
   Channels & flagship campaigns sourced from the master catalog
   (16,379 items · 23 channels · 383 Grade-AA flagships).
   ============================================================ */

const CHANNELS = [
  {slug:"purpose-calling",     name:"Purpose & Calling",                    v:"--c-purpose",    n:2089},
  {slug:"identity",            name:"Identity & Significance",              v:"--c-identity",   n:95},
  {slug:"community",           name:"Community & Belonging",                v:"--c-community",  n:945},
  {slug:"prayer",              name:"Prayer, Worship & Disciplines",        v:"--c-prayer",     n:744},
  {slug:"money",               name:"Money & Stewardship",                  v:"--c-money",      n:762},
  {slug:"generosity",          name:"Generosity & Legacy",                  v:"--c-generosity", n:464},
  {slug:"family-legacy",       name:"Family Legacy & Generations",          v:"--c-family",     n:1672},
  {slug:"marriage",            name:"Marriage & Relationships",             v:"--c-marriage",   n:419},
  {slug:"parenting",           name:"Parenting & Family",                   v:"--c-parenting",  n:461},
  {slug:"emotional-health",    name:"Peace & Emotional Health",             v:"--c-emotional",  n:626},
  {slug:"health-healing",      name:"Health, Healing & Care",               v:"--c-health",     n:353},
  {slug:"freedom",             name:"Freedom & Recovery",                   v:"--c-freedom",    n:294},
  {slug:"seasons-of-life",     name:"Seasons of Life",                      v:"--c-seasonslife",n:562},
  {slug:"work",                name:"Work & Marketplace",                   v:"--c-work",       n:1427},
  {slug:"leadership",          name:"Leadership & Serving",                 v:"--c-leadership", n:779},
  {slug:"church-vision",       name:"Church Vision & Values",               v:"--c-vision",     n:1001},
  {slug:"ministries",          name:"Ministries & Nonprofits",              v:"--c-ministries", n:330},
  {slug:"mission",             name:"Mission & Neighbor",                   v:"--c-mission",    n:779},
  {slug:"calendar",            name:"Seasons & the Church Calendar",        v:"--c-calendar",   n:785},
  {slug:"red-letter",          name:"Life of Christ & Red Letter",          v:"--c-redletter",  n:1182},
  {slug:"bible",               name:"Bible & Scripture Studies",            v:"--c-bible",      n:345},
  {slug:"doubt",               name:"Doubt & Honest Faith",                 v:"--c-doubt",      n:109, isnew:true},
  {slug:"digital",             name:"Digital Discernment & Faith in the Age of AI", v:"--c-digital", n:156, isnew:true},
];
const CH = Object.fromEntries(CHANNELS.map(c=>[c.slug,c]));

/* Curated Grade-AA flagships (real catalog titles). motif: 0 dots · 1 arcs · 2 rays */
const FLAGSHIPS = [
  {slug:"life-together", t:"40 Days of Life Together", s:"The flagship groups launch campaign — a whole church, walking together.", ch:"community", days:40, star:1, motif:1},
  {slug:"prayer",        t:"40 Days of Prayer", s:"The campaign for every church — one congregation, praying as one.", ch:"prayer", days:40, star:1, motif:0},
  {slug:"purpose",       t:"40 Days of Purpose", s:"The classic that started the movement. What on earth am I here for?", ch:"purpose-calling", days:40, star:1, motif:2},
  {slug:"god-owns-it-all", t:"God Owns It All", s:"Biblical financial wisdom with Ron Blue — freedom starts with ownership.", ch:"money", days:40, star:1, motif:0},
  {slug:"living-light",  t:"Living Light", s:"40 days of freedom from anxiety — a gentle, honest walk toward peace.", ch:"emotional-health", days:40, star:1, motif:1},
  {slug:"a-life-worth",  t:"A Life Worth", s:"Leaving faith, wisdom, and purpose to the next generation.", ch:"family-legacy", days:40, star:1, motif:2},
  {slug:"easter",        t:"30 Days to Easter", s:"The Lenten journey through the Passion narrative.", ch:"calendar", days:30, star:1, motif:1, badge:"SEASONAL"},
  {slug:"unplugged",     t:"Unplugged", s:"40 days of intentional life in a digital world.", ch:"digital", days:40, star:1, motif:0, badge:"NEW"},
  {slug:"better-together", t:"Better Together", s:"Biblical community and what it actually takes.", ch:"community", days:40, star:1, motif:2},
  {slug:"soul-care",     t:"Soul Care", s:"Psalm 23 and the rest your soul needs.", ch:"emotional-health", days:40, star:1, motif:0},
  {slug:"shape",         t:"SHAPE", s:"A 40-day personal ministry discovery journey.", ch:"leadership", days:40, star:1, motif:1},
  {slug:"proverbs",      t:"40 Days in Proverbs", s:"Wisdom for every decision you will make this year.", ch:"bible", days:40, star:1, motif:2},
  {slug:"built-to-last", t:"Built to Last", s:"Marriage on the rock — Matthew 7:24.", ch:"marriage", days:40, star:1, motif:0},
  {slug:"home-run",      t:"Home Run", s:"Building the family that wins at what matters most.", ch:"parenting", days:40, star:1, motif:1},
  {slug:"generosity",    t:"Generosity", s:"Why does giving change everything? 2 Corinthians 9 applied.", ch:"generosity", days:40, star:1, motif:2},
  {slug:"healing",       t:"40 Days of Healing", s:"Everyone is healing from something.", ch:"health-healing", days:40, star:1, motif:0},
  {slug:"made-for-this", t:"Made for This", s:"Young adult calling and Kingdom purpose.", ch:"seasons-of-life", days:40, star:1, motif:1},
  {slug:"rhythms",       t:"Rhythms of Grace", s:"Daily and weekly practices that sustain a life.", ch:"freedom", days:40, star:1, motif:2},
  {slug:"new-year",      t:"New Year Reset", s:"40 days of starting over with God.", ch:"calendar", days:40, star:1, motif:0, badge:"SEASONAL"},
  {slug:"living-sent",   t:"Living Sent", s:"A 40-day journey to everyday mission.", ch:"mission", days:40, star:1, motif:1},
  {slug:"beloved",       t:"Beloved", s:"40 days of living in God's love.", ch:"identity", days:40, star:1, motif:2},
  {slug:"steward-heart", t:"Heart of a Steward", s:"40 days of faithful influence — time, talent, and treasure.", ch:"generosity", days:40, star:1, motif:1},
  {slug:"honest-faith",  t:"Honest Faith", s:"Doubt, questions, and the God who isn't afraid of either.", ch:"doubt", days:40, star:1, motif:0, badge:"NEW"},
  {slug:"the-prodigal",  t:"The Prodigal", s:"40 days in the most famous parable ever told.", ch:"red-letter", days:40, star:1, motif:2},
];
const FLAG = Object.fromEntries(FLAGSHIPS.map(f=>[f.slug,f]));

/* ---------- deterministic cover engine ---------- */
function cssVal(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim()}
function hexToRgb(h){h=h.replace('#','');return [parseInt(h.slice(0,2),16),parseInt(h.slice(2,4),16),parseInt(h.slice(4,6),16)]}
function tint(hex,amt){const [r,g,b]=hexToRgb(hex);const m=c=>Math.round(c+(255-c)*amt);return `rgb(${m(r)},${m(g)},${m(b)})`}
function shade(hex,amt){const [r,g,b]=hexToRgb(hex);const m=c=>Math.round(c*(1-amt));return `rgb(${m(r)},${m(g)},${m(b)})`}

function coverSVG(item){
  const c = cssVal(CH[item.ch].v) || '#237A52';
  const bg1 = tint(c,.90), bg2 = tint(c,.78), fg = shade(c,.12);
  const filled = Math.min(item.days||40,40);
  let motif = '';
  if(item.motif===0){ /* 40-day dot grid, centered */
    for(let i=0;i<40;i++){
      const x=60+(i%8)*20, y=64+Math.floor(i/8)*22;
      motif+=`<circle cx="${x}" cy="${y}" r="4.6" fill="${fg}" opacity="${i<filled?.8:.2}"/>`;
    }
  } else if(item.motif===1){ /* rising concentric arcs */
    for(let i=0;i<5;i++){
      motif+=`<circle cx="130" cy="322" r="${58+i*36}" fill="none" stroke="${fg}" stroke-width="2.6" opacity="${.55-i*.09}"/>`;
    }
    motif+=`<circle cx="130" cy="120" r="12" fill="${fg}" opacity=".85"/>`;
  } else { /* rays descending from the arch keystone */
    for(let i=0;i<9;i++){
      const a=(i-4)*17*Math.PI/180;
      const x2=130+Math.sin(a)*230, y2=34+Math.cos(a)*230;
      motif+=`<line x1="130" y1="34" x2="${x2}" y2="${y2}" stroke="${fg}" stroke-width="2.3" opacity="${.46-Math.abs(i-4)*.06}"/>`;
    }
    motif+=`<circle cx="130" cy="34" r="11" fill="${fg}" opacity=".9"/><circle cx="130" cy="34" r="26" fill="none" stroke="${fg}" stroke-width="2.2" opacity=".5"/>`;
  }
  return `<svg viewBox="0 0 260 300" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <defs><linearGradient id="g${item.slug}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="${bg1}"/><stop offset="1" stop-color="${bg2}"/>
    </linearGradient></defs>
    <rect width="260" height="300" fill="url(#g${item.slug})"/>
    ${motif}
    <rect x="0" y="200" width="260" height="100" fill="url(#f${item.slug})"/>
    <defs><linearGradient id="f${item.slug}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="${bg1}" stop-opacity="0"/><stop offset="1" stop-color="#ffffff" stop-opacity=".82"/>
    </linearGradient></defs>
  </svg>`;
}

function campaignCard(item, opts={}){
  const ch = CH[item.ch];
  const href = opts.href || 'campaign.html';
  return `<a class="arch-card rv" href="${href}" aria-label="${item.t}">
    <div class="cover">
      ${coverSVG(item)}
      <span class="cv-days">${item.days} DAYS</span>
      ${item.star?'<span class="cv-star">★</span>':''}
      ${item.badge?`<span class="cv-new">${item.badge}</span>`:''}
      <span class="cv-title">${item.t}</span>
    </div>
    <div class="card-meta">
      <span class="ch"><i style="background:var(${ch.v})"></i>${ch.name}</span>
      <p class="sub">${item.s}</p>
    </div>
  </a>`;
}

function renderCards(sel, items, opts){
  const el=document.querySelector(sel);
  if(el) el.innerHTML=items.map(i=>campaignCard(i,opts)).join('');
}

/* ---------- nav ---------- */
function initNav(){
  const burger=document.querySelector('.nav-burger');
  const menu=document.querySelector('.mobile-menu');
  if(burger&&menu){
    burger.addEventListener('click',()=>{
      menu.classList.toggle('open');
      burger.classList.toggle('x');
      document.body.style.overflow=menu.classList.contains('open')?'hidden':'';
    });
  }
}

/* ---------- reveal on scroll ---------- */
function initReveal(){
  if(matchMedia('(prefers-reduced-motion: reduce)').matches){
    document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'));return;
  }
  const io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}
  }),{threshold:.12,rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.rv').forEach((e,i)=>{
    e.style.transitionDelay=(Math.min(i%6,4)*60)+'ms';io.observe(e)
  });
}

document.addEventListener('DOMContentLoaded',()=>{initNav();initReveal();});
