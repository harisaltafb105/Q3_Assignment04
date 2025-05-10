import random

def guess_my_number():

    random_number = random.randint(1, 6)
    your_guess = int(input("Guess a number between 1 and 6: "))

    while your_guess != random_number:
        if your_guess < random_number:
            print("Too low! Try again.")
        elif your_guess > random_number:
            print("Too high! Try again.")
        your_guess = int(input("Guess a number between 1 and 6: "))
    
    print("Congratulations! You've guessed the number!")
        
        
guess_my_number()