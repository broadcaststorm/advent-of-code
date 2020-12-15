#!/usr/bin/env python3
"""
The choice of dict for the matrix is for index convenience (personal style).
That approach as well as going sparse makes some error checking very
straightforward:
  - out of bounds checking (seats outside the grid)
  - checking for seat existing at location
Using 0 (empty) and 1 (occupied) makes occupied checks simpler via "if seat:"

It also permits simpler, less dependent passing of state to other methods
without having to include x/y max values, etc.

Of course, with part 2, those efforts get hampered with the directional
line of sight.
"""

import copy


def read_input_data(input_file):
    # Coordinate system: right => +x, down => +y
    matrix = {}

    with open(input_file, 'r') as f:
        # Read in the entire file (since it's small), stripping EOL whitespace
        lines = [x.rstrip() for x in f.readlines()]

    # Build a matrix from the data. You could make it sparse here if large.
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            # Don't record floor spaces
            if char == '.':
                continue

            # Empty seat == 0
            if char == 'L':
                matrix[(i, j)] = 0
            # Occupied seat == 1
            elif char == '#':
                matrix[(i, j)] = 1
            # Sanity check error condition
            else:
                raise Exception('Unknown type {0}'.format(char))

    # Extract grid size here given we are going sparse
    y_max = len(lines)
    x_max = len(lines[0])

    return x_max, y_max, matrix


def part2_count_perimeter(state, x, y, x_max, y_max):
    """
    Need to count the perimeter not based on adjacency but with line of sight
    of those 8 directions.
    """

    # # Calculate a grid size
    # points = list(state.keys())
    # points.sort()
    # x_max, y_max = points[-1]

    num_occupied = 0

    # (deltax, deltay) vectors
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]

    # Calculate a max radius - somewhat inefficient but sparse matrix
    # approach makes it lighterweight
    if x_max > y_max:
        max_radius = x_max
    else:
        max_radius = y_max

    for dx, dy in directions:
        # Expand outwards to the edge
        for r in range(1, max_radius+1):
            # Next seat in that trajectory
            ring = (x + r * dx, y + r * dy)

            # No seat, or past the edge
            if ring not in state:
                continue

            # Found the next seat, count it if occupied. Abort trajectory
            if state[ring]:
                num_occupied = num_occupied + 1
            break

    return num_occupied


def part1_count_perimeter(state, x, y, x_max, y_max):
    """
    Well, guessed right on the rules, didn't guess right on the perimeter
    so, for part 2, had to rename this method.
    """
    num_occupied = 0
    index = (x, y)

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            ring = (i, j)

            # Out of bounds check, space is floor check
            if ring not in state:
                continue

            # Skip myself
            if index == ring:
                continue

            # If someone is in the seat, count it
            if state[ring]:
                num_occupied = num_occupied + 1

    return num_occupied


def part1_rules(current, ring_count, ring_limit=4):
    """
    Making this separate as I have a sneaky suspicion these might change.
    For part2, added ring_limit argument and change below to make part2_rules
    straightforward
    """

    if current == 0 and ring_count == 0:
        return 1

    if current == 1 and ring_count >= ring_limit:
        return 0

    return current


def part2_rules(current, ring_count):
    return part1_rules(current, ring_count, 5)


def print_grid(state, x_max, y_max):
    for j in range(y_max):
        for i in range(x_max):
            if (i, j) not in state:
                print('.', end='')
                continue
            print(state[(i, j)], end='')
        print('')


def calculate_final_state(
        input_state, x_max, y_max, debug=False,
        count_perimeter=part1_count_perimeter,
        apply_rules=part1_rules):
    """
    Having done this contest - Advent of Code - I wisely predicted the change
    of rules for 'apply_rules'.  Missed the change in perimeter behavior so
    for part2, added an extra argument to specify the newly renamed perimeter
    counter.
    """

    # Track to see if our state changed in the most recent iteration
    changed = True

    # Need a separate state matrix to store the new results on each iteration
    current_state = copy.deepcopy(input_state)

    while(changed):
        # Reset changed state
        changed = False
        final_state = {}

        # Loop over the grid
        for y in range(y_max):
            for x in range(x_max):
                index = (x, y)

                # If index doesn't exist, there's no seat
                if index not in current_state:
                    continue

                # Iterate around this seat to see if my current seat changes
                num_occupied = count_perimeter(
                                        current_state, x, y, x_max, y_max
                                    )

                # Rules engine here
                current_seat = current_state[index]
                final_seat = apply_rules(current_seat, num_occupied)
                final_state[index] = final_seat

                if current_seat != final_seat:
                    changed = True

                if debug:
                    print(index, current_seat, num_occupied, final_seat)

        # Save the new results back into initial state for next iteration
        current_state = final_state

        if debug:
            print('-' * x_max)
            print_grid(final_state, x_max, y_max)

    return copy.deepcopy(current_state)


if __name__ == '__main__':

    print('Part 1')
    smpl_x, smpl_y, sample_state = read_input_data('sample.txt')
    sample_final_state = calculate_final_state(sample_state, smpl_x, smpl_y)
    print('Sample: ' + str(sum(sample_final_state.values())))

    x_max, y_max, part1_state = read_input_data('input.txt')
    part1_final_state = calculate_final_state(part1_state, x_max, y_max)
    print('Results: ' + str(sum(part1_final_state.values())))

    print('Part 2')
    part2_sample_state = calculate_final_state(
        sample_state, smpl_x, smpl_y,
        count_perimeter=part2_count_perimeter, apply_rules=part2_rules
    )
    print('Sample: ' + str(sum(part2_sample_state.values())))

    part2_final_state = calculate_final_state(
        part1_state, x_max, y_max,
        count_perimeter=part2_count_perimeter, apply_rules=part2_rules
    )
    print('Results: ' + str(sum(part2_final_state.values())))
