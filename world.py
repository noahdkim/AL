ORANGE = (255, 100, 0)
BROWN = (165, 42, 42)
BLACK = (0, 0, 0)


class World:
    def __init__(self):
        cube = Cube(ORANGE)
        table = Table(BROWN)
        floor = Floor(BLACK)
        self.objects = [cube, table, floor]
        self.relations = [('on', cube, table), ('on', table, floor)]


class ColoredObject:
    def __init__(self, color):
        self.color = color


class Cube(ColoredObject):
    pass


class Table(ColoredObject):
    pass


class Floor(ColoredObject):
    pass
