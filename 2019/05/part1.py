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

    while (i < size):
        # Step 1: pop the first code to determine how to consume next codes
        instruction = int(codes[i])

        # Parse the instruction
        op = instruction % 100
        modes = '{0:03d}'.format(instruction // 100)
        positional = [modes[2] == '0', modes[1] == '0', modes[0] == '0']

        # Terminate op code
        if op == 99:
            return

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

        # For op codes 1 and 2 (remaining codes), let's fetch the noun/verb
        next_int = int(codes[i + 1])
        if positional[0]:
            noun = int(codes[next_int])
        else:
            noun = next_int

        next_int = int(codes[i + 2])
        if positional[1]:
            verb = int(codes[next_int])
        else:
            verb = next_int

        if positional[2]:
            out_location = int(codes[i + 3])
        else:
            out_location = i + 3

        # Addition
        if op == 1:
            codes[out_location] = str(noun + verb)
            i = i + 4
            continue

        # Multiplication
        if op == 2:
            codes[out_location] = str(noun * verb)
            i = i + 4
            continue

        # Unknown op code
        raise Exception('Unknown op code {0}'.format(op))

    raise Exception('End of loop without termination')


def load_codes():
    # Input is a single CSV line in the text file
    with open('part1.txt', 'r') as f:
        line = f.readline()

    # Unlike the previous intcode problem, int() elements doesn't make sense
    codes = line.split(',')
    return codes


if __name__ == '__main__':

    # Test 1
    codes = [3, 0, 4, 0, 99]
    process_codes(codes)

    # Real Data
    codes = load_codes()
    process_codes(codes)
