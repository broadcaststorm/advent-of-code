#!/usr/bin/env python3
"""
Part 2: Find the first repeated frequency value

Loop over the input file (multiple times if need be),
process the frequency shifts like before but, this time, we
need to track each frequency encountered to find when we repeat
a particular frequency.

A "brute force" way to do this is simply store each value in a list
and search the entire list for a repeated value.  Since the search
is O(N), that will progressively get slower and slower which each
shift and consume progressively more memory.

My general idea - Rather than store every possible number let's create
essentially a character-based bit array.  Because I'm lazy, one for
negative and one for positive.

Also, because I don't know the maximum frequency value, provide some
logic to expand (and, lazy again, restart the process from scratch)

"""

import sys


def get_arrays(length=1000000):
    return '0'*length, '0'*length


if __name__ == '__main__':
    v = 0
    positive, negative = get_arrays(100000)

    while(True):
        print('Beginning input with frequency {}'.format(v))

        with open('input.txt', 'r') as f:
            for l in f:
                v = v + int(l.rstrip())

                # If I'm going to overrun, resize and restart
                if v > len(positive):
                    print('Bigger array needed: restarting')
                    new_length = len(positive)*10
                    positive, negative = get_arrays(new_length)
                    v = 0
                    break

                # Check to find previously found frequency
                if (v > 0):
                    check = positive
                elif (v < 0):
                    check = negative
                else:
                    print('Duplicate frequency is 0')
                    sys.exit(0)

                if int(check[v]) == 1:
                    print('Found duplicate frequency: {}'.format(v))
                    sys.exit(0)

                if (v > 0):
                    positive = positive[0:v] + '1' + positive[v+1:]
                else:
                    negative = negative[0:v] + '1' + negative[v+1:]
