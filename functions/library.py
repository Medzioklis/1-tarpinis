import pickle
import os
from datetime import datetime

from classes.user import User

# users_file_location = "D:/AI studijos/1 tarpinis/data/users.pickle" # namu kompe kelias iki data
users_file_location = "D:/AI studijos/1-tarpinis/data/users.pickle" # darbo kompe kelias iki data

def load_user_data():
    try:
        with open(users_file_location, "rb") as file:
            data = pickle.load(file)
        print("Duomenys nuskaityti")
        return data
    except FileNotFoundError:
        print("Failas nerastas!")
        return []
    except Exception:
        print("Klaida nuskaitant")
        return []
    
def save_user_data(users):
    try:
        with open(users_file_location, "wb") as file:
            pickle.dump(users, file)
            print("Duomenys įrašyti")
    except Exception as e:
        print(f"Klaida: {e}")

users = load_user_data()

def get_user_id():
    user_id = int(datetime.now().timestamp())
    return user_id

def get_role():
    while True:
        role = input("Priskirkite rolę (skaitytojas ar bibliotekininkas): ").lower()
        if role == "skaitytojas" or role == "bibliotekininkas":
            break
        else:
            print(f"Jūs įvedėte klaidingą rolę: {role}. Bandykite pakartoti!")
    return role

def get_name():
    while True:
        name = input("Įveskite vardą ir pavardę: ").strip() # su strip pasalinam tarpus pradzioje ir gale jei netycia jie buvo
        if name != "":
            break
        else:
            print("Prašau suveskite duomenis")
    return name

def get_password():
    while True:
        password = input("Įveskite slaptažodį: ").strip() # su strip pasalinam tarpus pradzioje ir gale jei netycia jie buvo
        if password != "":
            break
        else:
            print("Prašau suveskite duomenis")
    return password

def create_user(name, password, role):
    user_id = get_user_id()
    new_user = User(user_id, name, password, role)
    users.append(new_user)
    save_user_data(users)
    print(f"Vartotojas: {new_user.name} sukurtas. Jo prisijungimo vardas yra: {new_user.user_id}, o slaptazodis yra: {new_user.password}")
    return new_user

def get_user_by_id(user_id):
    for user in users:
        if user.user_id == user_id:
            return user
    return None

def update_user_info(user_id, name=None, password=None, role=None):
    user = get_user_by_id(user_id)
    if user:
        if name:
            user.name = name
        if password:
            user.password = password
        if role == "skaitytojas" or role =="bibliotekininkas":
            user.role = role
        else:
            print("Kadangi neteisingai priskyrėte rolę, suteiksime pagal nutylėjimą skaitytojo rolę")
            user.role = "skaitytojas"
        save_user_data(users)
    print(f"Vartotojas su ID: {user_id} nerastas")
        
def delete_user(user_id):
    global users
    original_len = len(users)
    users = [user for user in users if user.user_id != user_id]
    if len(users) < original_len:
        save_user_data(users)
        print(f"Vartotojas su ID: {user_id} ištrintas.")
    print(f"Vartotojas su ID {user_id} nerastas.")

def list_all_users():
    return users

def authenticate_user(user_id, password):
    user = get_user_by_id(user_id)
    if user and user.password == password:
        return user
    return None