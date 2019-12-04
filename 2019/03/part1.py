#!/usr/bin/env python3
"""
part1.py - find the closet point of intersection from the origin of two
wires laid out upon a grid.

For this problem, I'm going to build a list of (x,y) vertices that each
wire path traverses and then use intersection function to find the common
vertices.
"""


def trace_path(path_list):
    """
    trace_path(path_list) - generate a list of vertices (x,y values) that
    the wire traverses on a grid.  Return the entire list of vertices.

    Input values are a list of directions and units of travel in the format:
        XN+
    where:
        X := is a up/down/left/right direction (values RLUD)
        N+ := is one or more number characters indicating units of travel

    Directions:
       R means increasing on x-axis
       L means decreasing on x-axis
       U means increasing on y-axis
       D means decreasing on y-axis
    """

    # Starting point
    trace = []
    x = 0
    y = 0

    for i in path_list:
        # A good programmer would validate the direction input i[0]

        for j in range(1, int(i[1:])+1):
            if i[0] == 'R':
                x = x + 1
            if i[0] == 'L':
                x = x - 1
            if i[0] == 'U':
                y = y + 1
            if i[0] == 'D':
                y = y - 1

            trace.append((x, y))

    return trace


def find_intersections(path1, path2):
    """
    Expected input for each path: CSV string with direction+units

    Collisions are the unique set of vertex values common to both paths
    """

    trace1 = trace_path(path1.split(','))
    trace2 = trace_path(path2.split(','))

    collision = list(set(trace1) & set(trace2))
    return collision


def find_closest(crossings):
    total = 1e20

    for i in crossings:
        d = abs(i[0]) + abs(i[1])
        if d < total:
            total = d

    return total


def test_cases():
    path1 = "R8,U5,L5,D3"
    path2 = "U7,R6,D4,L4"
    answer = 6

    crossings = find_intersections(path1, path2)
    result = find_closest(crossings)
    if answer != result:
        print('Failed test 1')

    path1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    path2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    answer = 159

    crossings = find_intersections(path1, path2)
    result = find_closest(crossings)
    if answer != result:
        print('Failed test 2')

    path1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    path2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    answer = 135

    crossings = find_intersections(path1, path2)
    result = find_closest(crossings)
    if answer != result:
        print('Failed test 3')


def read_wires():
    with open('part1.txt', 'r') as f:
        path1 = f.readline()
        path2 = f.readline()

    return (path1, path2)


if __name__ == '__main__':
    test_cases()

    path1, path2 = read_wires()
    crossings = find_intersections(path1, path2)
    result = find_closest(crossings)

    print('Distance of closest crossing is {0}'.format(result))
