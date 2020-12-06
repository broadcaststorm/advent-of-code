#!/usr/bin/env python3
"""
Note: subtracting sets in the find_missing_seat() method below is only
a valid approach is you already know the lists are unique.  Otherwise,
conversion of a list to a set removes duplicates and produces unexpected
results.

In our case, we know the seat IDs are unique already so are fine with this
approach.
"""


def parse_passes(passes):
    seat_ids = {}

    for line in passes:
        row = int('0b' + line[0:7].replace('F', '0').replace('B', '1'), 2)
        col = int('0b' + line[7:10].replace('L', '0').replace('R', '1'), 2)
        id = row * 8 + col

        seat_ids[(row, col)] = id

    return seat_ids


def get_highest_seat(seat_ids):
    # Extract the values of the dictionary (we don't care about row, col index)
    ids = list(seat_ids.values())

    # sort() is in-place so has to be called separately.
    ids.sort()
    print(ids)

    # sort() defaults to increasing order, so return the last item (max)
    return(ids[-1])


def find_missing_seat(seat_ids):
    # Get the ID values from the dictionary and sort them
    ids = list(seat_ids.values())
    ids.sort()

    # Generate a range of seat IDs from ids[0] to ids[-1], inclusive
    all_ids = list(range(ids[0], ids[-1]+1))

    # Find the elements missing by subtracting pass seat IDs from complete list
    missing_ids = set(all_ids) - set(ids)

    # This results approach assumes that there could be more than one
    results = []
    for id in missing_ids:
        # The seat before mine is not in the boarding passes
        if id - 1 not in ids:
            continue

        # The seat after mine is not in the boarding passes
        if id + 1 not in ids:
            continue

        # Seat before and seat after this ('id') missing pass exists
        results.append(id)

    return results


def read_input_data(input_file):

    with open(input_file, 'r') as f:
        passes = [x.rstrip() for x in f.readlines()]

    return passes


if __name__ == '__main__':

    print('Part 1 results')
    passes = read_input_data('sample.txt')
    sample_seat_ids = parse_passes(passes)
    max_id = get_highest_seat(sample_seat_ids)
    print('Sample: ' + str(max_id))

    passes = read_input_data('input.txt')
    prod_seat_ids = parse_passes(passes)
    max_id = get_highest_seat(prod_seat_ids)
    print('Result: ' + str(max_id))

    print('Part 2 results')
    missing_id = find_missing_seat(prod_seat_ids)
    if len(missing_id) > 1:
        print('Found too many!')
        print(missing_id)

    print('Result: ' + str(missing_id[0]))
