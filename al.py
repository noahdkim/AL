from world.world import World


class AL:
    def tell(self, msg, world):
        if "under" in msg:
            world.al_command(msg)
            return 'Okay. I have moved the block under the table.'
        else:
            return 'Hello'
