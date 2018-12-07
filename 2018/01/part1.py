#!/usr/bin/env python3
"""
Part 1:  Determine the final frequency

Each line of the file contains the shift in frequency (v).
So, start at 0, loop over each line of the file, add the
shift to the current frequency.
"""

if __name__ == '__main__':
    v = 0
    with open('input.txt', 'r') as f:
        for l in f:
            v = v + int(l.rstrip())
    print('Frequency shift is {}'.format(v))
