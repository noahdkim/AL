import pygame

class PyWorld:
    screen = pygame.display.set_mode((900, 600))

    def __init__(self, world):
        """Create visual representation of world based on world API using pygame.

        Args:
            world - world that AL interacts with

        """
        self.world = world
        pygame.display.init()
        pygame.init()
        self.draw_world()
        self.animate()

    def draw_world(self):
        """Display all objects."""
        self.screen.fill((255, 255, 255))
        for item_list in self.world.objects:
            for item in item_list:
                pygame.draw.rect(self.screen, item.color,
                                 pygame.Rect(item.x, item.y, item.width, item.height))
        self.clock = pygame.time.Clock()
        pygame.display.flip()
        self.clock.tick(60)

    def animate(self):
        """Move cubes until they collide with stationary object."""
        table_cube = self.world.objects[1][0]
        table = pygame.Rect(table_cube.x, table_cube.y, table_cube.width, table_cube.height)
        floor_cube = self.world.objects[1][1]
        floor = pygame.Rect(floor_cube.x, floor_cube.y, floor_cube.width, floor_cube.height)
        continue_animating = False
        for item in self.world.objects[0]:
            cube = pygame.Rect(item.x, item.y, item.width, item.height)
            if cube.colliderect(table) or \
               cube.colliderect(floor):
                item.speed_y = 0
            else:
                continue_animating = True
                item.x = item.x + item.speed_x
                item.y = item.y + item.speed_y
        self.draw_world()
        if(continue_animating):
            self.animate()
