"""
L1T09 - elif control statements and conditionals  -Task 1
"""

user_input = int(input("What is your age? "))

if user_input >= 18:
    print("You're old enough!")
elif user_input >= 16 and user_input < 18:
    print("Almost there.")
else:
    print("You're just too young!")
