#!/usr/bin/env python3

import math


vectors = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}

compass = ('N', 'E', 'S', 'W')


def read_input_data(input_file):
    with open(input_file, 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]
    return lines


def navigate(directions, bearing='E', x=0, y=0):
    current = [x, y]

    for d in directions:
        action = d[0]
        units = int(d[1:])

        # Simply go "forward"
        if action == 'F':
            current[0] += vectors[bearing][0] * units
            current[1] += vectors[bearing][1] * units
            continue

        # Translate a different direction
        if action in compass:
            current[0] += vectors[action][0] * units
            current[1] += vectors[action][1] * units
            continue

        # Time to change directions. Find current bearing index.
        idx = compass.index(bearing)

        # Calculate position changes (assuming multiples of 90)
        delta_idx = units // 90

        # Left is counter clockwise
        if action == 'L':
            delta_idx *= -1

        # New bearing
        new_idx = (idx + delta_idx) % 4
        bearing = compass[new_idx]

    return current[0], current[1], bearing


def rotate(bearing, direction, degrees):
    # Clockwise is negative degrees in the rotation matrix
    if direction == 'R':
        degrees *= -1

    degrees = math.radians(degrees)
    rot = [
        [math.cos(degrees), -1 * math.sin(degrees)],
        [math.sin(degrees), math.cos(degrees)]
    ]

    new_x = round(bearing[0] * rot[0][0]) + round(bearing[1] * rot[0][1])
    new_y = round(bearing[0] * rot[1][0]) + round(bearing[1] * rot[1][1])

    return [new_x, new_y]


def waypoint_navigation(directions, waypoint=(10, 1), x=0, y=0):
    current = [x, y]
    bearing = list(waypoint)

    for d in directions:
        action = d[0]
        units = int(d[1:])

        # Simply go "forward"
        if action == 'F':
            current[0] += bearing[0] * units
            current[1] += bearing[1] * units
            continue

        # Change the waypoint bearing
        if action in compass:
            bearing[0] += vectors[action][0] * units
            bearing[1] += vectors[action][1] * units
            continue

        # Time to change waypoint directions.
        bearing = rotate(bearing, action, units)

    return current[0], current[1], bearing


if __name__ == '__main__':

    print('Part 1')
    smpl_nav = read_input_data('sample.txt')
    smpl_x, smpl_y, smpl_bearing = navigate(smpl_nav)
    print('Sample: ' + str(abs(smpl_x) + abs(smpl_y)))

    final_nav = read_input_data('input.txt')
    part1_x, part1_y, part1_bearing = navigate(final_nav)
    print('Results: ' + str(abs(part1_x) + abs(part1_y)))

    print('Part 2')
    smpl_x, smpl_y, smpl_bearing = waypoint_navigation(smpl_nav)
    print('Sample: ' + str(abs(smpl_x) + abs(smpl_y)))

    part1_x, part1_y, part1_bearing = waypoint_navigation(final_nav)
    print('Results: ' + str(abs(part1_x) + abs(part1_y)))
