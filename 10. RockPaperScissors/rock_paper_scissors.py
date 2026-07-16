"""
Rock Paper Scissors Game

This program allows a user to play Rock Paper Scissors
against the computer.

Rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

The game keeps track of:
- User wins
- Computer wins
- Draws

User can type:
- rock
- paper
- scissors
- q (to quit the game)
"""

import random


# -----------------------------
# Game Score Variables
# -----------------------------

# Store how many times the user wins
user_win = 0

# Store how many times the computer wins
computer_win = 0

# Store how many times the game is draw
draw_count = 0


# -----------------------------
# Game Options
# -----------------------------

# List of possible choices
options = [
    "rock",
    "paper",
    "scissors"
]


# -----------------------------
# Main Game Loop
# -----------------------------

while True:

    # Ask user to enter their choice
    user_input = input(
        "Type Rock/Paper/Scissors or Q to quit: "
    ).lower()


    # -----------------------------
    # Quit Game
    # -----------------------------

    # If user enters q, stop the loop
    if user_input == "q":
        break


    # -----------------------------
    # Validate User Input
    # -----------------------------

    # If user enters something not in options,
    # restart the loop and ask again
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue


    # -----------------------------
    # Computer Random Choice
    # -----------------------------

    # Computer randomly selects rock, paper, or scissors
    computer_pick = random.choice(options)

    print(f"Computer picked: {computer_pick}")


    # -----------------------------
    # Check Game Result
    # -----------------------------

    # Check if both players choose the same thing
    if user_input == computer_pick:

        print("It's a draw!")
        draw_count += 1


    # Check winning conditions
    elif (
        (user_input == "rock" and computer_pick == "scissors")
        or
        (user_input == "paper" and computer_pick == "rock")
        or
        (user_input == "scissors" and computer_pick == "paper")
    ):

        print("You won!")
        user_win += 1


    # If it is not a draw and user did not win,
    # then computer wins
    else:

        print("Computer won!")
        computer_win += 1



# -----------------------------
# Final Result
# -----------------------------

print("\n========== Final Score ==========")

print(f"You won: {user_win} time(s)")
print(f"Computer won: {computer_win} time(s)")
print(f"Draw: {draw_count} time(s)")

print("================================")

print("Goodbye!")