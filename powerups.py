# powerups.py

class PowerUpManager:
    def __init__(self, paddle):
        self.paddle = paddle

    def on_brick_hit(self, brick):
        if brick.color == (255, 0, 0):  # RED
            self.paddle.increase_speed()

