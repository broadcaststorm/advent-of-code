#!/usr/bin/env python3


class NoMessage(Exception):
    pass


class Finished(Exception):
    pass


class IntCode:
    """
    IntCode(program) - assumes you have read the single line, string of
    CSV entries that represent the IntCode programming.
    """
    def __init__(self, program):
        # Current int code operating on
        self._current = 0

        # Relative base offset for opcode 9
        self._offset = 0

        # Intcode "programming" - I chose to use a dictionary because we
        # have to allow for write to the program "beyond the end" of the
        # program
        self._codes = {}
        for i, item in enumerate(program.split(',')):
            self._codes[i] = item

        self._size = len(list(self._codes.keys()))

        # State - amplifier program finished
        self._finished = False

        # State - input provided
        self._input_ready = False

        # State - output ready for readout
        self._output_ready = False
        self._message = None

    def input_message(self, message):
        if self._input_ready:
            raise Exception('Clobbering existing message')

        self._input_ready = True
        self._message = message
        return

    def readout_message(self):
        if not self._output_ready:
            raise NoMessage()

        self._output_ready = False
        return self._message

    def read_code(self, position):
        if position < 0:
            raise Exception('Negative index'.format(position))

        if position in self._codes:
            return int(self._codes[position])

        return 0

    def write_code(self, position, value):
        if position < 0:
            raise Exception('Negative index'.format(position))

        if position not in self._codes:
            self._size = self._size + 1

        self._codes[position] = value

    def get_position(self, mode, position):
        """
        3 mode values:
            0 == position mode (next parameter indicates next memory location)
            1 == immediate mode (next parameter IS the location)
            2 == relative mode (next parameter indicates next relative mem loc)
        """

        if position < 0:
            raise Exception("Position OOB {0}".format(position))

        # Immediate first
        if mode == '1':
            return position

        p = self.read_code(position)
        if mode == '0':
            return p

        r = p + self._offset
        if r < 0:
            raise Exception('Negative index {0},{1}'.format(p, self._offset))

        if mode == '2':
            return r

        raise Exception('Invalid mode {0}'.format(mode))

    def process_codes(self):
        """
        ABCDE
        1002
            DE - two-digit opcode,      02 == opcode 2
            C - mode of 1st parameter,  0 == position mode
            B - mode of 2nd parameter,  1 == immediate mode
            A - mode of 3rd parameter,  0 == position mode,
                                            omitted due to being a leading zero
        """

        if self._finished:
            raise Finished()

        while (True):
            # Step 1: pop the first code to determine how to consume next codes
            instruction = self.read_code(self._current)

            # Parse the instruction
            op = instruction % 100
            modes = '{0:03d}'.format(instruction // 100)
            modes = list(modes)
            modes.reverse()

            ###
            #   ZERO parameter operations
            ###

            # Terminate op code
            if op == 99:
                self._finished = True
                raise Finished()

            ###
            #   ONE parameter operations
            ###

            # Input op code
            if op == 3:
                if not self._input_ready:
                    return None

                if modes[0] == '1':
                    print('uh oh')
                write_position = self.get_position(modes[0], self._current + 1)

                # Store input value
                self.write_code(write_position, str(self._message))
                self._input_ready = False

                # Advance to next operation
                self._current = self._current + 2
                continue

            # Output op code
            if op == 4:
                # Is my parameter positional or immediate
                read_position = self.get_position(modes[0], self._current + 1)

                # Print out the correct location
                self._message = self.read_code(read_position)
                self._output_ready = True

                # Advance to next operation
                self._current = self._current + 2
                return

            # Relative base op code
            if op == 9:
                # Get relative or immediate position
                read_position = self.get_position(modes[0], self._current + 1)

                # Adjust the base location
                self._offset = self._offset + self.read_code(read_position)

                # Advance to next operation
                self._current = self._current + 2
                continue

            ###
            #   TWO parameter operations
            ###

            # Because of the nature of these two parameters, I have to do the
            # mode logic here.  Bad form, yes.
            position = self.read_code(self._current + 1)
            if modes[0] == '2':
                position = position + self._offset
            if modes[0] == '1':
                parm1 = position
            else:
                parm1 = self.read_code(position)

            position = self.read_code(self._current + 2)
            if modes[1] == '2':
                position = position + self._offset
            if modes[1] == '1':
                parm2 = position
            else:
                parm2 = self.read_code(position)

            # Jump if true op code
            if op == 5:
                if parm1 != 0:
                    self._current = parm2
                else:
                    self._current = self._current + 3
                continue

            # Jump if not true op code
            if op == 6:
                if parm1 == 0:
                    self._current = parm2
                else:
                    self._current = self._current + 3
                continue

            ###
            #   THREE parameter operations
            ###

            parm3 = self.get_position(modes[2], self._current + 3)

            # Addition
            if op == 1:
                self.write_code(parm3, str(parm1 + parm2))
                self._current = self._current + 4
                continue

            # Multiplication
            if op == 2:
                self.write_code(parm3, str(parm1 * parm2))
                self._current = self._current + 4
                continue

            # Less than
            if op == 7:
                if parm1 < parm2:
                    self.write_code(parm3, 1)
                else:
                    self.write_code(parm3, 0)
                self._current = self._current + 4
                continue

            # Equal
            if op == 8:
                if parm1 == parm2:
                    self.write_code(parm3, 1)
                else:
                    self.write_code(parm3, 0)
                self._current = self._current + 4
                continue

            # Unknown op code
            raise Exception('Iter {0}: op code {1}'.format(self._current, op))

        raise Exception('End of loop without termination')
