import random

high_score = 0


def dice_game():
    global high_score
    while True:
        print(f"Current High score: {high_score}\n1) Roll Dice\n2) Leave Game")
        user_input = input("Enter your choice: ")
        if user_input == "2":
            print("Goodbye!")
            break
        elif user_input == "1":
            number_1 = random.randint(1,6)
            number_2 = random.randint(1,6)
            print(f"you roll....{number_1}")
            print(f"You roll....{number_2}")
            high_score = number_1 + number_2
        else:
            print('invalid option please try again')



dice_game()