#!/usr/bin/env python3


#!/usr/bin/env python3


operation = [

]

def calculation(values, ops) -> int:
    sum = values[0]

    for i in range(1, len(values)):
        if ops[i-1] == "0":
            sum += values[i]
        if ops[i-1] == "1":
            sum *= values[i]
        if ops[i-1] == "2":
            sum = int(str(sum) + str(values[i]))

    return sum


def get_base3_string(idx: int, max: int) -> str:
    """
    Take the base 10 integer 'idx' and convert to a base3 number string
    and zero pad it to max
    """

    result = ''
    while idx > 0:
        result = str(idx % 3) + result
        idx //= 3

    result = "0"*(max-len(result)) + result
    return result 


def check_operations(result: int, values: list[int]) -> str:
    # How many values -> subtract 1 -> number of operations 
    num_ops = len(values) - 1

    for i in range(pow(3, num_ops)):
        ops_string = get_base3_string(i, num_ops)

        if result == calculation(values, ops_string):
            return ops_string

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

    print(f"Answer for part 2: {total}")
