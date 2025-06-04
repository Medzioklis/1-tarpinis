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
        print("8. Šalinti pasenusias knygas")
        print("9. Peržiūrėti knygų sąrašą")
        print("10. Knygos paieška")
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
                delete_old_book()
            case 9:
                list_books()
            case 10:
                search_book()
            case 0:
                print("Išėjote iš programos")
                exit()
            case _:
                print("Klaida. Bandykite dar kartą.")

def reader_menu():
    while True:
        print("\n--- Skaitytojo Meniu ---")
        print("1. Peržiūrėti savo duomenis")
        print("2. Knygos paieška")
        print("3. Paimti knygas")
        print("0. Baigti darbą")
        choice = int(input("Įveskite savo pasirinkimą: "))

        match choice:
            case 1:
                view_my_data()
            case 2:
                search_book()
            case 3:
                print("Knygos pasiemimas")
            case 0:
                print("Išėjote iš programos.")
                exit()
            case _:
                print("Neteisingas pasirinkimas. Bandykite dar kartą.")

# -------------------------------------------------------------------------
# -------------------------- Skaitytojo -----------------------------------
# ------------------------ Meniu valdymas ---------------------------------
# -------------------------------------------------------------------------

def view_my_data():
    if current_user:
        print("\n--- Jūsų duomenys ---")
        print(current_user)
    else:
        print("Nėra prisijungusio vartotojo.")

def borrow_book():
    global current_user

    book_title = input("Įveskite knygos pavadinimą kurią norite paimti: ")
    book_to_take = lib.get_book_by_title(book_title)
    if not book_to_take:
        print(f"Knyga {book_title} nerasta")
        return
    if book_to_take.book_unit <= 0:
        print(f"Knygos šiuo metu nėra sandėlyje")
        return
    
    lib.


# -------------------------------------------------------------------------
# ------------------------- Bibliotekininko -------------------------------
# ------------------------ Vartotojo valdymas -----------------------------
# -------------------------------------------------------------------------

def create_user():
    print("\n--- Kuriame naują vartotoją ---")
    name = input("Įveskite vardą ir pavardę: ")
    password = input("Įveskite slaptažodį: ")
    while True:
        role = input("Įveskite rolę (skaitytojas ar bibliotekininkas): ").lower()
        if role == "skaitytojas" or role == "bibliotekininkas":
            break
        else:
            print(f"Neteisingai įvedėte rolę {role}. Bandykite dar kartą")
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
# ------------------------- Bibliotekininko -------------------------------
# ------------------------- Knygos valdymas -------------------------------
# -------------------------------------------------------------------------

def create_book():
    print("\n--- Pridedame naują knygą ---")
    book_title = input("Įveskite knygos pavadinimą: ")
    book_author = input("Įveskite knygos autorių: ")
    while True:
        book_genre = input("Įveskite knygos žanrą:(romanas, detektyvas, fantastika, biografija): ").lower()
        if book_genre == "detektyvas" or book_genre == "romanas" or book_genre == "fantastika" or book_genre == "biografija":
            break
        else:
            print(f"Neteisingai įvedėte {book_genre} žanrą. Bandykite dar kartą")
    book_release = input("Įveskite knygos išleidimo metus: (2005): ")
    while True:
        try:
            book_unit = int(input("Įveskite kiek tokių knygų turime: "))
            break
        except ValueError:
            print("Įveskite vienetų skaičių")
    lib.create_book(book_title, book_author, book_genre, book_release, book_unit)

def list_books():
    print("\n---------- Visos knygos --------")
    books = lib.list_all_books()
    if books:
        for book in books:
            print("-" * 150)
            print(book)
        print("-" * 150)
    else:
        print("Nėra įvestų knygų.")

def update_book():
    print("\n--- Atnaujiname knygos duomenis ---")
    book_id = input("Įveskite knygos ID, kurią norite atnaujinti: ")
    book_to_update = lib.get_book_by_id(book_id)

    if book_to_update:
        print(f"Atnaujinama knyga: {book_to_update.book_title}, jei nenorite kurios nors reikšmės keisti palikite tuščią")
        book_title = input(f"Naujas pavadinimas (dabar: {book_to_update.book_title}): ")
        book_author = input(f"Naujas autorius (dabar: {book_to_update.book_author}): ")
        while True:
            book_genre = input(f"Naujas žanras (dabar: {book_to_update.book_genre}): ").lower()
            if book_genre == "detektyvas" or book_genre == "romanas" or book_genre == "fantastika" or book_genre == "biografija" or book_genre == "":
                break
            else:
                print(f"Neteisingai įvedėte {book_genre} žanrą. Bandykite dar kartą")
        book_release = int(input(f"Nauji leidimo metai (dabar: {book_to_update.book_release}): "))
        while True:
            try:
                book_unit = int(input(f"Atnaujinkite vnt., skaičių (privaloma) (dabar yra: {book_to_update.book_unit} vnt.): "))
                break
            except ValueError:
                print("Įveskite vienetų skaičių")

        lib.update_book_info(book_id, book_title if book_title else None, book_author if book_author else None, book_genre if book_genre else None, book_release if book_release else None, book_unit if book_unit else None)
    else:
        print(f"Knyga kurios ID: '{book_id}' nerasta.")

def delete_book():
    print("\n--- Ištriname knygą ---")
    book_id = input("Įveskite knygos ID, kurią norite ištrinti: ")
    lib.delete_book(book_id)

def search_book():
    print("\n-------- Knygos paieška ----------")
    search_input = input("Įveskite knygos pavadinimą ar autorių: ")
    found_books_list = lib.get_book_by_search(search_input)

    if found_books_list:
        print("\nRastos knygos:")
        for book in found_books_list:
            print("-" * 150)
            print(f"Knygos ID: {book.book_id}, pavadinimas: {book.book_title}, autorius: {book.book_author}, žanras: {book.book_genre}, sandėlyje: {book.book_unit} vnt.")
    else:
        print(f"Knyga su pavadinimu ar autoriumi, atitinkančiu {search_input}, nerasta.")

def delete_old_book():
    print("\n----- Ištriname senas knygas -----")
    year_input = input("Įveskite metus nuo kurių knyga laikoma pasenusi ir reikia ištrinti (pvz: 1970): ")
    found_books_list = lib.get_books_by_years(year_input)

    if found_books_list:
        print("\nRastos knygos:")
        for book in found_books_list:
            print("-" * 150)
            print(f"Knygos ID: {book.book_id}, pavadinimas: {book.book_title}, autorius: {book.book_author}, žanras: {book.book_genre}, sandėlyje: {book.book_unit} vnt.")
            lib.delete_book(book.book_id)
    else:
        print(f"Senesnių knygų nei {year_input} metų, nerasta.")
    