from shell import write

HEAD = """
<style>
.aud{max-width:920px;margin:0 auto;padding:60px 30px 110px}
.aud h1{font-size:clamp(36px,4.6vw,54px)}
.aud .sec{margin-top:64px}
.aud .sec>h2{font-size:clamp(24px,3vw,34px);display:flex;align-items:center;gap:18px}
.aud .sec>h2::after{content:'';flex:1;border-top:2px dotted #C9C9BE}
.aud p{margin:14px 0;font-size:16.5px;line-height:1.75}
.aud .note{background:#F4F4EF;border:1px solid var(--line);border-left:6px solid var(--lt-green);padding:18px 22px;font-size:15px;margin:20px 0}
.aud .note.orange{border-left-color:var(--lt-orange)}
.aud .note.blue{border-left-color:var(--lt-blue)}
table.at{width:100%;border-collapse:collapse;margin:22px 0;font-size:14.5px}
table.at th{font-family:var(--display);font-size:12px;letter-spacing:.18em;text-transform:uppercase;text-align:left;color:#fff;background:#1C1C1C;padding:11px 14px}
table.at td{border:1px solid var(--line);padding:12px 14px;vertical-align:top;background:#fff}
table.at tr:nth-child(even) td{background:#FAFAF6}
.tag{display:inline-block;font-family:var(--display);font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;padding:4px 9px;white-space:nowrap}
.tag.works{background:var(--lt-green);color:#fff}
.tag.proto{background:var(--lt-lime);color:#1C1C1C}
.tag.stub{background:var(--lt-gray);color:#fff}
.tag.needs{background:var(--lt-orange);color:#fff}
.tag.s{background:#EAF0E2;color:#5F8540}
.tag.m{background:#E8EDF6;color:#2E4C97}
.tag.l{background:#FBE7DE;color:#C23F10}
.aud ol.plan{margin:16px 0 0 22px;display:flex;flex-direction:column;gap:12px;font-size:15.5px}
.aud ol.plan b{color:var(--ink)}
.aud ul.cl{margin:12px 0 0 22px;display:flex;flex-direction:column;gap:9px;font-size:15px}
</style>
"""

BODY = """
<div class="aud">
  <span class="eyebrow">Internal Document · August 2026</span>
  <h1 class="mt16">Site Audit &amp;<br>Launch <em>Checklist</em>.</h1>
  <p class="lede mt16">An honest, complete inventory of lifetogether.com as it stands: what genuinely works, what is prototype-only, every button that doesn&rsquo;t yet do the real thing, and exactly what has to be connected to open the doors to the public.</p>

  <div class="sec">
    <h2>Where the site is today</h2>
    <p>This is a <b>high-fidelity working prototype</b> — not a mock-up. The two hero experiences (Find My Path and the pastor Create studio) are real, running software; the design system is built from the actual Lifetogether catalog; every internal link resolves; and as of this build, a <b>prototype account layer</b> exists: sign in, upload sermons, and everything you upload or generate is saved to My Library, alongside the best of the Lifetogether flagship shelf.</p>
    <p>The gap between this and a public product is <b>not design and not the front-end</b> — it is three connections: <b>(1) a real backend</b> (accounts, database, file storage), <b>(2) the AI engine server-side</b> (Claude API + the Lifetogether corpus), and <b>(3) Stripe</b>. Everything else on this list hangs off one of those three.</p>
  </div>

  <div class="sec">
    <h2>What genuinely works right now</h2>
    <table class="at">
      <tr><th>Capability</th><th>Status</th><th>Notes</th></tr>
      <tr><td>All navigation, mega-menu, mobile menu, every internal link &amp; anchor</td><td><span class="tag works">Works</span></td><td>Programmatically link-checked, zero broken links</td></tr>
      <tr><td>Assessment: 24 statements, deterministic scoring, profile, growth-area choice, matched campaigns</td><td><span class="tag works">Works</span></td><td>Same answers always produce the same profile</td></tr>
      <tr><td>Personalized Day One reader (name, area, campaign, path length)</td><td><span class="tag works">Works</span></td><td>Driven by URL parameters; NIV verse with attribution</td></tr>
      <tr><td>Create studio: sample sermon, paste-your-own analysis, editable confirmation, preferences, 4/5/6-session generation, live editor, &ldquo;your words&rdquo; marks, regenerate</td><td><span class="tag works">Works</span></td><td>Custom-paste analysis is on-device heuristics, labeled as such</td></tr>
      <tr><td><b>Word download</b> from the Create studio</td><td><span class="tag works">Works</span></td><td>Downloads a real .doc that opens and edits in Word today</td></tr>
      <tr><td><b>Print / Save-as-PDF</b> of the full curriculum</td><td><span class="tag works">Works</span></td><td>Browser print dialog; all sessions formatted</td></tr>
      <tr><td>Sign in / Create account → My Library (uploads, generated curricula, saved path, flagship shelf, reopen &amp; re-export)</td><td><span class="tag proto">Prototype</span></td><td>Saves to this device only (browser storage) — no server yet, no real password. Proves the product; not yet the product</td></tr>
      <tr><td>Browse search over the flagship shelf; channel tiles with real catalog counts</td><td><span class="tag works">Works</span></td><td>Counts from the live 16,379-title master catalog</td></tr>
      <tr><td>All photography</td><td><span class="tag works">Works</span></td><td>22 images extracted directly from the printed catalog PDF</td></tr>
    </table>
  </div>

  <div class="sec">
    <h2>Every button that doesn&rsquo;t do the real thing yet</h2>
    <table class="at">
      <tr><th>Where</th><th>Control</th><th>Today</th><th>Needs</th></tr>
      <tr><td>Header / util bar</td><td>Search</td><td><span class="tag stub">Links to Browse</span></td><td>Site-wide search over the full 16k catalog (index + search API)</td></tr>
      <tr><td>Header / util bar</td><td>Request a Sample</td><td><span class="tag stub">Goes to contact</span></td><td>Email capture + automated sample delivery (email service)</td></tr>
      <tr><td>Login</td><td>Sign in / Create account</td><td><span class="tag proto">Device-only session</span></td><td>Real auth (Supabase / Clerk / Netlify Identity) + database</td></tr>
      <tr><td>My Library</td><td>All saved items</td><td><span class="tag proto">Browser storage</span></td><td>Cloud storage per account so a pastor&rsquo;s library follows them across devices; church-team roles</td></tr>
      <tr><td>Create studio</td><td>Paste-your-own analysis</td><td><span class="tag proto">On-device heuristics</span></td><td>Claude API server-side + Lifetogether formation engine + verse-bound scripture validation</td></tr>
      <tr><td>Create studio</td><td>Word / PDF file upload (drag a .docx in)</td><td><span class="tag needs">Not built</span></td><td>File upload + text extraction service (small server function)</td></tr>
      <tr><td>Create studio</td><td>Open in Canva</td><td><span class="tag stub">Alert stub</span></td><td>Canva Connect API (OAuth + design import) — phase 2; manual PDF-import into Canva works day one</td></tr>
      <tr><td>Create studio</td><td>Devotional / Leader Guide / 40-Day Campaign outputs</td><td><span class="tag stub">Coming soon by design</span></td><td>Same engine, additional output templates</td></tr>
      <tr><td>Pricing</td><td>Start with Starter / Standard / Complete, License one campaign</td><td><span class="tag stub">Go to contact</span></td><td>Stripe Products + Checkout + customer portal + webhooks → account entitlements</td></tr>
      <tr><td>About</td><td>Contact form &ldquo;Request the call&rdquo;</td><td><span class="tag stub">Visual only</span></td><td>Form handler (Netlify Forms) + notification email</td></tr>
      <tr><td>Browse</td><td>23 channel tiles</td><td><span class="tag stub">Anchor to flagships</span></td><td>Real channel pages backed by the catalog data shards (already built in the 40daycampaigns engine — wire, don&rsquo;t rebuild)</td></tr>
      <tr><td>Browse</td><td>Search beyond the 24 flagships</td><td><span class="tag proto">Flagships only</span></td><td>Full-catalog search index</td></tr>
      <tr><td>Assessment</td><td>Email-my-profile</td><td><span class="tag needs">Not built</span></td><td>Accounts + transactional email</td></tr>
      <tr><td>Campaign detail</td><td>Only one detail page exists (Life Together)</td><td><span class="tag proto">Template proven</span></td><td>Generate detail pages for all 383 flagships from catalog data (the 40daycampaigns build already prerenders these — port them)</td></tr>
      <tr><td>Footer</td><td>Privacy / Terms</td><td><span class="tag needs">Missing</span></td><td>Legal pages required before public launch</td></tr>
      <tr><td>Site-wide</td><td>Favicon, social-share (OG) images, sitemap, analytics</td><td><span class="tag needs">Missing</span></td><td>Small, do at deploy time</td></tr>
    </table>
  </div>

  <div class="sec">
    <h2>The export question, answered precisely</h2>
    <p>You asked: once someone finishes the flow and has the curriculum they want, how close are we to handing them a Word file, a PDF, or a Canva file?</p>
    <table class="at">
      <tr><th>Format</th><th>Distance to done</th><th>What connects it</th></tr>
      <tr><td><b>Word</b></td><td><span class="tag works">Working today</span> <span class="tag s">Small lift to perfect</span></td><td>The download button already produces a real, editable .doc. Upgrade path: a serverless function producing true branded <b>.docx</b> (cover page, church logo, styles) using the document pipeline we already run for campaign masters. This is the easiest of the three.</td></tr>
      <tr><td><b>PDF</b></td><td><span class="tag works">Working via Print</span> <span class="tag m">Medium-small to automate</span></td><td>Print → Save as PDF works now. Production: a WeasyPrint render function — <b>the exact HTML→PDF pipeline already built and battle-tested for the 40daycampaigns masters</b> — triggered by the Export button, saved to the user&rsquo;s library, emailed as a copy.</td></tr>
      <tr><td><b>Canva</b></td><td><span class="tag needs">Stub</span> <span class="tag l">Phase 2</span></td><td>Two paths: <b>Day one</b> — export the PDF and use Canva&rsquo;s standard PDF import (works now, one manual step). <b>Phase 2</b> — Canva Connect API: register a Canva app, OAuth the user, push the curriculum in as an editable branded design. This matches the existing platform roadmap (PDF import today, Connect/Button API phase 2).</td></tr>
    </table>
    <div class="note">The honest headline: <b>the export is not the hard part.</b> Word works today and PDF is a port of a pipeline we already own. The real distance to a public product is accounts + database, the AI engine server-side, and Stripe.</div>
  </div>

  <div class="sec">
    <h2>The launch checklist</h2>
    <p>Everything required to take this from prototype to public, grouped and sized. <span class="tag s">Small</span> = hours-to-a-day of work · <span class="tag m">Medium</span> = days · <span class="tag l">Large</span> = the real projects.</p>
    <table class="at">
      <tr><th>#</th><th>Item</th><th>Size</th><th>Detail</th></tr>
      <tr><td>1</td><td><b>Hosting &amp; domain</b></td><td><span class="tag s">S</span></td><td>GitHub repo → Netlify (our established pattern — Netlify Drop fails at this file count). Point lifetogether.com DNS. HTTPS automatic.</td></tr>
      <tr><td>2</td><td><b>Real accounts &amp; database</b></td><td><span class="tag l">L</span></td><td>Auth (Supabase recommended: auth + Postgres + file storage in one), user profiles, church/team roles, migrate the My Library prototype from browser storage to the cloud. This unlocks: cross-device libraries, saved paths, email-my-profile, entitlements.</td></tr>
      <tr><td>3</td><td><b>AI engine server-side</b></td><td><span class="tag l">L</span></td><td>Anthropic API behind a serverless function: sermon analysis, curriculum generation on the Lifetogether corpus, verse-bound scripture validation (the corpus-audit pattern), and the confirmation step preserved as the trust hinge. API keys as Netlify environment variables — same pattern as 40daycampaigns.</td></tr>
      <tr><td>4</td><td><b>Stripe commerce</b></td><td><span class="tag m">M</span></td><td>Products/Prices for the three tiers + single campaign license, Checkout, customer portal, webhooks writing entitlements to the database. Keys in Netlify env. Confirm final tier pricing first (current numbers are drafts).</td></tr>
      <tr><td>5</td><td><b>Export service</b></td><td><span class="tag m">M</span></td><td>True .docx + branded WeasyPrint PDF functions; save to library; email a copy. Canva Connect as phase 2.</td></tr>
      <tr><td>6</td><td><b>File upload</b></td><td><span class="tag s">S</span></td><td>Accept .docx / .pdf / .txt sermon uploads with text extraction (audio transcription as a later add).</td></tr>
      <tr><td>7</td><td><b>Full catalog wiring</b></td><td><span class="tag m">M</span></td><td>Port the 16,379-title data shards and 383 prerendered flagship detail pages from the 40daycampaigns build; real channel pages; site-wide search. This is porting, not building — it exists.</td></tr>
      <tr><td>8</td><td><b>Email</b></td><td><span class="tag s">S</span></td><td>Transactional service (Resend/Postmark): welcome, export delivery, receipts, sample requests. Contact form → Netlify Forms.</td></tr>
      <tr><td>9</td><td><b>Trust &amp; legal</b></td><td><span class="tag s">S</span></td><td>Privacy Policy, Terms of Service, refund policy page (30-day guarantee already written), cookie notice. NIV/Biblica line is in place; licensing agreement continues in parallel.</td></tr>
      <tr><td>10</td><td><b>SEO &amp; analytics</b></td><td><span class="tag s">S</span></td><td>Favicon, per-page titles/descriptions (done), OG share images, sitemap.xml, Plausible or GA4.</td></tr>
      <tr><td>11</td><td><b>Accessibility pass</b></td><td><span class="tag s">S</span></td><td>Descriptive alt text on content photos, form label audit, contrast check on lime-on-white moments, keyboard walk-through of both flows.</td></tr>
      <tr><td>12</td><td><b>Media upgrade</b></td><td><span class="tag s">S</span></td><td>Your original photo ZIP (see below), plus campaign trailer video embeds when ready (Vimeo/YouTube).</td></tr>
    </table>
  </div>

  <div class="sec">
    <h2>Suggested build order</h2>
    <ol class="plan">
      <li><b>Phase 1 — Ship the marketing site.</b> Items 1, 8, 9, 10, 11, 12. The site as it stands goes public as the new lifetogether.com: both flows run as &ldquo;preview&rdquo; experiences, contact and sample-request emails actually arrive, legal pages exist. Nothing blocks this but a deploy.</li>
      <li><b>Phase 2 — Turn on the product.</b> Items 2, 3, 5, 6. Real accounts, real AI engine, real exports, real uploads. My Library becomes cloud-backed. This is the platform launch.</li>
      <li><b>Phase 3 — Open the store &amp; the vault.</b> Items 4, 7, plus Canva Connect. Stripe goes live behind confirmed pricing; the full 16k catalog and all 383 flagship detail pages come across from the 40daycampaigns engine.</li>
    </ol>
    <div class="note blue"><b>One decision gates Phase 3:</b> final pricing. Everything on the pricing page is a draft awaiting your confirmation before Stripe products are created.</div>
  </div>

  <div class="sec">
    <h2>About the images</h2>
    <p><b>Yes — I pulled the photography straight out of the catalog PDF successfully.</b> Twenty-two frames (the timber-ceiling church, the beach shoot, the coastal cove, the baptism, Rick Warren, the crews, the couples) were extracted, color-corrected from print CMYK, and are now doing real work across the site: the homepage mosaic, every campaign cover, and the section imagery.</p>
    <p><b>And yes — a ZIP of the original JPEGs would still make things better.</b> The PDF versions are print-resolution and look clean at web sizes, but originals give me three things: higher resolution for full-bleed hero use, no print compression, and far more selection than the 126 pages contain. Uploading a ZIP is easy on my end — I drop them into the asset library, curate, optimize, and re-map covers in minutes. If you assemble one, prioritize:</p>
    <ul class="cl">
      <li>Wide church-interior and worship shots (heroes and dark bands)</li>
      <li>Small groups around tables, homes, patios (community campaigns)</li>
      <li>Families, couples, generations together (family-legacy channel)</li>
      <li>Baptisms and celebration moments (heritage &amp; Celebration Sunday)</li>
      <li>Brett with pastors — Rick Warren, Cordeiro, Harlow if you have them (About page)</li>
      <li>Any beach / creation / Southern California landscape frames (peace &amp; seasonal)</li>
    </ul>
    <div class="note orange">Also welcome in the same ZIP: the vector logo (SVG/EPS/AI) so the wordmark is pixel-perfect at every size, and any brand-font license files if Proxima Nova / DIN are licensed for web — otherwise the current Oswald + Source Sans pairing stays as the faithful web equivalent.</div>
  </div>
</div>
"""

write("SITE-AUDIT.html", "Site Audit & Launch Checklist — Lifetogether", BODY, active="", head=HEAD)
