from ttkbootstrap import Frame, Label, Button, Entry
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic


class LoginFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)
        self.main_view = main_view

        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)

        self.login_forme_label = Label(self, text="Login Form")
        self.login_forme_label.grid(row=0, column=1, padx=5, pady=(10, 5))

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, padx=(5, 2.5), pady=2.5, sticky="e")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, padx=5, pady=2.5, sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, padx=(5, 2.5), pady=2.5, sticky="e")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=(5, 0), pady=2.5, sticky="ew")

        self.show_button = Button(self, width=4, text="@@", command=self.show_password)
        self.show_button.grid(row=2, column=1, padx=(0, 5), pady=2.5, sticky="e")

        self.login_button = Button(self, text="Login", command=self.login, bootstyle="primary")
        self.login_button.grid(row=3, column=1, padx=5, pady=2.5, sticky="w")

        self.register_button = Button(self, text="Register", command=self.register, bootstyle="success")
        self.register_button.grid(row=4, column=1, padx=5, pady=2.5, sticky="w")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business_logic.login(username, password)
        if result.success:

            home_frame = self.main_view.switch_frame("home")
            home_frame.set_current_user(result.data)

            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
        else:
            Messagebox.show_info( result.message,"Erorr")

    def register(self):
        self.main_view.switch_frame("register")

    def show_password(self):
        if self.password_entry["show"] == "*":
            self.password_entry.config(show="")
            self.show_button.config(text="--")

        else:
            self.password_entry.config(show="*")
            self.show_button.config(text="@@")
