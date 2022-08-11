from tkinter import *
from PIL import ImageTk, Image
import sounddevice
from scipy.io.wavfile import write
import pickle
import os
from playsound import playsound
import train


# second: the time duration is taken to record an audio
# fs:  sampling frequency
second = 6
fs = 22050


def record():
    global count
    count += 1
    print("start")
    playsound('..\\materials\\start-record.wav')
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait(6)
    playsound('..\\materials\\end-record.wav')
    write(f"user_voice_temp\\temp{count}.wav", fs, record_voice)
    print("record finished")


def check_submit():
    if count != 10:
        return False
    return True


def submit():
    if check_submit():
        try:
            new_dir = '..\\..\\feat_logfbank_nfilt40\\train\\new_user'
            os.makedirs(new_dir, exist_ok=True)
            for i in range(1, 11):
                if os.path.exists(f"user_voice_temp\\temp{i}.wav"):
                    with open(os.path.join(new_dir, f"temp{i}.p"), 'wb') as f:
                        pickle.dump(f"user_voice_temp\\temp{i}.wav", f)
            train.main()
        except OSError as error:
            print("Directory ", new_dir, " can not be created: ", error)
    else:
        playsound('..\\materials\\message.wav')
        return


count = 0
root = Tk()
root.title("Register voice")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# set screensize as fullscreen and not resizable
root.geometry("%dx%d" % (width / 1.2, height))
root.resizable(True, True)

# put image in a label and place label as background
bgTemp = Image.open("background.png")
bg2 = bgTemp.resize((width, height))
bg = ImageTk.PhotoImage(bg2)

label = Label(root, image=bg)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

frame = Frame(root, bg='#2B2C33', width=500, height=300)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add buttons
record_btn = Button(frame, text="Press to record voice", command=record)
record_btn.pack(anchor=CENTER)

submit_btn = Button(frame, text="Register now", command=submit)
submit_btn.pack(anchor=CENTER)

root.mainloop()
