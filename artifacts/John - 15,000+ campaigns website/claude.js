// netlify/functions/claude.js
// Server-side proxy for the Anthropic Messages API.
// The browser calls THIS; this function attaches the key. The key never leaves the server.
//
// Set in Netlify → Site settings → Environment variables:
//   ANTHROPIC_API_KEY = sk-ant-...
//
// Optional:
//   ALLOWED_ORIGIN = https://40daycampaigns.com   (defaults to "*")

const ANTHROPIC_URL = "https://api.anthropic.com/v1/messages";
const MODEL_ALLOW = new Set(["claude-sonnet-4-6", "claude-haiku-4-5-20251001"]);

exports.handler = async (event) => {
  const origin = process.env.ALLOWED_ORIGIN || "*";
  const cors = {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Content-Type": "application/json",
  };

  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: cors, body: "" };
  if (event.httpMethod !== "POST")
    return { statusCode: 405, headers: cors, body: JSON.stringify({ error: "POST only" }) };

  const key = process.env.ANTHROPIC_API_KEY;
  if (!key)
    return { statusCode: 500, headers: cors, body: JSON.stringify({ error: "Server not configured: ANTHROPIC_API_KEY is missing." }) };

  let body;
  try { body = JSON.parse(event.body || "{}"); }
  catch { return { statusCode: 400, headers: cors, body: JSON.stringify({ error: "Bad JSON" }) }; }

  // Whitelist what the client may control; the server owns everything sensitive.
  const model = MODEL_ALLOW.has(body.model) ? body.model : "claude-sonnet-4-6";
  const max_tokens = Math.min(Math.max(parseInt(body.max_tokens, 10) || 1800, 64), 4096);
  const messages = Array.isArray(body.messages) ? body.messages.slice(0, 12) : [];
  const system = typeof body.system === "string" ? body.system.slice(0, 8000) : undefined;
  if (!messages.length)
    return { statusCode: 400, headers: cors, body: JSON.stringify({ error: "messages required" }) };

  try {
    const ctl = new AbortController();
    const timer = setTimeout(() => ctl.abort(), 55000);
    const res = await fetch(ANTHROPIC_URL, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({ model, max_tokens, system, messages }),
      signal: ctl.signal,
    });
    clearTimeout(timer);
    const text = await res.text();
    // Pass Anthropic's response straight through (status + JSON body).
    return { statusCode: res.status, headers: cors, body: text };
  } catch (e) {
    const offline = e.name === "AbortError";
    return {
      statusCode: offline ? 504 : 502,
      headers: cors,
      body: JSON.stringify({ error: offline ? "Upstream timeout" : "Upstream error", detail: String(e.message || e) }),
    };
  }
};
