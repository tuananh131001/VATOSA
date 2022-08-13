from tkinter import *
from PIL import ImageTk, Image
import pickle
import os
from playsound import playsound
import train
from frontend.control import ControlModel
from frontend.resources import Constants
from frontend.views.login_page import LoginPage


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
        label_width = 570
        label_height = 105
        welcome_label = ControlModel.create_label_image(self, "vatosa_enroll_title",
                                                        (label_width, label_height))
        footer_label = ControlModel.create_footer(self)

        # Button
        # record
        record_btn = ControlModel.create_record_button(self, "train", lambda event,
                                                                              activating_img,
                                                                              normal_img,
                                                                              deny_img=None:
        self.click_record_button(event,
                                 activating_img,
                                 normal_img,
                                 deny_img))
        submit_btn = ControlModel.create_button(self, "Submit", self.submit)

        # packing
        record_btn.place(relx=0.5, rely=0.42, anchor=CENTER)
        submit_btn.place(relx=0.5, rely=0.8, anchor=CENTER)
        footer_label.place(relx=0.68, rely=0.97, anchor=CENTER)

    def click_record_button(self, event, activating_img, normal_img, deny_img):
        if self.count < 10 and not self.click:
            self.click = True
            self.model.record("train",
                              event.widget,
                              activating_img,
                              normal_img)
            self.count += 1
            self.click = False
        elif self.count >= 10:
            print("You have finished recording 10 records already. Please submit now.")

    # def record(self):
    #     self.count += 1
    #     print("start")
    #     playsound('..\\materials\\start-record.wav')
    #     record_voice = sounddevice.rec(int((Constants.TRAIN_DURATION + 1) * Constants.SAMPLE_RATE),
    #                                    samplerate=Constants.SAMPLE_RATE, channels=2)
    #     sounddevice.wait(Constants.TRAIN_DURATION + 1)
    #     playsound('..\\materials\\end-record.wav')
    #     write(f"user_voice_temp\\temp{self.count}.wav", Constants.SAMPLE_RATE, record_voice)
    #     print("record finished")

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

            train.main()
            print("Train done")

            # self.controller.show_frame(LoginPage)
        else:
            playsound('../materials/message.wav')
            return

# root = Tk()
# root.title("Register voice")
#
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
#
# # set screensize as fullscreen and not resizable
# root.geometry("%dx%d" % (width / 1.2, height))
# root.resizable(True, True)
#
# # put image in a label and place label as background
# bgTemp = Image.open("../resources/assets/background.png")
# bg2 = bgTemp.resize((width, height))
# bg = ImageTk.PhotoImage(bg2)
#
# label = Label(root, image=bg)
# label.place(relx=0.5, rely=0.5, anchor=CENTER)
#
# frame = Frame(root, bg='#2B2C33', width=500, height=300)
# frame.place(relx=0.5, rely=0.5, anchor=CENTER)
#
# # Add buttons
# record_btn = Button(frame, text="Press to record voice", command=record)
# record_btn.pack(anchor=CENTER)
#
# submit_btn = Button(frame, text="Register now", command=submit)
# submit_btn.pack(anchor=CENTER)
#
# root.mainloop()
