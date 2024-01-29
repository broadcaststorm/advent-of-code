#!/usr/bin/env python3
"""
2022/template/solution.py: Python based solution in template folder
"""


import re
from typing import List

import typer


app = typer.Typer()
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def extract_digits(data: str) -> int:
    """
    Given the calibration data, use a regex to extract the numerical digits.
    The various digits in the string will be concatenated and converted to
    an integer to return.
    """

    # Returns a list of all matches as string
    results: List[str] = re.findall(r"\d+", data)

    # Join the first and last digits into a string
    value = f"{results[0][0]}{results[-1][-1]}"

    # Convert to int, and return
    return int(value)


def fetch_data(filename) -> List[int]:
    """
    Given an input file name, extract the relevant data from the file
    """

    row_data = list()

    # Open a file
    with open(filename, "r") as input_file:
        # Extract each line
        for line in input_file:
            row_data.append(line.strip())

    return row_data


@app.command()
def part1(filename: str = 'input.txt'):
    # Solve part1

    calibration_strings = fetch_data(filename)
    calibrated_values = list()

    for cal_data in calibration_strings:
        calibrated_values.append(extract_digits(cal_data))

    result = sum(calibrated_values)

    print(f'Part 1 results are {result}')
    return result


@app.command()
def part2(filename: str = 'input.txt'):
    # Solve part2

    calibration_strings = fetch_data(filename)
    calibrated_values = list()

    for cal_data in calibration_strings:
        for num, val in numbers.items():
            if num in cal_data:
                cal_data = cal_data.replace(num, val)
        calibrated_values.append(extract_digits(cal_data))

    output = sum(calibrated_values)

    print(f'Part 2 output is {output}')
    return output


if __name__ == '__main__':
    app()
