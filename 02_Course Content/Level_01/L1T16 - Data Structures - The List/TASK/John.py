"""L1T16 - Data Structures - The List - Task 2"""
# Resubmission - I completely misread the instruction. My apologies.
# Updated and renamed the saved names variable to include both the correct
# And incorrect names then used the .pop(index) to removed the last name as
# well as removing the redundant if block. Thanks for pointing that out.

# User input
user_input = input("Enter your name: ").upper()  # Force to upper()
user_entries = []  # List to store all string, correct & incorrect

while user_input != "JOHN":  # Condition False
    user_entries.append(user_input)  # Append user entry to list as string in
    # at the end.
    user_input = input("Enter your name: ").upper()  # repeat user input
else:  # Condition True
    user_entries.append(user_input)  # Add the user entry to the list at the
    #  end
    user_entries.pop(-1)  # LIst method to remove the last element in the list
    print("Incorrect Names:", " ".join(user_entries).title())  # Print output
