""" Task 26 - Challenging task. Got quite a bit of assistance from the original
Pyth0n PEP8 docs as well as geeksforgeeks, stack-overflow and w3schools.
"""
import operator
num_container = []
doc_list = []


def display_archive() -> str:
    """Read, clean, append and display txt data.
    Args:
    Returns:
        string: cleaned data from txt file
    """
    try:
        with open("equations.txt", "r", encoding='utf-8') as sum_doc:
            raw_data = sum_doc.readlines()
            for i in raw_data:
                cleaned = i.strip().split(", ")
                doc_list.append(cleaned)
                for col in doc_list:
                    display = "".join(col)
                print(display)
                return display
    except Exception:
        print("""
No calculations have been added yet. Please add a calculation and try again.
""")


def calculate(num1: int, user: int, num2: int) -> str:
    """_Calculate user input, append to global variable, process variable and
    write data in str format to external txt file.
    Args:
        num1 (_int_): _user int input.
        user (_str_): _user operator input.
        num2 (_int_): _user int input.

    Returns:
        _str_: _string to txt file.
    """
    try:
        if user == "+":
            result = operator.add(num1, num2)
        elif user == "*":
            result = operator.mul(num1, num2)
        elif user == "-":
            result = operator.sub(num1, num2)
        elif user == "/":
            result = operator.truediv(num1, num2)
        num_container.append(result)
        all_to_string = " ".join(map(str, num_container))
        with open("equations.txt", "a+", encoding='utf-8') as sum_doc:
            sum_doc.write(f"{all_to_string}\n")
        num_container.clear()
        return all_to_string
    except ZeroDivisionError:
        print("\nYou can not divide 0 by 0. Please try again.")
        num_container.clear()


def start():
    """_Validate and check user inputs.
    """
    while True:
        try:
            num1 = float(input("Enter first number: \n"))
            if float.is_integer(num1):
                num1 = int(num1)
            else:
                num1 = num1
            num_container.append(num1)
            break
        except ValueError:
            print("Please enter a number.")
    while True:
        op_func = str(input("Enter an operation: + - * /\n"))
        if (op_func == "+" or op_func == "-" or
                op_func == "*" or op_func == "/"):
            num_container.append(op_func)
            break
        else:
            print("Please enter the correct operator function.")
    while True:
        try:
            num2 = float(input("Enter second number: \n"))
            if float.is_integer(num2):
                num2 = int(num2)
            else:
                num2 = num2
            num_container.append(f"{num2} =")
            break
        except Exception:
            print("Please enter a number.")
    calculate(num1, op_func, num2)
    # print(f"\nYou calculation output is: {calculator}")


def main(display_archive, start):
    while True:
        user_menu = input("""
Please enter A or B to continue:

A : Do a new calculation
B : View Past Calculations
E : Exit

""").lower()
        if user_menu == "a":
            start()
        elif user_menu == "b":
            display_archive()
        elif user_menu == "e":
            print("Cheers")
            exit()
        else:
            print(f"{user_menu} is not a viable option.")


main(display_archive, start)
