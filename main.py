# pradedam
from functions import login

while True:
    username = input("Iveskite vartotojo varda: ")
    password = input("Iveskite slaptazodi: ")

    sesion = login.check_login_user(username, password)
    if sesion == True:
        print(f"Sveiki prisijunge {username}")
        from functions import menu
        perm = menu.check_user_perm(username)
        menu.menu(perm)
        break
    else:
        print(f"Prisijungimas nepavyko. Bandykite dar karta")
    