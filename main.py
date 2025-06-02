# pradedam
from classes.user import User

# users_file_location = "D:/AI studijos/1 tarpinis/data/users.pickle" # namu kompe kelias iki data
users_file_location = "D:/AI studijos/1-tarpinis/data/users.pickle" # darbo kompe kelias iki data

user = User(users_file_location)
users = user.collect_data()
for ele in users:
    print(ele)



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
    