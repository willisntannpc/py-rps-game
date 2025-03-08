import random

options = ["rock", "paper", "scissors"]

def play_round(user_choice):
    computer_choice = random.choice(options)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        return "user"
    else:
        print("Computer wins this round!")
        return "computer"