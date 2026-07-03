"""
Computer Quiz Program
---------------------
This program asks the user if they want to play a computer-related quiz.
The quiz contains four questions about common computer hardware terms.

Scoring:
- score: Number of correct answers.
- unscore: Number of incorrect answers.
"""

# Display a welcome message
print("Welcome to my computer quiz!")

# Ask the user if they want to play
playing = input("Do you want to play? ")

# If the user does not answer "yes", exit the program
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

# Initialize score counters
score = 0      # Stores the number of correct answers
unscore = 0    # Stores the number of incorrect answers

# -----------------------------
# Question 1
# -----------------------------
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    unscore += 1

# -----------------------------
# Question 2
# -----------------------------
answer = input("What does GPU stand for? ")

if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    unscore += 1

# -----------------------------
# Question 3
# -----------------------------
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    unscore += 1

# -----------------------------
# Question 4
# -----------------------------
answer = input("What does PSU stand for? ")

if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    unscore += 1

# -----------------------------
# Display Final Results
# -----------------------------
print(f"\nYou got {score} questions correct!")
print(f"You got {unscore} questions incorrect!")

# Calculate and display the percentage score
total_questions = score + unscore
percentage = (score / total_questions) * 100

print(f"Your score is {percentage:.2f}%")