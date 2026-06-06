# Chapter 6 — Gravity & fade

**You'll build:** sparks that arc, fall, slow, shrink, and die away — like the real
thing.
**You'll learn:** applying gravity and drag, giving things a lifespan, and removing
them when they're done.
**Starts from:** your finished Chapter 5 `main.py`. **Three steps.**

> Right now sparks fly straight out forever. We'll make them behave like real sparks.

---

## Step 1 — Make them fall

**What you're adding:** gravity and a little air drag on each spark.

**The code** *(add **inside the spark move loop** in `tick`, right **above**
`s["x"] += s["vx"]`)*
```python
        s["vy"] += 0.1
        s["vx"] *= 0.99
        s["vy"] *= 0.99
```

**What it does:** each frame, gravity adds a little downward speed (`vy += 0.1`), and
drag gently shrinks both speeds (`*= 0.99`) so the sparks slow as they travel.

**Why it matters:** it's the same gravity idea as the rocket, now on every spark — and
the drag is what makes an explosion "puff" and settle instead of flying off like
lasers.

**Run it — what you'll see:** the sparks now **arc outward and fall**, slowing as they
go. Already much more like a firework.

**Checkpoint:** ✅ sparks curve downward and slow down instead of flying straight.

**If it's not right:**
- *They still fly straight* → these three lines must be inside the spark loop.

---

## Step 2 — Give them a lifespan

**What you're adding:** a `life` counter, and removing sparks when it runs out.

**The code — part A** *(in `burst`, add `"life"` to the spark you append)*
```python
        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color, "life": random.randint(60, 110)})
```

**The code — part B** *(in the spark move loop, add at the **end** of the loop)*
```python
        s["life"] -= 1
```

**The code — part C** *(in `tick`, add right **after** the spark move loop)*
```python
    for s in sparks[:]:
        if s["life"] <= 0:
            sparks.remove(s)
```

**What it does:** each spark is born with a random `life` (60–110 frames). Every frame
we count it down, and any spark that hits zero is removed (looping over a *copy*,
`sparks[:]`, so we can safely remove from the real list — same trick as the rockets).

**Why it matters:** without this, sparks pile up forever and the program slowly chokes.
A lifespan is how anything temporary cleans up after itself.

**Run it — what you'll see:** sparks now **disappear** a second or so after the burst,
instead of lingering. The sky clears itself between fireworks.

**Checkpoint:** ✅ sparks vanish a moment after exploding; the screen doesn't fill up.

**If it's not right:**
- *`KeyError: 'life'`* → make sure part A added `"life"` to the spark in `burst`.
- *They never disappear* → part C must be a separate loop after the move loop.

---

## Step 3 — Fade as they die

**What you're adding:** sparks that shrink as their life runs out.

**The code** *(change the spark-drawing line — replace the fixed `2`s with a size based
on life)*
```python
    for s in sparks:
        size = 1 + s["life"] // 40
        canvas.create_oval(s["x"] - size, s["y"] - size, s["x"] + size, s["y"] + size, fill=s["color"], outline="", tags="firework")
```

**What it does:** instead of every spark being the same size, we set `size` from its
remaining `life` — bright and fat when young, tiny just before it dies.

**Why it matters:** Tkinter can't truly fade colors, but a shrinking dot reads as a
spark burning out — the same "diminish and vanish" feeling, done simply.

**Run it — what you'll see:** 🎆 sparks now **shrink as they fall and fade away.**
**That's Beat 6 — a complete, lifelike firework.**

**Checkpoint:** ✅ sparks shrink smaller as they age, then disappear.

**If it's not right:**
- *All the same size* → make sure you replaced the `2`s with `size`, and `size` is
  computed just above.

---

## Chapter 6 complete

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
    fireworks.append({"x": event.x, "y": 800, "vx": random.uniform(-1, 1), "vy": -15, "trail": []})

def burst(x, y, color):
    for i in range(60):
        angle = random.uniform(0, 6.28)
        speed = random.uniform(2, 6)
        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color, "life": random.randint(60, 110)})

canvas.bind("<Button-1>", launch)

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
    window.after(16, tick)

tick()

window.mainloop()
```

A full, lifelike firework — burst, arc, fall, fade. Next, the same burst learns **six
different shapes.**

➡️ **Next: Chapter 7 — Six fireworks**
