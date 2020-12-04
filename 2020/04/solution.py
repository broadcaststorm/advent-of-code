#!/usr/bin/env python3

import copy
import re

valid_fields = [
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'
]


def parse_entry(entry):
    kvPairs = entry.split(' ')

    data = {}
    for pair in kvPairs:
        k, v = pair.split(':')
        data[k] = v

    return data


def read_input_data(input_file):
    """
    Read in all the lines, parse into a data structure, return it.
    'Blank line delimited entries'.
    """

    with open(input_file, 'r') as f:
        # We've got to read the entire file given that entries are
        # whitespace or newline delimited

        data = f.read()

    # Now, split the big string along a \n\n delimiter
    entries = data.split('\n\n')

    # Normalize the "white space" by replacing \n with ' 'characters
    results = [x.replace('\n', ' ').rstrip() for x in entries]

    return results


def validate(passport, required_fields):
    attrs = list(passport.keys())

    for field in required_fields:
        if field not in attrs:
            return False

    return True


def part_one(entries, exclude='cid'):
    required_fields = copy.copy(valid_fields)
    required_fields.remove(exclude)

    valid_passports = []
    for entry in entries:
        passport = parse_entry(entry)
        if validate(passport, required_fields):
            valid_passports.append(passport)

    return valid_passports


def validate_data(passport):
    """
    If we get here, it's got all the required attributes
    """

    # byr check
    byr = passport['byr']
    try:
        ibyr = int(byr)
        if ibyr < 1920 or ibyr > 2002:
            return False
    except Exception:
        return False

    # iyr check
    iyr = passport['iyr']
    try:
        iiyr = int(iyr)
        if iiyr < 2010 or iiyr > 2020:
            return False
    except Exception:
        return False

    # eyr check
    eyr = passport['eyr']
    try:
        ieyr = int(eyr)
        if ieyr < 2010 or ieyr > 2030:
            return False
    except Exception:
        return False

    # hgt check
    hgt = passport['hgt']
    if hgt[-2:] == 'cm':
        ihgt = int(hgt[:-2])
        if ihgt < 150 or ihgt > 193:
            return False
    elif hgt[-2:] == 'in':
        ihgt = int(hgt[:-2])
        if ihgt < 59 or ihgt > 76:
            return False
    else:
        return False

    # hcl check
    hcl = passport['hcl']
    if len(hcl) != 7:
        return False
    if hcl[0] != '#':
        return False
    if not re.match(r'[a-z0-9]{6,6}', hcl[1:]):
        print('failed regex')
        return False

    # ecl check
    valid_eye = [
        'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    ]

    if passport['ecl'] not in valid_eye:
        return False

    # pid check
    pid = passport['pid']
    if len(pid) != 9:
        return False

    try:
        # is it all numbers?
        int(pid)
    except Exception:
        return False

    # They all pass!
    return True


def part_two(entries, exclude='cid'):
    required_fields = copy.copy(valid_fields)
    required_fields.remove(exclude)

    valid_passports = []
    for entry in entries:
        passport = parse_entry(entry)

        # Re-use existing work
        if not validate(passport, required_fields):
            continue

        if validate_data(passport):
            valid_passports.append(passport)

    return valid_passports


if __name__ == '__main__':

    print('Part 1 Sample')
    entries = read_input_data('sample.txt')
    passports = part_one(entries)
    print(len(passports))

    print('Part 1 Full Data')
    entries = read_input_data('input.txt')
    passports = part_one(entries)
    print(len(passports))

    print('Part 2 Valid Sample')
    entries = read_input_data('valid.txt')
    passports = part_two(entries)
    print(len(passports))

    print('Part 2 Invalid Sample')
    entries = read_input_data('invalid.txt')
    passports = part_two(entries)
    print(len(passports))

    print('Part 2 Full Data')
    entries = read_input_data('input.txt')
    passports = part_two(entries)
    print(len(passports))
