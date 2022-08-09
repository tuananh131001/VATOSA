# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
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


class ControlModel:

    def __init__(self):
        self.recording = None
        # define file sample rate
        self.freq = 22050

        self.has_record_enroll = False


        self.current_user = None

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
