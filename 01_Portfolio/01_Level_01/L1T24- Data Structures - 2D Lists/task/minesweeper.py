""" Task 24 - Upon request for review, reading through the notes and reviewing
the suggestions from mentors, it was easy to see how I convoluted the solution
by targeting the "#" indexes instead of the "-"'s which make it easier to
update the cells. I updated the basic solution, courtesy of Chris Smit,  to
match the current criteria fot this task. I also did a version where I targeted
the "#"'s but the code is much loner and I prefer to think of the solution in
this  manner now. The cast to string from int is also genius and saves a lot
of looping, appending and joining to get back to a string.
"""
grid = [
    ["-", "#", "#", "-", "#"],  # Index 0
    ["-", "-", "#", "#", "-"],  # Index 1
    ["#", "-", "-", "#", "#"],  # Index 2
    ["#", "-", "-", "-", "#"],  # Index 3
    ["#", "-", "-", "#", "#"]   # Index 5
    ]

max_length = len(grid) - 1
# print(limit)
for row in range(len(grid)):
    # print(f"This is the row: {row}")
    for col in range(len(grid)):
        count = 0
        # print(f"This is the column: {col}")
        number = 0
        if grid[row][col] == "-":
            if row > 0 and grid[row - 1][col] == "#":
                count += 1
                grid[row][col] = str(count)
            if row < max_length and grid[row + 1][col] == "#":
                count += 1
                grid[row][col] = str(1)
            if col > 0 and grid[row][col - 1] == "#":
                count += 1
                grid[row][col] = str(count)
            if col < max_length and grid[row][col + 1] == "#":
                count += 1
                grid[row][col] = str(count)
            if row > 0 and col > 0 and grid[row - 1][col - 1] == "#":
                count += 1
                grid[row][col] = str(count)
            if col < max_length and row > 0 and grid[row - 1][col + 1] == "#":
                count += 1
                grid[row][col] = str(count)
            if row < max_length and col > 0 and grid[row + 1][col - 1] == "#":
                count += 1
                grid[row][col] = str(count)
            if (row < max_length and col <
                    max_length and grid[row + 1][col + 1] == "#"):
                count += 1
                grid[row][col] = str(count)
        else:
            continue


for i in grid:
    print(i)
