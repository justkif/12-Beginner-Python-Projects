import random

def isWin(user, computer):
    if (user == 's' and computer == 'p') or (user == 'p' and computer == 'r') \
        or (user == 'r' and computer == 's'):
        return True
    
def play():
    print("Rock, Paper, Scissors!")

    user = input("r for Rock, p for Paper, s for Scissors.\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "TIE!!"
    
    if isWin(user, computer):
        return f"You win! The computer chooses '{computer}'."
    
    return f"You lose! The computer choose '{computer}'."

print(play())