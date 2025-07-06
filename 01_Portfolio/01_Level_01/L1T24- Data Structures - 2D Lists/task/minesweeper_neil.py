""" Task 26 - Task 1. Initially, very tricky to wrap my head around being able
to separately reference the indexes and their values. I did it in a dictionary
and then reverted back to lists.
"""
grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
        ]
x = "#"
count = 0


def counter(value: type) -> int:
    """input existing cel data and compute on that.
    Args:
        value (type): accept either a string or an int
    Returns:
        int: int
    """
    if type(value) is int:
        return value
    else:
        return 0


def dash_zero(grid: list[list[str]]) -> int:
    """Convert all non impacted cells to 0.
    Args:
        grid (list[list[str]]): REad grid
    Returns:
        int: return 0.
    """
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == "-":
                grid[row][col] = 0
    return 0


def south(range_start: int, range_end: int, south: int):
    """Update grid cells based on parameter inputs
    Args:
        range_start (int): row start
        range_end (int): _row end
        south (int): row + 1
    """
    for row in range(len(grid)):
        for col in range(len(grid)):
            # Row 0
            if grid[range_start][col] == x:
                max = len(grid)
                end = max - 1
                # east
                if grid[range_start][col - 1] != x and col > 0:
                    cel_count = counter(grid[range_start][col - 1])
                    grid[range_start][col - 1] = count + cel_count + 1
                # west
                if col < end and grid[range_start][col + 1] != x:
                    cel_count = counter(grid[range_start][col + 1])
                    grid[range_start][col + 1] = cel_count + 1
                # South
                if grid[south][col] != x:
                    cel_count = counter(grid[south][col])
                    grid[south][col] = count + cel_count + 1
                # South East
                if grid[south][col - 1] != x and col > 0:
                    cel_count = counter(grid[south][col - 1])
                    grid[south][col - 1] = count + cel_count + 1
                # South West
                if col < end and grid[south][col + 1] != x:
                    cel_count = counter(grid[south][col + 1])
                    grid[south][col + 1] = cel_count + 1
    return


def coordinates(range_start: int, range_end: int, north: int, south: int):
    """Update grid cells based on parameter inputs
    Args:
        range_start (int): row start
        range_end (int): _row end
        north (int): row -1
        south (int): _description_row + 1
    """
    for row in range(len(grid)):
        for col in range(len(grid)):
            # Row 0
            if grid[range_start][col] == x:
                max = len(grid)
                end = max - 1
                # east
                if grid[range_start][col - 1] != x and col > 0:
                    cel_count = counter(grid[range_start][col - 1])
                    grid[range_start][col - 1] = count + cel_count + 1
                # west
                if col < end and grid[range_start][col + 1] != x:
                    cel_count = counter(grid[range_start][col + 1])
                    grid[range_start][col + 1] = cel_count + 1
                # North
                if grid[north][col] != x:
                    cel_count = counter(grid[north][col])
                    grid[north][col] = count + cel_count + 1
                # North East
                if grid[north][col - 1] != x and col > 0:
                    cel_count = counter(grid[north][col - 1])
                    grid[north][col - 1] = count + cel_count + 1
                # North West
                if col < end and grid[north][col + 1] != x:
                    cel_count = counter(grid[north][col + 1])
                    grid[north][col + 1] = cel_count + 1
                # South
                if grid[south][col] != x:
                    cel_count = counter(grid[south][col])
                    grid[south][col] = count + cel_count + 1
                # South East
                if grid[south][col - 1] != x and col > 0:
                    cel_count = counter(grid[south][col - 1])
                    grid[south][col - 1] = count + cel_count + 1
                # South West
                if col < end and grid[south][col + 1] != x:
                    cel_count = counter(grid[south][col + 1])
                    grid[south][col + 1] = cel_count + 1
    return


def north(range_start: int, range_end: int, north: int):
    """Update grid cells based on parameter inputs
    Args:
        range_start (int): row start
        range_end (int): _row end
        south (int): row - 1
    """
    for row in range(len(grid)):
        for col in range(len(grid)):
            # Row 0
            if grid[range_start][col] == x:
                max = len(grid)
                end = max - 1
                # east
                if grid[range_start][col - 1] != x and col > 0:
                    cel_count = counter(grid[range_start][col - 1])
                    grid[range_start][col - 1] = count + cel_count + 1
                # west
                if col < end and grid[range_start][col + 1] != x:
                    cel_count = counter(grid[range_start][col + 1])
                    grid[range_start][col + 1] = cel_count + 1
                # North
                if grid[north][col] != x:
                    cel_count = counter(grid[north][col])
                    grid[north][col] = count + cel_count + 1
                # North East
                if grid[north][col - 1] != x and col > 0:
                    cel_count = counter(grid[north][col - 1])
                    grid[north][col - 1] = count + cel_count + 1
                # North West
                if col < end and grid[north][col + 1] != x:
                    cel_count = counter(grid[north][col + 1])
                    grid[north][col + 1] = cel_count + 1
    return


def start() -> int:
    """Start function to start the functions to read and update grid.
    Returns:
        int: Updates various coordinates
    """
    # Row 1
    start_row_coordinates = south(0, 1, 1)
    # Row 2
    grid_coordinates = coordinates(1, 2, 0, 2)
    # Row 3
    grid_coordinates = coordinates(2, 3, 1, 3)
    # Row 4
    grid_coordinates = coordinates(3, 4, 2, 4)
    # Row 5
    end_row_coordinates = north(4, 5, 3)
    dash_zero(grid)
    return start_row_coordinates, grid_coordinates, end_row_coordinates


start()


print(str(grid[0]))
print(str(grid[1]))
print(str(grid[2]))
print(str(grid[3]))
print(str(grid[4]))

# for i in grid:
#     print(str(i))
