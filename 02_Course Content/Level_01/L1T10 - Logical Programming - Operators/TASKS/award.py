"""
L1T10 - Logical Programming - Operators - Task 1
"""
# Just be aware that the award criteria are not realistic and that a full
# triathlon will be in excess of 14 hours. 

swim_time = int(input("Enter the number on minutes it took to complete your"
                      " swim. "))
cycle_time = int(input("Enter the number of minutes it took to complete"
                 " your cycle. "))
run_time = int(input("Enter the number of minutes it took to complete "
                     "your run. "))

total_time = swim_time + cycle_time + run_time

full_colours = "you are awarded full provincial colours!"
half_colours = " you are awarded half provincial colours."
provincial_scroll = "you are awarded a provincial scroll."
no_award = "you did not manage to win an award of any sorts."

# Conditionals

if total_time <= 100:
    print(f"Your total time was {total_time} minutes and {full_colours}")
elif total_time > 100 and total_time <= 105:
    print(f"Your total time was {total_time} minutes and {half_colours}")
elif total_time > 105 and total_time <= 110:
    print(f"Your total time was {total_time} minutes and {provincial_scroll}")
else:
    print(f"Your total time was {total_time} minutes and {no_award}")
