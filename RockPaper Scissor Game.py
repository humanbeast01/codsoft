import random

def play_game():
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)

    user = input("Enter your choice (rock, paper, scissor): ").lower()
    while user not in choices:
        user = input("Invalid input! Enter your choice (rock, paper, scissor): ").lower()

    print(f"\nComputer chose {computer}")

    if user == computer:
        return "It's a tie!"
    if (user == "rock" and computer == "scissor") or (user == "scissor" and computer == "paper") or (user == "paper" and computer == "rock"):
        return "You win!"
    return "You lose!"

print(play_game())
