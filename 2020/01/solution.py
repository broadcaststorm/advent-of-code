#!/usr/bin/env python3

import sys


def part_one(numbers, target=2020):
    """
    Pass me a list of integers, I'll find two numbers that add to target
    """
    for i, n in enumerate(numbers):
        for m in numbers[i+1:]:
            if n + m == sum:
                return n, m


def part_two(numbers, target=2020):
    """
    Pass me a list of integers, I'll find three numbers that add to target
    """
    for i, m in enumerate(numbers):
        for j, n in enumerate(numbers[i+1:]):
            for o in numbers[j+1:]:
                if o + n + m == sum:
                    return o, n, m


if __name__ == '__main__':

    sum = 2020

    if len(sys.argv) == 1:
        input_file = 'input.txt'
    elif sys.argv[1]:
        input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        numbers = [int(n) for n in f.readlines()]

    n, m = part_one(numbers)
    print(n*m)

    a, b, c = part_two(numbers)
    print(a*b*c)
