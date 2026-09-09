const fs = require('fs');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync('/mnt/user-data/outputs/marketplace-ministry-intelligence.html', 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously' });
const doc = dom.window.document;
const win = dom.window;

let pass = 0, fail = 0;
function t(name, cond) {
  if (cond) { pass++; console.log('PASS  ' + name); }
  else { fail++; console.log('FAIL  ' + name); }
}
function click(el) { el.dispatchEvent(new win.Event('click', { bubbles: true })); }

// 1. document loads with no script errors (implicit) and title correct
t('01 loads, title set', doc.title.indexOf('Marketplace Ministry Intelligence') === 0);

// 2. seven tabs exist
const tabBtns = doc.querySelectorAll('.tab-btn');
t('02 seven tab buttons', tabBtns.length === 7);

// 3-4. each tab activates its panel
let allTabsWork = true;
const tabIds = ['ov','dom','diag','seats','form','journey','price'];
tabIds.forEach(id => {
  click(doc.getElementById('tabbtn-' + id));
  const p = doc.getElementById('panel-' + id);
  if (!p || p.className.indexOf('on') === -1) allTabsWork = false;
  // and every other panel hidden
  tabIds.forEach(o => { if (o !== id) { if (doc.getElementById('panel-' + o).className.indexOf('on') > -1) allTabsWork = false; } });
});
t('03 every tab activates its panel exclusively', allTabsWork);
click(doc.getElementById('tabbtn-ov'));
t('04 return to overview', doc.getElementById('panel-ov').className.indexOf('on') > -1);

// 5-6. audience segmentation
t('05 four audience buttons, senior pastor default', doc.querySelectorAll('.audbtn').length === 4 && doc.getElementById('audtext-sp').style.display !== 'none');
click(doc.getElementById('audbtn-xp'));
const xpVisible = doc.getElementById('audtext-xp').style.display === 'block';
const spHidden = doc.getElementById('audtext-sp').style.display === 'none';
t('06 switching audience swaps framing text', xpVisible && spHidden && doc.getElementById('audtext-xp').textContent.indexOf('leading indicators') > -1);
click(doc.getElementById('audbtn-bo'));
t('07 owner audience carries the confidentiality line', doc.getElementById('audtext-bo').textContent.indexOf('never sales intelligence') > -1);

// 8-9. six domains
const dcards = doc.querySelectorAll('.dcard');
t('08 six domain cards render', dcards.length === 6);
click(dcards[3].querySelector('.dhead'));
t('09 domain card expands (The Owners)', dcards[3].className.indexOf('open') > -1 && dcards[3].textContent.indexOf('letter of intent') > -1);

// 10. every domain carries a floor and a key line
let floorsOk = true;
dcards.forEach(c => { if (!c.querySelector('.floor') || !c.querySelector('.keyline')) floorsOk = false; });
t('10 every domain has a floor and a line', floorsOk);

// 11-12. diagnostic structure
const qblocks = doc.querySelectorAll('.qblock');
t('11 twelve diagnostic questions', qblocks.length === 12);
t('12 forty-eight options total', doc.querySelectorAll('.opt').length === 48);

// 13. picking an option selects it and updates score
const q0max = doc.querySelector('.opt[data-q="0"][data-val="4"]');
click(q0max);
t('13 option select updates score', q0max.className.indexOf('sel') > -1 && doc.getElementById('score-num').textContent === '4' && doc.getElementById('score-prog').textContent === '1 of 12 answered');

// 14. re-picking within the same question replaces, never stacks
click(doc.querySelector('.opt[data-q="0"][data-val="1"]'));
t('14 re-pick replaces value', doc.getElementById('score-num').textContent === '1');

// 15. band hidden until all twelve answered
t('15 band hidden while incomplete', doc.getElementById('band-out').style.display === 'none');

// 16. answer all twelve at max -> 48, top band
for (let q = 0; q < 12; q++) click(doc.querySelector('.opt[data-q="' + q + '"][data-val="4"]'));
t('16 max score 48 and top band shown', doc.getElementById('score-num').textContent === '48' && doc.getElementById('band-name').textContent === 'Commissioned & Multiplying' && doc.getElementById('band-out').style.display === 'block');

// 17. band boundary math via exposed function — no gaps, no overlaps
const b = win.mmiBand;
const boundaries =
  b(0)[2] === 'The Sunday Church' && b(14)[2] === 'The Sunday Church' &&
  b(15)[2] === 'Blessed, Not Equipped' && b(26)[2] === 'Blessed, Not Equipped' &&
  b(27)[2] === 'Equipping for Monday' && b(38)[2] === 'Equipping for Monday' &&
  b(39)[2] === 'Commissioned & Multiplying' && b(48)[2] === 'Commissioned & Multiplying';
t('17 band boundaries exact at 14/15, 26/27, 38/39', boundaries);
let covered = true;
for (let s = 0; s <= 48; s++) { if (!b(s)) covered = false; }
t('18 every score 0-48 maps to exactly one band', covered);

// 19. reset clears
win.mmiReset();
t('19 reset clears score, progress and band', doc.getElementById('score-num').textContent === '0' && doc.getElementById('score-prog').textContent === '0 of 12 answered' && doc.getElementById('band-out').style.display === 'none' && doc.querySelectorAll('.opt.sel').length === 0);

// 20-21. seats
t('20 three seats, employee default', doc.querySelectorAll('.seatbtn').length === 3 && doc.getElementById('seat-employee').className.indexOf('on') > -1);
click(doc.getElementById('seatbtn-owner'));
t('21 seat switch shows owner only', doc.getElementById('seat-owner').className.indexOf('on') > -1 && doc.getElementById('seat-employee').className.indexOf('on') === -1 && doc.getElementById('seat-owner').textContent.indexOf('God Owns It All') > -1);

// 22. formation tracks with honest status labels
const tracks = doc.querySelectorAll('.track');
let rights = false;
tracks.forEach(tr => { if (tr.textContent.indexOf('rights pending') > -1) rights = true; });
t('22 eight tracks, RBI rights label present', tracks.length === 8 && rights);

// 23. journey — six stages, expandable, integrity language present
const stages = doc.querySelectorAll('.jstage');
click(stages[2].querySelector('.jhead'));
t('23 six journey stages; stage 3 opens with the never-sells rule', stages.length === 6 && stages[2].className.indexOf('open') > -1 && stages[2].textContent.indexOf('never sells it') > -1);

// 24. pricing consistent with the ladder + status honesty
const priceText = doc.getElementById('panel-price').textContent;
t('24 pricing mirrors the ladder and states unvalidated status', priceText.indexOf('$590') > -1 && priceText.indexOf('$2,890') > -1 && priceText.indexOf('$3,900') > -1 && priceText.indexOf('unvalidated') > -1 && priceText.indexOf('Purpose Driven Business') > -1);

// 25. no emoji anywhere (blue-template rule)
const emojiRe = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{1F000}-\u{1F0FF}]/u;
t('25 no emoji in the document', !emojiRe.test(html));

// 26. no JS template literals (backticks) in the file
t('26 no template literals in JS', html.indexOf('`') === -1);

console.log('\n' + pass + '/' + (pass + fail) + ' tests pass');
process.exit(fail === 0 ? 0 : 1);
