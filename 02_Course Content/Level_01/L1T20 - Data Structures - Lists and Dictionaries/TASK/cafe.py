""" Task 20 - Data Structures - Lists and Dictionaries"""
menu = ["cake", "coffee", "croissant", "cannabis"]
# Stock_quantity
stock = {
    "cake": 25,
    "coffee": 150,
    "croissant": 20,
    "cannabis": 60
}
# Stock_price
price = {
    "cake": 75,
    "coffee": 35,
    "croissant": 40,
    "cannabis": 80
}
# Total_values - Two methods
# String concatenation using the loop to add and reassign on each loop.
sum_check = 0
# Using the list append() method and sum() to add the totals.
inventory_net = []
# Loop through items in menu. For each item in menu, use that item in each
# dictionary key in both dictionaries and multiply those values to each other,
# referencing a key with output the value of the key, and not the key itself.
for item in menu:
    calculate = stock[item] * price[item]
    # Reassign and concatenate each multiplication result to empty int variable
    # and append the same to the empty list variable.
    sum_check += calculate
    inventory_net.append(calculate)
    # Use sum() to add th totals. Courtesy of W3Schools.
    inventory_total = sum(inventory_net)
print(f"\nConcat method: The inventory total is: {sum_check}\n")
print(f"List method : The inventory total is: {inventory_total}\n")
