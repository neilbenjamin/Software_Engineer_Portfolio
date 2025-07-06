"""L1T08 - Control Structures - Else Statements - Task 01."""

# Distance
print("")
distance = float(input("What is the courier distance in kilometers? "))
print("")
print('FREIGHT CALCULATOR')
# Calculator
freight_input = input("Select A for air freight at R0.36 p/km, or\n"
                      "Select B for road freight at R0.25 p/km. ").upper()

print("")
# Insurance
print("INSURANCE")
insurance_input = input("Select A for the Full Insurance package at R50.00 "
                        "per km, or \nSelect B for the limited Insurance "
                        "package at R25.00 p/km?. ").upper() 
print("")

# Gift variable
print("GIFT")
gift_input = input("Select A for the Gift Cover package at R15.00, or \n"
                   "Select B for no gift valued at R0.00. ").upper() 
print("")

# Priority variable
print("PRIORITY")
priority_input = input("Select A for the priority deliver at R100.00, or \n"
                       "Select B for standard delivery valued at "
                       "R20.00.").upper() 
print("")

# Parcel variable
print("PARCEL")
parcel_input = input("Select A for the postage sleeve at R100.00 base fee "
                     "or \nSelect B for postage box valued at"
                     "R150.00. base. ").upper() 
print("")

# Freight

if freight_input == "A":
    freight_value = distance * .36
    print(f"Your freight will cost R {freight_value: .2f}")
else:
    if freight_input == "B":
        freight_value = distance * .25
        print(f"Your freight will cost R {freight_value: .2f}")

# Insurance
if insurance_input == "A":
    insurance_value = 50.00
    print(f"Your insurance value is R{insurance_value: .2f}")

else:
    insurance_value = 25.00
    print(f"Your insurance value is R{insurance_value: .2f}")

# Gift Cards
if gift_input == "A":
    gift_value = 15.00
    print(f"Your gift value is R{gift_value: .2f}")
else:
    gift_value = 0.00
    print(f"Your gift value is R{gift_value: .2f}")

# Priority Value
if priority_input == "A":
    priority_value = 100.00
    print(f"Your priority selection is R{priority_value: .2f}")
else:
    priority_value = 20.00
    print(f"Your priority selection is R{priority_value: .2f}")

# Priority Value
if parcel_input == "A":
    parcel_value = 100.00
    print(f"Your parcel selection is R{parcel_value: .2f}")
else:
    parcel_value = 150.00
    print(f"Your parcel selection is R{parcel_value: .2f}")

total_cost = float(freight_value + insurance_value + gift_value + priority_value +
                   parcel_value )
print()
print(f"The total cost is: R{total_cost: .2f}")
