import json, py_compile, os, tempfile, sys

# (ch,step) ordered; key = ch*10+step
STEPS = [11,12,13,14,15,21,22,23,31,32,33,34,41,42,43,44,51,52,53,61,62,63,71,72,81,82,83,84]

def K(c,s): return c*10+s

# Each fragment: list of (key, text) versions, in FINAL document order.
F = []
def frag(*versions): F.append(list(versions))

frag((11,"import tkinter as tk"))
frag((31,"import random"))
frag((51,"import math"))
frag((12,"window = tk.Tk()"))
frag((14,'window.title("Firework Simulator")'))
frag((14,"window.resizable(False, False)"))
frag((15,'canvas = tk.Canvas(window, width=1200, height=800, bg="#0a0a1e", highlightthickness=0)'))
frag((15,"canvas.pack()"))
frag((21,'canvas.create_oval(1040, 20, 1160, 140, fill="#3a3a5a", outline="")'))
frag((22,'canvas.create_oval(1070, 50, 1130, 110, fill="#ffffdc", outline="")'))
frag((23,'canvas.create_oval(1087, 70, 1097, 80, fill="#e6e6c8", outline="")'))
frag((23,'canvas.create_oval(1095, 83, 1113, 91, fill="#e6e6c8", outline="")'))
frag((32,'stars = []\nfor i in range(100):\n    x = random.randint(0, 1200)\n    y = random.randint(0, 400)\n    size = random.choice([1, 1, 1, 2])\n    star = canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")\n    stars.append({"id": star, "brightness": random.uniform(0.5, 1.0), "speed": random.uniform(0.01, 0.03)})'))
frag((41,"fireworks = []"))
frag((51,"sparks = []"))
frag((51,'colors = ["#ff3232", "#3264ff", "#32ff64", "#ffd700", "#c832ff", "#ffffff", "#ffa500"]'))
frag((71,'shapes = ["rocket", "peony", "willow", "palm", "ring", "cracker"]'))
frag((71,'current = {"shape": "rocket"}'),(82,'current = {"shape": "rocket", "auto": False, "timer": 0}'))
frag((41,'def launch(event):\n    fireworks.append({"x": event.x, "y": 800, "vx": random.uniform(-1, 1), "vy": random.uniform(-20, -12), "trail": []})'),
     (71,'def launch(event):\n    fireworks.append({"x": event.x, "y": 800, "vx": random.uniform(-1, 1), "vy": random.uniform(-20, -12), "trail": [], "shape": current["shape"]})'))
frag((81,'def random_firework(event=None):\n    fireworks.append({"x": random.randint(100, 1100), "y": 800, "vx": random.uniform(-1, 1), "vy": random.uniform(-20, -12), "trail": [], "shape": random.choice(shapes)})'))
frag((71,'def set_shape(name):\n    current["shape"] = name'))
frag((82,'def toggle_auto(event=None):\n    current["auto"] = not current["auto"]'))
frag((83,'def clear_all(event=None):\n    fireworks.clear()\n    sparks.clear()\n    canvas.delete("firework")'))
BURST_BASE='def burst(x, y, color):\n    for i in range(60):\n        angle = random.uniform(0, 6.28)\n        speed = random.uniform(2, 6)\n        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color})'
BURST_LIFE='def burst(x, y, color):\n    for i in range(60):\n        angle = random.uniform(0, 6.28)\n        speed = random.uniform(2, 6)\n        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color, "life": random.randint(60, 110)})'
BURST_SHAPE_SIG='def burst(x, y, color, shape):\n    for i in range(60):\n        angle = random.uniform(0, 6.28)\n        speed = random.uniform(2, 6)\n        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color, "life": random.randint(60, 110)})'
BURST_FULL='def burst(x, y, color, shape):\n    count = 80\n    for i in range(count):\n        angle = random.uniform(0, 6.28)\n        speed = random.uniform(2.5, 5)\n        life = random.randint(70, 110)\n        if shape == "peony":\n            speed = random.uniform(6, 10)\n            life = random.randint(100, 140)\n        elif shape == "willow":\n            speed = random.uniform(2, 3.5)\n            life = random.randint(150, 210)\n        elif shape == "palm":\n            angle = -1.57 + random.uniform(-0.5, 0.5)\n            speed = random.uniform(8, 12)\n        elif shape == "ring":\n            angle = (i / count) * 6.28\n            speed = 8\n        elif shape == "cracker":\n            speed = random.uniform(1, 3)\n            life = random.randint(18, 38)\n        sparks.append({"x": x, "y": y, "vx": math.cos(angle) * speed, "vy": math.sin(angle) * speed, "color": color, "life": life})'
frag((51,BURST_BASE),(62,BURST_LIFE),(71,BURST_SHAPE_SIG),(72,BURST_FULL))
frag((41,'canvas.bind("<Button-1>", launch)'))
frag((81,'window.bind("<space>", random_firework)'))
frag((71,'window.bind("1", lambda e: set_shape("rocket"))\nwindow.bind("2", lambda e: set_shape("peony"))\nwindow.bind("3", lambda e: set_shape("willow"))\nwindow.bind("4", lambda e: set_shape("palm"))\nwindow.bind("5", lambda e: set_shape("ring"))\nwindow.bind("6", lambda e: set_shape("cracker"))'))
frag((82,'window.bind("r", toggle_auto)'))
frag((83,'window.bind("c", clear_all)'))
frag((84,'hud = canvas.create_text(20, 20, anchor="nw", fill="#88ff88", font=("Arial", 12), text="")'))
frag((33,"def tick():"))
frag((34,'    for star in stars:\n        star["brightness"] += (random.random() - 0.5) * star["speed"]\n        star["brightness"] = max(0.3, min(1.0, star["brightness"]))\n        gray = int(star["brightness"] * 255)\n        canvas.itemconfig(star["id"], fill=f"#{gray:02x}{gray:02x}{gray:02x}")'))
frag((82,'    if current["auto"]:\n        current["timer"] += 1\n        if current["timer"] >= 90:\n            current["timer"] = 0\n            random_firework()'))
frag((43,'    for fw in fireworks:\n        fw["vy"] += 0.3\n        fw["x"] += fw["vx"]\n        fw["y"] += fw["vy"]'),
     (44,'    for fw in fireworks:\n        fw["vy"] += 0.3\n        fw["x"] += fw["vx"]\n        fw["y"] += fw["vy"]\n        fw["trail"].append((fw["x"], fw["y"]))\n        if len(fw["trail"]) > 15:\n            fw["trail"].pop(0)'))
frag((52,'    for fw in fireworks[:]:\n        if fw["vy"] >= 0:\n            burst(fw["x"], fw["y"], random.choice(colors))\n            fireworks.remove(fw)'),
     (71,'    for fw in fireworks[:]:\n        if fw["vy"] >= 0:\n            burst(fw["x"], fw["y"], random.choice(colors), fw["shape"])\n            fireworks.remove(fw)'))
frag((53,'    for s in sparks:\n        s["x"] += s["vx"]\n        s["y"] += s["vy"]'),
     (61,'    for s in sparks:\n        s["vy"] += 0.1\n        s["vx"] *= 0.99\n        s["vy"] *= 0.99\n        s["x"] += s["vx"]\n        s["y"] += s["vy"]'),
     (62,'    for s in sparks:\n        s["vy"] += 0.1\n        s["vx"] *= 0.99\n        s["vy"] *= 0.99\n        s["x"] += s["vx"]\n        s["y"] += s["vy"]\n        s["life"] -= 1'))
frag((62,'    for s in sparks[:]:\n        if s["life"] <= 0:\n            sparks.remove(s)'))
frag((42,'    canvas.delete("firework")'))
frag((42,'    for fw in fireworks:\n        canvas.create_oval(fw["x"] - 3, fw["y"] - 3, fw["x"] + 3, fw["y"] + 3, fill="white", outline="", tags="firework")'),
     (44,'    for fw in fireworks:\n        if len(fw["trail"]) > 1:\n            canvas.create_line(fw["trail"], fill="white", width=2, tags="firework")\n        canvas.create_oval(fw["x"] - 3, fw["y"] - 3, fw["x"] + 3, fw["y"] + 3, fill="white", outline="", tags="firework")'))
frag((52,'    for s in sparks:\n        canvas.create_oval(s["x"] - 2, s["y"] - 2, s["x"] + 2, s["y"] + 2, fill=s["color"], outline="", tags="firework")'),
     (63,'    for s in sparks:\n        size = 1 + s["life"] // 40\n        canvas.create_oval(s["x"] - size, s["y"] - size, s["x"] + size, s["y"] + size, fill=s["color"], outline="", tags="firework")'))
frag((84,'    canvas.itemconfig(hud, text=f"Shape: {current[\'shape\']}    Sparks: {len(sparks)}")\n    canvas.tag_raise(hud)'))
frag((33,"    window.after(16, tick)"))
frag((33,"tick()"))
frag((13,"window.mainloop()"))

def render(N):
    out=[]
    for versions in F:
        cur=None
        for k,t in versions:
            if k<=N: cur=t
        if cur is not None: out.append(cur)
    return "\n".join(out)

def norm(src):
    lines=[ln.rstrip() for ln in src.split("\n")]
    return "\n".join(ln for ln in lines if ln.strip() and not ln.strip().startswith("#"))

# verify each step compiles + final matches reference
ref = open("/Users/0ne29/MoreSalamander/buildit-remaster/chapters/firework-tkinter/firework_complete.py").read()
allfull={}
for N in STEPS:
    code=render(N)
    f=tempfile.NamedTemporaryFile("w",suffix=".py",delete=False); f.write(code); f.close()
    try: py_compile.compile(f.name,doraise=True)
    except Exception as e: print("COMPILE FAIL at",N,":",e); sys.exit(1)
    allfull[N]=code

if norm(render(84))!=norm(ref):
    print("FINAL != reference. diff:")
    import difflib
    for l in difflib.unified_diff(norm(ref).split("\n"), norm(render(84)).split("\n"), "reference","generated", lineterm=""):
        print(l)
    sys.exit(1)
print("ALL", len(STEPS), "steps compile; final == firework_complete.py (normalized) ✅")

# emit BUILDIT_FULLS as [chapter][step]
chsteps={1:5,2:3,3:4,4:4,5:3,6:3,7:2,8:4}
arr=[]
for c in range(1,9):
    arr.append([allfull[K(c,s)] for s in range(1,chsteps[c]+1)])
open("/Users/0ne29/MoreSalamander/buildit-remaster/fulls.js","w").write(
    "// Auto-generated cumulative 'whole file so far' per step. Final == firework_complete.py.\nwindow.BUILDIT_FULLS = "+json.dumps(arr,ensure_ascii=False)+";\n")
print("wrote fulls.js")
