import ttkbootstrap

from ttkbootstrap import Window


class MainWindow(Window):
    def __init__(self):
        super().__init__(themename="darkly", iconphoto="Images/user_manage_profile.png")
        self.title("User Management Application")
        self.geometry("500x300")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show(self):
        self.mainloop()
