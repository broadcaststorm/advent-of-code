#!/usr/bin/env python3

import re


def read_input_data(input_file):
    rules = {}

    with open(input_file, 'r') as f:
        # Build regex engine for rule
        rule_pattern = r'^(?P<color>.*?) bags contain (?P<reqs>.*)\.$'
        rule_engine = re.compile(rule_pattern)

        bag_pattern = r'\s?(?P<qty>\d+) (?P<color>.*?) bag(s?)\s*'
        bag_engine = re.compile(bag_pattern)

        # Loop over entire file, matching each line
        for line in f.readlines():
            result = rule_engine.match(line)
            if not result:
                print('Failed: {}'.format(line))

            # Special case, no known dependencies
            color = result.group('color')
            reqs = result.group('reqs')
            if reqs == 'no other bags':
                rules[color] = None
                continue

            # Split on commas and extract out quantity and color entris
            rules[color] = {}
            for x in reqs.split(','):
                bag_result = bag_engine.match(x)
                if not bag_result:
                    print('Failed: {}'.format(x))
                    continue

                bag_color = bag_result.group('color')
                bag_number = int(bag_result.group('qty'))
                rules[color][bag_color] = bag_number

    return rules


def carries_bag(rules, target_color, my_color):
    if rules[my_color] is None:
        return False

    for k, v in rules[my_color].items():
        if k == target_color:
            return True

        if carries_bag(rules, target_color, k):
            return True

    return False


def find_carrying_bags(rules, color):
    """
    For the provided color, search the list of rules to determine which
    bags can ultimately carry it.  Return the list of bags.

    rules is a dictionary of the format:
      key = bag color
      value = dictionary of key/value pairs indicating:
              key = required color of bag held inside key's color
              value = required number of that color type
    """

    answers = []

    # Loop over the keys of my rules
    for outer_bag in rules.keys():
        if carries_bag(rules, color, outer_bag):
            answers.append(outer_bag)

    return answers


def count_carried_bags(rules, target_color):
    count = 0

    # Sanity check
    if target_color not in rules:
        print('Not in rules')
        return 0

    # As long as we have inner bags, start counting the inner ones
    if rules[target_color] is not None:

        # Loop over each type contained
        for inner_bag, inner_quantity in rules[target_color].items():

            # Recursive call to count all the internal bags for this instance
            inner_count = count_carried_bags(rules, inner_bag)

            # Multiply by the required quantity for this instance
            inner = inner_count * inner_quantity

            # Sum and proceed to next bag
            count = count + inner

    # Don't forget to count the bag holding all the inner bags
    count = count + 1
    return count


if __name__ == '__main__':

    print("Part 1 Solution:")
    sample_color = 'shiny gold'
    sample_rules = read_input_data('sample.txt')
    sample_bags = find_carrying_bags(sample_rules, sample_color)
    print('Sample: {0}'.format(len(sample_bags)))

    color = sample_color
    rules = read_input_data('input.txt')
    bags = find_carrying_bags(rules, color)
    print('Answer: {0}'.format(len(bags)))

    print("Part 2 Solution")
    # This answer includes counting the outermost bag because of the
    # recursive math. Need to subtract 1 to get the correct final answer
    count = count_carried_bags(rules, color)
    print('Answer: {0}'.format(count-1))
