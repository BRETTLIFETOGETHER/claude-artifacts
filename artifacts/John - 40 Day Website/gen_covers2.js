/* gen_covers2.js — 1,252 unique, topic-aware, portrait campaign covers.
   Reads each campaign's title/theme/subtitle, picks a detailed scene from a
   36-motif illustrated vocabulary, layers pattern + frame + grain, and sets
   a centered title stack inside a crop-safe zone (survives 16:10.4 crops). */
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
const GOLD='#E4AC43';
const W=600, H=800;
const CX=300;

function seedOf(str){ let h=5381; for(let i=0;i<str.length;i++){ h=((h<<5)+h+str.charCodeAt(i))>>>0; } return h; }
function rng(seed){ let a=seed>>>0; return function(){ a|=0; a=(a+0x6D2B79F5)|0; let t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&apos;');
const st=(o,w)=>`stroke="rgba(255,255,255,${o})" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round"`;
const fillW=o=>`fill="rgba(255,255,255,${o})"`;

/* =================== BACKGROUND PATTERN FIELDS =================== */
const PATTERNS = [
  r=>{ let s='<g '+st(.06,1.4)+'>'; for(let x=-800;x<W+100;x+=26+Math.floor(r()*4)) s+=`<line x1="${x}" y1="0" x2="${x+520}" y2="${H}"/>`; return s+'</g>'; },
  r=>{ let s='<g '+fillW(.07)+'>'; const g=34+Math.floor(r()*8); for(let x=g/2;x<W;x+=g) for(let y=g/2;y<H;y+=g) s+=`<circle cx="${x}" cy="${y}" r="1.6"/>`; return s+'</g>'; },
  r=>{ let s='<g '+st(.055,1.3)+'>'; const cx=r()*W, cy=r()*H; for(let i=1;i<14;i++) s+=`<circle cx="${cx.toFixed(0)}" cy="${cy.toFixed(0)}" r="${i*62}"/>`; return s+'</g>'; },
  r=>{ let s='<g '+st(.05,1.2)+'>'; for(let y=-40;y<H+40;y+=30){ let d=`M -20 ${y}`; for(let x=-20;x<=W+20;x+=44) d+=` l 22 ${-12} l 22 12`; s+=`<path d="${d}"/>`; } return s+'</g>'; },
  r=>{ let s='<g '+st(.06,1.3)+'>'; for(let y=20;y<H;y+=52) for(let x=((y/52)%2)*30+16;x<W;x+=60) s+=`<path d="M ${x-9} ${y} H ${x+9} M ${x} ${y-9} V ${y+9}"/>`; return s+'</g>'; },
  r=>{ let s='<g '+st(.06,1.3)+'>'; for(let y=0;y<H+60;y+=46) for(let x=((y/46)%2)*33;x<W+40;x+=66) s+=`<path d="M ${x-33} ${y} A 33 33 0 0 1 ${x+33} ${y}"/>`; return s+'</g>'; },
  r=>{ let s='<g '+st(.05,1.2)+'>'; for(let i=-14;i<20;i++){ s+=`<line x1="${i*60}" y1="0" x2="${i*60+400}" y2="${H}"/><line x1="${i*60}" y1="${H}" x2="${i*60+400}" y2="0"/>`; } return s+'</g>'; },
  r=>{ let s='<g '+st(.06,1.3)+'>'; const cx=CX, cy=H+140; for(let a=0;a<Math.PI;a+=Math.PI/16) s+=`<line x1="${cx}" y1="${cy}" x2="${(cx+Math.cos(a)*1200).toFixed(0)}" y2="${(cy-Math.sin(a)*1200).toFixed(0)}"/>`; return s+'</g>'; }
];

/* =================== 36 DETAILED TOPIC MOTIFS ===================
   Each draws a scene in the TOP band (roughly y 70–300, centered on x=300)
   plus a small grounding element in the BOTTOM band (y 640–740). */
function gPoint(x,y,r=6){ return `<circle cx="${x}" cy="${y}" r="${r}" fill="${GOLD}"/>`; }

const M = {};
M.keys = r=>{ const y=185;
  return `<g ${st(.6,3)}>
    <circle cx="${CX-52}" cy="${y-28}" r="34"/><circle cx="${CX-52}" cy="${y-28}" r="15"/>
    <path d="M ${CX-22} ${y-8} L ${CX+66} ${y+56} M ${CX+34} ${y+32} l 16 -20 M ${CX+52} ${y+46} l 16 -20"/>
    <rect x="${CX-118}" y="${y+52}" width="150" height="96" rx="8"/>
    <path d="M ${CX-98} ${y+78} h 96 M ${CX-98} ${y+98} h 110 M ${CX-98} ${y+118} h 76"/></g>
  <circle cx="${CX+8}" cy="${y+128}" r="17" ${st(.55,2.6)}/><path d="M ${CX+2} ${y+128} l 5 5 9 -11" ${st(.7,2.6)}/>
  ${gPoint(CX+66,y+56)}
  <path d="M ${CX-120} 700 h 240 M ${CX-84} 716 h 168" ${st(.3,2)}/>`; };
M.torch = r=>{ const y=200;
  return `<g ${st(.62,3.2)}>
    <path d="M ${CX-14} ${y+40} L ${CX-30} ${y+150} h 60 L ${CX+14} ${y+40} z"/>
    <path d="M ${CX-34} ${y+34} h 68"/>
    <path d="M ${CX} ${y+22} C ${CX-40} ${y-8} ${CX-26} ${y-62} ${CX} ${y-84} C ${CX+26} ${y-62} ${CX+40} ${y-8} ${CX} ${y+22}"/>
    <path d="M ${CX} ${y+8} C ${CX-16} ${y-12} ${CX-8} ${y-38} ${CX} ${y-50} C ${CX+8} ${y-38} ${CX+16} ${y-12} ${CX} ${y+8}"/></g>
  <g ${st(.4,2.4)}><path d="M ${CX-84} ${y-40} q -26 -26 -30 -60"/><path d="M ${CX+84} ${y-40} q 26 -26 30 -60"/></g>
  <circle cx="${CX-58}" cy="${y-96}" r="4" ${fillW(.7)}/><circle cx="${CX+64}" cy="${y-108}" r="3.4" ${fillW(.6)}/><circle cx="${CX+30}" cy="${y-140}" r="2.8" ${fillW(.5)}/>
  ${gPoint(CX,y-50,7)}
  <path d="M ${CX-110} 706 q 55 -22 110 0 q 55 22 110 0" ${st(.3,2.2)}/>`; };
M.heart = r=>{ const y=190;
  return `<g ${st(.62,3.2)}>
    <path d="M ${CX} ${y+96} C ${CX-120} ${y+10} ${CX-84} ${y-88} ${CX-6} ${y-30} C ${CX+78} ${y-92} ${CX+122} ${y+8} ${CX} ${y+96} z"/>
    <path d="M ${CX-64} ${y-18} q 20 -30 52 -26"/></g>
  <path d="M ${CX-170} ${y+130} h 70 l 16 -30 20 56 16 -26 h 218" ${st(.45,2.6)}/>
  <g ${st(.35,2.2)}><path d="M ${CX-120} ${y-96} l 0 -22 M ${CX-131} ${y-107} l 22 0"/><path d="M ${CX+128} ${y-70} l 0 -18 M ${CX+119} ${y-79} l 18 0"/></g>
  ${gPoint(CX,y-34)}
  <path d="M ${CX-96} 700 C ${CX-40} 676 ${CX+40} 724 ${CX+96} 700" ${st(.3,2.2)}/>`; };
M.scales = r=>{ const y=150;
  return `<g ${st(.6,3)}>
    <path d="M ${CX} ${y} v 178 M ${CX-120} ${y+34} h 240 M ${CX} ${y} l -120 34 M ${CX} ${y} l 120 34"/>
    <path d="M ${CX-120} ${y+34} l -34 62 h 68 z M ${CX+120} ${y+34} l -34 62 h 68 z"/>
    <path d="M ${CX-154} ${y+96} a 34 20 0 0 0 68 0 M ${CX+86} ${y+96} a 34 20 0 0 0 68 0"/>
    <path d="M ${CX-56} ${y+178} h 112 M ${CX-40} ${y+196} h 80"/></g>
  <circle cx="${CX}" cy="${y-16}" r="12" ${st(.6,3)}/>${gPoint(CX,y-16,5)}
  <path d="M ${CX-110} 702 h 220" ${st(.3,2.2)}/><circle cx="${CX}" cy="702" r="5" ${st(.3,2)}/>`; };
M.anchor = r=>{ const y=170;
  return `<g ${st(.62,3.2)}>
    <circle cx="${CX}" cy="${y-38}" r="20"/>
    <path d="M ${CX} ${y-18} V ${y+140} M ${CX-58} ${y+18} h 116"/>
    <path d="M ${CX-88} ${y+96} a 88 88 0 0 0 176 0 M ${CX-88} ${y+96} l -18 -24 M ${CX-88} ${y+96} l 26 -14 M ${CX+88} ${y+96} l 18 -24 M ${CX+88} ${y+96} l -26 -14"/></g>
  <path d="M ${CX+26} ${y-52} q 60 -30 92 6 q 22 26 -6 44" ${st(.35,2.4)}/>
  ${gPoint(CX,y-38,5)}
  <g ${st(.35,2.4)}><path d="M ${CX-150} 690 q 37 -18 75 0 q 38 18 75 0 q 37 -18 75 0 q 38 18 75 0"/><path d="M ${CX-110} 716 q 37 -18 74 0 q 37 18 74 0 q 37 -18 74 0"/></g>`; };
M.lighthouse = r=>{ const y=250; const bx=CX;
  return `<g ${st(.6,3)}>
    <path d="M ${bx-30} ${y+60} L ${bx-20} ${y-92} h 40 L ${bx+30} ${y+60}"/>
    <path d="M ${bx-26} ${y-92} h 52 M ${bx-16} ${y-112} h 32 M ${bx-16} ${y-112} v -22 h 32 v 22 M ${bx-22} ${y-134} h 44 l -22 -22 z"/>
    <path d="M ${bx-27} ${y-40} h 54 M ${bx-24} ${y+6} h 48"/></g>
  <g ${st(.4,2.4)}><path d="M ${bx-34} ${y-122} l -78 -26 M ${bx-34} ${y-114} l -80 6"/><path d="M ${bx+34} ${y-122} l 78 -26 M ${bx+34} ${y-114} l 80 6"/></g>
  <g ${st(.42,2.6)}><path d="M ${bx-190} ${y+66} q 46 -22 92 0 q 46 22 92 0 q 46 -22 92 0 q 46 22 92 0"/><path d="M ${bx-150} ${y+94} q 50 -22 100 0 q 50 22 100 0"/></g>
  <path d="M ${bx-120} ${y-160} q 10 -12 22 0 q 10 -12 22 0 M ${bx+80} ${y-186} q 9 -11 20 0 q 9 -11 20 0" ${st(.45,2.4)}/>
  ${gPoint(bx,y-123,6)}`; };
M.sunrise = r=>{ const hy=240;
  return `<g ${st(.55,2.8)}>
    <path d="M ${CX-96} ${hy} A 96 96 0 0 1 ${CX+96} ${hy}"/>
    <path d="M ${CX-250} ${hy} H ${CX+250}"/>
    <path d="M ${CX-236} ${hy+44} q 96 -50 192 0 q -96 26 -192 0 z M ${CX+44} ${hy+44} q 96 -50 192 0 q -96 26 -192 0 z" stroke-width="2.4"/></g>
  <g ${st(.5,2.6)}>${[0.14,0.32,0.5,0.68,0.86].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+Math.cos(a)*118).toFixed(0)}" y1="${(hy-Math.sin(a)*118).toFixed(0)}" x2="${(CX+Math.cos(a)*152).toFixed(0)}" y2="${(hy-Math.sin(a)*152).toFixed(0)}"/>`;}).join('')}</g>
  <path d="M ${CX-150} ${hy-140} q 11 -13 24 0 q 11 -13 24 0 M ${CX+96} ${hy-170} q 10 -12 22 0 q 10 -12 22 0" ${st(.5,2.4)}/>
  ${gPoint(CX,hy-64,7)}
  <path d="M ${CX-120} 700 H ${CX+120} M ${CX-80} 716 H ${CX+80}" ${st(.28,2)}/>`; };
M.sprout = r=>{ const y=250;
  return `<g ${st(.6,3)}>
    <path d="M ${CX} ${y+40} V ${y-70}"/>
    <path d="M ${CX} ${y-40} C ${CX-64} ${y-52} ${CX-84} ${y-108} ${CX-70} ${y-140} C ${CX-24} ${y-128} ${CX-4} ${y-84} ${CX} ${y-40} z"/>
    <path d="M ${CX} ${y-56} C ${CX+58} ${y-70} ${CX+76} ${y-118} ${CX+64} ${y-148} C ${CX+20} ${y-136} ${CX+2} ${y-96} ${CX} ${y-56} z"/>
    <path d="M ${CX-160} ${y+40} H ${CX+160}"/>
    <path d="M ${CX} ${y+40} q -10 34 -44 44 M ${CX} ${y+40} q 12 40 50 48 M ${CX} ${y+40} q -2 52 -14 62"/></g>
  <g ${st(.45,2.4)}><path d="M ${CX-110} ${y-150} q 6 12 0 24 M ${CX-88} ${y-176} q 6 12 0 24 M ${CX+112} ${y-166} q 6 12 0 24"/></g>
  ${gPoint(CX,y-74,5)}
  <path d="M ${CX-96} 700 q 24 -16 48 0 M ${CX} 700 q 24 -16 48 0 M ${CX+8} 686 v 14 M ${CX-56} 686 v 14" ${st(.3,2)}/>`; };
M.mountains = r=>{ const y=290;
  return `<g ${st(.58,2.8)}>
    <path d="M ${CX-250} ${y} L ${CX-150} ${y-120} L ${CX-70} ${y-30} L ${CX+10} ${y-160} L ${CX+110} ${y-40} L ${CX+180} ${y-100} L ${CX+250} ${y}"/>
    <path d="M ${CX-250} ${y+34} L ${CX-120} ${y-30} L ${CX-10} ${y+20} L ${CX+120} ${y-40} L ${CX+250} ${y+34}" stroke-width="2.2" stroke="rgba(255,255,255,.36)"/>
    <path d="M ${CX+10} ${y-160} l -16 24 h 32 z" ${fillW(.5)}/>
    <path d="M ${CX+10} ${y-160} v -30 l 26 8 -26 8"/></g>
  <circle cx="${CX-160}" cy="${y-200}" r="26" ${st(.5,2.6)}/>
  ${[0,1,2,3].map(i=>`<circle cx="${CX-40+i*34}" cy="${y+ (i%2?4:-6)}" r="3" ${fillW(.6)}/>`).join('')}
  ${gPoint(CX+10,y-190,6)}
  <path d="M ${CX-110} 704 l 36 -22 34 22 36 -22 34 22" ${st(.3,2.2)}/>`; };
M.path = r=>{ const y=300;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-40} ${y+60} C ${CX-140} ${y+10} ${CX+90} ${y-30} ${CX-20} ${y-80} C ${CX-100} ${y-120} ${CX+40} ${y-150} ${CX+10} ${y-186}" stroke-dasharray="16 13"/>
    <path d="M ${CX-250} ${y-40} q 80 -20 150 -8 M ${CX+120} ${y-90} q 70 -14 130 -2" stroke-width="2" stroke="rgba(255,255,255,.3)"/></g>
  <g ${st(.55,2.8)}>
    <path d="M ${CX-120} ${y+18} v -44 M ${CX-120} ${y-26} h 30 v 16 h -30"/>
    <path d="M ${CX+96} ${y-36} v -40"/><circle cx="${CX+96}" cy="${y-88}" r="12"/></g>
  <g ${st(.5,2.6)}><path d="M ${CX+176} ${y-160} v 26 M ${CX+164} ${y-150} h 24"/><circle cx="${CX-190}" cy="${y-120}" r="10"/></g>
  ${gPoint(CX+10,y-186,6)}
  <path d="M ${CX-100} 702 C ${CX-40} 686 ${CX+40} 718 ${CX+100} 702" ${st(.3,2.2)} stroke-dasharray="10 9"/>`; };
M.book = r=>{ const y=210;
  return `<g ${st(.62,3)}>
    <path d="M ${CX-140} ${y} C ${CX-90} ${y-46} ${CX-30} ${y-40} ${CX} ${y-16} C ${CX+30} ${y-40} ${CX+90} ${y-46} ${CX+140} ${y} V ${y+96} C ${CX+90} ${y+54} ${CX+30} ${y+58} ${CX} ${y+82} C ${CX-30} ${y+58} ${CX-90} ${y+54} ${CX-140} ${y+96} z"/>
    <path d="M ${CX} ${y-16} V ${y+82}"/>
    <path d="M ${CX-112} ${y+8} c 40 -26 76 -24 96 -8 M ${CX-112} ${y+34} c 40 -26 76 -24 96 -8 M ${CX+16} ${y} c 40 -26 76 -24 96 8 M ${CX+16} ${y+26} c 40 -26 76 -24 96 8" stroke-width="2.2" stroke="rgba(255,255,255,.42)"/>
    <path d="M ${CX+52} ${y+70} l 10 34 10 -14 16 6 -12 -34"/></g>
  <g ${st(.45,2.4)}><path d="M ${CX-40} ${y-70} v -20 M ${CX-50} ${y-80} h 20"/><path d="M ${CX+64} ${y-88} v -16 M ${CX+56} ${y-80} h 16"/></g>
  ${gPoint(CX,y-46,5)}
  <path d="M ${CX-90} 700 h 180 M ${CX-64} 715 h 128" ${st(.3,2)}/>`; };
M.prayer = r=>{ const y=200;
  return `<g ${st(.62,3)}>
    <path d="M ${CX} ${y-70} C ${CX-26} ${y-30} ${CX-34} ${y+30} ${CX-30} ${y+96} L ${CX-6} ${y+120} L ${CX} ${y+96} L ${CX+6} ${y+120} L ${CX+30} ${y+96} C ${CX+34} ${y+30} ${CX+26} ${y-30} ${CX} ${y-70} z"/>
    <path d="M ${CX-30} ${y+30} q 30 16 60 0"/></g>
  <g ${st(.42,2.4)}><path d="M ${CX-70} ${y-40} q -16 -34 -6 -70"/><path d="M ${CX+70} ${y-40} q 16 -34 6 -70"/><path d="M ${CX} ${y-96} q -6 -28 4 -48"/></g>
  <g ${st(.5,2.6)}><path d="M ${CX-140} ${y+80} v 44 M ${CX-152} ${y+82} h 24"/><path d="M ${CX-140} ${y+66} C ${CX-146} ${y+56} ${CX-134} ${y+52} ${CX-140} ${y+44}"/></g>
  ${gPoint(CX,y-84,5)}
  <path d="M ${CX-84} 704 q 42 -24 84 0 M ${CX-40} 688 q 20 -12 40 0 v 0" ${st(.3,2)}/>`; };
M.gift = r=>{ const y=200;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-160} ${y+96} q 60 -34 130 -8 q 80 30 190 -6" />
    <path d="M ${CX-160} ${y+96} q -20 8 -26 26"/>
    <rect x="${CX-56}" y="${y-30}" width="112" height="86" rx="8"/>
    <path d="M ${CX-56} ${y+2} h 112 M ${CX} ${y-30} v 86"/>
    <path d="M ${CX} ${y-30} c -14 -30 -52 -34 -56 -10 c -2 16 30 16 56 10 z M ${CX} ${y-30} c 14 -30 52 -34 56 -10 c 2 16 -30 16 -56 10 z"/></g>
  <g ${st(.5,2.6)}><circle cx="${CX-116}" cy="${y-56}" r="12"/><circle cx="${CX+116}" cy="${y-70}" r="9"/><circle cx="${CX+70}" cy="${y-110}" r="6"/></g>
  <g ${st(.4,2.2)}><path d="M ${CX-160} ${y-110} l 0 -18 M ${CX-169} ${y-119} l 18 0"/></g>
  ${gPoint(CX,y-40,5)}
  <path d="M ${CX-96} 700 q 48 -20 96 0 q 48 20 96 0" ${st(.3,2.2)} transform="translate(-48 0)"/>`; };
M.coins = r=>{ const y=210; const x=CX;
  return `<g ${st(.58,2.8)}>
    ${[0,1,2,3,4].map(i=>`<ellipse cx="${x-70}" cy="${y+70-i*24}" rx="56" ry="15"/>`).join('')}
    ${[0,1,2].map(i=>`<ellipse cx="${x+78}" cy="${y+76-i*24}" rx="48" ry="13"/>`).join('')}
    <circle cx="${x+70}" cy="${y-72}" r="30"/><path d="M ${x+70} ${y-88} v 32 M ${x+62} ${y-80} c 0 -8 16 -8 16 0 c 0 8 -16 8 -16 0 c 0 8 16 8 16 0"/>
    <path d="M ${x-150} ${y+96} q 150 44 300 0"/></g>
  <g ${st(.42,2.2)}><path d="M ${x-140} ${y-70} l 0 -18 M ${x-149} ${y-79} l 18 0"/><path d="M ${x-20} ${y-110} l 0 -14 M ${x-27} ${y-103} l 14 0"/></g>
  ${gPoint(x+70,y-72,5)}
  <path d="M ${x-90} 704 h 180 M ${x-60} 688 h 120" ${st(.28,2)}/>`; };
M.tree = r=>{ const y=280;
  return `<g ${st(.6,2.8)}>
    <path d="M ${CX} ${y+60} V ${y-30} M ${CX} ${y-4} q -40 -12 -58 -44 M ${CX} ${y-14} q 42 -10 60 -48"/>
    <path d="M ${CX-104} ${y-58} C ${CX-140} ${y-120} ${CX-70} ${y-186} ${CX} ${y-160} C ${CX+70} ${y-186} ${CX+140} ${y-120} ${CX+104} ${y-58} C ${CX+70} ${y-30} ${CX-70} ${y-30} ${CX-104} ${y-58} z"/>
    <path d="M ${CX} ${y+60} q -26 22 -60 24 M ${CX} ${y+60} q 26 22 60 24 M ${CX-160} ${y+60} H ${CX+160}"/></g>
  <g ${st(.5,2.4)}>
    <path d="M ${CX-190} ${y+30} v 30 M ${CX-190} ${y+30} q -20 -26 0 -40 q 20 14 0 40"/>
    <path d="M ${CX+190} ${y+30} v 30 M ${CX+190} ${y+30} q -20 -26 0 -40 q 20 14 0 40"/></g>
  ${[[-60,-120],[0,-150],[58,-118],[-24,-92],[34,-88]].map(p=>`<circle cx="${CX+p[0]}" cy="${y+p[1]}" r="3.2" ${fillW(.55)}/>`).join('')}
  ${gPoint(CX,y-160,5)}
  <path d="M ${CX-96} 704 q 48 -18 96 0 M ${CX-40} 690 v 14 M ${CX+22} 692 v 12" ${st(.3,2)}/>`; };
M.arrowlaunch = r=>{ const y=230;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-120} ${y+90} C ${CX-40} ${y+60} ${CX+10} ${y-10} ${CX+60} ${y-90}" stroke-dasharray="3 12"/>
    <path d="M ${CX+60} ${y-90} l 34 -56 M ${CX+94} ${y-146} l -30 6 M ${CX+94} ${y-146} l -4 30"/>
    <path d="M ${CX-160} ${y+40} A 130 130 0 0 1 ${CX-30} ${y-90}"/>
    <path d="M ${CX-160} ${y+40} l -22 -18 M ${CX-160} ${y+40} l 26 12 M ${CX-30} ${y-90} l -18 -22 M ${CX-30} ${y-90} l 12 26"/></g>
  <g ${st(.45,2.4)}><circle cx="${CX+130}" cy="${y-40}" r="26"/><circle cx="${CX+130}" cy="${y-40}" r="12"/></g>
  ${gPoint(CX+94,y-146,6)}
  <path d="M ${CX-100} 700 l 40 0 l 14 -18 l 14 18 l 40 0 M ${CX-10} 682 v -12" ${st(.3,2.2)}/>`; };
M.home = r=>{ const y=190;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-110} ${y+30} L ${CX} ${y-70} L ${CX+110} ${y+30}"/>
    <path d="M ${CX-88} ${y+22} V ${y+130} H ${CX+88} V ${y+22}"/>
    <rect x="${CX-20}" y="${y+66}" width="40" height="64" rx="3"/>
    <rect x="${CX-66}" y="${y+52}" width="30" height="30" rx="3"/><path d="M ${CX-51} ${y+52} v 30 M ${CX-66} ${y+67} h 30"/>
    <path d="M ${CX+40} ${y-38} v -34 h 22 v 14"/>
    <path d="M ${CX+62} ${y-92} q 12 -12 4 -26 M ${CX+74} ${y-84} q 12 -12 4 -26"/></g>
  <path d="M ${CX+48} ${y+70} c -8 -12 -26 -6 -22 8 c 3 9 14 12 22 20 c 8 -8 19 -11 22 -20 c 4 -14 -14 -20 -22 -8 z" ${st(.55,2.6)}/>
  <g ${st(.45,2.4)}><path d="M ${CX-160} ${y+130} h -40 M ${CX-172} ${y+112} v 18 M ${CX-188} ${y+118} v 12 M ${CX+160} ${y+130} h 40 M ${CX+172} ${y+112} v 18 M ${CX+188} ${y+118} v 12"/></g>
  ${gPoint(CX,y-70,5)}
  <path d="M ${CX-100} 704 h 200 M ${CX-64} 690 h 128" ${st(.28,2)}/>`; };
M.rings = r=>{ const y=190;
  return `<g ${st(.62,3.2)}>
    <circle cx="${CX-34}" cy="${y}" r="58"/><circle cx="${CX+34}" cy="${y}" r="58"/>
    <path d="M ${CX-34} ${y-58} l -12 -22 h 24 z M ${CX+34} ${y-58} l -12 -22 h 24 z" stroke-width="2.6"/></g>
  <g ${st(.4,2.2)}><path d="M ${CX-130} ${y-70} l 0 -18 M ${CX-139} ${y-79} l 18 0"/><path d="M ${CX+128} ${y-88} l 0 -14 M ${CX+121} ${y-81} l 14 0"/></g>
  <path d="M ${CX-96} ${y+96} q 96 44 192 0" ${st(.42,2.4)}/>
  ${gPoint(CX,y,5)}
  <path d="M ${CX-84} 700 q 42 -18 84 0 q 42 18 84 0" ${st(.3,2.2)} transform="translate(-42 0)"/>`; };
M.kite = r=>{ const y=180;
  return `<g ${st(.6,3)}>
    <path d="M ${CX} ${y-90} L ${CX+64} ${y} L ${CX} ${y+90} L ${CX-64} ${y} z M ${CX} ${y-90} V ${y+90} M ${CX-64} ${y} H ${CX+64}"/>
    <path d="M ${CX} ${y+90} C ${CX-30} ${y+140} ${CX+30} ${y+170} ${CX-10} ${y+220}"/>
    <path d="M ${CX-16} ${y+130} l 12 -10 12 10 -12 10 z M ${CX+6} ${y+172} l 11 -9 11 9 -11 9 z" stroke-width="2.4"/></g>
  <g ${st(.45,2.4)}><path d="M ${CX-140} ${y-40} q 12 -14 26 0 q 12 -14 26 0"/><path d="M ${CX+90} ${y-90} q 11 -13 24 0 q 11 -13 24 0"/></g>
  ${gPoint(CX,y-90,5)}
  <path d="M ${CX-90} 700 q 30 -14 60 0 q 30 14 60 0" ${st(.3,2.2)} transform="translate(-15 0)"/>`; };
M.crown = r=>{ const y=190;
  return `<g ${st(.62,3)}>
    <path d="M ${CX-110} ${y+40} L ${CX-124} ${y-60} L ${CX-58} ${y-6} L ${CX} ${y-84} L ${CX+58} ${y-6} L ${CX+124} ${y-60} L ${CX+110} ${y+40} z"/>
    <path d="M ${CX-110} ${y+58} h 220 M ${CX-104} ${y+76} h 208"/>
    <circle cx="${CX-124}" cy="${y-70}" r="9"/><circle cx="${CX}" cy="${y-96}" r="10"/><circle cx="${CX+124}" cy="${y-70}" r="9"/></g>
  ${[[-64,26],[0,20],[64,26]].map(p=>`<circle cx="${CX+p[0]}" cy="${y+p[1]}" r="6" ${st(.5,2.4)}/>`).join('')}
  <g ${st(.4,2.2)}><path d="M ${CX-180} ${y-110} l 0 -16 M ${CX-188} ${y-118} l 16 0"/><path d="M ${CX+176} ${y-120} l 0 -14 M ${CX+169} ${y-113} l 14 0"/></g>
  ${gPoint(CX,y-96,5)}
  <path d="M ${CX-96} 704 h 192 M ${CX-64} 690 h 128" ${st(.28,2)}/>`; };
M.cross = r=>{ const y=200;
  return `<g ${st(.62,3.2)}>
    <path d="M ${CX} ${y-100} V ${y+110} M ${CX-64} ${y-30} H ${CX+64}"/>
    <path d="M ${CX-140} ${y+110} q 140 -50 280 0"/></g>
  <g ${st(.42,2.4)}>${[0.2,0.4,0.6,0.8].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+Math.cos(a)*112).toFixed(0)}" y1="${(y-30-Math.sin(a)*112).toFixed(0)}" x2="${(CX+Math.cos(a)*148).toFixed(0)}" y2="${(y-30-Math.sin(a)*148).toFixed(0)}"/>`;}).join('')}</g>
  ${gPoint(CX,y-30,6)}
  <path d="M ${CX-84} 704 q 84 -30 168 0" ${st(.3,2.2)}/>`; };
M.compass = r=>{ const y=190;
  return `<g ${st(.6,2.8)}>
    <circle cx="${CX}" cy="${y}" r="92"/><circle cx="${CX}" cy="${y}" r="72"/>
    <path d="M ${CX} ${y-92} v 16 M ${CX} ${y+76} v 16 M ${CX-92} ${y} h 16 M ${CX+76} ${y} h 16"/>
    <path d="M ${CX} ${y} L ${CX+34} ${y-46} L ${CX+8} ${y-6} z" ${fillW(.5)}/>
    <path d="M ${CX} ${y} L ${CX-34} ${y+46} L ${CX-8} ${y+6} z"/>
    ${[45,135,225,315].map(a=>{const rd=a*Math.PI/180;return `<line x1="${(CX+Math.cos(rd)*80).toFixed(0)}" y1="${(y+Math.sin(rd)*80).toFixed(0)}" x2="${(CX+Math.cos(rd)*90).toFixed(0)}" y2="${(y+Math.sin(rd)*90).toFixed(0)}"/>`;}).join('')}</g>
  <g ${st(.4,2.2)}><path d="M ${CX-170} ${y-90} l 0 -16 M ${CX-178} ${y-98} l 16 0"/></g>
  ${gPoint(CX,y,5)}
  <path d="M ${CX-110} 700 h 44 M ${CX-52} 700 h 24 M ${CX-14} 700 h 124" ${st(.3,2.2)}/>`; };
M.lamp = r=>{ const y=200;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-70} ${y+20} q -18 -44 24 -58 q 6 -22 46 -22 q 40 0 46 22 q 42 14 24 58 q -70 24 -140 0 z"/>
    <path d="M ${CX+66} ${y-2} q 40 -6 52 -30 M ${CX+118} ${y-32} l -14 -2 M ${CX+118} ${y-32} l -2 14"/>
    <path d="M ${CX-46} ${y+40} q 46 18 92 0 M ${CX-24} ${y+58} h 48"/>
    <path d="M ${CX+112} ${y-56} C ${CX+96} ${y-76} ${CX+112} ${y-96} ${CX+118} ${y-108} C ${CX+128} ${y-92} ${CX+140} ${y-76} ${CX+124} ${y-58} z"/></g>
  <g ${st(.42,2.4)}>${[0.25,0.5,0.75].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+118+Math.cos(a)*34).toFixed(0)}" y1="${(y-90-Math.sin(a)*34).toFixed(0)}" x2="${(CX+118+Math.cos(a)*52).toFixed(0)}" y2="${(y-90-Math.sin(a)*52).toFixed(0)}"/>`;}).join('')}</g>
  <path d="M ${CX-130} ${y+66} h 260" ${st(.4,2.4)}/>
  ${gPoint(CX+118,y-84,5)}
  <path d="M ${CX-90} 704 h 180 M ${CX-58} 690 h 116" ${st(.28,2)}/>`; };
M.sundial = r=>{ const y=190;
  return `<g ${st(.6,2.8)}>
    <circle cx="${CX}" cy="${y}" r="96"/>
    ${[...Array(12)].map((_,i)=>{const a=i*Math.PI/6;return `<line x1="${(CX+Math.cos(a)*84).toFixed(0)}" y1="${(y+Math.sin(a)*84).toFixed(0)}" x2="${(CX+Math.cos(a)*96).toFixed(0)}" y2="${(y+Math.sin(a)*96).toFixed(0)}"/>`;}).join('')}
    <path d="M ${CX} ${y} L ${CX+52} ${y-64} M ${CX} ${y} L ${CX-8} ${y-70} L ${CX+52} ${y-64}"/></g>
  <g ${st(.45,2.4)}><circle cx="${CX-150}" cy="${y-110}" r="18"/><path d="M ${CX+150} ${y-116} a 16 16 0 1 0 10 28 a 13 13 0 0 1 -10 -28 z"/></g>
  ${gPoint(CX,y,5)}
  <path d="M ${CX-100} 702 h 200 M ${CX-100} 702 l 20 -14 M ${CX+100} 702 l -20 -14" ${st(.3,2.2)}/>`; };
M.well = r=>{ const y=210;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-84} ${y+20} h 168 v 26 q -84 20 -168 0 z"/>
    <path d="M ${CX-70} ${y+20} L ${CX-52} ${y-80} M ${CX+70} ${y+20} L ${CX+52} ${y-80}"/>
    <path d="M ${CX-70} ${y-80} h 140 l -18 -30 h -104 z"/>
    <path d="M ${CX} ${y-80} V ${y-16}"/>
    <path d="M ${CX-16} ${y-16} h 32 v 24 q -16 8 -32 0 z"/></g>
  <g ${st(.42,2.4)}><path d="M ${CX-140} ${y+70} q 24 -12 48 0 M ${CX+92} ${y+70} q 24 -12 48 0"/><path d="M ${CX+120} ${y-120} c -6 10 6 16 0 26 M ${CX-124} ${y-104} c -6 10 6 16 0 26"/></g>
  ${gPoint(CX,y-96,5)}
  <path d="M ${CX-120} 696 q 40 -18 80 0 q 40 18 80 0 q 40 -18 80 0" ${st(.3,2.2)} transform="translate(-40 0)"/>`; };
M.door = r=>{ const y=180;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-70} ${y+130} V ${y-40} A 70 70 0 0 1 ${CX+70} ${y-40} V ${y+130}"/>
    <path d="M ${CX-46} ${y+130} V ${y-30} A 46 46 0 0 1 ${CX+30} ${y-64} L ${CX+30} ${y+130}"/>
    <circle cx="${CX+12}" cy="${y+40}" r="5"/></g>
  <g ${st(.42,2.4)}>${[0.15,0.35,0.55].map(t=>{return `<line x1="${CX+36}" y1="${(y+10-t*90).toFixed(0)}" x2="${(CX+96+t*40).toFixed(0)}" y2="${(y+40-t*160).toFixed(0)}"/>`;}).join('')}</g>
  <path d="M ${CX-110} ${y+130} h 220 M ${CX-96} ${y+152} h 192" ${st(.5,2.6)}/>
  ${gPoint(CX+12,y+40,5)}
  <path d="M ${CX-84} 700 h 168" ${st(.3,2.2)}/>`; };
M.table = r=>{ const y=210;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-150} ${y} h 300 M ${CX-130} ${y} V ${y+110} M ${CX+130} ${y} V ${y+110}"/>
    <path d="M ${CX-64} ${y-24} a 24 24 0 0 1 48 0 z M ${CX-40} ${y-24} v 24"/>
    <path d="M ${CX+28} ${y-16} q 30 -22 60 0 q -30 14 -60 0 z"/>
    <path d="M ${CX-6} ${y-58} v -26 M ${CX-6} ${y-58} c -10 0 -10 14 0 14 c 10 0 10 -14 0 -14"/></g>
  <g ${st(.42,2.4)}><path d="M ${CX-6} ${y-96} q -5 -10 0 -18"/></g>
  ${gPoint(CX-6,y-70,4.5)}
  <path d="M ${CX-96} 700 h 192 M ${CX-72} 686 h 144" ${st(.28,2)}/>`; };
M.flame = r=>{ const y=200;
  return `<g ${st(.62,3.2)}>
    <path d="M ${CX} ${y+90} C ${CX-70} ${y+50} ${CX-56} ${y-40} ${CX-8} ${y-96} C ${CX-20} ${y-40} ${CX+18} ${y-46} ${CX+16} ${y-90} C ${CX+62} ${y-30} ${CX+64} ${y+54} ${CX} ${y+90} z"/>
    <path d="M ${CX} ${y+64} C ${CX-28} ${y+40} ${CX-20} ${y-4} ${CX+2} ${y-30} C ${CX-2} ${y} ${CX+22} ${y+2} ${CX+26} ${y+28} C ${CX+22} ${y+52} ${CX+8} ${y+62} ${CX} ${y+64} z"/></g>
  <g ${st(.4,2.4)}><path d="M ${CX-80} ${y+10} q -20 -30 -12 -66"/><path d="M ${CX+84} ${y+4} q 20 -30 12 -66"/></g>
  <circle cx="${CX-52}" cy="${y-96}" r="3.4" ${fillW(.6)}/><circle cx="${CX+58}" cy="${y-108}" r="2.8" ${fillW(.5)}/>
  ${gPoint(CX+4,y+16,6)}
  <path d="M ${CX-84} 704 q 42 -16 84 0 q 42 16 84 0" ${st(.3,2.2)} transform="translate(-42 0)"/>`; };
M.stars = r=>{ const y=170; const pts=[[-150,-40],[-70,-90],[10,-30],[90,-100],[170,-40],[40,40]];
  return `<g ${st(.5,2.2)}><path d="M ${pts.map(p=>(CX+p[0])+' '+(y+p[1])).join(' L ')}"/></g>
  ${pts.map(p=>`<circle cx="${CX+p[0]}" cy="${y+p[1]}" r="4" ${fillW(.7)}/>`).join('')}
  <path d="M ${CX-40} ${y+90} l 9 18 20 3 -14 14 3 20 -18 -9 -18 9 3 -20 -14 -14 20 -3 z" ${st(.6,2.8)}/>
  <path d="M ${CX+150} ${y+60} a 30 30 0 1 0 20 52 a 24 24 0 0 1 -20 -52 z" ${st(.5,2.6)}/>
  ${gPoint(CX+90,y-100,6)}
  <path d="M ${CX-90} 700 h 180" ${st(.28,2)}/><circle cx="${CX-60}" cy="686" r="2.4" ${fillW(.5)}/><circle cx="${CX+44}" cy="682" r="2" ${fillW(.4)}/>`; };
M.shepherd = r=>{ const y=250;
  return `<g ${st(.6,3)}>
    <path d="M ${CX+90} ${y+70} V ${y-110} a 26 26 0 1 0 -40 20"/>
    <path d="M ${CX-250} ${y+40} q 120 -44 250 -10 q 130 34 250 6" stroke-width="2.2" stroke="rgba(255,255,255,.32)"/></g>
  ${[[-140,30],[-60,52],[10,26]].map((p,i)=>`<g ${st(.55,2.6)}>
    <path d="M ${CX+p[0]-30} ${y+p[1]} a 16 16 0 0 1 8 -22 a 18 18 0 0 1 24 -8 a 16 16 0 0 1 26 6 a 14 14 0 0 1 2 24 q -30 10 -60 0 z"/>
    <circle cx="${CX+p[0]+30}" cy="${y+p[1]-24}" r="9"/>
    <path d="M ${CX+p[0]-18} ${y+p[1]+2} v 16 M ${CX+p[0]+8} ${y+p[1]+2} v 16"/></g>`).join('')}
  ${gPoint(CX+90,y-116,5)}
  <path d="M ${CX-100} 704 q 50 -18 100 0 q 50 18 100 0" ${st(.3,2.2)} transform="translate(-50 0)"/>`; };
M.blueprint = r=>{ const y=200;
  return `<g ${st(.55,2.6)}>
    <path d="M ${CX-110} ${y+110} V ${y+10} L ${CX} ${y-70} L ${CX+110} ${y+10} V ${y+110}" stroke-dasharray="9 8"/>
    <path d="M ${CX-110} ${y+110} h 220"/>
    <rect x="${CX-88}" y="${y+58}" width="52" height="52" rx="3"/>
    <path d="M ${CX-88} ${y+58} l 52 52 M ${CX-36} ${y+58} l -52 52" stroke-width="2"/>
    <path d="M ${CX+30} ${y+66} h 52 v 44 h -52 z M ${CX+56} ${y+66} v 44"/></g>
  <g ${st(.5,2.6)}><path d="M ${CX-170} ${y-40} h 60 M ${CX-170} ${y-52} v 24 M ${CX-110} ${y-52} v 24"/><circle cx="${CX-140}" cy="${y-40}" r="5"/></g>
  ${gPoint(CX-62,y+84,6)}
  <path d="M ${CX-100} 700 h 200 M ${CX-100} 690 v 10 M ${CX+100} 690 v 10 M ${CX-50} 694 v 6 M ${CX} 694 v 6 M ${CX+50} 694 v 6" ${st(.3,2)}/>`; };
M.restnight = r=>{ const y=180;
  return `<g ${st(.6,3)}>
    <path d="M ${CX-20} ${y-70} a 62 62 0 1 0 44 106 a 52 52 0 0 1 -44 -106 z"/>
    <path d="M ${CX-140} ${y+90} q 140 -34 280 0 M ${CX-110} ${y+118} q 110 -26 220 0"/></g>
  <path d="M ${CX+90} ${y-60} l 6 12 13 2 -9 9 2 13 -12 -6 -12 6 2 -13 -9 -9 13 -2 z" ${fillW(.6)}/>
  <circle cx="${CX-130}" cy="${y-90}" r="2.6" ${fillW(.5)}/><circle cx="${CX+150}" cy="${y+6}" r="2.2" ${fillW(.45)}/>
  ${gPoint(CX-20,y-70,4.5)}
  <path d="M ${CX-84} 700 h 168 M ${CX-56} 714 h 112" ${st(.28,2)}/>`; };
M.shield = r=>{ const y=190;
  return `<g ${st(.6,3)}>
    <path d="M ${CX} ${y-90} C ${CX+50} ${y-70} ${CX+90} ${y-72} ${CX+96} ${y-58} C ${CX+96} ${y+30} ${CX+64} ${y+96} ${CX} ${y+126} C ${CX-64} ${y+96} ${CX-96} ${y+30} ${CX-96} ${y-58} C ${CX-90} ${y-72} ${CX-50} ${y-70} ${CX} ${y-90} z"/>
    <path d="M ${CX} ${y-56} V ${y+92} M ${CX-64} ${y+8} H ${CX+64}"/></g>
  <g ${st(.4,2.2)}><path d="M ${CX-150} ${y-96} l 0 -16 M ${CX-158} ${y-104} l 16 0"/><path d="M ${CX+148} ${y-104} l 0 -14 M ${CX+141} ${y-97} l 14 0"/></g>
  ${gPoint(CX,y+8,6)}
  <path d="M ${CX-96} 702 h 66 M ${CX-14} 702 h 110 M ${CX-24} 702 l 10 -8 M ${CX-24} 702 l 10 8" ${st(.3,2.2)}/>`; };
M.bird = r=>{ const y=180;
  return `<g ${st(.62,3)}>
    <path d="M ${CX-30} ${y} C ${CX-90} ${y-60} ${CX-150} ${y-56} ${CX-180} ${y-30} C ${CX-130} ${y-26} ${CX-92} ${y-10} ${CX-56} ${y+10}"/>
    <path d="M ${CX-30} ${y} C ${CX+16} ${y-70} ${CX+90} ${y-80} ${CX+140} ${y-60} C ${CX+96} ${y-40} ${CX+50} ${y-16} ${CX+8} ${y+12}"/>
    <path d="M ${CX-56} ${y+10} q 30 26 64 2"/>
    <path d="M ${CX+8} ${y+12} l 40 34 M ${CX+30} ${y+30} l 26 6"/></g>
  <g ${st(.4,2.4)}><path d="M ${CX-160} ${y+60} q 40 -12 80 0 M ${CX+60} ${y+80} q 40 -12 80 0"/></g>
  <path d="M ${CX+120} ${y+120} C ${CX+108} ${y+96} ${CX+130} ${y+80} ${CX+150} ${y+76} C ${CX+146} ${y+98} ${CX+138} ${y+114} ${CX+120} ${y+120} z M ${CX+124} ${y+116} L ${CX+146} ${y+82}" ${st(.5,2.4)}/>
  ${gPoint(CX-30,y,5)}
  <path d="M ${CX-84} 700 q 42 -14 84 0 q 42 14 84 0" ${st(.28,2)} transform="translate(-42 0)"/>`; };
M.chainbreak = r=>{ const y=190;
  return `<g ${st(.6,3)}>
    <rect x="${CX-150}" y="${y-20}" width="56" height="34" rx="17"/>
    <rect x="${CX-104}" y="${y-2}" width="56" height="34" rx="17"/>
    <rect x="${CX+48}" y="${y-2}" width="56" height="34" rx="17"/>
    <rect x="${CX+94}" y="${y-20}" width="56" height="34" rx="17"/>
    <path d="M ${CX-30} ${y-6} l 18 -14 M ${CX-24} ${y+16} l 20 -4 M ${CX+30} ${y-10} l -16 -12 M ${CX+26} ${y+16} l -18 -2" stroke-width="2.6"/></g>
  <g ${st(.42,2.4)}>${[0.25,0.5,0.75].map(t=>{const a=Math.PI*t;return `<line x1="${(CX+Math.cos(a)*70).toFixed(0)}" y1="${(y-40-Math.sin(a)*70).toFixed(0)}" x2="${(CX+Math.cos(a)*104).toFixed(0)}" y2="${(y-40-Math.sin(a)*104).toFixed(0)}"/>`;}).join('')}</g>
  ${gPoint(CX,y-40,6)}
  <path d="M ${CX-90} 702 h 180" ${st(.28,2)}/>`; };
M.globe = r=>{ const y=190; const R=96;
  return `<g ${st(.58,2.8)}>
    <circle cx="${CX}" cy="${y}" r="${R}"/>
    <ellipse cx="${CX}" cy="${y}" rx="${R/3}" ry="${R}"/><ellipse cx="${CX}" cy="${y}" rx="${R*2/3}" ry="${R}"/>
    <ellipse cx="${CX}" cy="${y}" rx="${R}" ry="${R/3}"/><path d="M ${CX-R} ${y-R*0.62} q ${R} 40 ${2*R} 0 M ${CX-R} ${y+R*0.62} q ${R} -40 ${2*R} 0"/></g>
  ${[[-130,-130],[150,-100],[120,120],[-160,90]].map(p=>`<path d="M ${CX+p[0]-7} ${y+p[1]} h 14 M ${CX+p[0]} ${y+p[1]-7} v 14" ${st(.5,2.4)}/>`).join('')}
  ${gPoint(CX+R*0.5,y-R*0.55,6)}
  <path d="M ${CX-100} 702 q 100 -26 200 0" ${st(.3,2.2)}/>`; };
M.wheat = r=>{ const y=230;
  const stalk=(x,tilt)=>{ let s=`<path d="M ${x} ${y+90} C ${x+tilt*8} ${y+30} ${x+tilt*14} ${y-30} ${x+tilt*18} ${y-80}" ${st(.58,2.8)}/>`;
    for(let i=0;i<6;i++){ const t=i/6, px=x+tilt*(8+t*10), py=y+60-t*130;
      s+=`<path d="M ${px} ${py} q ${-14-tilt*4} -12 ${-10-tilt*4} -30 q 14 8 ${10+tilt*4} 30 z M ${px} ${py} q ${14-tilt*4} -12 ${10-tilt*4} -30 q -14 8 ${-10+tilt*4} 30 z" ${st(.5,2.2)}/>`; }
    return s; };
  return stalk(CX-60,-1)+stalk(CX,0)+stalk(CX+60,1)+
  `<path d="M ${CX-110} ${y+90} q 110 30 220 0" ${st(.5,2.6)}/>
  ${gPoint(CX+18,y-80,5)}
  <path d="M ${CX-96} 704 q 24 -14 48 0 M ${CX-24} 704 q 24 -14 48 0 M ${CX+48} 704 q 24 -14 48 0" ${st(.3,2)}/>`; };

/* keyword rules — first match wins */
const RULES = [
  [/torch|passing the torch|baton|relay/, 'torch'],
  [/\bown|ownership|deed|belongs/, 'keys'],
  [/heart\b|love\b|beloved/, 'heart'],
  [/enough|content|simplic|simple\b|less\b|minimal/, 'scales'],
  [/anchor|steadfast|unshak|immovable/, 'anchor'],
  [/storm|anxi|fear\b|afraid|worry|overwhelm|troubled/, 'lighthouse'],
  [/dawn|morning|sunrise|new day|awaken|arise|light\b|hope\b/, 'sunrise'],
  [/harvest|wheat|sow\b|reap/, 'wheat'],
  [/seed|grow|root|plant|soil|fruit|vine|flourish|bloom/, 'sprout'],
  [/mountain|climb|summit|higher|peak/, 'mountains'],
  [/journey|path|walk\b|road|steps|pilgrim|wander/, 'path'],
  [/\bword\b|scripture|bible|book|read|study|devot/, 'book'],
  [/pray|prayer|interced/, 'prayer'],
  [/generos|give\b|giving|gift|offering|tithe|open.?hand/, 'gift'],
  [/money|steward|wealth|rich|treasure|invest|budget|financ|provision|debt|save|fund/, 'coins'],
  [/legacy|inherit|generation|grandparent|grand\b|estate|heirloom/, 'tree'],
  [/heir|launch|arrow|ready\b|prepare|sending|commission/, 'arrowlaunch'],
  [/family|home\b|house\b|parent|household|roof/, 'home'],
  [/marriage|marri|couple|wedding|spouse|two become/, 'rings'],
  [/child|kids|children|youth|young/, 'kite'],
  [/king\b|kingdom|crown|reign|throne|majesty/, 'crown'],
  [/cross|gospel|redeem|salvation|calvary|savior/, 'cross'],
  [/work\b|business|vocation|market|labor|career|calling|succession|office/, 'compass'],
  [/wisdom|wise|discern|decision|understand/, 'lamp'],
  [/season|time\b|clock|number our|years|sabbatical|chapter/, 'sundial'],
  [/water|well\b|river|thirst|rain|spring\b/, 'well'],
  [/door|open\b|invite|welcome|threshold/, 'door'],
  [/table|meal|bread|feast|supper|hospitality|dinner/, 'table'],
  [/fire|flame|spirit\b|revival|burn/, 'flame'],
  [/star|night\b|dark|midnight/, 'stars'],
  [/shepherd|sheep|flock|pasture/, 'shepherd'],
  [/build|foundation|cornerstone|construct|blueprint/, 'blueprint'],
  [/rest\b|sabbath|still\b|quiet|slow\b|pause|peace\b/, 'restnight'],
  [/battle|fight|armor|stand firm|warfare|struggle/, 'shield'],
  [/free|freedom|soar|wings|fly\b|release/, 'bird'],
  [/forgiv|reconcil|mercy/, 'chainbreak'],
  [/mission|nations|world|global|neighbor|witness|reach|multiply|send/, 'globe'],
  [/grace/, 'cross'],
  [/faith|trust|believ/, 'anchor'],
  [/identity|purpose|who (i|you) (am|are)/, 'compass'],
];
const CAT_FALLBACK = {1:'coins',2:'scales',3:'gift',4:'globe',5:'tree',6:'arrowlaunch',7:'home',8:'compass',9:'lamp',10:'book',11:'sundial',12:'sunrise',13:'well',14:'path',15:'sprout'};

function pickMotif(row){
  const hay=(row[0]+' '+(row[10]||'')+' '+(row[1]||'')).toLowerCase();
  for(const [re,name] of RULES) if(re.test(hay)) return name;
  return CAT_FALLBACK[row[2]]||'path';
}

/* =================== TYPOGRAPHY (crop-safe, centered, balanced) =================== */
function balancedWrap(t, per){
  const words=t.split(' ');
  if(t.length<=per) return [t];
  const target=Math.min(4, Math.ceil(t.length/per));
  // distribute words into `target` lines with near-equal length
  const lines=[]; let li=0, remaining=words.slice();
  for(let i=0;i<target;i++){
    const slots=target-i;
    const budget=Math.ceil(remaining.join(' ').length/slots);
    let cur='';
    while(remaining.length && (cur.length===0 || (cur+' '+remaining[0]).length<=Math.max(budget, per*0.72))){
      if((cur+' '+remaining[0]).trim().length>per && cur) break;
      cur=(cur+' '+remaining.shift()).trim();
    }
    lines.push(cur);
    if(!remaining.length) break;
  }
  if(remaining.length) lines[lines.length-1]+=' '+remaining.join(' ');
  return lines.filter(Boolean);
}
function titleBlock(title, sub){
  const len=title.length;
  const fs = len<=14?58 : len<=22?50 : len<=30?44 : len<=42?38 : 33;
  const per=Math.floor((W*0.76)/(fs*0.52));
  let lines=balancedWrap(title, per);
  if(lines.length>4){ lines=lines.slice(0,4); lines[3]=lines[3].replace(/\s?\S*$/,'')+'…'; }
  // shrink if any line still overflows
  let maxLine=Math.max(...lines.map(l=>l.length));
  let fs2=fs;
  if(maxLine*0.52*fs > W*0.8) fs2=Math.floor((W*0.8)/(maxLine*0.52));
  const lh=fs2*1.12;
  const subLines = (sub && sub.length<=84) ? balancedWrap(sub, Math.floor((W*0.72)/(19*0.5))).slice(0,2) : [];
  return {fs:fs2, lines, lh, subLines};
}

/* =================== COVER =================== */
function cover(row){
  const id=row[9], title=row[0], sub=row[1]||'', cat=row[2], lenTxt=row[3];
  const [A,B]=HUE[cat]||HUE[5];
  const r=rng(seedOf(id));
  const angles=[[0,0,0,1],[0,0,1,1],[1,0,0,1],[0,0.2,1,0.8],[0.2,0,0.8,1]];
  const g=angles[Math.floor(r()*angles.length)];
  const pat=PATTERNS[(cat + Math.floor(r()*3)) % PATTERNS.length](r);
  const motifName=pickMotif(row);
  const motif=M[motifName](r);
  const {fs,lines,lh,subLines}=titleBlock(title, sub);
  // vertical centering of the whole stack inside safe zone (y 335–565 center 450)
  const blockH = 26 + 26 + lines.length*lh + (subLines.length? 18+subLines.length*24 : 0);
  let y = 450 - blockH/2 + 20;
  const catLabel=esc((CATS[cat]||'').split('&')[0].trim().toUpperCase());
  let text='';
  text+=`<text x="${CX}" y="${y}" text-anchor="middle" font-family="Verdana, Arial, sans-serif" font-size="13.5" letter-spacing="4.5" ${fillW(.85)} font-weight="bold">${catLabel}</text>`;
  y+=26;
  text+=`<g ${st(.55,1.8)}><line x1="${CX-70}" y1="${y}" x2="${CX-16}" y2="${y}"/><line x1="${CX+16}" y1="${y}" x2="${CX+70}" y2="${y}"/></g><path d="M ${CX} ${y-6} l 6 6 -6 6 -6 -6 z" fill="${GOLD}"/>`;
  y+=26+fs*0.82;
  for(const L of lines){ text+=`<text x="${CX}" y="${y.toFixed(0)}" text-anchor="middle" font-size="${fs}" fill="#FFFFFF" font-weight="600">${esc(L)}</text>`; y+=lh; }
  if(subLines.length){
    y+=6;
    text+=`<g ${st(.4,1.6)}><line x1="${CX-46}" y1="${(y-16).toFixed(0)}" x2="${CX+46}" y2="${(y-16).toFixed(0)}"/></g>`;
    for(const L of subLines){ text+=`<text x="${CX}" y="${y.toFixed(0)}" text-anchor="middle" font-size="18.5" font-style="italic" ${fillW(.88)}>${esc(L)}</text>`; y+=24; }
  }
  const num=parseInt(lenTxt)||40;
  const turbSeed=Math.floor(r()*1000), bf=(0.5+r()*0.5).toFixed(2);
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" font-family="Georgia, 'Times New Roman', serif">
<defs>
  <linearGradient id="bg" x1="${g[0]}" y1="${g[1]}" x2="${g[2]}" y2="${g[3]}"><stop offset="0" stop-color="${A}"/><stop offset="1" stop-color="${B}"/></linearGradient>
  <radialGradient id="vin" cx="0.5" cy="0.46" r="0.85"><stop offset="0.55" stop-color="rgba(0,0,0,0)"/><stop offset="1" stop-color="rgba(0,0,0,.30)"/></radialGradient>
  <radialGradient id="tglow" cx="0.5" cy="0.56" r="0.5"><stop offset="0" stop-color="rgba(0,0,0,.30)"/><stop offset="1" stop-color="rgba(0,0,0,0)"/></radialGradient>
  <filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="${bf}" numOctaves="2" seed="${turbSeed}" stitchTiles="stitch"/><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .045 0"/></filter>
</defs>
<rect width="${W}" height="${H}" fill="url(#bg)"/>
${pat}
${motif}
<rect width="${W}" height="${H}" fill="url(#vin)"/>
<ellipse cx="${CX}" cy="452" rx="270" ry="150" fill="url(#tglow)"/>
<rect width="${W}" height="${H}" filter="url(#gr)"/>
<rect x="17" y="17" width="${W-34}" height="${H-34}" rx="10" ${st(.3,2)}/>
<circle cx="${CX}" cy="76" r="27" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="2.2"/>
<text x="${CX}" y="84" text-anchor="middle" font-size="21" fill="#FFFFFF">${num}</text>
${text}
</svg>`;
}

/* =================== RUN =================== */
const outDir='/home/claude/site/covers';
fs.rmSync(outDir,{recursive:true,force:true});
fs.mkdirSync(outDir,{recursive:true});
const crypto=require('crypto');
const hashes=new Set(); let n=0, bytes=0; const motifCount={};
for(const row of ROWS){
  const svg=cover(row);
  fs.writeFileSync(outDir+'/'+row[9]+'.svg', svg);
  hashes.add(crypto.createHash('sha1').update(svg).digest('hex'));
  bytes+=Buffer.byteLength(svg); n++;
  const mn=pickMotif(row); motifCount[mn]=(motifCount[mn]||0)+1;
}
console.log('covers:', n, '| unique:', hashes.size, '| avg KB:', (bytes/n/1024).toFixed(1), '| total MB:', (bytes/1048576).toFixed(1));
console.log('motif spread:', Object.entries(motifCount).sort((a,b)=>b[1]-a[1]).map(([k,v])=>k+':'+v).join(' '));
