# Klasė teikianti bendrą funkcionalumą bibliotekininkams ir skaitytojams, užtikrinanti pickle suderinamumą (users.pkl) ir vaidmenų kontrolę.

from datetime import datetime
import pickle
import os

class User():
    def __init__(self, users_file_location, user_id=None, role=None, name=None):
        self.users_file_location = users_file_location
        self.user_id = user_id
        self.role = role
        self.name = name

    def get_user_id(self):
        user_id = int(datetime.now().timestamp())
        return user_id
    
    def get_role(self):
        while True:
            role = input("Priskirkite rolę (skaitytojas ar bibliotekininkas): ").lower()
            if role == "skaitytojas" or role == "bibliotekininkas":
                break
            else:
                print(f"Jūs įvedėte klaidingą rolę: {role}. Bandykite pakartoti!")
        return role
    
    def get_name(self):
        while True:
            name = input("Įveskite vardą ir pavardę: ")
            if name != "":
                break
            else:
                print("Prašau suveskite duomenis")
        return name
    
    def load_user_data(self):
        try:
            with open(self.users_file_location, "rb") as file:
                data = pickle.load(file)
            print("Duomenys nuskaityti")
            return data
        except FileNotFoundError:
            print("Failas nerastas!")
            return []
        except Exception:
            print("Klaida nuskaitant")
            return []
    
    def save_user_data(self, data):
        try:
            with open(self.users_file_location, "wb") as file:
                pickle.dump(data, file)
                print("Duomenys įrašyti")
        except Exception as e:
            print(f"Klaida: {e}")
    
    def collect_data(self):
        data = self.load_user_data()
        user_data = {
            "user_id": self.get_user_id(),
            "role": self.get_role(),
            "name": self.get_name()
        }
        data.append(user_data)

        self.save_user_data(data)
        return data

            
    
    
    
