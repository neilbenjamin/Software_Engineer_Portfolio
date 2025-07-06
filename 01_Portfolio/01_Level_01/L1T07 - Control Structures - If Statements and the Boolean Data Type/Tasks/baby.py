# Pseudo solution: Ask the user to enter what year they were born.
# Save their answer in a variable and minus that value from the current
# year to a new variable. 
# Create a variable to hold the YTrue Boolean. Assign the condition of the
# deduced age to either True or False and print the appropriate response.

# Code

# input
user_age = int(input("What year were you born? "))
current_age = 2025 - user_age

# Boolean
old_enough = True

# Conditions & response block
if (current_age < 18): # if
    old_enough = False 
    print("You're not old enough")

elif (old_enough): # else if which equates to True
    print("You're old enough")
