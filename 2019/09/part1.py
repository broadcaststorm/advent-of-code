class NoMessage(Exception):
    pass


class Finished(Exception):
    pass


class Amplifier:
    def __init__(self, codes):
        # Current int code operating on
        self.current = 0

        # Relative base offset for opcode 9
        self.offset = 0

        # Intcode "programming"
        self.size = len(codes)
        self.codes = {}

        for i in range(0, self.size):
            self.codes[i] = codes[i]

        # State - amplifier program finished
        self.finished = False

        # State - input provided
        self.input_ready = False
        self.output_ready = False

        self.message = None

    def input_message(self, message):
        if self.input_ready:
            raise Exception('Clobbering existing message')

        self.input_ready = True
        self.message = message
        return

    def readout_message(self):
        if not self.output_ready:
            raise NoMessage()

        self.output_ready = False
        return self.message

    def read_code(self, position):
        if position < 0:
            raise Exception('Negative index'.format(position))

        if position in self.codes:
            return int(self.codes[position])

        return 0

    def write_code(self, position, value):
        if position < 0:
            raise Exception('Negative index'.format(position))

        if position not in self.codes:
            self.size = self.size + 1

        self.codes[position] = value

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

        r = p + self.offset
        if r < 0:
            raise Exception('Negative index {0},{1}'.format(p, self.offset))

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

        if self.finished:
            raise Finished()

        while (True):
            # Step 1: pop the first code to determine how to consume next codes
            instruction = self.read_code(self.current)

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
                self.finished = True
                raise Finished()

            ###
            #   ONE parameter operations
            ###

            # Input op code
            if op == 3:
                if not self.input_ready:
                    return None

                if modes[0] == '1':
                    print('uh oh')
                write_position = self.get_position(modes[0], self.current + 1)

                # Store input value
                self.write_code(write_position, str(self.message))
                self.input_ready = False

                # Advance to next operation
                self.current = self.current + 2
                continue

            # Output op code
            if op == 4:
                # Is my parameter positional or immediate
                read_position = self.get_position(modes[0], self.current + 1)

                # Print out the correct location
                self.message = self.read_code(read_position)
                self.output_ready = True

                # Advance to next operation
                self.current = self.current + 2
                return

            # Relative base op code
            if op == 9:
                # Get relative or immediate position
                read_position = self.get_position(modes[0], self.current + 1)

                # Adjust the base location
                self.offset = self.offset + self.read_code(read_position)

                # Advance to next operation
                self.current = self.current + 2
                continue

            ###
            #   TWO parameter operations
            ###

            # Because of the nature of these two parameters, I have to do the
            # mode logic here.  Bad form, yes.
            position = self.read_code(self.current + 1)
            if modes[0] == '2':
                position = position + self.offset
            if modes[0] == '1':
                parm1 = position
            else:
                parm1 = self.read_code(position)

            position = self.read_code(self.current + 2)
            if modes[1] == '2':
                position = position + self.offset
            if modes[1] == '1':
                parm2 = position
            else:
                parm2 = self.read_code(position)

            # Jump if true op code
            if op == 5:
                if parm1 != 0:
                    self.current = parm2
                else:
                    self.current = self.current + 3
                continue

            # Jump if not true op code
            if op == 6:
                if parm1 == 0:
                    self.current = parm2
                else:
                    self.current = self.current + 3
                continue

            ###
            #   THREE parameter operations
            ###

            parm3 = self.get_position(modes[2], self.current + 3)

            # Addition
            if op == 1:
                self.write_code(parm3, str(parm1 + parm2))
                self.current = self.current + 4
                continue

            # Multiplication
            if op == 2:
                self.write_code(parm3, str(parm1 * parm2))
                self.current = self.current + 4
                continue

            # Less than
            if op == 7:
                if parm1 < parm2:
                    self.write_code(parm3, 1)
                else:
                    self.write_code(parm3, 0)
                self.current = self.current + 4
                continue

            # Equal
            if op == 8:
                if parm1 == parm2:
                    self.write_code(parm3, 1)
                else:
                    self.write_code(parm3, 0)
                self.current = self.current + 4
                continue

            # Unknown op code
            raise Exception('Iter {0}: op code {1}'.format(self.current, op))

        raise Exception('End of loop without termination')


def run_test_case(codes):

    answer = []
    boost = Amplifier(codes)

    while(not boost.finished):
        try:
            boost.process_codes()
            output = boost.readout_message()
            answer.append(str(output))
        except Finished:
            break

    return answer


def load_codes(filename='part1.txt'):
    # Input is a single CSV line in the text file
    with open(filename, 'r') as f:
        line = f.readline()

    # Unlike the previous intcode problem, int() elements doesn't make sense
    codes = line.split(',')
    return codes


def test_cases():
    # Test Case 1
    codes = load_codes('sample1.txt')
    output = run_test_case(codes)
    assert(codes == output)
    print('Pass Test 1')

    # Test Case 2
    codes = load_codes('sample2.txt')
    output = run_test_case(codes)
    assert(int(output[0]) == 1219070632396864)
    print('Pass Test 2')

    # Test Case 3
    codes = load_codes('sample3.txt')
    output = run_test_case(codes)
    assert(int(output[0]) == 1125899906842624)
    print('Pass Test 3')


def run_program(codes, input):
    boost = Amplifier(codes)
    boost.input_message(input)

    while(not boost.finished):
        try:
            boost.process_codes()
            if boost.output_ready:
                answer = boost.readout_message()
        except Finished:
            break

    return answer


if __name__ == '__main__':
    test_cases()

    codes = load_codes('input.txt')
    answer = run_program(codes, 1)
    print('BOOST Keycode is {0}'.format(answer))

    codes = load_codes('input.txt')
    answer = run_program(codes, 2)
    print('Coordinates are {0}'.format(answer))
