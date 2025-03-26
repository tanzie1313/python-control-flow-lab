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
        letter_lower = letter.lower() #maybe  not needed....for comparison

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

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Prompt the user to input the dog's age
    dog_age = int(input("Input a dog's age: ").strip())

    # Calculate the dog's age in dog years
    if dog_age == 1:
        dog_years = 10
    elif dog_age == 2: #if-elif-else block
        dog_years = 20
    else:
        dog_years = 20 + (dog_age - 2) * 7

    # Print the calculated age
    print(f"The dog's age in dog years is {dog_years}.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.



def weather_advice():
    # Prompt the user for weather conditions
    cold_input = input("Is it cold? (yes/no): ").strip().lower()
    raining_input = input("Is it raining? (yes/no): ").strip().lower() #whitespace removed/ convert to lowercase

    # Determine weather conditions based on user input
    is_cold = cold_input == "yes"
    is_raining = raining_input == "yes"

    # Provide clothing advice based on conditions using logical operators
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    elif not is_cold and not is_raining:
        print("Wear light clothing.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Define the season ranges as tuples (start_month, start_day, end_month, end_day, season)
    seasons = [
        ("Dec", 21, "Mar", 19, "Winter"),
        ("Mar", 20, "Jun", 20, "Spring"),
        ("Jun", 21, "Sep", 21, "Summer"),
        ("Sep", 22, "Dec", 20, "Fall")
    ]

    # Prompt the user to enter the month and day
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize() #strip and capitalize
    day = int(input("Enter the day of the month: ").strip())

    # Validate the month input
    if month not in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
        print("Invalid month entered. Please use the format 'Jan - Dec'.")
        return

    # Validate the day input
    if day < 1 or day > 31:
        print("Invalid day entered. Please enter a valid day of the month.")
        return

    # Find the corresponding season based on the date
    for start_month, start_day, end_month, end_day, season in seasons:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            print(f"{month} {day} is in {season}.") 
            return

    # Handle cases where the date does not fall within the defined seasons
    print("The entered date does not correspond to a season.")
# Call the function
determine_season()







