# world.py

# world.py (extended)

import pygame

# === Screen Config ===
SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080
FPS = 60

# Create the actual screen surface
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout: Hip-Hop Edition")



# === Color Palette ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 215, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
INDIGO = (75, 0, 130)
VIOLET = (138, 43, 226)
RAINBOW = (255, 255, 255)  # Placeholder for future FX

# === Bricks ===
BRICK_WIDTH = 70
BRICK_HEIGHT = 30
BRICK_PADDING = 6

# === Layout ===
TOP_OFFSET = 60  # Space from top to first brick row
