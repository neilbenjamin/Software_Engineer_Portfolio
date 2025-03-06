"""L1T08 - Control Structures - Else Statements - Task 02 Optional Task."""

sales_person = 2000.00
manager = 40.00

user_role = input("Select A if you are a manager or\n"
"Select B if you are a sales-person ").upper()

if user_role == "B":
    monthly_sales = float(input("What is your gross, monthly sales total? "))
    sales_comm = monthly_sales * 0.08
    sales_total = sales_comm + sales_person
    print(f"Your monthly wage is: R{sales_total:,.2f}")
elif user_role == "A":
    hours_worked = float(input("How many hours did you work this month? "))
    hours_total = hours_worked * manager
    print(f"Your monthly wage is: R{hours_total:,.2f}")
else:
    print("You didn't enter A or B, please try again.")
