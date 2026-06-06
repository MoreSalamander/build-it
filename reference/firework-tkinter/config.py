"""Configuration for Firework Simulator"""
# Window settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
FPS = 60

# Physics
GRAVITY = 0.15
DRAG = 0.99

# Firework settings
LAUNCH_SPEED = 15
EXPLOSION_SPEED_MIN = 3
EXPLOSION_SPEED_MAX = 8
PARTICLE_LIFETIME_MIN = 60
PARTICLE_LIFETIME_MAX = 120

# Colors (RGB format)
COLORS = {
    'red': ['#ff3232', '#ff6464', '#c80000'],
    'blue': ['#3264ff', '#6496ff', '#1e46c8'],
    'green': ['#32ff64', '#64ff96', '#1ec846'],
    'gold': ['#ffd700', '#ffeb64', '#c8aa00'],
    'purple': ['#c832ff', '#dc64ff', '#961ec8'],
    'white': ['#ffffff', '#f0f0ff', '#c8c8dc'],
    'orange': ['#ffa500', '#ffc864', '#c87800'],
    'pink': ['#ffb6c1', '#ff7896', '#c86478']
}

# Background
BG_COLOR = '#0a0a1e'
STAR_COUNT = 100
