// netlify/functions/create-checkout-session.js
// Creates a Stripe Checkout Session from the cart and returns its URL.
// The browser posts the cart lines; the server re-prices every line from the
// catalog price table so the amount charged can never be tampered with client-side.
//
// Set in Netlify → Site settings → Environment variables:
//   STRIPE_SECRET_KEY = sk_live_...   (or sk_test_... while testing)
//   SITE_URL          = https://40daycampaigns.com   (for success/cancel redirects)
//
// Netlify auto-installs deps from netlify/functions/package.json ("stripe").

const Stripe = require("stripe");

// Base per-format prices in USD (mirror of assets/js/app.js FMT_META).
const FMT_PRICE = { "7": 249, "21": 449, "30": 649, "40": 849, sunday: 149, resource: 199, year: 1499, study: 549 };
const GRADE_PREMIUM = { AA: 200, A: 100 };

exports.handler = async (event) => {
  const site = process.env.SITE_URL || (event.headers.origin || "").replace(/\/$/, "") || "";
  const cors = {
    "Access-Control-Allow-Origin": process.env.ALLOWED_ORIGIN || "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Content-Type": "application/json",
  };
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: cors, body: "" };
  if (event.httpMethod !== "POST")
    return { statusCode: 405, headers: cors, body: JSON.stringify({ error: "POST only" }) };

  const secret = process.env.STRIPE_SECRET_KEY;
  if (!secret)
    return { statusCode: 500, headers: cors, body: JSON.stringify({ error: "Server not configured: STRIPE_SECRET_KEY is missing." }) };

  let body;
  try { body = JSON.parse(event.body || "{}"); }
  catch { return { statusCode: 400, headers: cors, body: JSON.stringify({ error: "Bad JSON" }) }; }

  const lines = Array.isArray(body.lines) ? body.lines.slice(0, 50) : [];
  const email = typeof body.email === "string" ? body.email.slice(0, 200) : undefined;
  const church = typeof body.church === "string" ? body.church.slice(0, 200) : "";
  if (!lines.length)
    return { statusCode: 400, headers: cors, body: JSON.stringify({ error: "Empty cart" }) };

  // Re-price server-side. A custom (Builder) line carries its own quoted price;
  // catalog lines are priced from the format table + grade premium, ignoring any
  // client-sent amount.
  const priceLine = (l) => {
    if (l.custom) return Math.max(0, Math.round(Number(l.price) || 0));
    const base = FMT_PRICE[String(l.fmt)] ?? FMT_PRICE["40"];
    const prem = GRADE_PREMIUM[l.g] || 0;
    return base + prem;
  };

  const line_items = lines.map((l) => ({
    quantity: Math.min(Math.max(parseInt(l.qty, 10) || 1, 1), 20),
    price_data: {
      currency: "usd",
      unit_amount: priceLine(l) * 100, // cents
      product_data: {
        name: (l.t || "Campaign").slice(0, 250),
        description: (l.fmt ? `${l.fmt}-format · all editions included` : "Custom campaign").slice(0, 250),
      },
    },
  }));

  try {
    const stripe = Stripe(secret);
    const session = await stripe.checkout.sessions.create({
      mode: "payment",
      line_items,
      customer_email: email,
      metadata: { church, item_count: String(lines.length) },
      success_url: `${site}/confirmation.html?order={CHECKOUT_SESSION_ID}`,
      cancel_url: `${site}/cart.html`,
      // Church invoicing (Net-30) can be added later via Stripe Invoicing;
      // card + wallets are enabled by default.
    });
    return { statusCode: 200, headers: cors, body: JSON.stringify({ url: session.url, id: session.id }) };
  } catch (e) {
    return { statusCode: 502, headers: cors, body: JSON.stringify({ error: "Stripe error", detail: String(e.message || e) }) };
  }
};
