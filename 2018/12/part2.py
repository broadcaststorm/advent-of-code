#!/usr/bin/env python3
"""
For 50 BILLION generations, a more sophisticated approach is needed.

We need a better memory efficient approach - namely, only adding padding
if there's a potted plant close to the edge (beginning or end)

We also need a better computationally efficient approach - as memory
serves, 10000 generations took about 10 seconds.

This second part is terribly difficult because the nature of the problem
prevents significant parallelism (previous generation dictates next
generation results).  Range of pots does present huge savings for the
parallelism effort either.

The "trick" is noticing in the "every 10k" output that the range of pots
stays the same size and all the pots are filled with plants. The program
input and generators have saturated the pots.

So, once saturated, rather than calculating each future generation, we
can "fast forward" to the end - adjusting the index values as needed.
"""

import re


def print_result(generation, current_state, left_index):
    left_hash = current_state.find('#')
    right_hash = current_state.rfind('#') + 1
    delta = right_hash - left_hash
    result = current_state[left_hash:right_hash]

    plants = 0
    for i in range(left_hash, right_hash):
        if current_state[i] == '#':
            plants = plants + (left_index + i)

    print('Generation', generation, 'Answer', plants)
    print('LeftIndex', 'LeftHash', 'RightHash', 'Range', 'Pots')
    print(left_index, left_hash, right_hash, delta, result)


if __name__ == '__main__':

    # Store all the generators
    generators = {}

    # Store the current state
    current_state = ''
    left_index = 0
    right_index = 0

    with open('input.txt', 'r') as f:

        # Get initial state
        first = f.readline().rstrip()
        label, state = first.split(':')

        # Assign current state and define solution right index
        current_state = state.lstrip()
        right_index = len(current_state)-1

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

    # Are our live pots close to the edge? If so, extend left/right
    left_hash = current_state.find('#')
    if left_hash < 2:
        current_state = '...' + current_state
        left_hash = left_hash + 3
        left_index = left_index - 3

    right_hash = current_state.rfind('#') + 1
    if len(current_state) - right_hash < 2:
        current_state = current_state + '...'
        right_index = right_index + 3

    # Prime the delta history
    previous_delta = right_index - left_index
    current_delta = right_hash - left_hash

    # Loop over all the required generations
    max_generations = 50000000000
    for n in range(0, max_generations):
        if n % 10 == 0:
            print_result(n, current_state, left_index)

        if n == 20:
            print_result(n, current_state, left_index)

        # Have we reached stable saturation - short cut to the finish
        #  1. No further growth in number of live plants
        #  2. A contiguous block of live plants
        if current_delta == previous_delta:
            if '#'*current_delta == current_state[left_hash:right_hash]:
                left_pattern = current_state[left_hash-2:left_hash+3]
                right_pattern = current_state[right_hash-3:right_hash+2]
                left_side = generators[left_pattern]
                right_side = generators[right_pattern]

                print('Fast forwarding...')

                # Stable and not moving
                if left_side == '#' and right_side == '#':
                    n = max_generations - 1
                    break

                # Stable but moving "right"
                if left_side == '.' and right_side == '#':
                    shift = max_generations - n
                    left_index = left_index + shift
                    right_index = right_index + shift
                    n = max_generations - 1
                    break

                # Stable but moving "left"
                if left_side == '#' and right_side == '.':
                    shift = max_generations - n
                    left_index = left_index - shift
                    right_index = right_index - shift
                    n = max_generations - 1
                    break

                # Unstable and shouldn't get here
                raise Exception('Should be stable')

        ###
        #   Walk the entire state and use generators to determine next
        #   generation's state
        ###

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

        # Determine if we need to pad the right end of the list
        left_hash = current_state.find('#')
        right_hash = current_state.rfind('#') + 1

        if len(current_state) - right_hash < 3:
            current_state = current_state + '...'
            right_index = right_index + 3

        previous_delta = current_delta
        current_delta = right_hash - left_hash

    print_result(n+1, current_state, left_index)
