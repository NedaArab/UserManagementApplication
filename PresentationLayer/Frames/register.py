from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic


class RegisterFrame(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)

        self.register_frame_label = Label(self, text="Register Frame")
        self.register_frame_label.grid(row=0, column=1, padx=10, pady=5)

        self.firstname_label = Label(self, text="Firstname")
        self.firstname_label.grid(row=1, column=0, padx=(10, 2.5), pady=2.5)

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1, column=1, padx=(2.5, 10), pady=2.5, sticky="ew")

        self.lastname_label = Label(self, text="Lastname")
        self.lastname_label.grid(row=2, column=0, padx=(10, 2.5), pady=2.5)

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2, column=1, padx=(2.5, 10), pady=2.5, sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, padx=(10, 2.5), pady=2.5)

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, padx=(2.5, 10), pady=2.5, sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=4, column=0, padx=(10, 2.5), pady=2.5)

        self.password_entry = Entry(self)
        self.password_entry.grid(row=4, column=1, padx=(2.5, 10), pady=2.5, sticky="ew")

        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=5, column=1, padx=(2.5, 10), pady=2.5, sticky="w")

    def submit(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business_logic.register(firstname, lastname, username, password)
        if not result.success:
            messagebox.showinfo("Erorr", result.message)

        else:
            messagebox.showinfo("Info", result.message)
            self.firstname_entry.delete(0, "end")
            self.lastname_entry.delete(0, "end")
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")
