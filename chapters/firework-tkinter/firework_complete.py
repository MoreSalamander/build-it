import tkinter as tk
import random
import math

window = tk.Tk()
window.title("Firework Simulator")
window.resizable(False, False)

canvas = tk.Canvas(window, width=1200, height=800, bg="#0a0a1e", highlightthickness=0)
canvas.pack()

canvas.create_oval(1040, 20, 1160, 140, fill="#3a3a5a", outline="")
canvas.create_oval(1070, 50, 1130, 110, fill="#ffffdc", outline="")
canvas.create_oval(1087, 70, 1097, 80, fill="#e6e6c8", outline="")
canvas.create_oval(1095, 83, 1113, 91, fill="#e6e6c8", outline="")

stars = []
for i in range(100):
    x = random.randint(0, 1200)
    y = random.randint(0, 400)
    size = random.choice([1, 1, 1, 2])
    star = canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")
    stars.append({"id": star, "brightness": random.uniform(0.5, 1.0), "speed": random.uniform(0.01, 0.03)})

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
