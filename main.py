# pradedam
from classes.user import User

catalog = "D:/AI studijos/1 tarpinis/data"  # namu kompe kelias iki data
users_data = "users.pickle"

user = User()
data = user.load_user_data(catalog, users_data)
data = user.collect_data()
user.save_user_data(catalog, users_data, data)
# users = user.load_user_data(catalog, users_data)
# for ele in users:
#     print(ele)


# from functions import login

# while True:
#     username = input("Iveskite vartotojo varda: ")
#     password = input("Iveskite slaptazodi: ")

#     sesion = login.check_login_user(username, password)
#     if sesion == True:
#         print(f"Sveiki prisijunge {username}")
#         from functions import menu
#         perm = menu.check_user_perm(username)
#         menu.menu(perm)
#         break
#     else:
#         print(f"Prisijungimas nepavyko. Bandykite dar karta")
    