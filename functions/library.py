import pickle
import os
from datetime import datetime
import uuid

from classes.user import User
from classes.book import Book

# users_file_location = "D:/AI studijos/1 tarpinis/data/users.pickle" # namu kompe kelias iki data
# books_file_location = "D:/AI studijos/1 tarpinis/data/books.pickle" # namu kompe kelias iki data
users_file_location = "D:/AI studijos/1-tarpinis/data/users.pickle" # darbo kompe kelias iki data
books_file_location = "D:/AI studijos/1-tarpinis/data/books.pickle" # darbo kompe kelias iki data

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
        print("Klaida nuskaitant arba nėra duomenų")
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
    user_id_int = int(datetime.now().timestamp())
    user_id = str(user_id_int)
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

def update_user_info(user_id, name=None, password=None):
    user = get_user_by_id(user_id)
    if user:
        if name:
            user.name = name
        if password:
            user.password = password
        save_user_data(users)
    else:
        print(f"Vartotojas su ID: {user_id} nerastas")
        
def delete_user(user_id):
    global users
    original_len = len(users)                                   # nustatom saraso vartotoju skaiciu (ilgi)
    users = [user for user in users if user.user_id != user_id] # sukuria naują sąrašą users, į kurį įtraukiami tie vartotojai, kurių user_id nesutampasu tuo kurį norime ištrinti
    if len(users) < original_len:                               # tikrinam ar saraso ilgis sumazejo, jei sumazejo reiskia kad vartotojas istrintas ir galima is naujo isaugoti sarasa
        save_user_data(users)
        print(f"Vartotojas su ID: {user_id} ištrintas.")
    else:
        print(f"Vartotojas su ID {user_id} nerastas.")

def list_all_users():
    return users

def authenticate_user(user_id, password):
    user = get_user_by_id(user_id)
    if user and user.password == password:
        return user
    return None

# --------------------------------------------------------------
# ---------------- Knygos funkcijos ----------------------------
# --------------------------------------------------------------

def load_books_data():
    try:
        with open(books_file_location, "rb") as file:
            data = pickle.load(file)
        print("Duomenys nuskaityti")
        return data
    except FileNotFoundError:
        print("Failas nerastas!")
        return []
    except Exception:
        print("Klaida nuskaitant arba nėra duomenų")
        return []
    
def save_books_data(books):
    try:
        with open(books_file_location, "wb") as file:
            pickle.dump(books, file)
            print("Duomenys įrašyti")
    except Exception as e:
        print(f"Klaida: {e}")

books = load_books_data()

def get_book_id():
    book_id = str(uuid.uuid4())
    return book_id

def create_book(book_title, book_author, book_genre, book_release):
    book_id = get_book_id()
    new_book = Book(book_id, book_title, book_author, book_genre, book_release)
    books.append(new_book)
    save_user_data(books)
    print(f"Knygos ID: {new_book.book_id}, pavadinimas: {new_book.book_title}, autorius: {new_book.book_author}, žanras: {new_book.book_genre}, leidinio metai: {new_book.book_release}")
    return new_book

def list_all_books():
    return books