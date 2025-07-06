""" Task 21 - Programming with Built-in Functions - Task 01"""
# I imported the statistics module. The math module has been previously
# installed globally.
import statistics
# containers for data
num_list = []
new_list = []
sum_total = []
counter = 1
# While loop for entering the numbers with conditional set to 11 and a counter
# to help check number of inputs. User float input validation courtesy of
# https://docs.python.org/2/tutorial/errors.html#handling-exceptions
while True:
    try:
        user_input = float(input("Enter 11 numbers,whole or decimal : "))
        num_list.append(user_input)
        print(f"Entries : {counter}")
        counter += 1
    except ValueError:
        print("Enter a number")
    if len(num_list) == 11:
        break
# All method assistance courtesy of W3schools and GeeksForGeeks
sum_total = sum(num_list)
max_num = max(num_list)
max_index = num_list.index(max_num)
min_num = min(num_list)
min_index = num_list.index(min_num)
average = statistics.mean(num_list)
rounded = round(average, 2)
median = statistics.median(num_list)
print(f"\nThe total is : {sum_total}\n")
print(f"The max number is: {max_num} at index position : {max_index}\n")
print(f"The min number is: {min_num} at index position : {min_index}\n")
print(f"The average number is: {rounded}\n")
print(f"The median number is: {median}\n")
