from datetime import datetime

def check_login_user(username, password):
    bibl_login = {
        "admin": "pass",
    }
    return bibl_login.get(username) == password

def create_new_user():
    name_input = input("Įveskite vartotojo vardą: ")
    surname_input = input("Įveskite vartotojo pavardę: ")
    user_id = create_user_id()
    permision = 1
    return name_input, surname_input, user_id, permision

def create_user_id():
    user_id = int(datetime.now().timestamp())
    return user_id


