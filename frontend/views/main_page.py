# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
from tkinter import *
import customtkinter
from PIL import ImageTk, Image

from frontend.resources import Constants
from frontend.control import ControlModel
from enroll_page import EnrollPage
from frontend.views.traning_page import TrainingPage
from result_page import ResultPage
from login_page import LoginPage



class VatosaApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # height = self.winfo_screenheight()
        width=491
        height = 241

        if width <= 700:
            width = int(self.winfo_screenwidth() / 1.02)
            width = 491
            self.frame_width = int(width / 1.05)
            self.frame_height = int(height / 1.1)

            # self.login_record_button_size = 310
            self.login_record_button_size = int(self.frame_width / 5.2)
            # self.signup_record_button_size = 180
            self.signup_record_button_size = int(self.frame_width / 7.8)
        else:
            width = int(self.winfo_screenwidth() / 1.1)
            self.frame_width = int(width / 1.3)
            self.frame_height = int(height / 1.3)

            # self.login_record_button_size = 310
            self.login_record_button_size = int(self.frame_width / 3.4)
            # self.signup_record_button_size = 180
            self.signup_record_button_size = int(self.frame_width / 5.8)

        # self.entry_height = 43
        self.entry_height = int(self.frame_height / 17.5)
        # self.entry_width = 250
        self.entry_width = int(self.frame_width / 4.22)

        # self.signup_label_width = 570
        self.signup_welcome_label_width = int(self.frame_width / 1.85)
        # self.signup_label_height = 105
        self.signup_welcome_label_height = int(self.frame_height / 7.15)
        # self.login_label_width = 465
        self.login_welcome_label_width = int(self.frame_width / 2.27)
        # self.login_label_height = 81
        self.login_welcome_label_height = int(self.frame_height / 9.28)
        # self.default_font = 25
        self.default_font_size = int(self.frame_width / 42.1)


        self.title("Vatosa")
        self.geometry(f'{width}x{height}')
        # self.resizable(True, True)
        # Window only
        # self.wm_attributes('-transparentcolor', '#ab23ff')

        self.model = ControlModel.ControlModel()

        # create container for background and window inside
        canvas = Canvas(self, width=width, height=height)
        canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

        bg = Image.open(Constants.IMG_CONTAINER_URL + "background.png").resize((width, height))
        background_image = ImageTk.PhotoImage(bg)
        canvas.background_image = background_image
        canvas.create_image(0, 0, anchor=NW, image=background_image)

        container = Frame(self, bg="")
        canvas.create_window(width / 2, height / 2, width=self.frame_width, height=self.frame_height, window=container)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # init frames empty array
        self.frames = {}

        # iterating through page layouts
        for Page in (EnrollPage, TrainingPage, LoginPage, ResultPage):
            frame = Page(container, self)

            # init frame and store to array
            self.frames[Page] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            # frame.configure(width=300, height=300)
            frame.configure(bg=Constants.main_color)

        # check if open sign up page first or login page first
        if self.model.current_user:
            self.show_frame(LoginPage)
        else:
            self.show_frame(EnrollPage)

    def show_frame(self, current_frame):
        frame = self.frames[current_frame]
        frame.tkraise()


app = VatosaApp()
app.mainloop()
