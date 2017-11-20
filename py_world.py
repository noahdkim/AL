import pygame

class PyWorld:
    screen = pygame.display.set_mode((900, 600))
    def __init__(self, world):
        self.world = world
        pygame.display.init()
        pygame.init()
        self.draw_world()
        self.clock = pygame.time.Clock()
        pygame.display.flip()
        self.clock.tick(60)

    def draw_world(self):
        self.screen.fill((255, 255, 255))
        for item in self.world.objects:
            print("1")
            pygame.draw.rect(self.screen, item.color,
                             pygame.Rect(item.x, item.y, item.width, item.height))

    def animate(self, table, floor):
        if self.cube_rect.colliderect(table.table_rect) or \
           self.cube_rect.colliderect(floor.floor_rect):
            self.speed_y = 0
        else:
            self.cube_rect.x = self.cube_rect.x + self.speed_x
            self.cube_rect.y = self.cube_rect.y + self.speed_y
        return self
