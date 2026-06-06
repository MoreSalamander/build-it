# Chapter 1 — The night sky

**You'll build:** a window that opens and fills with deep-blue night — the stage
every firework in this project happens on.
**You'll learn:** how to open a window, keep it open, and paint a drawing surface.
**Starts from:** an empty folder. **Five steps.**

> Make a new file called `main.py`. Everything in this chapter goes in that one file.

---

## Step 1 — Load the toolkit

**What you're adding:** the line that gives you Python's window-and-drawing tools.

**The code**
```python
import tkinter as tk
```

**What it does:** `tkinter` is the toolkit built into Python for making windows,
buttons, and drawings. `import` brings it in; `as tk` gives it a short nickname so
you can type `tk` instead of `tkinter` everywhere.

**Why it matters:** every visible thing you build — the window, the stars, the
fireworks — comes from this toolkit. And it ships *inside* Python, so there's
nothing to install. This one line is the door.

**Run it — what you'll see:** `python3 main.py` → **nothing.** No window, no error,
just your prompt again. That's exactly right; we only opened the toolbox.

**Checkpoint:** ✅ it ran and gave you back your prompt with no red text.

**If it's not right:**
- *`No module named tkinter`* → rare; your Python was built without Tk. Paste it to
  the helper — this is a setup issue, not your code.
- *Any other error* → check the spelling: `import tkinter as tk`, all lowercase.

---

## Step 2 — Make a window

**What you're adding:** the window itself.

**The code**
```python
window = tk.Tk()
```

**What it does:** `tk.Tk()` creates the main application window and hands it back to
you. We store it in a box named `window` so we can talk to it later.

**Why it matters:** this is the container everything else lives inside — the frame
around your whole night sky.

**Run it — what you'll see:** the window will **blink open and instantly vanish**
(or you may see nothing at all). **That's expected.** You just met the most common
surprise in beginner programming — and the next step cures it for good.

**Checkpoint:** ✅ it ran with no red error. (The blink-and-vanish is *not* a
failure here — it's the lesson.)

**If it's not right:**
- *Red error* → check the capitals: it's `tk.Tk()` — lowercase `tk`, capital `T`,
  lowercase `k`.

---

## Step 3 — Tell the window to stay

**What you're adding:** one line that keeps your window on screen.

**The code** *(add it as the very last line of your file)*
```python
window.mainloop()
```

**What it does:** `mainloop()` starts Tkinter's *event loop* — a little engine that
keeps running, watching for things like clicks, key presses, and the close button.
Without it, your program reaches the end of the file and quits instantly, taking the
window with it. With it, the program stays alive and waits for you.

**Why it matters:** every Tkinter app you'll ever build ends with this line — it's
the heartbeat. And it's the same loop that, a few chapters from now, will let you
*click to launch a firework*. It's already listening; we just haven't given it
anything to listen for yet.

**Run it — what you'll see:** a small empty gray window opens and **stays open**
until you click its close button. (Last step it blinked and vanished — this is the
cure.)

**Checkpoint:** ✅ the window opened and *stayed*. Not sure? Paste what happened to
the helper and it'll tell you.

**If it's not right:**
- *Still blinks and vanishes* → `mainloop()` must be the **very last line**, not
  indented inside anything.
- *Red error mentioning `mainloop`* → check the spelling: one word, all lowercase.

---

## Step 4 — Name it and lock the size

**What you're adding:** a title, and a fixed size.

**The code** *(add these just above `window.mainloop()`)*
```python
window.title("Firework Simulator")
window.resizable(False, False)
```

**What it does:** `title(...)` sets the text in the window's title bar.
`resizable(False, False)` stops the window from being dragged bigger or smaller —
the two `False`s are for width and height.

**Why it matters:** our night sky is a fixed-size *stage*. Locking it keeps the
layout predictable, so later the moon, the stars, and every firework land exactly
where we expect them to.

**Run it — what you'll see:** the title bar now reads **Firework Simulator**, and
dragging the window's edge won't change its size.

**Checkpoint:** ✅ the title shows, and the edges won't resize.

**If it's not right:**
- *Title didn't change* → these lines must come **after** `window = tk.Tk()` and
  **before** `window.mainloop()`.
- *Red error* → in Python, `False` is capitalized. Not `false`.

---

## Step 5 — Hang the night sky

**What you're adding:** the dark canvas — your stage.

**The code** *(add these just above `window.mainloop()`)*
```python
canvas = tk.Canvas(window, width=1200, height=800, bg="#0a0a1e", highlightthickness=0)
canvas.pack()
```

**What it does:** a `Canvas` is a blank surface you can draw on. We make it 1200×800,
fill it with `#0a0a1e` (a very dark midnight blue), and turn off its default focus
border with `highlightthickness=0`. `pack()` places it into the window.

**Why it matters:** this canvas is the stage for the *entire* project. Every star,
the moon, every rocket and spark gets drawn right here. The dark color is your night.

**Run it — what you'll see:** 🎆 a **large window filled with deep midnight-blue** —
no border line, just clean dark sky.

**Checkpoint:** ✅ a big dark-navy window (about 1200×800) with no thin line around
the dark area. **That's Beat 1 — the night sky.**

**If it's not right:**
- *Window is tiny and gray* → you're missing `canvas.pack()`; the canvas exists but
  was never placed.
- *Thin white line around the edge* → check `highlightthickness=0`.
- *Red error about color* → the color must be the text `"#0a0a1e"` in quotes.

---

## Chapter 1 complete

Your whole `main.py` now reads:

```python
import tkinter as tk

window = tk.Tk()
window.title("Firework Simulator")
window.resizable(False, False)

canvas = tk.Canvas(window, width=1200, height=800, bg="#0a0a1e", highlightthickness=0)
canvas.pack()

window.mainloop()
```

Eight lines — and you opened a window and painted the night. **You can stop here
with something that runs.** When you're ready, Chapter 2 hangs a moon in your sky.

➡️ **Next: Chapter 2 — The moon**
