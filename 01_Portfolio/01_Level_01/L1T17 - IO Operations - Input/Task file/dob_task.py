"""L1T17 - IO Operations - Input - Task"""
# Access the external txt file to import the data
# Variable 'file' uses the with/as short and then saves the doc data as 'file'.
# Declare new variable 'file-data' value as individual lists segmented by using
# the readlines() method on the file var. Intrinsically it reads the data in
# file and segments eah new line into an element inside a list.
with open("L1T17 - IO Operations - Input/Task file/DOB.txt", "r") as file:
    file_data = file.readlines()

# Instead of reassigning the string var on each loop iteration,
# 'name_year = ""', I'm going to instead use 2 list containers to catch the
# appended loop items;

names = []
dates = []
print("This is the file data")
print(file_data)

# Loop through the extracted data to remove white spaces and to segment the
# data into elements segmented by any spaces.

for line in file_data:
    # Remove the \n and other whitespaces to clean the data as it loops;
    cleaned_data = line.strip().split()
    # Append the desired element indexes to the relevant container using the
    # index splicing technique. First we will segment each loop of the cleaned
    # data to slice elements from 0 up to -3 leaving the first two elements.
    # The nice thing about using lists is that we can mutate and directly
    # assign value without having to reassign the variable each time. This was
    # a little because I initially forgot to append and ended up with the last
    # element of the loop each time. Confusing.
    names.append(cleaned_data[:-3])
    # and the slicing for the DOB would be to keep the elements on the right
    # from index -3 to the end, ignoring any elements lower than -3 i.e. 0,1,2
    # 3,4,5 & 6. GeeksForGeeks helped me with this a lot.
    dates.append(cleaned_data[-3:])
    # This now essentially gives us 2 lists, one with names and one with dates
    # of birth. However, the lists are now INSIDE of a list, which again
    # caused brain-drain because I wasn't able to ''.join(var) them, citing
    # error expecting a string but found a list (isn't that what join is
    # supposed to do, turn lists into strings...?). Anyway, I eventually tried
    # looping through the list to extract the list and this happened:
print("\nNAMES\n")
for name in names:
    print(" ".join(name))

print("\nDATES\n")
for dob in dates:
    print(" ".join(dob))
    # Certainly much better than the previous method.
