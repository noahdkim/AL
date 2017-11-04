from tkinter import *

from al import AL
from world.world import World
class Visualization:
    def __init__(self, master):
        self.al = AL()
        self.user_turn = True
        self.world = World()
        self.textarea = Text(master)
        self.textarea.grid(row=0, columnspan=3, sticky=N + S + E + W)
        self.textarea.config(state=DISABLED)

        Label(master, text="Enter Message: ").grid(row=1, column=0)
        self.msg_area = Entry(master)
        self.msg_area.grid(row=1, column=1)
        self.msg_area.bind('<Return>', lambda x: self.send_msg(self.user_turn))

        self.enter = Button(master, text='Send', command=self.send_msg(self.user_turn)).grid(row=1, column=2)

    def send_msg(self, user_turn):
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
            self.world.al_command(msg)
            self.textarea.config(state=DISABLED)
            self.user_turn = True


root = Tk()
app = Visualization(root)
root.mainloop()
