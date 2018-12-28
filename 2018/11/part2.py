#!/usr/bin/env python3
"""
Officially, this program runs a really long time because of the
extensive scaling grid size calculations.  So, you can let it run
overnight to see all the values.

However, after the grid size reaches about 90x90, the maximum power
level found for those grid searches converges to the same value (90 or
so).  So, you can look at the output at that point and determine the
correct value of the solution before the program completes.

"""


def generate_cell(serial_number):
    """
    Initialize the power levels for each cell throughout the grid based
    on the puzzles problem description
    """
    cell_power = {}

    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            power_level = rack_id * y
            power_level = power_level + serial_number
            power_level = power_level * rack_id
            power_level = power_level // 100
            power_level = power_level % 10
            cell_power[(x, y)] = power_level - 5

    return cell_power


def generate_grid(cell_power, size):
    grid_power = {}
    max_power = 0
    max_cell = ()

    # Loop over the entire grid
    for x in range(1, 301):
        for y in range(1, 301):

            # n x n Cell Summation
            sum = 0

            for i in range(x, x+size):
                if i > 300:
                    continue
                for j in range(y, y+size):
                    if j > 300:
                        continue

                    if (i, j) not in cell_power:
                        raise Exception("out of bounds {},{}".format(i, j))

                    sum = sum + cell_power[(i, j)]

            # Store the NxN sum value using the top left index values
            grid_power[(x, y)] = sum

            # If the value is the largest we've seen, record it.
            if sum > max_power:
                max_cell = (x, y)
                max_power = sum

    # Only return the max value and the x,y location it occurred
    return max_power, max_cell


if __name__ == '__main__':

    # First two are test inputs, third is puzzle input
    serials = [18, 42, 7803]

    for serial_number in serials:
        cell_power = generate_cell(serial_number)

        max_power = 0
        max_cell = ()
        max_grid = 0

        print('Starting serial number {}'.format(serial_number))
        for n in range(1, 300):
            current_power, current_cell = generate_grid(cell_power, n)
            print('\t', n, current_power, current_cell)

            if current_power > max_power:
                max_power = current_power
                max_cell = current_cell
                max_grid = n

        data = (serial_number, max_grid, max_cell, max_power)
        print('Puzzle 2 - serial({}) grid({}) cell({}) power({})'.format(data))
