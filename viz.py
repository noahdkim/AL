import pygame
from tkinter import *


from al import AL
from visualization.message_area import MessageArea
from visualization.py_world import PyWorld
from world.world import World


class Visualization:
    def __init__(self, master):
        self.world = World()
        self.al = AL(self.world)
        self.py_world = PyWorld(self.world)
        self.msg_area = MessageArea(self.al, self.py_world, master)

root = Tk()
app = Visualization(root)
root.mainloop()
