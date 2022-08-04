from tkinter import *
from PIL import ImageTk, Image
# from frontend.customtkinter import CTkButton
import sounddevice
from scipy.io.wavfile import write

# from frontend.gradient_background import apply_background
from frontend.training_page.button1 import Button1


# second: the time duration is taken to record an audio
# fs:  sampling frequency
def record(second, fs):
    global count
    count += 1
    print("start")
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
    sounddevice.wait(6)
    print("record finished")
    write(f"temp{count}.wav", fs, record_voice)


def submit():
    if count != 10:
        return
    

count = 0
root = Tk()
root.title("Register voice")
# apply_background(root)

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
record_btn = Button(frame, text="Press to record voice", command=record(second=5, fs=22050, filename="temp2"))
record_btn.pack(anchor=CENTER)

submit_btn = Button(frame, text="Register now", command=record(second=5, fs=22050, filename="temp2"))
root.mainloop()
