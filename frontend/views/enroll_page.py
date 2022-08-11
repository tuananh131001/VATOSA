# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

from frontend.resources import Constants
from frontend.control import ControlModel

from login_page import LoginPage
# from page1 import Page1

from tkinter import *
import customtkinter


# input username + voice -> store username + voice to json(username, voice file in json + real voice file in 1
# specific path)


class EnrollPage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model

        # tkinter element
        self.username_entry = None
        self.password_entry = None

        self.build_page()

    def build_page(self):
        # Entry Input
        username_box = ControlModel.create_input_text(self, "Username")
        password_box = ControlModel.create_input_text(self, "Password", True)

        self.username_entry = ControlModel.get_input_children(username_box)
        self.password_entry = ControlModel.get_input_children(password_box)

        # Button
        # record
        record_btn = customtkinter.CTkButton(master=self, text="Record",
                                             command=lambda: self.model.record(Constants.SIGNUP_DURATION))
        submit_btn = ControlModel.create_button(self, "Submit", self.sign_up)

        # packing
        username_box.place(relx=0.5, rely=0.5, anchor=CENTER)
        password_box.place(relx=0.5, rely=0.6, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "" or not self.model.has_record_enroll:
            # add validate username here
            # add validate password here
            return

        # Write date to json file
        user_info_dict = {"username": username, "password": password}
        self.model.write_file(user_info_dict)

        if username != "":
            self.model.write_record(username)

        # delete old input
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        print("Sign up done")
        # move to next page
        print(self.model.current_user)
        self.controller.show_frame(LoginPage)
