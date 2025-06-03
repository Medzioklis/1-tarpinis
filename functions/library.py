import pickle
import os
from datetime import datetime

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

def get_id():
    id_int = int(datetime.now().timestamp())
    id = str(id_int)[3:]
    return id

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
    user_id = get_id()
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

def get_book_by_id(book_id):
    for book in books:
        if book.book_id == book_id:
            return book
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

def create_book(book_title, book_author, book_genre, book_release):
    book_id = get_id()
    new_book = Book(book_id, book_title, book_author, book_genre, book_release)
    books.append(new_book)
    save_books_data(books)
    print(f"Knygos ID: {new_book.book_id}, pavadinimas: {new_book.book_title}, autorius: {new_book.book_author}, žanras: {new_book.book_genre}, leidinio metai: {new_book.book_release}")
    return new_book

def list_all_books():
    return books

def update_book_info(book_id, book_title=None, book_author=None, book_genre=None, book_release=None):
    book = get_book_by_id(book_id)
    if book:
        if book_title:
            book.book_title = book_title
        if book_author:
            book.book_author = book_author
        if book_genre:
            book.book_genre = book_genre
        if book_release:
            book.book_release = book_release
        save_books_data(books)
    else:
        print(f"Knyga su ID: {book_id} nerasta")

def delete_book(book_id):
    books = load_books_data()
    original_len = len(books)                                   # nustatom saraso iteraciju skaiciu (ilgi)
    books = [book for book in books if book.book_id != book_id] # sukuria naują sąrašą books, į kurį įtraukiamos tos knygos, kurių book_id nesutampa su tuo kuri norime ištrinti
    if len(books) < original_len:                               # tikrinam ar saraso ilgis sumazejo, jei sumazejo reiskia kad knyga istrinta ir galima is naujo isaugoti sarasa
        save_books_data(books)
        print(f"Knyga su ID: {book_id} ištrinta")
    else:
        print(f"Knyga su ID: {book_id} nerasta")