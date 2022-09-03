import os
from tkinter import *

from frontend.resources import Constants
from frontend.control import ControlModel
from voice_controller import prediction
import subprocess
from frontend.resources import Apps

apps = ["vs", "excel", "word", "powerpoint"]

open_dict = {
    "vs": Apps.VSCODE,
    "excel": Apps.EXCEL,
    "word": Apps.WORD,
    "powerpoint": Apps.POWERPOINT
}

close_dict = {
    "vs": "Code.exe",
    "excel": "EXCEL.EXE",
    "word": "WINWORD.EXE",
    "powerpoint": "POWERPNT.EXE"
}


class HomePage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model
        self.click = False
        self.message = None
        self.result = None
        self.count_down = None
        self.proc = None

        ControlModel.create_nav(self, self.controller, "nav_home")

        self.build_page()

    def build_page(self):
        welcome_label = ControlModel.create_label_image(self, "vatosa_login_title",
                                                        (self.controller.login_welcome_label_width,
                                                         self.controller.login_welcome_label_height))

        self.count_down = ControlModel.create_text(self, "Press and Speak in 5 seconds to make command",
                                                   Constants.count_down_size + 1)
        self.message = ControlModel.create_text(self, '', Constants.count_down_size, 'yellow')
        self.result = ControlModel.create_text(self, '', Constants.count_down_size, 'yellow')

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

        # packing
        welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        record_btn.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.count_down.place(relx=0.5, rely=0.73, anchor=CENTER)
        self.message.place(relx=0.5, rely=0.84, anchor=CENTER)
        self.result.place(relx=0.5, rely=0.9, anchor=CENTER)

    def click_record_button(self, event, activating_img, normal_img, deny_img):
        self.click = True
        self.model.record("command", self.count_down,
                          event.widget,
                          activating_img,
                          normal_img)
        username = self.model.current_user.get("username")
        self.model.write_record(username, "command")
        self.process_command(f"{Constants.command_dir + username}/command.wav")
        self.count_down.configure(text=f"Press and Speak in 5 seconds to make command")
        self.click = False

    def process_command(self, command_wav_file):
        self.message.configure(text="")
        self.result.configure(text="")
        try:
            command_text = prediction.speech_to_text(command_wav_file)
            command_split = command_text.split(" ", 1)
        except IndexError:
            command_split = []

        print("command: ", command_text)
        if len(command_split) == 2:
            command = command_split[0]
            app = command_split[1].lower()

            if (command != 'open' and command != 'close') or (app not in apps):
                self.message.configure(text="Unsupported command. Please try again.")
                return

            self.message.configure(text=f"COMMAND: {command_text.upper()}")
            if command == 'open':
                path = open_dict.get(app)
                if path is None:
                    self.result.configure(text=f"RESULT: Cannot open. Not found {app.upper()}")
                else:
                    subprocess.Popen([path, '-new-tab'])
                    self.result.configure(text=f"RESULT: {app.upper()} is opened")

            elif command == 'close':
                if os.system(f"taskkill /f /im {close_dict.get(app)}") == 0:
                    self.message.configure(text=f"RESULT: {app.upper()} is closed")
                else:
                    self.result.configure(text=f"RESULT: Cannot close. {app.upper()} isn't running now")

        else:
            self.message.configure(text="Cannot recognize command. Please try again.")
            return

