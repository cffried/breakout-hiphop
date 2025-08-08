import pygame
import random
from world import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    BRICK_WIDTH, BRICK_HEIGHT, BRICK_PADDING, TOP_OFFSET
)

# === ROYGBIV Color Hierarchy ===
COLOR_ORDER = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# === Brick Type Configuration ===
def build_brick_types():
    brick_types = {}
    for i, color in enumerate(COLOR_ORDER):
        next_color = COLOR_ORDER[i + 1] if i + 1 < len(COLOR_ORDER) else None
        brick_types[color] = {
            "next_color": next_color,
            "width": 1 + (i // 2),  # TODO: Tune this to balance visual weight
            "special_abilities": [],
        }

    brick_types["rainbow"] = {
        "next_color": "random",
        "width": 4,
        "special_abilities": [],
    }

    return brick_types

BRICK_TYPES = build_brick_types()

# === Brick Class ===
class Brick:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.set_props_from_color()
        self.alive = True

        total_width = self.width * BRICK_WIDTH + (self.width - 1) * BRICK_PADDING
        self.rect = pygame.Rect(
            LEFT_OFFSET + col * (BRICK_WIDTH + BRICK_PADDING),
            TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_PADDING),
            total_width,
            BRICK_HEIGHT
        )

    def set_props_from_color(self):
        props = BRICK_TYPES[self.color]
        self.next_color = props["next_color"]
        self.width = props["width"]
        self.special_abilities = props["special_abilities"]

    def take_hit(self):
        if self.next_color == "random":
            current_index = COLOR_ORDER.index(self.color) if self.color in COLOR_ORDER else -1
            if current_index != -1 and current_index < len(COLOR_ORDER) - 1:
                self.color = random.choice(COLOR_ORDER[current_index + 1:])
                self.set_props_from_color()
            else:
                self.alive = False
        elif self.next_color:
            self.color = self.next_color
            self.set_props_from_color()
        else:
            self.alive = False
        return None

    def draw(self, surface):
        if not self.alive:
            return

        color_map = {
            "red": (255, 0, 0),
            "orange": (255, 165, 0),
            "yellow": (255, 215, 0),
            "green": (0, 200, 0),
            "blue": (0, 100, 255),
            "indigo": (75, 0, 130),
            "violet": (138, 43, 226),
            "rainbow": (255, 255, 255),  # TODO: Animate or rainbow-cycle
        }

        pygame.draw.rect(surface, color_map.get(self.color, (255, 255, 255)), self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

    @classmethod
    def create_at_pixel(cls, x, y, color):
        brick = cls.__new__(cls)
        brick.color = color
        brick.set_props_from_color()
        brick.alive = True
        total_width = brick.width * BRICK_WIDTH + (brick.width - 1) * BRICK_PADDING
        brick.rect = pygame.Rect(x, y, total_width, BRICK_HEIGHT)
        return brick

# === BrickManager Class ===
class BrickManager:
    def __init__(self):
        self.bricks = []
        all_colors = COLOR_ORDER + ["rainbow"]

        rows = 8

        # Define usable horizontal space for brick layout
        cluster_padding = 2 * (BRICK_WIDTH + BRICK_PADDING)
        usable_width = SCREEN_WIDTH - cluster_padding * 2
        x_start = cluster_padding
        x_max = SCREEN_WIDTH - cluster_padding

        for row in range(rows):
            y = TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_PADDING)
            x = x_start

            while x < x_max:
                color = random.choice(all_colors)
                width = BRICK_TYPES[color]["width"]
                pixel_width = width * BRICK_WIDTH + (width - 1) * BRICK_PADDING

                if x + pixel_width > x_max:
                    break  # No room for this brick

                brick = Brick.create_at_pixel(x, y, color)
                self.bricks.append(brick)
                x += pixel_width + BRICK_PADDING

    def update(self):
        self.bricks = [b for b in self.bricks if b.alive]

    def draw(self, surface):
        for brick in self.bricks:
            brick.draw(surface)

    def check_collision(self, ball):
        for brick in self.bricks:
            if brick.alive and brick.rect.colliderect(ball.rect):
                brick.take_hit()
                return True
        return False
