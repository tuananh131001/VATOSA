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
            "Office": ["word, powerpoint, excel"],
            "IDE": ["vs"]
        }

        dashboard_x = 0.13
        dashboard_y = 0.1

        list_x = dashboard_x + 0.02
        list_y = dashboard_y + 0.05

        app_x = list_x + 0.1

        current_list_idx = 0

        self.list_titles = []
        self.apps = []

        # nav bar
        ControlModel.create_nav(self, self.controller, "nav_explore")

        title_label = ControlModel.create_text(self, "Dashboard".upper(), self.controller.explore_title_font_size,
                                               'white', "nav_explore")

        for list_name in self.app_list:
            list_title = ControlModel.create_text(self, f'{list_name} Apps', self.controller.explore_list_font_size,
                                                  'white', "nav_explore")
            list_title.place(relx=list_x, rely=0.2 + 0.1 * current_list_idx, anchor=W)

            # make sure create multiple elements inside for loop
            self.list_titles.append(list_title)

            current_list_idx += 1
                # for app in self.app_list[list_name]:
                #


        title_label.place(relx=dashboard_x, rely=0.1, anchor=W)
