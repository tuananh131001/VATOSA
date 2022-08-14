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
        self.click = False

        # tkinter elements
        self.username_box = None
        self.password_box = None
        self.username_entry = None
        self.password_entry = None
        self.normal_login_label = None
        self.change_alternative_label = None
        self.record_btn = None
        self.login_btn = None

        # create and place tkinter elements
        self.build_page()

    def build_page(self):

        # label
        welcome_label = ControlModel.create_label_image(self, "vatosa_login_title",
                                                        (self.controller.login_welcome_label_width,
                                                         self.controller.login_welcome_label_height))
        footer_label = ControlModel.create_footer(self, self.controller.default_font_size)
        self.normal_login_label = ControlModel.create_text(
            self, f'Press and Speak in {Constants.LOGIN_DURATION} seconds to login'.upper(),
            self.controller.default_font_size)

        # Entry Input
        self.username_box = ControlModel.create_input_text(self, "Username", self.controller.entry_width,
                                                           self.controller.entry_height,
                                                           self.controller.default_font_size)
        self.password_box = ControlModel.create_input_text(self, "Password", self.controller.entry_width,
                                                           self.controller.entry_height,
                                                           self.controller.default_font_size,
                                                           True)

        self.username_entry = ControlModel.get_input_children(self.username_box)
        self.password_entry = ControlModel.get_input_children(self.password_box)

        # Button
        self.change_alternative_label = ControlModel.create_click_text(self, "Alternative Login Here".upper(),
                                                                       self.change_to_alternative,
                                                                       self.controller.entry_height,
                                                                       self.controller.default_font_size,
                                                                       Constants.main_color,
                                                                       Constants.alternative_text_color)
        # record
        self.record_btn = ControlModel.create_record_button(self, self.controller.login_record_button_size,
                                                            "login",
                                                            lambda event,
                                                                   activating_img,
                                                                   normal_img,
                                                                   deny_img:
                                                            self.click_record_button(event,
                                                                                     activating_img,
                                                                                     normal_img,
                                                                                     deny_img))
        self.login_btn = ControlModel.create_button(self, "Login", self.login,
                                                    self.controller.entry_width,
                                                    self.controller.entry_height,
                                                    self.controller.default_font_size)

        # packing
        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.record_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.normal_login_label.place(relx=0.5, rely=0.78, anchor=CENTER)
        self.change_alternative_label.place(relx=0.5, rely=0.85, anchor=CENTER)
        # self.change_alternative_label.bind('<Button-1>', lambda event: print("clcik"))

    def click_record_button(self, event, activating_img, normal_img, deny_img):

        if not self.click:
            self.click = True
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

            self.click = False

    def change_to_alternative(self):
        # hide voice login button, display login with alternative method
        self.record_btn.destroy()
        self.change_alternative_label.destroy()
        # pack
        self.normal_login_label.config(text="voice control and authentication to open software applications".upper())
        self.username_box.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.password_box.place(relx=0.5, rely=0.53, anchor=CENTER)
        self.login_btn.place(relx=0.5, rely=0.63, anchor=CENTER)

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
