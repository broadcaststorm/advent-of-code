#!/usr/bin/env
"""
Some more class inheritance and set the default first starting point
to be white.  Created print function to output the registration data.
"""


from part1 import Robot


class Registration(Robot):
    def __init__(self, program, xmax, ymax):
        Robot.__init__(self, program, xmax, ymax)
        self.set(0, 0, 1)

    def print(self):
        for y in range(self._ymax, -self._ymax, -1):
            line = []
            for x in range(-self._xmax, self._xmax):
                value = self.get(x, y)
                line.append(self.symbol(value))
            print('{0: 3}: {1}'.format(y, ''.join(line)))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.readline()

    painter = Registration(program, 50, 6)
    count = painter.run()
    painter.print()
