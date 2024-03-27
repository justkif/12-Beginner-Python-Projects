import random

def guess(x):
    print(f"Think of a number from 1 to {x}.")

    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            num = random.randint(low, high)
        else:
            num = low

        feedback = input(f"Is {num} too high(h), too low(l) or correct(c)?: ")

        if low != high:
            if feedback == 'l':
                low = num + 1
            elif feedback == 'h':
                high = num - 1

            
    print(f"I've guessed your number: {num}")

guess(10)
    