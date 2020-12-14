#!/usr/bin/env python3
"""
This is a really strange puzzle setup.  From the example, I think the
idea is to expose the participant to the concept of histograms.

"""

import math


def read_input_data(input_file):
    with open(input_file, 'r') as f:
        joltage = [int(x.rstrip()) for x in f.readlines()]
        joltage.sort()

    return joltage


def get_differences(joltages, source=0, device=3):
    """
    Receive a sorted list (min to max) of adapter joltage ratings.

    Iterate through the list to find the distribution of differences
    between the source joltage and rated input.

    That rating is then used as the source joltage for the next adapter.

    Initial source joltage is 'source' argument.
    Device is the offset for the device's builtin adapter relative to the
    highest adapter.
    """

    # Use a dict for easy math and avoiding off by 1 issues
    bins = {
        1: 0,
        2: 0,
        3: 0
    }

    # (Not sure this will hold up) Add the end device +3 offset
    device_joltage = joltages[-1] + device
    joltages.append(device_joltage)

    for adapter in joltages:
        dj = adapter - source

        # Sanity checks
        if dj < 1:
            print('Too small {0} - {1}, {2}'.format(dj, source, adapter))
            continue
        if dj > 3:
            print('Too large {0} - {1}, {2}'.format(dj, source, adapter))
            continue

        bins[dj] = bins[dj] + 1
        source = adapter

    return device_joltage, bins


def get_optional(joltages):
    """
    Okay, the list I have it the maximum number of adapters when going end
    to end.  So I need to walk the list and count each iteration that include
    """

    # 0 = required, 1 = optional
    num_devices = len(joltages)
    last = num_devices - 1
    optional = [0] * num_devices

    # Walk the list and identify the number of optional adapters
    for idx, adapter in enumerate(joltages):
        # First device is the source
        if idx == 0:
            continue

        # Last device is required
        if idx == last:
            continue

        # If the delta to the next adapter is 3, I'm required
        if joltages[idx+1] - adapter == 3:
            optional[idx] = 0
            continue

        # If delta to the prev adapter is 3, I'm required
        if adapter - joltages[idx-1] == 3:
            optional[idx] = 0
            continue

        optional[idx] = 1

    return optional


def get_arrangements(joltages, source=0, device=3):
    """
    The idea is very simple: the combinatorics (if that's the correct math
    terminology... sorry, I'm old and an experimental physicist) are such
    that you can simply multiply the combinations of contiguous optional
    adapters.  So for example: [0, 1, 1, 0, 0, 1, 0, 0]
        The first element is source, the last element is the final device.
        The first two optional elements result in 4 possible combinations:
            - all present, one missing, other missing, both missing
        The 5th adapter being optional has 2 possible combinations:
            - present and not
    Multiplying the two independent options gives you a total of 8 possible
    combinations.

    The one caveat is 3-in-a-row. Because of the 1-3 range of the joltage in
    this problem, instead of 2**3 (8) combinations, one of the combinations
    is excluded (the all three removed cased) because, when two are removed,
    the third is no longer optional. Thus the special case below.
    """

    # Set up initial device
    joltages.insert(0, source)

    # Set up terminal end device
    device_joltage = joltages[-1] + device
    joltages.append(device_joltage)

    # Determine which adapters are permanently optional
    optional = get_optional(joltages)

    current = 1
    arrangements = 1
    end = len(optional)

    while(current < end):
        try:
            # Find the next index for an optional adapter
            next_opt = optional.index(1, current, end)
        except Exception:
            # Reached the end
            break

        # Find next required adapter
        next_req = optional.index(0, next_opt, end)

        # Concurrent number of optional adapters
        dapt = next_req - next_opt

        # Special cases
        if dapt > 3:
            raise Exception('Number of contiguous adapters > 3')

        if dapt == 3:
            arrangements = arrangements * 7
        else:
            arrangements = arrangements * math.pow(2, dapt)
        current = next_req + 1

    return int(arrangements)


if __name__ == '__main__':

    print('Part one')
    sample_joltage = read_input_data('sample.txt')
    device, bins = get_differences(sample_joltage)
    print('Sample: max {0}, bins {1}'.format(device, bins))

    sample2_joltage = read_input_data('sample2.txt')
    device, bins = get_differences(sample2_joltage)
    print('Sample: max {0}, bins {1}'.format(device, bins))

    joltage = read_input_data('input.txt')
    device, bins = get_differences(joltage)
    print('Outputs: max {0}, bins {1}'.format(device, bins))
    print('Results: {0}'.format(bins[1]*bins[3]))

    print('Part two')
    sample1 = get_arrangements(sample_joltage)
    print('Sample1: ' + str(sample1))
    sample2 = get_arrangements(sample2_joltage)
    print('Sample2: ' + str(sample2))
    final = get_arrangements(joltage)
    print('Results: ' + str(final))
