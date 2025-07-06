# In this challenge we wil use the built-in replace, upper and negative indexing methods in python by first assigning them to new
# variable with the relevant methods included, and again directly with the methods included in the print function. 

#Task 2 - Assigned to new variables

sentence="The!quick!brown!fox!jumps!over!the!lazy!dog."

# Task 2.1

print("ASSIGNED TO NEW NEW VARIABLES \n")

no_exclamation=sentence.replace("!", " ")
print(no_exclamation)
print()

# Task 2.2

loud_sentence=sentence.upper()
print(loud_sentence)
print()

# Task 2.3

backwards_sentence=sentence[::-1]
print(backwards_sentence)
print()

print()
# Task 2 - Assigned directly to print

print("PRINTED OUT DIRECTLY \n")

# Task 2.1
print(sentence.replace("!", " "))
print()

# Task 2.2
print(sentence.upper())
print()

# Task 2.3
print(sentence[::-1])
print()