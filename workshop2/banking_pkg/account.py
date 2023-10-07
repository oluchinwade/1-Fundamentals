def show_balance(balance):
    return balance
    

def deposit(balance):
    amount = float(input("Enter amount to deposit:  "))
    if amount >0:
        balance = amount + balance
        return balance
    else:
        print('You cannot input a value less than or equal to $0')

def withdraw(balance):
    with_amount = float(input("Enter amount to withdraw: "))
    balance = balance - with_amount
    return balance

def logout(name):
    print(f"Goodbye {name}!")

