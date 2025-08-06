import pygame
from config import WHITE

# --- Special Colors ---
PURPLE = (150, 0, 200)
YELLOW = (255, 255, 0)

class Brick:
    def __init__(self, x, y, width=60, height=20, hp=1, color=WHITE, special=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.hp = hp
        self.color = color
        self.special = special  # Placeholder for future abilities

    def hit(self):
        """Reduce hp when hit, change color if needed, return True if destroyed."""
        self.hp -= 1

        # Special behavior: Purple bricks turn yellow when hp goes to 1
        if self.color == PURPLE and self.hp == 1:
            self.color = YELLOW

        return self.hp <= 0  # True if brick is destroyed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class BrickManager:
    def __init__(self, rows=5, cols=10, brick_width=60, brick_height=20, padding=5, offset_y=50):
        """Generate a grid of bricks with different properties."""
        self.bricks = []

        for row in range(rows):
            for col in range(cols):
                x = col * (brick_width + padding) + 40
                y = row * (brick_height + padding) + offset_y

                # Top row: Purple, 2 HP, turns yellow after 1 hit
                if row == 0:
                    color = PURPLE
                    hp = 2
                else:
                    # Example: stronger bricks lower down
                    hp = 1 if row < 2 else 2
                    color = (200, 200 - row * 30, 50 + row * 40)

                # Create brick object
                self.bricks.append(Brick(x, y, brick_width, brick_height, hp, color))

    def draw(self, surface):
        """Draw all bricks."""
        for brick in self.bricks:
            brick.draw(surface)

    def check_collision(self, ball_rect):
        """
        Check collisions with the ball.
        - Removes brick if destroyed
        - Returns True if collision occurred (for ball bounce)
        """
        for brick in self.bricks[:]:  # Copy to avoid issues when removing
            if ball_rect.colliderect(brick.rect):
                destroyed = brick.hit()
                if destroyed:
                    self.bricks.remove(brick)
                return True  # Only handle one collision per frame
        return False
