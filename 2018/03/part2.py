#!/usr/bin/env python3
"""
This approach is somewhat different in that I now have to track which
claim has no overlaps - i.e. an approach that is claim-centric rather
than cell-centric.  So I chose a different approach - this time relying
on 2D-coordinates (in tuple format) as keys to a dict whose values were
claim numbers.

In short, the dictionary now is a dynamically allocated grid of max size
x,y who values at each coordinate is a list of claims wanting that x,y
coordinate.

The trick is that if one (x,y) value of a claim overlaps, the whole
claim must be invalid in the search.  So, as we are processing the
claims, we simply invalidate as we discover them.

"""

import re


def compile_parser():
    regex = r"#(?P<claim>\d+) @ (?P<x>\d+),(?P<y>\d+)"
    regex = r"{}: (?P<l>\d+)x(?P<w>\d+)".format(regex)
    parse = re.compile(regex)

    return parse


def parse_line(parse, line):
    result = parse.match(line)
    return (int(result.group('claim')),
            int(result.group('x')), int(result.group('y')),
            int(result.group('l')), int(result.group('w')))


if __name__ == '__main__':

    parse = compile_parser()
    grid = {}
    overlap = {}

    with open('input.txt', 'r') as f:
        for l in f:
            claim, x, y, l, w = parse_line(parse, l)

            for i in range(x, x+l):
                for j in range(y, y+w):
                    idx = (i, j)
                    if idx not in grid:
                        grid[idx] = [claim]
                    else:
                        # Found first overlap, invalidate previous claim number
                        if len(grid[idx]) == 1:
                            if grid[idx][0] not in overlap:
                                overlap[grid[idx][0]] = 0
                        # Invalidate new claim number too
                        if claim not in overlap:
                            overlap[claim] = 0
                        # Store claim
                        grid[idx].append(claim)

    num_overlap = 0
    unique = []

    for idx in grid.keys():
        if len(grid[idx]) > 1:
            num_overlap = num_overlap + 1
        if (len(grid[idx]) == 1) and (grid[idx][0] not in overlap):
            if grid[idx][0] not in unique:
                unique.append(grid[idx][0])

    print('Number of overlapping cells: {}'.format(num_overlap))
    print('Claims with no overlaps:')
    for u in unique:
        print('\t{}'.format(u))
