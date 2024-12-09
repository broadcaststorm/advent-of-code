#!/usr/bin/env python3


import copy

valid_patterns = [
    [
        ["M", None, "M"],
        [None, "A", None],
        ["S", None, "S"]
    ],
    [
        ["M", None, "S"],
        [None, "A", None],
        ["M", None, "S"]
    ],
    [
        ["S", None, "S"],
        [None, "A", None],
        ["M", None, "M"]
    ],
    [
        ["S", None, "M"],
        [None, "A", None],
        ["S", None, "M"]
    ]
]


def match_grid(pattern, cell):
    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            if pattern[row][col]:
                if pattern[row][col] != cell[row][col]:
                    return False
    return True


def match_patterns(cell):
    for pattern in valid_patterns:
        if match_grid(pattern, cell):
            return True
    return False


def search_grid(grid: list[str], used: list[list[bool]]):

    # Get the dimensions of the grid
    size = (len(grid),len(grid[0]))
    word_count = 0

    for row in range(1,size[0]-1):
        for col in range(1,size[1]-1):
            if grid[row][col] == "A":
                cell = list()
                cell.append(grid[row-1][col-1:col+2])
                cell.append(grid[row][col-1:col+2])
                cell.append(grid[row+1][col-1:col+2])
                if match_patterns(cell):
                    word_count += 1

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

    print(f"Answer for part 2: {total}")
