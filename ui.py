def display_welcome_message():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print("- Type 'rock', 'paper', or 'scissors' to play.")
    print("- Type 'q' to quit.")
    print("- First to 3 wins becomes the champion!\n")

def get_user_choice():
    while True:
        user_input = input("Your choice (rock/paper/scissors/q to quit): ").lower()
        if user_input in ["rock", "paper", "scissors", "q"]:
            return user_input
        else:
            print("Invalid choice. Please try again.")