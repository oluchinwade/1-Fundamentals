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
    
    def show_balance (self):
        print(f"{self.name} has an account balance of: £{self.balance}")
    
    def withdraw(self, amount):
        self.amount = 0
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.amount = 0
        self.balance += amount
        return self.balance

    def transfer_money(self, amount, receiver, input_pin):
        print(f"You are transferring £{amount} to {receiver.name}")
        print("Authentication required!")
        input_pin = input("Enter your PIN: ")
        input_pin = int(input_pin)
        if input_pin == self.pin:
            print("Transfer authorized")  
            if amount <= self.balance:  
                self.balance -= amount
                receiver.balance += amount
                print(f"{self.name} has an account balance of £{self.balance}")
                print(f"{receiver.name} has an account balance of £{receiver.balance}")

                return True 
            else:
                print("Insufficient funds.")
        else:
            print("Invalid PIN. Transaction canceled.")

    
    def request_money(self, request_amount, put_pin, input_password, person):
        print(f"You are requesting £{request_amount} from {person.name}")
        print("User authentication is required... ")
        put_pin = input(f"Enter {person.name}'s PIN: ")
        put_pin = int(put_pin)
        if put_pin == person.pin:
            input_password = input("Enter your password: ")
            if input_password == person.password:
                print("Request authorized")
                print(f"{self.name} sent £{request_amount} to {person.name}")
            else:
                print("Invalid password. Transaction canceled.")
        else:
            print("Invalid recipient's PIN. Transaction canceled.")
    




""" Driver Code for Task 1 """
'''driver_code = User("Bob", 1234,"password")
print(driver_code.name, driver_code.pin, driver_code.password)
'''
""" Driver Code for Task 2 """
driver_code2 = User("Olly", 1234, "password123")
print(driver_code2.name, driver_code2.pin, driver_code2.password)

""" Driver Code for Task 3"""
driver_code3 = BankUser("Bob", 1234, "password", 0)
print(driver_code3.name, driver_code3.pin, driver_code3.password, driver_code3.balance)

""" Driver Code for Task 4"""
'''driver_code3.show_balance()
driver_code3.deposit(5000)
driver_code3.show_balance()
driver_code3.withdraw(500)
driver_code3.show_balance()'''

""" Driver Code for Task 5"""

driver_code2 = BankUser("Olly", 1234, "password123",0)
print(driver_code2.name, driver_code2.pin, driver_code2.password)
driver_code3.show_balance()
driver_code3.deposit(5000)
driver_code3.show_balance()
driver_code2.show_balance()
transfer_tansaction = driver_code3.transfer_money(500,driver_code2,1234)
driver_code2.show_balance()
driver_code3.show_balance()