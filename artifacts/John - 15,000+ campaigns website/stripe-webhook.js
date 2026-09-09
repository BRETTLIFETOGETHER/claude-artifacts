// netlify/functions/stripe-webhook.js
// OPTIONAL. Verifies Stripe events and is where you'd record fulfillment
// (email the downloads, mark the order paid in your database, etc.).
// Not required for the storefront to function — the confirmation page already
// unlocks the starter downloads on return — but recommended for real receipts.
//
// Set in Netlify → Environment variables:
//   STRIPE_SECRET_KEY     = sk_live_...
//   STRIPE_WEBHOOK_SECRET = whsec_...   (from the Stripe dashboard endpoint you create)
// Point a Stripe webhook at: https://YOURSITE/.netlify/functions/stripe-webhook
// listening for: checkout.session.completed

const Stripe = require("stripe");

exports.handler = async (event) => {
  const secret = process.env.STRIPE_SECRET_KEY;
  const whsec = process.env.STRIPE_WEBHOOK_SECRET;
  if (!secret || !whsec) return { statusCode: 500, body: "Webhook not configured" };

  const stripe = Stripe(secret);
  const sig = event.headers["stripe-signature"];
  let evt;
  try {
    // Netlify delivers the raw body; verify the signature against it.
    const raw = event.isBase64Encoded ? Buffer.from(event.body, "base64") : event.body;
    evt = stripe.webhooks.constructEvent(raw, sig, whsec);
  } catch (e) {
    return { statusCode: 400, body: `Signature verification failed: ${e.message}` };
  }

  if (evt.type === "checkout.session.completed") {
    const s = evt.data.object;
    // TODO: fulfillment — s.customer_email, s.metadata.church, s.amount_total.
    // e.g. send the four editions, create a receipt, write to your store of record.
    console.log("Paid:", s.id, s.customer_email, s.metadata && s.metadata.church, s.amount_total);
  }
  return { statusCode: 200, body: JSON.stringify({ received: true }) };
};
