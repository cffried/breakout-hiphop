import pygame
import sys
from config import WIDTH, HEIGHT, BLACK, FPS
from paddle import Paddle
from ball import Ball
from bricks import BrickManager


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout: Hip-Hop Edition")
        self.clock = pygame.time.Clock()

        # --- Game Objects ---
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = BrickManager()  # Grid of bricks

    def run(self):
        """Main game loop."""
        while True:
            # --- Event Handling ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # --- Player Input ---
            keys = pygame.key.get_pressed()
            self.paddle.move(keys)

            # --- Ball Update ---
            if not self.ball.update(self.paddle):
                print("Game Over!")
                pygame.quit()
                sys.exit()

            # --- Brick Collision ---
            if self.bricks.check_collision(self.ball):
                # Simple behavior: reverse ball's Y direction when hitting a brick
                self.ball.speed[1] = -self.ball.speed[1]

            # --- Win Condition ---
            if not self.bricks.bricks:
                print("You Win!")
                pygame.quit()
                sys.exit()

            # --- Drawing ---
            self.screen.fill(BLACK)
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.bricks.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)


# --- Entry Point
