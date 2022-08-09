# https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

from frontend.resources import Constants
from frontend.control import ControlModel

from tkinter import *
import customtkinter

# input username + voice -> store username + voice to json(username, voice file in json + real voice file in 1
# specific path)
model = ControlModel.ControlModel()


def signUp():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "" or not model.has_record_enroll:
        return

    # Write date to json file
    user_info_dict = {"username": username, "password": password}
    model.writeFile(user_info_dict)

    if username != "":
        model.write_record(username)

    # delete old input
    username_input.set("")
    password_input.set("")
    print("Sign up done")


# create window
root = customtkinter.CTk()
root.title("Vatosa".upper())

# Assign passing variables
username_input = StringVar()
password_input = StringVar()

# Entry Input
username_entry = customtkinter.CTkEntry(master=root, textvariable=username_input,
                                        placeholder_text="Username".upper(),
                                        width=120,
                                        height=25,
                                        border_width=2,
                                        corner_radius=10)
password_entry = customtkinter.CTkEntry(master=root, textvariable=password_input,
                                        placeholder_text="Password".upper(),
                                        width=120,
                                        height=25,
                                        border_width=2,
                                        corner_radius=10,
                                        show="*")

# Button
# record
record_btn = customtkinter.CTkButton(master=root, text="Record",
                                     command=lambda: model.record(Constants.SIGNUP_DURATION))
submit_btn = customtkinter.CTkButton(master=root, text="Submit", command=signUp)

# packing
username_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
password_entry.place(relx=0.5, rely=0.6, anchor=CENTER)
record_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
submit_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
signUp()
