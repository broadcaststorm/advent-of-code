#!/usr/bin/env python3


class Grid:
    """
    If _xmax or _ymax is not None, the grid is fixed size along that axis
    """
    def __init__(self, xmax=None, ymax=None, default='0'):
        self._grid = {}
        self._xmax = xmax
        self._ymax = ymax
        self._grid_default = default

    def _valid_x_axis(self, x):
        # Is x-axis within grid
        if self._xmax is None:
            return True
        if abs(x) <= self._xmax:
            return True
        return False

    def _valid_y_axis(self, y):
        # Is y-axis within grid
        if self._ymax is None:
            return True
        if abs(y) <= self._ymax:
            return True
        return False

    def _valid_axes(self, x, y):
        if not self._valid_x_axis(x):
            raise Exception('X-axis error {0},{1}'.format(x, self._xmax))

        if not self._valid_y_axis(y):
            raise Exception('Y-axis error {0},{1}'.format(y, self._ymax))

        return True

    def missing_grid(self, x, y):
        self._valid_axes(x, y)
        return self._grid_default

    def get(self, x, y):
        if (x, y) not in self._grid:
            return self.missing_grid(x, y)
        return self._grid[(x, y)]

    def set(self, x, y, value):
        self._valid_axes(x, y)
        self._grid[(x, y)] = value
