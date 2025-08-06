import pygame
from config import WIDTH, HEIGHT, WHITE

class Paddle:
    def __init__(self):
        self.width, self.height = 100, 15
        self.speed = 7
        self.rect = pygame.Rect(WIDTH//2 - self.width//2, HEIGHT - 40, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
