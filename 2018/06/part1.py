#!/usr/bin/env python3

from operator import itemgetter


if __name__ == '__main__':

    # Data structure to store the various anchor points
    points = []

    # Initialize search - set based on cursory examination of input
    min_x = 1000
    min_y = 1000
    max_x = 0
    max_y = 0

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

    # For each point, let's walk the grid to calculate the Manhattan
    # distance at each grid coordinate
    for i in range(0, len(points)):
        x0 = points[i][0]
        y0 = points[i][1]

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                d = abs(x - x0) + abs(y - y0)
                if (x, y) not in grid:
                    grid[(x, y)] = [(i, d)]
                else:
                    grid[(x, y)].append((i, d))

    # Entire grid is populated, let's find the shortest distances
    shortest = {}

    # Count the number of cells for each point as we go along (+1 tied)
    counts = [0]*len(points)
    rejected = []

    for p in grid.keys():
        # Sort the list of points and their distances by distance
        s = sorted(grid[p], key=itemgetter(1))

        # Two points of same distance, use "tie" index
        if s[0][1] == s[1][1]:
            shortest[p] = len(points)
        else:
            shortest[p] = s[0][0]
            counts[s[0][0]] = counts[s[0][0]] + 1

        # If a source point extends to edge of grid, add to rejected
        if p[0] in (min_x, max_x):
            if s[0][0] not in rejected:
                rejected.append(s[0][0])

        if p[1] in (min_y, max_y):
            if s[0][0] not in rejected:
                rejected.append(s[0][0])

    # Sort index, count pairs
    sorted_counts = sorted(zip(range(0, len(counts)), counts),
                           key=itemgetter(1), reverse=True)

    # Process the list and reject "infinite" points
    for i, n in sorted_counts:
        if i not in rejected:
            print('Puzzle 1: {}'.format(n))
            break
