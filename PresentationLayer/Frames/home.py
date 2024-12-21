from ttkbootstrap import Frame, Label, Entry, Button


class HomeFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.current_user = None
        self.main_view = main_view
        self.grid_columnconfigure(0, weight=1)

        self.welcom_label = Label(self)
        self.welcom_label.grid(row=0, column=0, padx=10, pady=(10, 5))

        self.log_out_button = Button(self, text="Log out", command=self.log_out_button)
        self.log_out_button.grid(row=1, column=0, padx=10, pady=2.5, sticky="ew")

        self.user_management_button = None

    def set_current_user(self, current_user):
        self.current_user = current_user
        self.welcom_label.config(text=f"welcome {current_user.get_fullname()}")
        self.user_management_button = Button(self, text="User Management", command=self.user_management)

        if current_user.show_role_title() == "Admin":
            self.user_management_button.grid(row=2, column=0, padx=10, pady=2.5, sticky="ew")

        else:
            if self.user_management_button:
                self.user_management_button.destroy()

    def log_out_button(self):
        login_frame = self.main_view.switch_frame("login")

    def user_management(self):
        user_management_frame = self.main_view.switch_frame("user_management")
        user_management_frame.set_current_user(self.current_user)
