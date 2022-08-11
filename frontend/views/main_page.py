# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
from tkinter import *
from tkinter import font
import customtkinter

from frontend.control import ControlModel
from enroll_page import EnrollPage
from login_page import LoginPage


class VatosaApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Vatosa")
        self.geometry("500x500")
        # Window only
        # self.wm_attributes('-transparentcolor', '#ab23ff')

        self.model = ControlModel.ControlModel()

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # init frames empty array
        self.frames = {}

        # iterating through page layouts
        for Page in (EnrollPage, LoginPage):
            frame = Page(container, self)

            # init frame and store to array
            self.frames[Page] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(EnrollPage)

    def show_frame(self, current_frame):
        frame = self.frames[current_frame]
        frame.tkraise()


app = VatosaApp()
# app = customtkinter.CTk()


app.mainloop()