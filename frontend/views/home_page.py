from tkinter import *
from PIL import Image, ImageTk
import customtkinter

from frontend.resources import Constants
from frontend.control import ControlModel


class HomePage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model


        ControlModel.create_nav(self, self.controller, "nav_home")

        # nav.place(relx=0.5, rely=0.2, anchor=CENTER)
        # .place(relx=0.5, rely=0.2, anchor=CENTER)


