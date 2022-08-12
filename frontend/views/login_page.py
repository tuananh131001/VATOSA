from frontend.resources import Constants
from frontend.control import ControlModel

from result_page import ResultPage

from tkinter import *
import customtkinter
from PIL import ImageTk, Image


class LoginPage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model

        # tkinter elements
        self.username_box = None
        self.password_box = None
        self.username_entry = None
        self.password_entry = None
        self.record_btn = None
        self.login_btn = None

        # create and place tkinter elements
        self.build_page()

    def build_page(self):
        # Entry Input
        self.username_box = ControlModel.create_input_text(self, "Username")
        self.password_box = ControlModel.create_input_text(self, "Password", True)

        self.username_entry = ControlModel.get_input_children(self.username_box)
        self.password_entry = ControlModel.get_input_children(self.password_box)

        # Button
        # record
        self.record_btn = ControlModel.create_record_button(self, "login",
                                                            lambda event,
                                                            activating_img,
                                                            normal_img,
                                                            deny_img:
                                                            self.click_record_button(event,
                                                                                     activating_img,
                                                                                     normal_img,
                                                                                     deny_img))
        self.login_btn = ControlModel.create_button(self, "Login", self.login)

        # packing
        # login_btn.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.record_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    def click_record_button(self, event, activating_img, normal_img, deny_img):
        # validate voice
        self.model.identify_voice("login", event, activating_img, normal_img, deny_img)

        # display actions based on the identify result
        if self.model.current_identify_result:
            print("Valid Voice", self.model.current_login_count)
            self.navigate_next_page()
        elif not self.model.current_identify_result \
                and self.model.current_login_count == 3:
            self.change_to_alternative()
            print("Invalid voice", self.model.current_login_count)
        else:
            print("Invalid voice", self.model.current_login_count)

    def change_to_alternative(self):
        # hide voice login button, display login with alternative method
        self.record_btn.destroy()
        # pack
        self.username_box.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.password_box.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.login_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    def login(self):
        username_input = self.username_entry.get()
        password_input = self.password_entry.get()

        # invalid
        if username_input != self.model.current_user.get("username") \
                or password_input != self.model.current_user.get("password"):
            print("Invalid login")
            return

        # delete old input
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.model.current_identify_result = True
        self.navigate_next_page()
        print("Login Successfully")

    def navigate_next_page(self):
        self.controller.show_frame(ResultPage)
