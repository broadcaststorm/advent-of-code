#!/usr/bin/env python3
"""
2022/07/test_solution.py: pyunit test file for solution
"""

import solution


def test_tree_building():
    """
    test_tree_building() - using the sample input file, verify that we can
    read the file and create a directory structure out of it.
    """

    pstree: solution.DirTree = solution.process_input_file(filename='sample-part1.txt')

    pstree.top()
    entries = pstree.list()
    assert len(entries) == 4

    pstree.down('a')
    entries = pstree.list()
    assert len(entries) == 4

    pstree.down('e')
    entries = pstree.list()
    assert len(entries) == 1

    pstree.top()
    pstree.down('d')
    entries = pstree.list()
    assert "j" in entries
    assert "k" in entries

    storage = pstree.get_size('/')
    assert storage == 48381165

    storage = pstree.get_size('/d')
    assert storage == 24933642

    storage = pstree.get_size('/a')
    assert storage == 94853

    storage = pstree.get_size('/a/e')
    assert storage == 584


# Unit testing of the function against the sample data
def test_part1_sample(input_file_name="sample-part1.txt"):
    """
    Unit testing of Day 7, Part 1 sample input
    """

    answer = solution.part1(filename=input_file_name)
    assert answer == 95437


def test_part2_sample(input_file_name="sample-part1.txt", result=24933642):
    """
    Unit testing of Day 1, Part 2 sample input
    """

    answer = solution.part2(filename=input_file_name)
    assert answer == result
