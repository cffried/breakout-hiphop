import pygame
import random

# === Constants ===
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_PADDING = 5
TOP_OFFSET = 50
LEFT_OFFSET = 40

# === Color Hierarchy (ROYGBIV) ===
COLOR_ORDER = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# === Brick Config (no hp, just color downgrade) ===
def build_brick_types():
    brick_types = {}
    for i, color in enumerate(COLOR_ORDER):
        next_color = COLOR_ORDER[i + 1] if i + 1 < len(COLOR_ORDER) else None
        brick_types[color] = {
            "next_color": next_color,
            "width": 1 + (i // 2),  # TODO: Adjust to balance tanky bricks
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
            "rainbow": (255, 255, 255),  # TODO: Add animation or cycling effect later
        }

        pygame.draw.rect(surface, color_map.get(self.color, (255, 255, 255)), self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

# === BrickManager Class ===
class BrickManager:
    def __init__(self):
        self.bricks = []
        all_colors = COLOR_ORDER + ["rainbow"]

        rows = 6
        cols = 12

        for row in range(rows):
            col = 0
            while col < cols:
                color = random.choice(all_colors)
                width = BRICK_TYPES[color]["width"]
                if col + width > cols:
                    break
                self.bricks.append(Brick(row, col, color))
                col += width

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
