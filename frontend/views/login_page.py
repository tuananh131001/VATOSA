from frontend.resources import Constants
from frontend.control import ControlModel


from tkinter import *
import customtkinter

model = ControlModel.ControlModel()
current_user = model.read_file()
current_login_count = 0
voice_match = False
login_state = False


def check_voice_login(username_json):
    model.write_record(username_json, "login")
    if voice_match:
        login_state = True
        return login_state
    else:
        print("Invalid Voice")
        return False


def login():
    global current_login_count, login_state

    current_login_count += 1
    print(current_login_count)

    if current_login_count <= 3:
        if check_voice_login(current_user.get("username")):
            return True
        elif current_login_count == 3:
            # hide voice login button, display login with alternative method
            record_btn.destroy()
            # pack
            username_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
            password_entry.place(relx=0.5, rely=0.6, anchor=CENTER)
        return False
    else:
        username_input = username_entry.get()
        password_input = password_entry.get()

        # invalid
        if username_input != current_user.get("username") or password_input != current_user.get("password"):
            print("Invalid login")
            return False

        # delete old input
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        print("Login Successfully")
        return True


# create window
root = customtkinter.CTk()
root.title("Vatosa".upper())

# entry
username_entry = customtkinter.CTkEntry(master=root,
                                        placeholder_text="Username".upper(),
                                        width=120,
                                        height=25,
                                        border_width=2,
                                        corner_radius=10)
password_entry = customtkinter.CTkEntry(master=root,
                                        placeholder_text="Password".upper(),
                                        width=120,
                                        height=25,
                                        border_width=2,
                                        corner_radius=10,
                                        show="*")

# buttons
record_btn = customtkinter.CTkButton(master=root, text="Record",
                                     command=lambda: model.record(Constants.SIGNUP_DURATION))
login_btn = customtkinter.CTkButton(master=root,
                                    text="Login",
                                    command=login)


# packing
record_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
login_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
