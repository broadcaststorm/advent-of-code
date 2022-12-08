#!/usr/bin/env python3
"""
2022/05/test_solution.py: pyunit test file for solution
"""

import solution


# Unit test stack parsing
def test_stack_parsing():
    """
    Unit test stack parsing
    """

    input_str = "\n".join([
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 "
    ])

    stacks = solution.parse_stack_content(input_str)
    assert len(stacks.keys()) == 3
    assert set(stacks.keys()) == set(['1', '2', '3'])
    assert stacks['1'][-1] == 'N'
    assert stacks['2'][1] == 'C'
    assert stacks['3'][0] == 'P'


# Unit test instruction parsing
def test_instruction_parsing():
    """
    Unit test instruction parsing
    """

    input_str = "\n".join([
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ])

    instructions = solution.parse_instruction_content(input_str)
    assert len(instructions) == 4
    for i in instructions:
        assert len(i) == 3

    assert instructions[1][0] == 3
    assert instructions[1][1] == "1"
    assert instructions[2][2] == "1"


# Unit testing of the function against the sample data
def test_part1_sample(input_file_name="sample-part1.txt", result="CMZ"):
    """
    Unit testing of Day 1, Part 1 sample input
    """

    answer = solution.part1(filename=input_file_name)
    assert answer == result


def test_part2_sample(input_file_name="sample-part1.txt", result="MCD"):
    """
    Unit testing of Day 1, Part 2 sample input
    """

    answer = solution.part2(filename=input_file_name)
    assert answer == result
