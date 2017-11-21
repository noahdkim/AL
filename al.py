from world import World


class AL:
    def __init__(self, world=None):
        self.world = world if world is not None else World()

    def tell(self, msg):
        return 'Hello!'
