/* LifeTogether Campaign Engine — spec, planner, assembler.
   Turns a title + subtitle into a complete publishable campaign by planning a
   sequence of small Claude calls, then assembling and verifying the result.

   Why chunked: one 8-week campaign at full spec is ~20,000 tokens of JSON —
   far past a single response, and far past Netlify's function timeout. Each
   task below is sized to return in a few seconds, so the build streams in,
   shows progress, and can retry one piece without restarting. */
(function(){
"use strict";

/* ---------------- derivation (mirrors the spec's DERIVE block) ---------------- */
const NUMW={one:1,two:2,three:3,four:4,five:5,six:6,seven:7,eight:8,nine:9,ten:10,eleven:11,twelve:12};
const SET_NOUNS=/\b(beatitudes|words|questions|promises|parables|signs|names|commandments|petitions|i ?ams|sayings|habits|marks|virtues|gifts|fruits)\b/i;

function derive(subtitle,title){
  const s=String(subtitle||""), t=String(title||"");
  let weeks=null, source="default";
  let m=s.match(/(\d+)\s*[-–—\s]?\s*week/i);
  if(m){weeks=parseInt(m[1],10);source="subtitle"}
  if(!weeks){const m2=s.match(/\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s*[-–—\s]?\s*week/i);
    if(m2){weeks=NUMW[m2[1].toLowerCase()];source="subtitle"}}
  let setLabel="";
  const ms=s.match(/\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s+(?:last\s+)?([a-z][a-z ]{2,20}?)\b/i);
  if(ms&&SET_NOUNS.test(s)){
    const n=/^\d+$/.test(ms[1])?parseInt(ms[1],10):NUMW[ms[1].toLowerCase()];
    const noun=(s.match(SET_NOUNS)||[""])[0];
    if(n>=2&&n<=12){setLabel=`${ms[1]} ${noun}`.trim();
      if(!weeks){weeks=n;source="fixed set"}}
  }
  if(!weeks){weeks=6;source="default (no count stated)"}
  weeks=Math.max(1,Math.min(12,weeks));
  return {weeks,days:weeks*5,setLabel,source,title:t,subtitle:s};
}

/* ---------------- batch input parsing ---------------- */
const BATCH_CAP=5;
function parseBatch(text){
  const lines=String(text||"").split(/\r?\n/).map(l=>l.trim()).filter(Boolean);
  const all=[];
  for(const raw of lines){
    const line=raw.replace(/^\s*\d+\s*[.)]\s*/,"").trim();
    if(!line||/^\.{2,}$/.test(line))continue;
    const parts=line.split("|").map(p=>p.trim());
    if(!parts[0])continue;
    all.push({title:parts[0],subtitle:parts[1]||"",text:parts[2]||""});
  }
  return {list:all.slice(0,BATCH_CAP),dropped:Math.max(0,all.length-BATCH_CAP),total:all.length};
}

/* ---------------- shared system prompt ---------------- */
const SYS=`You are the LifeTogether Campaign Engine. You build complete, publishable church campaigns. Nothing you produce is a placeholder.

VOICE RULES — THESE GOVERN EVERYTHING
- Write like a pastor who has actually sat with people, not like a curriculum committee.
- Short declarative sentences. No stacked adjectives. Never use the words "journey", "unpack", "lean into", "season of life", or "do life together".
- Never open with a rhetorical question you immediately answer.
- Concrete over abstract. "The layoffs at the plant" beats "economic uncertainty."
- Assume the reader is an intelligent adult who has been to church and is tired of being talked down to.
- Where a Greek or Hebrew word does real work, use it once and explain it in plain English. Never more than one per session.
- Quote Scripture by reference. Keep any direct quotation to a single short verse.
- Scripture references must be real and correctly abbreviated. Never invent a reference or a fact about a real person.

HARD RULES
- No placeholder text. No "content to come." No brackets.
- If you cannot write something well, write it shorter, not vaguer.
- You are producing ONE SLICE of a larger campaign. Return only the JSON for the slice requested, matching the shape given exactly.`;

/* ---------------- task planner ---------------- */
function ctxLine(c){
  return `CAMPAIGN\nTitle: ${c.title}\nSubtitle: ${c.subtitle}\nPrimary text: ${c.text||"choose the text the title implies"}\nWeeks: ${c.weeks} (exactly ${c.weeks} sessions and ${c.days} devotional days)`+
    (c.setLabel?`\nThe subtitle names a fixed set: ${c.setLabel}. One item per session, in order.`:"");
}
function sessCtx(sessions,upto){
  const done=(sessions||[]).filter(Boolean).slice(0,upto);
  if(!done.length)return "";
  return "\nSessions already written (do not repeat their texts or big ideas):\n"+
    done.map(s=>`  ${s.n}. ${s.t} — ${s.ref} — ${s.big}`).join("\n");
}

function plan(c){
  const T=[];const W=c.weeks;
  for(let i=1;i<=W;i++)T.push({phase:"sessions",key:"s"+i,n:i,max:1500,
    label:`Session ${i} of ${W}`,
    user:st=>`${ctxLine(c)}${sessCtx(st.sessions,i-1)}

Write SESSION ${i} of ${W}${c.setLabel?` — item ${i} of the ${c.setLabel}`:""}.
"com" is exactly 3 paragraphs of 60–90 words each. "Q" is exactly 5 objects; each "note" says what will actually happen in the room when that question is asked. "app" is one specific act with a deadline before the next meeting. "prayer" is 2–3 sentences in first person. "LN" is exactly 2 strings: where this session stalls, and what to do about it.
Return JSON: {"n":${i},"t":"","sub":"","ref":"","big":"","open":"","com":["","",""],"Q":[{"q":"","note":""},{"q":"","note":""},{"q":"","note":""},{"q":"","note":""},{"q":"","note":""}],"app":"","prayer":"","LN":["",""]}`});

  for(let w=1;w<=W;w++){const a=(w-1)*5+1,b=w*5;
    T.push({phase:"devotionals",key:"d"+w,n:w,max:1400,
      label:`Devotionals ${a}–${b}`,
      user:st=>{const s=(st.sessions||[])[w-1];
        return `${ctxLine(c)}
Week ${w} session: ${s?`"${s.t}" — ${s.ref} — ${s.big}`:"(write toward the week's theme)"}

Write devotional days ${a} through ${b} — Monday through Friday of week ${w}. They lead into that session, so the group arrives having read the same five days.
Each "body" is 3–4 sentences, under 90 seconds to read. Each "practice" is a physical or verbal act, never a feeling.
Return JSON: {"devotionals":[${[0,1,2,3,4].map(k=>`{"d":${a+k},"t":"","ref":"","body":"","q":"","practice":""}`).join(",")}]}`}});
  }

  for(let w=1;w<=W;w+=2){const pair=w+1<=W?[w,w+1]:[w];
    T.push({phase:"sermons",key:"m"+w,n:w,max:1200,
      label:`Sermon${pair.length>1?"s":""} ${pair.join(" & ")}`,
      user:st=>`${ctxLine(c)}${sessCtx(st.sessions,W)}

Write the weekend sermon outline${pair.length>1?"s":""} for week${pair.length>1?"s":""} ${pair.join(" and ")}.
The sermon title must differ from the session title — this one is for a platform. Exactly 3 movements. The "cta" names a specific response with a mechanism: a card, a silence, an envelope, a conversation.
Return JSON: {"sermons":[${pair.map(n=>`{"n":${n},"t":"","ref":"","big":"","movements":["","",""],"cta":""}`).join(",")}]}`});
  }

  for(let w=1;w<=W;w++)T.push({phase:"kit",key:"k"+w,n:w,max:1600,
    label:`Kit — week ${w}`,
    user:st=>{const s=(st.sessions||[])[w-1];
      return `${ctxLine(c)}
Week ${w} session: ${s?`"${s.t}" — ${s.ref} — ${s.big}`:"(write toward the week's theme)"}

Write every kit asset for WEEK ${w} only. The video fields are the pastor speaking in first person, time-coded 0:00 (opening line), 3:00 (the heart of it), 8:00 (the handoff question). "takehome" is the blank a child fills in. "verses" carries the week's memory verse reference, its short text, and one practice printed on the back. "testimony" is one question designed to produce a usable story.
Return JSON: {"family":{"w":${w},"big":"","dinner":"","prayer":"","practice":"","coaching":""},"student":{"w":${w},"line":"","honest":"","q":"","week":"","verse":""},"video":{"w":${w},"open":"","heart":"","handoff":""},"leader":{"w":${w},"prep":"","stalls":"","ifshort":""},"campaign":{"w":${w},"bulletin":"","card":"","social":"","followup":""},"kids":{"w":${w},"big":"","q":"","activity":"","takehome":""},"verses":{"w":${w},"ref":"","text":"","practice":""},"testimony":{"w":${w},"prompt":""}}`}});

  const COMP=[
   ["testimony_system","Testimony capture system","When to ask, the specific question, the format, the permission protocol, and what makes a story usable. 5–7 label/value pairs.",`{"testimony_system":[{"l":"","v":""}]}`],
   ["callback","The 90-day callback","What gets written in the final session, who holds it, who mails it, and the follow-up message. 4–6 label/value pairs.",`{"callback":[{"l":"","v":""}]}`],
   ["host","Host recruitment","The ask in one paragraph, what a host does and does not do, the six real objections and the single answer that covers all six. 8–10 label/value pairs.",`{"host":[{"l":"","v":""}]}`],
   ["measurement","Measurement sheet","8–10 metrics: what to collect, when to collect it, and what it tells you.",`{"measurement":[{"metric":"","when":"","tells":""}]}`],
   ["lengths","Alternate lengths","Full, half, quarter, and single-Sunday versions. For each: what it keeps, what it drops, and who it is best for.",`{"lengths":[{"t":"","count":"","keeps":"","bestfor":""}]}`],
   ["access","Translation and accessibility","Spanish, large print, audio-first, plain language, and real captions. 5–7 label/value pairs.",`{"access":[{"l":"","v":""}]}`]];
  COMP.forEach(([k,label,ask,shape])=>T.push({phase:"completions",key:"c_"+k,comp:k,max:1400,
    label,user:()=>`${ctxLine(c)}

Write the ${label} for this campaign. ${ask} Write it for this campaign specifically, not generically.
Return JSON: ${shape}`}));
  return T;
}

/* ---------------- assembly ---------------- */
function blank(c){return {meta:{title:c.title,subtitle:c.subtitle,weeks:c.weeks,days:c.days,text:c.text||""},
  sessions:[],devotionals:[],sermons:[],
  kit:{family:[],student:[],video:[],leader:[],campaign:[],kids:[],verses:[],testimony:[]},
  completions:{testimony_system:[],callback:[],host:[],measurement:[],lengths:[],access:[]}}}
const KITKEYS=["family","student","video","leader","campaign","kids","verses","testimony"];
function merge(camp,task,out){
  if(!out)return camp;
  if(task.phase==="sessions"){camp.sessions[task.n-1]=Object.assign({},out,{n:task.n})}
  else if(task.phase==="devotionals"){(out.devotionals||[]).forEach((d,k)=>{camp.devotionals[(task.n-1)*5+k]=Object.assign({},d,{d:(task.n-1)*5+k+1})})}
  else if(task.phase==="sermons"){(out.sermons||[]).forEach((s,k)=>{const n=task.n+k;camp.sermons[n-1]=Object.assign({},s,{n})})}
  else if(task.phase==="kit"){KITKEYS.forEach(k=>{if(out[k])camp.kit[k][task.n-1]=Object.assign({},out[k],{w:task.n})})}
  else if(task.phase==="completions"){camp.completions[task.comp]=out[task.comp]||[]}
  return camp;
}

/* ---------------- verification (the spec's "verify before you output") ---------------- */
function verify(camp){
  const W=camp.meta.weeks,D=camp.meta.days,issues=[];
  const filled=a=>a.filter(Boolean).length;
  if(filled(camp.sessions)!==W)issues.push(`sessions ${filled(camp.sessions)} of ${W}`);
  if(filled(camp.devotionals)!==D)issues.push(`devotional days ${filled(camp.devotionals)} of ${D}`);
  if(filled(camp.sermons)!==W)issues.push(`sermons ${filled(camp.sermons)} of ${W}`);
  KITKEYS.forEach(k=>{if(filled(camp.kit[k])!==W)issues.push(`kit.${k} ${filled(camp.kit[k])} of ${W}`)});
  Object.keys(camp.completions).forEach(k=>{if(!camp.completions[k]||!camp.completions[k].length)issues.push(`completion ${k} empty`)});
  camp.sessions.forEach((s,i)=>{if(!s)return;
    if((s.com||[]).length!==3)issues.push(`session ${i+1}: ${(s.com||[]).length} commentary paragraphs, expected 3`);
    if((s.Q||[]).length!==5)issues.push(`session ${i+1}: ${(s.Q||[]).length} questions, expected 5`);
    if((s.LN||[]).length!==2)issues.push(`session ${i+1}: ${(s.LN||[]).length} leader notes, expected 2`)});
  camp.sermons.forEach((m,i)=>{if(m&&(m.movements||[]).length!==3)issues.push(`sermon ${i+1}: ${(m.movements||[]).length} movements, expected 3`)});
  camp.devotionals.forEach((d,i)=>{if(d&&d.d!==i+1)issues.push(`devotional numbering drift at day ${i+1}`)});
  // sermon titles must differ from session titles
  camp.sermons.forEach((m,i)=>{const s=camp.sessions[i];
    if(m&&s&&m.t&&s.t&&m.t.trim().toLowerCase()===s.t.trim().toLowerCase())issues.push(`sermon ${i+1} title repeats the session title`)});
  const BAN=/\b(journey|unpack|lean into|season of life|do life together)\b/i;
  const hits=[];
  JSON.stringify(camp).split(/","|":"/).forEach(chunk=>{const m=chunk.match(BAN);if(m&&hits.length<4)hits.push(m[0])});
  if(hits.length)issues.push(`banned voice words present: ${[...new Set(hits)].join(", ")}`);
  return issues;
}

/* ---------------- exports ---------------- */
function esc(s){return String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function toDoc(camp){
  const W=camp.meta.weeks;const P=[];
  P.push(`<h1>${esc(camp.meta.title)}</h1><p><i>${esc(camp.meta.subtitle)}</i></p><p>${W} sessions · ${camp.meta.days} devotional days${camp.meta.text?` · ${esc(camp.meta.text)}`:""}</p>`);
  P.push("<h2>Sessions</h2>");
  camp.sessions.forEach(s=>{if(!s)return;
    P.push(`<h3>Session ${s.n} — ${esc(s.t)}</h3><p><i>${esc(s.sub||"")} · ${esc(s.ref||"")}</i></p>
    <p><b>Big idea.</b> ${esc(s.big)}</p><p><b>Opening question.</b> ${esc(s.open)}</p>
    ${(s.com||[]).map(c=>`<p>${esc(c)}</p>`).join("")}
    <p><b>Formation questions.</b></p><ol>${(s.Q||[]).map(q=>`<li>${esc(q.q)}<br><i>Leader note: ${esc(q.note)}</i></li>`).join("")}</ol>
    <p><b>Application.</b> ${esc(s.app)}</p><p><b>Prayer.</b> ${esc(s.prayer)}</p>
    <p><b>Leader notes.</b> ${(s.LN||[]).map(esc).join(" ")}</p>`)});
  P.push("<h2>Devotionals</h2>");
  camp.devotionals.forEach(d=>{if(!d)return;
    P.push(`<h3>Day ${d.d} — ${esc(d.t)}</h3><p><i>${esc(d.ref)}</i></p><p>${esc(d.body)}</p><p><b>Question.</b> ${esc(d.q)}</p><p><b>Practice.</b> ${esc(d.practice)}</p>`)});
  P.push("<h2>Sermon outlines</h2>");
  camp.sermons.forEach(m=>{if(!m)return;
    P.push(`<h3>Week ${m.n} — ${esc(m.t)}</h3><p><i>${esc(m.ref)}</i></p><p><b>Big idea.</b> ${esc(m.big)}</p>
    <ol>${(m.movements||[]).map(x=>`<li>${esc(x)}</li>`).join("")}</ol><p><b>Call to action.</b> ${esc(m.cta)}</p>`)});
  const KL={family:"Family Edition",student:"Student Edition",video:"Video Script",leader:"Leader Guide",campaign:"Campaign Kit",kids:"Kids Curriculum",verses:"Memory Verse",testimony:"Testimony Prompt"};
  P.push("<h2>Campaign kit</h2>");
  KITKEYS.forEach(k=>{P.push(`<h3>${KL[k]}</h3>`);
    camp.kit[k].forEach(w=>{if(!w)return;
      P.push(`<p><b>Week ${w.w}.</b> `+Object.keys(w).filter(x=>x!=="w").map(x=>`<i>${x}:</i> ${esc(w[x])}`).join(" · ")+`</p>`)})});
  const CL={testimony_system:"Testimony capture system",callback:"The 90-day callback",host:"Host recruitment",measurement:"Measurement sheet",lengths:"Alternate lengths",access:"Translation & accessibility"};
  P.push("<h2>The completions</h2>");
  Object.keys(camp.completions).forEach(k=>{P.push(`<h3>${CL[k]||k}</h3>`);
    (camp.completions[k]||[]).forEach(r=>{
      P.push(r.metric?`<p><b>${esc(r.metric)}</b> — ${esc(r.when)} — ${esc(r.tells)}</p>`
        :r.t?`<p><b>${esc(r.t)}</b> (${esc(r.count)}) — keeps: ${esc(r.keeps)} — best for: ${esc(r.bestfor)}</p>`
        :`<p><b>${esc(r.l)}</b> — ${esc(r.v)}</p>`)})});
  return P.join("\n");
}

const SPEC={derive,parseBatch,plan,blank,merge,verify,toDoc,SYS,BATCH_CAP,KITKEYS};
if(typeof window!=="undefined")window.SPEC=SPEC;
if(typeof module!=="undefined"&&module.exports)module.exports=SPEC;
})();
