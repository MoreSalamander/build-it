"""Firework class with different explosion patterns"""
import random
import math
from particle import Particle
from config import *


class Firework:
    def __init__(self, x, y, firework_type='rocket'):
        self.x = x
        self.y = WINDOW_HEIGHT
        self.vx = random.uniform(-1, 1)
        self.vy = -LAUNCH_SPEED + random.uniform(-2, 2)

        self.type = firework_type
        self.state = 'launching'  # 'launching' or 'exploded'
        self.alive = True
        self.trail = []
        self.particles = []

        # Target explosion height
        self.target_y = WINDOW_HEIGHT * (0.15 + random.random() * 0.15)

        # Choose color scheme
        self.color_scheme = random.choice(list(COLORS.keys()))

    def update(self, dt):
        """Update firwork state"""
        if self.state == 'launching':
            # Store trail
            self.trail.append((self.x, self.y))
            if len(self.trail) > 20:
                self.trail.pop(0)

            # Apply gravity
            self.vy += GRAVITY * 0.5 * dt * 60

            # Update position
            self.x += self.vx * dt * 60
            self.y += self.vy * dt * 60

            # Check if should explode
            if self.y <= self.target_y or self.vy > 0:
                self.explode()

        elif self.state == 'exploded':
            # Update particles
            for particle in self.particles:
                particle.update(dt)

            # Remove dead particles
            self.particles = [p for p in self.particles if p.is_alive()]

            # Check if all fireworks are dead
            if len(self.particles) == 0:
                self.alive = False

    def explode(self):
        """Create explosion based on type"""
        self.state = 'exploded'

        patterns = {
            'rocket': lambda: self.create_sphere(100),
            'peony': lambda: self.create_sphere(150),
            'willow': lambda: self.create_willow(200),
            'palm': lambda: self.create_palm(80),
            'ring': lambda: self.create_ring(100),
            'cracker': lambda: self.create_cracker(50)
        }

        pattern_func = patterns.get(self.type, patterns['rocket'])
        pattern_func()

    def create_sphere(self, num_particles):
        """Spherical explosion"""
        colors = COLORS[self.color_scheme]

        for i in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(EXPLOSION_SPEED_MIN, EXPLOSION_SPEED_MAX)

            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed

            color = random.choice(colors)
            lifetime = random.randint(
                PARTICLE_LIFETIME_MIN, PARTICLE_LIFETIME_MAX)

            self.particles.append(
                Particle(self.x, self.y, vx, vy, color, lifetime))

    def create_willow(self, num_particles):
        """Willow/drooping effect"""
        colors = COLORS[self.color_scheme]

        for i in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(EXPLOSION_SPEED_MIN, EXPLOSION_SPEED_MAX)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed - 2  # Upward bias

            color = random.choice(colors)
            lifetime = random.randint(
                PARTICLE_LIFETIME_MAX, PARTICLE_LIFETIME_MAX + 40)

            particle = Particle(self.x, self.y, vx, vy, color, lifetime)
            self.particles.append(particle)

    def create_palm(self, num_particles):
        """Palm tree pattern"""
        colors = COLORS[self.color_scheme]
        branches = 5
        per_branch = num_particles // branches

        for branch in range(branches):
            base_angle = (branch / branches) * 2 * math.pi

            for i in range(per_branch):
                angle = base_angle + random.uniform(-0.3, 0.3)
                speed = random.uniform(
                    EXPLOSION_SPEED_MIN + 2, EXPLOSION_SPEED_MAX)
                vx = math.cos(angle) * speed
                vy = math.sin(angle) * speed - 5  # Strong upward

                color = random.choice(colors)
                lifetime = random.randint(
                    PARTICLE_LIFETIME_MIN + 20, PARTICLE_LIFETIME_MAX + 20)

                self.particles.append(
                    Particle(self.x, self.y, vx, vy, color, lifetime))

    def create_ring(self, num_particles):
        """Ring pattern"""
        colors = COLORS[self.color_scheme]

        for i in range(num_particles):
            angle = (i / num_particles) * 2 * math.pi
            speed = random.uniform(
                EXPLOSION_SPEED_MIN + 1, EXPLOSION_SPEED_MAX)

            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed * 0.3  # Flatten

            color = random.choice(colors)
            lifetime = random.randint(
                PARTICLE_LIFETIME_MIN, PARTICLE_LIFETIME_MAX)

            self.particles.append(
                Particle(self.x, self.y, vx, vy, color, lifetime))

    def create_cracker(self, num_particles):
        """Multiple small bursts"""
        colors = COLORS[self.color_scheme]
        num_bursts = random.randint(3, 5)

        for burst in range(num_bursts):
            burst_angle = random.uniform(0, 2 * math.pi)
            burst_distance = random.uniform(20, 50)

            burst_x = self.x + burst_distance * math.cos(burst_angle)
            burst_y = self.y + burst_distance * math.sin(burst_angle)

            particles_per_burst = num_particles // num_bursts

            for i in range(particles_per_burst):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(2, 5)

                vx = math.cos(angle) * speed
                vy = math.sin(angle) * speed

                color = random.choice(colors)
                lifetime = random.randint(30, 60)

                particle = Particle(burst_x, burst_y, vx, vy, color, lifetime)
                particle.size = 2
                self.particles.append(particle)

    def is_alive(self):
        return self.alive
