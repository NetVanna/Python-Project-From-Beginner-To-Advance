import random
import string

# Function to generate a random password
# Parameters:
# - min_length: minimum required password length
# - numbers: include numbers if True
# - special_characters: include special characters if True
def generate_password(min_length, numbers=True, special_characters=True):

    # All uppercase and lowercase letters (A-Z, a-z)
    letters = string.ascii_letters

    # Digits 0-9
    digits = string.digits

    # Special characters such as !@#$%^&*
    special = string.punctuation

    # Start with letters as the available character set
    character = letters

    # Add digits if user wants numbers
    if numbers:
        character += digits

    # Add special characters if user wants them
    if special_characters:
        character += special

    # Stores the generated password
    pwd = ""

    # Controls whether password requirements are met
    meets_criteria = False

    # Track whether password contains a number
    has_number = False

    # Track whether password contains a special character
    has_special = False

    # Continue generating characters until:
    # 1. Password meets all required criteria
    # 2. Password reaches the minimum length
    while not meets_criteria or len(pwd) < min_length:

        # Randomly select one character
        new_char = random.choice(character)

        # Add selected character to password
        pwd += new_char

        # Check if selected character is a digit
        if new_char in digits:
            has_number = True

        # Check if selected character is a special character
        if new_char in special:
            has_special = True

        # Assume criteria are met
        meets_criteria = True

        # If numbers are required,
        # password must contain at least one number
        if numbers:
            meets_criteria = has_number

        # If special characters are required,
        # password must also contain at least one special character
        if special_characters:
            meets_criteria = meets_criteria and has_special

    # Return the completed password
    return pwd


# Ask user for minimum password length
min_length = int(input("Enter the minimun length: "))

# Ask if numbers should be included
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"

# Ask if special characters should be included
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

# Generate password using user preferences
pwd = generate_password(min_length, has_number, has_special)

# Display generated password
print(f"The generated password is: {pwd}")