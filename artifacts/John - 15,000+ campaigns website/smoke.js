/* Smoke tests: execute pages in jsdom, fail on console errors / broken assertions. */
const { JSDOM } = require("jsdom");
const path = require("path");
const SITE = "/home/claude/site";
let failures = 0;
function fail(msg){ console.error("  ✗ " + msg); failures++; }
function ok(msg){ console.log("  ✓ " + msg); }

async function load(rel, { seed, url } = {}) {
  const errors = [];
  const dom = await JSDOM.fromFile(path.join(SITE, rel), {
    resources: "usable", runScripts: "dangerously", pretendToBeVisual: true,
    url: url || "file://" + path.join(SITE, rel),
    beforeParse(w) {
      w.addEventListener("error", e => errors.push(e.message));
      const _err = w.console.error.bind(w.console);
      w.console.error = (...a) => { errors.push(a.join(" ")); _err(...a); };
      if (seed) for (const [k, v] of Object.entries(seed)) w.localStorage.setItem(k, JSON.stringify(v));
      w.matchMedia = w.matchMedia || (() => ({ matches:false, addListener(){}, removeListener(){} }));
      w.HTMLElement.prototype.scrollIntoView = function(){};
    }
  });
  await new Promise(r => setTimeout(r, 1400));
  return { dom, w: dom.window, d: dom.window.document, errors };
}

(async () => {
  // ---------- index
  {
    const { w, d, errors } = await load("index.html");
    console.log("index.html");
    errors.length ? fail("console errors: " + errors.slice(0,3).join(" | ")) : ok("no console errors");
    const tiles = d.querySelectorAll("#tiles .tile").length;
    tiles === w.DATA40.channels.length ? ok(`${tiles} channel tiles`) : fail(`tiles ${tiles}`);
    const flags = d.querySelectorAll("#flagrow .card").length;
    flags >= 10 ? ok(`${flags} flagship cards`) : fail(`flagship row ${flags}`);
    d.querySelectorAll("#searow .card").length >= 4 ? ok("seasonal row populated") : fail("seasonal row empty");
    d.querySelectorAll("#herocards svg").length === 4 ? ok("hero covers render") : fail("hero covers");
    const links = [...d.querySelectorAll("a[href]")].map(a=>a.getAttribute("href"));
    links.some(h=>h==="channel.html?c=22") ? ok("white-space channel linked") : fail("ch22 tile link");
  }
  // ---------- browse
  {
    const { w, d, errors } = await load("browse.html", { url: "file://" + SITE + "/browse.html?ch=21&f=8" });
    console.log("browse.html?ch=21&f=8");
    errors.length ? fail("console errors: " + errors.slice(0,3).join(" | ")) : ok("no console errors");
    const rc = d.querySelector("#rescount").textContent;
    parseInt(rc.replace(/,/g,"")) > 0 ? ok("filtered results: " + rc) : fail("no results text: " + rc);
    d.querySelectorAll("#railbody label").length > 40 ? ok("facet rail built") : fail("rail empty");
    d.querySelectorAll("#vlist .card").length > 0 ? ok("virtual cards mounted") : fail("no cards mounted");
    // live search
    const q = d.querySelector("#q"); q.value = "prayer"; q.dispatchEvent(new w.Event("input", {bubbles:true}));
    await new Promise(r=>setTimeout(r,400));
    ok("search executed → " + d.querySelector("#rescount").textContent);
  }
  // ---------- campaign
  {
    const { w, d, errors } = await load("campaign.html", { url: "file://" + SITE + "/campaign.html?id=M-10001" });
    console.log("campaign.html?id=M-10001");
    errors.length ? fail("console errors: " + errors.slice(0,3).join(" | ")) : ok("no console errors");
    d.querySelector("#title").textContent.length > 2 ? ok("title: " + d.querySelector("#title").textContent) : fail("no title");
    d.querySelectorAll("#arc .day").length >= 7 ? ok(d.querySelectorAll("#arc .day").length + " arc days") : fail("arc empty");
    d.querySelectorAll("#sermons .sermon").length >= 1 ? ok("sermon builds render") : fail("no sermons");
    d.querySelector("#ref").textContent.match(/\d+:\d+/) ? ok("scripture backbone: " + d.querySelector("#ref").textContent) : fail("ref missing");
    // sample day modal
    d.querySelector("#preview").click(); await new Promise(r=>setTimeout(r,100));
    !d.querySelector("#modal").classList.contains("hide") ? ok("sample-day modal opens") : fail("modal");
  }
  // ---------- nested Red Letter parent
  {
    const idx = require(SITE + "/data/index.json");
    const nested = idx.rows.find(r => r[14] > 0);
    const { d, errors } = await load("campaign.html", { url: "file://" + SITE + "/campaign.html?id=" + nested[0] });
    console.log("campaign.html (nested parent " + nested[0] + " '" + nested[2] + "')");
    errors.length ? fail("console errors: " + errors.slice(0,2).join(" | ")) : ok("no console errors");
    await new Promise(r=>setTimeout(r,400));
    d.querySelectorAll("#nest .edbox").length >= 6 ? ok("six sessions nested") : fail("nest sessions " + d.querySelectorAll("#nest .edbox").length);
  }
  // ---------- finder full run
  {
    const { w, d, errors } = await load("finder.html");
    console.log("finder.html");
    for (let i=0;i<7;i++){
      const r = d.querySelector('input[name=q]'); r.checked = true;
      r.dispatchEvent(new w.Event("change",{bubbles:true}));
      d.querySelector("#next").click(); await new Promise(r=>setTimeout(r,60));
    }
    errors.length ? fail("console errors: " + errors.slice(0,3).join(" | ")) : ok("no console errors");
    d.querySelectorAll("#picks .card").length === 3 ? ok("three ranked picks") : fail("picks " + d.querySelectorAll("#picks .card").length);
    d.querySelector("#wild .card") ? ok("unexpected pick present") : fail("no wildcard");
    d.querySelectorAll("#picks .why").length === 3 ? ok("why-explanations present") : fail("no why");
  }
  // ---------- builder full run
  {
    const { w, d, errors } = await load("builder.html");
    console.log("builder.html");
    d.querySelector("#b-idea").value = "Our church needs to trust God with money";
    d.querySelector("#bnext").click(); await new Promise(r=>setTimeout(r,60));
    d.querySelector("#bnext").click(); await new Promise(r=>setTimeout(r,60));
    d.querySelector("#bnext").click(); await new Promise(r=>setTimeout(r,120));
    errors.length ? fail("console errors: " + errors.slice(0,3).join(" | ")) : ok("no console errors");
    d.querySelector("#brief .inner h2") ? ok("brief generated: " + d.querySelector("#brief .inner h2").textContent) : fail("no brief");
    d.querySelector("#baddcart") ? ok("custom add-to-cart present") : fail("no custom cart button");
  }
  // ---------- commerce chain
  {
    const seedCart = [{id:"M-10001",fmt:"40",qty:1,t:"Welcome Home",price:949}];
    const c1 = await load("cart.html", { seed: { cart40: seedCart } });
    console.log("cart.html (seeded)");
    c1.errors.length ? fail("console errors") : ok("no console errors");
    c1.d.querySelectorAll(".cartline").length === 1 ? ok("cart line renders") : fail("cart empty");
    c1.d.querySelector(".summary .total") ? ok("totals render") : fail("no totals");

    const c2 = await load("checkout.html", { seed: { cart40: seedCart } });
    console.log("checkout.html");
    c2.d.querySelector("#co-church").value = "Grace Chapel";
    c2.d.querySelector("#co-name").value = "Pat Rivera";
    c2.d.querySelector("#co-email").value = "pat@gracechapel.org";
    c2.d.querySelector("#cc-num").value = "4242 4242 4242 4242";
    c2.d.querySelector("#cc-exp").value = "08/27";
    c2.d.querySelector("#cc-cvc").value = "123";
    let dest = null;
    // capture navigation
    Object.defineProperty(c2.w, "location", { value: new Proxy(c2.w.location, {
      set(t,k,v){ if(k==="href") dest=v; return true },
      get(t,k){ if(k==="href") return t.href; const v=t[k]; return typeof v==="function"?v.bind(t):v }
    })});
    c2.d.querySelector("#place").click(); await new Promise(r=>setTimeout(r,150));
    const orders = JSON.parse(c2.w.localStorage.getItem("orders40")||"[]");
    orders.length === 1 ? ok("order stored: " + orders[0].n) : fail("order not stored");
    JSON.parse(c2.w.localStorage.getItem("cart40")||"[]").length === 0 ? ok("cart cleared") : fail("cart not cleared");
    (dest||"").startsWith("confirmation.html?o=") ? ok("→ " + dest) : fail("no redirect: " + dest);
    c2.errors.length ? fail("checkout console errors: " + c2.errors.slice(0,2).join("|")) : ok("no console errors");

    const c3 = await load("confirmation.html", { seed: { orders40: orders }, url: "file://" + SITE + "/confirmation.html?o=" + orders[0].n });
    console.log("confirmation.html");
    c3.errors.length ? fail("console errors: "+c3.errors.slice(0,2).join("|")) : ok("no console errors");
    c3.d.querySelector("#ordno").textContent === orders[0].n ? ok("order recalled") : fail("order not recalled");
    c3.d.querySelectorAll("#dls .dl").length === 4 ? ok("4 downloads offered") : fail("downloads " + c3.d.querySelectorAll("#dls .dl").length);

    const c4 = await load("account.html", { seed: { orders40: orders } });
    console.log("account.html");
    c4.d.querySelectorAll("#orders tr").length === 1 && c4.d.querySelector("#orders td") ? ok("order history renders") : fail("history");
    c4.d.querySelectorAll("#library .card").length === 1 ? ok("library shows purchase") : fail("library");
  }
  // ---------- channel / theme / seasonal / ES page
  for (const [p, sel, min] of [["channel.html?c=22","#chgrid .card",5],["theme.html?t=3","#grid .card",1],["seasonal.html",".season",2],["es/index.html","#tiles .tile",23],["pt/browse.html","#railbody label",40]]) {
    const f = p.split("?")[0];
    const { d, errors } = await load(f, { url: "file://" + SITE + "/" + p });
    console.log(p);
    errors.length ? fail("console errors: " + errors.slice(0,2).join(" | ")) : ok("no console errors");
    d.querySelectorAll(sel).length >= min ? ok(`${sel} × ${d.querySelectorAll(sel).length}`) : fail(`${sel} ${d.querySelectorAll(sel).length} < ${min}`);
  }
  console.log(failures ? `\nSMOKE FAILURES: ${failures}` : "\nALL SMOKE TESTS PASS");
  process.exit(failures ? 1 : 0);
})().catch(e => { console.error("HARNESS ERROR", e); process.exit(1); });
