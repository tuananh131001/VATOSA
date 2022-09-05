import os
from tkinter import *

from frontend.control import ControlModel
from frontend.resources import Constants
from login_page import LoginPage
from subprocess import call


class TrainingPage(Frame):

    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model
        self.click = False
        self.count = 0
        self.message = None
        self.count_down = None

        self.build_page()

    def build_page(self):
        # label
        welcome_label = ControlModel.create_label_image(self, "vatosa_enroll_title",
                                                        (self.controller.signup_welcome_label_width,
                                                         self.controller.signup_welcome_label_height))

        self.count_down = ControlModel.create_text(self, f"Press and Speak in {Constants.TRAIN_DURATION} seconds\nRepeat for {Constants.TOTAL_TRAIN_FILE} times", Constants.count_down_size + 1)
        self.message = ControlModel.create_text(self, '', Constants.count_down_size, 'red')

        # Button
        # record
        record_btn = ControlModel.create_record_button(self, self.controller.signup_record_button_size,
                                                       "train", lambda event,
                                                       activating_img,
                                                       normal_img,
                                                       deny_img=None:
                                                       self.click_record_button(event,
                                                                                activating_img,
                                                                                normal_img,
                                                                                deny_img))
        submit_btn = ControlModel.create_button(self, "Register".upper(),
                                                self.submit,
                                                self.controller.entry_width,
                                                self.controller.entry_height,
                                                self.controller.default_font_size)

        # packing
        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.count_down.place(relx=0.5, rely=0.7, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.82, anchor=CENTER)
        self.message.place(relx=0.5, rely=0.9, anchor=CENTER)

    def click_record_button(self, event, activating_img, normal_img, deny_img):
        if self.count < Constants.TOTAL_TRAIN_FILE and not self.click:
            self.message.configure(text='')
            self.click = True
            self.model.record("train", self.count_down,
                              event.widget,
                              activating_img,
                              normal_img)
            self.count += 1
            if self.count < Constants.TOTAL_TRAIN_FILE:
                self.count_down.configure(text=f"Press and Speak in 5 seconds\nRepeat for {Constants.TOTAL_TRAIN_FILE} times\n{Constants.TOTAL_TRAIN_FILE - self.count} times left")
            else:
                self.count_down.configure(text=f"{Constants.TOTAL_TRAIN_FILE} records already. Please submit now.")

            self.click = False
        elif self.count == Constants.TOTAL_TRAIN_FILE and not self.click:
            self.message.configure(text=f"Please submit")

    def check_submit(self):
        if self.count != Constants.TOTAL_TRAIN_FILE:
            return False
        return True

    def submit(self):
        try:
            if self.check_submit():
                # self.message.configure(text="")
                # self.count_down.configure(text=f"Training phase is on process. Please wait.")
                username = self.model.current_user.get("username")
                self.model.write_record(username, "train")

                call(["python", Constants.train_py_path])
                print("Train done")
                self.controller.show_frame(LoginPage)

            else:
                self.message.configure(text=f"Please record {Constants.TOTAL_TRAIN_FILE} times to register")
                return

        except IOError as err:
            print("TRANNING_PAGE.PY : cannot call train.py", err)






