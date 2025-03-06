"""
L1T11 - While Loop
"""

num_total = 0
loop_qty = 0
user_entry = int(input("Enter a number (Tip: -1 to exit) "))

while user_entry != -1:
    loop_qty += 1
    # print(loop_qty)
    num_total += user_entry
    # print(num_total)
    user_entry = int(input("Enter a number (Tip: -1 to exit) "))
if user_entry == -1:
    print("The average of the incorrect numbers entered "
          f"is: {num_total / loop_qty: .2f}")
