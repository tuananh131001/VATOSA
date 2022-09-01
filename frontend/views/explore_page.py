from tkinter import *
from PIL import Image, ImageTk

from frontend.resources import Constants
from frontend.control import ControlModel


class ExplorePage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model

        ControlModel.create_nav(self, self.controller, "nav_explore")

        label = Label(self, text="This Is The Explore", bg=Constants.main_color, fg="white")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
