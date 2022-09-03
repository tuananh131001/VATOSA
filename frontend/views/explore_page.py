from tkinter import *
from PIL import Image, ImageTk

from frontend.resources import Constants
from frontend.control import ControlModel


class ExplorePage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model

        self.app_list = {
            "Office": ["word", "powerpoint", "excel"],
            "IDE": ["vs"]
        }

        dashboard_x = 0.13
        dashboard_y = 0.1

        list_x = dashboard_x + 0.02
        list_y = dashboard_y + 0.1

        image_size = (self.controller.explore_image_size + 7, self.controller.explore_image_size)

        current_list_idx = 0
        current_app_idx = 0

        self.list_titles = []
        self.apps = []

        # nav bar
        ControlModel.create_nav(self, self.controller, "nav_explore")

        title_label = ControlModel.create_text(self, "Dashboard".upper(), self.controller.explore_title_font_size,
                                               'white', "nav_explore")
        divider_app_size = self.controller.explore_image_size / 1000
        divider_app_title_size = self.controller.explore_app_font_size / 1000
        for list_name in self.app_list.keys():
            list_y = list_y + (divider_app_size + divider_app_title_size + 0.2) * current_list_idx
            list_title = ControlModel.create_text(self, f'{list_name} Apps', self.controller.explore_list_font_size,
                                                  'white', "nav_explore")
            list_title.place(relx=list_x, rely=list_y, anchor=W)

            # make sure create multiple elements inside for loop
            self.list_titles.append(list_title)
            app_x = list_x + 0.1
            app_y = list_y + 0.1

            for app in self.app_list.get(list_name):
                x_position = app_x + current_app_idx * (divider_app_title_size + 0.2)

                if list_name == "IDE":
                    text = "Visual Studio"
                else:
                    text = f'Microsoft {app.capitalize()}'

                app_image = ControlModel.create_label_image(self, f'app_list/{app}.svg', image_size)
                app_title = ControlModel.create_text(self, text, self.controller.explore_app_font_size)

                app_image.place(relx=x_position, rely=app_y, anchor=CENTER)
                app_title.place(relx=x_position, rely=app_y + (divider_app_size + 0.02), anchor=CENTER)

                current_app_idx += 1

            current_app_idx = 0
            current_list_idx += 1

        title_label.place(relx=dashboard_x, rely=0.1, anchor=W)
