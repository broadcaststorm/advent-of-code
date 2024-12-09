#!/usr/bin/env python3


import copy


def find_words(grid: list[str], word: str, start: tuple[int,int], size: tuple[int,int]):
    """
    This routine is simply to take a starting point and search radially from
    that point for the provided word.
    """

    word_len = len(word)
    word_count = 0

    # The search patterns are bounded by the sides of the grid.  Given that our pattern
    # is North, Northeast, East, Southeast, South, Southwest, West, and Northwest.
    right_valid = True if (start[1] + (word_len - 1) < size[1]) else False
    left_valid = True if (start[1] - (word_len - 1) >= 0) else False
    down_valid = True if (start[0] + (word_len - 1) < size[0]) else False
    up_valid = True if (start[0] - (word_len -1) >= 0) else False

    # Easterly options
    if right_valid:
        east = True
        northeast = True if up_valid else False
        southeast = True if down_valid else False

        for col in range(word_len):
            # Due east
            if east:
                if word[col] != grid[start[0]][start[1]+col]:
                    east = False

            # Northeast
            if northeast:
                if word[col] != grid[start[0]-col][start[1]+col]:
                    northeast = False

            # Southeast
            if southeast:
                if word[col] != grid[start[0]+col][start[1]+col]:
                    southeast = False

        if east:
            word_count += 1

        if northeast:
            word_count += 1

        if southeast:
            word_count += 1

    # westerly options
    if left_valid:
        west = True
        northwest = True if up_valid else False
        southwest = True if down_valid else False

        for col in range(word_len):
            # Due west
            if west:
                if word[col] != grid[start[0]][start[1]-col]:
                    west = False

            # Northwest
            if northwest:
                if word[col] != grid[start[0]-col][start[1]-col]:
                    northwest = False

            # Southwest
            if southwest:
                if word[col] != grid[start[0]+col][start[1]-col]:
                    southwest = False

        if west:
            word_count += 1

        if northwest:
            word_count += 1

        if southwest:
            word_count += 1

    # North
    if up_valid:
        north = True
        for col in range(word_len):
            if word[col] != grid[start[0]-col][start[1]]:
                north = False
                break
        if north:
            word_count += 1
            
    # South
    if down_valid:
        south = True
        for col in range(word_len):
            if word[col] != grid[start[0]+col][start[1]]:
                south = False
                break
        if south:
            word_count += 1

    return word_count


def search_grid(grid: list[str], used: list[list[bool]]):

    # Get the dimensions of the grid
    size = (len(grid),len(grid[0]))
    word_count = 0

    for row in range(size[0]):
        for col in range(size[1]):
            word_count += find_words(grid, "XMAS", (row, col), size)

    return word_count


def read_input(filename: str) -> list[str]:
    grid: list[list] = list()

    with open(filename, "r") as f:
        for line in f.readlines():
            grid.append(line.strip())

    return grid


def create_used_grid(grid: list[str]) -> list[list[bool]]:

    used: list[list[str]] = list()

    y_size = len(grid)
    x_size = len(grid[0])

    row = [False for i in range(x_size)]

    for i in range(y_size):
        used.append(copy.copy(row))

    return used


def main(filename="input.txt") -> int:
    grid: list[str] = read_input(filename)
    used: list[list[bool]] = create_used_grid(grid)
    total_words = search_grid(grid, used)
    return total_words


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 1: {total}")
