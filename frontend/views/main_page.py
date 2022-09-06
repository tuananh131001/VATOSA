# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
from tkinter import *
import customtkinter
from PIL import ImageTk, Image

from frontend.resources import Constants
from frontend.control import ControlModel
from enroll_page import EnrollPage
from traning_page import TrainingPage
from home_page import HomePage
from explore_page import ExplorePage
from login_page import LoginPage



class VatosaApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        height = self.winfo_screenheight()
        width = self.winfo_screenwidth()

        if width <= 700:
            # init window size
            width = int(self.winfo_screenwidth() / 1.02)
            self.frame_width = int(width / 1.05)
            self.frame_height = int(height / 1.1)

            # init record button size
            self.login_record_button_size = int(self.frame_width / 5.2)
            self.signup_record_button_size = int(self.frame_width / 7.8)
        else:
            # init window size
            width = int(self.winfo_screenwidth() / 1.1)
            self.frame_width = int(width / 1.3)
            self.frame_height = int(height / 1.3)

            # init record button size
            self.login_record_button_size = int(self.frame_width / 3.4)
            self.signup_record_button_size = int(self.frame_width / 5.8)

        # entry size
        self.entry_height = int(self.frame_height / 17.5)
        self.entry_width = int(self.frame_width / 4.22)

        # label size
        # sign up
        self.signup_welcome_label_width = int(self.frame_width / 1.85)
        self.signup_welcome_label_height = int(self.frame_height / 7.15)
        # loginR
        self.login_welcome_label_width = int(self.frame_width / 2.27)
        self.login_welcome_label_height = int(self.frame_height / 9.28)
        # font size
        self.default_font_size = int(self.frame_width / 42.1)

        # explore
        self.explore_title_font_size = int(self.frame_width / 33)  # 32
        self.explore_list_font_size = int(self.frame_width / 40)  # 26
        self.explore_image_size = int(self.frame_width / 17)  # 75
        self.explore_app_font_size = int(self.frame_width / 57)  # 19
        self.explore_app_open_font_size = int(self.frame_width / 62)  # 17

        # nav bar
        self.nav_width = int(self.frame_width / 10.5)  # 100
        self.nav_height = self.frame_height
        self.nav_button_size = int(self.nav_width * 70 / 100)  # 70

        self.title("Vatosa")
        self.geometry(f'{width}x{height}')
        self.resizable(True, True)

        # model
        self.model = ControlModel.ControlModel()

        # create container for background and window inside
        canvas = Canvas(self, width=width, height=height)
        canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

        bg = Image.open(Constants.IMG_CONTAINER_URL + "background.png").resize((width, height))
        background_image = ImageTk.PhotoImage(bg)
        # labelabell = Label(canvas, image=background_image)
        # label.place(relx=0.5, rely=0.5, anchor=CENTER)
        canvas.create_image(0, 0, anchor=NW, image=background_image)
        canvas.background_image = background_image
        # canvas.create_image(0, 0, anchor=NW, image=background_image)

        container = Frame(self, bg="")
        canvas.create_window(width / 2, height / 2, width=self.frame_width, height=self.frame_height, window=container)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # init frames empty array
        self.frames = {}

        # iterating through page layouts
        for Page in (EnrollPage, TrainingPage, LoginPage, HomePage, ExplorePage):
            # for Page in (HomePage, ExplorePage):
            frame = Page(container, self)

            # init frame and store to array
            self.frames[Page] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            # frame.configure(width=300, height=300)
            frame.configure(bg=Constants.main_color)

        # check if open sign up page first or login page first
        if self.model.current_user != {"username": "", "password": ""}:
            self.show_frame(HomePage)
            # self.show_frame(LoginPage)
        else:
            self.show_frame(EnrollPage)

    def show_frame(self, current_frame):
        frame = self.frames[current_frame]
        frame.tkraise()

    def navigate_page(self, button_type):
        if button_type == "nav_home":
            self.show_frame(HomePage)
        elif button_type == "nav_explore":
            self.show_frame(ExplorePage)
        elif button_type == "login" or button_type == "nav_logout":
            self.show_frame(LoginPage)


app = VatosaApp()
app.mainloop()
