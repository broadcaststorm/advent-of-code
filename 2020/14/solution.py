#!/usr/bin/env python3

import re
import math
import copy


def read_input_data(input_file):

    mem_regex = r'mem\[(?P<addr>\d+?)\] = (?P<value>\d+)'
    pattern = re.compile(mem_regex)

    input_data = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            # Mask operations
            if line[0:4] == 'mask':
                input_data.append(
                    ('mask', line[7:].rstrip())
                )

            # Memory assignment operation
            if line[0:3] == 'mem':
                results = pattern.match(line)
                if not results:
                    raise Exception(line)

                addr = int(results.group('addr'))
                value = int(results.group('value'))

                input_data.append(('mem', addr, value))

    return input_data


def calculate_masked_value(mask, decimal):
    # Convert decimal to zero padded binary string
    binary = f'{decimal:036b}'

    # Loop over the two string and do the binary math
    result = map(
        lambda m, b: b if m == 'X' else m,
        mask, binary
    )

    bit_string_result = ''.join(result)
    return int(bit_string_result, 2)


def assign_memory(input_data):
    """
    Part 1 solution - mask modifies the data to be stored.
    """
    current_mask = 'X'*36
    memory = {}

    for entry in input_data:
        # Change the mask
        if entry[0] == 'mask':
            current_mask = entry[1]
            continue

        # Calculate new memory value and set it to the location
        result = calculate_masked_value(current_mask, entry[2])
        memory[entry[1]] = result

    return memory


def calculate_masked_addresses(mask, decimal):
    """
    New rules for part2:
      - Overwrite value with '1' if mask == '1'
      - Persist existing value if mask == '0'
      - Create entries for both '0' and '1' if mask == 'X'

    Since I need to create all combinations of X values, I'll need
    something more detailed than the map() from before. So a simple
    loop with more steps is required.
    """

    # Convert decimal to zero padded binary string
    binary = f'{decimal:036b}'

    # Loop over the two string and do the binary math for 0,1, identify X
    result = []
    var_index = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            var_index.append(i)
            result.append('X')
            continue
        if mask[i] == '1':
            result.append('1')
            continue
        result.append(binary[i])

    # len(var_index) indicates the number of variable bits for which I have
    # to account.
    bits = len(var_index)
    num_vars = int(math.pow(2, bits))
    locations = []

    for n in range(num_vars):
        # I want to use my iteration counter to determine the values for 'X'

        # Zero pad my iteration number converted to binary, truncated to the
        # size of var_index
        var_mapping = f'{n:036b}'[-bits:]

        # That var_mapping now has '0' or '1' foreach idx position in var_index

        # Loop over var_index to find the index in result to replace with the
        # bit value in var_mapping
        next_variation = copy.copy(result)
        for idx, result_idx in enumerate(var_index):
            next_variation[result_idx] = var_mapping[idx]

        # Take the string bit array, concat it, and convert to integer
        locations.append(
            int(''.join(next_variation), 2)
        )

    return locations


def assign_address(input_data):
    """
    Part 2 solution - mask modified the ADDRESS where the data is stored.
    """
    current_mask = 'X'*36
    memory = {}

    for entry in input_data:
        # Change the mask
        if entry[0] == 'mask':
            current_mask = entry[1]
            continue

        # Calculate address location and assign value to it
        results = calculate_masked_addresses(current_mask, entry[1])
        for r in results:
            memory[r] = entry[2]

    return memory


if __name__ == '__main__':

    print('Part 1:')
    sample_data = read_input_data('sample.txt')
    sample_memory = assign_memory(sample_data)
    print(
        'Sample:',
        sum(sample_memory.values())
    )

    data = read_input_data('input.txt')
    memory = assign_memory(data)
    print(
        'Results:',
        sum(memory.values())
    )

    print('Part 2:')
    sample_data = read_input_data('sample2.txt')
    sample_memory = assign_address(sample_data)
    print(
        'Sample:',
        sum(sample_memory.values())
    )

    addresses = assign_address(data)
    print(
        'Results:',
        sum(addresses.values())
    )
