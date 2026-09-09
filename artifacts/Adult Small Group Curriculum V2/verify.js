const { sessions } = require('./content.js');
const { more } = require('./sessions2to6.js');
const all = sessions.concat(more);

let problems = [];
function check(cond, msg) { if (!cond) problems.push(msg); }

all.forEach(s => {
  const S = `S${s.n}`;
  check(!!s.question && !!s.subtitle, `${S}: header missing`);
  check(!!s.memoryVerse && !!s.memoryRef, `${S}: memory verse missing`);
  check(typeof s.intro === 'string' && s.intro.length > 40, `${S}: intro missing`);
  // opening story
  check(s.story && s.story.label && s.story.subtitle, `${S}: story label/subtitle missing`);
  check(s.story && s.story.paras && s.story.paras.length === 3, `${S}: story should have 3 paragraphs, has ${s.story?.paras?.length}`);
  check(s.story && !!s.story.quote, `${S}: story pull-quote missing`);
  // come together
  check(s.comeTogether && s.comeTogether.prayerPara && s.comeTogether.tonePara, `${S}: come together paragraphs missing`);
  check(s.comeTogether && s.comeTogether.discuss && s.comeTogether.discuss.length === 2, `${S}: come together needs 2 discuss questions, has ${s.comeTogether?.discuss?.length}`);
  // building only S1
  if (s.n === 1) check(!!s.building, `S1: building block required`);
  else check(!s.building, `${S}: building block should be absent`);
  // learn: 6 blanks
  check(s.learn && s.learn.listenPara, `${S}: learn listen paragraph missing`);
  check(s.learn && s.learn.blanks && s.learn.blanks.length === 6, `${S}: learn needs 6 blanks, has ${s.learn?.blanks?.length}`);
  s.learn.blanks.forEach((b, i) => check(b.includes('________'), `${S}: blank ${i+1} has no underscore blank`));
  // grow: 7 questions, practices >=1, mostAbsent
  check(s.grow && s.grow.questions && s.grow.questions.length === 7, `${S}: grow needs 7 questions, has ${s.grow?.questions?.length}`);
  const devoRef = s.grow.questions.some(q => /devotional/i.test(q));
  check(devoRef, `${S}: grow needs at least one question referencing the devotional`);
  check(s.grow && s.grow.practices && s.grow.practices.length >= 1, `${S}: grow practices missing`);
  check(s.grow && /most absent/i.test(s.grow.mostAbsent || ''), `${S}: grow missing 'most absent' closer`);
  // exercise: name, quietLine, table, circleLine, finishSentence, selfCheck w/ two blanks
  check(s.exercise && s.exercise.name, `${S}: exercise name missing`);
  check(s.exercise && /read it aloud/i.test(s.exercise.quietLine || ''), `${S}: exercise 'do quietly' line missing`);
  check(s.exercise && s.exercise.table && s.exercise.table.headers && s.exercise.table.rows && s.exercise.table.rows.length >= 3, `${S}: exercise table missing/too small`);
  check(s.exercise && !!s.exercise.circleLine, `${S}: exercise circle line missing`);
  check(s.exercise && !!s.exercise.finishSentence, `${S}: exercise finish sentence missing`);
  const blanksInSelf = (s.exercise.selfCheck.match(/___/g) || []).length;
  check(s.exercise && /\(private\)/.test(s.exercise.selfCheck || ''), `${S}: self-check not marked private`);
  check(blanksInSelf >= 2, `${S}: self-check needs two blanks, has ${blanksInSelf}`);
  // next steps 3
  check(s.nextSteps && s.nextSteps.length === 3, `${S}: needs 3 next steps, has ${s.nextSteps?.length}`);
  // family intro + 3
  check(s.family && s.family.intro && s.family.questions && s.family.questions.length === 3, `${S}: family needs intro + 3 questions`);
  // going deeper: 2 reads x 3
  check(s.goingDeeper && s.goingDeeper.reads && s.goingDeeper.reads.length === 2, `${S}: going deeper needs 2 reads`);
  s.goingDeeper.reads.forEach((r, i) => {
    check(/^READ /.test(r.ref), `${S}: read ${i+1} ref should start with READ`);
    check(r.qs && r.qs.length === 3, `${S}: read ${i+1} needs 3 questions, has ${r.qs?.length}`);
  });
  // readings: week header + 7 days each 5 fields
  check(s.readings && s.readings.weekHeader, `${S}: readings week header missing`);
  check(s.readings && s.readings.days && s.readings.days.length === 7, `${S}: readings need 7 days, has ${s.readings?.days?.length}`);
  s.readings.days.forEach((d, i) => check(d.length === 5, `${S}: reading day ${i+1} needs 5 fields (title,subtitle,ref,verse,respond), has ${d.length}`));
  // close 2 paras
  check(s.close && s.close.p1 && s.close.p2, `${S}: close needs 2 paragraphs`);
  // no em-dashes in prose fields
  const proseBlob = [s.intro, ...s.story.paras, s.comeTogether.prayerPara, s.comeTogether.tonePara, ...s.grow.questions, s.close.p1, s.close.p2].join(' ');
  check(!proseBlob.includes('\u2014'), `${S}: em-dash found in prose`);
});

if (problems.length === 0) {
  console.log('PASS — all six sessions conform to the locked spec.');
} else {
  console.log('FAIL — ' + problems.length + ' issue(s):');
  problems.forEach(p => console.log('  - ' + p));
  process.exit(1);
}
