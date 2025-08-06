import pygame, sys
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
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = BrickManager()  # <-- add bricks

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.paddle.move(keys)

            # Update ball and check collisions
            if not self.ball.update(self.paddle):
                print("Game Over!")
                pygame.quit()
                sys.exit()

            # Ball hits bricks
            if self.bricks.check_collision(self.ball.rect):
                self.ball.speed[1] = -self.ball.speed[1]

            # Win condition: no bricks left
            if not self.bricks.bricks:
                print("You Win!")
                pygame.quit()
                sys.exit()

            # Draw everything
            self.screen.fill(BLACK)
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.bricks.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
