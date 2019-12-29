#!/usr/bin/env python3


class Direction:
    def __init__(self):
        self._up = (0, 1)
        self._down = (0, -1)
        self._left = (-1, 0)
        self._right = (1, 0)

        self._turn = {
            self._up: [self._left, self._right],
            self._down: [self._right, self._left],
            self._left: [self._down, self._up],
            self._right: [self._up, self._down],
        }

        self._vector = self._up

    def up(self):
        if self._vector == self._up:
            return True
        return False

    def down(self):
        if self._vector == self._down:
            return True
        return False

    def left(self):
        if self._vector == self._left:
            return True
        return False

    def right(self):
        if self._vector == self._right:
            return True
        return False

    def turn(self, code):
        if code not in [0, 1]:
            raise Exception('Invalid turn instruction')

        self._vector = self._turn[self._vector][code]
