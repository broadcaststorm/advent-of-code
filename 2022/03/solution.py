#!/usr/bin/env python3
"""
2022/03/solution.py: Python based solution for day 03 challenge, finding the
unique item in the two compartments as well as across three elves.
"""

from typing import List, Tuple


def calculate_priorities(duplicates: List[str]) -> List[int]:
    """
    calculate_priorites(duplicates) - take the list of items (single chars)
    and map them to priorities based on the guidance in the problem:
       a-z -> 1-26
       A-Z -> 27-52

    "Keys to the game": ord('A') = 65, ord('a') = 97
    """

    priorities = [
        ord(x)-64+26 if ord(x) < 97 else ord(x)-96
        for x in duplicates
    ]

    return priorities


def get_duplicates(backpack_contents: List[Tuple]) -> List[str]:
    """
    get_duplicates(backpack_contents): evaluate each pack and find the item
    (character) that is in both halves.  Assumption from the problem is that
    there is one and only one duplicate.
    """

    doppel = [
        (set(x) & set(y)).pop()
        for x, y in backpack_contents
    ]

    return doppel


def get_badges(backpack_contents: List[str]) -> List[str]:
    """
    get_badges(backpack_contents) - aggregate groups of 3 in backpack_contents
    to find the common item (single char) which identifies the badge for that
    group.  Return that list of badges.

    Badges list len will be 1/3 contents list.  Again, assumption
    from the problem is there's a single, unique character
    """

    offset = 0
    badges = list()

    while offset < len(backpack_contents):
        badges.append(
            (
                set(backpack_contents[offset]) &
                set(backpack_contents[offset+1]) &
                set(backpack_contents[offset+2])
            ).pop()
        )

        offset += 3

    return badges


def fetch_pack_contents(filename: str) -> List[str]:
    """
    fetch_pack_contents(filename) - read in the file and return a list of
    entries.  Here, we want the whole pack contents for a given elf in each
    entry. 
    """

    with open(file=filename, mode='r', encoding='UTF-8') as f_obj:
        contents = f_obj.read().split('\n')

    return contents


def fetch_pack_compartments(filename: str) -> List[Tuple]:
    """
    fetch_pack_compartments(filename) - read the file and return a list of tuples,
    each containing the full list of contents of the left half and right half
    of the pack.
    """

    # Initialize the return data structure
    packs = list()

    # Open the file and iterate through each line
    with open(file=filename, mode='r', encoding='UTF-8') as f_obj:

        for line in f_obj:

            # Line will have \n at the end, except perhaps the last line
            middle = (len(line) - 1) // 2 if len(line) % 2 else len(line) // 2

            # Use array/string splicing to create left/right halves and remove
            # the potential new line character for the right half
            packs.append((line[:middle], line[middle:].rstrip()))

    return packs


def part1(filename: str = 'input.txt'):
    """
    part1(filename): solve part 1 of day 3!
    """

    # Get the input data, return as a list of split items
    contents = fetch_pack_compartments(filename)

    # Extract duplicated item list
    duplicated_items = get_duplicates(contents)

    # Calculate priorities on the items
    priorities = calculate_priorities(duplicated_items)

    # Sum it all up and return the answer
    return sum(priorities)


def part2(filename: str = 'input.txt'):
    """
    part2(filename): solve part 2 of day 3!
    """

    # Need a new input data fetcher
    contents = fetch_pack_contents(filename)

    # Find badge identifier by groups of 3
    badges = get_badges(contents)

    # Map the badges to priorities
    priorities = calculate_priorities(badges)

    return sum(priorities)


if __name__ == '__main__':

    # Solve part1
    result = part1(filename='input-part1.txt')
    print(f'Result is {result}')

    # Solve part2
    output = part2(filename='input-part1.txt')
    print(f'Output is {output}')
