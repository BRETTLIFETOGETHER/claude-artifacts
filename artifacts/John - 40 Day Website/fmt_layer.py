import re
s = open('/home/claude/site/engine.js').read()
assert 'function bookFmt' not in s, "already applied"

NEW = r'''
/* ================= sixteen-format layer ================= */
function stripTags(h){ return String(h).replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim(); }
function firstPara(h){ var m=/<p>([\s\S]*?)<\/p>/.exec(h); return m?stripTags(m[1]):stripTags(h).slice(0,220); }

function bookFmt(C){
  var dev=devotional(C), r=rngFor(C[9],'book');
  var m={c:rot(KB[FAM_BY_CAT[C[2]]].concepts,0), t:C[0], ap:audPhrase(C), th:C[10]};
  var byPart={}, order=[];
  dev.days.forEach(function(d){ if(!byPart[d.wk]){byPart[d.wk]=[];order.push(d.wk);} byPart[d.wk].push(d); });
  var chapters=order.map(function(w,i){
    var ri=rngFor(C[9],'bkch'+i);
    return { n:i+1, title:w.replace(/^Part \d+ \u00b7 /,''),
      intro:gOpen(ri,m)+" "+gTruth(ri,m),
      sections:byPart[w].map(function(d){ return {h:d.title, scr:d.scr, body:d.body}; }) };
  });
  var words=dev.days.reduce(function(a,d){return a+stripTags(d.body).split(' ').length;},0);
  return { kind:'Book', title:C[0], sub:C[1]||'', author:'The Lifetogether Team',
    howto:"Read one section a day, or a chapter a week with a pen nearby. "+gTruth(r,m)+" "+gStepCore(r,m,true),
    chapters:chapters,
    epilogue:gPromise(r,C[0],C[1],m.c)+" "+gClose(r,m,dev.days.length)+" "+gCarry(r,dev.days.length),
    pagesEst:Math.round(words/280)+8 };
}

function courseFmt(C){
  var dev=devotional(C), gs=groupStudy(C);
  var m={c:rot(KB[FAM_BY_CAT[C[2]]].concepts,1), t:C[0], ap:audPhrase(C), th:C[10]};
  var byPart={}, order=[];
  dev.days.forEach(function(d){ if(!byPart[d.wk]){byPart[d.wk]=[];order.push(d.wk);} byPart[d.wk].push(d); });
  var modules=order.map(function(w,i){
    var r=rngFor(C[9],'crs'+i);
    var lessons=byPart[w].map(function(d){ return {t:d.title, key:firstPara(d.body), scr:d.scr}; });
    return { n:i+1, title:w.replace(/^Part \d+ \u00b7 /,''),
      objectives:[ "Name where "+m.c+" is currently thin in your ordinary week.",
                   "Trace what Scripture in this module actually claims about "+m.c+".",
                   "Practice one measurable act of "+m.c+" before the module closes." ].map(function(o,oi){ var ro=rngFor(C[9],'obj'+i+'-'+oi); return pk(ro,["","By the end of this module you will be able to ",""]) ? o : o; }),
      lessons:lessons,
      quiz:[gQuestion(r,m),gQuestion(r,m),gQuestion(r,m)],
      challenge:gPractice(r,m) };
  });
  return { kind:'Membership Course', title:C[0]+" \u2014 The Course", sub:C[1]||'', modules:modules,
    completion:"Members who finish all "+modules.length+" modules receive the "+C[0]+" completion certificate and the alumni discussion track." };
}

function leaderTrainingFmt(C){
  var gs=groupStudy(C);
  var m={c:rot(KB[FAM_BY_CAT[C[2]]].concepts,2), t:C[0], ap:'your group', th:C[10]};
  var names=["Before You Launch","Leading the Room","Shepherding the Middle Weeks","Landing the Plane"];
  var mods=names.map(function(nm,i){
    var r=rngFor(C[9],'lt'+i);
    var tipLead=pk(r,["The best facilitators of "+C[0]+" ","Groups rise to the level of their questions, so ","Your job is temperature, not content, which means ","Silence is a tool here; ","Nobody joins a group to be lectured, so "]);
    var tipCore=pk(r,["ask, wait a full seven seconds, and then wait three more.","let the readings do the heavy lifting and keep your own airtime under a quarter.","open with the easiest honest question and save the deep one for minute forty.","name the quiet person kindly and hand them the second question, never the first.","end five minutes early on purpose; people remember rooms that respected them.","text one member midweek about one thing they said; retention is pastoral, not procedural."]);
    var tipTail=pk(r,[" Trust the process across all "+gs.sessions.length+" sessions."," That single habit changes the whole journey."," Do this weekly and the room will start doing it for you."," It is small, repeatable, and it works."]);
    return { n:i+1, title:nm,
      aims:["Know exactly what session "+(Math.min(i*2+1,gs.sessions.length))+" of "+C[0]+" is trying to produce","Handle the two moments most likely to stall a room","Leave with one practice you will use this week"],
      note:tipLead+tipCore+tipTail,
      practice:gPractice(r,m) };
  });
  return { kind:'Leader Training', title:C[0]+" \u2014 Facilitator Course", sessions:gs.sessions.map(function(x){return x.title;}), modules:mods,
    promise:"Forty minutes of training now saves forty awkward minutes every week of the journey." };
}

function familyFmt(C){
  var dev=devotional(C);
  var m={c:rot(KB[FAM_BY_CAT[C[2]]].concepts,3), t:C[0], ap:'your home', th:C[10]};
  var weeks=[]; var seen={};
  dev.days.forEach(function(d,i){ var w=Math.floor(i/7); if(!seen[w]){seen[w]=true; weeks.push({i:w, mem:d.mem});} });
  var out=weeks.map(function(w){
    var r=rngFor(C[9],'famw'+w.i);
    var actLead=pk(r,["Around the table this week, ","One evening this week, ","On the fridge this week: ","Pick a night and ","Before Sunday, "]);
    var actCore=pk(r,["build a family list of places you spotted "+m.c+" and read it out loud on Sunday.","let the youngest pick one act of "+m.c+" the whole house does together.","write the memory verse on the mirror and say it together at breakfast.","cook one meal as a team and pray one sentence each before eating.","take a walk and let everyone name one thing they are thankful for per block.","have each person secretly serve one other person in the house, then guess who at week\u2019s end."]);
    var debrief=pk(r,[" Debrief with one question: where did it feel easiest, and hardest?"," Close by asking what surprised everyone."," No lecture after; the doing is the lesson."," Let the kids grade the grown-ups, kindly."]);
    var pr=(function(){ var rr=rngFor(C[9],'famp'+w.i);
      return pk(rr,["Father,","Lord,","God,"])+" "+pk(rr,["thank You for this family, exactly as it is today.","thank You for our table and everyone around it."])+" "+pk(rr,["Grow "+m.c+" in our home this week.","Help each of us practice "+m.c+" where we live."])+" "+pk(rr,["Amen.","In Jesus\u2019 name, amen."]); })();
    return { week:w.i+1, verse:w.mem, tableTalk:[gQuestion(r,m),gQuestion(r,m)], activity:actLead+actCore+debrief, prayer:pr,
      blessing:"Speak this over each child at bedtime once this week: \u201CYou are loved, you are Ours and God\u2019s, and "+m.c+" looks good on you.\u201D" };
  });
  return { kind:'Family Guide', title:C[0]+" \u2014 Family Guide", weeks:out,
    note:"Ten relaxed minutes, a few nights a week. The guide follows the same journey the adults are reading, so the whole house is in one story." };
}

function podcastFmt(C){
  var dev=devotional(C), gs=groupStudy(C);
  var m={c:rot(KB[FAM_BY_CAT[C[2]]].concepts,4), t:C[0], ap:'your week', th:C[10]};
  var eps=gs.sessions.map(function(sx,i){
    var r=rngFor(C[9],'pod'+i);
    var day=dev.days[Math.min(i*7,dev.days.length-1)];
    return { ep:i+1, title:sx.title,
      coldOpen:gHook(r,m),
      segments:[
        {h:'Scripture moment', body:'Read '+day.scr+' slowly on air; let it sit for two beats before commentary.'},
        {h:'The conversation', body:gQuestion(r,m)+' '+gQuestion(r,m)},
        {h:'A story from the road', body:gStory(r)},
        {h:'This week\u2019s move', body:gStep(r,m)}
      ],
      outro:pk(r,["Same feed, next week: ","We pick the road back up next episode with ","Do not miss the next stretch: "]) + (gs.sessions[i+1]?gs.sessions[i+1].title:"the Celebration episode") + ". "+gCarry(r,(i+1)*7),
      runtime:'22\u201328 min' };
  });
  return { kind:'Podcast Series', title:C[0]+" \u2014 The Podcast", trailer:{ title:'Trailer', script:gPromise(rngFor(C[9],'podT'),C[0],C[1],m.c)+" Subscribe and walk the whole journey with us." }, episodes:eps };
}

function videoCourseFmt(C){
  var gs=groupStudy(C);
  var m={c:rot(KB[FAM_BY_CAT[C[2]]].concepts,5), t:C[0], ap:'this room', th:C[10]};
  var lessons=gs.sessions.map(function(sx,i){
    var r=rngFor(C[9],'vid'+i);
    return { n:i+1, title:sx.title,
      lowerThirds:(sx.movements||[]).slice(0,3).map(function(mv){return mv.t||mv.title||sx.title;}),
      beats:[
        {b:'Open (0:00\u20131:30)', s:gHook(r,m)},
        {b:'Teach (1:30\u201310:00)', s:gTruth(r,m)+' '+gTruth(r,m)+' '+gApply(r,m)},
        {b:'Story (10:00\u201313:00)', s:gStory(r)},
        {b:'Send (13:00\u201315:00)', s:gStep(r,m)+' '+gClose(r,m,(i+1)*7)}
      ],
      runtime:'12\u201315 min' };
  });
  return { kind:'Video Course', title:C[0]+" \u2014 On Video", lessons:lessons,
    production:"Shot as direct-to-camera teaching with two b-roll passes; scripts below are delivery-ready and match the group study beat for beat." };
}

function podFmt(C){
  var dev=devotional(C), r=rngFor(C[9],'pod-print');
  var m={c:rot(KB[FAM_BY_CAT[C[2]]].concepts,6), t:C[0], ap:'your church', th:C[10]};
  var words=dev.days.reduce(function(a,d){return a+stripTags(d.body).split(' ').length;},0);
  var pages=Math.round(words/280)+12;
  return { kind:'Print-on-Demand', title:C[0],
    trim:'5.5\u2033 \u00d7 8.5\u2033 trade paperback', pages:pages, paper:'60# cream, perfect bound', cover:'Matte softcover',
    interior:['Title page','Welcome & how to use','Memory verse index',dev.days.length+' daily readings','Group discussion appendix','Notes pages'],
    backCover:gPromise(r,C[0],C[1],m.c)+" "+gTruth(r,m)+" One book, one church, one journey \u2014 congregation-wide print rights included.",
    note:'Upload-ready spec for KDP, IngramSpark, or your local printer; per-unit cost at this page count typically lands between $2.85 and $4.10.' };
}

function libraryFmt(C){
  var keys=FORMAT_KEYS.filter(function(k){return k!=='Digital Library';});
  var slug=C[0].toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
  return { kind:'Digital Library', title:C[0]+" \u2014 Complete Digital Library",
    items:keys.map(function(k){ return {format:k, file:slug+'-'+k.toLowerCase().replace(/[^a-z0-9]+/g,'-')+'.pdf'}; }),
    license:'One church license covers every file: print, project, email, and adapt inside your congregation.',
    delivery:'All files unlock in your account immediately after checkout and stay in your library.' };
}

var FORMAT_KEYS=['Book','Devotional','7-Day Experience','21-Day Challenge','30-Day Journey','40-Day Campaign','Membership Course','Small Group Curriculum','Leader Training','Family Guide','Youth Edition','Children\u2019s Edition','Podcast Series','Video Course','Print-on-Demand','Digital Library'];

function formatFor(C,key){
  switch(key){
    case 'Book': return bookFmt(C);
    case 'Devotional': return devotional(C);
    case '7-Day Experience': return devotional(C,'7-Day');
    case '21-Day Challenge': return devotional(C,'21-Day');
    case '30-Day Journey': return devotional(C,'30-Day');
    case '40-Day Campaign': return devotional(C,'40-Day');
    case 'Membership Course': return courseFmt(C);
    case 'Small Group Curriculum': return groupStudy(C);
    case 'Leader Training': return leaderTrainingFmt(C);
    case 'Family Guide': return familyFmt(C);
    case 'Youth Edition': return youth(C);
    case 'Children\u2019s Edition': return children(C);
    case 'Podcast Series': return podcastFmt(C);
    case 'Video Course': return videoCourseFmt(C);
    case 'Print-on-Demand': return podFmt(C);
    case 'Digital Library': return libraryFmt(C);
  }
  return devotional(C);
}
'''

i = s.index('window.Engine={')
s = s[:i] + NEW + '\n' + s[i:]
s = s.replace('window.Engine={ get:get,', 'window.Engine={ get:get, format:formatFor, FORMAT_KEYS:FORMAT_KEYS, book:bookFmt, course:courseFmt, leaderTraining:leaderTrainingFmt, family:familyFmt, podcast:podcastFmt, videoCourse:videoCourseFmt, printOnDemand:podFmt, library:libraryFmt,')
open('/home/claude/site/engine.js','w').write(s)
print("format layer installed")
