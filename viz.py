import pygame
from tkinter import *


from al import AL
from world.world import World
from message_area import MessageArea


class Visualization:
    def __init__(self, master):
        self.al = AL()
        self.msg_area = MessageArea(self.al, master)
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.flip()
        self.clock.tick(60)

root = Tk()
app = Visualization(root)
root.mainloop()
