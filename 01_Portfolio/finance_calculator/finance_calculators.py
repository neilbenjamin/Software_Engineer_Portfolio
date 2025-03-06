"""
L1T11 - CAPSTONE PROJECT 1 - FINANCE CALCULATOR
"""

import math

# User intro & Input

print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on your home loan      
""")

user_input = input("Enter either 'investment' or 'bond' from the menu above "
                    "to proceed: ").upper()

# Error return
# if user_input != "INVESTMENT" and user_input != "BOND":
#     print("Please ensure you enter only 'investment' or 'bond'.")

# Node 1
# Branch 1 - Investment Output
if user_input == ("INVESTMENT"):
    deposit_amount = float(input("How much are you depositing? "))
    interest_rate = float(input("What is the interest rate? Please enter only "
                                "a number and not the '%' sign. "))
    num_years = int(input("How many years do you plan on investing? "))
    interest_type = input("Select either Compound interest, or\n"
                          "Simple interest. ").upper()
    # Node 1.1
    interest = interest_type
    if interest == "SIMPLE":
        # Values
        r = interest_rate / 100        
        P = deposit_amount
        t = num_years
        # computation
        A = P *(1 + r*t)
        total_interest = A
        print(f"""
              Your initial deposit of {P:,.2f};
              with an interest rate of: {r};
              Invested for {t:.2f} years with {interest} interest will 
              total R {total_interest:,.2f}
            """)
    elif interest == "COMPOUND":
        # Values
        r = interest_rate / 100        
        P = deposit_amount
        t = num_years
        # computation
        A = P * math.pow((1+r),t)
        total_interest = A
        print(f"""
              Your initial deposit of {P:,.2f};
              with an interest rate of: {r};
              Invested for {t} years with {interest} interest will 
              total R {total_interest:,.2f}
            """)
    else:
        print("Please only choose either 'Compound' or 'Simple'")

#  Node 2
#  Bond Output
elif user_input == "BOND":
    present_value = int(input("What is the present value of your home? "))
    interest_rate = float(input("What is the interest rate? Please enter only "
                                "a number and not the '%' sign. "))
    num_months = int(input("How many months will you repay your bond? "))
    # Values
    P = present_value
    i = interest_rate / 100 / 12
    n = num_months
    # computation
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print(f"""
              Your initial value of your home is {P:,.2f};
              with a monthly interest rate of: {i:,.2f};
              Paid over {n} months will cost R {repayment:,.2f} per month.
            """)
# Error return
else:
    print("Please ensure you enter only 'investment' or 'bond'.")

# Assistance from Google to double check equation outputs
