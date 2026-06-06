# Build It (remaster)

A calm, page-by-page "build manual" for absolute beginners. First project:
**Firework Simulator** (Python / Tkinter, easy tier) — eight chapters from an empty
file to a clickable night sky full of fireworks.

A MoreSalamander StudioLabs production. Made the way Lego makes a manual: all the
hard work goes into production, so the build itself is effortless.

## Layout

```
index.html · styles.css · app.js     the static reader
data.js                              the project SOT (frozen content, all 8 chapters)
api/chat.js                          serverless Anthropic proxy (LLM voicing; key server-side)
reference/firework-tkinter/          the verified source app + SPEC.md (factory input)
chapters/firework-tkinter/           the authored chapters + runnable firework_complete.py
```

The site is served from the repo root (no build step). The deterministic
"check my code" runs client-side; the LLM helper + setup interview (phase 2) call
`/api/chat`. Learner progress lives in `localStorage` — no database.

## Run locally

```
python3 -m http.server 8011
# open http://localhost:8011
```

## Deploy (Vercel)

1. Push to GitHub.
2. vercel.com → Add New → Project → import the repo.
3. Framework preset: **Other**. No build step, nothing to configure — the site lives
   at the repo root and deploys as-is.
4. (Optional, for the phase-2 chat) add an env var **ANTHROPIC_API_KEY**.
5. Deploy.

The static reader is fully functional with no key — the chat backend is additive.
