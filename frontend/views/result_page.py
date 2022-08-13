from tkinter import *
from PIL import Image, ImageTk

from frontend.resources import Constants


class ResultPage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model

        label = Label(self, text="This Is The Homepage", bg=Constants.main_color, fg="white")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
