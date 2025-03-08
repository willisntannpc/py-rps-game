from ui import display_welcome_message, get_user_choice
from game_logic import play_round
from scores import load_leaderboard, save_leaderboard, update_leaderboard

def main():
    display_welcome_message()
    leaderboard = load_leaderboard()
    user_wins = 0
    computer_wins = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == "q":
            break

        result = play_round(user_choice)
        if result == "user":
            user_wins += 1
        elif result == "computer":
            computer_wins += 1

        print(f"Score: You {user_wins} - Computer {computer_wins}\n")

    print("\nFinal Scores:")
    print(f"You: {user_wins} wins")
    print(f"Computer: {computer_wins} wins")

    leaderboard = update_leaderboard(leaderboard, user_wins, computer_wins)
    save_leaderboard(leaderboard)
    print("\nLeaderboard updated. Goodbye!")

if __name__ == "__main__":
    main()