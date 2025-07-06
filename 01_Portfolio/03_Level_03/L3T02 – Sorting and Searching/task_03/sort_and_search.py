""" L3T02 – Sorting and Searching - Task 3.
"""

sample = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# 3.1
# The enumerate function.
# Easy and quick to impliment and returns the index and value of the search.
for i, number in enumerate(sample):
    if number == 9:
        print(f"9 found at index: {i}")


# 3.2 - Insertion sort. Ref - Geeks for Geeks


def insertionSort(arr: list) -> list:
    """Takes an unordered list to be ordered.
    Args:
        arr (list): list

    Returns:
        list: Ordered numerical list from lowest to highest
    """
    n = len(arr)  # Get the length of the array
    if n <= 1:
        # If the array has 0 or 1 element, it is already sorted, so return
        return
        # Iterate over the array starting from the second element
    for i in range(1, n):
        # Store the current element as the key to be inserted in the
        # right position
        key = arr[i]
        j = i-1
        # Move elements greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
# Sorting the array [12, 11, 13, 5, 6] using insertionSort


arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
insertionSort(arr)
print(f"Insertion sort: {arr}")

# 3.3 Alt search method - Index. Quick and simple to impliment and would
# be usedful to in menu navigation and determining unique id's amnd names.

use_index = sample.index(9)
print(use_index)
