#!/usr/bin/env python3


from copy import copy, deepcopy
from math import gcd


class Grid:
    def __init__(self, input_file):
        self.grid = {}
        self.ymax = None
        self.xmax = None
        self.dmax = None

        self._parse_file(input_file)

    def _parse_file(self, input_file):
        with open(input_file, 'r') as file:
            y = 0
            for line in file:
                columns = list(line.rstrip())
                for x in range(len(columns)):
                    self.grid[(x, y)] = columns[x]
                y = y + 1

        self.xmax = x + 1
        self.ymax = y
        if x > y:
            self.dmax = self.xmax
        else:
            self.dmax = self.ymax

        return

    def print_grid(self):
        for y in range(self.ymax):
            line = []
            for x in range(self.xmax):
                line.append(self.grid[(x, y)])
            print(''.join(line))

    def has_asteroid(self, x, y):
        if self.grid[(x, y)] == '#':
            return True
        return False

    def build_deltas(self, x0, y0):
        deltas = {}

        for x in range(self.xmax):
            for y in range(self.ymax):
                # Skip origin point
                if (x == x0) and (y == y0):
                    continue

                # Is there an asteroid here?
                if not self.has_asteroid(x, y):
                    continue

                # Determine dx, dy from observer location
                dx = x - x0
                dy = y - y0

                # Reduce the slope to its lowest form
                div = gcd(dx, dy)
                dx = dx // div
                dy = dy // div

                # Store the reduced slope
                deltas[(x, y)] = (dx, dy)

        return deltas

    def perimeter(self, x0, y0, d):
        points = []

        # Top and bottom of the box
        for y in (y0 - d, y0 + d):

            # Are we within the grid
            if not self.valid_y_point(y):
                continue

            for x in range(x0 - d, x0 + d + 1):
                # Are we within the grid
                if not self.valid_x_point(x):
                    continue

                # Does the grid point have an asteroid
                if not self.has_asteroid(x, y):
                    continue

                points.append((x, y))

        # Left and right of the box
        for x in (x0 - d, x0 + d):

            # Are we within the grid
            if not self.valid_x_point(x):
                continue

            # This range is slightly smaller to account for top/bot logic
            # already including those points
            for di in range(-d + 1, d):
                y = y0 + di

                # Are we within the grid
                if not self.valid_y_point(y):
                    continue

                # Does the grid point have an asteroid
                if not self.has_asteroid(x, y):
                    continue

                points.append((x, y))

        return points

    def valid_x_point(self, x):
        # Are we within the grid
        if x >= self.xmax:
            return False
        if x < 0:
            return False
        return True

    def valid_y_point(self, y):
        # Are we within the grid
        if y >= self.ymax:
            return False
        if y < 0:
            return False
        return True

    def valid_vertex(self, x, y):
        if not self.valid_x_point(x):
            return False
        if not self.valid_y_point(y):
            return False
        return True

    def find_shadows(self, x0, y0, deltas):
        shadow = {}

        # Eliminate shadows - loop over range of radii
        for i in range(1, self.dmax):

            # Get the next perimeter of points to consider
            box_points = self.perimeter(x0, y0, i)

            for x, y in box_points:
                # All perimeter points w/ asteroids returned.
                # Need to check if it's valid (non-shadowed)
                if (x, y) not in deltas:
                    continue

                dx, dy = deltas[(x, y)]

                # Loop over multiples of deltas to find asteroids in shadow
                for mult in range(1, self.dmax):
                    xm = x + mult * dx
                    ym = y + mult * dy

                    if not self.valid_vertex(xm, ym):
                        continue

                    if not self.has_asteroid(xm, ym):
                        continue

                    shadow[(xm, ym)] = True

        return shadow

    def direct_asteroids(self, x0, y0):
        # Sweep the grid and find all the reduced dx, dy components of L.O.S
        # (Line of Sight)
        deltas = self.build_deltas(x0, y0)
        shadow = self.find_shadows(x0, y0, deltas)

        direct = {}
        for x, y in deltas:
            if (x, y) not in shadow:
                direct[(x, y)] = copy(deltas[(x, y)])

        return deepcopy(direct)

    def find_max_asteroids(self, x0, y0):
        direct = self.direct_asteroids(x0, y0)

        return len(list(direct.keys()))

    def find_optimal_asteroid(self):
        max_asteroids = 0
        max_x0 = -1
        max_y0 = -1

        for y0 in range(self.ymax):
            line = []
            for x0 in range(self.xmax):
                if not self.has_asteroid(x0, y0):
                    continue

                current = self.find_max_asteroids(x0, y0)
                line.append(str(current))
                if current > max_asteroids:
                    max_asteroids = current
                    max_x0 = x0
                    max_y0 = y0

        return max_x0, max_y0, max_asteroids


def unit_tests():
    sample1 = Grid('sample1.txt')
    x0, y0, max = sample1.find_optimal_asteroid()
    assert((3, 4, 8) == (x0, y0, max))

    sample2 = Grid('sample2.txt')
    x0, y0, max = sample2.find_optimal_asteroid()
    assert((5, 8, 33) == (x0, y0, max))

    sample3 = Grid('sample3.txt')
    x0, y0, max = sample3.find_optimal_asteroid()
    assert((1, 2, 35) == (x0, y0, max))

    sample4 = Grid('sample4.txt')
    x0, y0, max = sample4.find_optimal_asteroid()
    assert((6, 3, 41) == (x0, y0, max))

    sample5 = Grid('sample5.txt')
    x0, y0, max = sample5.find_optimal_asteroid()
    assert((11, 13, 210) == (x0, y0, max))


if __name__ == '__main__':

    unit_tests()

    part1 = Grid('input.txt')
    x0, y0, max = part1.find_optimal_asteroid()

    print(x0, y0, max)
