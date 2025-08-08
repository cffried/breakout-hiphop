import pygame
from world import SCREEN_WIDTH, SCREEN_HEIGHT

class Paddle:
    def __init__(self):
        self.width = 150
        self.height = 20
        self.speed = 12
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 2 - self.width // 2,
            SCREEN_HEIGHT - 40,
            self.width,
            self.height
        )

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
