"""Firework Simulator using Tkinter"""
import tkinter as tk
import random
import time
from firework import Firework
from config import *


class FireworkSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Firework Simulator 🎆")
        self.root.resizable(False, False)

        # Create canvas
        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg=BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack()

        # Game start
        self.fireworks = []
        self.current_type = 'rocket'
        self.auto_show = False
        self.auto_show_timer = 0
        self.running = True
        self.last_time = time.time()

        # Stats
        self.fps = 60
        self.frame_count = 0
        self.fps_timer = 0

        # Create background elements
        self.stars = []
        self.create_stars()
        self.create_moon()

        # UI elements
        self.create_ui()

        # Bind events
        self.canvas.bind('<Button-1>', self.on_click)
        self.root.bind('<space>', lambda e: self.launch_random())
        self.root.bind('r', lambda e: self.toggle_auto_show())
        self.root.bind('c', lambda e: self.clear_all())
        self.root.bind('<Escape>', lambda e: self.quit())

        # Bind number keys for firwork types
        types = ['rocket', 'peony', 'willow', 'palm', 'ring', 'cracker']
        for i, fw_type in enumerate(types, 1):
            self.root.bind(str(i), lambda e, t=fw_type: self.set_type(t))

        print(" 🎆 Firework Simulator Started!")
        print("\nControls:")
        print("   Click: Launch firework")
        print("   1-6: Select type")
        print("   Space: Random firework")
        print("   R: Toggle auto-show")
        print("   C: Clear all")
        print("   ESC: Quit")

        # Start game loop
        self.update()
        self.root.mainloop()

    def create_stars(self):
        """Create background stars"""
        for i in range(STAR_COUNT):
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT // 2)
            size = random.choice([1, 1, 1, 2])
            brightness = random.uniform(0.5, 1.0)

            star_id = self.canvas.create_oval(
                x, y, x + size, y + size,
                fill='white', outline=''
            )

            self.stars.append({
                'id': star_id,
                'x': x,
                'y': y,
                'size': size,
                'brightness': brightness,
                'twinkle_speed': random.uniform(0.01, 0.03)
            })

    def create_moon(self):
        """Create moon"""
        moon_x = WINDOW_WIDTH - 100
        moon_y = 80
        moon_radius = 30

        # Glow
        self.canvas.create_oval(
            moon_x - moon_radius * 2, moon_y - moon_radius * 2,
            moon_x + moon_radius * 2, moon_y + moon_radius * 2,
            fill='#3a3a5a', outline=''
        )

        # Moon
        self.canvas.create_oval(
            moon_x - moon_radius, moon_y - moon_radius,
            moon_x + moon_radius, moon_y + moon_radius,
            fill='#ffffdc', outline=''
        )

        # Craters
        self.canvas.create_oval(
            moon_x - 13, moon_y - 10,
            moon_x - 3, moon_y,
            fill='#e6e6c8', outline=''
        )

        self.canvas.create_oval(
            moon_x - 5, moon_y + 3,
            moon_x + 13, moon_y + 11,
            fill='#e6e6c8', outline=''
        )

    def create_ui(self):
        """Create UI elements"""
        # Stats panel
        panel_x = 20
        panel_y = 20

        self.canvas.create_rectangle(
            panel_x, panel_y,
            panel_x + 200, panel_y + 140,
            fill='#000000', outline='#666699',
            stipple='gray50'
        )

        self.fps_text = self.canvas.create_text(
            panel_x + 10, panel_y + 20,
            text=f"FPS: {self.fps}",
            fill='#00ff00', anchor='w',
            font=('Arial', 12, 'bold')
        )

        self.active_text = self.canvas.create_text(
            panel_x + 10, panel_y + 45,
            text="Active: 0",
            fill='white', anchor='w',
            font=('Arial', 10)
        )

        self.particle_text = self.canvas.create_text(
            panel_x + 10, panel_y + 65,
            text="Particles: 0",
            fill='white', anchor='w',
            font=('Arial', 10)
        )

        self.type_text = self.canvas.create_text(
            panel_x + 10, panel_y + 85,
            text=f"Type: {self.current_type.capitalize()}",
            fill='#ffff00', anchor='w',
            font=('Arial', 10)
        )

        self.auto_text = self.canvas.create_text(
            panel_x + 10, panel_y + 110,
            text="Auto-show: OFF",
            fill='#ff6666', anchor='w',
            font=('Arial', 10)
        )

        # Instructions
        inst_y = WINDOW_HEIGHT - 30
        self.canvas.create_text(
            WINDOW_WIDTH // 2, inst_y,
            text="Click to launch | 1-6: Types | Space: Random | R: Auto | C: Clear | ESC: Quit",
            fill='#aaaaaa',
            font=('Arial', 10)
        )

    def update_ui(self):
        """Update UI text"""
        active = len(self.fireworks)
        particles = sum(len(fw.particles)
                        for fw in self.fireworks if fw.state == 'exploded')

        self.canvas.itemconfig(self.fps_text, text=f"FPS: {self.fps}")
        self.canvas.itemconfig(self.active_text, text=f"Active: {active}")
        self.canvas.itemconfig(
            self.particle_text, text=f"Particles: {particles}")
        self.canvas.itemconfig(
            self.type_text, text=f"Type: {self.current_type.capitalize()}")

        if self.auto_show:
            self.canvas.itemconfig(
                self.auto_text, text="Auto-show: ON", fill='#00ff00')
        else:
            self.canvas.itemconfig(
                self.auto_text, text="Auto-show OFF", fill='#ff6666')

    def on_click(self, event):
        """Handle mouse click"""
        self.launch_firework(event.x, event.y, self.current_type)

    def launch_firework(self, x, y, fw_type):
        """Launch a new firework"""
        self.fireworks.append(Firework(x, y, fw_type))

    def launch_random(self):
        """Launch random firework at random position"""
        x = random.randint(100, WINDOW_WIDTH - 100)
        types = ['rocket', 'peony', 'willow', 'palm', 'ring', 'cracker']
        self.launch_firework(x, 0, random.choice(types))

    def set_type(self, fw_type):
        """Set current firework type"""
        self.current_type = fw_type
        print(f"Selected: {fw_type.capitalize()}")

    def toggle_auto_show(self):
        """Toggle auto-show mode"""
        self.auto_show = not self.auto_show
        print(f"Auto-show: {'ON' if self.auto_show else 'OFF'}")

    def clear_all(self):
        """Clear all fireworks"""
        self.fireworks.clear()
        self.canvas.delete('firework')
        print("Cleared all fireworks")

    def quit(self):
        """Quit the application"""
        self.running = False
        self.root.quit()

    def update(self):
        """Main game loop"""
        if not self.running:
            return

        # Calculate delta time
        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time

        # Update FPS
        self.frame_count += 1
        self.fps_timer += dt
        if self.fps_timer >= 1.0:
            self.fps = self.frame_count
            self.frame_count = 0
            self.fps_timer = 0

        # Update stars (twinkling)
        for star in self.stars:
            star['brightness'] += (random.random() - 0.5) * \
                star['twinkle_speed']
            star['brightness'] = max(0.3, min(1.0, star['brightness']))

            # Update color based on brightness
            gray = int(255 * star['brightness'])
            color = f'#{gray:02x}{gray:02x}{gray:02x}'
            self.canvas.itemconfig(star['id'], fill=color)

        # Auto-show mode
        if self.auto_show:
            self.auto_show_timer += dt
            if self.auto_show_timer >= 1.5:
                self.auto_show_timer = 0
                self.launch_random()

        # Update fireworks
        for fw in self.fireworks:
            fw.update(dt)

        # Remobe dead fireworks
        self.fireworks = [fw for fw in self.fireworks if fw.is_alive()]

        # Render
        self.render()

        # Update UI
        self.update_ui()

        # Schedule next update
        self.root.after(int(1000 / FPS), self.update)

    def render(self):
        """Render all Fireworks"""
        # Clear previous fireworks
        self.canvas.delete('firework')

        for fw in self.fireworks:
            if fw.state == 'launching':
                # Draw trail
                if len(fw.trail) > 1:
                    self.canvas.create_line(
                        fw.trail,
                        fill='white',
                        width=2,
                        smooth=True,
                        tags='firework'
                    )

                # Drawf firework
                self.canvas.create_oval(
                    fw.x - 3, fw.y - 3,
                    fw.x + 3, fw.y + 3,
                    fill='white',
                    outline='',
                    tags='firework'
                )
            elif fw.state == 'exploded':
                # Draw particles
                for particle in fw.particles:
                    # Draw tail
                    if len(particle.trail) > 1:
                        for i in range(len(particle.trail) - 1):
                            alpha = int((i / len(particle.trail))
                                        * particle.alpha)
                            if alpha > 20:
                                self.canvas.create_line(
                                    particle.trail[i][0], particle.trail[i][1],
                                    particle.trail[i +
                                                   1][0], particle.trail[i + 1][1],
                                    fill=particle.color,
                                    width=1,
                                    tags='firework'
                                )

                # Draw particle with glow
                size = particle.size
                if particle.alpha > 100:
                    # Glow
                    self.canvas.create_oval(
                        particle.x - size * 2, particle.y - size * 2,
                        particle.x + size * 2, particle.y + size * 2,
                        fill=particle.color,
                        outline='',
                        stipple='gray25', tags='firework'
                    )

                    # Main particle
                    self.canvas.create_oval(
                        particle.x - size, particle.y - size,
                        particle.x + size, particle.y + size,
                        fill=particle.color,
                        outline='',
                        tags='firework'
                    )


if __name__ == '__main__':
    app = FireworkSimulator()
