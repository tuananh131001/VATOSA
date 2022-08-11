from frontend.resources import Constants
from frontend.control import ControlModel

from tkinter import *
import customtkinter


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.model = controller.model
        self.model.read_file()
        self.current_user = self.model.current_user

        self.current_login_count = 0
        self.voice_match = False

        # tkinter elements
        self.username_box = None
        self.password_box = None
        self.username_entry = None
        self.password_entry = None
        self.record_btn = None

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
        self.record_btn = customtkinter.CTkButton(master=self, text="Record",
                                                  command=lambda: self.model.record(Constants.SIGNUP_DURATION))
        login_btn = ControlModel.create_button(self, "Login", self.login)

        # packing
        self.record_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
        login_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    def check_voice_login(self):
        self.model.write_record(self.current_user.get("username"), "login")
        if self.voice_match:
            login_state = True
            return login_state
        else:
            print("Invalid Voice")
            return False

    def login(self):
        self.current_login_count += 1

        if self.current_login_count <= 3:
            if self.check_voice_login():
                return True
            if self.current_login_count == 3:
                # hide voice login button, display login with alternative method
                self.record_btn.destroy()
                # pack
                self.username_box.place(relx=0.5, rely=0.5, anchor=CENTER)
                self.password_box.place(relx=0.5, rely=0.6, anchor=CENTER)
            return False
        else:
            username_input = self.username_entry.get()
            password_input = self.password_entry.get()

            # invalid
            if username_input != self.model.current_user.get("username") \
                    or password_input != self.model.current_user.get("password"):
                print("Invalid login")
                return False

            # delete old input
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            print("Login Successfully")
            return True
