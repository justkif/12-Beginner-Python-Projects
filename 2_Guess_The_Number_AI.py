import random

def guess(x):
    num = random.randint(1,x)
    guess = 0
    while guess != num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > num:
            print("Number's too high. Try again.")
        elif guess < num:
            print("Number's too low. Try again.")

    print(f"Correct! The number is {num}.")

guess(10)
