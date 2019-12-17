#!/usr/bin/env python3

import copy
from part1 import Reactions


class OutOfOre(Exception):
    pass


class Generate(Reactions):
    def __init__(self, reactions, ore):
        Reactions.__init__(self, reactions)
        self._chemicals['ORE'] = ore

    def consume(self, reagent, amount):
        """
        The original Reactions class assumed we could make as many
        intermediates and we were simply adding up how many ORE was needed.
        As such, the generate() method contained the logic of "do we have
        enough".

        In part 2, we need to actually consume ORE and not just tabulate
        how much is needed.  In order to reuse the existing Reaction.generate
        code, we need to duplicate some code here specifically for ORE
        """

        if reagent != 'ORE':
            # Make the intermediates
            self.generate(reagent, amount)
        else:
            # We have run out, raise Exception to abort FUEL production
            if self._chemicals['ORE'] < amount:
                raise OutOfOre

        # Consume chemicals
        self._chemicals[reagent] = self._chemicals[reagent] - amount
        return True


def process_file(filename, ore):
    with open(filename, 'r') as f:
        reactions = [x.rstrip() for x in f.readlines()]

    compounds = Generate(reactions, ore)

    # Because this could take a LONG time, let's be aggressive in searching
    # the space.  Take large jumps and save state in case we overshoot.

    i = 0
    increment = 10000
    previous_chemicals = copy.deepcopy(compounds._chemicals)

    while(True):
        try:
            # Process a large amount of ore
            compounds.consume('FUEL', increment)

            # We succeeded, rinse and repeat
            i = i + increment

            previous_chemicals = copy.deepcopy(compounds._chemicals)

        except OutOfOre:
            # If we ran out, but incremented by one, we found the answer
            if increment == 1:
                return i

            # Otherwise, reset, reduce the increment, and retry
            compounds._chemicals = copy.deepcopy(previous_chemicals)
            increment = increment // 2


def unit_tests(ore):
    if process_file('sample5.txt', ore) != 460664:
        print('Failed test 5')

    if process_file('sample4.txt', ore) != 5586022:
        print('Failed test 4')

    if process_file('sample3.txt', ore) != 82892753:
        print('Failed test 3')


if __name__ == '__main__':

    ore = 1000000000000
    unit_tests(ore)

    fuel = process_file('part1.txt', ore)

    print('FUEL produced with 1T ORE: {0}'.format(fuel))
