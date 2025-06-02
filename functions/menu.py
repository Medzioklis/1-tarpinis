import functions.library as lib

current_user = None

def display_main_menu():
    """Atvaizduoja pagrindinį meniu."""
    while True:
        print("\n--- Pagrindinis Meniu ---")
        print("1. Prisijungti")
        print("2. Registruotis (kaip skaitytojas)")
        print("0. Išeiti")
        choice = input("Įveskite savo pasirinkimą: ")

        if choice == '1':
            login_menu()
        elif choice == '2':
            register_reader_menu()
        elif choice == '0':
            print("Iki pasimatymo!")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

def register_reader_menu():
    """Meniu naujo skaitytojo registracijai."""
    print("\n--- Registruotis kaip skaitytojas ---")
    first_name = input("Įveskite vardą: ")
    last_name = input("Įveskite pavardę: ")
    password = input("Įveskite slaptažodį: ")
    lib.create_user(first_name, last_name, password, "reader")

def login_menu():
    """Vartotojo prisijungimo meniu."""
    global current_user
    user_id = input("Įveskite savo ID: ")
    password = input("Įveskite savo slaptažodį: ")

    user = lib.authenticate_user(user_id, password)
    if user:
        current_user = user
        print(f"Sveiki prisijungę, {current_user.first_name}!")
        if current_user.role == "librarian":
            librarian_menu()
        else:
            reader_menu()
    else:
        print("Neteisingas ID arba slaptažodis.")

def librarian_menu():
    """Bibliotekininko meniu."""
    while True:
        print("\n--- Bibliotekininko Meniu ---")
        print("1. Peržiūrėti savo duomenis")
        print("2. Valdyti vartotojus")
        print("0. Atsijungti")
        choice = input("Įveskite savo pasirinkimą: ")

        if choice == '1':
            view_my_data()
        elif choice == '2':
            manage_users_menu()
        elif choice == '0':
            global current_user
            current_user = None
            print("Atsijungta.")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

def reader_menu():
    """Skaitytojo meniu."""
    while True:
        print("\n--- Skaitytojo Meniu ---")
        print("1. Peržiūrėti savo duomenis")
        print("0. Atsijungti")
        choice = input("Įveskite savo pasirinkimą: ")

        if choice == '1':
            view_my_data()
        elif choice == '0':
            global current_user
            current_user = None
            print("Atsijungta.")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

def view_my_data():
    """Peržiūrėti prisijungusio vartotojo duomenis."""
    if current_user:
        print("\n--- Jūsų duomenys ---")
        print(current_user)
    else:
        print("Nėra prisijungusio vartotojo.")

def manage_users_menu():
    """Meniu vartotojų valdymui (tik bibliotekininkui)."""
    while True:
        print("\n--- Valdyti Vartotojus ---")
        print("1. Sukurti naują vartotoją")
        print("2. Atnaujinti vartotojo duomenis")
        print("3. Ištrinti vartotoją")
        print("4. Peržiūrėti visus vartotojus")
        print("0. Grįžti į Bibliotekininko meniu")
        choice = input("Įveskite savo pasirinkimą: ")

        if choice == '1':
            create_user_menu()
        elif choice == '2':
            update_user_menu()
        elif choice == '3':
            delete_user_menu()
        elif choice == '4':
            list_users_menu()
        elif choice == '0':
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

def create_user_menu():
    """Meniu naujo vartotojo kūrimui (tik bibliotekininkui)."""
    print("\n--- Kurti Naują Vartotoją ---")
    first_name = input("Įveskite vardą: ")
    last_name = input("Įveskite pavardę: ")
    password = input("Įveskite slaptažodį: ")
    role = input("Įveskite rolę ('reader' arba 'librarian'): ").lower()
    lib.create_user(first_name, last_name, password, role)

def update_user_menu():
    """Meniu vartotojo duomenų atnaujinimui (tik bibliotekininkui)."""
    print("\n--- Atnaujinti Vartotoją ---")
    user_id = input("Įveskite vartotojo ID, kurį norite atnaujinti: ")
    user_to_update = lib.get_user_by_id(user_id)

    if user_to_update:
        print(f"Atnaujinamas vartotojas: {user_to_update.first_name} {user_to_update.last_name}")
        first_name = input(f"Naujas vardas (palikite tuščią, jei nenorite keisti, dabartinis: {user_to_update.first_name}): ")
        last_name = input(f"Nauja pavardė (palikite tuščią, jei nenorite keisti, dabartinis: {user_to_update.last_name}): ")
        password = input("Naujas slaptažodis (palikite tuščią, jei nenorite keisti): ")
        role = input(f"Nauja rolė ('reader' arba 'librarian', palikite tuščią, jei nenorite keisti, dabartinė: {user_to_update.role}): ").lower()

        lib.update_user_info(user_id, # Funkcijos pavadinimas pakeistas
                             first_name if first_name else None,
                             last_name if last_name else None,
                             password if password else None,
                             role if role in ["reader", "librarian"] else None)
    else:
        print(f"Vartotojas su ID '{user_id}' nerastas.")

def delete_user_menu():
    """Meniu vartotojo ištrynimui (tik bibliotekininkui)."""
    print("\n--- Ištrinti Vartotoją ---")
    user_id = input("Įveskite vartotojo ID, kurį norite ištrinti: ")
    lib.delete_user(user_id)

def list_users_menu():
    """Meniu visų vartotojų sąrašui (tik bibliotekininkui)."""
    print("\n--- Visi Vartotojai ---")
    users = lib.list_all_users()
    if users:
        for user in users:
            print("-" * 20)
            print(user)
        print("-" * 20)
    else:
        print("Nėra registruotų vartotojų.")

# def check_user_perm(username):
#     if username == "admin":
#         perm = 1
#     else:
#         perm = 2
#     return perm

# def menu(perm):
#     if perm == 1:
#         print(f"{"-" * 15} MENIU {"-" * 15}")
#         print("1. Knygų sąrašas")
#         print("2. Knygos paieška")
#         print("3. Įvesti knyga")
#         print("4. Redaguoti knyga")
#         print("5. Trinti knyga")
#         print("\n")
#         print("6. Vartotojų sąrašas")
#         print("7. Vartotojo paieška")
#         print("8. Įvesti vartotoją")
#         print("9. Redaguoti vartotoją")
#         print("10. Trinti vartotoją")
#         print("10. Išeiti iš programos")
#         print("-" * 36)
#     elif perm == 2:
#         print(f"{"-" * 15} MENIU {"-" * 15}")
#         print("1. Knygų sąrašas")
#         print("2. Paimti knygą")
#         print("3. Gražinti knyga")
#         print("4. Mano knygų krepšelis")
#         print("5. Išeiti iš programos")
#         print("-" * 36)
#     else:
#         print("Neturite prieigos prie meniu")
        