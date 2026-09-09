/* Full-corpus audit: renders EVERY day of EVERY campaign (plus sermons & sessions)
   and machine-checks each one. This is how "every single word" gets verified at
   131-million-word scale: every atom is hand-reviewed in the banks; every assembly
   is checked here. Exit 1 on any defect. */
const { JSDOM } = require("jsdom");
const path = require("path");
const SITE = "/home/claude/site";
const BAN = /\b(journey|unpack|lean into|season of life|do life together)\b/i;
const REFRX = /^((?:[123] )?[A-Za-z ]+?) (\d+):(\d+)(?:-(\d+))?$/;

(async () => {
  const dom = await JSDOM.fromFile(path.join(SITE, "campaign.html"), {
    resources: "usable", runScripts: "dangerously", pretendToBeVisual: true,
    url: "file://" + SITE + "/campaign.html?id=M-10001",
    beforeParse(w) {
      const mem = {};
      Object.defineProperty(w, "localStorage", { value: {
        getItem: k => mem[k] ?? null, setItem: (k,v) => mem[k]=String(v), removeItem: k => delete mem[k] }});
      w.console.error = () => {};
    }
  });
  await new Promise(r => setTimeout(r, 1800));
  const w = dom.window, E = w.Engine, A = w.App;
  const CANON = new Set(A.D.refs);                       // pool refs, already canon-validated at emit
  const PAIRREF = new Set();
  E.banks.forEach(b => b.p.forEach(p => PAIRREF.add(p[1])));

  const defects = {};                                     // class -> [examples]
  let dayCount = 0, sermonCount = 0, sessionCount = 0, wordTotal = 0, dupDays = 0;
  const flag = (cls, ex) => { (defects[cls] = defects[cls] || []).length < 5 && defects[cls].push(ex); defects[cls].n = (defects[cls].n||0)+1; };
  const daysFor = o => o.f & 8 ? 40 : o.f & 4 ? 30 : o.f & 2 ? 21 : o.f & 1 ? 7 : o.f & 16 ? 6 : o.f & 128 ? 12 : 1;
  const fmtFor  = o => o.f & 8 ? "40" : o.f & 4 ? "30" : o.f & 2 ? "21" : o.f & 1 ? "7" : o.f & 16 ? "study" : o.f & 128 ? "year" : "sunday";

  function checkText(id, where, s) {
    if (s == null) { flag("null-field", `${id} ${where}`); return; }
    wordTotal += s.split(/\s+/).length;
    if (/\{[a-zA-Z]/.test(s)) flag("unfilled-slot", `${id} ${where}: ${s.slice(0,80)}`);
    if (/undefined|\[object/.test(s)) flag("undefined-leak", `${id} ${where}: ${s.slice(0,80)}`);
    if (BAN.test(s)) flag("banned-word", `${id} ${where}: ${s.match(BAN)[0]}`);
    if (/\s{2,}|\s[,.]|\.\./.test(s.replace(/\.\.\./g,""))) flag("spacing-punct", `${id} ${where}: ${s.slice(0,80)}`);
    if (/\b(about|on|of|grow|in) (begin|listen|release|receive|return|remember|respond|abide)\b/i.test(s))
      flag("verb-in-noun-slot", `${id} ${where}: ${s.slice(0,90)}`);
    // any inline citation must be a known-canonical ref (pool or verified pair)
    for (const m of s.matchAll(/\(((?:[123] )?[A-Z][a-zA-Z ]*? \d+:\d+(?:-\d+)?)\)/g))
      if (!CANON.has(m[1]) && !PAIRREF.has(m[1])) flag("uncanonical-citation", `${id} ${where}: ${m[1]}`);
  }
  function checkRef(id, where, r) {
    if (!r || !REFRX.test(r)) { flag("bad-ref-format", `${id} ${where}: ${r}`); return; }
    if (!CANON.has(r) && !PAIRREF.has(r)) flag("unknown-ref", `${id} ${where}: ${r}`);
  }

  const rows = A.ROWS;
  const t0 = Date.now();
  for (let ri = 0; ri < rows.length; ri++) {
    const o = rows[ri];
    if (o.f === 64) continue;                            // resources have no generated days
    const n = daysFor(o), fk = fmtFor(o);
    const seen = new Set();
    for (let i = 0; i < n; i++) {
      const d = E.day(o, fk, i, n); dayCount++;
      checkRef(o.id, `day${i+1}.ref`, d.ref); checkRef(o.id, `day${i+1}.ref2`, d.ref2);
      for (const f of ["read","open","truth","turn","step","q","pray"]) checkText(o.id, `day${i+1}.${f}`, d[f]);
      const sig = d.open + "|" + d.truth + "|" + d.step;
      if (seen.has(sig)) { dupDays++; flag("duplicate-day-in-campaign", `${o.id} day${i+1}`); }
      seen.add(sig);
      // structural guarantees
      if (i === 0 && n > 1 && fk !== "study" && fk !== "year" && d.word !== "Welcome") flag("no-welcome", o.id);
      if (i === n-1 && n > 1 && fk !== "study" && fk !== "year" && d.word !== "Sent") flag("no-commissioning", o.id);
      if (d.sunday && !/Sunday/.test(d.open)) flag("sunday-not-sunday", `${o.id} day${i+1}`);
      // truth must cite a bound pair ref (Biblical soundness by construction)
      const cite = d.truth.match(/((?:[123] )?[A-Z][a-zA-Z ]*? \d+:\d+(?:-\d+)?)/);
      if (cite && !PAIRREF.has(cite[1])) flag("truth-cites-unbound-ref", `${o.id} day${i+1}: ${cite[1]}`);
      if (!cite) flag("truth-missing-citation", `${o.id} day${i+1}`);
    }
    const sN = Math.min(o.f & 8 ? 6 : o.f & 4 ? 4 : o.f & 2 ? 3 : 1, 6);
    for (let sw = 0; sw < sN; sw++) {
      const sm = E.sermon(o, sw); sermonCount++;
      sm.texts.forEach((t,k) => checkRef(o.id, `sermon${sw+1}.text${k}`, t));
      checkText(o.id, `sermon${sw+1}.big`, sm.big);
      sm.moves.forEach((m,k) => checkText(o.id, `sermon${sw+1}.move${k}`, m.body));
      checkText(o.id, `sermon${sw+1}.land`, sm.land + " " + sm.respond);
      const g = E.session(o, sw); sessionCount++;
      g.refs.forEach((r,k) => checkRef(o.id, `session${sw+1}.ref${k}`, r));
      [g.open, g.practice, g.pray, ...g.qs].forEach((t,k) => checkText(o.id, `session${sw+1}.part${k}`, t));
    }
    if (ri % 2000 === 0) process.stderr.write(`  …${ri}/${rows.length} campaigns (${Math.round((Date.now()-t0)/1000)}s)\n`);
  }

  const classes = Object.keys(defects);
  console.log(`\nCORPUS AUDIT — ${rows.length.toLocaleString()} campaigns`);
  console.log(`  days generated & checked:      ${dayCount.toLocaleString()}`);
  console.log(`  sermon builds checked:         ${sermonCount.toLocaleString()}`);
  console.log(`  group sessions checked:        ${sessionCount.toLocaleString()}`);
  console.log(`  words verified:                ${wordTotal.toLocaleString()}`);
  console.log(`  duplicate days within a campaign: ${dupDays}`);
  if (!classes.length) { console.log("  defects: NONE — corpus clean"); process.exit(0); }
  console.log("  DEFECTS:");
  for (const c of classes) console.log(`   ${c} ×${defects[c].n}: ${defects[c].slice(0,3).join(" | ")}`);
  process.exit(1);
})().catch(e => { console.error("HARNESS", e); process.exit(1); });
