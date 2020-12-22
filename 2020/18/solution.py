#!/usr/bin/env python3

import re


def read_input_data(input_file):
    with open(input_file, 'r') as f:
        ops = [x.rstrip() for x in f.readlines()]

    return ops


def compute_expression(sequence):
    """
    This method will take an unit expression and compute the quantity
    based on the established precedence rules (+ and * are equivalent,
    processed left to right).
    """

    elements = sequence.split(' ')

    while(len(elements) > 1):
        if len(elements) < 3:
            print('Length is 2???')
            break
        if elements[1] == '+':
            elements = [int(elements[0]) + int(elements[2])] + elements[3:]
        elif elements[1] == '*':
            elements = [int(elements[0]) * int(elements[2])] + elements[3:]
        else:
            raise Exception('Unknown op: {0}'.format(elements[2]))

    return elements[0]


def compute_add_before_multiply(sequence):
    """
    Part 2 order of operations - add happens before multiply.

    Again, assumption is the parenthesis have all been dealt with
    prior to the sequence string being sent.
    """

    elements = sequence.split(' ')

    # Loop over entire sequence finding '+' operations and reducing them
    try:
        add = elements.index('+')
        while(add):
            elements = elements[0:add-1] + [
                    int(elements[add-1]) + int(elements[add+1])
                ] + elements[add+2:]
            add = elements.index('+', add-1)
    except Exception:
        # At some point, we'll have no further addition
        pass

    # Remaining operations should only be multiply (retain error/sanity checks)
    while(len(elements) > 1):
        if len(elements) < 3:
            print('Length is 2???')
            break
        if elements[1] == '*':
            elements = [int(elements[0]) * int(elements[2])] + elements[3:]
        else:
            raise Exception('Unknown op: {0}'.format(elements[2]))

    return elements[0]


def process_ops(operations, compute=compute_expression):
    """
    This method has the hard job of extracting parentheses for correcting
    the order of operations.  The input is a list of each set of operations.

    For part 2: add second argument which is the method to use for computing
    the result based on the different order of operations.  Made changes to
    propagate the new method reference
    """

    paren_regex = r'\((?P<expr>(?:\d+? [\+\*] )+\d+?)\)'
    engine = re.compile(paren_regex)

    results = []
    for line in operations:

        # Reduce all the parenthetical operations
        match = engine.search(line)
        while(match):
            span = match.span()
            expr = match.group('expr')
            reduction = compute(expr)
            line = line[0:span[0]] + str(reduction) + line[span[1]:]
            match = engine.search(line)

        # Once we exit the parenthetical operations, the rest is equal
        results.append(compute(line))

    return results


if __name__ == '__main__':

    print('Part 1:')
    sample_ops = read_input_data('sample.txt')
    sample = process_ops(sample_ops)
    print('Sample: ' + str(sample))

    ops = read_input_data('input.txt')
    results = process_ops(ops)
    print('Results: ' + str(sum(results)))

    print('Part 2:')
    sample = process_ops(sample_ops, compute_add_before_multiply)
    print('Sample: ' + str(sample))

    part2 = process_ops(ops, compute_add_before_multiply)
    print('Results: ' + str(sum(part2)))
