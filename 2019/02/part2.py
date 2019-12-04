#!/usr/bin/env python3
"""
Part2.py - Find the noun and verb to produce a particular result,
namely the ISO format for the Apollo 11 moon shot 19690720

This is a parameter space search using the pre-built methods,
which I've imported.

Note: because Python "passes by reference" and "assigns by reference"
(my terminology) when assigning a list to a variable, we need to copy
the list when running the next iteration of the test (hence, the deepcopy).
Strictly speaking, given the input, a simple copy.copy would have
sufficed but deepcopy works with complex, nested data structures (like
list of lists, list of hashes, etc.)

Also note: Python has this weirdness with breaking out of double loops.
The Benevolent Dictator rejected the inclusion of labelled loops and
break LABEL syntax. Instead, you use the exception handling method
below.
"""

from copy import deepcopy
from part1 import run_codes, load_codes

if __name__ == '__main__':

    # Read in the original instruction codes
    codes = load_codes()
    target = 19690720

    # Loop over noun and verb values from 0 to 99
    try:
        for noun in range(100):
            for verb in range(100):
                test = deepcopy(codes)
                test[1] = noun
                test[2] = verb

                result = run_codes(test)

                if result[0] == target:
                    raise StopIteration

    except StopIteration:
        pass

    print('Result was {0}'.format(noun*100+verb))
