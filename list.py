'''new_list = ['food', 'man','apple','fashion']

list2 = list(new_list)

new_list.append('bootcamp')

print(list2, new_list)'''


import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press 'Enter' to pick a card or Press 'Q' then enter to quit:  ").lower()
    if user_input == "q":
        print("Sad to see you go. Bye!")
        break
    else:
        new_list = random.choice(diamonds)
        hand.append(new_list)
        diamonds.remove(new_list)
        print(f"Your hand: {hand}")
        print(f"Remaining cards: {diamonds}")    
    if not diamonds:
        print("There are no more cards to pick \nThank you playing, Bye! ")
        break



