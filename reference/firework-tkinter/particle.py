"""Particle class for firework effects"""
import math
from config import *


class Particle:
    def __init__(self, x, y, vx, vy, color, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.alpha = 255
        self.size = 3
        self.trail = []
        self.alive = True

    def update(self, dt):
        """Update particle physics"""
        if not self.alive:
            return

        # Store trail
        if len(self.trail) < 10:
            self.trail.append((self.x, self.y))
        else:
            self.trail.pop(0)
            self.trail.append((self.x, self.y))

        # Apply gravity
        self.vy += GRAVITY * dt * 60

        # Apply drag
        self.vx *= DRAG
        self.vy *= DRAG

        # Update position
        self.x += self.vx * dt * 60
        self.y += self.vy * dt * 60

        # Update lifetime
        self.lifetime -= 1

        # Fade out
        if self.lifetime < self.max_lifetime * 0.3:
            self.alpha = int((self.lifetime / (self.max_lifetime * 0.3)) * 255)

        # Check if dead
        if self.lifetime <= 0 or self.y > WINDOW_HEIGHT + 50:
            self.alive = False

    def is_alive(self):
        return self.alive
