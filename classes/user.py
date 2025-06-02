class User():
    def __init__(self, user_id, name, password, role="skaitytojas"):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.role = role
    
    def __str__(self):
        return (f"ID: {self.user_id}, Vardas, Pavardė: {self.name}, rolė: {self.role}")


            
    
    
    
