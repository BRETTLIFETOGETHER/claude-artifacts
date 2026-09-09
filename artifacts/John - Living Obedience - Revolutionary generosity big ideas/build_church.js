const pptxgen = require("pptxgenjs");
const NAVY="12253F", CREAM="FAF7F0", WARM="F2EDE1", GOLD="B08B3F", CHAR="2B2B2B", MUTE="6E6A62", LINE="D8D0C2", PALE="E6E0D4";
const pres = new pptxgen(); pres.layout="LAYOUT_WIDE"; pres.title="40 Days of Generosity — Church Adoption";
const SER="Georgia", SAN="Calibri";
let N=0;
function motif(s,d){s.addShape(pres.ShapeType.ellipse,{x:0.75,y:6.9,w:0.12,h:0.12,fill:{color:GOLD}});s.addShape(pres.ShapeType.ellipse,{x:0.96,y:6.9,w:0.12,h:0.12,fill:{color:"FFFFFF",transparency:100},line:{color:d?GOLD:LINE,width:1}});}
function slide(mode,eb,title){N++;const s=pres.addSlide();const d=mode==="dark";s.background={color:d?NAVY:(mode==="warm"?WARM:CREAM)};
 if(eb)s.addText(eb.toUpperCase(),{x:0.75,y:0.6,w:9.5,h:0.28,fontFace:SER,fontSize:9.5,color:GOLD,charSpacing:3.5,margin:0});
 if(title)s.addText(title,{x:0.75,y:1.0,w:11.8,h:0.85,fontFace:SER,fontSize:28,bold:true,color:d?"FFFFFF":NAVY,margin:0});
 motif(s,d);s.addText(String(N).padStart(2,"0"),{x:12.1,y:6.85,w:0.5,h:0.25,fontFace:SER,fontSize:10,color:d?"6B6455":"B4AC9C",align:"right",margin:0});return s;}
function hair(s,y){s.addShape(pres.ShapeType.line,{x:0.75,y:y,w:11.8,h:0,line:{color:LINE,width:1}});}

/* 1 */{const s=slide("dark");
 s.addShape(pres.ShapeType.ellipse,{x:5.98,y:2.05,w:0.2,h:0.2,fill:{color:GOLD}});
 s.addShape(pres.ShapeType.ellipse,{x:6.42,y:2.05,w:0.19,h:0.19,fill:{color:"FFFFFF",transparency:100},line:{color:GOLD,width:2}});
 s.addText("40 DAYS",{x:0.9,y:2.65,w:11.5,h:1.0,fontFace:SER,fontSize:58,bold:true,color:"FFFFFF",align:"center",charSpacing:2,margin:0});
 s.addText("OF GENEROSITY",{x:0.9,y:3.6,w:11.5,h:1.0,fontFace:SER,fontSize:58,bold:true,color:GOLD,align:"center",charSpacing:2,margin:0});
 s.addShape(pres.ShapeType.line,{x:5.9,y:4.85,w:1.5,h:0,line:{color:GOLD,width:2.5}});
 s.addText("Six weeks. Three tracks. One church.",{x:0.9,y:5.1,w:11.5,h:0.5,fontFace:SER,fontSize:19,italic:true,color:PALE,align:"center",margin:0});
 s.addNotes("Open by naming the covenant: this campaign asks the congregation for nothing.");}

/* 2 */{const s=slide("light","Why most churches avoid this","We only talk about money when we need some");
 s.addText("Which trains a congregation to brace at the word generosity, and to hear every mention of it as an appeal. They are not wrong to. Usually it is one.",{x:0.75,y:2.05,w:10.6,h:0.9,fontFace:SAN,fontSize:15,color:CHAR,lineSpacing:25,margin:0});
 hair(s,3.2);
 s.addText("This campaign is built to break that pattern in your church.\nIt disciples people out of fear rather than into the offering.",{x:0.75,y:3.5,w:11.8,h:1.4,fontFace:SER,fontSize:26,bold:true,color:NAVY,lineSpacing:40,margin:0});
 s.addText("Giving frequently rises afterward. That is a side effect. The moment it becomes the goal, the campaign stops working.",{x:0.75,y:5.3,w:10.6,h:0.8,fontFace:SAN,fontSize:13.5,italic:true,color:MUTE,lineSpacing:21,margin:0});}

/* 3 */{const s=slide("warm","The design","Three tracks, and you choose how many");
 const t=[["The weekend","Six messages with outlines, illustrations, Scripture and transitions supplied. Run this alone and the campaign still works — which is how most churches should start."],
 ["The groups","Six sessions, ninety minutes each. Participant guide and leader script for every week, written so a first-time host can lead without training."],
 ["The daily reader","Forty readings across the whole campaign. A story, a short teaching, an action step and three reflection questions each day."]];
 t.forEach((r,i)=>{const y=2.2+i*1.45;
  s.addText(r[0],{x:0.75,y:y,w:3.0,h:0.6,fontFace:SER,fontSize:20,bold:true,color:NAVY,margin:0});
  s.addText(r[1],{x:4.15,y:y-0.05,w:8.4,h:1.2,fontFace:SAN,fontSize:13,color:CHAR,lineSpacing:20,margin:0});
  hair(s,y+1.2);});
 s.addText("Someone who never joins a group still moves with the church.",{x:0.75,y:6.35,w:11.8,h:0.4,fontFace:SER,fontSize:14,italic:true,color:GOLD,margin:0});}

/* 4 */{const s=slide("light","The arc","Six weeks, six questions");
 const w=[["01","Who Owns It?","Whose is this, actually?"],["02","Enough","How much do we keep?"],["03","Open Hands","What am I afraid of?"],
 ["04","What Do You See?","What has God put in front of me?"],["05","Together","Who decides, and who comes after?"],["06","The Return","What is any of this for?"]];
 w.forEach((r,i)=>{const col=i%2,row=Math.floor(i/2);const x=0.75+col*6.05,y=2.2+row*1.5;
  s.addText(r[0],{x:x,y:y,w:0.85,h:0.6,fontFace:SER,fontSize:26,bold:true,color:"DDD5C4",margin:0});
  s.addText(r[1],{x:x+0.95,y:y-0.02,w:4.5,h:0.5,fontFace:SER,fontSize:17,bold:true,color:NAVY,margin:0});
  s.addText(r[2],{x:x+0.95,y:y+0.48,w:4.5,h:0.5,fontFace:SAN,fontSize:12.5,italic:true,color:MUTE,margin:0});});
 s.addNotes("Ownership, contentment, fear, sight, community, joy. Anyone at any income can travel this arc — that is deliberate.");}

/* 5 */{const s=slide("dark","The rule that makes it work");
 s.addText("Nobody is asked\nfor anything.",{x:0.9,y:1.9,w:11.3,h:1.8,fontFace:SER,fontSize:42,bold:true,color:"FFFFFF",lineSpacing:56,margin:0});
 s.addShape(pres.ShapeType.line,{x:0.95,y:4.0,w:2.0,h:0,line:{color:GOLD,width:2.5}});
 s.addText("No pledge cards. No commitment weekend. No capital appeal built into week six. That constraint is not politeness — it is the reason people talk honestly, and it is what separates formation from fundraising.",{x:0.9,y:4.3,w:10.4,h:1.4,fontFace:SAN,fontSize:15,color:PALE,lineSpacing:25,margin:0});
 s.addText("Somebody in every group is waiting to see whether it holds for all six weeks. It should.",{x:0.9,y:5.85,w:10.4,h:0.5,fontFace:SER,fontSize:16,italic:true,color:GOLD,margin:0});}

/* 6 */{const s=slide("light","Timing","Run it when the church needs nothing");
 const c=[["Recommended","January · post-Easter · early fall. Any season with nothing attached to it. The congregation will believe you, and that belief is the whole asset."],
 ["Not recommended","Alongside a budget appeal or at fiscal year end. They will read six weeks as a setup — reasonably, because it usually is."],
 ["If you must","Say so from the platform in week one, and keep every ask entirely outside the groups. Pastors can carry either answer. They cannot carry both."]];
 const w=(11.8-0.8)/3;
 c.forEach((r,i)=>{const x=0.75+i*(w+0.4);
  s.addText(r[0],{x:x,y:2.3,w:w,h:0.5,fontFace:SER,fontSize:18,bold:true,color:i===1?GOLD:NAVY,margin:0});
  s.addShape(pres.ShapeType.line,{x:x,y:2.95,w:1.1,h:0,line:{color:LINE,width:1.5}});
  s.addText(r[1],{x:x,y:3.15,w:w,h:2.3,fontFace:SAN,fontSize:12.5,color:CHAR,lineSpacing:20,margin:0});});}

/* 7 */{const s=slide("warm","What you receive","The kit");
 const k=["Six message outlines with Scripture and illustrations","Six group sessions — participant guide and leader script","The forty-day daily reader","A family edition for households with children",
 "Testimony recruitment and briefing guide","Promotional artwork, slides and social assets","Leader training video","Launch checklist and timeline"];
 k.forEach((t,i)=>{const col=i%2,row=Math.floor(i/2);const x=0.75+col*6.05,y=2.3+row*1.05;
  s.addShape(pres.ShapeType.ellipse,{x:x,y:y+0.12,w:0.13,h:0.13,fill:{color:GOLD}});
  s.addText(t,{x:x+0.4,y:y,w:5.5,h:0.6,fontFace:SAN,fontSize:13.5,color:CHAR,margin:0});});}

/* 8 */{const s=slide("light","What it costs you","Three decisions and four weeks of coordination");
 const d=[["How many tracks","One, two, or three. Most churches start with the weekend and add groups the second time they run it."],
 ["When","Six weekends of your teaching calendar, in a season with nothing attached."],
 ["Who tells the stories","Six testimonies, three minutes each, no dollar amounts. Vary them deliberately — if all six come from your wealthiest households, the campaign quietly teaches that generosity belongs to them."]];
 d.forEach((r,i)=>{const y=2.3+i*1.4;
  s.addText(r[0],{x:0.75,y:y,w:3.3,h:0.6,fontFace:SER,fontSize:17,bold:true,color:NAVY,margin:0});
  s.addText(r[1],{x:4.4,y:y-0.05,w:8.15,h:1.15,fontFace:SAN,fontSize:13,color:CHAR,lineSpacing:20,margin:0});
  hair(s,y+1.15);});
 s.addText("No consultant. No travel. No on-site team.",{x:0.75,y:6.4,w:11.8,h:0.4,fontFace:SER,fontSize:15,italic:true,color:GOLD,margin:0});}

/* 9 */{const s=slide("dark");
 s.addText("What would be true in your church\nif nobody were afraid of money?",{x:0.9,y:2.4,w:11.3,h:1.9,fontFace:SER,fontSize:33,bold:true,color:"FFFFFF",lineSpacing:48,margin:0});
 s.addShape(pres.ShapeType.line,{x:0.95,y:4.6,w:2.0,h:0,line:{color:GOLD,width:2.5}});
 s.addText("A thirty-minute conversation and a sample kit. No cost, no obligation, and nobody from our side will follow up asking you for anything.",{x:0.9,y:4.9,w:10.4,h:1.0,fontFace:SAN,fontSize:15,color:PALE,lineSpacing:24,margin:0});
 s.addText("LifeTogether",{x:0.9,y:6.3,w:10.4,h:0.35,fontFace:SER,fontSize:14,bold:true,color:GOLD,margin:0});}

pres.writeFile({fileName:"/mnt/user-data/outputs/40-Days-of-Generosity-Church-Adoption-Deck.pptx"}).then(()=>console.log("ok"));
