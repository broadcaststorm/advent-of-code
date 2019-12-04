#!/usr/bin/env python3
"""
part1.py - Day 2: 1202 Program Alarm

Opcode 1 = Add
Opcode 2 = Multiple
Opcode 99 = Halt

I chose to break the opcode operations, the instruction set parsing,
instruction set input, and some sample test cases into separate methods.
This turned out to be very handy for part 2 as I could import most of
this work there.

"""


class Finished(Exception):
    pass


def opcode(ops=None, x=None, y=None):
    """
    opcode(ops, x, y): method to take the operation code ops and
    operate on the x and y values accordingly. Using Exceptions
    as a convenient signaling mechanism for being finished with the
    processing.
    """

    if ops == 1:
        return x + y
    if ops == 2:
        return x * y
    if ops == 99:
        raise Finished()

    raise Exception('Unknown opcode {0}'.format(ops))


def run_codes(codes=None):
    i = 0
    j = len(codes)

    while(i < j-3):
        pos1 = codes[i+1]
        pos2 = codes[i+2]
        result = codes[i+3]

        try:
            codes[result] = opcode(codes[i], codes[pos1], codes[pos2])
        except Finished:
            break
        # Don't catch IndexError if intcode values exceed array value

        i = i + 4

    return codes


def test_cases():
    """
    test_cases() - sample input and output provided by the problem
    description for day 2.
    """

    codes = [1, 0, 0, 0, 99]
    codes = run_codes(codes)
    test = [2, 0, 0, 0, 99]

    if codes != test:
        print('Test 1 failed')
        print(codes)
        print(test)

    codes = [2, 3, 0, 3, 99]
    codes = run_codes(codes)
    test = [2, 3, 0, 6, 99]

    if codes != test:
        print('Test 2 failed')
        print(codes)
        print(test)

    codes = [2, 4, 4, 5, 99, 0]
    codes = run_codes(codes)
    test = [2, 4, 4, 5, 99, 9801]

    if codes != test:
        print('Test 3 failed')
        print(codes)
        print(test)

    codes = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    codes = run_codes(codes)
    test = [30, 1, 1, 4, 2, 5, 6, 0, 99]

    if codes != test:
        print('Test 4 failed')
        print(codes)
        print(test)


def load_codes():
    # Input is a single CSV line in the text file
    with open('part1.txt', 'r') as f:
        line = f.readline()

    codes = [int(x) for x in line.split(',')]
    return codes


if __name__ == '__main__':

    # Run some test cases
    test_cases()

    # Get the operation codes
    codes = load_codes()

    # 1202 replacement
    codes[1] = 12
    codes[2] = 2

    codes = run_codes(codes)
    print('Position 0 value is: {0}'.format(codes[0]))
