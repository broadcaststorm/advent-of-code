#!/usr/bin/env python3


def process_codes(codes=None):
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
    print(size)

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
            return

        ###
        #   ONE parameter operations
        ###

        # Input op code
        if op == 3:
            print("Provide input parameter")
            user_input = int(input())
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
            print(codes[read_position])

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


def load_codes():
    # Input is a single CSV line in the text file
    with open('part1.txt', 'r') as f:
        line = f.readline()

    # Unlike the previous intcode problem, int() elements doesn't make sense
    codes = line.split(',')
    return codes


def test_cases():

    # Test 1 (input 1, output 1)
    codes = [3, 0, 4, 0, 99]
    process_codes(codes)

    # Test 2 (input 8, output 1; input 7, output 0)
    codes = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    process_codes(codes)
    process_codes(codes)

    # Test 3 (input 7, output 1; input 9, output 0)
    codes = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    process_codes(codes)
    process_codes(codes)

    # Test 4 (input 8, output 1; input 7, output 0)
    codes = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    process_codes(codes)
    process_codes(codes)

    # Test 5 (input 7, output 1; input 9, output 0)
    codes = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    process_codes(codes)
    process_codes(codes)

    # Test 6 (input 0, output 0, input 30, output 1)
    codes = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    process_codes(codes)
    process_codes(codes)

    # Test 7 (input 0, output 0, input 30, output 1)
    codes = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    process_codes(codes)
    process_codes(codes)


def final_test():
    # Test 8 (output 999, input<8; output 1000, input=8; output 1001, input>8)
    codes = [
        3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20,
        31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1,
        46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1,
        46, 98, 99
        ]
    process_codes(codes)
    process_codes(codes)
    process_codes(codes)


if __name__ == '__main__':

    # Real Data
    codes = load_codes()
    process_codes(codes)
