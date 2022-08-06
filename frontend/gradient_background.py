from tkinter import *
from PIL import ImageTk, Image


def apply_background(screen):
    # get width & height of screen
    width = screen.winfo_screenwidth()
    height = screen.winfo_screenheight()

    # set screensize as fullscreen and not resizable
    screen.geometry("%dx%d" % (width, height))
    screen.resizable(True, True)

    # put image in a label and place label as background
    imgTemp = Image.open("../materials/background.png")
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(screen, image=img)
    label.pack(side='top', fill=Y, expand=True)

    # screen.mainloop()
