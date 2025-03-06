# Pseudo code
# Dividing the user input with a modulus and having a result of 1 indicates an
# odd number wheres 0 equates to an even number. Create and define
# boolean value and evaluate condition to user input and output relevent 
# response.


user_input = int(input("Please enter an Integer "))

is_even = True

if(user_input % 2 == 1):
 is_even = False
 print(f"{user_input} is an odd number")
else:
  is_even
  print(f"{user_input} is even.")
