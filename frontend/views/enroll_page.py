# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

from frontend.resources import Constants
from frontend.control import ControlModel
from frontend.views.traning_page import TrainingPage

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
        self.click = False

        # tkinter element
        self.username_entry = None
        self.password_entry = None

        self.build_page()

    def build_page(self):
        # label
        label_width = 570
        label_height = 105
        welcome_label = ControlModel.create_label_image(self, "vatosa_enroll_title",
                                                        (label_width, label_height))
        footer_label = ControlModel.create_footer(self)

        # Entry Input
        username_box = ControlModel.create_input_text(self, "Username")
        password_box = ControlModel.create_input_text(self, "Password", True)

        self.username_entry = ControlModel.get_input_children(username_box)
        self.password_entry = ControlModel.get_input_children(password_box)

        # Button
        # record
        record_btn = ControlModel.create_record_button(self, "enroll", lambda event,
                                                                       activating_img,
                                                                       normal_img,
                                                                       deny_img=None:
                                                                       self.click_record_button(event,
                                                                                                activating_img,
                                                                                                normal_img,
                                                                                                deny_img))
        submit_btn = ControlModel.create_button(self, "Submit", self.sign_up)

        # packing
        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.42, anchor=CENTER)
        username_box.place(relx=0.5, rely=0.6, anchor=CENTER)
        password_box.place(relx=0.5, rely=0.7, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.8, anchor=CENTER)
        footer_label.place(relx=0.68, rely=0.97, anchor=CENTER)

    def click_record_button(self, event, activating_img, normal_img, deny_img):
        if not self.click:
            self.click = True
            self.model.record("enroll",
                              event.widget,
                              activating_img,
                              normal_img)
            self.click = False

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        allowed = ['!', '@', '#', '$', '%', '^', '&', '*']
        # special_characters = "!@#$%^&*()-+?_=,.<>/"
        if username == "" or password == "" or not self.model.has_record_enroll:
            print("Please fill in all the information")
            return
        elif len(password) < 5 or any((not c.isalnum()) and (c not in allowed) for c in password):
            print("Password must have more than 5 characters. "
                  "Valid values for passwords include alphanumeric, !, @, #, $, %, ^, &, or *. "
                  "No other special characters are allowed.")
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
        self.controller.show_frame(TrainingPage(username))
