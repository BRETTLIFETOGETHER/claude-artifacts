# CAN — Next Steps

Everything you need to take this from files in a chat to a live site at christianadvisornetwork.com.

---

## Straight answers first

**Is this live like a website?**
No. What you have are self-contained HTML files. They render inside Claude, and the AI generation works there because Claude supplies the model connection. Put those same files on a web server unchanged and every screen still works — profile, sliders, the 225 journeys, the calendar, the .ics export — but every "Generate" button fails, because there is no API key on the other end. This repo fixes that with a small server-side function.

**Can I set it up on christianadvisornetwork.com?**
No. I have no access to your domain, DNS, registrar, or hosting account, and I can't create accounts or push code on your behalf. You or a developer must do that. It is roughly 30 minutes of work and the steps are below.

**Can I load it to GitHub?**
Same answer — I can't push to a repo I have no credentials for. What I have done is build the complete repo, ready to drag into GitHub. You'll be pushing existing files, not writing code.

**One site or two?**
**One site, two doors.** Marketing pages at the root, the app at `/app` behind login. Reasons: one domain builds one brand and one SEO footprint; an RIA that reads the brochure is one tap from the demo; you run one analytics account and one deploy pipeline. Split into two sites only when the platform is sold under its own brand to firms that never hear the CAN story first. That is a year-two problem, not a launch problem.

---

## The 30-minute path to live

1. **Create the GitHub repo.** github.com → New repository → name it `can-platform` → Private. On the next screen use "uploading an existing file" and drag in everything from this folder.
2. **Create a Vercel account** at vercel.com and sign in with GitHub. Free tier is fine to start.
3. **Import the repo.** Vercel → Add New → Project → pick `can-platform` → Deploy. No build settings to change.
4. **Add the API key.** Vercel → your project → Settings → Environment Variables → add `ANTHROPIC_API_KEY` with a key from console.anthropic.com. Redeploy.
5. **Point the domain.** Vercel → Settings → Domains → add `christianadvisornetwork.com`. Vercel shows you two DNS records. Add them at your registrar (GoDaddy, Namecheap, wherever the domain lives). Propagation is usually under an hour.
6. **Test.** Visit the domain. Open `/app`. Press one Generate button. If it returns text, you are live.

At the end of this you have a public marketing site and a working demo. What you do **not** have yet: logins, saved data per advisor, or billing. Those are the MVP, not the demo.

---

## What is still missing for a real product

| Gap | Why it matters | Typical answer |
|---|---|---|
| Authentication | Advisors need private accounts | Clerk or Auth0 |
| Database | Right now a profile lives in one browser | Supabase or Neon (Postgres) |
| Multi-family | One advisor has 100 households, not one | Households table + list view |
| Firm rollup | The Firm tab is one household extrapolated | Real aggregate queries |
| Billing | No revenue without it | Stripe |
| Compliance | Advisor-facing output touches SEC marketing and books-and-records rules | Securities attorney + archiving |
| Security review | No RIA enterprise buys without it | SOC 2 via Vanta or Drata |

---

## Adding the 15,000-title library

Do **not** paste 15,000 rows into an HTML file. Past roughly 2,000 records the page gets slow to load and impossible to edit.

The included script handles it. Tested on 15,000 synthetic rows: **30 shards, a 200 KB index, a 556 KB search file, 3.1 MB total.**

```bash
# 1. Export your catalog to data/library.csv with this header:
#    id,category,title,subtitle,format,audience,tags
# 2. Run:
node scripts/build-library.mjs data/library.csv public/data
```

You get:
- `index.json` — categories and counts, loaded first, renders the browse screen instantly
- `search.json` — title/category pairs for instant client-side search across all 15,000
- `shard-N.json` — 500 full records each, fetched only when a category is opened

The page loads in under a second and never holds more than a few hundred records in memory. When you outgrow this — when advisors need to save favorites, or you want per-firm catalogs — move the same CSV into Postgres. The shape does not change.

**One thing to confirm:** I assumed the 15,000 is the LifeTogether campaign catalog. If it is something else, the header row above is the only thing that changes.

---

## Seven calls for Monday

I'm naming firms and roles rather than individuals — I can't verify who is available or any specific person's current situation, and a name I invented would waste your Monday.

**1. A senior full-stack contractor** — Gun.io, A.Team, or Toptal.
The ask: *"Next.js and Postgres. I have a working front end and a defined data model. I need auth, a households table, and Stripe in ten days."* Expect $10–20k for that scope. This is your single most important call.

**2. Vercel** (vercel.com, sales or partner directory).
Ask for their agency partner list if call #1 goes nowhere. Also confirms hosting is a non-issue.

**3. Clerk** (clerk.com).
Auth for multi-tenant B2B — advisors inside firms. A day of work, not a week. Confirm their organizations feature fits an RIA with 40 advisors.

**4. Supabase or Neon.**
Postgres with an instant API. Ask about row-level security so one firm can never read another firm's households. This is the question an RIA's diligence will ask you.

**5. A securities regulatory attorney** — someone who does investment adviser compliance, not general corporate.
Ask specifically about the SEC Marketing Rule and books-and-records when AI drafts client-facing material. Get this opinion *before* the first firm pilots, not after. Your state's investment adviser association or a Kingdom Advisors referral is the fastest route.

**6. Vanta or Drata.**
SOC 2 readiness. You do not need the certificate to pilot, but enterprise RIAs will ask, and starting the clock early is cheap.

**7. Your design-partner RIA.**
Not a vendor — a friendly firm willing to be customer zero. You already know who this is. The ask: *"Ten of your families, ninety days, free, in exchange for telling me everything that's wrong with it."* Nothing on this list matters if that call doesn't happen.

---

## What a real 10-day MVP looks like

- **Days 1–2** — repo live on the domain, auth working, one advisor can log in
- **Days 3–5** — households in a database; an advisor creates and switches between families
- **Days 6–7** — generation persisted, so a document survives a refresh; the 15,000-title library loaded
- **Days 8–9** — firm view over real households; Stripe for one plan
- **Day 10** — design-partner walkthrough

Realistic with one strong contractor. Tight with two. Impossible with a committee.

**Do first, before any of it:** make call #7. A pilot firm on the calendar changes every other decision on this page.
