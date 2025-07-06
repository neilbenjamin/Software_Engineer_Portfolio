# Pseudo solution
# Add a prompt to as the user to enter at least two names.
# Use string validation to determine the amount of characters entered into
# to output the correct response as well as checking for empty spaces that 
# indicates the end of one name and the beginning of the next. Output the 
# correct responses to the user.

# Conditional statements    

# Prompt
user_input = input("Please enter a your full name. ")

# variables
string_len = len(user_input) # Checks  string char length
space_char = user_input.find(" ") # Checks for empty space index
number_of_spaces = user_input.count(" ") # Checks for empty space total
decrement_string = string_len - 1 # Assist with logic for True

# Checks - Commented out
# print(f"The length is: {string_len} long")
# print(f"The first space is at index: {space_char}")
# print(f"The number of space in the string: {number_of_spaces}")
# print(f"The decremented1 string is: {decrement_string}")

# no input
if (user_input == ""):
    print("You haven’t entered anything. Please enter your full name.")

#smaller than 4
if (string_len == 1 or string_len == 2 or string_len == 3):
    print("You have entered less than 4 characters. Please make sure that "
          "you have entered your name and surname.")     

# single word larger than 3 chars and no space
if (string_len > 3 and space_char == -1):
    print("Please enter another name preceded with a space")



if (string_len >= 4 and string_len < 25 and number_of_spaces):
    # Check if just one word and one space without 2nd word.
    if (decrement_string == space_char):
     print("Please enter a second name and not just a name with a space")
    # Check char after space - 2nd word True
    else:
     print("Thanks for entering your name.") 


if (string_len > 25):
    print("You have entered more than 25 characters. Please make sure that "
          "you have only entered your full name.")         

  
