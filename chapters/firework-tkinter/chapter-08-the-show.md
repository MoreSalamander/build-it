# Chapter 8 — The show

**You'll build:** the finishing touches — random launches, a hands-free auto-show, a
clear key, and a live readout.
**You'll learn:** more key bindings, a timer inside the loop, and a text overlay.
**Starts from:** your finished Chapter 7 `main.py`. **Four steps.**

> The fireworks all work. Now we make it a *show.*

---

## Step 1 — Space launches a random firework

**What you're adding:** a spacebar that fires a random shape at a random spot.

**The code — part A** *(add near your other functions, above `def tick():`)*
```python
def random_firework(event=None):
    fireworks.append({"x": random.randint(100, 1100), "y": 800, "vx": random.uniform(-1, 1), "vy": -15, "trail": [], "shape": random.choice(shapes)})
```

**The code — part B** *(add with your other bindings)*
```python
window.bind("<space>", random_firework)
```

**What it does:** `random_firework` launches a rocket from a random `x` with a random
shape. `event=None` lets it be called both by the spacebar *and* by us directly (next
step). The bind ties it to the spacebar.

**Why it matters:** reusing one function from two places (a key and, soon, the timer)
is exactly the kind of reuse that keeps programs small.

**Run it — what you'll see:** tap **space** — a random firework launches somewhere
across the sky.

**Checkpoint:** ✅ pressing space fires a random firework.

**If it's not right:**
- *`shapes` not defined* → this builds on Chapter 7; `shapes` comes from there.

---

## Step 2 — An auto-show

**What you're adding:** press **R** to make fireworks fire on their own.

**The code — part A** *(update your `current` box to remember two more things)*
```python
current = {"shape": "rocket", "auto": False, "timer": 0}
```

**The code — part B** *(add a toggle function and its binding)*
```python
def toggle_auto(event=None):
    current["auto"] = not current["auto"]

window.bind("r", toggle_auto)
```

**The code — part C** *(add **inside `tick`**, right after the star loop)*
```python
    if current["auto"]:
        current["timer"] += 1
        if current["timer"] >= 90:
            current["timer"] = 0
            random_firework()
```

**What it does:** `R` flips `auto` on or off. While it's on, the loop counts frames in
`timer`; every 90 frames (about 1.5 seconds at ~60 per second) it resets and fires a
random firework.

**Why it matters:** this is your first **timer** — "do something every so often" —
built from nothing but counting frames in the loop you already have.

**Run it — what you'll see:** press **R** — fireworks start launching on their own,
about every 1.5 seconds. Press **R** again to stop.

**Checkpoint:** ✅ R starts and stops a hands-free firework show.

**If it's not right:**
- *Nothing auto-fires* → part C must be inside `tick`; check `current` has `"auto"`
  and `"timer"`.

---

## Step 3 — A clear key

**What you're adding:** press **C** to wipe the sky.

**The code — part A** *(add with your other functions)*
```python
def clear_all(event=None):
    fireworks.clear()
    sparks.clear()
    canvas.delete("firework")
```

**The code — part B** *(add with your other bindings)*
```python
window.bind("c", clear_all)
```

**What it does:** empties both lists and erases every shape tagged `"firework"` —
leaving the stars and moon untouched (they aren't tagged).

**Why it matters:** a reset is a small kindness — and a neat reminder of why we tagged
the moving things separately.

**Run it — what you'll see:** during a busy show, press **C** — all rockets and sparks
vanish instantly; the sky stays.

**Checkpoint:** ✅ C clears the fireworks but leaves the stars and moon.

**If it's not right:**
- *The stars vanish too* → you must delete `"firework"`, not everything.

---

## Step 4 — A live readout

**What you're adding:** a little text panel showing the current shape and spark count.

**The code — part A** *(add once, just above `def tick():`)*
```python
hud = canvas.create_text(20, 20, anchor="nw", fill="#88ff88", font=("Arial", 12), text="")
```

**The code — part B** *(add **inside `tick`**, just **above** `window.after(16, tick)`)*
```python
    canvas.itemconfig(hud, text=f"Shape: {current['shape']}    Sparks: {len(sparks)}")
    canvas.tag_raise(hud)
```

**What it does:** `create_text` makes one text item in the top-left. Each frame we
update its words with the current shape and how many sparks are alive, and
`tag_raise` lifts it above the fireworks so it's always readable (draw order, from
Chapter 2, on demand).

**Why it matters:** a readout turns a toy into something that feels finished — and it's
just `itemconfig` (change what's there), the same tool that twinkles the stars.

**Run it — what you'll see:** 🎆 a soft green readout in the corner, updating live as
you switch shapes and sparks come and go. **That's Beat 8 — the show.**

**Checkpoint:** ✅ the readout shows the current shape and a live spark count, sitting
on top of everything.

**If it's not right:**
- *Readout hidden behind sparks* → make sure `canvas.tag_raise(hud)` runs each frame.

---

## Chapter 8 complete — the whole firework simulator

```python
import tkinter as tk
import random
import math

window = tk.Tk()
window.title("Firework Simulator")
window.resizable(False, False)

canvas = tk.Canvas(window, width=1200, height=800, bg="#0a0a1e", highlightthickness=0)
canvas.pack()

# The moon
canvas.create_oval(1040, 20, 1160, 140, fill="#3a3a5a", outline="")
canvas.create_oval(1070, 50, 1130, 110, fill="#ffffdc", outline="")
canvas.create_oval(1087, 70, 1097, 80, fill="#e6e6c8", outline="")
canvas.create_oval(1095, 83, 1113, 91, fill="#e6e6c8", outline="")

# Stars
stars = []
for i in range(100):
    x = random.randint(0, 1200)
    y = random.randint(0, 400)
    size = random.choice([1, 1, 1, 2])
    star = canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
    stars.append({"id": star, "brightness": random.uniform(0.5, 1.0), "speed": random.uniform(0.01, 0.03)})

# Rockets, sparks, palette, shapes, and state
fireworks = []
sparks = []
colors = ["#ff3232", "#3264ff", "#32ff64", "#ffd700", "#c832ff", "#ffffff", "#ffa500"]
shapes = ["rocket", "peony", "willow", "palm", "ring", "cracker"]
current = {"shape": "rocket", "auto": False, "timer": 0}

def launch(event):
    fireworks.append({"x": event.x, "y": 800, "vx": random.uniform(-1, 1), "vy": -15, "trail": [], "shape": current["shape"]})

def random_firework(event=None):
    fireworks.append({"x": random.randint(100, 1100), "y": 800, "vx": random.uniform(-1, 1), "vy": -15, "trail": [], "shape": random.choice(shapes)})

def set_shape(name):
    current["shape"] = name

def toggle_auto(event=None):
    current["auto"] = not current["auto"]

def clear_all(event=None):
    fireworks.clear()
    sparks.clear()
    canvas.delete("firework")

def burst(x, y, color, shape):
    count = 60
    if shape == "peony":
        count = 100
    if shape == "cracker":
        count = 90
    for i in range(count):
        angle = random.uniform(0, 6.28)
        speed = random.uniform(2, 6)
        life = random.randint(60, 110)
        if shape == "ring":
            angle = (i / count) * 6.28
            speed = 5
        elif shape == "willow":
            speed = random.uniform(1.5, 3.5)
            life = random.randint(110, 150)
        elif shape == "palm":
            angle = (i % 5) / 5 * 6.28 + random.uniform(-0.2, 0.2)
            speed = random.uniform(5, 8)
        elif shape == "cracker":
            speed = random.uniform(1, 4)
            life = random.randint(25, 50)
        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color, "life": life})

canvas.bind("<Button-1>", launch)
window.bind("<space>", random_firework)
window.bind("1", lambda e: set_shape("rocket"))
window.bind("2", lambda e: set_shape("peony"))
window.bind("3", lambda e: set_shape("willow"))
window.bind("4", lambda e: set_shape("palm"))
window.bind("5", lambda e: set_shape("ring"))
window.bind("6", lambda e: set_shape("cracker"))
window.bind("r", toggle_auto)
window.bind("c", clear_all)

hud = canvas.create_text(20, 20, anchor="nw", fill="#88ff88", font=("Arial", 12), text="")

def tick():
    for star in stars:
        star["brightness"] += (random.random() - 0.5) * star["speed"]
        star["brightness"] = max(0.3, min(1.0, star["brightness"]))
        gray = int(star["brightness"] * 255)
        canvas.itemconfig(star["id"], fill=f"#{gray:02x}{gray:02x}{gray:02x}")
    if current["auto"]:
        current["timer"] += 1
        if current["timer"] >= 90:
            current["timer"] = 0
            random_firework()
    for fw in fireworks:
        fw["vy"] += 0.3
        fw["x"] += fw["vx"]
        fw["y"] += fw["vy"]
        fw["trail"].append((fw["x"], fw["y"]))
        if len(fw["trail"]) > 15:
            fw["trail"].pop(0)
    for fw in fireworks[:]:
        if fw["vy"] >= 0:
            burst(fw["x"], fw["y"], random.choice(colors), fw["shape"])
            fireworks.remove(fw)
    for s in sparks:
        s["vy"] += 0.1
        s["vx"] *= 0.99
        s["vy"] *= 0.99
        s["x"] += s["vx"]
        s["y"] += s["vy"]
        s["life"] -= 1
    for s in sparks[:]:
        if s["life"] <= 0:
            sparks.remove(s)
    canvas.delete("firework")
    for fw in fireworks:
        if len(fw["trail"]) > 1:
            canvas.create_line(fw["trail"], fill="white", width=2, tags="firework")
        canvas.create_oval(fw["x"] - 3, fw["y"] - 3, fw["x"] + 3, fw["y"] + 3, fill="white", outline="", tags="firework")
    for s in sparks:
        size = 1 + s["life"] // 40
        canvas.create_oval(s["x"] - size, s["y"] - size, s["x"] + size, s["y"] + size, fill=s["color"], outline="", tags="firework")
    canvas.itemconfig(hud, text=f"Shape: {current['shape']}    Sparks: {len(sparks)}")
    canvas.tag_raise(hud)
    window.after(16, tick)

tick()

window.mainloop()
```

**You built a firework simulator.** Click to launch, 1–6 for six shapes, space for
random, R for a hands-free show, C to clear — over a twinkling sky with a moon.

That's the whole thing — eight chapters, from an empty file to *this*. **Turn your
laptop around.**
