#!/usr/bin/env python3

import re


def read_input_data(input_file):

    # Okay, I avoided regex on Day 04, so let's go for it today
    with open(input_file, 'r') as f:
        data = f.read()

    # Look for strings separated by two new line chars (e.g. blank line)
    pattern = r'(?P<group>.*?)\n\n'

    # re.S ensures that I find strings that include multiple lines of text
    # separated by two new lines
    engine = re.compile(pattern, re.S)

    entries = []

    # Iterate over the string and each pattern matched
    for i, entry in enumerate(engine.finditer(data)):
        entries.append(
            tuple(entry.group('group').split('\n'))
        )

    return entries


def get_uniques(entries):
    """
    Loop over the entries, examine each entry's tuple contents and count
    all the unique entries within each entry/group.
    """

    sums = []
    for entry in entries:
        # Take each tuple entry and concat into a single string.
        # Use set to split the joined string into unique list of questions
        uniq_q = set(''.join(entry))
        sums.append(len(uniq_q))

    return sums


def get_common(entries):
    """
    Loop over the entries, examine each entry's tuple contents and identify
    the common questions/characters across ALL entries.
    """

    sums = []
    for entry in entries:
        # This is a hack to seed the first match.
        common = set(entry[0])

        # Loop over all entries and perform intersection "and" operation
        for t in entry:
            common &= set(t)

        sums.append(len(common))

    return sums


if __name__ == '__main__':

    print('Part 1:')
    sample_entries = read_input_data('sample.txt')
    sample_sums = get_uniques(sample_entries)
    print('Sample: ' + str(sum(sample_sums)))

    entries = read_input_data('input.txt')
    prod_sums = get_uniques(entries)
    print('Results: ' + str(sum(prod_sums)))

    print('Part 2:')
    sample_common_sums = get_common(sample_entries)
    print('Sample: ' + str(sum(sample_common_sums)))

    common_sums = get_common(entries)
    print('Results: ' + str(sum(common_sums)))
