#!/usr/bin/env python3


from copy import copy, deepcopy
from math import atan2, pi
from part1 import Grid


class Blast(Grid):
    def __init__(self, input_file):
        Grid.__init__(self, input_file)

    def blast_order(self, x0, y0, direct):
        """
        Okay, this one is a mind bending, the y-axis is inverted compared to
        normal trignometry.  So despite the problem statement indicating it
        starts pointing up, default math is oriented in the opposite direction

        Straight up in the coordinate system would equate to -pi/2 in the
        "usual" orientation.  So, -pi/2 to -pi (sign flips to +pi) then
        decreases to 0, then again to -pi/2.
        """

        angles = {}
        for x, y in direct:
            dx = x - x0
            dy = y - y0

            # Determine the angle
            angle = atan2(dy, dx)

            # Add angle to dictionary
            angles[angle] = (x, y)

        # Sort the list of angles
        sorted_angles = list(angles.keys())
        sorted_angles.sort()

        # Find the starting point
        i = 0
        start = -pi / 2
        while(i < len(sorted_angles)):
            if sorted_angles[i] < start:
                i = i + 1
                continue
            # We have stepped passed the start point so escape here
            break

        # Rebuild the list so that we start at the right spot
        sorted_angles = sorted_angles[i:] + sorted_angles[:i]

        return copy(sorted_angles), deepcopy(angles)

    def clear_asteroids(self, x0, y0):
        """
        This method is here in case there are not 200 asteroids in the initial
        direct line of sight order.  So, first fetch the list of directly
        visible asteroids.  Then, pull the 200th element.

        The code to deal with "round 2" of rotations isn't written because it
        wasn't needed.  Whew!

        But the idea is simple: iterate through the direct list, removing
        the entries from self.grid.  Then, regenerate the direct list. Rinse
        and repeat.
        """

        direct = self.direct_asteroids(x0, y0)

        order, angles = self.blast_order(x0, y0, direct)

        if len(order) >= 200:
            angle = order[199]
            x, y = angles[angle]
            return x, y

        raise Exception('Do something else')


def unit_tests():
    sample5 = Blast('sample5.txt')
    x, y = sample5.clear_asteroids(11, 13)
    assert((x, y) == (8, 2))


if __name__ == '__main__':
    unit_tests()

    part2 = Blast('input.txt')
    x, y = part2.clear_asteroids(26, 36)
    print(x*100+y)
