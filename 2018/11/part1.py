#!/usr/bin/env python3


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


if __name__ == '__main__':

    # Debug cell values
    serials = [57, 39, 71]
    points = [(122, 79), (217, 196), (101, 153)]
    levels = [-5, 0, 4]

    # Test the generation of the grid cell energy levels
    for i in range(0, len(serials)):
        cell_power = generate_cell(serials[i])
        print(serials[i], points[i], cell_power[points[i]], levels[i])

    # Let's find the 3x3 max energy sums for each of the three cases:
    # two test inputs and one problem input value
    serials = [18, 42, 7803]

    for serial_number in serials:

        cell_power = generate_cell(serial_number)
        grid_power = {}

        max_power = 0
        max_cell = ()

        for x in range(1, 301):
            for y in range(1, 301):

                # 3x3 Cell Summation
                sum = 0

                for i in range(x, x+3):
                    if i > 300:
                        continue
                    for j in range(y, y+3):
                        if j > 300:
                            continue

                        if (i, j) not in cell_power:
                            raise Exception("out of bounds {},{}".format(i, j))

                        sum = sum + cell_power[(i, j)]

                grid_power[(x, y)] = sum

                if sum > max_power:
                    max_cell = (x, y)
                    max_power = sum

        print("Puzzle 1 is {} at {}".format(max_power, max_cell))
