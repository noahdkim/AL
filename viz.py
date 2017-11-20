import pygame
from tkinter import *


from al import AL
from message_area import MessageArea
from py_world import PyWorld
from world.world import World


class Visualization:
    def __init__(self, master):
        self.world = World()
        self.al = AL(self.world)
        self.msg_area = MessageArea(self.al, master)
        self.py_world = PyWorld(self.world)

root = Tk()
app = Visualization(root)
root.mainloop()
