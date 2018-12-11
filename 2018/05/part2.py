#!/usr/bin/env python3

import string


def generate_opposites():
    """
    To avoid calling the "lower case" or "upper case" function all the
    time, and needing to have if statements to determine which to call,
    simply make a mapping dictionary that are key/value pairs of the
    opposites for easy reference
    """

    ret = {}
    for i in string.ascii_lowercase:
        ret[i] = i.upper()
    for i in string.ascii_uppercase:
        ret[i] = i.lower()
    ret['\n'] = ','
    ret['.'] = ','
    return ret


def get_unique_units(l):
    """
    Use set data type in Python to determine the unique units in the
    entire string.  Returned as an array, conveniently.
    """

    return set(l)


def reduce_units(l):
    """
    Original reduction algorithm from part1.  Come across two
    consecutive characters that cancel each other and remove them.
    Back up a little and check the two characters that are now adjacent
    because of the removal.
    """

    # Convert the string 
    array = list(l)

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

    return array


if __name__ == '__main__':

    opp = generate_opposites()

    # Input is just a single line
    with open('input.txt','r') as f:
        l = f.readline()

    l = l.rstrip()

    # Get a unique list of all units (characters) from the input
    # Lower case because I'm testing the removal of the lc and uc at the 
    # same time to avoid duplicates
    units = get_unique_units(l.lower())
    
    min_result = []
    min_size = len(l)

    for u in units:
        # Extract out the unit and its annihilator
        reduced = l.replace(u,'')
        reduced = reduced.replace(opp[u],'')

        # Run the normal annihilation/reduction routine
        result = reduce_units(reduced)

        # Save result if it's the smallest one seen so far
        s = len(result)
        if s < min_size:
            min_size = s
            min_result = result

    print('Puzzle 2: {}'.format(len(min_result)))
