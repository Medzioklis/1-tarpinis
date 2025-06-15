import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from classes.user import User
from . import data_functions as df

user_file = "data/users.pickle"

def create_user():
    users = df.load_users()
    user_id = df.get_id()
    user_name = input("\nĮveskite vartotojo vardą ir pavardę: ")
    user_password = input("\nĮveskite slaptažodį: ")
    while True:
        user_role = input("\nĮveskite rolę (skaitytojas ar bibliotekininkas): ").lower()
        if user_role == "skaitytojas" or user_role == "bibliotekininkas":
            break
        else:
            print(f"\n{Fore.RED}Neteisingai įvedėte rolę {user_role}. Bandykite dar kartą")
    user = User(user_id, user_name, user_password, user_role)
    users.append(user)
    df.save_users(users)
    print(f"{Fore.BLUE}-" * 100)
    print(f"{Fore.GREEN}Vartotojas: {user.user_name} sukurtas. Jo kortelės numeris yra: {user.user_id}, o slaptazodis yra: {user.user_password}")

def delete_user():
    users = df.load_users()
    original_len = len(users)
    user_id = input("\nĮveskite vartotojo kortelės numerį, kurį norite ištrinti: ")
    users = [user for user in users if user.user_id != user_id]
    if len(users) < original_len:                        # tikrinam ar saraso ilgis sumazejo, jei sumazejo reiskia kad vartotojas istrintas ir galima is naujo isaugoti sarasa
        df.save_users(users)
        print(f"\n{Fore.GREEN}Vartotojas su ID: {user_id} ištrintas.")
    else:
        print(f"\n{Fore.RED}Vartotojas su ID {user_id} nerastas.")

def update_user():
    users = df.load_users()
    try:
        user_id = input("\nĮveskite vartotojo ID, kurį norite atnaujinti: ")
        for user in users:
            if user.user_id == user_id:
                user_name = input("\nNaujas vartotojo vardas ir pavardė: ")
                if user_name:
                    user.user_name = user_name
                user_password = input("\nNaujas slaptažodis: ")
                if user_password:
                    user.user_password = user_password
                user_role = input(f"\nAr keisite rolę ?(dabar {Fore.RED}{user.user_role}): ")
                if user_role == "skaitytojas" or user_role == "bibliotekininkas":
                    user.user_role = user_role
                df.save_users(users)
                print(f"{Fore.BLUE}-" * 140)
                print(f"{Fore.GREEN}Vartotojas: {user.user_name} atnaujintas. Kortelės numeris yra: {user.user_id}, slaptazodis yra: {user.user_password}, o rolė yra: {user.user_role}")
                return
        print(f"\n{Fore.RED}Vartotojas nerastas.")
    except ValueError:
        print(f"\n{Fore.RED}Netinkamas ID formatas.")

def list_users():
    users = df.load_users()
    if not users:
        print(f"\n{Fore.RED}Vartotojų sąraše nėra.")
    else:
        for user in users:
            print(f"{Fore.BLUE}-" * 100)
            print(user)
            