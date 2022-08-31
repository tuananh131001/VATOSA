# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

from frontend.resources import Constants
from frontend.control import ControlModel
from traning_page import TrainingPage

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
        self.enroll_message = None
        self.count_down_label = None

        self.build_page()

    def build_page(self):
        # label
        welcome_label = ControlModel.create_label_image(self, "vatosa_enroll_title",
                                                        (self.controller.signup_welcome_label_width,
                                                         self.controller.signup_welcome_label_height))
        footer_label = ControlModel.create_footer(self, self.controller.default_font_size)
        count_down = ControlModel.create_text(self, f"Press and Speak in {Constants.SIGNUP_DURATION} seconds to "
                                                    f"enroll your voice", Constants.count_down_size)
        self.enroll_message = ControlModel.create_text(self, '', 10)
        self.count_down_label = ControlModel.create_text(
            self, f'Press and Speak in {Constants.LOGIN_DURATION} seconds to login'.upper(),
            self.controller.default_font_size - 10
        )
        # Entry Input
        username_box = ControlModel.create_input_text(self, "Username", self.controller.entry_width,
                                                      self.controller.entry_height,
                                                      self.controller.default_font_size)
        password_box = ControlModel.create_input_text(self, "Password", self.controller.entry_width,
                                                      self.controller.entry_height,
                                                      self.controller.default_font_size,
                                                      True)

        self.username_entry = ControlModel.get_input_children(username_box)
        self.password_entry = ControlModel.get_input_children(password_box)

        # Button
        # record
        record_btn = ControlModel.create_record_button(self, self.controller.signup_record_button_size - 10,
                                                       "enroll", lambda event,
                                                       activating_img,
                                                       normal_img,
                                                       deny_img=None:
                                                       self.click_record_button(self.count_down_label, event,
                                                                                activating_img,
                                                                                normal_img,
                                                                                deny_img))
        submit_btn = ControlModel.create_button(self, "Next".upper(),
                                                self.sign_up,
                                                self.controller.entry_width,
                                                self.controller.entry_height,
                                                self.controller.default_font_size)

        # packing
        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.count_down_label.place(relx=0.5, rely=0.6, anchor=CENTER)
        username_box.place(relx=0.5, rely=0.67, anchor=CENTER)
        password_box.place(relx=0.5, rely=0.75, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.85, anchor=CENTER)
        self.enroll_message.place(relx=0.5, rely=0.92, anchor=CENTER)

    def click_record_button(self, count_down, event, activating_img, normal_img, deny_img):
        if not self.click:
            self.click = True
            self.model.record("enroll", count_down,
                              event.widget,
                              activating_img,
                              normal_img)
            self.click = False

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        allowed = ['!', '@', '#', '$', '%', '^', '&', '*']
        if username == "" or password == "" or not self.model.has_record_enroll:
            self.enroll_message.configure(text="Please fill in all the information")
            return
        elif len(password) < 5:
            self.enroll_message.configure(text="Password must have at least 5 characters")
            return
        elif any((not c.isalnum()) and (c not in allowed) for c in password):
            self.enroll_message.configure(text="Password can only include alphanumeric, !, @, #, $, %, ^, &, *")
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
        self.controller.show_frame(TrainingPage)
