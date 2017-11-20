from world.world import World


class AL:
    def __init__(self, world):
        self.world = world

    def tell(self, msg):
        if "under" in msg:
            self.world.move(self.world.objects[0][0], self.world.table, "under")
            return 'Okay. I have moved the block under the table.'
        else:
            return 'Hello'
