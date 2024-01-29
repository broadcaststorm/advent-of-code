#!/usr/bin/env python3
"""
2022/template/test_solution.py: pyunit test file for solution
"""

import solution


# Unit testing of the function against the sample data
def test_part1_sample(input_file_name="sample1.txt", result=142):
    """
    Unit testing of Part 1 sample input
    """

    answer = solution.part1(filename=input_file_name)
    assert answer == result


def test_part2_sample(input_file_name="sample2.txt", result=281):
    """
    Unit testing of Part 2 sample input
    """

    answer = solution.part2(filename=input_file_name)
    assert answer == result
