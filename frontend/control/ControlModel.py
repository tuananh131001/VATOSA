# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# https://stackoverflow.com/questions/27202990/add-an-image-to-tkinter-entry
# https://www.youtube.com/watch?v=rGOWG7aug58
# import sys
# sys.path.append('../resources')
# from ..resources import Constants

from frontend.resources import Constants

import json
import sounddevice as sd
# write record file
from scipy.io.wavfile import write
# create directory
import pathlib

from tkinter import *
import customtkinter
from PIL import Image, ImageTk


# tkinter element
def create_input_text(root, entry_name, hidden=False):
    entry_height = 43
    border_width = 2
    entry_vertical_padding = 8
    entry_horizontal_padding = border_width + 2
    entry_radius = 10

    entry_text_color = "white"
    entry_font_size = 20

    frame = customtkinter.CTkFrame(master=root,
                                   corner_radius=entry_radius,
                                   bg_color=Constants.main_color,
                                   fg_color=Constants.main_color,
                                   border_color=entry_text_color,
                                   border_width=border_width,
                                   relief="solid")
    # for display background of frame when have children inside
    frame.config(bg=Constants.main_color)
    # frame.pack(side="bottom")

    # for storing the icon
    canvas = Canvas(frame, background=Constants.main_color, width=50, height=entry_height)
    canvas.config(highlightthickness=0)
    canvas.pack(side="left", fill="y",
                pady=entry_vertical_padding,
                padx=entry_horizontal_padding)

    entry = customtkinter.CTkEntry(master=frame,
                                   placeholder_text=entry_name.upper(),
                                   width=250,
                                   height=entry_height,
                                   border_width=0,
                                   fg_color=Constants.main_color,
                                   bg_color=Constants.main_color,
                                   text_color=entry_text_color,
                                   text_font=("Avenir", entry_font_size),
                                   show="*" if hidden else "")

    # for storing input
    entry.image = ImageTk.PhotoImage(Image.open(f'../resources/assets/{entry_name}-icon.png')
                                     .resize((entry_height - 10, entry_height - 10)))
    canvas.create_image(entry_height / 2,
                        entry_height / 2,
                        image=entry.image)

    entry.pack(side="right", fill="both", expand=True,
               pady=entry_vertical_padding,
               padx=entry_horizontal_padding)
    return frame


def create_button(root, btn_name, command):
    return customtkinter.CTkButton(master=root, text=btn_name,
                                   command=command)


class ControlModel:

    def __init__(self):
        self.recording = None
        # define file sample rate
        self.freq = 22050

        self.has_record_enroll = False

        self.current_user = None

    # recording
    def record(self, record_type):

        # file duration and file name
        if record_type == "enroll":
            duration = Constants.SIGNUP_DURATION
            file_name = "enroll"
        else:
            duration = Constants.LOGIN_DURATION
            file_name = "test"

        # start recording
        print("Start Recording")
        self.recording = sd.rec(duration * self.freq, samplerate=self.freq, channels=1)
        sd.wait()

        # write the recorded audio to file
        print("Done Recording")
        self.has_record_enroll = True

    def write_record(self, username="", type="enroll"):
        if type == "enroll":
            # create directory if not exist
            pathlib.Path(f'{Constants.audio_filepath + username}/{username}').mkdir(parents=True, exist_ok=True)
            # write recording file
            write(f'{Constants.audio_filepath + username}/{username}/enroll.wav', self.freq, self.recording)

            # add to train here
        else:
            try:
                # write recording file
                write(f'{Constants.audio_filepath + username}/{username}/test.wav', self.freq, self.recording)

                # add for authenticate here
            except:
                # tam thoi
                pathlib.Path(f'{Constants.audio_filepath + username}/{username}').mkdir(parents=True, exist_ok=True)
                write(f'{Constants.audio_filepath + username}/{username}/test.wav', self.freq, self.recording)

    # json file
    def write_file(self, json_dict):
        # Serializing json
        json_object = json.dumps(json_dict, indent=4)

        # create directory if not exist
        pathlib.Path(Constants.json_filepath).mkdir(parents=True, exist_ok=True)

        # Writing to sample.json
        with open(Constants.json_filepath + Constants.json_filename, "w+") as outfile:
            outfile.write(json_object)

    def read_file(self):
        with open(Constants.json_filepath + Constants.json_filename, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
