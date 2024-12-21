from re import search
from tkinter import Frame, Label, Button, messagebox, Entry
from tkinter.ttk import Treeview

from pyexpat.errors import messages

from BusinessLogicLayer.user_business_logic import UserBusinessLogic


class UserManagementFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view
        self.user_business_logic = UserBusinessLogic()

        self.user_list = []
        self.row_list = []
        self.current_user = None
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.user_information_label = Label(self)
        self.user_information_label.grid(row=0, column=0, padx=10, pady=5)

        self.active_button = Button(self, text="Active", command=self.active)
        self.active_button.grid(row=2, column=0, padx=5, pady=2.5, sticky="w")

        self.deactive_button = Button(self, text="Deactive", command=self.deactive)
        self.deactive_button.grid(row=2, column=0, padx=5, pady=2.5, sticky="e")

        self.user_treeview = Treeview(self, columns=("firstname", "lastname", "username", "role", "statuse"))
        self.user_treeview.grid(row=3, column=0, sticky="nsew")

        self.user_treeview.heading("#0", text="NO")
        self.user_treeview.heading("#1", text="Firstname")
        self.user_treeview.heading("#2", text="Lastname")
        self.user_treeview.heading("#3", text="Username")
        self.user_treeview.heading("#4", text="Role")
        self.user_treeview.heading("#5", text="Statuse")

        self.back_button = Button(self, text="Back",command=self.back_button_go_home)
        self.back_button.grid(row=4, column=0,padx=5, pady=2.5,sticky="e")

    def set_current_user(self, current_user):
        self.current_user = current_user
        self.user_information_label.config(text=self.current_user.get_fullname())
        self.get_user_list()

    def load_data(self, user_list):
        for row in self.row_list:
            self.user_treeview.delete(row)

        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_treeview.insert("", "end", iid=str(user.id), text=str(row_number), values=(
                user.firstname, user.lastname, user.username, user.show_role_title(),
                "Active" if user.is_active == 1 else "Deactive"))

            self.row_list.append(row)
            row_number += 1

    def active(self):
        active_list = self.user_treeview.selection()
        result = self.user_business_logic.active_user(self.current_user, active_list)

        self.get_user_list()

    def deactive(self):
        deactive_list = self.user_treeview.selection()
        result = self.user_business_logic.deactive_user(self.current_user, deactive_list)

        self.get_user_list()

    def get_user_list(self):
        result = self.user_business_logic.get_user_list(self.current_user)

        if result.success:
            self.load_data(result.data)

        else:
            messagebox.showinfo("Erorr", result.message)

    def back_button_go_home(self):
        self.main_view.switch_frame("home")

