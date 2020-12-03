#!/usr/bin/env python3

import sys
import re


def valid_passwords(p, passwords):
    """
    For a list of password entries of the format below, return a list of
    valid passwords (just passwords):
       min-max val: password
    """

    # The list to return
    valid = []

    # Loop over each line
    for entry in passwords:

        # Perform a match, skip this line if no match
        match = p.match(entry)
        if not match:
            print('Failed to match {0}'.format(entry))
            continue

        # Extract the results
        results = match.groupdict()

        # Sanity check
        if int(results['max']) < int(results['min']):
            raise Exception('Min and max values wrong; {0}'.format(entry))

        # Count the number using a list comprehension trick
        vals = [x for x in list(results['pass']) if x == results['val']]
        num = len(vals)

        if num < int(results['min']):
            continue

        if num > int(results['max']):
            continue

        valid.append(results['pass'])

    return valid


def specific_location_passwords(p, passwords):
    """
    Plot twist:
      - 'min' and 'max' are specific character locations.
      - 'val' is the character to be found
      - 'pass' is still the password
      - 'val' can only be found in either 'min' or 'max' but not both
    """

    specific = []

    for entry in passwords:

        # Perform a match, skip this line if no match
        match = p.match(entry)
        if not match:
            print('Failed to match {0}'.format(entry))
            continue

        results = match.groupdict()

        # The "-1" is to account for the first position being "1" in their
        # scheme and - of course - reality starts indexing at "0"
        loc1 = results['pass'][int(results['min'])-1]
        loc2 = results['pass'][int(results['max'])-1]
        val = results['val']

        # If both match, we always fail... regardless of whether it matches val
        if loc1 == loc2:
            continue

        if loc1 == val:
            specific.append(results['pass'])
            continue

        if loc2 == val:
            specific.append(results['pass'])

    return specific


if __name__ == '__main__':

    if len(sys.argv) == 1:
        input_file = 'input.txt'
    elif sys.argv[1]:
        input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        passwords = f.readlines()

    # Create and compile a regular expression with named group matches
    pattern = r'(?P<min>\d+)-(?P<max>\d+) (?P<val>\w): (?P<pass>\w+)'
    p = re.compile(pattern)

    # Get list of valid passwords
    valid = valid_passwords(p, passwords)

    print('Part one solution: {0}'.format(len(valid)))

    specific = specific_location_passwords(p, passwords)
    print('Part two solution: {0}'.format(len(specific)))
