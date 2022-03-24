from tkinter import *
from random import choice
from string import printable
import pyperclip


class Interface(Frame):

    def __init__(self, master):

        super(Interface, self).__init__(master)

        self.pack(expand = True)

        self.body(None, 13)
    
    def body(self, f , s):

        self.header = Label(self, font = (f, s, "bold"), text="Password Generator")

        self.password = Label(self, font = (f, s), text='')

        self.pass_button = Button(self, font = (f, s, "bold"), text="Generate",command=self.compute)

        for widget in self.children:

            self.children[widget].pack(pady = 13)

    def compute(self):

        self.pw = ''

        chars = printable[:95]

        for self.c in range(12):
            self.pw += choice(chars)

        pyperclip.copy(self.pw)

        self.password.config(text=f"{self.pw}")

        for widget in self.children:

            self.children[widget].pack()

if __name__ == "__main__":

    rt = Tk(None)

    rt.title("Password Generator")

    rt.geometry("362x362")

    Interface(rt)

    rt.mainloop(n = 0)