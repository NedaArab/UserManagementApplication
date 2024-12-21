import sqlite3
from DataAccessLayer import database_name
from common.Entity.user import User


class UserDataAccess:
    def get_user_with_user_pass(self, username, password):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   firstname,
                   lastname,
                   username,
                   password,
                   role_id,
                   is_active
            FROM   User
            WHERE  username=?
            AND    password=?
            """, (username, password))
            data = cursor.fetchone()
            if data:
                user = User(*data)
                user.password = None
                return user

    def inser_user(self, firstname, lastname, username, password):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO User (
                     firstname,
                     lastname,
                     username,
                     password
                 )
            VALUES (
                     ?,
                     ?,
                     ?,
                     ?
                 );

            """, (firstname, lastname, username, password))
            connection.commit()

    def get_user_list(self, user_id):
        user_list = []
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT 
                   id,
                   firstname,
                   lastname,
                   username,
                   password,
                   role_id,
                   is_active
            FROM   User
            WHERE  id !={user_id}


            """)
            data = cursor.fetchall()

            for item in data:
                user = User(*item)
                user.password = None
                user_list.append(user)

        return user_list

    def update_user(self, user_id, new_value):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            UPDATE User
            SET    is_active = ?
            WHERE id = ?
               
            """, (new_value, user_id))
            connection.commit()
