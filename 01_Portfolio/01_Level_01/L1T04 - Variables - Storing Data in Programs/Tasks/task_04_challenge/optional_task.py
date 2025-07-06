# This was a little tricky as I initially just swapped them but num2's value was already changed so it became the same as num1 after the swap.
# I found the solution on Google linked to unstop which required another temporary variable to store the original value of num1
# https://unstop.com/blog/swapping-two-variables-in-python#:~:text=Swapping%20Two%20Variables%20Using%20A,first%20original%20variable%20to%20it.


num1=input("Choose a number")
num2=input("Choose another number")
print()
print("Original user inputs")
print(num1)
print(num2)
print()

temp=num1
num1=num2
num2=temp

print("After swap")
print(num1)
print(num2)

