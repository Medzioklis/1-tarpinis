import functions.login_functions as fl
import functions.menu_functions as fm

def main():
    fl.create_initial_fakeadmin()

    print("=== Bibliotekos sistema ===")
    username = input("Įveskite kortelės numerį: ")
    password = input("Įveskite slaptažodį: ")

    user = fl.login(username, password)
    if user:
        print("-" * 70)
        print(f"Sveiki, {user.user_name}! Jūsų rolė: {user.user_role}")
        print("-" * 70)
        if user.user_role == "bibliotekininkas":
            fm.librarian_menu()
        else:
            print("Skaitytojo meniu dar kuriamas...")
    else:
        print("Neteisingas kortelės numeris arba slaptažodis.")

main()


# from functions.menu import login_menu

# def main():
#     login_menu()

# main()

    