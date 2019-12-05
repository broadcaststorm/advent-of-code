#!/usr/bin/env python3
"""
part1.py

For a given range of numbers (with 6 digits), count the number of numbers
that have a particular criteria for the numbers in the string
"""


def has_increasing_digits(number):
    """
    has_increasing_digits(number):  The idea is simple.  If the digits are
    in increasing order, if I convert the string to a list and sort it, the
    original and sorted lists will be the same.
    """

    # Make a list and sort it
    num_list = list(number)
    num_list.sort()

    # Rejoin into a string and compare to original
    sorted_number = ''.join(num_list)
    if sorted_number != number:
        return False

    return True


def has_adjacent_digits(number):
    """
    has_adjacent_digits(number) - loop over the 6 characters and compare them
    two at a time
    """

    for i in range(1, 6):
        if number[i-1] == number[i]:
            return True

    return False


def pass_test(number):
    """
    Number sent as a string to parse
    """

    if not has_increasing_digits(number):
        return False

    if not has_adjacent_digits(number):
        return False

    return True


if __name__ == '__main__':

    # Yes, I know.  I could've just done this manually.  But, now you see an
    # example of splitting a string by a character
    input_string = '197487-673251'
    input_list = input_string.split('-')

    # We add 1 to the end because of range() behavior
    start = int(input_list[0])
    end = int(input_list[1]) + 1

    possible = 0
    for i in range(start, end):
        if pass_test(str(i)):
            possible = possible + 1

    print('Total possible passwords: {0}'.format(possible))
