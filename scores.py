import json
import os

LEADERBOARD_FILE = "data/leaderboard.json"

def load_leaderboard():
    # Create the data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # If the leaderboard file doesn't exist, create it with default values
    if not os.path.exists(LEADERBOARD_FILE):
        default_leaderboard = {"user": 0, "computer": 0}
        with open(LEADERBOARD_FILE, "w") as file:
            json.dump(default_leaderboard, file, indent=4)
        return default_leaderboard
    
    # Load the leaderboard from the file
    with open(LEADERBOARD_FILE, "r") as file:
        return json.load(file)

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

def update_leaderboard(leaderboard, user_wins, computer_wins):
    leaderboard["user"] += user_wins
    leaderboard["computer"] += computer_wins
    return leaderboard