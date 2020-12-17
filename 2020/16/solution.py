#!/usr/bin/env python3

import re


def read_input_data(input_file):
    """
    This input file format is trash. LOL.

    valid_range dict format:
      - Key is the range description ('departure location')
      - Value is a list of all the valid numbers, fully expanded

    I need penance for other_tickets.
    """

    # Read the whole thing in one chunk
    with open(input_file, 'r') as f:
        whole_file = f.read()

    # Split into sections (valid ranges, my ticket, other tickets)
    sections = whole_file.split('\n\n')

    # Section 1: extract valid ranges
    regex = r'(?P<key>.*?): (?P<lmin>\d+)-(?P<lmax>\d+)'
    regex = regex + r' or (?P<umin>\d+)-(?P<umax>\d+)'
    pattern = re.compile(regex)

    valid_ranges = {
        x.group('key'):
            list(range(int(x.group('lmin')), int(x.group('lmax')) + 1)) +
            list(range(int(x.group('umin')), int(x.group('umax')) + 1))
        for x in pattern.finditer(sections[0])
    }

    # Section 2: my ticket
    my_ticket = [int(x) for x in sections[1].split('\n')[1].split(',')]

    # Section 3: Other tickets
    other_tickets = [
        [int(y) for y in x.split(',')]
        for x in sections[2].rstrip().split('\n')[1:]
    ]

    return valid_ranges, my_ticket, other_tickets


def find_any_invalid_values(valid_ranges, tickets):
    """
    The goal is to determine if a specifc value in a given ticket is not
    in any of the valid ranges.

    So, merge all the valid values into a set and do membership checks
    """

    all_valid_ranges = []
    for vals in valid_ranges.values():
        all_valid_ranges = all_valid_ranges + vals
    all_valid_ranges = set(all_valid_ranges)

    invalid_numbers = []
    for tkt in tickets:
        # Return values in set(tkt) that do not exist in all_valid_ranges
        bad = set(tkt) - all_valid_ranges
        if bad:
            invalid_numbers = invalid_numbers + list(bad)

    return invalid_numbers


def find_valid_tickets(valid_ranges, tickets):
    """
    Adapted the "part1" solution above (find_any_invalid_values) to return
    valid tickets instead of invalid values.
    """

    all_valid_ranges = []
    for vals in valid_ranges.values():
        all_valid_ranges = all_valid_ranges + vals
    all_valid_ranges = set(all_valid_ranges)

    valid_tickets = []
    for tkt in tickets:
        # Return values in set(tkt) that do not exist in all_valid_ranges
        bad = set(tkt) - all_valid_ranges
        if not bad:
            valid_tickets.append(tkt)

    return valid_tickets


def identify_fields(valid_ranges, valid_tickets):
    """
    There's definitely an inherent assumption based on the example in the
    challenge that there will be one position with only one possible
    field value, then a second position with 2, and so forth.

    The first half identifies all possible field values for a given
    position.  The second half sorts that data and extracts each field
    and its position
    """

    fields = []

    # Loop over each position in the ticket
    for i in range(len(valid_tickets[0])):
        # Loop over each ticket and get the values of the i-th position
        vals = [
            tkt[i] for tkt in valid_tickets
        ]

        vals = set(vals)
        candidates = []
        for field, ranges in valid_ranges.items():
            bad = vals - set(ranges)
            if not bad:
                candidates.append(field)

        fields.append((len(candidates), candidates, i))

    # Sort the results from fewest number of candidates to the most
    fields.sort()

    # Final result dictionary
    field_names = dict()

    for length, candidates, pos in fields:
        this_field = set(candidates) - set(field_names.keys())

        # Sanity check
        if len(this_field) != 1:
            raise Exception(str(this_field))

        field_names[list(this_field)[0]] = pos

    return field_names


def calculate_values(field_names, mine):
    """
    The final step of the part 2 challenge is finding the 6 fields with
    'departure' in the field name and multiplying the values together.
    Since I got in a 'list comprehension' pattern this day, I kept right
    on rolling rather than combine the two loops
    """

    positional_values = [
        mine[pos] for field, pos in field_names.items() if 'departure' in field
    ]

    product = 1
    for v in positional_values:
        product *= v

    return product


if __name__ == '__main__':

    print('Part 1:')
    valid_sample, my_sample, others_sample = read_input_data('sample.txt')
    bad_sample = find_any_invalid_values(valid_sample, others_sample)
    print('Sample: ' + str(sum(bad_sample)))

    valid, mine, others = read_input_data('input.txt')
    bad = find_any_invalid_values(valid, others)
    print('Result: ' + str(sum(bad)))

    print('Part 2:')
    valid_sample2, my_sample2, others_sample2 = read_input_data('sample2.txt')
    sample_good = find_valid_tickets(valid_sample2, others_sample2)
    sample_fields = identify_fields(valid_sample2, sample_good)
    print('Sample: ' + str(sample_fields))

    good = find_valid_tickets(valid, others)
    fields = identify_fields(valid, good)
    product = calculate_values(fields, mine)
    print('Result: ' + str(product))
