import pytest


from part1 import main as main1
from part2 import main as main2


def test_part1_sample(input_filename="sample1.txt", answer=18):
    assert main1(input_filename) == answer

def test_part1_full(input_filename="input.txt", answer=2390):
    assert main1(input_filename) == answer

def test_part2_sample(input_filename="sample1.txt", answer=9):
    assert main2(input_filename) == answer

def test_part2_full(input_filename="input.txt", answer=1809):
    assert main2(input_filename) == answer