#!/usr/bin/env python3
"""
The basic mechanics of this puzzle is fairly straightforward.  You have
a position (x, y) and velocity (dx, dy) for each element in the grid.
In a loop that acts as each second of velocity, it's simple math.

The hard part is how do you know when the message has converged?

You could be an AI/ML junky and convert the grid to an image and run an
OCR method on it to see if it produces a result.

Or, you can use a concept called entropy.  Since the letters are block
character letters, most of the well formed letters will be vertical
lines.  So, if you define entropy for a given vertical line at a
particular y-coordinate as the sum over all elements (i) of the delta
between that y (y_j) and the y-value of the element (i_j), namely:
    E_j = Sum(i) [y_j - i_y]

And then sum all the entropy values for each vertical line, that is,
all y grid values (y_j), namely:

    E = Sum(y_j) Sum(i) [y_j - i_y]

For a truly random assortment of elements (i), this entropy (E) will be
an extremely large value. As the letters come into focus, the value will
converge to a minimum value before growing again.

This program calculates the entropy (a costly operation) initially at
large intervals.  As the entropy change rate gets bigger, the interval
automatically decreases to eventually calculate entropy every iteration
to find the inflection point.
"""

import re


def regex_engine():
    s = r'position=<(?P<position>.+?)> velocity=<(?P<velocity>.+?)>'
    return re.compile(s)


def calculate_grid(lights):
    x_min = 10000
    y_min = 10000
    x_max = -10000
    y_max = -10000

    for key in lights:
        if key[0] < x_min:
            x_min = key[0]
        if key[0] > x_max:
            x_max = key[0]
        if key[1] < y_min:
            y_min = key[1]
        if key[1] > y_max:
            y_max = key[1]

    return (x_min, x_max, y_min, y_max)


def print_grid(lights):

    # Get reduced grid size
    grid = calculate_grid(lights)

    # Print the grid
    for y in range(grid[2], grid[3]+1):
        line = ''
        for x in range(grid[0], grid[1]+1):
            if (x, y) in points:
                line = line + '#'
            else:
                line = line + '.'
        print(line)


def calculate_entropy(lights):
    # Find max grid size
    points = lights.keys()

    # Get reduced grid size
    grid = calculate_grid(lights)

    # Let's do vertical entropy
    entropy = 0

    for y in range(grid[2], grid[3]+1):
        for p in points:
            entropy = entropy + abs(y - p[1])*len(lights[p])

    return entropy


if __name__ == '__main__':

    engine = regex_engine()
    lights = {}

    # Read initial vector data
    with open('input.txt', 'r') as f:
        for l in f:
            result = engine.match(l)

            pos_str = result.group('position')
            pos = pos_str.split(',')
            key = (int(pos[0]), int(pos[1]))

            vel_str = result.group('velocity')
            vel = vel_str.split(',')
            val = (int(vel[0]), int(vel[1]))

            lights[key] = [val]

    # Loop over all the points to find a message
    entropy = 0
    seconds = 0
    interval = 2000
    previous_lights = lights

    print('Seconds', 'Entropy', 'Reporting_Interval')
    while(True):
        # On first iteration, calculate and print initial entropy
        if seconds == 0:
            entropy = calculate_entropy(lights)
            print(seconds, entropy, interval)
        elif seconds % interval == 0:
            # After the interval, recalculate the entropy
            delta = calculate_entropy(lights)

            # If the entropy change is big enough, reduce the interval
            if entropy / delta > 2.0:
                interval = max(int(interval / 2), 1)

            # If the entropy is increasing now, exit the loop
            if delta > entropy:
                break

            # Record the new entropy level
            entropy = delta
            print(seconds, delta, interval)

        # Relocate points based on the velocity vectors
        points = list(lights.keys())
        new_lights = {}

        # Loop over each x,y point stored
        for p in points:
            # We are accounting for multiple points in same location
            for v in lights[p]:
                # Calculate new position
                x = p[0] + v[0]
                y = p[1] + v[1]

                # Store new location with same velocity
                if (x, y) in new_lights:
                    new_lights[(x, y)].append(v)
                else:
                    new_lights[(x, y)] = [v]

        # Remember the old lights
        previous_lights = lights

        # Record the new lights
        lights = new_lights

        # Increase the clock
        seconds = seconds + 1

    # Entropy started increasing - print the result
    print('Puzzle 2 is {}'.format(seconds-1))
    print('Puzzle 1 is below:')
    print_grid(previous_lights)
