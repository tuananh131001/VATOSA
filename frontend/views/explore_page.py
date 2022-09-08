from tkinter import *

from frontend.control import ControlModel


class ExplorePage(Frame):
    def __init__(self, parent, root):
        Frame.__init__(self, parent)

        self.controller = root
        self.model = root.model

        # self.app_list = {
        #     "Office": [["word", "word"], ["powerpoint", "pp"], ["excel", "excel"]],
        #     "IDE": [["vs", "vs"]]
        # }
        self.app_list = ["word", "teams", "excel", "zalo"]

        dashboard_y = 0.1
        app_y = dashboard_y + 0.2

        image_size = (self.controller.explore_image_size + 7, self.controller.explore_image_size)

        current_app_idx_x = 0
        current_app_idx_y = 0

        self.list_titles = []
        self.apps = []

        # nav bar
        ControlModel.create_nav(self, self.controller, "nav_explore")

        # explore elements
        title_label = ControlModel.create_text(self, "Dashboard".upper(), self.controller.explore_title_font_size,
                                               'white')

        divider_app_size = self.controller.explore_image_size / 1000
        divider_app_title_size = self.controller.explore_app_font_size / 1000
        divider_app_open_size = self.controller.explore_app_open_font_size / 1000

        # display apps
        width = self.controller.frame_width - self.controller.nav_width
        for app in self.app_list:
            if current_app_idx_x == 2:
                current_app_idx_y = 1
                current_app_idx_x = 0
            # x position of app when place
            x_position = 0.3333 + current_app_idx_x * 0.3333
            y_position = app_y + current_app_idx_y * 0.35

            # create elements
            if app != "zalo":
                app_image = ControlModel.create_label_image(self, f'app_list/{app}.svg', image_size)
            else:
                app_image = ControlModel.create_label_image(self, f'app_list/{app}', image_size)


            app_title = ControlModel.create_text(self, app.capitalize(), self.controller.explore_app_font_size)

            # place elements
            app_image.place(relx=x_position, rely=y_position, anchor=CENTER)
            app_title.place(relx=x_position, rely=y_position + 0.1, anchor=CENTER)

            current_app_idx_x += 1

        # placing
        ControlModel.create_footer(self, self.controller.default_font_size, "header",
                                   self.model.current_user["username"])
        title_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        ControlModel.create_footer(self, self.controller.default_font_size)
