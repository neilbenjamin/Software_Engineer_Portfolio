"""L1T14 - Defensive Programming - Task 3."""
print("Write a sum to total 5\n")

sum1 = "1"
sum2 = "2"
sum3 = "2"

print("This still runs, but outputs the incorrect logic")
addition = sum1 + sum2 + sum3
print(addition)
print("\n")

# The correct requirement was actually.
print("This outputs the correct logic")
addition = int(sum1) + int(sum2) + int(sum3)
print(addition)
