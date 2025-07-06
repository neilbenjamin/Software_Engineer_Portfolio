"""
Data structures: 2d lists.
Replicating the common approach
using a 3x3 grid.
"""

# NOTE:
# A fantastic beginner friendly resource is -> https://www.geeksforgeeks.org/
# Examples are simplified and they cover all
# concepts across most languages.
# Search using keywords like "python loops" using
# the built-in search bar.

grid = [
    ["-", "#", "-", "-", "#"],  # Index 0
    ["-", "-", "#", "#", "-"],  # Index 1
    ["#", "-", "-", "#", "#"],  # Index 2
    ["#", "-", "-", "#", "#"],  # Index 3
    ["#", "-", "-", "#", "#"]   # Index 5
    ]

# Simplified algorithm using only
# control structures and a range() loop.


def minesweeper(grid):
    limit = len(grid) - 1
    for row in range(len(grid)):
        for col in range(len(grid)):
            count = 0
            print(f"Live position coordinates: [{row}][{col}]")
            if grid[row][col] == "-":
                if row > 0 and grid[row - 1][col] == "#":
                    print("bomb north!")
                    count += 1
                if row < limit and grid[row + 1][col] == "#":
                    print("bomb south!")
                    count += 1
                if col > 0 and grid[row][col - 1] == "#":
                    print("bomb west!")
                    count += 1
                if col < limit and grid[row][col + 1] == "#":
                    print("bomb east!")
                    count += 1
                if row > 0 and col > 0 and grid[row - 1][col - 1] == "#":
                    print("bomb north west!")
                    count += 1
                if col < limit and row > 0 and grid[row - 1][col + 1] == "#":
                    print("bomb north east!")
                    count += 1
                if row < limit and col > 0 and grid[row + 1][col - 1] == "#":
                    print("bomb south west!")
                    count += 1
                if (row < limit and col <
                        limit and grid[row + 1][col + 1] == "#"):
                    print("bomb south east!")
                    count += 1
            else:
                print("I am a bomb!")
                continue
            grid[row][col] = str(count)


minesweeper(grid)

# Result display.
for i in grid:
    print(i)
