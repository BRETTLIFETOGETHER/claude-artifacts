/* gen_covers3.js — every campaign gets its own design recipe.
   Independent seeded axes: layout archetype (10) × background treatment (14) ×
   gradient variant (5) × motif combination (primary + up to 2 secondaries from 58)
   × divider style (8) × title alignment/treatment. A design fingerprint
   (layout|bg|grad|motifs|divider|align) is enforced UNIQUE across all 1,252 —
   collisions reroll with a salt. Titles stay inside the crop-safe band. */
const fs=require('fs');
const {PRIM, KIND, GOLD, st, fillW}=require('./motifs3');
global.window={};
eval(fs.readFileSync('/home/claude/site/data.js','utf8'));
const ROWS=window.CAMPAIGNS, CATS=window.CATS;
const HUE={1:['#16A88F','#0C5A4E'],2:['#C8484C','#7E2326'],3:['#4F86E0','#26417F'],4:['#E0703F','#8A3A1E'],5:['#E8A52E','#9A6810'],6:['#36A85E','#176233'],7:['#7B5FE0','#3F2E86'],8:['#E2542F','#8A2A14'],9:['#5A6B8C','#2E3A52'],10:['#C99A3C','#7E601C'],11:['#3E8FB0','#1D4B60'],12:['#B0578D','#5F2A4C'],13:['#C86B8F','#7A2F4E'],14:['#8C6BD0','#4A2F86'],15:['#3FA796','#1E5C52']};
const W=600,H=800,CX=300;
function seedOf(s){let h=5381;for(let i=0;i<s.length;i++)h=((h<<5)+h+s.charCodeAt(i))>>>0;return h;}
function rng(seed){let a=seed>>>0;return function(){a|=0;a=(a+0x6D2B79F5)|0;let t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&apos;');
const place=(name,x,y,s,r,op)=> (op?`<g opacity="${op}">`:'')+`<g transform="translate(${x.toFixed(1)} ${y.toFixed(1)}) scale(${s.toFixed(3)}) translate(-300 -195)">${PRIM[name](r)}</g>`+(op?'</g>':'');

/* ---------------- keyword rules ---------------- */
const RULES=[
 [/torch|passing the torch|baton|relay/,'torch'],[/\bown|ownership|deed|belongs/,'keys'],
 [/heart\b|love\b|beloved/,'heart'],[/enough|content|simplic|simple\b|less\b|minimal/,'scales'],
 [/anchor|steadfast|unshak|immovable/,'anchor'],[/storm|anxi|fear\b|afraid|worry|overwhelm|troubled/,'lighthouse'],
 [/dawn|morning|sunrise|new day|awaken|arise/,'sunrise'],[/harvest|wheat|sow\b|reap/,'wheat'],
 [/seed|grow|root|plant|soil|fruit|flourish|bloom/,'sprout'],[/mountain|climb|summit|higher|peak/,'mountains'],
 [/journey|path|walk\b|road|steps|pilgrim|wander/,'path'],[/\bword\b|scripture|bible|book|read|study|devot/,'book'],
 [/pray|prayer|interced/,'prayer'],[/generos|give\b|giving|gift|offering|tithe|open.?hand/,'gift'],
 [/money|steward|wealth|rich|treasure|invest|budget|financ|provision|debt|save|fund/,'coins'],
 [/legacy|inherit|generation|grandparent|grand\b|estate|heirloom/,'tree'],
 [/heir|launch|arrow|ready\b|prepare|commission/,'arrowlaunch'],[/family|home\b|house\b|parent|household|roof/,'home'],
 [/marriage|marri|couple|wedding|spouse|two become/,'rings'],[/child|kids|children|youth|young/,'kite'],
 [/king\b|kingdom|crown|reign|throne|majesty/,'crown'],[/cross|gospel|redeem|salvation|calvary|savior|grace/,'cross'],
 [/work\b|business|vocation|market|labor|career|calling|succession|office/,'compass'],
 [/wisdom|wise|discern|decision|understand/,'lamp'],[/season|time\b|clock|number our|years|chapter/,'sundial'],
 [/water|well\b|river|thirst|spring\b/,'well'],[/door|open\b|invite|welcome|threshold/,'door'],
 [/table|meal|bread|feast|supper|hospitality|dinner/,'table'],[/fire|flame|spirit\b|revival|burn/,'flame'],
 [/star|night\b|midnight/,'stars'],[/shepherd|sheep|flock|pasture/,'shepherd'],
 [/build|foundation|cornerstone|construct|blueprint/,'blueprint'],[/rest\b|sabbath|still\b|quiet|slow\b|pause/,'restnight'],
 [/battle|fight|armor|stand firm|warfare|struggle/,'shield'],[/free|freedom|soar|wings|fly\b|release/,'bird'],
 [/forgiv|reconcil|mercy/,'chainbreak'],[/mission|nations|world|global|neighbor|witness|reach|multiply|send/,'globe'],
 [/peace\b|dove|holy spirit/,'dove'],[/voyage|sail|sea\b|ship|boat|waters/,'sail'],
 [/bridge|connect|between|gap/,'bridge'],[/today|now\b|urgen|moment|fleeting/,'hourglass'],
 [/call\b|calling|awake|summon|bell/,'bell'],[/enter|gate|threshold/,'gate'],
 [/promise|covenant|rainbow/,'rainbow'],[/story|history|remember\b|memoir|testimony/,'scroll'],
 [/communion|cup\b|remembrance/,'chalice'],[/fisher|evangel|catch/,'fishnet'],
 [/dream|vision|ladder/,'ladder'],[/dwell|sojourn|tabernacle|tent/,'tent'],
 [/city|urban|neighborhood/,'skyline'],[/abide|vine|branch/,'vine'],
 [/commit|vow|bond|knot/,'knot'],[/guide|direction|north|true north/,'northstar'],
 [/follow|footsteps|walk with/,'footsteps'],[/together|unity|one another|community|belong/,'together'],
 [/candle|light\b|shine|lamp/,'candles'],[/message|invitation|letter|sent\b/,'letter'],
 [/hope\b|window|light of/,'window'],[/faith|trust|believ/,'anchor'],[/identity|purpose|who (i|you) (am|are)/,'compass'],
];
const CAT_FALLBACK={1:'coins',2:'scales',3:'gift',4:'globe',5:'tree',6:'arrowlaunch',7:'home',8:'compass',9:'lamp',10:'book',11:'sundial',12:'sunrise',13:'well',14:'path',15:'sprout'};
const CAT_ACCENTS={1:['keys','scroll'],2:['restnight','olive'],3:['heart','together'],4:['northstar','sail'],5:['scroll','knot'],6:['ladder','northstar'],7:['candles','window'],8:['hourglass','ladder'],9:['northstar','scroll'],10:['candles','scroll'],11:['hourglass','rainbow'],12:['dove','window'],13:['dove','olive'],14:['footsteps','northstar'],15:['vine','olive']};
function motifsFor(row,r){
 const hay=(row[0]+' '+(row[10]||'')+' '+(row[1]||'')).toLowerCase();
 const hits=[]; for(const [re,n] of RULES){ if(re.test(hay)&&!hits.includes(n)) hits.push(n); if(hits.length>=3)break; }
 let primary=hits[0]||CAT_FALLBACK[row[2]]||'path';
 let secs=hits.slice(1,3);
 if(!secs.length){ const acc=CAT_ACCENTS[row[2]]||['northstar']; secs=[acc[Math.floor(r()*acc.length)]]; }
 secs=secs.filter(n=>n!==primary).slice(0,2);
 return {primary, secs};
}

/* ---------------- backgrounds ---------------- */
const GRADS=[[0,0,0,1],[0,0,1,1],[1,0,0,1],[0,0.2,1,0.8],[0.5,0,0.5,1]];
function mix(hex,hex2,t){const a=parseInt(hex.slice(1),16),b=parseInt(hex2.slice(1),16);
 const c=[16,8,0].map(sh=>Math.round(((a>>sh&255)*(1-t))+((b>>sh&255)*t)));
 return '#'+c.map(x=>x.toString(16).padStart(2,'0')).join('');}
const FIELDS=[
 (r)=>'' ,
 (r)=>`<polygon points="0,0 ${W},0 ${W},${(H*0.34+r()*80).toFixed(0)} 0,${(H*0.6+r()*80).toFixed(0)}" fill="rgba(0,0,0,.14)"/>`,
 (r)=>`<circle cx="${(r()*W).toFixed(0)}" cy="${(120+r()*200).toFixed(0)}" r="${(220+r()*120).toFixed(0)}" fill="rgba(255,255,255,.06)"/>`,
 (r)=>{const cx=r()<.5?0:W, cy=r()<.5?0:H; let s='<g '+st(.07,2)+'>'; for(let a=0;a<Math.PI*2;a+=Math.PI/10) s+=`<line x1="${cx}" y1="${cy}" x2="${(cx+Math.cos(a)*1100).toFixed(0)}" y2="${(cy+Math.sin(a)*1100).toFixed(0)}"/>`; return s+'</g>';},
 (r)=>{let s='<g '+st(.07,2.2)+'>'; for(let i=1;i<9;i++) s+=`<path d="M ${-100} ${H+60-i*90} Q ${CX} ${H-40-i*118} ${W+100} ${H+60-i*90}"/>`; return s+'</g>';},
 (r)=>{const cx=r()*W, cy=r()*H; let s='<g '+st(.055,1.3)+'>'; for(let i=1;i<13;i++) s+=`<circle cx="${cx.toFixed(0)}" cy="${cy.toFixed(0)}" r="${i*64}"/>`; return s+'</g>';},
 (r)=>{let s='<g '+fillW(.06)+'>'; const g=36; for(let x=18;x<W;x+=g) for(let y=18;y<H;y+=g) s+=`<circle cx="${x}" cy="${y}" r="1.6"/>`; return s+'</g>';},
 (r)=>{let s='<g '+st(.055,1.4)+'>'; for(let x=-800;x<W+100;x+=28) s+=`<line x1="${x}" y1="0" x2="${x+520}" y2="${H}"/>`; return s+'</g>';},
 (r)=>{let s='<g '+st(.05,1.2)+'>'; for(let y=-40;y<H+40;y+=32){let d=`M -20 ${y}`; for(let x=-20;x<=W+20;x+=44) d+=` l 22 -12 l 22 12`; s+=`<path d="${d}"/>`;} return s+'</g>';},
 (r)=>{let s='<g '+st(.055,1.3)+'>'; for(let y=0;y<H+60;y+=48) for(let x=((y/48)%2)*33;x<W+40;x+=66) s+=`<path d="M ${x-33} ${y} A 33 33 0 0 1 ${x+33} ${y}"/>`; return s+'</g>';},
 (r)=>{let s='<g '+st(.05,1.3)+'>'; for(let y=24;y<H;y+=56) for(let x=((y/56)%2)*32+18;x<W;x+=64) s+=`<path d="M ${x-8} ${y} H ${x+8} M ${x} ${y-8} V ${y+8}"/>`; return s+'</g>';},
 (r)=>{let s='<g '+fillW(.07)+'>'; for(let y=30;y<H;y+=44){const rr=1+3.4*(y/H); for(let x=24;x<W;x+=44) s+=`<circle cx="${x}" cy="${y}" r="${rr.toFixed(1)}"/>`;} return s+'</g>';},
 (r)=>`<rect x="34" y="34" width="${W-68}" height="${H-68}" rx="14" fill="rgba(0,0,0,.1)"/><rect x="46" y="46" width="${W-92}" height="${H-92}" rx="10" fill="rgba(255,255,255,.05)"/>`,
 (r)=>{let s=''; for(let i=0;i<3;i++) s+=`<rect x="${(i*W/3).toFixed(0)}" y="0" width="${(W/3).toFixed(0)}" height="${H}" fill="rgba(${i%2?'0,0,0':'255,255,255'},.05)"/>`; return s;},
];

/* ---------------- typography ---------------- */
function balancedWrap(t,per){const words=t.split(' ');if(t.length<=per)return[t];
 const target=Math.min(4,Math.ceil(t.length/per));const lines=[];let remaining=words.slice();
 for(let i=0;i<target;i++){const slots=target-i;const budget=Math.ceil(remaining.join(' ').length/slots);let cur='';
  while(remaining.length&&(cur.length===0||(cur+' '+remaining[0]).length<=Math.max(budget,per*0.72))){
   if((cur+' '+remaining[0]).trim().length>per&&cur)break;cur=(cur+' '+remaining.shift()).trim();}
  lines.push(cur);if(!remaining.length)break;}
 if(remaining.length)lines[lines.length-1]+=' '+remaining.join(' ');return lines.filter(Boolean);}
function titleBlock(title,sub,maxW,boost){
 const len=title.length;
 let fsz=(len<=14?58:len<=22?50:len<=30?44:len<=42?38:33)*(boost||1);
 const per=Math.floor(maxW/(fsz*0.52));
 let lines=balancedWrap(title,per);
 if(lines.length>4){lines=lines.slice(0,4);lines[3]=lines[3].replace(/\s?\S*$/,'')+'…';}
 const maxLine=Math.max(...lines.map(l=>l.length));
 if(maxLine*0.52*fsz>maxW)fsz=Math.floor(maxW/(maxLine*0.52));
 const lh=fsz*1.12;
 const subLines=(sub&&sub.length<=84)?balancedWrap(sub,Math.floor(maxW/(18.5*0.5))).slice(0,2):[];
 return{fsz,lines,lh,subLines};}

const DIVIDERS=[
 y=>`<g ${st(.55,1.8)}><line x1="${CX-70}" y1="${y}" x2="${CX-16}" y2="${y}"/><line x1="${CX+16}" y1="${y}" x2="${CX+70}" y2="${y}"/></g><path d="M ${CX} ${y-6} l 6 6 -6 6 -6 -6 z" fill="${GOLD}"/>`,
 y=>`<g ${st(.5,1.6)}><line x1="${CX-78}" y1="${y-3}" x2="${CX+78}" y2="${y-3}"/><line x1="${CX-56}" y1="${y+4}" x2="${CX+56}" y2="${y+4}"/></g>`,
 y=>`<g ${fillW(.6)}>${[-40,-20,0,20,40].map(d=>`<circle cx="${CX+d}" cy="${y}" r="2.4"/>`).join('')}</g><circle cx="${CX}" cy="${y}" r="3.4" fill="${GOLD}"/>`,
 y=>`<g ${st(.55,2)}><path d="M ${CX-40} ${y+4} l 14 -9 14 9 M ${CX+12} ${y+4} l 14 -9 14 9"/></g>`,
 y=>`<g ${st(.55,2)}><path d="M ${CX-58} ${y} q 10 -12 22 0 q -10 12 -22 0 z M ${CX+36} ${y} q 10 -12 22 0 q -10 12 -22 0 z"/><line x1="${CX-24}" y1="${y}" x2="${CX+24}" y2="${y}"/></g>`,
 y=>`<path d="M ${CX} ${y-8} l 2.5 5.5 6 .8 -4.4 4.2 1.1 6 -5.2 -3 -5.2 3 1.1 -6 -4.4 -4.2 6 -.8 z" fill="${GOLD}"/><g ${st(.5,1.6)}><line x1="${CX-64}" y1="${y}" x2="${CX-16}" y2="${y}"/><line x1="${CX+16}" y1="${y}" x2="${CX+64}" y2="${y}"/></g>`,
 y=>`<path d="M ${CX-56} ${y} q 14 -10 28 0 q 14 10 28 0 q 14 -10 28 0 q 14 10 28 0" ${st(.55,2)} transform="translate(-14 0)"/>`,
 y=>`<g ${st(.55,2)}><path d="M ${CX} ${y-8} v 16 M ${CX-8} ${y} h 16"/><line x1="${CX-66}" y1="${y}" x2="${CX-20}" y2="${y}"/><line x1="${CX+20}" y1="${y}" x2="${CX+66}" y2="${y}"/></g>`,
];

function textStack(o){ /* {x,anchor,catLabel,tb,divIdx,treat,yCenter} */
 const {x,anchor,catLabel,tb,divIdx,treat}=o;
 const blockH=26+26+tb.lines.length*tb.lh+(tb.subLines.length?18+tb.subLines.length*24:0);
 let y=(o.yCenter||450)-blockH/2+18;
 let out='', plate='';
 const wMax=Math.max(...tb.lines.map(l=>l.length))*tb.fsz*0.52;
 if(treat==='plate'){
  const pw=Math.min(520,wMax+70), ph=blockH+34;
  plate=`<rect x="${(anchor==='middle'?CX-pw/2:x-26).toFixed(0)}" y="${(y-34).toFixed(0)}" width="${pw.toFixed(0)}" height="${ph.toFixed(0)}" rx="12" fill="rgba(0,0,0,.30)" stroke="rgba(255,255,255,.25)" stroke-width="1.6"/>`;
 }
 if(treat==='ribbon'){
  const pw=Math.min(540,wMax+90), ph=blockH+30;
  const x0=(anchor==='middle'?CX-pw/2:x-30);
  plate=`<path d="M ${x0} ${y-30} h ${pw} l -14 ${ph/2} 14 ${ph/2} h -${pw} l 14 -${ph/2} z" fill="rgba(0,0,0,.28)" stroke="rgba(255,255,255,.22)" stroke-width="1.5"/>`;
 }
 if(treat==='rules'){
  plate=`<g ${st(.5,2)}><line x1="${anchor==='middle'?CX-150:x}" y1="${y-30}" x2="${anchor==='middle'?CX+150:x+300}" y2="${y-30}"/><line x1="${anchor==='middle'?CX-150:x}" y1="${y+blockH-14}" x2="${anchor==='middle'?CX+150:x+300}" y2="${y+blockH-14}"/></g>`;
 }
 out+=`<text x="${x}" y="${y}" text-anchor="${anchor}" font-family="Verdana, Arial, sans-serif" font-size="13.5" letter-spacing="4.5" ${fillW(.85)} font-weight="bold">${catLabel}</text>`;
 y+=26;
 if(anchor==='middle') out+=DIVIDERS[divIdx](y);
 else out+=`<g ${st(.55,2)}><line x1="${x}" y1="${y}" x2="${x+64}" y2="${y}"/></g><path d="M ${x+74} ${y-5} l 5 5 -5 5 -5 -5 z" fill="${GOLD}"/>`;
 y+=26+tb.fsz*0.82;
 for(const L of tb.lines){ out+=`<text x="${x}" y="${y.toFixed(0)}" text-anchor="${anchor}" font-size="${tb.fsz}" fill="#FFFFFF" font-weight="600">${esc(L)}</text>`; y+=tb.lh; }
 if(tb.subLines.length){ y+=6;
  out+=`<g ${st(.4,1.6)}><line x1="${anchor==='middle'?CX-46:x}" y1="${(y-16).toFixed(0)}" x2="${anchor==='middle'?CX+46:x+92}" y2="${(y-16).toFixed(0)}"/></g>`;
  for(const L of tb.subLines){ out+=`<text x="${x}" y="${y.toFixed(0)}" text-anchor="${anchor}" font-size="18.5" font-style="italic" ${fillW(.88)}>${esc(L)}</text>`; y+=24; } }
 return plate+out;
}
const ring=(x,y)=>`<circle cx="${x}" cy="${y}" r="27" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="2.2"/><text x="${x}" y="${y+8}" text-anchor="middle" font-size="21" fill="#FFFFFF" font-family="Georgia, serif">NUM</text>`;
const frameKey=`<rect x="17" y="17" width="${W-34}" height="${H-34}" rx="10" ${st(.3,2)}/>`;
const frameTicks=`<g ${st(.4,2.2)}>${[[24,24,1,1],[W-24,24,-1,1],[24,H-24,1,-1],[W-24,H-24,-1,-1]].map(([x,y,sx,sy])=>`<path d="M ${x} ${y+sy*22} V ${y} H ${x+sx*22}"/>`).join('')}</g>`;
const frameDouble=`<rect x="14" y="14" width="${W-28}" height="${H-28}" rx="12" ${st(.28,1.6)}/><rect x="24" y="24" width="${W-48}" height="${H-48}" rx="9" ${st(.22,1.4)}/>`;

/* ---------------- layouts ---------------- */
/* each returns {art, text, ringPos, frame} given ctx {r, primary, secs, tb, catLabel, divIdx} */
const LAYOUTS=[
 c=>({ art: place(c.primary,CX,205,0.86,c.r) + (c.secs[0]?place(c.secs[0],CX,688,0.4,c.r):''),
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'bare'}), ringPos:[CX,76], frame:frameKey }),
 c=>({ art: `<circle cx="${CX}" cy="200" r="148" ${st(.4,2.2)}/><circle cx="${CX}" cy="200" r="160" ${st(.22,1.6)} stroke-dasharray="2 8"/>` + place(c.primary,CX,202,0.56,c.r) + (c.secs[0]?place(c.secs[0],110,690,0.34,c.r):'') + (c.secs[1]?place(c.secs[1],490,690,0.34,c.r):''),
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'bare'}), ringPos:[W-58,62], frame:frameTicks }),
 c=>({ art: place(c.primary,CX,405,1.55,c.r,0.3) + (c.secs[0]?place(c.secs[0],96,120,0.4,c.r):''),
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'plate'}), ringPos:[CX,76], frame:`<g ${st(.35,2.4)}><line x1="30" y1="120" x2="30" y2="${H-120}"/><line x1="${W-30}" y1="120" x2="${W-30}" y2="${H-120}"/></g>` }),
 c=>({ art: place(c.primary,190,200,0.68,c.r) + (c.secs[0]?place(c.secs[0],452,660,0.46,c.r):''),
   text: textStack({x:66,anchor:'start',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'bare'}), ringPos:[W-58,62], frame:frameKey }),
 c=>({ art: `<g ${st(.4,2)}><line x1="40" y1="122" x2="${W-40}" y2="122"/><line x1="40" y1="330" x2="${W-40}" y2="330"/></g>` + place(c.primary,CX,226,0.82,c.r) + (c.secs[0]?place(c.secs[0],CX,700,0.38,c.r):''),
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'rules'}), ringPos:[CX,72], frame:'' }),
 c=>({ art: `<path d="M 96 330 V 210 A 204 204 0 0 1 504 210 V 330" ${st(.42,2.4)}/><path d="M 118 330 V 214 A 182 182 0 0 1 482 214 V 330" ${st(.25,1.8)}/>` + place(c.primary,CX,218,0.66,c.r) + (c.secs[0]?place(c.secs[0],CX,694,0.4,c.r):''),
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'bare'}), ringPos:[CX,330-246], frame:frameTicks }),
 c=>({ art: place(c.primary,CX,650,0.72,c.r) + (c.secs[0]?place(c.secs[0],CX,152,0.44,c.r):''),
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'ribbon',yCenter:432}), ringPos:[W-58,62], frame:frameDouble }),
 c=>({ art: `<g ${st(.4,2)}><line x1="72" y1="96" x2="72" y2="${H-96}"/>${[180,400,620].map(y=>`<path d="M 72 ${y} l 5 -5 5 5 -5 5 z" fill="${GOLD}" stroke="none"/>`).join('')}</g>` + place(c.primary,352,208,0.76,c.r) + (c.secs[0]?place(c.secs[0],382,672,0.4,c.r):''),
   text: textStack({x:104,anchor:'start',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'bare'}), ringPos:[64,62], frame:'' }),
 c=>({ art: `<circle cx="${CX}" cy="212" r="168" ${st(.3,1.8)} stroke-dasharray="1 8"/>` + place(c.primary,CX,208,0.62,c.r) + (c.secs[0]?place(c.secs[0],CX+168*Math.cos(2.4),212+168*Math.sin(2.4),0.26,c.r):'') + (c.secs[1]?place(c.secs[1],CX+168*Math.cos(0.6),212+168*Math.sin(0.6),0.26,c.r):'') + `<circle cx="${CX+168*Math.cos(3.8)}" cy="${212+168*Math.sin(3.8)}" r="5" fill="${GOLD}"/>`,
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:c.tb,divIdx:c.divIdx,treat:'bare'}), ringPos:[W-58,H-58], frame:'' }),
 c=>({ art: `<g ${st(.5,2.6)}><line x1="60" y1="208" x2="${W-60}" y2="208"/><line x1="60" y1="620" x2="${W-60}" y2="620"/></g>` + place(c.primary,CX,300,0.4,c.r) + (c.secs[0]?place(c.secs[0],CX,690,0.34,c.r):''),
   text: textStack({x:CX,anchor:'middle',catLabel:c.catLabel,tb:{...c.tb},divIdx:c.divIdx,treat:'bare',yCenter:468}), ringPos:[CX,150], frame:frameKey }),
];

/* ---------------- cover ---------------- */
function build(row,salt){
 const id=row[9], title=row[0], sub=row[1]||'', cat=row[2];
 const [A,B]=HUE[cat]||HUE[5];
 const r=rng(seedOf(id)+salt*7919);
 const layout=Math.floor(r()*LAYOUTS.length);
 const bg=Math.floor(r()*FIELDS.length);
 const grad=Math.floor(r()*GRADS.length);
 const divIdx=Math.floor(r()*DIVIDERS.length);
 const {primary,secs}=motifsFor(row,r);
 const align=(layout===3||layout===7)?'l':'c';
 const fp=[layout,bg,grad,divIdx,primary,secs.join('+'),align].join('|');
 const g=GRADS[grad];
 const mid=mix(A,B,0.42+r()*0.2);
 const boost=(layout===9)?1.16:1;
 const maxW=(align==='l')?W*0.78:W*0.8;
 const tb=titleBlock(title,sub,maxW,boost);
 const catLabel=esc((CATS[cat]||'').split('&')[0].trim().toUpperCase());
 const ctx={r,primary,secs,tb,catLabel,divIdx};
 const L=LAYOUTS[layout](ctx);
 const num=parseInt(row[3])||40;
 const turbSeed=Math.floor(r()*1000), bf=(0.5+r()*0.5).toFixed(2);
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" font-family="Georgia, 'Times New Roman', serif">
<defs>
<linearGradient id="bg" x1="${g[0]}" y1="${g[1]}" x2="${g[2]}" y2="${g[3]}"><stop offset="0" stop-color="${A}"/><stop offset="0.5" stop-color="${mid}"/><stop offset="1" stop-color="${B}"/></linearGradient>
<radialGradient id="vin" cx="0.5" cy="0.46" r="0.85"><stop offset="0.55" stop-color="rgba(0,0,0,0)"/><stop offset="1" stop-color="rgba(0,0,0,.30)"/></radialGradient>
<radialGradient id="tglow" cx="0.5" cy="0.56" r="0.5"><stop offset="0" stop-color="rgba(0,0,0,.30)"/><stop offset="1" stop-color="rgba(0,0,0,0)"/></radialGradient>
<filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="${bf}" numOctaves="2" seed="${turbSeed}" stitchTiles="stitch"/><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .045 0"/></filter>
</defs>
<rect width="${W}" height="${H}" fill="url(#bg)"/>
${FIELDS[bg](r)}
${L.art}
<rect width="${W}" height="${H}" fill="url(#vin)"/>
<ellipse cx="${align==='l'?248:CX}" cy="452" rx="286" ry="150" fill="url(#tglow)"/>
<rect width="${W}" height="${H}" filter="url(#gr)"/>
${L.frame}
${ring(L.ringPos[0],L.ringPos[1]).replace('NUM',String(num))}
${L.text}
</svg>`;
 return {svg, fp};
}

/* ---------------- run with fingerprint uniqueness ---------------- */
const outDir='/home/claude/site/covers';
fs.rmSync(outDir,{recursive:true,force:true}); fs.mkdirSync(outDir,{recursive:true});
const crypto=require('crypto');
const fps=new Set(), hashes=new Set();
let bytes=0, rerolls=0; const layCount={}, motCount={};
for(const row of ROWS){
 let salt=0, out=build(row,salt);
 while(fps.has(out.fp) && salt<40){ salt++; rerolls++; out=build(row,salt); }
 fps.add(out.fp);
 fs.writeFileSync(outDir+'/'+row[9]+'.svg', out.svg);
 hashes.add(crypto.createHash('sha1').update(out.svg).digest('hex'));
 bytes+=Buffer.byteLength(out.svg);
 const lay=out.fp.split('|')[0]; layCount[lay]=(layCount[lay]||0)+1;
 const pm=out.fp.split('|')[4]; motCount[pm]=(motCount[pm]||0)+1;
}
console.log('covers:',ROWS.length,'| unique svg:',hashes.size,'| unique design fingerprints:',fps.size,'| rerolls:',rerolls);
console.log('avg KB:',(bytes/ROWS.length/1024).toFixed(1),'| total MB:',(bytes/1048576).toFixed(1));
console.log('layout spread:',Object.entries(layCount).sort((a,b)=>a[0]-b[0]).map(([k,v])=>k+':'+v).join(' '));
console.log('primary motifs in use:',Object.keys(motCount).length);
