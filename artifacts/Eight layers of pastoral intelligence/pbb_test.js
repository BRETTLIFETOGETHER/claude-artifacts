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

// structure
t('01 loads, title set', doc.title.indexOf('Purpose Built Business') === 0);
t('02 nine nav anchors, all targets exist', (function(){
  const links = doc.querySelectorAll('nav a');
  if (links.length !== 9) return false;
  let ok = true;
  links.forEach(a => { const id = a.getAttribute('href').slice(1); if (!doc.getElementById(id)) ok = false; });
  return ok;
})());
t('03 hero: four stats, both CTAs', doc.querySelectorAll('.stat').length === 4 && doc.querySelectorAll('.hero .btn').length === 2);
t('04 internal-edition chip on hero', doc.querySelector('.chipline').textContent.indexOf('remove before external use') > -1);
t('05 argument carries the two-door line', doc.getElementById('argument').textContent.indexOf('church door') > -1);

// frameworks
t('06 PBB framework: five purposes', (function(){
  const p = doc.querySelectorAll('.pgrid.two .pnl')[0];
  return p.querySelectorAll('.frow').length === 5 && p.textContent.indexOf('Worship') > -1 && p.textContent.indexOf('Mission') > -1;
})());
t('07 Flourishing framework: six criteria incl. Across Generations', (function(){
  const p = doc.querySelectorAll('.pgrid.two .pnl')[1];
  return p.querySelectorAll('.frow').length === 6 && p.textContent.indexOf('Across Generations') > -1;
})());

// diagnostic (instrument 1)
t('08 diagnostic: 12 questions, 48 options', doc.querySelectorAll('#diagnostic .qblock').length === 12 && doc.querySelectorAll('#diagnostic .opt').length === 48);
const d0 = doc.querySelector('.opt[data-q="0"][data-val="4"]');
click(d0);
t('09 pick updates score and progress', d0.className.indexOf('sel') > -1 && doc.getElementById('d-score').textContent === '4' && doc.getElementById('d-prog').textContent === '1 of 12 answered');
click(doc.querySelector('.opt[data-q="0"][data-val="1"]'));
t('10 re-pick replaces, never stacks', doc.getElementById('d-score').textContent === '1');
t('11 band hidden while incomplete', doc.getElementById('d-band').style.display === 'none');
for (let q = 0; q < 12; q++) click(doc.querySelector('.opt[data-q="' + q + '"][data-val="4"]'));
t('12 full max = 48, band Purpose Built shown', doc.getElementById('d-score').textContent === '48' && doc.getElementById('d-band-name').textContent === 'Purpose Built' && doc.getElementById('d-band').style.display === 'block');
const b = win.pbbBand;
t('13 diagnostic band boundaries 14/15, 26/27, 38/39', b(14)[2] === 'Well-Run, Unformed' && b(15)[2] === 'Values on the Wall' && b(26)[2] === 'Values on the Wall' && b(27)[2] === 'Formation Underway' && b(38)[2] === 'Formation Underway' && b(39)[2] === 'Purpose Built');
t('14 every score 0-48 maps to one band', (function(){ for (let s = 0; s <= 48; s++) { if (!b(s)) return false; } return true; })());
win.pbbDReset();
t('15 diagnostic reset clears fully', doc.getElementById('d-score').textContent === '0' && doc.getElementById('d-band').style.display === 'none' && doc.querySelectorAll('#diagnostic .opt.sel').length === 0);

// flourishing (instrument 2)
t('16 flourishing: 24 statements, 120 rating buttons, 6 dimension heads', doc.querySelectorAll('.stmt').length === 24 && doc.querySelectorAll('.rbtn').length === 120 && doc.querySelectorAll('.dimhead').length === 6);
const f0 = doc.querySelector('.rbtn[data-q="0"][data-val="3"]');
click(f0);
t('17 rating select updates total; subtotal waits for full dimension', f0.className.indexOf('sel') > -1 && doc.getElementById('f-score').textContent === '3' && doc.getElementById('fsub-0').textContent.indexOf('\u2013') === 0);
click(doc.querySelector('.rbtn[data-q="1"][data-val="5"]'));
click(doc.querySelector('.rbtn[data-q="2"][data-val="5"]'));
click(doc.querySelector('.rbtn[data-q="3"][data-val="5"]'));
t('18 dimension subtotal appears at four answered (18/20)', doc.getElementById('fsub-0').textContent === '18 / 20');
for (let q = 0; q < 24; q++) click(doc.querySelector('.rbtn[data-q="' + q + '"][data-val="5"]'));
t('19 all fives = 120, top band, every subtotal 20/20', (function(){
  if (doc.getElementById('f-score').textContent !== '120') return false;
  if (doc.getElementById('f-band-name').textContent !== 'A Flourishing Workplace') return false;
  for (let d = 0; d < 6; d++) { if (doc.getElementById('fsub-' + d).textContent !== '20 / 20') return false; }
  return true;
})());
const fb = win.pbbFlourBand;
t('20 flourishing band boundaries 59/60, 83/84, 104/105', fb(24)[2] === 'Begin with Trust and Purpose' && fb(59)[2] === 'Begin with Trust and Purpose' && fb(60)[2] === 'Foundations Forming' && fb(83)[2] === 'Foundations Forming' && fb(84)[2] === 'Emerging Flourishing Culture' && fb(104)[2] === 'Emerging Flourishing Culture' && fb(105)[2] === 'A Flourishing Workplace' && fb(120)[2] === 'A Flourishing Workplace');
t('21 every score 24-120 maps to one band', (function(){ for (let s = 24; s <= 120; s++) { if (!fb(s)) return false; } return true; })());
win.pbbFReset();
t('22 flourishing reset clears totals and subtotals', doc.getElementById('f-score').textContent === '0' && doc.getElementById('fsub-3').textContent.indexOf('\u2013') === 0 && doc.querySelectorAll('.rbtn.sel').length === 0);

// seats + peer group
t('23 three seats, owner switch works', (function(){
  if (doc.querySelectorAll('.seatbtn').length !== 3) return false;
  click(doc.getElementById('seatbtn-team'));
  return doc.getElementById('seat-team').className.indexOf('on') > -1 && doc.getElementById('seat-owner').className.indexOf('on') === -1;
})());
t('24 owner peer group: ten studies with Scripture anchors', (function(){
  const rows = doc.querySelectorAll('#seats .dirrow');
  if (rows.length !== 10) return false;
  return rows[0].textContent.indexOf('Proverbs 27:17') > -1 && rows[9].textContent.indexOf('Psalm 78') > -1;
})());

// library
t('25 library: seven parts, twenty verticals, five-section spine, honest math', (function(){
  const lib = doc.getElementById('library');
  const parts = lib.querySelectorAll('.dirrow').length === 7;
  const verts = lib.querySelectorAll('.chips')[1].querySelectorAll('.chip').length === 20;
  const spine = lib.textContent.indexOf('Legacy & Kingdom Impact') > -1;
  const math = lib.textContent.indexOf('165 categories') > -1 && lib.textContent.indexOf('2,025 titles') > -1;
  return parts && verts && spine && math;
})());

// process + pricing
t('26 process: five steps with reconciled bands', (function(){
  const p = doc.getElementById('process');
  return p.querySelectorAll('.steprow').length === 5 && p.textContent.indexOf('$18,000\u2013$60,000') > -1 && p.textContent.indexOf('$1,500\u2013$4,500') > -1;
})());
t('27 pricing: four tiers and five models, subscription primary', (function(){
  const p = doc.getElementById('pricing');
  return p.querySelectorAll('.tierrow').length === 4 && p.querySelectorAll('.dirrow').length === 5 && p.textContent.indexOf('$28,000') > -1 && p.textContent.indexOf('The primary model') > -1;
})());

// strategy + status honesty
t('28 strategy: four rows, every one labeled prospect, internal warning present', (function(){
  const rows = doc.querySelectorAll('#strategy .srow');
  if (rows.length !== 4) return false;
  let ok = true;
  rows.forEach(r => { if (r.querySelector('.stt').textContent.toLowerCase().indexOf('prospect') === -1) ok = false; });
  const names = doc.getElementById('strategy').textContent;
  return ok && names.indexOf('Rick Reynolds') > -1 && names.indexOf('Convene') > -1 && names.indexOf('C12') > -1 && names.indexOf('internal edition only') > -1;
})());
t('29 status: six rows incl. naming ruling, unvalidated pricing, no-endorsement line', (function(){
  const rows = doc.querySelectorAll('.statusrow');
  const txt = doc.getElementById('strategy').textContent;
  return rows.length === 6 && txt.indexOf('Purpose Driven Business name is held back') > -1 && txt.indexOf('unvalidated') > -1 && txt.indexOf('implies endorsement') > -1;
})());

// design-system integrity
t('30 exact font URL, exact hero gradient, exact header blur', html.indexOf('Playfair+Display:ital,wght@0,500;0,700;0,800;0,900;1,500;1,600') > -1 && html.indexOf('radial-gradient(80% 120% at 78% -10%, rgba(201,163,92,.12), transparent 55%)') > -1 && html.indexOf('rgba(11,23,38,.86)') > -1 && html.indexOf('blur(14px)') > -1);
t('31 no drop shadows, no emoji, no JS template literals', (function(){
  const shadowCount = (html.match(/box-shadow/g) || []).filter(x => true).length;
  // one box-shadow:none allowed on active seat button; no real shadows
  const realShadow = /box-shadow\s*:\s*(?!none)/.test(html);
  const emojiRe = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{1F000}-\u{1F0FF}]/u;
  return !realShadow && !emojiRe.test(html) && html.indexOf('`') === -1;
})());
t('32 panel discipline: gap 1px over line-gold, radius 0 on panels / 3px controls', html.indexOf('gap:1px;background:var(--line-gold)') > -1 && html.indexOf('border-radius:3px') > -1 && html.indexOf('.pnl{background:var(--panel)') > -1 && html.indexOf('.pnl{border-radius') === -1);

console.log('\n' + pass + '/' + (pass + fail) + ' tests pass');
process.exit(fail === 0 ? 0 : 1);
