# Pseudo Solution

# Ask the user to enter the name of their favourite restaurant and save it
# to a variable
# Ask the user to enter their favourite number (cast to integer) and store 
# this as a variable.
# Print both user inputs
# Cast the string variable to an integer variable and observe.

# Code

string_fav = input("What is the name of your favourite restaurant? ")
int_fave = int(input("Enter your favourite number. "))

# Print inputs

# print("Be Careful!") 
print(string_fav)
print(int_fave)

# Cast string to Int

print(int(string_fav))

# Observation is that there are no numbers entered as a string for the cast 
# function to convert a string number to an integer number. If the user entered
# "6" as their favourite restaurant, the cast function would convert the "6" 
# string data-type to a 6 integer data type. 