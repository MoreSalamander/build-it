// Vercel serverless function — thin Anthropic proxy.
// The API key lives ONLY here (server-side), never in the browser.
// The front-end's deterministic checks run client-side; this endpoint is
// only for the LLM *voicing* (helper explanations + setup interview).
//
// Endpoint: POST /api/chat   { system?, prompt }  ->  { text }
// Requires env var: ANTHROPIC_API_KEY  (set it in the Vercel dashboard)

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "POST only" });
  }
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) {
    return res.status(500).json({ error: "ANTHROPIC_API_KEY is not set" });
  }

  try {
    const body = typeof req.body === "string" ? JSON.parse(req.body || "{}") : (req.body || {});
    const { system, prompt } = body;

    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        // Swap the model if you prefer; a small/cheap model is plenty for voicing.
        model: "claude-3-5-haiku-latest",
        max_tokens: 700,
        system:
          system ||
          "You are a calm, encouraging coding helper for absolute beginners. " +
          "You are given deterministic findings about the learner's code; explain them " +
          "plainly and kindly. Never invent errors that aren't in the findings.",
        messages: [{ role: "user", content: String(prompt || "") }],
      }),
    });

    const data = await r.json();
    const text = data?.content?.[0]?.text || "";
    return res.status(200).json({ text });
  } catch (e) {
    return res.status(500).json({ error: String(e) });
  }
}
