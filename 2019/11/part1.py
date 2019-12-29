#!/usr/bin/env python3
"""
For this day's problem, decided to really leverage pre-existing code in the
form of classes and use multiple class inheritance.  Cleaned up several of
the previous day's efforts into those classes (Grid, IntCode) so that there
wasn't instance variable name overlap.

"""


from IntCode import Finished, IntCode
from Grid import Grid
from Direction import Direction


class Robot(IntCode, Direction, Grid):
    def __init__(self, program, xmax, ymax):
        # Color options
        self.__black = 0
        self.__white = 1

        # Location
        self.location = [0, 0]

        IntCode.__init__(self, program)
        Direction.__init__(self)
        Grid.__init__(self, xmax=xmax, ymax=ymax, default=self.__black)

    def symbol(self, instruction):
        if instruction == self.__black:
            return '.'
        if instruction == self.__white:
            return '#'
        raise Exception('Invalid color {0}'.format(instruction))

    def step(self):
        x = self.location[0]
        y = self.location[1]

        # Read the current position and use as input
        input_instruction = self.get(x, y)
        self.input_message(input_instruction)

        # Extract the new color
        self.process_codes()
        color = self.readout_message()
        self.set(x, y, int(color))

        # Extract the new direction
        self.process_codes()
        turn = self.readout_message()
        self.turn(int(turn))

        # Moved to new spot
        self.location = [
            self.location[0] + self._vector[0],
            self.location[1] + self._vector[1]
        ]

    def count_panels(self):
        return len(self._grid.values())

    def run(self):
        while(True):
            try:
                self.step()
            except Finished:
                break

        count = self.count_panels()
        return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.readline()

    painter = Robot(program, 70, 40)
    count = painter.run()
    print(count)
