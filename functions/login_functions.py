from classes.user import User
from . import data_functions

def login(username, password):
    users = data_functions.load_users()
    for user in users:
        if user.user_name == username and user.user_password == password:
            return user
    return None

def create_initial_fakeadmin():
    users = data_functions.load_users()
    if not users:
        admin = User(user_id=1, user_name="admin", user_password="admin", user_role="bibliotekininkas")
        data_functions.save_users([admin])
        print("Programos startui sukurtas fake admin vartotojas")