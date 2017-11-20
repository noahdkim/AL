import pygame

from world.cube import Cube
from world.structures import Floor
from world.structures import Table


class World:
    floor = Floor()
    table = Table()

    def __init__(self):
        x = 30
        y = 30
        orange = (255, 100, 0)
        self.stationary = [self.floor, self.table]
        self.objects = [[Cube(orange, x, y)], self.stationary]

    def move(self, object1, object2, relation):
        self.objects[0][0] = self.objects[0][0].move(self.table, relation)

    def animate(self):
        animate = True
        while animate:
            for cube in self.objects:
                animate = animate and cube.speed_y
                cube = cube.animate(self.table, self.floor)
            pygame.display.flip()
