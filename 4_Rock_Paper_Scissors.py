import random

def isWin(user, computer):
    if (user == 's' and computer == 'p') or (user == 'p' and computer == 'r') or (user == 'r' and computer == 's'):
        return True
    return False

def play():
    print("Rock, Paper, Scissors!\n")

    user = input("r for Rock, p for Paper, s for Scissors.\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("TIE!!")
    elif isWin(user, computer):
        print(f"You win! The computer chooses '{computer}'.")
    elif not isWin(user, computer):
        print(f"You lose! The computer choose '{computer}'.")

play()