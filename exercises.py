# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Prompt the user to enter a letter
    letter = input("Please enter a letter (a-z or A-Z): ").strip() # Remove leading/trailing whitespaces

    # Check if the input is a single alphabetical character
    if len(letter) == 1 and letter.isalpha(): # Check if the input is a single alphabetical character
        # Convert the letter to lowercase for easier comparison 
        letter_lower = letter.lower()

        # Check if the letter is a vowel
        if letter_lower in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        # Handle invalid input
        print("Invalid input. Please enter a single alphabetical letter.")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    try:
        # Prompt the user to input their age
        age = int(input("Please enter your age: ").strip()) #can use a try except block to handle invalid input in python

        # Validate the input to ensure the age is not negative
        if age < 0:
            print("Invalid input. Age cannot be negative.")
        else:
            # Set the minimum voting age
            voting_age = 18

            # Check if the user is eligible to vote
            if age >= voting_age:
                print("You are eligible to vote!")
            else:
                print("You are not old enough to vote.")
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Invalid input. Please enter a valid number.")

# Call the function
check_voting_eligibility()



