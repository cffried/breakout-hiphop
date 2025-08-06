import pygame
from config import WHITE

class Brick:
    def __init__(self, x, y, width=60, height=20, hp=1, color=WHITE, special=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.hp = hp
        self.color = color
        self.special = special  # placeholder for future abilities

    def hit(self):
        """Reduce hp when hit, return True if destroyed."""
        self.hp -= 1
        return self.hp <= 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class BrickManager:
    def __init__(self, rows=5, cols=10, brick_width=60, brick_height=20, padding=5, offset_y=50):
        self.bricks = []
        for row in range(rows):
            for col in range(cols):
                x = col * (brick_width + padding) + 40
                y = row * (brick_height + padding) + offset_y
                # Example: make top rows stronger
                hp = 1 if row < 2 else 2
                color = (200, 200 - row * 30, 50 + row * 40)
                self.bricks.append(Brick(x, y, brick_width, brick_height, hp, color))

    def draw(self, surface):
        for brick in self.bricks:
            brick.draw(surface)

    def check_collision(self, ball_rect):
        """Check collisions with the ball and remove bricks as needed."""
        for brick in self.bricks[:]:
            if ball_rect.colliderect(brick.rect):
                destroyed = brick.hit()
                if destroyed:
                    self.bricks.remove(brick)
                # Simple bounce: reverse Y direction
                return True
        return False
