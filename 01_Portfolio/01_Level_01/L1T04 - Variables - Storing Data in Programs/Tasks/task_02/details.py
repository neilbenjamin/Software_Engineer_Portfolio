# We will use the input command to ask the user for a set of details which we will then store in a myriad of different variables
# and different variable types i.e. strings, integers and floats etc...
#We will use the f (format) preceding the string in the parenthesis to format the string literals {} and pull the data into the them 
# and replacing the variable name it is referring to.
# We will print all this out in a single print command.

user_name=input("What is your name?")
user_age=input("What is your age?")
user_house_number=input("what is your house number?")
user_street_name=input("What si your street name?")
print(f"This is {user_name}. He is {user_age} old and lives at house number {user_house_number} on {user_street_name} street.")

