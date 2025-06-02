import functions.library as lib

current_user = None

def login_menu():
    while True:
        global current_user
        user_id = input("Įveskite savo ID: ")
        password = input("Įveskite savo slaptažodį: ")

        user = lib.authenticate_user(user_id, password)
        if user:
            current_user = user
            print("-" * 40)
            print(f"Labas, {current_user.name}!")
            if current_user.role == "bibliotekininkas":
                librarian_menu()
            else:
                reader_menu()
            break
        elif user_id == "admin" and password == "admin":
            current_user = user_id
            print("-" * 40)
            print(f"Labas, {current_user}")
            librarian_menu()
            break
        else:
            print("Neteisingas ID arba slaptažodis. Bandykite dar kartą")
        return current_user


def librarian_menu():
    while True:
        print("\n------ Valdyti Vartotojus ------")
        print("1. Sukurti naują vartotoją")
        print("2. Atnaujinti vartotojo duomenis")
        print("3. Ištrinti vartotoją")
        print("4. Peržiūrėti vartotojų sąrašą")
        print("0. Baigti darbą")
        
        choice = int(input("Įveskite savo pasirinkimą: "))

        match choice:
            case 1:
                create_user_menu()
            case 2:
                update_user_menu()
            case 3:
                delete_user_menu()
            case 4:
                list_users_menu()
            case 0:
                print("Išėjote iš programos")
                exit()
            case _:
                print("Klaida. Bandykite dar kartą.")

def reader_menu():
    while True:
        print("\n--- Skaitytojo Meniu ---")
        print("1. Peržiūrėti savo duomenis")
        print("0. Baigti darbą")
        choice = int(input("Įveskite savo pasirinkimą: "))

        match choice:
            case 1:
                view_my_data()
            case 0:
                print("Išėjote iš programos.")
                exit()
            case _:
                print("Neteisingas pasirinkimas. Bandykite dar kartą.")

def view_my_data():
    if current_user:
        print("\n--- Jūsų duomenys ---")
        print(current_user)
    else:
        print("Nėra prisijungusio vartotojo.")

def create_user_menu():
    print("\n--- Kuriame naują vartotoją ---")
    name = input("Įveskite vardą ir pavardę: ")
    password = input("Įveskite slaptažodį: ")
    role = input("Įveskite rolę (skaitytojas ar bibliotekininkas): ").lower()
    lib.create_user(name, password, role)

def update_user_menu():
    print("\n--- Atnaujiname vartotojo duomenis ---")
    user_id = input("Įveskite vartotojo ID, kurį norite atnaujinti: ")
    user_to_update = lib.get_user_by_id(user_id)

    if user_to_update:
        print(f"Atnaujinamas vartotojas: {user_to_update.name}, jei nenorite kurios nors reikšmės keisti palikite tuščią")
        name = input(f"Naujas vardas (dabar: {user_to_update.name}): ")
        password = input("Naujas slaptažodis: ")

        lib.update_user_info(user_id, 
                             name if name else None,
                             password if password else None)
    else:
        print(f"Vartotojas kurio ID: '{user_id}' nerastas.")

def delete_user_menu():
    print("\n--- Ištriname vartotoją ---")
    user_id = input("Įveskite vartotojo ID, kurį norite ištrinti: ")
    lib.delete_user(user_id)

def list_users_menu():
    print("\n--- Visi vartotojai ---")
    users = lib.list_all_users()
    if users:
        for user in users:
            print("-" * 100)
            print(user)
        print("-" * 100)
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
        