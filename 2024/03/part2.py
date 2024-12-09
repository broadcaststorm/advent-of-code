#!/usr/bin/env python3
"""
--- Day 3: Mull It Over ---

Clearly, I need to find exact pattern of mul(X,Y) where X and Y are integers
of 1-3 characters. This is a call for regular expressions.

In part 2, we now need to actually treat this as a state machine and process
the memory block in a more linear fashion. Fortunately, since this 'do()' and
"don't()" toggles are literal (meaning, they don't encapsulate the ops they
affect), we don't need to regex those toggles.

"""

import re

mult_ops = r"""mul\(\d{1,3},\d{1,3}\)"""
mult_ops_nums = r"""mul\((?P<first>\d{1,3}),(?P<second>\d{1,3})\)"""

enabled_text = r"""do()"""
disabled_text = r"""don't()"""


def select_enabled(pattern: str, memory: str, ops_enabled: bool) -> tuple[list, bool]:

    results = list()

    # We need to find the range of text to search
    if ops_enabled:
        # If we inherited an enabled condition, start at 0
        start_idx = 0
    else:
        # Otherwise, identify where the next "enabled" marker is
        start_idx = memory.find(enabled_text)

        # If we didn't find it, simply return (passing "false" back)
        if start_idx == -1:
            return results, ops_enabled

    # Now find the stop index based on the identified starting point
    stop_idx = memory.find(disabled_text, start_idx)

    # If the stop text wasn't found, choose the end
    if stop_idx == -1:
        stop_idx = None

    # Okay search for operations in the selected substring
    matches = re.findall(pattern, memory[start_idx:stop_idx])
    if matches:
        results.extend(matches)

    # Okay, if we are at the end of the string, we are finished!
    if stop_idx == None:
        # If we made it here, we had an "enabled" state and didn't find a stop (None)
        return results, True
    else:
        # We found a stop point, meaning there's additional text to process
        matches, new_state = select_enabled(pattern, memory[stop_idx:], False)
        if matches:
            results.extend(matches)
        return results, new_state


def find_operations(memory_block: list[str], pattern: str) -> list[str]:
    """
    Need to extract the 'mul(X,Y)' matches from the memory block provided
    """

    matched_operations = list()
    ops_enabled: bool = True

    for memory in memory_block:
        matches, new_state = select_enabled(pattern, memory, ops_enabled)
        matched_operations.extend(matches)
        ops_enabled = new_state
    
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


def main(filename="sample1.txt") -> int:
    memory_block = read_input(filename)  
    ops = find_operations(memory_block, mult_ops_nums)
    sum_of_product = multiply_and_sum(ops)
    return sum_of_product


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 1: {total}")
