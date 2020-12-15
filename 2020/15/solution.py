#!/usr/bin/env python3

import copy


def find_spoken(sample, target):
    """
    List is in reverse order to help with the indexing
    """

    # Loop len(sample) to target
    for idx in range(len(sample), target):
        if sample[0] not in sample[1:]:
            sample.insert(0, 0)
            continue
        last_idx = sample.index(sample[0], 1)
        sample.insert(0, last_idx)

        if not idx % 1000:
            print(idx, sample)

    return sample


def find_spoken_dict(sample, target):
    """
    Dictionary whose keys are the numbers spoken and the values would be the
    indexes of the times they are spoken.
    """

    idx = 0
    spoken = {}

    while(idx < len(sample)):
        item = sample[idx]
        if item not in spoken:
            spoken[item] = [idx]
        else:
            spoken[item].append(idx)
        idx += 1

    while(idx < target):
        # Is the only one the one I just inserted?
        if len(spoken[item]) == 1:
            item = 0
        else:
            item = spoken[item][-1] - spoken[item][-2]

        if item not in spoken:
            spoken[item] = [idx]
        else:
            spoken[item].append(idx)

        idx += 1
        if not idx % 100000:
            print(idx)

    return item


if __name__ == '__main__':

    sample_input = '0,3,6'
    sample = [int(x) for x in sample_input.split(',')]
    sample.reverse()

    sample_answer = find_spoken(sample, 2020)
    print('Sample: ' + str(sample_answer[0]))

    puzzle_input = '1,17,0,10,18,11,6'
    part1_input = [int(x) for x in puzzle_input.split(',')]
    part2_input = copy.copy(part1_input)

    part1_input.reverse()
    part1_answer = find_spoken(part1_input, 2020)
    print('Result: ' + str(part1_answer[0]))

    print('Part 2:')
    part2_answer = find_spoken_dict(part2_input, 30000000)
    print('Result: ' + str(part2_answer))
