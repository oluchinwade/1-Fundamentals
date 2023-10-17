def login(database, username, password):
        if username in database and database[username] == password:
            print(f"Welcome back {username}!")
            return username
        elif username in database and database[username] != password:
            print(f"{username}, you have entered an incorrect username/password")
            return ""
        else:
            print("User not found. Please register")
            return""


def register(database, username):
    if username in database:
        print("username already exists, choose a new username")
        return ""
    else:
        print(f"{username} you've been registered!")