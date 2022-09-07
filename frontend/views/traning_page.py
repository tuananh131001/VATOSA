from tkinter import *

from frontend.control import ControlModel
from frontend.resources import Constants
from enroll_page import EnrollPage
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
        record_btn = ControlModel.create_record_button(self, self.controller.signup_record_button_size,
                                                       "train", lambda event,
                                                       activating_img,
                                                       normal_img,
                                                       deny_img=None:
                                                       self.click_record_button(event,
                                                                                activating_img,
                                                                                normal_img,
                                                                                deny_img))
        submit_btn = ControlModel.create_button(self, "Next".upper(),
                                                self.submit,
                                                self.controller.entry_width,
                                                self.controller.entry_height,
                                                self.controller.default_font_size)

        # packing
        ControlModel.create_footer(self, self.controller.default_font_size, "header",
                                   self.model.current_user["username"])
        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.41, anchor=CENTER)
        self.count_down.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.message.place(relx=0.5, rely=0.93, anchor=CENTER)

        username_box.place(relx=0.5, rely=0.67, anchor=CENTER)
        password_box.place(relx=0.5, rely=0.75, anchor=CENTER)

        submit_btn.place(relx=0.5, rely=0.85, anchor=CENTER)

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
                self.count_down.configure(text=f"{Constants.TOTAL_TRAIN_FILE} records already. Please click next now.")

            self.click = False
        elif self.count == Constants.TOTAL_TRAIN_FILE and not self.click:
            self.message.configure(text=f"Please submit")

    def check_submit(self, username, password):
        allowed = ['!', '@', '#', '$', '%', '^', '&', '*']
        if self.count != Constants.TOTAL_TRAIN_FILE:
            return False
        if username == "" or password == "" or not self.model.has_record_enroll:
            self.message.configure(text="Please record and fill in all the information")
            return False
        elif len(password) < 5:
            self.message.configure(text="Password must have at least 5 characters")
            return False
        elif any((not c.isalnum()) and (c not in allowed) for c in password):
            self.message.configure(text="Password can only include alphanumeric, !, @, #, $, %, ^, &, *")
            return False
        return True

    def submit(self):
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()
            if self.check_submit(username, password):
                # username = self.model.current_user.get("username")
                # add list here

                # Write date to json file
                self.model.current_user = {"username": username, "password": password}
                self.model.write_file(self.model.current_user)
                self.model.write_record(username, "train")

                # call(["python", Constants.train_py_path])

                # call(["python", Constants.enroll_py_path])
                print("Train done")

                # get_apps_exe_path()

                # delete old input
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                print("Sign up done")
                # move to next page
                print(self.model.current_user)

                self.controller.show_frame(EnrollPage)

            else:
                self.message.configure(text=f"Please record {Constants.TOTAL_TRAIN_FILE} times to register")
                return

        except IOError as err:
            print("TRANNING_PAGE.PY : cannot call train.py", err)
