from tkinter import *

class Chat_Area:
    def __init__(self, master):
        self.user_turn = True

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
            print(self.msg_area.get())
            self.textarea.config(state=NORMAL)
            self.textarea.insert(INSERT, 'ME: %s\n' % msg)
            self.textarea.config(state=DISABLED)
            self.msg_area.delete(0, 'end')
            self.user_turn = False
            self.AL_response()

    def AL_response(self):
        self.textarea.config(state=NORMAL)
        self.textarea.insert(INSERT, 'AL: %s\n' % "Hello")
        self.textarea.config(state=DISABLED)
        self.user_turn = True
