import pygame


class Table:
    color = (165, 42, 42)  # brown
    width, height = 900, 50
    x, y = 0, 300
    screen = 0
    table_rect = pygame.Rect(x, y, width, height)


class Floor:
    color = (0, 0, 0)  # black
    width, height = 900, 50
    x, y = 0, 550
    screen = 0
    floor_rect = pygame.Rect(x, y, width, height)
