import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import pickle
from datetime import datetime

# ------------------ User Data --------------------
# =================================================

users_file = "data/users.pickle"

def load_users():
    try:
        with open(users_file, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"\n{Fore.RED}Failas nerastas!")
        return []
    except Exception:
        print(f"\n{Fore.RED}Vartotojų sąrašas tuščias")
        return []
    
def save_users(users):
    try:
        with open(users_file, "wb") as file:
            pickle.dump(users, file)
    except Exception as e:
        print(f"\n{Fore.RED}Klaida: {e}")

def get_id():
    id_int = int(datetime.now().timestamp())
    id = str(id_int)[3:]
    return id

# ------------------ Book Data --------------------
# =================================================

books_file = "data/books.pickle"

def load_books():
    try:
        with open(books_file, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"\n{Fore.RED}Failas nerastas!")
        return []
    except Exception:
        print(f"\n{Fore.RED}Knygų sąrašas tuščias")
        return []
    
def save_books(books):
    try:
        with open(books_file, "wb") as file:
            pickle.dump(books, file)
    except Exception as e:
        print(f"\n{Fore.RED}Klaida: {e}")

# ----------------- Basket Data -------------------
# =================================================

baskets_file = "data/baskets.pickle"

def load_baskets():
    try:
        with open(baskets_file, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"\n{Fore.RED}Failas nerastas!")
        return []
    except Exception:
        print(f"\n{Fore.RED}Krepšelių sąrašas tuščias")
        return []
    
def save_baskets(baskets):
    try:
        with open(baskets_file, "wb") as file:
            pickle.dump(baskets, file)
    except Exception as e:
        print(f"\n{Fore.RED}Klaida: {e}")