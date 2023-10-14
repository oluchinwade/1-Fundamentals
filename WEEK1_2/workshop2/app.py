from banking_pkg import account
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

while True:
    print("          === Automated Teller Machine ===          ")
    name = input("Enter name to register:  ")
    if len(name) >=1 and len(name) <= 10:
        break
    else: 
        print("Name choice is limited to 10 character")

while True:
    pin = input("Enter PIN: ")
    if len(pin)==4:
        break
    else:
        print("Pin is limited to 4 numerical characters")
balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    user_name = input("Enter name: ")
    user_pin = input("Enter PIN: ")
    if user_name!= name or user_pin != pin:
        print("Invalid credentials! Please try again.")
    else:
        print("Login successful")
        break

while True:
    print(atm_menu(name))
    option = int(input("Choose an option: "))
    if option == 1:
        print(f"Your current balance is ${account.show_balance(balance)}")
    elif option == 2:
        balance = account.deposit(balance)
        print(f"Your new balance is ${balance}")
    elif option == 3:
        with_bal = account.withdraw(balance)
        print(with_bal)
        if with_bal < 0:
            print("Insufficient fund!")
    elif option == 4:
        account.logout(name)
        break
    else:
        print("Your selection is wrong, please select from existing options")   
