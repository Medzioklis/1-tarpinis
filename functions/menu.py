def check_user_perm(username):
    if username == "admin":
        perm = 1
    else:
        perm = 2
    return perm

def menu(perm):
    if perm == 1:
        print(f"{"-" * 15} MENIU {"-" * 15}")
        print("1. Knygų sąrašas")
        print("2. Knygos paieška")
        print("3. Įvesti knyga")
        print("4. Redaguoti knyga")
        print("5. Trinti knyga")
        print("\n")
        print("6. Vartotojų sąrašas")
        print("7. Vartotojo paieška")
        print("8. Įvesti vartotoją")
        print("9. Redaguoti vartotoją")
        print("10. Trinti vartotoją")
        print("10. Išeiti iš programos")
        print("-" * 36)
    elif perm == 2:
        print(f"{"-" * 15} MENIU {"-" * 15}")
        print("1. Knygų sąrašas")
        print("2. Paimti knygą")
        print("3. Gražinti knyga")
        print("4. Mano knygų krepšelis")
        print("5. Išeiti iš programos")
        print("-" * 36)
    else:
        print("Neturite prieigos prie meniu")
        