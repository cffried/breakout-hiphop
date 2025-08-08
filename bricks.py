# bricks.py

import pygame

class Brick:
    def __init__(self, x, y, width, height, color, hits=1, brick_type='normal'):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hits = hits
        self.destroyed = False
        self.brick_type = brick_type  # e.g., 'normal', 'side', 'powerup'

    def hit(self):
        if self.brick_type == 'indestructible':
            return  # No effect
        self.hits -= 1
        if self.hits <= 0:
            self.destroyed = True

    def draw(self, surface):
        if not self.destroyed:
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)  # black outline for clarity
