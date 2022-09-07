import os
from tkinter import *

from frontend.resources import Constants
from frontend.control import ControlModel
from voice_controller import prediction
import subprocess
from frontend.resources import Apps


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

        self.count_down = ControlModel.create_text(self,
                                                   f"Press and Speak in {Constants.COMMAND_DURATION} seconds to make command",
                                                   self.controller.default_font_size - 8)
        self.message = ControlModel.create_text(self, '', Constants.count_down_size, 'yellow')
        self.result = ControlModel.create_text(self, '', Constants.count_down_size, 'yellow')

        # footer or header
        ControlModel.create_footer(self, self.controller.default_font_size, "header",
                                   self.model.current_user["username"])
        ControlModel.create_footer(self, self.controller.default_font_size)

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
        self.message.configure(text="")
        self.result.configure(text="")
        self.model.record("command", self.count_down,
                          event.widget,
                          activating_img,
                          normal_img)
        username = self.model.current_user.get("username")
        self.model.write_record(username, "command")
        self.process_command(f"{Constants.command_dir + username}/command.wav")
        self.count_down.configure(text=f"Press and Speak in {Constants.COMMAND_DURATION} seconds to make command")
        self.click = False

    def process_command(self, command_wav_file):
        try:
            command_text = prediction.speech_to_text(command_wav_file)
            if "\\" in command_text:
                command_split_dataset = command_text.split("\\")
            else:
                command_split_dataset = command_text.split('\r')

            command_split = command_split_dataset[-1].split(" ", 1)
        except IndexError:
            command_split = []

        print("command: ", command_text)
        print(command_split)
        # if len(command_split) == 1:
        # command = command_split[0]
        app = command_split[0].lower()

        # if (command != 'open' and command != 'close') or (app not in Constants.apps_dict.keys()):
        #     self.message.configure(text="Unsupported command. Please try again.")
        #     return

        self.message.configure(text=f"RECEIVE COMMAND: {command_split[0].upper()}")
        # if command == 'open':
        path = Apps.app_paths.get(app)
        print(path)
        if path is None:
            self.result.configure(text=f"RESULT: Cannot open. Not found {app.upper()}")
        else:
            if app == "excel":
                os.system('open -a /Applications/Microsoft\ Excel.app')
            elif app == "team":
                os.system('open -a /Applications/Microsoft\ Teams.app')
            elif app == "word":
                os.system('open -a /Applications/Microsoft\ Word.app')
            else:
                os.system(f'open -a {app}')
            subprocess.Popen([path, '-new-tab'])
            self.result.configure(text=f"RESULT: {app.upper()} is opened")

            # elif command == 'close':
            #     if os.system(f"taskkill /f /im {Constants.apps_dict.get(app)}") == 0:
            #         self.result.configure(text=f"RESULT: {app.upper()} is closed")
            #     else:
            #         self.result.configure(text=f"RESULT: Cannot close. {app.upper()} isn't running now")

        # else:
        #     self.message.configure(text="Cannot recognize command. Please try again.")
        #     return
