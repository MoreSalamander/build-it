# Build It (remaster)

A calm, page-by-page "build manual" for absolute beginners. First project:
**Firework Simulator** (Python / Tkinter, easy tier) — eight chapters from an empty
file to a clickable night sky full of fireworks.

A MoreSalamander StudioLabs production. Made the way Lego makes a manual: all the
hard work goes into production, so the build itself is effortless.

## Layout

```
web/                  ← the deployed site (Vercel "Root Directory" = web)
  index.html · styles.css · app.js
  data.js             the project SOT (frozen content, all 8 chapters)
  api/chat.js         serverless Anthropic proxy (LLM voicing; key stays server-side)
reference/firework-tkinter/   the verified source app + SPEC.md (factory input)
chapters/firework-tkinter/    the authored chapters + the runnable firework_complete.py
```

The deterministic "check my code" runs client-side. The LLM helper + setup interview
(phase 2) call `/api/chat`. Learner progress lives in `localStorage` — no database.

## Run locally

```
cd web && python3 -m http.server 8011
# open http://localhost:8011
```

## Deploy (Vercel)

1. Push this repo to GitHub.
2. On vercel.com → **Add New → Project** → import the repo.
3. Set **Root Directory** to `web`. Framework preset: **Other** (no build step).
4. Add an environment variable **ANTHROPIC_API_KEY** (only needed once the chat is
   wired; the static reader works without it).
5. Deploy. Add a custom domain when ready.

The static reader is fully functional with no key — the chat backend is additive.
