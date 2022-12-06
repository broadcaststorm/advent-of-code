#!/usr/bin/env python3
"""
2022/04/solution.py: Python based solution of day 4 problem.

A similar theme to yesterday, finding overlapping sets in ranges of data.
For part 1, the overlaps are in number ranges, rather than yesterdays
characters in a string.

Learn lesson from yesterday: create separate functions for reading in entire
data set and then slicing the data set

"""

from typing import List, Tuple


def get_partial_overlaps(assignments: List[Tuple]) -> List[int]:
    """
    get_partial_overlaps(assignments) - determine overlaps based on
    set operations, namely intersection
    """

    overlaps = list()

    for i, elf in enumerate(assignments):
        if len(set(elf[0]) & set(elf[1])):
            overlaps.append(i)

    return overlaps


def get_complete_overlaps(assignments: List[Tuple]) -> List[int]:
    """
    get_complete_overlaps(assignments) - determine overlaps based on
    set operations, namely "superset"
    """

    overlaps = list()

    for i, elf in enumerate(assignments):
        s = set(elf[0])
        t = set(elf[1])

        if s.issubset(t) or s.issuperset(t):
            overlaps.append(i)

    return overlaps


def get_section_ranges(filename: str) -> List[Tuple]:
    """
    get_section_ranges(filename) - read each line in file, split the CSV
    entries (each one belongs to an elf in a pair), then explode the number
    range into a full list
    """

    pairs = list()

    # Loop over each line of the file (elf pairs)
    with open(file=filename, mode='r', encoding='UTF-8') as f_obj:
        for line in f_obj:

            # Separate the pairs into list elements
            this_pair = line.strip().split(',')
            sections = list()

            # Loop over each elf
            for elf in this_pair:

                # Extract the start and stop ranges
                start, stop = elf.split('-')

                # Create a full list of sections IDs for this elf
                # The +1 is to account for range() behavior (end not included)
                # The list is to force the range() iterator to generate them

                sections.append(
                    list(
                        range(
                            int(start.strip()),
                            int(stop.strip())+1
                        )
                    )
                )

            # Store the two elf assigned section ID lists as a tuple (not list)
            pairs.append(tuple(sections))

    return pairs


def part1(filename: str = 'input.txt'):
    """
    part1(filename): solve part 1 of day 4!
    """

    # Get the elf pair assigned cleaning sections
    cleaning_assignments = get_section_ranges(filename)

    # Loop over the assignments and find the inclusive sections
    complete_overlaps = get_complete_overlaps(cleaning_assignments)

    return len(complete_overlaps)


def part2(filename: str = 'input.txt'):
    """
    part2(filename): solve part 2 of day 4!
    """

    # Get the elf pair assigned cleaning sections
    cleaning_assignments = get_section_ranges(filename)

    # Loop over the assignments and find the partial overlaps
    partial_overlaps = get_partial_overlaps(cleaning_assignments)

    return len(partial_overlaps)


if __name__ == '__main__':

    # Solve part1
    result = part1(filename='input-part1.txt')
    print(f'Result is {result}')

    # Solve part2
    output = part2(filename='input-part1.txt')
    print(f'Output is {output}')
