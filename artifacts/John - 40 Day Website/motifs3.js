/* motifs3.js — 58 placeable illustrated primitives.
   Each draws in a 600-wide reference space centered near (300,195);
   place(name, x, y, s) transplants it anywhere. Ground strips removed —
   layouts supply their own base ornaments. */
const GOLD='#E4AC43';
const st=(o,w)=>`stroke="rgba(255,255,255,${o})" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round"`;
const fillW=o=>`fill="rgba(255,255,255,${o})"`;
const gp=(x,y,r=6)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${GOLD}"/>`;
const CX=300;

const PRIM = {};
const KIND = {}; // 'L' large scene, 's' small accent

function def(name, kind, fn){ PRIM[name]=fn; KIND[name]=kind; }

/* ============ ported large scenes (v2, ground strips removed) ============ */
def('keys','L', r=>{ const y=185; return `<g ${st(.6,3)}>
 <circle cx="${CX-52}" cy="${y-28}" r="34"/><circle cx="${CX-52}" cy="${y-28}" r="15"/>
 <path d="M ${CX-22} ${y-8} L ${CX+66} ${y+56} M ${CX+34} ${y+32} l 16 -20 M ${CX+52} ${y+46} l 16 -20"/>
 <rect x="${CX-118}" y="${y+52}" width="150" height="96" rx="8"/>
 <path d="M ${CX-98} ${y+78} h 96 M ${CX-98} ${y+98} h 110 M ${CX-98} ${y+118} h 76"/></g>
 <circle cx="${CX+8}" cy="${y+128}" r="17" ${st(.55,2.6)}/><path d="M ${CX+2} ${y+128} l 5 5 9 -11" ${st(.7,2.6)}/>${gp(CX+66,y+56)}`; });
def('torch','L', r=>{ const y=200; return `<g ${st(.62,3.2)}>
 <path d="M ${CX-14} ${y+40} L ${CX-30} ${y+150} h 60 L ${CX+14} ${y+40} z"/><path d="M ${CX-34} ${y+34} h 68"/>
 <path d="M ${CX} ${y+22} C ${CX-40} ${y-8} ${CX-26} ${y-62} ${CX} ${y-84} C ${CX+26} ${y-62} ${CX+40} ${y-8} ${CX} ${y+22}"/>
 <path d="M ${CX} ${y+8} C ${CX-16} ${y-12} ${CX-8} ${y-38} ${CX} ${y-50} C ${CX+8} ${y-38} ${CX+16} ${y-12} ${CX} ${y+8}"/></g>
 <g ${st(.4,2.4)}><path d="M ${CX-84} ${y-40} q -26 -26 -30 -60"/><path d="M ${CX+84} ${y-40} q 26 -26 30 -60"/></g>
 <circle cx="${CX-58}" cy="${y-96}" r="4" ${fillW(.7)}/><circle cx="${CX+64}" cy="${y-108}" r="3.4" ${fillW(.6)}/>${gp(CX,y-50,7)}`; });
def('heart','L', r=>{ const y=190; return `<g ${st(.62,3.2)}>
 <path d="M ${CX} ${y+96} C ${CX-120} ${y+10} ${CX-84} ${y-88} ${CX-6} ${y-30} C ${CX+78} ${y-92} ${CX+122} ${y+8} ${CX} ${y+96} z"/>
 <path d="M ${CX-64} ${y-18} q 20 -30 52 -26"/></g>
 <path d="M ${CX-170} ${y+130} h 70 l 16 -30 20 56 16 -26 h 218" ${st(.45,2.6)}/>${gp(CX,y-34)}`; });
def('scales','L', r=>{ const y=150; return `<g ${st(.6,3)}>
 <path d="M ${CX} ${y} v 178 M ${CX-120} ${y+34} h 240 M ${CX} ${y} l -120 34 M ${CX} ${y} l 120 34"/>
 <path d="M ${CX-120} ${y+34} l -34 62 h 68 z M ${CX+120} ${y+34} l -34 62 h 68 z"/>
 <path d="M ${CX-154} ${y+96} a 34 20 0 0 0 68 0 M ${CX+86} ${y+96} a 34 20 0 0 0 68 0"/>
 <path d="M ${CX-56} ${y+178} h 112 M ${CX-40} ${y+196} h 80"/></g>
 <circle cx="${CX}" cy="${y-16}" r="12" ${st(.6,3)}/>${gp(CX,y-16,5)}`; });
def('anchor','L', r=>{ const y=170; return `<g ${st(.62,3.2)}>
 <circle cx="${CX}" cy="${y-38}" r="20"/><path d="M ${CX} ${y-18} V ${y+140} M ${CX-58} ${y+18} h 116"/>
 <path d="M ${CX-88} ${y+96} a 88 88 0 0 0 176 0 M ${CX-88} ${y+96} l -18 -24 M ${CX-88} ${y+96} l 26 -14 M ${CX+88} ${y+96} l 18 -24 M ${CX+88} ${y+96} l -26 -14"/></g>
 <path d="M ${CX+26} ${y-52} q 60 -30 92 6 q 22 26 -6 44" ${st(.35,2.4)}/>${gp(CX,y-38,5)}`; });
def('lighthouse','L', r=>{ const y=250; const bx=CX; return `<g ${st(.6,3)}>
 <path d="M ${bx-30} ${y+60} L ${bx-20} ${y-92} h 40 L ${bx+30} ${y+60}"/>
 <path d="M ${bx-26} ${y-92} h 52 M ${bx-16} ${y-112} h 32 M ${bx-16} ${y-112} v -22 h 32 v 22 M ${bx-22} ${y-134} h 44 l -22 -22 z"/>
 <path d="M ${bx-27} ${y-40} h 54 M ${bx-24} ${y+6} h 48"/></g>
 <g ${st(.4,2.4)}><path d="M ${bx-34} ${y-122} l -78 -26 M ${bx-34} ${y-114} l -80 6"/><path d="M ${bx+34} ${y-122} l 78 -26 M ${bx+34} ${y-114} l 80 6"/></g>
 <g ${st(.42,2.6)}><path d="M ${bx-190} ${y+66} q 46 -22 92 0 q 46 22 92 0 q 46 -22 92 0 q 46 22 92 0"/><path d="M ${bx-150} ${y+94} q 50 -22 100 0 q 50 22 100 0"/></g>
 <path d="M ${bx-120} ${y-160} q 10 -12 22 0 q 10 -12 22 0 M ${bx+80} ${y-186} q 9 -11 20 0 q 9 -11 20 0" ${st(.45,2.4)}/>${gp(bx,y-123,6)}`; });
def('sunrise','L', r=>{ const hy=240; return `<g ${st(.55,2.8)}>
 <path d="M ${CX-96} ${hy} A 96 96 0 0 1 ${CX+96} ${hy}"/><path d="M ${CX-250} ${hy} H ${CX+250}"/>
 <path d="M ${CX-236} ${hy+44} q 96 -50 192 0 q -96 26 -192 0 z M ${CX+44} ${hy+44} q 96 -50 192 0 q -96 26 -192 0 z" stroke-width="2.4"/></g>
 <g ${st(.5,2.6)}>${[0.14,0.32,0.5,0.68,0.86].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+Math.cos(a)*118).toFixed(0)}" y1="${(hy-Math.sin(a)*118).toFixed(0)}" x2="${(CX+Math.cos(a)*152).toFixed(0)}" y2="${(hy-Math.sin(a)*152).toFixed(0)}"/>`;}).join('')}</g>
 <path d="M ${CX-150} ${hy-140} q 11 -13 24 0 q 11 -13 24 0 M ${CX+96} ${hy-170} q 10 -12 22 0 q 10 -12 22 0" ${st(.5,2.4)}/>${gp(CX,hy-64,7)}`; });
def('sprout','L', r=>{ const y=250; return `<g ${st(.6,3)}>
 <path d="M ${CX} ${y+40} V ${y-70}"/>
 <path d="M ${CX} ${y-40} C ${CX-64} ${y-52} ${CX-84} ${y-108} ${CX-70} ${y-140} C ${CX-24} ${y-128} ${CX-4} ${y-84} ${CX} ${y-40} z"/>
 <path d="M ${CX} ${y-56} C ${CX+58} ${y-70} ${CX+76} ${y-118} ${CX+64} ${y-148} C ${CX+20} ${y-136} ${CX+2} ${y-96} ${CX} ${y-56} z"/>
 <path d="M ${CX-160} ${y+40} H ${CX+160}"/>
 <path d="M ${CX} ${y+40} q -10 34 -44 44 M ${CX} ${y+40} q 12 40 50 48 M ${CX} ${y+40} q -2 52 -14 62"/></g>
 <g ${st(.45,2.4)}><path d="M ${CX-110} ${y-150} q 6 12 0 24 M ${CX-88} ${y-176} q 6 12 0 24 M ${CX+112} ${y-166} q 6 12 0 24"/></g>${gp(CX,y-74,5)}`; });
def('mountains','L', r=>{ const y=290; return `<g ${st(.58,2.8)}>
 <path d="M ${CX-250} ${y} L ${CX-150} ${y-120} L ${CX-70} ${y-30} L ${CX+10} ${y-160} L ${CX+110} ${y-40} L ${CX+180} ${y-100} L ${CX+250} ${y}"/>
 <path d="M ${CX-250} ${y+34} L ${CX-120} ${y-30} L ${CX-10} ${y+20} L ${CX+120} ${y-40} L ${CX+250} ${y+34}" stroke-width="2.2" stroke="rgba(255,255,255,.36)"/>
 <path d="M ${CX+10} ${y-160} l -16 24 h 32 z" ${fillW(.5)}/><path d="M ${CX+10} ${y-160} v -30 l 26 8 -26 8"/></g>
 <circle cx="${CX-160}" cy="${y-200}" r="26" ${st(.5,2.6)}/>${gp(CX+10,y-190,6)}`; });
def('path','L', r=>{ const y=300; return `<g ${st(.6,3)}>
 <path d="M ${CX-40} ${y+60} C ${CX-140} ${y+10} ${CX+90} ${y-30} ${CX-20} ${y-80} C ${CX-100} ${y-120} ${CX+40} ${y-150} ${CX+10} ${y-186}" stroke-dasharray="16 13"/>
 <path d="M ${CX-250} ${y-40} q 80 -20 150 -8 M ${CX+120} ${y-90} q 70 -14 130 -2" stroke-width="2" stroke="rgba(255,255,255,.3)"/></g>
 <g ${st(.55,2.8)}><path d="M ${CX-120} ${y+18} v -44 M ${CX-120} ${y-26} h 30 v 16 h -30"/><path d="M ${CX+96} ${y-36} v -40"/><circle cx="${CX+96}" cy="${y-88}" r="12"/></g>
 <g ${st(.5,2.6)}><path d="M ${CX+176} ${y-160} v 26 M ${CX+164} ${y-150} h 24"/><circle cx="${CX-190}" cy="${y-120}" r="10"/></g>${gp(CX+10,y-186,6)}`; });
def('book','L', r=>{ const y=210; return `<g ${st(.62,3)}>
 <path d="M ${CX-140} ${y} C ${CX-90} ${y-46} ${CX-30} ${y-40} ${CX} ${y-16} C ${CX+30} ${y-40} ${CX+90} ${y-46} ${CX+140} ${y} V ${y+96} C ${CX+90} ${y+54} ${CX+30} ${y+58} ${CX} ${y+82} C ${CX-30} ${y+58} ${CX-90} ${y+54} ${CX-140} ${y+96} z"/>
 <path d="M ${CX} ${y-16} V ${y+82}"/>
 <path d="M ${CX-112} ${y+8} c 40 -26 76 -24 96 -8 M ${CX-112} ${y+34} c 40 -26 76 -24 96 -8 M ${CX+16} ${y} c 40 -26 76 -24 96 8 M ${CX+16} ${y+26} c 40 -26 76 -24 96 8" stroke-width="2.2" stroke="rgba(255,255,255,.42)"/>
 <path d="M ${CX+52} ${y+70} l 10 34 10 -14 16 6 -12 -34"/></g>${gp(CX,y-46,5)}`; });
def('prayer','L', r=>{ const y=200; return `<g ${st(.62,3)}>
 <path d="M ${CX} ${y-70} C ${CX-26} ${y-30} ${CX-34} ${y+30} ${CX-30} ${y+96} L ${CX-6} ${y+120} L ${CX} ${y+96} L ${CX+6} ${y+120} L ${CX+30} ${y+96} C ${CX+34} ${y+30} ${CX+26} ${y-30} ${CX} ${y-70} z"/>
 <path d="M ${CX-30} ${y+30} q 30 16 60 0"/></g>
 <g ${st(.42,2.4)}><path d="M ${CX-70} ${y-40} q -16 -34 -6 -70"/><path d="M ${CX+70} ${y-40} q 16 -34 6 -70"/><path d="M ${CX} ${y-96} q -6 -28 4 -48"/></g>
 <g ${st(.5,2.6)}><path d="M ${CX-140} ${y+80} v 44 M ${CX-152} ${y+82} h 24"/><path d="M ${CX-140} ${y+66} C ${CX-146} ${y+56} ${CX-134} ${y+52} ${CX-140} ${y+44}"/></g>${gp(CX,y-84,5)}`; });
def('gift','L', r=>{ const y=200; return `<g ${st(.6,3)}>
 <path d="M ${CX-160} ${y+96} q 60 -34 130 -8 q 80 30 190 -6"/><path d="M ${CX-160} ${y+96} q -20 8 -26 26"/>
 <rect x="${CX-56}" y="${y-30}" width="112" height="86" rx="8"/><path d="M ${CX-56} ${y+2} h 112 M ${CX} ${y-30} v 86"/>
 <path d="M ${CX} ${y-30} c -14 -30 -52 -34 -56 -10 c -2 16 30 16 56 10 z M ${CX} ${y-30} c 14 -30 52 -34 56 -10 c 2 16 -30 16 -56 10 z"/></g>
 <g ${st(.5,2.6)}><circle cx="${CX-116}" cy="${y-56}" r="12"/><circle cx="${CX+116}" cy="${y-70}" r="9"/><circle cx="${CX+70}" cy="${y-110}" r="6"/></g>${gp(CX,y-40,5)}`; });
def('coins','L', r=>{ const y=210; const x=CX; return `<g ${st(.58,2.8)}>
 ${[0,1,2,3,4].map(i=>`<ellipse cx="${x-70}" cy="${y+70-i*24}" rx="56" ry="15"/>`).join('')}
 ${[0,1,2].map(i=>`<ellipse cx="${x+78}" cy="${y+76-i*24}" rx="48" ry="13"/>`).join('')}
 <circle cx="${x+70}" cy="${y-72}" r="30"/><path d="M ${x+70} ${y-88} v 32 M ${x+62} ${y-80} c 0 -8 16 -8 16 0 c 0 8 -16 8 -16 0 c 0 8 16 8 16 0"/>
 <path d="M ${x-150} ${y+96} q 150 44 300 0"/></g>${gp(x+70,y-72,5)}`; });
def('tree','L', r=>{ const y=280; return `<g ${st(.6,2.8)}>
 <path d="M ${CX} ${y+60} V ${y-30} M ${CX} ${y-4} q -40 -12 -58 -44 M ${CX} ${y-14} q 42 -10 60 -48"/>
 <path d="M ${CX-104} ${y-58} C ${CX-140} ${y-120} ${CX-70} ${y-186} ${CX} ${y-160} C ${CX+70} ${y-186} ${CX+140} ${y-120} ${CX+104} ${y-58} C ${CX+70} ${y-30} ${CX-70} ${y-30} ${CX-104} ${y-58} z"/>
 <path d="M ${CX} ${y+60} q -26 22 -60 24 M ${CX} ${y+60} q 26 22 60 24 M ${CX-160} ${y+60} H ${CX+160}"/></g>
 <g ${st(.5,2.4)}><path d="M ${CX-190} ${y+30} v 30 M ${CX-190} ${y+30} q -20 -26 0 -40 q 20 14 0 40"/><path d="M ${CX+190} ${y+30} v 30 M ${CX+190} ${y+30} q -20 -26 0 -40 q 20 14 0 40"/></g>
 ${[[-60,-120],[0,-150],[58,-118],[-24,-92],[34,-88]].map(p=>`<circle cx="${CX+p[0]}" cy="${y+p[1]}" r="3.2" ${fillW(.55)}/>`).join('')}${gp(CX,y-160,5)}`; });
def('arrowlaunch','L', r=>{ const y=230; return `<g ${st(.6,3)}>
 <path d="M ${CX-120} ${y+90} C ${CX-40} ${y+60} ${CX+10} ${y-10} ${CX+60} ${y-90}" stroke-dasharray="3 12"/>
 <path d="M ${CX+60} ${y-90} l 34 -56 M ${CX+94} ${y-146} l -30 6 M ${CX+94} ${y-146} l -4 30"/>
 <path d="M ${CX-160} ${y+40} A 130 130 0 0 1 ${CX-30} ${y-90}"/>
 <path d="M ${CX-160} ${y+40} l -22 -18 M ${CX-160} ${y+40} l 26 12 M ${CX-30} ${y-90} l -18 -22 M ${CX-30} ${y-90} l 12 26"/></g>
 <g ${st(.45,2.4)}><circle cx="${CX+130}" cy="${y-40}" r="26"/><circle cx="${CX+130}" cy="${y-40}" r="12"/></g>${gp(CX+94,y-146,6)}`; });
def('home','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX-110} ${y+30} L ${CX} ${y-70} L ${CX+110} ${y+30}"/>
 <path d="M ${CX-88} ${y+22} V ${y+130} H ${CX+88} V ${y+22}"/>
 <rect x="${CX-20}" y="${y+66}" width="40" height="64" rx="3"/>
 <rect x="${CX-66}" y="${y+52}" width="30" height="30" rx="3"/><path d="M ${CX-51} ${y+52} v 30 M ${CX-66} ${y+67} h 30"/>
 <path d="M ${CX+40} ${y-38} v -34 h 22 v 14"/><path d="M ${CX+62} ${y-92} q 12 -12 4 -26 M ${CX+74} ${y-84} q 12 -12 4 -26"/></g>
 <path d="M ${CX+48} ${y+70} c -8 -12 -26 -6 -22 8 c 3 9 14 12 22 20 c 8 -8 19 -11 22 -20 c 4 -14 -14 -20 -22 -8 z" ${st(.55,2.6)}/>${gp(CX,y-70,5)}`; });
def('rings','L', r=>{ const y=190; return `<g ${st(.62,3.2)}>
 <circle cx="${CX-34}" cy="${y}" r="58"/><circle cx="${CX+34}" cy="${y}" r="58"/>
 <path d="M ${CX-34} ${y-58} l -12 -22 h 24 z M ${CX+34} ${y-58} l -12 -22 h 24 z" stroke-width="2.6"/></g>
 <path d="M ${CX-96} ${y+96} q 96 44 192 0" ${st(.42,2.4)}/>${gp(CX,y,5)}`; });
def('kite','L', r=>{ const y=180; return `<g ${st(.6,3)}>
 <path d="M ${CX} ${y-90} L ${CX+64} ${y} L ${CX} ${y+90} L ${CX-64} ${y} z M ${CX} ${y-90} V ${y+90} M ${CX-64} ${y} H ${CX+64}"/>
 <path d="M ${CX} ${y+90} C ${CX-30} ${y+140} ${CX+30} ${y+170} ${CX-10} ${y+220}"/>
 <path d="M ${CX-16} ${y+130} l 12 -10 12 10 -12 10 z M ${CX+6} ${y+172} l 11 -9 11 9 -11 9 z" stroke-width="2.4"/></g>
 <g ${st(.45,2.4)}><path d="M ${CX-140} ${y-40} q 12 -14 26 0 q 12 -14 26 0"/><path d="M ${CX+90} ${y-90} q 11 -13 24 0 q 11 -13 24 0"/></g>${gp(CX,y-90,5)}`; });
def('crown','L', r=>{ const y=190; return `<g ${st(.62,3)}>
 <path d="M ${CX-110} ${y+40} L ${CX-124} ${y-60} L ${CX-58} ${y-6} L ${CX} ${y-84} L ${CX+58} ${y-6} L ${CX+124} ${y-60} L ${CX+110} ${y+40} z"/>
 <path d="M ${CX-110} ${y+58} h 220 M ${CX-104} ${y+76} h 208"/>
 <circle cx="${CX-124}" cy="${y-70}" r="9"/><circle cx="${CX}" cy="${y-96}" r="10"/><circle cx="${CX+124}" cy="${y-70}" r="9"/></g>
 ${[[-64,26],[0,20],[64,26]].map(p=>`<circle cx="${CX+p[0]}" cy="${y+p[1]}" r="6" ${st(.5,2.4)}/>`).join('')}${gp(CX,y-96,5)}`; });
def('cross','L', r=>{ const y=200; return `<g ${st(.62,3.2)}>
 <path d="M ${CX} ${y-100} V ${y+110} M ${CX-64} ${y-30} H ${CX+64}"/>
 <path d="M ${CX-140} ${y+110} q 140 -50 280 0"/></g>
 <g ${st(.42,2.4)}>${[0.2,0.4,0.6,0.8].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+Math.cos(a)*112).toFixed(0)}" y1="${(y-30-Math.sin(a)*112).toFixed(0)}" x2="${(CX+Math.cos(a)*148).toFixed(0)}" y2="${(y-30-Math.sin(a)*148).toFixed(0)}"/>`;}).join('')}</g>${gp(CX,y-30,6)}`; });
def('compass','L', r=>{ const y=190; return `<g ${st(.6,2.8)}>
 <circle cx="${CX}" cy="${y}" r="92"/><circle cx="${CX}" cy="${y}" r="72"/>
 <path d="M ${CX} ${y-92} v 16 M ${CX} ${y+76} v 16 M ${CX-92} ${y} h 16 M ${CX+76} ${y} h 16"/>
 <path d="M ${CX} ${y} L ${CX+34} ${y-46} L ${CX+8} ${y-6} z" ${fillW(.5)}/><path d="M ${CX} ${y} L ${CX-34} ${y+46} L ${CX-8} ${y+6} z"/>
 ${[45,135,225,315].map(a=>{const rd=a*Math.PI/180;return `<line x1="${(CX+Math.cos(rd)*80).toFixed(0)}" y1="${(y+Math.sin(rd)*80).toFixed(0)}" x2="${(CX+Math.cos(rd)*90).toFixed(0)}" y2="${(y+Math.sin(rd)*90).toFixed(0)}"/>`;}).join('')}</g>${gp(CX,y,5)}`; });
def('lamp','L', r=>{ const y=200; return `<g ${st(.6,3)}>
 <path d="M ${CX-70} ${y+20} q -18 -44 24 -58 q 6 -22 46 -22 q 40 0 46 22 q 42 14 24 58 q -70 24 -140 0 z"/>
 <path d="M ${CX+66} ${y-2} q 40 -6 52 -30 M ${CX+118} ${y-32} l -14 -2 M ${CX+118} ${y-32} l -2 14"/>
 <path d="M ${CX-46} ${y+40} q 46 18 92 0 M ${CX-24} ${y+58} h 48"/>
 <path d="M ${CX+112} ${y-56} C ${CX+96} ${y-76} ${CX+112} ${y-96} ${CX+118} ${y-108} C ${CX+128} ${y-92} ${CX+140} ${y-76} ${CX+124} ${y-58} z"/></g>
 <g ${st(.42,2.4)}>${[0.25,0.5,0.75].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+118+Math.cos(a)*34).toFixed(0)}" y1="${(y-90-Math.sin(a)*34).toFixed(0)}" x2="${(CX+118+Math.cos(a)*52).toFixed(0)}" y2="${(y-90-Math.sin(a)*52).toFixed(0)}"/>`;}).join('')}</g>
 <path d="M ${CX-130} ${y+66} h 260" ${st(.4,2.4)}/>${gp(CX+118,y-84,5)}`; });
def('sundial','L', r=>{ const y=190; return `<g ${st(.6,2.8)}>
 <circle cx="${CX}" cy="${y}" r="96"/>
 ${[...Array(12)].map((_,i)=>{const a=i*Math.PI/6;return `<line x1="${(CX+Math.cos(a)*84).toFixed(0)}" y1="${(y+Math.sin(a)*84).toFixed(0)}" x2="${(CX+Math.cos(a)*96).toFixed(0)}" y2="${(y+Math.sin(a)*96).toFixed(0)}"/>`;}).join('')}
 <path d="M ${CX} ${y} L ${CX+52} ${y-64} M ${CX} ${y} L ${CX-8} ${y-70} L ${CX+52} ${y-64}"/></g>
 <g ${st(.45,2.4)}><circle cx="${CX-150}" cy="${y-110}" r="18"/><path d="M ${CX+150} ${y-116} a 16 16 0 1 0 10 28 a 13 13 0 0 1 -10 -28 z"/></g>${gp(CX,y,5)}`; });
def('well','L', r=>{ const y=210; return `<g ${st(.6,3)}>
 <path d="M ${CX-84} ${y+20} h 168 v 26 q -84 20 -168 0 z"/>
 <path d="M ${CX-70} ${y+20} L ${CX-52} ${y-80} M ${CX+70} ${y+20} L ${CX+52} ${y-80}"/>
 <path d="M ${CX-70} ${y-80} h 140 l -18 -30 h -104 z"/><path d="M ${CX} ${y-80} V ${y-16}"/>
 <path d="M ${CX-16} ${y-16} h 32 v 24 q -16 8 -32 0 z"/></g>
 <g ${st(.42,2.4)}><path d="M ${CX+120} ${y-120} c -6 10 6 16 0 26 M ${CX-124} ${y-104} c -6 10 6 16 0 26"/></g>${gp(CX,y-96,5)}`; });
def('door','L', r=>{ const y=180; return `<g ${st(.6,3)}>
 <path d="M ${CX-70} ${y+130} V ${y-40} A 70 70 0 0 1 ${CX+70} ${y-40} V ${y+130}"/>
 <path d="M ${CX-46} ${y+130} V ${y-30} A 46 46 0 0 1 ${CX+30} ${y-64} L ${CX+30} ${y+130}"/>
 <circle cx="${CX+12}" cy="${y+40}" r="5"/></g>
 <g ${st(.42,2.4)}>${[0.15,0.35,0.55].map(t=>`<line x1="${CX+36}" y1="${(y+10-t*90).toFixed(0)}" x2="${(CX+96+t*40).toFixed(0)}" y2="${(y+40-t*160).toFixed(0)}"/>`).join('')}</g>
 <path d="M ${CX-110} ${y+130} h 220 M ${CX-96} ${y+152} h 192" ${st(.5,2.6)}/>${gp(CX+12,y+40,5)}`; });
def('table','L', r=>{ const y=210; return `<g ${st(.6,3)}>
 <path d="M ${CX-150} ${y} h 300 M ${CX-130} ${y} V ${y+110} M ${CX+130} ${y} V ${y+110}"/>
 <path d="M ${CX-64} ${y-24} a 24 24 0 0 1 48 0 z M ${CX-40} ${y-24} v 24"/>
 <path d="M ${CX+28} ${y-16} q 30 -22 60 0 q -30 14 -60 0 z"/>
 <path d="M ${CX-6} ${y-58} v -26 M ${CX-6} ${y-58} c -10 0 -10 14 0 14 c 10 0 10 -14 0 -14"/></g>
 <g ${st(.42,2.4)}><path d="M ${CX-6} ${y-96} q -5 -10 0 -18"/></g>${gp(CX-6,y-70,4.5)}`; });
def('flame','L', r=>{ const y=200; return `<g ${st(.62,3.2)}>
 <path d="M ${CX} ${y+90} C ${CX-70} ${y+50} ${CX-56} ${y-40} ${CX-8} ${y-96} C ${CX-20} ${y-40} ${CX+18} ${y-46} ${CX+16} ${y-90} C ${CX+62} ${y-30} ${CX+64} ${y+54} ${CX} ${y+90} z"/>
 <path d="M ${CX} ${y+64} C ${CX-28} ${y+40} ${CX-20} ${y-4} ${CX+2} ${y-30} C ${CX-2} ${y} ${CX+22} ${y+2} ${CX+26} ${y+28} C ${CX+22} ${y+52} ${CX+8} ${y+62} ${CX} ${y+64} z"/></g>
 <g ${st(.4,2.4)}><path d="M ${CX-80} ${y+10} q -20 -30 -12 -66"/><path d="M ${CX+84} ${y+4} q 20 -30 12 -66"/></g>${gp(CX+4,y+16,6)}`; });
def('stars','L', r=>{ const y=170; const pts=[[-150,-40],[-70,-90],[10,-30],[90,-100],[170,-40],[40,40]];
 return `<g ${st(.5,2.2)}><path d="M ${pts.map(p=>(CX+p[0])+' '+(y+p[1])).join(' L ')}"/></g>
 ${pts.map(p=>`<circle cx="${CX+p[0]}" cy="${y+p[1]}" r="4" ${fillW(.7)}/>`).join('')}
 <path d="M ${CX-40} ${y+90} l 9 18 20 3 -14 14 3 20 -18 -9 -18 9 3 -20 -14 -14 20 -3 z" ${st(.6,2.8)}/>
 <path d="M ${CX+150} ${y+60} a 30 30 0 1 0 20 52 a 24 24 0 0 1 -20 -52 z" ${st(.5,2.6)}/>${gp(CX+90,y-100,6)}`; });
def('shepherd','L', r=>{ const y=250; return `<g ${st(.6,3)}>
 <path d="M ${CX+90} ${y+70} V ${y-110} a 26 26 0 1 0 -40 20"/>
 <path d="M ${CX-250} ${y+40} q 120 -44 250 -10 q 130 34 250 6" stroke-width="2.2" stroke="rgba(255,255,255,.32)"/></g>
 ${[[-140,30],[-60,52],[10,26]].map(p=>`<g ${st(.55,2.6)}>
 <path d="M ${CX+p[0]-30} ${y+p[1]} a 16 16 0 0 1 8 -22 a 18 18 0 0 1 24 -8 a 16 16 0 0 1 26 6 a 14 14 0 0 1 2 24 q -30 10 -60 0 z"/>
 <circle cx="${CX+p[0]+30}" cy="${y+p[1]-24}" r="9"/>
 <path d="M ${CX+p[0]-18} ${y+p[1]+2} v 16 M ${CX+p[0]+8} ${y+p[1]+2} v 16"/></g>`).join('')}${gp(CX+90,y-116,5)}`; });
def('blueprint','L', r=>{ const y=200; return `<g ${st(.55,2.6)}>
 <path d="M ${CX-110} ${y+110} V ${y+10} L ${CX} ${y-70} L ${CX+110} ${y+10} V ${y+110}" stroke-dasharray="9 8"/>
 <path d="M ${CX-110} ${y+110} h 220"/>
 <rect x="${CX-88}" y="${y+58}" width="52" height="52" rx="3"/>
 <path d="M ${CX-88} ${y+58} l 52 52 M ${CX-36} ${y+58} l -52 52" stroke-width="2"/>
 <path d="M ${CX+30} ${y+66} h 52 v 44 h -52 z M ${CX+56} ${y+66} v 44"/></g>
 <g ${st(.5,2.6)}><path d="M ${CX-170} ${y-40} h 60 M ${CX-170} ${y-52} v 24 M ${CX-110} ${y-52} v 24"/><circle cx="${CX-140}" cy="${y-40}" r="5"/></g>${gp(CX-62,y+84,6)}`; });
def('restnight','L', r=>{ const y=180; return `<g ${st(.6,3)}>
 <path d="M ${CX-20} ${y-70} a 62 62 0 1 0 44 106 a 52 52 0 0 1 -44 -106 z"/>
 <path d="M ${CX-140} ${y+90} q 140 -34 280 0 M ${CX-110} ${y+118} q 110 -26 220 0"/></g>
 <path d="M ${CX+90} ${y-60} l 6 12 13 2 -9 9 2 13 -12 -6 -12 6 2 -13 -9 -9 13 -2 z" ${fillW(.6)}/>
 <circle cx="${CX-130}" cy="${y-90}" r="2.6" ${fillW(.5)}/>${gp(CX-20,y-70,4.5)}`; });
def('shield','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX} ${y-90} C ${CX+50} ${y-70} ${CX+90} ${y-72} ${CX+96} ${y-58} C ${CX+96} ${y+30} ${CX+64} ${y+96} ${CX} ${y+126} C ${CX-64} ${y+96} ${CX-96} ${y+30} ${CX-96} ${y-58} C ${CX-90} ${y-72} ${CX-50} ${y-70} ${CX} ${y-90} z"/>
 <path d="M ${CX} ${y-56} V ${y+92} M ${CX-64} ${y+8} H ${CX+64}"/></g>${gp(CX,y+8,6)}`; });
def('bird','L', r=>{ const y=180; return `<g ${st(.62,3)}>
 <path d="M ${CX-30} ${y} C ${CX-90} ${y-60} ${CX-150} ${y-56} ${CX-180} ${y-30} C ${CX-130} ${y-26} ${CX-92} ${y-10} ${CX-56} ${y+10}"/>
 <path d="M ${CX-30} ${y} C ${CX+16} ${y-70} ${CX+90} ${y-80} ${CX+140} ${y-60} C ${CX+96} ${y-40} ${CX+50} ${y-16} ${CX+8} ${y+12}"/>
 <path d="M ${CX-56} ${y+10} q 30 26 64 2"/><path d="M ${CX+8} ${y+12} l 40 34 M ${CX+30} ${y+30} l 26 6"/></g>
 <path d="M ${CX+120} ${y+120} C ${CX+108} ${y+96} ${CX+130} ${y+80} ${CX+150} ${y+76} C ${CX+146} ${y+98} ${CX+138} ${y+114} ${CX+120} ${y+120} z M ${CX+124} ${y+116} L ${CX+146} ${y+82}" ${st(.5,2.4)}/>${gp(CX-30,y,5)}`; });
def('chainbreak','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <rect x="${CX-150}" y="${y-20}" width="56" height="34" rx="17"/><rect x="${CX-104}" y="${y-2}" width="56" height="34" rx="17"/>
 <rect x="${CX+48}" y="${y-2}" width="56" height="34" rx="17"/><rect x="${CX+94}" y="${y-20}" width="56" height="34" rx="17"/>
 <path d="M ${CX-30} ${y-6} l 18 -14 M ${CX-24} ${y+16} l 20 -4 M ${CX+30} ${y-10} l -16 -12 M ${CX+26} ${y+16} l -18 -2" stroke-width="2.6"/></g>
 <g ${st(.42,2.4)}>${[0.25,0.5,0.75].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+Math.cos(a)*70).toFixed(0)}" y1="${(y-40-Math.sin(a)*70).toFixed(0)}" x2="${(CX+Math.cos(a)*104).toFixed(0)}" y2="${(y-40-Math.sin(a)*104).toFixed(0)}"/>`;}).join('')}</g>${gp(CX,y-40,6)}`; });
def('globe','L', r=>{ const y=190; const R=96; return `<g ${st(.58,2.8)}>
 <circle cx="${CX}" cy="${y}" r="${R}"/>
 <ellipse cx="${CX}" cy="${y}" rx="${R/3}" ry="${R}"/><ellipse cx="${CX}" cy="${y}" rx="${R*2/3}" ry="${R}"/>
 <ellipse cx="${CX}" cy="${y}" rx="${R}" ry="${R/3}"/><path d="M ${CX-R} ${y-R*0.62} q ${R} 40 ${2*R} 0 M ${CX-R} ${y+R*0.62} q ${R} -40 ${2*R} 0"/></g>
 ${[[-130,-130],[150,-100],[120,120],[-160,90]].map(p=>`<path d="M ${CX+p[0]-7} ${y+p[1]} h 14 M ${CX+p[0]} ${y+p[1]-7} v 14" ${st(.5,2.4)}/>`).join('')}${gp(CX+R*0.5,y-R*0.55,6)}`; });
def('wheat','L', r=>{ const y=230;
 const stalk=(x,tilt)=>{ let s=`<path d="M ${x} ${y+90} C ${x+tilt*8} ${y+30} ${x+tilt*14} ${y-30} ${x+tilt*18} ${y-80}" ${st(.58,2.8)}/>`;
  for(let i=0;i<6;i++){ const t=i/6, px=x+tilt*(8+t*10), py=y+60-t*130;
   s+=`<path d="M ${px} ${py} q ${-14-tilt*4} -12 ${-10-tilt*4} -30 q 14 8 ${10+tilt*4} 30 z M ${px} ${py} q ${14-tilt*4} -12 ${10-tilt*4} -30 q -14 8 ${-10+tilt*4} 30 z" ${st(.5,2.2)}/>`; }
  return s; };
 return stalk(CX-60,-1)+stalk(CX,0)+stalk(CX+60,1)+`<path d="M ${CX-110} ${y+90} q 110 30 220 0" ${st(.5,2.6)}/>${gp(CX+18,y-80,5)}`; });

/* ============ 22 new primitives ============ */
def('dove','L', r=>{ const y=190; return `<g ${st(.62,3)}>
 <path d="M ${CX-10} ${y+20} C ${CX-70} ${y+6} ${CX-96} ${y-30} ${CX-84} ${y-56} C ${CX-50} ${y-46} ${CX-26} ${y-22} ${CX-10} ${y+20} z"/>
 <path d="M ${CX-10} ${y+20} C ${CX+30} ${y-56} ${CX+96} ${y-70} ${CX+130} ${y-40} C ${CX+92} ${y-8} ${CX+40} ${y+16} ${CX-10} ${y+20}"/>
 <path d="M ${CX+118} ${y-46} q 20 -2 30 8 M ${CX+130} ${y-40} l 16 -4"/>
 <path d="M ${CX-10} ${y+20} q -14 34 -50 44 M ${CX-24} ${y+30} q -6 26 -30 38"/>
 <path d="M ${CX-70} ${y+72} q 12 -4 16 -14 l 8 10 q 10 -4 12 -12" stroke-width="2.2"/></g>
 <path d="M ${CX+52} ${y+58} q 18 -6 24 -20 q 12 8 26 4" ${st(.45,2.4)}/>${gp(CX+140,y-42,4.5)}`; });
def('sail','L', r=>{ const y=210; return `<g ${st(.6,3)}>
 <path d="M ${CX-120} ${y+60} q 120 44 240 0 l -26 34 h -188 z"/>
 <path d="M ${CX} ${y+56} V ${y-120}"/>
 <path d="M ${CX} ${y-120} C ${CX+90} ${y-84} ${CX+96} ${y-10} ${CX+8} ${y+36} z"/>
 <path d="M ${CX-8} ${y-96} C ${CX-72} ${y-64} ${CX-76} ${y-6} ${CX-8} ${y+30} z"/>
 <path d="M ${CX} ${y-120} l 26 -14 v 16 z"/></g>
 <g ${st(.42,2.4)}><path d="M ${CX-170} ${y+96} q 40 -16 80 0 M ${CX+92} ${y+98} q 40 -16 80 0"/><path d="M ${CX-150} ${y-140} q 10 -12 22 0 q 10 -12 22 0"/></g>${gp(CX+26,y-130,5)}`; });
def('bridge','L', r=>{ const y=220; return `<g ${st(.58,2.8)}>
 <path d="M ${CX-230} ${y} H ${CX+230}"/>
 <path d="M ${CX-230} ${y} C ${CX-120} ${y-130} ${CX+120} ${y-130} ${CX+230} ${y}"/>
 ${[-160,-90,-30,30,90,160].map(x=>`<line x1="${CX+x}" y1="${y}" x2="${CX+x}" y2="${(y-118+Math.abs(x)*0.42).toFixed(0)}"/>`).join('')}
 <path d="M ${CX-230} ${y+26} H ${CX+230}" stroke-width="2.2" stroke="rgba(255,255,255,.36)"/></g>
 <g ${st(.4,2.2)}><path d="M ${CX-140} ${y+56} q 30 -12 60 0 M ${CX+80} ${y+56} q 30 -12 60 0"/></g>${gp(CX,y-118,5.5)}`; });
def('hourglass','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX-70} ${y-100} h 140 M ${CX-70} ${y+100} h 140"/>
 <path d="M ${CX-56} ${y-100} C ${CX-56} ${y-30} ${CX-12} ${y-16} ${CX-6} ${y} C ${CX-12} ${y+16} ${CX-56} ${y+30} ${CX-56} ${y+100}"/>
 <path d="M ${CX+56} ${y-100} C ${CX+56} ${y-30} ${CX+12} ${y-16} ${CX+6} ${y} C ${CX+12} ${y+16} ${CX+56} ${y+30} ${CX+56} ${y+100}"/>
 <path d="M ${CX-34} ${y-64} q 34 20 68 0" stroke-width="2.4"/>
 <path d="M ${CX-40} ${y+84} h 80 l -34 -40 h -12 z" ${fillW(.35)}/></g>
 <path d="M ${CX} ${y-4} v 60" ${st(.5,2)} stroke-dasharray="2 7"/>${gp(CX,y,4.5)}`; });
def('bell','L', r=>{ const y=190; return `<g ${st(.62,3)}>
 <path d="M ${CX-74} ${y+56} C ${CX-74} ${y-44} ${CX-40} ${y-88} ${CX} ${y-88} C ${CX+40} ${y-88} ${CX+74} ${y-44} ${CX+74} ${y+56} z"/>
 <path d="M ${CX-92} ${y+56} h 184"/>
 <circle cx="${CX}" cy="${y+78}" r="12"/>
 <path d="M ${CX-8} ${y-88} a 8 8 0 0 1 16 0"/></g>
 <g ${st(.42,2.4)}><path d="M ${CX-108} ${y-40} q -16 -8 -22 -26 M ${CX-100} ${y-70} q -12 -10 -14 -26"/><path d="M ${CX+108} ${y-40} q 16 -8 22 -26 M ${CX+100} ${y-70} q 12 -10 14 -26"/></g>${gp(CX,y-96,5)}`; });
def('gate','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX-110} ${y+110} V ${y-60} M ${CX+110} ${y+110} V ${y-60}"/>
 <path d="M ${CX-110} ${y-60} A 110 110 0 0 1 ${CX+110} ${y-60}"/>
 ${[-70,-35,0,35,70].map(x=>`<line x1="${CX+x}" y1="${y+110}" x2="${CX+x}" y2="${(y-52-Math.cos(x/110*1.57)*46).toFixed(0)}"/>`).join('')}
 <path d="M ${CX-110} ${y+30} h 220"/></g>
 <g ${st(.42,2.4)}><path d="M ${CX-160} ${y+110} h -30 M ${CX+160} ${y+110} h 30"/></g>${gp(CX,y-150,5)}`; });
def('olive','L', r=>{ const y=190; return `<g ${st(.6,2.8)}>
 <path d="M ${CX-140} ${y+70} C ${CX-60} ${y+20} ${CX+60} ${y-60} ${CX+150} ${y-96}"/>
 ${[[0.2,-1],[0.35,1],[0.5,-1],[0.65,1],[0.8,-1]].map(([t,sd])=>{const px=CX-140+t*290, py=y+70-t*166;
  return `<path d="M ${px} ${py} q ${sd*26} ${-14} ${sd*38} ${-40} q ${-sd*30} ${6} ${-sd*38} ${40} z"/>`;}).join('')}
 <circle cx="${CX-40}" cy="${y+44}" r="7"/><circle cx="${CX+30}" cy="${y-4}" r="7"/></g>${gp(CX+150,y-96,5)}`; });
def('rainbow','L', r=>{ const y=250; return `<g ${st(.55,3)}>
 ${[120,150,180].map((R,i)=>`<path d="M ${CX-R} ${y} A ${R} ${R} 0 0 1 ${CX+R} ${y}" stroke="rgba(255,255,255,${.6-i*.14})"/>`).join('')}
 <path d="M ${CX-230} ${y} H ${CX+230}" stroke-width="2.2"/></g>
 <g ${st(.45,2.4)}><path d="M ${CX-190} ${y-160} q 12 -14 26 0 q 12 -14 26 0"/><path d="M ${CX+150} ${y-190} q 11 -13 24 0 q 11 -13 24 0"/></g>
 <path d="M ${CX-60} ${y-40} c -6 10 6 16 0 26 M ${CX+52} ${y-56} c -6 10 6 16 0 26" ${st(.42,2.2)}/>${gp(CX,y-180,5.5)}`; });
def('scroll','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX-96} ${y-80} h 168 a 22 22 0 0 1 0 44 h -12"/>
 <path d="M ${CX-96} ${y-80} a 22 22 0 0 0 0 44 h 10 V ${y+96} a 20 20 0 0 1 -40 0 a 20 20 0 0 1 40 0"/>
 <path d="M ${CX-86} ${y-36} H ${CX+60} V ${y+96} H ${CX-86}"/>
 <path d="M ${CX-64} ${y-6} h 100 M ${CX-64} ${y+18} h 112 M ${CX-64} ${y+42} h 86 M ${CX-64} ${y+66} h 104" stroke-width="2.2" stroke="rgba(255,255,255,.42)"/></g>${gp(CX+72,y-58,5)}`; });
def('chalice','L', r=>{ const y=190; return `<g ${st(.62,3)}>
 <path d="M ${CX-84} ${y-70} h 168 c 0 70 -50 104 -84 108 c -34 -4 -84 -38 -84 -108 z"/>
 <path d="M ${CX} ${y+38} V ${y+92} M ${CX-52} ${y+112} a 52 16 0 0 1 104 0 z"/>
 <path d="M ${CX-64} ${y-48} q 64 24 128 0" stroke-width="2.4"/></g>
 <g ${st(.42,2.4)}>${[0.3,0.5,0.7].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+Math.cos(a)*104).toFixed(0)}" y1="${(y-84-Math.sin(a)*30).toFixed(0)}" x2="${(CX+Math.cos(a)*128).toFixed(0)}" y2="${(y-84-Math.sin(a)*54).toFixed(0)}"/>`;}).join('')}</g>${gp(CX,y-84,5)}`; });
def('fishnet','L', r=>{ const y=200; return `<g ${st(.58,2.8)}>
 ${[[-70,-30,1],[40,10,-1],[-20,60,1]].map(([dx,dy,sd])=>`<g><path d="M ${CX+dx-44*sd} ${y+dy} q ${44*sd} -30 ${88*sd} 0 q ${-44*sd} 30 ${-88*sd} 0 z"/><path d="M ${CX+dx+44*sd} ${y+dy} l ${20*sd} -14 v 28 z"/><circle cx="${CX+dx-24*sd}" cy="${y+dy-6}" r="2.6" ${fillW(.7)}/></g>`).join('')}
 <path d="M ${CX-150} ${y-96} q 150 60 300 -10" stroke-dasharray="1 9" stroke-width="2.2"/></g>${gp(CX+96,y+4,5)}`; });
def('ladder','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX-44} ${y+120} L ${CX-16} ${y-120} M ${CX+44} ${y+120} L ${CX+16} ${y-120}"/>
 ${[0,1,2,3,4,5].map(i=>{const t=i/5;const xL=CX-44+28*t, xR=CX+44-28*t, yy=y+120-240*t;return `<line x1="${xL.toFixed(0)}" y1="${yy.toFixed(0)}" x2="${xR.toFixed(0)}" y2="${yy.toFixed(0)}"/>`;}).join('')}</g>
 <g ${st(.42,2.4)}><path d="M ${CX-90} ${y-130} q 12 -14 26 0"/><circle cx="${CX+92}" cy="${y-140}" r="3" ${fillW(.6)}/></g>${gp(CX,y-140,5.5)}`; });
def('tent','L', r=>{ const y=210; return `<g ${st(.6,3)}>
 <path d="M ${CX-130} ${y+70} L ${CX} ${y-90} L ${CX+130} ${y+70} z"/>
 <path d="M ${CX} ${y-90} V ${y+70} M ${CX-34} ${y+70} L ${CX} ${y+6} L ${CX+34} ${y+70}"/>
 <path d="M ${CX-130} ${y+70} l -26 20 M ${CX+130} ${y+70} l 26 20"/></g>
 <g ${st(.45,2.4)}><path d="M ${CX+150} ${y-60} l 6 12 13 2 -9 9 2 13 -12 -6 -12 6 2 -13 -9 -9 13 -2 z"/></g>${gp(CX,y-98,5)}`; });
def('skyline','L', r=>{ const y=230; return `<g ${st(.58,2.8)}>
 <path d="M ${CX-210} ${y+60} V ${y-20} h 60 V ${y+60} M ${CX-150} ${y-20} V ${y-70} h 70 V ${y+60} M ${CX-80} ${y-70} l 35 -40 35 40 M ${CX-10} ${y+60} V ${y-40} h 64 V ${y+60} M ${CX+54} ${y-40} V ${y-96} h 56 V ${y+60} M ${CX+110} ${y-96} l 28 -24 M ${CX+138} ${y-120} v 180 M ${CX+138} ${y+60} h 72 M ${CX+210} ${y+60} V ${y-8} h -40"/>
 ${[[-190,10],[-120,-40],[-120,0],[20,-10],[80,-70],[80,-20]].map(p=>`<rect x="${CX+p[0]}" y="${y+p[1]}" width="12" height="12"/>`).join('')}</g>${gp(CX-45,y-116,5)}`; });
def('vine','L', r=>{ const y=190; return `<g ${st(.6,2.8)}>
 <path d="M ${CX-170} ${y-70} C ${CX-60} ${y-110} ${CX+60} ${y-30} ${CX+170} ${y-70}"/>
 ${[[-90,-88,1],[30,-64,-1],[120,-78,1]].map(([dx,dy,sd])=>`<path d="M ${CX+dx} ${y+dy} q ${sd*10} 20 0 34"/>`).join('')}
 ${[[-90,-40],[30,-16],[120,-30]].map(p=>{const cx0=CX+p[0], cy0=y+p[1]; return [[0,0],[-14,20],[14,20],[0,40],[-10,58]].map(q=>`<circle cx="${cx0+q[0]}" cy="${cy0+q[1]}" r="9"/>`).join('');}).join('')}
 <path d="M ${CX-130} ${y-84} q -18 -22 -8 -44 q 22 6 8 44 z"/></g>${gp(CX+170,y-70,5)}`; });
def('knot','L', r=>{ const y=190; return `<g ${st(.6,3.2)}>
 <path d="M ${CX-120} ${y-40} C ${CX-40} ${y-90} ${CX+40} ${y+10} ${CX+120} ${y-40}"/>
 <path d="M ${CX-120} ${y+40} C ${CX-40} ${y+90} ${CX+40} ${y-10} ${CX+120} ${y+40}"/>
 <path d="M ${CX-120} ${y-40} q -26 40 0 80 M ${CX+120} ${y-40} q 26 40 0 80"/></g>${gp(CX,y,5.5)}`; });
def('northstar','L', r=>{ const y=180; return `
 <path d="M ${CX} ${y-110} L ${CX+18} ${y-18} L ${CX+110} ${y} L ${CX+18} ${y+18} L ${CX} ${y+110} L ${CX-18} ${y+18} L ${CX-110} ${y} L ${CX-18} ${y-18} z" ${st(.62,3)}/>
 <circle cx="${CX}" cy="${y}" r="150" ${st(.3,1.8)} stroke-dasharray="1 9"/>
 ${[[-120,-90],[130,-70],[100,110],[-140,80]].map(p=>`<circle cx="${CX+p[0]}" cy="${y+p[1]}" r="3" ${fillW(.55)}/>`).join('')}${gp(CX,y,6)}`; });
def('footsteps','L', r=>{ const y=210; return `<g ${st(.58,2.8)}>
 ${[[-120,80,-14],[-40,30,10],[40,-20,-14],[120,-70,10]].map(([dx,dy,rot])=>`<g transform="rotate(${rot} ${CX+dx} ${y+dy})"><ellipse cx="${CX+dx}" cy="${y+dy}" rx="16" ry="26"/><ellipse cx="${CX+dx}" cy="${y+dy-38}" rx="10" ry="9"/></g>`).join('')}
 <path d="M ${CX-170} ${y+130} C ${CX-60} ${y+70} ${CX+40} ${y+10} ${CX+170} ${y-110}" stroke-dasharray="2 10" stroke-width="2"/></g>${gp(CX+150,y-96,5)}`; });
def('together','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX-110} ${y+40} a 44 44 0 1 1 62 -62"/>
 <path d="M ${CX+110} ${y+40} a 44 44 0 1 0 -62 -62"/>
 <path d="M ${CX-58} ${y-14} C ${CX-30} ${y-40} ${CX+30} ${y-40} ${CX+58} ${y-14} C ${CX+40} ${y+20} ${CX-40} ${y+20} ${CX-58} ${y-14} z"/>
 <path d="M ${CX-24} ${y-2} h 48 M ${CX-16} ${y+12} h 32" stroke-width="2.4"/></g>
 <path d="M ${CX-96} ${y+96} q 96 40 192 0" ${st(.42,2.4)}/>${gp(CX,y-30,5)}`; });
def('candles','L', r=>{ const y=200; return `<g ${st(.6,3)}>
 ${[[-70,20,54],[0,0,74],[70,26,48]].map(([dx,dy,h])=>`<g>
 <path d="M ${CX+dx-14} ${y+dy+80} v ${-h} h 28 v ${h}"/>
 <path d="M ${CX+dx} ${y+dy+80-h-8} C ${CX+dx-9} ${y+dy+80-h-22} ${CX+dx-2} ${y+dy+80-h-34} ${CX+dx} ${y+dy+80-h-40} C ${CX+dx+8} ${y+dy+80-h-28} ${CX+dx+9} ${y+dy+80-h-20} ${CX+dx} ${y+dy+80-h-8} z"/></g>`).join('')}
 <path d="M ${CX-120} ${y+86} h 240" stroke-width="2.4"/></g>${gp(CX,y-40,5)}`; });
def('letter','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <rect x="${CX-110}" y="${y-58}" width="220" height="140" rx="10"/>
 <path d="M ${CX-110} ${y-50} L ${CX} ${y+22} L ${CX+110} ${y-50}"/>
 <path d="M ${CX-104} ${y+76} l 74 -54 M ${CX+104} ${y+76} l -74 -54"/></g>
 <path d="M ${CX+96} ${y-96} l 6 12 13 2 -9 9 2 13 -12 -6 -12 6 2 -13 -9 -9 13 -2 z" ${st(.5,2.4)}/>${gp(CX,y+22,5)}`; });
def('window','L', r=>{ const y=190; return `<g ${st(.6,3)}>
 <path d="M ${CX-80} ${y+110} V ${y-40} A 80 80 0 0 1 ${CX+80} ${y-40} V ${y+110} z"/>
 <path d="M ${CX} ${y-118} V ${y+110} M ${CX-80} ${y+10} h 160"/></g>
 <g ${st(.42,2.4)}>${[0.2,0.45,0.7].map(t=>`<line x1="${(CX-140-t*40).toFixed(0)}" y1="${(y-90+t*160).toFixed(0)}" x2="${CX-88}" y2="${(y-30+t*80).toFixed(0)}"/>`).join('')}</g>
 <path d="M ${CX+40} ${y+64} c -7 -10 -22 -5 -19 7 c 2 8 12 10 19 17 c 7 -7 17 -9 19 -17 c 3 -12 -12 -17 -19 -7 z" ${st(.5,2.4)}/>${gp(CX,y-118,5)}`; });

module.exports = { PRIM, KIND, GOLD, st, fillW, gp };
