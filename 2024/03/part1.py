#!/usr/bin/env python3
"""
--- Day 3: Mull It Over ---

Clearly, I need to find exact pattern of mul(X,Y) where X and Y are integers
of 1-3 characters. This is a call for regular expressions.

"""

import re

mult_ops = r"""mul\(\d{1,3},\d{1,3}\)"""
mult_ops_nums = r"""mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)"""

def find_operations(memory_block: list[str], pattern: str) -> list[str]:
    """
    Need to extract the 'mul(X,Y)' matches from the memory block provided
    """

    matched_operations = list()

    for memory in memory_block:
        matches = re.findall(pattern, memory)
        matched_operations.extend(matches)
    
    return matched_operations


def multiply_and_sum(pairs: list[tuple]) -> int:

    products: list[int] = [int(x)*int(y) for x,y in pairs]
    return sum(products)


def read_input(filename: str) -> list[str]:
    """
    The input file is a single, 
    """

    memory: list[str] = list()

    with open(filename, "r") as f:
        for line in f.readlines():
            memory.append(line.strip())

    return memory


def main(filename="input.txt") -> int:
    memory_block = read_input(filename)  
    ops = find_operations(memory_block, mult_ops_nums)
    sum_of_product = multiply_and_sum(ops)
    return sum_of_product


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 1: {total}")
