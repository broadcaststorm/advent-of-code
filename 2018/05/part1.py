#!/usr/bin/env python3

import string


def generate_opposites():
    ret = {}
    for i in string.ascii_lowercase:
        ret[i] = i.upper()
    for i in string.ascii_uppercase:
        ret[i] = i.lower()
    ret['\n'] = ','
    ret['.'] = ','
    return ret


if __name__ == '__main__':

    # Generate map of annihilators
    opp = generate_opposites()

    # Input is just a single line
    with open('input.txt', 'r') as f:
        line = f.readline()

    # Remove the end of line junk
    line = line.rstrip()

    # Convert the string
    array = list(line)

    # Initialize the loop
    i = 1
    max = len(array)

    # Loop over the entire string
    while(i < max):

        # If annihilating units are adjacent, remove them
        if array[i] == opp[array[i-1]]:
            del array[i]
            del array[i-1]

            # Back up to compare the newly adjacent characters
            i = i - 1

            # Reduce our maximum list size to match new length
            max = max - 2
        else:
            # Nothing to see here, move along
            i = i + 1

    print('Puzzle 1: {}'.format(len(array)))
