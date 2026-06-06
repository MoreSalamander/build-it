# Chapter 7 — Six fireworks

**You'll build:** six visibly different explosions, chosen with the number keys 1–6.
**You'll learn:** responding to key presses, remembering a choice, and varying one
function with a setting.
**Starts from:** your finished Chapter 6 `main.py`. **Two steps.**

> Every burst is a plain sphere right now. We'll teach the *one* `burst` function six
> different looks — no new machine, just different settings.

---

## Step 1 — Choose a shape with the keys

**What you're adding:** a remembered shape, the number-key bindings, and passing the
shape into the burst.

**The code — part A** *(add near your `colors` line, above `def tick():`)*
```python
shapes = ["rocket", "peony", "willow", "palm", "ring", "cracker"]
current = {"shape": "rocket"}

def set_shape(name):
    current["shape"] = name

window.bind("1", lambda e: set_shape("rocket"))
window.bind("2", lambda e: set_shape("peony"))
window.bind("3", lambda e: set_shape("willow"))
window.bind("4", lambda e: set_shape("palm"))
window.bind("5", lambda e: set_shape("ring"))
window.bind("6", lambda e: set_shape("cracker"))
```

**The code — part B** *(in `launch`, add the chosen shape to the rocket)*
```python
def launch(event):
    fireworks.append({"x": event.x, "y": 800, "vx": random.uniform(-1, 1), "vy": random.uniform(-20, -12), "trail": [], "shape": current["shape"]})
```

**The code — part C** *(change `burst` to accept a `shape`, and the call in `tick` to
pass it)*
```python
def burst(x, y, color, shape):
```
```python
            burst(fw["x"], fw["y"], random.choice(colors), fw["shape"])
```

**What it does:** `current` is a little box that remembers which shape you've picked.
Each number key runs `set_shape` to change it. (`lambda e: ...` is a tiny throwaway
function — the key handler hands it an event we ignore.) When you launch, the rocket
remembers the shape it was fired with, and passes it to `burst`.

**Why it matters:** this is keyboard control, and the "remember a choice in a box you
can change" pattern — you'll use it again for the auto-show next chapter.

**Run it — what you'll see:** press 1–6, then click. They all still look the *same*
(plain spheres) for now — but the keys are working and the choice is travelling
through. Next step makes each one its own.

**Checkpoint:** ✅ it runs; clicking still makes fireworks; no error pressing 1–6.

**If it's not right:**
- *Error about `shape`* → `burst` must now be `def burst(x, y, color, shape):`, and
  the call must pass `fw["shape"]`.

---

## Step 2 — Give each shape its own look

**What you're adding:** the recipe that makes each shape different.

**The code** *(replace the inside of your `burst` function with this)*
```python
def burst(x, y, color, shape):
    count = 80
    for i in range(count):
        angle = random.uniform(0, 6.28)
        speed = random.uniform(2.5, 5)
        life = random.randint(70, 110)
        if shape == "peony":
            speed = random.uniform(6, 10)
            life = random.randint(100, 140)
        elif shape == "willow":
            speed = random.uniform(2, 3.5)
            life = random.randint(150, 210)
        elif shape == "palm":
            angle = -1.57 + random.uniform(-0.5, 0.5)
            speed = random.uniform(8, 12)
        elif shape == "ring":
            angle = (i / count) * 6.28
            speed = 8
        elif shape == "cracker":
            speed = random.uniform(1, 3)
            life = random.randint(18, 38)
        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color, "life": life})
```

**What it does:** same loop as before, but each shape tweaks the sparks:
- **rocket** — a plain round sphere (the default).
- **peony** — a *bigger, denser* sphere (more sparks).
- **willow** — slow sparks that live long, so they hang and droop.
- **palm** — a narrow fountain that shoots straight up.
- **ring** — sparks spaced evenly at one speed, making a clean expanding circle.
- **cracker** — lots of tiny, fast, short-lived sparks — a quick crackle.

**Why it matters:** this is the big lesson of the chapter — *one* function, six results,
just by changing a few numbers. That's how real programs avoid copy-pasting six near-
identical functions.

**Run it — what you'll see:** 🎆 press 1–6 and click — each key now makes a **clearly
different** explosion. **That's Beat 7 — six fireworks.**

**Checkpoint:** ✅ all six keys produce visibly distinct bursts (ring looks like a
ring, palm shoots up, etc.).

**If it's not right:**
- *Some shapes look identical* → check the `if`/`elif` names match the key bindings
  exactly (`willow`, not `wilow`!).
- *Indentation error* → the `if`/`elif` block lives *inside* the `for` loop.

---

## Chapter 7 complete

You now have six fireworks on the number keys. The full `main.py` is getting long —
the key new piece is the `burst` function above and the keybindings in Step 1. **Stop
here and put on a show by hand**, or go to the last chapter, where the show runs
itself.

➡️ **Next: Chapter 8 — The show**
