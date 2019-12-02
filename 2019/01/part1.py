#!/usr/bin/env python3
"""
Part 1: Determine fuel requirements for all modules.
"""


def module_fuel_required(mass=None):
    """
    module_fuel_required(mass): return the amount of fuel required
    for the provided mass value using the following math:
        mass / 3, round down, subtract 2

    For Python 3, the '//' (floor division) does the round down for
    us.
    """

    if type(mass) not in [int, float]:
        raise Exception('Mass must be an integer')

    return (mass // 3) - 2


if __name__ == '__main__':
    total_fuel = 0

    with open('part1.txt', 'r') as f:
        for l in f:
            mass = int(l)
            fuel = module_fuel_required(mass=mass)
            total_fuel = total_fuel + fuel

    print('Part 1: Total fuel is {0}'.format(total_fuel))
