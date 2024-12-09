import pytest


from part1 import main as main1
from part2 import main as main2


def test_part1_sample(input_filename="sample1.txt", answer=161):
    assert main1(input_filename) == answer

def test_part1_full(input_filename="input.txt", answer=183669043):
    assert main1(input_filename) == answer

def test_part2_sample(input_filename="sample2.txt", answer=48):
    assert main2(input_filename) == answer

def test_part2_full(input_filename="input.txt", answer=59097164):
    assert main2(input_filename) == answer
