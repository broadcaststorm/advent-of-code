import pytest


from part1 import main as main1
from part2 import main as main2


def test_part1_sample(input_filename="sample1.txt", answer=3749):
    assert main1(input_filename) == answer

def test_part1_full(input_filename="puzzle-input.txt", answer=1708857123053):
    assert main1(input_filename) == answer

def test_part2_sample(input_filename="sample1.txt", answer=11387):
    assert main2(input_filename) == answer

def test_part2_full(input_filename="puzzle-input.txt", answer=189207836795655):
    assert main2(input_filename) == answer
