# Firework Simulator (Tkinter) — Verified Behavior Spec

**Status:** Ground truth established (Factory Step 1 complete)
**Reference:** this folder — a *corrected copy*. Original frozen at `~/firework_sim_tkinter/` (the "before" receipt; do not touch).

This one list is three things at once: the **spec** the code is held to, the
**assertions** the gate will check, and the **chapter map** (each beat ends a chapter).

## Intended observable behaviors — every beat is something you can SEE

- **B1 — Night.** Window opens and fills with a dark night sky (fixed size).
- **B2 — Stars.** Stars scatter across the upper sky and twinkle.
- **B3 — Moon.** A moon hangs top-right (glow + body + craters).
- **B4 — Launch.** Click → a glowing rocket rises from the bottom, trailing white.
- **B5 — Burst.** The rocket reaches its peak and bursts into a sphere of colored sparks.
- **B6 — Fall & fade.** Sparks arc, fall under gravity, slow (drag), fade, then die.
- **B7 — Six shapes.** Keys 1–6 select six *visibly distinct* explosions:
  rocket (sphere) · peony · willow · palm · ring · cracker.
- **B8 — Controls.** Space = random launch; R = auto-show (~every 1.5s);
  C = clear; a live stats panel (FPS / active / particles / type).

~8 beats ≈ ~8 chapters. Each chapter ends when its beat is true on screen.

## Declared intended (NOT bugs — don't "fix", don't checkpoint against)

- Click ignores the y-coordinate: rockets always launch from the ground
  (physically correct). No checkpoint should expect launch-at-cursor.

## Step 1(b) fixes applied to this copy (legacy transcription errors — one-off)

These were hand-typing artifacts in the original; the normal ingest path generates
clean code, so this class of fix is specific to fireworks.

- `firework.py` — patterns key `'peonyy'` → `'peony'` (key 2 silently rendered a plain sphere)
- `main.py` — `launch_random` `'wilow'` → `'willow'` (random/auto-show never produced willows)
- `main.py` — printed strings `Selfected`→`Selected`, `Cleard`→`Cleared`
- `firework.py` — stray comment `'exploded'abs` → `'exploded'`
- Verified: all 4 files compile; the six names agree across keybind list,
  `launch_random` list, and the patterns dict.

## Still open — needs a display run

Static checks (compile + name agreement) are necessary but not sufficient.
**B7's "visibly distinct"** must be eyeballed by running `python3 main.py` on a
machine with a display. That's the one assertion a compile can't prove.
