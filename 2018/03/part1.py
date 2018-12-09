#!/usr/bin/env python3
"""
In this solution, since this screamed 2D array, I felt like resurrecting
my use of scientific modules like NumPy.  Not strictly required but was
fun bringing back some of the old days :)

Used a few methods to create a compiled regex and parse each line.

General idea is simple - start out with a '0' initialized 2D array and
add '1' in each cell that the patch of cloth is supposed to consume.
Simply count the cells that have a patch count of more than '1'.

"""

import re
import numpy as np


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
    grid = np.zeros((1000, 1000), dtype=np.uint8)

    with open('input.txt', 'r') as f:
        for l in f:
            claim, x, y, l, w = parse_line(parse, l)

            for i in range(x, x+l):
                for j in range(y, y+w):
                    grid[i][j] = grid[i][j] + 1

    nx, ny = grid.shape
    num_overlap = 0

    for i in range(0, nx):
        for j in range(0, ny):
            if grid[i][j] > 1:
                num_overlap = num_overlap + 1

    print(num_overlap)
