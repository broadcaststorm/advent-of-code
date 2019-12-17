#!/usr/bin/env python3
"""
So my original design of Amp A completes, feeds into Amp B, etc.
doesn't work with part 2.  Amp A will get to a point it needs input
from Amp E after printing out the input for Amp B.

So now I have to track 5 amplifier states and retool the machine
to return the output when its generated.

To maintain the various states, I'll build an Amplifier class that will
get 5 instances created with its own independent set of Intcodes.  I need
to retool the input and output logic to store/fetch those values before/after
the process_code method gets called.  The "finished" state needs augmenting
too.

It would appear from the messaging I built in that the problem set was
designed such that all 5 amplifiers were Finished in the same iteration.
"""


from copy import copy
from part1 import load_codes, generate_phases
from part1 import test_cases as part1_test_cases


class NoMessage(Exception):
    pass


class Finished(Exception):
    pass


class Amplifier:
    def __init__(self, codes):
        # Current int code operating on
        self.current = 0

        # Intcode "programming"
        self.codes = codes
        self.size = len(codes)

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

        while (self.current < self.size):
            # Step 1: pop the first code to determine how to consume next codes
            instruction = int(self.codes[self.current])

            # Parse the instruction
            op = instruction % 100
            modes = '{0:03d}'.format(instruction // 100)
            positional = [modes[2] == '0', modes[1] == '0', modes[0] == '0']

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

                write_position = int(self.codes[self.current + 1])

                # Store input value
                self.codes[write_position] = str(self.message)
                self.input_ready = False

                # Advance to next operation
                self.current = self.current + 2
                continue

            # Output op code
            if op == 4:
                # Is my parameter positional or immediate
                if positional[0]:
                    read_position = int(self.codes[self.current + 1])
                else:
                    read_position = self.current + 1

                # Print out the correct location
                self.message = int(self.codes[read_position])
                self.output_ready = True

                # Advance to next operation
                self.current = self.current + 2
                return

            ###
            #   TWO parameter operations
            ###
            next_int = int(self.codes[self.current + 1])
            if positional[0]:
                parm1 = int(self.codes[next_int])
            else:
                parm1 = next_int

            next_int = int(self.codes[self.current + 2])
            if positional[1]:
                parm2 = int(self.codes[next_int])
            else:
                parm2 = next_int

            # Jump if true op code
            if op == 5:
                if parm1 != 0:
                    self.current = parm2
                else:
                    self.current = self.current + 3
                continue

            # Jump if not true op cope
            if op == 6:
                if parm1 == 0:
                    self.current = parm2
                else:
                    self.current = self.current + 3
                continue

            ###
            #   THREE parameter operations
            ###

            if positional[2]:
                parm3 = int(self.codes[self.current + 3])
            else:
                parm3 = self.current + 3

            # Addition
            if op == 1:
                self.codes[parm3] = str(parm1 + parm2)
                self.current = self.current + 4
                continue

            # Multiplication
            if op == 2:
                self.codes[parm3] = str(parm1 * parm2)
                self.current = self.current + 4
                continue

            # Less than
            if op == 7:
                if parm1 < parm2:
                    self.codes[parm3] = 1
                else:
                    self.codes[parm3] = 0
                self.current = self.current + 4
                continue

            # Equal
            if op == 8:
                if parm1 == parm2:
                    self.codes[parm3] = 1
                else:
                    self.codes[parm3] = 0
                self.current = self.current + 4
                continue

            # Unknown op code
            raise Exception('Iter {0}: op code {1}'.format(self.current, op))

        raise Exception('End of loop without termination')


def run_amplifier(codes, phase):

    amplifiers = []

    # Initial the 5 machines
    for p in phase:
        # Create the amplifier
        amp = Amplifier(copy(codes))

        # Set the amplifier phase
        amp.input_message(p)
        amp.process_codes()

        # Create feedback loop
        amplifiers.append(amp)

    # Now let's loop through the amplifiers taking the output of one
    # in feeding it into the next
    current = 0
    n = len(phase)

    output = 0
    finished = 0

    while(finished < n):
        try:
            if not amplifiers[current].finished:
                amplifiers[current].input_message(output)
                amplifiers[current].process_codes()
                output = amplifiers[current].readout_message()
            else:
                print('Amp {0} done, total done {1}'.format(current, finished))
        except Finished:
            # Termination condition
            if amplifiers[current].finished:
                finished = finished + 1

        current = (current + 1) % n

    return output


def test_cases():
    part1_test_cases()

    final = 139629729
    codes = load_codes('test4.txt')
    phase = [9, 8, 7, 6, 5]

    output = run_amplifier(codes, phase)

    if final != output:
        print('{0}/{1} mismatch with {2}'.format(output, final, phase))
    else:
        print('Passed test 4: {0}'.format(final))

    final = 18216
    codes = load_codes('test5.txt')
    phase = [9, 7, 8, 5, 6]

    output = run_amplifier(codes, phase)

    if final != output:
        print('{0}/{1} mismatch with {2}'.format(output, final, phase))
    else:
        print('Passed test 5: {0}'.format(final))


if __name__ == '__main__':

    test_cases()

    codes = load_codes('part1.txt')
    phases = generate_phases([5, 6, 7, 8, 9])

    max = 0
    for p in phases:
        output = run_amplifier(codes, p)
        if output > max:
            max = output

    print('Max signal to thrusters: {0}'.format(max))
