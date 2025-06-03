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
        print("\n------ Vartotojų valdymas ------")
        print("1. Sukurti naują vartotoją")
        print("2. Atnaujinti vartotojo duomenis")
        print("3. Ištrinti vartotoją")
        print("4. Peržiūrėti vartotojų sąrašą")
        print("\n------ Knygų valdymas ----------")
        print("5. Pridėti naują knygą")
        print("6. Atnaujinti knygą sąraše")
        print("7. Ištrinti knygą")
        print("8. Peržiūrėti knygų sąrašą")
        print("0. Baigti darbą")
        
        choice = int(input("Įveskite savo pasirinkimą: "))

        match choice:
            case 1:
                create_user()
            case 2:
                update_user()
            case 3:
                delete_user()
            case 4:
                list_users()
            case 5:
                create_book()
            case 6:
                update_book()
            case 7:
                delete_book()
            case 8:
                list_books()
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

def create_user():
    print("\n--- Kuriame naują vartotoją ---")
    name = input("Įveskite vardą ir pavardę: ")
    password = input("Įveskite slaptažodį: ")
    role = input("Įveskite rolę (skaitytojas ar bibliotekininkas): ").lower()
    lib.create_user(name, password, role)

def update_user():
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

def delete_user():
    print("\n--- Ištriname vartotoją ---")
    user_id = input("Įveskite vartotojo ID, kurį norite ištrinti: ")
    lib.delete_user(user_id)

def list_users():
    print("\n--- Visi vartotojai ---")
    users = lib.list_all_users()
    if users:
        for user in users:
            print("-" * 100)
            print(user)
        print("-" * 100)
    else:
        print("Nėra registruotų vartotojų.")

# -------------------------------------------------------------------------
# -------------------------- Knygos valdymas ------------------------------
#--------------------------------------------------------------------------

def create_book():
    print("\n--- Pridedame naują knygą ---")
    book_title = input("Įveskite knygos pavadinimą: ")
    book_author = input("Įveskite knygos autorių: ")
    book_genre = input("Įveskite knygos žanrą:(romanas, detektyvas, fantastika, biografija): ").lower()
    book_release = input("Įveskite knygos išleidimo metus: (2005): ")
    lib.create_book(book_title, book_author, book_genre, book_release)

def list_books():
    print("\n---------- Visos knygos --------")
    books = lib.list_all_books()
    if books:
        for book in books:
            print("-" * 150)
            print(book)
        print("-" * 150)
    else:
        print("Nėra registruotų vartotojų.")

def update_book():
    print("\n--- Atnaujiname knygos duomenis ---")
    book_id = input("Įveskite knygos ID, kurią norite atnaujinti: ")
    book_to_update = lib.get_book_by_id(book_id)

    if book_to_update:
        print(f"Atnaujinama knyga: {book_to_update.title}, jei nenorite kurios nors reikšmės keisti palikite tuščią")
        book_title = input(f"Naujas pavadinimas (dabar: {book_to_update.title}): ")
        book_author = input(f"Naujas autorius (dabar: {book_to_update.author}): ")
        book_genre = input(f"Naujas žanras (dabar: {book_to_update.genre}): ")
        book_release = int(input(f"Naujas žanrasleidimo metai (dabar: {book_to_update.release}): "))

        lib.update_book_info(book_id, 
                             book_title if book_title else None,
                             book_author if book_author else None,
                             book_genre if book_genre else None,
                             book_release if book_release else None)
    else:
        print(f"Knyga kurios ID: '{book_id}' nerasta.")

def delete_book():
    print("\n--- Ištriname knygą ---")
    book_id = input("Įveskite knygos ID, kurią norite ištrinti: ")
    lib.delete_book(book_id)