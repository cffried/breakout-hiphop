import pygame

# === Central Brick Behavior Dictionary ===
BRICK_BEHAVIOR = {
    "purple": {"hits": 1, "next": None},
    "purple_cracked": {"hits": 1, "next": "yellow"},
    "yellow": {"hits": 1, "next": None},
    "orange": {"hits": 1, "next": "yellow"},
    "red":    {"hits": 1, "next": "orange"},
    "pink":   {"hits": 1, "next": "red"},
    "pink_special": {"hits": 3, "next": ["purple_cracked", "yellow", None]},
}

# === Brick Dimensions ===
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_PADDING = 5
TOP_OFFSET = 50
LEFT_OFFSET = 40

# === Brick Class ===
class Brick:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.set_behavior_from_color()
        self.alive = True
        self.rect = pygame.Rect(
            LEFT_OFFSET + col * (BRICK_WIDTH + BRICK_PADDING),
            TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_PADDING),
            BRICK_WIDTH,
            BRICK_HEIGHT
        )

    def set_behavior_from_color(self):
        behavior = BRICK_BEHAVIOR[self.color]
        self.hits = behavior["hits"]
        self.next = behavior["next"]

    def take_hit(self):
        self.hits -= 1
        if self.hits <= 0:
            if isinstance(self.next, list):
                # Handle multi-stage brick with queue
                next_color = self.next.pop(0)
                if next_color:
                    self.color = next_color
                    self.set_behavior_from_color()
                else:
                    self.alive = False
            elif self.next:
                self.color = self.next
                self.set_behavior_from_color()
            else:
                self.alive = False

    def draw(self, surface):
        if not self.alive:
            return
        color_map = {
            "purple": (160, 32, 240),
            "purple_cracked": (200, 100, 255),
            "yellow": (255, 215, 0),
            "orange": (255, 165, 0),
            "red": (255, 0, 0),
            "pink": (255, 105, 180),
            "pink_special": (255, 105, 180),
        }
        pygame.draw.rect(surface, color_map.get(self.color, (255, 255, 255)), self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)  # outline

# === BrickManager Class ===
class BrickManager:
    def __init__(self):
        self.bricks = []

        # === Row 0: Sparse Pink Special Row ===
        pink_special_cols = [1, 4, 7, 10]
        for col in pink_special_cols:
            self.bricks.append(Brick(0, col, "pink_special"))

        # === Row 1: Purple ===
        for col in range(12):
            self.bricks.append(Brick(1, col, "purple"))

        # === Row 2: Yellow ===
        for col in range(12):
            self.bricks.append(Brick(2, col, "yellow"))

        # === Row 3: Orange ===
        for col in range(12):
            self.bricks.append(Brick(3, col, "orange"))

        # === Row 4: Red ===
        for col in range(12):
            self.bricks.append(Brick(4, col, "red"))

        # === Row 5: Pink ===
        for col in range(12):
            self.bricks.append(Brick(5, col, "pink"))

    def update(self):
        self.bricks = [b for b in self.bricks if b.alive]

    def draw(self, surface):
        for brick in self.bricks:
            brick.draw(surface)

    def check_collision(self, ball):
        for brick in self.bricks:
            if brick.alive and brick.rect.colliderect(ball.rect):
                brick.take_hit()
                return True  # stop after first collision
        return False
