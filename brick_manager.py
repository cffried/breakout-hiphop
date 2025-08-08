import pygame
from bricks import Brick
from world import SCREEN_WIDTH, BRICK_WIDTH, BRICK_HEIGHT, BRICK_PADDING, TOP_OFFSET, RED, ORANGE, YELLOW

# For future level configs
DEFAULT_LAYOUT = [
    {"color": YELLOW, "hits": 1, "rows": 3},
    {"color": ORANGE, "hits": 2, "rows": 3},
    {"color": RED,    "hits": 1, "rows": 2},
]

COL_MARGIN = 2  # will be configurable per stage later


class BrickManager:
    def __init__(self, layout=DEFAULT_LAYOUT):
        self.bricks = []
        self.layout = layout
        self.create_bricks()

    def create_bricks(self):
        total_cols = SCREEN_WIDTH // (BRICK_WIDTH + BRICK_PADDING)
        usable_cols = total_cols - (COL_MARGIN * 2)  # trim sides

        grid_width = usable_cols * (BRICK_WIDTH + BRICK_PADDING) - BRICK_PADDING
        x_start = (SCREEN_WIDTH - grid_width) // 2

        y_offset = TOP_OFFSET

        for row in self.layout:
            color = row["color"]
            hits = row["hits"]
            for _ in range(row["rows"]):
                for col in range(usable_cols):
                    x = x_start + col * (BRICK_WIDTH + BRICK_PADDING)
                    y = y_offset
                    brick = Brick(x, y, BRICK_WIDTH, BRICK_HEIGHT, color, hits)
                    self.bricks.append(brick)
                y_offset += BRICK_HEIGHT + BRICK_PADDING

    def draw(self, surface):
        for brick in self.bricks:
            brick.draw(surface)

    def update(self):
        self.bricks = [b for b in self.bricks if not b.destroyed]

    def check_collision(self, ball):
        """Returns True if the ball hit any brick."""
        for brick in self.bricks:
            if brick.rect.colliderect(ball.rect):
                brick.hit()
                return True
        return False
