""" Task 25 - Task 2."""
num_list = [3, 1, 16, 8, 84, 48, -2, 4, 5, 77]


def largest_number(num_list: list[int]) -> int:
    """Set base to len = 1 to ensure that the recursion stops when the length
    of the list is 1.
    Args:
        num_list (list[int]): Random integers
    Returns:
        int: returns the current value of the integer which in the first
        recursive call is 77.
    """
    # set base case
    # print(num_list)
    if len(num_list) == 1:
        return num_list[0]
    else:
        """Returns the current value of the previous return which is used as
        an argument inside a max() method to determine the largest value
        between itself and the recursive call, namely the list elements - 1
        element to ensure that the list becomes one element smaller when it
        calls itself each time until it gets to the base case and then stops.
        Who figured this out...?
        Returns:
            num_list[1:] (list[int]):list with int elements
        """
        # print(num_list[0])
        return max(num_list[0], largest_number(num_list[1:]))


print(largest_number(num_list))
