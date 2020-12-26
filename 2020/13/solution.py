#!/usr/bin/env python3

import copy


def read_input_data(input_file):
    with open(input_file, 'r') as f:
        arrival = int(f.readline().rstrip())
        bus_routes = f.readline().rstrip().split(',')

    return arrival, bus_routes


def find_earliest_bus(arrival, routes):
    """
    Essentially, I have to loop over the bus routes and find the "anti-mod"
    value - namely, instead of the remainder, I need the denom - mod value.
    """

    wait_times = [
        (int(r) - (arrival % int(r)), int(r))
        for r in routes
        if r != 'x'
    ]

    wait_times.sort()
    return wait_times[0]


def get_max_bus_id(buses):
    sorted_buses = copy.deepcopy(buses)
    sorted_buses.sort()

    max_id = sorted_buses[-1][0]
    max_offset = sorted_buses[-1][1]

    return max_id, max_offset


def is_linear(t0, buses):
    for id, idx in buses:
        if (t0+idx) % id != 0:
            return False
    return True


def find_earliest_time(routes):
    """
    So the cycle is going to be driven by the largest bus ID
    """

    buses = [
        (int(id), i) for i, id in enumerate(routes) if id != 'x'
    ]

    max_id, max_offset = get_max_bus_id(buses)
    t0 = max_id

    # We are going in multiples of max_id to find our linear set
    while(not is_linear(t0 - max_offset, buses)):
        if not t0 % 1000000:
            print(t0)
        t0 += max_id

    return t0


if __name__ == '__main__':

    print('Part 1')
    sarr, sbus = read_input_data('sample.txt')
    wait, bus = find_earliest_bus(sarr, sbus)
    print('Sample: ' + str(wait*bus))

    arr, routes = read_input_data('input.txt')
    wait, bus = find_earliest_bus(arr, routes)
    print('Results: ' + str(wait*bus))

    print('Part 2:')
    t0 = find_earliest_time(sbus)
    print('Sample: ' + str(t0))

    t0 = find_earliest_time([67, 7, 59, 61])
    print('Sample: ' + str(t0))

    t0 = find_earliest_time([67, 'x', 7, 59, 61])
    print('Sample: ' + str(t0))

    t0 = find_earliest_time([67, 7, 'x', 59, 61])
    print('Sample: ' + str(t0))

    t0 = find_earliest_time([1789, 37, 47, 1889])
    print('Sample: ' + str(t0))

    t0 = find_earliest_time(routes)
    print('Results: ' + str(t0))
