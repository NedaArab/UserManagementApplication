from DataAccessLayer.user_data_access import UserDataAccess
from common.ResponseModel.response import Response
import hashlib


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

        self.user_list = []

    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return Response(False, "Invalid request", None)

        hash_password = hashlib.md5(password.encode())
        user = self.user_data_access.get_user_with_user_pass(username, hash_password.hexdigest())
        if not user:
            return Response(False, "Invalid username or password", None)
        else:
            if user.is_active:
                return Response(True, None, user)
            else:
                return Response(False, "Your account is deactive", None)

    def register(self, firstname, lastname, username, password):
        if len(firstname) == 0 or len(lastname) == 0 or len(username) == 0 or len(password) == 0:
            return Response(False, "Please complate the items", None)

        elif len(username) < 3 or len(password) < 3:
            return Response(False, "please enter more than 3 characters", None)

        hash_password = hashlib.md5(password.encode())
        self.user_data_access.inser_user(firstname, lastname, username, hash_password.hexdigest())
        return Response(True, "Your registration was successful", None)

    def get_user_list(self, current_user):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access denied", None)

        self.user_list = self.user_data_access.get_user_list(current_user.id)
        return Response(True, None, self.user_list)

    def active_user(self, current_user, active_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access denied", None)

        for user_id in active_list:
            self.user_data_access.update_user(user_id, 1)

    def deactive_user(self, current_user, deactive_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access denied", None)

        for user_id in deactive_list:
            self.user_data_access.update_user(user_id, 0)

    # def search_user(self):
    #     result = filter(lambda user: search_word.upper() in (user.firstname).upper() or search_word.upper() in (
    #         user.lastname).upper(), self.user_list)
