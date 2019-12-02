#!/usr/bin/env python3
"""
Part 2:
    Determine fuel requirements for all modules.  This time,
    recursively account for the mass of the fuel as well.

    Rather than duplicate the code, I'm going to demo some
    code reusability in part2 with 'import'.
"""

from part1 import module_fuel_required

if __name__ == '__main__':
    total_fuel = 0

    with open('part1.txt', 'r') as f:
        for l in f:
            mass = int(l)
            while(mass > 0):
                fuel = module_fuel_required(mass=mass)
                if (fuel < 0):
                    break
                total_fuel = total_fuel + fuel
                mass = fuel

    print('Part 2: Total fuel is {0}'.format(total_fuel))
