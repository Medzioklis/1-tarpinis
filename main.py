import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import functions.login_functions as fl
import functions.menu_functions as fm

def main():
    fl.create_initial_fakeadmin()

    print(f"{Fore.CYAN}\n======= Bibliotekos sistema =======\n")
    username = input(f"Įveskite kortelės numerį: ")
    password = input(f"Įveskite slaptažodį: ")

    user = fl.login(username, password)
    if user:
        print(f"{Fore.GREEN}\nSveiki, {user.user_name}! Jūsų rolė: {user.user_role}")
        print("-" * 70)
        if user.user_role == "bibliotekininkas":
            fm.librarian_menu()
        else:
            fm.reader_menu(user)
    else:
        print(f"{Fore.RED}Neteisingas kortelės numeris arba slaptažodis.")

main()


    