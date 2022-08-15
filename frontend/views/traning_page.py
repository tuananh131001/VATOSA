from tkinter import *

import customtkinter
from PIL import ImageTk, Image
import pickle
import os
from playsound import playsound
import train
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

        self.build_page()

    def build_page(self):
        # label
        welcome_label = ControlModel.create_label_image(self, "vatosa_enroll_title",
                                                        (self.controller.signup_welcome_label_width,
                                                         self.controller.signup_welcome_label_height))

        footer_label = ControlModel.create_footer(self, self.controller.default_font_size)

        count_down = ControlModel.create_text(self, f"Press and Speak in 5 seconds\nRepeat for 10 times\n{10 - self.count} time(s) left", Constants.count_down_size)

        # Button
        # record
        record_btn = ControlModel.create_record_button(self, self.controller.signup_record_button_size,
                                                       "train", lambda event,
                                                       activating_img,
                                                       normal_img,
                                                       deny_img=None:
                                                       self.click_record_button(count_down, event,
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
        record_btn.place(relx=0.5, rely=0.52, anchor=CENTER)
        count_down.place(relx=0.5, rely=0.7, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    def click_record_button(self, count_down, event, activating_img, normal_img, deny_img):
        if self.count < 10 and not self.click:
            self.click = True
            self.model.record("train", count_down,
                              event.widget,
                              activating_img,
                              normal_img)
            self.count += 1
            if self.count < 10:
                count_down.configure(text=f"Press and Speak in 5 seconds\nRepeat for 10 times\n{10 - self.count} time(s) left")
            else:
                count_down.configure(text=f"10 records already. Please submit now.")

            self.click = False

    def check_submit(self):
        if self.count != 1:
            return False
        return True

    def submit(self):
        if self.check_submit():
            username = self.model.current_user.get("username")
            self.model.write_record(username, "train")

            # # test file
            # with open(f'../../feat_logfbank_nfilt40/train/{username}/{username}_train1.p', 'rb') as file:
            #     playsound(pickle.load(file))

            # Popen('python train.py')
            # train.py
            # call(["python", "../../train.py"])
            print("Train done")
            self.controller.show_frame(LoginPage)
        else:
            playsound('../materials/message.wav')
            return
