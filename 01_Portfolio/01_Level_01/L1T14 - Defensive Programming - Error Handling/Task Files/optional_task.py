"""L1T14 - Defensive Programming - Task 3_Optional."""

"""""
# Runtime error  Uncomment the correct code and comment out the errors.
# The code below will execute a runtime error as the input is not cast to an
# integer data type and therefore won't work correctly. 

user_input = input("Guess the mystery number between 1 and ten")

#The code below is done correctly. 
# user_input = int(input("Guess the mystery number between 1 and ten. "))

mystery_num = 7

# while user_input != 7 # Syntax error. Missing : Correct version below.
while user_input != 7: 
print("Incorrect. Guess again and enter a new number \n") # Syntax. Bad
                                                # Indentation. Correct version
                                                # Below.
    # print("Incorrect. Guess again and enter a new number \n")

    user_input = int(input("Guess the mystery number between 1 and ten. "))
    if user_input == 8: # Logical error. The correct answer should be 7
    # if user_input == 7: # Correct conditional 
        print(f"Well done, the mystery number is {mystery_num}.")
        break"""
