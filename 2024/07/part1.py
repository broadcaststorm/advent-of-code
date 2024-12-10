#!/usr/bin/env python3


def calculation(values, ops) -> int:
    sum = values[0]

    for i in range(1, len(values)):
        if ops[i-1] == "0":
            sum += values[i]
        if ops[i-1] == "1":
            sum *= values[i]

    return sum


def check_operations(result: int, values: list[int]) -> list[str]:
    # How many values -> subtract 1 -> number of operations 
    num_ops = len(values) - 1

    for i in range(pow(2, num_ops)):
        binary_string = str(bin(i)[2:])
        binary_string = "0"*(num_ops-len(binary_string)) + binary_string
        if result == calculation(values, binary_string):
            return binary_string.split()

    return None


def find_good_operators(calibrations: dict) -> dict:
    # Key will be same as calibrations, value will be the operations
    good_operators = dict()

    for test_result in calibrations.keys():
        operations = check_operations(test_result, calibrations[test_result])
        if operations:
            good_operators[test_result] = operations

    return good_operators


def read_input(filename: str) -> dict:
    calibrations = dict()

    with open(filename, "r") as f:
        for line in f.readlines():
            result, values = line.strip().split(':')
            calibrations[int(result)] = [int(x) for x in values.split()]

    return calibrations


def main(filename: str = "puzzle-input.txt") -> int:
    calibrations = read_input(filename)
    valid_calibrations = find_good_operators(calibrations)
    total_sum = sum(valid_calibrations.keys())
    return total_sum


if __name__ == '__main__':
    total: int = main()

    print(f"Answer for part 1: {total}")
