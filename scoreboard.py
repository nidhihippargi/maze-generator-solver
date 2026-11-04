
import json
import os

SCOREBOARD_FILE = "scoreboard.json"


def calculate_score(moves, elapsed_time):
    """Calculate score based on moves and completion time."""

    score = 1000 - (moves * 5) - (elapsed_time * 2)

    return max(0, int(score))


def save_score(name, moves, elapsed_time, score):
    """Save completed game details to a JSON file."""

    # Read existing scores safely
    try:
        with open(SCOREBOARD_FILE, "r") as file:
            scores = json.load(file)

        if not isinstance(scores, list):
            scores = []

    except (json.JSONDecodeError, FileNotFoundError, OSError):
        scores = []

    result = {
        "name": name,
        "moves": moves,
        "time": round(elapsed_time, 2),
        "score": score
    }

    scores.append(result)

    scores.sort(key=lambda item: item["score"], reverse=True)

    # Save updated scores
    with open(SCOREBOARD_FILE, "w") as file:
        json.dump(scores, file, indent=4)


def display_scoreboard():
    """Display all saved scores."""

    try:
        with open(SCOREBOARD_FILE, "r") as file:
            scores = json.load(file)

        if not isinstance(scores, list):
            scores = []

    except (json.JSONDecodeError, FileNotFoundError, OSError):
        scores = []

    if not scores:
        print("\nNo scores recorded yet.")
        return

    print("\n========== SCOREBOARD ==========")

    for index, result in enumerate(scores, start=1):
        print(
            f"{index}. {result['name']} | "
            f"Moves: {result['moves']} | "
            f"Time: {result['time']}s | "
            f"Score: {result['score']}"
        )

    print("===============================")

