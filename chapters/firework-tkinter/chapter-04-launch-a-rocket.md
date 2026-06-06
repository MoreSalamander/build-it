# Chapter 4 — Launch a rocket

**You'll build:** click anywhere and a rocket streaks up from the ground, trailing
white.
**You'll learn:** responding to a mouse click, moving an object with simple physics,
and erase-then-redraw animation with tags.
**Starts from:** your finished Chapter 3 `main.py`. **Four steps.**

> A rocket is just a note-card in a list — exactly like a star. You already know this
> shape; now it moves.

---

## Step 1 — Get ready to launch

**What you're adding:** a list to hold rockets, and a click that adds one.

**The code** *(add this block just **above** your `def tick():` line)*
```python
fireworks = []

def launch(event):
    fireworks.append({
        "x": event.x,
        "y": 800,
        "vx": random.uniform(-1, 1),
        "vy": -15,
        "trail": []
    })

canvas.bind("<Button-1>", launch)
```

**What it does:** `fireworks` is a list, like `stars`. `launch` is a function that
runs whenever you click — `event` tells it *where* you clicked. It adds a new rocket
note-card: starting at your click's `x` but down at the ground (`y` = 800), drifting
slightly sideways (`vx`), shooting **up** (`vy` = -15 — negative is up, because `y`
grows *downward* on a screen), and an empty `trail` to fill in later. `canvas.bind`
connects left-clicks to `launch`.

**Why it matters:** this is your first **interaction** — the program now responds to
*you*. And notice it's the same list-of-note-cards idea from the stars.

**Run it — what you'll see:** click a few times — **nothing appears yet.** That's
expected: you're recording rockets, but we haven't drawn them. Next step puts them on
screen. (No error = good.)

**Checkpoint:** ✅ it runs and clicking causes no error (even with nothing visible).

**If it's not right:**
- *Error about `event`* → the function must be `def launch(event):`.
- *Clicking errors* → check the bind text: `"<Button-1>"`.

---

## Step 2 — Draw the rockets

**What you're adding:** drawing each rocket, fresh, every frame.

**The code** *(add **inside `tick`**, right after the star loop, before
`window.after`)*
```python
    canvas.delete("firework")
    for fw in fireworks:
        canvas.create_oval(fw["x"] - 3, fw["y"] - 3, fw["x"] + 3, fw["y"] + 3, fill="white", outline="", tags="firework")
```

**What it does:** each frame we first erase last frame's rockets with
`canvas.delete("firework")` — that removes only shapes we labelled `"firework"`,
leaving the stars and moon untouched. Then we draw a small white dot for each rocket
at its current spot, **tagging** each one `"firework"` so next frame can clear it.
(Tags are just labels you stick on shapes to find them again.)

**Why it matters:** erase-then-redraw is how *everything that moves* gets animated —
and it's exactly how the explosion's hundreds of sparks get drawn two chapters from
now. Tags let you wipe only the moving things without erasing your sky.

**Run it — what you'll see:** click — a **white dot appears at the bottom** of the
sky, in line with where you clicked. It doesn't move yet, but it's there.

**Checkpoint:** ✅ clicking puts a white dot at the bottom of the sky.

**If it's not right:**
- *The stars disappear too* → you must delete `"firework"` (the tag), not everything.
- *No dot* → these lines must be **inside** `tick`.

---

## Step 3 — Make it fly

**What you're adding:** gravity and motion.

**The code** *(add **inside `tick`**, just **above** the `canvas.delete("firework")`
line)*
```python
    for fw in fireworks:
        fw["vy"] += 0.3
        fw["x"] += fw["vx"]
        fw["y"] += fw["vy"]
```

**What it does:** every frame, gravity tugs each rocket by adding `0.3` to its
downward speed (`vy`). Then we move it: `x` by its sideways drift, `y` by its vertical
speed. Since `vy` starts at -15 (up) and gravity keeps adding, the rocket rises fast,
slows, stops, and arcs back down — just like the real thing.

**Why it matters:** this is **physics**, and it's the very same three lines (gravity,
then move) that will make every spark fall in Chapter 6. Motion is just "change
position a little each frame" — the pattern you already met with the twinkle.

**Run it — what you'll see:** click — the rocket **shoots up** from the ground, slows
as it climbs, and arcs back down. 🎆

**Checkpoint:** ✅ clicking launches a dot that rises, slows, and falls.

**If it's not right:**
- *The dot doesn't move* → the move loop must be inside `tick`.
- *It flies off instantly* → check `vy` starts at -15 and gravity adds a small `0.3`.

---

## Step 4 — Give it a trail

**What you're adding:** the glowing streak behind the rocket.

**The code — part A** *(add **inside the move loop** from Step 3, right after
`fw["y"] += fw["vy"]`)*
```python
        fw["trail"].append((fw["x"], fw["y"]))
        if len(fw["trail"]) > 15:
            fw["trail"].pop(0)
```

**The code — part B** *(add **inside the draw loop** from Step 2, just **above** the
`create_oval` line)*
```python
        if len(fw["trail"]) > 1:
            canvas.create_line(fw["trail"], fill="white", width=2, tags="firework")
```

**What it does:** part A remembers the rocket's current spot in its `trail` list each
frame, keeping only the last 15 so the tail stays short instead of growing forever.
Part B connects those points with a line — a streak chasing the rocket. The
`if len(...) > 1` guard waits until there are at least two points to connect.

**Why it matters:** the trail is what turns a dot into a *rocket*. And it's the same
"a list that grows and gets trimmed" idea again — you keep reusing the few things you
already know.

**Run it — what you'll see:** 🎆 click — a rocket **streaks up trailing a white tail**
behind it. **That's Beat 4 — launch a rocket.**

**Checkpoint:** ✅ rockets rise with a white trailing streak behind them.

**If it's not right:**
- *No trail* → part A goes in the **move** loop, part B in the **draw** loop.
- *Tail too long or short* → change the `15`.

---

## Chapter 4 complete

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

# Rockets
fireworks = []

def launch(event):
    fireworks.append({
        "x": event.x,
        "y": 800,
        "vx": random.uniform(-1, 1),
        "vy": -15,
        "trail": []
    })

canvas.bind("<Button-1>", launch)

# The heartbeat
def tick():
    for star in stars:
        star["brightness"] += (random.random() - 0.5) * star["speed"]
        star["brightness"] = max(0.3, min(1.0, star["brightness"]))
        gray = int(star["brightness"] * 255)
        canvas.itemconfig(star["id"], fill=f"#{gray:02x}{gray:02x}{gray:02x}")
    for fw in fireworks:
        fw["vy"] += 0.3
        fw["x"] += fw["vx"]
        fw["y"] += fw["vy"]
        fw["trail"].append((fw["x"], fw["y"]))
        if len(fw["trail"]) > 15:
            fw["trail"].pop(0)
    canvas.delete("firework")
    for fw in fireworks:
        if len(fw["trail"]) > 1:
            canvas.create_line(fw["trail"], fill="white", width=2, tags="firework")
        canvas.create_oval(fw["x"] - 3, fw["y"] - 3, fw["x"] + 3, fw["y"] + 3, fill="white", outline="", tags="firework")
    window.after(16, tick)

tick()

window.mainloop()
```

Click your sky and rockets fly. **Stop here if you like** — but they go up and come
back down, and that's begging to be fixed. In Chapter 5 we catch the rocket at the
top of its arc and make it **burst.**

➡️ **Next: Chapter 5 — The big bang**
