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
    print(f"Random number to find is {random_number}")
    for x in range(start,stop+1):
        guess = x

        if guess == random_number:
            print(f'You got it! the guessed number is :{random_number}')
        
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

def guess_random_num_binary(tries, start, stop):
    ran_number = random.randint(start, stop)
    print(f"Random number to find is: {ran_number}")
    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
        pivot = (lower_bound+upper_bound)//2

        if pivot == ran_number:
            print(f"Found it {ran_number}")
            return 
        elif pivot > ran_number:
            upper_bound = pivot -1
            tries -=1
            print("Guess Lower")

        else:
            lower_bound = pivot +1
            tries -= 1
            print("Guess Higher!")
        

        if tries == 0:
            print("Your program failed to find the number.")
            return
    

guess_random_num_binary(5,0,100)





