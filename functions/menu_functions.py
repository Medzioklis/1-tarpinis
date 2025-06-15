import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from . import librarian_functions as lf
from . import book_function as bf
from . import reader_functions as rf


def librarian_menu():
    while True:
        print(f"{Fore.CYAN}\n===== Bibliotekininko meniu =====\n")
        print(f"{Fore.YELLOW}1. Vartotojų valdymas")
        print(f"{Fore.YELLOW}2. Knygų valdymas")
        print(f"{Fore.YELLOW}0. Atsijungti")
       
        choice = int(input("\nPasirinkite: "))

        match choice:
            case 1:
                user_management_menu()  
            case 2:
                book_management_menu()
            case 0:
                print(f"{Fore.GREEN}Atsijungėte")
                exit()
            case _:
                print(f"{Fore.RED}Neteisingas pasirinkimas.")


def user_management_menu():
    while True:
        print(f"{Fore.CYAN}\n======= Vartotojų valdymas =======\n")
        print(f"{Fore.YELLOW}1. Sukurti vartotoją")
        print(f"{Fore.YELLOW}2. Ištrinti vartotoją")
        print(f"{Fore.YELLOW}3. Atnaujinti vartotoją")
        print(f"{Fore.YELLOW}4. Peržiūrėti vartotojų sąrašą")
        print(f"{Fore.YELLOW}0. Grįžti į pradinį meniu")
        
        choice = int(input("\nPasirinkite: "))

        match choice:
            case 1:
                lf.create_user()
            case 2:
                lf.delete_user()
            case 3:
                lf.update_user()
            case 4:
                lf.list_users()
            case 0:
                librarian_menu()
            case _:
                print(f"\n{Fore.RED}Neteisingas pasirinkimas.")


def book_management_menu():
    while True:
        print(f"{Fore.CYAN}\n=========== Knygų valdymas ===========\n")
        print(f"{Fore.YELLOW}1. Pridėti knygą")
        print(f"{Fore.YELLOW}2. Ištrinti knygą")
        print(f"{Fore.YELLOW}3. Atnaujinti knygą")
        print(f"{Fore.YELLOW}4. Peržiūrėti visas knygas")
        print(f"{Fore.YELLOW}5. Ieškoti knygos pagal pavadinimą/autorių")
        print(f"{Fore.YELLOW}0. Grįžti į pradinį meniu")
        
        choice = int(input("\nPasirinkite: "))

        match choice:
            case 1:
                bf.add_book()
            case 2:
                bf.delete_book()
            case 3:
                bf.update_book()
            case 4:
                bf.list_books()
            case 5:
                bf.search_books()
            case 0:
                librarian_menu()
            case _:
                print(f"\n{Fore.RED}Neteisingas pasirinkimas.")


def reader_menu(user):
    while True:
        print(f"{Fore.CYAN}\n=== Skaitytojo meniu ===\n")
        print(f"{Fore.YELLOW}1. Peržiūrėti visas knygas")
        print(f"{Fore.YELLOW}2. Paimti knygą")
        print(f"{Fore.YELLOW}3. Grąžinti knygą")
        print(f"{Fore.YELLOW}4. Mano pasiskolintos knygos")
        print(f"{Fore.YELLOW}0. Atsijungti")
        
        choice = int(input("\nPasirinkite: "))

        match choice:

            case 1:
                bf.list_books()
            case 2:
                rf.book_basket(user)
            case 3:
                rf.return_book(user)
            case 4:
                rf.view_my_books(user)
            case 0:
                print(f"\n{Fore.GREEN}Atsijungėte")
                exit()
            case _:
                print(f"\n{Fore.RED}Neteisingas pasirinkimas.")