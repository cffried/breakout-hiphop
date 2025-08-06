import pygame, sys
from config import WIDTH, HEIGHT, BLACK, FPS
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout: Hip-Hop Edition")
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.ball = Ball()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.paddle.move(keys)

            if not self.ball.update(self.paddle):
                print("Game Over!")
                pygame.quit()
                sys.exit()

            self.screen.fill(BLACK)
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
