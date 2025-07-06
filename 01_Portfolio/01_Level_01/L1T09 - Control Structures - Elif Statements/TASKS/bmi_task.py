"""
L1T09 - elif control statements and conditionals - Task 2
"""

user_weight = float(input("What is your weight in kilograms? "))
user_height = float(input("What is your height in meters? "))
bmi = user_weight / ((user_height) * (user_height))

if bmi >= 30:
    status = "Obese"
    print(f"Your BMI is {bmi:,.2f} and you are {status}.")
elif bmi >=25 and bmi < 30:
    status = "Overweight"
    print(f"Your BMI is {bmi:,.2f} and you are {status}.")
elif bmi >= 18.5 and bmi <25:
    status = "Normal"
    print(f"Your BMI is {bmi:,.2f} and you are {status}.")
elif bmi < 18.5:
    status = "Underweight"
    print(f"Your BMI is {bmi:,.2f} and you are {status}.")
