"""L1T14 - Defensive Programming - Task 1."""

# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Syntax Error - Added Parenthesis
print("\n") # Syntax Error - Bad Indentation. Moved to the left

# Variables declaring the user's age, casting the str to an int, and 
# printing the result

age_str = "24" # Syntax Error - bad Indentation corrected and made the S and s
               # to keep the variable all small caps.
               # Runtime error - removed the 'years old' as this string meeds
               # to be cast to an integer and the "years old" is already 
               # hardcoded in the print
age = int(age_str) # Syntax error - Bad Indentation 
print("I'm" + " " + str(age) + " " + "years old.") # Syntax error - 
                                                   #Bad Indentation and poor
                                                   #grammar. Added spaces.

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # Syntax error - Bad Indentation and incorrect math which
                     # will result in the incorrect output and produce a 
                     # logical error, so I corrected the math. 
total_years = age + years_from_now

print("The total number of years:" + f" {total_years}") # Syntax errors. 
                              # Missing print parenthesis. 
                              # Runtime errors with missing f-string literal 
                              # interpolation for the second concatenated 
                              # string. Additional syntax error with the wrong 
                              # variable name stated. 

# Variable to calculate the total amount of months from the total amount of years 
# and printing the result
total_months = total_years * 12 # Runtime error. Incorrect variable assignment
                                # from a variable that doesn't exist. 
                                # the variable to match the correct value.
print("In 3 years and 6 months, I'll be " + str(round(total_months)) + " "
      "months old.") # Syntax error with no parenthesis for the print function, 
                    # as well as a runtime error by trying to concatenate a 
                    # string with an Int value. We cast the Int to a string 
                    # and then rounded it to match the answer given to remove 
                    # the decimal values. 

#HINT, 330 months is the correct answer
