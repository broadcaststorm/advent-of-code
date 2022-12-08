#!/usr/bin/env python3
"""
2022/template/test_solution.py: pyunit test file for solution
"""

import solution


# Unit testing of the function against the sample data
def test_part1_sample():
    """
    Unit testing of Day 1, Part 1 sample input
    """

    test_data = {
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
        "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
        "nppdvjthqldpwncqszvftbrmjlhg": 6,
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11
    }

    for signal, answer in test_data.items():
        assert solution.part1(signal) == answer


def test_part2_sample():
    """
    Unit testing of Day 1, Part 2 sample input
    """

    test_data = {
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7): 19,
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5): 23,
        ("nppdvjthqldpwncqszvftbrmjlhg", 6): 23,
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10): 29,
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11): 26
    }

    for signal, answer in test_data.items():
        print(signal, answer)
        assert solution.part2(signal[0], signal[1]) == answer
