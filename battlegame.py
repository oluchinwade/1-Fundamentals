#TASK 1
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Ocr"

#now declaring hitpoints
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 150

# declaring the damages
wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 120

#Dragons Variables
dragon_hp = 300
dragon_damage = 50

while True:
    print(f" 1) {wizard}\n 2) {elf}\n 3) {human}\n 4) {orc}\n Choose your character:" )
    character = input().lower()
    if character == '1' or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print(f"Health: {my_hp}\nDamage: {my_damage}")
        break
    elif character == '2' or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print(f"Health: {my_hp}\nDamage: {my_damage}")
        break
    elif character == '3' or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print(f"Health: {my_hp}\nDamage: {my_damage}")
        break
    elif character == '4' or character == "orc":
        character = orc
        my_hp = orc_hp 
        my_damage = orc_damage
        print(f"Health: {my_hp}\nDamage: {my_damage}")
        break
    else:
        print("Unknown character. Please choose 1, 2, 3, or 4.")
        
while True:
    dragon_hp = dragon_hp - my_damage
    print(f"The {character}, damaged the Dragon!")
    print(f"The Dragon's hitpoints are now:,{dragon_hp}\n")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print(f"The dragon stricks back!\nThe {character}, has been damaged by the Dragon!\nThe {character} Hitpoint is now {my_hp} \n")
    if my_hp <= 0:
        print(f"{character} has lost the battle")
        break
while True:
    option = input("Would you like to play again? YES/NO:   ").lower()
    if option == "yes":
        print("Game starting oveR.\n LOADING.......")
    else:
        break
