#!/usr/bin/env python3

import re
import math


class Reactions:
    def __init__(self, reactions):
        self._ore = 0
        self._chemicals = {}
        self._formulas = {}
        self.__process_reactions(reactions)

    def __process_reactions(self, reactions):
        """
        process_reactions - each line of the file has a list of reagents
        and the product of the reaction in the format:
            (Q N+), (Q N+), ... => (Q N+)

        Build a dictionary whose top level keys are the products and the
        values is a dictionary of reagents (keys) and amount (values)
        """

        # Build a simple regex to extra the amount and material
        unit = re.compile(r'(?P<qty>\d+) (?P<rgnt>[A-Z]+)')

        for r in reactions:
            # Split the line into ingredients and products
            ingredients, result = r.split(' => ')

            # Parse the product
            p = unit.match(result)
            if p is None:
                raise Exception('Null product {0}'.format(r))
            out = p.group('rgnt')
            qty = int(p.group('qty'))

            if out in ingredients:
                raise Exception('Result {0} in compound'.format(out))
            self._formulas[out] = {'qty': qty, 'reagents': {}}

            # Parse the ingredients
            for i in ingredients.split(', '):
                p = unit.match(i)
                if p is None:
                    raise Exception('Null ingredient {0}'.format(i))
                r = p.group('rgnt')
                self._formulas[out]['reagents'][r] = int(p.group('qty'))

    def consume(self, reagent, amount):
        if reagent == 'ORE':
            self._ore = self._ore + amount
            return

        # Make sure we have enough reagent
        self.generate(reagent, amount)

        # Consume chemicals
        self._chemicals[reagent] = self._chemicals[reagent] - amount
        return True

    def generate(self, reagent, amount):
        """
        Amount is how much we need.
        self._chemicals[reagent] is how much we have.

        Just need to generate enough to get amount.
        Will use fetch to get materials
        """

        # Ensure key is present
        if reagent not in self._chemicals:
            self._chemicals[reagent] = 0

        # If we have enough chemicals, simply return
        current = self._chemicals[reagent]
        if current >= amount:
            return

        # Should not be true
        if reagent not in self._formulas:
            raise Exception('{0} not in formulas'.format(reagent))

        produced = self._formulas[reagent]['qty']
        multiple = math.ceil((amount - current) / produced)

        for r in self._formulas[reagent]['reagents']:
            q = multiple * self._formulas[reagent]['reagents'][r]
            self.consume(r, q)

        self._chemicals[reagent] = self._chemicals[reagent] + produced*multiple
        return


def process_file(filename):
    with open(filename, 'r') as f:
        reactions = [x.rstrip() for x in f.readlines()]

    compounds = Reactions(reactions)
    compounds.consume('FUEL', 1)

    return compounds._ore


def unit_tests():
    # Tests basic formula substitutions
    if process_file('sample1.txt') != 31:
        print('Failed test 1')

    # Tests two stage substitions (but even multiples)
    if process_file('sample2.txt') != 165:
        print('Failed test 2')

    # Tests non-even multiples in any given formula (but even bases overall)
    if process_file('sample3.txt') != 13312:
        print('Failed test 3')

    # Tests non even multiples and uneven bases
    if process_file('sample4.txt') != 180697:
        print('Failed test 4')

    # Forces requirement of tracking inventory to have the absolute minumums
    if process_file('sample5.txt') != 2210736:
        print('Failed test 5')


if __name__ == '__main__':

    unit_tests()

    ore = process_file('part1.txt')

    print('ORE required for 1 FUEL is: {0}'.format(ore))
