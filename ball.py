import pygame
from config import WIDTH, HEIGHT, WHITE

class Ball:
    def __init__(self):
        self.radius = 10
        self.rect = pygame.Rect(WIDTH//2 - self.radius, HEIGHT//2 - self.radius, self.radius*2, self.radius*2)
        self.speed = [4, -4]

    def update(self, paddle):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]

        if self.rect.colliderect(paddle.rect):
            self.speed[1] = -self.speed[1]

        return self.rect.bottom < HEIGHT  # True = alive, False = game over

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)
