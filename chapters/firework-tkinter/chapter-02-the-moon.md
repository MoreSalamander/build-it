# Chapter 2 — The moon

**You'll build:** a glowing moon hanging in the top-right of your night sky.
**You'll learn:** how to draw shapes on the canvas, place them with corner numbers,
and stack them front-to-back.
**Starts from:** your finished Chapter 1 `main.py`. **Three steps.**

> All three lines go in `main.py`, just above `window.mainloop()`.

---

## Step 1 — The moon's glow

**What you're adding:** a soft halo where the moon will sit.

**The code**
```python
canvas.create_oval(1040, 20, 1160, 140, fill="#3a3a5a", outline="")
```

**What it does:** `create_oval` draws an oval on the canvas. The four numbers are the
corners of an invisible **box** — top-left `(1040, 20)` and bottom-right
`(1160, 140)` — and Tkinter draws the biggest oval that fits inside it. The box is
square, so you get a circle. `fill` is its color; `outline=""` removes the default
black edge so it blends softly into the night.

**Why it matters:** this is your first drawing — and *everything* visual in this
project (the moon, the stars, every rocket and spark) is a shape drawn on the canvas
exactly like this. Those four corner numbers are how you place anything; nudge them
and the shape moves.

**Run it — what you'll see:** a soft, dim halo — a gentle lighter patch of blue-gray
— up in the top-right. Not bright; just a glow. The moon itself lands inside it next.

**Checkpoint:** ✅ a faint round glow in the top-right corner.

**If it's not right:**
- *Nothing appeared* → the line must come **after** `canvas.pack()` and **before**
  `window.mainloop()`.
- *A black ring around it* → check `outline=""` — two quotes with nothing between.

---

## Step 2 — The moon

**What you're adding:** the bright moon itself, sitting on top of the glow.

**The code**
```python
canvas.create_oval(1070, 50, 1130, 110, fill="#ffffdc", outline="")
```

**What it does:** another oval, in a smaller box centered on the same spot, filled
pale moon-yellow. Because we draw it **after** the glow, it sits in *front* of it —
that's the rule: whatever you draw later lands on top.

**Why it matters:** "later draws on top" — draw order, or *layering* — is one of the
most useful things to know about the canvas. It's exactly why the glow had to come
first: so the moon could shine in front of it.

**Run it — what you'll see:** a bright pale-yellow moon appears, glowing softly
inside its halo in the top-right.

**Checkpoint:** ✅ a bright round moon centered in the glow.

**If it's not right:**
- *The moon is hidden, or the glow looks on top* → make sure the moon line comes
  **after** the glow line.
- *Moon is off to one side* → check its four numbers: `1070, 50, 1130, 110`.

---

## Step 3 — Craters

**What you're adding:** two little shadow spots, for depth.

**The code**
```python
canvas.create_oval(1087, 70, 1097, 80, fill="#e6e6c8", outline="")
canvas.create_oval(1095, 83, 1113, 91, fill="#e6e6c8", outline="")
```

**What it does:** two more small ovals in a slightly darker cream, drawn on top of
the moon's face. Small boxes make small ovals; they read as gentle craters.

**Why it matters:** tiny details like these are what make something feel *real*
instead of flat — the same instinct will make sparks shimmer later. And notice
you're now stacking shapes with confidence: glow, then moon, then craters, each one
landing in front of the last.

**Run it — what you'll see:** two small spots appear on the moon's face, giving it a
touch of depth. Your moon is finished.

**Checkpoint:** ✅ a glowing moon with two small craters, top-right. **That's Beat 3
— the moon.**

**If it's not right:**
- *The spots don't show* → both lines must come **after** the moon line.
- *Want them somewhere else* → these four-number boxes just place two little spots.
  Nudge the numbers and move them wherever you like.

---

## Chapter 2 complete

Your `main.py` now reads:

```python
import tkinter as tk

window = tk.Tk()
window.title("Firework Simulator")
window.resizable(False, False)

canvas = tk.Canvas(window, width=1200, height=800, bg="#0a0a1e", highlightthickness=0)
canvas.pack()

# The moon's glow
canvas.create_oval(1040, 20, 1160, 140, fill="#3a3a5a", outline="")
# The moon
canvas.create_oval(1070, 50, 1130, 110, fill="#ffffdc", outline="")
# Craters
canvas.create_oval(1087, 70, 1097, 80, fill="#e6e6c8", outline="")
canvas.create_oval(1095, 83, 1113, 91, fill="#e6e6c8", outline="")

window.mainloop()
```

A night sky with a moon in it — and you can **stop here** with something that runs.
When you're ready, Chapter 3 fills the sky with stars and makes them twinkle (and
that's where your program comes alive).

➡️ **Next: Chapter 3 — A living sky**
