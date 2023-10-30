import random

'''def guess_random_number(tries, start, stop):
    rand_num = random.randint(start,stop)
    while tries != 0:
        print(f"You have {tries} more tries")
        guess = int(input(f"Guess the number between {start} and {stop}: "))
        if guess == rand_num:
            print("You guessed the right number!!")
            break

        elif guess != rand_num:
            tries-=1
            if guess > rand_num:
                print("Hint: Guess lower!")
            elif guess < rand_num:
                print("Hint: Guess Higher!")
            
        
        if tries == 0:
            print("Your time is up!")
            break

guess_random_number(5,0,10)'''
            
"""def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    for x in range(start,stop+1):
        guess = x

        if guess == random_number:
            print(f'You got it! the guessed number was {random_number}')
        
        elif guess < random_number:
            print("Guess Higher!")
            tries -=1
        
        else:
            print("Guess lower")
            tries -=1
        

        if tries == 0:
            print(f"You have run out of time. the right number was {random_number}")
            break

guess_random_num_linear(5,0,10)"""





