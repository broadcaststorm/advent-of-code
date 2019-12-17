#!/usr/bin/env python3
"""
Duplicate Day 5 code, extend to automate the inputs

"""


from itertools import permutations


def process_codes(codes=None, inputs=None):
    """
    ABCDE
     1002
        DE - two-digit opcode,      02 == opcode 2
        C - mode of 1st parameter,  0 == position mode
        B - mode of 2nd parameter,  1 == immediate mode
        A - mode of 3rd parameter,  0 == position mode,
                                         omitted due to being a leading zero
    """

    i = 0
    size = len(codes)
    result = 0

    while (i < size):
        # Step 1: pop the first code to determine how to consume next codes
        instruction = int(codes[i])

        # Parse the instruction
        op = instruction % 100
        modes = '{0:03d}'.format(instruction // 100)
        positional = [modes[2] == '0', modes[1] == '0', modes[0] == '0']

        ###
        #   ZERO parameter operations
        ###

        # Terminate op code
        if op == 99:
            return result

        ###
        #   ONE parameter operations
        ###

        # Input op code
        if op == 3:
            if inputs is None:
                print("Provide input parameter")
                user_input = int(input())
            elif len(inputs) == 0:
                print("Provide input parameter")
                user_input = int(input())
            else:
                user_input = inputs.pop(0)
            write_position = int(codes[i + 1])

            # Store input value
            codes[write_position] = str(user_input)

            # Advance to next operation
            i = i + 2
            continue

        # Output op code
        if op == 4:
            # Is my parameter positional or immediate
            if positional[0]:
                read_position = int(codes[i + 1])
            else:
                read_position = i + 1

            # Print out the correct location
            result = int(codes[read_position])

            # Advance to next operation
            i = i + 2
            continue

        ###
        #   TWO parameter operations
        ###
        next_int = int(codes[i + 1])
        if positional[0]:
            parm1 = int(codes[next_int])
        else:
            parm1 = next_int

        next_int = int(codes[i + 2])
        if positional[1]:
            parm2 = int(codes[next_int])
        else:
            parm2 = next_int

        # Jump if true op code
        if op == 5:
            if parm1 != 0:
                i = parm2
            else:
                i = i + 3
            continue

        # Jump if not true op cope
        if op == 6:
            if parm1 == 0:
                i = parm2
            else:
                i = i + 3
            continue

        ###
        #   THREE parameter operations
        ###

        if positional[2]:
            parm3 = int(codes[i + 3])
        else:
            parm3 = i + 3

        # Addition
        if op == 1:
            codes[parm3] = str(parm1 + parm2)
            i = i + 4
            continue

        # Multiplication
        if op == 2:
            codes[parm3] = str(parm1 * parm2)
            i = i + 4
            continue

        # Less than
        if op == 7:
            if parm1 < parm2:
                codes[parm3] = 1
            else:
                codes[parm3] = 0
            i = i + 4
            continue

        # Equal
        if op == 8:
            if parm1 == parm2:
                codes[parm3] = 1
            else:
                codes[parm3] = 0
            i = i + 4
            continue

        # Unknown op code
        raise Exception('Iter {0}: Unknown op code {1}'.format(i, op))

    raise Exception('End of loop without termination')


def run_amplifier(codes, phases):
    output = 0

    for i in phases:
        output = process_codes(codes, [i, output])

    return output


def test_cases():
    final = 43210
    codes = load_codes('test1.txt')
    phases = [4, 3, 2, 1, 0]

    output = run_amplifier(codes, phases)

    if final != output:
        print('{0}/{1} mismatch with {2}'.format(output, final, phases))
    else:
        print('Passed test 1: {0}'.format(final))

    final = 54321
    codes = load_codes('test2.txt')
    phases = [0, 1, 2, 3, 4]

    output = run_amplifier(codes, phases)

    if final != output:
        print('{0}/{1} mismatch with {2}'.format(output, final, phases))
    else:
        print('Passed test 2: {0}'.format(final))

    final = 65210
    codes = load_codes('test3.txt')
    phases = [1, 0, 4, 3, 2]

    output = run_amplifier(codes, phases)

    if final != output:
        print('{0}/{1} mismatch with {2}'.format(output, final, phases))
    else:
        print('Passed test 3: {0}'.format(final))


def load_codes(filename='part1.txt'):
    # Input is a single CSV line in the text file
    with open(filename, 'r') as f:
        line = f.readline()

    # Unlike the previous intcode problem, int() elements doesn't make sense
    codes = line.split(',')
    return codes


def generate_phases(elements):
    return list(permutations(elements))


if __name__ == '__main__':

    test_cases()

    # Real Data
    codes = load_codes()
    output = 0
    phases = generate_phases([0, 1, 2, 3, 4])

    for p in phases:
        result = run_amplifier(codes, p)
        if result > output:
            output = result

    print('Highest signal to thrusters: {0}'.format(output))
