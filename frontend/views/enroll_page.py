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
    def __init__(self, parent, controller):
        # self.root = root
        Frame.__init__(self, parent)
        self.controller = controller
        self.model = controller.model

        self.build_page()

    def build_page(self):
        # Entry Input
        username_entry = ControlModel.create_input_text(self, "Username")
        password_entry = ControlModel.create_input_text(self, "Password", True)

        # Button
        # record
        record_btn = customtkinter.CTkButton(master=self, text="Record",
                                             command=lambda: self.model.record(Constants.SIGNUP_DURATION))
        submit_btn = ControlModel.create_button(self, "Submit", lambda: self.sign_up(username_entry, password_entry))

        # packing
        username_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        password_entry.place(relx=0.5, rely=0.6, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    def sign_up(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()

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
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        print("Sign up done")
        self.controller.show_frame(LoginPage)
