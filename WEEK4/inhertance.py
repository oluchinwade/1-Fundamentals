class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def change_password(self,password):
        self.password = password
        print("Your password hass been changed to:", self.password)


class Bankuser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 10
    
    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)
    

bankuser1 = Bankuser("Olly", "olly@nucamp.com", "password123")
print(bankuser1.name, bankuser1.check_balance())