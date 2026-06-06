# Chapter 5 — The big bang

**You'll build:** the rocket reaches the top of its arc and **bursts** into a sphere
of colored sparks.
**You'll learn:** making many things at once with a function, aiming them in all
directions, and removing things from a list.
**Starts from:** your finished Chapter 4 `main.py`. **Three steps.**

> This is the payoff. By the end of this chapter, clicking makes fireworks.

---

## Step 1 — Build the explosion machine

**What you're adding:** a palette, a place to keep sparks, and a `burst` function.

**The code — part A** *(add at the top, with your other imports)*
```python
import math
```

**The code — part B** *(add near your `fireworks = []` line, above `def tick():`)*
```python
colors = ["#ff3232", "#3264ff", "#32ff64", "#ffd700", "#c832ff", "#ffffff", "#ffa500"]
sparks = []

def burst(x, y, color):
    for i in range(60):
        angle = random.uniform(0, 6.28)
        speed = random.uniform(2, 6)
        sparks.append({
            "x": x,
            "y": y,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "color": color
        })
```

**What it does:** `import math` gives you trig tools. `colors` is a palette of bright
firework colors. `sparks` is a list to hold every spark, just like `fireworks` holds
rockets. `burst` makes one explosion: 60 sparks fired from `(x, y)`, each in a random
direction (`angle` is anywhere around a full circle — `6.28` is roughly once around)
at a random `speed`. `cos` and `sin` turn that "direction + speed" into sideways
(`vx`) and vertical (`vy`) motion. Each spark remembers its `color`.

**Why it matters:** it's the "a for-loop makes many" idea again — 60 sparks from one
call. `cos`/`sin` look fancy, but you're only using them to point each spark a
different way around a circle.

**Run it — what you'll see:** nothing new — you built the machine but haven't fired
it. No error.

**Checkpoint:** ✅ it runs with no error.

**If it's not right:**
- *`name 'math' is not defined`* → make sure `import math` is up with your imports.

---

## Step 2 — Fire it at the top

**What you're adding:** burst the rocket at its peak, and draw the sparks.

**The code — part A** *(add **inside `tick`**, right after the rocket **move** loop)*
```python
    for fw in fireworks[:]:
        if fw["vy"] >= 0:
            burst(fw["x"], fw["y"], random.choice(colors))
            fireworks.remove(fw)
```

**The code — part B** *(add **inside `tick`**, in the **draw** section, right after
the loop that draws the rockets)*
```python
    for s in sparks:
        canvas.create_oval(s["x"] - 2, s["y"] - 2, s["x"] + 2, s["y"] + 2, fill=s["color"], outline="", tags="firework")
```

**What it does:** part A walks a *copy* of the rockets (`fireworks[:]`) so we can
safely remove from the real list while looping. Any rocket that has reached the top —
`vy >= 0` means it's stopped rising — `burst`s into sparks at its spot in a random
color, and is then removed with `.remove(fw)`. Part B draws every spark as a small
colored dot, tagged `"firework"` so it's cleared and redrawn each frame like the
rockets.

**Why it matters:** this is the instant the rocket *becomes* the explosion — and it's
exactly why we tracked `vy`: the moment it stops rising is the top of the arc, the
perfect time to burst.

**Run it — what you'll see:** click — the rocket rises, and at the top it **pops into
a tight ball of colored sparks**. They don't fly apart yet — frozen in a clump — but
the burst is born. 🎆

**Checkpoint:** ✅ rockets reach the top and turn into a clump of colored dots.

**If it's not right:**
- *Rocket just vanishes, no sparks* → check part B draws `sparks`, and `burst` is
  being called in part A.
- *Clump in the wrong spot* → `burst` should use `fw["x"], fw["y"]`.

---

## Step 3 — Blow it apart

**What you're adding:** motion for the sparks.

**The code** *(add **inside `tick`**, right after the burst loop from Step 2)*
```python
    for s in sparks:
        s["x"] += s["vx"]
        s["y"] += s["vy"]
```

**What it does:** every frame, each spark moves by its own velocity. Because `burst`
gave them velocities pointing every which way, they fly *outward* from the center —
an expanding sphere.

**Why it matters:** it's the same one-line motion idea as the rocket
(`position += velocity`) — but 60 of them at once, each heading a different
direction, is what *reads* as an explosion.

**Run it — what you'll see:** 🎆🎆 click — the rocket rises and **BURSTS into a sphere
of colored sparks flying outward.** **That's Beat 5 — the big bang.**

**Checkpoint:** ✅ explosions spray sparks outward in a colored sphere.

**If it's not right:**
- *Sparks don't move* → the spark move loop must be inside `tick`.
- *They fly in a line, not a ball* → `burst` must use `cos` for `vx` and `sin` for
  `vy`, with a random `angle`.

---

## Chapter 5 complete

Your `main.py` now reads:

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

# Rockets and sparks
fireworks = []
colors = ["#ff3232", "#3264ff", "#32ff64", "#ffd700", "#c832ff", "#ffffff", "#ffa500"]
sparks = []

def launch(event):
    fireworks.append({"x": event.x, "y": 800, "vx": random.uniform(-1, 1), "vy": random.uniform(-20, -12), "trail": []})

def burst(x, y, color):
    for i in range(60):
        angle = random.uniform(0, 6.28)
        speed = random.uniform(2, 6)
        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color})

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
    for fw in fireworks[:]:
        if fw["vy"] >= 0:
            burst(fw["x"], fw["y"], random.choice(colors))
            fireworks.remove(fw)
    for s in sparks:
        s["x"] += s["vx"]
        s["y"] += s["vy"]
    canvas.delete("firework")
    for fw in fireworks:
        if len(fw["trail"]) > 1:
            canvas.create_line(fw["trail"], fill="white", width=2, tags="firework")
        canvas.create_oval(fw["x"] - 3, fw["y"] - 3, fw["x"] + 3, fw["y"] + 3, fill="white", outline="", tags="firework")
    for s in sparks:
        canvas.create_oval(s["x"] - 2, s["y"] - 2, s["x"] + 2, s["y"] + 2, fill=s["color"], outline="", tags="firework")
    window.after(16, tick)

tick()

window.mainloop()
```

You click, and fireworks bloom. **This is the moment you'd turn your laptop around.**
Right now the sparks fly straight out forever — in Chapter 6 we add gravity so they
arc and fall, and a fade so they die away like real sparks.

➡️ **Next: Chapter 6 — Gravity & fade**
