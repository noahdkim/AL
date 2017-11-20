import pygame


class Table:
    color = (165, 42, 42)  # brown
    width, height = 900, 50
    x, y = 0, 300
    screen = 0
    table_rect = pygame.Rect(x, y, width, height)
    def __init__(self):
        """Initialize and draw square."""


    def draw(self):
        """Draw square on screen."""
        pygame.draw.rect(pygame.display.set_mode((900, 600)), self.color,
                         pygame.Rect(self.x, self.y, self.width, self.height))


class Floor:
    color = (0, 0, 0)  # black
    width, height = 900, 50
    x, y = 0, 550
    screen = 0
    floor_rect = pygame.Rect(x, y, width, height)

    def __init__(self):
        """Initialize and draw square."""

    def draw(self):
        """Draw square on screen."""
        pygame.draw.rect(pygame.display.set_mode((900, 600)), self.color,
                         pygame.Rect(self.x, self.y, self.width, self.height))
