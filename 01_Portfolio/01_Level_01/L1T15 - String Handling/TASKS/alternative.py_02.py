"""L1T15 - String Handling - Task - Take 2"""


sentence = "mary had a little lamb"
# Stripping whitespace and creating a list prior to loop.
new_list = sentence.strip().split()
# Empty list for adding to.
new_words = []

# Loop through new_list length and check for even and odd indexes.
# Create a temp variable inside each condition with correct variance.
# Append outcome to the empty list instead of reassign a new value to
# the same variable on each iteration.
for word in range(len(new_list)):  # True
    if word % 2 == 0:
        upper = new_list[word].upper()
        new_words.append(upper)
    else:  # False
        lower = new_list[word].lower()
        new_words.append(lower)
# Print list back into a string with the .join() method.
print(" ".join(new_words))
