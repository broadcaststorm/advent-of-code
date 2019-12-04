#!/usr/bin/env python3
"""
part2.py - Need to find the shortest combined path of each wire to the
common intersection.  In short, not closest intersection in space but
closest intersect along the paths of the circuit.

Turns out, the approach I took in part 1 - storing the vertex values as
you travel the wire path - gives us a simple mechanism for calculating the
wire path distance: index value (plus 1).

The way I built the methods in the first part don't quite align with
the second parts plans - I can't re-use find_intersections() because I need
the full list for each path, not just the intersections.

So, the shortest_path method below duplicates some code but it makes sense
in this case.
"""

from part1 import read_wires, trace_path


def shortest_path(path1, path2):

    # Generate the wire trace paths for each wire
    trace1 = trace_path(path1.split(','))
    trace2 = trace_path(path2.split(','))

    # Find the intersection points for the two wires
    collisions = list(set(trace1) & set(trace2))

    # Initialize the maximum distance possible
    d = len(trace1) + len(trace2)

    # Loop over all collisions looking for the shortest path
    for c in collisions:

        # For each intersection, find out the total path travelled along each
        # path.  Look for the minimum of the total paths.  Adding 1 because
        # index 0 of each path is the 1st step away from the path origin.
        d1 = trace1.index(c) + 1
        d2 = trace2.index(c) + 1
        if (d1 + d2) < d:
            d = d1 + d2

    return d


def test_cases():
    path1 = "R8,U5,L5,D3"
    path2 = "U7,R6,D4,L4"
    answer = 30

    result = shortest_path(path1, path2)
    if answer != result:
        print('Failed test 1')

    path1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    path2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    answer = 610

    result = shortest_path(path1, path2)
    if answer != result:
        print('Failed test 2')

    path1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    path2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    answer = 410

    result = shortest_path(path1, path2)
    if answer != result:
        print('Failed test 3')


if __name__ == '__main__':

    test_cases()

    path1, path2 = read_wires()
    d = shortest_path(path1, path2)

    print('Shortest path is {0}'.format(d))
