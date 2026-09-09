const pptxgen = require("pptxgenjs");
const NAVY="12253F", DEEP="0B1728", CREAM="FAF7F0", WARM="F2EDE1", GOLD="B08B3F",
      CHAR="2B2B2B", MUTE="6E6A62", LINE="D8D0C2", PALE="E6E0D4";
const pres=new pptxgen(); pres.layout="LAYOUT_WIDE"; pres.title="Living Obedience — Board Presentation";
const SER="Georgia", SAN="Calibri";
let N=0;
function motif(s,d){s.addShape(pres.ShapeType.ellipse,{x:0.75,y:6.9,w:0.12,h:0.12,fill:{color:GOLD}});
 s.addShape(pres.ShapeType.ellipse,{x:0.96,y:6.9,w:0.12,h:0.12,fill:{color:"FFFFFF",transparency:100},line:{color:d?GOLD:LINE,width:1}});}
function slide(mode,eb,title){N++;const s=pres.addSlide();const d=mode==="dark";
 s.background={color:d?NAVY:(mode==="warm"?WARM:CREAM)};
 if(eb)s.addText(eb.toUpperCase(),{x:0.75,y:0.6,w:9.5,h:0.28,fontFace:SER,fontSize:9.5,color:GOLD,charSpacing:3.5,margin:0});
 if(title)s.addText(title,{x:0.75,y:1.0,w:11.8,h:0.9,fontFace:SER,fontSize:30,bold:true,color:d?"FFFFFF":NAVY,margin:0});
 motif(s,d);return s;}
function hair(s,y){s.addShape(pres.ShapeType.line,{x:0.75,y:y,w:11.8,h:0,line:{color:LINE,width:1}});}

/* 1 TITLE */{const s=slide("dark");
 s.addShape(pres.ShapeType.ellipse,{x:0.9,y:1.95,w:0.19,h:0.19,fill:{color:GOLD}});
 s.addShape(pres.ShapeType.ellipse,{x:1.32,y:1.95,w:0.18,h:0.18,fill:{color:"FFFFFF",transparency:100},line:{color:GOLD,width:2}});
 s.addText("Living Obedience",{x:0.9,y:2.55,w:11.5,h:1.2,fontFace:SER,fontSize:60,bold:true,color:"FFFFFF",margin:0});
 s.addShape(pres.ShapeType.line,{x:0.95,y:3.85,w:2.0,h:0,line:{color:GOLD,width:2.5}});
 s.addText("Saying yes to God with your life, your family, your business, your wealth.",{x:0.9,y:4.1,w:11,h:0.5,fontFace:SER,fontSize:19,italic:true,color:PALE,margin:0});
 s.addText("A proposal to the Board of The Signatry  ·  LifeTogether  ·  August 2026",{x:0.9,y:6.35,w:11,h:0.3,fontFace:SAN,fontSize:11,color:"8C8578",margin:0});
 s.addNotes("[0:00] Thank them. One line: you've already approved a book — I want to show you the book, and then show you what it could become. I'll be done in eight minutes.");}

/* 2 APPROVED */{const s=slide("light","What you have already approved","The book");
 const r=[["Living Obedience","Eighteen chapters. Written with Steve and Dale, in one voice, from their own material."],
 ["The six-session curriculum","Participant guide and leader script — so a first-time host can lead it without training."],
 ["The forty-day reader","A story, a Scripture, an exercise and three questions each morning."]];
 r.forEach((x,i)=>{const y=2.3+i*1.35;
  s.addText(x[0],{x:0.75,y:y,w:3.9,h:0.6,fontFace:SER,fontSize:19,bold:true,color:NAVY,margin:0});
  s.addText(x[1],{x:5.0,y:y-0.03,w:7.5,h:1.05,fontFace:SAN,fontSize:14,color:CHAR,lineSpacing:22,margin:0});
  hair(s,y+1.1);});
 s.addText("Ready to commission today  ·  publication-ready inside twelve months",{x:0.75,y:6.35,w:11.8,h:0.4,fontFace:SER,fontSize:15,italic:true,color:GOLD,margin:0});
 s.addNotes("[1:00] Keep this fast. The room already said yes to this — you're confirming, not selling. Then pivot: here's why I think it's bigger than a book.");}

/* 3 THE IDEA */{const s=slide("dark","The idea");
 s.addText("Living Obedience is not\na generosity book.",{x:0.9,y:1.9,w:11.3,h:1.8,fontFace:SER,fontSize:40,bold:true,color:"FFFFFF",lineSpacing:54,margin:0});
 s.addShape(pres.ShapeType.line,{x:0.95,y:4.0,w:2.0,h:0,line:{color:GOLD,width:2.5}});
 s.addText("Generosity is what flows out of it — which is exactly why it will reach people a generosity book never reaches. Obedience is the capstone idea, and the counterintuitive one.",{x:0.9,y:4.3,w:10.6,h:1.3,fontFace:SAN,fontSize:16,color:PALE,lineSpacing:27,margin:0});
 s.addText("And 'living' matters as much as 'obedience' — a pathway, not a single decision.",{x:0.9,y:5.75,w:10.6,h:0.5,fontFace:SER,fontSize:16,italic:true,color:GOLD,margin:0});
 s.addNotes("[2:00] This is the line Dale and I agreed on. Don't over-explain — say it and let it sit for two seconds.");}

/* 4 PROGRESSION */{const s=slide("warm","The vision","One book, or a progression");
 const r=[["01","Living Obedience","The yes."],["02","Lifestyle Obedience","The day after the yes."],
 ["03","Living Obedience Together","The household."],["04","The Living Pledge","The yes in writing, witnessed."],
 ["05","Living Legacy","What outlives you."],["06","Living Leadership","Into the enterprise."]];
 r.forEach((x,i)=>{const col=i%2,row=Math.floor(i/2);const xx=0.75+col*6.05,y=2.2+row*1.45;
  s.addText(x[0],{x:xx,y:y,w:0.85,h:0.55,fontFace:SER,fontSize:24,bold:true,color:"DDD5C4",margin:0});
  s.addText(x[1],{x:xx+0.9,y:y-0.02,w:4.6,h:0.5,fontFace:SER,fontSize:18,bold:true,color:NAVY,margin:0});
  s.addText(x[2],{x:xx+0.9,y:y+0.48,w:4.6,h:0.5,fontFace:SAN,fontSize:13,italic:true,color:MUTE,margin:0});});
 s.addNotes("[3:00] Six volumes. Each one is a product an advisor or a church would buy on its own. Don't teach them — just let them see the shape.");}

/* 5 DIFFERENTIATOR */{const s=slide("light","Why only you can publish this","Give · Grow · Grant");
 s.addText("Every organization in this field can teach giving and granting.",{x:0.75,y:2.15,w:11.8,h:0.6,fontFace:SAN,fontSize:17,color:CHAR,margin:0});
 s.addText("The Signatry is the only one that can write honestly\nabout what happens to the money in between.",{x:0.75,y:2.95,w:11.8,h:1.5,fontFace:SER,fontSize:30,bold:true,color:NAVY,lineSpacing:44,margin:0});
 hair(s,4.75);
 s.addText("Twenty types of alternative investment in five years. General partner positions in operating businesses. Donor capital curated and grown rather than parked. That is the chapter no other publisher in this category can commission — and it is what turns this from a good book anyone could have written into the book only this house could produce.",{x:0.75,y:5.0,w:11.4,h:1.5,fontFace:SAN,fontSize:14.5,color:CHAR,lineSpacing:24,margin:0});
 s.addNotes("[4:30] This is the most important slide. It came from Dale. It is the argument that this is strategic rather than sentimental.");}

/* 6 WHAT IT BECOMES */{const s=slide("warm","What it becomes","Beyond the book");
 const r=[["Forty families, forty stories","Dale's idea, and the strongest one here. Real families on film, one per campaign day — the one asset a book cannot fake and a competitor cannot buy."],
 ["A churchwide campaign","Six weeks, three tracks, into congregations LifeTogether already serves."],
 ["An advisor edition","The fastest channel in this category — advisors already hold the relationship and the trust."],
 ["An assessment","Ten minutes, scored — the reason a family comes back, and data The Signatry could publish annually."]];
 r.forEach((x,i)=>{const y=2.2+i*1.2;
  s.addText(x[0],{x:0.75,y:y,w:3.6,h:0.6,fontFace:SER,fontSize:16,bold:true,color:NAVY,margin:0});
  s.addText(x[1],{x:4.7,y:y-0.05,w:7.8,h:1.0,fontFace:SAN,fontSize:13,color:CHAR,lineSpacing:20,margin:0});
  hair(s,y+1.0);});
 s.addNotes("[5:30] Lead with the forty stories and credit Dale by name. It's his idea and he'll defend it in the room after you leave.");}

/* 7 THE NUMBERS */{const s=slide("light","The estimate","Three tiers");
 const r=[["TIER ONE","The book and curriculum","$95,000","Approved. Ready to commission."],
 ["TIER TWO","The system — volumes, campaign, film, assessment","$430K – $600K","Modular. Commission in sequence over 24–30 months."],
 ["TIER THREE","The platform — licensing and tools","No fee","Built at our cost and risk, co-branded, on revenue participation."]];
 r.forEach((x,i)=>{const y=2.25+i*1.5;
  s.addText(x[0],{x:0.75,y:y,w:1.9,h:0.4,fontFace:SER,fontSize:11,bold:true,color:GOLD,charSpacing:1.5,margin:0});
  s.addText(x[1],{x:0.75,y:y+0.4,w:6.3,h:0.5,fontFace:SER,fontSize:18,bold:true,color:NAVY,margin:0});
  s.addText(x[3],{x:0.75,y:y+0.88,w:6.3,h:0.4,fontFace:SAN,fontSize:12.5,italic:true,color:MUTE,margin:0});
  s.addText(x[2],{x:8.3,y:y+0.35,w:4.2,h:0.6,fontFace:SER,fontSize:24,bold:true,color:i===2?NAVY:GOLD,align:"right",margin:0});
  hair(s,y+1.32);});
 s.addNotes("[6:30] Say the tier three line out loud: we are not asking you to fund a platform on faith. We'll build it at our risk. If it works we both earn.");}

/* 8 ASK */{const s=slide("dark","The ask");
 s.addText("Three decisions.",{x:0.9,y:1.75,w:11.3,h:0.9,fontFace:SER,fontSize:38,bold:true,color:"FFFFFF",margin:0});
 const r=[["One","Approve Tier One and commission the book."],
 ["Two","Ask us back in ninety days with a scoped recommendation for Tier Two."],
 ["Three","Give us permission to bring a Tier Three structure to the chair — at no cost either way."]];
 r.forEach((x,i)=>{const y=3.0+i*1.1;
  s.addText(x[0],{x:0.9,y:y,w:1.5,h:0.5,fontFace:SER,fontSize:16,bold:true,color:GOLD,margin:0});
  s.addText(x[1],{x:2.6,y:y-0.02,w:9.6,h:0.8,fontFace:SAN,fontSize:16,color:PALE,lineSpacing:25,margin:0});});
 s.addText("LifeTogether",{x:0.9,y:6.35,w:11,h:0.35,fontFace:SER,fontSize:13,bold:true,color:GOLD,margin:0});
 s.addNotes("[8:00] Finish early. A guest who takes eight of his ten minutes is the guest they invite back. Stop talking and take questions.");}

pres.writeFile({fileName:"/mnt/user-data/outputs/Living-Obedience-Board-Deck.pptx"}).then(()=>console.log("ok"));
