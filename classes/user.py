# Klasė teikianti bendrą funkcionalumą bibliotekininkams ir skaitytojams, užtikrinanti pickle suderinamumą (users.pkl) ir vaidmenų kontrolę.

from datetime import datetime
import pickle, os

class User():
    def __init__(self, user_id=None, role=None, name=None):
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
    
    def collect_data(self):
        data_in = []
        id = self.get_user_id()
        role = self.get_role()
        name = self.get_name()
        data_in.append({"user_id": id, "role": role, "name": name})
        print(data_in)
        
    
    def load_user_data(self, catalog, users_data):
        self.catalog = catalog
        self.users_data = users_data
        self.road_to_file = os.path.join(catalog, users_data)

        try:
            with open(self.road_to_file, "rb") as file:
                data = pickle.load(file)
            print("Duomenys nuskaityti")
            return data
        except FileNotFoundError:
            print("Failas nerastas!")
        except Exception:
            print("Klaida nuskaitant")
   

    def save_user_data(self, catalog, users_data, data_in):
        self.catalog = catalog
        self.users_data = users_data
        self.road_to_file = os.path.join(catalog, users_data)

        try:
            with open(self.road_to_file, "wb") as file:
                pickle.dump(data_in, file)
                print("Duomenys įrašyti")
        except Exception as e:
            print(f"Klaida: {e}")
            
    
    
    
