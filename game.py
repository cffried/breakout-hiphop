# game.py

import pygame
import sys

from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
from world import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FPS
from powerups import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()

        # --- Game Objects ---
        self.screen = SCREEN
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = BrickManager()
        self.clock = pygame.time.Clock()
        self.powerups = PowerUpManager(self.paddle)  # 💡 pass paddle

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
            if self.bricks.check_collision(self.ball,powerup_manager=self.powerups):
                # Reverse Y direction on hit
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
