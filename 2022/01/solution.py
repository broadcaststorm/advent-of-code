#!/usr/bin/env python3


from typing import List, Tuple


def count_calories(elves: List[str]) -> List[Tuple]:
    """
    count_calories(list of strs):  take the list of strings and generate
    calorie counts.

    Each string element maps to a specific elf.  Each elf's entry is a string
    containing one or more lines of numbers (string) that must be then be
    summed to get the total.
    """

    # Final counts for each elf
    counts = []

    # Loop over each elf's entry
    for i, elf in enumerate(elves):

        # Get all the calorie entries, convert to integer
        meals = [
            int(c) for c in elf.split('\n')
        ]

        # Sum them up and store them
        counts.append((sum(meals), i))

    return counts


def get_elf_data(filename: str) -> List[str]:
    """
    get_elf_data(filename) - open the input file, read the contents and break
    up the contents into elf by elf information
    """

    with open(file=filename, mode='r', encoding='UTF-8') as fobj:
        contents = fobj.read().strip()

    # Identify all the elves
    elves = contents.split('\n\n')

    return elves


def get_most_calories(calorie_entries: List[Tuple], num=1) -> List[Tuple]:
    """
    get_most_calories(calorie_entries, num): sort the provided calorie entries
    and return the top 'num' entries
    """

    # Sort the list by the calorie count entry in the tuple
    calorie_entries.sort(key=lambda cal: cal[0], reverse=True)

    return calorie_entries[:num]


def part1(filename: str) -> Tuple[int, int]:
    """
    part1(filename) - for a given filename, read the contents and pass the
    data structure to the main routines for computation.  Return the expected
    output for part1: calorie count and elf # for top elf.
    """

    # Get the Elf data
    elves = get_elf_data(filename)

    # Count calories for all the elves
    counts = count_calories(elves)

    # Return the elf identifier and the elf's calorie count
    return get_most_calories(counts, 1)[0]


def part2(filename: str) -> int:
    """
    part2(filename) - for a given filename, read the contents and pass the
    data structure to the main routines for computation.  Return the expected
    output for part2: total calories for top 3 elves.
    """

    # Get the Elf data
    elves = get_elf_data(filename)

    # Count calories for all the elves
    counts = count_calories(elves)

    # Return the elf identifier and the elf's calorie count
    elf_data = get_most_calories(counts, 3)

    # Sum the calories of the top 3 entries
    sum_calories = sum(
        [
            cals for cals, elf_id in elf_data
        ]
    )

    return sum_calories


if __name__ == '__main__':

    # Solve the part1 ask
    calories, elf_number = part1(filename = 'input-part1.txt')
    print(f"Elf number {elf_number} has {calories} calories")

    # Solve the part2 ask
    total_calories = part2(filename = 'input-part1.txt')
    print(f"Calories of the top 3 elves are {total_calories}")
