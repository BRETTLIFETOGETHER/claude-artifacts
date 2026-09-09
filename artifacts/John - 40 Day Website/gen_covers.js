/* gen_covers.js — 1,252 unique campaign thumbnails
   Deterministic generative covers: category hue pair + per-campaign seeded
   composition (gradient angle, glow, motif variation, grain) + adaptive title. */
const fs = require('fs');
global.window = {};
eval(fs.readFileSync('/home/claude/site/data.js', 'utf8'));
const ROWS = window.CAMPAIGNS, CATS = window.CATS;

const HUE = {
  1:['#16A88F','#0C5A4E'], 2:['#C8484C','#7E2326'], 3:['#4F86E0','#26417F'],
  4:['#E0703F','#8A3A1E'], 5:['#E8A52E','#9A6810'], 6:['#36A85E','#176233'],
  7:['#7B5FE0','#3F2E86'], 8:['#E2542F','#8A2A14'], 9:['#5A6B8C','#2E3A52'],
  10:['#C99A3C','#7E601C'], 11:['#3E8FB0','#1D4B60'], 12:['#B0578D','#5F2A4C'],
  13:['#C86B8F','#7A2F4E'], 14:['#8C6BD0','#4A2F86'], 15:['#3FA796','#1E5C52']
};
const GOLD = '#E4AC43';

function seedOf(str){ let h=5381; for(let i=0;i<str.length;i++){ h=((h<<5)+h+str.charCodeAt(i))>>>0; } return h; }
function rng(seed){ let a=seed>>>0; return function(){ a|=0; a=(a+0x6D2B79F5)|0; let t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&apos;');

const W=800, H=525;

/* ---------- motif families (abstract, stroke-based, seeded) ---------- */
function stroke(o){ return `stroke="rgba(255,255,255,${o})" fill="none"`; }
const MOTIFS = {
  1(r){ // Stewardship — coin stack + orbit
    const x=560+r()*140, base=300+r()*60, n=4+Math.floor(r()*3); let s='';
    for(let i=0;i<n;i++) s+=`<ellipse cx="${x}" cy="${base-i*26}" rx="${58-i*3}" ry="16" ${stroke(.5)} stroke-width="2.5"/>`;
    s+=`<circle cx="${x-160-r()*60}" cy="${120+r()*80}" r="${70+r()*40}" ${stroke(.22)} stroke-width="2" stroke-dasharray="1 9"/>`;
    s+=`<circle cx="${x}" cy="${base-n*26-14}" r="7" fill="${GOLD}"/>`;
    return s; },
  2(r){ // Contentment — horizon + low sun + star
    const hy=330+r()*70, sx=170+r()*180;
    return `<line x1="0" y1="${hy}" x2="${W}" y2="${hy}" ${stroke(.4)} stroke-width="2"/>
      <circle cx="${sx}" cy="${hy}" r="${64+r()*30}" ${stroke(.55)} stroke-width="3"/>
      <circle cx="${sx}" cy="${hy}" r="4.5" fill="${GOLD}"/>
      <path d="M ${600+r()*140} ${96+r()*60} l 7 14 15 2 -11 11 3 15 -14 -7 -14 7 3 -15 -11 -11 15 -2 z" fill="rgba(255,255,255,.5)"/>`; },
  3(r){ // Generosity — radiating arcs from corner
    const n=5+Math.floor(r()*3); let s=''; const cx=-40+r()*60, cy=H+40-r()*60;
    for(let i=1;i<=n;i++) s+=`<circle cx="${cx}" cy="${cy}" r="${i*(85+r()*14)}" ${stroke(.14+.32/i)} stroke-width="${3.4-i*0.32}"/>`;
    s+=`<circle cx="${cx+n*62}" cy="${cy-n*54}" r="6" fill="${GOLD}"/>`; return s; },
  4(r){ // Kingdom — meridians + scattered points
    const cx=590+r()*110, cy=190+r()*90, R=110+r()*40; let s=`<circle cx="${cx}" cy="${cy}" r="${R}" ${stroke(.5)} stroke-width="2.5"/>`;
    for(let i=1;i<=2;i++){ s+=`<ellipse cx="${cx}" cy="${cy}" rx="${R*i/3}" ry="${R}" ${stroke(.34)} stroke-width="1.8"/>`; }
    s+=`<ellipse cx="${cx}" cy="${cy}" rx="${R}" ry="${R/3}" ${stroke(.34)} stroke-width="1.8"/>`;
    for(let i=0;i<4;i++) s+=`<circle cx="${120+r()*300}" cy="${120+r()*240}" r="3.2" fill="rgba(255,255,255,.6)"/>`;
    s+=`<circle cx="${cx+R*Math.cos(r()*6.28)*0.7}" cy="${cy+R*Math.sin(r()*6.28)*0.7}" r="6" fill="${GOLD}"/>`; return s; },
  5(r){ // Legacy — branching tree
    let s=''; const bx=600+r()*110;
    function branch(x,y,a,len,d){ if(d>3||len<24) return;
      const x2=x+Math.cos(a)*len, y2=y-Math.sin(a)*len;
      s+=`<line x1="${x.toFixed(1)}" y1="${y.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" ${stroke(.55-d*0.11)} stroke-width="${4.5-d}" stroke-linecap="round"/>`;
      branch(x2,y2,a+0.42+r()*0.3,len*(0.62+r()*0.14),d+1);
      branch(x2,y2,a-0.42-r()*0.3,len*(0.62+r()*0.14),d+1); }
    branch(bx,430,Math.PI/2,110+r()*30,0);
    s+=`<circle cx="${bx}" cy="430" r="5.5" fill="${GOLD}"/>`; return s; },
  6(r){ // Heirs — ascending steps + arrow
    let s=''; let x=470+r()*60, y=380; const st=58+r()*14;
    for(let i=0;i<4;i++){ s+=`<path d="M ${x} ${y} h ${st} v ${-st*0.62}" ${stroke(.5)} stroke-width="3" stroke-linecap="round"/>`; x+=st; y-=st*0.62; }
    s+=`<path d="M ${x} ${y} l 26 -18 M ${x} ${y} l 4 -30 M ${x} ${y} l 30 -4" ${stroke(.7)} stroke-width="3" stroke-linecap="round"/>
        <circle cx="${x+28}" cy="${y-20}" r="5.5" fill="${GOLD}"/>`; return s; },
  7(r){ // Family — clustered circles under one arc (roof)
    const cx=600+r()*90, cy=300+r()*40; let s='';
    const kids=[[ -52,10,30],[0,-6,40],[54,12,28],[8+r()*30,52,20]];
    kids.forEach(k=>{ s+=`<circle cx="${cx+k[0]}" cy="${cy+k[1]}" r="${k[2]}" ${stroke(.5)} stroke-width="2.6"/>`; });
    s+=`<path d="M ${cx-120} ${cy+8} A 120 120 0 0 1 ${cx+120} ${cy+8}" ${stroke(.35)} stroke-width="2.4"/>
        <circle cx="${cx}" cy="${cy-46}" r="5.5" fill="${GOLD}"/>`; return s; },
  8(r){ // Business & work — ledger grid + rising line
    let s='<g '+stroke(.16)+' stroke-width="1.4">';
    for(let i=1;i<6;i++) s+=`<line x1="${430+i*58}" y1="120" x2="${430+i*58}" y2="420"/>`;
    for(let j=1;j<6;j++) s+=`<line x1="460" y1="${90+j*58}" x2="770" y2="${90+j*58}"/>`;
    s+='</g>';
    const pts=[]; let px=470, py=390;
    for(let i=0;i<5;i++){ pts.push(px+','+py); px+=62; py-=34+r()*44; }
    s+=`<polyline points="${pts.join(' ')}" ${stroke(.62)} stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="${px-62}" cy="${py+34+ (0)}" r="0" fill="none"/>
        <circle cx="${pts[pts.length-1].split(',')[0]}" cy="${pts[pts.length-1].split(',')[1]}" r="6" fill="${GOLD}"/>`; return s; },
  9(r){ // Leadership — mountain path + summit mark
    const base=400+r()*30; let s='';
    s+=`<path d="M 430 ${base} L ${520+r()*30} ${base-110-r()*40} L ${600+r()*20} ${base-40} L ${680+r()*30} ${base-170-r()*40} L 790 ${base-60}" ${stroke(.55)} stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>`;
    s+=`<circle cx="${684+r()*20}" cy="${base-176-r()*30}" r="6" fill="${GOLD}"/>`;
    s+=`<path d="M 430 ${base+26} H 790" ${stroke(.2)} stroke-width="2" stroke-dasharray="2 10"/>`; return s; },
  10(r){ // Faith & Word — open book arcs + ribbon
    const cx=610+r()*80, cy=280+r()*50, w=130+r()*30;
    return `<path d="M ${cx-w} ${cy} Q ${cx-w*0.5} ${cy-46} ${cx} ${cy} Q ${cx+w*0.5} ${cy-46} ${cx+w} ${cy}" ${stroke(.6)} stroke-width="3"/>
      <path d="M ${cx-w} ${cy+16} Q ${cx-w*0.5} ${cy-30} ${cx} ${cy+16} Q ${cx+w*0.5} ${cy-30} ${cx+w} ${cy+16}" ${stroke(.35)} stroke-width="2.4"/>
      <line x1="${cx}" y1="${cy}" x2="${cx}" y2="${cy+70+r()*30}" ${stroke(.5)} stroke-width="2.6"/>
      <circle cx="${cx}" cy="${cy-8}" r="5.5" fill="${GOLD}"/>`; },
  11(r){ // Seasons — orbit with sun and moon positions
    const cx=600+r()*90, cy=250+r()*60, R=120+r()*40, a=r()*6.28;
    return `<circle cx="${cx}" cy="${cy}" r="${R}" ${stroke(.4)} stroke-width="2" stroke-dasharray="1 8"/>
      <circle cx="${cx+R*Math.cos(a)}" cy="${cy+R*Math.sin(a)}" r="16" ${stroke(.7)} stroke-width="3"/>
      <circle cx="${cx-R*Math.cos(a)}" cy="${cy-R*Math.sin(a)}" r="8" fill="rgba(255,255,255,.55)"/>
      <circle cx="${cx}" cy="${cy}" r="5" fill="${GOLD}"/>`; },
  12(r){ // Hope — sunrise + rays
    const cx=600+r()*90, hy=360+r()*40, R=90+r()*30; let s='';
    s+=`<path d="M ${cx-R} ${hy} A ${R} ${R} 0 0 1 ${cx+R} ${hy}" ${stroke(.65)} stroke-width="3.4"/>
        <line x1="${cx-R-60}" y1="${hy}" x2="${cx+R+60}" y2="${hy}" ${stroke(.35)} stroke-width="2"/>`;
    for(let i=0;i<5;i++){ const a=Math.PI*(0.16+i*0.17); s+=`<line x1="${cx+Math.cos(a)*(R+16)}" y1="${hy-Math.sin(a)*(R+16)}" x2="${cx+Math.cos(a)*(R+42+r()*14)}" y2="${hy-Math.sin(a)*(R+42+r()*14)}" ${stroke(.5)} stroke-width="2.6" stroke-linecap="round"/>`; }
    s+=`<circle cx="${cx}" cy="${hy-R*0.45}" r="5.5" fill="${GOLD}"/>`; return s; },
  13(r){ // Waves
    let s=''; for(let j=0;j<3;j++){ const y=250+j*54+r()*20; let d=`M -20 ${y}`; for(let x=0;x<=W+40;x+=80){ d+=` q 40 ${j%2?-34:-28-r()*14} 80 0`; } s+=`<path d="${d}" ${stroke(.42-j*0.1)} stroke-width="${3-j*0.5}"/>`; }
    s+=`<circle cx="${620+r()*120}" cy="${210+r()*40}" r="6" fill="${GOLD}"/>`; return s; },
  14(r){ // Path
    const d=`M ${80+r()*60} 470 C ${240+r()*80} ${380-r()*60}, ${420+r()*60} ${430-r()*40}, ${560+r()*40} ${300-r()*40} S ${740} ${170-r()*50}, ${760} ${120-r()*40}`;
    return `<path d="${d}" ${stroke(.55)} stroke-width="3.4" stroke-dasharray="14 12" stroke-linecap="round"/>
      <circle cx="758" cy="${118-r()*36}" r="6" fill="${GOLD}"/>`; },
  15(r){ // Petals
    let s=''; for(let i=0;i<7;i++){ const x=460+r()*300, y=110+r()*280, rot=r()*180; s+=`<ellipse cx="${x}" cy="${y}" rx="26" ry="11" transform="rotate(${rot.toFixed(0)} ${x} ${y})" ${stroke(.4)} stroke-width="2.2"/>`; }
    s+=`<circle cx="${560+r()*140}" cy="${180+r()*120}" r="5.5" fill="${GOLD}"/>`; return s; }
};

/* ---------- title layout ---------- */
function wrapTitle(t){
  const len=t.length;
  const fs = len<=15?62 : len<=24?52 : len<=34?45 : len<=46?39 : 34;
  const per = Math.floor((W-96)/(fs*0.5));
  const words=t.split(' '); const lines=[]; let cur='';
  for(const w of words){ if((cur+' '+w).trim().length<=per) cur=(cur+' '+w).trim(); else { lines.push(cur); cur=w; } }
  if(cur) lines.push(cur);
  if(lines.length>3){ lines.length=3; lines[2]=lines[2].replace(/\s?\S*$/,'')+'…'; }
  return {fs, lines};
}

function cover(r0){
  const id=r0[9], title=r0[0], cat=r0[2], lenTxt=r0[3];
  const [A,B]=HUE[cat]||HUE[5];
  const r=rng(seedOf(id));
  const angles=[[0,0,1,1],[1,0,0,1],[0,1,1,0],[1,1,0,0],[0,0.2,1,0.8],[0.15,1,0.85,0]];
  const g=angles[Math.floor(r()*angles.length)];
  const glowX=(0.15+r()*0.5)*W, glowY=(0.1+r()*0.4)*H;
  const motif=(MOTIFS[cat]||MOTIFS[5])(r);
  const {fs,lines}=wrapTitle(title);
  const baseY=H-46-(lines.length-1)*(fs*1.04);
  const tspans=lines.map((L,i)=>`<tspan x="48" y="${(baseY+i*fs*1.04).toFixed(0)}">${esc(L)}</tspan>`).join('');
  const catLabel=esc((CATS[cat]||'').split('&')[0].trim().toUpperCase());
  const num=parseInt(lenTxt)||40;
  const turbSeed=Math.floor(r()*1000);
  const bf=(0.55+r()*0.5).toFixed(2);
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" font-family="Georgia, 'Times New Roman', serif">
<defs>
  <linearGradient id="bg" x1="${g[0]}" y1="${g[1]}" x2="${g[2]}" y2="${g[3]}">
    <stop offset="0" stop-color="${A}"/><stop offset="1" stop-color="${B}"/>
  </linearGradient>
  <radialGradient id="gl" cx="${(glowX/W).toFixed(2)}" cy="${(glowY/H).toFixed(2)}" r="0.9">
    <stop offset="0" stop-color="rgba(255,255,255,.20)"/><stop offset="0.55" stop-color="rgba(255,255,255,0)"/>
  </radialGradient>
  <linearGradient id="scrim" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0.45" stop-color="rgba(0,0,0,0)"/><stop offset="1" stop-color="rgba(0,0,0,.38)"/>
  </linearGradient>
  <filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="${bf}" numOctaves="2" seed="${turbSeed}" stitchTiles="stitch"/>
    <feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0"/></filter>
</defs>
<rect width="${W}" height="${H}" fill="url(#bg)"/>
<rect width="${W}" height="${H}" fill="url(#gl)"/>
${motif}
<rect width="${W}" height="${H}" filter="url(#gr)"/>
<rect width="${W}" height="${H}" fill="url(#scrim)"/>
<circle cx="${W-64}" cy="64" r="34" fill="none" stroke="rgba(255,255,255,.8)" stroke-width="2.5"/>
<text x="${W-64}" y="${64+9}" text-anchor="middle" font-size="26" fill="#FFFFFF">${num}</text>
<text x="48" y="${baseY-fs-16}" font-family="Verdana, Arial, sans-serif" font-size="14.5" letter-spacing="4" fill="rgba(255,255,255,.85)" font-weight="bold">${catLabel}</text>
<text font-size="${fs}" fill="#FFFFFF" font-weight="600">${tspans}</text>
</svg>`;
}

/* ---------- run ---------- */
const outDir='/home/claude/site/covers';
fs.mkdirSync(outDir,{recursive:true});
const crypto=require('crypto');
const hashes=new Set(); let n=0, bytes=0;
for(const row of ROWS){
  const svg=cover(row);
  fs.writeFileSync(outDir+'/'+row[9]+'.svg', svg);
  hashes.add(crypto.createHash('sha1').update(svg).digest('hex'));
  bytes+=Buffer.byteLength(svg); n++;
}
console.log('covers written:', n, '| unique:', hashes.size, '| avg bytes:', Math.round(bytes/n), '| total MB:', (bytes/1048576).toFixed(1));
