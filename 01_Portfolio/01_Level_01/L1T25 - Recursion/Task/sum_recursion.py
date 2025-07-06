""" Task 25 - Task 1. I find this concept rather confusing and managed to find
assistance on youtube and geeksforgeeks for this solution as well as
invaluable help from mentor feedback. I removed the while loop which was
intended to assist with the error handling in case the entered integer is
larger than the length of the list. I've left the conditional in though.
"""
nums = [1, 4, 5, 3, 12, 16]


def adding_up_to(nums: list[int],  i: int) -> int:
    """Calculate the sum from index 0 to given i variable recursively.
    Args:
        list (int): Random integers in a list.
        i (int): user input integer to set index to count back from.
    Returns:
        int: sum value of each iterations index value -1 until 0 is
        reached.
    """
    if i > len(nums):
        print("index is longer than list. Try again.")
    # Base
    elif i == 0:
        return nums[i]
    # recursion conditions
    else:
        # print(nums[i])
        return nums[i] + adding_up_to(nums, i-1)


print(adding_up_to(nums, 4))
