class Cube:
    def __init__(self, color, x, y):
        """Initialize and draw square."""
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.color = color

    def move(self, obj, relation):
        """Move square on top of object."""
        if(relation == "top"):
            self.y = obj.y - self.height
        elif(relation == "under"):
            # Possibly include gravity and a random range so cubes are not floating.
            self.y = obj.y + obj.height
            self.speed_y = 1
        print(relation, self.speed_y)
        return self
        self.draw(self.screen, self.color, self.cube_rect)
