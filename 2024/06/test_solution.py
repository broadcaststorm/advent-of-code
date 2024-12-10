import pytest


from part1 import main as main1
from part2 import main as main2


def test_part1_sample(input_filename="sample1.txt", answer=41):
    assert main1(input_filename) == answer

def test_part1_full(input_filename="puzzle-input.txt", answer=4374):
    assert main1(input_filename) == answer

def test_part2_sample(input_filename="sample1.txt", answer=6):
    assert main2(input_filename) == answer

def test_part2_full(input_filename="puzzle-input.txt", answer=1705):
    assert main2(input_filename) == answer
