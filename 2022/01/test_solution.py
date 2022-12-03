#!/usr/bin/env python3

import solution

# Unit testing of the function against the sample data
def test_part1_sample(input_file_name="sample-part1.txt", result=24000):
    """
    Unit testing of Day 1, Part 1 sample input
    """

    entry = solution.part1(input_file_name)
    assert entry[0] == result


def test_part2_sample(input_file_name="sample-part1.txt", result=45000):
    """
    Unit testing of Day 1, Part 2 sample input
    """

    calories = solution.part2(input_file_name)
    assert calories == result
