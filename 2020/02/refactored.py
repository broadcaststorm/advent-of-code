#!/usr/bin/env python3
"""
After writing the first form of the solution - which I try not to hack the
"part 1" effort to build the "part 2" result UNLESS there is an obvious
refactor requirement built into the story - there's an obvious simple
trick I can do with passing methods.
"""

import sys
import re


def policy_part_one(results):
    """
    Password policy for part one of the problem:
      - results['val'] contains the character to count
      - results['min'] and results['max'] provide the inclusive required count
      - results['pass'] is the password to check
    Return true if valid, return false if not.

    If the min > max, raise an exception
    """

    # Sanity check
    if int(results['max']) < int(results['min']):
        raise Exception('Min and max values wrong; {0}'.format(results))

    # Count the number using a list comprehension trick
    vals = [x for x in list(results['pass']) if x == results['val']]
    num = len(vals)

    if num < int(results['min']):
        return False

    if num > int(results['max']):
        return False

    return True


def policy_part_two(results):
    """
    Password policy for part two of the problem:
    Plot twist:
      - 'min' and 'max' are specific character locations.
      - 'val' is the character to be found
      - 'pass' is still the password
      - 'val' can only be found in either 'min' or 'max' but not both
    """

    # The "-1" is to account for the first position being "1" in their
    # scheme and - of course - reality starts indexing at "0"
    loc1 = results['pass'][int(results['min'])-1]
    loc2 = results['pass'][int(results['max'])-1]
    val = results['val']

    # If both match, we always fail... regardless of whether it matches val
    if loc1 == loc2:
        return False

    if loc1 == val:
        return True

    if loc2 == val:
        return True

    return False


def valid_passwords(p, passwords, policy):
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

        if policy(results):
            valid.append(results['pass'])

    return valid


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

    # Get list of valid passwords. Pass the policy method as an argument
    part1 = valid_passwords(p, passwords, policy_part_one)
    print('Part one solution: {0}'.format(len(part1)))

    part2 = valid_passwords(p, passwords, policy_part_two)
    print('Part two solution: {0}'.format(len(part2)))
