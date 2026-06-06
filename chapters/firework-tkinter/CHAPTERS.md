# Firework Simulator (Tkinter, easy tier) — Chapter Map

Derived milestone-first from `reference/firework-tkinter/SPEC.md`. Each chapter ends
when its observable beat is true on screen. Wow rises top to bottom.

| Beat | Chapter | Where it lives in the reference |
|---|---|---|
| B1 Night | **Ch1 — The night sky** | `Tk()` + `Canvas` + dark bg + `mainloop()` |
| B3 Moon | **Ch2 — The moon** | `create_moon()` — static drawing |
| B2 Stars | **Ch3 — A living sky** | `create_stars()` + game loop (`root.after`) + twinkle |
| B4 Launch | **Ch4 — Launch a rocket** | `Firework` (launching) + `on_click` + trail render |
| B5 Burst | **Ch5 — The big bang** | `explode()` + `create_sphere()` + `Particle` + render |
| B6 Fall & fade | **Ch6 — Gravity & fade** | `Particle.update()` physics + fade + cleanup |
| B7 Six shapes | **Ch7 — Six fireworks** | `create_willow/palm/ring/cracker` + `set_type` + keys 1–6 |
| B8 Controls | **Ch8 — The show** | random / auto-show / clear + the stats panel |

## Build-order note

This is a build *order*, not a line-range slice. The reference does everything at
once inside one `update()`/`render()`; our chapters make the loop *accrete*
responsibilities (first it only twinkles stars; later it flies rockets). The
reference defines the **target behavior**; intermediate chapters are simpler
versions that grow. The gate proves the final reconstruction matches the reference.

## Authoring decisions (easy tier)

1. **Single file, procedural, hardcoded** — not the reference's class + `config.py`
   split. Structure (a class, maybe a config split) arrives in a later chapter when
   complexity earns it. The three-stage spirit (simple → structured) re-emerges
   naturally rather than being imposed.
2. **`mainloop` is taught through the flash-and-vanish trap** (Ch1 Step 2 → Step 3):
   the #1 silent beginner failure becomes a calm, expected, inoculating lesson.

## Status

- Ch1 — drafted (`chapter-01-night-sky.md`)
- Ch2 — drafted (`chapter-02-the-moon.md`)
- Ch3 — drafted (`chapter-03-a-living-sky.md`)
- Ch4 — drafted (`chapter-04-launch-a-rocket.md`)
- Ch5 — drafted (`chapter-05-the-big-bang.md`)
- Ch6 — drafted (`chapter-06-gravity-and-fade.md`)
- Ch7 — drafted (`chapter-07-six-fireworks.md`)
- Ch8 — drafted (`chapter-08-the-show.md`)
- **All 8 chapters drafted ✅** — outstanding: a real display run + per-shape eyeball (B7) on a screen.
