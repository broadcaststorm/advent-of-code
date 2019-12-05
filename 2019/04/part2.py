#!/usr/bin/env python3
"""
part2.py

So this one required a careful reading of the examples to get correct,
particularly the last example:
   "111122 meets the criteria (even though 1 is repeated more
    than twice, it still contains a double 22)."

The first example would lead you to believe that 111123 is perfectly
fine because it had two pairs.  But this last example clearly shows that
it's the double 22s that make the string viable.

So, a nested loop is required and searching only for a doublet.

"""

from part1 import has_increasing_digits


def only_two_digits(number):
    # Generate list
    num_list = list(number)

    # All other cases "brute force"
    i = 0
    while(i < 6):
        j = i + 1

        while(j < 6):
            if num_list[i] != num_list[j]:
                break
            j = j + 1

        # Find the delta (number of consecutive numbers)
        delta = j - i

        # If we found ONLY a pair of repeated values, we win
        if delta == 2:
            return True

        # Reset i for the next iteration
        i = j

    return False


def pass_test(number):
    if not has_increasing_digits(number):
        return False

    if not only_two_digits(number):
        return False

    return True


if __name__ == '__main__':

    if not pass_test('112233'):
        print("Fail test 1")

    if pass_test('123444'):
        print("Fail test 2")

    if not pass_test('111122'):
        print("Fail test 3")

    input_string = '197487-673251'
    input_list = input_string.split('-')

    start = int(input_list[0])
    end = int(input_list[1]) + 1

    possible = 0
    for i in range(start, end):
        if pass_test(str(i)):
            possible = possible + 1

    print('Total possible passwords: {0}'.format(possible))
