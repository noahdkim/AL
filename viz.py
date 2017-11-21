import pygame
from tkinter import *


from al import AL
from world import World


class Visualization:
    def __init__(self, master):
        self.world = World()
        self.al = AL(self.world)
        self.py_world = PyWorld(self.world)
        self.msg_area = MessageArea(self.al, self.py_world, master)


class MessageArea:
    def __init__(self, al, py_world, master):
        """Initialize the message area.

        Args:
            al - al will receive the messages that are typed in
            py_world - py_world will be redrawn after al makes API requests
            master - from tkinter I think.

        """
        self.user_turn = True
        self.al = al
        self.py_world = py_world
        self.textarea = Text(master)
        self.textarea.grid(row=0, columnspan=3, sticky=N + S + E + W)
        self.textarea.config(state=DISABLED)
        Label(master, text="Enter Message: ").grid(row=1, column=0)
        self.msg_area = Entry(master)
        self.msg_area.grid(row=1, column=1)
        self.msg_area.bind('<Return>', lambda x: self.send_msg(self.al, self.user_turn))
        self.enter = Button(master, text='Send',
                            command=self.send_msg(self.al, self.user_turn)).grid(row=1, column=2)

    def send_msg(self, al, user_turn):
        """Add message to textarea and clear msg_area."""
        msg = self.msg_area.get()
        if user_turn and msg:
            self.textarea.tag_config("me", foreground="red")
            self.textarea.tag_config("AL", foreground="blue")
            self.textarea.config(state=NORMAL)
            self.textarea.insert(INSERT, 'ME: ', ("me"))
            self.textarea.insert(INSERT, '%s\n' % msg)
            self.textarea.config(state=DISABLED)
            self.msg_area.delete(0, 'end')
            self.user_turn = False
            # Display AL's response
            self.textarea.config(state=NORMAL)
            self.textarea.insert(INSERT, 'AL: ', ("AL"))
            self.textarea.insert(INSERT, '%s\n' % self.al.tell(msg))
            self.py_world.draw_world()
            self.py_world.animate()
            self.textarea.config(state=DISABLED)

            self.user_turn = True


class PyWorld:
    screen = pygame.display.set_mode((900, 600))

    def __init__(self, world):
        """Create visual representation of world based on world API using pygame.

        Args:
            world - world that AL interacts with

        """
        self.world = world
        pygame.display.init()
        pygame.init()
        self.draw_world()
        self.animate()

    def draw_world(self):
        """Display all objects."""
        self.screen.fill((255, 255, 255))
        for item_list in self.world.objects:
            for item in item_list:
                pygame.draw.rect(self.screen, item.color,
                                 pygame.Rect(item.x, item.y, item.width, item.height))
        self.clock = pygame.time.Clock()
        pygame.display.flip()
        self.clock.tick(60)

    def animate(self):
        """Move cubes until they collide with stationary object."""
        table_cube = self.world.objects[1][0]
        table = pygame.Rect(table_cube.x, table_cube.y, table_cube.width, table_cube.height)
        floor_cube = self.world.objects[1][1]
        floor = pygame.Rect(floor_cube.x, floor_cube.y, floor_cube.width, floor_cube.height)
        continue_animating = False
        for item in self.world.objects[0]:
            cube = pygame.Rect(item.x, item.y, item.width, item.height)
            if cube.colliderect(table) or \
               cube.colliderect(floor):
                item.speed_y = 0
            else:
                continue_animating = True
                item.x = item.x + item.speed_x
                item.y = item.y + item.speed_y
        self.draw_world()
        if(continue_animating):
            self.animate()


root = Tk()
app = Visualization(root)
root.mainloop()
