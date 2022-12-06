#!/usr/bin/env python3
"""
2022/03/test_solution.py: pyunit test file for solution
"""

import solution


# Test the priority calculation function
def test_calculate_priorities():
    """
    test_calculate_priorities() - build test data and validate the fxn
    """

    test_data = [ 'A', 'a', 'M', 'm']
    prios = solution.calculate_priorities(test_data)

    assert prios[0] == 27
    assert prios[1] == 1
    assert prios[2] == 39
    assert prios[3] == 13


# Specifically test the doppel function
def test_get_duplicates():
    """
    test_get_duplicates() - build test data and validate get_duplicates()
    """

    test_data = [
        ('abcdefg', 'ghijklm'),
        ('nopqrst', 'tuvwxyz')
    ]

    doppels = solution.get_duplicates(test_data)

    assert doppels[0] == 'g'
    assert doppels[1] == 't'


def test_get_badges():
    """
    test_get_badges() - build test data and validate get_badges()
    """

    test_data = [
        'abcd', 'eafg', 'hiaj',
        'wxyz', 'tuvz', 'qzrs'
    ]

    badges = solution.get_badges(test_data)

    assert len(badges) == 2
    assert badges[0] == 'a'
    assert badges[1] == 'z'


# Unit testing of the function against the sample data
def test_part1_sample(input_file_name="sample-part1.txt", result=157):
    """
    Unit testing of Day 1, Part 1 sample input
    """

    answer = solution.part1(filename=input_file_name)
    assert answer == result


def test_part2_sample(input_file_name="sample-part1.txt", result=70):
    """
    Unit testing of Day 1, Part 2 sample input
    """

    answer = solution.part2(filename=input_file_name)
    assert answer == result
