# Import the random module to generate a random number
import random

# Define the minimum and maximum range for the guessing game
lowest_num = 1
highest_number = 100

# Generate a random number between lowest_num and highest_number
answer = random.randint(lowest_num, highest_number)

# Variable to count how many guesses the player makes
guesses = 0

# Controls whether the game loop continues running
is_running = True

# Display game title and instructions
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_number}")

# Main game loop
while is_running:

    # Ask the player to enter a guess
    guess = input("Enter your guess: ")

    # Check if the input contains only digits
    if guess.isdigit():

        # Convert the input string to an integer
        guess = int(guess)

        # Increment the guess counter
        guesses += 1

        # Check if the guess is outside the allowed range
        if guess < lowest_num or guess > highest_number:
            print(f"That number {guess} is out of the range")
            print(f"Please Select a number between {lowest_num} and {highest_number}")

        # Check if the guess is lower than the answer
        elif guess < answer:
            print(f"This number {guess} too low! Try again!")

        # Check if the guess is higher than the answer
        elif guess > answer:
            print(f"This number {guess} too high! Try again!")

        # Player guessed correctly
        else:
            print(f"CORRECT! The answer was {answer}")

            # Display the number of guesses taken
            print(f"Number of guesses: {guesses}")

            # Ask the player if they want to play again
            play_again = input("Do you want to play again [y/n]: ")

            # Stop the game if the player chooses 'n' or 'N'
            if play_again == "N" or play_again == "n":
                is_running = False

    # Handle invalid input (non-numeric values)
    else:
        print("Invalid guess")
        print(f"Please Select a number between {lowest_num} and {highest_number}")