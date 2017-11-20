import pygame


class Cube:
    color = (0, 128, 255)  # Orange # amazing
    width, height = 60, 60
    speed_x = 0
    speed_y = 1
    screen = 0
    cube_rect = pygame.Rect(30, 30, width, height)
    def __init__(self, screen, color, x, y):
        """Initialize and draw square."""
        self.screen = screen
        self. color = color
        self.cube_rect = pygame.Rect(x, y, self.width, self.height)
        self.draw(self.screen, self.color, self.cube_rect)

    def draw(self, screen, color, cube_rect):
        """Draw square on screen."""
        pygame.draw.rect(screen, color, cube_rect)

    def move(self, obj, relation):
        """Move square on top of object."""
        if(relation == "top"):
            self.cube_rect.y = obj.y - self.height
        elif(relation == "under"):
            # Possibly include gravity and a random range so cubes are not floating.
            self.cube_rect.y = obj.y + obj.height
            self.speed_y = 1
        print(relation, self.speed_y)
        return self
        self.draw(self.screen, self.color, self.cube_rect)

    def animate(self, table, floor):
        if self.cube_rect.colliderect(table.table_rect) or \
           self.cube_rect.colliderect(floor.floor_rect):
            self.speed_y = 0
        else:
            self.cube_rect.x = self.cube_rect.x + self.speed_x
            self.cube_rect.y = self.cube_rect.y + self.speed_y
        return self
