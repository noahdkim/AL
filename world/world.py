import pygame
from world.cube import Cube
from world.table import Table, Floor

class World:
    screen = pygame.display.set_mode((900, 600))
    x = 30
    y = 30
    clock = pygame.time.Clock()
    orange = (255, 100, 0)
    orange_cube = Cube(screen, orange, x, y)
    table = Table(screen)
    floor = Floor(screen)
    cubes = [orange_cube]

    def __init__(self):
        pygame.init()
        self.screen.fill((255, 255, 255))
        self.table.draw()
        self.floor.draw()
        self.orange_cube = Cube(self.screen, self.orange, self.x, self.y)
        self.animate(self.cubes)
        pygame.display.flip()
        self.clock.tick(60)


    def al_command(self, instruct):
        pygame.event.pump()
        self.screen.fill((255, 255, 255))
        self.floor.draw()
        self.table.draw()
        self.cubes[0] = self.cubes[0].move(self.table, "under")
        self.animate(self.cubes)
        pygame.display.flip()

    def animate(self, cubes):
        animate = True
        while animate:
            pygame.event.pump()
            self.screen.fill((255, 255, 255))
            self.floor.draw()
            self.table.draw()
            for cube in cubes:
                animate = animate and cube.speed_y
                cube = cube.animate(self.table, self.floor)
            pygame.display.flip()
