from PresentationLayer.Frames.user_management import UserManagementFrame
from PresentationLayer.window import MainWindow
from PresentationLayer.Frames.login import LoginFrame
from PresentationLayer.Frames.home import HomeFrame
from PresentationLayer.Frames.register import RegisterFrame


class MainView:
    def __init__(self):
        self.window = MainWindow()
        self.frames = {}

        self.add_frames("user_management", UserManagementFrame(self.window, self))
        self.add_frames("register", RegisterFrame(self.window))
        self.add_frames("home", HomeFrame(self.window, self))
        self.add_frames("login", LoginFrame(self.window, self))

        self.window.show()

    def add_frames(self, name, frame):
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def switch_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        return frame
