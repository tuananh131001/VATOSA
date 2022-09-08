# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

from frontend.resources import Constants
from frontend.control import ControlModel
from subprocess import call
# from home_page import HomePage
from tkinter import *
import voice_authentication.enroll
# input username + voice -> store username + voice to json(username, voice file in json + real voice file in 1
# specific path)


class EnrollPage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model
        self.click = False
        self.count_record = 0  # for checking if user has record yet then click submit

        # tkinter element
        self.username_entry = None
        self.password_entry = None
        self.message = None
        self.count_down_label = None

        self.build_page()

    def build_page(self):
        # label
        welcome_label = ControlModel.create_label_image(self, "enroll_title",
                                                        (self.controller.signup_welcome_label_width,
                                                         self.controller.signup_welcome_label_height - 17))
        footer_label = ControlModel.create_footer(self, self.controller.default_font_size)
        count_down = ControlModel.create_text(self, f"Press and Speak in {Constants.SIGNUP_DURATION} seconds to "
                                                    f"enroll your voice", Constants.count_down_size + 2)

        self.message = ControlModel.create_text(self, '', Constants.count_down_size, 'red')
        self.count_down_label = ControlModel.create_text(
            self, f'Press and Speak in {Constants.LOGIN_DURATION} seconds to enroll'.upper(),
            self.controller.default_font_size - 8
        )

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
        submit_btn = ControlModel.create_button(self, "Enroll".upper(),
                                                self.sign_up,
                                                self.controller.entry_width,
                                                self.controller.entry_height,
                                                self.controller.default_font_size)

        # packing
        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.count_down_label.place(relx=0.5, rely=0.68, anchor=CENTER)
        self.message.place(relx=0.5, rely=0.88, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.79, anchor=CENTER)

    def click_record_button(self, count_down, event, activating_img, normal_img, deny_img):
        if not self.click:
            self.message.configure(text="")
            self.click = True
            self.model.record("enroll", count_down,
                              event.widget,
                              activating_img,
                              normal_img)
            self.click = False
            self.count_record += 1

    def sign_up(self):
        if self.count_record != 0:
            self.model.write_record(self.model.current_user.get("username"))
            call(["python", Constants.enroll_py_path])

            print("Sign up done")
            # move to next page
            print(self.model.current_user)
            voice_authentication.enroll.main()
            self.controller.navigate_page("login")
        else:
            self.message.configure(text="Please record before click submit")

