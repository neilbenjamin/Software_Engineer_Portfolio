"""L1T15 - String Handling - Task"""

# Task A - Alternate Char Case
# Task B - Alternate Case for each word.

# Task A Variables
word = "Mary had a little lamb "
new_word = ""

# Task B variables
split_word = word.split()
flipped_caps = ""
filler = " "
i = 0

# Task A - Relatively simply looping over the string and determining the
# even number and manipulating the index of i for each specific iteration.
# Assigning i as the counter to loop through each char of the string 'word
# It checks each index iteration to assess if it's even or odd and then based
# on True or False it will either upper() or lower() the char on that inde
# iteration and then assign the results thereof to the empty variable,
# new_word which in turns get's reassigned a new value upon each iteration.

for i in range(0, len(word)):
    if i % 2 == 0:
        new_word += word[i].upper()
    else:
        new_word += word[i].lower()

# Prints the solution for Task A
print("")
print("Challenge 1")
print(f"{new_word}\n")

# Task B - Similar concept to A, but first we need to split the words into 
# their owb containers, or boxes, separated by "" and , Each "", within the 
# list [] represents an item, hence the 5 items presented when we apply the 
# ,split() method to the word. This then creates a list we can now also loop 
# through to manipulate even and odd numbers based on the index position. This
# Correctly capitalizes ever second index. I'm not quite sure how to add the 
# " ".join(variable) method to this to add a space between each space and 
# instead hardcoded a space variable into each iteration to reach the same 
# output. 

print("")
print("Challenge 2")
print("Split word creates a list")
print(split_word)
print("\n")

print("Loop to capitalize every 2nd word")

for i in range(len(split_word)):
    if i % 2 == 0:
        flipped_caps += filler + split_word[i].upper()
     
    elif i % 2 != 0:
        flipped_caps += filler + split_word[i].lower()

# Removed the whitespace added by the blank space on iteration no, 1
print(f"{flipped_caps.strip()}\n")
