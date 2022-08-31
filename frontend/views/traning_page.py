from tkinter import *

from playsound import playsound
from frontend.control import ControlModel
from frontend.resources import Constants
from login_page import LoginPage
from subprocess import call
import pickle


class TrainingPage(Frame):

    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model
        self.click = False
        self.count = 0
        self.message = None

        self.build_page()

    def build_page(self):
        # label
        welcome_label = ControlModel.create_label_image(self, "vatosa_enroll_title",
                                                        (self.controller.signup_welcome_label_width,
                                                         self.controller.signup_welcome_label_height))

        count_down = ControlModel.create_text(self, f"Press and Speak in 5 seconds\nRepeat for {Constants.TOTAL_TRAIN_FILE} times", Constants.count_down_size + 1)
        self.message = ControlModel.create_text(self, '', Constants.count_down_size, 'red')

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
        record_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        count_down.place(relx=0.5, rely=0.7, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.82, anchor=CENTER)
        self.message.place(relx=0.5, rely=0.9, anchor=CENTER)

    def click_record_button(self, count_down, event, activating_img, normal_img, deny_img):
        if self.count < Constants.TOTAL_TRAIN_FILE and not self.click:
            self.click = True
            self.model.record("train", count_down,
                              event.widget,
                              activating_img,
                              normal_img)
            self.count += 1
            if self.count < Constants.TOTAL_TRAIN_FILE:
                count_down.configure(text=f"Press and Speak in 5 seconds\nRepeat for {Constants.TOTAL_TRAIN_FILE} times\n{Constants.TOTAL_TRAIN_FILE - self.count} time(s) left")
            else:
                count_down.configure(text=f"{Constants.TOTAL_TRAIN_FILE} records already. Please submit now.")

            self.click = False

    def check_submit(self):
        if self.count != Constants.TOTAL_TRAIN_FILE:
            return False
        return True

    def submit(self):
        try:
            if self.check_submit():
                username = self.model.current_user.get("username")
                self.model.write_record(username, "train")

            # # ignore cuz this is for testing purpose only
            # with open(f'{Constants.test_filepath}/train1.pkl', 'rb') as file:
            #     playsound(pickle.load(file))

                call(["python", Constants.train_py_path])
                print("Train done")
                self.controller.show_frame(LoginPage)


            else:
                self.message.configure(text=f"Please record {Constants.TOTAL_TRAIN_FILE} times to register")
                return

        except:
            print("TRANNING_PAGE.PY : cannot call train.py")
