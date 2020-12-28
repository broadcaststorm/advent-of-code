#!/usr/bin/env python3

import copy


def read_input_data(input_file):

    grid = {}
    max_cols = 0
    max_rows = 0

    with open(input_file, 'r') as f:
        raw = [x.rstrip() for x in f.readlines()]
        max_rows = len(raw)
        max_cols = len(raw[0])

        for y, row in enumerate(raw):
            for x, col in enumerate(row):
                grid[(x, y, 0, 0)] = col

    return max_cols, max_rows, grid


def apply_rules(grid, center):
    """
    - If a cube is inactive but exactly 3 of its neighbors are active, the
      cube becomes active. Otherwise, the cube remains inactive.
    - If a cube is active and exactly 2 or 3 of its neighbors are also active,
      the cube remains active. Otherwise, the cube becomes inactive.
    """

    # Active neighbor count
    active = 0

    # Count all the neighbors
    for x in [center[0]-1, center[0], center[0]+1]:
        for y in [center[1]-1, center[1], center[1]+1]:
            for z in [center[2]-1, center[2], center[2]+1]:
                for w in [center[3]-1, center[3], center[3]+1]:
                    current = (x, y, z, w)
                    if current == center:
                        continue

                    if current not in grid:
                        continue

                    if grid[current] == '#':
                        active = active + 1
                
    # Apply the rules
    if grid[center] == '.':
        if active == 3:
            return '#'
        else:
            return '.'

    if grid[center] == '#':
        if active == 2 or active == 3:
            return '#'
        else:
            return '.'

    raise Exception('Should not land here')


def cycle(grid, x_max, y_max, rounds=6):
    """
    Beginning the cycle, z_max = 0 but the max values must expand as the
    cycle ripples out.
    """

    # Finish defining bounds of the initial grid
    x_min = 0
    y_min = 0
    z_min = 0
    z_max = 1
    w_min = 0
    w_max = 1

    # Make a copy to be updated on each iteration
    updated = copy.deepcopy(grid)

    # Loop over the various rounds
    for n in range(0, rounds):

        # Expand the grid range around the perimeter
        x_min -= 1
        y_min -= 1
        z_min -= 1
        w_min -= 1
        x_max += 1
        y_max += 1
        z_max += 1
        w_max += 1

        # Process the grid
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                for z in range(z_min, z_max):
                    for w in range(w_min, w_max):
                        current = (x, y, z, w)

                        # The fringes may be expanded and not yet defined
                        if current not in grid:
                            grid[current] = '.'

                        # Apply the rules to determine active
                        updated[current] = apply_rules(grid, current)

        # Save the updates
        grid = copy.deepcopy(updated)

    return (x_min, y_min, z_min, w_min), (x_max, y_max, z_max, w_max), grid


def count_active(min_grid, max_grid, grid):
    num_active = 0

    for x in range(min_grid[0], max_grid[0]):
        for y in range(min_grid[1], max_grid[1]):
            for z in range(min_grid[2], max_grid[2]):
                for w in range(min_grid[3], max_grid[3]):
                    p = (x, y, z, w)
                    if p in grid:
                        if grid[p] == '#':
                            num_active += 1
    
    return num_active


if __name__ == '__main__':

    print('Part 2')
    sample_x_max, sample_y_max, sample_grid = read_input_data('sample.txt')
    v_min, v_max, final_grid = cycle(sample_grid, sample_x_max, sample_y_max)
    sample_active = count_active(v_min, v_max, final_grid)
    print('Sample: ' + str(sample_active))

    xmax, ymax, grid = read_input_data('input.txt')
    vmin, vmax, final = cycle(grid, xmax, ymax)
    num_active = count_active(vmin, vmax, final)
    print('Results: ' + str(num_active))
