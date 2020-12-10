#!/usr/bin/env python3

def read_input_data(input_file):
    with open(input_file, 'r') as f:
        return [
            int(x.rstrip()) for x in f.readlines()
        ]


def find_invalid(data, preamble=25):
    """
    Invalid entry is a number that doesn't equal the sum of two
    unique entries in the previous 'preamble' number of entries
    """

    # Starting after the preamble, loop over list of data
    for idx in range(preamble, len(data)):
        test_val = data[idx]

        found = False

        # Loop over the preamble
        for n in range(idx-preamble, idx):
            current_val = data[n]
            check_val = test_val - current_val

            if check_val in data[n+1:idx]:
                found = True
                break

        if not found:
            return test_val

    return None


def find_weakness(data, invalid):
    """
    Environmentalists everywhere are demanding my cancellation for the
    excessive brute force effort laid out here.
    """

    num_data = len(data)
    for b in range(0, num_data-2):
        for e in range(2, num_data-2-b):
            test_range = data[b:e]
            if sum(test_range) == invalid:
                return test_range

    return None


if __name__ == '__main__':

    print("Part 1")
    sample_data = read_input_data('sample.txt')
    sample_invalid = find_invalid(sample_data, 5)
    print('Sample: {0}'.format(sample_invalid))

    data = read_input_data('input.txt')
    invalid = find_invalid(data)
    print('Results: {0}'.format(invalid))

    print("Part 2")
    sample_weakness = find_weakness(sample_data, sample_invalid)
    sample_weakness.sort()
    print('Sample {0}'.format(sample_weakness[0] + sample_weakness[-1]))

    weakness = find_weakness(data, invalid)
    weakness.sort()
    print('Results {0}'.format(weakness[0] + weakness[-1]))
