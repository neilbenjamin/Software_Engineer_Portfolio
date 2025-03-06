"""L1T13 - Control Structures - For Loop."""

# Commented out the len function to help with the counting.
# Assistance with negative indexing string splicing and indexing
# https://www.geeksforgeeks.org/string-slicing-in-python/
# https://www.freecodecamp.org/news/slicing-and-indexing-in-python/,
# https://www.linode.com/docs/guides/how-to-slice-and-index-strings-in-python/

star = ""
length = len(star)
for i in range(0,12):
    if i >= 0 and i < 6:
        star += "*"
        print(star)
        # length = len(star)
        # print(length)
    elif i > 5 and i < 11:
        star = star[0:-1]
        print(star)
        # length = len(star)
        # print(length)
