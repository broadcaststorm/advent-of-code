#!/usr/bin/env python3
"""
Essentially, the fundamental challenge is data transformation filter
based on related data points (+/- 2 from center point).

Created a "generator" dictionary with the 5 character filter as the key
and the 1 character result (either . or #) as the value.

The edge cases (beginning and end) of the current state of the plants in
the pot required adding additional "empty pots" on the beginning and the
end of the current state vector before applying the sliding generator
filter.

A more sophisticated approach would leverage the left_hash, right_hash,
and delta values to only store the number of characters needed while
also tracking what the new state vector's "0" and "max-1" indices really
mapped to in the solution set.

Fortunately, for 19 generations, the state length isn't that large and
the excessive padding isn't memory intensive.
"""

import re


def print_result(generation, current_state, zero_index):
    left_hash = current_state.find('#') - 1
    right_hash = current_state.rfind('#') + 2
    delta = right_hash - left_hash
    result = current_state[left_hash:right_hash]

    plants = 0
    for i in range(0, len(current_state)):
        if current_state[i] == '#':
            plants = plants + (i - zero_index)

    # Generation in problem starts at 1, in software starts at 0
    print('Generation', 'Sum', 'LeftHash', 'RightHash', 'HashDelta', 'Pots')
    print(generation+1, plants, left_hash, right_hash, delta, result)


if __name__ == '__main__':

    # Store all the generators
    generators = {}

    # Store the current state
    current_state = ''
    zero_index = 0

    with open('input.txt', 'r') as f:

        # Get initial state
        first = f.readline().rstrip()
        label, state = first.split(':')

        # We pad the beginning and end by 3 each for the sliding window
        current_state = '...' + state.lstrip() + '...'
        zero_index = 3

        # Skip blank line
        f.readline()

        parse = re.compile(r'(?P<pattern>.+) => (?P<result>.)')

        # Read the state changes
        for l in f:
            match = parse.match(l)
            pattern = match.group('pattern')
            result = match.group('result')

            if pattern in generators:
                raise Exception('Duplicate patterns {}'.format(pattern))

            generators[pattern] = result

    for n in range(0, 20):
        # Set up result list
        current_result = ['.']*len(current_state)
        max = len(current_state)

        # Walk the list of states (assume ends are padded)
        for i in list(range(2, max-2)):
            pattern = current_state[i-2:i+3]

            if pattern not in generators:
                generators[pattern] = '.'

            current_result[i] = generators[pattern]

        current_state = ''.join(current_result)

        # Arbitrarily keep padding the beginning and ends to ensure we
        # aren't possibly missing some pot plant generation
        current_state = '..' + current_state + '..'
        zero_index = zero_index + 2

    print_result(n, current_state, zero_index)
