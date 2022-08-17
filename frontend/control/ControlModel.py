# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# https://stackoverflow.com/questions/27202990/add-an-image-to-tkinter-entry
# https://www.youtube.com/watch?v=rGOWG7aug58
# https://maxinterview.com/code/tkinter-get-child-in-frame-D13470A155688BB/
# https://github.com/petervalberg/Image_as_button-Tkinter/blob/main/ButtonOverImage.py

import os
import time
import pickle

from playsound import playsound

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


# utility
def update_label_variable(label, new_value):
    label.cget("textvariable").set(new_value)

def get_input_children(input_container):
    for children in input_container.winfo_children():
        # if children is frame -> means is CTkEntry
        if children.winfo_class() == 'Frame':
            return children


def get_assist_size_input_text(entry_width, entry_height, default_font_size):
    # self.entry_radius = 10
    entry_radius = int(entry_width / 25)

    # border_width = 2
    border_width = int(entry_width / 125)
    if border_width < 1:
        border_width = 1

    # entry_vertical_padding = 8
    entry_vertical_padding = int(entry_height / 5.17)

    # entry_horizontal_padding = border_width + 2
    entry_horizontal_padding = border_width * 2

    # entry_font_size = 20
    entry_font_size = int(default_font_size / 1.25)

    return entry_radius, border_width, entry_vertical_padding, entry_horizontal_padding, entry_font_size


# tkinter element
def create_input_text(root, entry_name, entry_width, entry_height,
                      default_font_size,
                      hidden=False):
    entry_radius, border_width, \
    entry_vertical_padding, \
    entry_horizontal_padding, entry_font_size = get_assist_size_input_text(entry_width, entry_height, default_font_size)

    # icon_size = entry_height - 10
    icon_size = entry_height - int(entry_height / 4.3)

    frame = customtkinter.CTkFrame(master=root,
                                   corner_radius=entry_radius,
                                   bg_color=Constants.main_color,
                                   fg_color=Constants.main_color,
                                   border_color=Constants.main_text_color,
                                   border_width=border_width,
                                   relief="solid")
    # for display background of frame when have children inside
    frame.config(bg=Constants.main_color)

    # for storing the icon
    canvas = Canvas(frame, background=Constants.main_color, width=entry_width / 5, height=entry_height)
    canvas.config(highlightthickness=0)
    canvas.pack(side="left", fill="y",
                pady=entry_vertical_padding,
                padx=entry_horizontal_padding)

    # for storing input
    entry = customtkinter.CTkEntry(master=frame,
                                   placeholder_text=entry_name.upper(),
                                   width=entry_width,
                                   height=entry_height,
                                   border_width=0,
                                   fg_color=Constants.main_color,
                                   bg_color=Constants.main_color,
                                   text_color=Constants.main_text_color,
                                   text_font=("Avenir", entry_font_size - 4),
                                   show="*" if hidden else "")
    entry.image = ImageTk.PhotoImage(Image.open(f'{Constants.IMG_CONTAINER_URL + entry_name}-icon.png')
                                     .resize((icon_size, icon_size)))
    canvas.create_image(entry_height / 2,
                        entry_height / 2,
                        image=entry.image)

    entry.pack(side="right", fill="both", expand=True,
               pady=entry_vertical_padding,
               padx=entry_horizontal_padding)
    return frame


def create_label_image(root, image_name, size):
    root.image = image = ImageTk.PhotoImage(Image.open(f'{Constants.IMG_CONTAINER_URL + image_name}.png')
                                            .resize(size))
    return Label(root, bg=Constants.main_color, image=image)


def create_footer(root, default_font_size):
    # footer_font_size = 16
    footer_font_size = int(default_font_size / 1.55)
    footer = customtkinter.CTkLabel(master=root,
                                    text="Produced by Anh Nguyen, Huy Vo, Khanh Tran, Nhung Tran".upper(),
                                    text_color=Constants.footer_text_color,
                                    bg_color=Constants.main_color,
                                    text_font=("Heiti SC", footer_font_size))
    footer.place(relx=1.0, rely=1, anchor=SE)
    return footer

def create_text(root, text,
                font_size,
                text_color=Constants.main_text_color):
    return customtkinter.CTkLabel(master=root,
                                  text_color=text_color,
                                  bg_color=Constants.main_color,
                                  text=text,
                                  text_font=("Avenir", font_size),
                                  wraplength=700)


def create_button(root, btn_name, command, entry_width, entry_height,
                  font_size,
                  fg_color=Constants.button_bck_color,
                  text_color=Constants.button_text_color):
    entry_radius, border_width, \
    entry_vertical_padding, \
    entry_horizontal_padding, \
    font_size = get_assist_size_input_text(entry_width, entry_height, font_size)
    button_width = entry_width + entry_horizontal_padding * 2 + border_width * 2 + entry_width / 5
    button_height = entry_height + entry_vertical_padding * 2 + border_width * 2
    return customtkinter.CTkButton(master=root,
                                   text=btn_name,
                                   fg_color=fg_color,
                                   text_color=text_color,
                                   width=button_width,
                                   height=button_height,
                                   corner_radius=entry_radius,
                                   text_font=("Avenir", font_size),
                                   command=command)


def create_click_text(root, btn_name, command, entry_height,
                      font_size,
                      fg_color=Constants.button_bck_color,
                      text_color=Constants.button_text_color):
    button_height = entry_height
    return customtkinter.CTkButton(master=root,
                                   text=btn_name,
                                   fg_color=fg_color,
                                   text_color=text_color,
                                   height=button_height,
                                   text_font=("Avenir", font_size, "underline"),
                                   command=command)


def create_image(image_url, image_size):
    return ImageTk.PhotoImage(Image.open(image_url).resize((image_size, image_size)))


def create_record_button(root, image_size, record_type="enroll", command=None):
    # initializing the image properties
    if record_type == "enroll" or record_type == "train":
        deny_image = None
    else:
        root.deny_image = deny_image = create_image(f'{Constants.IMG_CONTAINER_URL}login_button_deny.png',
                                                    image_size)

    # create the images
    root.normal_image = playImage = create_image(f'{Constants.IMG_CONTAINER_URL + record_type}_button.png',
                                                 image_size)
    root.activating_image = activating_image = create_image(
        f'{Constants.IMG_CONTAINER_URL + record_type}_button_activating.png',
        image_size)

    # create container
    canvas1 = Canvas(root, width=image_size, height=image_size, bg=Constants.main_color, cursor="hand2")
    canvas1.configure(highlightthickness=0)

    # store image to container
    button = canvas1.create_image(0, 0, anchor=NW, image=playImage)
    # add tag for accessing easier
    canvas1.itemconfig(button, tag="canvas_button")
    # add event for it acting like a real button
    canvas1.tag_bind(button, "<Button-1>",
                     lambda event,
                            activate_img=activating_image,
                            normal_img=playImage,
                            deny_img=deny_image:
                     command(event, activate_img, normal_img, deny_img))

    return canvas1


class ControlModel:

    def __init__(self):
        self.recording = None
        self.recording_train = []
        # define file sample rate
        self.freq = 22050

        self.has_record_enroll = False
        self.current_user = {}

        self.remaining_time_record = 0

        self.current_identify_result = False
        self.current_login_count = 0

        self.read_file()

    # recording
    def record(self, record_type, count_down, canvas=None, activating_image=None, normal_image=None):
        button = canvas.find_withtag("canvas_button")[0]
        # file duration and file name
        if record_type == "enroll":
            duration = Constants.SIGNUP_DURATION
        elif record_type == "train":
            duration = Constants.TRAIN_DURATION
        else:
            duration = Constants.LOGIN_DURATION

        # start recording
        if record_type == "train":
            playsound('../materials/start-record.wav')
            print("Start Recording")
            self.recording_train.append(sd.rec(duration * self.freq, samplerate=self.freq, channels=1))
        else:
            print("Start Recording")
            self.recording = sd.rec(duration * self.freq, samplerate=self.freq, channels=1)
        canvas.itemconfig(button, image=activating_image)

        # count down recording time
        self.remaining_time_record = duration
        while self.remaining_time_record >= 0:
            count_down.configure(text=f'Press and Speak in {str(self.remaining_time_record)} seconds to login')
            canvas.update()
            time.sleep(1)
            self.remaining_time_record -= 1
        sd.wait(duration)

        count_down.configure(text="voice recorded ✓")
        canvas.itemconfig(button, image=normal_image)
        playsound("../materials/end-record.wav")
        # write the recorded audio to file
        print("Done Recording")
        self.has_record_enroll = True

    def write_record(self, username="", record_type="enroll"):
        if record_type == "login":
            # create directory if not exist
            pathlib.Path(f'{Constants.audio_filepath + username}/{username}').mkdir(parents=True, exist_ok=True)
            # write recording file
            write(f'{Constants.audio_filepath + username}/{username}/enroll.wav', self.freq, self.recording)

        # train: write wav file to feat_logbank_nfilt40/train_wav/{username}
        elif record_type == "train":
            try:
                train_wav_dir = Constants.train_wav_filepath + username
                os.makedirs(train_wav_dir, exist_ok=True)
                for i in range(1, 2):
                    write(f'{train_wav_dir}/{username}_train{i}.wav', self.freq, self.recording_train[i - 1])

                train_dir = Constants.train_filepath + username
                os.makedirs(train_dir, exist_ok=True)
                for i in range(1, 2):
                    with open(f'{train_dir}/{username}_train{i}.p', 'wb') as f:
                        pickle.dump(f'{train_wav_dir}/{username}_train{i}.wav', f)
            except OSError as error:
                print("Directory can not be created: ", error)

        else:
            try:
                # write recording file
                write(f'{Constants.audio_filepath + username}/{username}/test.wav', self.freq, self.recording)

                # add for authenticate here
            except:
                # tam thoi
                pathlib.Path(f'{Constants.audio_filepath + username}/{username}').mkdir(parents=True, exist_ok=True)
                write(f'{Constants.audio_filepath + username}/{username}/test.wav', self.freq, self.recording)

    def identify_voice(self,
                       record_type, count_down, event,
                       activating_img, normal_img, deny_img):
        self.current_login_count += 1
        self.record("login", count_down,
                    event.widget,
                    activating_img,
                    normal_img)
        self.write_record(self.current_user.get("username"), record_type)

        # final result
        self.current_identify_result = False

        # display result via changing record button appearance
        if not self.current_identify_result:
            canvas = event.widget
            canvas.itemconfig(canvas.find_withtag("canvas_button")[0], image=deny_img)

    # json file
    def write_file(self, json_dict):
        self.current_user = json_dict
        # Serializing json
        json_object = json.dumps(json_dict, indent=4)

        # create directory if not exist
        pathlib.Path(Constants.json_filepath).mkdir(parents=True, exist_ok=True)

        # Writing to sample.json
        with open(Constants.json_filepath + Constants.json_filename, "w+") as outfile:
            outfile.write(json_object)

    def read_file(self):
        filepath = Constants.json_filepath + Constants.json_filename
        filesize = os.path.getsize(filepath)
        with open(filepath, 'r') as openfile:
            if filesize < 2:
                print("Empty")
                return
            else:
                # Reading from json file
                jsonobj = json.load(openfile)
        self.current_user = jsonobj
