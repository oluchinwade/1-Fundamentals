from donation_pkg import homepage
from donation_pkg import user

database = {"Olly":"password123"}
donation = []
authorized_user = ""



while True:
    homepage.show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
        
    else:
        print(f"Logged in as: {authorized_user}")
    
    option = input("Choose an option: ")
    if option == "1":
        username = input("Enter username: ")
        password = input("Enter password:")
        authorized_user = user.login(database, username, password)
        continue
    elif option == "2":
        username = input("Enter username: ")
        password = input("Enter password:")
        authorized_user = user.register(database, username)
        if authorized_user != "":
            database[username] = password
        continue
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = homepage.donate(username)
            donation.append(donation_string)
        continue
    elif option == "4":
        homepage.show_donation(donation)
        continue
    else:
        print("Sad to see you go. Goodbye!")
        break



