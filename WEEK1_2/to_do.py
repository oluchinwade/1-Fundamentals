to_do_list = []

while True:
    while True:
        list = input("What would you like to do to the list today?\n add,remove or quit   ").lower()

        if list == "quit":
            print("Thanks for showing up, have a good day!")
            break
        elif list == "add":
            item = input("What would you like to add?   ").lower()
            to_do_list.append(item)
            print("Item added successfully!")
            print(to_do_list)
            break
        elif list == "remove":
            item = input("What would you like to remove from list?   ").lower()
            if item not in to_do_list:
                print("Sorry, this item does not exist")
                print(to_do_list)
            else:
                to_do_list.remove(item)
                break
        else:
            print("Selection not recognized please try again.")
    option = input(" Would you like to continue on this app?\n Yes/No   ").lower()
    if option == "yes":
        continue
    else:
        break    