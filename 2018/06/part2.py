#!/usr/bin/env python3


if __name__ == '__main__':

    # Data structure to store the various anchor points
    points = []

    # Initialize search - set based on cursory examination of input
    min_x = 1000
    min_y = 1000
    max_x = 0
    max_y = 0

    max_distance = 10000

    with open('input.txt', 'r') as f:
        for l in f:
            x, y = l.split(',')

            # Convert str to int
            x = int(x)
            y = int(y)

            # Determine if we found a new outer limit of the box
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

            points.append((int(x), int(y)))

    # Grid dictionary
    grid = {}

    # Walk the grid, sum the Manhattan distances over all data points
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            d = 0
            for x0, y0 in points:
                d = d + abs(x - x0) + abs(y - y0)

            if d >= max_distance:
                continue

            if (x, y) not in grid.keys():
                grid[(x, y)] = d

    print('Puzzle 2: {}'.format(len(grid.keys())))
