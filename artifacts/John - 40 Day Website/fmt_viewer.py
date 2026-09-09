import re
s = open('/home/claude/site/curriculum.html').read()

# 1) chips: two-tier format list
old = "const FMTS=['40-Day','30-Day','21-Day','7-Day','6-Week','Youth','Kids','Leader Kit'];"
assert old in s
new = ("const LENGTHS=['40-Day','30-Day','21-Day','7-Day'];\n"
       "const FMTS=[...LENGTHS,'6-Week','Youth','Kids','Leader Kit','Book','Course','Leader Training','Family Guide','Podcast','Video Course','Print-on-Demand','Digital Library'];")
s = s.replace(old, new)

# 2) renderers: insert before the Leader Kit branch's closing else-chain end. Find 'else if(fmt===\'Leader Kit\')' block end by anchoring on the final `}` before NOTICE append? Safer: append new branches right after the Kids branch closing. Anchor on the Leader Kit branch start and insert BEFORE it new branches.
anchor = "else if(fmt==='Leader Kit'){"
assert anchor in s
branches = r'''else if(fmt==='Book'){
  const bk=Engine.book(C);
  h=cover('The Book \u00b7 '+bk.pagesEst+' pages');
  h+=`<div class="se"><div class="lbl">How to read this book</div><p>${bk.howto}</p></div>`;
  bk.chapters.forEach(ch=>{
    h+=`<div class="day"><div class="dn">CHAPTER ${ch.n}</div><h2>${ch.title}</h2><p><em>${ch.intro}</em></p>`;
    ch.sections.forEach(sec=>{ h+=`<h3 style="margin:16px 0 4px">${sec.h}</h3><div class="scrx" style="margin-bottom:6px">${sec.scr}</div>${sec.body}`; });
    h+=`</div>`;
  });
  h+=`<div class="se"><div class="lbl">Epilogue</div><p>${bk.epilogue}</p></div>`;
}
else if(fmt==='Course'){
  const cr=Engine.course(C);
  h=cover('Membership Course \u00b7 '+cr.modules.length+' modules');
  cr.modules.forEach(md=>{
    h+=`<div class="day"><div class="dn">MODULE ${md.n}</div><h2>${md.title}</h2>
    <div class="lbl">You will</div><ul class="plain">${md.objectives.map(o=>`<li>${o}</li>`).join('')}</ul>
    <div class="lbl">Lessons</div><ul class="plain">${md.lessons.map(l=>`<li><b>${l.t}</b> \u00b7 ${l.scr}<br><span style="color:#5E5E6B">${l.key}</span></li>`).join('')}</ul>
    <div class="lbl">Check yourself</div><ol>${md.quiz.map(q=>`<li>${q}</li>`).join('')}</ol>
    <div class="lbl">Module challenge</div><p>${md.challenge}</p></div>`;
  });
  h+=`<div class="se"><p>${cr.completion}</p></div>`;
}
else if(fmt==='Leader Training'){
  const lt=Engine.leaderTraining(C);
  h=cover('Facilitator Course');
  h+=`<div class="se"><div class="lbl">The sessions you will lead</div><ul class="plain">${lt.sessions.map((t,i)=>`<li>Session ${i+1} \u2014 ${t}</li>`).join('')}</ul><p><em>${lt.promise}</em></p></div>`;
  lt.modules.forEach(md=>{
    h+=`<div class="day"><div class="dn">TRAINING ${md.n}</div><h2>${md.title}</h2>
    <div class="lbl">Aims</div><ul class="plain">${md.aims.map(a=>`<li>${a}</li>`).join('')}</ul>
    <div class="lbl">Field note</div><p>${md.note}</p>
    <div class="lbl">Your practice</div><p>${md.practice}</p></div>`;
  });
}
else if(fmt==='Family Guide'){
  const fg=Engine.family(C);
  h=cover('Family Guide');
  h+=`<div class="se"><p>${fg.note}</p></div>`;
  fg.weeks.forEach(w=>{
    h+=`<div class="day"><div class="dn">WEEK ${w.week}</div><h2>Around the table</h2>
    <div class="lbl">Memory verse</div><p>\u201C${w.verse.v}\u201D \u2014 ${w.verse.ref} (KJV)</p>
    <div class="lbl">Table talk</div><ol><li>${w.tableTalk[0]}</li><li>${w.tableTalk[1]}</li></ol>
    <div class="lbl">This week\u2019s activity</div><p>${w.activity}</p>
    <div class="lbl">Family prayer</div><p>${w.prayer}</p>
    <div class="lbl">Bedtime blessing</div><p>${w.blessing}</p></div>`;
  });
}
else if(fmt==='Podcast'){
  const pc=Engine.podcast(C);
  h=cover('Podcast Series \u00b7 '+pc.episodes.length+' episodes');
  h+=`<div class="se"><div class="lbl">Trailer</div><p>${pc.trailer.script}</p></div>`;
  pc.episodes.forEach(ep=>{
    h+=`<div class="day"><div class="dn">EPISODE ${ep.ep} \u00b7 ${ep.runtime}</div><h2>${ep.title}</h2>
    <div class="lbl">Cold open</div><p>${ep.coldOpen}</p>
    ${ep.segments.map(sg=>`<div class="lbl">${sg.h}</div><p>${sg.body}</p>`).join('')}
    <div class="lbl">Outro</div><p>${ep.outro}</p></div>`;
  });
}
else if(fmt==='Video Course'){
  const vc=Engine.videoCourse(C);
  h=cover('Video Course \u00b7 '+vc.lessons.length+' lessons');
  h+=`<div class="se"><p>${vc.production}</p></div>`;
  vc.lessons.forEach(ls=>{
    h+=`<div class="day"><div class="dn">LESSON ${ls.n} \u00b7 ${ls.runtime}</div><h2>${ls.title}</h2>
    ${ls.lowerThirds.length?`<div class="lbl">Lower thirds</div><ul class="plain">${ls.lowerThirds.map(x=>`<li>${x}</li>`).join('')}</ul>`:''}
    ${ls.beats.map(b=>`<div class="lbl">${b.b}</div><p>${b.s}</p>`).join('')}</div>`;
  });
}
else if(fmt==='Print-on-Demand'){
  const pd=Engine.printOnDemand(C);
  h=cover('Print-on-Demand Edition');
  h+=`<div class="se"><div class="lbl">Specification</div><ul class="plain">
    <li><b>Trim</b> \u00b7 ${pd.trim}</li><li><b>Pages</b> \u00b7 ${pd.pages}</li><li><b>Paper</b> \u00b7 ${pd.paper}</li><li><b>Cover</b> \u00b7 ${pd.cover}</li></ul>
  <div class="lbl">Interior order</div><ol>${pd.interior.map(x=>`<li>${x}</li>`).join('')}</ol>
  <div class="lbl">Back-cover copy</div><p>${pd.backCover}</p>
  <p><em>${pd.note}</em></p></div>`;
}
else if(fmt==='Digital Library'){
  const dl=Engine.library(C);
  h=cover('Complete Digital Library');
  h+=`<div class="se"><div class="lbl">Every file in this campaign</div><ul class="plain">${dl.items.map(it=>`<li><b>${it.format}</b> \u00b7 <span style="color:#5E5E6B">${it.file}</span></li>`).join('')}</ul>
  <p>${dl.license}</p><p><em>${dl.delivery}</em></p></div>`;
}
'''
s = s.replace(anchor, branches + anchor)
open('/home/claude/site/curriculum.html','w').write(s)
print("curriculum viewer: 8 new renderers + chips")
