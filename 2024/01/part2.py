#!/usr/bin/env python3


def calculate_similarity(left_list: list[int], right_list: list[int]) -> int:
    """
    Similarity counts number of times entry in left appears in right (num), and
    then multiplies that by the value of entry in left.  We sum those products.
    """

    total_similarity: int = 0

    for left in left_list:
        count = right_list.count(left)
        total_similarity += left * count

    return total_similarity


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
    total: int = calculate_similarity(left_list, right_list)
    return total


if __name__ == '__main__':
    total = main()

    print(f"Answer for part 2: {total}")
