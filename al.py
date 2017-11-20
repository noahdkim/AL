from world.world import World


class AL:
    def __init__(self):
        self.world = World()
    def tell(self, msg):
        if "under" in msg:
            self.world.move(self.world.objects[0], self.world.table, "under")
            return 'Okay. I have moved the block under the table.'
        else:
            return 'Hello'
