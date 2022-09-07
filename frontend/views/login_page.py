import os

import customtkinter

from frontend.resources import Constants
from frontend.control import ControlModel
from home_page import HomePage
from tkinter import *
from traning_page import TrainingPage


class LoginPage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model
        self.click = False
        self.login_name = None
        self.login_name_entry = None

        # tkinter elements
        self.username_box = None
        self.password_box = None
        self.username_entry = None
        self.password_entry = None
        self.normal_login_label = None
        self.change_alternative_label = None
        self.record_btn = None
        self.login_btn = None
        self.login_message = None
        self.back_btn = None
        self.training_btn = None
        # self.register_btn = None

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
            self.controller.default_font_size - 8)
        self.login_message = ControlModel.create_text(self, '', Constants.count_down_size, 'red')

        # Entry Input
        self.login_name = ControlModel.create_input_text(self, "Username", self.controller.entry_width,
                                                         self.controller.entry_height,
                                                         self.controller.default_font_size)
        self.username_box = ControlModel.create_input_text(self, "Username", self.controller.entry_width,
                                                           self.controller.entry_height,
                                                           self.controller.default_font_size)
        self.password_box = ControlModel.create_input_text(self, "Password", self.controller.entry_width,
                                                           self.controller.entry_height,
                                                           self.controller.default_font_size,
                                                           True)
        self.login_name_entry = ControlModel.get_input_children(self.login_name)
        self.username_entry = ControlModel.get_input_children(self.username_box)
        self.password_entry = ControlModel.get_input_children(self.password_box)

        # Button
        count_down = ControlModel.create_text(self, "", 12)
        self.training_btn = customtkinter.CTkButton(master=self, text="Don't have an account? Register here!", command=self.go_training, fg_color="#2B2C33", text_color="yellow", hover= False)
        self.change_alternative_label = ControlModel.create_click_text(self, "Alternative Login Here".upper(),
                                                                       self.change_to_alternative,
                                                                       self.controller.entry_height,
                                                                       self.controller.default_font_size - 10,
                                                                       Constants.main_color,
                                                                       Constants.alternative_text_color)

        self.back_btn = ControlModel.create_click_text(self, "Back",
                                                       self.go_back,
                                                       self.controller.entry_height,
                                                       self.controller.default_font_size - 8,
                                                       Constants.main_color,
                                                       Constants.main_text_color)

        # record
        self.record_btn = ControlModel.create_record_button(self, self.controller.login_record_button_size - 50,
                                                            "login",
                                                            lambda event,
                                                                   activating_img,
                                                                   normal_img,
                                                                   deny_img:
                                                            self.click_record_button(self.normal_login_label, event,
                                                                                     activating_img,
                                                                                     normal_img,
                                                                                     deny_img))

        self.login_btn = ControlModel.create_button(self, "Login", self.login,
                                                    self.controller.entry_width,
                                                    self.controller.entry_height,
                                                    self.controller.default_font_size)

        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.record_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.normal_login_label.place(relx=0.5, rely=0.76, anchor=CENTER)
        self.change_alternative_label.place(relx=0.5, rely=0.83, anchor=CENTER)
        self.login_name.place(relx=0.5, rely=0.72, anchor=CENTER)
        self.login_message.place(relx=0.5, rely=0.71, anchor=CENTER)
        self.training_btn.place(relx=0.5, rely=0.90, anchor=CENTER)

    def click_record_button(self, count_down, event, activating_img, normal_img, deny_img):
        folder = os.path.dirname(os.path.dirname(os.getcwd())) + '/voice_authentication' + '/feat_logfbank_nfilt40/test'
        print(folder)
        sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
        print(sub_folders)
        print(self.login_name_entry.get())
        if not self.click:
            # if self.login_name_entry.get() not in sub_folders:

            self.model.current_user = {"username": self.login_name_entry.get(), "password": "12345"}
            self.click = True
            # validate voice
            self.model.current_identify_result = self.model.identify_voice("login", count_down, event, activating_img, normal_img, deny_img)

            # display actions based on the identify result
            if self.model.current_identify_result:
                print("Valid Voice", self.model.current_login_count)

                self.model.current_user = {"username": self.login_name_entry.get(), "password": "12345"}
                self.model.write_file(self.model.current_user)
                ControlModel.create_footer(self, self.controller.default_font_size, "header",
                                           self.model.current_user["username"])
                self.navigate_next_page()
            elif not self.model.current_identify_result \
                    and self.model.current_login_count == 3:
                self.change_to_alternative()
                print("Invalid voice", self.model.current_login_count)
            else:
                print("Invalid voice", self.model.current_login_count)
                self.normal_login_label.configure(text="Invalid voice. Please try again")
            # else:
            #     self.normal_login_label.configure(text="Invalid name. Please try again")
            self.click = False

    def change_to_alternative(self):
        # hide voice login button, display login with alternative method
        self.record_btn.destroy()
        self.change_alternative_label.destroy()

        # pack
        self.normal_login_label.configure(text="voice control and authentication to open software applications".upper())
        self.username_box.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.password_box.place(relx=0.5, rely=0.53, anchor=CENTER)
        self.login_btn.place(relx=0.5, rely=0.63, anchor=CENTER)
        self.back_btn.place(relx=0, rely=0.04, anchor=NW)

    def login(self):
        username_input = self.username_entry.get()
        password_input = self.password_entry.get()

        # invalid
        if username_input != self.model.current_user.get("username") \
                or password_input != self.model.current_user.get("password"):
            print("Invalid login")
            self.login_message.config(text="Invalid login credentials. Please try again")
            return

        self.login_message.config(text="Login successfully. Please wait.")

        # # get apps exe paths
        # get_apps_exe_path()

        # delete old input
        self.login_message.config(text="")
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.model.current_identify_result = True
        self.navigate_next_page()

    def navigate_next_page(self):
        self.controller.show_frame(HomePage)

    def go_back(self):
        self.record_btn.destroy()
        self.change_alternative_label.destroy()
        self.username_box.destroy()
        self.password_box.destroy()
        self.login_btn.destroy()
        self.login_message.destroy()
        self.normal_login_label.destroy()
        self.back_btn.destroy()
        self.build_page()

    def go_enroll(self):
        self.controller.show_frame(EnrollPage)

    def go_training(self):
        self.controller.show_frame(TrainingPage)


def get_apps_exe_path():
    app_paths = {}
    paths = []
    for k, v in Constants.apps_dict.items():
        # try path in dir C:
        path = find_file(v, "C:")

        # if cannot find any path then find in dir D:
        if path is None:
            path = find_file(v, "D:\\")

        # if still cannot find in dir D: then print message
        if path is None:
            print("cannot find path for ", v)

        paths.append(path)
        app_paths[f'{k}'] = path

    with open(Constants.APPS_PY, 'w') as f:
        f.write(f"app_paths = {{\n")
        f.write(f"\"excel\" : \"{paths[0]}\",\n")
        f.write(f"\"word\" :  \"{paths[1]}\",\n")
        f.write(f"\"pp\" :  \"{paths[2]}\",\n")
        f.write(f"\"teams\" :  \"{paths[3]}\",\n")
        f.write(f"\"chrome\" :  \"{paths[4]}\",\n")
        f.write(f"\"zalo\" :  \"{paths[5]}\"\n")
        f.write(f"}}")


# ref: https://www.tutorialspoint.com/file-searching-using-python
def find_file(filename, search_path):
    """
    Function to find the first matched file, then returns the path to that file
    If no matched file is found, returns None
    """
    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        files_temp = list(map(str.lower, files))
        if filename.lower() in files_temp:
            result = os.path.join(root, filename)
            result = result.replace("\\", "\\\\")
            return result
