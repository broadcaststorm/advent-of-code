#!/usr/bin/env python3
"""
2022/02/test_solution.py: pyunit test file for solution
"""

import solution


# Unit testing of the function against the sample data
def test_part1_sample(input_file_name="sample-part1.txt", result=15):
    """
    Unit testing of Day 1, Part 1 sample input
    """

    answer = solution.part1(filename=input_file_name)
    assert answer == result


def test_part2_sample(input_file_name="sample-part1.txt", result=12):
    """
    Unit testing of Day 1, Part 2 sample input
    """

    answer = solution.part2(filename=input_file_name)
    assert answer == result
