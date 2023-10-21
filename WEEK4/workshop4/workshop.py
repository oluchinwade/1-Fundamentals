class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password
    
    def change_name(self,name):
        self.name = name
        print(f"Your name name is {self.name}")
    
    def change_pin(self,pin):
        self.pin = pin
        print(f"Your pin has been changed to {self.pin}")
    
    def change_password(self,password):
        self.password = password
        print("Your password has been changed")
    
class BankUser(User):
    def __init__(self,name, pin, password, balance):
        super().__init__(name,pin,password)
        self.balance = balance
        self.balance = 0
    
    def show_balance (self, balance):
        print(balance)
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    





""" Driver Code for Task 1 """
driver_code = User("Bob", 1234,"password")
print(driver_code.name, driver_code.pin, driver_code.password)

""" Driver Code for Task 2 """
'''driver_code2 = User("Olly", 1234, "password123")
print(driver_code2.name, driver_code2.pin, driver_code2.password)'''

""" Driver Code for Task 3"""
driver_code3 = BankUser("Bob", 1234, "password", 0)
print(driver_code3.name, driver_code3.pin, driver_code3.password, driver_code3.balance)

""" Driver Code for Task 4"""
driver_code3.show_balance()

