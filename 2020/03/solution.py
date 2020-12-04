#!/usr/bin/env python3
"""
For today's challenge, I'm going to structure the main section
to better simplify the "sample" test case and the "production"
test case.
"""


def find_trees(input_data, rows, cols, right, down):
    """
    We know the pattern repeats "infinitely" to the right (+x)
    and our termination condition is the "bottom" of the matrix.
    Rather than copy unknown templates of data, simply use mod/%
    to replicate the repetition.
    """

    trees_in_path = []
    x = 0

    # Advancing down the grid we'll use a loop
    for y in range(0, rows, down):
        # Current position
        loc = (x, y)

        # Sanity check... but only if not sparse. If spare, 'continue' instead
        if loc not in input_data:
            break

        if input_data[loc] == '#':
            trees_in_path.append(loc)

        # Advancing across the grid will use mod math
        x = (x + right) % cols

    return trees_in_path


def read_input_data(input_file):
    """
    Read in all the lines, parse into a data structure, return it.
    """

    # Coordinate system: right => +x, down => +y
    matrix = {}

    with open(input_file, 'r') as f:
        # Read in the entire file (since it's small), stripping EOL whitespace
        lines = [x.rstrip() for x in f.readlines()]

    # Build a matrix from the data. You could make it sparse here if large.
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            matrix[(i, j)] = char

    y_max = len(lines)
    x_max = len(lines[0])

    return x_max, y_max, matrix


def part_one(input_file):
    """
    The general solution form is:
      - Build matrix of the input file
      - Walk the matrix and return all the trees
      - Use "len" to count them
    """

    cols, rows, data = read_input_data(input_file)
    trees = find_trees(data, rows, cols, 3, 1)
    return len(trees)


def part_two(input_file):
    """
    For part two, I can re-use everything I had built for part one.
    Yes, I got lucky!

    So, build an array of slopes to test, build matrix, loop over slopes
    and walk the matrix, multiplying all the tree counts.
    """

    slopes = [
        (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    ]

    cols, rows, data = read_input_data(input_file)

    print('Part 2: Individual slope results')
    num_trees = 1
    for x, y in slopes:
        temp = find_trees(data, rows, cols, x, y)
        count = len(temp)
        print('Right {0}, Down {1}, Trees {2}'.format(x, y, count))
        num_trees = num_trees * count

    return num_trees


if __name__ == '__main__':

    # Part 1: Test the sample
    test_file = 'sample.txt'
    print('Sample result: {0}'.format(part_one(test_file)))

    # Part 1: Run the full data set
    prod_file = 'input.txt'
    print('Part 1 result: {0}'.format(part_one(prod_file)))

    # Part two: - woo hoo, my find_trees can be used unchanged!
    print('Part 2 Sample: {0}'.format(part_two(test_file)))
    print('Part 2 result: {0}'.format(part_two(prod_file)))
