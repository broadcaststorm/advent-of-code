#!/usr/bin/env python3

import sys


def compare(str1, str2):
    """
    compare(str1, str2) - Character by character comparison of str1
    and str2.  If only one character difference is found, return the
    string with the mismatched character spliced out.  All other
    scenarios returns False
    """

    diffs = -1

    # Comparison between different length strings non-sensical
    if len(str1) != len(str2):
        print('{} and {} different lengths'.format(str1, str2))
        return False

    # Side-by-side comparison of string
    for i in range(0, len(str1)):

        # Found character difference
        if str1[i] != str2[i]:

            # Store position if this is the first instance, abort otherwise
            if diffs == -1:
                diffs = i
            else:
                return False

    # If no differences found, abort
    if diffs == -1:
        return False

    # Only one difference found in position 'diffs'
    return str1[0:diffs] + str1[diffs+1:]


if __name__ == '__main__':

    # List of all box IDs (lines) from file
    lines = []

    # Read in entire file
    with open('input.txt', 'r') as f:
        # Remove newline character from each line before storing
        for l in f:
            lines.append(l.rstrip())

    # How many box IDs do we have
    max_boxes = len(lines)

    # First loop
    for x in range(0, max_boxes):
        # Second loop
        for y in range(0, max_boxes):
            # Skip self comparisons
            if x == y:
                next

            # Conduct detailed comparison
            result = compare(lines[x], lines[y])

            # If we find it, print the returned value and exit
            if result:
                print(result)
                sys.exit(0)
