# Chapter 3 — A living sky

**You'll build:** a sky full of stars that gently twinkle.
**You'll learn:** keeping many things in a *list*, repeating with a *for loop*, and
the *game loop* — the heartbeat that powers every moving thing from here on.
**Starts from:** your finished Chapter 2 `main.py`. **Four steps.**

> This is the chapter where your program stops being a picture and starts being
> *alive*. We'll take the loop slowly — it's the most important piece in the project.

---

## Step 1 — Bring in randomness

**What you're adding:** a second built-in toolkit, for random numbers.

**The code** *(add it right under `import tkinter as tk`)*
```python
import random
```

**What it does:** `random` is another toolkit that ships inside Python. It makes
random numbers. We'll use it to scatter the stars so no two skies ever look alike.

**Why it matters:** a real night sky isn't a neat grid — randomness is what makes it
feel natural. You'll reach for `random` again on every firework, to throw its sparks
out in all directions.

**Run it — what you'll see:** nothing new, no error. We only loaded a toolkit.

**Checkpoint:** ✅ it ran with no red text.

**If it's not right:**
- *An error* → check the spelling: `import random`, all lowercase.

---

## Step 2 — Scatter a sky full of stars

**What you're adding:** a hundred little stars, in random spots.

**The code** *(add after the moon lines, above `window.mainloop()`)*
```python
stars = []
for i in range(100):
    x = random.randint(0, 1200)
    y = random.randint(0, 400)
    size = random.choice([1, 1, 1, 2])
    star = canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
    stars.append({"id": star, "brightness": random.uniform(0.5, 1.0), "speed": random.uniform(0.01, 0.03)})
```

**What it does:** `stars = []` makes an empty **list** — a container to keep all our
stars in. `for i in range(100):` runs the indented lines **100 times**. Each time we
pick a random spot in the upper sky (`x` across, `y` in the top half), a random tiny
`size`, draw a little white oval there — and then *remember* that star by adding a
small note-card to the list: its `id` (so we can change it later), a starting
`brightness`, and a `speed` for how fast it'll twinkle. (We use brightness and speed
two steps from now.)

**Why it matters:** this is your first **list** and your first **for loop** — "keep
many things" and "do this many times." It's how you make 100 of something without
writing 100 lines. Every firework explosion uses this exact idea to spray dozens of
sparks at once.

**Run it — what you'll see:** the upper sky fills with a scatter of tiny white stars.
(Still, for now — they'll twinkle soon.)

**Checkpoint:** ✅ a sky full of little white stars across the top.

**If it's not right:**
- *No stars* → the block must come after `canvas.pack()`.
- *Indentation error* → the five lines under `for` must all be indented the same
  amount (four spaces).
- *All stars in one place* → make sure `x` and `y` each use `random.randint`.

---

## Step 3 — Start the heartbeat

**What you're adding:** the game loop — a block of code that runs over and over.

**The code** *(add after the stars, above `window.mainloop()`)*
```python
def tick():
    window.after(16, tick)

tick()
```

**What it does:** `def tick():` creates a reusable block of instructions named
`tick`. For now it does just one thing: `window.after(16, tick)` asks the window to
run `tick` again in 16 milliseconds. So `tick` keeps re-running about 60 times a
second, forever. The last line, `tick()`, starts it off the first time.

**Why it matters:** this is **the heartbeat** — the most important machine in the
whole project. Everything that *moves* — twinkling stars, rising rockets, falling
sparks — happens because this loop runs many times a second and changes things a
little each time. (We use `window.after` instead of letting `tick` call itself
directly, because calling itself would freeze the program. `after` politely takes
turns with the window.)

**Run it — what you'll see:** nothing changes — the stars sit still, no error. That's
right: the engine is now running, it just has no job inside it yet. We give it one
next.

**Checkpoint:** ✅ everything looks exactly as before, no red error. (A running loop
with no job looks identical — that's expected.)

**If it's not right:**
- *The window freezes / spins* → the line inside must be `window.after(16, tick)`,
  **not** `tick()`. Calling `tick()` directly inside itself freezes everything.
- *`tick is not defined`* → the `tick()` start line must come *after* the
  `def tick():` block.

---

## Step 4 — Make them twinkle

**What you're adding:** the loop's first real job — softly brightening and dimming
each star.

**The code** *(add these lines **inside** `tick`, just above the
`window.after(16, tick)` line)*
```python
    for star in stars:
        star["brightness"] += (random.random() - 0.5) * star["speed"]
        star["brightness"] = max(0.3, min(1.0, star["brightness"]))
        gray = int(star["brightness"] * 255)
        canvas.itemconfig(star["id"], fill=f"#{gray:02x}{gray:02x}{gray:02x}")
```

**What it does:** every frame, we walk through each star's note-card and nudge its
`brightness` up or down by a tiny random amount (its `speed`). The
`max(0.3, min(1.0, ...))` line keeps brightness from going too dark or past full.
Then we turn that brightness into a shade of gray and repaint the star with
`canvas.itemconfig` — which *changes* a shape we already drew instead of drawing a
new one. (That last `f"#{gray:02x}..."` line's only job is to turn the brightness
number into a color — you don't need to memorize its shape, just know that's what it
does.)

**Why it matters:** this is the pattern behind **all** animation here — each frame,
change something a little. `itemconfig` (change what's already there) is how we'll
move rockets and fade sparks too, without redrawing the whole sky each time. And
because the drift is tiny and slow, the stars *shimmer* softly instead of strobing.

**Run it — what you'll see:** 🎆 the stars **twinkle** — each one softly brightening
and dimming on its own. Your sky is alive.

**Checkpoint:** ✅ the stars gently shimmer (a soft flicker, not harsh flashing).
**That's Beat 2 — a living sky.**

**If it's not right:**
- *Nothing twinkles* → the new lines must be **inside** `tick` (indented under it)
  and **above** the `window.after` line.
- *Stars flash wildly* → the change must be multiplied by `star["speed"]` (a tiny
  number); double-check that part.
- *`KeyError: 'brightness'`* → make sure Step 2's note-card included `"brightness"`
  and `"speed"`.

---

## Chapter 3 complete

Your `main.py` now reads:

```python
import tkinter as tk
import random

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

# Scatter the stars
stars = []
for i in range(100):
    x = random.randint(0, 1200)
    y = random.randint(0, 400)
    size = random.choice([1, 1, 1, 2])
    star = canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
    stars.append({"id": star, "brightness": random.uniform(0.5, 1.0), "speed": random.uniform(0.01, 0.03)})

# The heartbeat: runs about 60 times a second
def tick():
    for star in stars:
        star["brightness"] += (random.random() - 0.5) * star["speed"]
        star["brightness"] = max(0.3, min(1.0, star["brightness"]))
        gray = int(star["brightness"] * 255)
        canvas.itemconfig(star["id"], fill=f"#{gray:02x}{gray:02x}{gray:02x}")
    window.after(16, tick)

tick()

window.mainloop()
```

A living night sky — moon, stars, and a heartbeat. **You can stop here.** Next, that
heartbeat earns its keep: in Chapter 4 you click, and a rocket flies.

➡️ **Next: Chapter 4 — Launch a rocket**
