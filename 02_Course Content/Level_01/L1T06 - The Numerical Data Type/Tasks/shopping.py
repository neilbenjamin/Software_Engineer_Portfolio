# Pseudo code solution
# Ask the user to enter the names of 3 products and store each value in a 
# variable. 
# Ask ask the user the price for each product which needs to be a 2 decimal
# float value and store these values in there own variables.
# Add the totals and divide by the quantity of products for the average using 
# the round(number, 2) to round the answer to a floating point with a 2
# decimal value. 
# Using the format method, print the answers back to the user.

# Task 2

# Ask for product choice
product1 = input("Enter your first product. ")
product2 = input("Enter your second product. ")
product3 = input("Enter your second product. ")

# Enter float values
product1_value = float(input("Enter your 2 decimal value price" 
                             "for the first product. "))
product2_value = float(input("Enter your 2 decimal value price" 
                             "for the second product. "))
product3_value = float(input("Enter your 2 decimal value price" 
                             "for the third product. "))

# Testing outputs - Commented out
# print(product1_value)
# print(product2_value)
# print(product3_value)

# sum of value inputs
total_value = product1_value + product2_value + product3_value

# Rounding the total
rounded_value = round(total_value, 2)

# testing sum value - commented out
# print(total_value)

# Determine average
average_cost = rounded_value / 3

# Testing average - Commented out
# print(round(average_cost, 2))

# Final output

print(f"The Total of {product1}, {product2}, {product3} is R{total_value} and" 
      f"the average price of the items is R {round(average_cost, 2)}")

# end