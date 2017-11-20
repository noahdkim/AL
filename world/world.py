import pygame

from world.cube import Cube
from world.structures import Floor
from world.structures import Table



class World:
    floor = Floor()
    table = Table()
    def __init__(self):
        screen = pygame.display.set_mode((900, 600))
        x = 30
        y = 30
        orange = (255, 100, 0)
        self.objects = [Cube(screen, orange, x, y)]


    def move(self, object1, object2, relation):
        self.objects[0] = self.objects[0].move(self.table, relation)
        self.animate()

    def animate(self):
        animate = True
        while animate:
            for cube in self.objects:
                animate = animate and cube.speed_y
                cube = cube.animate(self.table, self.floor)
            pygame.display.flip()
