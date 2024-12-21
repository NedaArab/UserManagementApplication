class User:
    def __init__(self, id, firstname, lastname, username, password, role_id, is_active):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.role_id = role_id
        self.is_active = bool(is_active)

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def show_role_title(self):
        match self.role_id:
            case 1:
                return "Admin"
            case 2:
                return "Defult user"
            case _:
                raise ValueError("Invalid value for role id.")
