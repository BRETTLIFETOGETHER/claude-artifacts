/* Claude connection — powers "Enhance with Claude" across the Builder tools.
   Inside Claude-hosted contexts this endpoint works as-is (no key required).
   ------------------------------------------------------------------------
   SELF-HOSTING SEAM: when serving 40daycampaigns.com from your own domain,
   route this call through a tiny backend proxy that attaches your Anthropic
   API key server-side (never ship a key to the browser):
       const ENDPOINT = "https://YOUR-BACKEND/claude";   // forwards to
       // https://api.anthropic.com/v1/messages with x-api-key + anthropic-version
   Everything else in this file stays unchanged.
   ------------------------------------------------------------------------ */
(function(){
"use strict";
const ENDPOINT = "https://api.anthropic.com/v1/messages";
const MODEL = "claude-sonnet-4-6";

async function ask({system, user, max=1800, timeout=30000}){
  if (typeof fetch !== "function") throw new Error("offline");
  const ctl = new AbortController();
  const t = setTimeout(()=>ctl.abort(), timeout);
  try{
    const res = await fetch(ENDPOINT, {
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body: JSON.stringify({model: MODEL, max_tokens: max,
        system, messages:[{role:"user", content:user}]}),
      signal: ctl.signal
    });
    if(!res.ok) throw new Error("http "+res.status);
    const data = await res.json();
    const text = (data.content||[]).filter(b=>b.type==="text").map(b=>b.text).join("\n");
    if(!text) throw new Error("empty");
    return text;
  } finally { clearTimeout(t); }
}

function stripFences(s){return s.replace(/^```(?:json|html|markdown)?\s*/i,"").replace(/```\s*$/,"").trim()}
async function askJSON(opts){
  const text = await ask({...opts,
    system:(opts.system||"")+"\nRespond with ONLY valid JSON. No preamble, no markdown fences."});
  return JSON.parse(stripFences(text));
}

const VOICE = "You write in the Lifetogether / Rick Warren pastoral register: warm, direct, second person, short sentences, zero jargon, zero hype. Scripture references must be real, NIV-standard, correctly abbreviated. Never invent quotes or facts about real people.";

window.AI = {
  ask, askJSON, VOICE, MODEL,
  async enhanceCampaign(inputs, draft){
    return askJSON({max:2200, system:VOICE+" You are Lifetogether's senior campaign architect.",
      user:`A pastor is building a custom churchwide campaign.
Pastor's message (one sentence): ${inputs.idea}
Anchor texts they named: ${inputs.texts||"none"}
Voice: ${inputs.voice}. Channel: ${inputs.channelName}. Format: ${inputs.days}-day (${inputs.sessions} weekend sessions). Launch window: ${inputs.when}. Editions: ${inputs.eds}.
Here is our engine's first draft for reference: ${JSON.stringify(draft)}
Improve it. Return JSON: {"title":str,"altTitles":[3 str],"bigIdea":str,"weeks":[{"n":int,"theme":one-word str,"title":str,"text":ref,"summary":2-sentence str}],"sampleDay":{"word":str,"ref":str,"body":[3 short paragraphs],"step":str,"prayer":str}}. Weeks length = ${inputs.sessions}.`});
  },
  async enhanceSermon(inputs, draft){
    return ask({max:2200, system:VOICE+" You are a veteran preaching coach.",
      user:`Rewrite and deepen this sermon build as a preachable outline with 2–3 manuscript-quality sentences per movement. Keep the structure (big idea, three movements with texts, two illustrations, landing/response). Audience: ${inputs.audience}. Length: ${inputs.minutes} minutes. Voice: ${inputs.voice}. Topic/passage: ${inputs.topic}. ${inputs.big?("Pastor's big idea: "+inputs.big):""}
Engine draft: ${JSON.stringify(draft)}
Return clean HTML using only <h3>, <p>, <b>, <i>, <ol>, <li>.`});
  },
  async enhanceGroup(inputs, draft){
    return ask({max:2200, system:VOICE+" You design small-group curriculum any volunteer host can run.",
      user:`Deepen this ${inputs.sessions}-session small group guide on "${inputs.topic}" for a ${inputs.gtype} group (${inputs.depth} depth). Keep the session order: Open, Watch, Discuss (4 questions), Practice, Pray. Sharpen questions so they surface real stories, not right answers.
Engine draft: ${JSON.stringify(draft)}
Return clean HTML using only <h3>, <p>, <b>, <ol>, <li>.`});
  }
};
})();
