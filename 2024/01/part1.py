#!/usr/bin/env python3


def calculate_distance(left_list: list[int], right_list: list[int]) -> int:
    left: list[int] = sorted(left_list)
    right: list[int] = sorted(right_list)

    total_distance: int = 0
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])

    return total_distance


def read_input(filename: str) -> tuple[list[int], list[int]]:

    # Create the lists
    left_list: list[int] = list()
    right_list: list[int] = list()

    # Extract the two lists
    with open(filename, 'r') as f:
        # Each line has two numbers
        for line in f.readlines():
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))

    return left_list, right_list


def main(filename="../input.txt") -> int:
    left_list, right_list = read_input(filename)    
    total: int = calculate_distance(left_list, right_list)
    return total


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 1: {total}")
