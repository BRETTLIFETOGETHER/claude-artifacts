/* 40dc cover engine — deterministic from fingerprint. Gold palettes are reserved for flagship. */
(function(){
"use strict";
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
const NAVY9="#101E38",NAVY8="#172542",NAVY7="#22335A",GOLD="#C9A13B",GDEEP="#B98D3E",GSOFT="#E4C878",
      EMBER="#E2703A",CREAM="#FBF8F1",PAPER="#FFFFFF",LINE="#E7E0D2";
/* palettes: [bg1,bg2,ornament,text,accent]  0-4 gold(flagship) 5-17 standard */
const PAL=[
 [NAVY9,NAVY8,GOLD,GSOFT,GOLD],[NAVY8,"#1d2c50",GSOFT,"#F6EBCF",GOLD],[GDEEP,GOLD,NAVY9,NAVY9,NAVY8],
 ["#2a2410",NAVY9,GOLD,GSOFT,GDEEP],[NAVY7,NAVY9,GOLD,"#F2E7C9",GSOFT],
 [NAVY8,NAVY7,"#8fa0c4","#EDEFF5",EMBER],[NAVY9,"#15223f","#5f739e","#DFE5F0",EMBER],
 [CREAM,"#f3edde",NAVY7,NAVY8,EMBER],[PAPER,CREAM,"#c9c2ae",NAVY8,EMBER],
 [NAVY7,"#2b3d68","#93a5cc","#F0F3F9",EMBER],["#20304f",NAVY9,"#7286ad","#E7EBF4",EMBER],
 [EMBER,"#C85A28","#FBE3D4","#FFF6EF",NAVY9],["#f6efdf",CREAM,"#b9ad8d",NAVY8,EMBER],
 [NAVY8,"#101a30","#42557f","#E3E8F2",GSOFT?EMBER:EMBER],["#e9e1cd","#f6f1e4",NAVY7,NAVY8,EMBER],
 ["#152036",NAVY7,"#6d81a8","#EAEEF6",EMBER],[CREAM,"#efe7d3","#a89f83",NAVY8,EMBER],
 ["#1b2a49",NAVY9,"#556a96","#E5EAF3",EMBER]];
const GOLD_SET=[0,1,2,3,4],STD_SET=[5,6,7,8,9,10,11,12,13,14,15,16,17];
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}
function wrap(t,max){const w=String(t).split(/\s+/),ls=[];let c="";for(const x of w){if((c+" "+x).trim().length>max){if(c)ls.push(c);c=x}else c=(c+" "+x).trim()}if(c)ls.push(c);return ls.slice(0,4)}
function orn(i,r,c,W,H){const o=[];const R=(a,b)=>a+r()*(b-a);
 switch(i%14){
 case 0:for(let k=0;k<26;k++)o.push(`<circle cx="${R(0,W)}" cy="${R(0,H*.62)}" r="${R(1.2,3.4)}" fill="${c}" opacity="${R(.18,.5)}"/>`);break;
 case 1:for(let k=0;k<4;k++)o.push(`<circle cx="${W*.78}" cy="${H*.2}" r="${28+k*22}" fill="none" stroke="${c}" stroke-width="1.4" opacity="${.5-k*.09}"/>`);break;
 case 2:o.push(`<path d="M${W*.5} ${H*.1} v${H*.24} M${W*.38} ${H*.2} h${W*.24}" stroke="${c}" stroke-width="5" opacity=".7" stroke-linecap="round"/>`);break;
 case 3:{const cx=W*.76,cy=H*.18;for(let k=0;k<8;k++){const a=k*Math.PI/4;o.push(`<line x1="${cx+Math.cos(a)*12}" y1="${cy+Math.sin(a)*12}" x2="${cx+Math.cos(a)*30}" y2="${cy+Math.sin(a)*30}" stroke="${c}" stroke-width="3.4" stroke-linecap="round" opacity=".85"/>`)}o.push(`<circle cx="${cx}" cy="${cy}" r="6.5" fill="${c}"/>`);break}
 case 4:for(let k=0;k<6;k++)o.push(`<line x1="0" y1="${H*.12+k*13}" x2="${W*.42}" y2="${H*.12+k*13}" stroke="${c}" stroke-width="2" opacity="${.55-k*.07}"/>`);break;
 case 5:for(let k=0;k<5;k++)o.push(`<path d="M${W*.62+k*16} ${H*.3} l14 -18 l14 18" fill="none" stroke="${c}" stroke-width="2.4" opacity=".6"/>`);break;
 case 6:o.push(`<path d="M${W*.2} ${H*.24} q22 -34 44 0 q-22 30 -44 0" fill="${c}" opacity=".55"/><path d="M${W*.2+52} ${H*.24} q22 -34 44 0 q-22 30 -44 0" fill="${c}" opacity=".35"/>`);break;
 case 7:o.push(`<circle cx="${W*.5}" cy="${H*.2}" r="34" fill="none" stroke="${c}" stroke-width="1.6" opacity=".7"/><circle cx="${W*.5+34}" cy="${H*.2}" r="4.6" fill="${c}"/>`);break;
 case 8:for(let y=0;y<5;y++)for(let x=0;x<9;x++)o.push(`<circle cx="${W*.1+x*13}" cy="${H*.1+y*13}" r="1.7" fill="${c}" opacity="${(x+y)%2?.45:.22}"/>`);break;
 case 9:o.push(`<rect x="${W*.66}" y="${H*.1}" width="46" height="46" transform="rotate(45 ${W*.66+23} ${H*.1+23})" fill="none" stroke="${c}" stroke-width="2.2" opacity=".7"/>`);break;
 case 10:o.push(`<rect x="14" y="14" width="${W-28}" height="${H-28}" fill="none" stroke="${c}" stroke-width="1.4" opacity=".5" rx="10"/>`);break;
 case 11:{const cx=W*.24,cy=H*.16;for(let k=0;k<12;k++){const a=k*Math.PI/6;o.push(`<line x1="${cx}" y1="${cy}" x2="${cx+Math.cos(a)*26}" y2="${cy+Math.sin(a)*26}" stroke="${c}" stroke-width="1.6" opacity=".55"/>`)}break}
 case 12:for(let k=0;k<4;k++)o.push(`<rect x="${W*.6+k*13}" y="${H*.3-k*11}" width="9" height="9" fill="${c}" opacity="${.7-k*.12}"/>`);break;
 case 13:break}
 return o.join("")}
function layout(i,W,H,p,r){const[b1,b2,oc]=p;const g=`g${Math.floor(r()*1e9)}`;let d=`<defs><linearGradient id="${g}" x1="0" y1="0" x2="${["0","1","1","0"][i%4]}" y2="1"><stop offset="0" stop-color="${b1}"/><stop offset="1" stop-color="${b2}"/></linearGradient></defs>`;
 let base=`<rect width="${W}" height="${H}" fill="url(#${g})"/>`;
 switch(i%12){
 case 1:base+=`<path d="M0 ${H*.62} Q ${W*.5} ${H*.52} ${W} ${H*.66} V${H} H0 Z" fill="${b2}" opacity=".55"/>`;break;
 case 2:base+=`<circle cx="${W*.5}" cy="${H*.34}" r="${W*.34}" fill="${oc}" opacity=".14"/>`;break;
 case 3:base+=`<path d="M0 0 H${W} V${H*.16} H0 Z" fill="${oc}" opacity=".2"/>`;break;
 case 4:base+=`<path d="M0 ${H} L${W} ${H*.55} V${H} Z" fill="${b1}" opacity=".5"/>`;break;
 case 5:base+=`<path d="M${W*.5} ${H*.06} A ${W*.42} ${W*.42} 0 0 1 ${W*.5} ${H*.5}" fill="none" stroke="${oc}" stroke-width="2" opacity=".5"/>`;break;
 case 6:base+=`<rect x="0" y="${H*.5}" width="${W}" height="1.5" fill="${oc}" opacity=".6"/>`;break;
 case 7:base+=`<path d="M0 ${H*.3} Q ${W*.25} ${H*.22} ${W*.5} ${H*.3} T ${W} ${H*.3}" fill="none" stroke="${oc}" stroke-width="2" opacity=".55"/>`;break;
 case 8:base+=`<circle cx="${W*.85}" cy="${H*.86}" r="${W*.5}" fill="${b2}" opacity=".5"/>`;break;
 case 9:base+=`<path d="M0 ${H*.14} H${W*.6}" stroke="${oc}" stroke-width="6" opacity=".7" stroke-linecap="round"/>`;break;
 case 10:base+=`<rect x="${W*.08}" y="${H*.06}" width="${W*.84}" height="${H*.5}" rx="14" fill="${b2}" opacity=".4"/>`;break;
 case 11:base+=`<path d="M0 0 L${W*.4} 0 L0 ${H*.4} Z" fill="${oc}" opacity=".16"/>`;break}
 return d+base}
function coverSVG(o,opts){opts=opts||{};const W=300,H=400,fp=parseInt(o.fp,16)||1,r=mulberry32(fp);
 const flag=!!(o.co&1);const pi=flag?GOLD_SET[fp%GOLD_SET.length]:STD_SET[fp%STD_SET.length];
 const p=PAL[pi],li=(fp>>>3)%12,oi=(fp>>>6)%14,lk=(fp>>>9)%9;
 const tcol=p[3],acc=p[4];
 const lines=wrap(o.t, lk%3===0?14:16), fs=lines.length>2?30:34, lh=fs*1.12;
 const anchor=lk%3===2?"middle":"start", tx=anchor==="middle"?W/2:30;
 const ty=[H*.55,H*.62,H*.5][lk%3];
 let txt=`<text x="${tx}" y="${ty}" text-anchor="${anchor}" font-family="'Hanken Grotesk',sans-serif" font-weight="700" font-size="${fs}" fill="${tcol}">`+
   lines.map((l,i)=>`<tspan x="${tx}" dy="${i?lh:0}">${esc(l)}</tspan>`).join("")+`</text>`;
 const eyeb=`<text x="${tx}" y="${ty-lines.length*0+ -8 - (fs*.9)}" text-anchor="${anchor}" font-family="'Archivo',sans-serif" font-weight="600" font-size="11" letter-spacing="2.4" fill="${acc}">${esc(opts.eyebrow||"40 DAY CAMPAIGN")}</text>`;
 let sub="";if(o.s&&lk%2===0){const sl=wrap(o.s,30).slice(0,2);sub=`<text x="${tx}" y="${ty+lines.length*lh+6}" text-anchor="${anchor}" font-family="'Spectral',serif" font-size="13.5" fill="${tcol}" opacity=".82">`+sl.map((l,i)=>`<tspan x="${tx}" dy="${i?17:0}">${esc(l)}</tspan>`).join("")+`</text>`}
 const rule=`<rect x="${anchor==="middle"?W/2-22:30}" y="${ty+lines.length*lh+(sub?46:16)}" width="44" height="3.5" rx="2" fill="${acc}"/>`;
 const brand=`<text x="30" y="${H-24}" font-family="'Archivo',sans-serif" font-weight="600" font-size="9.5" letter-spacing="2" fill="${tcol}" opacity=".65">LIFETOGETHER</text>`;
 const star=flag?`<g transform="translate(${W-46},22)"><rect width="26" height="26" rx="7" fill="${GOLD}"/><path transform="translate(13,13.5)" d="M0,-7 L2,-2.2 L7,-2 L3.2,1.4 L4.4,6.4 L0,3.6 L-4.4,6.4 L-3.2,1.4 L-7,-2 L-2,-2.2 Z" fill="${NAVY9}"/></g>`:"";
 return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(o.t)}">`+
   layout(li,W,H,p,r)+orn(oi,r,p[2],W,H)+eyeb+txt+sub+rule+brand+star+`</svg>`}
window.Covers={svg:coverSVG,uri:o=>"data:image/svg+xml;utf8,"+encodeURIComponent(coverSVG(o))};
})();
