const fs = require('fs');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync('/mnt/user-data/outputs/purpose-built-business.html', 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously' });
const doc = dom.window.document;
const win = dom.window;

let pass = 0, fail = 0;
function t(name, cond) {
  if (cond) { pass++; console.log('PASS  ' + name); }
  else { fail++; console.log('FAIL  ' + name); }
}
function click(el) { el.dispatchEvent(new win.Event('click', { bubbles: true })); }

// ---------- structure ----------
t('01 loads, title set', doc.title.indexOf('Purpose Built Business') === 0);
t('02 eleven nav anchors, all targets exist', (function(){
  const links = doc.querySelectorAll('nav a');
  if (links.length !== 11) return false;
  let ok = true;
  links.forEach(a => { const id = a.getAttribute('href').slice(1); if (!doc.getElementById(id)) ok = false; });
  return ok;
})());
t('03 hero: four stats, both CTAs, internal chip', doc.querySelectorAll('.stat').length === 4 && doc.querySelectorAll('.hero .btn').length === 2 && doc.querySelector('.chipline').textContent.indexOf('remove before external use') > -1);
t('04 frameworks: five purposes and six criteria', (function(){
  const p = doc.querySelectorAll('.pgrid.two .pnl');
  return p[0].querySelectorAll('.frow').length === 5 && p[1].querySelectorAll('.frow').length === 6 && p[1].textContent.indexOf('Across Generations') > -1;
})());

// ---------- instrument 1: diagnostic ----------
t('05 diagnostic: 12 questions, 48 options', doc.querySelectorAll('#diagnostic .qblock').length === 12 && doc.querySelectorAll('#diagnostic .opt').length === 48);
click(doc.querySelector('.opt[data-q="0"][data-val="4"]'));
t('06 pick updates score', doc.getElementById('d-score').textContent === '4' && doc.getElementById('d-prog').textContent === '1 of 12 answered');
click(doc.querySelector('.opt[data-q="0"][data-val="1"]'));
t('07 re-pick replaces', doc.getElementById('d-score').textContent === '1');
for (let q = 0; q < 12; q++) click(doc.querySelector('.opt[data-q="' + q + '"][data-val="4"]'));
t('08 full max 48, top band shown', doc.getElementById('d-score').textContent === '48' && doc.getElementById('d-band-name').textContent === 'Purpose Built' && doc.getElementById('d-band').style.display === 'block');
const b = win.pbbBand;
t('09 diagnostic band boundaries and coverage', (function(){
  if (!(b(14)[2] === 'Well-Run, Unformed' && b(15)[2] === 'Values on the Wall' && b(26)[2] === 'Values on the Wall' && b(27)[2] === 'Formation Underway' && b(38)[2] === 'Formation Underway' && b(39)[2] === 'Purpose Built')) return false;
  for (let s = 0; s <= 48; s++) { if (!b(s)) return false; }
  return true;
})());
win.pbbDReset();
t('10 diagnostic reset', doc.getElementById('d-score').textContent === '0' && doc.querySelectorAll('#diagnostic .opt.sel').length === 0);

// ---------- instrument 2: flourishing ----------
t('11 flourishing: 24 statements, 120 buttons, 6 dims', doc.querySelectorAll('.stmt').length === 24 && doc.querySelectorAll('.rbtn').length === 120 && doc.querySelectorAll('.dimhead').length === 6);
click(doc.querySelector('.rbtn[data-q="0"][data-val="3"]'));
click(doc.querySelector('.rbtn[data-q="1"][data-val="5"]'));
click(doc.querySelector('.rbtn[data-q="2"][data-val="5"]'));
click(doc.querySelector('.rbtn[data-q="3"][data-val="5"]'));
t('12 dimension subtotal at four answered (18/20)', doc.getElementById('fsub-0').textContent === '18 / 20');
for (let q = 0; q < 24; q++) click(doc.querySelector('.rbtn[data-q="' + q + '"][data-val="5"]'));
t('13 all fives: 120, top band, subtotals 20/20', (function(){
  if (doc.getElementById('f-score').textContent !== '120') return false;
  if (doc.getElementById('f-band-name').textContent !== 'A Flourishing Workplace') return false;
  for (let d = 0; d < 6; d++) { if (doc.getElementById('fsub-' + d).textContent !== '20 / 20') return false; }
  return true;
})());
const fb = win.pbbFlourBand;
t('14 flourishing band boundaries and coverage 24-120', (function(){
  if (!(fb(59)[2] === 'Begin with Trust and Purpose' && fb(60)[2] === 'Foundations Forming' && fb(83)[2] === 'Foundations Forming' && fb(84)[2] === 'Emerging Flourishing Culture' && fb(104)[2] === 'Emerging Flourishing Culture' && fb(105)[2] === 'A Flourishing Workplace')) return false;
  for (let s = 24; s <= 120; s++) { if (!fb(s)) return false; }
  return true;
})());
win.pbbFReset();
t('15 flourishing reset', doc.getElementById('f-score').textContent === '0' && doc.querySelectorAll('.rbtn.sel').length === 0);

// ---------- seats + peer ----------
t('16 three seats switch; peer group ten studies with Scripture', (function(){
  if (doc.querySelectorAll('.seatbtn').length < 3) return false;
  click(doc.getElementById('seatbtn-team'));
  const seatOk = doc.getElementById('seat-team').className.indexOf('on') > -1 && doc.getElementById('seat-owner').className.indexOf('on') === -1;
  const rows = doc.querySelectorAll('#seats .dirrow');
  return seatOk && rows.length === 10 && rows[0].textContent.indexOf('Proverbs 27:17') > -1 && rows[9].textContent.indexOf('Psalm 78') > -1;
})());

// ---------- launch ----------
t('17 launch: two doors, church default', (function(){
  const btns = doc.querySelectorAll('[id^="doorbtn-"]');
  return btns.length === 2 && doc.getElementById('door-church').className.indexOf('on') > -1 && doc.getElementById('door-work').className.indexOf('on') === -1;
})());
t('18 church launch: six phases, each expandable with steps', (function(){
  const accs = doc.querySelectorAll('#door-church .acc');
  if (accs.length !== 6) return false;
  click(accs[0].querySelector('.ahead'));
  if (accs[0].className.indexOf('open') === -1) return false;
  return accs[0].querySelectorAll('.stepli').length === 4 && accs[0].textContent.indexOf('senior pastor owns the why') > -1;
})());
t('19 church launch carries the no-ask and shepherding rules', doc.getElementById('door-church').textContent.indexOf('ninety days minimum') > -1 && doc.getElementById('door-church').textContent.indexOf('never sales intelligence') > -1);
t('20 door switch reveals workplace, hides church', (function(){
  click(doc.getElementById('doorbtn-work'));
  return doc.getElementById('door-work').className.indexOf('on') > -1 && doc.getElementById('door-church').className.indexOf('on') === -1;
})());
t('21 workplace launch: six phases, guardrails include voluntary + values-default + HR', (function(){
  const wp = doc.getElementById('door-work');
  const accs = wp.querySelectorAll('.acc');
  if (accs.length !== 6) return false;
  const txt = wp.textContent;
  const guards = wp.querySelectorAll('.pnl.alt2 .stepli').length === 5;
  return guards && txt.indexOf('voluntary, always') > -1 && txt.indexOf('never a requirement') > -1 && txt.indexOf('HR counsel') > -1 && txt.indexOf('smallest yes') > -1;
})());

// ---------- journeys ----------
t('22 four journeys render with price bands', (function(){
  const js = doc.querySelectorAll('#journeys .acc');
  return js.length === 4 && doc.getElementById('j40').textContent.indexOf('$18,000\u2013$60,000') > -1 && doc.getElementById('j10').textContent.indexOf('$4,500\u2013$12,000') > -1;
})());
function dayCount(id) { return doc.getElementById(id).querySelectorAll('.dayli').length; }
t('23 journey day-count integrity: 10 / 21 / 30 / 40', dayCount('j10') === 10 && dayCount('j21') === 21 && dayCount('j30') === 30 && dayCount('j40') === 40);
t('24 30-day journey opens: six Flourishing weeks, Day 30 is the Flourishing Commitment', (function(){
  const j = doc.getElementById('j30');
  click(j.querySelector('.ahead'));
  if (j.className.indexOf('open') === -1) return false;
  const weeks = j.querySelectorAll('.jweek');
  const days = j.querySelectorAll('.dayli');
  return weeks.length === 6 && days[29].textContent.indexOf('Day 30') > -1 && days[29].textContent.indexOf('The Flourishing Commitment') > -1;
})());
t('25 40-day flagship: eight weeks, purposes as weeks 2-6, Day 40 Commissioning Day', (function(){
  const j = doc.getElementById('j40');
  const weeks = j.querySelectorAll('.jweek');
  const days = j.querySelectorAll('.dayli');
  const txt = j.textContent;
  return weeks.length === 8 && txt.indexOf('Worship') > -1 && txt.indexOf('Mission') > -1 && days[39].textContent.indexOf('Day 40') > -1 && days[39].textContent.indexOf('Commissioning Day') > -1;
})());
t('26 21-day: capstone Day 21 commitment; workday rhythm stated in intro', (function(){
  const j = doc.getElementById('j21');
  const days = j.querySelectorAll('.dayli');
  return days[20].textContent.indexOf('Day 21') > -1 && doc.getElementById('journeys').textContent.indexOf('Forty days is eight working weeks') > -1;
})());
t('27 roster: ten rows pulled over, statuses honest', (function(){
  const jn = doc.getElementById('journeys');
  const rows = jn.querySelectorAll('.dirrow');
  const txt = jn.textContent;
  return rows.length === 10 && txt.indexOf('40 Days of Movement') > -1 && txt.indexOf('Prospective concept') > -1 && txt.indexOf('Rights pending') > -1 && txt.indexOf('Monday Is the Mission Field') > -1 && txt.indexOf('front row, not the building') > -1;
})());

// ---------- library / pricing ----------
t('28 library: seven parts, twenty verticals, honest math', (function(){
  const lib = doc.getElementById('library');
  return lib.querySelectorAll('.dirrow').length === 7 && lib.querySelectorAll('.chips')[1].querySelectorAll('.chip').length === 20 && lib.textContent.indexOf('165 categories') > -1;
})());
t('29 pricing: four tiers, five models, subscription primary', (function(){
  const p = doc.getElementById('pricing');
  return p.querySelectorAll('.tierrow').length === 4 && p.querySelectorAll('.dirrow').length === 5 && p.textContent.indexOf('$28,000') > -1;
})());

// ---------- founding 25 ----------
t('30 founding: three-paragraph argument, five gives, four asks, honest math', (function(){
  const f = doc.getElementById('founding');
  const gives = f.querySelectorAll('.pgrid.two .pnl')[0].querySelectorAll('.stepli').length === 5;
  const asks = f.querySelectorAll('.pgrid.two .pnl')[1].querySelectorAll('.stepli').length === 4;
  const txt = f.textContent;
  return f.querySelectorAll('.prose p').length === 3 && gives && asks && txt.indexOf('$9,000') > -1 && txt.indexOf('does not fund a business') > -1 && txt.indexOf('only if it is working, never as a condition') > -1;
})());
t('31 edition toggle: faith default shows Devotion; values swap shows Identity and hides faith', (function(){
  const faithOn = doc.getElementById('ed-faith').className.indexOf('on') > -1;
  const devotion = doc.getElementById('ed-faith').textContent.indexOf('Excellence as Devotion') > -1;
  click(doc.getElementById('edbtn-values'));
  const valuesOn = doc.getElementById('ed-values').className.indexOf('on') > -1 && doc.getElementById('ed-faith').className.indexOf('on') === -1;
  const identity = doc.getElementById('ed-values').textContent.indexOf('Excellence as Identity') > -1;
  const sameDays = doc.getElementById('ed-values').querySelectorAll('.dayli').length === 5 && doc.getElementById('ed-faith').querySelectorAll('.dayli').length === 5;
  return faithOn && devotion && valuesOn && identity && sameDays;
})());
t('32 edition toggle does not disturb seat or door panels', doc.getElementById('door-work').className.indexOf('on') > -1 && doc.getElementById('seat-team').className.indexOf('on') > -1);

// ---------- strategy / status ----------
t('33 strategy: four prospect rows, internal warning, three notes', (function(){
  const rows = doc.querySelectorAll('#strategy .srow');
  if (rows.length !== 4) return false;
  let ok = true;
  rows.forEach(r => { if (r.querySelector('.stt').textContent.toLowerCase().indexOf('prospect') === -1) ok = false; });
  const txt = doc.getElementById('strategy').textContent;
  return ok && txt.indexOf('Rick Reynolds') > -1 && txt.indexOf('Convene') > -1 && txt.indexOf('internal edition only') > -1 && doc.querySelectorAll('#strategy .dir .dirrow').length === 3;
})());
t('34 status: eight rows incl. journeys drafted, founding zero recruits, naming ruling', (function(){
  const rows = doc.querySelectorAll('.statusrow');
  const txt = doc.getElementById('strategy').textContent;
  return rows.length === 8 && txt.indexOf('one hundred and one daily readings') > -1 && txt.indexOf('zero recruits') > -1 && txt.indexOf('Purpose Driven Business name is held back') > -1;
})());

// ---------- design-system integrity ----------
t('35 exact font URL, hero gradient, header blur', html.indexOf('Playfair+Display:ital,wght@0,500;0,700;0,800;0,900;1,500;1,600') > -1 && html.indexOf('radial-gradient(80% 120% at 78% -10%, rgba(201,163,92,.12), transparent 55%)') > -1 && html.indexOf('rgba(11,23,38,.86)') > -1 && html.indexOf('blur(14px)') > -1);
t('36 no real shadows, no emoji, no template literals, panel discipline', (function(){
  const realShadow = /box-shadow\s*:\s*(?!none)/.test(html);
  const emojiRe = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{1F000}-\u{1F0FF}]/u;
  return !realShadow && !emojiRe.test(html) && html.indexOf('`') === -1 && html.indexOf('gap:1px;background:var(--line-gold)') > -1;
})());

console.log('\n' + pass + '/' + (pass + fail) + ' tests pass');
process.exit(fail === 0 ? 0 : 1);
