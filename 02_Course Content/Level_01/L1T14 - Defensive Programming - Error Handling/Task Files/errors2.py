"""L1T14 - Defensive Programming - Task 2."""

# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion" # Runtime error. Lion value is not previously defined 
                # and this needs to be a string. 
                #Syntax error. The string needs quotation marks and the 
                # capitalized L needs to be small-capped. 
animal_type = "cub"
number_of_teeth = 16

full_spec = f"""
This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth
""" # Runtime and logical errors. The string 
    # interpolation format is missing and the values are
    # incorrectly placed. Correct the order to print 
    # the correct output.  Syntax error. The string is also too long.

print(full_spec) # Syntax Error. Missing print parenthesis. 
